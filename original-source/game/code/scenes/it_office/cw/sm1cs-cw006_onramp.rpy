label sm1cs_cw006_onramp:
    $ LocationController.draw_current_location("cw")
    show expression cc.get_expression_image("cw", "neutral01") as lit_cw_neutral
    play voice2 mc_hey_hey3 noloop
    mc "Hey Claire, do you have a minute?"
    play voice3 girl29_yes_serious noloop
    cw "Yes, but be quick about it."
    mc "I'd rather not discuss it here. It's... it's kind of private."
    hide lit_cw_neutral
    show expression cc.get_expression_image("cw", "serious01") as lit_cw_serious
    play voice3 girl29_arrogant_huh noloop
    cw "Private? Is this actually important, or are you wasting my time?"
    play voice2 mc_thinking_mmm4 noloop
    mc "It is important to me."
    cw "*sighs* Alright. Conference room in five."
    $ player.progress_storyline(CW_STORY, -1)
    if player.get_choice("sm1ms_cw006_offramp_1"):
        jump sm1cs_cw006_onramp_1
    if player.get_choice("sm1ms_cw006_offramp_2"):
        jump sm1cs_cw006_onramp_2