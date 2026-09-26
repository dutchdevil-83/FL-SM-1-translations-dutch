init 1 python:
    DEFAULT_CHARACTERS_TIMETABLES["default_ms"] = {
            PRIORITY: 0,

            MONDAY: {
                TIMESLOT_3: [ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_OUTSIDE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_SEATS, ["slouch01", "sit01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_OVERVIEW, ["stand01_20"], QUICK), ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_FRIDGES, ["stand01_20"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["hotdog_stand01"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FOUNTAIN, ["hotdog_stand01"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_HOTDOG, ["hotdog_stand01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["hotdog_stand01"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FOUNTAIN, ["hotdog_stand01"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_HOTDOG, ["hotdog_stand01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],
            },
            TUESDAY:{
                TIMESLOT_3: [ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_OUTSIDE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_SEATS, ["slouch01", "sit01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_OUTSIDE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_SEATS, ["slouch01", "sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["hotdog_stand01"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FOUNTAIN, ["hotdog_stand01"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_HOTDOG, ["hotdog_stand01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],
            },
            WEDNESDAY: {
                TIMESLOT_3: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["sit01"], QUICK), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_COUNTER, ["sit01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_6: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
            },
            THURSDAY: {
                TIMESLOT_5: [ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_OVERVIEW, ["stand01_20"], QUICK), ScheduleSlot(SHOP_71STORE, DEFAULT_SUBLOCATION, L71_FRIDGES, ["stand01_20"], QUICK)],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],
            },
            FRIDAY: {
                TIMESLOT_6: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["sit01"], QUICK), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_COUNTER, ["sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["sit01"], QUICK), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_COUNTER, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],
            },
            SATURDAY:{
                TIMESLOT_3: [ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_OUTSIDE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_SEATS, ["slouch01", "sit01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_OUTSIDE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_SEATS, ["slouch01", "sit01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_OUTSIDE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_SEATS, ["slouch01", "sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["sit01"], QUICK), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_COUNTER, ["sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],
            },
            SUNDAY: {
                TIMESLOT_4: [ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE, ["sit01"], QUICK), ScheduleSlot(STARDUCKS, DEFAULT_SUBLOCATION, LSC_COUNTER, ["sit01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE, ["hotdog_stand01"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_FOUNTAIN, ["hotdog_stand01"]), ScheduleSlot(PARK, DEFAULT_SUBLOCATION, LPA_HOTDOG, ["hotdog_stand01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_7: [ScheduleSlot("Void", "b", "c", [])],
                TIMESLOT_8: [ScheduleSlot("Void", "b", "c", [])],
            },
            WORKDAYS : {
                TIMESLOT_5: [ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_OUTSIDE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_SEATS, ["slouch01", "sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_OUTSIDE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE, ["slouch01", "sit01"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_SEATS, ["slouch01", "sit01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_OUTSIDE, ["sit02", "sit03"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE, ["sit02", "sit03"]), ScheduleSlot(WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_SEATS, ["sit02", "sit03"], QUICK)],
            },

            ODDDAYS: {},
            ALLDAYS: {},
        }
