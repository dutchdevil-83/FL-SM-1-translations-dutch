init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_sj"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODDDAYS: {},
            TUESDAY: {
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], ANGRY_PEEK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_2, ["look01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["look01"])],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],

            },
            WEDNESDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_2, ["look01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["look01"])],
            },
            THURSDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_2, ["look01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["look01"])],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], ANGRY_PEEK)],
            },
            FRIDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], ANGRY_PEEK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_2, ["look01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["look01"])],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
            },
            SATURDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_ENTR, ["stand01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["sit01"], QUICK)],
            },
        }
