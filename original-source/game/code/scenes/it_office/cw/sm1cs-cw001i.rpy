label sm1cs_cw001i:
    $ LocationController.draw_current_location("cw")
    play voice2 mc_hey_hey8 noloop
    show expression cc.get_expression_image("cw", "neutral01") as lit_cw_neutral
    mc "Hello Ms. Watts."
    play voice3 girl29_hey_happy noloop
    hide lit_cw_neutral
    show expression cc.get_expression_image("cw", "serious01") as lit_cw_serious
    cw "Hello, [mcname]. Can you come meet me when you have some free time?"
    mc "Uh sure. Will do."
    $ StoryController.end_scene(CW_STORY)
    return