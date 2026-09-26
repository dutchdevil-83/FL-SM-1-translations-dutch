label sm1mv01s06i:
    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "neutral01") as lst_sy_neutral01
    play voice2 mc_happy_yay2 noloop
    mc "Hi Taisia."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("tl", "excited01") as lst_sy_excited01
    play voice3 girl24_hey_greeting noloop
    tl "Hey handsome."
    play voice2 mc_thinking_emm1 noloop
    mc "Ready to film the second scene?"
    hide lst_sy_excited01
    show expression cc.get_expression_image("tl", "smile01") as lst_sy_smile01
    play voice3 girl24_happy_yeah2 noloop
    tl "I was born ready!"
    play voice2 mc_arrogant_heh3 noloop
    mc "Haha. Time to film some porn!"
    $ StoryController.end_scene(MOVIE_PIRATES)
    return