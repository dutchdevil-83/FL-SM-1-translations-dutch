init -1 python:
    import random

    class SMCharacter:
        def __init__(self, name, surname, codename, constant):
            self.name = name
            self.surname = surname
            self.codename = codename
            self.constant = constant
            self.faction = False
            self.storyline = False
            self.is_essential = False
            self.unlock_condition = False
            self.unlocked_var = f"{self.codename}_unlocked"
            self.default_schedule_name = f"default_{self.codename}"
            self.relationship_points_var = f"{self.codename}_relationship_points"
            self.relationship_points_limit_var = f"{self.codename}_relationship_points_limit"
            self.override_schedules_var = f"{self.codename}_override_schedules_list"
            self.traits_var = f"{self.codename}_traits_storage"
            self.topics_var = f"{self.codename}_topics_storage"
            self.override_interaction_options_var = f"{self.codename}_override_interaction_options"
            self.chat_available = False
            self.chat_history_var = f"{self.codename}_chat_history_var"
            self.chat_queue = f"{self.codename}_chat_queue"
            self.active_chat_index = f"{self.codename}_active_chat_index"
    
        def set_defaults(self, defaults):
            for k, v in defaults.items():
                if not hasattr(renpy.store, k):
                    setattr(renpy.store, k, v)
    
        def unlock_character(self):
            if not getattr(renpy.store, self.unlocked_var):
                setattr(renpy.store, self.unlocked_var, True)
    
        def get_is_unlocked(self):
            if getattr(renpy.store, self.unlocked_var):
                return True
            if isinstance(self.unlock_condition, (list, tuple)):
                if player.is_storyline_item_finished(self.unlock_condition[0], self.unlock_condition[1]):
                    self.unlock_character()
                    return True
            return False
    
        @property
        def full_name(self):
            return f"{self.name} {self.surname}".strip()
    
        @property
        def char_image(self):
            char_with_random_images = {"sy": 2, "mes": 2}
            for char, rand_image_count in char_with_random_images.items():
                if self.codename == char:
                    random_image_number = renpy.random.randint(1, rand_image_count)
                    return f"character_{self.codename}_{random_image_number}"
            return f"character_{self.codename}"
    
    
    
        @property
        def points(self):
            if vn_mode:
                return 99999
            return getattr(renpy.store, self.relationship_points_var)
    
        def add_point(self, amount=1):
            total = self.points + amount
            limit = self.get_points_limit()
        
            if total >= limit:
                difference = limit - self.points
                total = limit
                message = f"You got {difference} relationship point(s) with {self.name}" if difference > 0 else f"You have reached the current maximum relationship points limit with {self.name}"
                player.log_action(f"Player reached current maximum Point(s) with '{self.codename}'")
                amount = difference
            elif total < 0:
                total = 0
                message = f"You lost {abs(amount)} relationship point(s) with {self.name}"
            else:
                message = f"You got {amount} relationship point(s) with {self.name}"
        
            self.unlock_character()
            if not vn_mode:
                renpy.notify(message)
            setattr(renpy.store, self.relationship_points_var, total)
            player.log_action(f"Added '{amount}' point(s) to character '{self.codename}'. Point limit '{limit}'")
            renpy.play(audio.sfx_menu_notification2, channel="sound9")
            EventController.action(RELATIONSHIP_POINTS_ADDED, self.codename, amount, total)
    
        def deduct_point(self, amount=1):
            total = self.points - amount
            if total < 0:
                total = 0
            if not vn_mode:
                renpy.notify(f"You lost {amount} relationship point with {self.name}")
            setattr(renpy.store, self.relationship_points_var, total)
            player.log_action(f"Removed '{amount}' point from character '{self.codename}'. Point limit '{self.get_points_limit()}'")
            renpy.play(audio.sfx_menu_notification2, channel="sound9")
            EventController.action(RELATIONSHIP_POINTS_ADDED, self.codename, amount, total)
    
        def get_points_limit(self):
            return getattr(renpy.store, self.relationship_points_limit_var)
    
        def update_points_limit(self, amount):
            setattr(renpy.store, self.relationship_points_limit_var, amount)
    
    
    
        def get_override_schedules(self):
            return getattr(renpy.store, self.override_schedules_var).copy()
    
        def has_schedule(self):
            return self.default_schedule_name in DEFAULT_CHARACTERS_TIMETABLES
    
        def add_schedule(self, schedule_name):
            schedule_list = self.get_override_schedules()
            if schedule_name not in schedule_list:
                schedule_list.insert(0, schedule_name)
                player.log_action(f"Added '{schedule_name}' to character '{self.codename}'")
                setattr(renpy.store, self.override_schedules_var, schedule_list)
    
        def remove_schedule(self, schedule_name):
            schedule_list = self.get_override_schedules()
            if schedule_name in schedule_list:
                schedule_list.remove(schedule_name)
                player.log_action(f"Removed '{schedule_name}' from character '{self.codename}'")
                setattr(renpy.store, self.override_schedules_var, schedule_list)
    
        def get_schedule(self, timeslot, day):
            if not self.has_schedule():
                return False
            schedule_list = QuestController.get_quest_schedule_overrides_for_character(self.codename) + self.get_override_schedules()
            schedule_list.append(self.default_schedule_name)
            for schedule_name in schedule_list:
                result = Schedule.find_schedule_in_day(DEFAULT_CHARACTERS_TIMETABLES[schedule_name], timeslot, day)
                if result:
                    return result
            return False
    
        def get_schedule_in_location(self, timeslot, day, location, sublocation, position):
            current_slots = self.get_schedule(timeslot, day)
            if current_slots:
                for slot in current_slots:
                    if slot.location == location and slot.sublocation == sublocation and slot.position == position:
                        return slot
            return False
    
        def get_character_in_location(self, timeslot, day, location):
            current_slots = self.get_schedule(timeslot, day)
            if current_slots:
                for slot in current_slots:
                    if slot.location == location and slot.get_interactable() is True:
                        return True
            return False
    
        def get_character_in_sublocation(self, timeslot, day, location, sublocation):
            current_slots = self.get_schedule(timeslot, day)
            if current_slots:
                for slot in current_slots:
                    if slot.location == location and slot.sublocation == sublocation and slot.get_interactable() is True:
                        return True
            return False
    
        def get_character_in_position(self, timeslot, day, location, sublocation, position):
            current_slots = self.get_schedule(timeslot, day)
            if current_slots:
                for slot in current_slots:
                    if slot.location == location and slot.sublocation == sublocation and slot.position == position and slot.get_accurate_position() is True:
                        return True
            return False
    
        @staticmethod
        def get_specific_character_in_position(character_codename):
            character = CharacterController.get_character(character_codename)
            current_slots = character.get_schedule(gt.curr_timeslot, gt.curr_day)
            if current_slots:
                for slot in current_slots:
                    if slot.location == curr_location and slot.sublocation == curr_sublocation and slot.position == curr_position:
                        if character.get_character_interactable(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                            return True
            return False
    
        @staticmethod
        def get_specific_character_in_location(character_codename, check_whole_location=False):
            character = CharacterController.get_character(character_codename)
            current_slots = character.get_schedule(gt.curr_timeslot, gt.curr_day)
            if current_slots:
                for slot in current_slots:
                    if slot.location == curr_location and (slot.sublocation == curr_sublocation or check_whole_location is True):
                        return True
            return False
    
    
    
        def get_character_pose(self, timeslot, day, location, sublocation, position):
            slot = self.get_schedule_in_location(timeslot, day, location, sublocation, position)
            random.seed(gt.get_random_seed)
            return random.choice(slot.state)
    
        def get_pose_depth(self, timeslot, day, location, sublocation, position):
            default_depth = "50"
            pose = self.get_character_pose(timeslot, day, location, sublocation, position)
            pose_digits = "".join(char for char in pose if char.isdigit())
            return pose_digits[-2:] if pose_digits else default_depth
    
        def get_character_image(self, timeslot, day, location, sublocation, position, what=IDLE):
            char_image = self.get_character_pose(timeslot, day, location, sublocation, position)
            dress_code = DressCodeController.get_dress_code(self.codename, timeslot, day, location, sublocation, position)
            suffix = {IDLE: "", HOVER: "_hover", MASK: "_mask"}.get(what, "")
        
            possible_file_names = [
                    f"{location}_{sublocation}_{gt.curr_display_time_short}_{self.codename}_{char_image}#{dress_code}_{position}{suffix}",
                    f"{location}_{sublocation}_td_{self.codename}_{char_image}#{dress_code}_{position}{suffix}",
                    f"{location}_{sublocation}_{gt.curr_display_time_short}_{self.codename}_{char_image}_{position}{suffix}",
                    f"{location}_{sublocation}_td_{self.codename}_{char_image}_{position}{suffix}",
                    ]
        
            for img in possible_file_names:
                if renpy.has_image(img):
                    return img
            return possible_file_names[-1]
    
    
    
        def init_traits(self, traits):
            if not self.get_traits():
                setattr(renpy.store, self.traits_var, traits)
    
        def get_traits(self):
            return getattr(renpy.store, self.traits_var).copy()
    
        def discover_trait(self, trait):
            traits = self.get_traits()
            if trait in traits:
                return False
            traits.append(trait)
            setattr(renpy.store, self.traits_var, traits)
            trait_type = sm_indexed_traits_list[trait][TYPE]
            trait_name = sm_indexed_traits_list[trait][NAME]
            if trait_type == TYPE_FETISH:
                renpy.notify(f"You discovered that {self.name} likes {trait_name}")
            elif trait_type == TYPE_PHYSIC:
                renpy.notify(f"You discovered trait {trait_name} about {self.name}")
            player.log_action(f"Added '{trait}' trait to character '{self.codename}'")
            renpy.play(audio.sfx_menu_notification3, channel="sound9")
            EventController.action(CHARACTER_TRAIT_DISCOVERED, trait)
    
    
    
        def init_topics(self, topics):
            if not self.get_topics():
                setattr(renpy.store, self.topics_var, topics)
    
        def get_topics(self):
            return getattr(renpy.store, self.topics_var).copy()
    
        def discover_topic(self, topic):
            topics = self.get_topics()
            if topic in topics:
                return False
            topics.append(topic)
            setattr(renpy.store, self.topics_var, topics)
            renpy.notify(f"You discovered that {self.name} likes topic {topic}")
            player.log_action(f"Added '{topic}' topic to character '{self.codename}'")
            renpy.play(audio.sfx_menu_notification3, channel="sound9")
            EventController.action(CHARACTER_TOPIC_DISCOVERED, topic)
    
    
    
        def get_default_interaction_for_timeslot(self, timeslot, day, location, sublocation, position):
            slot = self.get_schedule_in_location(timeslot, day, location, sublocation, position)
            slot_default_image = slot.get_default_interaction_image(self, timeslot, day, location, sublocation, position)
            if slot_default_image:
                return slot_default_image
            default_expression = getattr(self, "default_expression", "empty")
            return CharacterController.get_expression_image(self.codename, default_expression)
    
        def get_random_interaction_dialogue(self, pose):
            if hasattr(renpy.store, f"{self.codename}_{pose}_interactions_list"):
                dialogue_list = getattr(renpy.store, f"{self.codename}_{pose}_interactions_list")
                return renpy.random.choice(dialogue_list)
            return False
    
        def get_character_interactable(self, timeslot, day, location, sublocation, position):
            slot = self.get_schedule_in_location(timeslot, day, location, sublocation, position)
            interaction = slot.get_interaction_options(self, timeslot, day, location, sublocation, position)
            if interaction is NOT_INTERACTABLE or not interaction:
                return self.has_visible_override_interaction_options()
            return True
    
        def get_character_schedule_interactions(self, timeslot, day, location, sublocation, position):
            slot = self.get_schedule_in_location(timeslot, day, location, sublocation, position)
            interaction = slot.get_interaction_options(self, timeslot, day, location, sublocation, position)
            return interaction if interaction is not NOT_INTERACTABLE else False
    
        def get_interaction_options(self, timeslot, day, location, sublocation, position):
            schedule_interaction_value = self.get_character_schedule_interactions(timeslot, day, location, sublocation, position)
            if schedule_interaction_value and not isinstance(schedule_interaction_value, list):
                schedule_interaction_value = [schedule_interaction_value]
            elif schedule_interaction_value is False:
                schedule_interaction_value = []
            result = []
            for codename in schedule_interaction_value:
                if codename != NOT_INTERACTABLE:
                    result.append(InteractionCharacterOption.init_interaction_option(codename, self))
            for codename in self.get_override_interaction_options():
                result.append(InteractionCharacterOption.init_interaction_option(codename, self))
            return result
    
        def is_angry_peek(self, timeslot, day, location, sublocation, position):
            return self.get_character_schedule_interactions(timeslot, day, location, sublocation, position) == ANGRY_PEEK
    
        def is_watch_pee(self, timeslot, day, location, sublocation, position):
            return self.get_character_schedule_interactions(timeslot, day, location, sublocation, position) == WATCH_PEE
    
        def is_busy(self, timeslot, day, location, sublocation, position):
            return self.get_character_schedule_interactions(timeslot, day, location, sublocation, position) == BUSY
    
        def add_override_interaction_option(self, interaction_option_codename):
            interaction_options_list = self.get_override_interaction_options()
            interaction_options_list.insert(0, interaction_option_codename)
            player.log_action(f"Added '{interaction_option_codename}' to character '{self.codename}'")
            setattr(renpy.store, self.override_interaction_options_var, interaction_options_list)
    
        def get_override_interaction_options(self):
            return getattr(renpy.store, self.override_interaction_options_var).copy()
    
        def has_visible_override_interaction_options(self):
            interaction_options_list = self.get_override_interaction_options()
            visible_interaction_options_list = []
            for io in interaction_options_list:
                io_object = InteractionCharacterOption.init_interaction_option(io, self)
                if io_object.is_visible():
                    visible_interaction_options_list.append(io)
            return bool(visible_interaction_options_list)
    
        def remove_override_interaction_option(self, interaction_option_codename):
            interaction_options_list = self.get_override_interaction_options()
            if interaction_option_codename in interaction_options_list:
                interaction_options_list.remove(interaction_option_codename)
                player.log_action(f"Removed '{interaction_option_codename}' from character '{self.codename}'")
            setattr(renpy.store, self.override_interaction_options_var, interaction_options_list)
    
    
    
        def interact(self):
            if player.has_interacted(self):
                return
            renpy.jump("quick_interaction")
    
        def get_quick_interaction(self):
            result_list = []
            if "interactions" not in dir(self):
                return "busy_interaction"
            location = curr_location
            sublocation = curr_sublocation
            day = gt.curr_day
            timeslot = gt.curr_timeslot
            for interaction in self.interactions:
                if sublocation in interaction.get(BANNED_SUBLOCATIONS, []):
                    continue
                if LOCATIONS in interaction and not SMGameTime.check_list_for_location(interaction[LOCATIONS], location):
                    continue
                if DAYS in interaction and not SMGameTime.check_list_for_day(interaction[DAYS], day):
                    continue
                if TIMESLOTS in interaction and not SMGameTime.check_list_for_timeslot(interaction[TIMESLOTS], timeslot):
                    continue
                if AFTER_SCENE in interaction and not player.is_storyline_item_finished(interaction[AFTER_SCENE][0], interaction[AFTER_SCENE][1]):
                    continue
                if BEFORE_SCENE in interaction and player.is_storyline_item_finished(interaction[BEFORE_SCENE][0], interaction[BEFORE_SCENE][1]):
                    continue
                result_list.append(interaction[LABEL])
            if result_list:
                random.seed(gt.get_random_seed)
                return random.choice(result_list)
            return "busy_interaction"
    
        def after_quick_interaction(self):
            player.interact(self)
            gt.add(0, 15, 0)
    
    
    
        def get_chat_queue(self):
            return getattr(renpy.store, self.chat_queue).copy()
    
        def add_chat_to_queue(self, chat):
            chat_queue = self.get_chat_queue()
            chat_queue.append({CHAT: chat, UUID: get_uuid()})
            setattr(renpy.store, self.chat_queue, chat_queue)
    
        def remove_chat_from_queue(self, chat):
            chat_queue = self.get_chat_queue()
            if chat in chat_queue:
                chat_queue.remove(chat)
                setattr(renpy.store, self.chat_queue, chat_queue)
    
        def get_active_chat(self):
            if not self.get_chat_queue():
                return None
            return self.get_chat_queue()[0]
    
        def get_chat_history(self):
            return getattr(renpy.store, self.chat_history_var).copy()
    
        def add_to_chat_history(self, chat):
            chat_history = self.get_chat_history()
            chat_history.append({CHAT: chat[CHAT], UUID: chat[UUID]})
            setattr(renpy.store, self.chat_history_var, chat_history)
    
        def get_active_chat_index(self):
            return getattr(renpy.store, self.active_chat_index)
    
        def set_active_chat_index(self, index):
            return setattr(renpy.store, self.active_chat_index, index)
    
        def get_unread_chat(self):
            return self.get_active_chat() and (self.get_active_chat_index() >= 0 or ChatController.get_next_available_message_info(self).get(MESSAGE, {}).get(SENDER) == YOU)
    
    
    
        @staticmethod
        def init_character(data):
            character = SMCharacter(data[NAME], data[SURNAME], data[CODENAME], data[CONSTANT])
            character.faction = data.get(FACTION, False)
            character.storyline = data.get(STORYLINE, False)
            character.is_essential = data.get(ESSENTIAL, False)
            character.unlock_condition  = data.get(UNLOCK_CONDITION, False)
            character.chat_available = data.get(CHAT, False)
            defaults = {
                    character.unlocked_var: True if not character.unlock_condition else False,
                    character.relationship_points_var: 0,
                    character.relationship_points_limit_var: 5,
                    character.override_schedules_var: [],
                    character.override_interaction_options_var: [],
                    character.traits_var: [],
                    character.topics_var: [],
                    character.chat_history_var: [],
                    character.chat_queue: [],
                    character.active_chat_index: -1,
                }
            character.set_defaults(defaults)
            return character
