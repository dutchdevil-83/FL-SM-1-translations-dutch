label sm1cs_am_renovation:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    play music music_funky_day fadein 2.5
    scene sm1cs-am-01 mc-am-talk-point-at-speck with dissolve
    play voice3 girl22_arrogant_he noloop
    am "What's that?"
    play sound sfx_chair_slide1
    scene sm1cs-am-02 mc-am-talk-lean-in with dissolve
    play voice3 girl22_disappointed_ah noloop
    am "Dandruff?"
    scene sm1cs-am-03 mc-am-talk-close-up-unimpressed with dissolve
    play voice3 girl22_disgust_meeh noloop
    am "I know you're trying to work hard and make something of yourself, but you should still take care of yourself, [mcname]."
    play sound sfx_cloth_rustling2
    scene sm1cs-am-04 mc-am-talk-sit-up-snarky with dissolve
    play voice3 girl22_happy_laugh3 noloop
    am "A lesser woman would avoid dating you if she saw that."
    scene sm1cs-am-05 mc-am-talk-look-at-shoulder with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh. It's plaster."
    scene sm1cs-am-06 mc-am-talk-roll-eyes with dissolve
    play voice3 girl22_arrogant_pff noloop
    am "Right. Just plaster."
    scene sm1cs-am-07 mc-am-talk-serious with dissolve
    play voice2 mc_no_no8 noloop
    mc "No I swear."
    mc "I'm remodeling my home, and I'm doing a lot of the work myself."
    scene sm1cs-am-09 mc-am-talk-curious with dissolve
    play voice3 girl22_surprised_huh2 noloop
    am "Why are you remodeling your home?"
    scene sm1cs-am-07 mc-am-talk-serious with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "The place is nice, but there is definitely room for improvement."
    play voice3 girl22_arrogant_ha noloop
    am "Haha. That should be the title of your biography."
    menu:
        "Insult April"(hint="sm1cs_am_renovation_m01_h01"):
            call sm1cs_am_renovation_m01_c01 from _call_sm1cs_am_renovation_m01_c01
            scene sm1cs-am-10 mc-am-talk-insult-choice-little-mad with dissolve
            play voice2 mc_angry_errr2 noloop
            mc "And yours would be World's Bitchiest Coder."
            scene sm1cs-am-11 mc-am-talk-insult-choice-surprised with dissolve
            play voice3 girl22_happy_mew1 noloop
            am "Meow."
            am "I've heard better titles."
        "Shake it off"(hint="sm1cs_am_renovation_m01_h02"):
            scene sm1cs-am-14 mc-am-talk-confused with dissolve
            play voice2 mc_yes_yeah9 noloop
            mc "Whatever."
    scene sm1cs-am-16 mc-am-talk-first option-annoyed with dissolve
    play voice3 girl22_hey_happy noloop
    am "So why didn't you ask for my help with this remodel thing?"
    scene sm1cs-am-17 mc-am-talk-first option-point-finger with dissolve
    play voice3 girl22_arrogant_hm noloop
    am "Too proud?"
    scene sm1cs-am-18 mc-am-talk-first option-apologizing with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Huh? Oh, you mean for my home?"
    play voice3 girl22_disappointed_geh noloop
    am "Duh."
    menu:
        "I didn't think to ask."(hint="sm1cs_am_renovation_m02_h01"):
            scene sm1cs-am-15 mc-am-talk-first option-feels-bad with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "I honestly didn't think about asking you, April."
            scene sm1cs-am-16 mc-am-talk-first option-annoyed with dissolve
            play voice3 girl22_yes_aga4 noloop
            am "That was a mistake."
            play voice2 d2s9_confused noloop
            mc "Uh... if you say so."
            scene sm1cs-am-17 mc-am-talk-first option-point-finger with dissolve
            play voice3 girl22_angry_dagh noloop
            am "You think because I'm a pro coder, I can't swing a hammer or run a saw?"
            play voice2 mc_arrogant_hm1 noloop
            mc "I've never heard of 'running' a saw."
            scene sm1cs-am-18 mc-am-talk-first option-apologizing with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.6
            mc "But honestly, it was just a-"
            scene sm1cs-am-09 mc-am-talk-curious with dissolve
            play voice3 girl22_no_uhuh1 noloop
            am "Save it. I'm going to make you eat your chauvinistic attitude, [mcname]."
            am "We're going to your place right now."
        "You want to help?"(hint="sm1cs_am_renovation_m02_h02"):
            call sm1cs_am_renovation_m02_c02 from _call_sm1cs_am_renovation_m02_c02
            scene sm1cs-am-14 mc-am-talk-confused with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "You really want to help?"
            scene sm1cs-am-11 mc-am-talk-insult-choice-surprised with dissolve
            play voice3 girl22_yes_happy noloop
            am "Of course I want to help."
            am "It's no good living in a half-complete mess of a place."
            am "And I don't want you to use this as an excuse the next time I want to go on a date."
            scene sm1cs-am-21 mc-am-talk-surprised with dissolve
            play voice2 mc_surprised_wow4 noloop
            mc "I wouldn't dream of it."
            scene sm1cs-am-20 mc-am-talk-second-option-excited-to-help with dissolve
            play voice3 girl22_yes_aga4 noloop
            am "Then it's settled. We'll go to your place right now."
    scene sm1cs-am-18 mc-am-talk-first option-apologizing with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, 'now' now?"
    mc "What about work?"
    play sound sfx_paper_bag_1
    scene sm1cs-am-22 mc-am-grab-bag with dissolve
    pause
    play sound sfx_jeans_fly1 volume 2.0
    scene sm1cs-am-23 mc-am-talk-stand-hold-bag with dissolve
    play voice3 girl22_happy_mmm noloop
    am "I have plenty of PTO to use."
    scene sm1cs-am-24 mc-am-talk-unsure-walk-away with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I'm not so lucky."
    play voice3 girl22_yes_yep1 noloop
    am "I'll email Claire that I dragged you off to work on the project."
    play sound2 sfx_heels_steps1
    scene sm1cs-am-25 mc-am-talk-leaving-office with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "She won't mind. Or she will, whatever."
    scene sm1cs-am-26 mc-am-both-leaving with dissolve
    pause
    stop sound2 fadeout 1.5
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.6, 3.5, "music" )
    jump sm1cs_am_renovation_studio
