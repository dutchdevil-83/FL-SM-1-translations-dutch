init 1 python:
    DEFAULT_OBJECTS_TIMETABLES["default_ns_panty"] = {
            PRIORITY: 0,
        }

    DEFAULT_OBJECTS_TIMETABLES["Q-NS003-panty"] = {
            PRIORITY: 0,
            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BR_STALL_3, ["idle15"], "io-get-ns-panty")],
                TIMESLOT_2: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BR_STALL_3, ["idle15"], "io-get-ns-panty")],
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BR_STALL_3, ["idle15"], "io-get-ns-panty")],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BR_STALL_3, ["idle15"], "io-get-ns-panty")],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BR_STALL_3, ["idle15"], "io-get-ns-panty")],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BR_STALL_3, ["idle15"], "io-get-ns-panty")],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BR_STALL_3, ["idle15"], "io-get-ns-panty")],
                TIMESLOT_8: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BR_STALL_3, ["idle15"], "io-get-ns-panty")],
            },
        }
