label sm1cs_vs002i:
    $ LocationController.draw_current_location("vs")
    show expression cc.get_expression_image("vs", "neutral01") as lth_vs_neutral01
    play voice2 mc_hey_hey5 noloop
    mc "What do you got there, Veronica?"
    play voice3 girl33_thinking_hmm1 noloop
    vs "Just the latest issue of {u}Stars Weekly{/u}."
    vs "The comprehensive guide to everything happening in Hollywood."
    menu:
        "Looks cool"(hint="sm1cs_vs002i_m01_h01"):
            call sm1cs_vs002i_m01_c01 from _call_sm1cs_vs002i_m01_c01
            play voice2 mc_thinking_oh1 noloop
            mc "Looks interesting."
            hide lth_vs_neutral01
            show expression cc.get_expression_image("vs", "excited01") as lth_vs_excited01
            play voice3 girl33_yes_happy noloop
            vs "It's the best. It keeps me up to date on all the news about upcoming films and new trends."
            vs "With this magazine, I can keep my knowledge as sharp as my nails and be ready to make a splash when I burst onto the scene."
            play voice2 mc_thinking_mmm6 noloop
            mc "I thought that working here would give me all I need to eventually become a great actor."
            hide lth_vs_excited01
            show expression cc.get_expression_image("vs", "smile01") as lth_vs_smile01
            play voice3 girl33_no_unsure noloop
            vs "That's where you're wrong, [mcname]."
            hide lth_vs_smile01
        "Why are you reading that?"(hint="sm1cs_vs002i_m01_h02"):
            hide lth_vs_neutral01
            show expression cc.get_expression_image("vs", "annoyed01") as lth_vs_annoyed01
            play voice3 girl33_surprised_huh4 noloop
            vs "Uh, are you telling me you've never read {u}Stars Weekly{/u}?"
            play voice2 mc_thinking_emm1 noloop
            mc "Ummm. I'm more into comics."
            vs "*gasps* You're serious, aren't you?"
            hide lth_vs_annoyed01
            show expression cc.get_expression_image("vs", "serious01") as lth_vs_serious01
            play voice3 girl33_arrogant_hm noloop
            vs "[mcname], how are you ever going to become a great star on the stage if you don't keep up to date on how to become a movie star?"
            play voice2 d1s5b_ehhh noloop
            mc "I guess I was thinking it's just a matter of luck."
            vs "Luck by your side is good, but you've got to learn how the industry works if you ever want to survive in it."
            hide lth_vs_serious01
    show expression cc.get_expression_image("vs", "curious01") as lth_vs_curious01
    play voice3 girl33_arrogant_he noloop
    if True:
        vs "You'll never succeed if you just come here to work backstage."
    else:
        vs "You'll never succeed if all you do is just come in and rehearse."
    play voice2 mc_thinking_hmm7 noloop
    mc "What do I need to do?"
    hide lth_vs_curious01
    show expression cc.get_expression_image("vs", "smile01") as lth_vs_smile01
    play voice3 girl33_happy_laugh1 noloop
    vs "Find magazines like {u}Stars Weekly{/u} and read them from cover to ass."
    vs "They'll keep you up to date with movies and stars, and give you plenty of advice and tips."
    vs "I learned more than half of what I know from this magazine."
    play voice2 mc_yes_okay3 noloop
    mc "Nice. Any chance I can borrow it when I'm done?"
    hide lth_vs_smile01
    show expression cc.get_expression_image("vs", "neutral01") as lth_vs_neutral01
    play voice3 girl33_angry_mfhmm noloop
    vs "As if. Come on, you can find your own. Any shop that is not a complete disaster will have a copy or two."
    mc "Cool, I might just check it out."
    jump sm1cs_vs002i_end
label sm1cs_vs002i_end:
    $ StoryController.end_scene(VS_STORY, 0, 15, 0)
    return
label sm1cs_vs002i_m01_c01:
    $ player.set_choice("sm1cs_vs002i_looks_cool")
    return