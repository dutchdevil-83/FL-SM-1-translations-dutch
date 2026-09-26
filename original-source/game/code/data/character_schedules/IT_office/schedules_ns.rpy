init 1 python:
    NS_CUSTOM_POSES_LIST = [
            "run01_15", "run01_60", "meeting01", "beanbag_sit02_75", "beanbag_sit01_80", "ns009", "pee01",
        ]

    DEFAULT_CHARACTERS_TIMETABLES["default_ns"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            THIRD_WORK_DAYS: {
                TIMESLOT_7: [ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_OVERVIEW, ["stand01_30"]), ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_FRIDGES, ["stand01_10"], QUICK)],
                TIMESLOT_3: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["run01_15"], QUICK), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["run01_60"])],
            },
            EVEN_WORK_DAYS: {
            },
            ODD_WORK_DAYS: {
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MEETING, ["meeting01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_TOILET, ["meeting01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["meeting01_96"]) ],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting20"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting55"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting60"])],
            },
            SATURDAY: {
                TIMESLOT_7: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["sit01_40"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FOUNTAIN, ["sit01_40"], QUICK)],
            },
            WORKDAYS: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting20", "sit02_20"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting55", "sit02_55"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting60", "sit02_60"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_BEANBAGS, ["beanbag_sit02_75", "beanbag_sit01_80"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["beanbag_sit02_75", "beanbag_sit01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["beanbag_sit02_75", "beanbag_sit01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["beanbag_sit02_75", "beanbag_sit01_80"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting20", "sit02_20"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting55", "sit02_55"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting60", "sit02_60"])],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting20", "sit02_20"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting55", "sit02_55"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting60", "sit02_60"])],
            },
        }


    DEFAULT_CHARACTERS_TIMETABLES["Q-NS004"] = {
            WORKDAYS: {
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_BEANBAGS, ["beanbag_sit02_75"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["beanbag_sit02_75"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["beanbag_sit02_75"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["beanbag_sit02_75"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_BEANBAGS, ["beanbag_sit02_75"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["beanbag_sit02_75"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["beanbag_sit02_75"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["beanbag_sit02_75"])],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-NS009"] = {
            WORKDAYS: {
                TIMESLOT_8: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_COUCH, ["ns009"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["ns009"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["ns009"])],
            },
        }
    DEFAULT_CHARACTERS_TIMETABLES["Q-NS012_2"] = {
            EVENDAYS : {
                TIMESLOT_7: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["gaming02"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["gaming01"], QUICK)],

            },
            ODDDAYS : {
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["fridge01_90", "kitchen01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["fridge01_90", "kitchen01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["fridge01_90", "kitchen01"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["kitchen01"])],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["fridge01_90", "kitchen01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["fridge01_90", "kitchen01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["fridge01_90", "kitchen01"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["kitchen01"])],
            },

        }
    DEFAULT_CHARACTERS_TIMETABLES["default_ns2"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            THIRD_WORK_DAYS: {
                TIMESLOT_7: [ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_OVERVIEW, ["stand01_30"]), ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_FRIDGES, ["stand01_10"], QUICK)],
                TIMESLOT_3: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["run01_15"], QUICK), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["run01_60"])],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["loungeup01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["loungeup01"], QUICK)],
            },
            EVEN_WORK_DAYS: {
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["loungeup01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["loungeup01"], QUICK)],
            },
            ODD_WORK_DAYS: {
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MEETING, ["meeting01"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_TOILET, ["meeting01"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["meeting01_96"]) ],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting20"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting55"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting60"])],
            },
            TUESDAY:{
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["shower01"], QUICK)],
            },
            THURSDAY:{
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["pee01"], WATCH_PEE)],
            },
            SATURDAY: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["gaming02"], QUICK)],
                TIMESLOT_2: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["sleep01", "sleep02"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["gaming01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["fridge01_90", "kitchen01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["fridge01_90", "kitchen01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["fridge01_90", "kitchen01"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["kitchen01"])],
                TIMESLOT_5: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["gaming01", "gaming02"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["loungeup01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["loungeup01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["sit01_40"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FOUNTAIN, ["sit01_40"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["gaming01", "gaming02"], QUICK)]
            },
            SUNDAY:{
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["fridge01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["fridge01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["fridge01_90"], QUICK),   ],
                TIMESLOT_2: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["sleep01", "sleep02"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["sleep02", "sleep01"], SLEEP)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["sleep01", "sleep02"], SLEEP)],
                TIMESLOT_5: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["gaming01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["gaming02"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["kitchen01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["kitchen01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["sleep01", "sleep02"], QUICK)],
            },
            MONDAY:{
                TIMESLOT_1: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["sleep02", "sleep01"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["shower01"], QUICK)],

            },
            WORKDAYS: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["sleep01", "sleep02"], SLEEP)],
                TIMESLOT_2: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["sleep02", "sleep01"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting20", "sit02_20"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting55", "sit02_55"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting60", "sit02_60"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_BEANBAGS, ["beanbag_sit02_75", "beanbag_sit01_80"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["beanbag_sit02_75", "beanbag_sit01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["beanbag_sit02_75", "beanbag_sit01_80"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["beanbag_sit02_75", "beanbag_sit01_80"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting20", "sit02_20"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting55", "sit02_55"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting60", "sit02_60"])],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["sitting20", "sit02_20"], QUICK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW, ["sitting70", "sit02_70"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_DESKS, ["sitting50", "sit02_50"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CORRIDOR, ["sitting55", "sit02_55"]), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_CWDESK, ["sitting60", "sit02_60"])],
                TIMESLOT_8: [ScheduleSlot(STUDIO, SD_SUB_NARI, SD_NARI, ["gaming01"], QUICK)],
            },
        }
