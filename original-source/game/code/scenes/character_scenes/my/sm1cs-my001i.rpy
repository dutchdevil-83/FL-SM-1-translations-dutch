label sm1cs_my001i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_hey_hey7 noloop
    mc "Hey, Stacy. Can I get your advice on something?"
    play voice3 stacy_yes_ugu1 noloop
    sy "Sure, what's up?"
    mc "Uhhh, let me show you."
    hide lst_sy_neutral01
    $ StoryController.end_scene(MY_STORY)