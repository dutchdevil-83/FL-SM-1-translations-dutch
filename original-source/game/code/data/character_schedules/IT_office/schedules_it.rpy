init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_en"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODD_WORK_DAYS: {},
            WORKDAYS: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting10"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sit02_10"], QUICK)],
            
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting10"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sit02_10"], QUICK)],
            }
        }

    DEFAULT_CHARACTERS_TIMETABLES["default_jh"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODD_WORK_DAYS: {
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting40", "sit02_40"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting55", "sit02_55"])],
            },
            WORKDAYS: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting40", "sit02_40"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting55", "sit02_55"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting40", "sit02_40"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting55", "sit02_55"])],

                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting40", "sit02_40"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting55", "sit02_55"])],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["default_lm"] = {
            PRIORITY: 0,

            EVEN_WORK_DAYS : {
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting40", "sit02_40"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting60", "sit02_60"])],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["watercooler01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["watercooler01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["watercooler01_60"], QUICK)],
            },
            ODD_WORK_DAYS: {
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting40", "sit02_40"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting60", "sit02_60"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["watercooler01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["watercooler01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["watercooler01_60"], QUICK)],
            },
            WORKDAYS: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting40", "sit02_40"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting60", "sit02_60"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting40", "sit02_40"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting60", "sit02_60"])],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting40", "sit02_40"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting60", "sit02_60"])],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["default_mj"] = {
            PRIORITY: 0,

            EVENDAYS : {
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["fridge01_90"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["fridge01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["fridge01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_TOILET, ["fridge01_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_KITCHEN, ["fridge01_30"], QUICK)],
            },
            ODD_WORK_DAYS: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["fridge01_90"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["fridge01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["fridge01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_TOILET, ["fridge01_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_KITCHEN, ["fridge01_30"], QUICK)],
            },
            WORKDAYS: {
            
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting35", "sit02_35"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting35", "sit02_35"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting80"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting35", "sit02_35"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting35", "sit02_35"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting80"])],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting35", "sit02_35"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting35", "sit02_35"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting80"])],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["default_pm"] = {
            PRIORITY: 0,

            EVEN_WORK_DAYS : {
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MEETING, ["meeting01_30"], QUICK)],
            },
            ODD_WORK_DAYS: {
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MEETING, ["meeting01_30"], QUICK)],
            },
            WORKDAYS: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting10", "sit02_10"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting20", "sit02_20"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting55", "sit02_55"])],
            
            
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting10", "sit02_10"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting20", "sit02_20"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting55", "sit02_55"])],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting10", "sit02_10"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting20", "sit02_20"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting55", "sit02_55"])],
                TIMESLOT_8: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting10", "sit02_10"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting20", "sit02_20"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting55", "sit02_55"])],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["default_sr"] = {
            PRIORITY: 0,

            EVEN_WORK_DAYS : {
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting30"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting50"])],
            },
            ODD_WORK_DAYS: {
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MEETING, ["meeting01_50"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["meeting01_95"])],
            },
            THURSDAY: {
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MEETING, ["meeting01_50"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["meeting01_95"])],
            },
            WORKDAYS: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting30", "sit02_30"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting50", "sit02_50"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting30", "sit02_30"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting50", "sit02_50"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting30", "sit02_30"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting50", "sit02_50"])],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting30", "sit02_30"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting50", "sit02_50"])],
            },
        }
