init 3 python:
    CharacterController.get_character("kw").interactions = [
            {LABEL: "q_inter_kw_1", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_kw_2", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_kw_3", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_kw_4", LOCATIONS: [THEATER]},
            ]
    CharacterController.get_character("kw").default_expression = "neutral01"

label q_inter_kw_1:
    show expression cc.get_expression_image("kw", "neutral01") as lth_kw_neutral01
    play voice2 mc_hey_hey7 noloop
    mc "Hello Kai."
    play voice3 boy10_hey_happy noloop
    kw "Good to see you, [mcname]. You need anything? How is your training coming?"
    mc "Pretty good. Bruce is a good teacher. Little rough around the edges, but fair."
    hide lth_kw_neutral01
    show expression cc.get_expression_image("kw", "smile01")
    play voice3 boy10_happy_laugh1 noloop
    kw "Haha. Yeah. Probably comes from a life on the stage. He's got more experience than all of us."
    play voice2 mc_arrogant_huh1 noloop
    mc "Really? I didn't know."
    kw "He doesn't like to brag."
    return
label q_inter_kw_2:
    show expression cc.get_expression_image("kw", "neutral01") as lth_kw_neutral01
    play voice3 boy10_thinking_hmm1 noloop
    kw "Mmmm."
    play voice2 mc_thinking_hmm2 noloop
    mc "You okay, Kai?"
    hide lth_kw_neutral01
    show expression cc.get_expression_image("kw", "smile01")
    play voice3 boy10_happy_laugh2 noloop
    kw "Haha. Yeah, [mcname]. Just centering myself before warmup."
    kw "In my experience, a performance is the best when everyone is completely engaged with their work."
    kw "You never want someone in the audience feeling like our minds are elsewhere during a song or dance number."
    play voice2 mc_thinking_oh1 noloop
    mc "Makes a lot of sense. Any tips?"
    kw "Haha. I wish. Deep breathing is probably my core excersize for it, but I think everyone has their style."
    kw "If you stick around, I'm sure you'll figure out what works for you, and what doesn't."
    return
label q_inter_kw_3:
    show expression cc.get_expression_image("kw", "neutral01")
    play voice3 boy10_hey_happy noloop
    kw "Hi [mcname]."
    play voice2 mc_happy_yay2 noloop
    mc "Hey Kai. You look pumped. What's up?"
    play voice3 boy10_yes_yeah noloop
    kw "My uncle will be in town for our next performance."
    mc "Cool. He likes theater too?"
    kw "He likes it to support me and he's always been the most supportive in my family."
    kw "So when he comes out, I go all out."
    return
label q_inter_kw_4:
    show expression cc.get_expression_image("kw", "sad01") as lth_kw_sad01
    play voice3 boy10_disappointed_ohh noloop
    kw "*deep breathing* It will be fine. Perfectly fine. Perfect, perfect."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "You alright, Kai?"
    play voice3 boy10_pain_ahh2 noloop
    kw "Fine. Hahaha? No no. Not fine, [mcname]. A friend told me that the Knightly Herald has a new theater critic on their staff."
    kw "I've everyone I know and no one knows what they look like and I am... well I'm you can see."
    play voice2 mc_hey_hey2 noloop
    mc "You're pretty good at this stuff, Kai. I'm sure you have nothing to worry about."
    hide lth_kw_sad01
    show expression cc.get_expression_image("kw", "angry01") as lth_kw_angry01
    play voice3 boy10_disappointed_ugh noloop
    kw "Of course I don't. I'm not an idiot, [mcname]. I'm fantastic on stage. But I... it's getting to me and..."
    hide lth_kw_angry01
    show expression cc.get_expression_image("kw", "sad01")
    play voice3 boy10_disappointed_exhale noloop
    kw "*sighs* I'm sorry, [mcname]. I gotta go take a walk or steal one of Denise's ciggarettes."
    kw "Something..."
    mc "Okay."
    return