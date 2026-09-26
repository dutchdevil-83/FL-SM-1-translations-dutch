label sm1mv02s06i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_surprised_huh1 noloop
    sy "Is it time for the next scene?"
    play voice2 mc_yes_yeah1 noloop
    mc "I think so!"
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "excited01") as lit_sy_excited01
    play voice3 stacy_happy_yay1 noloop
    sy "Great! Let's get everyone and head over to the Photo Dojo!"
    play voice2 d1s5_mchappy noloop
    mc "Sounds good!"
    $ StoryController.end_scene(MOVIE_SCIFI)
    return