label sm1ms024i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01")
    play voice3 stacy_happy_wooh1 noloop
    sy "[mcname]! It's done!"
    play voice2 mc_surprised_uh3 noloop
    mc "What's done?"
    sy "The video!"
    mc "Really?"
    sy "Yep! Come here!"
    $ StoryController.end_scene(MS)
    return