init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_nj"] = {
            PRIORITY: 0,

            WORKDAYS : {},
            EVENDAYS : {
                TIMESLOT_4: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FORK, ["run01_30"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["run01_80"])],
            },
            ODDDAYS: {},
        }
    DEFAULT_CHARACTERS_TIMETABLES["default_cg"] = {
            PRIORITY: 0,

            THIRDDAYS : {
                TIMESLOT_1: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FORK, ["stand01_60"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["stand01_90"])],
                TIMESLOT_2: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FORK, ["stand01_60"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["stand01_90"])],
            },
            EVENDAYS : {},
            ODDDAYS: {},
        }
    DEFAULT_CHARACTERS_TIMETABLES["default_dw"] = {
            PRIORITY: 0,

            ODDDAYS : {
                TIMESLOT_5: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["dogwalking01"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FORK, ["dogwalking01"])],
                TIMESLOT_7: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_CENTER, ["dogwalking02"])],
            },
            EVENDAYS : {},
        }
