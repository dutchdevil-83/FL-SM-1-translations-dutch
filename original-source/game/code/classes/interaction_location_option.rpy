init -1 python:
    class InteractionLocationOption:
        def __init__(self, location, name, action):
            self.location = location
            self.name = name
            self.action = action
            self.target = False
            self.params = False
            self.daily_limit = False
            self.energy_limit = False
            self.available_timeslots = False
            self.available_days = False
            self.hidden = False
            self.disabled_by_penalty = False
    
        def click(self):
            player.log_action(f"Clicked on location interaction '{self.name}'")
            action = self.get_action()
            if action == JUMP:
                self.consume_player_interaction_limit()
                renpy.jump(self.target)
            elif action == CALL:
                self.consume_player_interaction_limit()
                renpy.call(self.target)
            elif action == FUNCTION:
                self.consume_player_interaction_limit()
                if self.params:
                    self.target(self.params)
                else:
                    self.target()
            elif action == PROGRESS_STORY:
                self.consume_player_interaction_limit()
                StoryController.advance_storyline_by_interaction_option(self.target)
    
        def consume_player_interaction_limit(self):
            if self.daily_limit:
                player.consume_interaction(f"{self.location.get_codename()}_{self.daily_limit}")
    
        def get_name(self):
            if self.daily_limit and player.has_interacted_location(self.location, self.daily_limit):
                return _("{name} (done today)").format(name=self.name)
            if self.energy_limit and not player.enough_energy(self.energy_limit):
                return _("{name} (not enough energy)").format(name=self.name)
            if self.available_timeslots and gt.curr_timeslot not in self.available_timeslots:
                wrong_time_msg = gt.get_wrong_time_msg(self.available_timeslots)
                return _("{name} ({wrong_time_message})").format(name=self.name, wrong_time_message=wrong_time_msg)
            if self.available_days and gt.curr_day not in self.available_days:
                return _("{name} (wrong day)").format(name=self.name)
            if self.disabled_by_penalty and player.is_rent_penalty():
                return _("{name} (disabled on penalty week)").format(name=self.name)
            return self.name
    
        def get_action(self):
            return DISABLED_ACTION if self.is_disabled() else self.action
    
        def is_disabled(self):
            if self.daily_limit and player.has_interacted_location(self.location, self.daily_limit):
                return True
            if self.energy_limit and not player.enough_energy(self.energy_limit):
                return True
            if self.available_timeslots and gt.curr_timeslot not in self.available_timeslots:
                return True
            if self.available_days and gt.curr_day not in self.available_days:
                return True
            if self.disabled_by_penalty and player.is_rent_penalty():
                return True
            return False
    
        def is_visible(self):
            if self.available_days and gt.curr_day not in self.available_days:
                return False
            if self.available_timeslots and gt.curr_timeslot not in self.available_timeslots:
                return False
            if self.daily_limit and player.has_interacted_location(self.location, self.daily_limit):
                return True
            if self.energy_limit and not player.enough_energy(self.energy_limit):
                return True
            if self.disabled_by_penalty and player.is_rent_penalty():
                return True
            return True
    
        @staticmethod
        def get_visible_interaction_options(interaction_options):
            interaction_option_list = []
            for interaction_option in interaction_options:
                if interaction_option.hidden:
                    continue
                if interaction_option.is_visible() is False:
                    continue
                interaction_option_list.append(interaction_option)
            return interaction_option_list
    
        @staticmethod
        def init_interaction_option(code, location):
            io_data = INTERACTIONS_LOCATION_CATALOGUE[code]
            io_location = InteractionLocationOption(location, io_data[NAME], io_data[ACTION])
            io_location.target = io_data.get(TARGET, False)
            io_location.params = io_data.get(PARAMS, False)
            io_location.daily_limit = io_data.get(DAILY_LIMIT, False)
            io_location.energy_limit = io_data.get(ENERGY_LIMIT, False)
            io_location.available_timeslots = io_data.get(TIMESLOTS, False)
            io_location.available_days = io_data.get(DAYS, False)
            io_location.hidden = io_data.get(HIDDEN, False)
            io_location.schedule_hidden = io_data.get(DISABLED_HIDDEN, False)
            io_location.disabled_by_penalty = io_data.get(DISABLED_BY_PENALTY, False)
            return io_location
