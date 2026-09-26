init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_my"] = {
            PRIORITY: 0,

            WORKDAYS : {},
            EVENDAYS : {},
            ODDDAYS: {},

        }
    DEFAULT_CHARACTERS_TIMETABLES["default_my2"] = {
            PRIORITY: 0,

            WORKDAYS : {
            
            
            
            },
            EVENDAYS : {
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["couch_lean01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_COUCH, ["couch_lean01"], QUICK)],
            },
            ODDDAYS: {},
            THIRDDAYS:{},
            MONDAY: {
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["pee01"], ANGRY_PEEK)],
            },
            WEDNESDAY:{
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["stand01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["stand01"] ), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["stand01"], QUICK)],
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit_wine01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit_wine01"] ), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["sit_wine01"], QUICK)],
            },
            FRIDAY:{
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit_wine01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit_wine01"] ), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["sit_wine01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["stand01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["stand01"] ), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["stand01"], QUICK)],

            },
            SATURDAY:{
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit_wine01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit_wine01"] ), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["sit_wine01"], QUICK)],
            },
            WEEKENDS: {
            
            
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["upstairs_leanover01"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["upstairs_leanover01"], QUICK)],
            
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["stand01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["stand01"] ), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["stand01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit_wine01"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit_wine01"] ), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_STAGE, ["sit_wine01"], QUICK)],
            },

        }

    DEFAULT_CHARACTERS_TIMETABLES["q_my001"] = {
            PRIORITY: 0,

            ALLDAYS : {
                TIMESLOT_3: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_4: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_5: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_6: [ScheduleSlot("Void", "b", "c", [])],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["my_reno_base02"] = {
            PRIORITY: 0,

            WORKDAYS : {},
            EVENDAYS : {},
            ODDDAYS: {},

            MONDAY: {
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_gazing01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["renovation_gazing01_base02"], QUICK)],
            },
            TUESDAY: {
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_crouch01_base02"], QUICK)],
            },
            THURSDAY: {
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_crouch01_base02"], QUICK)],
            },
            FRIDAY: {
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_gazing01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["renovation_gazing01_base02"], QUICK)],
            },

            ALLDAYS: {
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_gazing01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["renovation_gazing01_base02"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_crouch01_base02"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_hammer01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS, ["renovation_hammer01_base02"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_hammer01_base02"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS, ["renovation_hammer01_base02"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_crouch01_base02"], QUICK)],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["my_reno_base03"] = {
            PRIORITY: 0,

            WORKDAYS : {},
            EVENDAYS : {},
            ODDDAYS: {},

            MONDAY: {
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_gazing01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["renovation_gazing01_base03"], QUICK)],
            },
            TUESDAY: {
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_1, ["renovation_leaning01_base03"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["renovation_leaning01_base03"], QUICK)],
            },
            THURSDAY: {
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_1, ["renovation_leaning01_base03"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["renovation_leaning01_base03"], QUICK)],
            },
            FRIDAY: {
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_gazing01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["renovation_gazing01_base03"], QUICK)],
            },

            ALLDAYS: {
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_gazing01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["renovation_gazing01_base03"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_1, ["renovation_leaning01_base03"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2, ["renovation_leaning01_base03"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_hammer01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS, ["renovation_hammer01_base03"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_gazing01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["renovation_gazing01_base03"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["renovation_hammer01_base03"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS, ["renovation_hammer01_base03"], QUICK)],
            },
        }
