label sm1cs_my003i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_arrogant_huh1 noloop
    sy "How did the art exhibit work out?"
    play voice2 mc_yes_yeah4 noloop
    if persistent.is_special:
        mc "It went great! Mom loved it."
    else:
        mc "It went great! Melony loved it."
    mc "But I would have loved if you had given me a heads up that it was a nude art exhibit."
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "naughty01")
    play voice3 stacy_arrogant_ha2 noloop
    sy "What's the fun in that?"
    $ StoryController.end_scene(MY_STORY)
    return