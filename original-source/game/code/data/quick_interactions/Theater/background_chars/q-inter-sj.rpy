init 3 python:
    CharacterController.get_character("sj").interactions = [
            {LABEL: "q_inter_sj_1", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_sj_2", LOCATIONS: [THEATER]},
            {LABEL: "q_inter_sj_3", LOCATIONS: [THEATER]},
            ]
    CharacterController.get_character("sj").default_expression = "neutral01"

label q_inter_sj_1:
    show expression cc.get_expression_image("sj", "neutral01") as lth_sj_neutral01
    play voice2 d2s9_mchey noloop
    mc "Hello Sue."
    play voice3 girl35_hey_greeting noloop
    sj "Hey [mcname]."
    mc "I was thinking about something I wanted to ask you. If you have a moment."
    sj "Sure."
    mc "I was wondering if you used to act on the stage. Or if you've always just been a fixer for the group?"
    hide lth_sj_neutral01
    show expression cc.get_expression_image("sj", "smile01") as lth_sj_smile01
    play voice3 girl35_happy_laugh1 noloop
    sj "Hahaha."
    play voice2 mc_arrogant_huh1 noloop
    mc "What did I say?"
    sj "Nothing. I just imagined me on stage. Denise would probably lose it."
    mc "You're that bad?"
    hide lth_sj_smile01
    show expression cc.get_expression_image("sj", "sad01")
    play voice3 girl35_yes_yeah1 noloop
    sj "Oh yeah. I tried when I was younger. But to this day I can't memorize a line or hold a note to save my life."
    sj "A life on the stage is just not in the cards for me. Of course I still love the theater, the presentation, all the people working together."
    sj "I'd love to work in movies as a producer one day, managing the stuff behind the scenes."
    sj "So for now, I keep the wheels from falling off around here. Stick around here long enough and you'll see that making a show run is a lot more than just people on stage."
    return
label q_inter_sj_2:
    show expression cc.get_expression_image("sj", "neutral01") as lth_sj_neutral01
    play voice2 d2s9_mchey noloop
    mc "How's it going, Sue?"
    play voice3 girl35_no_nah5 noloop
    sj "Not bad. Just taking a little breather, then I gotta go again."
    mc "I hope Denise isn't running you ragged?"
    hide lth_sj_neutral01
    show expression cc.get_expression_image("sj", "smile01")
    play voice3 girl35_arrogant_ha9 noloop
    sj "Hah. Nothing I can't handle. I was on the track in field team during college. I love a good run when the situation calls for it."
    play voice2 mc_thinking_hmm3 noloop
    mc "So you do this to work out?"
    sj "Little collum A, little collum B. Sometimes a show has an emergency and you need someone who can fix the problem in a flash."
    sj "And that's where I come in. Speaking of which, Bruce needs some shield polish. Catch you later, [mcname]."
    return
label q_inter_sj_3:
    show expression cc.get_expression_image("sj", "neutral01") as lth_sj_neutral01
    play voice2 mc_thinking_hmm4 noloop
    mc "How long have you been doing this, Sue?"
    play voice3 girl35_thinking_hmm1 noloop
    sj "I started halfway through getting my degree. Wanted to get some walking around money for a summer and when I was done, Denise begged me to stick around."
    mc "You must be really good at it."
    sj "Or I'm just good at interpreting her moods. She has as lot of them."
    mc "Can you tell me if she's in a bad mood? Might save me from getting yelled at if I mess up."
    hide lth_sj_neutral01
    show expression cc.get_expression_image("sj", "smile01")
    play voice3 girl35_happy_laugh2 noloop
    sj "Haha. I'll try but she sometimes she just needs to vent. It's nothing personal. She puts a lot of herself into her craft."
    play voice2 mc_yes_yeah8 noloop
    mc "And it doesn't stress you out?"
    sj "Not at all. If I ever end up working on movies, I'm sure I'll be dealing with people who make Denise look like a soft little kitty."
    return