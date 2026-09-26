init 3 python:
    CharacterController.get_character("ag").interactions = [
            {LABEL: "q_inter_ag_1", LOCATIONS: [IT_OFFICE], TIMESLOTS: [TIMESLOT_3]},
            {LABEL: "q_inter_ag_2", LOCATIONS: [IT_OFFICE], TIMESLOTS: [TIMESLOT_3, TIMESLOT_4]},
            {LABEL: "q_inter_ag_3", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ag_4", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ag_5", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ag_6", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ag_7", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ag_8", LOCATIONS: [IT_OFFICE], TIMESLOTS: [TIMESLOT_5]},
            {LABEL: "q_inter_ag_9", LOCATIONS: [PARK, SHOP_71STORE], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ag_10", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ag_12", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ag_13", LOCATIONS: [SHOP_71STORE], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ag_14", LOCATIONS: [SHOP_71STORE], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ag_15", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ag_16", LOCATIONS: [GR_BAR], AFTER_SCENE: [IT_STORY_LINE, "sm1cs_ag002"]},
            {LABEL: "q_inter_ag_17", LOCATIONS: [GR_BAR], AFTER_SCENE: [IT_STORY_LINE, "sm1cs_ag002"]},
            {LABEL: "q_inter_ag_18", LOCATIONS: [STARDUCKS], AFTER_SCENE: [IT_STORY_LINE, "sm1cs_ag003"]},
            ]
    CharacterController.get_character("ag").default_expression = "smile01"

label q_inter_ag_1:
    show expression cc.get_expression_image("ag", "smile01")
    play voice3 girl27_hey_active noloop
    ag "Hey [mcname]. I hope you're having a good day."
    return
label q_inter_ag_2:
    show expression cc.get_expression_image("ag", "smile02")
    play voice3 girl27_happy_laugh6 noloop
    ag "Looks like you've got your head in the clouds today."
    play voice2 d4s4_mclaugh noloop volume 1.5
    mc "Hahaha. Nice one."
    ag "Thanks."
    $ CharacterController.get_character("ag").add_point()
    return
label q_inter_ag_3:
    show expression cc.get_expression_image("ag", "curious01")
    play voice3 girl27_hey_simple1 noloop
    ag "Reading anything interesting these days, [mcname]?"
    play voice2 mc_arrogant_nah1 noloop
    mc "Not really. Mostly just technical manuals."
    ag "That's a bummer."
    return
label q_inter_ag_4:
    show expression cc.get_expression_image("ag", "annoyed01")
    play voice3 girl27_angry_err4 noloop
    ag "Grrr."
    play voice2 d1s2_hmm noloop volume 1.4
    mc "What's wrong, Anna?"
    play voice3 girl27_surprised_huh noloop
    ag "Huh? Oh. Nothing. I uh ... I kind of stayed up late playing a game."
    ag "I defnintely shouldn't have had that extra energy drink."
    $ CharacterController.get_character("ag").add_point()
    return
label q_inter_ag_5:
    show expression cc.get_expression_image("ag", "serious01")
    play voice3 girl27_disappointed_eh1 noloop volume 1.3
    ag "Sorry, I can't talk right now. Jayden is making my life miserable. Again."
    return
label q_inter_ag_6:
    show expression cc.get_expression_image("ag", "smile02")
    play voice3 girl27_happy_relief1 noloop
    ag "I'm glad to have you on the team, [mcname]."
    ag "Haha. Stick with us and you'll go far."
    mct "Oh god."
    $ CharacterController.get_character("ag").add_point()
    return
label q_inter_ag_7:
    show expression cc.get_expression_image("ag", "curious01")
    play voice3 girl27_hey_interested noloop
    ag "How's it going, [mcname]?"
    play voice2 mc_thinking_mmm5 noloop
    mc "Not too bad. How about you."
    play voice3 girl27_happy_great2 noloop
    ag "Great. I finished my book, 'The Mask of Morraco last night."
    ag "It was amazing."
    $ CharacterController.get_character("ag").add_point()
    return
label q_inter_ag_8:
    show expression cc.get_expression_image("ag", "serious01")
    play voice3 girl27_disgust_mff noloop
    ag "I could have gone to nationals. I would have won the golden joystick."
    play voice2 mc_arrogant_heh3 noloop
    mc "You okay, Anna?"
    play voice3 girl27_surprised_oh3 noloop
    ag "Oh! Hey [mcname]. Sorry, got caught up in a day dream."
    $ CharacterController.get_character("ag").add_point()
    return
label q_inter_ag_9:
    show expression cc.get_expression_image("ag", "smile01")
    play voice3 girl27_hey_interested noloop
    ag "Oh hey, [mcname]. Nice to see you outside of work."
    play voice2 mc_happy_yay2 noloop
    mc "You too, Anna."
    return
label q_inter_ag_10:
    show expression cc.get_expression_image("ag", "smile01")
    play voice2 d2s9_mchey noloop volume 1.4
    mc "Hey Anna. How's it going?"
    play voice3 girl27_happy_hmm3 noloop
    ag "Mmmm. Wonderful. Nothing beats a little stroll. What brings you out here, [mcname]?"
    mc "Yeah. Sometimes it scares me how much time I'm just staring at a screen or sitting around indoors."
    ag "Mmhmm."
    $ CharacterController.get_character("ag").add_point()
    return
label q_inter_ag_12:
    show expression cc.get_expression_image("ag", "smile02")
    play voice3 girl27_hey_active noloop
    ag "Hey [mcname]. I gotta run, but I'll see you next time at work."
    return
label q_inter_ag_13:
    show expression cc.get_expression_image("ag", "smile02")
    play voice3 girl27_happy_hmm3 noloop
    ag "Got any fun plans tonight?"
    play voice2 mc_yes_yeah4 noloop
    mc "I'm thinking about reading this new book I got."
    ag "Oooh, that's always a good plan!"
    return
label q_inter_ag_14:
    show expression cc.get_expression_image("ag", "smile02")
    play voice3 girl27_surprised_wow1 noloop
    ag "I can't believe they sell seaweed chips here!"
    return
label q_inter_ag_15:
    show expression cc.get_expression_image("ag", "smile02") as lst_ag_smile02
    play voice2 d1s2_hmm noloop
    mc "What are you up to, Anna?"
    play voice3 girl27_thinking_oh2 noloop
    ag "Oh just was relaxing with my book."
    mc "Cool, what kind of book is it?"
    ag "Oh just a um... classic. Great Expectations."
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I remember that one."
    hide lst_ag_smile02
    show expression cc.get_expression_image("ag", "curious01")
    play voice3 girl27_yes_yap2 noloop
    ag "Yup. Sometimes I like to reread old books. A bit like comfort books."
    play voice2 mc_thinking_mmm1 noloop
    mc "Or pleasure literature."
    play voice3 girl27_happy_laugh4 noloop
    ag "*chuckles* Exactly."
    return
label q_inter_ag_16:
    show expression cc.get_expression_image("ag", "smile02")
    play voice3 girl27_hey_greeting noloop
    ag "Hey, [mcname]! Joining me for happy hour?"
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Maybe for a little bit."
    ag "Awesome!"
    $ CharacterController.get_character("ag").add_point()
    return
label q_inter_ag_17:
    show expression cc.get_expression_image("ag", "smile01")
    play voice3 girl27_happy_relief2 noloop
    ag "You know, Ridley makes a pretty margharita."
    ag "And you'd expect her old fashioned to be her best drink, and it's great!"
    ag "But man, her marg is to die for."
    return
label q_inter_ag_18:
    show expression cc.get_expression_image("ag", "curious01") as lst_ag_curious01
    play voice2 d1s2_hmm noloop volume 1.7
    mc "How's work going?"
    play voice3 girl27_yes_ya noloop
    ag "It's good."
    hide lst_ag_curious01
    show expression cc.get_expression_image("ag", "embarrassed01")
    play voice2 mc_thinking_mmm4 noloop
    mc "Going to be working at the coffee shop for awhile?"
    play voice3 girl27_thinking_emm4 noloop
    ag "Oh, erm... yep. Just until I finish this, erm, other project."
    return