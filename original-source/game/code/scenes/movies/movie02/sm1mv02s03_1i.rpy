label sm1mv02s03_1i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_happy_a1 noloop
    mc "All right, I think we have everything we need to start building sets."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_yes_yeah2 noloop
    sy "Hell yeah! Let's head over to Kanya's!"
    $ StoryController.end_scene(MOVIE_SCIFI)
    return