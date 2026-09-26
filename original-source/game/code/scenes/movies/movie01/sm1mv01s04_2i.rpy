label sm1mv01s04i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01")
    play voice2 mc_happy_a1 noloop
    mc "All right, Stacy. Do we have everything we need to build the sets?"
    play voice3 stacy_yes_simple1 noloop
    sy "We do, you ready to get started?"
    mc "Yep, I'm ready!"
    $ StoryController.end_scene(MOVIE_PIRATES)
    return