label sm1cs_am_renovation_studio:
    play sound sfx_door_openclosed1
    scene sm1cs-am-27 mc-am-arrive-at-studio with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-am-28 mc-am-talk-close-up-look-around with dissolve
    play voice3 girl22_surprised_eh1 noloop
    am "Not bad."
    scene sm1cs-am-29 mc-am-talk-behind-shot-room-view with dissolve
    pause
    play sound sfx_heels_steps1 loop
    scene sm1cs-am-30 mc-am-talk-walk-forward-into-room with dissolve
    play voice3 girl22_surprised_huh1 noloop
    am "So what exactly do you need with all this space?"
    scene sm1cs-am-31 mc-am-talk-notices-sketch with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "You planning to build a startup? Or a small motel?"
    scene sm1cs-am-32 mc-am-talk-walk-towards-painting with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Something like that."
    stop sound fadeout 1.0
    scene sm1cs-am-33 mc-am-talk-pov-looking-at-painting with dissolve
    play voice3 girl22_disappointed_mmf noloop
    am "Why do I feel like you're a lot richer than you act?"
    play voice2 mc_arrogant_heh1 noloop
    mc "Even if I was rich, I'm not sure how to act rich."
    scene sm1cs-am-34 mc-am-pause-smile-at with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "But I'm not rich. I've been working my butt off to get the money to do this renovation."
    scene sm1cs-am-33 mc-am-talk-pov-looking-at-painting with dissolve
    play voice3 girl22_arrogant_yeah noloop
    am "Really? You show this hard work very sneakily."
    scene sm1cs-am-35 mc-am-talk-menu-all-options with dissolve
    play voice3 girl22_happy_relief noloop
    if player.has_played_scene("sm1ms015"):
        if persistent.is_special:
            am "Is that supposed to be your sister or something?"
            scene sm1cs-am-37 mc-am-talk-tv-point with dissolve
            play voice2 mc_yes_yeah2 noloop
            mc "Yeah. Just something my mom wanted to add."
            mc "Liven up the place I guess."
        else:
            am "Uh. Is this supposed to be your friend Stacy or something?"
            scene sm1cs-am-37 mc-am-talk-tv-point with dissolve
            play voice2 mc_yes_yeah2 noloop
            mc "Yeah. Melony is doing the piece. She's got a natural talent for painting."
        play sound sfx_heels_steps1 loop
        scene sm1cs-am-38 mc-am-talk-walk-away-annoyed with dissolve
        play voice3 girl22_thinking_hmm2 noloop
        am "Hmmm."
    else:
        am "Nice artwork. Someone you know."
        scene sm1cs-am-37 mc-am-talk-tv-point with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "Yeah."
        if persistent.is_special:
            mc "It's a piece showing off my sister. Artist friend wanted to add a personal touch."
        else:
            mc "Just something an artist friend wanted to add to the place."
        play sound sfx_heels_steps1 loop
        scene sm1cs-am-38 mc-am-talk-walk-away-annoyed with dissolve
        play voice3 girl22_thinking_hmm2 noloop
        am "Hmmm."
    stop sound fadeout 1.0
    scene sm1cs-am-39 mc-am-talk-reading-box-mc-watch with dissolve
    play voice3 girl22_yes_aga11 noloop
    am "Alright, so what can I do to help out?"
    scene sm1cs-am-40 mc-am-talk-agree with dissolve
    play voice2 mc_thinking_hm noloop
    mc "You can help me figure out the wiring for the TV. Should be easy with your technical know-how."
    play voice3 girl22_disappointed_oh noloop
    am "Uh. I'm more than just a pretty brain, [mcname]."
    am "Huberu Office Desk and Kenner-Tran Gaming Chair. Not bad."
    am "I can help you build those two. Easy."
    play voice2 mc_yes_okay1 noloop
    mc "Alright. Let's do it."
    $ renpy.music.set_volume(1.0, 2.0, "music" )
    jump sm1cs_am_renovation_later
