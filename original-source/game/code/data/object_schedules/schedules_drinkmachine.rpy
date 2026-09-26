init 1 python:
    DEFAULT_OBJECTS_TIMETABLES["default_drinkmachine01"] = {
            PRIORITY: 0,
            ALLDAYS: {
                TIMESLOT_ANY: [ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_COUNTER, ["idle95"], BUY_ENERGY_DRINK)],
            },
        }

    DEFAULT_OBJECTS_TIMETABLES["default_drinkmachine02"] = {
            PRIORITY: 0,
            ALLDAYS: {
                TIMESLOT_ANY: [ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_KITCHEN, ["idle95"], BUY_ENERGY_DRINK), ScheduleSlot(IT_OFFICE, DEFAULT_SUBLOCATION, IT_TOILET, ["idle95"], BUY_ENERGY_DRINK)],
            },
        }
