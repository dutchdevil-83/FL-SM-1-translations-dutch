init -1 python:
    import datetime

    class SMGameTime:
        def __init__(self, dt):
            self._start_dt = datetime.datetime.strptime(dt, "%d %b %a %H %M %S")
            self._dt = self._start_dt
    
        def __repr__(self):
            return _strftime("%d %b %a %I:%M:%S %p", self._dt.timetuple())
    
        def update(self, hr, mn, sc):
            self._dt = self._dt.replace(hour=hr, minute=mn, second=sc, microsecond=0)
    
        def add(self, hr, mn, sc):
            if vn_mode:
                return
            self._dt += datetime.timedelta(hours=hr, minutes=mn, seconds=sc)
            if 4 <= self.curr_hour < 6:
                self.force_sleep()
    
        def force_sleep(self):
            global curr_location, curr_sublocation, curr_position
            curr_location = STUDIO
            curr_sublocation = DEFAULT_SUBLOCATION
            if player.is_storyline_item_finished(MS, "sm1ms020"):
                curr_position = SD_UPSTAIRS_BED
            else:
                curr_position = SD_MATTRESS
            player.log_action("Player forced to sleep\n")
            player.sleep()
    
        def skip_time(self, times=1):
            next_hour = (self._dt.hour // 3 + times) * 3
            hours_to_next = next_hour - self._dt.hour
            self._dt += datetime.timedelta(hours=hours_to_next)
            self._dt = self._dt.replace(minute=0, second=0)
            player.log_action("Skipped time to next timeslot")
    
        def after_sleep(self):
            if self.curr_day == SUNDAY:
                self.new_week()
                if player.is_rent_penalty():
                    renpy.jump("sleep_transition_with_penalty")
                    return
            renpy.jump("sleep_transition")
    
        def get_week_number(self):
            delta = self._dt.date() - self._start_dt.date()
            return delta.days // 7 + 1
    
        def get_day_number(self):
            delta = self._dt.date() - self._start_dt.date()
            return delta.days + 1
    
        def new_week(self):
            player.new_week()
    
        def skip_time_button_action(self):
            self.skip_time()
            if renpy.get_screen("city_map"):
                LocationController.enter()
            else:
                renpy.jump("location_reenter")
    
        @property
        def get_random_seed(self):
            return f"{self.get_day_number()}_{self.curr_timeslot}_{random_seed}"
    
        @property
        def get_weekly_random_seed(self):
            return f"{self.get_week_number()}_{random_seed}"
    
        @property
        def curr_day(self):
            return _strftime("%A", self._dt.timetuple()).split("}")[-1]
    
        @property
        def curr_weekday(self):
            return self._dt.weekday()
    
        @property
        def next_day(self):
            return (self._dt + datetime.timedelta(days=1)).strftime("%A").split("}")[-1]
    
        @property
        def curr_day_short(self):
            return _strftime("%a", self._dt.timetuple()).split("}")[-1]
    
        @property
        def minigame_timer(self):
            return self._dt.time().strftime("%M:%S")
    
        @property
        def minigame_length(self):
            t = self._dt.time()
            return t.hour * 3600 + t.minute * 60 + t.second
    
        @property
        def curr_time(self):
            return self._dt.time().strftime("%I:%M %p")
    
        @property
        def curr_hour(self):
            return self._dt.hour
    
        @property
        def curr_minute(self):
            return self._dt.minute
    
        @property
        def curr_timeslot(self):
            return [k[-1] for k in (
                    (0,  1,  2,  TIMESLOT_1),
                    (3,  4,  5,  TIMESLOT_2),
                    (6,  7,  8,  TIMESLOT_3),
                    (9,  10, 11, TIMESLOT_4),
                    (12, 13, 14, TIMESLOT_5),
                    (15, 16, 17, TIMESLOT_6),
                    (18, 19, 20, TIMESLOT_7),
                    (21, 22, 23, TIMESLOT_8)
                    ) if self._dt.hour in k][0]
    
        @property
        def timeslot_after_travel(self):
            adjusted_dt = self._dt + datetime.timedelta(minutes=TRAVEL_TIME_MINUTES)
            return [k[-1] for k in (
                    (0,  1,  2,  TIMESLOT_1),
                    (3,  4,  5,  TIMESLOT_2),
                    (6,  7,  8,  TIMESLOT_3),
                    (9,  10, 11, TIMESLOT_4),
                    (12, 13, 14, TIMESLOT_5),
                    (15, 16, 17, TIMESLOT_6),
                    (18, 19, 20, TIMESLOT_7),
                    (21, 22, 23, TIMESLOT_8)
                    ) if adjusted_dt.hour in k][0]
    
        @property
        def curr_time_of_day(self):
            return [k[-1] for k in (
                    (TIMESLOT_1, TIMESLOT_2, TIMESLOT_8, IS_NIGHT),
                    (TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, IS_DAY)
                    ) if self.curr_timeslot in k][0]
    
        @property
        def curr_display_time(self):
            return [k[-1] for k in (
                    (TIMESLOT_1, TIMESLOT_2, DISPLAY_TIME_1),
                    (TIMESLOT_3, TIMESLOT_4, DISPLAY_TIME_3),
                    (TIMESLOT_5,             DISPLAY_TIME_5),
                    (TIMESLOT_7,             DISPLAY_TIME_7),
                    (TIMESLOT_8,             DISPLAY_TIME_8)
                    ) if self.curr_timeslot in k][0]
    
        @property
        def curr_display_time_short(self):
            return [k[-1] for k in (
                    (TIMESLOT_1, TIMESLOT_2, T1),
                    (TIMESLOT_3, TIMESLOT_4, T3),
                    (TIMESLOT_5, TIMESLOT_6, T5),
                    (TIMESLOT_7,             T7),
                    (TIMESLOT_8,             T8)
                    ) if self.curr_timeslot in k][0]
    
        @staticmethod
        def get_week_day_number(day):
            return ALLDAYS_LIST.index(day)
    
        @staticmethod
        def get_timeslot_number(timeslot):
            return ALL_TIMESLOTS.index(timeslot) + 1
    
        @staticmethod
        def get_timeslot_number_in_day_order(timeslot):
            return ALL_TIMESLOTS_DAY_ORDER.index(timeslot) + 1
    
        @staticmethod
        def check_list_for_location(list, location):
            return location in list
    
        @staticmethod
        def check_list_for_day(list, day):
            return day in list or (
                    (day in WORKDAYS_LIST and WORKDAYS in list) or
                    (day in WEEKENDS_LIST and WEEKENDS in list) or
                    (day in EVENDAYS_LIST and EVENDAYS in list) or
                    (day in ODDDAYS_LIST and ODDDAYS in list) or
                    (ALLDAYS in list)
                    )
    
        @staticmethod
        def get_wrong_time_msg(timeslot_list):
            if len(timeslot_list) == 1:
                if timeslot_list[0] in [TIMESLOT_3, TIMESLOT_4, TIMESLOT_6, TIMESLOT_7]:
                    return _("Wrong time. Available in the {}").format(timeslot_list[0])
                else:
                    return _("Wrong time. Available at {}").format(timeslot_list[0])
        
            curr_slot_num = gt.get_timeslot_number_in_day_order(gt.curr_timeslot)
            earliest_timeslot = min(timeslot_list, key=gt.get_timeslot_number_in_day_order)
            all_earlier = all(curr_slot_num < gt.get_timeslot_number_in_day_order(ts) for ts in timeslot_list)
            all_later = all(curr_slot_num > gt.get_timeslot_number_in_day_order(ts) for ts in timeslot_list)
        
            if all_earlier:
                return _("Too early. Available from {}").format(earliest_timeslot)
            elif all_later:
                return _("Too late for the day. Available from {}").format(earliest_timeslot)
            else:
                return _("Wrong time.")
    
        @staticmethod
        def check_list_for_timeslot(list, timeslot):
            return timeslot in list or ANYTIME in list
    
        @staticmethod
        def calculate_rotation(hour, minute):
            return 0.5 * ((hour % 12) * 60 + minute)
    
        def range_includes_sunday(self, start_dt, days):
            current_day = _strftime("%A", start_dt.timetuple()).split("}")[-1]
            if current_day == SUNDAY:
                return False
            for _ in range(days):
                start_dt += datetime.timedelta(days=1)
                current_day = _strftime("%A", start_dt.timetuple()).split("}")[-1]
                if current_day == SUNDAY:
                    return True
            return False
