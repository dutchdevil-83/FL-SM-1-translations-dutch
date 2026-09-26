init 3 python:
    CharacterController.get_character("rd").interactions = [
            {LABEL: "q_inter_rd_1"},
            {LABEL: "q_inter_rd_2"},
            {LABEL: "q_inter_rd_3"},
            {LABEL: "q_inter_rd_4", DAYS: [WEEKENDS, FRIDAY]},
            {LABEL: "q_inter_rd_5", DAYS: [WEEKENDS, FRIDAY]},
            {LABEL: "q_inter_rd_6", DAYS: [WEEKENDS, FRIDAY]},


            ]
    CharacterController.get_character("rd").default_expression = "neutral01"

label q_inter_rd_1:
    show expression cc.get_expression_image("rd", "neutral01")
    play voice3 girl26_thinking_hmm1 noloop
    rd "What can I get you?"
    play voice2 mc_thinking_hm noloop
    mc "Just a beer."
    return
label q_inter_rd_2:
    show expression cc.get_expression_image("rd", "neutral01")
    play voice2 d2s12_emmm noloop
    mc "I must be crazy, I think I saw blood in the bathroom."
    play voice3 girl26_happy_laugh1 noloop
    rd "Haha. Must have been seeing stuff."
    rd "No bloodsports around my bar."
    mc "Okay."
    return
label q_inter_rd_3:
    show expression cc.get_expression_image("rd", "smile01")
    play voice2 mc_happy_yay2 noloop
    mc "Hi, Ridley."
    play voice3 girl26_hey_greeting noloop
    rd "Sup, [mcname]."
    return
label q_inter_rd_4:
    show expression cc.get_expression_image("rd", "smile01")
    play voice2 mc_disgust_pfe1 noloop
    mc "Phe. Thanks god it's the weekend."
    play voice3 girl26_yes_aga noloop
    rd "I am right there with you, [mcname]."
    return
label q_inter_rd_5:
    show expression cc.get_expression_image("rd", "neutral01")
    play voice3 girl26_thinking_hmm2 noloop
    rd "It's days like today I wish I worked corporate."
    rd "Just a little extra busy."
    return
label q_inter_rd_6:
    show expression cc.get_expression_image("rd", "smile01")
    play voice3 girl26_hey_confused noloop
    rd "Hey [mcname]."
    play voice2 d9s2_ugu noloop
    mc "Ridley."
    return