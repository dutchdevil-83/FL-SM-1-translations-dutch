init 3 python:
    CharacterController.get_character("dc").interactions = [
            {LABEL: "q_inter_dc_1", LOCATIONS: [PARK]},
            {LABEL: "q_inter_dc_2", LOCATIONS: [PARK]},
            {LABEL: "q_inter_dc_3", LOCATIONS: [PARK]},
            {LABEL: "q_inter_dc_4", LOCATIONS: [PARK], BEFORE_SCENE: [DC_STORY, "sm1cs_dc002"]},
            {LABEL: "q_inter_dc_5", LOCATIONS: [PARK], AFTER_SCENE: [DC_STORY, "sm1cs_dc001i"]},
            {LABEL: "q_inter_dc_6", LOCATIONS: [STARDUCKS], BEFORE_SCENE: [DC_STORY, "sm1cs_dc002"]},
            {LABEL: "q_inter_dc_7", LOCATIONS: [STARDUCKS], BEFORE_SCENE: [DC_STORY, "sm1cs_dc002"]},
            {LABEL: "q_inter_dc_8", LOCATIONS: [STARDUCKS], BEFORE_SCENE: [DC_STORY, "sm1cs_dc002"]},
            {LABEL: "q_inter_dc_9", LOCATIONS: [STARDUCKS], AFTER_SCENE: [DC_STORY, "sm1cs_dc003"]},

            ]
    CharacterController.get_character("dc").default_expression = "serious01"

label q_inter_dc_1:
    show expression cc.get_expression_image("dc", "serious01")
    play voice3 girl24_arrogant_hm1 noloop
    dc "Keep your eyes peeled for pickpockets. Apparently, there's a little group of them running around the park."
    return
label q_inter_dc_2:
    show expression cc.get_expression_image("dc", "embarrassed01")
    play voice3 girl24_disappointed_hmf noloop
    dc "Ugh, another date cancelled..."
    dc "Oh, uh, another, uhm, court date cancelled. Keep moving."
    return
label q_inter_dc_3:
    show expression cc.get_expression_image("dc", "serious01")
    play voice3 girl24_arrogant_hm3 noloop
    dc "Nothing to see here, move along. Move along."
    return
label q_inter_dc_4:
    show expression cc.get_expression_image("dc", "serious01") as dc_serious01
    play voice3 girl24_hey_angry noloop
    dc "Hey you! You match the description of a flasher in the park. I need to see some identification."
    play voice2 mc_thinking_emm1 noloop
    mc "You don't need to see my identification."
    play voice3 girl24_disappointed_eeh1 noloop
    dc "I... Guess I don't. The guy they described was blonde."
    hide dc_serious01
    show expression cc.get_expression_image("dc", "serious01")
    play voice2 mc_yes_okay2 noloop
    mc "I'll move along then."
    play voice3 girl24_yes_yap noloop
    dc "Yep, move along, move along."
    return
label q_inter_dc_5:
    show expression cc.get_expression_image("dc", "serious01")
    play voice3 girl36_surprised_huh1 noloop
    dc "Have you seen that creep at all?"
    play voice2 mc_no_uhuh1 noloop
    mc "I haven't."
    dc "Damn. Well let me know if you do."
    return
label q_inter_dc_6:
    show expression cc.get_expression_image("dc", "serious01")
    play voice3 girl36_arrogant_hmf noloop
    dc "Civilian."
    play voice2 mc_yes_yes7 noloop
    mc "Officer."
    return
label q_inter_dc_7:
    show expression cc.get_expression_image("dc", "serious01") as q_inter_dc7_serious01
    play voice3 girl36_arrogant_huh1 noloop
    dc "Do I know you from somewhere?"
    play voice2 mc_no_no10 noloop
    mc "I don't think so?"
    hide q_inter_dc7_serious01
    show expression cc.get_expression_image("dc", "neutral01")
    play voice3 girl36_thinking_hmm noloop
    dc "I swear you look so familiar..."
    return
label q_inter_dc_8:
    show expression cc.get_expression_image("dc", "serious01") as q_inter_dc8_serious01
    play voice2 mc_hey_hey5 noloop
    mc "Hey, Debbie-"
    play voice3 girl36_disappointed_geh noloop
    dc "I, uhm, can't talk right now. I'm needed back at the station."
    mc "But-"
    hide q_inter_dc8_serious01
    show expression cc.get_expression_image("dc", "neutral01")
    dc "Later, [mcname]."
    return
label q_inter_dc_9:
    show expression cc.get_expression_image("dc", "embarrassed01") as q_inter_dc9_embarrassed01
    play voice2 mc_hey_hey2 noloop
    mc "Deb-"
    play sound sfx_walkie_talkie1
    play voice3 girl36_arrogant_huh1 noloop
    dc "Krsssht - what was that?"
    mc "Huh?"
    hide q_inter_dc9_embarrassed01
    show expression cc.get_expression_image("dc", "serious01")
    play voice3 girl36_thinking_hmm noloop
    dc "Something on my radio, uhh, I need to respond right away."
    play sound sfx_walkie_talkie1
    dc "Krrrsssssht - roger that, over and out."
    return
label q_inter_dc_10:
    show expression cc.get_expression_image("dc", "sad01") as q_inter_dc10_sad01
    play voice3 girl36_surprised_ohmy1 noloop
    dc "What am I going to say..."
    play voice2 d1s2_hmm noloop volume 1.4
    mc "Debbie?"
    hide q_inter_dc10_sad01
    show expression cc.get_expression_image("dc", "embarrassed01")
    play voice3 girl36_surprised_eeh noloop
    dc "Oh, uhm, [mcname], I... I have to go - somewhere. Bye."
    return
label q_inter_dc_11:
    show expression cc.get_expression_image("dc", "serious01")
    play voice3 girl36_hey_angry1 noloop
    dc "I know this isn't the park, but keep your eyes peeled. You never know where that creep might be."
    return