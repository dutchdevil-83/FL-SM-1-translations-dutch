label sm1cs_tl002i:
    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "excited01") as lth_tl_excited01
    play voice3 girl24_hey_greeting noloop
    tl "'Sup, [mcname]?"
    hide lth_tl_excited01
    scene sm1cs-tl002-01 mc-tl-talk1_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Hey Taisia... So, uhm..."
    scene sm1cs-tl002-02 mc-tl-talk2_c2 with dissolve
    play voice3 girl24_thinking_huh1 noloop
    tl "You make any progress on the movie stuff?"
    scene sm1cs-tl002-03 mc-tl-talk3_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "That's actually what I wanted to talk to you about."
    scene sm1cs-tl002-03 mc-tl-talk3_c2 with dissolve
    play voice3 girl24_yes_yeah noloop
    tl "Yeah?"
    scene sm1cs-tl002-04 mc-tl-talk4_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "I'm... Coming up with nothing."
    scene sm1cs-tl002-04 mc-tl-talk4_c2 with dissolve
    play voice3 girl24_arrogant_huh2 noloop
    tl "... I should take that other job..."
    scene sm1cs-tl002-05 mc-tl-talk5_c1 with dissolve
    play voice2 mc_thinking_wait2 noloop
    mc "Wait! I think that I'm struggling with the fact that I don't really know a whole lot about you. I mean, some of the kink stuff, but not like your {i}vibe{/i}, you know?"
    scene sm1cs-tl002-05 mc-tl-talk5_c2 with dissolve
    play voice3 girl24_arrogant_hah noloop
    tl "It's a Hatichi wand."
    scene sm1cs-tl002-06 mc-tl-talk6_c1 with dissolve
    play voice2 mc_no_no6 noloop
    mc "No, not that kind of a vibe. I mean, what would be a good film for you, and what we would do, and a theme, and-"
    scene sm1cs-tl002-06 mc-tl-talk6_c2 with dissolve
    play voice3 girl24_arrogant_kgh1 noloop
    tl "Fucking creatives, I swear."
    scene sm1cs-tl002-05 mc-tl-talk5_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Look, all I'm suggesting is that we hang out and maybe something will come to me, you know?"
    scene sm1cs-tl002-05 mc-tl-talk5_c2 with dissolve
    play voice3 girl24_yes_aga noloop
    tl "Sure. Fine. Whatever. What do you want to do?"
    play voice2 d3s7_mcemm noloop volume 1.3
    mc "Uh..."
    mct "I didn't think this far ahead..."
    mc "Sex shop?"
    play voice3 girl24_surprised_what2 noloop
    tl "You want to bring me to a sex shop?"
    scene sm1cs-tl002-06 mc-tl-talk6_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah. It'll be a work trip."
    scene sm1cs-tl002-06 mc-tl-talk6_c2 with dissolve
    tl "..."
    play voice3 girl24_yes_ugu noloop
    tl "Kinky, I like it. Let's go."
    $ StoryController.end_scene(TL_STORY, 0, 15, 0)
    return