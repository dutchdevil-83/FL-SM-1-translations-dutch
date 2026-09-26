label sm1ms009_01i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    play voice3 stacy_happy_yay1 noloop
    sy "Sweet! Kanya said she could be here in like an hour!"
    play voice2 mc_surprised_oh3 noloop
    mc "Sweet! Uhm... what do we have to do?"
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_happy_laugh1 noloop
    sy "Clean! Get the studio ready!"
    play voice2 mc_yes_okay3 noloop
    mc "Uhm, okay!"
    $ StoryController.end_scene(MS)
    return