image sm1fs_t001-glambot-1 = Movie(play = "images/FS_T/s001/anim/sm1fs_t001-a08-2x-60fps.webm", start_image = "sm1fs_t001-a08 mc-hold-sec-sy-why-mc-that-glambot-08-000_i", image = "sm1fs_t001-a08 mc-hold-sec-sy-why-mc-that-glambot-08-120_i", loop = False)
image sm1fs_t001-glambot-2 = Movie(play = "images/FS_T/s001/anim/sm1fs_t001-a17-2x-50fps.webm", start_image = "sm1fs_t001-a17 tl-clown-reveal-glambot-000_i", image = "sm1fs_t001-a17 tl-clown-reveal-glambot-119_i", loop = False)
image sm1fs_t001-a36-1 = Movie(play = "images/FS_T/s001/anim/sm1fs-t001-a36-1-3x-60fps.webm", start_image = "sm1fs-t001-a36-1 sy-gives-mc-hj-anim-01")
image sm1fs_t001-a36-1-f = Movie(play = "images/FS_T/s001/anim/sm1fs-t001-a36-1-2x-60fps.webm", start_image = "sm1fs-t001-a36-1 sy-gives-mc-hj-anim-01")
image sm1fs_t001-a36-2 = Movie(play = "images/FS_T/s001/anim/sm1fs-t001-a36-2-3x-60fps.webm", start_image = "sm1fs-t001-a36-2 sy-gives-mc-hj-anim-01")
image sm1fs_t001-a36-2-f = Movie(play = "images/FS_T/s001/anim/sm1fs-t001-a36-2-2x-60fps.webm", start_image = "sm1fs-t001-a36-2 sy-gives-mc-hj-anim-01")
image sm1fs_t001-a36-3 = Movie(play = "images/FS_T/s001/anim/sm1fs-t001-a36-3-3x-60fps.webm", start_image = "sm1fs-t001-a36-3 sy-gives-mc-hj-anim-01")
image sm1fs_t001-a36-3-f = Movie(play = "images/FS_T/s001/anim/sm1fs-t001-a36-3-2x-60fps.webm", start_image = "sm1fs-t001-a36-3 sy-gives-mc-hj-anim-01")
label sm1fs_t001:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music funhouse_music_horror_1
    play sound sfx_door_creak4
    scene sm1fs_t001-01 mc-sy-walking-hallway-before-tl-room_c1 with Fade(1.0, 0.5, 1.0)
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I gotta admit - I've been wondering why you were so certain she would be at the theater."
    scene sm1fs_t001-02 mc-sy-walking-from-behind-talk_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "I told you she was distinct, right?"
    play voice2 mc_no_uhuh1 noloop
    mc "Uh huh."
    scene sm1fs_t001-03 sy-mc-pause-sy-talk_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, that video of her was uploaded 37 times with different usernames - all from a local community theater's IP address."
    scene sm1fs_t001-04 mc-upset_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Seriously? Must have been pretty desperate for a Fetish Locator account."
    if player.has_played_scene("sm1ms006"):
        scene sm1fs_t001-05 mc-pov-sy-looking-defensive_c1 with dissolve
        play voice3 stacy_yes_yeah1 noloop
        sy "Which makes her the perfect candidate for the porn studio!"
        play voice2 mc_thinking_hmm2 noloop
        mc "Stacy... I'm still upset with you."
        play voice3 stacy_thinking_emm4 noloop
        sy "I know, but..."
        scene sm1fs_t001-06 sy-relaxes-no-need-genius-mc-guess-so_c1 with dissolve
        play voice3 stacy_angry noloop
        sy "It's going to help us out with finding actresses. Or at least {i}was{/i} going to help us."
        play voice2 mc_arrogant_hm3 noloop
        mc "I guess..."
        scene sm1fs_t001-07 mc-sy-continue-walking_c1 with dissolve
    else:
        mc "Didn't you tell me that you separated all the data and got rid of any personally identifiable information?"
        scene sm1fs_t001-05 mc-pov-sy-looking-defensive_c1 with dissolve
        play voice3 stacy_yes_yeah1 noloop
        sy "I did! It's just-"
        play voice2 mc_thinking_hmm2 noloop
        mc "It's just what?"
        play voice3 stacy_thinking_emm4 noloop
        sy "I disconnected all the data, but..."
        sy "Look, there were 37 uploads of this video and 37 attempts to create a Fetish Locator account submitting a video."
        scene sm1fs_t001-06 sy-relaxes-no-need-genius-mc-guess-so_c1 with dissolve
        play voice3 stacy_angry noloop
        sy "It doesn't take a genius to put the pieces together."
        play voice2 mc_arrogant_hm3 noloop
        mc "I guess..."
        scene sm1fs_t001-07 mc-sy-continue-walking_c1 with dissolve
    pause
    scene sm1fs_t001-08 mc-hold-sec-sy-why-mc-that_c1 with dissolve
    play voice2 mc_surprised_huh1 noloop
    mc "Oh, hold up a second."
    play voice3 stacy_surprised_huh1 noloop
    sy "What's up?"
    play voice2 mc_arrogant_heh1 noloop
    mc "That."
    play sound3 ["<silence 0.2>", sfx_double_door1] noloop volume 2.0
    scene sm1fs_t001-glambot-1
    play sound ["<silence 0.4>", funhouse_monster_out]
    pause
    scene sm1fs_t001-10 sy-is-that-scary-mc-was-first-time-sy-thanks-warning_c1 with dissolve
    play voice3 stacy_disgust_oh2 noloop
    sy "Oh. {w}Was that supposed to be scary?"
    play voice2 mc_yes_yeah5 noloop
    mc "It was the first time. For me, at least."
    scene sm1fs_t001-11 mc-ask-video-sy-explains-mc-not-recognizable_c1 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Oh, well, thanks for the warning."
    play voice2 mc_thinking_hmm1 noloop
    mc "So, you were saying? About her video."
    scene sm1fs_t001-12 mc-sy-contnue-conversation-as-walk-in-hallway_c1 with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Oh, her video is in full body make-up. How was I supposed to know that anyone would be able to identify her?"
    play voice2 mc_thinking_hmm3 noloop
    mc "I guess it is only recognizable if you've seen her."
    play voice3 stacy_yes_yeah2 noloop
    sy "So, yeah. I followed reasonable protocols to preserve privacy... but this was an outlier."
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    $ renpy.music.set_volume(1.0, 0.0, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2")
    $ renpy.music.play(audio.funhouse_music_horror_2, "music" , True, None, True, 1.0)
    $ renpy.music.play(audio.funhouse_music_horror_2d, "music2", True, None, True, 1.0)
    play sound sfx_ferris_wheel_stop
    play sound2 sfx_light_shutdown1 noloop
    scene black with vpunch
    play voice2 mc_scared_huh1 noloop
    play voice3 stacy_scared_oof3 noloop
    pause 0.1
    scene sm1fs_t001-13 lights-go-out_c1 with dissolve
    pause
    scene sm1fs_t001-14 sy-asking-another-jumpscare-mc-dont-think-so-mc-anyway_c1 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Huh. Another jumpscare incoming?"
    scene sm1fs_t001-15 mc-ask-about-arj-data-sy-deleted-everything_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "I don't think so. Last time I really thought the power had gone out."
    mc "Anyway, it's just through that door up there."
    scene sm1fs_t001-16 mc-sy-see-tl-clown_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "What about AmRose's data? She was very concerned about that."
    play voice3 stacy_thinking_hmm4 noloop
    sy "I deleted everything related to AmRose's account before I even started splitting the data up."
    mc "So, did you see what AmRose posted?"
    play sound2 sfx_camera_fly1 volume 2.0 noloop
    play sound3 ["<silence 1.7>", sfx_camera_fly1] noloop volume 2.0
    scene sm1fs_t001-glambot-2 with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1fs_t001-17 tl-clown-reveal_c1 with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh wow, there she is."
    play voice2 mc_yes_yeah7 noloop
    mc "I told you."
    play sound sfx_double_door1
    scene sm1fs_t001-18 mc-sy-enter-room-sy-there-tl-is-mc-told-her_c1 with dissolve
    pause
    scene sm1fs_t001-18-01 room-stablishing-shot_c1 with dissolve
    pause
    scene sm1fs_t001-19 sy-whispering-mc_c1 with dissolve
    play voice3 amrose_old_psst2 noloop
    sy "*whisper* Don't say anything about the video or Fetish Locator."
    play voice2 d1s2_hmm noloop
    mc "*whisper* Why not?"
    scene sm1fs_t001-20 sy-continues-whispering-mc_c1 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "*whisper* We don't want her to know we're connected to that. Duh."
    play voice2 mc_yes_okay2 noloop
    mc "*whisper* Uh, okay. Do you think she can hear us whispering?"
    sy "*whisper* Just follow my lead."
    scene sm1fs_t001-21 sy-explains-to-mc-connection-mc-ask-hear-whispering-sy-follow-lead_c1 with dissolve
    pause
    scene sm1fs_t001-22 mc-sy-talk-no-longer-whispering_c1 with dissolve
    play voice3 stacy_surprised_huh4 noloop
    sy "Why are you whispering?"
    play voice2 d2s9_confused noloop volume 2.0
    mc "I don't know. Didn't you start it?"
    scene sm1fs_t001-23 sy-rolls-eyes_c1 with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "I mean, if you want to fuck that clown over there, her mouth is open."
    scene sm1fs_t001-24 tl-clown-closeup_c1 with dissolve
    pause
    scene sm1fs_t001-25 sy-she-looks-like-mannequin-mc-bets-ten-bucks_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?! I didn't say-"
    play voice3 stacy_disappointed_oh3 noloop
    sy "But she looks like a mannequin or something, so I doubt she has any other holes you can use."
    scene sm1fs_t001-26 sy-believe-for-dirty-thoughts-mc-are-serious-look-her_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Very funny. Ten bucks, I bet you she's an actress."
    scene sm1fs_t001-27 sy-looking-at-her-skin-plastic-mc-that-makeup_c1 with dissolve
    play voice3 stacy_yeahno noloop
    sy "You just want to believe that for your dirty thoughts."
    play voice2 mc_surprised_huh6 noloop
    mc "Are you serious? Look at her!"
    scene sm1fs_t001-28 sy-not-sweating-mc-chilly-enough_c1 with dissolve
    play voice3 stacy_no_nah2 noloop
    sy "I am looking at her. Her skin looks plastic."
    play voice2 mc_thinking_hmm4 noloop
    mc "I'm sure that's just the makeup. Latex or something."
    scene sm1fs_t001-29 sy-not-even-breathing-mc-let-ask-her_c1 with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "She's not sweating."
    play voice2 d9s2_yeah noloop volume 2.5
    mc "It's chilly enough in here."
    scene sm1fs_t001-31 sy-didnt-even-twitch-mc-so-good-actress_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "She doesn't even seem to be breathing."
    play voice2 mc_disappointed_ehh1 noloop
    mc "Look, let's just ask her."
    scene sm1fs_t001-32 sy-will-prove-ask-see-eyes-mc-yeah_c1 with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Hey, Miss Clown Lady. If you are a real person, blink once. If you are a plastic doll, blink twice."
    play voice2 mc_disappointed_off1 noloop
    mc "Did you really think that would work?"
    play voice3 stacy_arrogant_ha1 noloop
    sy "Her eyes didn't even twitch. I'm telling you this is a wax model or something."
    play voice2 mc_happy_a1 noloop
    mc "So, she's a good actress."
    scene sm1fs_t001-33 sy-look-mc-wants-pull-cock-out-mc-must-be-kidding-sy-fine-will-do-it-herself_c1 with dissolve
    play voice3 stacy_angry_argh1 noloop
    sy "I'll prove it to you. See her eyes?"
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, so."
    play voice3 stacy_arrogant_hmm2 noloop
    sy "Pull out your cock. If she's human her eyes will react somehow."
    play voice2 mc_disappointed_ah2 noloop
    mc "You must be kidding."
    $ renpy.music.set_volume(0.0, 15.0, "music" )
    $ renpy.music.set_volume(0.7, 10.0, "music2")
    play sound sfx_jeans_on1 volume 1.5
    scene sm1fs_t001-34 sy-takes-mc-cock-out_c1 with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "Fine, I'll do it for you."
    queue voice3 stacy_suckmoan3 noloop
    sy "Mmmm. Nice and hard."
    play voice2 mc_thinking_emm1 noloop
    mc "I think her eyes got a bit wider."
    scene sm1fs_t001-35 sy-gets-mc-nice-hard-mc-thinks-her-eyes-moved_c1 with dissolve
    play voice3 stacy_no_uhuh3 noloop
    sy "I didn't notice any difference."
    scene sm1fs_t001-36 sy-gives-mc-hanjob-anim_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "You were staring at my cock."
    scene sm1fs-t001-a36-3 sy-gives-mc-hj-anim-01 with dissolve
    pause
    play sound sfx_handjob_cream1 volume 1.5 loop
    play voisex3 stacy_moans1 volume 0.6
    play voisex2 d7s4_mcbreathing
    scene sm1fs_t001-a36-3
    mc "..."
    mc "You're still staring at my cock."
    scene sm1fs_t001-a36-1 with dissolve
    play voisex3 stacy_yes_ugu1 noloop
    queue voisex3 stacy_moans1 volume 0.6
    sy "That's because I know she's a plastic doll. There's nothing worth looking at over there."
    pause
    scene sm1fs_t001-a36-2 with dissolve
    mc "I'm pretty certain that the mouth of that \"plastic doll\" is watering and looking at my dick."
    pause
    scene sm1fs_t001-a36-3-f with dissolve
    play voisex3 stacy_no_nonono1 noloop
    queue voisex3 stacy_moans1 volume 0.6
    sy "You're imagining things. It's just a glossy reflection and wishful thinking."
    pause
    scene sm1fs_t001-a36-1-f with dissolve
    mc "Aren't you even going to look at her?"
    pause
    scene sm1fs_t001-a36-2-f with dissolve
    play voisex3 stacy_yes_fine4 noloop
    queue voisex3 stacy_moans1 volume 0.6
    sy "Fine. I'll take my eyes off your hard, pumping cock long enough to prove you wrong."
    stop sound fadeout 1.0
    stop voisex3 fadeout 1.0
    stop voisex2 fadeout 1.0
    scene sm1fs_t001-40 sy-touches-tl-leg-imagining-things_c1 with dissolve
    play sound sfx_cloth_rustling2
    pause
    play sound sfx_cloth_rustling1
    scene sm1fs_t001-41 sy-reaches-tl-breast-see-real-person-would-react_c1 with dissolve
    play voice3 stacy_huh2 noloop
    sy "See? If she were a real person she'd react to me grabbing her tit like this."
    scene sm1fs_t001-42 sy-breast-grab-close-up-huh-would-use-sex-doll-for-horror-house_c1 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "Huh."
    sy "You don't suppose they'd use a RealDoll for a haunted house."
    play voice4 girl22_angry_argh1 noloop
    play sound sfx_bed_slide1
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound3 sfx_horror_violin2 noloop
    scene sm1fs_t001-43 clown-jumpscare_c1 with hpunch
    "Scary Clown" "GAAAAAAAHHHHHH!!!!!"
    play voice4 girl22_angry_argh2 noloop
    play sound3 sfx_horror_violin1 noloop
    play sound sfx_bed_slide3
    scene sm1fs_t001-44 clown-scare_c1 with hpunch
    pause
    play voice3 stacy_scared_ah4 noloop
    play voice2 d6s1_pain noloop
    scene sm1fs_t001-45 clown-garh-sy-holy-fuck_c1 with hpunch
    sy "HOLY FUCK!!!"
    menu:
        "Fight"(hint="sm1fs_t001_m01_h01"):
            call sm1fs_t001_m01_c01 from _call_sm1fs_t001_m01_c01
            play voice2 mc_pain_argh1 noloop
            play sound sfx_kick3
            scene sm1fs_t001-46 choice-fight-mc-smacks-clown-face_c1 with hpunch
            mc "HiiiiiYAAAHHH!!!"
            play voice4 girl24_scared_oh3 noloop
            "Scary Clown" "FUCKING OWWW!!!"
            scene sm1fs_t001-47 tl-licks-lips-mc-sorry-she-wants-one-more_c1 with dissolve
            play voice2 mc_pain_ou1 noloop
            mc "I'm so sorry! You scared the crap out of us!!!"
            play voice4 girl24_sex_closedmoan1 noloop
            "Scary Clown" "Do it again! I liked it!!!"
        "Flight"(hint="sm1fs_t001_m01_h02"):
            call sm1fs_t001_m01_c02 from _call_sm1fs_t001_m01_c02
            play sound sfx_cloth_planket2 volume 1.5
            play voice2 mc_pain_argh1 noloop
            scene sm1fs_t001-48 choice-flight-mc-tries-run-away_c1 with hpunch
            mct "Runaway!!!"
            play voice2 mc_angry_errr4 noloop
            with hpunch
            mc "FUCK!!!"
            mc "Stacy! Will you LET GO!!!"
        "Fuck"(hint="sm1fs_t001_m01_h03"):
            call sm1fs_t001_m01_c03 from _call_sm1fs_t001_m01_c03
            play voice2 d1s5_orgasm2 noloop volume 1.7
            play sound mc_cum_sound1
            scene sm1fs_t001-49 choice-fuck-mc-cums-tl-mouth_c1 with hpunch
            mc "FUCKING HELL!!!"
            scene sm1fs_t001-50_tl-licks-cum-lips-mc-asking-what-happened-tl-only-made-people-pee-themselves_c1 with dissolve
            play voice4 girl24_sex_closedmoan4 noloop
            "Scary Clown" "Fuck me. {w}I've never seen THAT response before."
            scene sm1fs_t001-51 mc-pov-sy-what-mc-what-happened-clown-got-what-came-for_c1 with dissolve
            play voice2 mc_arrogant_huh2 noloop
            mc "What the hell just happened???"
            play voice4 girl24_happy_laugh1 noloop
            "Scary Clown" "I mean, I've made people pee themselves, but that was new."
    scene sm1fs_t001-52 sy-what-mc-never-happened-before-tl-move-along_c1 with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "What?"
    play voice2 mc_disappointed_off2 noloop
    mc "The Hell Just Happened??"
    play voice4 girl24_arrogant_hah noloop
    "Scary Clown" "You got what you paid for. Move along."
    scene sm1fs_t001-53 mct-so-wierd-sy-okay-you-real-tl-ofc-real_c1 with dissolve
    play voice3 stacy_surprised_ah2 noloop
    sy "WHAT???"
    play voice2 mc_scared_oh1 noloop
    mc "That never happened before! I'm so confused."
    scene sm1fs_t001-57 tl-another-group-might-come-sy-came-here-talk-you-tl-why_c1 with dissolve
    play voice4 girl24_happy_laugh2 noloop
    "Scary Clown" "That's it for this room. Move along to the next."
    play voice2 mc_scared_oh2 noloop
    mc "That is so..."
    scene sm1fs_t001-52 sy-what-mc-never-happened-before-tl-move-along_c1 with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "Okay, so you're real."
    play voice4 girl24_yes_simple2 noloop
    "Scary Clown" "Of course I'm real. Would you mind taking your hand off my tit?"
    play sound sfx_cloth_planket2
    scene sm1fs_t001-54 sy-no-longer-holding-tl-oh-sure-mc-better-put-dick-away_c1 with dissolve
    play voice3 stacy_oh2 noloop
    sy "Oh, um, sure."
    play voice2 mc_happy_oof3 noloop
    mc "I think I better put this away..."
    scene sm1fs_t001-55 mc-ask-stacy-she-what-mc-let-go-dick_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Stacy...?"
    play voice3 stacy_happy_hmm1 noloop
    sy "Hmm?"
    mc "Could you let go of my dick?"
    play sound sfx_jeans_on1
    scene sm1fs_t001-56 mc-pulls-pants-up-sy-sure-tl-best-guests-some-time-mc-thank-you_c1 with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Oh, yeah, sure."
    scene sm1fs_t001-57 tl-another-group-might-come-sy-came-here-talk-you-tl-why_c1 with dissolve
    play voice4 girl24_happy_laugh3 noloop
    "Scary Clown" "Don't get me wrong, you two have been the most interesting guests I've had in quite a while."
    play voice2 mc_yes_yeah7 noloop
    mc "Thank you?"
    scene sm1fs_t001-58 sy-explains-mc-recongnized-her-mc-confirms_c1 with dissolve
    play voice4 girl24_thinking_emm1 noloop
    "Scary Clown" "But another group might be along at any time. And you've both been here a while."
    play voice3 stacy_hey_happy1 noloop
    sy "Wait, but we came here to talk to you."
    play voice4 girl24_surprised_huh3 noloop
    "Scary Clown" "Huh?{w} Why?"
    scene sm1fs_t001-59 tl-interesting-ofter-jerk-front-strangers-sy-not-exactly-mc-sometimes_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, I... I mean, [mcname] - my partner recognized you."
    play voice2 mc_yes_yes2 noloop
    mc "I did."
    play voice4 girl24_arrogant_huh1 noloop
    "Scary Clown" "Interesting...{w} Do you often jerk him off in front of strangers like this?"
    scene sm1fs_t001-60 sy-anyway-not-important-mc-ask-name-tl-tells-her-name_c1 with dissolve
    play voice3 stacy_no_sad1 noloop
    sy "Not exactly."
    play voice2 mc_thinking_mmm4 noloop
    mc "I mean, sometimes..."
    scene sm1fs_t001-61 sy-cool-introduces-herself-mc-tl-nice-meet-you-move-along_c1 with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "Anyway. That's not important right now."
    play voice2 mc_yes_yeah1 noloop
    mc "Sorry, we haven't been properly introduced. What's your name?"
    scene sm1fs_t001-62 mc-have-talk-her-tl-meet-ferris-wheel-sy-wont-kick-them-out_c1 with dissolve
    play voice4 girl24_thinking_huh1 noloop
    tl "Taisia."
    scene sm1fs_t001-63 mc-heroic-pose-take-care-has-plan-tl-just-tell-them-waiting-for-her_c1 with dissolve
    play voice3 stacy_happy_yay2 noloop
    sy "Cool name. I'm Stacy, and this is [mcname]."
    play voice4 girl24_arrogant_yeah3 noloop
    tl "Nice to meet you, but seriously, you need to move along."
    scene sm1fs_t001-64 mc-shrugs-could-work-too_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "But we really want to talk to you - you personally."
    scene sm1fs_t001-62 mc-have-talk-her-tl-meet-ferris-wheel-sy-wont-kick-them-out_c1 with dissolve
    play voice4 girl24_disappointed_neh noloop
    tl "Fine. Whatever.{w} Meet me by the Ferris Wheel after the park closes."
    scene sm1fs_t001-60 sy-anyway-not-important-mc-ask-name-tl-tells-her-name_c1 with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "Won't they kick us out?"
    scene sm1fs_t001-63 mc-heroic-pose-take-care-has-plan-tl-just-tell-them-waiting-for-her_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I'll take care of it.{w} I've got a plan."
    play voice4 girl24_thinking_hmm2 noloop
    tl "Just tell them you're waiting for me."
    scene sm1fs_t001-64 mc-shrugs-could-work-too_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, that would work too."
    jump sm1fs_t001_later
label sm1fs_t001_later:
    $ renpy.music.set_volume(0.35, 3.0, "music2")
    $ renpy.music.set_volume(1.0, 3.0, "sound2")
    play sound2 sfx_parknight_crickets fadein 2.0
    scene sm1fs_t001-65 mc-sy-waiting-next-wheel-ferris-wheel_c1 with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1fs_t001-66 sy-this-cool-mct-wonder-what-tl-looks-like-mc-how-recognize-her_c1 with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "This is so cool. I can't wait to talk to her for real."
    mct "I wonder what she looks like."
    play voice2 mc_thinking_mmm5 noloop
    mc "How do you suppose we're going to recognize her?"
    scene sm1fs_t001-67 sy-what-mean-already-know-her-mc-with-makeup_c1 with dissolve
    play voice3 stacy_arrogant_hmm3 noloop
    sy "What do you mean? You already recognized her."
    play voice2 mc_yes_sure1 noloop
    mc "In her make-up, sure. I have no idea what the woman actually looks like."
    play sound sfx_drink_slurp1
    scene sm1fs_t001-68 sy-takes-sip-thinks-things-over_c1 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Huh. I hadn't thought of that."
    scene sm1fs_t001-70 tl-saw-both-of-them-mc-wow-nothing-like-expected_c1 with dissolve
    play voice4 girl24_arrogant_huh2 noloop
    tl "Maybe she'll recognize you."
    scene sm1fs_t001-69 tl-walks-to-gang-sy-hadnt-thought-that-tl-talks-mc-awesome_c1 with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Whoa!"
    scene sm1fs_t001-71 tl-doesnt-sound-compliment-mc-sy-tries-explain-mc-never-thought-hot_c1 with dissolve
    play voice4 girl24_arrogant_hm1 noloop
    tl "After all, she saw both of you..."
    scene sm1fs_t001-72 tl-thank-you-sy-we-have-pro-position_c1 with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow, you didn't look anything like I expected!"
    play voice4 girl24_arrogant_pff noloop
    tl "That doesn't sound like a compliment."
    play voice3 stacy_thinking_emm2 noloop
    sy "What [mcname] meant was-"
    play voice2 mc_yes_yeah4 noloop
    mc "What I mean was - I didn't expect you to be so fricken' HAWT!"
    play voice4 girl24_thinking_ah noloop
    tl "Oh, thank you."
    scene sm1fs_t001-73 tl-girl-power-she-charge-sy-starts-we-mc-insists-its-partnership_c1 with dissolve
    play voice3 stacy_thinking_hmm2 noloop
    sy "We have a proposition for you."
    scene sm1fs_t001-75 tl-explains-scary-clown-mc-tempting-but-no_c1 with dissolve
    play voice4 girl24_surprised_huh2 noloop
    tl "Girl power. I guess you're in charge?"
    scene sm1fs_t001-77 mc-basic-makeup-naked-sy-want-her-sex-camera-tl-sorry-what_c1 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "We-"
    play voice2 mc_happy_a1 noloop
    mc "It's a partnership."
    sy "But yes, you can talk to me."
    scene sm1fs_t001-79 tl-ask-if-they-think-she-whore-sy-what_c1 with dissolve
    play voice4 girl24_yes_aga noloop
    tl "Good. So, I'm guessing you two aren't the normal clients, but I can guess what you want."
    tl "Scary clown. Probably for some kind of sexy, young adult, maybe college party?"
    scene sm1fs_t001-78 sy-has-film-studio-mct-porn-studio-sy-continues-they-way-her_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "Tempting, but no."
    play voice3 stacy_mmm2 noloop
    sy "What we are looking for is something more au natural..."
    scene sm1fs_t001-76 sy-explains-natural-tl-color-me-intrigued_c1 with dissolve
    play voice4 girl24_disgust_ooh2 noloop
    tl "Oh? Color me intrigued."
    scene sm1fs_t001-72 tl-thank-you-sy-we-have-pro-position_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "As in without makeup... and naked."
    play voice3 stacy_yes_yap1 noloop
    sy "Basically, we want you to have sex - on camera."
    scene sm1fs_t001-79 tl-ask-if-they-think-she-whore-sy-what_c1 with dissolve
    play voice4 girl24_surprised_what2 noloop
    tl "I'm sorry, what?!"
    play voice3 stacy_yes_yeah1 noloop
    sy "We run an adult film studio..."
    scene sm1fs_t001-81 tl-insist-judge-agreed-mct-interesting_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Just call it a porn studio."
    play voice3 stacy_thinking_emm3 noloop
    sy "...and we want you to-"
    play voice4 girl24_angry_argh2 noloop
    scene sm1fs_t001-80 tl-getting-very-angry-asking-if-look-like-whore-sy-no_c1 with hpunch
    tl "Do you think I'm a whore?"
    scene sm1fs_t001-82 tl-explains-stupid-bet-not-prostitution-sy-didnt-mean-bad_c1 with dissolve
    play voice3 stacy_surprised_huh3 noloop
    sy "What?!"
    play voice4 girl24_angry_geh noloop
    scene sm1fs_t001-80 tl-getting-very-angry-asking-if-look-like-whore-sy-no_c1 with vpunch
    tl "DO. YOU. THINK. I'M. A. WHORE???"
    play voice3 stacy_no_sad1 noloop
    sy "What? No..."
    play voice4 girl24_angry_err1 noloop
    tl "Because I'll have you know that the judge agreed with me!"
    scene sm1fs_t001-81 tl-insist-judge-agreed-mct-interesting_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mct "Interesting..."
    scene sm1fs_t001-79 tl-ask-if-they-think-she-whore-sy-what_c1 with dissolve
    play voice4 girl24_angry_cough2 noloop
    tl "It was just a stupid bet.{w} It wasn't prostitution."
    play voice3 stacy_no_nonono4 noloop
    sy "I didn't mean-"
    play sound sfx_skirt_off2
    scene sm1fs_t001-83 mc-steps-in-sy-steps-behind-him_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Can I jump in here? Great."
    mc "What my partner here is trying to say is that we've seen a small example of your work."
    mc "We would like to explore your abilities further and possibly contract you for further... performances."
    scene sm1fs_t001-84 mc-not-looking-charity-deserve-compensation-tl-doesnt-sound-bad_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.8
    mc "Of course, we're not looking for charity."
    mc "You're a dedicated performer, and deserve adequate compensation."
    play voice4 girl24_disappointed_eeh1 noloop
    tl "That... doesn't sound so bad."
    play sound sfx_drink_slurp1
    scene sm1fs_t001-85 mc-shall-continue-tl-more-info-mc-tells-sy-go-ahead_c1 with dissolve
    play voice2 d9s2_ugu noloop volume 2.0
    mc "Shall we continue?"
    play voice4 girl24_yes_simple1 noloop
    tl "I would like more information."
    mc "Stacy, go ahead."
    scene sm1fs_t001-86 mct-more-tact-this-time-sy-explains-tl-uh-huh_c1 with dissolve
    mct "Hopefully with more tact this time."
    play voice3 stacy_yes_fine3 noloop
    sy "Right, so. I assume you've heard of casting couch videos?"
    scene sm1fs_t001-87 sy-like-film-no-make-up-during-test-tl-asking-screen-partner_c1 with dissolve
    play voice4 girl24_yes_ugu noloop
    tl "Uh huh."
    scene sm1fs_t001-86 mct-more-tact-this-time-sy-explains-tl-uh-huh_c1 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "We'd like to film you - without your makeup - during a test of your talents and abilities."
    play voice4 girl24_thinking_hmm1 noloop
    tl "Who would I be working with?"
    scene sm1fs_t001-88 mc-raises-hand-he-costar-sy-explains-mc-only-male_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Me."
    play voice3 stacy_thinking_hm1 noloop
    sy "Our studio specializes in a specific... genre."
    sy "Our only male performer is [mcname] here."
    scene sm1fs_t001-89 tl-so-pay-her-fuck-him-sy-explain-casting-mc-paying-work-future_c1 with dissolve
    play voice4 girl24_surprised_eeh2 noloop
    tl "So, you pay me to fuck him on camera?"
    scene sm1fs_t001-90 tl-asking-else-should-know-mc-probably-ask-concerns_c1 with dissolve
    play voice3 stacy_no1 noloop
    sy "Not yet. This will just be a casting video. It won't be sold."
    play voice2 mc_yes_yeah2 noloop
    mc "But if it goes well you can expect paying work in the future."
    play voice4 girl24_arrogant_hm4 noloop
    tl "Anything else I should know?"
    play voice2 mc_thinking_mmm4 noloop
    mc "Probably. Do you have any immediate questions or concerns?"
    scene sm1fs_t001-91 tl-hmm-was-about-asking-cock-size-but-saw-earlier_c1 with dissolve
    play voice4 girl24_thinking_hmm3 noloop
    tl "Hmm..."
    tl "I was going to ask, \"How big is your cock?\", but I saw that earlier."
    scene sm1fs_t001-93 sy-assures-tl-mc-quite-skilled-cock-he-can-provide-refs_c1 with dissolve
    play voice3 stacy_angry noloop
    sy "He's quite skilled with it. I can assure you."
    play voice2 mc_yes_yes1 noloop
    mc "I could literally provide you with at least a dozen satisfied references."
    scene sm1fs_t001-94 tl-thinks-about-it-still-looking-mc-cock-sy-no-need-do-now_c1 with dissolve
    play voice4 girl24_thinking_hmm6 noloop volume 1.5
    tl "Hmm."
    play voice3 stacy_hey_happy2 noloop
    sy "You don't have to agree now. Let me give you my digits and you can contact-"
    scene sm1fs_t001-95 tl-will-do-it_c1 with dissolve
    play voice4 girl24_yes_yeah noloop
    tl "Okay, I'll do it."
    play voice2 d1s1_mmm noloop
    mct "Well, that was easy enough."
    tl "Give me your info and I'll let you know when it fits into my schedule."
    scene sm1fs_t001-96 sy-sounds-good-mc-no-condoms-tl-fine_c1 with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "Sounds good."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, it probably goes without saying, but we'd prefer to shoot this video without using condoms."
    play voice4 girl24_yes_happy noloop
    tl "That's fine with me. I'm protected."
    scene sm1fs_t001-97 tl-exchange-numbers-end-scene_c1 with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "Terrific. Here's my info."
    play voice4 girl24_yes_yap noloop
    tl "Excellent, and here's mine."
    play voice2 mc_happy_yay2 noloop
    mc "We look forward to hearing from you."
    stop music
    stop music2 fadeout 3.0
    stop sound2 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "music2")
    $ renpy.music.set_volume(1.0, 3.0, "music")
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene_in_time(THEATER_STORY_LINE, 19, 30, 3)
    return
label sm1fs_t001_m01_c01:
    $ player.set_choice("sm1fs_t001_fight")
    return
label sm1fs_t001_m01_c02:
    $ player.set_choice("sm1fs_t001_flight")
    return
label sm1fs_t001_m01_c03:
    $ player.set_choice("sm1fs_t001_fuck")
    return
label sm1fs_t001_unlocks:
    call sm1fs_t001_m01_c03 from _call_sm1fs_t001_m01_c03_1
    if config_storyline_mode is True:
        $ execute_storyline_config(THEATER_STORY_LINE)
    return