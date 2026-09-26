label sm1cs_my002i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_arrogant_huh5 noloop
    if persistent.is_special:
        sy "How'd your date with Mom go!"
    else:
        sy "How'd your date with Melony go!"
    play voice2 mc_thinking_oh1 noloop
    mc "I think it went well! Had some good bants, and, you know, fancy food, and..."
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "annoyed1")
    play voice3 stacy_surprised_ah2 noloop
    sy "Bants, really? That's the word you want to use? {i}Bants{/i}?"
    play voice2 mc_yes_yeah2 noloop
    mc "That's what I said."
    sy "Ugh, I need more coffee for this..."
    $ StoryController.end_scene(MY_STORY)
    return