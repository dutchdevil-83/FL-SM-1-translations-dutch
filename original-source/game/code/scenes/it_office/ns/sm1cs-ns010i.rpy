label sm1cs_ns010i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_thinking_mmm4 noloop
    mc "I've been thinking. Something has come up with my friend Nari at work."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_thinking_oh2 noloop
    sy "Ooooh, are things getting spicy with her?"
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
    play voice3 stacy_happy_laugh1 noloop
    sy "Have you two done some {i}overtime{/i} in a cubicle yet?"
    play voice2 mc_surprised_what1 noloop
    mc "What? No. We don't have cubicles."
    mc "But I guess you could say we have fooled around at the office once or twice."
    hide lst_sy_naughty01
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    play voice3 stacy_happy_laugh4 noloop
    sy "*giggles* You dog. I knew you'd loosen her up."
    play voice2 mc_yes_aga2 noloop
    mc "That's part of what I wanted to talk to you about."
    mc "You remember I told you that Nari left her family behind in South Korea to build her career here."
    hide lst_sy_laugh01
    show expression cc.get_expression_image("sy", "neutral02") as lst_sy_neutral02
    play voice3 stacy_yes_yap3 noloop
    sy "Totally. I was really impressed hearing how far she's come."
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. But there is a problem now."
    mc "She's had a problem with her landlord. He tried to guilt trip her into staying when she mentioned she would start looking for her own place."
    mc "So she had to leave her current place behind and has been living at the Orbix office."
    hide lst_sy_neutral02
    show expression cc.get_expression_image("sy", "sad01") as lst_sy_sad01
    play voice3 stacy_disappointed_oh1 noloop
    sy "That's terrible."
    play voice2 mc_yes_yeah2 noloop
    mc "Yup. But then I realized something that maybe she can come and stay with us."
    hide lst_sy_sad01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_arrogant_huh2 noloop
    sy "Here?"
    if persistent.is_special:
        sy "Hmmm. How well do you know this girl, bro?"
    else:
        sy "Hmmm. How well do you know this girl?"
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Pretty good. She's hard-working, cute and eager."
    mc "And I should mention, super kinky."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "naughty01") as lst_sy_naughty01
    play voice3 stacy_happy_laugh2 noloop
    sy "Haha. I see what's going on."
    sy "You're thinking she might be a candidate to join the studio one day."
    play voice2 mc_happy_yes1 noloop
    mc "Totally. She's super friendly and pretty damn kinky too."
    hide lst_sy_naughty01
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    play voice3 stacy_happy_yay2 noloop
    sy "Hahah. Nice."
    hide lst_sy_laugh01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_thinking_emm4 noloop
    sy "So does she know you're looking for people to join our studio?"
    play voice2 mc_no_no1 noloop
    mc "Not yet. I haven't figured out the right time."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "curious01") as lst_sy_curious01
    play voice3 stacy_thinking_hmm1 noloop
    sy "Well sooner is probably going to be better than later. Especially if she is living with us."
    sy "She's bound to figure things out on her own."
    play voice2 mc_thinking_wait1 noloop
    mc "I know. Wait, does that mean I can invite her over?"
    hide lst_sy_curious01
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    play voice3 stacy_laugh4 noloop
    sy "*giggles* Yes, you can invite her to stay with us."
    if player.get_choice("sm1ms_renovation_completed"):
        hide lst_sy_laugh01
        show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
        play voice3 stacy_hmm noloop
        sy "It's a good thing we got the place fixed up. If you asked me earlier, we wouldn't have really had any space that gives her privacy."
        play voice2 mc_arrogant_heh3 noloop
        mc "I think she would have been okay with that, heh."
        hide lst_sy_excited01
        show expression cc.get_expression_image("sy", "neutral02") as lst_sy_neutral02
        play voice3 stacy_hey noloop
        sy "But I still need to meet her first."
    else:
        hide lst_sy_laugh01
        show expression cc.get_expression_image("sy", "ask01") as lst_sy_ask01
        play voice3 stacy_hmm noloop
        sy "There is one thing. Even if I meet her and she's cool, she can't really come over just yet?"
        play voice2 mc_surprised_why3 noloop
        mc "Why not?"
        sy "I mean, the place is fine for us, but if we're going to have other people staying here, we really should spruce it up a bit."
        hide lst_sy_ask01
        show expression cc.get_expression_image("sy", "neutral02") as lst_sy_neutral02
        play voice3 stacy_hey noloop
        sy "And we always wanted to make it nicer to it would be a better place to film at."
        mc "That's a good point."
    mc "Wait, back up. You want to meet her before I invite her?"
    if persistent.is_special:
        hide lst_sy_neutral02
        show expression cc.get_expression_image("sy", "smile02") as lst_sy_smile02
        play voice3 stacy_yes_yap2 noloop
        sy "Yup. I mean this girl is dating my brother. I have to take a long look at her and make sure she's not just using you or planning to make your life a living hell."
        sy "It's the sisterly thing to do."
    else:
        hide lst_sy_neutral02
        show expression cc.get_expression_image("sy", "smile02") as lst_sy_smile02
        play voice3 stacy_arrogant_ha2 noloop
        sy "Haha. I'm your partner, [mcname]. If someone is going to come live with us, I couldn't live with myself if I didn't check her out head to toe to make sure she's good enough for you."
    mc "Yeah, that makes sense."
    hide lst_sy_smile02
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_arrogant_hmm3 noloop
    sy "Good. So why don't you set up a meeting sometime in the afternoon so the three of us can meet in person?"
    play voice2 mc_yes_sure1 noloop
    mc "Great. And... thanks. Not everyone would be so cool to have another girl joining us."
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_thinking_emm2 noloop
    sy "Well, it's kind of always been the plan. And besides, I've known from the first time we really shared our feelings that I wasn't going to be the only girl for you."
    play voice2 d9s2_yeah noloop volume 2.0
    mc "Yeah, but you know you'll always come first."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_laugh noloop
    sy "Hehehe. That's good to hear."
    $ StoryController.end_scene(NS_STORY, 0, 15, 0)
    return