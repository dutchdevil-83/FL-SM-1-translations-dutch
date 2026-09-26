label sm1cs_sy003i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
    play voice2 mc_hey_hey3 noloop
    mc "Hey gorgeous."
    play voice3 stacy_hey_happy2 noloop
    sy "Hey you. Why don't you come to bed?"
    sy "*soft moan* I've been thinking about you all day."
    mc "Mmmm."
    hide lst_sy_naughty01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    menu:
        "Have sex with Stacy on your bed":
            jump sm1cs_sy003_repeatable
        "Just sleep":
            jump sm1cs_sy003i_sleep
label sm1cs_sy003i_sleep:
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "You know it's been such a long day, I should probably just get some sleep."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    play voice3 stacy_happy_laugh2 noloop
    sy "Haha. Always being Mr. Responsible."
    hide lst_sy_laugh01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_yes_yeah2 noloop
    sy "Alright, I won't push you to take me to pound town."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
    play voice3 stacy_thinking_hmm4 noloop
    sy "But don't forget that girls can be just as horny as guys, [mcname]."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh I won't be forgetting that any time soon."
    hide lst_sy_naughty01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_thinking_hmm1 noloop
    sy "Goodnight."
    $ StoryController.end_scene_without_storyline(None, 0, 30)
    return