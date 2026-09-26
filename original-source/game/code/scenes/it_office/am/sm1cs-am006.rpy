label sm1cs_am006:
    $ renpy.music.set_volume(0.54, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    scene am006-00 arcade_fun_mc_talk_standing_frontof_am with dissolve
    play music music_bits_of_calm fadein 2.5
    play voice2 mc_happy_yay2 noloop
    mc "April."
    scene am006-01 arcade_fun_am_talk_standing_frontof_am with dissolve
    play sound sfx_keyboard_typing2 loop
    play voice3 girl22_yes_questioning noloop
    am "Yes?"
    scene am006-02 arcade_fun_mc_talk with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I figured out a place for our date."
    scene am006-03 arcade_fun_am_talk with dissolve
    play voice3 girl22_yes_aga1 noloop
    am "Cool."
    stop sound fadeout 1.5
    scene am006-04 arcade_fun_mc_talk with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "You don't seem very excited."
    play sound2 sfx_cloth_rustling2 noloop
    scene am006-05 arcade_fun_am_talk with dissolve
    play voice3 girl22_no_simple noloop
    am "For your information, I am very excited."
    am "I'm just also super pissed off because Claire couldn't convince a customer to stop shitting the bed."
    am "Now, because Claire couldn't convince an idiot to take my infinitely better advice, I have to restructure two thousand lines of code."
    scene am006-06 arcade_fun_mc_talk with dissolve
    menu:
        "That really sucks."(hint="sm1cs_am006_m01_h01"):
            call sm1cs_am006_m01_c01 from _call_sm1cs_am006_m01_c01
            play voice2 mc_disappointed_off1 noloop
            mc "That really sucks."
            scene am006-07 arcade_fun_am_talk with dissolve
            play voice3 girl22_yes_yeah3 noloop
            am "Yeah. Looks like today, I'll be wasting a bunch of time for Orbix instead of the usual suspect."
            scene am006-08 arcade_fun_mc_talk with dissolve
            play voice2 d3s11b_mcheh noloop volume 1.6
            mc "Haha. Yeah."
            scene am006-09 arcade_fun_am_talk with dissolve
            play voice3 girl22_thinking_hmm1 noloop
            am "I mean you, [mcname]."
            scene am006-10 arcade_fun_mc_talk with dissolve
            play voice2 mc_thinking_oh1 noloop
            mc "Oh."
            mc "Thanks."
            scene am006-11 arcade_fun_am_talk_laugh with dissolve
            play voice3 girl22_happy_laugh1 noloop
            am "Haha."
        "Isn't the customer always right?"(hint="sm1cs_am006_m01_h02"):
            play voice2 mc_surprised_uh1 noloop
            mc "Isn't the customer always lying?"
            scene am006-07 arcade_fun_am_talk with dissolve
            play voice3 girl22_no_nonono1 noloop
            am "Absolutely not. And euphemisms like that try to make those capable of critical thinking bow to the dumbest among us."
            am "It's a false statement even from a statistical standpoint."
            am "No one is right one hundred percent of the time."
            am "Especially humans. Our failure rate is depressingly high."
            scene am006-12 arcade_fun_mc_talk with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "Well at least we have minds like yours to help out our numbers."
            scene am006-13 arcade_fun_am_talk with dissolve
            play voice3 girl22_happy_laugh1 noloop
            am "Heh."
    scene am006-15 arcade_fun_am_talk_look with dissolve
    play voice3 girl22_surprised_huh2 noloop
    am "Anyhow, you were saying something about our date?"
    am "Make it quick, I need to get back to this slog soon."
    scene am006-16 arcade_fun_mc_talk with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Yes. I just hope that you'll like this place for our date."
    mc "It's the arcade downtown. I've always enjoyed going there."
    scene am006-17 arcade_fun_am_talk_teaselook with dissolve
    play voice3 girl22_surprised_what noloop
    am "How old are you?"
    scene am006-18 arcade_fun_mc_talk with dissolve
    play voice2 d2s12_emmm noloop volume 1.67
    mc "I'm-"
    play sound sfx_cloth_rustling1
    scene am006-19 arcade_fun_am_talk_wavehand with dissolve
    play voice3 girl22_no_uhuh1 noloop
    am "That was rhetorical."
    scene am006-20 arcade_fun_am_talk_softenlook with dissolve
    play voice3 girl22_thinking_hmm2 noloop
    am "Just text me the details, and I'll meet you there."
    scene am006-21 arcade_fun_am_lookcomputer with dissolve
    pause
    scene am006-22 arcade_fun_am_talk_lookback with dissolve
    play voice3 girl22_hey_simple noloop
    am "Are you going to wear something nice?"
    scene am006-23 arcade_fun_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Of course."
    scene am006-24 arcade_fun_mc_talk_look_clothes with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Well, nicer than this, anyhow."
    play sound sfx_cloth_rustling2
    scene am006-25 arcade_fun_am_talk_lookcomputer with dissolve
    play voice3 girl22_yes_aga4 noloop
    am "Okay. I'll plan accordingly."
    play sound sfx_mouse_clicks1
    scene am006-26 arcade_fun_mc_talk_am_workmode with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What does that mean?"
    mct "Looks like I lost her."
    play sound sfx_chair_slide1
    scene am006-27 arcade_fun_mc_thought_phone with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mct "I bet that she'll really enjoy the date after doing that work for Claire."
    mct "Or this will end up a disaster like after I saw her play."
    jump sm1cs_am006_arcade
label sm1cs_am006_arcade:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    stop music fadeout 3.0
    scene black
    show screen scene_transistion(_("In the evening at the arcade"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.0, 3.5, "music" )
    $ renpy.music.set_volume(0.8, 0.5, "music2" )
    scene am006-28 arcade_fun_mc_talk_meet_arcade
    $ renpy.music.play(audio.music_game_business, "music" , True, None, True, 1.5)
    $ renpy.music.play(audio.music_game_business_radio, "music2", True, None, True, 1.5)
    play sound4 sfx_casino_ambience1 fadein 3.0 volume 0.7
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_surprised_wow4 noloop
    mc "You look really nice, April."
    scene am006-29 arcade_fun_am_talk_fun with dissolve
    play voice3 girl22_arrogant_he noloop
    am "So the best programmer at Orbix is just another pretty face to you?"
    scene am006-30 arcade_fun_mc_talk_surprised with dissolve
    play voice2 mc_no_no6 noloop
    mc "No I just-"
    menu:
        "You're messing with me, aren't you?"(hint="sm1cs_am006_m02_h01"):
            call sm1cs_am006_m02_c01 from _call_sm1cs_am006_m02_c01
            scene am006-31 arcade_fun_mc_talk_beteased with dissolve
            play voice2 mc_hey_hey3 noloop
            mc "You're messing with me, aren't you."
            scene am006-32 arcade_fun_am_talk with dissolve
            play voice3 girl22_arrogant_hm noloop
            am "So when there is broken code, you need help, but when I'm trying to pull a fast one, you're on top of things."
            scene am006-33 arcade_fun_mc_talk_cool with dissolve
            play voice2 mc_thinking_mmm7 noloop
            mc "Well if you don't want me to be on top, I can play dumb."
            scene am006-34 arcade_fun_am_talk_blush with dissolve
            play voice3 girl22_surprised_eh2 noloop
            am "That's not what I-"
            play voice3 girl22_happy_laugh4 noloop
            scene am006-35 arcade_fun_am_talk_straighten with dissolve
            am "Shut up. *chuckles*"
        "You look great."(hint="sm1cs_am006_m02_h02"):
            call sm1cs_am006_m02_c02 from _call_sm1cs_am006_m02_c02
            scene am006-31 arcade_fun_mc_talk_beteased with dissolve
            play voice2 mc_hey_hey3 noloop
            mc "You look great, April."
            scene am006-36 arcade_fun_am_talk_pretendmad with dissolve
            play voice3 girl22_yes_aga5 noloop
            am "I'm far more than just a cut of fuckable meat, [mcname]."
            scene am006-37 arcade_fun_mc_talk_reallythink with dissolve
            play voice2 mc_yes_yes7 noloop
            mc "I know, that's why I said you look 'great'."
            mc "And did you really think I'd use a line from Cyberpunk 2077 on you?"
            scene am006-38 arcade_fun_am_talk_realize with dissolve
            play voice3 girl22_happy_mmm noloop
            am "Mmmm."
            am "Maybe I've been hanging around Anna too much."
        "I'm glad we both look good"(hint="sm1cs_am006_m02_h03"):
            call sm1cs_am006_m02_c03 from _call_sm1cs_am006_m02_c03
            scene am006-39 arcade_fun_mc_talk_pose with dissolve
            play voice2 mc_happy_hah2 noloop
            mc "We're both looking good, and that's just my style."
            mc "Nothing wrong with that, right?"
            scene am006-40 arcade_fun_am_talk_thrownoff with dissolve
            play voice3 girl22_disappointed_geh noloop
            am "Whatever. We both could have worn pajamas for all I care."
    scene am006-41 arcade_fun_am_talk_lookaround with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "I'm surprised you picked this place."
    scene am006-42 arcade_fun_mc_talk with dissolve
    play voice2 mc_surprised_why3 noloop
    mc "Why?"
    scene am006-43 arcade_fun_am_talk_bratty with dissolve
    play voice3 girl22_happy_laugh3 noloop
    am "*chuckles* It definitely reinforces my assumption that you're just some manchild who has never really developed mentally."
    scene am006-44 arcade_fun_mc_talk_what with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What?"
    scene am006-45 arcade_fun_am_talk_what with dissolve
    play voice3 girl22_arrogant_yeah noloop
    am "Yeah, I mean, why else would you be at Orbix, making a half-ass attempt at becoming a real coder."
    scene am006-46 arcade_fun_mc_talk_mad with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "First, I always full-ass everything I do."
    mc "And second, maybe it's been a minute for you, but on most dates, usually you don't start by insulting your date."
    play sound sfx_heels_steps2 loop
    scene am006-47 arcade_fun_mc_movesaway_am_handup with dissolve
    mc "..."
    play voice3 girl22_disappointed_mmf noloop
    am "[mcname]..."
    scene am006-48 arcade_fun_mc_lookforgame with dissolve
    pause
    play sound [sfx_gambling_coin1, sfx_gambling_lever1]
    scene am006-49 arcade_fun_mc_findsarcade_putcoin with dissolve
    pause
    play sound2 sfx_gambling_knobs1
    scene am006-50 arcade_fun_mc_playingscreen with dissolve
    pause
    scene am006-51 arcade_fun_am_talk_joins with dissolve
    play voice3 girl22_angry_cough noloop
    am "*clears throat*"
    scene am006-52 arcade_fun_mc_talk_glance with dissolve
    pause
    scene am006-53 arcade_fun_am_talk with dissolve
    play voice3 girl22_hey_scared noloop
    am "I know I can be a lot. That's what you're thinking, right?"
    scene am006-54 arcade_fun_am_talk_notlooking with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "You know that a lot of my job is focused on security."
    am "And sometimes, it's not easy to approach things with an open mind."
    scene am006-55 arcade_fun_am_talk_foldarms with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "I have to remember the golden rule."
    am "If your shields are up, no one can come aboard and talk to you."
    scene am006-56 arcade_fun_mc_talk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "So. These shields. They're down now?"
    scene am006-57 arcade_fun_am_talk_grin with dissolve
    play voice3 girl22_happy_relief noloop
    am "Let's say they're at half power."
    scene am006-58 arcade_fun_mc_talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "When was the last time you brought them down?"
    scene am006-59 arcade_fun_am_look_thinking with dissolve
    am "..."
    stop sound2 fadeout 1.0
    scene am006-60 arcade_fun_am_point with dissolve
    play voice3 girl22_no_uhuh5 noloop
    am "I'm not that easy, [mcname]."
    scene am006-61 arcade_fun_mc_talk with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "The last time we were out, you asked me to fuck you in your car."
    scene am006-62 arcade_fun_am_mischevious with dissolve
    play voice3 girl22_angry_hmm noloop
    am "I told you, I was just pent up from the music and-"
    am "And in the end, I remembered to stop myself."
    scene am006-63 arcade_fun_am_talk_normal with dissolve
    play voice3 girl22_arrogant_pff noloop
    am "Listen to you, just airing my dirty laundry out in public."
    scene am006-64 arcade_fun_am_talk_lookaround with dissolve
    pause
    scene am006-63 arcade_fun_am_talk_normal with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "You're lucky no one was close enough to hear you say that."
    scene am006-65 arcade_fun_am_talk_noticegame with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "Hmmm."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene am006-66 arcade_fun_am_talk_grabmc with dissolve
    play voice3 girl22_yes_aga6 noloop
    am "Come on."
    scene am006-67 arcade_fun_mc_talk_grabmc with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Alright."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene am006-68 arcade_fun_am_talk_grabmc with dissolve
    play voice3 girl22_surprised_eh1 noloop
    am "Buy me a round or two of skeeball, and maybe I'll tell you about the last time I lowered my shields."
    scene am006-69 arcade_fun_mc_talk_chuckles with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.7
    mc "*chuckles*"
    play sound sfx_gambling_coin1
    scene am006-70 arcade_fun_mc_coin with dissolve
    pause
    scene am006-71 arcade_fun_mc_thought_looking_machine with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "I remember this machine. It's easier to throw into the big rings but you get the most points by throwing the ball into the smaller rings."
    scene am006-72 arcade_fun_mc_thought_showrings with dissolve
    $ renpy.music.set_volume(0.3, 5.5, "music" )
    $ renpy.music.set_volume(0.5, 5.5, "music2" )
    mct "Of course, the smaller rings are harder to hit."
    scene am006-73 arcade_fun_mc_thought_ballsready with dissolve
    pause
    play sound sfx_vending_cola
    scene am006-74 arcade_fun_am_talk_grabball with dissolve
    play voice3 girl22_yes_yep1 noloop
    am "We'll go in threes."
    play sound sfx_skeeball_rolling1
    scene am006-75 arcade_fun_am_throwball with dissolve
    pause
    play sound sfx_skeeball_goal1
    scene am006-76 arcade_fun_am_bigcircle with dissolve
    pause
    scene am006-77 arcade_fun_am_frustrated with dissolve
    play voice3 girl22_disappointed_oh noloop
    pause
    play sound sfx_skeeball_rolling2
    scene am006-78 arcade_fun_am_throwball with dissolve
    pause
    play sound sfx_skeeball_goal2
    scene am006-79 arcade_fun_am_bigcircle with dissolve
    pause
    scene am006-80 arcade_fun_am_talk_prepare with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "I'm a little rusty."
    scene am006-81 arcade_fun_mc_talk with dissolve
    play voice2 d1s5_mchappy noloop volume 2.3
    mc "You know you're supposed to go for the smaller holes."
    scene am006-82 arcade_fun_am_talk_snakeeyes with dissolve
    play voice3 girl22_arrogant_ha noloop
    am "And you know you're never going to see my smaller hole acting like that."
    play sound sfx_throw_something1 volume 2.0
    play sound2 [sfx_skeeball_bounce1, sfx_skeeball_bounce2, sfx_skeeball_bounce3] volume 2.5 noloop
    scene am006-83 arcade_fun_am_toss_almost with dissolve
    pause
    play sound2 [sfx_skeeball_bounce4, sfx_skeeball_bounce5, sfx_skeeball_bounce6] volume 2.5 noloop
    scene am006-84 arcade_fun_am_toss_bouncedown with dissolve
    pause
    play sound sfx_skeeball_bounce8
    play sound2 sfx_skeeball_goal3 noloop
    scene am006-85 arcade_fun_am_toss_bouncedown_bigcircle with dissolve
    pause
    scene am006-86 arcade_fun_am_talk with dissolve
    play voice3 girl22_angry_argh3 noloop
    am "Fuck."
    play sound sfx_gambling_print1
    scene am006-87 arcade_fun_tickets_out with dissolve
    pause
    play sound2 sfx_handwork_flowerbreak1 noloop
    scene am006-88 arcade_fun_am_talk_tickets_out with dissolve
    play voice3 girl22_yes_aga11 noloop
    am "You're up."
    play sound sfx_vending_cola
    scene am006-89 arcade_fun_mc_talk_ball with dissolve
    play voice2 mc_thinking_hmm6 noloop volume 1.6
    mc "I think I know the problem."
    scene am006-90 arcade_fun_am_talk with dissolve
    play voice3 girl22_disgust_meeh noloop
    am "It's gotta be you. When I do this alone, I always score way higher."
    scene am006-91 arcade_fun_mc_talk with dissolve
    play voice2 d9s2_yeah noloop volume 2.7
    mc "That might be it. Or it's because you're not really letting yourself relax."
    play sound sfx_skeeball_rolling1
    scene am006-92 arcade_fun_mc_toss with dissolve
    pause
    play sound sfx_skeeball_goal1
    scene am006-93 arcade_fun_mc_smallhole with dissolve
    pause
    scene am006-94 arcade_fun_mc_talk with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "I was watching you. Your body was so stiff and tense."
    scene am006-95 arcade_fun_am_talk_crossarm with dissolve
    play voice3 girl22_angry_dagh noloop
    am "I know how to throw a fucking ball."
    play sound sfx_skeeball_rolling2
    scene am006-96 arcade_fun_mc_toss with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah, sounds like you're totally relaxed."
    play sound sfx_skeeball_goal3
    scene am006-97 arcade_fun_mc_talk_secondhole with dissolve
    pause
    scene am006-98 arcade_fun_am_talk_grumbling with dissolve
    play voice3 girl22_angry_heergh noloop
    am "*grumbles* You're just lucky."
    scene am006-99 arcade_fun_mc_talk_holdball with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Once is lucky. Twice is good."
    play sound sfx_skeeball_rolling3
    scene am006-100 arcade_fun_mc_talk_toss with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Three times is-"
    play sound sfx_skeeball_goal2
    scene am006-101 arcade_fun_mc_talk_highesthole with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Major skills."
    play sound sfx_gambling_print2
    scene am006-102 arcade_fun_mc_ticketscomeout with dissolve
    pause
    play sound2 sfx_handwork_flowerbreak1 noloop
    stop sound fadeout 1.5
    scene am006-103 arcade_fun_mc_talk_gettickets with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "I think I won that match."
    mc "You going to tell me the last time you lowered your shields?"
    scene am006-104 arcade_fun_am_embarassed with dissolve
    pause
    scene am006-105 arcade_fun_am_talk_shakehead with dissolve
    play voice3 girl22_no_nope3 noloop
    am "No way. Best two out of three."
    $ renpy.music.set_volume(0.85, 3.5, "music" )
    $ renpy.music.set_volume(0.0, 5.5, "music2" )
    $ renpy.music.set_volume(0.0, 1.5, "sound4" )
    play sound sfx_skeeball_rolling2
    scene am006-106 arcade_fun_monstage with fade
    pause
    play sound sfx_skeeball_goal1
    scene am006-107 arcade_fun_monstage with dissolve
    pause
    play sound sfx_skeeball_rolling1
    scene am006-108 arcade_fun_monstage with dissolve
    pause
    play sound sfx_skeeball_goal2
    scene am006-109 arcade_fun_monstage with dissolve
    pause
    play sound sfx_airhockey_smash2
    scene am006-110 arcade_fun_monstage with dissolve
    pause
    play sound sfx_airhockey_smash3
    scene am006-111 arcade_fun_monstage with dissolve
    pause
    play sound sfx_airhockey_smash1
    scene am006-112 arcade_fun_monstage with dissolve
    pause
    $ renpy.music.set_volume(0.0, 5.5, "music" )
    $ renpy.music.set_volume(0.8, 3.5, "music2" )
    $ renpy.music.set_volume(1.0, 1.5, "sound4" )
    play sound3 sfx_airhockey_hum fadein 1.0
    play sound sfx_airhockey_score1
    scene am006-113 arcade_fun_mc_talk_cantstop with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "Damn."
    play voice3 girl22_happy_yay noloop
    play sound sfx_phone_fall1 volume 0.6
    scene am006-114 arcade_fun_am_talk_cheer with hpunch
    stop sound fadeout 0.5
    am "Yes! Wooh. She shoots, she scores!"
    am "Mercer takes the gold!"
    play sound sfx_heels_steps1
    scene am006-115 arcade_fun_am_talk_goes_uptomc with dissolve
    play voice3 girl22_arrogant_huh noloop
    am "You like that?"
    play sound sfx_throw_something1
    scene am006-116 arcade_fun_am_talk_handface with dissolve
    play voice3 girl22_angry_argh1 noloop
    am "In your face! In your stupid handsome face!"
    scene am006-117 arcade_fun_am_talk_realizes with dissolve
    play voice3 girl22_disappointed_ah noloop
    am "Umm."
    scene am006-118 arcade_fun_mc_talk with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Having fun?"
    scene am006-119 arcade_fun_am_talk with dissolve
    play voice3 girl22_yes_yeah1 noloop
    am "Oh yeah. Forget I said anything."
    scene am006-120 arcade_fun_mc_talk with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh, totally."
    mc "You think I'm handsome."
    scene am006-121 arcade_fun_am_talk with dissolve
    play voice3 girl22_disappointed_oof noloop
    am "Shut up. No, I don't."
    play sound sfx_cloth_rustling2
    scene am006-122 arcade_fun_am_talk_embarrassed_pose with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    am "Can you get me a beer, that will help me relax."
    scene am006-123 arcade_fun_mc_talk_walks with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure. And then someone owes me some answers."
    play sound sfx_heels_steps2 loop
    scene am006-124 arcade_fun_am_talk_walks with dissolve
    play voice3 girl22_hey_happy noloop
    am "But I won."
    scene am006-125 arcade_fun_mc_talk_walking with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah the last one, what about the four I won?"
    mc "*chuckles*"
    scene am006-126 arcade_fun_am_worried with dissolve
    pause
    stop sound fadeout 3.0
    $ renpy.music.set_volume(0.0, 5.5, "music" )
    $ renpy.music.set_volume(0.0, 20.5, "music2" )
    $ renpy.music.set_volume(0.7, 20.5, "music3" )
    $ renpy.music.set_volume(0.45, 3.5, "sound4" )
    stop sound3 fadeout 3.0
    scene am006-127 arcade_fun_mc_talk_beer_fries with fade
    play sound sfx_beer_open1
    play voice2 d1s2_hmm noloop volume 1.7
    mc "So spill it. When was the last time you let your shields down?"
    scene am006-128 arcade_fun_am_talk with dissolve
    play voice3 girl22_disappointed_mmf noloop
    am "Ummm."
    play sound2 sfx_cloth_rustling4 noloop
    play sound sfx_drink_loop1 volume 2.3
    scene am006-129 arcade_fun_am_talk_beer with dissolve
    pause
    stop sound fadeout 1.0
    scene am006-130 arcade_fun_am_talk_beer with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "I guess that night with you after my band played."
    scene am006-131 arcade_fun_mc_talk with dissolve
    play voice2 mc_no_no5 noloop
    mc "Come on. Not that one. I was there for that one."
    scene am006-132 arcade_fun_am_talk_nervous with dissolve
    play voice3 girl22_sex_closedmoan3 noloop
    am "I... I don't really remember."
    scene am006-133 arcade_fun_mc_talk with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay liar."
    scene am006-134 arcade_fun_am_talk_pleading with dissolve
    play voice3 girl22_no_questioning noloop
    am "I'm not a liar. I... I really mean it, [mcname]."
    am "It's probably been years."
    scene am006-135 arcade_fun_am_talk_sad with dissolve
    play voice3 girl22_disappointed_geh noloop
    am "When I started getting really good at coding, a lot of guys {i}changed{/i} how they acted toward me."
    am "Or worse. Some friends I'd known for years turned into super assholes."
    play sound sfx_drink_loop1 volume 1.3
    scene am006-136 arcade_fun_mc_talk_drink with dissolve
    pause
    stop sound fadeout 1.0
    play sound2 sfx_cloth_rustling1 noloop
    scene am006-137 arcade_fun_am_talk_fries with dissolve
    play voice3 girl22_arrogant_he noloop
    am "So I started fighting fire with fire."
    am "It wasn't enough to destroy them with my code and just being better than them."
    $ renpy.music.set_volume(0.0, 5.5, "music" )
    $ renpy.music.set_volume(0.0, 10.5, "music2" )
    $ renpy.music.set_volume(0.1, 30.5, "sound4" )
    stop music fadeout 6.0
    stop music2 fadeout 6.0
    play sound sfx_bite_strawberry1 volume 0.65
    play music3 music_bits_of_calm fadein 20.0 volume 0.6
    scene am006-138 arcade_fun_am_talk_fries with dissolve
    pause
    scene am006-140 arcade_fun_am_talk_scoff with dissolve
    play voice3 girl22_arrogant_hm noloop
    am "I had to break them with my words. Or at least get them to leave me the hell alone."
    scene am006-139 arcade_fun_mc_talknsightful with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Is that why you treat Anna like you do? Because she got the promotion and is now above you?"
    scene am006-140 arcade_fun_am_talk_scoff with dissolve
    play voice3 girl22_arrogant_pff noloop
    am "*scoffs* What, are you my shrink, now?"
    scene am006-141 arcade_fun_mc_talk with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Am I wrong, April?"
    scene am006-142 arcade_fun_am_talk_glad with dissolve
    play voice3 girl22_yes_simple noloop
    am "Tch. Yes. Maybe. I..."
    am "I don't know why I'm talking to you about this stuff."
    scene am006-143 arcade_fun_mc_talk with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Maybe because I'm the first non-asshole who saw the real you? Underneath the barbs."
    mc "You're like a cute porcupine."
    scene am006-144 arcade_fun_am_talk with dissolve
    play voice3 girl22_sex_closedmoan6 noloop
    am "Hmmph. Maybe you're onto something."
    am "But I think it's just that I have a crush on you. And one day, it will wear off."
    menu:
        "I hope it doesn't."(hint="sm1cs_am006_m03_h01"):
            call sm1cs_am006_m03_c01 from _call_sm1cs_am006_m03_c01
            scene am006-145 arcade_fun_mc_talk_menu_sincere with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.8
            mc "I hope it doesn't, April."
            scene am006-146 arcade_fun_menu_am_talk_close with dissolve
            play voice3 girl22_surprised_huh1 noloop
            am "You... really mean that?"
            scene am006-147 arcade_fun_mc_talk_menu with dissolve
            play voice2 mc_yes_yes3 noloop
            mc "I do. Maybe we can test things out again."
            scene am006-148 arcade_fun_menu_am_talk with dissolve
            play voice3 girl22_disappointed_oh noloop
            am "I'm... I'm not ready for that again."
            scene am006-149 arcade_fun_mc_talk_menu with dissolve
            play voice2 mc_yes_ugu1 noloop
            mc "Sure. But there are other things."
            scene am006-150 arcade_fun_menu_am_talk_blushes with dissolve
            play voice3 girl22_thinking_oh noloop
            am "Like what?"
            scene am006-152 arcade_fun_menu_mc_talk_yeahmaybe with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "*softly* A kiss..."
        "Maybe."(hint="sm1cs_am006_m03_h02"):
            scene am006-145 arcade_fun_mc_talk_menu_sincere with dissolve
            play voice2 mc_yes_yeah3 noloop
            mc "Maybe."
            mc "If that happens, I hope that we'll still be cool."
            scene am006-146 arcade_fun_menu_am_talk_close with dissolve
            play voice3 girl22_disappointed_ehh2 noloop
            am "Well... there is a first time for everything, [mcname]."
            am "But maybe we can test things."
            am "Approach this logically."
            scene am006-147 arcade_fun_mc_talk_menu with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "Shall we go back to your car."
            scene am006-148 arcade_fun_menu_am_talk with dissolve
            play voice3 girl22_no_high noloop
            am "Not like that. Jeez."
            am "No I mean. Just a kiss..."
            scene am006-152 arcade_fun_menu_mc_talk_yeahmaybe with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "Alright."
    scene am006-151 arcade_fun_menu_mc_talk_amlips with dissolve
    play voice2 d14s16_smell noloop
    mct "Here goes nothing."
    scene am006-153 arcade_fun_menu_mc_thought_am_nervous with dissolve
    pause
    play voice3 girl22_scared_eh noloop
    play sound sfx_skirt_off2
    scene am006-154 arcade_fun_am_talk_mc_gokiss with hpunch
    am "Wait!"
    scene am006-155 arcade_fun_mc_talk with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay, okay. We don't have to-"
    play sound sfx_cloth_rustling1
    scene am006-156 arcade_fun_am_talk_glasses with dissolve
    play voice3 girl22_no_simple noloop
    am "No. That's not it. I just... I wanted to take off my glasses."
    scene am006-157 arcade_fun_am_talk_ready with dissolve
    play voice3 girl22_angry_breathing noloop
    am "*deep breath* Okay. Let's do this."
    scene am006-158 arcade_fun_am_kiss with dissolve
    play voice2 d1s1_mmm noloop
    play voice3 girl22_sex_closedmoan2 noloop
    play sound dahlia_kiss_french1
    am "Mmm."
    play sound2 sfx_cloth_rustling4 noloop
    scene am006-159 arcade_fun_mc_thought_kiss with dissolve
    play voice2 mc_arrogant_hm1 noloop
    play sound mc_kiss2
    mct "Hehe. She's peeking her tongue at my lips."
    mct "I didn't think she'd want try out kissing with a French kiss."
    scene am006-160 arcade_fun_am_handsides with dissolve
    play voice3 girl22_sex_closedmoan5 noloop
    play sound mc_kiss1
    am "Mmmmm."
    mct "Woah. She's... she's really into this."
    scene am006-161 arcade_fun_mc_talk_am_pullback with dissolve
    play voice2 mc_happy_a1 noloop
    mc "And?"
    scene am006-162 arcade_fun_am_talk_am_pullback with dissolve
    play voice3 girl22_surprised_eh2 noloop
    am "I... your lips taste like beer."
    scene am006-163 arcade_fun_mc_talk_smile with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "That's it?"
    scene am006-164 arcade_fun_am_talk_blushes with dissolve
    play voice3 girl22_surprised_huh2 noloop
    am "What more do you want me to say?"
    am "That I got wet when we kissed?"
    scene am006-165 arcade_fun_mc_talk_question with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Did you?"
    scene am006-166 arcade_fun_am_talk_mad with dissolve
    play voice3 girl22_surprised_what noloop
    am "What? No. Of course I didn't. Shut up."
    scene am006-167 arcade_fun_am_talk_bashful with dissolve
    play voice3 girl22_sex_closedmoan6 noloop
    am "Unless... you wanted me to-"
    am "Talk about stuff like that."
    scene am006-168 arcade_fun_mc_talk with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "April... It's not just about what I want."
    scene am006-169 arcade_fun_am_talk_worrried with dissolve
    play voice3 girl22_yes_yep4 noloop
    am "I know. I don't know what's gotten into me."
    am "I hate this. Not being in control. But...{w} when I try to think about stopping this."
    scene am006-170 arcade_fun_mc_talk_am_bightlip with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    am "I hate that thought more."
    mc "..."
    scene am006-171 arcade_fun_mc_talk_shrug with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "So what happens now."
    scene am006-172 arcade_fun_am_talk_lookaway with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "I... You should walk me to my car."
    am "And... I... I ended up having a good time on our date, [mcname]."
    am "You were right, this was a good idea."
    am "I just. For now, I still need time."
    scene am006-173 arcade_fun_mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Sure. I understand."
    scene am006-174 arcade_fun_am_talk with dissolve
    play voice3 girl22_yes_aga11 noloop
    am "Yes..."
    scene am006-175 arcade_fun_mc_thought_leanback with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "What's this? Does she..."
    mct "Does she want me to kiss her again?"
    menu:
        "Kiss April again."(hint="sm1cs_am006_m04_c01"):
            call sm1cs_am006_m04_c01 from _call_sm1cs_am006_m04_c01
            play sound sfx_hair_scratch1
            scene am006-176 arcade_fun_am_talk_handcheek with dissolve
            play voice3 girl22_sex_closedmoan3 noloop
            am "*softly* Yes..."
            scene am006-177 arcade_fun_am_talk_kiss with dissolve
            play voice2 mc_thinking_mmm4 noloop
            play voice3 girl22_sex_closedmoan4 noloop
            play sound dahlia_kiss_french1
            am "*moaning softly*"
            scene am006-178 arcade_fun_mc_talk_kiss with dissolve
            play sound mc_kiss2
            play voice2 d1s5_orgasm noloop
            mct "This feels really nice."
            mct "She's letting me take the lead completely this time."
            scene am006-179 arcade_fun_mc_talk_kiss_angle with dissolve
            play sound mc_kiss1
            mct "Damn, I wish we could do more."
            mct "What if we had kissed in her car like this?"
            scene am006-180 arcade_fun_am_talk_daze with dissolve
            play voice3 girl22_angry_breathing noloop
            am "Woah."
            am "Uh... buh. My car."
            play sound sfx_cloth_rustling3
            scene am006-181 arcade_fun_mm_talk_hand with dissolve
            play voice2 d9s2_mcyes noloop volume 2.3
            mc "I got you."
        "Don't kiss April."(hint="sm1cs_am006_m04_c02"):
            play sound sfx_cloth_rustling3
            scene am006-181 arcade_fun_mm_talk_hand with dissolve
            play voice2 mc_yes_okay3 noloop
            mc "This way."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene am006-182 arcade_fun_mc_am_walkout with dissolve
    pause
    stop sound4 fadeout 2.0
    stop sound fadeout 1.5
    stop sound2 fadeout 1.5
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "music3" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 3.5, "sound4" )
    jump sm1cs_am006_end
label sm1cs_am006_end:
    $ StoryController.end_scene(AM_STORY, 2, 0, 2, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1cs_am006_m01_c01:
    $ player.set_choice("sm1cs_am006_that_sucks")
    return
label sm1cs_am006_m02_c01:
    $ player.set_choice("sm1cs_am006_messing_with_me")
    $ CharacterController.get_character("am").add_point(2)
    return
label sm1cs_am006_m02_c02:
    $ player.set_choice("sm1cs_am006_look_great")
    $ CharacterController.get_character("am").add_point(1)
    return
label sm1cs_am006_m02_c03:
    $ player.set_choice("sm1cs_am006_pajamas")
    return
label sm1cs_am006_m03_c01:
    $ player.set_choice("sm1cs_am006_kiss_am")
    $ CharacterController.get_character("am").add_point(1)
    return
label sm1cs_am006_m04_c01:
    $ player.set_choice("sm1cs_am006_kiss_again")
    $ CharacterController.get_character("am").add_point(2)
    return