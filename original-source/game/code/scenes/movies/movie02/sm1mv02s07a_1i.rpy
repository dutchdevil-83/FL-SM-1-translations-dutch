label sm1mv02s07a_1i:
    $ LocationController.draw_current_location("mes")
    show expression cc.get_expression_image("mes", "neutral01") as lit_mes_neutral01
    play voice7 min_hey_greeting noloop
    mes "Hey, [mcname]. Can I ask you something?"
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    play voice7 min_surprised_huh1 noloop
    mes "What is Nari's deal?"
    play voice2 mc_surprised_huh1 noloop
    mc "Uh. Her deal?"
    mes "Yeah. I tried to talk to her a bit after filming, but she was a bit shy."
    mes "I didn't think she'd be so shy, since she's working on a porno."
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah. That's just how she is. But she'll open up eventually."
    hide lit_mes_neutral01
    show expression cc.get_expression_image("mes", "smile01") as lit_mes_smile01
    play voice7 min_thinking_hmm1 noloop
    mes "Maybe we should try giving her a nudge."
    mes "After all, we're filming a scene together soon, I don't want her to be uncomfortable."
    hide lit_mes_smile01
    show expression cc.get_expression_image("mes", "curious01") as lit_mes_curious01
    mes "How about a spa trip? We can get some massages and facials."
    mes "And then maybe the three of us can just chill and talk."
    play voice2 mc_yes_okay3 noloop
    mc "Should work. I'll let Nari know."
    hide lit_mes_curious01
    show expression cc.get_expression_image("mes", "excited01") as lit_mes_excited01
    play voice7 min_yes_happy noloop
    mes "Good."
    $ StoryController.end_scene(MOVIE_SCIFI, 0, 15, 0)
    return