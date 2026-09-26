label sm1mv02s03_2i:
    $ LocationController.draw_current_location("kv")
    show expression cc.get_expression_image("kv", "neutral01") as lpd_dc_neutral1
    play voice3 kanya_hey_simple1 noloop
    kv "Hey, [mcname]."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh hey, Kanya. I'm going to keep working on the set."
    hide lpd_dc_neutral1
    show expression cc.get_expression_image("kv", "smile01") as lpd_dc_smile1
    play voice3 kanya_yes_yeah1 noloop
    kv "Awesome. Holler when you're done and we can get these green screens set up."
    play voice2 mc_yes_aga2 noloop
    mc "Will do!"
    $ StoryController.end_scene(MOVIE_SCIFI)
    return