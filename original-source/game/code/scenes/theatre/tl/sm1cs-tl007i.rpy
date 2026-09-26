label sm1cs_tl007i:
    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "smile01") as lth_tl_smile01
    tl "So, when can I move in?"
    mc "Uhm..."
    if player.has_played_scene("sm1ms020"):
        mc "Well the studio is all renovated, so... whenever?"
        hide lth_tl_smile01
        show expression cc.get_expression_image("tl", "excited01") as lth_tl_excited01
        tl "Sick. I'll be by later then."
        mc "Oh shit - sorry, Stacy just texted me. I have to run!"
        $ StoryController.end_scene(TL_STORY, 0, 0, 0)
    else:
        mc "We just need a little more time to get the studio ready."
        hide lth_tl_smile01
        show expression cc.get_expression_image("tl", "depressed01") as lth_tl_depressed01
        tl "Ugh, hurry up."
        mc "We're doing our best!"
        tl "I really need a new place to live."
        mc "As soon as the room is ready, we'll let you know. I promise."
        $ player.progress_storyline(TL_STORY, -1)
    return