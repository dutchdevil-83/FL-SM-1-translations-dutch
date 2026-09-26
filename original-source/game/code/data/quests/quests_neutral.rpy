init -1 python:
    sm_quest_list = {
            PAUSE           : {},
            WAITING         : {HINT: _("Progress other storylines")},
            END             : {},

            "Q-MS002-0"     : {STORY_LINE: MS, EVENT: "event_ms002_0", HINT: _("Open Map and go to Wurst Delivery")},
            "Q-MS002"       : {STORY_LINE: MS, EVENT: "event_ms002", HINT: _("Talk to Wurst Manager")},
            "Q-MS002-2"     : {STORY_LINE: MS, EVENT: "event_go_home", HINT: _("Go home")},
            "Q-MS002-3"     : {STORY_LINE: MS, EVENT: "event_q_ms002_3", HINT: _("Skip until night")},
            "Q-MS002-4"     : {STORY_LINE: MS, EVENT: "event_q_ms002_4", HINT: _("Go to sleep")},
            "Q-MS002-5"     : {STORY_LINE: MS, EVENT: "event_ms002_5", HINT: _("Work Wurst Delivery until you have $200")},
            "Q-MS002-6"     : {STORY_LINE: MS, EVENT: "event_ms002_6", HINT: _("Talk to Stacy when she is using her laptop"), SCHEDULE: {"sy": "Q-MS002-6_sy"}},
            "Q-MS003-3"     : {STORY_LINE: MS, EVENT: "event_talk_sy", HINT: _("Talk to Stacy during the evening"), SCHEDULE: {"sy": "Q-MS003-3_sy"}},
            "Q-MS004-2"     : {STORY_LINE: MS, EVENT: "event_go_home", HINT: _("Go home"), SCHEDULE: {"sy": "Q-MS004-2_sy"}},
            "Q-MS005"       : {STORY_LINE: MS, EVENT: "event_talk_sy_in_bed", HINT: _("Talk with Stacy when she is bed"), SCHEDULE: {"sy": "Q-MS005"}},
            "Q-MS011_i"     : {STORY_LINE: MORE_FACTIONS, HINT: _("Talk with Stacy about getting more jobs"), CHAR_INTR: {"sy": "io-MSI011-01"}},
            "Q-MS011_1"     : {STORY_LINE: MS, EVENT: "event_ms011_1", HINT: {"hint_ms011_it_job": _("Progress IT job's story line"),
                                                                                "hint_ms011_theater": _("Progress Theater job's story line"),
                                                                                DEFAULT: _("Progress IT and Theater job story lines")}},
            "Q-MS011"       : {STORY_LINE: MS, HINT: {"hint_ms011_post_it_job": _("Talk with Stacy about the IT job"),
                                                        DEFAULT: _("Talk with Stacy about the theater")}, CHAR_INTR: {"sy": "io-MSI011"}},
            "Q-MS006"       : {STORY_LINE: MS, EVENT: "event_ms006", HINT: _("Go To Sleep")},
            "Q-MS007"       : {STORY_LINE: MS, HINT: _("Go on a Date with Stacy"), CHAR_INTR: {"sy": "io-MS007"}},
            "Q-MS007_01"    : {STORY_LINE: MS, HINT: _("Give Stacy $50 for a wig"), CHAR_INTR: {"sy": "io-MS007_01i"}},
            "Q-MS008"       : {STORY_LINE: MS, HINT: _("Talk with Stacy after she buys a wig"), CHAR_INTR: {"sy": "io-MS008"}}, 
            "Q-MS009"       : {STORY_LINE: MS, HINT: _("Talk to Stacy about filming"), CHAR_INTR: {"sy": "io-MS009"}}, 
            "Q-MS010_1"     : {STORY_LINE: MS, EVENT: "event_ms010_1", HINT: _("Progress AmRose's Storyline")}, 
            "Q-MS010_2"     : {STORY_LINE: MS, EVENT: "event_ms010_2", HINT: _("Wait for one day")},
            "Q-MS010_3"     : {STORY_LINE: MS, HINT: _("Talk with Stacy about AmRose"), CHAR_INTR: {"sy": "io-MS010"}},
            "Q-MS012"       : {STORY_LINE: MS, HINT: _("Wait for Stacy to finish editing the film"), DAYS_PASSED: [{TARGET: "sm1ms010", DAYS: 3}]},
            "Q-MS012_2"     : {STORY_LINE: MS, HINT: _("Talk with Stacy in the morning"), CHAR_INTR: {"sy": "io-MS012_2"}},
            "Q-MS013"       : {STORY_LINE: MS, HINT: {"hint_ms013": _("Progress Taisia's story line"),
                                                        DEFAULT: _("Talk with Stacy during the day")}, CHAR_INTR: {"sy": "io-MS013"}},
            "Q-MS014"       : {STORY_LINE: MS, HINT: _("Talk with Stacy to start renovation"), CHAR_INTR: {"sy": "io-MS014"}},
        
            "Q-MS016"       : {STORY_LINE: MS, HINT: _("Work on renovation and visit one of your jobs with Stacy and Melony"), CHAR_INTR: {"sy": ["io-RENO", "io-MS015", "io-MS018"], "my": "io-RENO", "ns": "io-ns-RENO", "tl": "io-tl-RENO", "kv": "io-kv-RENO"}, SCHEDULE: {"sy": "sy_reno_base02", "my": "my_reno_base02"}},
            "Q-MS016_2"     : {STORY_LINE: MS, HINT: _("Work on renovation"), EVENT: "event_ms016_2", CHAR_INTR: {"sy": "io-RENO", "my": "io-RENO", "ns": "io-ns-RENO", "tl": "io-tl-RENO", "kv": "io-kv-RENO"}, SCHEDULE: {"sy": "sy_reno_base02", "my": "my_reno_base02"}},
            "Q-MS016_3"     : {STORY_LINE: MS, HINT: _("Talk with Stacy to install stairs"), CHAR_INTR: {"sy": "io-MS016_3"}, SCHEDULE: {"sy": "sy_reno_base02"}},
            "Q-MS019"       : {STORY_LINE: MS, HINT: _("Work on renovation and visit your other job with Stacy and Melony"), CHAR_INTR: {"sy": ["io-RENO", "io-MS015_2", "io-MS018_2"], "my": "io-RENO", "am": "io-am-RENO", "vs": "io-vs-RENO", "dc": "io-dc-RENO"}, SCHEDULE: {"sy": "sy_reno_base03", "my": "my_reno_base03"}},
            "Q-MS019_2"     : {STORY_LINE: MS, HINT: _("Work on renovation"), EVENT: "event_ms019_2", CHAR_INTR: {"sy": "io-RENO", "my": "io-RENO", "am": "io-am-RENO", "vs": "io-vs-RENO", "dc": "io-dc-RENO"}, SCHEDULE: {"sy": "sy_reno_base03", "my": "my_reno_base03"}},
            "Q-MS019_3"     : {STORY_LINE: MS, HINT: _("Talk with Stacy"), CHAR_INTR: {"sy": "io-MS019_3"}, SCHEDULE: {"sy": "sy_reno_base03", "my": "my_reno_base03"}},
            "Q-MS021_1"     : {STORY_LINE: MS, HINT: _("Wait a few days"), DAYS_PASSED: [{TARGET: "sm1ms020", DAYS: 2}]},
            "Q-MS021_2"     : {STORY_LINE: MS, HINT: _("Talk with Stacy during the day"), CHAR_INTR: {"sy": "io-MS021_2"}},
            "Q-MS021_3"     : {STORY_LINE: MS, HINT: _("Talk to Stacy at the studio at Morning"), CHAR_INTR: {"sy": "io-MS021_3"}},
        
            "Q-MS021_4"     : {STORY_LINE: MS, HINT: _("Have $200 and text Kanya"), CHAT: {"kv": "sms-ms021"}},
            "Q-MS022"       : {STORY_LINE: MS, HINT: _("Talk to Stacy about filming"), CHAR_INTR: {"sy": "io-MS022"}},
            "Q-MS023"       : {STORY_LINE: MS, HINT: _("Wait a few days"), DAYS_PASSED: {TARGET: "sm1ms022", DAYS: 2}},
            "Q-MS023_2"     : {STORY_LINE: MS, HINT: _("Talk to Stacy about editing during the day"), CHAR_INTR: {"sy": "io-MS023_2"}},
            "Q-MS023_3"     : {STORY_LINE: MS, HINT: _("Wait for Stacy to make editing progress"), DAYS_PASSED: {TARGET: "sm1ms023", DAYS: 2}},
            "Q-MS023_4"     : {STORY_LINE: MS, HINT: _("Talk to Stacy about editing again... during the day"), CHAR_INTR: {"sy": "io-MS023_4"}},
            "Q-MS024"       : {STORY_LINE: MS, HINT: _("Wait for Stacy to finish editing"), DAYS_PASSED: {TARGET: "sm1ms023_02", DAYS: 2}},
            "Q-MS024_2"     : {STORY_LINE: MS, HINT: _("Talk to Stacy"), CHAR_INTR: {"sy": "io-MS024_2"}},
            "Q-MS025"       : {STORY_LINE: MS, HINT: _("Talk to Stacy about new order from the client"), CHAR_INTR: {"sy": "io-MS025"}},
            "Q-MS025"       : {STORY_LINE: MS, HINT: _("Talk to Stacy about new order from the client"), CHAR_INTR: {"sy": "io-MS025"}},
            "Q-MS026"       : {STORY_LINE: MS, HINT: {"hint_ms026": _("Progress Taisia's story line"),
                                                        DEFAULT: _("Talk to Stacy about the new movie")}, CHAR_INTR: {"sy": "io-MS026"}},
            "Q-MS027"       : {STORY_LINE: MS, HINT: _("Film and release the new movie"), EVENT: "event_ms027"},
            "Q-MS027_2"     : {STORY_LINE: MS, HINT: _("Wait for Stacy to launch the website"), EVENT: "event_ms027_2"},
            "Q-MS028"       : {STORY_LINE: MS, HINT: _("This quest line will continue in the next release"), AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},

        
            "Q-SY001"       : {STORY_LINE: SY_STORY, EVENT: "event_q_sy001", SCHEDULE: {"sy": "Q-SY001"}, HIDDEN: True},
            "Q-SY002_1"     : {STORY_LINE: SY_STORY, EVENT: "event_sy002_1", AUTO_UNTRACK: True, HIDDEN: True},
            "Q-SY002_2"     : {STORY_LINE: SY_STORY, EVENT: "event_sy002_2", AUTO_UNTRACK: True, HIDDEN: True, CHAR_INTR: {"sy": "io-SY002_2"}},
            "Q-SY003"       : {STORY_LINE: SY_STORY, AUTO_UNTRACK: True, HIDDEN: True, CHAR_INTR: {"sy": ["io-SY002_2", "io-SY003"]}},
        

        
            "Q-KV000"       : {STORY_LINE: KV_STORY, HINT: _("Talk with Stacy about the camera girl"), CHAR_INTR: {"sy": "io-KV000i"}},
            "Q-KV001"       : {STORY_LINE: KV_STORY, EVENT: "event_enter_photo_dojo", HINT: _("Find Kanya at Photo Dojo"), MAP_HINT: {PHOTO_DOJO: _("Find Kanya at Photo Dojo")}},
            "Q-KV002_01"    : {STORY_LINE: KV_STORY, EVENT: "event_enter_71_store", HINT: _("Go to General Store")},
            "Q-KV002_02"    : {STORY_LINE: KV_STORY, EVENT: "event_kv002_02", HINT: _("Purchase Photography-101"), CHAR_INTR: {"ic": "io-KV002_02"}},
            "Q-KV002_03"    : {STORY_LINE: KV_STORY, EVENT: "event_kv002_03", HINT: _("Read the book on your couch")},
            "Q-KV002_04"    : {STORY_LINE: KV_STORY, EVENT: "event_kv002_04", HINT: {"hint_kv002_04": _("Learn Photography until you have 5 in this topic (current {})"),
                                                                                    DEFAULT: _("Learn Photography until you have 5 in this topic")}},
            "Q-KV002_05"    : {STORY_LINE: KV_STORY, EVENT: "event_enter_photo_dojo", HINT: _("Visit Kanya in Photo Dojo")},
            "Q-KV003"       : {STORY_LINE: KV_STORY, HINT: _("Talk with Stacy in the morning about your visit to Kanya"), CHAR_INTR: {"sy": "io-KV003"}},
            "Q-KV004"       : {STORY_LINE: KV_STORY, HINT: {"hint_kv004_lyssa": _("Get help with legal documents from Lyssa"),
                                                            DEFAULT: _("Talk about getting Legal Advice with Stacy")}},
            "Q-KV004_1"     : {STORY_LINE: KV_STORY, EVENT: "event_enter_photo_dojo", HINT: _("Visit Kanya")}, 
            "Q-KV004_2"     : {STORY_LINE: KV_STORY, HINT: _("Talk to Kanya about 'practice'"), HIDDEN: True, CHAR_INTR: {"kv": "io-KV004_2"}}, 
            "Q-KV005_1"     : {STORY_LINE: KV_STORY, EVENT: "event_kv005_1", HINT: _("Wait a few days")},
            "Q-KV005_2"     : {STORY_LINE: KV_STORY, HINT: _("Talk with Kanya to learn more about Photography"), SCHEDULE_CONDITION: "event_kv005_2", SCHEDULE: {"kv": "Q-KV005"}, CHAR_INTR: {"kv": "io-KV005"}},
            "Q-KV006"       : {STORY_LINE: KV_STORY, HINT: _("This quest line will continue in the next release"), AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},
        
            "Q-ARJ001_1"    : {STORY_LINE: ARJ_STORY, EVENT: "event_arj001_1", HIDDEN: True}, 
            "Q-ARJ001_2"    : {STORY_LINE: ARJ_STORY, HINT: _("Talk with Stacy about the USB drive"), CHAR_INTR: {"sy": "io-ARJ001"}}, 
            "Q-ARJ001_3"    : {STORY_LINE: ARJ_STORY, EVENT: "event_arj001_3", HINT: _("Go to Starducks in the morning")}, 
            "Q-ARJ002_1"    : {STORY_LINE: ARJ_STORY, EVENT: "event_arj002" , HINT: _("Progress Main Story")}, 
            "Q-ARJ002_2"    : {STORY_LINE: ARJ_STORY, HINT: _("This quest line will continue in the next release"), AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},
        
            "Q-BG001"       : {STORY_LINE: BG_STORY, EVENT: "event_bg001", HINT: _("Go to the Photodojo to talk with the BDSM girl")},
            "Q-BG002"       : {STORY_LINE: BG_STORY, EVENT: "event_bg002", HINT: _("Talk to Amore in the Photodojo"), SCHEDULE_CONDITION: "event_bg002_time", SCHEDULE: {"bg": "Q-BG002", "kv": "Q-BG002_KV"}},
            "Q-BG003"       : {STORY_LINE: BG_STORY, HINT: _("Talk to Amore about the photos"), CHAR_INTR: {"bg": "io-BG003"}, SCHEDULE_CONDITION: "event_bg003_time", SCHEDULE: {"bg": "Q-BG002", "kv": "Q-BG003_KV"}},
            "Q-BG004"       : {STORY_LINE: BG_STORY, EVENT: "event_bg004", HINT: {"hint_bg004": _("Wait a few days"),
                                                                                            DEFAULT :_("Visit the Photodojo")}},
            "Q-BG005"       : {STORY_LINE: BG_STORY, HINT: _("This quest line will continue in the next release"), AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},
        
            "Q-MAS001_1"    : {STORY_LINE: MAS_STORY, EVENT: "event_mas001_1", HIDDEN: True }, 
            "Q-MAS001_2"    : {STORY_LINE: MAS_STORY, EVENT: "event_mas001_2", HINT: _("Go to Wurst Delivery during the day"), RP_LIMIT: {"ms": 8}}, 
            "Q-MAS002"      : {STORY_LINE: MAS_STORY, EVENT: "event_mas002", HINT: _("Get 6 Relationship points with Maya and talk to her in Wurst Delivery")}, 
            "Q-MAS003"      : {STORY_LINE: MAS_STORY, EVENT: "event_mas003", HINT: {"hint_mas003": _("Get {}/9 Relationship points with Maya"),
                                                                                    DEFAULT: _("Visit Wurst Delivery in the evening")}, RP_LIMIT: {"ms": 12}},
            "Q-MAS004"      : {STORY_LINE: MAS_STORY, HINT: _("This quest line will continue in the next release"), RP_LIMIT: {"ms": 14}, AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},
        
            "Q-MH001"       : {STORY_LINE: MH_STORY,  CHAR_INTR: {"sy": "io-MH001"}, HIDDEN: True},
            "Q-MH002-00"    : {STORY_LINE: MH_STORY,  HINT: _("Talk with Stacy about going to Lyssa during the day timeslot"), CHAR_INTR: {"sy": "io-MH002-00"}},
            "Q-MH003"       : {STORY_LINE: MH_STORY,  HINT: _("Talk with Stacy about Lyssa during the day timeslot"), CHAR_INTR: {"sy": "io-MH003"}},
            "Q-MH003-01"    : {STORY_LINE: MH_STORY,  LOC_INTR: {"lly_sin_03_overview": "io-MH003_01"}, AUTO_UNTRACK: True, HIDDEN: True},
            "Q-MH003-02"    : {STORY_LINE: MH_STORY,  HINT: _("Talk with Stacy about your date with Lyssa"), CHAR_INTR: {"sy": "io-MH003_02"}},
            "Q-MH004"       : {STORY_LINE: MH_STORY,  EVENT: "event_mh004", HINT: _("Take Lyssa out for a nice Dinner"), LOC_INTR: {"lly_sin_03_overview": "io-lly-Q-MH004"}, MAP_HINT: {LYSSAS_HOUSE: _("Go to Lyssa's House during evening timeslot")}},
            "Q-MH004-01"    : {STORY_LINE: MH_STORY,  HINT: _("Tell Stacy about your date with Lyssa"), CHAR_INTR: {"sy": "io-MH004_01"}},
            "Q-MH005"       : {STORY_LINE: MH_STORY,  EVENT: "event_mh_005", HINT: _("Take Lyssa out for the next date in the evening"),  MAP_HINT: {LYSSAS_HOUSE: _("Go to Lyssa's House during evening timeslot")}},
            "Q-MH006"       : {STORY_LINE: MH_STORY,  EVENT: "event_mh_006", HINT: _("Take Lyssa out for another date"), MAP_HINT: {LYSSAS_HOUSE: _("Go to Lyssa's House during evening timeslot")}},
            "Q-MH007"       : {STORY_LINE: MH_STORY,  HINT: _("Wait a few days"), DAYS_PASSED: {TARGET: "sm1cs_mh006", DAYS: 4}},
            "Q-MH007_2"     : {STORY_LINE: MH_STORY,  HINT: _("Wait for Lyssa's message"), CHAT: {"mh": "sms-mh007"}},
            "Q-MH007_3"     : {STORY_LINE: MH_STORY,  HINT: _("Answer Lyssa's message")},
            "Q-MH008"       : {STORY_LINE: MH_STORY,  HINT: _("Finish renovation"), EVENT: "event_renovation_finished"},
            "Q-MH008_2"     : {STORY_LINE: MH_STORY,  HINT: _("Wait a few days"), DAYS_PASSED: {TARGET: "sm1ms020", DAYS: 3}},
            "Q-MH008_3"     : {STORY_LINE: MH_STORY,  HINT: _("Visit Lyssa in the afternoon"), EVENT: "event_mh_008_3", },
            "Q-MH009"       : {STORY_LINE: MH_STORY,  HINT: _("Wait for Lyssa's message"), CHAT: {"mh": "sms-mh009"}},
            "Q-MH009_2"     : {STORY_LINE: MH_STORY,  HINT: _("Invite Lyssa to visit studio"),},
            "Q-MH010"       : {STORY_LINE: MH_STORY,  HINT: _("This quest line will continue in the next release"),  AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},
        
            "Q-DC001"       : {STORY_LINE: DC_STORY,  EVENT: "event_dc001", HIDDEN: True},
            "Q-DC002"       : {STORY_LINE: DC_STORY,  EVENT: "event_dc002", HINT: _("Look out for the shady guy in the park at night")},
            "Q-DC003"       : {STORY_LINE: DC_STORY,  EVENT: "event_dc003", HINT: _("Talk to Debbie in the park during the day")},
            "Q-DC004_01"    : {STORY_LINE: DC_STORY,  EVENT: "event_dc004_01", HINT: _("Wait a few days")},
            "Q-DC004_02"    : {STORY_LINE: DC_STORY,  EVENT: "event_dc004_02", HINT: _("Talk to Debbie in the Park during the day")},
            "Q-DC005"       : {STORY_LINE: DC_STORY,  HINT: _("Wait for few days"), DAYS_PASSED: {TARGET: "sm1cs_dc004", DAYS: 2}},
            "Q-DC005_2"     : {STORY_LINE: DC_STORY,  HINT: _("Talk to Debbie"), CHAR_INTR: {"dc": "io-DC005_2"}}, 
            "Q-DC006"       : {STORY_LINE: DC_STORY,  HINT: _("Wait for a day"), DAYS_PASSED: {TARGET: "sm1cs_dc005i", DAYS: 1}},
            "Q-DC006_2"     : {STORY_LINE: DC_STORY,  HINT: _("Talk to Debbie in the evening"), CHAR_INTR: {"dc": "io-DC006_2"}},
        
            "Q-DC007_1"     : {STORY_LINE: DC_STORY,  HINT: _("Wait for Debbie to message you"), DAYS_PASSED: {TARGET: "sm1cs_dc006", DAYS: 2}, OFFRAMP: {"sm1cs_dc006_offramp" : {CHAR_INTR: {"dc": "io-DC007_1_offramp"}}}},
            "Q-DC007_2"     : {STORY_LINE: DC_STORY,  HINT: _("Wait for Debbie to message you"), CHAT: {"dc": "sms-dc007"}, SILENT_QUEST: True},
            "Q-DC007_3"     : {STORY_LINE: DC_STORY,  HINT: _("Answer Debbie")},
            "Q-DC007_4"     : {STORY_LINE: DC_STORY,  EVENT: "event_dc007_4", HINT: _("Find Debbie in the park at nightfall")},
            "Q-DC008"       : {STORY_LINE: DC_STORY,  HINT: _("Text Debbie"), DAYS_PASSED: {TARGET: "sm1cs_dc007", DAYS: 2}},
            "Q-DC008_2"     : {STORY_LINE: DC_STORY,  HINT: _("Text Debbie"), CHAT: {"dc": "sms-dc008"}},
            "Q-DC009"       : {STORY_LINE: DC_STORY,  HINT: _("This quest line will continue in the next release"),  AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},

        
            "Q-MES001"      : {STORY_LINE: MES_STORY, EVENT: "event_mes001", SCHEDULE: {"mes": "sm1cs_mes001"}, HIDDEN: True},
            "Q-MES002"      : {STORY_LINE: MES_STORY, HINT: _("Talk with Stacy about Min"), CHAR_INTR: {"sy": "io-MES002"}},
            "Q-MES003_1"    : {STORY_LINE: MES_STORY, HINT: _("Finish renovation to invite Min"), DAYS_PASSED: {TARGET: "sm1ms020", DAYS: 1}},
            "Q-MES003_2"    : {STORY_LINE: MES_STORY, HINT: _("Text Min"), CHAT: {"mes": "sms-mes003"}},
            "Q-MES004"      : {STORY_LINE: MES_STORY,  HINT: _("Get to 3 relationship points with Min"), EVENT: "event_mes004_1" },
            "Q-MES004_2"    : {STORY_LINE: MES_STORY,  HINT: _("Wait for Min to text you"), CHAT: {"mes": "sms-mes004"}},
            "Q-MES004_3"    : {STORY_LINE: MES_STORY,  HINT: _("Answer Min"), RP_LIMIT: {"mes": 10} },
            "Q-MES005_1"    : {STORY_LINE: MES_STORY,  HINT: _("Get to 5 relationship points with Min"), EVENT: "event_mes005_1" },
            "Q-MES005_2"    : {STORY_LINE: MES_STORY,  HINT: _("Talk with Min in a bar"), EVENT: "event_mes005_2" },
            "Q-MES006"      : {STORY_LINE: MES_STORY,  HINT: _("This quest line will continue in the next release"),  AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},

        
            "Q-MY001_1"     : {STORY_LINE: MY_STORY, HINT: _("Text Melony"), CHAT: {"my": "sms-my001"}, SCHEDULE: {"my":"q_my001"}},
            "Q-MY001_2"     : {STORY_LINE: MY_STORY, HINT: _("Talk with Stacy before going with Melony"), CHAR_INTR: {"sy": "io-MY001_2"}, SCHEDULE: {"my":"q_my001"}},
            "Q-MY002"       : {STORY_LINE: MY_STORY, RP_LIMIT: {"my": 10}, HINT: _("Talk with Stacy"), CHAR_INTR: {"sy": "io-MY002"}},
            "Q-MY003"       : {STORY_LINE: MY_STORY, HINT: _("Wait a few days"), DAYS_PASSED: {TARGET: "sm1ms022", DAYS: 2}},
            "Q-MY003_2"     : {STORY_LINE: MY_STORY, HINT: _("Talk with Stacy"), CHAR_INTR: {"sy": "io-MY003_2"},},
            "Q-MY004"       : {STORY_LINE: MY_STORY, HINT: _("This quest line will continue in the next release"),  AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True},

        
            "Q-RD000"       : {STORY_LINE: RD_STORY,  EVENT: "event_rd_000",  HINT: _("Meet Ridley"), HIDDEN: True},
            "Q-RD001"       : {STORY_LINE: RD_STORY,  HINT: _("This quest line will continue in the next release"),  AUTO_UNTRACK: True, CURRENT_QUEST_LINE_END: True, HIDDEN: True},
        }



    MSQuestLineList = [
            "sm1ms001", "Q-MS002-0", "Q-MS002",
            "sm1cs_nr001i",
            "Q-MS002-2", "Q-MS002-3", "sm1ms001_02",
            "Q-MS002-4", "Q-MS002-5", "Q-MS002-6",
            "sm1ms002", PAUSE,
            "Q-MS003-3",
            "sm1ms003", PAUSE,
            "Q-MS004-2", "sm1ms004", "sm1ms011", PAUSE,
            "Q-MS002-6", "sm1ms002", PAUSE,
            "Q-MS005", "sm1ms005_01i", "sm1ms005",
            "Q-MS006", "sm1ms006",
            "Q-MS011_1", "Q-MS011", "sm1ms011_02i",
            "Q-MS007", "sm1ms007",
            "Q-MS007_01", "sm1ms007_01i",
            "Q-MS008", "sm1ms008_01i", "sm1ms008",
            "Q-MS009", "sm1ms009_01i", "sm1ms009",
            "Q-MS010_1" , "Q-MS010_2", "Q-MS010_3", "sm1ms010i", "sm1ms010",
            "Q-MS012", "Q-MS012_2", "sm1ms012i", "sm1ms012",
            "Q-MS013", "sm1ms013i", "sm1ms013",
            "Q-MS014", "sm1ms014i", "sm1ms014",
            "Q-MS016", "sm1ms015_18_first", "Q-MS016_2", "Q-MS016_3", "sm1ms016", "sm1ms017",
            "Q-MS019", "sm1ms015_18_second", "Q-MS019_2", "Q-MS019_3", "sm1ms019i", "sm1ms019", "sm1ms020", "sm1cs_sy003",
            "Q-MS021_1", "Q-MS021_2", "sm1ms021", "Q-MS021_3", "sm1ms021i", "Q-MS021_4",
            "Q-MS022", "sm1ms022i", "sm1ms022",
            "Q-MS023", "Q-MS023_2", "sm1ms023i", "sm1ms023", "Q-MS023_3", "Q-MS023_4", "sm1ms023_02i", "sm1ms023_02",
            "Q-MS024", "Q-MS024_2", "sm1ms024i", "sm1ms024",
            "Q-MS025", "sm1ms025i", "sm1ms025",
            "Q-MS026", "sm1ms026i", "sm1ms026",
            "Q-MS027", "Q-MS027_2", "sm1ms027",
            "Q-MS028",
        ]

    UnlockMoreFactionsQuestLineList = [
            "Q-MS011_i", "sm1ms011_01i", PAUSE,
            "Q-MS011_i", "sm1ms011_01i", PAUSE,
            "Q-MS011_i", "sm1ms011_01i", PAUSE,
        ]


    KVQuestLineList = [
            "Q-KV000", "sm1cs_kv000i",
            "Q-KV001", "sm1cs_kv001",
            "Q-KV002_01", "Q-KV002_02", "Q-KV002_03", "Q-KV002_04", "Q-KV002_05", "sm1cs_kv002",
            "Q-KV003", "sm1cs_kv003",
            "Q-KV004", "Q-KV004_1", "sm1cs_kv004", "Q-KV004_2",
            "Q-KV005_1", "Q-KV005_2", "sm1cs_kv005i",
            "Q-KV006",
        ]

    SYQuestLineList = [
            "Q-SY001", "sm1cs_sy001",
            "Q-SY002_1", "Q-SY002_2",
            "Q-SY003",
        ]

    ARJ_QuestLineList = [
            "Q-ARJ001_1", "Q-ARJ001_2", "sm1cs_arj001i", "Q-ARJ001_3",  "sm1cs_arj001",
            "Q-ARJ002_1", "Q-ARJ002_2",
        ]

    MH_quest_line_list = [
            "Q-MH001", "sm1cs_mh001i",
            "Q-MH002-00", "sm1cs_mh002_00i",
            "sm1cs_mh002",
            "Q-MH003", "sm1cs_mh003i", "sm1cs_mh003",
            "Q-MH003-01",
            "Q-MH003-02", "sm1cs_mh004i",
            "Q-MH004", "sm1cs_mh004",
            "Q-MH004-01", "sm1cs_mh004_01i",
            "Q-MH005", "sm1cs_mh005i", "sm1cs_mh005",
            "Q-MH006", "sm1cs_mh006i", "sm1cs_mh006",
            "Q-MH007", "Q-MH007_2", "Q-MH007_3", "sm1cs_mh007",
            "Q-MH008", "Q-MH008_2", "Q-MH008_3", "sm1cs_mh008",
            "Q-MH009", "Q-MH009_2", "sm1cs_mh009",
            "Q-MH010",
        ]

    DC_quest_line_list = [
            "Q-DC001", "sm1cs_dc001i",
            "Q-DC002", "sm1cs_dc002",
            "Q-DC003", "sm1cs_dc003i", "sm1cs_dc003",
            "Q-DC004_01", "Q-DC004_02", "sm1cs_dc004i", "sm1cs_dc004",
            "Q-DC005", "Q-DC005_2", "sm1cs_dc005i",
            "Q-DC006", "Q-DC006_2", "sm1cs_dc006i", "sm1cs_dc006",
            "Q-DC007_1", "Q-DC007_2", "Q-DC007_3", "Q-DC007_4", "sm1cs_dc007",
            "Q-DC008", "Q-DC008_2", "sm1cs_dc008",
            "Q-DC009",
        ]

    BG_quest_line_list = [
            "Q-BG001", "sm1cs_bg001",
            "Q-BG002", "sm1cs_bg002i", "sm1cs_bg002",
            "Q-BG003", "sm1cs_bg003i", "sm1cs_bg003",
            "Q-BG004", "sm1cs_bg004",
            "Q-BG005",

        ]

    MAS_quest_line_list = [
            "Q-MAS001_1", "Q-MAS001_2", "sm1cs_mas001",
            "Q-MAS002", "sm1cs_mas002",
            "Q-MAS003", "sm1cs_mas003",
            "Q-MAS004",
        ]

    MES_quest_line_list = [
            "Q-MES001", "sm1cs_mes001",
            "Q-MES002", "sm1cs_mes002i",
            "Q-MES003_1", "Q-MES003_2", "sm1cs_mes003",
            "Q-MES004", "Q-MES004_2", "Q-MES004_3", "sm1cs_mes004",
            "Q-MES005_1", "Q-MES005_2", "sm1cs_mes005",
            "Q-MES006",
        ]

    MY_quest_line_list = [
            "Q-MY001_1", "Q-MY001_2", "sm1cs_my001i", "sm1cs_my001",
            "Q-MY002", "sm1cs_my002i", "sm1cs_my002",
            "Q-MY003", "Q-MY003_2", "sm1cs_my003i", "sm1cs_my003",
            "Q-MY004",
        ]

    RD_quest_line_list =[
            "Q-RD000", "sm1cs_rd001i",
            "Q-RD001"
        ]
