init 3 python:
    CharacterController.get_character("sy").interactions = [
            {LABEL: "q_inter_sy_1"},
            {LABEL: "q_inter_sy_2"},
            {LABEL: "q_inter_sy_3", TIMESLOTS: [TIMESLOT_5]},
            {LABEL: "q_inter_sy_4", TIMESLOTS: [TIMESLOT_8]},
            {LABEL: "q_inter_sy_5", TIMESLOTS: [TIMESLOT_4]},
            {LABEL: "q_inter_sy_6", TIMESLOTS: [TIMESLOT_4]},
            {LABEL: "q_inter_sy_7", TIMESLOTS: [TIMESLOT_6]},
            {LABEL: "q_inter_sy_8", TIMESLOTS: [TIMESLOT_6]},
            {LABEL: "q_inter_sy_9", DAYS: [FRIDAY]},
            {LABEL: "q_inter_sy_10", DAYS: [WEEKENDS]},
            {LABEL: "q_inter_sy_11", DAYS: [THURSDAY], TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5]},
            {LABEL: "q_inter_sy_12", TIMESLOTS: [TIMESLOT_4]},
            {LABEL: "q_inter_sy_13", TIMESLOTS: [TIMESLOT_4]},
            {LABEL: "q_inter_sy_14", TIMESLOTS: [TIMESLOT_5]},
            {LABEL: "q_inter_sy_15", TIMESLOTS: [TIMESLOT_5]},
            {LABEL: "q_inter_sy_16"},
            {LABEL: "q_inter_sy_17", TIMESLOTS: [TIMESLOT_6]},
            {LABEL: "q_inter_sy_18"},
            {LABEL: "q_inter_sy_19"},
            {LABEL: "q_inter_sy_20", AFTER_SCENE: [TL_STORY, "sm1cs_tl003"]},
            {LABEL: "q_inter_sy_21", AFTER_SCENE: [TL_STORY, "sm1cs_tl003"]},
            {LABEL: "q_inter_sy_22", AFTER_SCENE: [TL_STORY, "sm1cs_tl003"]},
            {LABEL: "q_inter_sy_23", AFTER_SCENE: [MS, "sm1ms014"]},
            {LABEL: "q_inter_sy_24", AFTER_SCENE: [MS, "sm1ms014"]},
            {LABEL: "q_inter_sy_25", AFTER_SCENE: [MS, "sm1ms014"]},
            {LABEL: "q_inter_sy_26", AFTER_SCENE: [MS, "sm1ms014"]},
            {LABEL: "q_inter_sy_27", AFTER_SCENE: [MS, "sm1ms014"]},
            {LABEL: "q_inter_sy_28", AFTER_SCENE: [MS, "sm1ms014"], BEFORE_SCENE: [MS, "sm1ms020"]},
            {LABEL: "q_inter_sy_29", AFTER_SCENE: [MS, "sm1ms014"], BEFORE_SCENE: [MS, "sm1ms020"]},
            {LABEL: "q_inter_sy_30", AFTER_SCENE: [MS, "sm1ms014"], BEFORE_SCENE: [MS, "sm1ms020"]},
            {LABEL: "q_inter_sy_31", AFTER_SCENE: [MS, "sm1ms020"]},
            {LABEL: "q_inter_sy_32", AFTER_SCENE: [MS, "sm1ms020"]},
            ]
    CharacterController.get_character("sy").default_expression = "naughty01"

label q_inter_sy_1:
    show expression cc.get_expression_image("sy", "naughty1")
    play voice3 stacy_hey_happy2 noloop
    sy "Hey stud. You're looking good for Stacy today."
    return
label q_inter_sy_2:
    show expression cc.get_expression_image("sy", "smile1")
    play voice3 stacy_laugh4 noloop
    sy "Echo echo echo. Mmm. This place is great."
    return
label q_inter_sy_3:
    show expression cc.get_expression_image("sy", "smile1")
    play voice3 stacy_hey_happy2 noloop
    sy "*blows raspberry* Oh hey, [mcname]. Just waiting on a new download."
    return
label q_inter_sy_4:
    show expression cc.get_expression_image("sy", "ask1")
    play voice3 stacy_huh2 noloop
    sy "Well look what the cat dragged in."
    play voice2 mc_hey_hey3 noloop
    mc "Hey sweet thang."
    return
