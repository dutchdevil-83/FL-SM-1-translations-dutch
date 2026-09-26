label sm1cs_mh010i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_hey_happy1 noloop
    sy "What's up, [mcname]?"
    play voice2 mc_thinking_emm1 noloop
    mc "Can I borrow your laptop?"
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
    play voice3 stacy_arrogant_huh2 noloop
    sy "You're not going to look at porn with it, are you?"
    play voice2 mc_no_no1 noloop
    mc "No, I need to do some editing."
    hide lst_sy_naughty01
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_thinking_oh1 noloop
    sy "What are you editing?"
    play voice2 mc_thinking_mmm2 noloop
    mc "When Lyssa was over the other day, we did a little shoot-"
    play voice3 stacy_surprised_ohmy1 noloop
    sy "You did a shoot with Lyssa!?!"
    play voice2 mc_yes_aga2 noloop
    mc "Uhm, yes-"
    sy "Can I see!?!"
    mc "No, I promised her I wouldn't show it to anyone."
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "annoyed01") as lst_sy_annoyed01
    play voice3 stacy_disappointed_ehh2 noloop
    sy "Boooooooo."
    play voice2 mc_surprised_uh1 noloop
    mc "So... can I borrow your laptop?"
    play voice3 stacy_yes_fine1 noloop
    sy "Fiiiiiiiiiiiine."
    play voice2 mc_happy_a1 noloop
    mc "Thanks!"
    hide lst_sy_annoyed01
    scene black
    show screen scene_transistion(_("20 Minutes Later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_hey_hey4 noloop
    mc "Here's your laptop back!"
    play voice3 stacy_disappointed_oh3 noloop
    sy "Still not going to show me?"
    if player.get_choice("sm1cs_mh008_convince_mh"):
        play voice2 mc_yes_sure1 noloop
        mc "I'll ask Lyssa what she's comfortable with, okay?"
        hide lst_sy_neutral01
        show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
        play voice3 stacy_happy_yay1 noloop
        sy "I'll take it!"
    else:
        play voice2 mc_no_nope1 noloop
        mc "Nope!"
    mc "Thanks for letting me borrow your laptop!"
    play voice3 stacy_yes_yeah2 noloop
    sy "Of course."
    $ StoryController.end_scene(MH_STORY, 1, 30, 3)
    return