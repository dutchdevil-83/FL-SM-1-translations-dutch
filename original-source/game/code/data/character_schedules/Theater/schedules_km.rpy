init 1 python:
    KM_CUSTOM_POSES_LIST = [
            "shower01"
        ]

    DEFAULT_CHARACTERS_TIMETABLES["default_km"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODDDAYS: {},
            TUESDAY: {
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], ANGRY_PEEK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_TO_STAGE, ["phone01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_2, LTH_DRESSINGROOM_2, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["perform01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["perform01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_2, LTH_DRESSINGROOM_2, ["phone01"], QUICK)],
            },
            WEDNESDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_TO_STAGE, ["phone01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["stand01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_2, LTH_DRESSINGROOM_2, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["perform01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["perform01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_2, LTH_DRESSINGROOM_2, ["phone01"], QUICK)],
            },
            THURSDAY:{

            },
            FRIDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["stand01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["sit01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_TO_STAGE, ["phone01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_2, LTH_DRESSINGROOM_2, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["perform01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["perform01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], ANGRY_PEEK)],
            },
            SATURDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["stand01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["sit01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_TO_STAGE, ["phone01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_2, LTH_DRESSINGROOM_2, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["perform01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["perform01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_2, LTH_DRESSINGROOM_2, ["phone01"], QUICK)],
            },
            SUNDAY:{
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_2, LTH_DRESSINGROOM_2, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["perform01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW, ["perform01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_2, LTH_DRESSINGROOM_2, ["phone01"], QUICK)],
            },
        }
    DEFAULT_CHARACTERS_TIMETABLES["shower_after_km004"] = {
            PRIORITY: 0,
            FRIDAY:{
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
            },
        }
