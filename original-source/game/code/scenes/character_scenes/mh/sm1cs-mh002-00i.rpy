label sm1cs_mh002_00i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice2 d2s9_mchey noloop
    mc "Hey Stacy. Ready to go to Lyssa's office?"
    play voice3 stacy_yes_yeah2 noloop
    sy "Oh yeah."
    $ LocationController.draw_current_location("sy")
    hide lst_sy_naughty1
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    play voice3 stacy_thinking_hmm1 noloop
    sy "Hmmm."
    sy "Just give me a minute. Let me freshen up."
    $ StoryController.end_scene(MH_STORY)
    return