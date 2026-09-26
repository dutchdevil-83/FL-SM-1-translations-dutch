init 1 python:
    TL_CUSTOM_POSES_LIST = [
            "shower01", "sleep01", "pee01"
        ]

    DEFAULT_CHARACTERS_TIMETABLES["default_tl"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODDDAYS: {},
            MONDAY: {
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
            },
            TUESDAY: {
            
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["stand01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
            
            },
            WEDNESDAY: {
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_1, ["chill01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["chill01"])],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
            },
            THURSDAY: {
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_1, ["chill01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["chill01"])],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["stand01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean02"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
            },
            FRIDAY: {
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["sit01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_1, ["chill01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["chill01"])],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
            },
            SATURDAY: {
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean02"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["sit01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["stand01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
            
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_1, ["chill01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["chill01"])],
            },
            SUNDAY: {
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean02"], QUICK)],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-TL008_2"] = {
            PRIORITY: 0,

            EVENDAYS : {
                TIMESLOT_7: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
            },
            ODDDAYS: {
                TIMESLOT_7: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["default_tl2"] = {
            PRIORITY: 0,

            EVENDAYS : {},
            ODDDAYS: {},
            MONDAY: {
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
                TIMESLOT_2: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep01"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep02"], SLEEP)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["kitchen01_90"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["kitchen01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["kitchen01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_BED, ["kitchen01_90"])],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["pee01"], WATCH_PEE)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["shower01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
            },
            TUESDAY: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep02"], SLEEP)],
                TIMESLOT_2: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep01"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["kitchen01_90"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["kitchen01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["kitchen01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_BED, ["kitchen01_90"])],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["stand01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["fridge01_90"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["fridge01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["fridge01_90"])],
            },
            WEDNESDAY: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep02"], SLEEP)],
                TIMESLOT_2: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep01"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["sit01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_1, ["chill01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["chill01"])],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["kitchen01_90"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["kitchen01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_4, ["kitchen01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_BED, ["kitchen01_90"])],
            },
            THURSDAY: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["fridge01_90"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["fridge01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["fridge01_90"])],
                TIMESLOT_2: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep02"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep01"], SLEEP)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS, ["lean01"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["lean01"])],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_1, ["chill01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["chill01"])],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
            },
            FRIDAY: {
                TIMESLOT_1: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["pee01"], WATCH_PEE)],
                TIMESLOT_2: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep02"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS, ["lean01"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["lean01"])],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_SHELVES_1, ["chill01"], QUICK), ScheduleSlot(THEATER, LTH_SUB_STORAGE, LTH_ENTRANCE_BACKSTAGE, ["chill01"])],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
            },
            SATURDAY: {
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean02"], QUICK)],
                TIMESLOT_2: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep02"], SLEEP)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep01"], SLEEP)],
                TIMESLOT_4: [ScheduleSlot(THEATER, LTH_SUB_LOCKERS, LTH_LOCKERS, ["stand01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(THEATER, LTH_SUB_SHOWER, LTH_SHOWERS_ENTRANCE, ["shower01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(THEATER, LTH_SUB_DRESSING_1, LTH_DRESSINGROOM_1, ["phone01"], QUICK)],
                TIMESLOT_7: [ScheduleSlot(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE, ["sit01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS, ["lean01"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["lean01"])],
            },
            SUNDAY: {
                TIMESLOT_1: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
                TIMESLOT_2: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM, ["pee01"], WATCH_PEE)],
                TIMESLOT_3: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep01"], SLEEP)],
                TIMESLOT_4: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["sleep01"], SLEEP)],
                TIMESLOT_5: [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["fridge01_90"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["fridge01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["fridge01_90"])],
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean01"], QUICK)],
                TIMESLOT_8: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["lean02"], QUICK)],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-MV01Q02"] = {
            ALLDAYS: {
                TIMESLOT_1: [ScheduleSlot("Null", "Void", "", [])],
                TIMESLOT_2: [ScheduleSlot("Null", "Void", "", [])],
                TIMESLOT_3: [ScheduleSlot("Null", "Void", "", [])],
                TIMESLOT_4: [ScheduleSlot("Null", "Void", "", [])],
                TIMESLOT_5: [ScheduleSlot("Null", "Void", "", [])],
                TIMESLOT_6: [ScheduleSlot("Null", "Void", "", [])],
                TIMESLOT_7: [ScheduleSlot(GR_BAR, LGR_SUB_BAR, LGR_BILLIARD, ["mv01s03_2"], "io-MV01S03_2", "empty_image")],
                TIMESLOT_8: [ScheduleSlot("Null", "Void", "", [])],
            },
        }

    DEFAULT_CHARACTERS_TIMETABLES["Q-MV01S06_2"] = {
            ALLDAYS: {
                TIMESLOT_3:  [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
                TIMESLOT_4:  [ScheduleSlot(STUDIO, SD_SUB_TAISIA, SD_TAISIA, ["laptop01"], QUICK)],
                TIMESLOT_5: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS, ["lean01"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS, ["lean01"])],
                TIMESLOT_6: [ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN, ["fridge01_90"], QUICK), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW, ["fridge01_90"]), ScheduleSlot(STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_3, ["fridge01_90"])],
            },
        }
