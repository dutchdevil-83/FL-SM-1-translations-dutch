init 1 python:
    DEFAULT_OBJECTS_TIMETABLES["default_sign_rehearsal"] = {
            TUESDAY: {
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Rehearsal")],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Rehearsal")],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Rehearsal")],
            },
            WEDNESDAY: {
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Rehearsal")],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Rehearsal")],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Rehearsal")],
            },
            FRIDAY: {
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Rehearsal")],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Rehearsal")],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Rehearsal")],
            },
        }

    DEFAULT_OBJECTS_TIMETABLES["default_sign_show"] = {
            SATURDAY: {
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Work")],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Work")],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR, ["idle95"], "io-TH_Work")],
            },
        }
