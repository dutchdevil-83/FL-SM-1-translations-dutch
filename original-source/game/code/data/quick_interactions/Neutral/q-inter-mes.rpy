init 3 python:
    CharacterController.get_character("mes").interactions = [
            {LABEL: "q_inter_mes_1", AFTER_SCENE: [MES_STORY, "sm1cs_mes001"]},
            {LABEL: "q_inter_mes_2", AFTER_SCENE: [MES_STORY, "sm1cs_mes001"]},
            {LABEL: "q_inter_mes_3", AFTER_SCENE: [MES_STORY, "sm1cs_mes001"]},
            {LABEL: "q_inter_mes_4", AFTER_SCENE: [MES_STORY, "sm1cs_mes003"]},
            {LABEL: "q_inter_mes_5", AFTER_SCENE: [MES_STORY, "sm1cs_mes003"]},
            {LABEL: "q_inter_mes_6", AFTER_SCENE: [MES_STORY, "sm1cs_mes003"]},


            ]
    CharacterController.get_character("mes").default_expression = "neutral01"

label q_inter_mes_1:
    show expression cc.get_expression_image("mes", "neutral01") as lst_my_neutral
    play voice3 min_hey_simple noloop
    mes "Hey [mcname]."
    mes "What's your poison?"
    play voice2 mc_no_uhuh1 noloop
    mc "Nothing right now. Maybe another time, Min."
    mes "Sure."
    return
label q_inter_mes_2:
    show expression cc.get_expression_image("mes", "annoyed01") as lst_my_annoyed
    play voice2 d1s2_mchey noloop
    mc "How are your classes going?"
    play voice3 min_disappointed_ehh1 noloop
    mes "I'd rather not talk about them."
    mc "Everything alright?"
    hide lst_my_annoyed
    show expression cc.get_expression_image("mes", "neutral01")
    play voice3 min_thinking_oh noloop
    mes "Oh the classes are fine, but being in there is like eating unsalted kimchi."
    $ CharacterController.get_character("mes").add_point()
    return
label q_inter_mes_3:
    show expression cc.get_expression_image("mes", "smile01") as lst_my_smile
    play voice3 min_happy_mmm noloop
    mes "It is nice of you to check in on me, [mcname]."
    mes "But I am fine. I promise you."
    play voice2 mc_yes_okay2 noloop
    mc "Good, then you won't mind me hanging out for a drink."
    mes "Of course not."
    return
label q_inter_mes_4:
    show expression cc.get_expression_image("mes", "neutral01") as lst_my_neutral
    play voice2 mc_hey_hey10 noloop
    mc "Hey there."
    play voice3 min_hey_greeting noloop
    mes "Hey yourself."
    mc "How you doing?"
    hide lst_my_neutral
    show expression cc.get_expression_image("mes", "smile01")
    play voice3 min_thinking_hmm2 noloop
    mes "Every day, I feel a little bit more confident in my decision to come home."
    play voice2 mc_thinking_mmm5 noloop
    mc "Sounds good."
    $ CharacterController.get_character("mes").add_point()
    return
label q_inter_mes_5:
    show expression cc.get_expression_image("mes", "neutral01") as lst_my_neutral
    play voice3 min_disgust_off noloop
    mes "My ass still hurts, [mcname]."
    play voice2 mc_thinking_oh1 noloop
    mc "Sorry. I won't be so rough next time."
    mes "I meant, it feels so good after not feeling it for so long."
    mc "Heh. Well thank you, Squizzle."
    hide lst_my_neutral
    show expression cc.get_expression_image("mes", "laugh01")
    play voice3 min_old_laugh noloop
    mes "*chuckles softly*"
    $ CharacterController.get_character("mes").add_point()
    return
label q_inter_mes_6:
    show expression cc.get_expression_image("mes", "neutral01") as lst_my_neutral
    play voice3 min_old_huh noloop
    mes "How is the studio going, [mcname]?"
    play voice2 d9s2_yeah noloop volume 1.67
    mc "Not too bad."
    mc "Always something going on."
    mc "Sometimes I forget to take a break and live a little."
    hide lst_my_neutral
    show expression cc.get_expression_image("mes", "smile01")
    play voice3 min_thinking_hmm2 noloop
    mes "Well, I'm honored you chose my company as for your precious break time."
    $ CharacterController.get_character("mes").add_point()
    return