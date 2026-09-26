image lst_mh_sad01_flip:
    cc.get_expression_image("mh", "sad01")
    xzoom -1
    xanchor 0.0
    yanchor 0.0
    ypos 30
    xpos -80
label sm1cs_mh003_1i:
    scene black with dissolve
    $ curr_position = LLY_DOOR
    $ LocationController.draw_current_location("mh")
    show expression cc.get_expression_image("mh", "sad01") as lst_mh_sad01 with dissolve
    play voice2 d2s9_mchey noloop
    mc "There's something I want to talk to you about."
    mc "You've been on my mind a lot since you started helping us out with the studio."
    hide lst_mh_sad01
    show lst_mh_sad01_flip
    mc "And I was wondering... Would you want to give \"us\" another shot?"
    hide lst_mh_sad01_flip
    show expression cc.get_expression_image("mh", "neutral01") as lst_mh_neutral01
    play voice3 lissa_moan2 noloop
    mh "Well this comes as a shock."
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, I know."
    hide lst_mh_neutral01
    show expression cc.get_expression_image("mh", "neutral02") as lst_mh_neutral02
    play voice3 lissa_thinking1 noloop
    mh "After all, you're the one who said we didn't have a relationship before."
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah..."
    hide lst_mh_neutral02
    show expression cc.get_expression_image("mh", "neutral01") as lst_mh_neutral01
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "Why now? After telling Stacy we weren't seeing each other before? Why come here and ask me out?"
    play voice2 mc_thinking_mmm3 noloop
    mc "I don't know. You've just been on my mind a lot and... I would just like to see more of you."
    hide lst_mh_neutral01
    show expression cc.get_expression_image("mh", "sad01") as lst_mh_sad01
    play voice3 dahlia_sex_closedmoan1 noloop
    mh "I'd be lying if I didn't say that I've been thinking about you too."
    play voice2 mc_yes_yeah8 noloop
    mc "Really?"
    mh "I've always liked you, [mcname]. Even when..."
    hide lst_mh_sad01
    show expression cc.get_expression_image("mh", "neutral02") as lst_mh_neutral02
    play voice3 dahlia_thinking_hmm1 noloop
    mh "We don't need to get into that right now. But yes, I've been thinking about you too."
    play voice2 mc_happy_a1 noloop
    mc "I mean, I am happy to hear that."
    hide lst_mh_neutral02
    show expression cc.get_expression_image("mh", "neutral01") as lst_mh_neutral01
    play voice3 dahlia_thinking_hmm2 noloop
    mh "I still have my reservations but... I will let you take me out on a date."
    play voice2 mc_angry_really noloop
    mc "Really!?"
    mh "Yes, really. You can take me out on a date. But this time, things are going to be different."
    mc "Oh?"
    hide lst_mh_neutral01
    show expression cc.get_expression_image("mh", "neutral02") as lst_mh_neutral02
    play voice3 lissa_haha2 noloop
    mh "You need to wine and dine me, you need to take me out on dates. You need to prove to me that this time is different."
    play voice2 mc_yes_okay2 noloop
    mc "Okay! Yes, absolutely! Whatever I need to do."
    hide lst_mh_neutral02
    show expression cc.get_expression_image("mh", "smile01") as lst_mh_smile01
    play voice3 dahlia_happy_hmm2 noloop
    mh "Then I look forward to your call."
    play voice2 mc_happy_yes1 noloop
    mc "Good, I'll definitely call you!"
    hide lst_mh_smile01
    show expression cc.get_expression_image("mh", "smile02") as lst_mh_smile02
    play voice3 lissa_aga noloop
    mh "I'll see you later, [mcname]."
    play voice2 mc_hey_bye2 noloop
    mc "Yeah! I'll see you later!"
    $ curr_position = LLY_OUTSIDE
    $ StoryController.end_scene(MH_STORY, 0, 30, 0)
    return