init 3 python:
    CharacterController.get_character("my").interactions = [
            {LABEL: "q_inter_my_1", BEFORE_SCENE: [MS, "sm1ms019"]},
            {LABEL: "q_inter_my_2", BEFORE_SCENE: [MS, "sm1ms019"]},
            {LABEL: "q_inter_my_3", BEFORE_SCENE: [MS, "sm1ms019"]},
            {LABEL: "q_inter_my_4"},
            {LABEL: "q_inter_my_5", BEFORE_SCENE: [MS, "sm1ms019"]},
            {LABEL: "q_inter_my_6", AFTER_SCENE: [MS, "sm1ms020"]},
            {LABEL: "q_inter_my_7", LOCATIONS:[GR_BAR], AFTER_SCENE: [MS, "sm1ms020"]},
            {LABEL: "q_inter_my_8", LOCATIONS:[GR_BAR], AFTER_SCENE: [MS, "sm1ms020"]},
            {LABEL: "q_inter_my_9", LOCATIONS:[GR_BAR], AFTER_SCENE: [MS, "sm1ms020"]},
            {LABEL: "q_inter_my_10", AFTER_SCENE: [MY_STORY, "sm1cs_my001"]},
            ]
    CharacterController.get_character("my").default_expression = "smile01"

label q_inter_my_1:
    show expression cc.get_expression_image("my", "neutral01") as lst_my_neutral
    play voice3 girl34_thinking_hmm6 noloop
    my "So, have you thought any more about college?"
    play voice2 d2s9_confused noloop volume 1.7
    mc "Erm..."
    hide lst_my_neutral
    show expression cc.get_expression_image("my", "sad01")
    play voice3 girl34_disappointed_eeh2 noloop
    my "Please just promise me you will."
    return
label q_inter_my_2:
    show expression cc.get_expression_image("my", "excited01")
    play voice3 girl34_surprised_wow1 noloop
    my "Wow, the studio renovation is really coming along, isn't it?"
    play voice2 mc_yes_yes2 noloop
    mc "It is! And thank you for helping."
    if persistent.is_special:
        my "Anything for my two children."
    else:
        my "Anything for you two."
    return
label q_inter_my_3:
    show expression cc.get_expression_image("my", "excited01")
    play voice2 mc_thinking_mmm3 noloop
    mc "I don't think I've really expressed my gratitude for all of your help around the studio."
    play voice3 girl34_no_nah2 noloop
    my "And you don't need to. I'm happy to do it."
    return
label q_inter_my_4:
    show expression cc.get_expression_image("my", "neutral01") as lst_my_neutral
    play voice3 girl34_happy_mmm2 noloop
    my "He wants 4 walls in the gallery... and then the other artists wants-"
    play voice2 d1s2_mchey noloop
    if persistent.is_special:
        mc "Hey, Mom, what are you mumbling about?"
    else:
        mc "Hey, Melony, what are you mumbling about?"
    hide lst_my_neutral
    show expression cc.get_expression_image("my", "smile01") as lst_my_smile
    play voice3 girl34_disappointed_oh2 noloop
    my "Oh, just work stuff."
    play voice2 mc_thinking_hmm2 noloop
    mc "How are things going at the gallery?"
    hide lst_my_smile
    show expression cc.get_expression_image("my", "laugh01")
    play voice3 girl34_disappointed_oh3 noloop
    my "Oh, you know artists. Always something dramatic going on!"
    play voice2 mc_thinking_oh1 noloop
    mc "Oh boy, do I."
    $ CharacterController.get_character("my").add_point()
    return
