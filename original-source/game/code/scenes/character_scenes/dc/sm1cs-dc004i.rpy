label sm1cs_dc004i:
    $ LocationController.draw_current_location("dc")
    show expression cc.get_expression_image("dc", "serious01") as lpa_dc_serious
    play voice2 mc_happy_yay2 noloop
    mc "Debbie! Hey!"
    hide lpa_dc_serious
    show expression cc.get_expression_image("dc", "embarrassed01") as lpa_dc_embarrassed01
    play voice3 girl36_thinking_oh noloop
    dc "Oh, uhm, hi [mcname]."
    play voice2 mc_thinking_hmm2 noloop
    mc "Everything okay?"
    $ StoryController.end_scene(DC_STORY)
    return