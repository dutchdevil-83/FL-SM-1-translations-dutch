label sm1cs_tl007i_1:
    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "depressed01") as lth_tl_depressed01
    play voice3 girl24_surprised_eeh2 noloop
    tl "So, when can I move in?"
    play voice2 d2s9_confused noloop volume 1.7
    mc "Uhm..."
    if player.has_played_scene("sm1ms020"):
        mc "Well the studio is all renovated, so... whenever?"
        hide lth_tl_depressed01
        show expression cc.get_expression_image("tl", "excited01") as lth_tl_excited01
        play voice3 girl24_yes_aga noloop
        tl "Sick. I'll be by later then."
        play voice2 mc_surprised_oh2 noloop
        mc "Oh shit - sorry, Stacy just texted me. I have to run!"
        $ player.progress_storyline(TL_STORY, 2)
    else:
        mc "We just need a little more time to get the studio ready."
        hide lth_tl_depressed01
        show expression cc.get_expression_image("tl", "annoyed01") as lth_tl_annoyed01
        play voice3 girl24_disappointed_eeh2 noloop
        tl "Ugh, hurry up."
        play voice2 mc_hey_hey7 noloop
        mc "We're doing our best!"
        hide lth_tl_annoyed01
        show expression cc.get_expression_image("tl", "depressed01")
        play voice3 girl24_disappointed_neh noloop
        tl "I really need a new place to live."
        play voice2 mc_yes_sure1 noloop
        mc "As soon as the room is ready, we'll let you know. I promise."
    $ StoryController.end_scene(TL_STORY)
    return