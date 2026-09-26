init 1 python:
    AM_CUSTOM_POSES_LIST = [
            "meeting01", "sink_wash01", "walk02_20", "beanbag_sit01"
        ]

    DEFAULT_CHARACTERS_TIMETABLES["default_am"] = {
            PRIORITY: 0,


            EVENDAYS : {},
            TUESDAY: {
                TIMESLOT_3: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FOUNTAIN, ["walk01_20"], QUICK), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["walk01_70"])],
            },
            THURSDAY: {
                TIMESLOT_3: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FOUNTAIN, ["walk01_20"], QUICK), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["walk01_70"])],
            },
            EVEN_WORK_DAYS: {
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MEETING, ["meeting01"], QUICK)],
            },
            ODD_WORK_DAYS: {
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["sink_wash01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting75", "sit02_75"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting80", "sit02_80"])],
                TIMESLOT_8: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["walk02_20"], QUICK)],
            },
            FRIDAY: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting75", "sit02_75"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting80", "sit02_80"])],
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["sit01"], QUICK), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit01"])],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["stretch01"], QUICK), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["stretch01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["stretch01"])],
            },
            SATURDAY: {
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["sit01"], QUICK), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit01"])],
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["stretch01"], QUICK), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["stretch01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["stretch01"])],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["stretch01"], QUICK), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["stretch01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["stretch01"])],
            },
            WORKDAYS: {
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting75", "sit02_75"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting80", "sit02_80"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting75", "sit02_75"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting80", "sit02_80"])],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting30", "sit02_30"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting75", "sit02_75"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting60", "sit02_60"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting80", "sit02_80"])],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_BEANBAGS, ["beanbag_sit01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["beanbag_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["beanbag_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["beanbag_sit01"])]
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-AM003"] = {
            WEDNESDAY: {
                TIMESLOT_3: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_4: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_5: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["scene003"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["scene003"], QUICK)],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
            },
            FRIDAY: {
                TIMESLOT_3: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_4: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_5: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["scene003"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["scene003"], QUICK)],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-AM004"] = {
            MONDAY: {
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_BEANBAGS, ["beanbag_sit01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["beanbag_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["beanbag_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["beanbag_sit01"])]
            },
            THURSDAY: {
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_BEANBAGS, ["beanbag_sit01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["beanbag_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["beanbag_sit01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["beanbag_sit01"])]
            },
        }
