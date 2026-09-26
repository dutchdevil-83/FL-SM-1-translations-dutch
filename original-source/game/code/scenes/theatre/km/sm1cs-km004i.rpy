label sm1cs_km004i:
    $ LocationController.draw_current_location("km")
    show expression cc.get_expression_image("km", "smile01") as lth_km_smile01
    play voice3 girl31_thinking_oh noloop
    km "Great timing. I was just about to text you."
    play voice2 mc_yes_yeah8 noloop
    mc "Cool. Text me about what?"
    play voice3 girl31_happy_laugh2 noloop
    km "I'm about to launch my prank war against Veronica."
    km "I was beginning to worry that I would have to start without you."
    if curr_position != LTH_DRESSINGROOM_2:
        hide lth_km_smile01
        show expression cc.get_expression_image("km", "neutral01") as lth_km_neutral01
        play voice3 girl31_happy_mmm1 noloop
        km "Come on. We need to go to the dressing room."
        play voice2 mc_yes_okay1 noloop
        mc "Okay."
    $ StoryController.end_scene(KM_STORY)
    return