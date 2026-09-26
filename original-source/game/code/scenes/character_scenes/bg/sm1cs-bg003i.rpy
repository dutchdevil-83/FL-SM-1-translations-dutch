label sm1cs_bg003i:
    $ LocationController.draw_current_location("bg")
    show expression cc.get_expression_image("bg", "smile01") as lpd_bg_smile
    play voice3 girl26_hey_greeting noloop
    bg "Hey, [mcname]."
    play voice2 mc_happy_yay2 noloop
    mc "Hey, Amore! What's up?"
    bg "Have you seen the photos yet?"
    mc "The photos...?"
    hide lpd_bg_smile
    show expression cc.get_expression_image("bg", "smile02") as lpd_bg_smile_2
    play voice3 girl26_thinking_hmm1 noloop
    bg "You know, from our photoshoot?"
    play voice2 mc_no_no10 noloop
    mc "No! They're done?"
    bg "Yeah!"
    hide lpd_bg_smile_2
    show expression cc.get_expression_image("bg", "neutral01") as lpd_bg_neutral
    play voice3 girl26_angry_cough noloop
    bg "Kanya!"
    hide lpd_bg_neutral
    $ StoryController.end_scene(BG_STORY)
    return