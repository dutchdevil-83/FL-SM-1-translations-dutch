init 3 python:
    CharacterController.get_character("vs").interactions = [
            {LABEL: "q_inter_vs_1", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_vs_2", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_vs_3", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_vs_4", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_vs_5", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_vs_6", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_vs_7", LOCATIONS: [THEATER], AFTER_SCENE: [VS_STORY, "sm1cs_vs001"]},
            {LABEL: "q_inter_vs_8", LOCATIONS: [THEATER], AFTER_SCENE: [VS_STORY, "sm1cs_vs001"], BEFORE_SCENE: [VS_STORY, "sm1cs_vs003"]},
            {LABEL: "q_inter_vs_9", LOCATIONS: [THEATER], AFTER_SCENE: [VS_STORY, "sm1cs_vs003"]},
            {LABEL: "q_inter_vs_10", LOCATIONS: [THEATER], AFTER_SCENE: [VS_STORY, "sm1cs_vs003"]},
            {LABEL: "q_inter_vs_11", LOCATIONS: [THEATER], AFTER_SCENE: [VS_STORY, "sm1cs_vs003"]},

            ]
    CharacterController.get_character("vs").default_expression = "neutral01"

label q_inter_vs_1:
    show expression cc.get_expression_image("vs", "smile01")
    play voice2 d1s2_mchey noloop
    mc "Hey, Veronica!"
    play voice3 girl33_hey_serious noloop
    vs "Hey, yourself!"
    return
label q_inter_vs_2:
    show expression cc.get_expression_image("vs", "smile01")
    play voice2 d1s2_hmm noloop volume 1.8
    mc "What're you up to?"
    play voice3 girl33_disappointed_oh noloop
    vs "Oh, I'm just about to do some stretching!"
    play voice2 mc_thinking_mmm7 noloop
    mc "Niccce."
    play voice3 girl33_arrogant_laugh noloop
    vs "You know, you're always welcome to join me!"
    mc "Really? I'll have to keep that in mind..."
    $ CharacterController.get_character("vs").add_point()
    return
label q_inter_vs_3:
    show expression cc.get_expression_image("vs", "ask01") as lth_vs_ask01
    play voice3 girl33_surprised_huh3 noloop
    vs "What's your favorite animal, [mcname]?"
    play voice2 mc_thinking_hmm7 noloop
    mc "Mmm. You know I swear I had one when I was younger, but I can't remember."
    vs "What? You should always have a favorite animal, no matter how old you are."
    play voice2 mc_surprised_why3 noloop
    mc "Why?"
    hide lth_vs_ask01
    show expression cc.get_expression_image("vs", "neutral01")
    play voice3 girl33_happy_laugh1 noloop
    vs "So whenever you have a bad day, you just imagine yourself as that animal and think of all the fun you'd be having."
    vs "I do it all the time!"
    $ CharacterController.get_character("vs").add_point()
    return
label q_inter_vs_4:
    show expression cc.get_expression_image("vs", "curious01")
    play voice3 girl33_hey_serious noloop
    vs "Hi, [mcname]. I relaly hope you're enjoying your time in the theater."
    vs "I know jumping into something new can be intimidating, but all you need to do is give it your best."
    vs "Everything else will work out. I just know it."
    play voice2 d2s9_confused noloop volume 1.7
    mc "Uh. Thanks, Veronica."
    vs "You got it."
    return
label q_inter_vs_5:
    show expression cc.get_expression_image("vs", "smile01")
    play voice3 girl33_happy_relief noloop
    vs "I really hope impress Denise the next time you get to audition, [mcname]."
    vs "Kai is great, but sometimes I think he gets a little nervous when we're playing as a couple."
    play voice2 mc_yes_yeah1 noloop
    mc "I'll do my best, Veronica."
    vs "Great!"
    return
label q_inter_vs_6:
    show expression cc.get_expression_image("vs", "neutral01")
    play voice3 girl33_thinking_hmm1 noloop
    vs "I think Sam really appreciates having you around to help him back stage, [mcname]."
    vs "Keep up the good work!"
    return
label q_inter_vs_7:
    show expression cc.get_expression_image("vs", "excited01") as lth_vs_excited01
    play voice3 girl33_hey_scared noloop
    vs "*whipsers* Hey [mcname]."
    play voice2 mc_hey_hey6 noloop
    mc "*whispers* Hey Veronica. Why are we whispering?"
    vs "*whispers* Because it's fun, and becauase you want to keep talk about FL on the downlow right?"
    mc "*whispers* Yes."
    hide lth_vs_excited01
    show expression cc.get_expression_image("vs", "ask01")
    play voice3 girl33_thinking_hmm2 noloop
    vs "I have a question."
    play voice2 mc_yes_aga2 noloop
    mc "Go for it."
    vs "What do you miss the most about Fetish Locator?"
    mc "Mmm. Probably the blitz challenges. Those were a lot of fun."
    vs "Ah... I'm so jealous. I never got to do one before the app shut down."
    $ CharacterController.get_character("vs").add_point()
    return
label q_inter_vs_8:
    show expression cc.get_expression_image("vs", "sad01")
    play voice3 girl33_thinking_hmm1 noloop
    vs "Mmm. Since we're secret buddies, maybe I should tell you a secret about me."
    play voice2 mc_scared_oh4 noloop
    mc "Oooh. What did you have in mind."
    vs "I don't know. I don't normally keep secrets. Hmmm. I'll have to think about it."
    return
label q_inter_vs_9:
    show expression cc.get_expression_image("vs", "curious01")
    play voice3 girl33_happy_relief noloop
    vs "That stuff in the dressing room was a lot of fun."
    vs "Our little secret."
    $ CharacterController.get_character("vs").add_point()
    return
label q_inter_vs_10:
    show expression cc.get_expression_image("vs", "smile01") as lth_vs_smile
    play voice3 girl33_thinking_hmm3 noloop
    vs "When I make it big, maybe I can have you be my assistant."
    vs "Then we can still do sneaky stuff now and then."
    play voice2 mc_thinking_oh1 noloop
    mc "Not the worst career path I've tried."
    hide lth_vs_smile
    show expression cc.get_expression_image("vs", "laugh01")
    play voice3 girl33_arrogant_laugh noloop
    vs "Hehe."
    $ CharacterController.get_character("vs").add_point()
    return
label q_inter_vs_11:
    show expression cc.get_expression_image("vs", "sad01")
    play voice3 girl33_thinking_hmm3 noloop
    vs "I've been thinking about your taste when I think about the alarm going off."
    vs "Bubblegum likes gum, but I think she likes your cum better. *giggles*"
    $ CharacterController.get_character("vs").add_point()
    return