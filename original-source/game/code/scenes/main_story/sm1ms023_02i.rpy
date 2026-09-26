label sm1ms023_02i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral02") as sy_neutral02
    play voice2 d1s2_hmm noloop volume 1.7
    mc "How's the edit coming?"
    play voice3 stacy_yes_yap1 noloop
    sy "Good! I actually just got picture lock."
    mc "Sick, so we can send it?"
    hide sy_neutral02
    show expression cc.get_expression_image("sy", "neutral01")
    play voice3 stacy_no1 noloop
    sy "Not yet."
    play voice2 mc_surprised_why3 noloop
    mc "Why not?"
    sy "Let me show you."
    $ StoryController.end_scene(MS)
    return