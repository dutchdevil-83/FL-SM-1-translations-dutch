init 1 python:
    sm_quest_lines_list = {
            MS:                 {QUEST_LINE: MSQuestLineList,                   NAME: _("Main Story"),          CONNECTED_CHARACTER: None},
            MORE_FACTIONS:      {QUEST_LINE: UnlockMoreFactionsQuestLineList,   NAME: _("Unlock more jobs"),    CONNECTED_CHARACTER: None},
            ARJ_STORY:          {QUEST_LINE: ARJ_QuestLineList,                 NAME: _("AmRose's story"),      CONNECTED_CHARACTER: "arj"},
            BG_STORY:           {QUEST_LINE: BG_quest_line_list,                NAME: _("Amore's story"),       CONNECTED_CHARACTER: "bg"},
            DC_STORY:           {QUEST_LINE: DC_quest_line_list,                NAME: _("Debbie's story"),      CONNECTED_CHARACTER: "dc"},
            KV_STORY:           {QUEST_LINE: KVQuestLineList,                   NAME: _("Kanya's story"),       CONNECTED_CHARACTER: "kv"},
            MAS_STORY:          {QUEST_LINE: MAS_quest_line_list,               NAME: _("Maya's story"),        CONNECTED_CHARACTER: "ms"},
            MH_STORY:           {QUEST_LINE: MH_quest_line_list,                NAME: _("Lyssa's story"),       CONNECTED_CHARACTER: "mh"},
            SY_STORY:           {QUEST_LINE: SYQuestLineList,                   NAME: _("Stacy's story"),       CONNECTED_CHARACTER: "sy"},
            MES_STORY:          {QUEST_LINE: MES_quest_line_list,               NAME: _("Min's story"),         CONNECTED_CHARACTER: "mes"},
            RD_STORY:           {QUEST_LINE: RD_quest_line_list,                NAME: _("Ridley's story"),      CONNECTED_CHARACTER: "rd"},
            MY_STORY:           {QUEST_LINE: MY_quest_line_list,                NAME: _("Melony's story"),      CONNECTED_CHARACTER: "my"},

        
            THEATER_STORY_LINE: {QUEST_LINE: TheatherUnlockQuestLineList,       NAME: _("Theater story"),       CONNECTED_CHARACTER: "th"},
            IT_STORY_LINE:      {QUEST_LINE: IT_job_quest_line_list,            NAME: _("Orbix story"),         CONNECTED_CHARACTER: "it"},
        
            AM_STORY:           {QUEST_LINE: AM_quest_line_list,                NAME: _("April's story"),       CONNECTED_CHARACTER: "am"},
            AG_STORY:           {QUEST_LINE: AG_quest_line_list,                NAME: _("Anna's story"),        CONNECTED_CHARACTER: "ag"},
            CW_STORY:           {QUEST_LINE: CW_quest_line_list,                NAME: _("Claire's story"),      CONNECTED_CHARACTER: "cw"},
            NS_STORY:           {QUEST_LINE: NS_quest_line_list,                NAME: _("Nari's story"),        CONNECTED_CHARACTER: "ns"},
        
            DVH_STORY:          {QUEST_LINE: DVH_quest_line_list,               NAME: _("Denise's story"),      CONNECTED_CHARACTER: "dvh"},
            KM_STORY:           {QUEST_LINE: KM_quest_line_list,                NAME: _("Kelly's story"),       CONNECTED_CHARACTER: "km"},
            TL_STORY:           {QUEST_LINE: TL_quest_line_list,                NAME: _("Taisia's story"),      CONNECTED_CHARACTER: "tl"},
            VS_STORY:           {QUEST_LINE: VS_quest_line_list,                NAME: _("Veronica's story"),    CONNECTED_CHARACTER: "vs"},

        
            MOVIE_PIRATES:     {QUEST_LINE: PiratesMovieQuestLineList,          NAME: _("Pirates Movie"),       CONNECTED_CHARACTER: "pmv"},
        }
