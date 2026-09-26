init -1 python:
    class QuestController:
    
        @staticmethod
        def get_quest_pool():
            quest_pool = []
            all_story_lines_progressions = player.get_storylines_progress()
            for quest_line_name in all_story_lines_progressions:
                current_status = sm_quest_lines_list[quest_line_name][QUEST_LINE][all_story_lines_progressions[quest_line_name]]
                current_status = QuestController.check_storyline_item_for_sub_line(quest_line_name, current_status)
                if current_status not in [PAUSE, WAITING] and current_status.startswith("Q"):
                    quest_pool.append(current_status)
            return quest_pool
    
        @staticmethod
        def get_schedule_overrides(codename, schedule_type, action_data = {}):
            quest_pool = QuestController.get_quest_pool()
            schedules = []
            for quest_name in quest_pool:
                offramp = QuestController.get_offramp(quest_name)
                if offramp:
                    if schedule_type in sm_quest_list[quest_name][OFFRAMP][offramp] and codename in sm_quest_list[quest_name][OFFRAMP][offramp][schedule_type]:
                        schedules.append(sm_quest_list[quest_name][OFFRAMP][offramp][schedule_type][codename])
                elif schedule_type in sm_quest_list[quest_name] and codename in sm_quest_list[quest_name][schedule_type]:
                    is_schedule_applied = False
                    if SCHEDULE_CONDITION in sm_quest_list[quest_name]:
                        event_function_name = sm_quest_list[quest_name][SCHEDULE_CONDITION]
                        event_function = globals().get(event_function_name)
                        result = event_function(action_data)
                        if result != False:
                            is_schedule_applied = True
                    else:
                        is_schedule_applied = True
                    if is_schedule_applied:
                        schedules.append(sm_quest_list[quest_name][schedule_type][codename])
            return schedules
    
        @staticmethod
        def get_offramp(quest):
            if quest not in sm_quest_list:
                return False
            quest_data = sm_quest_list[quest]
            if OFFRAMP not in quest_data:
                return False
            for player_choice_variable, offramp_data in quest_data[OFFRAMP].items():
                if player.get_choice(player_choice_variable):
                    return player_choice_variable
            return False
    
        @staticmethod
        def get_quest_schedule_overrides_for_character(character_codename):
            return QuestController.get_schedule_overrides(character_codename, SCHEDULE)
    
        @staticmethod
        def get_quest_schedule_overrides_for_objects(object_codename):
            return QuestController.get_schedule_overrides(object_codename, OBJ_SCHEDULE)
    
        @staticmethod
        def get_quest_schedule_overrides_for_locations(location_codename, location):
            schedules = QuestController.get_schedule_overrides(location_codename, LOC_SCHEDULE)
            quest_pool = QuestController.get_quest_pool()
            for quest_name in quest_pool:
                if WHOLE_LOCATION_SCHEDULE in sm_quest_list[quest_name] and location in sm_quest_list[quest_name][WHOLE_LOCATION_SCHEDULE]:
                    schedules.append(sm_quest_list[quest_name][WHOLE_LOCATION_SCHEDULE][location])
            return schedules
    
        @staticmethod
        def activate_quest(quest_name):
            quest = sm_quest_list[quest_name]
            if RP_LIMIT in quest:
                for character_codename, limit in quest[RP_LIMIT].items():
                    CharacterController.get_character(character_codename).update_points_limit(limit)
            if DAYS_PASSED in quest:
                days_passed = quest[DAYS_PASSED]
                QuestController.days_passed_check(days_passed, quest_name)
    
        @staticmethod
        def resolve_quest(quest_name):
            quest_pool = QuestController.get_quest_pool()
            if quest_name not in quest_pool:
                if config.developer is True:
                    print_verbose(f"Can't resolve \"{quest_name}\" because it isn't in QuestPool")
                    player.log_action(f"Can't resolve '{quest_name}' because it isn't in QuestPool")
                return
            quest = sm_quest_list[quest_name]
            if STORY_LINE in quest:
                story_line_name = quest[STORY_LINE]
                player.progress_storyline(story_line_name)
                ChatController.add_chat_from_quest()
                ChatController.get_waiting_chats()
                StoryController.activate_story_line(story_line_name, True)
                EventController.action(QUEST_RESOLVED, quest_name)
    
        @staticmethod
        def start_day_quests_resolve():
            quests = QuestController.get_quest_pool()
            for quest_name in quests:
                if DAYS_PASSED in sm_quest_list[quest_name]:
                    days_passed = sm_quest_list[quest_name][DAYS_PASSED]
                    QuestController.days_passed_check(days_passed, quest_name)
    
        @staticmethod
        def days_passed_check(days_passed, quest_name):
            if QuestController.get_offramp(quest_name):
            
                return
            if isinstance(days_passed, list):
                if all(player.completion_log_compare_date_for_item(item[TARGET], item[DAYS]) for item in days_passed):
                    QuestController.resolve_quest(quest_name)
            else:
                if player.completion_log_compare_date_for_item(days_passed[TARGET], days_passed[DAYS]):
                    QuestController.resolve_quest(quest_name)
    
        @staticmethod
        def check_storyline_item_for_sub_line(storyline_name, item):
            if isinstance(item, list):
                return item[player.get_story_subline(storyline_name)]
            return item
    
        @staticmethod
        def get_current_quest(storyline_name):
            progress = player.get_storyline(storyline_name)
            story_line_quest_list = sm_quest_lines_list[storyline_name][QUEST_LINE]
            if progress > len(story_line_quest_list) - 1:
                return ""
            return QuestController.check_storyline_item_for_sub_line(storyline_name, story_line_quest_list[progress])
    
        @staticmethod
        def get_active_quest_hint():
            story_line_names = player.get_tracked_storylines()
            hint_dict = {}
            for story_line_name in story_line_names:
                progress = player.get_storyline(story_line_name)
                quest_name = QuestController.get_current_quest(story_line_name)
                if quest_name == "":
                    return {}
                hint = QuestController.get_hint(quest_name)
                if hint is not None:
                    hint_dict[story_line_name] = hint
            return hint_dict
    
        @staticmethod
        def get_hint(quest_name, is_default_hint = False, action_data = {}):
            hint = ""
            if quest_name.startswith("Q") or quest_name == WAITING:
                quest_info = sm_quest_list.get(quest_name, {})
                if DAYS_PASSED in quest_info:
                    message = ""
                    if type(quest_info[DAYS_PASSED]) != list:
                        quest_info[DAYS_PASSED] = [quest_info[DAYS_PASSED]]
                    for item in quest_info[DAYS_PASSED]:
                        if player.completion_log_get_date(item[TARGET]) == False:
                            if message:
                                message += "and "
                            message += _("You need to progress {storyline_name} ").format(storyline_name=QuestController.get_storyline_name_by_quest(item[TARGET]))
                    if message:
                        return message
                hint = QuestController.process_smart_hint(quest_info.get("HINT", ""), is_default_hint)
            return hint
    
        @staticmethod
        def process_smart_hint(hint, is_default_hint = False, action_data = {}):
            if isinstance(hint, tuple):
                if is_default_hint:
                    return hint[1][0]
                hint_function = globals().get(hint[0])
                hint_function_result = hint_function(action_data)
                if isinstance(hint_function_result, tuple):
                    return hint[1][hint_function_result[0]].format(hint_function_result[1])
                return hint[1][hint_function_result]
        
            elif isinstance(hint, dict):
            
                last_hint = ""
                if is_default_hint and DEFAULT in hint:
                    return hint[DEFAULT]
                for func, hint_string in hint.items():
                    if func == DEFAULT: 
                        return hint_string
                    event_function = globals().get(func)
                    if event_function:
                        val = event_function(action_data)
                        if val is True:
                            return hint_string
                        if val is False:
                            continue
                        if isinstance(val, list):
                            return hint_string.format(*val)
                        return hint_string.format(val)
                    last_hint = hint_string
                return last_hint
            return hint
    
        @staticmethod
        def get_quests_for_menu():
            quests_dict = {}
            available_storyline = player.get_storylines_progress()
            for storyline, progress in available_storyline.items():
                quest_name = QuestController.get_current_quest(storyline)
                if quest_name:
                    quest_data = [] if quest_name.startswith("s") else sm_quest_list.get(quest_name, {})
                    if quest_name != "pause" and quest_name != "end" and HIDDEN not in quest_data and QuestController.get_offramp(quest_name) == False:
                        quests_dict[storyline] = progress
        
            sorted_quests = dict(sorted(quests_dict.items(), key=lambda item: sm_quest_list.get(QuestController.get_current_quest(item[0]), {}).get(CURRENT_QUEST_LINE_END, False) is True))
            return sorted_quests
    
        @staticmethod
        def get_char_from_quest(quest_line):
            return sm_quest_lines_list[quest_line][CONNECTED_CHARACTER]
    
        @staticmethod
        def get_current_quest_hint(storyline, progress):
            quest_name = QuestController.get_current_quest(storyline)
            if quest_name.startswith("s"):
                return _("You are currently watching the scene")
            else:
                return QuestController.get_hint(quest_name)
    
        @staticmethod
        def get_quest_old_hints(storyline, progress):
            quest_hints_list = []
            story_line_quest_list = sm_quest_lines_list[storyline][QUEST_LINE]
            for quest in story_line_quest_list[:progress]:
                quest = QuestController.check_storyline_item_for_sub_line(storyline, quest)
                quest_data = [] if quest.startswith("s") else sm_quest_list[quest]
                if quest != "pause" and quest != "end" and not quest.startswith("s") and HIDDEN not in quest_data:
                    quest_hints_list.append(QuestController.get_hint(quest, True))
            quest_hints_list.reverse()
            return quest_hints_list
    
        @staticmethod
        def get_storyline_name_by_quest(item):
            for storyline, storyline_data in sm_quest_lines_list.items():
                if item in storyline_data[QUEST_LINE]:
                    return storyline_data[NAME]
            return ""
    
        @staticmethod
        def quest_action(quest_action, end_of_quest_line = False):
            if quest_action.startswith("Q"):
                if not end_of_quest_line:
                    player.log_action(f"Activated Next Quest '{quest_action}'")
                QuestController.activate_quest(quest_action)
                is_silent_quest = sm_quest_list[quest_action].get(SILENT_QUEST, False)
                if not end_of_quest_line and not vn_mode and not is_silent_quest:
                    renpy.show_screen("new_quest_animation")
                    renpy.play(audio.sfx_ui_quest_appear, channel = "sound9")
            else:
                return False
    
        @staticmethod
        def is_quest_line_end(storyline):
            progress = player.get_storyline(storyline)
            quest_name = QuestController.get_current_quest(storyline)
            if quest_name:
                quest_info = sm_quest_list.get(quest_name, {})
                hint = quest_info.get(CURRENT_QUEST_LINE_END, False)
                return hint
            return False
    
        @staticmethod
        def get_attribute_from_quest_pool(attribute, subattribute = False):
            quest_pool = QuestController.get_quest_pool()
            for quest_name in quest_pool:
                quest = sm_quest_list[quest_name]
                if attribute in quest:
                    if subattribute is False:
                        return quest[attribute]
                    if subattribute in quest[attribute]:
                        return quest[attribute][subattribute]
            return False
    
        @staticmethod
        def get_map_location_hint_from_quest_pool(location):
            quest_pool = QuestController.get_quest_pool()
            for quest_name in quest_pool:
                quest = sm_quest_list[quest_name]
                if MAP_HINT in quest:
                    for map_location, hint in quest[MAP_HINT].items():
                        if map_location == location.location:
                            return QuestController.process_smart_hint(hint)
            return False
    
        @staticmethod
        def add_interactions_override(entity, interactions_options, interaction_type, interaction_option_class):
            quest_pool = QuestController.get_quest_pool()
            for quest_name in quest_pool:
                quest = sm_quest_list[quest_name]
                offramp = QuestController.get_offramp(quest_name)
                if offramp and interaction_type in quest[OFFRAMP][offramp]:
                
                    interactions_options += QuestController.filter_interactions(entity, quest[OFFRAMP][offramp][interaction_type].items(), interaction_option_class)
                elif interaction_type in quest:
                    interactions_options += QuestController.filter_interactions(entity, quest[interaction_type].items(), interaction_option_class)
            return interactions_options
    
        @staticmethod
        def filter_interactions(entity, items, interaction_option_class):
            interactions_options = []
            for codename, override_io in items:
                if codename != entity.codename:
                    continue
                if isinstance(override_io, list):
                    for override_io_codename in override_io:
                        interactions_options.append(interaction_option_class.init_interaction_option(override_io_codename, entity))
                else:
                    interactions_options.append(interaction_option_class.init_interaction_option(override_io, entity))
            return interactions_options
    
        @staticmethod
        def add_character_interactions_override(character, interactions_options):
            return QuestController.add_interactions_override(character, interactions_options, CHAR_INTR, InteractionCharacterOption)
    
        @staticmethod
        def add_object_interactions_override(object, interactions_options):
            return QuestController.add_interactions_override(object, interactions_options, OBJ_INTR, InteractionObjectOption)
    
        @staticmethod
        def add_location_interactions_override(location, interactions_options):
            return QuestController.add_interactions_override(location, interactions_options, LOC_INTR, InteractionLocationOption)
