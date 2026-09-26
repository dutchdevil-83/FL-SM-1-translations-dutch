init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_sb"] = {
            PRIORITY: 0,

            TUESDAY: {
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER, ["box01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["smoke01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["smoke01"], ["io-rehearsal_at_th", QUICK])],
            },
            WEDNESDAY:{
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER, ["box01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER, ["box01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["smoke01"], ["io-rehearsal_at_th", QUICK])],
            },
            THURSDAY:{
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["smoke01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER, ["box01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER, ["box01"], QUICK)],
            },
            FRIDAY:{
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["smoke01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER, ["box01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["smoke01"], ["io-rehearsal_at_th", QUICK])],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER, ["box01"], QUICK)],
            },
            SATURDAY:{
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER, ["box01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER, ["box01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE, ["smoke01"], QUICK)],
            },
            EVENDAYS : {
                TIMESLOT_4:[ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_3, ["stand01"], QUICK)],
                TIMESLOT_8:[ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_CORRIDOR, ["smoke01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["smoke01"])],
            },
            ODDDAYS: {
                TIMESLOT_4:[ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_CORRIDOR, ["smoke01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["smoke01"])],
                TIMESLOT_8:[ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_3, ["stand01"], QUICK)],
            },
        }
