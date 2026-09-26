label sm1cs_kv004_1i:
    $ LocationController.draw_current_location("kv")
    if player.get_choice("sm1cs_kv004_practice_skills") is False:
        $ player.set_choice("sm1cs_kv004_01i_rejoined")
        show expression cc.get_expression_image("kv", "sad01") as lpd_dc_sad1
        play voice3 kanya_hey_simple1 noloop
        kv "Hey, [mcname]."
        play voice2 mc_hey_hey5 noloop
        mc "Hey, Kanya! I wanted to talk to you about something."
        hide lpd_dc_sad1
        show expression cc.get_expression_image("kv", "neutral01") as lpd_dc_neutral1
        play voice3 kanya_thinking_hmm3 noloop
        kv "What's up?"
        play voice2 d1s5_mchappy noloop volume 1.7
        mc "You know how you offered to help my practice some of my camera skills?"
        hide lpd_dc_neutral1
        show expression cc.get_expression_image("kv", "smile01") as lpd_dc_smile1
        play voice3 kanya_yes_yeah5 noloop
        kv "Yeah?"
        play voice2 d3s11b_mcheh noloop volume 1.67
        mc "Well I'm thinking that practice {i}does{/i} make perfect..."
        kv "Yeah!?"
        mc "And I was wondering if-"
        hide lpd_dc_smile1
        show expression cc.get_expression_image("kv", "smile02") as lpd_dc_smile2
        play voice3 kanya_surprised_oh noloop
        kv "Oh I don't have another client for hours! Come here!"
    else:
        show expression cc.get_expression_image("kv", "neutral01") as lpd_dc_neutral1
        play voice3 kanya_hey_simple1 noloop
        kv "'Sup, [mcname]."
        play voice2 mc_hey_hey5 noloop
        mc "Hey, Kanya. I was wondering if you have some free time right now?"
        kv "Yeah, I got some. What's up?"
        mc "Well I've been thinking that my camera skills could use some work..."
        hide lpd_dc_neutral1
        show expression cc.get_expression_image("kv", "smile02") as lpd_dc_smile2
        play voice3 kanya_surprised_oh noloop
        kv "Oh yeah?"
        play voice2 d3s11b_mcheh noloop volume 1.67
        mc "And I was wondering if you wanted to help me practice?"
        kv "Hell yeah I do, let's do it!"
    jump sm1cs_kv004_sex_repeatable