init python:
    map_locations_list = [
            MapLocation(SD_NAME,  STUDIO,         DEFAULT_SUBLOCATION,  SD_OVERVIEW,        848,  345),
            MapLocation(WD_NAME,  WURST_DELIVERY, DEFAULT_SUBLOCATION,  WD_OUTSIDE,         615,  650),
            MapLocation(IT_NAME,  IT_OFFICE,      DEFAULT_SUBLOCATION,  IT_OPENVIEW,        530,  345),
            MapLocation(LPA_NAME, PARK,           DEFAULT_SUBLOCATION,  LPA_ENTRANCE,       440,  490),
            MapLocation(LPD_NAME, PHOTO_DOJO,     LPD_SUB_INSIDE,       LPD_OVERVIEW,       550,  905),
            MapLocation(L71_NAME, SHOP_71STORE,   DEFAULT_SUBLOCATION,  L71_OVERVIEW,       1005, 480),
            MapLocation(LTH_NAME, THEATER,        LTH_SUB_CORRIDOR,     LTH_CORRIDOR_ENTR,  1410, 690),
            MapLocation(LSC_NAME, STARDUCKS,      DEFAULT_SUBLOCATION,  LSC_ENTRANCE,       250,  550),
            MapLocation(LLY_NAME, LYSSAS_HOUSE,   DEFAULT_SUBLOCATION,  LLY_OUTSIDE,        1385, 230),
            MapLocation(LGR_NAME, GR_BAR,         LGR_SUB_BAR,          LGR_ENTRANCE,       873,  620),
            ]

    indexed_map_locations_list = {}
    for location in map_locations_list:
        indexed_map_locations_list[location.codename] = location
