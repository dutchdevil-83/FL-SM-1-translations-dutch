init 1 python:
    CW_CUSTOM_POSES_LIST = [
            "meeting01", "sink_wash01",
        ]

    DEFAULT_CHARACTERS_TIMETABLES["default_cw"] = {
            PRIORITY: 0,

            EVEN_WORK_DAYS : {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["couch_sit01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["couch_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["couch_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["couch_sit01"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MEETING, ["meeting01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["meeting01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_TOILET, ["meeting01"])],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10"], QUICK)],
            },
            ODD_WORK_DAYS : {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["sink_wash01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MEETING, ["meeting01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["meeting01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_TOILET, ["meeting01"])],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["couch_sit01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["couch_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["couch_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["couch_sit01"])],
            },
            WORKDAYS : {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
            },
            ODDDAYS: {},
            ALLDAYS: {},
        }

    DEFAULT_CHARACTERS_TIMETABLES["q_cw001"] = {
            PRIORITY: 0,

            EVEN_WORK_DAYS : {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["q_cw001"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["q_cw001_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["q_cw001"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["q_cw001"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["q_cw001"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["q_cw001_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["q_cw001"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["q_cw001"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["q_cw001"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["q_cw001_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["q_cw001"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["q_cw001"])],
            },
            ODD_WORK_DAYS : {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["q_cw001"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["q_cw001_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["q_cw001"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["q_cw001"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["q_cw001"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["q_cw001_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["q_cw001"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["q_cw001"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["q_cw001"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["q_cw001_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["q_cw001"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["q_cw001"])],
            },
            WORKDAYS : {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["q_cw001"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["q_cw001_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["q_cw001"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["q_cw001"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["q_cw001"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["q_cw001_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["q_cw001"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["q_cw001"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["q_cw001"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["q_cw001_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["q_cw001"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["q_cw001"])],
            },
            ODDDAYS: {},
            ALLDAYS: {},
        }
    DEFAULT_CHARACTERS_TIMETABLES["q_cw002"] = {
            PRIORITY: 0,

            EVEN_WORK_DAYS : {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
            },
            ODD_WORK_DAYS : {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
            },
            WORKDAYS : {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting45", "sit02_45"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting10", "sit02_10"], QUICK)],
            },
            ODDDAYS: {},
            ALLDAYS: {},
        }
    DEFAULT_CHARACTERS_TIMETABLES["q_cw004_2"] = {
            PRIORITY: 0,

            FRIDAY : {
            
                TIMESLOT_6: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["cw004"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["cw004"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["cw004"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["cw004"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_KITCHEN, ["cw004"], QUICK)],
            },
        }
