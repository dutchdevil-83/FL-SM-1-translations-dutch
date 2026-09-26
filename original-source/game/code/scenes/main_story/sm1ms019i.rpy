label sm1ms019i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_hey noloop
    sy "I think we're almost done with the renovation, [mcname]!"
    play voice2 mc_happy_yay1 noloop
    mc "I think so too!"
    play voice3 stacy_happy_relief1 noloop
    sy "Let's pitter patter then!"
    hide lst_sy_excited01
    $ StoryController.end_scene(MS)
    return