label q_inter_my_5:
    show expression cc.get_expression_image("my", "serious01") as lst_my_serious
    play voice3 girl34_disappointed_mmf4 noloop
    my "Mmmmmm..."
    play voice2 mc_thinking_emm1 noloop
    if persistent.is_special:
        mc "Uhm, Mom?"
    else:
        mc "Uhm, Melony?"
    hide lst_my_serious
    show expression cc.get_expression_image("my", "curious01") as lst_my_curious
    play voice3 girl34_disappointed_oh1 noloop
    my "Oh, sorry. I was daydreaming a bit there."
    play voice2 d1s2_hmm noloop
    mc "About?"
    hide lst_my_curious
    show expression cc.get_expression_image("my", "neutral01") as lst_my_neutral
    play voice3 girl34_disappointed_eem4 noloop
    my "The last time I was in Crowning was... exciting."
    play voice2 mc_arrogant_heh1 noloop
    mc "More exciting than this?"
    hide lst_my_neutral
    show expression cc.get_expression_image("my", "naughty01")
    play voice3 girl34_thinking_hmm2 noloop
    my "Maybe... maybe not!"
    return
label q_inter_my_6:
    show expression cc.get_expression_image("my", "laugh01")
    play voice3 girl34_hey_laughing noloop
    my "[mcname]! Funny bumping into you here!"
    play voice2 mc_thinking_hmm1 noloop
    mc "Well, you know, only so many bars in Crowning."
    my "Hahaha! Yeah, you've got a point there."
    return
label q_inter_my_7:
    show expression cc.get_expression_image("my", "smile01")
    play voice3 girl34_happy_relief2 noloop
    my "I don't know what it is about this bar... but I really like it here."
    play voice2 mc_yes_yeah1 noloop
    mc "Me too."
    return
label q_inter_my_8:
    show expression cc.get_expression_image("my", "ask01") as lgr_my_ask
    play voice3 girl34_thinking_eeh2 noloop
    if persistent.is_special:
        my "Care to share a drink with your Mom?"
        play voice2 mc_yes_sure1 noloop
        mc "Of course, Mom!"
    else:
        my "Care to share a drink with me, [mcname]?"
        play voice2 mc_yes_sure1 noloop
        mc "Of course, Melony!"
    hide lgr_my_ask
    show expression cc.get_expression_image("my", "excited01") as lgr_my_excited
    play voice4 girl34_hey_scandalized3 noloop
    my "Shots!"
    play voice2 mc_surprised_what4 noloop
    mc "Wait, what?"
    hide lgr_my_excited
    show expression cc.get_expression_image("rd", "smile01") as lgr_rd_smile
    play voice4 girl26_yes_ugu noloop
    rd "Here you go."
    hide lgr_rd_smile
    show expression cc.get_expression_image("my", "excited01") as lgr_my_excited
    play voice3 girl34_happy_yay2 noloop
    my "Yay! To you, [mcname]."
    play voice2 d2s9_confused noloop
    if persistent.is_special:
        mc "Uhm, and to you, Mom!"
    else:
        mc "Uhm, and to you, Melony!"
    play sound sfx_drink_gulp
    play voice2 mc_angry_errr8 noloop
    mc "*gulp* Tsssssss! Damn, that burns!"
    hide lgr_my_excited
    show expression cc.get_expression_image("my", "excited01") as lgr_my_excited
    play voice3 girl34_happy_mmm2 noloop
    my "But yummy!"
    $ CharacterController.get_character("my").add_point()
    return
label q_inter_my_9:
    show expression cc.get_expression_image("my", "excited01") as lgr_my_excited
    play voice3 girl34_thinking_emm5 noloop
    my "Maybe one of the next times we spend some time together, we can do it here!"
    play voice2 mc_thinking_hmm4 noloop
    mc "I'd love that!"
    hide lgr_my_excited
    show expression cc.get_expression_image("my", "smile01") as lgr_my_smile
    play voice3 girl34_yes_ugu1 noloop
    my "I would to, [mcname]."
    hide lgr_my_smile
    play voice2 mc_thinking_mmm2 noloop
    mct "Sounds like we've got another date on the docket!"
    mct "Or, hangout, or whatever."
    $ CharacterController.get_character("my").add_point()
    return
label q_inter_my_10:
    show expression cc.get_expression_image("my", "smile01")
    play voice3 girl34_happy_relief2 noloop
    my "[mcname], I really enjoyed getting dinner with you."
    play voice2 mc_yes_yeah4 noloop
    mc "I had a lot of fun too!"
    my "I'm looking forward to going again."
    return