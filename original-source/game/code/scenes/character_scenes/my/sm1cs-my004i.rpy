label sm1cs_my004i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_hey_attention1 noloop
    sy "Hey! What have you got planned today?"
    play voice2 mc_thinking_hmm5 noloop
    mc "Uhm, nothing? Or at least nothing out of the ordinary?"
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
    play voice3 stacy_thinking_oh1 noloop
    sy "Good! Stay right there then!"
    play voice2 mc_thinking_mmm4 noloop
    mc "What are you doing...?"
    sy "It's a surprise!"
    mc "Stacy-"
    sy "I'll be right back!"
    $ StoryController.end_scene(MY_STORY)
    return