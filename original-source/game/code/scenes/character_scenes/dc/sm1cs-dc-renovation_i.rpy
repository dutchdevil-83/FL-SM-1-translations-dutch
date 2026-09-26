label sm1cs_dc_renovation_i:
    $ LocationController.draw_current_location("dc")
    show expression cc.get_expression_image("dc", "ask01") as lpa_dc_ask01
    play voice2 mc_hey_hey10 noloop
    mc "Officer Callahan!"
    play voice3 girl36_arrogant_hm noloop
    dc "So formal, [mcname]! Are you in trouble?"
    play voice2 mc_no_nope1 noloop
    mc "Nope. I just like using your title."
    hide lpa_dc_ask01
    show expression cc.get_expression_image("dc", "embarrassed01") as lpa_dc_embarrassed01
    play voice3 girl36_thinking_eem noloop
    dc "How are you doing?"
    play voice2 mc_thinking_mmm4 noloop
    mc "I'm fine. Just super busy with renovating my studio."
    play voice3 girl36_thinking_oh noloop
    dc "Oh? How's that going?"
    play voice2 mc_thinking_hmm5 noloop
    mc "Slowly."
    hide lpa_dc_embarrassed01
    show expression cc.get_expression_image("dc", "curious01") as lpa_dc_curious01
    play voice3 girl36_surprised_huh1 noloop
    dc "Would you... maybe want some extra help?"
    dc "Because my offer to come help out with the renovation still stands."
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, seriously?"
    hide lpa_dc_curious01
    show expression cc.get_expression_image("dc", "excited01") as lpa_dc_excited01
    play voice3 girl36_yes_yeah noloop
    dc "Yeah. I'm off the rest of the day and I don't have anything else to do. Besides, it sounds fun."
    play voice2 mc_happy_yay2 noloop
    mc "That would be awesome, Debbie!"
    play voice3 girl36_thinking_hmm noloop
    dc "Well let me head home and change and I can meet you there?"
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Sounds great! Here's the address!"
    play voice3 girl36_yes_aga noloop
    hide lpa_dc_excited01
    jump sm1cs_dc_renovation