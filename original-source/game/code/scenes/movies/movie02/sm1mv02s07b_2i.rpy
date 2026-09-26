label sm1mv02s07b_2i:
    $ LocationController.draw_current_location("mh")
    show expression cc.get_expression_image("mh", "neutral01") as lst_mh_neutral01
    play voice2 mc_happy_yay2 noloop
    mc "My lovely lady Lyssa What would you say to a little spa day?"
    mc "I'll pay for you, myself, and a friend of mine who’s been really looking forward to getting to know you better."
    hide lst_mh_neutral01
    show expression cc.get_expression_image("mh", "smile02") as lst_mh_smile02
    play voice8 lissa_haha noloop
    mh "You cornball! I hope you know no one else would get away with calling me \"my lady\"."
    mh "Yeah, a spa day sounds good. Do I know this mysterious friend of yours?"
    hide lst_mh_smile02
    show expression cc.get_expression_image("mh", "smile01") as lst_mh_smile01
    play voice2 mc_no_no1 noloop
    mc "No, you do not! But she's actually one of your costars in the movie."
    play voice8 dahlia_yes_yeah2 noloop
    mh "Alright, sure. I look forward to meeting this friend of yours!"
    $ StoryController.end_scene(MOVIE_SCIFI)
    return