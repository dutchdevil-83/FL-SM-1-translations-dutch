init -1 python:
    class ScheduleSlot:
    
        def __init__(self, location, sublocation, position, state, interactable=NOT_INTERACTABLE, default_image=False):
            self.location = location
            self.sublocation = sublocation
            self.position = position
            self.state = state
            self.interactable = interactable
            self.default_image = default_image
    
        def get_interactable(self):
            return self.interactable != NOT_INTERACTABLE
    
        def get_accurate_position(self):
            if self.interactable == NOT_INTERACTABLE:
                return False
            return True    
    
        def get_interaction_options(self, character, timeslot, day, location, sublocation, position):
            if isinstance(self.interactable, (str, list)):
                return self.interactable
            if isinstance(self.interactable, dict):
                pose = character.get_character_pose(timeslot, day, location, sublocation, position)
                return self.interactable.get(pose, NOT_INTERACTABLE)
            return NOT_INTERACTABLE
    
        def get_default_interaction_image(self, character, timeslot, day, location, sublocation, position):
            if not self.default_image:
                return False
            if isinstance(self.default_image, dict):
                pose = character.get_character_pose(timeslot, day, location, sublocation, position)
                return self.default_image.get(pose, False)
            return self.default_image

    class Schedule:
        def __init__(self, name, timetable):
            self.name = name
            self.timetable = timetable
    
        @staticmethod
        def find_schedule_in_day(timetable, timeslot, day):
            if day in timetable and timeslot in timetable[day]:
                return timetable[day][timeslot]
            else:
                matched_day = False
                matched_timeslot = False
            
                if gt.get_day_number() % 3 == 0 and THIRD_WORK_DAYS in timetable and day in WORKDAYS_LIST and (timeslot in timetable[THIRD_WORK_DAYS] or TIMESLOT_ANY in timetable[THIRD_WORK_DAYS]):
                    matched_day = THIRD_WORK_DAYS
                elif gt.get_day_number() % 2 == 0 and EVEN_WORK_DAYS in timetable and day in WORKDAYS_LIST and (timeslot in timetable[EVEN_WORK_DAYS] or TIMESLOT_ANY in timetable[EVEN_WORK_DAYS]):
                    matched_day = EVEN_WORK_DAYS
                elif gt.get_day_number() % 2 == 1 and ODD_WORK_DAYS in timetable and day in WORKDAYS_LIST and (timeslot in timetable[ODD_WORK_DAYS] or TIMESLOT_ANY in timetable[ODD_WORK_DAYS]):
                    matched_day = ODD_WORK_DAYS
                elif gt.get_day_number() % 3 == 0 and THIRDDAYS in timetable and (timeslot in timetable[THIRDDAYS] or TIMESLOT_ANY in timetable[THIRDDAYS]):
                    matched_day = THIRDDAYS
                elif gt.get_day_number() % 2 == 0 and EVENDAYS in timetable and (timeslot in timetable[EVENDAYS] or TIMESLOT_ANY in timetable[EVENDAYS]):
                    matched_day = EVENDAYS
                elif gt.get_day_number() % 2 == 1 and ODDDAYS in timetable and (timeslot in timetable[ODDDAYS] or TIMESLOT_ANY in timetable[ODDDAYS]):
                    matched_day = ODDDAYS
                elif day in WORKDAYS_LIST and WORKDAYS in timetable and (timeslot in timetable[WORKDAYS] or TIMESLOT_ANY in timetable[WORKDAYS]):
                    matched_day = WORKDAYS
                elif day in WEEKENDS_LIST and WEEKENDS in timetable and (timeslot in timetable[WEEKENDS] or TIMESLOT_ANY in timetable[WEEKENDS]):
                    matched_day = WEEKENDS
                elif ALLDAYS in timetable and (timeslot in timetable[ALLDAYS] or TIMESLOT_ANY in timetable[ALLDAYS]):
                    matched_day = ALLDAYS
                if matched_day:
                    if TIMESLOT_ANY in timetable[matched_day]:
                        matched_timeslot = TIMESLOT_ANY
                    else:
                        matched_timeslot = timeslot
                    return timetable[matched_day][matched_timeslot]
            return False
    
        @staticmethod
        def find_timeslots_for_day(timetable, day):
            if day in timetable:
                return timetable[day]
            else:
                if gt.get_day_number() % 3 == 0 and THIRD_WORK_DAYS in timetable and day in WORKDAYS_LIST:
                    return timetable[THIRD_WORK_DAYS]
                elif gt.get_day_number() % 2 == 0 and EVEN_WORK_DAYS in timetable and day in WORKDAYS_LIST:
                    return timetable[EVEN_WORK_DAYS]
                elif gt.get_day_number() % 2 == 1 and ODD_WORK_DAYS in timetable and day in WORKDAYS_LIST:
                    return timetable[ODD_WORK_DAYS]
                elif gt.get_day_number() % 3 == 0 and THIRDDAYS in timetable:
                    return timetable[THIRDDAYS]
                elif gt.get_day_number() % 2 == 0 and EVENDAYS in timetable:
                    return timetable[EVENDAYS]
                elif gt.get_day_number() % 2 == 1 and ODDDAYS in timetable:
                    return timetable[ODDDAYS]
                elif day in WORKDAYS_LIST and WORKDAYS in timetable:
                    return timetable[WORKDAYS]
                elif day in WEEKENDS_LIST and WEEKENDS in timetable:
                    return timetable[WEEKENDS]
                elif ALLDAYS in timetable:
                    return timetable[ALLDAYS]
            return False
