init 3 python:
    CharacterController.get_character("lm").interactions = [
            {LABEL: "q_inter_lm_1", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_lm_2", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_lm_3", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_lm_4", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_lm_5", LOCATIONS: [IT_OFFICE]},
            ]
    CharacterController.get_character("lm").default_expression = "neutral01"

label q_inter_lm_1:
    show expression cc.get_expression_image("lm", "neutral01")
    play voice3 girl36_hey_angry1 noloop
    lm "Can you do me a favor?"
    play voice2 mc_yes_sure1 noloop
    mc "Sure, what's up?"
    lm "If you see April messing around the the database, could you tell me?"
    mc "Sure?"
    lm "Awesome. Their good changes, I just need to know she's doing stuff."
    return
label q_inter_lm_2:
    show expression cc.get_expression_image("lm", "smile01")
    play voice3 girl36_hey_greeting3 noloop
    lm "Morning, [mcname]."
    play voice2 d1s2_mchey noloop
    mc "Hey, Libby. How's your morning going?"
    lm "Great! Claire and I went out to this diner last night and I'm still thinking about it. God, it was good..."
    return
label q_inter_lm_3:
    show expression cc.get_expression_image("lm", "neutral01")
    play voice3 girl36_thinking_oh noloop
    lm "Oh, [mcname]. if you see April can you tell her to come see me? I have a doozy of an error I need some help with."
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, I'll let her know."
    lm "Thanks!"
    return
label q_inter_lm_4:
    show expression cc.get_expression_image("lm", "sad01")
    play voice3 girl36_surprised_huh3 noloop
    lm "Have you seen these projected timelines from Claire?"
    play voice2 mc_no_no9 noloop
    mc "Not yet?"
    lm "Ugh, I can already feel the crunch time coming..."
    return
label q_inter_lm_5:
    show expression cc.get_expression_image("lm", "neutral01")
    play voice3 girl36_hey_greeting1 noloop
    lm "[mcname], do you know where Anna is?"
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, she should be around somewhere."
    lm "Great. We need to do an overview meeting of how the database is functioning."
    return