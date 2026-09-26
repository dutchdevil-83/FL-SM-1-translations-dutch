label sm1mv01s05i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 d2s9_mchey noloop
    mc "Hey Stacy. All set to film the 'Recruitment' scene?"
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_yes_yap3 noloop
    sy "Yup. I'm super excited."
    sy "The set looks so good."
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "yawn01") as lst_sy_yawn01
    play voice3 stacy_disappointed_ehh1 noloop
    sy "*sighs* Feels like it took months to get to this point."
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Haha. Well, now we're finally ready."
    hide lst_sy_yawn01
    show expression cc.get_expression_image("sy", "neutral01")
    play voice2 mc_thinking_hmm2 noloop
    mc "I'll call Kanya and Taisia and let them know the show is on."
    $ StoryController.end_scene(MOVIE_PIRATES)
    return