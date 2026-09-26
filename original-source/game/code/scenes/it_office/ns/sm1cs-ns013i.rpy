label sm1cs_ns013i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral02") as lit_sy_neutral2
    play voice2 mc_hey_hey7 noloop
    mc "Hey Stacy."
    play voice3 stacy_hey_happy1 noloop
    sy "Hello there."
    hide lit_sy_neutral2
    show expression cc.get_expression_image("sy", "smile01")
    play voice3 stacy_thinking_emm4 noloop
    sy "Come upstairs. It's getting late and I want to show you something."
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    $ StoryController.end_scene(NS_STORY)
    return