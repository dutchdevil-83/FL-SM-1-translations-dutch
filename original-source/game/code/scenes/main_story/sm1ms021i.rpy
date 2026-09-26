label sm1ms021i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice2 mc_hey_hey7 noloop
    mc "Hey Stacy."
    play voice3 stacy_hey noloop
    if persistent.is_special:
        sy "Hey bro. What's up?"
    else:
        sy "Hey [mcname]. What's up?"
    play voice2 mc_thinking_hmm6 noloop
    mc "I'm ready to start pre-production on the next film."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "serious01") as lst_sy_serious01
    play voice3 stacy_arrogant_huh2 noloop
    sy "Yeah? Sure you want to spend that money now."
    play voice2 mc_yes_yeah1 noloop
    mc "Oh yeah. It's burning a hole in my pocket."
    mc "Plus, I want to get back in gear."
    mc "Can't make our fans wait too long."
    hide lst_sy_serious01
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_yes_fine2 noloop
    sy "Heck yes."
    sy "Alright, I'll let the client know that we're starting production."
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_thinking_emm2 noloop
    sy "You should text Kanya and let her know we'll be starting something new."
    sy "Tell her we'd love to have her expertise again."
    play voice2 d9s2_yeah noloop volume 1.6
    mc "Good idea."
    hide lst_sy_neutral01
    $ StoryController.end_scene(MS)