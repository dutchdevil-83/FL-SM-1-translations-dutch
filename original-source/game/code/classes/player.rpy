init -1 python:
    class SMPlayer:
        def __init__(self):
            self.var = "SMPlayer_"
            defaults = {
                    self.var + MONEY: STARTING_MONEY,
                    self.var + ENERGY: MAX_ENERGY_ON_START,
                    self.var + MAX_ENERGY: MAX_ENERGY_ON_START,
                    self.var + DAILY_INTERACTIONS: [],
                    self.var + CHOICES: {},
                    self.var + MAIN_STORYLINE_PROGRESS: 0,
                    self.var + STORYLINES_PROGRESS: {},
                    self.var + STORY_SUB_LINES_PROGRESS: {},
                    self.var + TRACKED_STORYLINE: [],
                    self.var + TOPICS: {},
                    self.var + DATA: {},
                    self.var + SCENES: [],
                    self.var + COMPLETION_LOG: {},
                    self.var + ACTION_LOG: [],
                    self.var + CHAT_LOG: {},
                    self.var + MONEY_LOG: [],
                    self.var + PERMA_MONEY_LOG: [],
                    self.var + MOVIE_REPLAY_HISTORY: {},
                }
            self.set_defaults(defaults)
    
        def set_defaults(self, defaults):
            for k, v in defaults.items():
                if not hasattr(renpy.store, k):
                    setattr(renpy.store, k, v)
    
        def new_week(self):
            it_worked_days = self.get_data(DATA_IT_JOB_WORKED_DAYS)
            ITController.it_job_weekly_reward(it_worked_days)
            THController.th_reset_progress()
            player.log_action("Started 'New Week'")
            charge_amount = min(self.money, RENT_WEEKLY_AMOUNT)
            if self.money < RENT_WEEKLY_AMOUNT:
                penalty_dict = self.get_data("rent_penalty") or {}
                penalty_dict[gt.get_week_number()] = True
                player.log_action("Got 'Rent Penalty'")
                self.set_data("rent_penalty", penalty_dict)
            self.spend_money(charge_amount, _("Studio rent"))
            player.log_action(f"Charged '${charge_amount}' for rent")
            renpy.play(audio.sfx_menu_notification_money1, channel="sound9")
    
        def is_rent_penalty(self):
            penalty_dict = self.get_data("rent_penalty")
            return penalty_dict and gt.get_week_number() in penalty_dict
    
    
    
        @staticmethod
        def get_sleep_time():
            return [TIMESLOT_8, TIMESLOT_1, TIMESLOT_2]
    
        @staticmethod
        def sleep():
            if gt.curr_timeslot not in player.get_sleep_time():
                return False
            player.sleep_common_function()
            gt.skip_time(3)
            QuestController.start_day_quests_resolve()
            EventController.action(ACTION_SLEEP)
            gt.after_sleep()
    
        @staticmethod
        def sleep_common_function():
            player.log_action("Went to 'Sleep'\n")
            player.reset_energy()
            player.reset_interactions()
            renovation_controller.sy_renovation_work()
            ChatController.get_waiting_chats()
    
        @staticmethod
        def skip_and_sleep(is_confirmed=False):
            if not is_confirmed and gt.curr_timeslot not in player.get_sleep_time():
                layout.yesno_screen(_("Do you want to skip time and sleep right now?"), yes=Function(player.skip_and_sleep, True), no=Return())
                return
            player.log_action("'Skipped time'")
            if gt.curr_timeslot not in player.get_sleep_time():
                gt.update(21, 0, 0)
            player.sleep()
    
    
    
        @property
        def money(self):
            if vn_mode:
                return 99999
            return getattr(renpy.store, self.var + MONEY)
    
        def add_money(self, amount, reason=None, notify=False):
            new_value = self.money + amount
            if notify and not vn_mode:
                screen_uuid = get_uuid()
                Show("notification_screen", msg_type = PAYMENT, message = _("You just got ${}").format(amount) if notify is True else notify, tag = screen_uuid, _tag = screen_uuid)()
            renpy.play(audio.sfx_menu_notification_money1, channel="sound9")
            player.add_to_money_log(amount, reason)
            player.log_action(f"Earned money '${amount}'")
            setattr(renpy.store, self.var + MONEY, new_value)
            EventController.action(MONEY_RECEIVED, amount)
    
        def spend_money(self, amount, reason=None, notify=False):
            new_value = self.money - amount
            if notify and not vn_mode:
                screen_uuid = get_uuid()
                Show("notification_screen", msg_type = PAYMENT, message = _("You spent ${}").format(add_value) if notify is True else notify, tag = screen_uuid, _tag = screen_uuid)()
            setattr(renpy.store, self.var + MONEY, new_value)
            player.add_to_money_log(-amount, reason)
            player.log_action(f"Spent money '${amount}'")
            EventController.action(MONEY_SPENT, amount)
    
        def has_enough_money(self, amount):
            if 0 < amount <= self.money:
                return True
            return False
    
        def get_money_log(self):
            return getattr(renpy.store, self.var + MONEY_LOG)
    
        def get_concentrated_money_log(self):
            log = self.get_money_log().copy()
            concentrated_log = {}
            for entry in log:
                reason = entry[REASON]
                amount = entry[AMOUNT]
                if reason in concentrated_log:
                    concentrated_log[reason] += amount
                else:
                    concentrated_log[reason] = amount
            return [{REASON: reason, AMOUNT: amount} for reason, amount in concentrated_log.items()]
    
        def add_to_money_log(self, amount, reason=None):
            log = self.get_money_log().copy()
            log.append({AMOUNT: amount, REASON: reason})
            setattr(renpy.store, self.var + MONEY_LOG, log)
    
        def reset_money_log(self):
            log = self.get_money_log().copy()
            perma_log = self.get_perma_money_log().copy()
            perma_log.extend(log)
            setattr(renpy.store, self.var + PERMA_MONEY_LOG, perma_log)
            setattr(renpy.store, self.var + MONEY_LOG, [])
    
        def get_perma_money_log(self):
            return getattr(renpy.store, self.var + PERMA_MONEY_LOG)
    
    
    
        @property
        def energy(self):
            if vn_mode:
                return 99999
            return getattr(renpy.store, self.var + ENERGY)
    
        @property
        def max_energy(self):
            return getattr(renpy.store, self.var + MAX_ENERGY)
    
        @property
        def get_energy_percent(self):
            return round((self.energy * 100) // self.max_energy)
    
        def enough_energy(self, energy):
            return self.energy >= energy
    
        def consume_energy(self, energy):
            setattr(renpy.store, self.var + ENERGY, max(self.energy - energy, 0))
    
        def add_energy(self, energy):
            setattr(renpy.store, self.var + ENERGY, min(self.energy + energy, self.max_energy))
    
        def reset_energy(self):
            setattr(renpy.store, self.var + ENERGY, self.max_energy - LATE_SLEEP_ENERGY_PENALTY if gt.curr_timeslot == TIMESLOT_2 else self.max_energy)
    
        def set_max_energy(self, maxenergy):
            setattr(renpy.store, self.var + MAX_ENERGY, maxenergy)
    
    
    
        def interact(self, char):
            interactions = self.get_daily_interactions()
            interactions.append(char.codename + "_" + QUICK)
            setattr(renpy.store, self.var + DAILY_INTERACTIONS, interactions)
    
        def consume_interaction(self, code):
            interactions = self.get_daily_interactions()
            interactions.append(code)
            setattr(renpy.store, self.var + DAILY_INTERACTIONS, interactions)
    
        def get_daily_interactions(self):
            value = getattr(renpy.store, self.var + DAILY_INTERACTIONS).copy()
            return value if isinstance(value, list) else []
    
        def has_interacted(self, char, interaction=QUICK):
            return bool(self.get_daily_interactions().count(char.codename + "_" + interaction))
    
        def has_interacted_object(self, object, interaction=QUICK):
            return bool(self.get_daily_interactions().count(object.codename + "_" + interaction))
    
        def has_interacted_location(self, location, interaction=QUICK):
            return bool(self.get_daily_interactions().count(location.get_codename() + "_" + interaction))
    
        def reset_interactions(self):
            setattr(renpy.store, self.var + DAILY_INTERACTIONS, [])
    
    
    
        def has_choosen(self, name):
            return hasattr(renpy.store, self.var + CHOICES + name)
    
        def get_choice(self, name):
            sanitized_var = sanitize_variable_name(name)
            return getattr(renpy.store, self.var + CHOICES + sanitized_var, False)
    
        def set_choice(self, name, val=True):
            sanitized_var = sanitize_variable_name(name)
            player.log_action(f"Player chose '{sanitized_var}' as '{val}'")
            GameAnalytics.add_to_event_queue(GameAnalytics.design_event(f"choice:{sanitized_var}:{val}"))
            setattr(renpy.store, self.var + CHOICES + sanitized_var, val)
    
        def get_completion_log(self):
            return getattr(renpy.store, self.var + COMPLETION_LOG)
    
        def completion_log_add_item_date(self, itemname, date=False):
            date = date or gt.get_day_number()
            log = self.get_completion_log().copy()
            sanitized_itemname = sanitize_variable_name(itemname)
            count = sum(1 for key in log if key.endswith(sanitized_itemname))
            unique_key = f"{count}_{sanitized_itemname}" if count > 0 else sanitized_itemname
            log[unique_key] = {DATE: date}
            GameAnalytics.add_to_event_queue(GameAnalytics.design_event(f"completed:scene:{sanitized_itemname}", value=date))
            player.log_action(f"Completed '{sanitized_itemname}' on day '{date}'")
            setattr(renpy.store, self.var + COMPLETION_LOG, log)
    
        def completion_log_get_items(self, itemname):
            sanitized_itemname = sanitize_variable_name(itemname)
            log = self.get_completion_log().copy()
            return [entry for key, entry in log.items() if key.endswith(sanitized_itemname)]
    
        def completion_log_get_date(self, itemname):
            sanitized_itemname = sanitize_variable_name(itemname)
            log = self.get_completion_log().copy()
            relevant_entries = [entry[DATE] for key, entry in log.items() if key.endswith(sanitized_itemname)]
            if not relevant_entries:
                return False
            latest_date = max(relevant_entries)
            return latest_date
    
        def completion_log_compare_date_for_item(self, itemname, days_passed=1):
            sanitized_itemname = sanitize_variable_name(itemname)
            item_date = self.completion_log_get_date(sanitized_itemname)
            if not item_date:
                return False
            return (item_date + days_passed) <= gt.get_day_number()
    
        def has_played_scene(self, scene_name):
            sanitized_name = sanitize_variable_name(scene_name)
            log = self.get_completion_log().copy()
            return bool(log.get(sanitized_name, False))
    
    
    
        def get_storylines_progress(self):
            return getattr(renpy.store, self.var + STORYLINES_PROGRESS)
    
        def get_story_sublines_progress(self):
            return getattr(renpy.store, self.var + STORY_SUB_LINES_PROGRESS)
    
        def get_story_subline(self, storyline_name):
            all_story_sublines = self.get_story_sublines_progress()
            if storyline_name in all_story_sublines:
                return all_story_sublines[storyline_name]
            return 0
    
        def set_story_subline(self, storyline_name, value = 0):
            all_sublines = self.get_story_sublines_progress()
            all_sublines[storyline_name] = value
            setattr(renpy.store, self.var + STORY_SUB_LINES_PROGRESS, all_sublines)
    
        def create_storyline(self, storyline_name, step=0):
            all_story_lines = self.get_storylines_progress()
            if storyline_name not in all_story_lines:
                all_story_lines[storyline_name] = step
                player.log_action(f"Created storyline '{storyline_name}' and set progress to '{step}'")
                setattr(renpy.store, self.var + STORYLINES_PROGRESS, all_story_lines)
    
        def get_storyline(self, storyline_name):
            return self.get_storylines_progress().get(storyline_name, False)
    
        def progress_storyline(self, storyline_name, steps=1):
            all_story_lines = self.get_storylines_progress()
            if storyline_name not in all_story_lines:
                return
        
            quest_line = sm_quest_lines_list[storyline_name][QUEST_LINE]
            step = 1 if steps > 0 else -1
            for _ in range(0, abs(steps)):
                current_item = quest_line[all_story_lines[storyline_name]]
                if isinstance(current_item, list):
                    sub_progress = self.get_story_subline(storyline_name)
                    sub_length = len(current_item)
                    new_sub_progress = sub_progress + step
                    if new_sub_progress < 0:
                        all_story_lines[storyline_name] += -1
                        prev_item = quest_line[all_story_lines[storyline_name]]
                        if isinstance(prev_item, list):
                            self.set_story_subline(storyline_name, len(prev_item) - 1)
                        else:
                            self.set_story_subline(storyline_name, 0)
                    elif new_sub_progress > sub_length - 1:
                        self.set_story_subline(storyline_name, 0)
                        all_story_lines[storyline_name] += 1
                    else:
                        self.set_story_subline(storyline_name, new_sub_progress)
                else:
                    all_story_lines[storyline_name] += step
                    if steps < 0: 
                        next_item = quest_line[all_story_lines[storyline_name]]
                        if isinstance(next_item, list):
                            self.set_story_subline(storyline_name, len(next_item) - 1)
                        else:
                            self.set_story_subline(storyline_name, 0)
        
            setattr(renpy.store, self.var + STORYLINES_PROGRESS, all_story_lines)
    
    
        def untrack_storyline(self, storyline_name, is_automatic=False):
            tracked_quests = self.get_tracked_storylines()
            if storyline_name in tracked_quests:
                tracked_quests.remove(storyline_name)
                print_verbose(f"QuestTracker - Untracked Quest \"{storyline_name}\"")
                setattr(renpy.store, self.var + TRACKED_STORYLINE, tracked_quests)
            if not tracked_quests and is_automatic:
                StoryController.track_unfinished_quests()
    
        def track_storyline(self, storyline_name):
            all_story_lines = self.get_storylines_progress()
            tracked_quests = self.get_tracked_storylines()
            if storyline_name in all_story_lines:
                if storyline_name in tracked_quests:
                    tracked_quests.remove(storyline_name)
                tracked_quests.insert(0, storyline_name)
                if len(tracked_quests) > 3:
                    print_verbose(f"QuestTracker - Removed last index \"{tracked_quests[3]}\" because we are adding \"{storyline_name}\"")
                    tracked_quests.pop(3)
                setattr(renpy.store, self.var + TRACKED_STORYLINE, tracked_quests)
    
        def get_tracked_storylines(self):
            tracked_storylines = getattr(renpy.store, self.var + TRACKED_STORYLINE).copy()
            if not isinstance(tracked_storylines, list):
                tracked_storylines = [tracked_storylines]
            return tracked_storylines
    
        def is_storyline_item_finished(self, storyline_name, item):
            sanitized_name = sanitize_variable_name(storyline_name)
            storyline = sm_quest_lines_list[sanitized_name][QUEST_LINE][:self.get_storyline(sanitized_name)]
            for story_item in storyline:
                if story_item == item or (isinstance(story_item, list) and item in story_item):
                    return True
            return False
    
        def get_storyline_progress_percent(self, storyline_name):
            if not storyline_name:
                return 0
            sanitized_name = sanitize_variable_name(storyline_name)
            storyline = sm_quest_lines_list[sanitized_name][QUEST_LINE]
            list_of_quests = []
            for quest in storyline:
                if isinstance(quest, list):
                    list_of_quests.append(quest)
                elif quest in ["pause", "end"]:
                    list_of_quests.append(quest)
                elif quest.startswith("s"):
                    list_of_quests.append(quest)
                elif CURRENT_QUEST_LINE_END not in sm_quest_list[quest]:
                    list_of_quests.append(quest)
            return round((self.get_storyline(sanitized_name) * 100) // len(list_of_quests))
    
    
    
        def discover_map_location(self, location):
            LocationController.get_map_location(location).get_location().discover()
            renpy.notify(_("You just discovered new location on the map"))
            renpy.play(audio.sfx_menu_notification2, channel="sound9")
            EventController.action(MAP_LOCATION_DISCOVERED, location)
    
        def travel(self, location):
            gt.add(0, TRAVEL_TIME_MINUTES, 0)
    
    
    
        def get_topic(self, topic):
            if vn_mode:
                return 99999
            return getattr(renpy.store, self.var + TOPICS).get(topic, 0)
    
        def add_topic(self, topic, value=1):
            topics_dict = getattr(renpy.store, self.var + TOPICS)
            new_value = topics_dict.get(topic, 0) + value
            topics_dict[topic] = new_value
            setattr(renpy.store, self.var + TOPICS, topics_dict)
            if not vn_mode:
                renpy.notify(_("You just improved in topic") + " " + topic)
            renpy.play(audio.sfx_menu_notification2, channel="sound9")
            EventController.action(TOPIC_REACHED_VALUE, topic, new_value)
    
    
    
        def get_data(self, key):
            return getattr(renpy.store, self.var + DATA).get(key, False)
    
        def set_data(self, key, value=True):
            data_dict = getattr(renpy.store, self.var + DATA)
            data_dict[key] = value
            setattr(renpy.store, self.var + DATA, data_dict)
            EventController.action(PLAYER_DATA_UPDATED, key, value)
    
        def increment_data(self, key, increment=1):
            current_value = self.get_data(key) or 0
            self.set_data(key, current_value + increment)
            return current_value + increment
    
    
    
        def get_action_log(self):
            action_log_var = self.var + ACTION_LOG
            if not hasattr(renpy.store, action_log_var):
                setattr(renpy.store, action_log_var, [])
            return getattr(renpy.store, action_log_var)
    
        def log_action(self, action):
            log = self.get_action_log()
            log.append(action)
            if len(log) > 3000:
                log = log[-3000:]
            setattr(renpy.store, self.var + ACTION_LOG, log)
    
    
    
        def get_chat_log(self):
            return getattr(renpy.store, self.var + CHAT_LOG)
    
        def add_chat_to_log(self, chat_name, uuid, chat_message, date=False):
            date = date or gt.get_day_number()
            log = getattr(renpy.store, self.var + CHAT_LOG).copy()
            log[f"{chat_name}_{uuid}_{chat_message}"] = {DATE: date}
        
            setattr(renpy.store, self.var + CHAT_LOG, log)
    
    
    
        def get_movie_replay_history(self):
            return getattr(renpy.store, self.var + MOVIE_REPLAY_HISTORY)
    
        def add_movie_replay_history(self, movie_code):
            history = self.get_movie_replay_history().copy()
            if movie_code not in history:
                history[movie_code] = 0
            history[movie_code] += 1
            setattr(renpy.store, self.var + MOVIE_REPLAY_HISTORY, history)
            player.log_action(f"Added movie replay history for '{movie_code}' with count {history[movie_code]}")
