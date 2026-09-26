init 3 python:
    CharacterController.get_character("mj").interactions = [
            {LABEL: "q_inter_mj_1", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_mj_2", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_mj_3", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_mj_4", LOCATIONS: [IT_OFFICE]},
            ]
    CharacterController.get_character("mj").default_expression = "neutral01"

label q_inter_mj_1:
    show expression cc.get_expression_image("mj", "smile01")
    play voice3 girl35_thinking_hmm4 noloop
    mj "[mcname], are participating in this bet on who will have less errors, Anna or April?"
    play voice2 mc_thinking_oh1 noloop
    mc "I didn't even realize there was a contest between them."
    mj "My money is on April."
    return
label q_inter_mj_2:
    show expression cc.get_expression_image("mj", "sad01")
    play voice2 mc_happy_yay2 noloop
    mc "Morning, Megan."
    play voice3 girl35_disappointed_mmm1 noloop
    mj "Mmmm, coffee."
    play voice2 mc_surprised_uh2 noloop
    mc "Huh?"
    mj "Claire gets {i}the best{/i} coffee for the office."
    mc "I'll have to grab a cup then."
    return
label q_inter_mj_3:
    show expression cc.get_expression_image("mj", "smile01")
    play voice3 girl35_hey_fun3 noloop
    mj "Hey, [mcname], make sure you get me your test reports soon."
    play voice2 mc_yes_aga2 noloop
    mc "I will-"
    mj "Actually, I'll just talk to Anna about it! See if she can ge April to surrender her's too."
    return
label q_inter_mj_4:
    show expression cc.get_expression_image("mj", "neutral01") as lst_en_neutral01
    play voice3 girl35_hey_fun1 noloop
    mj "Hey, [mcname], I've got a question for you."
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah? What's up?"
    hide lst_en_neutral01
    show expression cc.get_expression_image("mj", "smile01")
    play voice3 girl35_arrogant_laugh noloop
    mj "Do you know April and Anna are always at each other's throats?"
    play voice2 mc_thinking_hmm5 noloop
    mc "Uhm... No."
    mj "Drats. I was hoping you would..."
    return