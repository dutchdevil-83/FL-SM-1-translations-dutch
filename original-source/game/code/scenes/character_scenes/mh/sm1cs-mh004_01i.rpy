label sm1cs_mh004_01i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    play voice3 stacy_hey noloop
    sy "I never got the chance to ask, how'd your date with Lyssa go?"
    play voice2 mc_thinking_oh1 noloop
    mc "It went well, I think. We talked and... Well, there's some work I need to do."
    hide lst_sy_ask1
    show expression cc.get_expression_image("sy", "annoyed1") as lst_sy_annoyed1
    play voice3 stacy_angry noloop
    sy "Good. You better get her back, [mcname]."
    play voice2 mc_yes_yeah3 noloop
    mc "I'm trying! I just need to be my usually charming self."
    hide lst_sy_annoyed1
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice3 stacy_arrogant_ha1 noloop
    sy "...Maybe better than your usual self."
    play voice2 mc_hey_hey9 noloop
    mc "Hey!"
    hide lst_sy_naughty1
    show expression cc.get_expression_image("sy", "annoyed1") as lst_sy_annoyed1
    play voice3 stacy_angry_breath1 noloop
    sy "I'm serious! Do whatever it takes."
    play voice2 mc_yes_ugu1 noloop
    mc "I am, I am... I think I got our next date figured out."
    hide lst_sy_annoyed1
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    play voice3 stacy_arrogant_huh1 noloop
    sy "Good! Where you going?"
    mc "The arcade."
    sy "Seriously?"
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh. Trust me, this is a good idea."
    sy "If you say so... I just want you to do everything you can to win her back."
    hide lst_sy_ask1
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    play voice3 stacy_happy_relief1 noloop
    sy "Lyssa is great, and I like when she's around a lot."
    sy "And I like how you are when she's around."
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Really?"
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "smile2") as lst_sy_smile2
    play voice3 stacy_happy_laugh2 noloop
    sy "Would I be her number one cheerleader if I thought otherwise?"
    play voice2 mc_thinking_mmm4 noloop
    mc "You've got a good point there..."
    hide lst_sy_smile2
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_hey_angry1 noloop
    sy "Now get out there, and woo that lady!"
    play voice2 mc_yes_yes1 noloop
    mc "I will - thanks, Stacy!"
    $ StoryController.end_scene(MH_STORY, 0, 15, 0)
    return