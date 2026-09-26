init python:
    location_music_list = [
            {
                NAME: audio.music_starducks2_reverbed,
                LOCATIONS: [STARDUCKS], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: EVENDAYS_LIST, VOLUME: 1.0
            },
            {
                NAME: audio.music_starducks1_radio,
                LOCATIONS: [STARDUCKS], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: ODDDAYS_LIST, VOLUME: 1.0
            },
            {
                NAME: audio.music_freeroam_theater1,
                LOCATIONS: [THEATER], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 0.6
            },
            {
                NAME: audio.music_freeroam_park1,
                LOCATIONS: [PARK], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: DAY_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 0.7
            },
            {
                NAME: audio.music_freeroam_itoffice1,
                LOCATIONS: [IT_OFFICE], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 0.8
            },
            {
                NAME: audio.music_freeroam_light1,
                LOCATIONS: [STUDIO, SHOP_71STORE, WURST_DELIVERY, LYSSAS_HOUSE], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: DAY_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 1.0
            },
            {
                NAME: audio.music_freeroam_light2,
                LOCATIONS: [STUDIO, SHOP_71STORE, WURST_DELIVERY, PARK, LYSSAS_HOUSE], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: NIGHT_TIMESOLTS, DAYS: ALLDAYS_LIST, VOLUME: 0.6
            },
            {
                NAME: audio.music_disco_funk_reverbed,
                LOCATIONS: [PHOTO_DOJO], SUBLOCATIONS: LPD_SUB_INSIDE, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 1.0
            },
            {
                NAME: audio.music_disco_funk_muffled,
                LOCATIONS: [PHOTO_DOJO], SUBLOCATIONS: DEFAULT_SUBLOCATION, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 1.0
            },
            {
                NAME: audio.music_freeroam_gunsnrosette1,
                LOCATIONS: [GR_BAR], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: [MONDAY, TUESDAY, FRIDAY], VOLUME: 1.0
            },
            {
                NAME: audio.music_freeroam_gunsnrosette2,
                LOCATIONS: [GR_BAR], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: NIGHT_TIMESOLTS, DAYS: [WEDNESDAY, THURSDAY], VOLUME: 1.0
            },
            {
                NAME: audio.music_freeroam_gunsnrosette3,
                LOCATIONS: [GR_BAR], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: [SATURDAY, SUNDAY], VOLUME: 1.0
            },
        ]

    location_ambience_list = [
            {
                NAME: audio.sfx_parkday_birds,
                LOCATIONS: [PARK, LYSSAS_HOUSE], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: DAY_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 0.5
            },
            {
                NAME: audio.sfx_parknight_crickets,
                LOCATIONS: [PARK, LYSSAS_HOUSE], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: NIGHT_TIMESOLTS, DAYS: ALLDAYS_LIST, VOLUME: 0.5
            },
            {
                NAME: audio.sfx_office_ambience1,
                LOCATIONS: [IT_OFFICE], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: [IT_OPENVIEW, IT_CORRIDOR, IT_COUCH, IT_TOILET, IT_CWDESK, IT_DESKS, IT_MCDESK, IT_BEANBAGS, IT_KITCHEN],
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7], DAYS: WORKDAYS_LIST, VOLUME: 0.8
            },
            {
                NAME: audio.sfx_store71_inside_amb_daynight1,
                LOCATIONS: [SHOP_71STORE], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 0.5
            },
            {
                NAME: audio.sfx_wurst_del_inside_amb_day1,
                LOCATIONS: [WURST_DELIVERY], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: [WD_ENTRANCE, WD_COUNTER, WD_SEATS],
                TIMESLOTS: ALL_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 0.5
            },
            {
                NAME: audio.sfx_wurst_del_outside_amb_day1,
                LOCATIONS: [WURST_DELIVERY], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: [WD_OUTSIDE],
                TIMESLOTS: DAY_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 1.0
            },
            {
                NAME: audio.sfx_wurst_del_outside_amb_night1,
                LOCATIONS: [WURST_DELIVERY], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: [WD_OUTSIDE],
                TIMESLOTS: NIGHT_TIMESOLTS, DAYS: ALLDAYS_LIST, VOLUME: 1.0
            },
            {
                NAME: audio.sfx_crowd_fightclub_ambient2,
                LOCATIONS: [GR_BAR], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: ALL_POSITIONS,
                TIMESLOTS: ALL_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 0.6
            },
        ]

    location_subambience_list = [
            {
                NAME: audio.sfx_fountain_ambience,
                LOCATIONS: [PARK], SUBLOCATIONS: ALL_SUBLOCATIONS, POSITIONS: [LPA_FOUNTAIN, LPA_HOTDOG, LPA_CENTER],
                TIMESLOTS: ALL_TIMESLOTS, DAYS: ALLDAYS_LIST, VOLUME: 0.8
            },

            {
                NAME: audio.sfx_shower_ambience1,
                LOCATIONS: [THEATER], SUBLOCATIONS: LTH_SUB_SHOWER, POSITIONS: [LTH_SHOWERS_ENTRANCE, LTH_SHOWERS_MIDDLE, LTH_SHOWERS_END],
                TIMESLOTS: TIMESLOT_4, DAYS: [TUESDAY, WEDNESDAY, FRIDAY], VOLUME: 0.8
            },
            {
                NAME: audio.sfx_shower_ambience1,
                LOCATIONS: [THEATER], SUBLOCATIONS: LTH_SUB_SHOWER, POSITIONS: [LTH_SHOWERS_ENTRANCE, LTH_SHOWERS_MIDDLE, LTH_SHOWERS_END],
                TIMESLOTS: TIMESLOT_5, DAYS: SATURDAY, VOLUME: 0.8
            },
            {
                NAME: audio.sfx_shower_ambience1,
                LOCATIONS: [THEATER], SUBLOCATIONS: LTH_SUB_SHOWER, POSITIONS: [LTH_SHOWERS_ENTRANCE, LTH_SHOWERS_MIDDLE, LTH_SHOWERS_END],
                TIMESLOTS: TIMESLOT_6, DAYS: TUESDAY, VOLUME: 0.8
            },
            {
                NAME: audio.sfx_shower_ambience1,
                LOCATIONS: [THEATER], SUBLOCATIONS: LTH_SUB_SHOWER, POSITIONS: [LTH_SHOWERS_ENTRANCE, LTH_SHOWERS_MIDDLE, LTH_SHOWERS_END],
                TIMESLOTS: TIMESLOT_8, DAYS: [WEDNESDAY, THURSDAY, SATURDAY], VOLUME: 0.8
            },
        ]
