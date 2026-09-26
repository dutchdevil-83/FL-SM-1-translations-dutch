init -1 python:
    class ChatController:
    
        @staticmethod
        def add_chat_from_quest():
            quest_pool = QuestController.get_quest_pool()
            for quest_name in quest_pool:
                if CHAT in sm_quest_list[quest_name]:
                    for character, chat_name in sm_quest_list[quest_name][CHAT].items():
                        chat_queue = CharacterController.get_character(character).get_chat_queue()
                        if not any(chat[CHAT] == chat_name for chat in chat_queue):
                            CharacterController.get_character(character).add_chat_to_queue(chat_name)
    
        @staticmethod
        def get_waiting_chats():
            for character in sm_indexed_character_list.values():
                active_chat = character.get_active_chat()
                if active_chat:
                    chat_catalogue = ChatController.get_chat_catalogue(active_chat[CHAT])
                    next_chat_index = character.get_active_chat_index() + 1
                    if TIMESLOTS in chat_catalogue[next_chat_index] and gt.curr_timeslot in chat_catalogue[next_chat_index][TIMESLOTS] and chat_catalogue[next_chat_index][SENDER] != YOU:
                        ChatController.progress_active_chat(character)
                        ChatController.send_chat_notification(character, active_chat)
                
                    iteration_count = 0
                    while ChatController.is_next_message_from_recipient(character) and ChatController.get_next_available_message_info(character) and not vn_mode:
                        iteration_count += 1
                        ChatController.progress_active_chat(character)
                        if iteration_count == 1:
                            ChatController.send_chat_notification(character, active_chat)
    
        @staticmethod
        def send_chat_notification(character, active_chat):
            screen_uuid = active_chat[UUID]
            message_recieved = ChatController.get_chat_history(character)[-1]
            message_content = ChatController.get_message_content(message_recieved, message_recieved[SENDER])
            Show("notification_screen", msg_type=MESSAGE, message=f"{character.name} : {message_content}", target=character.codename, tag=screen_uuid, _tag=screen_uuid)()
    
        @staticmethod
        def get_chat_catalogue(chat):
            return CHARACTER_CHAT_CATALOGUE[chat]
    
        @staticmethod
        def validate_chat_conditions(chat_message, uuid):
            conditions = chat_message.get(CONDITIONS)
            if not conditions:
                return True
            for condition in conditions:
                if condition[TYPE] == PERSISTENT:
                    if persistent.__getattribute__(condition[VARIABLE]) != condition[VALUE]:
                        return False
                elif condition[TYPE] == PLAYER_CHOICE:
                    if player.get_choice(condition[VARIABLE]) != condition[VALUE]:
                        return False
                elif condition[TYPE] == CHAT_CHOICE:
                    if player.get_choice(f"{chat[CHAT]}_{uuid}_{condition[VARIABLE]}") != condition[VALUE]:
                        return False
                elif condition[TYPE] == PLAYED_SCENE:
                    if player.is_storyline_item_finished(condition[VARIABLE], condition[VALUE]) == False:
                        return False
                elif condition[TYPE] == NOT_PLAYED_SCENE:
                    if player.is_storyline_item_finished(condition[VARIABLE], condition[VALUE]) == True:
                        return False
            return True
    
        @staticmethod
        def append_message(message_history, sender, msg_type, content):
            message_history.append({SENDER: sender, TYPE: msg_type, CONTENT: content})
    
        @staticmethod
        def get_chat_history(character):
            message_history = []
            chat_history = character.get_chat_history()
        
            for chat in chat_history:
                for message in ChatController.get_chat_catalogue(chat[CHAT]):
                    if ChatController.validate_chat_conditions(message, chat[UUID]):
                        ChatController.process_message(message_history, message, chat)
        
            active_chat = character.get_active_chat()
            active_chat_index = character.get_active_chat_index()
            if active_chat and active_chat_index >= 0:
                chat_catalogue = ChatController.get_chat_catalogue(active_chat[CHAT])
                for message in chat_catalogue[:active_chat_index + 1]:
                    if ChatController.validate_chat_conditions(message, active_chat[UUID]):
                        ChatController.process_message(message_history, message, active_chat)
            return message_history
    
        @staticmethod
        def process_message(message_history, message, chat):
            if message.get(TYPE) != CHOICE:
                ChatController.append_message(message_history, message[SENDER], message[TYPE], message[CONTENT])
            else:
                choices = message.get(CHOICES)
                for choice in choices:
                    if all(player.get_choice(f"{chat[CHAT]}_{chat[UUID]}_{variable}") == value for variable, value in choice[VARIABLES].items()):
                        ChatController.append_message(message_history, message[SENDER], MESSAGE, choice[CONTENT])
    
        @staticmethod
        def get_next_available_message_info(character):
            active_chat = character.get_active_chat()
            if not active_chat:
                return {}
        
            active_chat_index = character.get_active_chat_index()
            next_message_index = active_chat_index + 1
            chat_catalogue = ChatController.get_chat_catalogue(active_chat[CHAT])
            active_chat_uuid = active_chat[UUID]
        
            for index, chat_message in enumerate(chat_catalogue[next_message_index:]):
                actual_index = index + next_message_index
                if not ChatController.validate_chat_conditions(chat_message, active_chat_uuid):
                    continue
                if vn_mode:
                    return {MESSAGE: chat_message, INDEX: actual_index}
                if NEED_MONEY in chat_message and player.money < chat_message[NEED_MONEY]:
                    return {}
                if chat_message.get(SENDER) == YOU:
                    return {MESSAGE: chat_message, INDEX: actual_index}
                if TIMESLOTS in chat_message and gt.curr_timeslot not in chat_message[TIMESLOTS]:
                    return {}
                return {MESSAGE: chat_message, INDEX: actual_index}
            return {}
    
        @staticmethod
        def progress_active_chat(character):
            next_message_info = ChatController.get_next_available_message_info(character)
            character.set_active_chat_index(next_message_info.get(INDEX))
        
            active_chat = character.get_active_chat()
            active_chat_index = character.get_active_chat_index()
            chat_catalogue = ChatController.get_chat_catalogue(active_chat[CHAT])
            chat_action = chat_catalogue[active_chat_index].get(ACTION)
            action_target = chat_catalogue[active_chat_index].get(TARGET)
            action_params = chat_catalogue[active_chat_index].get(PARAMS)
        
            if chat_catalogue[active_chat_index].get(SENDER) != YOU:
                renpy.play(audio.sfx_message_in1, channel="sound10")
        
            if chat_catalogue[active_chat_index].get(TYPE) != CHOICE:
                player.add_chat_to_log(active_chat[CHAT], active_chat[UUID], chat_catalogue[active_chat_index][CONTENT])
        
            if GIVE_POINTS in chat_catalogue[active_chat_index]:
                for char, points in chat_catalogue[active_chat_index][GIVE_POINTS].items():
                    CharacterController.get_character(char).add_points(points)
        
            if active_chat_index + 1 >= len(ChatController.get_chat_catalogue(active_chat[CHAT])):
                ChatController.end_active_chat(character)
        
            if chat_action == PROGRESS_STORY:
                ChatController.progress_story_by_chat(action_target)
            elif chat_action == FUNCTION:
                action_target(action_params) if action_params else action_target()
    
        @staticmethod
        def end_active_chat(character):
            active_chat = character.get_active_chat()
            character.add_to_chat_history(active_chat)
            character.remove_chat_from_queue(active_chat)
            character.set_active_chat_index(-1)
    
        @staticmethod
        def is_next_message_player_reply(character):
            next_message_info = ChatController.get_next_available_message_info(character)
            return next_message_info and next_message_info.get(MESSAGE).get(SENDER) == YOU
    
        @staticmethod
        def is_next_message_from_recipient(character):
            next_message_info = ChatController.get_next_available_message_info(character)
            return next_message_info and next_message_info.get(MESSAGE).get(SENDER) != YOU
    
        @staticmethod
        def get_chat_choices(character):
            next_message_info = ChatController.get_next_available_message_info(character)
            chat_message = next_message_info[MESSAGE]
            choices = []
        
            if chat_message.get(TYPE) == CHOICE:
                for choice in chat_message[CHOICES]:
                    chat_content, is_sensitive = ChatController.get_choice_sensitive(chat_message, choice)
                    choices.append({CONTENT: chat_content[CONTENT], SENSITIVE: is_sensitive})
            else:
                chat_content = ChatController.get_message_content(chat_message, chat_message[SENDER])
                chat_content, is_sensitive = ChatController.get_choice_sensitive(chat_message, chat_content)
                choices.append({CONTENT: chat_content, SENSITIVE: is_sensitive})
            return choices
    
        def get_choice_sensitive(chat_message, chat_content):
            if not vn_mode:
                if TIMESLOTS in chat_message and gt.curr_timeslot not in chat_message[TIMESLOTS]:
                    wrong_time_msg = gt.get_wrong_time_msg(chat_message[TIMESLOTS])
                    return _("{chat_message} ({wrong_time_message})").format(chat_message=chat_content, wrong_time_message=wrong_time_msg), False
                if NEED_MONEY in chat_message and player.money < chat_message[NEED_MONEY]:
                    error_msg = "You need to have ${}".format(chat_message[NEED_MONEY])
                    return _("{chat_message} ({error_msg})").format(chat_message=chat_content, wrong_time_message=wrong_time_msg), False
            return chat_content, True
    
        @staticmethod
        def select_chat_choice(character, selected_choice):
            active_chat = character.get_active_chat()
            next_message_info = ChatController.get_next_available_message_info(character)
            chat_message = next_message_info[MESSAGE]
            if chat_message.get(TYPE) == CHOICE:
                for choice in chat_message[CHOICES]:
                    if choice[CONTENT] == selected_choice:
                        for variable, value in choice[VARIABLES].items():
                            player.set_choice(f"{active_chat[CHAT]}_{active_chat[UUID]}_{variable}", value)
                            player.add_chat_to_log(active_chat[CHAT], active_chat[UUID], choice[CONTENT])
            ChatController.progress_active_chat(character)
            renpy.play(audio.sfx_message_out1, channel="sound10")
    
        @staticmethod
        def get_message_content(message, sender):
            if message[TYPE] == MESSAGE:
                return message[CONTENT]
            elif message[TYPE] == VIDEO:
                return _("Send video") if sender == YOU else _("Sent a video.")
            elif message[TYPE] == PHOTO:
                return _("Send photo") if sender == YOU else _("Sent a photo.")
            return message[CONTENT]
    
        @staticmethod
        def get_active_chats_number():
            active_chats = 0
            for character in sm_indexed_character_list.values():
                if character.get_active_chat() and (character.get_active_chat_index() >= 0 or ChatController.get_next_available_message_info(character).get(MESSAGE, {}).get(SENDER) == YOU):
                    active_chats += 1
            return active_chats
    
        @staticmethod
        def progress_story_by_chat(story_line_name):
            player.progress_storyline(story_line_name)
            StoryController.activate_story_line(story_line_name, True)
    
        @staticmethod
        def is_same_message_group(chat_history, index):
            return index > 0 and chat_history[index].get(SENDER) == chat_history[index - 1].get(SENDER)
    
        @staticmethod
        def is_last_message(chat_history, index):
            return index == len(chat_history) - 1
    
        @staticmethod
        def is_chat_end(character):
            active_chat = character.get_active_chat()
            if active_chat is None:
                return True
            active_chat_index = character.get_active_chat_index()
            return active_chat_index + 1 >= len(ChatController.get_chat_catalogue(active_chat[CHAT]))
