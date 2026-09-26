label sm1fs_t007i:
    $ LocationController.draw_current_location("dvh")
    show expression cc.get_expression_image("dvh", "serious01") as lth_dvh_serious01
    play voice2 mc_happy_yay2 noloop
    mc "Hey, Denise."
    hide lth_dvh_serious01
    show expression cc.get_expression_image("dvh", "smile01") as lth_dvh_smile01
    play voice3 girl34_disappointed_ehh2 noloop
    dvh "Ah, the stray has returned to my office."
    hide lth_dvh_smile01
    show expression cc.get_expression_image("dvh", "serious01") as lth_dvh_serious01
    dvh "I expected you sooner."
    play voice2 mc_surprised_oh1 noloop
    mc "Oh?"
    play voice3 girl34_yes_yeah8 noloop
    dvh "Ya. I have been in contact with your associate, one Mr. Nelson Rohr."
    hide lth_dvh_serious01
    show expression cc.get_expression_image("dvh", "curious01") as lth_dvh_curious01
    dvh "He is the sponsor you mentioned earlier?"
    play voice2 mc_yes_yeah1 noloop
    mc "That is correct. And I got here as soon as I could."
    play voice3 girl34_thinking_hmm6 noloop
    dvh "Of course. I had assumed that you were just telling me what I wished to hear at the moment."
    hide lth_dvh_curious01
    show expression cc.get_expression_image("dvh", "laugh01") as lth_dvh_laugh01
    play voice3 girl34_happy_laugh1 noloop
    dvh "But it turns out I was wrong. And during my conversations so far with Mr. Rohr..."
    dvh "It looks like you have done very well by your fellow actors."
    play voice2 mc_happy_a1 noloop
    mc "I do what I can."
    hide lth_dvh_laugh01
    show expression cc.get_expression_image("dvh", "smile01") as lth_dvh_smile01
    play voice3 girl34_thinking_hmm1 noloop
    dvh "We shall talk more soon, [mcname]. If I can iron out the details with Mr. Rohr, we will have more resources than we would have had with Pizza World alone."
    dvh "And perhaps we can turn a simple show into something spectacular."
    play voice2 d1s5_mchappy noloop
    mc "Maybe even an extravaganza."
    hide lth_dvh_smile01
    show expression cc.get_expression_image("dvh", "serious01") as lth_dvh_serious01
    play voice3 girl34_no_nah1 noloop
    dvh "I did not say such. It is best to stay realistic, [mcname]."
    play voice2 mc_arrogant_heh2 noloop
    mc "Gotcha, Dense."
    dvh "Run along now. I need to handle some other work."
    play voice2 mc_yes_okay2 noloop
    mc "Okay."
    $ StoryController.end_scene(THEATER_STORY_LINE, 0, 30, 1)
    return