init -1 python:
    class SMLocation:
        def __init__(self, location, sublocation, position, discovered, unlocked):
            self.location = location
            self.sublocation = sublocation
            self.position = position
            self.position_name = position
            self.forward_move = False
            self.left_move = False
            self.back_move = False
            self.right_move = False
            self.is_in_navigation_list = True
            self.show_navigation_list = True
            self.buttons = []
            self.default_schedule = False
            self.unlock_var = self.get_codename() + "_location_unlocked"
            self.discovered_var = self.get_codename() + "_location_discovered"
            self.override_schedules_var = self.get_codename() + "_override_schedules_list"
            self.override_interaction_options_var = self.get_codename() + "_interaction_options_list"
            defaults = {
                    self.discovered_var: discovered,
                    self.unlock_var: unlocked,
                    self.override_schedules_var: [],
                    self.override_interaction_options_var: []
                }
            self.set_defaults(defaults)
    
        def set_defaults(self, defaults):
            for k, v in defaults.items():
                if not hasattr(renpy.store, k):
                    setattr(renpy.store, k, v)
    
        def get_codename(self):
            return f"{self.location}_{self.sublocation}_{self.position}"
    
        @property
        def codename(self):
            return self.get_codename()
    
    
    
        def get_location_image(self, vn_mode_time=None):
            base = self.get_base_state()
            default_image = f"{self.location}_{self.sublocation}_td_{base}_{self.position}"
            if vn_mode:
                image_name = f"{self.location}_{self.sublocation}_{vn_mode_time}_{base}_{self.position}"
            else:
                image_name = f"{self.location}_{self.sublocation}_{gt.curr_display_time_short}_{base}_{self.position}"
            return image_name if renpy.has_image(image_name) else default_image
    
        def get_hover_button_image(self, button):
            base = self.get_base_state()
            target_sublocation = self.get_direction_target_sublocation(button)
            target_position = self.get_direction_target_position(button)
            image_suffix = f"{target_sublocation}_{target_position}" if button != MAP else f"{target_position}"
            image_name_with_base = f"{self.location}_{self.sublocation}_{base}_{self.position}_{image_suffix}"
            return image_name_with_base if renpy.has_image(image_name_with_base) else f"{self.location}_{self.sublocation}_{self.position}_{image_suffix}"
    
        def get_mask_button_image(self, button):
            base = self.get_base_state()
            target_sublocation = self.get_direction_target_sublocation(button)
            target_position = self.get_direction_target_position(button)
            image_suffix = f"{target_sublocation}_{target_position}_mask" if button != MAP else f"{target_position}_mask"
            image_name_with_base = f"{self.location}_{self.sublocation}_{base}_{self.position}_{image_suffix}"
            return image_name_with_base if renpy.has_image(image_name_with_base) else f"{self.location}_{self.sublocation}_{self.position}_{image_suffix}"
    
        def get_arrow_button_image(self, direction):
            direction_map = {
                    FORWARD_MOVE: self.forward_move,
                    LEFT_MOVE: self.left_move,
                    BACK_MOVE: self.back_move,
                    RIGHT_MOVE: self.right_move
                    }
            move = direction_map.get(direction)
            if move == MAP:
                return "nav_exit_button_%s"
            return f"nav_{direction[:-5].lower()}_button_%s"
    
        def get_base_state(self):
            location_state_dict = DEFAULT_LOCATION_STATES.get(f"{self.location}_{self.sublocation}_states", {})
            for state, state_data in location_state_dict.items():
                storyline = state_data.get(STORYLINE)
                if storyline and player.is_storyline_item_finished(storyline[0], storyline[1]):
                    return state
            
                pose = state_data.get(POSE)
                if pose:
                    character = CharacterController.get_character(pose[0])
                    if not character.get_schedule_in_location(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                        continue
                    for pose_name in pose[1]:
                        if character.get_character_pose(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position) == pose_name or vn_mode:
                            return state
            
                characters = state_data.get(CHARACTERS)
                if characters:
                    for character_name in characters:
                        character = CharacterController.get_character(character_name)
                        if character.get_character_in_sublocation(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation) or vn_mode:
                            return state
                schedule = state_data.get(SCHEDULE)
                if schedule:
                    if gt.curr_day in schedule:
                        if gt.curr_timeslot in schedule[gt.curr_day]:
                            return state
        
            return "base01"
    
    
    
        def discover(self):
            player.log_action(f"Discovered location '{self.get_codename()}'")
            setattr(renpy.store, self.discovered_var, True)
    
        def unlock(self):
            player.log_action(f"Unlocked location '{self.get_codename()}'")
            setattr(renpy.store, self.unlock_var, False)
    
        def lock(self):
            player.log_action(f"Locked location '{self.get_codename()}'")
            setattr(renpy.store, self.unlock_var, True)
    
        def get_lock_status(self):
            return getattr(renpy.store, self.unlock_var)
    
        def get_discovered_status(self):
            return getattr(renpy.store, self.discovered_var)
    
        def get_implemented_status(self):
            return renpy.has_image(f"{self.location}_map_button_idle")
    
    
    
        def get_override_schedules(self):
            return getattr(renpy.store, self.override_schedules_var).copy()
    
        def add_schedule(self, schedule_name):
            schedule_list = self.get_override_schedules()
            if schedule_name not in schedule_list:
                schedule_list.insert(0, schedule_name)
                player.log_action(f"Added schedule to location '{self.get_codename()}'")
                setattr(renpy.store, self.override_schedules_var, schedule_list)
    
        def remove_schedule(self, schedule_name):
            schedule_list = self.get_override_schedules()
            if schedule_name in schedule_list:
                schedule_list.remove(schedule_name)
                player.log_action(f"Removed schedule from location '{self.get_codename()}'")
                setattr(renpy.store, self.override_schedules_var, schedule_list)
    
        def is_available_per_schedule(self):
            schedule = indexed_location_schedule[self.get_codename()]
            return SMGameTime.check_list_for_day(schedule[DAYS], gt.curr_day) and SMGameTime.check_list_for_timeslot(schedule[TIMESLOTS], gt.curr_timeslot)
    
        def is_available_day(self, day):
            schedule = indexed_location_schedule[self.get_codename()]
            return SMGameTime.check_list_for_day(schedule[DAYS], day)
    
        def is_available_time(self, timeslot):
            schedule = indexed_location_schedule[self.get_codename()]
            return SMGameTime.check_list_for_timeslot(schedule[TIMESLOTS], timeslot)
    
        def get_schedule_list(self):
            schedule_list = self.get_override_schedules()
            schedule_list += QuestController.get_quest_schedule_overrides_for_locations(self.get_codename(), self.location)
            schedule_list.append(self.default_schedule)
            return schedule_list
    
        def get_schedule(self, timeslot, day):
            for schedule_name in self.get_schedule_list():
                result = Schedule.find_schedule_in_day(DEFAULT_LOCATION_TIMETABLES[schedule_name], timeslot, day)
                if result:
                    return result
            return False
    
        def get_day_schedule(self, day):
            for schedule_name in self.get_schedule_list():
                result = Schedule.find_timeslots_for_day(DEFAULT_LOCATION_TIMETABLES[schedule_name], day)
                if result:
                    return result
            return False
    
    
    
        def get_interaction_options(self, timeslot, day):
            schedule_list = self.get_schedule(timeslot, day)
            if not isinstance(schedule_list, list):
                schedule_list = [schedule_list]
            result = []
            for schedule in schedule_list:
                if INTERACTION in schedule:
                    result.append(InteractionLocationOption.init_interaction_option(schedule[INTERACTION], self))
            for io in self.get_override_interaction_options():
                result.append(InteractionLocationOption.init_interaction_option(io, self))
            return QuestController.add_location_interactions_override(self, result)
    
        def add_override_interaction_option(self, interaction_option_codename):
            interaction_options_list = self.get_override_interaction_options()
            interaction_options_list.insert(0, interaction_option_codename)
            player.log_action(f"Added '{interaction_option_codename}' to location '{self.get_codename()}'")
            setattr(renpy.store, self.override_interaction_options_var, interaction_options_list)
    
        def get_override_interaction_options(self):
            return getattr(renpy.store, self.override_interaction_options_var).copy()
    
        def remove_override_interaction_option(self, interaction_option_codename):
            interaction_options_list = self.get_override_interaction_options()
            if interaction_option_codename in interaction_options_list:
                interaction_options_list.remove(interaction_option_codename)
                player.log_action(f"Removed '{interaction_option_codename}' from location '{self.get_codename()}'")
            setattr(renpy.store, self.override_interaction_options_var, interaction_options_list)
    
    
    
        def can_move(self, direction):
            if getattr(self, f"{direction}_move") == MAP:
                return True
            location = self.get_target_move_location(getattr(self, f"{direction}_move"))
            return location and SMLocation.check_location_discovered(location.location, location.sublocation, location.position)
    
        def can_move_forward(self):
            return self.can_move("forward")
    
        def can_move_left(self):
            return self.can_move("left")
    
        def can_move_back(self):
            return self.can_move("back")
    
        def can_move_right(self):
            return self.can_move("right")
    
        def get_direction_target_sublocation(self, direction_data):
            return direction_data[0] if direction_data and isinstance(direction_data, list) else self.sublocation
    
        def get_direction_target_position(self, direction_data):
            return direction_data[1] if direction_data and isinstance(direction_data, list) else direction_data
    
        def get_target_move_location(self, direction_data):
            if direction_data:
                if isinstance(direction_data, list):
                    return LocationController.get_location(self.location, direction_data[0], direction_data[1])
                return LocationController.get_location(self.location, self.sublocation, direction_data)
            return False
    
        def get_open_status(self):
            hint = QuestController.get_map_location_hint_from_quest_pool(self) or (self.get_schedule(gt.curr_timeslot, gt.curr_day) or {}).get(HINT, False)
            lock_status = self.get_lock_status()
            if lock_status is True:
                return {REASON: LOC_CLOSED_REASON_NOT_UNLOCKED, HINT: hint}
            if lock_status not in (False, True):
                return {REASON: LOC_CLOSED_REASON_LOCKED_WITH_REDIRECT, HINT: hint, TARGET: lock_status}
            location_schedule = self.get_schedule(gt.curr_timeslot, gt.curr_day)
            if location_schedule and location_schedule.get(OPEN):
                return {REASON: False, HINT: hint}
            day_schedule = self.get_day_schedule(gt.curr_day)
            if day_schedule:
                for timeslot, timeslot_data in day_schedule.items():
                    if timeslot_data[OPEN]:
                        if gt.get_timeslot_number_in_day_order(timeslot) < gt.get_timeslot_number_in_day_order(gt.curr_timeslot):
                            return {REASON: LOC_CLOSED_REASON_SCHEDULE_ALREADY_CLOSED, HINT: hint}
                        return {REASON: LOC_CLOSED_REASON_SCHEDULE_OPENS_LATER, HINT: hint}
                return {REASON: LOC_CLOSED_REASON_SCHEDULE_DAY, HINT: hint}
            return {REASON: LOC_CLOSED_REASON_SCHEDULE_DAY, HINT: hint}
    
        def is_nvagation_button_visible(self, button):
            target_sublocation = self.get_direction_target_sublocation(button)
            target_position = self.get_direction_target_position(button)
            location = LocationController.get_location(self.location, target_sublocation, target_position)
            if location:
                return location.get_discovered_status()
            return True
    
        @staticmethod
        def get_current_location():
            return indexed_locations_list[f"{curr_location}_{curr_sublocation}_{curr_position}"]
    
        @staticmethod
        def check_location_discovered(location, sublocation, position):
            if position == MAP:
                return True
            for l in sm_locations_list:
                if l.location == location and l.sublocation == sublocation and l.position == position:
                    return l.get_discovered_status()
            return False
    
        @staticmethod
        def init_location(data):
            location = SMLocation(data[LOCATION], data[SUBLOCATION], data[POSITION], data[DISCOVERED], data[LOCKED])
            location.forward_move = data.get(FORWARD_MOVE, False)
            location.position_name = data.get(P_NAME, False)
            location.left_move = data.get(LEFT_MOVE, False)
            location.back_move = data.get(BACK_MOVE, False)
            location.right_move = data.get(RIGHT_MOVE, False)
            location.is_in_navigation_list = data.get(IS_IN_NAVIGATION_LIST, False)
            location.show_navigation_list = data.get(SHOW_NAVIGATION_LIST, False)
            location.buttons = data.get(NAVIGATION_BUTTONS, False)
            location.default_schedule = data.get(SCHEDULE, False)
            return location
