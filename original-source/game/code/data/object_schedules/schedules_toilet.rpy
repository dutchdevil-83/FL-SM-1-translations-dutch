init 1 python:
    DEFAULT_OBJECTS_TIMETABLES["default_studio_toilet"] = {
            PRIORITY: 0,
            MONDAY:{
                TIMESLOT_5: [ScheduleSlot("Null", "Void", "", [])], 
                TIMESLOT_6: [ScheduleSlot("Null", "Void", "", [])], 
            },
            THURSDAY:{
                TIMESLOT_8: [ScheduleSlot("Null", "Void", "", [])], 
            },
            FRIDAY: {
                TIMESLOT_1: [ScheduleSlot("Null", "Void", "", [])], 
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"])] 
            },
            SUNDAY: {
                TIMESLOT_2: [ScheduleSlot("Null", "Void", "", [])], 
            },
            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"], "io-pee_in_st_toilet")],
                TIMESLOT_2: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"], "io-pee_in_st_toilet")],
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"], "io-pee_in_st_toilet")],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"], "io-pee_in_st_toilet")],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"], "io-pee_in_st_toilet")],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"], "io-pee_in_st_toilet")],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"], "io-pee_in_st_toilet")],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"], "io-pee_in_st_toilet")],
            },
        }

    DEFAULT_OBJECTS_TIMETABLES["studio_toilet_SY001_perma"] = {
            ODDDAYS: {TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["idle10"])]},
        }
