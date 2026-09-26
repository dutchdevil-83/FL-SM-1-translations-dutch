label sm1cs_ag003i:
    $ LocationController.draw_current_location("cw")
    show expression cc.get_expression_image("cw", "neutral01") as lst_cw_neutral01
    play voice3 girl29_arrogant_huh noloop
    cw "What can I do for you, [mcname]?"
    play voice2 mc_thinking_emm1 noloop
    mc "I was just wondering if you know where Anna is?"
    hide lst_cw_neutral01
    show expression cc.get_expression_image("cw", "neutral02") as lst_cw_neutral02
    play voice3 girl29_thinking_oh noloop
    cw "I believe she said something about working at home or a coffee shop or something."
    cw "Is there something you need help with?"
    play voice2 mc_no_nope1 noloop
    mc "Uhm, nope! Just wanted to talk with her."
    hide lst_cw_neutral02
    show expression cc.get_expression_image("cw", "curious01") as lst_cw_curious01
    play voice3 girl29_yes_aga1 noloop
    cw "Uh huh."
    hide lst_cw_curious01
    $ StoryController.end_scene(AG_STORY, 0, 15, 0)
    return