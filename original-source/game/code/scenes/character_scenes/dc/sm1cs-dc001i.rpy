label sm1cs_dc001i:
    $ LocationController.draw_current_location("dc")
    show expression cc.get_expression_image("dc", "embarrassed01") as lpa_dc_embarrassed01
    play voice3 girl36_hey_angry2 noloop
    dc "Excuse me, sir."
    play voice2 mc_yes_yes7 noloop
    mc "Can I help you, Officer...?"
    dc "Callahan. Debbie Callahan."
    mc "Nice to meet you Officer Callahan! I'm [mcname]."
    hide lpa_dc_embarrassed01
    show expression cc.get_expression_image("dc", "serious01") as lpa_dc_serious01
    play voice3 girl36_yes_aga noloop
    dc "Okay? Anyway, there have been reports of a creep around the park. Please let me know if you see anything suspicious."
    play voice2 mc_yes_sure1 noloop
    mc "Sure. If I see something, I'll say something."
    hide lpa_dc_serious01
    show expression cc.get_expression_image("dc", "serious02") as lpa_dc_serious02
    play voice3 girl36_disappointed_oof noloop
    dc "Please do! He's been seen stalking around the park at night."
    play voice2 mc_yes_okay1 noloop
    mc "I'll keep that in mind."
    $ StoryController.end_scene(DC_STORY, 0, 15, 0)
    return