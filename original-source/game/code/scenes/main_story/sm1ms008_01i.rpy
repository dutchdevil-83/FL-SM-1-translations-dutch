label sm1ms008_01i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    play voice3 stacy_hey_happy2 noloop
    sy "Good news, [mcname]. The red wig came in today."
    play voice2 mc_thinking_oh1 noloop
    mc "Already? That's awesome."
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_yes_yap1 noloop
    sy "Yup, we're one step closer to making our first scene."
    play voice2 mc_yes_ugu1 noloop
    mc "Mmhmm. I'll have to figure out a time to go talk to Kanya about the scene."
    hide lst_sy_excited1
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    play voice3 stacy_happy_yay1 noloop
    sy "Yay. {w}Oh! We should both go. I still haven't met Kanya yet."
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    play voice3 stacy_thinking_emm2 noloop
    sy "Wait, does watching her have sex with you count as meeting her?"
    hide lst_sy_ask1
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    play voice2 mc_no_nah2 noloop
    mc "I don't think so."
    play voice3 stacy_happy_laugh3 noloop
    sy "*giggles* I wonder what she would think if she found out I watched you two banging."
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice2 mc_happy_hah1 noloop
    mc "Haha. Maybe you can bring up the subject one day. But we should keep this first meeting professional."
    play voice3 stacy_yes_ugu1 noloop
    sy "That's me! Miss Professional."
    mc "Haha."
    $ StoryController.end_scene(MS)
    return