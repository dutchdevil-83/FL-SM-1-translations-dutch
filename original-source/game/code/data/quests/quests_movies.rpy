init python:
    sm_quest_list.update({
            "Q-MV01Q01"     : {STORY_LINE: MOVIE_PIRATES, EVENT: "event_mv01Q01", HINT: _("Talk to Stacy about the movie in the morning")},
            "Q-MV01Q02"     : {STORY_LINE: MOVIE_PIRATES, EVENT: "event_mv01Q02", SCHEDULE: {"tl": "Q-MV01Q02"}, HINT: ("hint_mv01Q02", [
                                                                                        _("Buy costumes and recruit actress for the movie"),
                                                                                        _("Choose whether to invest in costumes or recruit an actress first"),
                                                                                        _("Keep investing in the costume budget to prepare the outfits for the movie"),
                                                                                        _("Focus on recruiting an actress by filling the actress budget"),
                                                                                        _("Talk with stacy to buy costumes"),
                                                                                        _("Talk with stacy to hire actresses"),
                                                                                        _("Find Taisia and recruit her for the movie"),
                                                                                        ]), CHAR_INTR: {"sy": ["io-PIRATE_MOVIE_SCREEN", "io-MV01S02", "io-MV01S03_1"]}},
            "Q-MV01Q04"     : {STORY_LINE: MOVIE_PIRATES, HINT: _("Talk to Stacy about working on the movie"), CHAR_INTR: {"sy": ["io-PIRATE_MOVIE_SCREEN", "io-MV01S04"]}},
            "Q-MV01Q04_1"   : {STORY_LINE: MOVIE_PIRATES, EVENT: "event_mv01Q04_1", HINT: ("hint_mv01Q04_1", [
                                                                                        _("Add money for buying props and energy for building the props"),
                                                                                        _("Add money for buying props"),
                                                                                        _("Add energy for building the props"),
                                                                                        ]), CHAR_INTR: {"sy": "io-PIRATE_MOVIE_SCREEN"}},
            "Q-MV01Q04_2"   : {STORY_LINE: MOVIE_PIRATES, HINT: _("Talk with Stacy to finish building props"), CHAR_INTR: {"sy": ["io-PIRATE_MOVIE_SCREEN", "io-MV01S04_2"]}},
            "Q-MV01Q05"     : {STORY_LINE: MOVIE_PIRATES, HINT: _("Talk to Stacy in the Morning to start filming the movie"), CHAR_INTR: {"sy": ["io-PIRATE_MOVIE_SCREEN", "io-MV01S05"]}},
            "Q-MV01S06"     : {STORY_LINE: MOVIE_PIRATES, HINT: _("Wait to film next scene"), DAYS_PASSED: [{TARGET: "sm1mv01s05", DAYS: 1}], CHAR_INTR: {"sy": "io-PIRATE_MOVIE_SCREEN"},},
            "Q-MV01S06_2"   : {STORY_LINE: MOVIE_PIRATES, HINT: _("Talk with Taisia to start filming next scene"), CHAR_INTR: {"sy": "io-PIRATE_MOVIE_SCREEN", "tl": "io-MV01S06"}, SCHEDULE: {"tl": "Q-MV01S06_2"}},
            "Q-MV01S07"     : {STORY_LINE: MOVIE_PIRATES, HINT: _("Stacy wants to talk to you at Noon."), CHAR_INTR: {"sy": ["io-PIRATE_MOVIE_SCREEN", "io-MV01S07"]}},
            "Q-MV01S07_2"   : {STORY_LINE: MOVIE_PIRATES, EVENT: "event_mv01Q07", HINT: _("Add money for travel"), CHAR_INTR: {"sy": "io-PIRATE_MOVIE_SCREEN"}},
            "Q-MV01S07_3"   : {STORY_LINE: MOVIE_PIRATES, HINT: _("Talk with Taisia to travel"), CHAR_INTR: {"sy": "io-PIRATE_MOVIE_SCREEN", "tl": "io-MV01S07_3"}, SCHEDULE: {"tl": "Q-MV01S06_2"}},
            "Q-MV01Q11"     : {STORY_LINE: MOVIE_PIRATES, EVENT: "event_mv01Q11", HINT: _("Work on editing the movie"), CHAR_INTR: {"sy": "io-PIRATE_MOVIE_SCREEN"}},
            "Q-MV01Q11_2"   : {STORY_LINE: MOVIE_PIRATES, HINT: _("Talk with Stacy about the movie editing"), CHAR_INTR: {"sy": ["io-PIRATE_MOVIE_SCREEN", "io-MV01S11_2"], }},
            "Q-MV01Q12"     : {STORY_LINE: MOVIE_PIRATES, HIDDEN: True, AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},
        })



    PiratesMovieQuestLineList = [
            "Q-MV01Q01", "sm1mv01s01",
            "Q-MV01Q02",
            "Q-MV01Q04", "sm1mv01s04i", "Q-MV01Q04_1", "Q-MV01Q04_2", "sm1mv01s04_2i", "sm1mv01s04",
            "Q-MV01Q05", "sm1mv01s05i", "sm1mv01s05",
            "Q-MV01S06", "Q-MV01S06_2", "sm1mv01s06i", "sm1mv01s06",
            "Q-MV01S07", "sm1mv01s07i", "sm1mv01s07", "Q-MV01S07_2", "Q-MV01S07_3", "sm1mv01s07_2",
            "sm1mv01s08",
            "sm1mv01s09",
            "sm1mv01s10",
            "Q-MV01Q11", "Q-MV01Q11_2", "sm1mv01s11i",
            "Q-MV01Q12"
        ]
