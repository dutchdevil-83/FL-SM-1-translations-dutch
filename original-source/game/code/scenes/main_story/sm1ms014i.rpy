label sm1ms014i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    play voice3 stacy_angry noloop
    sy "All right, is today the big day when we start the renovation?"
    play voice2 mc_yes_yeah2 noloop
    mc "I think so."
    $ StoryController.end_scene(MS)
    return