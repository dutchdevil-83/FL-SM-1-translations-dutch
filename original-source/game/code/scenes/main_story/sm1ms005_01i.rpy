label sm1ms005_01i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "sad1") as lst_sy_sad1
    play voice3 stacy_disappointed_oh1 noloop
    sy "[mcname], we need to have a talk."
    play voice2 d2s12_emmm noloop
    mc "Uhm, okay? What's going on?"
    sy "I want a movie night."
    mc "Wait... That's it?"
    hide lst_sy_sad1
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    play voice3 stacy_yes_yap1 noloop
    sy "Yep. Me, you, movie."
    play voice2 mc_disappointed_ah2 noloop
    mc "Oh... I thought there was an emergency or something. Yeah, we can do a movie night."
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_happy_yay3 noloop
    sy "Yay! I'll start making popcorn."
    mc "Great thinking, Stacy."
    $ StoryController.end_scene(MS)
    return