label sm1cs_cw003i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "curious01") as lst_sy_curious01
    play voice2 mc_thinking_hm noloop
    mc "Do you remember my bosse's boss Claire?"
    play voice3 stacy_thinking_emm4 noloop
    sy "I guess... Let's talk at my desk!"
    hide lst_sy_curious01
    $ StoryController.end_scene(CW_STORY)
    return