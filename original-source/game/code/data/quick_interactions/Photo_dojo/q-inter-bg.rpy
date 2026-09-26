init 3 python:
    CharacterController.get_character("bg").interactions = [
            {LABEL: "q_inter_bg_1", LOCATIONS: [PHOTO_DOJO], BEFORE_SCENE: [BG_STORY, "sm1cs_bg001"]},
            {LABEL: "q_inter_bg_2", LOCATIONS: [PHOTO_DOJO], AFTER_SCENE: [BG_STORY, "sm1cs_bg001"]},
            {LABEL: "q_inter_bg_3", LOCATIONS: [PHOTO_DOJO], AFTER_SCENE: [BG_STORY, "sm1cs_bg001"]},
            {LABEL: "q_inter_bg_4", LOCATIONS: [PHOTO_DOJO], AFTER_SCENE: [BG_STORY, "sm1cs_bg001"]},
            {LABEL: "q_inter_bg_5", LOCATIONS: [PHOTO_DOJO], AFTER_SCENE: [BG_STORY, "sm1cs_bg001"]},
            {LABEL: "q_inter_bg_6", LOCATIONS: [PHOTO_DOJO], AFTER_SCENE: [BG_STORY, "sm1cs_bg001"]},

            ]
    CharacterController.get_character("bg").default_expression = "neutral01"

label q_inter_bg_1:
    show expression cc.get_expression_image("bg", "smile01")
    play voice3 girl28_hey_sexy noloop
    "BDSM Model" "Hey!"
    return
label q_inter_bg_2:
    show expression cc.get_expression_image("bg", "smile01")
    play voice3 girl28_hey_sexy noloop
    bg "Oh hey, [mcname]!"
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What are you up to, Amore?"
    play voice3 girl28_arrogant_heh noloop
    bg "I just got this new powder to help me get into the latex. Not sure how I feel about it yet."
    return
label q_inter_bg_3:
    show expression cc.get_expression_image("bg", "smile01")
    play voice3 girl28_happy_mmm1 noloop
    bg "Mmmmmm."
    play voice2 mc_surprised_huh7 noloop
    mc "Huh?"
    play voice3 girl28_happy_relief1 noloop
    bg "Oh, nothing. I just enjoy the feeling of latex."
    return
label q_inter_bg_4:
    show expression cc.get_expression_image("bg", "neutral01") as lpd_bg_neutral01
    play voice2 mc_surprised_huh7 noloop
    mc "How long can you wear that oufit for?"
    play voice3 girl26_thinking_ehh2 noloop
    bg "I mean, pretty much all day. I just need to stay hydrated."
    hide lpd_bg_neutral01
    show expression cc.get_expression_image("bg", "neutral02")
    play voice3 girl26_thinking_hmm1 noloop
    bg "It can get a little sweaty in this outfit."
    return
label q_inter_bg_5:
    show expression cc.get_expression_image("bg", "neutral01") as lpd_bg_neutral01
    play voice3 girl28_hey_sexy noloop
    bg "Hey, [mcname]..."
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah?"
    hide lpd_bg_neutral01
    show expression cc.get_expression_image("bg", "neutral02") as lpd_bg_neutral02
    play voice3 girl28_surprised_eeh noloop
    bg "When, uhh, are we going to shoot again?"
    play voice2 mc_thinking_oh1 noloop
    mc "Soon! I hope, at least."
    hide lpd_bg_neutral02
    show expression cc.get_expression_image("bg", "smile01")
    play voice3 girl26_happy_yay noloop
    bg "Me too!"
    return
label q_inter_bg_6:
    show expression cc.get_expression_image("bg", "smile01")
    play voice3 girl28_hey_sexy noloop
    bg "Hey [mcname]"
    return