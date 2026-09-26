init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_bg"] = {
            PRIORITY: 0,
            MONDAY:{
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["wait01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["wait01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_UPSTAIRS, ["dress01"], QUICK)],
            },
            TUESDAY: {
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_UPSTAIRS, ["dress01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["model01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["model01"], QUICK)],

            },
            WEDNESDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["model01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["model01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["wait01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["wait01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_UPSTAIRS, ["dress01"], QUICK)],

            },
            THURSDAY:{
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["wait01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["wait01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["wait01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["wait01"], QUICK)],

            },
            FRIDAY:{
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["model01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_PHOTOSPACE, ["model01"], QUICK)],

            },
            SATURDAY:{
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_UPSTAIRS, ["dress01"], QUICK)],
            },
            SUNDAY:{
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-BG002"] = {
            PRIORITY: 0,
            TUESDAY: {
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],

            },
            WEDNESDAY:{
                TIMESLOT_5: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],

            },
            THURSDAY:{
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],

            },
            FRIDAY:{
                TIMESLOT_8: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],

            },
            SATURDAY:{
                TIMESLOT_7: [ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW, ["sit01"]), ScheduleSlot(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_KITCHEN, ["sit01"], QUICK)],

            },
            }
