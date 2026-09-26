label sm1mv01s04_2i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice2 mc_thinking_hmm3 noloop
    mc "Alright Stacy. I'm all set to work on the sets."
    play voice3 stacy_no_angry1 noloop
    sy "Not so fast!"
    mc "Huh?"
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "serious01") as lst_sy_serious01
    play voice3 stacy_thinking_hmm1 noloop
    sy "You might {b}think{/b} you're ready, but you might be blinded by your arrogance."
    hide lst_sy_serious01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_disappointed_oh7 noloop
    sy "The next part of the movie is important, but it is also going to be a lot of work."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_thinking_emm1 noloop
    sy "We are going to need $250 in petty cash for the next step."
    sy "And you're also going to need 20 energy, or you might die on the next part of the project."
    play voice2 d1s5b_ehhh noloop
    mc "You're certainly in a dramatic mood."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "sad01") as lst_sy_sad01
    play voice3 stacy_yes_yap1 noloop
    sy "Filmmaking is serious business.{w} Plus, I'd hate to see you die on me, [mcname]."
    sy "Then I'd be all alone."
    play voice2 d3s11b_mcheh noloop volume 1.5
    mc "Haha."
    hide lst_sy_sad01
    show expression cc.get_expression_image("sy", "smile02") as lst_sy_smile02
    play voice2 mc_yes_okay2 noloop
    mc "Alright. So we need to have $250 in the bank, and I need to have 20 energy for the next part of the film."
    hide lst_sy_smile02
    show expression cc.get_expression_image("sy", "excited01")
    play voice3 stacy_yes_simple1 noloop
    sy "Bingo. Now get to it."
    $ StoryController.end_scene(MOVIE_PIRATES)
    return