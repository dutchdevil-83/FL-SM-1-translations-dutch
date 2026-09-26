label sm1mv01s03_1i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_hey_hey7 noloop
    mc "Hey Stacy."
    play voice3 stacy_hey_happy1 noloop
    sy "Hey you."
    mc "If you're free, we should finish up the script."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_yes_yeah1 noloop
    sy "Totally free.{w} Look at you, keeping us on schedule."
    if persistent.is_special:
        sy "My big bro.{w} Large and in charge."
        play voice2 mc_arrogant_heh3 noloop
        mc "Haha."
    else:
        sy "I love a take-charge man."
        play voice2 mc_arrogant_heh3 noloop
        mc "Let's get to it."
    jump sm1mv01s03_1