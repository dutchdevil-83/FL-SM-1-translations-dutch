init 1 python:
    VS_CUSTOM_POSES_LIST = [
            "shower01",
        ]

    DEFAULT_CHARACTERS_TIMETABLES["default_vs"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODDDAYS: {},
            TUESDAY: {
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["read01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],

            },
            WEDNESDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["read01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
            },
            THURSDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["sit01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["reaching01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["read01"], QUICK)],
            },
            FRIDAY:{
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["sit01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["read01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
            },
            SATURDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["read01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], QUICK)],
            },
            SUNDAY:{
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["read01"], QUICK)],
            },
        }
