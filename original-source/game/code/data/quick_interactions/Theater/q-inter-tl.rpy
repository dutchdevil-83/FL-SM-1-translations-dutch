init 3 python:
    CharacterController.get_character("tl").interactions = [
            {LABEL: "q_inter_tl_1", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_tl_2", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_tl_3", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_tl_4", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_tl_5", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_tl_6", LOCATIONS: [THEATER], AFTER_SCENE: [TL_STORY, "sm1cs_tl002"]},
            {LABEL: "q_inter_tl_7", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_tl_8", LOCATIONS: [GR_BAR], AFTER_SCENE: [TL_STORY, "sm1cs_tl004"]},
            {LABEL: "q_inter_tl_9", LOCATIONS: [GR_BAR], AFTER_SCENE: [TL_STORY, "sm1cs_tl004"]},
            {LABEL: "q_inter_tl_10", LOCATIONS: [GR_BAR], AFTER_SCENE: [TL_STORY, "sm1cs_tl006"]},
            {LABEL: "q_inter_tl_11", LOCATIONS: [GR_BAR], AFTER_SCENE: [TL_STORY, "sm1cs_tl005"]},
            {LABEL: "q_inter_tl_12", LOCATIONS: [GR_BAR], AFTER_SCENE: [TL_STORY, "sm1cs_tl004"]},
            {LABEL: "q_inter_tl_13", LOCATIONS: [STUDIO], AFTER_SCENE: [TL_STORY, "sm1cs_tl007"]},
            {LABEL: "q_inter_tl_14", LOCATIONS: [STUDIO], AFTER_SCENE: [TL_STORY, "sm1cs_tl007"]},
            {LABEL: "q_inter_tl_15", LOCATIONS: [STUDIO], AFTER_SCENE: [TL_STORY, "sm1cs_tl007"]},
            {LABEL: "q_inter_tl_16", LOCATIONS: [STUDIO], AFTER_SCENE: [TL_STORY, "sm1cs_tl007"]},
            {LABEL: "q_inter_tl_17", LOCATIONS: [STUDIO], AFTER_SCENE: [TL_STORY, "sm1cs_tl007"]},
            {LABEL: "q_inter_tl_18", AFTER_SCENE: [TL_STORY, "sm1cs_tl007"]},
            {LABEL: "q_inter_tl_19", AFTER_SCENE: [TL_STORY, "sm1cs_tl007"]},
            {LABEL: "q_inter_tl_20", AFTER_SCENE: [TL_STORY, "sm1cs_tl007"]},
            ]
    CharacterController.get_character("tl").default_expression = "serious01"

label q_inter_tl_1:
    show expression cc.get_expression_image("tl", "curious01")
    play voice2 mc_hey_hey7 noloop
    mc "Hey, Taisia."
    play voice3 girl24_thinking_ah noloop
    tl "Oh, what's up."
    return
label q_inter_tl_2:
    show expression cc.get_expression_image("tl", "annoyed01")
    play voice2 mc_hey_hey10 noloop
    mc "Wazzzzuuuuup!"
    tl "..."
    play voice2 d2s9_confused noloop
    mc "You know, like that one video?"
    tl "..."
    play voice3 girl24_disappointed_eeh2 noloop
    tl "Sometimes, I can't believe we had sex."
    return
label q_inter_tl_3:
    show expression cc.get_expression_image("tl", "ask01")
    play voice3 girl24_arrogant_huh2 noloop
    tl "So, when are we filming next?"
    play voice2 mc_yes_yeah3 noloop
    mc "Soon, just need to get a few more things figured out."
    return
label q_inter_tl_4:
    show expression cc.get_expression_image("tl", "depressed01")
    play voice3 girl24_disappointed_eeh1 noloop
    tl "To, like, be. Or, like, not to."
    play voice2 d2s12_emmm noloop
    mc "What are you doing?"
    tl "What does it look like I'm doing?"
    mc "Talking to yourself."
    tl "..."
    $ CharacterController.get_character("tl").add_point()
    return
label q_inter_tl_5:
    show expression cc.get_expression_image("tl", "sad01")
    play voice3 girl24_disappointed_hmf noloop
    tl "If i get 8 hours at the other job... And I save, what, half of that paycheck..."
    return
label q_inter_tl_6:
    show expression cc.get_expression_image("tl", "curious01")
    play voice2 d2s9_mchey noloop
    mc "Hey, would you be able to teach me some stuff about cars, sometime?"
    play voice3 girl24_surprised_huh3 noloop
    tl "You want to learn about cars?"
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Yeah, kind of. You seem to like cars, and I think you're cool, so..."
    play voice3 girl24_yes_yeah noloop
    tl "Yeah, [mcname], I can show you some car stuff."
    $ CharacterController.get_character("tl").add_point()
    return
label q_inter_tl_7:
    show expression cc.get_expression_image("tl", "curious01") as lth_tl_curious01
    play voice3 girl24_hey_greeting noloop
    tl "Hey, for our next scene, can I help write the script?"
    play voice2 d2s9_confused noloop volume 1.6
    mc "Uhm, sure! Any reason why?"
    hide lth_tl_curious01
    show expression cc.get_expression_image("tl", "depressed01") as lth_tl_depressed01
    play voice3 girl24_disappointed_neh noloop
    tl "Well... There were a shit ton of driving sex puns."
    play voice2 mc_surprised_what2 noloop
    mc "What, you didn't like those?"
    tl "No, they were fine... We might just want like 20 percent less of them."
    mc "Awe, man... But yeah, you can help."
    hide lth_tl_depressed01
    show expression cc.get_expression_image("tl", "laugh01")
    play voice3 girl24_arrogant_hah noloop
    tl "Sick."
    $ CharacterController.get_character("tl").add_point()
    return
label q_inter_tl_8:
    show expression cc.get_expression_image("tl", "sad01")
    play voice3 girl24_disappointed_hmf noloop
    tl "Not right now, [mcname], I'm drinking."
    return
label q_inter_tl_9:
    show expression cc.get_expression_image("tl", "smile01")
    play voice3 girl24_hey_simple noloop
    tl "Hey, what's up?"
    play voice2 mc_thinking_hm noloop
    mc "You know, just checking things out."
    tl "Cool. Cool, cool, cool."
    return
label q_inter_tl_10:
    show expression cc.get_expression_image("tl", "serious01") as lgr_tl_serious01
    play voice3 girl24_hey_angry noloop
    tl "You still owe me another game of pool."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, I haven't forgotten."
    hide lgr_tl_serious01
    show expression cc.get_expression_image("tl", "smile01")
    play voice3 girl24_yes_ugu noloop
    tl "Looking forward to it."
    return
label q_inter_tl_11:
    show expression cc.get_expression_image("tl", "smile01") as lgr_tl_smile01
    play voice3 girl24_surprised_huh4 noloop
    tl "Did you know there used to be a fight club here?"
    play voice2 mc_surprised_what2 noloop
    mc "What? No way."
    tl "Yeah."
    mc "How have I never heard about this?"
    hide lgr_tl_smile01
    show expression cc.get_expression_image("tl", "ask01")
    play voice3 girl24_disappointed_neh noloop
    tl "Don't know. But I'm not surprsied."
    return
label q_inter_tl_12:
    show expression cc.get_expression_image("tl", "ask01") as lgr_tl_ask
    play voice3 girl24_surprised_eeh2 noloop
    tl "Not going to lie, every time I see you here, I'm a little surprised."
    play voice2 mc_surprised_why2 noloop
    mc "Why's that?"
    tl "This just doesn't seem like the place you would drink."
    mc "Well, I'm full of surprises."
    hide lgr_tl_ask
    show expression cc.get_expression_image("tl", "smile01")
    play voice3 girl24_sex_closedmoan1 noloop
    tl "That you are..."
    $ CharacterController.get_character("tl").add_point()
    return
label q_inter_tl_13:
    show expression cc.get_expression_image("tl", "smile01")
    play voice3 girl24_arrogant_huh2 noloop
    tl "This is a pretty nice spot, [mcname]."
    play voice2 mc_happy_yay1 noloop
    mc "Thanks! I'm glad you like it."
    tl "Mmhmmmm."
    return
label q_inter_tl_14:
    show expression cc.get_expression_image("tl", "serious01") as lgr_tl_serious01
    play voice2 d2s9_confused noloop
    mc "So, cars?"
    play voice3 girl24_yes_yeah noloop
    tl "Yeah, cars."
    mc "I didn't realize you liked them so much."
    hide lgr_tl_serious01
    show expression cc.get_expression_image("tl", "ask01")
    play voice3 girl24_thinking_emm1 noloop
    tl "Remember that time we made a whole ass porno in a car?"
    play voice2 mc_scared_oh1 noloop
    mc "Oh yeaaaaa."
    tl "Yeah, that was like a dream of mine. It was fucking great."
    return
label q_inter_tl_15:
    show expression cc.get_expression_image("tl", "serious01") as lgr_tl_serious01
    play voice2 mc_surprised_uh2 noloop
    mc "What's the story with the mask?"
    play voice3 girl24_disappointed_ohh1 noloop
    tl "It's spooky."
    mc "..."
    mc "That's it?"
    tl "Pretty much."
    mc "Come on, there has to be more of a story to it than that."
    hide lgr_tl_serious01
    show expression cc.get_expression_image("tl", "sad01")
    play voice3 girl24_disappointed_eeh2 noloop
    tl "Ugh...{w} That was the first, like, costume piece I ever bought. I wore it for this music video thing I helped a guy with, years ago."
    play voice2 mc_surprised_oh3 noloop
    mc "Really? That's kind of cool."
    tl "Yeah, it kind of was."
    return
label q_inter_tl_16:
    show expression cc.get_expression_image("tl", "serious01") as lgr_tl_serious01
    play voice2 mc_surprised_uh3 noloop
    mc "You have a stuffed animal?"
    hide lgr_tl_serious01
    show expression cc.get_expression_image("tl", "annoyed01")
    play voice3 girl24_hey_angry noloop
    tl "You better shut the fuck up about it."
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, I didn't-"
    tl "I'm not going to talk about it, [mcname]. Drop it."
    mc "Okaaaaay."
    play voice3 girl24_angry_cough1 noloop
    tl "Even better, forget you ever saw it."
    play voice2 mc_yes_yes2 noloop
    mc "Not a problem, Taisia."
    $ CharacterController.get_character("tl").add_point()
    return
label q_inter_tl_17:
    show expression cc.get_expression_image("tl", "serious01") as lgr_tl_serious01
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Is the red balloon because of the clown?"
    play voice3 girl24_yes_aga noloop
    tl "Uh huh."
    mc "I never really asked... what is it with you and clowns?"
    tl "I don't know. Some people are scared of them, some people love them, some people want to fuck 'em."
    hide lgr_tl_serious01
    show expression cc.get_expression_image("tl", "curious01")
    play voice3 girl24_thinking_hmm4 noloop
    tl "And I think it's cool that you can do so much with one character."
    play voice2 mc_arrogant_heh1 noloop
    mc "Huh, I never thuoght about it like that."
    tl "You're trying to tell me you've never wanted to fuck a clown?"
    mc "Well, I didn't say that."
    tl "That's what I thought."
    $ CharacterController.get_character("tl").add_point()
    return
label q_inter_tl_18:
    show expression cc.get_expression_image("tl", "smile01")
    play voice3 girl24_hey_greeting noloop
    tl "'Sup, roomie."
    play voice2 mc_happy_yay2 noloop
    mc "Hey, Taisia."
    return
label q_inter_tl_19:
    show expression cc.get_expression_image("tl", "serious01")
    play voice3 girl24_thinking_hmm1 noloop
    tl "I think I need to get a car."
    play voice2 mc_yes_yeah8 noloop
    mc "Oh yeah?"
    tl "Yeah. I think I just need a project or something. I don't know."
    return
label q_inter_tl_20:
    show expression cc.get_expression_image("tl", "smile01")
    play voice3 girl24_hey_sexy noloop
    tl "Yo, just so you know, there was a leak in the kitchen. But I fixed it."
    play voice2 mc_disappointed_off2 noloop
    mc "Oh shit, thanks Taisia!"
    tl "It might start leaking again. You might need to get a new part to really fix it."
    mc "Good to know... I guess we'll deal with that if it becomes a problem."
    tl "Cool."
    $ CharacterController.get_character("tl").add_point()
    return
label q_inter_tl_21:
    show expression cc.get_expression_image("tl", "serious01")
    play voice2 d2s9_mchey noloop
    mc "Hey, were you throwing like a party or something last night?"
    play voice3 girl24_no_questioning noloop
    tl "No. Why?"
    play voice2 mc_thinking_mmm4 noloop
    mc "It was just... super loud up in your room."
    play voice3 girl24_yes_yeah noloop
    tl "Oh, yeah. I was just masturbating loudly. And I blast some music so it's not awkward for everyone."
    mc "Oh..."
    $ CharacterController.get_character("tl").add_point()
    return