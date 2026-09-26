init 3 python:
    CharacterController.get_character("ic").interactions = [
            {LABEL: "q_inter_ic_1", LOCATIONS: [SHOP_71STORE]},
            {LABEL: "q_inter_ic_2", LOCATIONS: [SHOP_71STORE], TIMESLOTS: [TIMESLOT_5] },
            {LABEL: "q_inter_ic_3", LOCATIONS: [SHOP_71STORE], DAYS: [FRIDAY], TIMESLOTS: [TIMESLOT_4]},
            {LABEL: "q_inter_ic_4", LOCATIONS: [SHOP_71STORE], DAYS: [TUESDAY], TIMESLOTS: [TIMESLOT_6]},
            {LABEL: "q_inter_ic_5", LOCATIONS: [SHOP_71STORE], TIMESLOTS: [TIMESLOT_7]},
            {LABEL: "q_inter_ic_6", LOCATIONS: [SHOP_71STORE], DAYS: [THURSDAY], TIMESLOTS: [TIMESLOT_4]},
            {LABEL: "q_inter_ic_7", LOCATIONS: [SHOP_71STORE], TIMESLOTS: [TIMESLOT_8]},
            {LABEL: "q_inter_ic_8", LOCATIONS: [SHOP_71STORE], DAYS: [SUNDAY], TIMESLOTS: [TIMESLOT_6]},
            {LABEL: "q_inter_ic_9", LOCATIONS: [SHOP_71STORE], DAYS: [WEDNESDAY], TIMESLOTS: [TIMESLOT_4]},
            ]
    CharacterController.get_character("ic").default_expression = False

label q_inter_ic_1:
    play voice3 girl30_thinking_hmm1 noloop
    ic "What can I get for you?"
    return
label q_inter_ic_2:
    play voice3 girl30_thinking_hmm2 noloop
    ic "Can I help you?"
    play voice2 mc_arrogant_hm1 noloop
    mc "Uhm, just looking."
    ic "Kay."
    return
label q_inter_ic_3:
    play voice3 girl30_arrogant_mmm noloop
    ic "If you're looking for condoms, we're out. Sorry."
    play voice2 mc_no_nah2 noloop
    mc "Actually I think I'm good."
    return
label q_inter_ic_4:
    play voice3 girl30_arrogant_hmf noloop
    ic "Can I help you find something?"
    play voice2 mc_no_uhuh1 noloop
    mc "I don't think so."
    ic "All right."
    return
label q_inter_ic_5:
    play voice3 girl30_arrogant_mmm noloop
    ic "Are you planning on buying something?"
    play voice2 d9s2_yeah noloop volume 1.5
    mc "Maybe."
    ic "Just let me know."
    return
label q_inter_ic_6:
    play voice3 girl30_disappointed_eeh2 noloop
    ic "If you're going to use the bathroom, please don't make a mess."
    play voice2 d2s9_confused noloop
    mc "Uh, okay?"
    return
label q_inter_ic_7:
    play voice3 girl30_disappointed_mmm2 noloop
    ic "We're closing soon, please grab whatever you're looking for and check out."
    return
label q_inter_ic_8:
    play voice3 girl30_arrogant_hmf noloop
    ic "If you see the weird chick talking about cashier robots, tell her I'm not in the mood tonight."
    return
label q_inter_ic_9:
    play voice3 girl30_thinking_mmm2 noloop
    ic "I'll be with you in a sec."
    return