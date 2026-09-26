init 3 python:
    CharacterController.get_character("dvh").interactions = [
            {LABEL: "q_inter_dvh_1", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_dvh_2", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_dvh_3", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_dvh_4", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_dvh_5", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_dvh_6", LOCATIONS: [THEATER]},
            ]
    CharacterController.get_character("dvh").default_expression = "angry01"

label q_inter_dvh_1:
    show expression cc.get_expression_image("dvh", "angry01")
    play voice3 girl34_yes_questioning2 noloop
    dvh "Yes?"
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, I was..."
    dvh "I am a busy woman, [mcname]. I do not have time for this."
    return
label q_inter_dvh_2:
    show expression cc.get_expression_image("dvh", "annoyed01")
    play voice2 d1s2_mchey noloop
    mc "Hi, Denise."
    dvh "..."
    return
label q_inter_dvh_3:
    show expression cc.get_expression_image("dvh", "serious01")
    play voice3 girl34_hey_angry3 noloop
    dvh "[mcname]. Have you been practicing for the show?"
    play voice2 d2s12_emmm noloop
    mc "Uhm, yep! Yep, yep, yep!"
    play voice3 girl34_disappointed_huh noloop
    dvh "...{w} I do not believe you."
    return
label q_inter_dvh_4:
    show expression cc.get_expression_image("dvh", "annoyed01")
    play voice3 girl34_arrogant_hm3 noloop
    dvh "If you need to speak with me. Don't."
    dvh "I will be in my office."
    return
label q_inter_dvh_5:
    show expression cc.get_expression_image("dvh", "depressed01")
    play voice3 girl34_angry_breath1 noloop
    dvh "Ik regisseerde echt theater in Nederland. Nu... Ik doe dit."
    play voice2 mc_surprised_what1 noloop
    mc "What was that, Denise?"
    dvh "It is nothing."
    return
label q_inter_dvh_6:
    show expression cc.get_expression_image("dvh", "yawn01")
    play voice2 d2s9_mchey noloop
    mc "Hey, Denise. I have a question about being a stagehand."
    play voice3 girl34_disappointed_snoring1 noloop
    dvh "Then ask Bruce."
    play voice2 d2s9_confused noloop volume 1.5
    mc "But-"
    dvh "Ask. Bruce."
    $ CharacterController.get_character("dvh").add_point()
    return