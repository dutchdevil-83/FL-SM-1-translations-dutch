label sm1mv02s10i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_hey_hey3 noloop
    mc "Hey there."
    play voice3 stacy_hey noloop
    sy "What's new, boo?"
    play voice2 mc_thinking_oh1 noloop
    mc "Well, since all the editing and post-production were done for the movie, I figured we should do a watch party."
    mc "Get everyone together and see our theatrical slash naughty brilliance."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_happy_hmm1 noloop
    sy "That sounds great, [mcname]."
    sy "We can put it on the big screen and have a bunch of popcorn and snacks."
    play voice2 mc_happy_yes1 noloop
    mc "Perfect. I'll make the calls."
    $ StoryController.end_scene(MOVIE_SCIFI)
    return