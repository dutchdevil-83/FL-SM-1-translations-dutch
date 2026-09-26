label sm1cs_km006_2i:
    $ LocationController.draw_current_location("km")
    show expression cc.get_expression_image("km", "neutral01") as lth_km_neutral01
    play voice2 mc_hey_hey5 noloop
    mc "Hey Kellie."
    play voice3 girl31_disappointed_ehh3 noloop
    km "[mcname]."
    mc "You okay?"
    hide lth_km_neutral01
    show expression cc.get_expression_image("km", "embarrassed01") as lth_km_embarrassed01
    play voice3 girl31_yes_simple1 noloop
    km "Yeah just... wary. The last time I saw you..."
    km "*whispers* Was also the time you came to Denise's desk."
    mc "Hey, that wasn't a one-man job."
    hide lth_km_embarrassed01
    show expression cc.get_expression_image("km", "annoyed01") as lth_km_annoyed01
    play voice3 girl31_disappointed_mff1 noloop
    km "Ew. What... what did you want to talk about?"
    play voice2 mc_thinking_hm noloop
    mc "I wanted to see if we could practice again."
    if False:
        mc "Gotta be ready for the next time I'm on stage with you."
        hide lth_km_annoyed01
        show expression cc.get_expression_image("km", "neutral01")
        play voice3 girl31_thinking_mmm6 noloop
        km "Mmmm. It's good to see you taking the initiative, [mcname]."
    else:
        mc "Every little bit is going to help me out when I get another chance to audition."
        hide lth_km_annoyed01
        show expression cc.get_expression_image("km", "neutral01")
        play voice3 girl31_thinking_mmm6 noloop
        km "Okay. I'll help you out."
    km "But that's all we're doing. Just practicing."
    $ StoryController.end_scene(KM_STORY)
    return