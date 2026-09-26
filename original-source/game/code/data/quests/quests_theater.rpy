init python:
    sm_quest_list.update({
            "Q-FST001"      : {STORY_LINE: THEATER_STORY_LINE, HINT: _("Invite Stacy to Amusement Park during the day"), CHAR_INTR: {"sy": "io-FST001"}},
            "Q-FST002"      : {STORY_LINE: THEATER_STORY_LINE, HINT: _("Talk to Stacy during day timeslot to interview Taisia"), CHAR_INTR: {"sy": "io-FST002"}},
            "Q-FST002_01"   : {STORY_LINE: THEATER_STORY_LINE, HINT: _("Progress Main Storyline")}, 
            "Q-FST003"      : {STORY_LINE: THEATER_STORY_LINE, EVENT: "event_t003", HINT: _("Go to the Theater"), MAP_HINT: {THEATER: _("Go to the Theater for audition during the Day timeslot")}},
            "Q-FST004_1"    : {STORY_LINE: THEATER_STORY_LINE, EVENT: "event_t004_1", HINT: _("Progress the individual storylines for the Theater girls")}, 
            "Q-FST004_2"    : {STORY_LINE: THEATER_STORY_LINE, EVENT: "event_t004_2", HINT: _("Wait for one day")},
            "Q-FST004_3"    : {STORY_LINE: THEATER_STORY_LINE, EVENT: "event_t004_3", HINT: _("Talk to Denise")},
            "Q-FST005_1"    : {STORY_LINE: THEATER_STORY_LINE, EVENT: "event_t005_1", HINT: { "hint_t005_1_0": _("Progress Veronica and Kellie story line"),
                                                                        "hint_t005_1_1": _("Do Saturday show at least {}/3 times"),
                                                                        "hint_t005_1_2": _("Have {}/10 total Relationship Points with Theater girls"),
                                                                        "hint_t005_1_3": _("Do Saturday show at least {}/3 times and have {}/10 total Relationship Points with Theater girls"),
                                                                        DEFAULT: "Do Saturday show at least 3 times and have 10 total Relationship Points with Theater girls"}, },
            "Q-FST005_2"    : {STORY_LINE: THEATER_STORY_LINE, HINT: _("Read message from Denise"), CHAT: {"dvh": "sms-t005"}},
            "Q-FST005_3"    : {STORY_LINE: THEATER_STORY_LINE, EVENT: "event_t005_2", HINT: _("Visit Theater at Noon"), },
            "Q-FST006"      : {STORY_LINE: THEATER_STORY_LINE, HINT: _("This quest line will continue in the next release"), AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},

            "Q-KM001"       : {STORY_LINE: KM_STORY, EVENT: "event_talk_km_in_dressigroom", HINT: _("Talk to Kelly at her dressing room")},
            "Q-KM002_01"    : {STORY_LINE: KM_STORY, EVENT: "event_km002_01", HINT: _("Progress the Theater storyline")},
            "Q-KM002_02"    : {STORY_LINE: KM_STORY, EVENT: "event_km002_02", HINT: _("Wait for one day")},
            "Q-KM002_03"    : {STORY_LINE: KM_STORY, EVENT: "event_km002_03", HINT: _("Talk to Kellie on the stage")},
            "Q-KM003_01"    : {STORY_LINE: KM_STORY, EVENT: "event_km003_01", HINT: _("Buy the 'An Actor Prepares' book at the store"), CHAR_INTR: {"ic": "io-KM002_03"}},
            "Q-KM003_02"    : {STORY_LINE: KM_STORY, EVENT: "event_km003_02", HINT: _("Get your Literature to 5")},
            "Q-KM003_03"    : {STORY_LINE: KM_STORY, EVENT: "event_km003_03", HINT: _("Talk to Kellie on the stage")},
            "Q-KM003_2"     : {STORY_LINE: KM_STORY, HINT: _("Talk to Kellie on the stage"), CHAR_INTR: {"km": "io-KM003_2"} },
            "Q-KM004"       : {STORY_LINE: KM_STORY, HINT: _("Talk to Kellie"), CHAR_INTR: {"km": "io-KM004"}, RP_LIMIT: {"km": 10}},
            "Q-KM005_1"     : {STORY_LINE: KM_STORY, EVENT: "event_km005_1", HINT: _("Progress Veronica's story")},
            "Q-KM005_2"     : {STORY_LINE: KM_STORY, HINT: _("Text Kellie"), CHAT: {"km": "sms-km005"} },
            "Q-KM006"       : {STORY_LINE: KM_STORY, HINT: _("Progress Veronica's story line"), EVENT: "event_km006", },
            "Q-KM006_1"     : {STORY_LINE: KM_STORY, HINT: _("Talk to Veronica in the afternoon"), CHAR_INTR: {"vs": "io-KM006_1"} },
            "Q-KM006_2"     : {STORY_LINE: KM_STORY, HINT: _("Talk to Kellie in the afternoon at Theater"), CHAR_INTR: {"km": "io-KM006_2"} },
            "Q-KM007"       : {STORY_LINE: KM_STORY, HINT: _("This quest line is finished for this game"), AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},

            "Q-DVH001"      : {STORY_LINE: DVH_STORY, EVENT: "event_talk_dvh_in_office", HINT: _("Talk with Denise in her office")},
            "Q-DVH002"      : {STORY_LINE: DVH_STORY, HINT: _("This quest line will continue in the next release"), AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},

            "Q-TL001"       : {STORY_LINE: TL_STORY, HINT: _("Talk with Taisia about \"work\" during the day time"), CHAR_INTR: {"tl": "io-TL001"}},
            "Q-TL002"       : {STORY_LINE: TL_STORY, EVENT: "event_tl002", HINT: {"hint_tl002": _("Have ${}/$50 and talk with Taisia when she is in front of the stage"),
                                                                                    DEFAULT: _("Have $50 and talk with Taisia when she is in front of the stage")}},
            "Q-TL003"       : {STORY_LINE: TL_STORY, EVENT: "event_tl003", HINT: {"hint_tl003": _("Have ${}/$100 and invite Taisia to make a film"),
                                                                                    DEFAULT: _("Have $100 and invite Taisia to make a film")}},
            "Q-TL004"       : {STORY_LINE: TL_STORY, HINT: _("Wait a few days"), RP_LIMIT: {"tl": 7}, DAYS_PASSED: [{TARGET: "sm1cs_tl003", DAYS: 4}]},
            "Q-TL004_2"     : {STORY_LINE: TL_STORY, HINT: _("Talk with Taisia"), CHAR_INTR: {"tl": "io-TL004"}},
            "Q-TL005"       : {STORY_LINE: TL_STORY, HINT: _("Wait a few days"), DAYS_PASSED: [{TARGET: "sm1cs_tl004", DAYS: 1}]},
            "Q-TL005_2"     : {STORY_LINE: TL_STORY, HINT: _("Wait for a message from Taisia"), CHAT: {"tl": "sms-tl005"}},
            "Q-TL005_3"     : {STORY_LINE: TL_STORY, HINT: _("Answer Taisia")},
            "Q-TL006"       : {STORY_LINE: TL_STORY, HINT: _("Wait a few days"), DAYS_PASSED: [{TARGET: "sm1cs_tl005", DAYS: 2}]},
            "Q-TL006_2"     : {STORY_LINE: TL_STORY, HINT: _("Talk with Stacy about Taisia"), CHAR_INTR: {"sy": "io-TL006"}},
            "Q-TL006_3"     : {STORY_LINE: TL_STORY, HINT: _("Message Taisia to meet her with Stacy"), CHAT: {"tl": "sms-tl006"}},
            "Q-TL007"       : {STORY_LINE: TL_STORY, HINT: _("Talk with Taisia about moving in"), CHAR_INTR: {"tl": "io-TL007"} },
            "Q-TL007_2"     : {STORY_LINE: TL_STORY, HINT: _("Talk with Taisia about moving in after finishing the renovations"), CHAR_INTR: {"tl": "io-TL007_2"} },
            "Q-TL008_1"     : {STORY_LINE: TL_STORY, HINT: _("Wait a few days"), DAYS_PASSED: [{TARGET: "sm1cs_tl007", DAYS: 2}, {TARGET: "sm1ms023", DAYS: 1}]},
            "Q-TL008_2"     : {STORY_LINE: TL_STORY, HINT: _("Visit Taisia in her room in the evening"), EVENT: "event_tl008_2", SCHEDULE: {"tl":"Q-TL008_2"} },
            "Q-TL009"       : {STORY_LINE: TL_STORY, HINT: _("This quest line will continue in the next release"),  AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},

            "Q-VS001"       : {STORY_LINE: VS_STORY, EVENT: "event_vs001", HINT: _("Talk to Veronica at the Stage")},
            "Q-VS002_01"    : {STORY_LINE: VS_STORY, EVENT: "event_vs002_01", HINT: _("Talk to Veronica")},
            "Q-VS002_02"    : {STORY_LINE: VS_STORY, EVENT: "event_vs002_02", HINT: _("Buy the 'Stars Weekly' Magazin from the store"), CHAR_INTR: {"ic": "io-VS002_02"}},
            "Q-VS002_03"    : {STORY_LINE: VS_STORY, EVENT: "event_vs002_03", HINT: _("Get your Film and TV Topic to 3")},
            "Q-VS002_04"    : {STORY_LINE: VS_STORY, EVENT: "event_vs002_04", HINT: _("Progress Kellie's storyline")},
            "Q-VS002_05"    : {STORY_LINE: VS_STORY, EVENT: "event_vs002_05", HINT: _("Wait for one day")},
            "Q-VS002_06"    : {STORY_LINE: VS_STORY, EVENT: "event_vs002_06", HINT: _("Talk to Veronica on the Stage")},
            "Q-VS003"       : {STORY_LINE: VS_STORY, EVENT: "event_vs003", HINT: {"hint_vs003_challenge_day": _("Do the rehearsal on {}")}},
            "Q-VS004_1"     : {STORY_LINE: VS_STORY, EVENT: "event_vs004_1", HINT: _("Progress Kellie's story")},
            "Q-VS004_2"     : {STORY_LINE: VS_STORY, HINT: _("Wait for Veronica to text you"), CHAT: {"vs": "sms-vs004"}, RP_LIMIT: {"vs": 10} },
            "Q-VS004_3"     : {STORY_LINE: VS_STORY, HINT: _("Text Veronica"), },
            "Q-VS005"       : {STORY_LINE: VS_STORY, HINT: _("Talk with Veronica in the afternoon"), CHAR_INTR: {"vs": "io-VS005"} },
            "Q-VS006_1"     : {STORY_LINE: VS_STORY, HINT: _("This quest line is finished for this game"), AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},
        })



    TheatherUnlockQuestLineList = [
            "Q-FST001", "sm1fs_t001",
            "Q-FST002", "sm1fs_t002",
            "Q-FST002_01", "Q-FST003", "sm1fs_t003",
            "Q-FST004_1", "Q-FST004_2", "Q-FST004_3", "sm1fs_t004i", "sm1fs_t004",
            "Q-FST005_1", "Q-FST005_2", "Q-FST005_3", "sm1fs_t005",
            "Q-FST006",
        ]

    DVH_quest_line_list = [
            "Q-DVH001", "sm1cs_dvh001",
            "Q-DVH002",
        ]

    KM_quest_line_list = [
            "Q-KM001", "sm1cs_km001i", "sm1cs_km001",
            "Q-KM002_01", "Q-KM002_02", "Q-KM002_03", "sm1cs_km002",
            "Q-KM003_01", "Q-KM003_02", "Q-KM003_03", "sm1cs_km003",
            "Q-KM003_2", "sm1cs_km003_2i", "sm1cs_km003_2",
            "Q-KM004", "sm1cs_km004i", "sm1cs_km004",
            "Q-KM005_1", "Q-KM005_2", "sm1cs_km005",
            "Q-KM006", "Q-KM006_1", "sm1cs_km006_1i", "Q-KM006_2", "sm1cs_km006_2i", "sm1cs_km006",
            "Q-KM007",
        ]

    TL_quest_line_list = [
            "Q-TL001", "sm1cs_tl001i", "sm1cs_tl001",
            "Q-TL002", "sm1cs_tl002i", "sm1cs_tl002",
            "Q-TL003", "sm1cs_tl003i", "sm1cs_tl003",
            "Q-TL004", "Q-TL004_2", "sm1cs_tl004i", "sm1cs_tl004",
            "Q-TL005", "Q-TL005_2", "Q-TL005_3", "sm1cs_tl005",
            "Q-TL006", "Q-TL006_2", "sm1cs_tl006i", "Q-TL006_3", "sm1cs_tl006",
            "Q-TL007", "sm1cs_tl007i_1", "Q-TL007_2", "sm1cs_tl007i_2", "sm1cs_tl007",
            "Q-TL008_1", "Q-TL008_2", "sm1cs_tl008",
            "Q-TL009",
        ]

    VS_quest_line_list = [
            "Q-VS001", "sm1cs_vs001",
            "Q-VS002_01", "sm1cs_vs002i", "Q-VS002_02", "Q-VS002_03", "Q-VS002_04", "Q-VS002_05", "Q-VS002_06", "sm1cs_vs002",
            "Q-VS003", "sm1cs_vs003",
            "Q-VS004_1", "Q-VS004_2", "Q-VS004_3", "sm1cs_vs004",
            "Q-VS005", "sm1cs_vs005i", "sm1cs_vs005",
            "Q-VS006_1",
        ]
