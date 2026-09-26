label sm1ms013i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice3 stacy_hey_attention1 noloop
    sy "Heyyyyyyy, [mcname]."
    play voice2 mc_yes_yes8 noloop
    mc "Yes, Stacy?"
    sy "You know what I've been thinking about?"
    mc "What?"
    hide lst_sy_naughty1
    show expression cc.get_expression_image("sy", "smile2") as lst_sy_smile2
    play voice3 stacy_suckmoan3 noloop
    sy "How hot it was when you were fucking me as a redhead."
    play voice2 mc_thinking_mmm1 noloop
    mc "It was pretty hot."
    sy "You wanna' do it again?"
    mc "Does the Pope shit in the woods?"
    hide lst_sy_smile2
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    sy "..."
    play voice3 stacy_surprised_huh1 noloop
    sy "What?"
    play voice2 mc_yes_yes1 noloop
    mc "Yes. Yes I do want to fuck you with the wig."
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_happy_yay3 noloop
    sy "Yay! Let me go get it!"
    $ StoryController.end_scene(MS)
    return