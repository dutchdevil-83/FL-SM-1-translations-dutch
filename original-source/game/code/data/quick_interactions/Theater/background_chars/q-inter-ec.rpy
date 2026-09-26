init 3 python:
    CharacterController.get_character("ec").interactions = [
            {LABEL: "q_inter_ec_1", LOCATIONS: [STARDUCKS], AFTER_SCENE: [THEATER_STORY_LINE, "sm1fs_t003"]},
            {LABEL: "q_inter_ec_2", LOCATIONS: [STARDUCKS], AFTER_SCENE: [THEATER_STORY_LINE, "sm1fs_t003"]},
            {LABEL: "q_inter_ec_3", LOCATIONS: [THEATER], AFTER_SCENE: [THEATER_STORY_LINE, "sm1fs_t003"]},
            {LABEL: "q_inter_ec_4", LOCATIONS: [THEATER], AFTER_SCENE: [THEATER_STORY_LINE, "sm1fs_t003"]},
            {LABEL: "q_inter_ec_5", LOCATIONS: [THEATER], AFTER_SCENE: [THEATER_STORY_LINE, "sm1fs_t003"]},
            {LABEL: "q_inter_ec_6", LOCATIONS: [THEATER], AFTER_SCENE: [THEATER_STORY_LINE, "sm1fs_t003"]},
            {LABEL: "q_inter_ec_7", LOCATIONS: [THEATER], AFTER_SCENE: [THEATER_STORY_LINE, "sm1fs_t003"]},
            ]
    CharacterController.get_character("ec").default_expression = "neutral01"

label q_inter_ec_1:
    show expression cc.get_expression_image("ec", "neutral01")
    play voice2 d2s9_mchey noloop volume 1.5
    mc "Hey Eileen."
    play voice3 girl32_hey_short noloop
    ec "Oh hey, [mcname]. Sorry I can't stay in chat. Deniese needs her coffee or she'll..."
    ec "Well she works a lot better with a good cofee."
    mc "I getcha. Later."
    return
label q_inter_ec_2:
    show expression cc.get_expression_image("ec", "neutral01")
    play voice3 girl32_hey_calm noloop
    ec "*waves* Hey [mcname], "
    play voice2 d2s9_mchey noloop volume 1.6
    mc "Eileen."
    play voice3 girl32_thinking_hmm3 noloop
    ec "I don't know if anyone has said anything, but it seems like you're doing a solid job helping Sam out."
    ec "If you're still interested in getting a part for a show, I think Denise will be open to it."
    ec "Some day. But... I should get going."
    mc "See ya."
    return
label q_inter_ec_3:
    show expression cc.get_expression_image("ec", "neutral01")
    play voice3 girl32_hey_happy noloop
    ec "Yo, [mcname]."
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Another day in the life of an actress, right?"
    play voice3 girl32_arrogant_tha noloop
    ec "You're an actress?"
    mc "No...?"
    ec "Well neither am I. I'm just a go-fer."
    return
label q_inter_ec_4:
    show expression cc.get_expression_image("ec", "sad01") as q_inter_ec4_sad01
    play voice3 girl32_arrogant_ahh noloop
    ec "Maaaaaaaaaan."
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What's wrong, Eileen?"
    hide q_inter_ec4_sad01
    show expression cc.get_expression_image("ec", "neutral01")
    play voice3 girl32_disappointed_ergh noloop
    ec "The coffee shop gave me soy milk today."
    play voice2 mc_surprised_huh7 noloop
    mc "As opposed to what, oat milk?"
    play voice3 girl32_no_confident noloop
    ec "No. Denise only drinks whole milk in her coffee."
    return
label q_inter_ec_5:
    show expression cc.get_expression_image("ec", "neutral01") as q_inter_ec5_neutral01
    play voice3 girl32_angry_argh noloop
    ec "Gah, Kellie can be such a pain!"
    play voice2 mc_surprised_huh7 noloop
    mc "What'd she do?"
    hide q_inter_ec5_neutral01
    show expression cc.get_expression_image("ec", "angry01")
    play voice3 girl32_disappointed_ehh1 noloop
    ec "She is {i}demanding{/i} that I go get her coffee! Because she's a star, and stars get coffee!"
    play voice2 mc_surprised_wow4 noloop
    mc "Wow..."
    ec "Gah, there is no matching the ego of an actress!"
    return
label q_inter_ec_6:
    show expression cc.get_expression_image("ec", "neutral01")
    play voice3 girl32_arrogant_tha noloop
    ec "You know, sometimes I wonder if Veronica is faking it."
    play voice2 mc_surprised_what1 noloop
    mc "Faking what?"
    ec "Being that nice. Nobody is that nice."
    return
label q_inter_ec_7:
    show expression cc.get_expression_image("ec", "neutral01") as q_inter_ec7_neutral01
    play voice3 girl32_thinking_hmm1 noloop
    ec "You're working with Bruce, right?"
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh."
    hide q_inter_ec7_neutral01
    show expression cc.get_expression_image("ec", "smile01")
    play voice3 girl32_happy_aha noloop
    ec "I like Bruce. He gets it."
    play voice2 mc_surprised_what7 noloop
    mc "Gets what?"
    ec "Exactly."
    return