init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_mes"] = {
            PRIORITY: 0,

            EVEN_WORK_DAYS: {

            },

        }

    DEFAULT_CHARACTERS_TIMETABLES["start_mes"] = {
            PRIORITY: 0,

            EVEN_WORK_DAYS: {

            },
            ALLDAYS:{
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["stand01"], QUICK)],
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BAR, ["sit02"], QUICK), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit02"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit02"], QUICK)],
            },
        }
    DEFAULT_CHARACTERS_TIMETABLES["sm1cs_mes001"] = {
            PRIORITY: 0,

            EVEN_WORK_DAYS: {

            },
            ALLDAYS:{
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BAR, ["sit02"], QUICK), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit02"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit02"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BAR, ["sit02"], QUICK), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit02"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit02"], QUICK)],
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BAR, ["sit02"], QUICK), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_ENTRANCE, ["sit02"]), ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_MIDDLE, ["sit02"], QUICK)],
            },
        }
