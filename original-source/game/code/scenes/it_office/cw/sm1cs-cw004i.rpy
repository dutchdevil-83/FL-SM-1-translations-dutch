label sm1cs_cw004i:
    $ LocationController.draw_current_location("cw")
    show expression cc.get_expression_image("cw", "neutral01") as lit_cw_neutral
    play voice2 d2s9_mchey noloop
    mc "Hello, Ms. Watts."
    mc "Everything going okay?"
    hide lit_cw_neutral
    show expression cc.get_expression_image("cw", "embarrassed01") as lit_cw_embarrassed01
    play voice3 girl29_no_simple noloop
    cw "As a matter of fact, it's not, Mr. Young."
    hide lit_cw_embarrassed01
    show expression cc.get_expression_image("cw", "neutral01") as lit_cw_neutral
    play voice2 mc_surprised_huh7 noloop
    mc "What's wrong? Anything I can help with?"
    play voice3 girl29_yes_serious noloop
    cw "Actually, yes. I need you to meet me Friday, here at the office."
    mc "Oh. Okay. Do you just want to tell me now?"
    hide lit_cw_neutral
    show expression cc.get_expression_image("cw", "serious01")
    play voice3 girl29_no_uhuh noloop
    cw "No. It's between us. Just...{w} Meet me here at the office kitchen, Friday evening."
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    $ StoryController.end_scene(CW_STORY)
    return