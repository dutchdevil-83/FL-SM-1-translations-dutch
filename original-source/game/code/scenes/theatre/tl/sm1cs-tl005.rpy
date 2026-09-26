image sm1cs_tl005-glambot-1 = Movie(play = "images/FS_T/TL/s005/anim/sm1cs-tl005-a32-4x-60fps.webm", start_image = "sm1cs-tl005-a32 stalker-dude-glambot-000", image = "sm1cs-tl005-a32 stalker-dude-glambot-120", loop = False)
label sm1cs_tl005:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "music" )
    play music music_horror_moment1
    play sound sfx_double_door1
    play sound2 sfx_heels_steps1 volume 0.6
    scene sm1cs-tl005-00 haunted_house_stalker with Fade(0.5, 0.5, 0.5)
    play voice2 mc_angry_errr7 noloop
    mct "Fuck, this place is still creepy as hell..."
    play sound sfx_door_creak4
    scene sm1cs-tl005-01 haunted_house_stalker_mc_talk_walkin with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Taisia? You here?"
    mc "..."
    mc "Taisia? Heelllloooooooo?"
    stop sound2 fadeout 1.0
    scene sm1cs-tl005-02 haunted_house_stalker_mc_talk_thought with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "God... why does she have to fuck with me like this?"
    mct "I just hope, I really hope..."
    play sound sfx_door_creak2
    scene sm1cs-tl005-03 haunted_house_stalker_mc_talk_thought_behind with dissolve
    play voice2 d14s16_smell noloop
    mct "That she's not in her clown makeup."
    scene sm1cs-tl005-04 haunted_house_stalker_tl_talk with dissolve
    play voice3 girl24_arrogant_huh1 noloop
    tl "Yo."
    play voice2 d6s1_pain noloop
    play music2 music_horror_moment1_short noloop
    play sound sfx_comic_castanet1
    play music3 music_battle_drums_1
    scene sm1cs-tl005-05 haunted_house_stalker_mc_talk with hpunch
    mc "{i}HOLY FUCK!{/i}"
    menu:
        "Scream"(hint="sm1cs_tl005_m01_h01"):
            play voice2 mc_pain_argh1 noloop
            scene sm1cs-tl005-06 haunted_house_stalker_mc_talk with vpunch
            mc "AAAAAAHHHHHHHH!!!!"
            scene sm1cs-tl005-07 haunted_house_stalker_tl_talk with dissolve
            play voice3 girl24_disappointed_eeh1 noloop
            tl "Ahh."
            scene sm1cs-tl005-08 haunted_house_stalker_mc_talk with dissolve
            play voice2 mc_angry_fuck1 noloop
            mc "FUCK!"
            stop music3 fadeout 10.0
            play sound sfx_skirt_off2
            scene sm1cs-tl005-09 haunted_house_stalker_mc_talk_bentover with dissolve
            play voice2 mc_pain_cough1 noloop
            mc "Goddammit, Taisia. You can't sneak up on a guy like that."
            scene sm1cs-tl005-10 haunted_house_stalker_tl_talk_bentover with dissolve
            play voice3 girl24_arrogant_hah noloop
            tl "I wasn't sneaking, I was clocking out."
            scene sm1cs-tl005-11 haunted_house_stalker_mc_talk_bentover with dissolve
            play voice2 mc_arrogant_huh2 noloop
            mc "Still! You can't walk around all quiet like that dressed up like that scary ass clown!"
        "Slap"(hint="sm1cs_tl005_m01_h02"):
            call sm1cs_tl005_m01_c02 from _call_sm1cs_tl005_m01_c02
            play voice2 mc_pain_argh1 noloop
            play voice3 girl24_scared_ah4 noloop
            play sound sfx_leg_kick1 volume 0.5
            play sound2 sfx_woodenspoon_slap2 noloop
            scene sm1cs-tl005-12 haunted_house_stalker_mc_talk_slap with hpunch
            pause
            play voice2 mc_scared_huuuh3 noloop
            stop music3 fadeout 10.0
            mc "Oh shit... I am so sorry, Taisia. I didn't mean to-"
            scene sm1cs-tl005-13 haunted_house_stalker_tl_talk_smirk with dissolve
            play voice3 girl24_happy_laugh1 noloop
            tl "Do it again."
            play sound sfx_skirt_off2
            scene sm1cs-tl005-14 haunted_house_stalker_mc_talk with dissolve
            play voice2 mc_surprised_what3 noloop
            mc "What?"
            scene sm1cs-tl005-15 haunted_house_stalker_tl_talk_turn with dissolve
            play voice3 girl24_sex_closedmoan5 noloop
            tl "That was hot. Do it again."
            scene sm1cs-tl005-16 haunted_house_stalker_mc_talk_turn with dissolve
            play voice2 mc_no_uhuhno noloop
            mc "No! What?"
    scene sm1cs-tl005-17 haunted_house_stalker_tl_talk with dissolve
    play voice3 girl24_arrogant_kgh1 noloop
    tl "Whatever. Come on, let's go."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    play sound3 sfx_door_open6 noloop
    scene sm1cs-tl005-18 haunted_house_stalker_mc_talk_walking with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Huh?"
    scene sm1cs-tl005-19 haunted_house_stalker_tl_talk_walking with dissolve
    play voice3 girl24_thinking_hmm1 noloop
    tl "We're leaving."
    scene sm1cs-tl005-20 haunted_house_stalker_mc_talk_walking with dissolve
    play voice2 mc_thinking_wait2 noloop
    mc "Wait, I thought you said you needed my help with something?"
    play voice3 girl24_arrogant_yeah3 noloop
    tl "Yeah. This."
    play sound sfx_door_open6
    scene sm1cs-tl005-21 haunted_house_stalker_mc_talk_walking_tlgone with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait..."
    play sound2 sfx_heels_run1 noloop
    scene sm1cs-tl005-22 haunted_house_stalker_mc_talk_runsout with dissolve
    play voice2 d2s12_emmm noloop volume 1.6
    mc "Wait - hang on!"
    stop music fadeout 6.0
    play sound sfx_heels_run2 loop
    play music3 amusement_park_music fadein 2.0
    play sound4 sfx_crowd_fightclub_ambient2 volume 0.24 fadein 3.0
    scene sm1cs-tl005-23 haunted_house_stalker_tl_talk_walkcircus with fade
    pause
    play sound2 sfx_heels_steps1
    scene sm1cs-tl005-24 haunted_house_stalker_mc_talk_walkcircus with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Wait, you texted me just to come and, what... walk you home?"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-tl005-25 haunted_house_stalker_tl_talk with dissolve
    play voice3 girl24_arrogant_yeah1 noloop
    tl "Maybe."
    scene sm1cs-tl005-26 haunted_house_stalker_mc_talk with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What-"
    scene sm1cs-tl005-27 haunted_house_stalker_dude_talk_aggro with dissolve
    play voice4 boy9_hey_angry noloop
    "Aggro Dude" "HEY! CLOWN BITCH!"
    "Aggro Dude" "I KNOW YOU HEARD ME!"
    scene sm1cs-tl005-28 haunted_house_stalker_tl_talk with dissolve
    play voice3 girl24_disappointed_neh noloop
    tl "Don't look at him, [mcname]."
    scene sm1cs-tl005-29 haunted_house_stalker_mc_talk with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What the hell-"
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-tl005-a32 stalker-dude-glambot-000 with dissolve
    play voice3 girl24_arrogant_hm1 noloop
    tl "Walk faster, come on."
    stop music3 fadeout 10.0
    $ renpy.music.set_volume(0.0, 0.0, "music" )
    $ renpy.music.set_volume(0.8, 0.0, "music2" )
    $ renpy.music.play(audio.music_error404_ver2, "music" , True, None, True, 4.5)
    $ renpy.music.play(audio.music_error404_ver3, "music2" , True, None, True, 4.5)
    play sound sfx_camera_fly1 volume 2.8
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    play sound3 ["<silence 3.5>", sfx_light_podium_1] noloop
    play music4 ["<silence 2.5>", "<from 0 to 2>audio/music/humble_bundle/music_horror_moment1.ogg"] noloop
    scene sm1cs_tl005-glambot-1
    pause 3.0
    play voice4 boy9_angry_argh6 noloop
    "Aggro Dude" "Bitch!"
    play voice3 girl24_disappointed_hmf noloop
    tl "[mcname]. Come on."
    play voice2 mc_yes_okay2 noloop
    mc "Okay, okay. I'm coming!"
    scene sm1cs-tl005-33 haunted_house_stalker_dude_talk_mcgone with dissolve
    play voice4 boy9_angry_argh7 noloop
    "Aggro Dude" "Hey, get the fuck out of my way!"
    "Aggro Dude" "Yo! Move!"
    "Aggro Dude" "Where the fuck did you go!?!"
    play sound4 sfx_parknight_crickets fadein 10.0 volume 0.55
    scene sm1cs-tl005-34 haunted_house_stalker_mc_talk_walk_park with fade
    pause
    play voice2 mc_hey_hey2 noloop
    mc "Wait, Taisia, just slow down for one sec!"
    $ renpy.music.set_volume(0.8, 4.0, "music" )
    $ renpy.music.set_volume(0.2, 6.0, "music2" )
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-tl005-35 haunted_house_stalker_tl_talk_fountain with dissolve
    play voice3 girl24_arrogant_huh2 noloop
    tl "What."
    scene sm1cs-tl005-36 haunted_house_stalker_mc_talk_walk_park with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Can you just tell me what the hell is going on?"
    scene sm1cs-tl005-37 haunted_house_stalker_tl_talk with dissolve
    play voice3 girl24_no_nah noloop
    tl "Nothing."
    menu:
        "Call her out"(hint="sm1cs_tl005_m02_h01"):
            call sm1cs_tl005_m02_c01 from _call_sm1cs_tl005_m02_c01
            scene sm1cs-tl005-38 haunted_house_stalker_mc_talk with dissolve
            play voice2 mc_angry_cough1 noloop
            mc "That's bullshit, Taisia."
            scene sm1cs-tl005-39 haunted_house_stalker_tl_talk with dissolve
            play voice3 girl24_disappointed_eeh2 noloop
            tl "[mcname]-"
            scene sm1cs-tl005-40 haunted_house_stalker_mc_talk with dissolve
            play voice2 mc_no_no4 noloop
            mc "No, no bullshit, Taisia. What the hell is going on?"
            play sound sfx_cloth_rustling4
            scene sm1cs-tl005-41 haunted_house_stalker_tl_sit with dissolve
            pause
        "Let her tell you in her own time"(hint="sm1cs_tl005_m02_h02"):
            play sound sfx_cloth_rustling4
            scene sm1cs-tl005-41 haunted_house_stalker_tl_sit with dissolve
            tl "..."
            mc "..."
            play voice3 girl24_disappointed_eeh2 noloop
            tl "...{w} Fine."
    jump sm1cs_tl005_fountain
