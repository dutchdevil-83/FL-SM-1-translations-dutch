init -1 python:
    class CharacterController:
    
        @staticmethod
        def click(char):
            player.log_action(f"Clicked on character '{char.codename}'")
            result = EventController.action(CHARACTER_CLICK, char.codename)
            if result:
                return
            interaction_options = []
            global interaction_character
            if char.is_busy(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                interaction_character = char
                player.log_action(f"Entered busy interaction for character '{interaction_character.codename}'")
                renpy.jump("busy_interaction")
            if char.is_angry_peek(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                interaction_character = char
                player.log_action(f"Entered angry peek interaction for character '{interaction_character.codename}'")
                renpy.jump("angry_peek_interaction")
            if char.is_watch_pee(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position): 
                interaction_character = char
                interaction_options = CharacterController.update_interaction_options(char)
                player.log_action(f"Entered watch pee interaction for character '{interaction_character.codename}'")
                renpy.jump("studio_watch_pee")
            interaction_options = CharacterController.update_interaction_options(char)
            if interaction_options is False:
                return
            result = EventController.action(CHARACTER_TALK, char.codename)
            if result:
                return
            interaction_character = char
            player.log_action(f"Entered interaction menu for character '{interaction_character.codename}'")
            renpy.jump("interaction_menu")
    
        @staticmethod
        def get_character(codename):
            return sm_indexed_character_list[codename] if codename in sm_indexed_character_list else False
    
        @staticmethod
        def update_interaction_options(char):
            global interaction_options
            interaction_options = []
            if not char.has_schedule():
                return False
            interaction_options = char.get_interaction_options(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
            interaction_options = QuestController.add_character_interactions_override(char, interaction_options)
            return interaction_options
    
        @staticmethod
        def get_characters_for_sandbox():
            result = []
            for char in sm_characters_list:
                if char.has_schedule() and char.get_schedule_in_location(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                    result.append(char)
            return result
    
        @staticmethod
        def get_characters_for_map(location):
            result = []
            for char in sm_characters_list:
                if char.is_essential is True and char.has_schedule() and char.get_is_unlocked():
                    if char.get_character_in_location(gt.curr_timeslot if location == curr_location else gt.timeslot_after_travel, gt.curr_day, location):
                        result.append(char)
            return result
    
        @staticmethod
        def get_characters_for_side_menu(location, sublocation, position):
            result = []
            for char in sm_characters_list:
                if char.is_essential is True and char.has_schedule() and char.get_is_unlocked():
                    if char.get_character_in_position(gt.curr_timeslot, gt.curr_day, location, sublocation, position):
                        result.append(char)
            return result
    
        @staticmethod
        def get_characters_for_phone_chat():
            results = []
            for char in sm_characters_list:
                if char.is_essential is True and char.get_is_unlocked() and char.chat_available:
                    results.append(char)
            sorted_results = sorted(results, key=lambda character: CharacterController.sort_phone_chat_characters(character))
            return sorted_results
    
        @staticmethod
        def sort_phone_chat_characters(character):
            if character.get_unread_chat():
                return (0, character.name)
            elif character.get_chat_history():
                return (1, character.name)
            else:
                return (2, character.name)
    
        @staticmethod
        def get_expression_image(character, expression):
            dress_code = DressCodeController.get_dress_code(character, gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
            dress_code_suffix = f"#{dress_code}" if dress_code else ""
            curr_disply_time_short = curr_vn_time if vn_mode else gt.curr_display_time_short
        
            possible_file_names = [
                    f"{curr_location}_{curr_sublocation}_{curr_disply_time_short}_inter_{character}_{expression}{dress_code_suffix}_{curr_position}",
                    f"{curr_location}_{curr_sublocation}_td_inter_{character}_{expression}{dress_code_suffix}_{curr_position}",
                    f"{curr_location}_{curr_sublocation}_{curr_disply_time_short}_inter_{character}_{expression}{dress_code_suffix}_default",
                    f"{curr_location}_{curr_sublocation}_td_inter_{character}_{expression}{dress_code_suffix}_default",
                    ]
        
            for img_name in possible_file_names:
                if renpy.has_image(img_name):
                    return img_name
            return possible_file_names[-1]
    
        @staticmethod
        def get_default_busy_sound(character):
            audio = f"audio/freeroam/voiceovers/default_{character}_busy.ogg"
            return audio
