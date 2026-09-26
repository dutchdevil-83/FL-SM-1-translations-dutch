init 3 python:
    CharacterController.get_character("en").interactions = [
            {LABEL: "q_inter_en_1", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_en_2", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_en_3", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_en_4", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_en_5", LOCATIONS: [IT_OFFICE]},
            ]
    CharacterController.get_character("en").default_expression = "neutral01"

label q_inter_en_1:
    show expression cc.get_expression_image("en", "angry01")
    play voice2 d2s9_mchey noloop
    mc "Hey, Eugene-"
    play voice3 boy5_angry_hmm1 noloop
    en "Email."
    mc "I just wanted to talk to you-"
    en "Put it in email."
    mc "Okay..."
    return
label q_inter_en_2:
    show expression cc.get_expression_image("en", "angry01")
    play voice2 d1s5_mchappy noloop volume 1.4
    mc "Eugene, can I talk-"
    play voice3 boy5_no_simple3 noloop
    en "No."
    mc "It will only-"
    en "I am busy. Put it in email."
    return
label q_inter_en_3:
    show expression cc.get_expression_image("en", "neutral01")
    play voice2 d1s2_hmm noloop volume 1.4
    mc "Have you seen-"
    play voice3 boy5_disappointed_geh2 noloop
    en "Can this be email?"
    mc "Uhm, maybe?"
    en "Then put in email."
    return
label q_inter_en_4:
    show expression cc.get_expression_image("en", "angry01")
    play voice2 mc_surprised_oh1 noloop
    mc "Eugene, I was wondering-"
    play voice3 boy5_angry_argh1 noloop
    en "Ile razy mam ci powtarzać, żebyś korzystał ze swojego e-maila?"
    mc "Okay, okay. I get it. I'll email you."
    return
label q_inter_en_5:
    show expression cc.get_expression_image("en", "smile01")
    play voice2 mc_surprised_how2 noloop
    mc "How'd your morning going, Eugene?"
    play voice3 boy5_thinking_oh2 noloop
    en "I have many emails to answer."
    mc "That's... Good?"
    en "Yes. It means people listen."
    return