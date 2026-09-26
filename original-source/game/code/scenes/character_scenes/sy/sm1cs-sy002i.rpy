label sm1cs_sy002i:
    $ LocationController.draw_current_location("sy")
    if not player.has_played_scene("sm1cs_sy002"):
        jump sm1cs_sy002i_first_time
    show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
    play voice3 stacy_angry noloop
    sy "You know, [mcname], our little park scene was a ton of fun."
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, I enjoyed practicing our \"acting skills\"."
    hide lst_sy_naughty01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_arrogant_hmm1 noloop
    sy "How would you feel about going to \"practice\" our skills, my little thespian?"
    play voice2 mc_yes_sure1 noloop
    mc "Lead the way!"
    jump sm1cs_sy002_2
label sm1cs_sy002i_first_time:
    if player.get_choice("sm1ms_renovation_started") and not player.get_choice("sm1ms_renovation_completed"):
        show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
        play voice2 mc_thinking_hmm1 noloop
        mc "You know, this place is going to be amazing once it's done. But..."
        mc "I wish we could film something right now. Could definitely use the money to help pay for the renovation."
        play voice3 stacy_yes_yeah1 noloop
        sy "Yeah, I know. All the dust and paint doesn't scream 'high quality porn'."
        hide lst_sy_smile01
        show expression cc.get_expression_image("sy", "smile02") as lst_sy_smile02
        play voice3 stacy_thinking_hmm1 noloop
        sy "Which is why we need to get creative."
        play voice2 d1s2_hmm noloop volume 1.6
        mc "Creative, huh? Any brilliant ideas?"
        sy "Well, I think we've talked about shooting on location before."
        mc "Like, out in public?"
        sy "Yeah, there are plenty of places around town we could use as sets. Parks, alleys, rooftops..."
        hide lst_sy_smile02
        show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
        play voice3 stacy_happy_laugh1 noloop
        sy "You know I love the fucking somewhere unexpected."
        play voice2 mc_yes_yes4 noloop
        mc "I do love some light exhibitionism... okay, why don't we try the park?"
        sy "Yay! Let's go check it out!"
    else:
        hide lst_sy_neutral01
        show expression cc.get_expression_image("sy", "excited01") as lst_sy_neutral01
        play voice3 stacy_hey_happy1 noloop
        sy "Hey, [mcname]!"
        play voice2 mc_happy_yay2 noloop
        mc "Hey, Stacy. What's up?"
        sy "I had an iddeeeeaaaaaa!"
        mc "Oh yeah? And what is it?"
        sy "What if we expanded our locations?"
        mc "What do you mean?"
        hide lst_sy_neutral01
        show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
        play voice3 stacy_thinking_emm3 noloop
        sy "You know, we've only ever really planned to film in the studio."
        if player.has_played_scene("sm1cs_tl003"):
            sy "Except that one time with Taisia."
        sy "But what if we had other places we could shoot?"
        play voice2 d1s2_hmm noloop volume 1.7
        mc "Like where?"
        hide lst_sy_naughty01
        show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
        play voice3 stacy_thinking_hm1 noloop
        sy "Let me show you."
        mct "Oh boy... here we go."
    jump sm1cs_sy002