init -1 python:
    class StoryController:
    
        @staticmethod
        def activate_story_line(story_line_name, make_it_active = False):
            StoryController.unpause_story_line(story_line_name)
            progress = player.get_storyline(story_line_name)
            if isinstance(progress, bool) and progress is False:
                player.create_storyline(story_line_name)
                progress = 0
        
            current_action = QuestController.get_current_quest(story_line_name)
            if current_action:
                if current_action.startswith("Q"):
                    end_of_quest_line = False
                    if CURRENT_QUEST_LINE_END in sm_quest_list[current_action]:
                        player.log_action(f"Untracked '{story_line_name}' because of 'CURRENT_QUEST_LINE_END'")
                        player.untrack_storyline(story_line_name, True)
                        end_of_quest_line = True
                    elif AUTO_UNTRACK in sm_quest_list[current_action]:
                        player.log_action(f"Untracked '{story_line_name}' because of 'AUTO_UNTRACK'")
                        player.untrack_storyline(story_line_name, True)
                    elif make_it_active:
                        player.log_action(f"Tracked '{story_line_name}' because of 'make_it_active'")
                        player.track_storyline(story_line_name)
                    QuestController.quest_action(current_action, end_of_quest_line)
                else:
                    if current_action in [PAUSE, WAITING, END]:
                        player.log_action(f"Untracked '{story_line_name}' because of 'PAUSE/WAITING/END'")
                        player.untrack_storyline(story_line_name, True)
                        return
                    player.log_action(f"Started next scene/interaction '{current_action}'")
                    setattr(renpy.store, "scene_start_day", (gt.get_day_number(), gt._dt))
                    player.completion_log_add_item_date(current_action)
                    renpy.hide_screen("phone")
                    renpy.call(current_action)
    
        @staticmethod
        def get_story_line_list(story_line_name):
            if story_line_name in sm_quest_lines_list:
                return sm_quest_lines_list[story_line_name][QUEST_LINE]
            return False
    
        @staticmethod
        def progress_story_after_scene(story_line_name):
            player.progress_storyline(story_line_name)
            progress = player.get_storyline(story_line_name)
            current_action = QuestController.get_current_quest(story_line_name)
            ChatController.add_chat_from_quest()
            ChatController.get_waiting_chats()
            if current_action and current_action in [PAUSE, WAITING, END]:
                player.untrack_storyline(story_line_name)
                return
            if QuestController.get_offramp(current_action):
                player.untrack_storyline(story_line_name)
                return
            StoryController.activate_story_line(story_line_name, True)
    
        @staticmethod
        def end_scene(story_line_name, hours = 0, minutes = 0, energy = 0, location = False, sublocation = False, position = False, start_new_week = True):
            StoryController.progress_story_after_scene(story_line_name)
            if vn_mode:
                return
            StoryController.consume_time_energy(hours, minutes, energy)
            if start_new_week:
                StoryController.after_scene_new_week()
            if location:
                StoryController.end_call_and_jump_to_location(location, sublocation, position)
    
        @staticmethod
        def end_scene_in_time(story_line_name, hour, minutes, energy = 0, location = False, sublocation = False, position = False, start_new_week = True):
            StoryController.progress_story_after_scene(story_line_name)
            if vn_mode:
                return
            if (hour < gt.curr_hour):
                StoryController.consume_time_energy(24 - gt.curr_hour + hour, minutes, energy)
            else:
                gt.update(hour, minutes, 0)
                player.consume_energy(energy)
            if start_new_week:
                StoryController.after_scene_new_week()
            if location:
                StoryController.end_call_and_jump_to_location(location, sublocation, position)
    
        @staticmethod
        def end_scene_without_progressing(story_line_name, hours = 0, minutes = 0, energy = 0):
            player.log_action(f"Ended scene in storyline '{story_line_name}' without progressing storyline")
            player.progress_storyline(story_line_name, -1)
            StoryController.activate_story_line(story_line_name, True)
            if vn_mode:
                return
            StoryController.consume_time_energy(hours, minutes, energy)
    
        def end_call_and_jump_to_location(location, sublocation, position):
            renpy.pop_call()
            player.log_action(f"Jumped to location '{location}_{sublocation}_{position}' after scene end")
            renpy.jump(location + "_" + sublocation + "_" + position)
    
        @staticmethod
        def end_repeatable_scene(scene_name, hours = 0, minutes = 0, energy = 0, location = False, sublocation = False, position = False):
            player.completion_log_add_item_date(scene_name)
            player.increment_data(scene_name)
            if vn_mode:
                return
            StoryController.consume_time_energy(hours, minutes, energy)
            player.log_action(f"Ended repeatable scene '{scene_name}'")
            if location:
                StoryController.end_call_and_jump_to_location(location, sublocation, position)
    
        @staticmethod
        def end_scene_without_storyline(scene_name=None, hours = 0, minutes = 0, energy = 0, location = False, sublocation = False, position = False):
            if scene_name:
                player.completion_log_add_item_date(scene_name)
            if vn_mode:
                return
            StoryController.consume_time_energy(hours, minutes, energy)
            if location:
                global curr_location, curr_sublocation, curr_position
                curr_location = STUDIO
                curr_sublocation = DEFAULT_SUBLOCATION
                curr_position = SD_OVERVIEW
    
        @staticmethod
        def after_scene_new_week():
            if not renpy.store.scene_start_day:
                return
            if gt.get_day_number() == renpy.store.scene_start_day[0]:
                return
            days_took = gt.get_day_number() - renpy.store.scene_start_day[0] + 1
            if days_took:
                if gt.range_includes_sunday(renpy.store.scene_start_day[1], days_took):
                    renpy.call("after_sleep_in_scene", True, True)
    
        @staticmethod
        def advance_storyline_by_interaction_option(story_line_name):
            progress = player.get_storyline(story_line_name)
            curr_quest_line_item = QuestController.get_current_quest(story_line_name)
            if curr_quest_line_item and curr_quest_line_item.startswith("Q"):
                QuestController.resolve_quest(curr_quest_line_item)
                player.progress_storyline(story_line_name)
                StoryController.activate_story_line(story_line_name)
    
        @staticmethod
        def unpause_story_line(story_line_name):
            progress = player.get_storyline(story_line_name)
            next_action = QuestController.get_current_quest(story_line_name)
            if next_action and next_action in [PAUSE, WAITING]:
                player.progress_storyline(story_line_name)
    
        @staticmethod
        def track_unfinished_quests():
            all_story_lines = player.get_storylines_progress()
            count = len(player.get_tracked_storylines())
            for story_line_name, progress in all_story_lines.items():
                current_action = QuestController.get_current_quest(story_line_name)
                if current_action and current_action.startswith("Q"):
                    quest_data = sm_quest_list[current_action]
                    if CURRENT_QUEST_LINE_END not in quest_data and HIDDEN not in quest_data:
                        if OFFRAMP not in quest_data or QuestController.get_offramp(current_action) == False:
                            player.track_storyline(story_line_name)
                            count += 1
                            if count >= 3:
                                return
    
        @staticmethod
        def consume_time_energy(hours, minutes, energy):
            gt.add(hours, minutes, 0)
            player.consume_energy(energy)
    
        @staticmethod
        def location_reenter_sanity_check():
            progress_list = player.get_storylines_progress()
            for story_line_name, progress in progress_list.items():
                current_action_list = StoryController.get_story_line_list(story_line_name)
                if not current_action_list:
                    continue
            
                current_action = current_action_list[progress]
                current_action = QuestController.check_storyline_item_for_sub_line(story_line_name, current_action)
                if current_action.startswith("Q"):
                    continue
                elif current_action in [PAUSE, WAITING, END]:
                    continue
                else:
                    player.log_action(f"Sanity check jump to action '{current_action}' for storyline '{story_line_name}'")
                    renpy.jump(current_action)
    
        @staticmethod
        def is_storyline_started(story_line_name):
            return bool(player.get_storyline(story_line_name))
    
        @staticmethod
        def is_all_storylines_finished():
            for storyline_name, progress in player.get_storylines_progress().items():
                if storyline_name in [MORE_FACTIONS, RD_STORY]:
                    continue
                if progress + 1 < len(sm_quest_lines_list[storyline_name][QUEST_LINE]):
                    return False
            return True
