init 3 python:
    CharacterController.get_character("cs").interactions = [
            {LABEL: "q_inter_cs_1", LOCATIONS: [STARDUCKS]},
            {LABEL: "q_inter_cs_2", LOCATIONS: [STARDUCKS]},
            {LABEL: "q_inter_cs_3", LOCATIONS: [STARDUCKS]},
            {LABEL: "q_inter_cs_4", LOCATIONS: [STARDUCKS]},
            {LABEL: "q_inter_cs_5", LOCATIONS: [STARDUCKS]},
            {LABEL: "q_inter_cs_6", LOCATIONS: [STARDUCKS]},
            ]
    CharacterController.get_character("cs").default_expression = "curious01"

label q_inter_cs_1:
    show expression cc.get_expression_image("cs", "curious01")
    play voice3 girl37_hey_simple noloop
    cs "Hi, welcome to Starducks. Where we don't purposefully burn the beans."
    play voice2 mc_surprised_what5 noloop
    mc "You... What?"
    cs "We burn the beans. On purpose."
    return
label q_inter_cs_2:
    show expression cc.get_expression_image("cs", "sad01") as lsc_cs_sad01
    play voice3 girl37_disappointed_aga2 noloop
    cs "If you want to order one of the frappes, they're unavailable today."
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "That sucks."
    cs "Yeah, the frappe machine is down. And there's only one approved technician who can service it. In the state."
    play voice2 mc_surprised_what1 noloop
    mc "Wait... What!?"
    hide lsc_cs_sad01
    show expression cc.get_expression_image("cs", "smile01")
    play voice3 girl37_yes_yep noloop
    cs "Yep. Company policy."
    return
label q_inter_cs_3:
    show expression cc.get_expression_image("cs", "embarrassed01")
    play voice2 mc_happy_yay2 noloop
    mc "How are you today, Cecilia?"
    play voice3 girl37_disappointed_aga1 noloop
    cs "I'm fine... Can't wait to get off though."
    mc "Any fun plans?"
    cs "Nope. Just going to go home, and cuddle up to my cat."
    return
label q_inter_cs_4:
    show expression cc.get_expression_image("cs", "annoyed01")
    play voice3 girl37_angry_argh1 noloop
    cs "I have to remember to quit my gym membership."
    play voice2 mc_surprised_oh1 noloop
    mc "Oh, why are you quitting the gym?"
    cs "Because they take the 'muct be able to lift 45 pounds over your head' at this job very seriously."
    cs "Why pay someone to work out, when I'm getting {i}paid{/i} to work out here?"
    return
label q_inter_cs_5:
    show expression cc.get_expression_image("cs", "curious01")
    play voice3 girl37_hey_simple noloop
    cs "Welcome to Starducks, home of the Starducks coffee. Can I take your order?"
    return
label q_inter_cs_6:
    show expression cc.get_expression_image("cs", "yawn01")
    play voice3 girl37_disappointed_mhh noloop
    cs "Mmmeeerrrmmmguguuuurg."
    play voice2 mc_thinking_mmm5 noloop
    mc "You okay, Cecilia?"
    cs "Need... Coffee..."
    return