label q_inter_sy_5:
    show expression cc.get_expression_image("sy", "smile2")
    play voice3 stacy_hey_attention1 noloop
    sy "Morning, better get ready to earn that paper, [mcname]."
    play voice2 mc_yes_yeah4 noloop
    mc "On it."
    return
label q_inter_sy_6:
    show expression cc.get_expression_image("sy", "yawn1") as lst_sy_yawn_1
    play voice3 stacy_disappointed_moan1 noloop
    sy "*yawns* Hey. Watcha thinking about?"
    play voice2 mc_thinking_mmm2 noloop
    mc "Even in the morning you look gorgeous."
    hide lst_sy_yawn_1
    show expression cc.get_expression_image("sy", "smile2")
    play voice3 stacy_laugh4 noloop
    sy "Haha. I haven't even put my face on yet."
    return
label q_inter_sy_7:
    show expression cc.get_expression_image("sy", "naughty1")
    play voice3 stacy_huh2 noloop
    sy "Hey there... Ready for some afternoon delight?"
    return
label q_inter_sy_8:
    show expression cc.get_expression_image("sy", "annoyed1")
    play voice3 stacy_happy_relief1 noloop
    sy "Phew. Hey sexy. Don't forget to keep doing those stretches we talked about."
    sy "They'll come in handy during our next marathon."
    play voice2 mc_yes_sure1 noloop
    mc "Looking forward to it."
    return
label q_inter_sy_9:
    show expression cc.get_expression_image("sy", "excited1")
    play voice3 stacy_happy_phew1 noloop
    sy "*singing* Everybody's working for the weekend!"
    return
label q_inter_sy_10:
    show expression cc.get_expression_image("sy", "excited1")
    play voice3 stacy_thinking_hmm2 noloop
    sy "We should check out the beach again some day."
    return
label q_inter_sy_11:
    show expression cc.get_expression_image("sy", "excited1")
    play voice3 stacy_happy_yay1 noloop
    sy "Today's gonna be great. I just know it!"
    return
label q_inter_sy_12:
    show expression cc.get_expression_image("sy", "annoyed1")
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Mmm. I slept like a log last night."
    play voice2 mc_thinking_oh1 noloop
    mc "Really? Cause you kind of snore like a lumberjack."
    play voice3 stacy_no_uhuh3 noloop
    sy "A lady never snores."
    play voice2 d3s11b_mcheh noloop volume 1.8
    mc "Haha. That's true. But you're no lady."
    return
label q_inter_sy_13:
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty_1
    play voice3 stacy_thinking_hm1 noloop
    sy "I was thinking, today is a no underwear kind of day."
    play voice2 mc_thinking_mmm2 noloop
    mc "Love that."
    hide lst_sy_naughty_1
    show expression cc.get_expression_image("sy", "smile2")
    play voice3 stacy_yeahno noloop
    sy "Yeah but I decided against it. I don't want to be {b}too{/b} distracting."
    play voice2 mc_arrogant_hm3 noloop
    mc "Oh yeah you hate that."
    return
label q_inter_sy_14:
    show expression cc.get_expression_image("sy", "sad1")
    play voice3 stacy_upset1 noloop
    sy "I kind of miss the burgers at the cafeteria."
    return
label q_inter_sy_15:
    show expression cc.get_expression_image("sy", "ask1")
    play voice3 stacy_thinking_hmm4 noloop
    sy "Got any lunch plans? Once things calm down we need to stake out a spot somewhere."
    sy "I like the idea of having a special spot, just the two of us."
    return
label q_inter_sy_16:
    show expression cc.get_expression_image("sy", "smile2")
    play voice2 d2s9_mchey noloop
    mc "What are you doing?"
    play voice3 stacy_thinking_hmm1 noloop
    sy "Just thinking about camera angles. I really found us a good space for filming."
    return
label q_inter_sy_17:
    show expression cc.get_expression_image("sy", "smile1")
    play voice3 stacy_thinking_oh2 noloop
    sy "Check it out, [mcname]. Those clouds look like two people holding hands."
    return
label q_inter_sy_18:
    show expression cc.get_expression_image("sy", "smile2")
    play voice3 stacy_hey_attention1 noloop
    sy "Hey [mcname]. Just waiting on a download to complete. Our WIFI needs a tuneup."
    return
label q_inter_sy_19:
    show expression cc.get_expression_image("sy", "smile1")
    play voice3 stacy_thinking_emm2 noloop
    sy "I'm thinking of updating our firewall. Don't want anyone playing in our playground without my explicit permission."
    return
