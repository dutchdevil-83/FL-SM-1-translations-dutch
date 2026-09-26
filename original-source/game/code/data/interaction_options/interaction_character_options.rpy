init 1 python:
    INTERACTIONS_CHARACTER_CATALOGUE = {
            "io-QuickInteraction": {
                NAME: _("Talk"),
                ACTION: QUICK,
                DAILY_LIMIT: QUICK,
                },
            "io-Sleep": {
                NAME: _("Go to sleep"),
                ACTION: FUNCTION,
                TARGET: SMPlayer.sleep,
                TIMESLOTS: [TIMESLOT_1, TIMESLOT_2]
                },
            WORK_WURST: {
                NAME: _("Work Wurst delivery"),
                ACTION: "call",
                TARGET: "play_wurst_delivery",
                ENERGY_LIMIT: WURST_DELIVERY_ENERGY_COST
                },
            "io-Watch_Pee": {
                NAME: _("Watch her pee..."),
                ACTION: CALL,
                TARGET: "sm1cs_##interaction_character.codename##_pee01",
                DAILY_LIMIT: "##interaction_character.codename##_pee",
                LOCATION: [STUDIO],
            
            
                },


            "io-MS005": {
                NAME: _("Talk"),
                ACTION: QUICK
                },
            "io-MS007": {
                NAME: _("Go on a Date"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DAYS_PASSED: [{TARGET: "sm1cs_kv003", DAYS: 0}, {TARGET: "sm1ms011_02i", DAYS: 1}],
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6]
                },
            "io-MS007_01i": {
                NAME: _("Give Stacy money for a wig"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                NEED_MONEY: 50,
                DAYS_PASSED: {TARGET: "sm1ms007", DAYS: 1},
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8]
                },
            "io-MS008": {
                NAME: _("Go to Kanya with the wig"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DAYS_PASSED: {TARGET: "sm1ms007_01i", DAYS: 1},
                DISABLED_BY_CONDITION: "interaction_is_disabled_ms008",
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8]
                },
            "io-MS009": {
                NAME: _("Talk about filming"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DAYS_PASSED: {TARGET: "sm1ms008", DAYS: 1},
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8]
                },
            "io-MS010": {
                NAME: _("Talk about AmRose"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                DAYS: [MONDAY, WEDNESDAY, FRIDAY, SATURDAY, SUNDAY],
                },
            "io-MSI011-01": {
                NAME: _("Talk about finding more jobs"),
                ACTION: PROGRESS_STORY,
                TARGET: MORE_FACTIONS,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8],
                },
            "io-MSI011": {
                NAME: _("Talk about your job progress"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6],
                },
            "io-ARJ001": {
                NAME: _("About that USB drive"),
                ACTION: PROGRESS_STORY,
                TARGET: ARJ_STORY,
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                DAYS_PASSED: {TARGET: "sm1ms008", DAYS: 1},
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4]
                },
            "io-MS012_2":{
                NAME: _("Talk about the film"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                },
            "io-MS013":{
                NAME: _("Answer booty call"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DAYS_PASSED: [{TARGET: "sm1ms012", DAYS: 1}, {TARGET:"sm1cs_tl002", DAYS: 0}],
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-MS014": {
                NAME: _("Start renovation!"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                NEED_MONEY: 300,
                DAYS_PASSED: {TARGET: "sm1ms013", DAYS: 1},
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                },
            "io-RENO": {
                NAME: _("Do renovation work"),
                ACTION: JUMP,
                TARGET: "renovation_screen",
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8]
                },
            "io-MS015": {
                NAME: _("Visit Orbix"),
                ACTION: [SET_CHOICE, PROGRESS_STORY],
                TARGET: MS,
                CHOICE_NAME: "io_MS015_first",
                DAYS_PASSED: {TARGET: "sm1ms014", DAYS: 1},
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                DAYS: [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY],
                },
            "io-MS015_2": {
                NAME: _("Visit Orbix"),
                ACTION: [SET_CHOICE, PROGRESS_STORY],
                TARGET: MS,
                CHOICE_NAME: "io_MS015_second",
                DAYS_PASSED: {TARGET: "sm1ms017", DAYS: 1},
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                HIDDEN_BY_CONDITION: "io_is_hidden_MS015",
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                DAYS: [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY],
                },
            "io-ns-RENO": {
                NAME: _("Ask for help with renovation"),
                ACTION: [SET_CHOICE, CALL],
                TARGET: "sm1cs_ns_renovation",
                CHOICE_NAME: "io_ns_renovation",
                HIDDEN_BY_CONDITION: "io_is_hidden_NS_RENO",
                DAYS_PASSED: {TARGET: "sm1cs_ns010", DAYS: 0},
                LOCATION: [IT_OFFICE],
                DISABLED_BY_POSE: NS_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                DAYS: [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY],
                },
            "io-tl-RENO": {
                NAME: _("Ask for help with renovation"),
                ACTION: [SET_CHOICE, CALL],
                TARGET: "sm1cs_tl_renovation_i",
                CHOICE_NAME: "io_tl_renovation",
                HIDDEN_BY_CONDITION: "io_is_hidden_TL_RENO",
                DAYS_PASSED: {TARGET: "sm1cs_tl006", DAYS: 0},
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-kv-RENO": {
                NAME: _("Ask for help with renovation"),
                ACTION: [SET_CHOICE, CALL],
                TARGET: "sm1cs_kv_renovation",
                CHOICE_NAME: "io_kv_renovation",
                HIDDEN_BY_CONDITION: "io_is_hidden_KV_RENO",
                DAYS_PASSED: {TARGET: "sm1cs_kv005i", DAYS: 0},
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-MS016_3": {
                NAME: _("Assemble stairs"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-MS018": {
                NAME: _("Visit Theater"),
                ACTION: [SET_CHOICE, PROGRESS_STORY],
                TARGET: MS,
                CHOICE_NAME: "io_MS018_first",
                DAYS_PASSED: {TARGET: "sm1ms014", DAYS: 1},
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6],
                DAYS: [TUESDAY, WEDNESDAY, FRIDAY, SATURDAY, SUNDAY],
                },
            "io-MS018_2": {
                NAME: _("Visit Theater"),
                ACTION: [SET_CHOICE, PROGRESS_STORY],
                TARGET: MS,
                CHOICE_NAME: "io_MS018_second",
                DAYS_PASSED: {TARGET: "sm1ms017", DAYS: 1},
                DISABLED_BY_POSE: ["masturbateclown", "shower01"],
                HIDDEN_BY_CONDITION: "io_is_hidden_MS018",
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6],
                DAYS: [TUESDAY, WEDNESDAY, FRIDAY, SATURDAY, SUNDAY],
                },
            "io-am-RENO": {
                NAME: _("Ask for help with renovation"),
                ACTION: [SET_CHOICE, CALL],
                TARGET: "sm1cs_am_renovation",
                CHOICE_NAME: "io_am_renovation",
                HIDDEN_BY_CONDITION: "io_is_hidden_AM_RENO",
                DAYS_PASSED: {TARGET: "sm1cs_am005", DAYS: 0},
                LOCATION: [IT_OFFICE],
                DISABLED_BY_POSE: AM_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                DAYS: [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY],
                },
            "io-vs-RENO": {
                NAME: _("Ask for help with renovation"),
                ACTION: [SET_CHOICE, CALL],
                TARGET: "sm1cs_vs_renovation",
                CHOICE_NAME: "io_vs_renovation",
                HIDDEN_BY_CONDITION: "io_is_hidden_VS_RENO",
                DAYS_PASSED: {TARGET: "sm1cs_vs003", DAYS: 0},
                LOCATION: [THEATER],
                DISABLED_BY_POSE: VS_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-dc-RENO": {
                NAME: _("Ask for help with renovation"),
                ACTION: [SET_CHOICE, CALL],
                TARGET: "sm1cs_dc_renovation_i",
                CHOICE_NAME: "io_dc_renovation",
                HIDDEN_BY_CONDITION: "io_is_hidden_DC_RENO",
                DAYS_PASSED: {TARGET: "sm1cs_dc007", DAYS: 0},
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-MS019_3": {
                NAME: _("Are we done?"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-MS021_3": {
                NAME: _("Let's start working!"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                },
            "io-MS021_2": {
                NAME: _("Ready for next adventure!"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                NEED_MONEY: 200,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-MS022": {
                NAME: _("Talk about Filming"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-MS023_2": {
                NAME: _("Ask about editing"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-MS023_4": {
                NAME: _("Ask about editing again..."),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-MS024_2": {
                NAME: _("Film done?"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_7, TIMESLOT_6],
                },
            "io-MS025": {
                NAME: _("Talk about new order from the client"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                DAYS_PASSED: {TARGET: "sm1ms024", DAYS: 1},
                TIMESLOTS: [TIMESLOT_7],
                },
            "io-MS026":{
                NAME: _("Talk to Stacy about the new movie"),
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                DAYS_PASSED: [{TARGET: "sm1ms025", DAYS: 1}, {TARGET:"sm1cs_tl007", DAYS: 1}],
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
        
            "io-MS003_perma": {
                NAME: _("Help Stacy"),
                ACTION: CALL,
                TARGET: "sm1ms003_repeatable",
                DISABLED_BY_PENALTY: True,
                },
            "io-MS005_perma": {
                NAME: _("Netfix and chill with Stacy"),
                ACTION: CALL,
                TARGET: "sm1ms005_02i",
                DISABLED_BY_PENALTY: True,
                },
            "io-SY001_perma": {
                NAME: _("Have a shower with Stacy"),
                ACTION: CALL,
                TARGET: "sm1cs_sy001_repeatable",
                DISABLED_BY_PENALTY: True,
                },
            "io-SY001_perma_2": {
                NAME: _("Check Stacy out"),
                ACTION: CALL,
                TARGET: "check_stacy_in_shower",
                },
            "io-SY002_2": {
                NAME: _("Filming practice"),
                ACTION: [SET_CHOICE, CALL],
                TARGET: "sm1cs_sy002i",
                CHOICE_NAME: "io_sy002_clicked",
                LOCATION: [STUDIO],
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                HIDDEN_BY_CONDITION: "io_is_hidden_SY002",
                TIMESLOTS: [TIMESLOT_8],
                },
            "io-SY003": {
                NAME: _("Come with me to the bed"),
                ACTION: [SET_CHOICE, CALL],
                TARGET: "sm1cs_sy003i",
                CHOICE_NAME: "io_sy003_clicked",
                LOCATION: [STUDIO],
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                HIDDEN_BY_CONDITION: "io_is_hidden_SY003",
                TIMESLOTS: [TIMESLOT_8],
                },

        
            "io-KV000i": {
                NAME: _("Talk about camera girl"),
                ACTION: PROGRESS_STORY,
                TARGET: KV_STORY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8]
                },
            "io-KV002_02": {
                NAME: _("Purchase Photography-101 for $") + "60",
                ACTION: FUNCTION,
                TARGET: PlayerController.buy_item,
                PARAMS: PHOTOGRAPHY_101
                },
            "io-KV003": {
                NAME: _("Tell Stacy about Kanya"),
                ACTION: PROGRESS_STORY,
                TARGET: KV_STORY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4]
                },
            "io-KV004_2": {
                NAME: _("Ask for 'practice'"),
                ACTION: PROGRESS_STORY,
                TARGET: KV_STORY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8],
                LOCATION: [PHOTO_DOJO]
                },
            "io-KV004_repeatable": {
                NAME: _("Ask for some sexy 'practice'"),
                ACTION: CALL,
                TARGET: "sm1cs_kv004_1i",
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8],
                LOCATION: [PHOTO_DOJO],
                DAILY_LIMIT: "io-KV004_repeatable"
                },
            "io-KV005": {
                NAME: _("Learn Photography"),
                ACTION: PROGRESS_STORY,
                TARGET: KV_STORY,
                DISABLED_BY_POSE: KV_DEFAULT_POSES_LIST
                },
        
            "io-BG003":{
                NAME: _("Talk about the Photoshoot"),
                ACTION: PROGRESS_STORY,
                TARGET: BG_STORY,
                LOCATION: [PHOTO_DOJO],
                DAYS_PASSED: {TARGET: "sm1cs_bg002", DAYS: 1},
                },

        
            "io-MH001": {
                NAME: _("Talk about hiring people"),
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
                DISABLED_BY_PENALTY: True,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8],
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST
                },
            "io-MH002-00": {
                NAME: _("Go with Stacy to meet with Lyssa"),
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST
                },
            "io-MH003": {
                NAME: _("Talk about Lyssa"),
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST
                },
            "io-MH003_02": {
                NAME: _("Date with Lyssa"),
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
                DAYS_PASSED: {TARGET: "sm1cs_mh003", DAYS: 1},
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7]
                },
            "io-MH004_01": {
                NAME: _("Date with Lyssa"),
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6]
                },
        
            "io-DC005_2": {
                NAME: _("Confront Debbie"),
                ACTION: PROGRESS_STORY,
                TARGET: DC_STORY,
                LOCATION: [PARK],
                DAYS_PASSED: {TARGET: "sm1cs_dc004", DAYS: 2},
                },
            "io-DC006_2": {
                NAME: _("Ask about getting coffee"),
                ACTION: PROGRESS_STORY,
                TARGET: DC_STORY,
                LOCATION: [PARK],
                TIMESLOTS: [TIMESLOT_7],
                },
            "io-DC007_1_offramp": {
                NAME: _("Ask Debbie out again"),
                ACTION: CALL,
                TARGET: "sm1cs_dc006_onramp",
                LOCATION: [PARK],
                },
        
            "io-MES002": {
                NAME: _("Talk about Min"),
                ACTION: PROGRESS_STORY,
                TARGET: MES_STORY,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                },
        
            "io-MY001_2": {
                NAME: _("Can you check my fit?"),
                ACTION: PROGRESS_STORY,
                TARGET: MY_STORY,
                NEED_MONEY: 200,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
            },
            "io-MY002": {
                NAME: _("Talk about Melony"),
                ACTION: PROGRESS_STORY,
                TARGET: MY_STORY,
                LOCATION: [STUDIO],
                TIMESLOTS: [TIMESLOT_7],
                DAYS_PASSED: {TARGET: "sm1cs_my001", DAYS: 2},
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
            },
            "io-MY003_2": {
                NAME: _("Talk about Melony"),
                ACTION: PROGRESS_STORY,
                TARGET: MY_STORY,
                LOCATION: [STUDIO],
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
            },



        
            "io-NS007_02": {
                NAME: _("Invite Nari"),
                ACTION: PROGRESS_STORY,
                TARGET: NS_STORY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                LOCATION: [IT_OFFICE],
                },
            "io-NS008": {
                NAME: _("Talk about last date"),
                ACTION: PROGRESS_STORY,
                TARGET: NS_STORY,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                LOCATION: [IT_OFFICE],
                },
            "io-NS010": {
                NAME: _("Talk about Nari"),
                ACTION: PROGRESS_STORY,
                TARGET: NS_STORY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8],
                },
            "io-NS011_3": {
                NAME: _("About moving in"),
                ACTION: PROGRESS_STORY,
                TARGET: NS_STORY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6],
                DISABLED_BY_POSE: NS_CUSTOM_POSES_LIST,
                },
            "io-NS012_2": {
                NAME: _("How is your room?"),
                ACTION: PROGRESS_STORY,
                TARGET: NS_STORY,
                LOCATION: [STUDIO],
                TIMESLOTS: [TIMESLOT_7, TIMESLOT_8],
                DISABLED_BY_POSE: NS_CUSTOM_POSES_LIST,
                },
            "io-NS013_2": {
                NAME: _("Hey sexy!!"),
                ACTION: PROGRESS_STORY,
                TARGET: NS_STORY,
                LOCATION: [STUDIO],
                TIMESLOTS: [TIMESLOT_7],
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                },
            "io-NS-sex-repeatable01":{
                NAME: _("Sexy Times?"),
                ACTION: CALL,
                TARGET: "sm1cs_ns012i_repeatable",
                DAILY_LIMIT: "io-NS-sex-repeatable01",
                HIDDEN_BY_CONDITION: "is_hidden_NS_sex_repeatable01",
                HIDDEN_BY_POSE: NS_CUSTOM_POSES_LIST,
                DISABLED_BY_POSE: NS_CUSTOM_POSES_LIST,
                },
        
            "io-AM005_03": {
                NAME: _("Fix things up with April"),
                ACTION: PROGRESS_STORY,
                TARGET: AM_STORY,
                LOCATION: [IT_OFFICE],
                DISABLED_BY_POSE: AM_CUSTOM_POSES_LIST,
                },
            "io-AM006": {
                NAME: _("Ask her out"),
                ACTION: PROGRESS_STORY,
                TARGET: AM_STORY,
                LOCATION: [IT_OFFICE],
                TIMESLOTS: [TIMESLOT_6],
                DISABLED_BY_POSE: AM_CUSTOM_POSES_LIST,
                DISABLED_BY_RP: {"am": 8}, 
                },
        
            "io-CW003": {
                NAME: _("Talk about Claire"),
                ACTION: PROGRESS_STORY,
                TARGET: CW_STORY,
                LOCATION: [STUDIO],
                TIMESLOTS: [TIMESLOT_7],
                DAYS_PASSED: {TARGET: "sm1ms020", DAYS: 0},
                DISABLED_BY_POSE: CW_CUSTOM_POSES_LIST,
                },
            "io-CW004-offramp": {
                NAME: _("I will help you Claire"),
                ACTION: JUMP,
                TARGET: "sm1cs_cw004_onramp",
                LOCATION: [IT_OFFICE],
                TIMESLOTS: [TIMESLOT_7],
                DAYS: [FRIDAY],
                DISABLED_BY_POSE: CW_CUSTOM_POSES_LIST,
                },
            "io-CW006-off-1": {
                NAME: _("I want to continue what we had"),
                ACTION: JUMP,
                TARGET: "sm1cs_cw006_onramp",
                LOCATION: [IT_OFFICE],
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6],
                DISABLED_BY_POSE: CW_CUSTOM_POSES_LIST,
                },
            "io-CW006-off-2": {
                NAME: _("I agree to your special assignment"),
                ACTION: JUMP,
                TARGET: "sm1cs_cw006_onramp",
                LOCATION: [IT_OFFICE],
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6],
                DISABLED_BY_POSE: CW_CUSTOM_POSES_LIST,
                },
        
            "io-AG002_2": {
                NAME: _("How are you?"),
                ACTION: PROGRESS_STORY,
                TARGET: AG_STORY,
                LOCATION: [IT_OFFICE],
                TIMESLOTS: [TIMESLOT_6],
                DISABLED_BY_RP: {"ag": 5}, 
                DISABLED_BY_POSE: AG_CUSTOM_POSES_LIST,
                },
            "io-AG003_2": {
                NAME: _("Do you know where is Anna?"),
                ACTION: PROGRESS_STORY,
                TARGET: AG_STORY,
                LOCATION: [IT_OFFICE],
                DISABLED_BY_POSE: CW_CUSTOM_POSES_LIST,
                },


            "io-rehearsal_at_th": {
                NAME: _("Rehearsal for the show"),
                ACTION: FUNCTION,
                TARGET: THController.work_th_job,
                ENERGY_LIMIT: 3,
                TIMESLOTS: [TIMESLOT_7],
                DAYS: [THController.rehearsal_day_1, THController.rehearsal_day_2, THController.rehearsal_day_3],
                DAILY_LIMIT: "io-rehearsal_at_th"
                },
            "io-FST001": {
                NAME: _("Let's go to Amusement Park"),
                ACTION: PROGRESS_STORY,
                TARGET: THEATER_STORY_LINE,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6]
                },
            "io-FST002": {
                NAME: _("Interview Taisia now"),
                ACTION: PROGRESS_STORY,
                TARGET: THEATER_STORY_LINE,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6]
                },
            "io-FST003": {
                NAME: _("___ INSERT _____"),
                ACTION: PROGRESS_STORY,
                TARGET: THEATER_STORY_LINE,
                HIDDEN: True
                },
            "io-VS002_02": {
                NAME: _("Purchase Stars Weekly for $") + "30",
                ACTION: FUNCTION,
                TARGET: PlayerController.buy_item,
                PARAMS: STARS_WEEKLY
                },
            "io-VS005": {
                NAME: _("Next Blitz?"),
                ACTION: PROGRESS_STORY,
                TARGET: VS_STORY,
                LOCATION: [THEATER],
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                DAYS_PASSED: [{TARGET: "sm1cs_km005", DAYS: 1}, {TARGET: "sm1ms020", DAYS: 1}],
                },
        
            "io-KM002_03": {
                NAME: _("Purchase An Actor Prepares for $") + "60",
                ACTION: FUNCTION,
                TARGET: PlayerController.buy_item,
                PARAMS: AN_ACTOR_PREPARES,
                },
            "io-KM003_2": {
                NAME: _("Hey Kellie!"),
                ACTION: PROGRESS_STORY,
                TARGET: KM_STORY,
                LOCATION: [THEATER],
                DAYS_PASSED: {TARGET: "sm1cs_km003", DAYS: 2},
                DISABLED_BY_POSE: KM_CUSTOM_POSES_LIST,
                },
            "io-KM004": {
                NAME: _("Hey!"),
                ACTION: PROGRESS_STORY,
                TARGET: KM_STORY,
                LOCATION: [THEATER],
                DAYS_PASSED: {TARGET: "sm1cs_km003_2", DAYS: 2},
                DISABLED_BY_POSE: KM_CUSTOM_POSES_LIST,
                },
            "io-KM006_1": {
                NAME: _("About Kellie"),
                ACTION: PROGRESS_STORY,
                TARGET: KM_STORY,
                LOCATION: [THEATER],
                DAYS_PASSED: {TARGET: "sm1cs_vs005", DAYS: 2},
                DISABLED_BY_POSE: VS_CUSTOM_POSES_LIST,
                },
            "io-KM006_2": {
                NAME: _("Talk about last time"),
                ACTION: PROGRESS_STORY,
                TARGET: KM_STORY,
                LOCATION: [THEATER],
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                DISABLED_BY_POSE: KM_CUSTOM_POSES_LIST,
                },
        
            "io-TL001": {
                NAME: _("Talk about \"work\""),
                ACTION: PROGRESS_STORY,
                TARGET: TL_STORY,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                },
            "io-TL004": {
                NAME: _("Chat with Taisia"),
                ACTION: PROGRESS_STORY,
                TARGET: TL_STORY,
                TIMESLOTS: [TIMESLOT_7],
                },
            "io-TL006": {
                NAME: _("Talk about Taisia"),
                ACTION: PROGRESS_STORY,
                TARGET: TL_STORY,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6, TIMESLOT_7],
                },
            "io-TL007": {
                NAME: _("Talk about moving in"),
                ACTION: PROGRESS_STORY,
                TARGET: TL_STORY,
                DAILY_LIMIT: "io-TL007",
                DAYS_PASSED: {TARGET: "sm1cs_tl006", DAYS: 1},
                TIMESLOTS: [TIMESLOT_6, TIMESLOT_7]
                },
            "io-TL007_2": {
                NAME: _("Talk about moving in"),
                ACTION: PROGRESS_STORY,
                TARGET: TL_STORY,
                DAILY_LIMIT: "io-TL007",
                DAYS_PASSED: {TARGET: "sm1ms020", DAYS: 1},
                TIMESLOTS: [TIMESLOT_6, TIMESLOT_7]
                },
            "io-TL-sex-repeatable01":{
                NAME: _("Sexy Times?"),
                ACTION: CALL,
                TARGET: "sm1cs_tl008i_repeatable",
                DAILY_LIMIT: "io-TL-sex-repeatable01",
                HIDDEN_BY_CONDITION: "is_hidden_TL_sex_repeatable01",
                HIDDEN_BY_POSE: TL_CUSTOM_POSES_LIST,
                },
        
            "io-MV01S02": {
                NAME: _("Buy costume for the movie"),
                ACTION: CALL,
                TARGET: "sm1mv01s02i",
                HIDDEN_BY_CONDITION: "io_is_hidden_mv01s02",
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5]
                },
            "io-MV01S03_1": {
                NAME: _("Recruit actress for the movie"),
                ACTION: CALL,
                TARGET: "sm1mv01s03_1i",
                HIDDEN_BY_CONDITION: "io_is_hidden_mv01s03_1",
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5]
                },
            "io-MV01S03_2": {
                NAME: _("Recruit Taisia for the movie"),
                ACTION: CALL,
                TARGET: "sm1mv01s03_2",
                HIDDEN_BY_CONDITION: "io_is_hidden_mv01s03_2",
                },
            "io-PIRATE_MOVIE_SCREEN": {
                NAME: _("Pirates Movie"),
                ACTION: JUMP,
                TARGET: "pirate_movie_screen",
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                },
            "io-MV01S04": {
                NAME: _("Talk about buying props for the movie"),
                ACTION: PROGRESS_STORY,
                TARGET: MOVIE_PIRATES,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7],
                },
            "io-MV01S04_2": {
                NAME: _("Build props for the movie"),
                ACTION: PROGRESS_STORY,
                TARGET: MOVIE_PIRATES,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                },
            "io-MV01S05": {
                NAME: _("Start filming the movie"),
                ACTION: PROGRESS_STORY,
                TARGET: MOVIE_PIRATES,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                },
            "io-MV01S06": {
                NAME: _("Start filming the second scene"),
                ACTION: PROGRESS_STORY,
                TARGET: MOVIE_PIRATES,
                DISABLED_BY_POSE: TL_CUSTOM_POSES_LIST,
                LOCATION: [STUDIO],
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6],
                },
            "io-MV01S07": {
                NAME: _("Talk about the movie"),
                ACTION: PROGRESS_STORY,
                TARGET: MOVIE_PIRATES,
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_5],
                },
            "io-MV01S07_3": {
                NAME: _("Travel!"),
                ACTION: PROGRESS_STORY,
                TARGET: MOVIE_PIRATES,
                LOCATION: [STUDIO],
                DISABLED_BY_POSE: TL_CUSTOM_POSES_LIST,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                },
            "io-MV01S11_2": {
                NAME: _("I finished editing!"),
                ACTION: PROGRESS_STORY,
                TARGET: MOVIE_PIRATES,
                LOCATION: [STUDIO],
                DISABLED_BY_POSE: SY_CUSTOM_POSES_LIST,
                },
            }
