label sm1cs_dc005i:
    $ LocationController.draw_current_location("dc")
    show expression cc.get_expression_image("dc", "embarrassed01") as lpa_dc_embarrassed01
    play voice2 d2s9_mchey noloop
    mc "Debbie, hey!"
    play voice3 girl36_hey_angry1 noloop
    dc "Uhm... hi, [mcname]..."
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "Okay, seriously - what's going on?"
    play voice3 girl36_happy_mmm noloop
    dc "I, uhm... we should talk."
    mc "Okay?"
    dc "But not right now... maybe we can meet at the coffee shop sometime I'm off duty?"
    mc "Sure, you just let me know when."
    hide lpa_dc_embarrassed01
    show expression cc.get_expression_image("dc", "serious01") as lpa_dc_serious
    play voice3 girl36_yes_yeah noloop
    dc "I will."
    dc "I'll see you later, [mcname]."
    $ StoryController.end_scene(DC_STORY)
    return