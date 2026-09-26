label sm1cs_ns006:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.7, 1.0, "music" )
    $ renpy.music.set_volume(1.0, 0.5, "sound4" )
    play sound4 sfx_office_ambience1 fadein 2.0 volume 0.7
    scene sm1cs-ns006-00 late_office_works_mc_thought with dissolve
    play music music_fairy_bit
    play voice2 mc_thinking_hm noloop
    mct "Okay. Time to ask Nari out on a date."
    scene sm1cs-ns006-01 late_office_works_mc_thought_nari_purse with dissolve
    mct "She's been giving me little looks all day and I don't want to disappoint her."
    play sound sfx_heels_steps2
    scene sm1cs-ns006-02 late_office_works_mc_thought_walk with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mct "The food at the place looks great, and then we'll walk down to the lighthouse under the moonlight."
    mct "It will be perfect."
    play sound sfx_chair_slide1
    scene sm1cs-ns006-03 late_office_works_ns_talk_getup_folder with dissolve
    play voice3 nari_hey_high noloop
    ns "Hello, [mcname]. Is there anything I can help you with?"
    scene sm1cs-ns006-04 late_office_works_mc_talk_about_to with dissolve
    play voice2 mc_angry_cough1 noloop
    pause
    scene sm1cs-ns006-05 late_office_works_cw_talk_popsup_surprise with dissolve
    play voice4 girl29_hey_angry noloop
    cw "Ms. Song. Mr. Young. What are you two doing right now?"
    scene sm1cs-ns006-06 late_office_works_mc_talk_awkward with dissolve
    play voice2 d1s5b_emmm noloop volume 1.4
    mc "Uh nothing."
    scene sm1cs-ns006-07 late_office_works_ns_talk_awkward with dissolve
    play voice3 nari_yes_aga2 noloop
    ns "Just getting ready to pack up for the day, Ms. Watts."
    scene sm1cs-ns006-08 late_office_works_cw_stare_nervous with dissolve
    pause
    scene sm1cs-ns006-09 late_office_works_cw_talk_mc_thought with dissolve
    play voice4 girl29_disappointed_ehh noloop
    cw "Thank god. I need you two for something."
    play voice2 mc_angry_errr8 noloop
    mct "What? I was going to take Nari out on a date."
    play sound sfx_heels_steps1 loop
    scene sm1cs-ns006-10 late_office_works_cw_talk_walk with dissolve
    play voice4 girl29_arrogant_ha noloop
    cw "Follow me to the conference room."
    scene sm1cs-ns006-11 late_office_works_cw_look_each_other with dissolve
    pause
    stop sound fadeout 1.5
    stop sound4 fadeout 2.0
    scene sm1cs-ns006-12 late_office_works_ns_mc_sitting_cw__talk_display with fade
    play voice4 girl29_thinking_hmm4 noloop
    cw "So in summation, the Orbix office in Dalton tried out a new Cloud import tool and it went berserk."
    cw "Jumbled all sorts of important files. They're looking at terabytes of confusion."
    cw "The manager asked us to lend a hand, and since Anna and April are out of the office with a client, I need your help to start tackling this."
    scene sm1cs-ns006-13 late_office_works_mc_talk with dissolve
    play voice2 d2s12_emmm noloop volume 1.2
    mc "Claire, it's already near the end of the work day."
    mc "Shouldn't we just start this on our next shift so we can focus on it?"
    scene sm1cs-ns006-14 late_office_works_cw_talk with dissolve
    play voice4 girl29_no_angry noloop
    cw "There is no time for that. This needs to be done pronto, or the Dalton office might end up hemorrhaging clients."
    scene sm1cs-ns006-15 late_office_works_cw_talk with dissolve
    play voice4 girl29_thinking_hmm3 noloop
    cw "I know it's late, and this is someone else's mess, but if you two can help, I can offer you some one-time bonuses."
    scene sm1cs-ns006-16 late_office_works_ns_talk_perk_mc_look with dissolve
    play voice3 nari_yes_yep noloop
    ns "We'll do it, Ms. Watts. You can count on us."
    scene sm1cs-ns006-17 late_office_works_cw_talk_relieved with dissolve
    play voice4 girl29_happy_relief noloop
    cw "*sighs* Oh, thank you both so much. I won't forget this."
    play sound sfx_photocamera_zoom4
    scene sm1cs-ns006-18 late_office_works_cw_turn off display with dissolve
    pause
    play sound sfx_heels_steps1 loop
    scene sm1cs-ns006-19 late_office_works_cw_talk_walk_door with dissolve
    play voice4 girl29_thinking_mmm1 noloop
    cw "Just make sure everything is locked up when you leave."
    scene sm1cs-ns006-20 late_office_works_ns_talk_cw_door with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Oh, you're not sticking around?"
    play sound sfx_door_open1
    scene sm1cs-ns006-22 late_office_works_cw_talk_straightenup with dissolve
    play voice4 girl29_no_questioning noloop
    cw "I'll check things in the morning, but I have a..."
    cw "A client meeting tonight. But I have every faith in you two."
    play sound sfx_door_closed1
    scene sm1cs-ns006-23 late_office_works_cw_door_closes with dissolve
    pause
    scene sm1cs-ns006-24 late_office_works_ns_mc_look_eachother with dissolve
    pause
    scene sm1cs-ns006-25 late_office_works_ns_talk_chuckle with dissolve
    play voice3 nari_happy_laugh1 noloop
    ns "Hehehe. Thanks for {i}volunteering{/i} with me."
    menu:
        "Be cool"(hint="sm1cs_ns006_m01_h01"):
            call sm1cs_ns006_m01_c01 from _call_sm1cs_ns006_m01_c01
            scene sm1cs-ns006-26 late_office_works_mc_talk_be_cool with dissolve
            play voice2 mc_yes_sure1 noloop
            mc "It's all good, Nari. I'm guessing you could use the extra money?"
            scene sm1cs-ns006-27 late_office_works_ns_talk_nod with dissolve
            play voice3 nari_yes_sad noloop
            ns "Every little bit helps. But I do feel bad about dragging you in with me."
            scene sm1cs-ns006-28 late_office_works_mc_talk_grin with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "There are worse things than being dragged along by a cute girl."
            scene sm1cs-ns006-29 late_office_works_ns_talk_giggle with dissolve
            play voice3 nari_happy_laugh2 noloop
            ns "*giggles*"
        "Be angry"(hint="sm1cs_ns006_m01_h02"):
            call sm1cs_ns006_m01_c02 from _call_sm1cs_ns006_m01_c02
            scene sm1cs-ns006-30 late_office_works_mc_talk_angry with dissolve
            play voice2 mc_angry_errr3 noloop
            mc "*grumbles* Thanks a lot, Nari."
            scene sm1cs-ns006-31 late_office_works_ns_talk with dissolve
            play voice3 nari_yes_aga1 noloop
            ns "Oh, you're welcome, [mcname]."
            scene sm1cs-ns006-32 late_office_works_mc_talk_angry with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "I was being sarcastic. I kind of had other plans tonight."
            scene sm1cs-ns006-33 late_office_works_ns_talk with dissolve
            play voice3 nari_disappointed_oh noloop
            ns "Oh, I'm so sorry. I just... I knew I could use help, and I can't afford to turn down extra work."
            scene sm1cs-ns006-34 late_office_works_ns_talk_beg with dissolve
            play voice3 nari_disappointed_mff noloop
            ns "I'm sure if we work together, we'll get through the work in no time."
            scene sm1cs-ns006-35 late_office_works_mc_talk_beg with dissolve
            play voice2 mc_yes_yeah9 noloop
            mc "I hope so."
    jump sm1cs_ns006_later
