label sm1cs_arj001i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "sad1") as lst_sy_sad1
    play voice3 stacy_thinking_emm1 noloop
    sy "So... about that flash drive..."
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah?"
    hide lst_sy_sad1
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    play voice3 stacy_disappointed_ehh2 noloop
    sy "We need to get it back."
    play voice2 mc_angry_off noloop
    mc "Stacy-"
    hide lst_sy_ask1
    show expression cc.get_expression_image("sy", "annoyed1") as lst_sy_annoyed1
    play voice3 stacy_hey_angry1 noloop
    sy "There's a lot of sensitive information on that flash drive, [mcname]!"
    play voice2 mc_yes_yes1 noloop
    mc "I know-"
    hide lst_sy_annoyed1
    show expression cc.get_expression_image("sy", "angry1") as lst_sy_angry1
    sy "So we need to get it back!"
    play voice2 mc_disappointed_off1 noloop
    mc "I know..."
    play voice3 stacy_arrogant_hmm1 noloop
    hide lst_sy_angry1
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    sy "So?"
    mc "So?"
    play voice3 stacy_arrogant_ha2 noloop
    sy "So are you going to text AmRose?"
    play voice2 mc_angry_errr1 noloop
    mc "Ugggh... fine."
    hide lst_sy_ask1
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    mct "Not like I had anything planned today..."
    mc "..."
    play voice2 mc_yes_okay2 noloop
    mc "Okay, she texted me back. She said we could meet at Starducks."
    play voice3 stacy_yay noloop
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    sy "Yay!"
    sy "Thanks, [mcname]!"
    play voice2 mc_no_nah1 noloop
    mc "Not a problem."
    $ StoryController.end_scene(ARJ_STORY, 0, 15, 0)
    return