init -1 python:
    class SMObject:
        def __init__(self, codename, days, times, unlocked, is_in_base_image=True):
            self.codename = codename
            self.days = days
            self.times = times
            self.is_in_base_image = is_in_base_image
            self.default_schedule_name = "default_" + self.codename
            self.override_schedules_var = self.codename + "_obj_override_schedules_list"
            self.override_interaction_options_var = self.codename + "_override_interaction_options"
        
            self.unlock_var = self.codename + "_object_unlocked"
            defaults = {
                    self.unlock_var: unlocked,
                    self.override_schedules_var: [],
                    self.override_interaction_options_var: [],
                }
            self.set_defaults(defaults)
    
        def set_defaults(self, defaults):
            for k, v in defaults.items():
                if not hasattr(renpy.store, k):
                    setattr(renpy.store, k, v)
    
        def get_lock_status(self):
            return getattr(renpy.store, self.unlock_var)
    
        def unlock(self):
            player.log_action(f"Unlock object '{self.codename}'")
            setattr(renpy.store, self.unlock_var, True)
    
        def lock(self):
            player.log_action(f"Lock object '{self.codename}'")
            setattr(renpy.store, self.unlock_var, False)
    
    
    
        def has_schedule(self):
            return self.default_schedule_name in DEFAULT_OBJECTS_TIMETABLES
    
        def add_schedule(self, schedule_name):
            schedule_list = self.get_override_schedules()
            if schedule_name not in schedule_list:
                schedule_list.insert(0, schedule_name)
                player.log_action(f"Added '{schedule_name}' to object '{self.codename}'")
                setattr(renpy.store, self.override_schedules_var, schedule_list)
    
        def get_schedule(self, timeslot, day):
            if not self.has_schedule():
                return False
            schedule_list = self.get_combined_schedules()
            for schedule_name in schedule_list:
                result = Schedule.find_schedule_in_day(DEFAULT_OBJECTS_TIMETABLES[schedule_name], timeslot, day)
                if result:
                    return result
            return False
    
        def remove_schedule(self, schedule_name):
            schedule_list = self.get_override_schedules()
            if schedule_name in schedule_list:
                schedule_list.remove(schedule_name)
                player.log_action(f"Removed '{schedule_name}' from object '{self.codename}'")
                setattr(renpy.store, self.override_schedules_var, schedule_list)
    
        def get_schedule_in_location(self, timeslot, day, location, sublocation, position):
            current_slots = self.get_schedule(timeslot, day)
            if current_slots:
                for slot in current_slots:
                    if slot.location == location and slot.sublocation == sublocation and slot.position == position:
                        return slot
            return []
    
        def get_override_schedules(self):
            return getattr(renpy.store, self.override_schedules_var).copy()
    
        def get_combined_schedules(self):
            schedule_list = self.get_override_schedules()
            schedule_list += QuestController.get_quest_schedule_overrides_for_objects(self.codename)
            schedule_list.append(self.default_schedule_name)
            return schedule_list
    
    
    
        def get_object_interactable(self, timeslot, day, location, sublocation, position):
            options = self.get_interaction_options(timeslot, day, location, sublocation, position)
            options = InteractionObjectOption.get_visible_interaction_options(options)
            return bool(options)
    
        def get_object_schedule_interactions(self, timeslot, day, location, sublocation, position):
            slot = self.get_schedule_in_location(timeslot, day, location, sublocation, position)
            return slot.interactable if slot.interactable else False
    
        def get_interaction_options(self, timeslot, day, location, sublocation, position):
            schedule_interaction_value = self.get_object_schedule_interactions(timeslot, day, location, sublocation, position)
            if not isinstance(schedule_interaction_value, list):
                schedule_interaction_value = [schedule_interaction_value]
            result = []
            for codename in schedule_interaction_value:
                if codename != NOT_INTERACTABLE:
                    result.append(InteractionObjectOption.init_interaction_option(codename, self))
            for codename in self.get_override_interaction_options():
                result.append(InteractionObjectOption.init_interaction_option(codename, self))
            return result
    
        def add_default_interaction_options(self, interaction_option_codename):
            self.add_interaction_option(interaction_option_codename, log_action=False)
    
        def add_override_interaction_option(self, interaction_option_codename):
            self.add_interaction_option(interaction_option_codename, log_action=True)
    
        def add_interaction_option(self, interaction_option_codename, log_action):
            interaction_options_list = self.get_override_interaction_options()
            interaction_options_list.insert(0, interaction_option_codename)
            if log_action:
                player.log_action(f"Added '{interaction_option_codename}' to object '{self.codename}'")
            setattr(renpy.store, self.override_interaction_options_var, interaction_options_list)
    
        def get_override_interaction_options(self):
            return getattr(renpy.store, self.override_interaction_options_var).copy()
    
        def remove_override_interaction_option(self, interaction_option_codename):
            interaction_options_list = self.get_override_interaction_options()
            if interaction_option_codename in interaction_options_list:
                interaction_options_list.remove(interaction_option_codename)
                player.log_action(f"Removed '{interaction_option_codename}' from object '{self.codename}'")
            setattr(renpy.store, self.override_interaction_options_var, interaction_options_list)
    
    
    
        def get_object_pose(self, timeslot, day, location, sublocation, position):
            slot = self.get_schedule_in_location(timeslot, day, location, sublocation, position)
            random.seed(gt.get_random_seed)
            return random.choice(slot.state)
    
        def get_pose_depth(self, timeslot, day, location, sublocation, position):
            default_depth = "50"
            pose = self.get_object_pose(timeslot, day, location, sublocation, position)
            if pose:
                pose_digits = "".join(char for char in pose if char.isdigit())
                return pose_digits[-2:] if pose_digits else default_depth
            return default_depth
    
        def get_object_image(self, timeslot, day, location, sublocation, position, what=IDLE):
            obj_image = self.get_object_pose(timeslot, day, location, sublocation, position)
            suffix = {IDLE: "", HOVER: "_hover", MASK: "_mask"}.get(what, "")
            base = LocationController.get_location(location, sublocation, position).get_base_state()
            if what == IDLE and self.is_in_base_image:
                return "empty_image"
        
            possible_file_names = [
                    f"{location}_{sublocation}_{base}_{gt.curr_display_time_short}_{self.codename}_{obj_image}_{position}{suffix}",
                    f"{location}_{sublocation}_{base}_td_{self.codename}_{obj_image}_{position}{suffix}",
                    f"{location}_{sublocation}_{gt.curr_display_time_short}_{self.codename}_{obj_image}_{position}{suffix}",
                    f"{location}_{sublocation}_td_{self.codename}_{obj_image}_{position}{suffix}",
                    ]
        
            for img in possible_file_names:
                if renpy.has_image(img):
                    return img
            return possible_file_names[-1]
