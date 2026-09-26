init 3 python:
    CharacterController.get_character("km").interactions = [
            {LABEL: "q_inter_km_1", LOCATIONS: [THEATER], BANNED_SUBLOCATIONS: [LTH_SUB_SHOWER], BEFORE_SCENE: [KM_STORY, "sm1cs_km001"]},
            {LABEL: "q_inter_km_2", LOCATIONS: [THEATER], BANNED_SUBLOCATIONS: [LTH_SUB_SHOWER], BEFORE_SCENE: [KM_STORY, "sm1cs_km001"]},
            {LABEL: "q_inter_km_3", LOCATIONS: [THEATER], BANNED_SUBLOCATIONS: [LTH_SUB_SHOWER], BEFORE_SCENE: [KM_STORY, "sm1cs_km001"]},
            {LABEL: "q_inter_km_4", LOCATIONS: [THEATER], BANNED_SUBLOCATIONS: [LTH_SUB_SHOWER], AFTER_SCENE: [KM_STORY, "sm1cs_km001"]},
            {LABEL: "q_inter_km_5", LOCATIONS: [THEATER], BANNED_SUBLOCATIONS: [LTH_SUB_SHOWER], AFTER_SCENE: [KM_STORY, "sm1cs_km001"]},
            {LABEL: "q_inter_km_6", LOCATIONS: [THEATER], BANNED_SUBLOCATIONS: [LTH_SUB_SHOWER], AFTER_SCENE: [KM_STORY, "sm1cs_km003_2"]}, 
            {LABEL: "q_inter_km_7", LOCATIONS: [THEATER], BANNED_SUBLOCATIONS: [LTH_SUB_SHOWER], AFTER_SCENE: [KM_STORY, "sm1cs_km003_2"]}, 
            {LABEL: "q_inter_km_8", LOCATIONS: [THEATER], BANNED_SUBLOCATIONS: [LTH_SUB_SHOWER], AFTER_SCENE: [KM_STORY, "sm1cs_km003_2"]}, 
            {LABEL: "q_inter_km_9", LOCATIONS: [THEATER], AFTER_SCENE: [KM_STORY, "sm1cs_km004"], BANNED_SUBLOCATIONS: [LTH_SUB_STAGE, LTH_SUB_DRESSING_1, LTH_SUB_DRESSING_2, LTH_SUB_BACKSTAGE, LTH_SUB_LOCKERS]},
            {LABEL: "q_inter_km_10", LOCATIONS: [THEATER], AFTER_SCENE: [KM_STORY, "sm1cs_km004"], BANNED_SUBLOCATIONS: [LTH_SUB_STAGE, LTH_SUB_DRESSING_1, LTH_SUB_DRESSING_2, LTH_SUB_BACKSTAGE, LTH_SUB_LOCKERS]}, 
            {LABEL: "q_inter_km_11", LOCATIONS: [THEATER], AFTER_SCENE: [KM_STORY, "sm1cs_km004"], BANNED_SUBLOCATIONS: [LTH_SUB_STAGE, LTH_SUB_DRESSING_1, LTH_SUB_DRESSING_2, LTH_SUB_BACKSTAGE, LTH_SUB_LOCKERS]}, 
            ]
    CharacterController.get_character("km").default_expression = "angry01"

    km_angry_peek_interactions_list = [
            "*angry* Get the hell out of here perv!",
            "Avert your eyes!",
            "Fuck you and get the fuck away from me.",
            "Get out of here!"
            ]

label q_inter_km_1:
    show expression cc.get_expression_image("km", "angry01")
    play voice3 girl31_angry_ergh6 noloop
    km "I hope you are going to work hard around here. The theater isn't the place for people who slack off or get distracted."
    play voice2 mc_yes_yeah2 noloop
    mc "I'll do my best Kellie."
    return
label q_inter_km_2:
    show expression cc.get_expression_image("km", "serious01")
    play voice3 girl31_arrogant_huh2 noloop
    km "What? Do I have something on my face?"
    play voice2 mc_no_no2 noloop
    mc "Uh no."
    km "Then please stop looking at me like that. It's distracting."
    return
label q_inter_km_3:
    show expression cc.get_expression_image("km", "neutral01") as lth_km_neutral01
    play voice2 d1s5_mchappy noloop volume 1.8
    mc "How's it going, Kellie?"
    play voice3 girl31_disappointed_ehh1 noloop
    km "If you must know, I was just thinking about one of my favorite scenes from the Hanna Parker Books."
    mc "Uh cool. Wait, aren't those kids books?"
    hide lth_km_neutral01
    show expression cc.get_expression_image("km", "annoyed01")
    play voice3 girl31_angry_cough4 noloop
    km "*clears throat* Young adult, actually. And if you'd ever read them, you'd know they're fantastic, and the themes in the book grew as they came out."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Meaning?"
    km "Hmmm. Forget about it, [mcname]."
    $ CharacterController.get_character("km").add_point()
    return
label q_inter_km_4:
    show expression cc.get_expression_image("km", "sad01")
    play voice3 girl31_disappointed_ehh9 noloop
    km "Oh..."
    mct "Looks like Kellie is still not ready to talk about what happened."
    return
label q_inter_km_5:
    show expression cc.get_expression_image("km", "embarrassed01")
    play voice3 girl31_thinking_emm3 noloop
    km "How are you feeling, [mcname]?"
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Good. Pretty normal. You?"
    km "Normal. Yes. Super normal. Bye."
    return
label q_inter_km_6:
    show expression cc.get_expression_image("km", "neutral01")
    play voice3 girl31_thinking_hmm1 noloop
    km "Always remember. Practice makes perfect around here, [mcname]."
    return
label q_inter_km_7:
    show expression cc.get_expression_image("km", "serious01")
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Are we going to do something more modern for our next practice, Coach Kellie?"
    play voice3 girl31_thinking_hmm2 noloop
    km "Mmm. I'll think about it."
    $ CharacterController.get_character("km").add_point()
    return
label q_inter_km_8:
    show expression cc.get_expression_image("km", "smile01") as lth_km_smile01
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Everything good, Kellie?"
    play voice3 girl31_yes_simple1 noloop
    km "Yes."
    hide lth_km_smile01
    show expression cc.get_expression_image("km", "embarrassed01")
    play voice3 girl31_thinking_emm3 noloop
    km "T-thank. Thank you for asking, [mcname]."
    $ CharacterController.get_character("km").add_point()
    return
label q_inter_km_9:
    show expression cc.get_expression_image("km", "annoyed01") as lth_km_annoyed01
    play voice3 girl31_disappointed_mff1 noloop
    km "[mcname]."
    return
label q_inter_km_10:
    show expression cc.get_expression_image("km", "annoyed01") as lth_km_smile01
    play voice3 girl31_hey_attention noloop
    km "Hey, [mcname]."
    km "Do I have something on my face?"
    play voice2 mc_no_no9 noloop
    mc "No you're good?"
    $ CharacterController.get_character("km").add_point()
    return
label q_inter_km_11:
    show expression cc.get_expression_image("km", "annoyed01") as lth_km_smile01
    play voice3 girl31_hey_upbeat noloop
    km "Hey..."
    return