label q_inter_sy_20:
    show expression cc.get_expression_image("sy", "naughty1")
    play voice3 stacy_happy_hmm1 noloop
    sy "You know, I {i}really{/i} enjoyed filming you and Taisia."
    play voice2 mc_yes_yeah8 noloop
    mc "Oh yeah?"
    play voice3 stacy_yes_ugu1 noloop
    sy "Uh huh. Next time I might have to jump in. Make it a POV type of shoot."
    return
label q_inter_sy_21:
    show expression cc.get_expression_image("sy", "ask1") as q_inter_sy21_ask1
    play voice3 stacy_hey noloop volume 0.8
    sy "How do you think Taisia knew about that car?"
    play voice2 mc_thinking_emm1 noloop
    mc "I don't think I want to know."
    hide q_inter_sy21_ask1
    show expression cc.get_expression_image("sy", "naughty1")
    play voice3 stacy_hmm noloop
    sy "I do. It was kind of hot..."
    return
label q_inter_sy_22:
    show expression cc.get_expression_image("sy", "annoyed1")
    play voice3 stacy_angryhuh noloop
    sy "You know what I hate?"
    play voice2 mc_thinking_hmm2 noloop
    mc "What?"
    sy "Editing. Even if it's super hot footage..."
    return
label q_inter_sy_23:
    show expression cc.get_expression_image("sy", "annoyed01")
    play voice3 stacy_angryhuh noloop
    if persistent.is_special:
        sy "This is going to take some getting used to, having Mom around here."
    else:
        sy "This is going to take some getting used to, having Melony around here."
    return
label q_inter_sy_24:
    show expression cc.get_expression_image("sy", "neutral01")
    play voice3 stacy_hmm noloop
    sy "I still can't believe how often she has come over. She never visited in college."
    return
label q_inter_sy_25:
    show expression cc.get_expression_image("sy", "smile01")
    play voice3 stacy_hey noloop
    if persistent.is_special:
        sy "Hey bro. Looking good today."
    else:
        sy "Hey sugar. Looking good today."
    play voice2 mc_yes_aga2 noloop
    mc "Thanks, Stacy."
    return
label q_inter_sy_26:
    show expression cc.get_expression_image("sy", "annoyed01") as sy_annoyed01
    play voice3 stacy_upset1 noloop
    sy "Ugh."
    play voice2 d1s2_hmm noloop
    mc "What's wrong, Stacy?"
    hide sy_annoyed01
    show expression cc.get_expression_image("sy", "sad01") as sy_sad01
    play voice3 stacy_angryhuh noloop
    sy "Last night I dreamed I was renovating this place."
    sy "And now I have to do it while I'm awake too."
    play voice2 d9s2_yeah noloop volume 1.6
    mc "It will be worth it."
    return
label q_inter_sy_27:
    show expression cc.get_expression_image("sy", "excited01")
    play voice3 stacy_laugh4 noloop
    sy "It's really awesome that we've already made our first movie."
    sy "And all the hard work with the renovation is just going to make the next ones better and better."
    play voice2 mc_yes_yes1 noloop
    mc "Exactly."
    return
label q_inter_sy_28:
    show expression cc.get_expression_image("sy", "serious01")
    play voice3 stacy_laugh4 noloop
    sy "Almost there, [mcname]."
    sy "We're not going to let the renovation win!"
    return
label q_inter_sy_29:
    show expression cc.get_expression_image("sy", "annoyed01")
    play voice3 stacy_laugh4 noloop
    sy "Just a few more hours. That is all it is going to take."
    return
label q_inter_sy_30:
    show expression cc.get_expression_image("sy", "excited01")
    play voice3 stacy_laugh4 noloop
    sy "It's going to be so worth it in the end."
    sy "I can almost see it."
    return
label q_inter_sy_31:
    show expression cc.get_expression_image("sy", "smile01")
    play voice3 stacy_laugh4 noloop
    sy "It still feels like some wonderful dream. But we made it."
    sy "Now I feel like we can do anything!"
    return
label q_inter_sy_32:
    show expression cc.get_expression_image("sy", "smile01")
    play voice3 stacy_laugh4 noloop
    sy "Mmm. Sleeping on the new bed really makes all the long days worth it doesn't it?"
    mc "Damn straight."
    return