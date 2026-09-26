label sm1ms023i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral02")
    play voice3 stacy_hey_happy2 noloop
    sy "Hey, [mcname], I need your help."
    play voice2 mc_yes_yeah8 noloop
    mc "What's up, Stacy?"
    sy "We need to go over to the editing station."
    mc "Lead the way."
    $ StoryController.end_scene(MS)
    return