label sm1cs_ns006_later:
    scene black
    show screen scene_transistion("Two hours later")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene sm1cs-ns006-36 late_office_works_ns_talk_sigh_backtodesk
    with Fade(0.5, 0.5, 0.5)
    play sound sfx_keyboard_typing2
    play voice3 nari_disappointed_eeh noloop
    ns "*sighs* The Dalton branch really screwed up. I didn't think the work would be this bad."
    scene sm1cs-ns006-37 late_office_works_mc_talk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "We can do it, Nari. Just hang in there a little bit longer. The team is depending on us."
    scene sm1cs-ns006-38 late_office_works_ns_talk_bored with dissolve
    play voice3 nari_thinking_mff noloop
    ns "I know, and it's not even like the work is difficult. It's just that there is so much of it."
    ns "I can feel my brain melting away."
    scene sm1cs-ns006-39 late_office_works_mc_talk_mhhh_backtowork with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Mmm."
    play sound sfx_chair_slide1
    scene sm1cs-ns006-40 late_office_works_ns_talk_side with dissolve
    play voice3 nari_scared_ah3 noloop
    ns "[mcname]!"
    scene sm1cs-ns006-41 late_office_works_mc_talk with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene sm1cs-ns006-42 late_office_works_ns_talk with dissolve
    play voice3 nari_pain_aaa1 noloop
    ns "You don't even care that this humdrum work is making my brain dissolve? It's going to become slime and melt out of my nose!"
    play sound sfx_cloth_rustling2
    scene sm1cs-ns006-43 late_office_works_mc_talk_handhip with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Of course I care."
    mc "I just... don't really know of a solution."
    mc "What do you usually do when you face a problem like this?"
    scene sm1cs-ns006-44 late_office_works_ns_talk_relaxes with dissolve
    play voice3 nari_thinking_hmm1 noloop
    ns "Hmmm."
    scene sm1cs-ns006-45 late_office_works_mc_talk with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Is there something else you can focus on? Or some music you like to listen to?"
    scene sm1cs-ns006-46 late_office_works_ns_talk_horny with dissolve
    play voice3 nari_sex_closedmoan2 noloop
    ns "Hmm."
    scene sm1cs-ns006-47 late_office_works_mc_talk with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "I think you're focusing on something inappropriate."
    scene sm1cs-ns006-48 late_office_works_ns_talk with dissolve
    play voice3 nari_yes_emotional noloop
    ns "Oh yes. Very inappropriate."
    play sound sfx_cloth_rustling3
    scene sm1cs-ns006-49 late_office_works_ns_talk_lean_thigh with dissolve
    play voice3 nari_thinking_emm noloop
    ns "I think, if I just have a little {i}fun{/i}... I'll be able to think clearer and finish the work faster."
    scene sm1cs-ns006-50 late_office_works_mc_talk_grinning with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Hmmm. Claire would want us working at our best."
    if player.get_choice("sm1cs_cw001_promise"):
        scene sm1cs-ns006-51 late_office_works_f_false_mc_talk with dissolve
        play voice2 mc_thinking_mmm5 noloop
        mc "But I really shouldn't. I promised Claire I wouldn't do anything in the office."
        scene sm1cs-ns006-52 late_office_works_f_false_ns_talk_surprised with dissolve
        play voice3 nari_surprised_huh1 noloop
        ns "Wait, does Ms. Watts know we did stuff in the bathroom?"
        scene sm1cs-ns006-53 late_office_works_f_false_mc_talk with dissolve
        play voice2 mc_no_no9 noloop
        mc "I don't think she saw us, but she certainly suspects something."
        scene sm1cs-ns006-54 late_office_works_f_false_ns_talk_chew_finger with dissolve
        play voice3 nari_pain_aaa3 noloop
        pause
        scene sm1cs-ns006-55 late_office_works_f_false_ns_talk_determined with dissolve
        play voice3 nari_disappointed_huh noloop
        ns "It's fine, [mcname]. It can be our secret."
        ns "It will just be a one-time thing."
        scene sm1cs-ns006-56 late_office_works_f_false_mc_talk_thought with dissolve
        play voice2 d1s1_mmm noloop
        mct "By the look in her eyes, I doubt that is true."
        scene sm1cs-ns006-57 late_office_works_mc_talk_rub_hip with dissolve
        play voice2 mc_yes_okay2 noloop
        mc "Okay. Just this one time."
    scene sm1cs-ns006-58 late_office_works_ns_talk with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Come here."
    play sound sfx_cloth_rustling4
    scene sm1cs-ns006-59 late_office_works_ns_onlap with dissolve
    play voice3 nari_sex_closedmoan6 noloop
    ns "*soft moan*"
    scene sm1cs-ns006-60 late_office_works_ns_talk_hair with dissolve
    play voice3 nari_happy_laugh3 noloop
    ns "Hehehe."
    scene sm1cs-ns006-61 late_office_works_handback with dissolve
    pause
    scene sm1cs-ns006-62 late_office_works_kiss with dissolve
    play voice3 nari_sex_closedmoan3 noloop
    play voice2 mc_thinking_mmm1 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-ns006-63 late_office_works_kiss with dissolve
    play voice3 nari_sex_closedmoan4 noloop
    play sound mc_kiss2
    ns "Mrmmm-ammmm."
    scene sm1cs-ns006-64 late_office_works_ns_talk_pullaway with dissolve
    play voice3 nari_hey_unsure noloop
    ns "*whispers* I-I... I want you in my mouth."
    scene sm1cs-ns006-65 late_office_works_mc_talk with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Yes. Anything else?"
    scene sm1cs-ns006-66 late_office_works_ns_talk with dissolve
    play voice3 nari_disgust_brrgh noloop
    ns "I want you to make me sticky... all over. Ooouhaah..."
    play sound sfx_jeans_on1
    scene sm1cs-ns006-67 late_office_works_ns_talk_onknees with dissolve
    queue voice3 nari_angry_breathing noloop
    ns "*shivering breaths*"
    play sound2 sfx_skirt_off1 noloop
    scene sm1cs-ns006-68 late_office_works_ns_talk_cockout with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Mmmm."
    scene sm1cs-ns006-69 late_office_works_ns_talk_strokelook with dissolve
    play voice3 nari_sex_closedmoan1 noloop
    ns "Ahuuaah..."
    scene sm1cs-ns006-70 late_office_works_ns_lick with dissolve
    play voisex3 nari_sex_sucking1
    play voisex2 mc_sex_openmoans1
    pause
    scene sm1cs-ns006-71 late_office_works_ns_lick_lickotherpart with dissolve
    pause
    stop voisex2 fadeout 1.0
    play voisex3 nari_sex_openmoans1 noloop
    scene sm1cs-ns006-72 late_office_works_ns_talk with dissolve
    stop voice3 fadeout 1.5
    ns "So warm. And tasty."
    scene sm1cs-ns006-73 late_office_works_ns_talk with dissolve
    play voice3 nari_thinking_hmm3 noloop
    ns "Just like last time."
    scene sm1cs-ns006-74 late_office_works_ns_mouth with dissolve
    play voisex3 nari_sex_sucking1
    play voisex2 mc_sex_openmoans1
    pause
    scene sm1cs-ns006-75 late_office_works_mc_thought with dissolve
    mct "Yes. Oh that feels great."
    stop voisex3 fadeout 1.0
    stop voisex2 fadeout 1.0
    play sound sfx_door_open7
    scene sm1cs-ns006-76 late_office_works_mc_ns_hear_noise with dissolve
    "Door opening"
    play voice3 nari_surprised_huh2 noloop
    ns "Huah?"
    scene sm1cs-ns006-78 late_office_works_mc_talk with dissolve
    play voice2 mc_scared_huuuh3 noloop
    mc "Shit. Someone is coming."
    scene sm1cs-ns006-79 late_office_works_ns_talk with dissolve
    pause
    play sound sfx_barefoot_run1
    scene sm1cs-ns006-80 late_office_works_ns_crawl_mc_pants with dissolve
    stop sound fadeout 4.0
    pause
    scene sm1cs-ns006-81 late_office_works_mc_thought with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "The fuck?"
    play sound sfx_heels_steps2 loop
    scene sm1cs-ns006-82 late_office_works_mj_talk with dissolve
    play voice4 girl35_thinking_oh2 noloop
    mj "Oh hi, [mcname]. I didn't realize anyone was still here."
    scene sm1cs-ns006-83 late_office_works_mc_talk with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh hey."
    stop sound fadeout 1.0
    scene sm1cs-ns006-84 late_office_works_ns_talk_appear with dissolve
    play voice3 nari_hey_asking noloop
    ns "Hello Megan. How are you?"
    scene sm1cs-ns006-85 late_office_works_mj_talk with dissolve
    play voice4 girl35_surprised_oh2 noloop
    mj "Oh. Sorry, Nari, I didn't see you there."
    mj "You look a little flush."
    scene sm1cs-ns006-86 late_office_works_ns_talk with dissolve
    play voice3 nari_disappointed_eh noloop
    ns "Uh... it's just this work Claire gave us. It's like untying a thousand digital knots."
    scene sm1cs-ns006-87 late_office_works_mj_talk with dissolve
    play voice4 girl35_yes_yeah1 noloop
    mj "Yeah, Claire mentioned it was a bit of a pickle."
    mj "The Dalton branch really is the worst."
    scene sm1cs-ns006-88 late_office_works_mj_talkmpressed with dissolve
    play voice4 girl35_hey_long noloop
    mj "But never fear, Megan the Amazing is here to save you."
    scene black
    show screen scene_transistion("A few minutes later")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene sm1cs-ns006-90 late_office_works_mj_talk_desk
    with Fade(0.5, 0.5, 0.5)
    play sound sfx_keyboard_typing2
    pause
    play voice4 girl35_angry_err2 noloop
    mj "I give up. This is way harder than my normal work."
    scene sm1cs-ns006-91 late_office_works_mc_talk with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Well, maybe you should just leave it to us then."
    scene sm1cs-ns006-92 late_office_works_ns_like with dissolve
    pause
    play sound sfx_chair_slide1
    scene sm1cs-ns006-93 late_office_works_mj_talk_actionpose with dissolve
    play voice4 girl35_no_angry2 noloop
    mj "No way. If I can't help on the computer, I'll make sure you two are fueled up to tackle this problem."
    scene sm1cs-ns006-94 late_office_works_ns_talk with dissolve
    play voice3 nari_thinking_oh noloop
    ns "*sarcastically* Oh, that sounds lovely."
    scene sm1cs-ns006-95 late_office_works_mj_talk_thumbup with dissolve
    play voice4 girl35_yes_aga7 noloop
    mj "I'm kind of a night owl so I've always got more energy late at night like tonight."
    play sound sfx_heels_steps2 loop
    scene sm1cs-ns006-96 late_office_works_mj_walks_kitchen with dissolve
    pause
    stop sound fadeout 2.0
    scene sm1cs-ns006-97 late_office_works_ns_talk_lean with dissolve
    play voice3 nari_angry_fff noloop
    ns "Looks like she ruined our date night."
    scene sm1cs-ns006-98 late_office_works_mc_talk with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Uh huh."
    play sound sfx_keyboard_typing2
    scene sm1cs-ns006-99 late_office_works_mc_thought_look_screen with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mct "Although technically Claire ruined it first. We'll just have to make plans another night."
    mct "Still, maybe Nari and I can be sneaky."
    scene black
    show screen scene_transistion("Another few minutes later")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene sm1cs-ns006-100 late_office_works_mc_thought_look_screen
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_arrogant_heh2 noloop
    mct "Now is our chance to sneak into the bathroom."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-ns006-101 late_office_works_sneaking_bathroom with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-ns006-102 late_office_works_mj_talk_outofnowhere with dissolve
    play voice4 girl35_hey_laughing noloop
    mj "Snack break! I've got crackers with turkey or crackers and cheese!"
    scene sm1cs-ns006-103 late_office_works_ns_talk_bathroom with dissolve
    play voice3 nari_happy_relief noloop
    ns "I need to use the toilet."
    scene sm1cs-ns006-104 late_office_works_mc_talk_bathroom with dissolve
    play voice2 d3s7_mcemm noloop volume 1.6
    mc "And uh... I was just stretching."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-ns006-105 late_office_works_mj_talk_alone with dissolve
    play voice4 girl35_yes_yeah6 noloop
    mj "Alright. More for me."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-ns006-106 late_office_works_mc_talk_whisper with fade
    play voice2 mc_hey_hey2 noloop
    mc "*whispers* Any sign of her?"
    scene sm1cs-ns006-107 late_office_works_ns_talk_whisper with dissolve
    play voice3 nari_no_sad noloop
    ns "*whispers* No, I think she's gone."
    scene sm1cs-ns006-108 late_office_works_mc_talk with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Conference room."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-ns006-109 late_office_works_walk_to_conference with dissolve
    pause
    stop sound2 fadeout 1.0
    play sound sfx_door_open1
    scene sm1cs-ns006-110 late_office_works_shock with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "Oh come on."
    scene sm1cs-ns006-111 late_office_works_mj_talk with dissolve
    play voice4 girl35_surprised_oh5 noloop
    mj "There you two are. You looked like you were really stressed so I decided we could do a quick game break."
    play sound sfx_cup_slide1
    scene sm1cs-ns006-112 late_office_works_mj_talk_cup with dissolve
    play voice4 girl35_happy_laugh1 noloop
    mj "Who loves Yahtzee?"
    scene sm1cs-ns006-113 late_office_works_mc_talk with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "Uh... I can't play Yahtzee. At night. Sorry, Megan."
    scene sm1cs-ns006-114 late_office_works_mj_talk with dissolve
    play voice4 girl35_surprised_what5 noloop
    mj "What? Why not?"
    scene sm1cs-ns006-115 late_office_works_mc_talk with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Uh, family curse. My great uncle Mortimor died after playing Yahtzee at night. So I'll have to take a rain check."
    scene sm1cs-ns006-116 late_office_works_mj_talk with dissolve
    play voice4 girl35_surprised_oh4 noloop
    mj "Ah that's too bad. Nari? What about you? Girl's night?"
    scene sm1cs-ns006-117 late_office_works_ns_talk with dissolve
    play voice3 nari_no_nah noloop
    ns "I uh... I'd love to, but it's probably better if we just... focus on our work."
    scene sm1cs-ns006-118 late_office_works_mj_talk_ms_ns_leave with dissolve
    play voice4 girl35_yes_yep2 noloop
    mj "Okay, another time then."
    mj "Well come on you two, let's get back to it."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-ns006-119 late_office_works_mc_thought_walkback_defeated with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mct "I guess no fun tonight."
    mct "Only work."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-ns006-120 late_office_works_mj_talk_mc_tired_ns_purse_mj_wave with fade
    play voice4 girl35_hey_bye3 noloop
    mj "Night you two. See you next time."
    scene sm1cs-ns006-121 late_office_works_ns_talk with dissolve
    play voice3 nari_yes_yeah noloop
    ns "Bye Megan."
    scene sm1cs-ns006-122 late_office_works_ns_talk_mc_nari_door_tired with dissolve
    play voice3 nari_disappointed_woof noloop
    ns "*sleepy* I am going to go home and crash. I'm so tired I won't even be able to check my stocks and crypto."
    scene sm1cs-ns006-123 late_office_works_mc_talk with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.4
    mc "Haha. Get some sleep, Nari. Hopefully next time, our luck will be better."
    scene sm1cs-ns006-124 late_office_works_ns_talk with dissolve
    play voice3 nari_yes_sad noloop
    ns "*sleepy* Yes. I want to sleep with [mcname]."
    ns "Stupid helpful Megan."
    scene sm1cs-ns006-125 late_office_works_mc_talk_laugh with dissolve
    play voice2 d4s4_mclaugh noloop
    mc "Haha. Get home safe, Nari."
    play sound2 sfx_heels_steps2
    scene sm1cs-ns006-126 late_office_works_ns_talk_back with dissolve
    play voice3 nari_happy_mmm noloop
    ns "Ni-ni, [mcname]."
    stop sound2 fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    jump sm1cs_ns006_end
label sm1cs_ns006_end:
    $ StoryController.end_scene_in_time(NS_STORY, 22, 30, 6, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1cs_ns006_m01_c01:
    $ player.set_choice("sm1cs_ns006_be_cool")
    $ CharacterController.get_character("ns").add_point()
    return
label sm1cs_ns006_m01_c02:
    $ player.set_choice("sm1cs_ns006_get_angry")
    $ CharacterController.get_character("ns").deduct_point(2)
    return