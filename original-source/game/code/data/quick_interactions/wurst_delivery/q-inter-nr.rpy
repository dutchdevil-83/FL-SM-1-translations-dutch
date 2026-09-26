init 3 python:
    CharacterController.get_character("nr").interactions = [
            {LABEL: "q_inter_nr_1", DAYS: [WORKDAYS], TIMESLOTS: [TIMESLOT_5]},
            {LABEL: "q_inter_nr_2", DAYS: [FRIDAY]},
            {LABEL: "q_inter_nr_3"},
            {LABEL: "q_inter_nr_4"},
            {LABEL: "q_inter_nr_5"},
            {LABEL: "q_inter_nr_6", TIMESLOTS: [TIMESLOT_8]},
            {LABEL: "q_inter_nr_7"},
            {LABEL: "q_inter_nr_8"},
            {LABEL: "q_inter_nr_9"},
            {LABEL: "q_inter_nr_10"},
            {LABEL: "q_inter_nr_11"},
            {LABEL: "q_inter_nr_12", TIMESLOTS: [TIMESLOT_6]},
            {LABEL: "q_inter_nr_13"},
            {LABEL: "q_inter_nr_14"},
            {LABEL: "q_inter_nr_15", AFTER_SCENE: [MAS_STORY, "sm1cs_mas002"]},
            {LABEL: "q_inter_nr_16", AFTER_SCENE: [MAS_STORY, "sm1cs_mas002"]},
            {LABEL: "q_inter_nr_17", AFTER_SCENE: [MAS_STORY, "sm1cs_mas002"]},
            {LABEL: "q_inter_nr_18"},
            ]
    CharacterController.get_character("nr").default_expression = "annoyed1"

label q_inter_nr_1:
    show expression cc.get_expression_image("nr", "serious1")
    play voice3 boy7_thinking_hmm1 noloop
    nr "Working hard or hardly working?"
    return
label q_inter_nr_2:
    show expression cc.get_expression_image("nr", "laugh1")
    play voice3 boy7_happy_phew noloop
    nr "Thank god it's Friday. Am I right or am I right?"
    return
label q_inter_nr_3:
    show expression cc.get_expression_image("nr", "laugh1")
    play voice3 boy7_happy_laugh2 noloop
    nr "I should get back to it. These wieners won't make themselves."
    return
label q_inter_nr_4:
    show expression cc.get_expression_image("nr", "laugh1")
    play voice3 boy7_hey_short noloop
    nr "Hey."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Huh?"
    play voice3 boy7_happy_laugh2 noloop
    nr "Pull my weiner. Heh heh."
    return
label q_inter_nr_5:
    show expression cc.get_expression_image("nr", "laugh1")
    play voice3 boy7_disappointed_hmm noloop
    nr "I had a good feeling about you, kid."
    nr "Don't prove me wrong."
    return
label q_inter_nr_6:
    show expression cc.get_expression_image("nr", "annoyed1")
    play voice3 boy7_disappointed_aah noloop
    nr "Ahh, nothing beats a banger in the mouth after a long day?"
    return
label q_inter_nr_7:
    show expression cc.get_expression_image("nr", "serious1")
    play voice3 boy7_happy_mmm noloop
    nr "Smell that? That's some good bavarian cooking right there."
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "What made you get into this kind of work, Nelson?"
    nr "Always loved a good brat. The heat, the taste. Does miracles for your mood."
    return
label q_inter_nr_8:
    show expression cc.get_expression_image("nr", "serious1")
    play voice3 boy7_thinking_hmm3 noloop
    nr "*sniffs* Mmm. Yup, needs a bit more dil before it's ready."
    return
label q_inter_nr_9:
    show expression cc.get_expression_image("nr", "annoyed1")
    play voice3 boy7_hey_serious noloop
    nr "Hey, what are you standing around for?"
    nr "Don't you have deliveries to make?"
    return
label q_inter_nr_10:
    show expression cc.get_expression_image("nr", "smile1")
    play voice3 boy7_arrogant_yeah noloop
    nr "Let it rip, kid! Get out there and show those weiners who's boss."
    return
label q_inter_nr_11:
    show expression cc.get_expression_image("nr", "laugh1")
    play voice3 boy7_happy_laugh3 noloop
    nr "My father always said 'Grab life by the sausage.'"
    return
label q_inter_nr_12:
    show expression cc.get_expression_image("nr", "serious1")
    play voice3 boy7_happy_mmm noloop
    nr "A day in Crowning isn't complete without a Wurst Dog."
    play voice2 mc_thinking_mmm4 noloop
    mc "I think most people say that about coffee, not hot dogs."
    nr "Yeah but that's just cause they haven't tried it yet."
    return
label q_inter_nr_13:
    show expression cc.get_expression_image("nr", "smile1")
    play voice3 boy7_thinking_hmm1 noloop
    nr "They might not be gourmet, but they will fill your belly."
    return
label q_inter_nr_14:
    show expression cc.get_expression_image("nr", "annoyed1")
    play voice3 boy7_thinking_oh noloop
    nr "I'm thinking of franchising, putting a shop near some of those resorts in the mountains."
    nr "Right now they only serve burgers. Can you believe that?"
    return
label q_inter_nr_15:
    show expression cc.get_expression_image("nr", "serious1")
    play voice3 boy7_thinking_oh noloop
    nr "Maya acting a little strange to you?"
    mc "Um. I didn't notice."
    nr "Alright."
    return
label q_inter_nr_16:
    show expression cc.get_expression_image("nr", "smile1")
    play voice3 boy7_thinking_oh noloop
    nr "Glad to see you're still coming by, [mcname]."
    mc "Thanks, Nelson."
    return
label q_inter_nr_17:
    show expression cc.get_expression_image("nr", "smile1")
    play voice3 boy7_thinking_oh noloop
    nr "Always glad we got our regulars."
    nr "Gives me room to try out special saussages."
    nr "From far out places."
    return
label q_inter_nr_18:
    show expression cc.get_expression_image("nr", "serious1")
    play voice3 boy7_thinking_oh noloop
    nr "Some customers are so strange."
    nr "Don't ask how it's made. Just eat it."
    return