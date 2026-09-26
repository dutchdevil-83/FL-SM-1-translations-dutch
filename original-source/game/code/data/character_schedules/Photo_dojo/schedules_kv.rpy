init 1 python:
    KV_DEFAULT_POSES_LIST =[
            "photo01", "sit01", "stand01", "stand02", "stand03", "stand04"
        ]

    DEFAULT_CHARACTERS_TIMETABLES["default_kv"] = {
            PRIORITY: 0,
            TUESDAY: {
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["stand01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand02"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["stand02"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand03"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand04"], QUICK)],
            },
            WEDNESDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand02"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["stand02"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand04"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],

            },
            THURSDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["stand01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand03"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],

            },
            FRIDAY:{
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand04"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand02"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["stand02"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],

            },
            SATURDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand03"], QUICK)],

            },
            }
    DEFAULT_CHARACTERS_TIMETABLES["Q-KV005"] = {
            PRIORITY: 0,
            TUESDAY: {
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
            },
            WEDNESDAY:{
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
            },
            THURSDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
            },
            FRIDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
            },
            SATURDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["kv005"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["kv005"], QUICK)],
            },
            }
    DEFAULT_CHARACTERS_TIMETABLES["Q-BG002_KV"] = {
            PRIORITY: 0,
            TUESDAY: {
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["stand01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand02"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["stand02"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand03"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand04"], QUICK)],
            },
            WEDNESDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand02"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["stand02"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand04"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand03"], QUICK)],

            },
            THURSDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["stand01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand03"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand02"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["stand02"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],

            },
            FRIDAY:{
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand04"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand02"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["stand02"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],

            },
            SATURDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand04"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["photo01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["photo01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["stand03"], QUICK)],

            },
            }
    DEFAULT_CHARACTERS_TIMETABLES["Q-BG003_KV"] = {
            PRIORITY: 0,
            TUESDAY: {
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],

            },
            WEDNESDAY:{
                TIMESLOT_5: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_6: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],

            },
            THURSDAY:{
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],

            },
            FRIDAY:{
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],

            },
            SATURDAY:{
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],

            },

            }
