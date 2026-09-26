label sm1cs_ag002i:
    $ LocationController.draw_current_location("cw")
    show expression cc.get_expression_image("ag", "smile01") as lst_ag_smile01
    play voice3 girl27_hey_greeting noloop
    ag "Hey, [mcname]! Good work today."
    play voice2 mc_yes_aga2 noloop
    mc "Thanks, Anna!"
    play voice3 girl27_thinking_hmm8 noloop
    ag "Say..."
    hide lst_ag_smile01
    show expression cc.get_expression_image("ag", "curious01") as lst_ag_curious01
    play voice3 girl27_arrogant_huh3 noloop
    ag "I was going to head to a bar close by for happy hour. Would you want to join me?"
    play voice2 mc_yes_sure1 noloop
    mc "Sure! Lead the way."
    hide lst_ag_curious01
    show expression cc.get_expression_image("ag", "excited01") as lst_ag_excited01
    ag "Awesome!"
    hide lst_ag_excited01
    $ StoryController.end_scene(AG_STORY, 0, 15, 0)
    return