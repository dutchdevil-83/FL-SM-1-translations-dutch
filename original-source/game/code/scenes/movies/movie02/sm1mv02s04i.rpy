label sm1mv02s04i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_happy_yay2 noloop
    mc "Hey Stacy."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lpd_sy_smile01
    play voice3 stacy_hey_happy2 noloop
    sy "Hello handsome."
    play voice2 mc_thinking_hmm5 noloop
    mc "Such a charmer.{w} I was thinking that today would be a good fit for the table read of the movie."
    hide lpd_sy_smile01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_yes_yap3 noloop
    sy "Works for me."
    play voice2 mc_thinking_mmm4 noloop
    mc "Want to come help me with the logistics?"
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lpd_sy_smile01
    play voice3 stacy_yes_yeah2 noloop
    sy "Sure!"
    $ StoryController.end_scene(MOVIE_SCIFI)
    return