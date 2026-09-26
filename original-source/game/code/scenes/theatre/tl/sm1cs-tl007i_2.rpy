label sm1cs_tl007i_2:
    $ LocationController.draw_current_location("tl")
    if player.has_played_scene("sm1cs_tl007i_1") and player.has_played_scene("sm1ms020") and not player.has_played_scene("sm1cs_tl007"):
        show expression cc.get_expression_image("tl", "excited01") as lth_tl_excited01
        play voice2 mc_hey_hey10 noloop
        mc "Hey, Taisia! The room is ready!"
        hide lth_tl_excited01
        show expression cc.get_expression_image("tl", "smile01") as lth_tl_smile01
        play voice3 girl24_happy_phew1 noloop
        tl "Sick. I'll be by later then."
        hide lth_tl_smile01
        show expression cc.get_expression_image("tl", "curious01") as lth_tl_curious01
        play voice2 mc_thinking_oh1 noloop
        mc "Oh shit - sorry, Stacy just texted me. I have to run!"
    $ StoryController.end_scene(TL_STORY)
    return