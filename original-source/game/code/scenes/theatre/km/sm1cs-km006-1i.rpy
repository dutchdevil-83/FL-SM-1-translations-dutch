label sm1cs_km006_1i:
    $ LocationController.draw_current_location("vs")
    show expression cc.get_expression_image("vs", "neutral01") as lth_vs_neutral01
    play voice2 mc_thinking_mmm5 noloop
    mc "I'm still having trouble figuring out how to talk to Kellie about you."
    play voice3 girl33_yes_aga noloop
    vs "Same here. But I have caught her watching me more than usual."
    hide lth_vs_neutral01
    show expression cc.get_expression_image("vs", "excited01") as lth_vs_excited01
    play voice3 girl33_happy_laugh1 noloop
    vs "You weren't lying, she is totally crushing on me."
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, but if we don't figure out something soon, she might panic and quit the theater."
    vs "No. We can't have that."
    hide lth_vs_excited01
    show expression cc.get_expression_image("vs", "curious01") as lth_vs_curious01
    play voice3 girl33_thinking_hmm1 noloop
    vs "Think, [mcname] think. We have to save Kellie from doing something she'll regret."
    play voice2 mc_thinking_mmm4 noloop
    mc "I know. Mmm. I think I got something."
    vs "What?"
    mc "I'll text you the details later. For now, I gotta find Kellie."
    hide lth_vs_curious01
    show expression cc.get_expression_image("vs", "excited01")
    play voice3 girl33_surprised_oh noloop
    vs "Oh, mystery. I love it. Good luck, [mcname]."
    play voice2 mc_happy_a1 noloop
    mc "Thanks."
    $ StoryController.end_scene(KM_STORY)
    return