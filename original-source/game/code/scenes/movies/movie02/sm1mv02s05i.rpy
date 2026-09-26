label sm1mv02s05i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_arrogant_huh2 noloop
    sy "Forgetting something, [mcname]?"
    play voice2 mc_no_uhuh1 noloop
    mc "I don't think so."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    play voice3 stacy_laugh4 noloop
    sy "Hahaha."
    hide lst_sy_laugh01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_angry noloop
    sy "It's payday, [mcname]."
    play voice2 mc_happy_yay1 noloop
    mc "Great. My wallet was getting hungry."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_no_nah1 noloop
    sy "Not for you, silly."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh right. We need to put together some money for Kanya and everyone else before we film the scene."
    sy "Now you're getting it."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_thinking_oh1 noloop
    sy "Oh, and make sure you are well-rested for the first scene too."
    sy "You're going to have to work hard to please two lovely ladies."
    play voice2 mc_yes_aga2 noloop
    mc "No need to worry about that."
    $ StoryController.end_scene(MOVIE_SCIFI)
    return