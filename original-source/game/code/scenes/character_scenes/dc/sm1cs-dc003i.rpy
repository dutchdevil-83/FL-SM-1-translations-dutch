label sm1cs_dc003i:
    $ LocationController.draw_current_location("dc")
    show expression cc.get_expression_image("dc", "embarrassed01") as lpa_dc_embarrassed01
    play voice3 girl36_hey_greeting3 noloop
    dc "[mcname]! I was hoping to bump into you!"
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah? What's up, Debbie?"
    dc "I thought of a way to pay you back!"
    mc "Oh, great!"
    hide lpa_dc_embarrassed01
    show expression cc.get_expression_image("dc", "serious01") as lpa_dc_serious01
    play voice3 girl36_thinking_eem noloop
    dc "Do you like coffee?"
    play voice2 mc_yes_sure1 noloop
    mc "I do!"
    dc "Well can I take you out to a coffee to thank you for helping the other night? As well as an apology for mistaking you for the creep?"
    mc "Of course, Debbie!"
    hide lpa_dc_serious01
    show expression cc.get_expression_image("dc", "serious02") as lpa_dc_serious02
    play voice3 girl36_happy_yay noloop
    dc "Great, there's a spot close by that I really like."
    play voice2 mc_thinking_hmm4 noloop
    mc "Sounds awesome, lead the way."
    $ StoryController.end_scene(DC_STORY, 0, 15, 0)
    return