label sm1cs_tl005_fountain:
    scene sm1cs-tl005-42 haunted_house_stalker_mc_sit with dissolve
    play voice3 girl24_thinking_emm1 noloop
    tl "I was working a few weeks ago and... a guy came in with his girlfriend..."
    play sound sfx_memory_cloud_change1
    scene sm1cs-tl005-43 haunted_house_stalker_tl_talk_hiding
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    play voice3 girl24_happy_mmm noloop
    tl "{i}It was the usual thing. I hid in my spot, heard him come in talking all big.{/i}"
    tl "{i}\"Oh, I ain't scared of shit. Only pussies get scared in haunted houses.\"{/i}"
    play voice3 girl24_angry_argh2 noloop
    play voice4 boy10_scared_huh noloop
    play sound2 funhouse_monster_out volume 0.4 noloop
    scene sm1cs-tl005-44 haunted_house_stalker_tl_talk_jumpout with hpunch
    tl "{i}So I jumped out, dressed all the way up.{/i}"
    play voice4 boy10_scared_ah1 noloop
    scene sm1cs-tl005-45 haunted_house_stalker_tl_talk_scared with hpunch
    tl "{i}And he screamed like a little girl.{/i}"
    play voice3 girl24_disgust_ooh2 noloop
    tl "{i}Worse, actually. You ever heard the noise makes when a little rabbit gets caught?{/i}"
    play sound sfx_memory_cloud_change1
    hide screen flashback_screen
    scene sm1cs-tl005-46 haunted_house_stalker_mc_talk_tl_lookdown
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    play voice2 mc_no_no10 noloop
    mc "Uhm... no. I can't say that I have..."
    $ renpy.music.set_volume(0.2, 16.0, "music" )
    $ renpy.music.set_volume(0.0, 6.0, "music2" )
    scene sm1cs-tl005-47 haunted_house_stalker_tl_talk_tl_lookdown with dissolve
    play voice3 girl24_thinking_hmm2 noloop
    tl "Well, that was the noise he made."
    tl "His girlfriend laughed so hard... I swear the dude looked like he was going to cry."
    tl "And then he looked at me, super pissed. Started screaming all the usual shit."
    scene sm1cs-tl005-48 haunted_house_stalker_tl_talk_tl_lookmc with dissolve
    play voice3 girl24_arrogant_hm4 noloop
    tl "\"I'll kill you bitch, you're a worthless piece of shit, yada, yada, ya.\""
    tl "It's all shit I've heard a million times before."
    scene sm1cs-tl005-49 haunted_house_stalker_tl_talk_tl_looksky with dissolve
    play voice3 girl24_angry_breath noloop
    tl "But this time... he started coming around. Started harassing me at work."
    tl "Started trying to follow me home..."
    scene sm1cs-tl005-50 haunted_house_stalker_mc_talk with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Oh..."
    mc "So you wanted me to walk you home..."
    scene sm1cs-tl005-51 haunted_house_stalker_tl_talk_lookmc with dissolve
    play voice3 girl24_happy_yeah3 noloop
    tl "Yeah. To make sure that dude doesn't follow me home."
    tl "But, it might be too late..."
    scene sm1cs-tl005-52 haunted_house_stalker_mc_talk with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "What do you mean?"
    play sound sfx_cloth_rustling2
    scene sm1cs-tl005-54 haunted_house_stalker_tl_talk with dissolve
    play voice3 girl24_disappointed_ohh1 noloop
    tl "I mean, one of my neighbors thinks he saw him prowling around my area. She thinks."
    tl "Which is... part of the reason I've been so hard up for money. I'm trying to save up for a new place."
    play sound sfx_cloth_rustling1
    scene sm1cs-tl005-55 haunted_house_stalker_mc_talk_standup with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Well why didn't you say something earlier?"
    stop music fadeout 20.0
    stop music2 fadeout 20.0
    play music3 music_fear_nothing fadein 20.0 volume 0.45
    scene sm1cs-tl005-56 haunted_house_stalker_tl_talkrritated with dissolve
    play voice3 girl24_surprised_huh4 noloop
    tl "Have you not met me, [mcname]? Being honest about my problems doesn't really go with the tough girl routine."
    scene sm1cs-tl005-57 haunted_house_stalker_mc_talk with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Fair point."
    scene sm1cs-tl005-58 haunted_house_stalker_tl_talk_sad with dissolve
    play voice3 girl24_arrogant_yeah3 noloop
    tl "Yeah..."
    tl "Anyways, that's enough of me spilling my guts for one night."
    scene sm1cs-tl005-59 haunted_house_stalker_tl_talk_neutral with dissolve
    play voice3 girl24_surprised_eeh2 noloop
    tl "You gonna' keep being a gentleman and walk me home?"
    scene sm1cs-tl005-60 haunted_house_stalker_tl_talk_walksup with dissolve
    play voice3 girl24_surprised_huh2 noloop
    tl "What?"
    tl "The hell are you looking at me like that for?"
    play sound sfx_cloth_rustling4
    scene sm1cs-tl005-61 haunted_house_stalker_tl_talk_hug with dissolve
    play voice3 girl24_surprised_oh3 noloop
    tl "The fuck..."
    scene sm1cs-tl005-62 haunted_house_stalker_mc_talk with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Thanks for being honest with me."
    scene sm1cs-tl005-63 haunted_house_stalker_tl_talk_hug with dissolve
    play voice3 girl24_pain_ou1 noloop
    tl "I-"
    scene sm1cs-tl005-64 haunted_house_stalker_mc_talk_hug with dissolve
    play voice2 d2s9_mchey noloop
    mc "Just, enjoy the moment."
    play voice3 girl24_sex_closedmoan4 noloop
    tl "I..."
    tl "..."
    play sound sfx_cloth_rustling5
    scene sm1cs-tl005-65 haunted_house_stalker_tl_talk_hug_back with dissolve
    pause
    scene sm1cs-tl005-66 haunted_house_stalker_tl_talk_step_back with dissolve
    play voice3 girl24_angry_cough2 noloop
    tl "All tight, moment over. Come on."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-tl005-67 haunted_house_stalker_mc_thought_walk with dissolve
    play voice2 d1s1_mmm noloop volume 2.0
    mct "I didn't realize Taisia had it so rough right now..."
    mct "But it makes a lot of things make a lot more sense."
    scene sm1cs-tl005-68 haunted_house_stalker_mc_thought_walk_look with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.8
    mct "But her looking for a place to live... that's something I should keep in mind."
    if player.get_choice("sm1ms_renovation_started"):
        mct "Maybe I can talk to her about moving into the studio."
    else:
        mct "Might come in handy one day."
    scene sm1cs-tl005-69 haunted_house_stalker_tl_talk_walk_look with dissolve
    play voice3 girl24_surprised_huh3 noloop
    tl "What?"
    scene sm1cs-tl005-70 haunted_house_stalker_mc_talk_walk_look with dissolve
    play voice2 d1s5_mchappy noloop volume 1.8
    mc "Just... thinking."
    scene sm1cs-tl005-71 haunted_house_stalker_tl_talk_walk_look with dissolve
    play voice3 girl24_arrogant_pff noloop
    tl "Don't get mushy on me now, [mcname]."
    tl "We still have plenty of porn to make!"
    scene sm1cs-tl005-72 haunted_house_stalker_tl_talk_walk_lookfprward with dissolve
    play voice3 girl24_angry_err1 noloop
    tl "And I swear to god, if you tell anyone this, I will end you."
    scene sm1cs-tl005-73 haunted_house_stalker_mc_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Your secret is safe with me, Taisia."
    scene sm1cs-tl005-74 haunted_house_stalker_tl_talk with dissolve
    play voice3 girl24_yes_aga noloop
    tl "It better be."
    tl "Otherwise I'm not putting out anymore."
    scene sm1cs-tl005-75 haunted_house_stalker_mc_talk with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.7
    mc "Hahahaha!"
    scene sm1cs-tl005-76 haunted_house_stalker_mc_tl_walkout with dissolve
    pause
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    stop sound4 fadeout 3.0
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    $ renpy.music.set_volume(1.0, 12.0, "music" )
    $ renpy.music.set_volume(1.0, 12.0, "music2" )
    $ renpy.music.set_volume(1.0, 10.0, "music3" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1cs_tl005_exit_to_free_roam
label sm1cs_tl005_exit_to_free_roam:
    $ StoryController.end_scene(TL_STORY, 2, 0, 2,  STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1cs_tl005_m01_c02:
    $ player.set_choice("sm1cs_tl005_slap_tl")
    return
label sm1cs_tl005_m02_c01:
    $ player.set_choice("sm1cs_tl005_call_tl_out")
    $ CharacterController.get_character("tl").add_point(1)
    return