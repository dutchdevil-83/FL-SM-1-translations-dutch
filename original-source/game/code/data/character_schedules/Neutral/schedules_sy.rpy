init 1 python:
    SY_CUSTOM_POSES_LIST = [
            "masturbateclown", "lay01", "sleep01", "sleep03"
        ]

    DEFAULT_CHARACTERS_TIMETABLES["default_sy"] = {
            PRIORITY: 0,

            WORKDAYS : {},
            EVENDAYS : {},
            ODDDAYS: {},

            MONDAY: {
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["clean01"], QUICK)],
            },
            TUESDAY: {
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["stand02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["stand02"], QUICK)],
            },
            THURSDAY: {
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["clean01"], QUICK)],
            },
            FRIDAY: {
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["stand02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["stand02"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["pee01"])],
            },

            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["sleep01"], SLEEP, "empty_image")],
                TIMESLOT_2: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["sleep01"], SLEEP, "empty_image")],
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit01", "stand01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit01", "stand01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit01", "stand01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit01", "stand01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit03", "sit02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit03", "sit02"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit03", "sit02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit03", "sit02"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit02", "clean02", "sit04"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit02", "clean02", "sit04"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["stand01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["stand01"], QUICK)],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["default_sy2"] = {
            PRIORITY: 0,

            WORKDAYS : {},
            EVENDAYS : {},
            ODDDAYS: {},

            MONDAY: {
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_CORNER, ["makeup01"], QUICK)],
            },
            TUESDAY: {
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_1, ["work12"], QUICK)],
            },
            THURSDAY: {
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["shower01"], QUICK)],
            
            },
            FRIDAY: {
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_1, ["work12"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["pee01"])],
            },

            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_BED, ["sleep03"], SLEEP, "empty_image")],
                TIMESLOT_2: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_BED, ["sleep03"], SLEEP, "empty_image")],
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["kitchen03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["kitchen03"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["couch03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["couch03"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["filmcouch01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_1, ["work12"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["couch03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["couch03"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["kitchen03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["kitchen03"], QUICK)],
            },
        }
    DEFAULT_CHARACTERS_TIMETABLES["sy_reno_base02"] = {
            PRIORITY: 0,

            WORKDAYS : {},
            EVENDAYS : {},
            ODDDAYS: {},

            TUESDAY: {
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_sitcouch01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["renovation_sitcouch01_base02"], QUICK)],
            },
            THURSDAY: {
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovating01_base02"], QUICK)],
            },
            FRIDAY: {
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["planning01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["planning01_base02"], QUICK)],
            },

            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["sleep01"], SLEEP, "empty_image")],
                TIMESLOT_2: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["sleep01"], SLEEP, "empty_image")],
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["planning01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["planning01_base02"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovating01_base02"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovating01_base02"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["planning01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["planning01_base02"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_sitcouch01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["renovation_sitcouch01_base02"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["planning01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["planning01_base02"], QUICK)],
            },
        }
    DEFAULT_CHARACTERS_TIMETABLES["sy_reno_base03"] = {
            PRIORITY: 0,

            WORKDAYS : {},
            EVENDAYS : {},
            ODDDAYS: {},

            MONDAY: {
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_sitcouch01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["renovation_sitcouch01_base03"], QUICK)],
            },
            TUESDAY: {
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["renovation_planning02_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["renovation_planning02_base03"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_BED, ["renovation_planning02_base03"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["renovation_planning02_base03"])],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_sitcouch01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["renovation_sitcouch01_base03"], QUICK)],
            },
            THURSDAY: {
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["renovation_planning02_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["renovation_planning02_base03"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_BED, ["renovation_planning02_base03"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["renovation_planning02_base03"])],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovating01_base03"], QUICK)],
            },
            FRIDAY: {
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["renovation_planning02_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["renovation_planning02_base03"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_BED, ["renovation_planning02_base03"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["renovation_planning02_base03"])],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["planning01_base03"], QUICK)],
            },

            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["sleep01"], SLEEP, "empty_image")],
                TIMESLOT_2: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["sleep01"], SLEEP, "empty_image")],
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["planning01_base03"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovating01_base03"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovating01_base03"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["planning01_base03"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_sitcouch01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["renovation_sitcouch01_base03"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["planning01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["planning01_base03"], QUICK)],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["sy_MS003_perma"] = {
            TUESDAY: { TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["clean02", "masturbateclown"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["clean02", "masturbateclown"], {"clean02":QUICK, "masturbateclown":"io-MS003_perma"}, {"clean02":False, "masturbateclown":"empty_image"})]}
        }

    DEFAULT_CHARACTERS_TIMETABLES["sy_MS005_perma"] = {
            MONDAY: { TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["lay01"], [SLEEP, "io-MS005_perma"], "empty_image")]}
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-SY001"] = {
            ALLDAYS: { TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["shower01"], ["io-SY001_perma"], "empty_image")]}
        }

    DEFAULT_CHARACTERS_TIMETABLES["sy_SY001_perma"] = {
            ODDDAYS: { TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["shower01"], ["io-SY001_perma", "io-SY001_perma_2"], "empty_image")]}
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-MS002-6_sy"] = {
            ALLDAYS: {
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit01", "stand01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit01", "stand01"], BUSY)], 
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit01", "stand01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit01", "stand01"], BUSY)], 
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit03", "sit02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit03", "sit02"], BUSY)], 
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit03", "sit02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit03", "sit02"], BUSY)], 
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["working_laptop"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["working_laptop"], QUICK)], 
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["stand01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["stand01"], BUSY)],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-MS003-3_sy"] = {
            ALLDAYS: {
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit01", "stand01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit01", "stand01"], BUSY)], 
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit01", "stand01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit01", "stand01"], BUSY)], 
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit03", "sit02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit03", "sit02"], BUSY)], 
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["sit03", "sit02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["sit03", "sit02"], BUSY)], 
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["masturbateclown"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["masturbateclown"], QUICK)], 
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["stand01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["stand01"], BUSY)],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-MS005"] = {
            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["lay01"], [SLEEP, "io-MS005"], "empty_image")],
                TIMESLOT_2: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["lay01"], [SLEEP, "io-MS005"], "empty_image")],
            },
        }
    DEFAULT_CHARACTERS_TIMETABLES["Q-MS004-2_sy"] = {
            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_2: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_3: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_4: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_5: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_6: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],
            },
        }
