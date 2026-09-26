label sm1mv02s02_02i:
    $ LocationController.draw_current_location("mh")
    show expression cc.get_expression_image("mh", "neutral01") as lst_mh_neutral01
    play voice8 lissa_hey noloop
    mh "[mcname], a pleasant surprise. What can I do for you?"
    play voice2 mc_hey_hey2 noloop
    mc "Hey, Lyssa! I actually wanted to ask you something."
    hide lst_mh_neutral01
    show expression cc.get_expression_image("mh", "smile01") as lst_mh_smile01
    play voice8 dahlia_surprised_oh noloop
    mh "Oh? What have you got on your mind, [mcname]?"
    play voice2 mc_thinking_hmm4 noloop
    mc "So, we're starting casting for our new movie, and..."
    hide lst_mh_smile01
    show expression cc.get_expression_image("mh", "neutral02") as lst_mh_neutral02
    play voice8 dahlia_thinking_hmm1 noloop
    mh "What kind of a movie?"
    play voice2 mc_thinking_oh1 noloop
    mc "We're doing a Sci-Fi, space explorer's thing. You know, more Trek than Wars."
    play voice8 dahlia_yes_questioning noloop
    mh "Okay, and who would I be in the movie?"
    play voice2 mc_happy_a1 noloop
    mc "I'm thinking a sexy alien science officer type."
    mc "Which means you'd have some special effects makeup on so people wouldn't be able to recognize you."
    hide lst_mh_neutral02
    show expression cc.get_expression_image("mh", "smile02") as lst_mh_smile02
    play voice8 lissa_oh2 noloop
    mh "Is that so?"
    play voice2 mc_yes_yeah1 noloop
    mc "Yep! And you'd be smart, and get to say smart things, and..."
    mc "Uhm... have sex with me? And maybe some other people?"
    hide lst_mh_smile02
    show expression cc.get_expression_image("mh", "smile01") as lst_mh_smile01
    play voice8 lissa_laugh noloop
    mh "Hehehehehehe."
    mh "I'd be interested, [mcname]. I've also wanted to see what it's like on one of your sets that isn't just your living room."
    play voice2 mc_surprised_huh2 noloop
    mc "Wait, is that a yes?"
    hide lst_mh_smile01
    show expression cc.get_expression_image("mh", "smile02") as lst_mh_smile02
    play voice8 dahlia_yes_yeah3 noloop
    mh "Hehehehe - yes, [mcname]. That's a yes."
    play voice2 mc_happy_yay1 noloop
    mc "Awesome!"
    mc "I'll get you the details ASAP!"
    play voice8 dahlia_happy_hmm1 noloop
    mh "Looking forward to it"
    $ player.set_choice("sm1mv02s02_recruit_mh")
    $ player.set_choice("sm1mv02_char", "mh")
    $ player.consume_energy(1)
    $ gt.add(0, 30, 0)
    $ player.progress_storyline(MOVIE_SCIFI)
    return