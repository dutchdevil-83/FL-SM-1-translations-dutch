label sm1mv02s02_01i:
    $ LocationController.draw_current_location("mes")
    show expression cc.get_expression_image("mes", "neutral01") as lst_mes_neutral
    play voice2 mc_hey_hey2 noloop
    mc "Hey, Min."
    play voice7 min_hey_greeting noloop
    mes "Hey there. What's new, [mcname]?"
    play voice2 mc_thinking_hm noloop
    mc "Nothing much."
    mc "I actually came to offer you a role in my new movie."
    hide lst_mes_neutral
    show expression cc.get_expression_image("mes", "smile01") as lst_mes_smile
    play voice7 min_thinking_emm noloop
    mes "Hmmm. You don't waste any time do you?"
    mes "I agree to be open to filming your super naughty films, and soon enough, you're banging on my door with a role."
    play voice2 mc_arrogant_heh2 noloop
    mc "I don't like to let a good thing pass me by."
    hide lst_mes_smile
    show expression cc.get_expression_image("mes", "laugh01") as lst_mes_laugh
    play voice7 min_arrogant_heh1 noloop
    mes "Smooth, mister."
    mes "Okay, I'm in."
    hide lst_mes_laugh
    show expression cc.get_expression_image("mes", "ask01") as lst_mes_ask
    mes "What kind of movie is it anyway? I probably should have asked before agreeing."
    play voice2 mc_thinking_oh1 noloop
    mc "It's a Sci-Fi movie. Kind of like Star Trek style."
    play voice7 min_surprised_huh1 noloop
    mes "Huh. Not the biggest fan, but I'll do it for you."
    play voice2 mc_happy_a1 noloop
    mc "Thanks. You're going to be playing Commander Vel Spectre, Science officer of the UPAS {i}Intrepid{/i}."
    hide lst_mes_ask
    show expression cc.get_expression_image("mes", "neutral01") as lst_mes_neutral
    play voice7 min_thinking_hmm1 noloop
    mes "Alright. But for your next movie, you should think of a cool murder mystery movie. Or something like 'Eyes Wide Shut'."
    play voice2 mc_happy_laugh2 noloop
    mc "Haha. Maybe next time."
    $ player.set_choice("sm1mv02s02_recruit_mes")
    $ player.set_choice("sm1mv02_char", "mes")
    $ gt.add(0, 30, 0)
    $ player.consume_energy(1)
    $ player.progress_storyline(MOVIE_SCIFI)
    return