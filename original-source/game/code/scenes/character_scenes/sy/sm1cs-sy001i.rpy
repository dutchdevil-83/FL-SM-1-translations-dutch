label sm1cs_sy001i_rent_penalty:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice2 mc_thinking_mmm4 noloop
    mc "Hmmm."
    play voice3 stacy_arrogant_huh1 noloop
    sy "Where is the money Lebovsky???"
    play voice2 mc_hey_hey3 noloop
    mc "Hey-hey, easy there! What's the problem?"
    hide lst_sy_naughty1
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    play voice3 stacy_disappointed_oh4 noloop
    sy "We didn't have enough money to cover rent this week."
    sy "Every week we owe $[RENT_WEEKLY_AMOUNT]."
    play voice2 mc_disappointed_ah1 noloop
    mc "Ah, sorry about that. I'll be better next week, I promise."
    hide lst_sy_ask1
    show expression cc.get_expression_image("sy", "annoyed1") as lst_sy_annoyed1
    play voice3 stacy_arrogant_hmm2 noloop
    sy "You better! For now, I'll have to take matters into my own hands."
    play voice2 mc_disappointed_off2 noloop
    mc "Uh... meaning?"
    if player.get_data("penalty_warning") is False:
        hide lst_sy_annoyed1
        show expression cc.get_expression_image("sy", "angry1") as lst_sy_angry1
        play voice3 stacy_angry noloop
        sy "This time I will cover for you, next time there will be consequences."
        sy "Don't let it happen again!"
        $ player.set_data("rent_penalty", False)
        $ player.set_data("penalty_warning", True)
    else:
        sy "Since you can't focus on rent, that means I have to 'help' you focus on it."
        mct "I don't like the sound of that."
        hide lst_sy_annoyed1
        show expression cc.get_expression_image("sy", "smile2") as lst_sy_smile2
        play voice3 stacy_arrogant_ha1 noloop
        sy "That means no sex until you get your act together, buster."
        play voice2 mc_angry_errr2 noloop
        mc "Oh come on, that's just cruel."
        sy "Hey I'd be missing out too. So... you going to clean up your act?"
        mc "Yes."
    $ gt.add(1, 30, 0)
    return