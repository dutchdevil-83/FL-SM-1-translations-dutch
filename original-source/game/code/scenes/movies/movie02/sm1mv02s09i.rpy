label sm1mv02s09i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_thinking_oh1 noloop
    sy "Oh hey, [mcname]."
    play voice2 d1s5_mcthinks noloop
    mc "Ready to film the finale of the movie?"
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_yes noloop
    sy "Hell yes I am! Let's get over to the Photo Dojo!"
    $ StoryController.end_scene(MOVIE_SCIFI)
    return