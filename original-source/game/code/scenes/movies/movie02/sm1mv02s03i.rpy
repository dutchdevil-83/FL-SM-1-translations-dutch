label sm1mv02s03i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_yes_okay2 noloop
    mc "I recruited Nari for the movie."
    play voice3 stacy_happy_yay1 noloop
    sy "Great. Now we need to gather raw materials to build the sets."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    play voice3 stacy_happy_laugh4 noloop
    sy "I require more vespian gas, [mcname]."
    play voice2 mc_surprised_uh1 noloop
    mc "Huh?"
    hide lst_sy_laugh01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_thinking_hmm1 noloop
    sy "I said we need more money to build the set."
    sy "Check your phone for the specifics."
    sy "Once we have enough money in the bank, we can build us a starship."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_yes_aga2 noloop
    mc "Awesome. I'll get to work on that."
    $ StoryController.end_scene(MOVIE_SCIFI, 0, 30, 0)
    return