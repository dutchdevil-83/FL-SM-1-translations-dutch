init 3 python:
    CharacterController.get_character("sb").interactions = [
            {LABEL: "q_inter_sb_1", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_sb_2", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_sb_3", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_sb_4", LOCATIONS: [THEATER]},

            ]
    CharacterController.get_character("sb").default_expression = "neutral02"

label q_inter_sb_1:
    show expression cc.get_expression_image("sb", "smile01")
    play voice3 boy5_hey_happy noloop
    sb "Hey, kid."
    play voice2 mc_surprised_oh1 noloop
    mc "Oh, uh, hey."
    return
label q_inter_sb_2:
    show expression cc.get_expression_image("sb", "neutral01") as lth_sb_neutral01
    play voice2 d1s2_mchey noloop volume 1.5
    mc "What's up, Sam?"
    play voice3 boy5_thinking_hmm1 noloop
    sb "Bruce."
    play voice2 mc_surprised_huh7 noloop
    mc "Huh?"
    hide lth_sb_neutral01
    show expression cc.get_expression_image("sb", "angry01")
    play voice3 boy5_thinking_eeh2 noloop
    sb "Only person that calls me Sam is my Mom. Call me Bruce."
    play voice2 mc_yes_okay2 noloop
    mc "Okay... Bruce."
    return
label q_inter_sb_3:
    show expression cc.get_expression_image("sb", "neutral01") as lth_sb_neutral01
    play voice2 mc_hey_hey2 noloop
    mc "Hey, Bruce."
    play voice3 boy5_yes_yeah noloop
    sb "Yeah?"
    play voice2 mc_thinking_emm1 noloop
    mc "You ever hear the expression you shouldn't trust someone with two first names?"
    hide lth_sb_neutral01
    show expression cc.get_expression_image("sb", "angry01")
    play voice3 boy5_disappointed_ehh1 noloop
    sb "..."
    play voice2 mc_thinking_mmm3 noloop
    mc "...{w} I'll just go."
    return
label q_inter_sb_4:
    show expression cc.get_expression_image("sb", "smile01")
    play voice3 boy5_arrogant_heh1 noloop
    sb "Quick, [mcname], how many knives you got on you?"
    play voice2 d2s12_emmm noloop
    mc "Uhm, none?"
    sb "How... What... I..."
    return