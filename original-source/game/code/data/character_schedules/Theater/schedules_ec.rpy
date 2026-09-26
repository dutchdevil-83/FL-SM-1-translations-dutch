init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_ec"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODDDAYS: {},
            TUESDAY: {
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["couch01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], ANGRY_PEEK)],

            },
            WEDNESDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["couch01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["couch01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], ANGRY_PEEK)],
            },
            THURSDAY:{
                TIMESLOT_4: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["daydream01"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["daydream01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["daydream01"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["daydream01"], QUICK)],
            },
            FRIDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], ANGRY_PEEK)],
                TIMESLOT_5: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["daydream01"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["daydream01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["couch01"], QUICK)],
            },
            SATURDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["couch01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], ANGRY_PEEK)],
            },
            SUNDAY:{
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["couch01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["couch01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["daydream01"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["daydream01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["couch01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], ANGRY_PEEK)],
            },
        }
    DEFAULT_CHARACTERS_TIMETABLES["ec_q_ag003"] = {
            PRIORITY: 0,
            THURSDAY:{
                TIMESLOT_3: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["daydream01"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["daydream01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_OFFICE, LTH_DIRECTORS_OFFICE, ["couch01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_MIDDLE, ["shower01"], ANGRY_PEEK)],
            },
            FRIDAY:{
                TIMESLOT_3: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["daydream01"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["daydream01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot("Void", "b", "c", [])],
            },
            ODDDAYS: {},
            ALLDAYS: {},
        }
