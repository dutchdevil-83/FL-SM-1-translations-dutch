label sm1cs_mh006i:
    $ curr_position = LLY_DOOR
    $ LocationController.draw_current_location("mh")
    show expression cc.get_expression_image("mh", "neutral01") as lst_mh_neutral01
    play voice2 mc_hey_hey8 noloop
    mc "Hey, Lyssa."
    play voice3 lissa_hey noloop
    mh "Evening, [mcname]."
    mc "I was wondering if you would want to get dinner tonight?"
    hide lst_mh_neutral01
    show expression cc.get_expression_image("mh", "smile01") as lst_mh_smile01
    play voice3 lissa_oh2 noloop
    mh "Oh, another date?"
    play voice2 mc_yes_yeah4 noloop
    mc "That was the hope."
    hide lst_mh_smile01
    show expression cc.get_expression_image("mh", "neutral02") as lst_mh_neutral02
    play voice3 lissa_aga noloop
    mh "Well, let me go put something nicer on."
    play voice2 mc_yes_yes8 noloop
    mc "Is that a yes?"
    hide lst_mh_neutral02
    show expression cc.get_expression_image("mh", "smile02") as lst_mh_smile02
    play voice3 lissa_laugh noloop
    mh "Take a wild guess."
    $ curr_position = LLY_OUTSIDE
    $ StoryController.end_scene(MH_STORY)
    return