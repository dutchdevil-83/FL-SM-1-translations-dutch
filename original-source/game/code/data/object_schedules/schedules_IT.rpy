init 1 python:
    DEFAULT_OBJECTS_TIMETABLES["default_itpc"] = {
            PRIORITY: 0,
            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["idle15"])],
                TIMESLOT_2: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["idle15"])],
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["idle15"])],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["idle15"])],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["idle15"])],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["idle15"])],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["idle15"])],
                TIMESLOT_8: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_MCDESK, ["idle15"])],
            },
        }

    DEFAULT_OBJECTS_TIMETABLES["default_animal_magazine"] = {
            PRIORITY: 0,
            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["idle05"], "io-animal-magazine")],
                TIMESLOT_2: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["idle05"], "io-animal-magazine")],
                TIMESLOT_3: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["idle05"], "io-animal-magazine")],
                TIMESLOT_4: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["idle05"], "io-animal-magazine")],
                TIMESLOT_5: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["idle05"], "io-animal-magazine")],
                TIMESLOT_6: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["idle05"], "io-animal-magazine")],
                TIMESLOT_7: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["idle05"], "io-animal-magazine")],
                TIMESLOT_8: [ScheduleSlot(IT_OFFICE, IT_SUB_TOILET, IT_BATHROOM, ["idle05"], "io-animal-magazine")],
            },
        }
