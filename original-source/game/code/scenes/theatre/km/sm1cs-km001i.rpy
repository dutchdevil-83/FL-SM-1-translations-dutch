label sm1cs_km001i:
    $ LocationController.draw_current_location("km")
    show expression cc.get_expression_image("km", "annoyed01") as lth_km_annoyed01
    play voice2 d2s9_mchey noloop
    mc "Hey Kellie."
    play voice3 girl31_arrogant_geh noloop
    km "Hey yourself."
    mct "Wow. Did someone spit in her coffee or something?"
    play voice2 mc_thinking_mmm3 noloop
    mc "I just wanted to ask if you had any tips for me."
    play voice3 girl31_arrogant_huh1 noloop
    km "Tips?"
    mc "You know, to get better at acting."
    if True:
        mc "I don't want to just be a stagehand my whole time here."
    else:
        mc "Just because I got a part doesn't mean I don't want to hone my skills a bit."
    hide lth_km_annoyed01
    show expression cc.get_expression_image("km", "ask01")
    play voice3 girl31_thinking_hmm1 noloop
    km "Hmmm."
    km "Sure. I might have something. Go to backstage and grab two prop swords and shields. The Roman ones."
    play voice2 mc_yes_okay2 noloop
    mc "Okay. Then what?"
    km "Meet me on stage. Duh."
    $ StoryController.end_scene(KM_STORY)
    return