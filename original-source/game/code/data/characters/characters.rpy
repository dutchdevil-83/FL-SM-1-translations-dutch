init 2 python:
    sm_characters_data = [
            {NAME: "Mike",          SURNAME: "Young",           CODENAME:"mc",  CONSTANT: mc,   FACTION: False,             STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Stacy",         SURNAME: get_sy_surname(),  CODENAME:"sy",  CONSTANT: sy,   FACTION: False,             STORYLINE: SY_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: False},
            {NAME: "Melony",        SURNAME: get_my_surname(),  CODENAME:"my",  CONSTANT: my,   FACTION: False,             STORYLINE: MY_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (MS, "sm1ms013")},
            {NAME: "Lyssa",         SURNAME: "Harris",          CODENAME:"mh",  CONSTANT: mh,   FACTION: False,             STORYLINE: MH_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (MH_STORY, "sm1cs_mh002")},
            {NAME: "Debbie",        SURNAME: "Callahan",        CODENAME:"dc",  CONSTANT: dc,   FACTION: False,             STORYLINE: DC_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (DC_STORY, "sm1cs_dc001i")},
            {NAME: "AmRose",        SURNAME: "Jenkins",         CODENAME:"arj", CONSTANT: arj,  FACTION: False,             STORYLINE: ARJ_STORY,   ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (MS, "sm1ms004")},
            {NAME: "Min",           SURNAME: "Eun-Soo",         CODENAME:"mes", CONSTANT: mes,  FACTION: False,             STORYLINE: MES_STORY,   ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (MES_STORY, "sm1cs_mes001")},
        
            {NAME: "Kanya",         SURNAME: "Vu",              CODENAME:"kv",  CONSTANT: kv,   FACTION: False,             STORYLINE: KV_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (KV_STORY, "sm1cs_kv001")},
            {NAME: "Amore",         SURNAME: "",                CODENAME:"bg",  CONSTANT: bg,   FACTION: False,             STORYLINE: BG_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (BG_STORY, "sm1cs_bg001")},
        
            {NAME: "Nelson",        SURNAME: "Rhor",            CODENAME:"nr",  CONSTANT: nr,   FACTION: False,             STORYLINE: False,       ESSENTIAL: True,  CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Maya",          SURNAME: "Siegel",          CODENAME:"ms",  CONSTANT: ms,   FACTION: False,             STORYLINE: MAS_STORY,   ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (MAS_STORY, "sm1cs_mas001")},
        
            {NAME: "Anna",          SURNAME: "Goodwin",         CODENAME:"ag",  CONSTANT: ag,   FACTION: IT_FACTION,        STORYLINE: AG_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (IT_STORY_LINE, "sm1fs_i003")},
            {NAME: "Claire",        SURNAME: "Watts",           CODENAME:"cw",  CONSTANT: cw,   FACTION: IT_FACTION,        STORYLINE: CW_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (IT_STORY_LINE, "sm1fs_i003")},
            {NAME: "Nari",          SURNAME: "Song",            CODENAME:"ns",  CONSTANT: ns,   FACTION: IT_FACTION,        STORYLINE: NS_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (IT_STORY_LINE, "sm1fs_i003")},
            {NAME: "April",         SURNAME: "Mercer",          CODENAME:"am",  CONSTANT: am,   FACTION: IT_FACTION,        STORYLINE: AM_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (IT_STORY_LINE, "sm1fs_i003")},
            {NAME: "Eugene",        SURNAME: "Nowakowski",      CODENAME:"en",  CONSTANT: en,   FACTION: IT_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Jayden",        SURNAME: "Hester",          CODENAME:"jh",  CONSTANT: jh,   FACTION: IT_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Libby",         SURNAME: "Moore",           CODENAME:"lm",  CONSTANT: lm,   FACTION: IT_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Megan",         SURNAME: "John",            CODENAME:"mj",  CONSTANT: mj,   FACTION: IT_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Peter",         SURNAME: "Maloney",         CODENAME:"pm",  CONSTANT: pm,   FACTION: IT_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Sienna",        SURNAME: "Roberts",         CODENAME:"sr",  CONSTANT: sr,   FACTION: IT_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
        
            {NAME: "Denise",        SURNAME: "Van der Haute",   CODENAME:"dvh", CONSTANT: dvh,  FACTION: TH_FACTION,        STORYLINE: DVH_STORY,   ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (THEATER_STORY_LINE, "sm1fs_t003")},
            {NAME: "Taisia",        SURNAME: "Lindqvist",       CODENAME:"tl",  CONSTANT: tl,   FACTION: TH_FACTION,        STORYLINE: TL_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (THEATER_STORY_LINE, "sm1fs_t003")},
            {NAME: "Veronica",      SURNAME: "Steele",          CODENAME:"vs",  CONSTANT: vs,   FACTION: TH_FACTION,        STORYLINE: VS_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (THEATER_STORY_LINE, "sm1fs_t003")},
            {NAME: "Kellie",        SURNAME: "Moore",           CODENAME:"km",  CONSTANT: km,   FACTION: TH_FACTION,        STORYLINE: KM_STORY,    ESSENTIAL: True,  CHAT: True,   UNLOCK_CONDITION: (THEATER_STORY_LINE, "sm1fs_t003")},
            {NAME: "Sam",           SURNAME: "Bruce",           CODENAME:"sb",  CONSTANT: sb,   FACTION: TH_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Eileen",        SURNAME: "Cavendish",       CODENAME:"ec",  CONSTANT: ec,   FACTION: TH_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Sue",           SURNAME: "Johnson",         CODENAME:"sj",  CONSTANT: sj,   FACTION: TH_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Kai",           SURNAME: "Wyatt",           CODENAME:"kw",  CONSTANT: kw,   FACTION: TH_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Amanda",        SURNAME: "Kline",           CODENAME:"ak",  CONSTANT: ak,   FACTION: TH_FACTION,        STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
        
            {NAME: "Inga",          SURNAME: "Cowen",           CODENAME:"ic",  CONSTANT: ic,   FACTION: False,             STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
        
            {NAME: "Cecilia",       SURNAME: "Siegel",          CODENAME:"cs",  CONSTANT: cs,   FACTION: False,             STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
        
            {NAME: "Nelly",         SURNAME: "Jogger",          CODENAME:"nj",  CONSTANT: nj,   FACTION: False,             STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Creepy",        SURNAME: "Guy",             CODENAME:"cg",  CONSTANT: cg,   FACTION: False,             STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Dog",           SURNAME: "Walker",          CODENAME:"dw",  CONSTANT: dw,   FACTION: False,             STORYLINE: False,       ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
            {NAME: "Ridley",        SURNAME: "Driver",          CODENAME:"rd",  CONSTANT: rd,   FACTION: False,             STORYLINE: RD_STORY,    ESSENTIAL: False, CHAT: False,  UNLOCK_CONDITION: False},
        ]

    sm_characters_list = []
    for data_item in sm_characters_data:
        sm_characters_list.append(SMCharacter.init_character(data_item))

    sm_indexed_character_list = {}
    for char in sm_characters_list:
        sm_indexed_character_list[char.codename] = char



    sm_character_traits_list = {
            "sy":  [DYED_HAIR, GREEN_HAIR, BRAIDS, SKINNY, SMALL_BOOBS, TAN_LINES],
            "my":  [BRUNETTE, CURVY, MILF],
            "arj": [REDHEAD, FRECKLES, SHORT],
            "mh":  [TRANS, TALL, DYED_HAIR, BLUE_HAIR],
            "kv":  [DYED_HAIR, GREEN_HAIR],
            "dc":  [BLONDE],
            "ms":  [REDHEAD, SKINNY],
            "bg":  [],

        
            "cw":  [REDHEAD, LONG_HAIR],
            "ns":  [GREY_HAIR, DYED_HAIR, TATTOO],
            "am":  [MULTIPLE_COLOR_HAIR, DYED_HAIR, FACIAL_PIERCING],
            "ag":  [SKINNY, DYED_HAIR, REDHEAD],

        
            "dvh": [FACIAL_PIERCING, MILF, BRUNETTE],
            "tl":  [BRUNETTE, SHORT_HAIR, SKINNY, PALE],
            "vs":  [DYED_HAIR, LONG_HAIR],
            "km":  [TATTOO, REDHEAD, CURVY],
        }

    for char_codename, traits_data in sm_character_traits_list.items():
        CharacterController.get_character(char_codename).init_traits(traits_data)



    sm_character_topics_list = {
        
            "cw":  [],
            "ns":  [],
            "am":  [],
            "ag":  [],

        
            "dvh": [],
            "tl":  [],
            "vs":  [],
            "km":  [],
        }

    for char_codename, topics_data in sm_character_topics_list.items():
        CharacterController.get_character(char_codename).init_topics(topics_data)
