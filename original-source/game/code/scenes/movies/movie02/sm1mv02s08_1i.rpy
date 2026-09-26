label sm1mv02s08_1i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_hey_attention1 noloop
    sy "Hey, [mcname]."
    play voice2 mc_hey_hey7 noloop
    mc "Morning, partner. Ready to film today?"
    sy "Oh yeah!"
    sy "I think it's going to be our biggest shoot yet."
    play voice2 mc_surprised_what1 noloop
    mc "Really?"
    play voice3 stacy_thinking_oh1 noloop
    sy "Oh yeah. Just think of it. We've got both a space fight and the-"
    play voice2 mc_shhh noloop
    mc "Sshhh. No spoilers."
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    play voice3 stacy_happy_laugh1 noloop
    sy "Haha. What is this a 'bad luck to see the bride before the wedding' thing?"
    hide lst_sy_laugh01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice2 mc_thinking_hmm1 noloop
    mc "I just don't want to jinx us."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_thinking_well1 noloop
    sy "Well, I think you can relax, [mcname]."
    sy "We planned this one out with extreme care."
    sy "Now we just have to deliver."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice2 mc_happy_yay1 noloop
    mc "Let's do it!"
    $ StoryController.end_scene(MOVIE_SCIFI)
    return