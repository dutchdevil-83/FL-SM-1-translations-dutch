label sm1ms025i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as sy_excited
    play voice2 mc_hey_hey7 noloop
    mc "Hey, Stacy."
    play voice3 stacy_hey_happy2 noloop
    sy "Hey, [mcname]. I've got good news."
    hide sy_excited
    show expression cc.get_expression_image("sy", "neutral02")
    play voice2 d1s2_hmm noloop
    mc "What?"
    play voice3 stacy_thinking_hmm4 noloop
    sy "Follow me to the computer. It's better to show you."
    $ StoryController.end_scene(MS)
    return