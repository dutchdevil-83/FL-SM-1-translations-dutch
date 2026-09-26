init -1 python:
    class InteractionObjectOption:
        def __init__(self, object, name, action):
            self.object = object
            self.name = name
            self.action = action
            self.target = False
            self.params = False
            self.daily_limit = False
            self.energy_limit = False
            self.available_timeslots = False
            self.available_days = False
            self.hidden = False
            self.schedule_hidden = False
            self.disabled_by_penalty = False
            self.days_passed = False
            self.need_money = False
    
        def click(self):
            player.log_action(f"Clicked on object interaction '{self.name}'")
            action = self.get_action()
            if action == JUMP:
                self.consume_player_interaction_limit()
                renpy.jump(self.target)
            elif action == CALL:
                self.consume_player_interaction_limit()
                renpy.call(self.target)
            elif action == FUNCTION:
                self.consume_player_interaction_limit()
                self.target(self.params) if self.params else self.target()
            elif action == PROGRESS_STORY:
                self.consume_player_interaction_limit()
                StoryController.advance_storyline_by_interaction_option(self.target)
    
        def consume_player_interaction_limit(self):
            if self.daily_limit:
                player.consume_interaction(f"{self.object.codename}_{self.daily_limit}")
    
        def get_name(self):
            if self.daily_limit and player.has_interacted_object(self.object, self.daily_limit):
                return _("{name} (done today)").format(name=self.name)
            if self.energy_limit and not player.enough_energy(self.energy_limit):
                return _("{name} (not enough energy)").format(name=self.name)
            if self.available_timeslots and gt.curr_timeslot not in self.available_timeslots:
                wrong_time_msg = gt.get_wrong_time_msg(self.available_timeslots)
                return _("{name} ({wrong_time_message})").format(name=self.name, wrong_time_message=wrong_time_msg)
            if self.available_days and gt.curr_day not in self.available_days:
                return _("{name} (wrong day)").format(name=self.name)
            if self.days_passed and not player.completion_log_compare_date_for_item(self.days_passed[TARGET], self.days_passed[DAYS]):
                return "{} ({})".format(self.name, _('not available today'))
            if self.need_money and player.money < self.need_money:
                return _("{name} (You need to have ${needed_money})").format(name=self.name, needed_money=self.need_money)
            if self.disabled_by_penalty and player.is_rent_penalty():
                return _("{name} (disabled on penalty week)").format(name=self.name)
            return self.name
    
        def get_action(self):
            return DISABLED_ACTION if self.is_disabled() else self.action
    
        def is_disabled(self):
            if self.daily_limit and player.has_interacted_object(self.object, self.daily_limit):
                return True
            if self.energy_limit and not player.enough_energy(self.energy_limit):
                return True
            if self.available_timeslots and gt.curr_timeslot not in self.available_timeslots:
                return True
            if self.available_days and gt.curr_day not in self.available_days:
                return True
            if self.days_passed and not player.completion_log_compare_date_for_item(self.days_passed[TARGET], self.days_passed[DAYS]):
                return True
            if self.need_money and player.money < self.need_money:
                return True
            if self.disabled_by_penalty and player.is_rent_penalty():
                return True
            return False
    
        @staticmethod
        def get_visible_interaction_options(interaction_options):
            interaction_option_list = []
            for interaction_option in interaction_options:
                if interaction_option.hidden:
                    continue
                if interaction_option.schedule_hidden and interaction_option.is_disabled():
                    continue
                interaction_option_list.append(interaction_option)
            return interaction_option_list
    
        @staticmethod
        def init_interaction_option(code, object):
            io_data = INTERACTIONS_OBJECT_CATALOGUE[code]
            io_object = InteractionObjectOption(object, io_data[NAME], io_data[ACTION])
            io_object.target = io_data.get(TARGET, False)
            io_object.params = io_data.get(PARAMS, False)
            io_object.daily_limit = io_data.get(DAILY_LIMIT, False)
            io_object.energy_limit = io_data.get(ENERGY_LIMIT, False)
            io_object.available_timeslots = io_data.get(TIMESLOTS, False)
            io_object.available_days = io_data.get(DAYS, False)
            io_object.days_passed = io_data.get(DAYS_PASSED, False)
            io_object.need_money = io_data.get(NEED_MONEY, False)
            io_object.hidden = io_data.get(HIDDEN, False)
            io_object.schedule_hidden = io_data.get(DISABLED_HIDDEN, False)
            io_object.disabled_by_penalty = io_data.get(DISABLED_BY_PENALTY, False)
            return io_object
