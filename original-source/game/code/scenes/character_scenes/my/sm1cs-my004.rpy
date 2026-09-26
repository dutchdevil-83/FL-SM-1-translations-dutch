image sm1cs-my004-a26-glam = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a26-4x-60fps.webm", start_image = "sm1cs-my004-a26 my-swimsuit-glambot-00", image = "sm1cs-my004-a26 my-swimsuit-glambot-90", loop = False)
image sm1cs-my004-a32-glam = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a32-3x-60fps.webm", start_image = "sm1cs-my004-a32 my-sy-looking-at-mc-glambot-00", image = "sm1cs-my004-a32 my-sy-looking-at-mc-glambot-89", loop = False)
image sm1cs-my004-a72-glam = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a72-4x-60fps.webm", start_image = "sm1cs-my004-a72 mc-my-oil-glambot-00", image = "sm1cs-my004-a72 mc-my-oil-glambot-90", loop = False)
image sm1cs-my004-a78-1 = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-1-2x-50fps.webm", start_image = "sm1cs-my004-a78-1 mc-fondling-my-anim-01")
image sm1cs-my004-a78-1-f = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-1-2x-60fps.webm", start_image = "sm1cs-my004-a78-1 mc-fondling-my-anim-01")
image sm1cs-my004-a78-2 = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-2-2x-50fps.webm", start_image = "sm1cs-my004-a78-2 mc-fondling-my-anim-01")
image sm1cs-my004-a78-2-f = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-2-2x-60fps.webm", start_image = "sm1cs-my004-a78-2 mc-fondling-my-anim-01")
image sm1cs-my004-a78-3 = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-3-2x-50fps.webm", start_image = "sm1cs-my004-a78-3 mc-fondling-my-anim-01")
image sm1cs-my004-a78-3-f = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-3-2x-60fps.webm", start_image = "sm1cs-my004-a78-3 mc-fondling-my-anim-01")
image sm1cs-my004-a78-4 = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-4-2x-50fps.webm", start_image = "sm1cs-my004-a78-4 mc-fondling-my-anim-01")
image sm1cs-my004-a78-4-f = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-4-2x-60fps.webm", start_image = "sm1cs-my004-a78-4 mc-fondling-my-anim-01")
image sm1cs-my004-a78-5 = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-5-2x-50fps.webm", start_image = "sm1cs-my004-a78-5 mc-fondling-my-anim-01")
image sm1cs-my004-a78-5-f = Movie(play = "images/Character-Scenes/MY/s004/anim/sm1cs-my004-a78-5-2x-60fps.webm", start_image = "sm1cs-my004-a78-5 mc-fondling-my-anim-01")
label sm1cs_my004:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    scene black
    show screen scene_transistion(_("20 Minutes Later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_cloth_rustling2
    play sound4 sfx_clock_ticks_loop1 fadein 2.0 volume 0.5
    scene sm1cs-my004-01 mc-thinking_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    play voice2 d1s5_mcthinks noloop volume 1.5
    mct "Where the hell did Stacy go? She's been gone so long..."
    mct "Whatever she's planning, it's probably going to cause a whole mess of problems for me."
    scene sm1cs-my004-02 mc-talking_c1 with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "Sorry! I'll be right down!"
    play voice2 mc_yes_aga1 noloop
    mc "Uh huh! Sure you will!"
    sy "I promise!"
    scene sm1cs-my004-03 mc-rolling-his-eyes_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "Like I haven't heard that-"
    scene sm1cs-my004-04 mc-sy-confused_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Stacy? Why are you wearing a robe?"
    stop sound4 fadeout 7.0
    play music music_big_and_bigger
    scene sm1cs-my004-04 mc-sy-confused_c2 with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Oh, I just wanted to get comfy!"
    scene sm1cs-my004-05 mc-sy-talking_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "...{w} What are you planning?"
    scene sm1cs-my004-05 mc-sy-talking_c2 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Me? Nothing! I would never!"
    play sound sfx_barefoot_steps1 loop
    scene sm1cs-my004-06 mc-sy-walking-down_c1 with dissolve
    play voice2 mc_angry_off noloop
    mc "Bullshit."
    scene sm1cs-my004-06 mc-sy-walking-down_c2 with dissolve
    play voice3 stacy_no_nonono3 noloop
    sy "I would never!"
    play voice2 mc_thinking_hmm1 noloop
    scene sm1cs-my004-07 mc-sy-talking_c1 with dissolve
    if persistent.is_special:
        mc "You're my sister, I've known you my whole life. I know when you're lying."
    else:
        mc "Stacy, you're my best friend. I know when you're lying."
    scene sm1cs-my004-07 mc-sy-talking_c2 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Why would I lie to you?"
    play voice2 mc_thinking_hmm2 noloop
    mc "To bamboozle me."
    play sound sfx_cloth_rustling3 volume 1.6
    scene sm1cs-my004-08 mc-sy-talking_c1 with dissolve
    play voice3 stacy_ah noloop
    sy "Me!? Bamboozle!?!"
    if persistent.is_special:
        sy "My own brother! Calling me a bamboozler!"
    else:
        sy "My boyfriend! Calling me a bamboozler!"
    scene sm1cs-my004-08 mc-sy-talking_c2 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Stacy-"
    call knock from _call_knock_10
    scene sm1cs-my004-09 sy-jumping_c1 with dissolve
    play voice3 stacy_arrogant_huh5 noloop
    sy "I'll get it!"
    play sound sfx_cloth_rustling4
    play sound2 sfx_barefoot_steps1
    scene sm1cs-my004-10 mc-thinking_c1 with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "Oh God... here it comes..."
    play sound2 sfx_door_open1 noloop
    scene sm1cs-my004-11 sy-mc-my-hi-surprised_c1 with dissolve
    play voice3 stacy_hey_attention1 noloop
    if persistent.is_special:
        sy "Hey, Mom!"
    else:
        sy "Hey, Melony!"
    scene sm1cs-my004-11 sy-mc-my-hi-surprised_c2 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    if persistent.is_special:
        mct "Why the hell is Mom here?"
    else:
        mct "Why the hell did Stacy invite Melony over?"
    play sound sfx_door_closed1
    play sound2 sfx_heels_steps1
    scene sm1cs-my004-12 sy-mc-my-walking-in_c1 with dissolve
    play voice4 girl34_hey_simple1 noloop
    my "Hi, Stacy. Hi, [mcname]!"
    stop sound2 fadeout 1.0
    scene sm1cs-my004-13 sy-mc-my-talking_c2 with dissolve
    play voice4 girl34_angry_ahem2 noloop
    if persistent.is_special:
        my "I see you won't even get off the couch for your own mother!"
    else:
        my "What, can't get up and say hello to me?"
    play sound sfx_cloth_planket2
    scene sm1cs-my004-13 sy-mc-my-talking_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Sorry, I just wasn't expecting you to be coming over today. I'm just a little surprised is all."
    scene sm1cs-my004-14 sy-mc-my-talking-surprised_c1 with dissolve
    play voice4 girl34_surprised_ah1 noloop
    my "Oh? But I thought we had our contest today?"
    scene sm1cs-my004-14 sy-mc-my-talking-surprised_c2 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "The what now?"
    scene sm1cs-my004-14 sy-mc-my-talking-surprised_c1 with dissolve
    play voice4 girl34_thinking_eeh1 noloop
    my "The swimsuit contest. The one Stacy had mentioned at the bar. She said you were doing that today?"
    scene sm1cs-my004-14 sy-mc-my-talking-surprised_c3 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Yeah, [mcname]. Did you forget?"
    scene sm1cs-my004-15 sy-mc-elbowing_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "Forget... forget what?"
    play sound sfx_leg_kick8
    scene sm1cs-my004-15 sy-mc-elbowing_c2 with dissolve
    play voice3 stacy_arrogant_laugh1 noloop
    if persistent.is_special:
        sy "Classic older brother, can't even remember what day of the week it is!"
    else:
        sy "Classic [mcname]. Can't even remember what day of the week it is!"
    play voice2 mc_pain_auch1 noloop
    mc "Ouch!"
    scene sm1cs-my004-16 my-rolling-her-eyes_c1 with dissolve
    play voice4 girl34_disappointed_oh2 noloop
    my "Oh you two..."
    scene sm1cs-my004-17 mc-my-sy-talking_c1 with dissolve
    play voice4 girl34_disappointed_mmf4 noloop
    my "Well, if you have space for one more contestant, I brought my swimsuit with me."
    scene sm1cs-my004-17 mc-my-sy-talking_c2 with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "Of course we do! Right, [mcname]?"
    scene sm1cs-my004-17 mc-my-sy-talking_c3 with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Uhm... right?"
    scene sm1cs-my004-18 my-sy-talking_c2 with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "Feel free to get dressed in the bathroom!"
    play voice4 girl34_surprised_huh5 noloop
    my "What about you?"
    play sound sfx_cloth_planket3 volume 0.6
    scene sm1cs-my004-19 my-sy-dropping-the-suit_c1 with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh, I got changed before you got here!"
    scene sm1cs-my004-19 my-sy-dropping-the-suit_c2 with dissolve
    play voice2 mc_angry_errr8 noloop
    mct "So that's what she was doing..."
    scene sm1cs-my004-19 my-sy-dropping-the-suit_c3 with dissolve
    play voice4 girl34_yes_aga2 noloop
    my "All right... give me a second, I'll be right back."
    play sound2 sfx_heels_steps1
    scene sm1cs-my004-20 my-sy-going-to-the-bathroom_c1 with dissolve
    play voice3 stacy_yes_fine4 noloop
    sy "Take your time!"
    stop sound2 fadeout 2.0
    scene sm1cs-my004-21 mc-sy-talking_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "What the hell are you doing, Stacy?"
    scene sm1cs-my004-21 mc-sy-talking_c2 with dissolve
    play voice3 stacy_disgust_meh1 noloop
    sy "You're taking sooooo long! I want to skip ahead to the juicy parts."
    scene sm1cs-my004-22 mc-sy-surprised-teasing_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "The juicy parts of?"
    scene sm1cs-my004-22 mc-sy-surprised-teasing_c2 with dissolve
    play voice3 stacy_moan4 noloop
    if persistent.is_special:
        sy "You know, Mom's tits wrapped around your cock?"
    else:
        sy "You know, Melony's tits wrapped around your cock?"
    sy "Those puppies are real juicy... God, I wish I had tits like that."
    scene sm1cs-my004-23 mc-sy-talking_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Jesus, Stacy-"
    scene sm1cs-my004-23 mc-sy-talking_c2 with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "What, you can't blame a girl for her fantasies!"
    scene sm1cs-my004-24 mc-sy-arguing_c2 with dissolve
    play voice2 mc_angry_errr5 noloop
    if persistent.is_special:
        mc "Everyone, meet my little sister, apparently the horniest woman in the world."
    else:
        mc "Everyone, meet Stacy, apparently the horniest woman in the world."
    scene sm1cs-my004-24 mc-sy-arguing_c1 with dissolve
    play voice3 stacy_no_angry1 noloop
    sy "Am not!"
    play voice2 mc_angry_hm1 noloop
    mc "Are too."
    scene sm1cs-my004-25 mc-sy-arguing_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Whatever. I figured if you couldn't score at a nude art exhibit, it would be impossible to fumble during a swimsuit contest."
    scene sm1cs-my004-25 mc-sy-arguing_c2 with dissolve
    play voice2 mc_angry_cough1 noloop
    if persistent.is_special:
        mc "But it's not a real contest! The only people here are you and Mom!"
    else:
        mc "But it's not a real contest! The only people here are you and Melony!"
    scene sm1cs-my004-a26 my-swimsuit-glambot-00 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs-my004-a26-glam
    pause
    play voice3 stacy_thinking_hmm2 noloop
    sy "Then it should be a pretty easy contest to judge."
    scene sm1cs-my004-26 mc-sy-my-suprised_c1 with dissolve
    play voice2 mc_znames_stacy3 noloop
    mc "Stacy-"
    play sound sfx_door_openclosed2
    scene sm1cs-my004-26 mc-sy-my-suprised_c3 with dissolve
    play voice4 girl34_thinking_eeh2 noloop
    my "How's it look?"
    scene sm1cs-my004-27 mc-sy-my-suprised_c1 with dissolve
    play voice2 mc_pain_mff3 noloop
    mct "Holy shit..."
    scene sm1cs-my004-27 mc-sy-my-suprised_c2 with dissolve
    if persistent.is_special:
        play voice3 stacy_thinking_hmm3 noloop
        sy "You look great, Mom!"
    else:
        sy "You look great, Melony!"
    sy "Right, [mcname]?"
    scene sm1cs-my004-27 mc-sy-my-suprised_c3 with dissolve
    play voice2 d1s5b_emmm noloop
    mc "Erm, right! Yeah! I think you've got, uhhh, a good chance of winning today!"
    scene sm1cs-my004-28 my-smiling_c1 with dissolve
    play voice4 girl34_happy_laugh1 noloop
    my "Thanks, hon."
    scene sm1cs-my004-29 my-sy-mc-talking_c1 with dissolve
    play voice4 girl34_thinking_emm2 noloop
    my "Where is everyone else?"
    scene sm1cs-my004-29 my-sy-mc-talking_c2 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Everyone else... uhm..."
    scene sm1cs-my004-29 my-sy-mc-talking_c3 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "They're all, uh, running late! You know how it is, actresses and models."
    scene sm1cs-my004-30 sy-mc-surprised_c1 with dissolve
    play voice4 girl34_yes_aga3 noloop
    my "Uh huh..."
    my "Well, what should we do in the meantime?"
    scene sm1cs-my004-30 sy-mc-surprised_c2 with dissolve
    play voice3 stacy_thinking_oh1 noloop
    sy "We can get started! Or, erm, practice! [mcname] can be the judge!"
    play voice4 girl34_arrogant_huh1 noloop
    my "Are you sure we shouldn't wait?"
    play sound sfx_cloth_rustling2
    scene sm1cs-my004-31 sy-my-together_c1 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah! They are all, like... super behind? So it'll take them a long time to get here..."
    sy "So no reason to sit around all day!"
    scene sm1cs-my004-31 sy-my-together_c2 with dissolve
    play voice4 girl34_disappointed_eh noloop
    my "If you say so.{w} Well, what should we do first for the contest?"
    scene sm1cs-my004-a32 my-sy-looking-at-mc-glambot-00 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 1.4>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs-my004-a32-glam
    pause
    play voice3 stacy_surprised_oh1 noloop
    sy "Have [mcname] check us out of course!"
    if persistent.is_special:
        play voice4 girl34_thinking_emm4 noloop
        my "Are you saying that my son should check out his own mother?"
        scene sm1cs-my004-33 mc-my-sy-looking-at-him_c1 with dissolve
        play voice3 stacy_yes_yap1 noloop
        sy "Yep!"
    else:
        play voice4 girl34_thinking_emm4 noloop
        my "Is that not a little... odd, Stacy?"
        scene sm1cs-my004-33 mc-my-sy-looking-at-him_c1 with dissolve
        play voice3 stacy_no_nope1 noloop
        sy "Nope!"
    sy "It's super normal. It's just for the contest! Right?"
    scene sm1cs-my004-33 mc-my-sy-looking-at-him_c2 with dissolve
    play voice4 girl34_disappointed_mmf2 noloop
    my "...{w} Right."
    scene sm1cs-my004-34 mc-sy-looking-at-her_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, [mcname], get to judging!"
    scene sm1cs-my004-33 mc-my-sy-looking-at-him_c3 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "God... Stacy comes up with the craziest ideas..."
    mct "I have absolutely no idea how we're going to pull this one off though."
    scene sm1cs-my004-34 mc-sy-looking-at-her_c2 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "I, uhhh, like the colors of your suit? And... it looks good?"
    scene sm1cs-my004-35 sy-rolling-her-eyes_c1 with dissolve
    play voice3 stacy_disappointed_ehh2 noloop
    sy "Come on, [mcname]. You have got to do better then that. How about the cut? The fit?"
    play voice2 mc_arrogant_huh3 noloop
    mc "It looks like it fits?"
    play sound sfx_barefoot_steps1
    scene sm1cs-my004-36 mc-sy-looking-at-her-again_c1 with dissolve
    play voice3 stacy_no_angry2 noloop
    sy "No, doofus. Like... how does it fit {i}on me{/i}, like \"it is high waisted, do I look good with a high waisted suit?\""
    sy "Or, \"the way the top of the suit is cut really accentuates your breats and makes them pop\"."
    scene sm1cs-my004-36 mc-sy-looking-at-her-again_c2 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Okay, uhm..."
    stop sound fadeout 1.0
    scene sm1cs-my004-37 mc-my-looking-at-her-now_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I think... pretty much everything you just said?"
    play voice3 stacy_disappointed_ehh1 noloop
    if persistent.is_special:
        sy "Ugh... fine, try commenting on Mom's suit. Maybe you'll do a better job with her."
    else:
        sy "Ugh... fine, try commenting on Melony's suit. Maybe you'll do a better job with her."
    scene sm1cs-my004-37 mc-my-looking-at-her-now_c2 with dissolve
    play voice4 girl34_arrogant_ha2 noloop
    my "Don't take it easy on me, [mcname], I can take it."
    scene sm1cs-my004-38 mc-my-looking-at-her_c1 with dissolve
    play voice2 d3s7_mcemm noloop
    mc "I..."
    if persistent.is_special:
        mc "You look great, Mom. Seriously."
    else:
        mc "You look great, Melony. Seriously."
    scene sm1cs-my004-38 mc-my-looking-at-her_c2 with dissolve
    play voice4 girl34_thinking_hmm3 noloop
    my "Thank you, [mcname]. But I think you're supposed to talk about cut and fit a little bit."
    scene sm1cs-my004-39 mc-my-talking_c1 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, right... uhm..."
    mc "Uh...{w} The cut of the swimsuit is right for you, it draws attentions to all the right parts..."
    mc "And, uhhh, the fit is good."
    mct "So fucking good."
    mc "It shows off all the right curves, and doesn't sag in places that are bad..."
    mc "And it's maybe the perfect swimsuit for your body type."
    scene sm1cs-my004-39 mc-my-talking_c2 with dissolve
    play voice4 girl34_surprised_ah4 noloop
    my "You're just saying that."
    scene sm1cs-my004-40 sy-mc-my-talking_c2 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I would never."
    scene sm1cs-my004-40 sy-mc-my-talking_c3 with dissolve
    play voice3 stacy_surprised_ah2 noloop
    sy "Ugh, that was a good critique, [mcname]! Why couldn't you do that for me?"
    play voice2 mc_thinking_emm1 noloop
    mc "I, uhhhh, will do better?"
    scene sm1cs-my004-41 sy-starring_c3 with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "I hope so."
    play sound sfx_comic_wink1
    scene sm1cs-my004-42 sy-mc-winking-thinking_c1 with dissolve
    pause
    scene sm1cs-my004-42 sy-mc-winking-thinking_c2 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mct "Damn, Stacy is really feeling herself today."
    scene sm1cs-my004-43 sy-mc-winking-thinking_c1 with dissolve
    play voice3 stacy_happy_yay2 noloop
    sy "Next we should do the catwalk!"
    scene sm1cs-my004-43 sy-mc-winking-thinking_c2 with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "A catwalk?"
    scene sm1cs-my004-44 sy-mc-my-talking_c1 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    if persistent.is_special:
        sy "Yeah! Me and Mom will strut our stuff and see what you think!"
    else:
        sy "Yeah! Me and Melony will strut our stuff and see what you think!"
    sy "Let you take a look at allll of the {b}assets{/b}."
    scene sm1cs-my004-44 sy-mc-my-talking_c2 with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "Stacy!"
    scene sm1cs-my004-44 sy-mc-my-talking_c3 with dissolve
    play voice4 girl34_thinking_hmm5 noloop
    my "She does have a point, [mcname]. It's hard to do a swimsuit competition without seeing what the model's body looks like when she's moving."
    scene sm1cs-my004-45 mc-okay_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "All right, if you two say so..."
    play sound sfx_barefoot_steps1 volume 1.6 loop
    scene sm1cs-my004-46 sy-mc-my-talking_c1 with dissolve
    play voice3 stacy_yes_fine3 noloop
    sy "All right, [mcname]. For this one, you need to tell us how our swimsuits looks when we move. Like, does it ride up, does it sit funny, that kind of thing."
    play voice2 mc_yes_okay2 noloop
    mc "Okay?"
    scene sm1cs-my004-46 sy-mc-my-talking_c2 with dissolve
    play voice4 girl34_arrogant_ha3 noloop
    my "He really has no idea what he's doing, does he?"
    scene sm1cs-my004-46 sy-mc-my-talking_c3 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "He never does."
    play voice2 mc_thinking_hmm5 noloop
    mc "You know I can hear you two!"
    play voice4 girl34_happy_laugh8 noloop
    my "Hehehehehehe!"
    stop sound fadeout 1.0
    scene sm1cs-my004-47 sy-mc-my-talking_c1 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "Ready?"
    scene sm1cs-my004-47 sy-mc-my-talking_c3 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure?"
    scene sm1cs-my004-49 sy-catwalking_c1 with dissolve
    pause
    scene sm1cs-my004-49 sy-catwalking_c2 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Be still my beating heart."
    scene sm1cs-my004-49 sy-catwalking_c3 with dissolve
    pause
    scene sm1cs-my004-50 sy-winking_c1 with dissolve
    play voice3 amrose_old_psst2 noloop
    sy "{size=*0.7}You got this, [mcname]. Knock her socks off.{/size}"
    scene sm1cs-my004-51 sy-catwalking-back_c1 with dissolve
    pause
    scene sm1cs-my004-51 sy-catwalking-back_c2 with dissolve
    pause
    scene sm1cs-my004-51 sy-catwalking-back_c3 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-my004-52 sy-my-talking_c1 with dissolve
    play voice3 stacy_yes_fine1 noloop
    if persistent.is_special:
        sy "All right! Your turn, Mom."
    else:
        sy "All right! Your turn, Melony."
    scene sm1cs-my004-52 sy-my-talking_c2 with dissolve
    play voice4 girl34_thinking_hmm6 noloop
    my "Here goes nothing..."
    play sound sfx_barefoot_steps1 volume 1.6 loop
    scene sm1cs-my004-53 my-catwalking_c1 with dissolve
    pause
    scene sm1cs-my004-53 my-catwalking_c2 with dissolve
    pause
    scene sm1cs-my004-53 my-catwalking_c3 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-my004-54 my-posing_c1 with dissolve
    play voice4 girl34_arrogant_huh3 noloop
    my "How am I doing so far?"
    scene sm1cs-my004-54 my-posing_c2 with dissolve
    play voice2 mc_surprised_wow2 noloop
    if persistent.is_special:
        mc "Crushing it, Mom."
    else:
        mc "Crushing it, Melony."
    scene sm1cs-my004-54 my-posing_c3 with dissolve
    play voice4 girl34_happy_laugh3 noloop
    my "Thanks, [mcname]."
    play sound sfx_barefoot_steps1 volume 1.6 loop
    scene sm1cs-my004-55 my-catwalking-back_c1 with dissolve
    pause
    scene sm1cs-my004-55 my-catwalking-back_c2 with dissolve
    pause
    scene sm1cs-my004-55 my-catwalking-back_c3 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-my004-56 mc-sy-asking-thinking_c1 with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "All right, [mcname]! Who wins the catwalk?"
    scene sm1cs-my004-56 mc-sy-asking-thinking_c2 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Oh shit, that's right. I need to pick someone if I want to keep the ruse going..."
    mct "Shit, who should I pick?"
    menu:
        "Mom" if persistent.is_special:
            $ player.set_choice("sm1cs_my004_choose_my")
            scene sm1cs-my004-57 mc-sy-choosing-his-mom_c2 with dissolve
            play voice2 mc_thinking_hmm8 noloop
            mc "I have to pick Mom. I think she really nailed that catwalk."
            play sound sfx_hands_clap1
            scene sm1cs-my004-57 mc-sy-choosing-his-mom_c1 with dissolve
            play voice3 stacy_yes_yeah1 noloop
            sy "Yeah, I think she did."
        "Melony" if not persistent.is_special:
            $ player.set_choice("sm1cs_my004_choose_my")
            scene sm1cs-my004-57 mc-sy-choosing-his-mom_c2 with dissolve
            play voice2 mc_thinking_hmm8 noloop
            mc "I have to pick Melony. I think she really nailed that catwalk."
            play sound sfx_hands_clap1
            scene sm1cs-my004-57 mc-sy-choosing-his-mom_c1 with dissolve
            play voice3 stacy_yes_yeah1 noloop
            sy "Yeah, I think she did."
        "Stacy":
            $ player.set_choice("sm1cs_my004_choose_sy")
            scene sm1cs-my004-58 mc-sy-choosing-his-sister_c2 with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "Stacy."
            scene sm1cs-my004-58 mc-sy-choosing-his-sister_c1 with dissolve
            play voice3 stacy_surprised_huh3 noloop
            sy "Stacy?"
            scene sm1cs-my004-58 mc-sy-choosing-his-sister_c3 with dissolve
            play voice3 stacy_angry noloop
            sy "What, no — you're supposed-"
            scene sm1cs-my004-59 sy-thanking_c1 with dissolve
            play voice3 stacy_disappointed_mmm1 noloop
            if persistent.is_special:
                sy "Thanks, bro."
            else:
                sy "Thanks, [mcname]."
    scene sm1cs-my004-60 mc-my-sy-asking_c1 with dissolve
    play voice4 girl34_thinking_emm5 noloop
    my "You know, it never occurred to me to ask, but what does the winner get?"
    scene sm1cs-my004-60 mc-my-sy-asking_c2 with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "The winner?"
    play sound sfx_hands_clap1
    scene sm1cs-my004-61 my-sy-talking_c2 with dissolve
    play voice4 girl34_yes_aga2 noloop
    my "This is a competition, right?"
    scene sm1cs-my004-60 mc-my-sy-asking_c3 with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "Yes! Erm... they win a..."
    scene sm1cs-my004-61 my-sy-talking_c1 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "The winner gets a movie date here with [mcname]!"
    play voice4 girl34_thinking_mmm noloop
    my "A movie date with [mcname]? That's the prize?"
    sy "Yep!"
    scene sm1cs-my004-61 my-sy-talking_c2 with dissolve
    play voice4 girl34_thinking_hmm7 noloop
    my "Hmmm..."
    scene sm1cs-my004-62 mc-sy-talking_c1 with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "Now, it's, erm, time to move on to theeeeee...{w} photo portion of the contest!"
    scene sm1cs-my004-62 mc-sy-talking_c2 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Oh God, Stacy is really flying by the seat of her pants."
    mct "She has no idea what she's doing."
    scene sm1cs-my004-63 my-sy-talking_c1 with dissolve
    play voice3 stacy_thinking_hmm2 noloop
    sy "And we should put on some oil for this!"
    scene sm1cs-my004-63 my-sy-talking_c2 with dissolve
    play voice4 girl34_surprised_what1 noloop
    my "We should do what?"
    play sound sfx_barefoot_steps1 volume 1.7 loop
    scene sm1cs-my004-65 sy-getting-the-bottle_c1 with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "Oil up! You know, it'll make the photos pop!"
    if persistent.is_special:
        sy "I'll oil myself up! And [mcname] can help you, Mom!"
    else:
        sy "I'll oil myself up! And [mcname] can help you, Melony!"
    scene sm1cs-my004-64 my-mc-nervous_c2 with dissolve
    play voice2 d1s5_orgasm noloop
    mct "Oh God... Stacy might have pushed it too far with that..."
    scene sm1cs-my004-64 my-mc-nervous_c1 with dissolve
    play voice4 girl34_disappointed_eeh4 noloop
    my "I...{w} Okay. Where's the oil?"
    play voice3 stacy_yes_yap3 noloop
    sy "It's right over here! Let me grab it for you!"
    scene sm1cs-my004-65 sy-getting-the-bottle_c2 with dissolve
    play voice2 mc_pain_mff2 noloop
    mct "I can't believe she agreed to that..."
    stop sound fadeout 2.5
    scene sm1cs-my004-66 my-mc-talking_c1 with dissolve
    play voice4 girl34_yes_aga4 noloop
    my "All right, [mcname]. Let's start rubbing me down!"
    mc "..."
    my "[mcname]?"
    mct "Shit! I think I spaced out for a minute."
    play sound sfx_hair_scratch1
    scene sm1cs-my004-66 my-mc-talking_c2 with dissolve
    if persistent.is_special:
        play voice2 mc_yes_yeah1 noloop
        mc "Yeah, erm, of course, Mom."
    else:
        play voice2 mc_yes_yeah2 noloop
        mc "Yeah, erm, of course, Melony."
    play sound sfx_squirt1
    scene sm1cs-my004-67 mc-putting-oil-on-hand_c1 with dissolve
    pause
    play sound2 sfx_handjob_cream1 volume 2.0 noloop
    scene sm1cs-my004-68 mc-my-talking_c2 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.4
    mc "Are you sure you want to do this?"
    scene sm1cs-my004-68 mc-my-talking_c1 with dissolve
    play voice4 girl34_thinking_eeh2 noloop
    my "Mostly. But you should start before I get cold feet."
    play voice2 mc_yes_aga2 noloop
    mc "Aye, aye!"
    play sound sfx_handjob_cream1 volume 2.0 loop
    scene sm1cs-my004-69 mc-thinking_c1 with dissolve
    play voice2 d14s16_smell noloop
    if persistent.is_special:
        mct "I can't believe Mom is letting me rub oil all over her..."
    else:
        mct "I can't believe Melony is letting me rub oil all over her..."
    mct "I wonder..."
    scene sm1cs-my004-70 mc-my-talking_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    if persistent.is_special:
        mc "Hey, Mom?"
    else:
        mc "Hey, Melony?"
    scene sm1cs-my004-70 mc-my-talking_c2 with dissolve
    play voice4 girl34_yes_questioning7 noloop
    my "Yes?"
    scene sm1cs-my004-71 mc-my-talking_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop volume 1.7
    mc "Uhhh, not that I'm not happy to have you in the competition, but... this doesn't feel like something you'd normally do-"
    play voice4 girl34_arrogant_hm2 noloop
    my "And you're wondering why I'm doing it?"
    scene sm1cs-my004-71 mc-my-talking_c2 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "A little bit, yeah."
    play voice4 girl34_happy_relief3 noloop
    my "*sigh* Well... I don't know why I'm doing it either."
    scene sm1cs-my004-a72 mc-my-oil-glambot-00 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs-my004-a72-glam with dissolve
    pause
    play voice4 girl34_thinking_emm1 noloop
    if persistent.is_special:
        my "Part of me thinks it's so I can spend time with you and your sister."
    else:
        my "Part of me thinks it's so I can spend time with you and Stacy."
    my "But I think another part is that... doing this...{w} To help me be more comfortable with what you do for work."
    scene sm1cs-my004-72 mc-my-talking_c2 with dissolve
    play voice4 girl34_disappointed_mmf1 noloop
    my "Another part of me... misses being a little wild."
    my "The last few years I've focused on work, and you two, and... everything else in my life."
    scene sm1cs-my004-73 my-looking-down_c1 with dissolve
    play voice4 girl34_happy_relief1 noloop
    my "And maybe I lost that side of that got really excited about life. It just... slipped away."
    scene sm1cs-my004-74 mc-my-talking_c1 with dissolve
    play voice4 girl34_happy_mmm2 noloop
    my "I miss that. The woman who could cut loose, be feral, be... free."
    scene sm1cs-my004-74 mc-my-talking_c2 with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Wow..."
    play voice4 girl34_yes_ugu2 noloop
    my "Maybe that's why I'm here. To find her again."
    stop sound fadeout 1.0
    scene sm1cs-my004-75 mc-thinking_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "..."
    mct "Damn..."
    scene sm1cs-my004-74 mc-my-talking_c1 with dissolve
    play voice4 girl34_disappointed_eem2 noloop
    my "You okay, [mcname]?"
    play voice2 d2s9_confused noloop
    mc "Uhm, yeah. Sorry. I just wasn't expecting such a deep thought."
    my "*giggles* I'm full of surprises."
    my "But uh... don't get too distrated. I think there are a more spots that need oil."
    mc "Oh, uhm... what'd I miss?"
    play sound sfx_cloth_rustling3
    scene sm1cs-my004-80 my-shocked_c1 with dissolve
    play voice4 girl34_arrogant_laugh2 noloop
    my "*giggles* They are kind of hard to miss, [mcname]."
    play voice2 d1s1_mmm noloop volume 1.8
    mct "My god. Melonly wants me to rub down her tits!"
    if persistent.is_special:
        mct "God, Mom is being so forward..."
    else:
        mct "God, Melony is acting so forward..."
    play voice2 mc_yes_yeah5 noloop
    mc "Erm, yeah. Let me, uhm, get that- those, uhhh. Yeah."
    if persistent.is_special:
        mct "All right... time to fondle my Mom..."
    else:
        mct "All right... time to fondle Melony..."
    mct "Come on, [mcname]. Pull yourself together. You can do this."
    mct "Tits are tits, you got game. You got this."
    scene sm1cs-my004-a78-1 mc-fondling-my-anim-01 with dissolve
    pause
    play sound sfx_handjob_cream1 volume 2.0 loop
    scene sm1cs-my004-a78-1
    play voisex2 mc_sex_openmoans2
    mct "All right, so far so good..."
    mct "Tits are just tits."
    pause
    scene sm1cs-my004-a78-2 with dissolve
    if persistent.is_special:
        mct "Even if they're your Mom's huge... soft... pillowy... warm tits..."
    else:
        mct "Even if they're Melony's huge... soft... pillowy... warm tits..."
    pause
    scene sm1cs-my004-a78-3 with dissolve
    mct "Oh God, I feel myself getting a boner. S-O-S, S-O-S."
    mct "Uhm, think of anything that isn't tits! Taxes, baseball, soccer balls..."
    pause
    scene sm1cs-my004-a78-4 with dissolve
    if persistent.is_special:
        mct "Mom's tits are as big as a soccer ball-"
    else:
        mct "Melony's tits are as big as a soccer ball-"
    pause
    scene sm1cs-my004-a78-5 with dissolve
    mct "Get your head in the game, man!"
    play voisex4 girl13_sex_closedmoan2 noloop
    my "{size=*0.6}Mmmmmmmm...{/size}"
    play voisex2 mc_angry_errr4 noloop
    scene sm1cs-my004-78 mc-thinking_c1 with vpunch
    if persistent.is_special:
        mct "Did Mom just moan!?!"
    else:
        mct "Did Melony just moan!?!"
    mct "No, I'm imagining it-"
    scene sm1cs-my004-a78-1-f with dissolve
    play voisex4 girl13_sex_closedmoan4 noloop
    my "{size=*0.6}Mmmmmmmmmmmmmmmmm...{/size}"
    pause
    scene sm1cs-my004-a78-2-f with dissolve
    play voisex2 mc_sex_openmoans2
    mct "Nope, not imaging it!"
    scene sm1cs-my004-a78-3-f with dissolve
    play voisex4 girl13_sex_closedmoan6 noloop
    pause
    scene sm1cs-my004-a78-4-f with dissolve
    my "{size=*0.6}Mmmmmmm...{/size}"
    pause
    scene sm1cs-my004-a78-5-f with dissolve
    play voisex2 d2s12_emmm noloop
    mc "Uhm..."
    pause
    stop sound fadeout 1.0
    scene sm1cs-my004-80 my-shocked_c1 with dissolve
    play voice4 girl34_surprised_ah3 noloop
    my "Oh, uhm-"
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, I think we're all done, erm..."
    my "Yep!{w} I don't think you missed anything..."
    play sound2 sfx_barefoot_steps1
    play sound sfx_door_openclosed2
    scene sm1cs-my004-81 my-sy-talking_c1 with dissolve
    if persistent.is_special:
        play voice3 stacy_thinking_hmm4 noloop
        sy "Looking good, Mom!"
    else:
        sy "Looking good, Melony!"
    stop sound2 fadeout 1.0
    scene sm1cs-my004-81 my-sy-talking_c2 with dissolve
    play voice4 girl34_thinking_emm5 noloop
    my "Thank you, Stacy. I, uhm, appreciate it."
    scene sm1cs-my004-81 my-sy-talking_c3 with dissolve
    play voice2 d1s5_orgasm noloop
    mct "God, did she... did she get turned on?"
    scene sm1cs-my004-82 my-sy-talking_c2 with dissolve
    play voice4 girl34_disappointed_ehh2 noloop
    my "Uhm, I actually... {w}I just remembered, I have an... important call with the gallery."
    scene sm1cs-my004-82 my-sy-talking_c1 with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "What! This is our last part of the contest!"
    play sound2 sfx_barefoot_steps1
    scene sm1cs-my004-83 my-walking-back_c1 with dissolve
    play voice4 girl34_disappointed_eeh2 noloop
    my "I know, I am so sorry. It totally slipped my mind but it's... important."
    my "I'm just going to wash up a bit, and then I'll have to go."
    play sound2 sfx_door_openclosed1 noloop
    scene sm1cs-my004-84 mc-sy-talking_c1 with dissolve
    play voice3 stacy_angry_argh1 noloop
    sy "{size=*0.6}[mcname]! What did you do!?{/size}"
    scene sm1cs-my004-84 mc-sy-talking_c2 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "{size=*0.6}Nothing! I just put the oil on her!{/size}"
    play voice3 stacy_angry_breath1 noloop
    sy "{size=*0.6}Then why is she sprinting out of here?{/size}"
    mc "I-"
    play sound sfx_door_openclosed2
    scene sm1cs-my004-85 my-talking_c1 with dissolve
    play voice4 girl34_disappointed_eeh3 noloop
    my "Again, I am so sorry, you two."
    my "We'll have to... do something to make up for the interruption."
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-my004-86 my-sy-hugging_c1 with dissolve
    if persistent.is_special:
        play voice3 stacy_thinking_oh2 noloop
        sy "Sounds good, Mom."
    else:
        sy "Sounds good, Melony."
    scene sm1cs-my004-87 my-mc-bye_c1 with dissolve
    play voice4 girl34_yes_aga8 noloop
    my "I'll see you two later, okay?"
    scene sm1cs-my004-87 my-mc-bye_c2 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay."
    play voice4 girl34_hey_bye7 noloop
    if persistent.is_special:
        mc "Bye, Mom."
        play sound sfx_heels_steps1
        scene sm1cs-my004-88 my-leaving_c1 with dissolve
        my "Bye, son."
    else:
        mc "Bye, Melony."
        play sound sfx_heels_steps1
        scene sm1cs-my004-88 my-leaving_c1 with dissolve
        my "Bye, [mcname]."
    play sound sfx_door_openclosed1
    scene sm1cs-my004-89 sy-mc-talking_c2 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Wow. I can't believe she bolted that fast."
    scene sm1cs-my004-90 sy-mc-talking_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "I mean... I'm not that surprised."
    scene sm1cs-my004-90 sy-mc-talking_c2 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "What do you mean?"
    scene sm1cs-my004-90 sy-mc-talking_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I mean, I think it's a lot to just surprise someone with a two on one swimsuit competition."
    mc "And then shove oil in their hands and tell them to get lubed up."
    scene sm1cs-my004-91 sy-mc-talking_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well what was I supposed to do!"
    sy "You weren't making any progress."
    scene sm1cs-my004-91 sy-mc-talking_c2 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "*annooyed noise* I can handle it, Stacy. You just have to have a little faith in the process."
    play sound sfx_hands_clap4
    scene sm1cs-my004-92 sy-rolling-her-eyes_c1 with dissolve
    play voice3 stacy_disappointed_mmm2 noloop
    sy "A little faith in the process, hmmmph."
    sy "And I covered myself in all this oil for nothing."
    scene sm1cs-my004-92 sy-rolling-her-eyes_c2 with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "What did you think was going to happen?"
    scene sm1cs-my004-93 sy-shrugging_c1 with dissolve
    play voice3 stacy_hmm2 noloop
    sy "I don't know. Maybe some oil wrestling. Or a nuru massage, those I guess are super hot."
    scene sm1cs-my004-93 sy-shrugging_c2 with dissolve
    play voice2 stacy_no_nah2 noloop
    if persistent.is_special:
        mc "You thought you'd get a nuru massage from Mom?"
    else:
        mc "You thought you'd get a nuru massage from Melony?"
    scene sm1cs-my004-94 sy-smirking_c1 with dissolve
    play voice3 stacy_no_questioning4 noloop
    sy "No, but maybe {i}we{/i} could have given you one."
    scene sm1cs-my004-94 sy-smirking_c2 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh..."
    scene sm1cs-my004-94 sy-smirking_c1 with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "Yeah, sounds pretty hot, doesn't it."
    mc "..."
    sy "That's what I thought."
    play sound sfx_barefoot_steps1 volume 1.6
    scene sm1cs-my004-95 sy-mc-walking-towards-the-bathroom_c1 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "But now I need to take a cold shower to calm down and get all of this crap off of me."
    scene sm1cs-my004-95 sy-mc-walking-towards-the-bathroom_c2 with dissolve
    pause
    play sound sfx_door_openclosed2
    scene sm1cs-my004-95 sy-mc-walking-towards-the-bathroom_c3 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Man, that was incredible..."
    if persistent.is_special:
        mct "I still can't get over the fact that Mom agreed to do the competition at all."
    else:
        mct "I can't believe Melony even agreed to do the competition in the first place."
    scene sm1cs-my004-96 mc-thinking_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "And then her moaning will I massaged her tits..."
    scene sm1cs-my004-96 mc-thinking_c2 with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "God, enough to make a man go crazy.{w} Or a woman."
    play sound sfx_heels_steps2 loop
    scene sm1cs-my004-97 mc-walking_c1 with dissolve
    mct "I should probably give Melony a few days to calm down. That will give me some time to come up with a plan for what comes next."
    scene sm1cs-my004-97 mc-walking_c2 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mct "Mmmm. I just hope that things didn't go too far today..."
    scene sm1cs-my004-98 mc-at-the-door_c1 with dissolve
    pause
    play sound sfx_door_openclosed1
    jump sm1cs_my004_exit_to_studio
label sm1cs_my004_exit_to_studio:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(MY_STORY, 3, 0, 5)
    return