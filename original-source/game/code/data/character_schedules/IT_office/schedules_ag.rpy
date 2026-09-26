init 1 python:
    AG_CUSTOM_POSES_LIST = [
            "towel_drying01", "couch_play01", "drinking01",
        ]

    DEFAULT_CHARACTERS_TIMETABLES["default_ag"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODDDAYS: {},
            MONDAY: {
                TIMESLOT_3: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["walk01_10"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["towel_drying01"], QUICK)],
            },
            TUESDAY: {
            
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_KITCHEN, ["drinking01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["drinking01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["drinking01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["drinking01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_BEANBAGS, ["drinking01"])],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["towel_drying01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_OVERVIEW, ["stand01_10"], QUICK)],
            },
            WEDNESDAY: {
                TIMESLOT_3: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["walk01_10"], QUICK)],
            },
            FRIDAY: {
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["couch_play01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["couch_play01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["couch_play01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["couch_play01"])],
                TIMESLOT_7: [ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_OVERVIEW, ["stand01_10"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["stand01_70"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["stand01_10"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit02"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit02"], QUICK)],

            },
            SATURDAY: {
                TIMESLOT_5: [ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_OVERVIEW, ["stand01_10"], QUICK)],
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit01"], QUICK)],
            },
            SUNDAY: {
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit02"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit02"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_OVERVIEW, ["stand01_10"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit02"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit02"], QUICK)],
            },
            EVEN_WORK_DAYS : {
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting65"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting90"])],
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_KITCHEN, ["drinking01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["drinking01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["drinking01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["drinking01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_BEANBAGS, ["drinking01"])],
            },
            WORKDAYS: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting60", "sit02_60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting65", "sit02_65"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting80", "sit02_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting90", "sit02_90"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting65"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting90"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting65"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting90"])],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting60"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting65"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting90"])],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["couch_play01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["couch_play01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["couch_play01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["couch_play01"])],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["q_ag003"] = {
            PRIORITY: 0,

            WORKDAYS : {
                TIMESLOT_3: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_4: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["ag003"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["ag003"], QUICK), ],
                TIMESLOT_5: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["ag003"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["ag003"], QUICK), ],
                TIMESLOT_6: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["ag003"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["ag003"], QUICK), ],
                TIMESLOT_7: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["ag003"]), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_CENTER, ["ag003"], QUICK), ],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],
            },
            ODDDAYS: {},
            ALLDAYS: {},
        }
