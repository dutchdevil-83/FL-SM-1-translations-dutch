init 1 python:
    DEFAULT_OBJECTS_TIMETABLES["default_studio_shower"] = {
            PRIORITY: 0,

            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle50"], "io-st_take_a_shower")],
                TIMESLOT_2: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle50"], "io-st_take_a_shower")],
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle50"], "io-st_take_a_shower")],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle50"], "io-st_take_a_shower")],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle50"], "io-st_take_a_shower")],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle50"], "io-st_take_a_shower")],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle50"], "io-st_take_a_shower")],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle50"], "io-st_take_a_shower")],
            },
        }

    DEFAULT_OBJECTS_TIMETABLES["studio_shower_SY001_perma"] = {
            ODDDAYS: {TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle50"])]},
        }
