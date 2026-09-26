init python:
    DRESS_CODE_CATALOGUE = {
            "th_bath_nude" : {NAME: "nude", PRIORITY: 2, CHARACTERS: [ALL], LOCATION: THEATER, SUBLOCATION: LTH_SUB_SHOWER},
            "lst_my_home": {NAME: "home", PRIORITY: 2, CHARACTERS: ["my"], LOCATION: STUDIO},
            "lst_bath_nude_sy" : {NAME: "nude", PRIORITY: 2, CHARACTERS: ["sy"], LOCATION: STUDIO, SUBLOCATION: DEFAULT_SUBLOCATION, POSITION: SD_BATHROOM},
            "lst_bath_nude_ns" : {NAME: "nude", PRIORITY: 2, CHARACTERS: ["ns"], LOCATION: STUDIO, SUBLOCATION: DEFAULT_SUBLOCATION, POSITION: SD_BATHROOM},
            "lst_bath_nude_tl" : {NAME: "nude", PRIORITY: 2, CHARACTERS: ["tl"], LOCATION: STUDIO, SUBLOCATION: DEFAULT_SUBLOCATION, POSITION: SD_BATHROOM},
            "lpa_ms_work": {NAME: "work", PRIORITY: 2, CHARACTERS: ["ms"], LOCATION: PARK, SUBLOCATION: DEFAULT_SUBLOCATION, POSITION: LPA_HOTDOG},
            "lpa_ms_work_wurst": {NAME: "work", PRIORITY: 3, CHARACTERS: ["ms"], LOCATION: WURST_DELIVERY},
            }

    PERSISTENT_DRESS_CODES = ["th_bath_nude", "lst_my_home", "lpa_ms_work", "lpa_ms_work_wurst", "lst_bath_nude_sy", "lst_bath_nude_ns", "lst_bath_nude_tl"]
