label sm1mv02s02i:
    $ LocationController.draw_current_location("ns")
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral1
    play voice2 mc_happy_yay2 noloop
    mc "Hey, Nari."
    play voice3 nari_hey_calm noloop
    ns "Hello, [mcname]."
    mc "I want to talk to you about something. Do you have a minute?"
    hide lit_ns_neutral1
    show expression cc.get_expression_image("ns", "excited01") as lit_ns_excited01
    play voice3 nari_thinking_oh noloop
    ns "For you? Of course."
    play voice2 mc_yes_yeah2 noloop
    mc "Great."
    if curr_position == SD_NARI:
        mc "Let's go to the living room."
    elif curr_position != SD_COUCH:
        mc "Let's go have a seat at the couch."
    else:
        mc "Let's have a seat."
    $ StoryController.end_scene(MOVIE_SCIFI)
    return