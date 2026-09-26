init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_dvh"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODDDAYS: {},
            TUESDAY: {
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], ANGRY_PEEK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["shoe01", "stand01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],

            },
            WEDNESDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
            },
            THURSDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], ANGRY_PEEK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["shoe01", "stand01"], QUICK)],
            },
            FRIDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], ANGRY_PEEK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["shoe01", "stand01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
            },
            SATURDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["stand01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], ANGRY_PEEK)],
            },
            SUNDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], ANGRY_PEEK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["shoe01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["work01"], QUICK)],
            },
        }
