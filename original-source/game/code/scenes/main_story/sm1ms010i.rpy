label sm1ms010i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    pause 0.2
    play voice2 d1s5_mcthinks noloop
    mc "Stacy, I wanted to...{w=1.2}{nw}"
    play voice3 stacy_no2 noloop
    sy "I gotta go get changed."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh... {w}Where are you headed off to?"
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_happy_laugh1 noloop
    sy "I want to check out the local sex shop."
    $ StoryController.end_scene(MS, 0, 10, 0)
    return