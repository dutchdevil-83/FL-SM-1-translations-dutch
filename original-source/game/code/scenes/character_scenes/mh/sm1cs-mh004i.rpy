label sm1cs_mh004i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_surprised_huh4 noloop
    sy "Excited for your date with Lyssa?"
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah! Maybe also a little nervous."
    hide lst_sy_excited1
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    play voice3 stacy_thinking_emm2 noloop
    sy "When is it?"
    play voice2 mc_arrogant_nah1 noloop
    mc "We haven't really picked a day yet..."
    sy "... "
    hide lst_sy_ask1
    show expression cc.get_expression_image("sy", "annoyed1") as lst_sy_annoyed1
    play voice3 stacy_angry_argh4 noloop
    sy "So you just going to stand there, or are you going to text her?"
    play voice2 mc_yes_okay2 noloop
    mc "Okay, okay, I'm texting her right now!"
    play sound sfx_message_in1
    mc "..."
    mc "She said she's free any night for a date so I should just drop by!"
    hide lst_sy_annoyed1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_happy_yay1 noloop
    sy "Well get dressed, and go get her!"
    play voice2 mc_yes_yes2 noloop
    mc "I'll get there when I have time, I promise!"
    hide lst_sy_excited1
    show expression cc.get_expression_image("sy", "angry1") as lst_sy_angry1
    play voice3 stacy_angry noloop
    sy "You better! Lyssa is an absolute catch, [mcname]. Don't fumble her. Got it?"
    play voice2 mc_yes_ugu1 noloop
    mc "I got it, I got it."
    $ StoryController.end_scene(MH_STORY, 0, 15, 0)
    return