init 3 python:
    CharacterController.get_character("sr").interactions = [
            {LABEL: "q_inter_sr_1", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_sr_2", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_sr_3", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_sr_4", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_sr_5", LOCATIONS: [IT_OFFICE]},
            ]
    CharacterController.get_character("sr").default_expression = "neutral01"

label q_inter_sr_1:
    show expression cc.get_expression_image("sr", "neutral01")
    play voice3 girl35_arrogant_he4 noloop
    sr "[mcname], you're not downloading music on your computer, are you?"
    play voice2 mc_no_no10 noloop
    mc "No? What?"
    sr "Okay. Then it's just April spoofing your IP. I'll handle it."
    return
label q_inter_sr_2:
    show expression cc.get_expression_image("sr", "neutral01")
    play voice3 girl35_arrogant_ha9 noloop
    sr "How secure is your password, [mcname]?"
    play voice2 d2s12_emmm noloop
    mc "Uhm... It's not 'password' if that helps?"
    sr "..."
    sr "Talk to April. She's great at making passwords that you can't crack."
    return
label q_inter_sr_3:
    show expression cc.get_expression_image("sr", "neutral01")
    play voice2 d2s9_mchey noloop
    mc "Hey, Sienna."
    play voice3 girl35_arrogant_hm1 noloop
    sr "[mcname]."
    mc "Anything new?"
    sr "Yeah. April downloaded something suspicious, and Anna left a gaping hole in our security. You haven't screwed up lately, have you?"
    mc "Uhm..."
    sr "Now I need to check all of {i}your work{/i} too."
    return
label q_inter_sr_4:
    show expression cc.get_expression_image("sr", "sad01")
    play voice3 girl35_arrogant_pff4 noloop
    sr "Aye yea yea..."
    play voice2 mc_surprised_uh1 noloop
    mc "What's wrong, Sienna?"
    sr "We've been getting bombarded with a DDoS all morning. Thank God we had April test the system when we implimented it."
    return
label q_inter_sr_5:
    show expression cc.get_expression_image("sr", "smile01")
    play voice3 girl35_disappointed_oh2 noloop
    sr "Oh, [mcname], are you a book reader?"
    play voice2 mc_yes_yeah4 noloop
    mc "When I have the time, sometimes. Yeah."
    sr "If you get a chance, you should check out A Castle of Thistles and Orchids. Real good."
    return