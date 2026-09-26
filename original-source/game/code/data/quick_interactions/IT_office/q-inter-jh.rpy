init 3 python:
    CharacterController.get_character("jh").interactions = [
            {LABEL: "q_inter_jh_1", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_jh_2", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_jh_3", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_jh_4", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_jh_5", LOCATIONS: [IT_OFFICE]},

            ]
    CharacterController.get_character("jh").default_expression = "neutral01"

label q_inter_jh_1:
    show expression cc.get_expression_image("jh", "neutral01") as lst_en_neutral01
    play voice2 mc_hey_hey7 noloop
    mc "Hey, Jayden."
    play voice3 boy10_surprised_oh noloop
    jh "Oh, uh, hi [mcname]."
    mc "What's up?"
    hide lst_en_neutral01
    show expression cc.get_expression_image("jh", "sad01")
    play voice3 boy10_disappointed_ugh noloop
    jh "Oh just trying to figure out why the adaptive assist high contrast mode on the site is making the website crash for people."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, sounds... Difficult."
    jh "You have {i}no idea.{/i}"
    return
label q_inter_jh_2:
    show expression cc.get_expression_image("jh", "sad01")
    play voice3 boy10_disappointed_ohh noloop
    jh "Urrrgggh..."
    play voice2 d1s2_hmm noloop volume 1.4
    mc "Something wrong, Jayden?"
    play voice3 boy10_yes_yeah noloop
    jh "Yeah. I think April's been messing with my code again."
    mc "Oh? How do you know?"
    jh "... It's better now."
    return
label q_inter_jh_3:
    show expression cc.get_expression_image("jh", "angry01")
    play voice2 mc_hey_hey5 noloop
    mc "Jayden, can I ask-"
    play voice3 boy10_disappointed_exhale noloop
    jh "Can't talk, busy."
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, I'm-"
    play voice3 boy10_arrogant_huh noloop
    jh "Why aren't we just using hex codes for colors!?!"
    mct "Someone has some feelings about colors, huh..."
    return
label q_inter_jh_4:
    show expression cc.get_expression_image("jh", "neutral01")
    play voice3 boy10_hey_happy noloop
    jh "What do you think, [mcname], CSS or HTML?"
    play voice2 d2s12_emmm noloop
    mc "Uhm... I don't really have to use either, but... HTML?"
    jh "Mmmmm. Maybe..."
    return
label q_inter_jh_5:
    show expression cc.get_expression_image("jh", "neutral01")
    play voice3 boy10_hey_happy noloop
    jh "Hey, have you heard about these new books?"
    play voice2 d1s2_hmm noloop volume 1.4
    mc "Which ones?"
    jh "A Castle of Thistle and Orchids. Anna turned me on to them."
    return