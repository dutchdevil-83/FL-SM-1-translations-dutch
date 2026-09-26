label sm1cs_tl003i:
    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "ask01") as lth_tl_ask01
    play voice3 girl24_hey_greeting noloop
    tl "'Sup, [mcname]? You make any progress with the film?"
    play voice2 mc_yes_yeah2 noloop
    mc "Actually, yeah. I think we're ready to film."
    hide lth_tl_ask01
    show expression cc.get_expression_image("tl", "excited01") as lth_tl_excited01
    play voice3 girl24_surprised_ohmy1 noloop
    tl "Really!?!"
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, we got-"
    hide lth_tl_excited01
    show expression cc.get_expression_image("tl", "smile01")
    play voice3 girl24_happy_laugh5 noloop
    tl "Shut up, let's go!"
    play voice2 mc_surprised_uh3 noloop
    mc "I - what? You're just ready to go?"
    tl "I'm always ready to go. Come on!"
    $ StoryController.end_scene(TL_STORY)
    return