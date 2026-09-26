init -1 python:
    class InteractionCharacterOption:
        def __init__(self, character, name, action):
            self.character = character
            self.name = name
            self.action = action
            self.target = False
            self.choice_name = False
            self.params = False
            self.daily_limit = False
            self.energy_limit = False
            self.available_timeslots = False
            self.available_days = False
            self.available_locations = False
            self.available_sublocations = False
            self.available_positions = False
            self.hidden = False
            self.hidden_by_condition = False
            self.hidden_by_pose = False
            self.schedule_hidden = False
            self.disabled_by_penalty = False
            self.disabled_by_pose = False
            self.disabled_by_condition = False
            self.disabled_by_relationship_points = False
            self.days_passed = False
            self.need_money = False
    
        def click(self):
            player.log_action(f"Clicked on character interaction '{self.name}'")
            action = self.get_action()
            if isinstance(action, list):
                for action_item in action:
                    self.process_action(action_item)
            else:
                self.process_action(action)
    
        def process_action(self, action):
            if action == JUMP:
                self.consume_player_interaction_limit()
                renpy.jump(self.target)
            elif action == CALL:
                self.consume_player_interaction_limit()
            
                renpy.call(self.target)
            elif action == FUNCTION:
                self.consume_player_interaction_limit()
                self.target(self.params) if self.params else self.target()
            elif action == OPEN_SCREEN:
                Show(self.target)()
            elif action == QUICK:
                self.character.interact()
            elif action == SET_CHOICE:
                player.set_choice(self.choice_name, True)
            elif action == PROGRESS_STORY:
                self.consume_player_interaction_limit()
                StoryController.advance_storyline_by_interaction_option(self.target)
            elif action == ONRAMP:
                player.set_choice(self.target, False)
    
        def consume_player_interaction_limit(self):
            if self.daily_limit:
                player.consume_interaction(f"{self.character.codename}_{self.daily_limit}")
    
        def get_name(self):
            if self.disabled_by_condition and globals().get(self.disabled_by_condition) and globals().get(self.disabled_by_condition)(self) is not False:
                return _("{name} ({reason})").format(name=self.name, reason=globals().get(self.disabled_by_condition)(self))
            if self.disabled_by_penalty and player.is_rent_penalty():
                return _("{name} (disabled on penalty week)").format(name=self.name)
            if self.disabled_by_relationship_points:
                for char, points in self.disabled_by_relationship_points.items():
                    if CharacterController.get_character(char).points < points:
                        return _("{name} (You have {current_points}/{required_points} Relationship Points with {character_name})").format(
                                name=self.name,
                                current_points=CharacterController.get_character(char).points,
                                required_points=points,
                                character_name=CharacterController.get_character(char).name
                            )
            if self.daily_limit and player.has_interacted(self.character, self.daily_limit):
                return _("{name} (done today)").format(name=self.name)
            if self.available_days and gt.curr_day not in self.available_days:
                return _("{name} (wrong day)").format(name=self.name)
            if self.days_passed:
                if isinstance(self.days_passed, list):
                    for days_data in self.days_passed:
                        if player.completion_log_get_date(days_data[TARGET]) == False:
                            return _("{name} (You need to progress {storyline_name} first)").format(name=self.name, storyline_name=QuestController.get_storyline_name_by_quest(days_data[TARGET]))
                        elif not player.completion_log_compare_date_for_item(days_data[TARGET], days_data[DAYS]):
                            return _("{name} (not available today)").format(name=self.name)
                else:
                    if player.completion_log_get_date(self.days_passed[TARGET]) == False:
                        return _("{name} (You need to progress {storyline_name} first)").format(name=self.name, storyline_name=QuestController.get_storyline_name_by_quest(self.days_passed[TARGET]))
                    elif not player.completion_log_compare_date_for_item(self.days_passed[TARGET], self.days_passed[DAYS]):
                        return _("{name} (not available today)").format(name=self.name)
            if self.need_money and player.money < self.need_money:
                return _("{name} (You need to have ${amount})").format(name=self.name, amount=self.need_money)
            if self.energy_limit and not player.enough_energy(self.energy_limit):
                return _("{name} (not enough energy)").format(name=self.name)
            if self.available_timeslots and gt.curr_timeslot not in self.available_timeslots:
                wrong_time_msg = gt.get_wrong_time_msg(self.available_timeslots)
                return _("{name} ({wrong_time_msg})").format(name=self.name, wrong_time_msg=wrong_time_msg)
            if (self.available_locations and curr_location not in self.available_locations) or (self.available_sublocations and curr_sublocation not in self.available_sublocations) or (self.available_positions and curr_position not in self.available_positions):
                return _("{name} (wrong location)").format(name=self.name)
            if self.disabled_by_pose and self.character.get_character_pose(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position) in self.disabled_by_pose:
                return _("{name} (not available now)").format(name=self.name)
            return self.name
    
        def get_action(self):
            return DISABLED_ACTION if self.is_disabled() else self.action
    
        def is_disabled(self):
            if self.daily_limit and player.has_interacted(self.character, self.daily_limit):
                return True
            if self.energy_limit and not player.enough_energy(self.energy_limit):
                return True
            if self.disabled_by_relationship_points:
                for char, points in self.disabled_by_relationship_points.items():
                    if CharacterController.get_character(char).points < points:
                        return True
            if self.available_timeslots and gt.curr_timeslot not in self.available_timeslots:
                return True
            if self.available_days and gt.curr_day not in self.available_days:
                return True
            if self.available_locations and curr_location not in self.available_locations:
                return True
            if self.available_sublocations and curr_sublocation not in self.available_sublocations:
                return True
            if self.available_positions and curr_position not in self.available_positions:
                return True
            if self.days_passed:
                if isinstance(self.days_passed, list):
                    for days_data in self.days_passed:
                        if not player.completion_log_compare_date_for_item(days_data[TARGET], days_data[DAYS]):
                            return True
                else:
                    if not player.completion_log_compare_date_for_item(self.days_passed[TARGET], self.days_passed[DAYS]):
                        return True
            if self.need_money and player.money < self.need_money:
                return True
            if self.disabled_by_penalty and player.is_rent_penalty():
                return True
            if self.disabled_by_pose and self.character.get_character_pose(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position) in self.disabled_by_pose:
                return True
            if self.disabled_by_condition and globals().get(self.disabled_by_condition) and globals().get(self.disabled_by_condition)(self) is not False:
                return True
            return False
    
        def is_visible(self):
            if self.hidden:
                return False
            if self.schedule_hidden and self.is_disabled():
                return False
            if self.hidden_by_pose and self.character.get_character_pose(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position) in self.hidden_by_pose:
                return False
            if self.hidden_by_condition and globals().get(self.hidden_by_condition)(self):
                return False
            return True
    
        @staticmethod
        def get_visible_interaction_options(interaction_options):
            interaction_option_list = []
            for interaction_option in interaction_options:
                if not interaction_option.is_visible():
                    continue
                interaction_option_list.append(interaction_option)
            return interaction_option_list
    
        @staticmethod
        def replace_placeholder_character(string, character):
            if isinstance(string, str) and "##interaction_character.codename##" in string:
                string = string.replace("##interaction_character.codename##", f"{character.codename}")
            return string
    
        @staticmethod
        def init_interaction_option(code, character):
            io_data = INTERACTIONS_CHARACTER_CATALOGUE[code]
            io_object = InteractionCharacterOption(character, io_data[NAME], io_data[ACTION])
        
            io_object.target = InteractionCharacterOption.replace_placeholder_character(io_data.get(TARGET, False), character)
            io_object.choice_name = io_data.get(CHOICE_NAME, False)
            io_object.params = io_data.get(PARAMS, False)
        
            io_object.daily_limit = InteractionCharacterOption.replace_placeholder_character(io_data.get(DAILY_LIMIT, False), character)
            io_object.energy_limit = io_data.get(ENERGY_LIMIT, False)
            io_object.available_timeslots = io_data.get(TIMESLOTS, False)
            io_object.available_days = io_data.get(DAYS, False)
            io_object.available_locations = io_data.get(LOCATION, False)
            io_object.available_sublocations = io_data.get(SUBLOCATION, False)
            io_object.available_positions = io_data.get(POSITION, False)
            io_object.days_passed = io_data.get(DAYS_PASSED, False)
            io_object.need_money = io_data.get(NEED_MONEY, False)
            io_object.hidden = io_data.get(HIDDEN, False)
            io_object.hidden_by_condition = io_data.get(HIDDEN_BY_CONDITION, False)
            io_object.hidden_by_pose = io_data.get(HIDDEN_BY_POSE, False)
            io_object.schedule_hidden = io_data.get(DISABLED_HIDDEN, False)
            io_object.disabled_by_penalty = io_data.get(DISABLED_BY_PENALTY, False)
            io_object.disabled_by_pose = io_data.get(DISABLED_BY_POSE, False)
            io_object.disabled_by_condition = io_data.get(DISABLED_BY_CONDITION, False)
            io_object.disabled_by_relationship_points = io_data.get(DISABLED_BY_RP, False)
            return io_object
