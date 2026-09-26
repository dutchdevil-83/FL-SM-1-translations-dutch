label sm1mv02s08i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_hey_hey3 noloop
    mc "Hey, Stacy."
    play voice3 stacy_hey_attention1 noloop
    sy "Hey, handsome."
    play voice2 mc_thinking_hmm1 noloop
    mc "So are we all set for the big scenes?"
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    mc "I'm eager to put this one to rest."
    play voice3 stacy_thinking_well1 noloop
    sy "Well, I would say we are halfway there."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_surprised_why1 noloop
    mc "Only halfway? What's the hold up?"
    play voice3 stacy_thinking_oh2 noloop
    sy "These last two scenes require a lot of CGI graphics to fill in the gaps, [mcname]."
    sy "So that means we need a lot of cheddar."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    play voice2 mc_surprised_huh1 noloop
    mc "What does cheese have to do with CGI?"
    play voice3 stacy_happy_laugh1 noloop
    sy "Hahaha."
    sy "Cash, man. Cash!"
    hide lst_sy_laugh01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    sy "These last two scenes are the real deal, and the movie bank is tapped out, so we need a cash infusion."
    play voice2 mc_yes_okay1 noloop
    mc "Alright. I'll see what I can do."
    $ StoryController.end_scene(MOVIE_SCIFI)
    return