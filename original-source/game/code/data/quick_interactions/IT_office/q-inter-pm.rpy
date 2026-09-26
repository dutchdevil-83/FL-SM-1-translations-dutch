init 3 python:
    CharacterController.get_character("pm").interactions = [
            {LABEL: "q_inter_pm_1", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_pm_2", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_pm_3", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_pm_4", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_pm_5", LOCATIONS: [IT_OFFICE]},
            ]
    CharacterController.get_character("pm").default_expression = "neutral01"

label q_inter_pm_1:
    show expression cc.get_expression_image("pm", "smile01")
    play voice3 boy7_hey_short noloop
    pm "[mcname]! How are things going over on Anna's team?"
    play voice2 mc_thinking_oh1 noloop
    mc "Good! I think."
    pm "Still blows my mind she hasn't been promoted yet."
    return
label q_inter_pm_2:
    show expression cc.get_expression_image("pm", "neutral01")
    play voice3 boy7_hey_short noloop
    pm "Hey, what's it like working with April?"
    play voice2 mc_thinking_hmm5 noloop
    mc "It's good? She definitely knows what she's doing."
    pm "Yeah, that's what her reports show. But I've heard she has a real big personality."
    return
label q_inter_pm_3:
    show expression cc.get_expression_image("pm", "neutral01") as q_inter_pm3_neutral01
    play voice2 mc_happy_yay2 noloop
    mc "Hey, Peter."
    play voice3 boy7_hey_serious noloop
    pm "Hey! [mcname], whose always playing the rock music way too loud over there?"
    play voice2 mc_thinking_hmm5 noloop
    mc "Uhm... April?"
    hide q_inter_pm3_neutral01
    show expression cc.get_expression_image("pm", "smile01")
    play voice3 boy7_arrogant_hmm3 noloop
    pm "Tell her I dig it."
    play voice2 mc_yes_okay2 noloop
    mc "Okay?"
    return
label q_inter_pm_4:
    show expression cc.get_expression_image("pm", "smile01")
    play voice3 boy7_hey_serious noloop
    pm "[mcname], tell me about Nari."
    play voice2 mc_thinking_mmm4 noloop
    mc "Well, she's quiet, but super smart and has a great work ethic."
    pm "Damn. I wish she was on my team..."
    return
label q_inter_pm_5:
    show expression cc.get_expression_image("pm", "angry01") as q_inter_pm5_angry01
    play voice3 boy7_angry_argh1 noloop
    pm "Shit!"
    play voice2 mc_surprised_what1 noloop
    mc "What's wrong, Peter?"
    hide q_inter_pm5_angry01
    show expression cc.get_expression_image("pm", "sad01") as q_inter_pm5_sad01
    play voice3 boy7_arrogant_hmm2 noloop
    pm "Agh, my portfolio took a hit and it's killing me."
    play voice2 mc_thinking_hmm3 noloop
    mc "I think Nari is into that..."
    hide q_inter_pm5_sad01
    show expression cc.get_expression_image("pm", "angry01")
    play voice3 boy7_thinking_oh noloop
    pm "Well, if she's any good at stocks, definitely get your tips from her. Not me."
    return