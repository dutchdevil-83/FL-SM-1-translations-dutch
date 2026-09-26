label sm1mv01s07i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_hey noloop
    sy "Hey, [mcname]."
    play voice2 mc_hey_hey5 noloop
    mc "Hey there."
    sy "I want to show you something on the computer."
    mc "Alright."
    $ StoryController.end_scene(MOVIE_PIRATES)
    return