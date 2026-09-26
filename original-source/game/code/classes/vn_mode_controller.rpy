init -1 python:
    class VNModeController:
    
        @staticmethod
        def get_next_scene(storyline_name):
            progress = player.get_storylines_progress()[storyline_name]
            quest_line = sm_quest_lines_list[storyline_name][QUEST_LINE]
            for item in quest_line[progress:]:
                if isinstance(item, list):
                    next_sub_line_item = QuestController.check_storyline_item_for_sub_line(storyline_name, item)
                    if next_sub_line_item.startswith("sm1"):
                        return next_sub_line_item
                    else:
                        start_index = item.index(next_sub_line_item)
                        for sub_item in item[start_index:]:
                            if sub_item.startswith("sm1"):
                                return sub_item
                        continue
                if item.startswith("sm1"):
                    return item
                elif CHAT in sm_quest_list[item]:
                    if VN_SKIP not in VN_MODE_DATA[item]:
                        return item
            return None
    
        @staticmethod
        def validate_vn_data_conditions(conditions):
            if isinstance(conditions, set):
                return all(player.has_played_scene(scene) for scene in conditions)
            if isinstance(conditions, list):
                return all(player.is_storyline_item_finished(item[0], item[1]) for item in conditions)
            elif isinstance(conditions, tuple):
                return any(player.is_storyline_item_finished(item[0], item[1]) for item in conditions)
            return False
    
        @staticmethod
        def get_next_chat_data(next_quest_with_chat):
            if CHAT in sm_quest_list[next_quest_with_chat]:
                return sm_quest_list[next_quest_with_chat][CHAT]
            return None
    
        @staticmethod
        def is_next_scene_visible(storyline_name, scene_without_storyline=False):
            if scene_without_storyline:
                if VNModeController.validate_vn_data_conditions(VN_MODE_DATA[storyline_name][SHOW_AFTER]):
                    if HIDE_AFTER in VN_MODE_DATA[storyline_name]:
                        if VNModeController.validate_vn_data_conditions(VN_MODE_DATA[storyline_name][HIDE_AFTER]):
                            return False
                    scene_name = storyline_name if ALT_NAME not in VN_MODE_DATA[storyline_name] else VN_MODE_DATA[storyline_name][ALT_NAME]
                    return not player.has_played_scene(scene_name)
                return False
        
            progress = player.get_storylines_progress()[storyline_name]
            quest_item = sm_quest_lines_list[storyline_name][QUEST_LINE][progress]
            quest = QuestController.check_storyline_item_for_sub_line(storyline_name, quest_item)
            if quest in [PAUSE, WAITING, END] or QuestController.get_offramp(quest):
                return False
        
            next_scene = VNModeController.get_next_scene(storyline_name)
            if not next_scene:
                return False
            next_scene_data = VN_MODE_DATA[next_scene]
            if VN_HIDE in next_scene_data:
                return VNModeController.validate_vn_data_conditions(next_scene_data[VN_HIDE])
            return True
    
        @staticmethod
        def is_next_scene_available(storyline_name, scene_without_storyline=False):
            if scene_without_storyline:
                if VN_BLOCK in VN_MODE_DATA[storyline_name[NAME]]:
                    if not VNModeController.validate_vn_data_conditions(VN_MODE_DATA[storyline_name[NAME]][VN_BLOCK]):
                        return False
                return True
        
            progress = player.get_storylines_progress()[storyline_name]
            quest_item = sm_quest_lines_list[storyline_name][QUEST_LINE][progress]
            quest = QuestController.check_storyline_item_for_sub_line(storyline_name, quest_item)
            if quest in [PAUSE, WAITING, END] or QuestController.get_offramp(quest):
                return False
        
            next_scene = VNModeController.get_next_scene(storyline_name)
            if not next_scene:
                return False
            next_scene_data = VN_MODE_DATA[next_scene]
            if VN_BLOCK in next_scene_data:
                return VNModeController.validate_vn_data_conditions(next_scene_data[VN_BLOCK])
            return True
    
        @staticmethod
        def resolve_quest_for_scene(storyline_name, quest_name):
            quest = QuestController.check_storyline_item_for_sub_line(storyline_name, quest_name)
            if VNModeController.is_quest_resolvable(quest):
                VNModeController.trigger_quest_unlocks(quest)
                QuestController.resolve_quest(quest)
    
        @staticmethod
        def auto_resolve_quests(storyline_name):
            progress = player.get_storylines_progress()[storyline_name]
            quest_line = sm_quest_lines_list[storyline_name][QUEST_LINE]
            for i in range(progress, len(quest_line)):
                quest_name = QuestController.check_storyline_item_for_sub_line(storyline_name, quest_line[i])
                if VNModeController.is_quest_resolvable(quest_name):
                    if VNModeController.get_next_quest(storyline_name, i):
                        VNModeController.trigger_quest_unlocks(quest_name)
                        QuestController.resolve_quest(quest_name)
                    else:
                        break
                else:
                    break
    
        @staticmethod
        def is_quest_resolvable(quest_name):
            if OFFRAMP in sm_quest_list[quest_name] and QuestController.get_offramp(quest_name):
                return False
            if CHAT in sm_quest_list[quest_name] and VN_SKIP not in VN_MODE_DATA[quest_name]:
                return False
            return quest_name not in [PAUSE, WAITING, END]
    
        @staticmethod
        def get_next_quest(storyline_name, progress):
            quest_line = sm_quest_lines_list[storyline_name][QUEST_LINE]
            if progress < len(quest_line) - 1:
                next_quest = QuestController.check_storyline_item_for_sub_line(storyline_name, quest_line[progress + 1])
                if next_quest.startswith("Q"):
                    return next_quest
            return None
    
        @staticmethod
        def auto_progress_all_quests():
            for storyline_name in player.get_storylines_progress():
                VNModeController.auto_resolve_quests(storyline_name)
    
        @staticmethod
        def trigger_quest_unlocks(quest_name):
            if quest_name.startswith("Q"):
                quest_data = sm_quest_list[quest_name]
                if EVENT in quest_data:
                    unlock_function = quest_data[EVENT] + "_unlocks"
                    if unlock_function in globals() and callable(globals()[unlock_function]):
                        print_verbose(f"Calling \"{unlock_function}\" function for \"{quest_name}\"")
                        globals()[unlock_function]()
    
        @staticmethod
        def get_next_scene_name(storyline_name, scene_without_storyline=False):
            if scene_without_storyline:
                return VN_MODE_DATA[storyline_name[NAME]][NAME]
            next_scene = VNModeController.get_next_scene(storyline_name)
            if not next_scene:
                return None
            if NAME in VN_MODE_DATA[next_scene] and VN_MODE_DATA[next_scene][NAME]:
                return VN_MODE_DATA[next_scene][NAME]
            if HINT in VN_MODE_DATA[next_scene] and VN_MODE_DATA[next_scene][HINT]:
                return VN_MODE_DATA[next_scene][HINT]
            progress = player.get_storylines_progress()[storyline_name]
            quest_item = sm_quest_lines_list[storyline_name][QUEST_LINE][progress]
            quest = QuestController.check_storyline_item_for_sub_line(storyline_name, quest_item)
            quest_hint = sm_quest_list[quest].get(HINT)
            if isinstance(quest_hint, str):
                return quest_hint
            return next_scene
    
        @staticmethod
        def get_next_scene_hint(storyline_name, scene_without_storyline):
            if scene_without_storyline:
                if HINT in VN_MODE_DATA[storyline_name]:
                    return VN_MODE_DATA[storyline_name][HINT]
                if VN_BLOCK in VN_MODE_DATA[storyline_name]:
                    return VNModeController.get_hint_from_vn_block(VN_MODE_DATA[storyline_name])
        
            next_scene = VNModeController.get_next_scene(storyline_name)
            if not next_scene:
                return None
            if HINT in VN_MODE_DATA[next_scene] and VN_MODE_DATA[next_scene][HINT]:
                return VN_MODE_DATA[next_scene][HINT]
            if VN_BLOCK in VN_MODE_DATA[next_scene]:
                return VNModeController.get_hint_from_vn_block(VN_MODE_DATA[next_scene])
            return next_scene
    
        @staticmethod
        def get_hint_from_vn_block(scene_data):
            if len(scene_data[VN_BLOCK]) == 1:
                scene_name = scene_data[VN_BLOCK][0][1]
                return _("Progress {storyline_name}").format(storyline_name=QuestController.get_storyline_name_by_quest(scene_name))
    
        @staticmethod
        def get_scene_transition_text(storyline_name, scene_without_storyline, is_offramp_scene=False):
            if is_offramp_scene:
                scene_transistion_data =  VN_MODE_DATA[quest_name].get(TRANSITION_TEXT, None)
                return scene_transistion_data
            next_scene = storyline_name[NAME] if scene_without_storyline else VNModeController.get_next_scene(storyline_name)
            return VN_MODE_DATA[next_scene].get(TRANSITION_TEXT, None)
    
        @staticmethod
        def set_location_data(scene_name):
            global curr_location, curr_sublocation, curr_position, curr_vn_time
            location_data = VN_MODE_DATA.get(scene_name)
            if location_data:
                curr_location = location_data[LOCATION]
                curr_sublocation = location_data[SUBLOCATION]
                curr_position = location_data[POSITION]
                curr_vn_time = location_data.get(SCENE_TIME, T5)
    
        @staticmethod
        def get_scene_location(scene_name):
            return VN_MODE_DATA.get(scene_name, {}).get(LOCATION, STUDIO)
    
        @staticmethod
        def get_storylines_in_location(location):
            story_progress_list = player.get_storylines_progress()
            storylines_in_location = []
            for story in story_progress_list:
                next_scene = VNModeController.get_next_scene(story)
                if next_scene and VN_MODE_DATA[next_scene][LOCATION] == location:
                    if VNModeController.is_next_scene_visible(story):
                        storylines_in_location.append(story)
        
            for scene in SCENES_WITHOUT_STORYLINE:
                if VN_MODE_DATA[scene][LOCATION] == location:
                    if VNModeController.is_next_scene_visible(scene, True):
                        storylines_in_location.append({NAME: scene, STORYLINE: VN_MODE_DATA[scene][STORYLINE]})
        
            return storylines_in_location
    
        @staticmethod
        def get_offramp_quests():
            quest_pool = QuestController.get_quest_pool()
            offramp_quests = []
            for quest_name in quest_pool:
                if QuestController.get_offramp(quest_name):
                    offramp_quests.append(quest_name)
            return offramp_quests
    
        @staticmethod
        def get_offramp_interaction(quest_name):
            vn_quest_data =  VN_MODE_DATA[quest_name]
            offramp_key = vn_quest_data[OFFRAMP][QuestController.get_offramp(quest_name)]
            return INTERACTIONS_CHARACTER_CATALOGUE[offramp_key]
    
        @staticmethod
        def get_offramp_option_name(quest_name):
            vn_quest_data =  VN_MODE_DATA[quest_name]
            if NAME in vn_quest_data:
                return vn_quest_data[NAME]
            interaction = VNModeController.get_offramp_interaction(quest_name)
            interaction_name = interaction[NAME]
            return interaction_name
    
        @staticmethod
        def get_offramp_label(quest_name):
            vn_quest_data =  VN_MODE_DATA[quest_name]
            interaction = VNModeController.get_offramp_interaction(quest_name)
            return interaction[TARGET]
    
        @staticmethod
        def get_offramp_character(quest_name):
            storyline_name = sm_quest_list[quest_name].get(STORY_LINE)
            return QuestController.get_char_from_quest(storyline_name)