label sm1cs_am_renovation_later:
    scene black
    show screen scene_transistion(_("A few minutes later"))
    with Fade(0.3, 0.5, 0.3)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.6, 2.0, "music" )
    scene sm1cs-am-41 mc-am-talk-in-pain
    with Fade(0.3, 0.5, 0.3)
    play voice3 girl22_pain_ou1 noloop
    play sound sfx_bones_wrench volume 0.5
    play sound2 sfx_fall_down1 noloop
    with hpunch
    am "Ah. Shit, fucking fuck."
    scene sm1cs-am-42 mc-am-talk-concerned with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "What happened?"
    play voice3 girl22_pain_ou2 noloop
    am "Fucking charlie horse. Nrraaah."
    play sound sfx_heels_steps2
    scene sm1cs-am-43 mc-am-talk-kneel-beside with dissolve
    stop sound fadeout 2.0
    play voice2 mc_angry_huh2 noloop
    mc "..."
    play sound sfx_handjob_cream1 loop volume 2.0
    scene sm1cs-am-44 mc-am-talk-kneel-beside-touch-leg with dissolve
    play voice3 girl22_scared_huh noloop
    am "What are you doing?"
    play voice2 mc_thinking_hmm2 noloop
    mc "Just giving you a quick rub. Always helps when I get one."
    scene sm1cs-am-45 mc-am-talk-annoyed with dissolve
    play voice3 girl22_angry_hmm noloop
    am "Listen closely, dummy. We might be dating but that doesn't mean my body is free to-"
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-am-46 mc-am-talk-relaxing with dissolve
    play voice3 girl22_sex_openmoans1
    am "Oooouhaah..."
    am "Fuck. That is actually really helping."
    scene sm1cs-am-47 mc-am-talk-respond with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "See. Little trust goes a long way."
    scene sm1cs-am-48 mc-am-talk-alt-unsure with dissolve
    am "I..."
    play sound sfx_skirt_off2
    scene sm1cs-am-49 mc-am-talk-back-away-embarrassed with dissolve
    play voice3 girl22_yes_yeah3 noloop
    am "Yeah, sure. Whatever."
    play sound sfx_cloth_rustling1
    scene sm1cs-am-50 mc-am-talk-stands-up-wants-to-be-alone with dissolve
    play voice3 girl22_angry_cough noloop
    am "Why don't you finish the desk on your own. I don't want to slow you down."
    play voice2 mc_no_no2 noloop
    mc "You won't."
    play sound sfx_heels_steps1
    scene sm1cs-am-51 mc-am-watch-her-go-downstairs with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "Just... leave me be for a minute, [mcname]."
    play voice2 mc_yes_okay2 noloop
    mc "Okay."
    play sound sfx_hair_scratch1
    scene sm1cs-am-52 mc-am-look-back-at-work with dissolve
    pause
    scene sm1cs-am-53 mc-am-talk-on-laptop with fade
    play sound sfx_keyboard_typing2 volume 1.5
    play voice2 d1s2_hmm noloop volume 1.8
    mc "What are you doing?"
    scene sm1cs-am-54 mc-am-talk-closer-to-am-alt with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Another charlie horse?"
    scene sm1cs-am-55 mc-am-talk-alt with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "I'm feeling much better. After I came down I made sure to do some stretches."
    am "Cribbed some notes from a yoga video."
    am "But that's not all I did."
    play sound sfx_gadgets_laptop_closed
    scene sm1cs-am-56 mc-am-close-laptop with dissolve
    pause
    play sound sfx_cloth_rustling1
    scene sm1cs-am-57 mc-am-thinking-menu with dissolve
    play voice2 d1s1_mmm noloop volume 1.7
    mct "Uhhh. I guess she wants me to ask her what she's up to."
    menu:
        "Ask April what she did."(hint="sm1cs_am_renovation_m03_h01"):
            call sm1cs_am_renovation_m03_c01 from _call_sm1cs_am_renovation_m03_c01
            play voice2 mc_thinking_hmm5 noloop
            mc "Would you like to show me something, April?"
            scene sm1cs-am-58 mc-am-talk-first-choice-happy with dissolve
            play voice3 girl22_yes_aga5 noloop
            am "Mmhmm."
        "Complain to April."(hint="sm1cs_am_renovation_m03_h01"):
            call sm1cs_am_renovation_m03_c02 from _call_sm1cs_am_renovation_m03_c02
            play voice2 mc_arrogant_nah1 noloop
            mc "Can you stop screwing around April?"
            scene sm1cs-am-59 mc-am-talk-second-choice-annoyed with dissolve
            play voice3 girl22_yes_aga10 noloop
            am "Fine!"
    scene sm1cs-am-60 mc-am-talk-alt with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "I went into your internet and checked your speeds."
    am "It was alright, decent enough for what your ISP is, but it was lacking a little juice."
    scene sm1cs-am-61 mc-am-talk-proud with dissolve
    play voice3 girl22_thinking_oh noloop
    am "Took a little digging, and your neighbors might have a bit slower speed."
    am "But I managed to boost your general speed up to one Gigabit."
    play sound sfx_cloth_rustling2
    scene sm1cs-am-62 mc-am-talk-bow with dissolve
    play voice3 girl22_happy_mmm noloop
    am "You're welcome."
    scene sm1cs-am-63 mc-am-talk-respond-happy with dissolve
    play voice2 mc_happy_thatsgood noloop
    mc "That's... really cool, April."
    mc "Thank you."
    play sound sfx_heels_steps1
    scene sm1cs-am-64 mc-am-talk-put-away-laptop with dissolve
    stop sound fadeout 2.0
    play sound2 sfx_jeans_fly1 noloop
    play voice3 girl22_yes_yep5 noloop
    am "It was nothing."
    play sound sfx_cloth_rustling3
    scene sm1cs-am-65 mc-am-talk-packed-standing with dissolve
    play voice3 girl22_hey_simple noloop
    am "And if the cops come asking questions, you don't know me."
    scene sm1cs-am-66 mc-am-talk-playful-closeup with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    am "Snitches get stitches."
    scene sm1cs-am-67 mc-am-talk with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.8
    mc "Haha."
    mc "Leaving already?"
    scene sm1cs-am-68 mc-am-talk-menu with dissolve
    play voice3 girl22_yes_yeah1 noloop
    am "Yeah. I probably should go work a bit at Orbix since I took off."
    am "Unless you want to tell me the big secret about why you have a place like this."
    menu:
        "Lie"(hint="sm1cs_am_renovation_m04_h01"):
            call sm1cs_am_renovation_m04_c01 from _call_sm1cs_am_renovation_m04_c01
            play voice2 mc_thinking_hmm8 noloop
            mc "There is no big secret. I just like a lot of space."
            play sound sfx_cloth_rustling4
            scene sm1cs-am-69 mc-am-talk-first-second-choice-annoyed-not-super-happy with dissolve
            play voice3 girl22_disappointed_mmm noloop
            am "Sure, [mcname]. Very believable."
        "Promise the answer one day."(hint="sm1cs_am_renovation_m04_h02"):
            play voice2 mc_thinking_mmm4 noloop
            mc "I... I will tell you one day. I promise."
            scene sm1cs-am-70 mc-am-talk-second-choice-smile with dissolve
            play voice3 girl22_arrogant_hm noloop
            am "Don't make a girl a promise, if you know you can't keep it."
            play voice2 mc_yes_yeah1 noloop
            mc "I'll be back... {w}Cortana."
            scene sm1cs-am-71 mc-am-talk-second-choice-cool with dissolve
            play voice3 girl22_yes_aga1 noloop
            am "Cool."
    play sound sfx_heels_steps1 loop
    scene sm1cs-am-72 mc-am-talk-leaving with dissolve
    play voice3 girl22_thinking_hmm2 noloop
    am "Well good luck with the rest of the build, [mcname]."
    am "I'll see you around."
    scene sm1cs-am-73 mc-am-talk-wave-bye with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. See ya around."
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    stop sound fadeout 1.0
    stop music fadeout 3.0
    jump sm1cs_am_renovation_end
label sm1cs_am_renovation_end:
    $ renovation_controller.set_progress(renovation_controller.get_renovation_scenes_progress())
    $ renovation_controller.set_daily_limit()
    $ StoryController.end_scene_without_storyline("sm1cs_am_renovation", 2, 0, 4, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1cs_am_renovation_m01_c01:
    $ player.set_choice("sm1cs_am_renovation_insult_am")
    return
label sm1cs_am_renovation_m02_c02:
    $ player.set_choice("sm1cs_am_renovation_am_wanted_to_help")
    return
label sm1cs_am_renovation_m03_c01:
    $ player.set_choice("sm1cs_am_renovation_what_am_did")
    $ CharacterController.get_character("am").add_point(1)
    return
label sm1cs_am_renovation_m03_c02:
    $ CharacterController.get_character("am").deduct_point(1)
    return
label sm1cs_am_renovation_m04_c01:
    $ player.set_choice("sm1cs_am_renovation_lie")
    return