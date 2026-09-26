label sm1cs_dc006i:
    $ LocationController.draw_current_location("dc")
    show expression cc.get_expression_image("dc", "serious01") as lpa_dc_serious
    play voice2 mc_hey_hey8 noloop
    mc "Good evening, Officer Callahan!"
    play voice3 girl36_yes_aga noloop
    dc "Good evening, cit-"
    hide lpa_dc_serious
    show expression cc.get_expression_image("dc", "embarrassed01") as lpa_dc_embarrassed01
    play voice3 girl36_surprised_oh noloop
    dc "Oh, erm, hi [mcname]."
    play voice2 mc_thinking_hmm8 noloop
    mc "I believe someone said something about getting a coffee?"
    dc "Well... when I'm not on duty."
    dc "But, my break is coming up..."
    hide lpa_dc_embarrassed01
    show expression cc.get_expression_image("dc", "sad01") as lpa_dc_sad01
    play voice3 girl36_yes_yeah noloop
    dc "Uhm... sure. We can do coffee."
    mct "Uh oh... she doesn't look too happy about it. I hope everything's okay."
    $ StoryController.end_scene(DC_STORY)
    return
label sm1cs_dc006_onramp:
    $ LocationController.draw_current_location("dc")
    show expression cc.get_expression_image("dc", "serious01") as lpa_dc_serious
    play voice2 mc_hey_hey8 noloop
    mc "Hey, Debbie!"
    play voice3 girl36_thinking_oh noloop
    dc "Oh! [mcname]."
    play voice2 mc_yes_yes2 noloop
    mc "Yes, I'm sorry of how I left things last time."
    mc "I was a bit shocked and needed time to process that information."
    hide lpa_dc_serious
    show expression cc.get_expression_image("dc", "neutral01") as lpa_dc_neutral01
    play voice3 girl36_no_nonono noloop
    dc "You don't need to apologize, [mcname]."
    play voice2 mc_no_no8 noloop
    mc "No-no, I should."
    mc "I was rude and I shouldn't have been."
    mc "So, can I ask you out?"
    hide lpa_dc_neutral01
    show expression cc.get_expression_image("dc", "curious01") as lpa_dc_curious01
    play voice3 girl36_arrogant_huh1 noloop
    dc "Ask me out?{w} Are you sure?"
    play voice2 mc_yes_yes1 noloop
    mc "Yes, I am."
    dc "Well okay."
    hide lpa_dc_curious01
    show expression cc.get_expression_image("dc", "smile01") as lpa_dc_smile01
    play voice3 girl36_thinking_hmm noloop
    dc "How about I text you when I have time for a coffee?"
    play voice2 mc_yes_sure1 noloop
    mc "Sure, that would be great."
    $ player.set_choice("sm1cs_dc006_offramp", False)
    return