image sm1mv02s08-a200-glam-mes = Movie(play = "images/MV/mv02/s08/anim/sm1mv02s08-a200-4x-60fps.webm", start_image = "sm1mv02s08-a200 airlock-explosion-000", image = "sm1mv02s08-a200 airlock-explosion-120", loop = False)
image sm1mv02s08-a200-glam-mh = Movie(play = "images/MV/mv02/s08/anim/sm1mv02s08-a200-1-4x-60fps.webm", start_image = "sm1mv02s08-a200-1 airlock-explosion-000", image = "sm1mv02s08-a200-1 airlock-explosion-120", loop = False)
image sm1mv02s08-ax-glam = Movie(play = "images/MV/mv02/s08/anim/sm1mv02s08-ax-2x-60fps.webm",     start_image = "sm1mv02s08-ax shield-impact-animation-00", image = "sm1mv02s08-ax shield-impact-animation-89", loop = False)
label sm1mv02_movie_replay_3:
label sm1mv02s08:
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 0.5, "music2" )
    $ renpy.music.play(audio.music_evilcoming_main, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_evilcoming_drums, "music2", True, None, True, 0.0)
    play sound4 sfx_spaceship_ambience1 fadein 1.5 volume 0.5
    if sm1mv02_character == "mes":
        $ renpy.music.set_volume(1.0, 0.0, "voice7" )
        $ renpy.music.set_volume(1.0, 0.0, "voisex7" )
        $ renpy.music.set_volume(0.0, 0.0, "voice8" )
        $ renpy.music.set_volume(0.0, 0.0, "voisex8" )
    else:
        $ renpy.music.set_volume(0.0, 0.0, "voice7" )
        $ renpy.music.set_volume(0.0, 0.0, "voisex7" )
        $ renpy.music.set_volume(1.0, 0.0, "voice8" )
        $ renpy.music.set_volume(1.0, 0.0, "voisex8" )
    scene sm1mv02s08-00 red-alert with Fade(0.5, 0.5, 0.5)
    pause
    play sound sfx_spaceship_call1
    scene sm1mv02s08-00 red-alert_sy_talk with dissolve
    play voice3 stacy_angry noloop
    sy "Communication from science division."
    scene sm1mv02s08-01 red-alert_mc_talk with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "On screen."
    play sound sfx_bleepbloopbleep1
    mc "I hope you have good news, Doctor."
    scene sm1mv02s08-02 red-alert_ns_talk with dissolve
    play sound sfx_keyboard_typing2 volume 2.0
    play voice4 nari_hey_unsure noloop
    ns "Captain, I've isolated the viral nucleotides, but the sequence is unstable. Every time I try to synthesize a binding agent, the protein folds collapse under the ionized plasma interference from the incubator."
    stop sound fadeout 1.0
    scene sm1mv02s08-03 red-alert_ns_talk_mcthinking with dissolve
    play voice4 nari_yes_emotional_phoned noloop
    ns "I can stabilize it with a counter-resonance field, but the math is beyond me."
    pause
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-04 red-alert_true_{sm1mv02_character}_talk_recruited")
    with dissolve
    play voice7 min_thinking_hmm2 noloop
    play voice8 lissa_thinking1 noloop volume 1.4
    mhmes "Captain, I believe my experience with harmonic phase alignments will aid Doctor Jaleera in locking the sequence down."
    scene sm1mv02s08-06 red-alert_mc_talk with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Good thinking, Spectre."
    scene sm1mv02s08-08_3 red-alert_ns_talk_smile_screen with dissolve
    play voice2 d2s9_mchey noloop
    mc "Doctor, we'll get you some help as soon as the Commander is done analyzing these sensor fluctuations."
    scene sm1mv02s08-08 red-alert_ns_talk_smile with dissolve
    play voice4 nari_happy_relief noloop
    ns "Thank you, Captain Ramses."
    scene sm1mv02s08-07 red-alert_mc_talk_nari with dissolve
    pause
    scene sm1mv02s08-08_2 red-alert_ns_talk_smile_screen with dissolve
    play voice4 nari_disappointed_mff noloop
    ns "It will be... disappointing to have our partnership end so soon."
    scene sm1mv02s08-09 red-alert_ns_talk_bittersweet with dissolve
    play voice4 nari_disappointed_eeh noloop
    ns "But my people are running out of time."
    scene sm1mv02s08-10 red-alert_mc_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course. Hornstar out."
    play sound sfx_spaceship_globe1
    scene sm1mv02s08-11 red-alert_sy_talk_mcglad with dissolve
    play voice3 stacy_surprised_ohmy1 noloop
    sy "This is great news, Captain."
    sy "You did it."
    scene sm1mv02s08-12 red-alert_mc_talk_nod with dissolve
    pause
    play sound sfx_cloth_rustling2 volume 1.6
    scene sm1mv02s08-13 red-alert_mc_talk with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "Everyone on the {i}Intreprid{/i} played their part, Commander."
    scene sm1mv02s08-14 red-alert_mc_talk_spectre with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Spectre, about how long do you think it will take for you to lock this cure down?"
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-15 red-alert_{sm1mv02_character}_talk_spectre")
    with dissolve
    play voice7 min_arrogant_heh1 noloop
    play voice8 dahlia_thinking_hmm2 noloop
    mhmes "I'll know more once I get to the lab. Shouldn't take longer than thirty minutes, Captain."
    scene sm1mv02s08-17 red-alert_mc_talk_spectre with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Best news I've heard all day."
    $ renpy.music.set_volume(1.0, 0.3, "music2" )
    play sound4 sfx_spaceship_siren1
    scene sm1mv02s08-18 red-alert_mc_talk_alarm with dissolve
    play voice2 mc_surprised_huh8 noloop
    "*alarms sounding*"
    play voice2 mc_hey_hey1 noloop
    mc "Report!"
    scene sm1mv02s08-19 red-alert_sy_talk_alarm with dissolve
    play voice3 stacy_scared_ah1 noloop
    sy "Kasaru Predator decloaking right off our bow, Captain!"
    scene sm1mv02s08-20 red-alert_mc_talk_redalert with dissolve
    play sound3 sfx_spaceship_shield_off1 noloop
    "*eerie space warping sound*"
    play voice2 mc_pain_argh1 noloop
    mc "Red alert!"
    scene sm1mv02s08-21 red-alert_sy_talk_ready with dissolve
    pause
    scene sm1mv02s08-22 red-alert_tl_talk_ready_joking with dissolve
    play voice5 girl24_happy_laugh2 noloop
    tl "At least they didn't catch you with your pants down, Captain."
    stop sound4 fadeout 1.0
    scene black
    show screen scene_transistion(_("To be continued..."))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene black
    show screen scene_transistion(_("Immediately"))
    with hpunch
    pause
    hide screen scene_transistion
    play sound4 sfx_spaceship_siren1 fadein 1.5 volume 0.5
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-24 red-alert_crewlookingout_{sm1mv02_character}")
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1mv02s08-25 red-alert_sy_talk_ready_sweating with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Captain... Nruaah...{w} We should..."
    scene sm1mv02s08-26 red-alert_sy_talk_fire with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Fire a full spread of torpedoes."
    scene sm1mv02s08-27 red-alert_mc_talk with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "Negative, Commander. They haven't fired on us yet."
    mc "There may be a chance to talk this out."
    scene sm1mv02s08-ax shield-impact-animation-00 with dissolve
    pause 0.1
    play sound sfx_sm1mv02s08_glambot1 volume 2.0
    scene sm1mv02s08-ax-glam
    "ZOOOPAW!"
    pause
    play voice2 mc_surprised_huh3 noloop
    play voice3 stacy_scared_ah4 noloop
    scene sm1mv02s08-28 red-alert_shake with vpunch
    pause
    scene sm1mv02s08-29 red-alert_shake_tl_talk with dissolve
    play voice5 girl24_thinking_emm2 noloop
    tl "So much for that hope."
    scene sm1mv02s08-30 red-alert_mc_talk with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Hail the Kasaru. Tell them we're engaging in important medical research and that lives are at stake."
    scene sm1mv02s08-31 red-alert_sy_talk with dissolve
    play voice3 stacy_pain_au2 noloop
    sy "No response, Captain."
    scene sm1mv02s08-32 red-alert_mc_talk with dissolve
    play voice2 mc_angry_errr5 noloop
    mc "Then fire all weapons. Show them the {i}Intrepid{/i} isn't just here to look pretty."
    play sound sfx_apocalypse
    scene sm1mv02s08-33 red-alert_hit with hpunch
    play voice2 mc_scared_huh2 noloop
    play voice3 stacy_scared_oof2 noloop
    "BOOM!"
    play sound2 [sfx_spaceship_error1, sfx_spaceship_error1, sfx_spaceship_error1] noloop
    scene sm1mv02s08-34 red-alert_tl_talk with dissolve
    play voice5 girl24_arrogant_yeah1 noloop
    tl "Shields at sixty-nine percent."
    scene sm1mv02s08-35 red-alert_mc_talk_grinning with dissolve
    play voice2 mc_happy_yay2 noloop volume 1.6
    mc "Nice.{w} I mean—that's bad!"
    scene sm1mv02s08-36 red-alert_mc_talk_lookcurious with dissolve
    play voice2 d2s9_confused noloop volume 2.6
    mc "Helm, engage evasive pattern Delta."
    scene sm1mv02s08-37 red-alert_tl_talk with dissolve
    play voice5 girl24_thinking_hmm1 noloop
    tl "Are we leaving the system, Captain?"
    scene sm1mv02s08-38 red-alert_mc_talk_resolve with dissolve
    play voice2 mc_no_no5 noloop volume 2.0
    mc "Not without a cure. Put us around the moon, give me some room to maneuver."
    scene sm1mv02s08-39 red-alert_sy_talk with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Aye, Captain."
    play sound sfx_spaceship_error1
    scene sm1mv02s08-40 red-alert_mc_talk_stand_shudder with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Computer, tactical map up."
    play sound sfx_bleepbloopbleep1
    scene sm1mv02s08-41 red-alert_mc_talk_stand_hologram with dissolve
    pause
    scene sm1mv02s08-42 red-alert_mc_talk_thinking with dissolve
    play voice2 d1s5_mcthinks noloop volume 2.2
    mc "..."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-43 red-alert_{sm1mv02_character}_talk")
    with dissolve
    play voice7 min_disappointed_ehh1 noloop
    play voice8 dahlia_angry_hm1 noloop
    mhmes "Captain, evasive pattern is stressing the engines. In thirty seconds we're going to lose our edge."
    mhmes "Or our engines."
    play sound sfx_spaceship_globe_swipe1
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-46 red-alert_mc_talk_point_{sm1mv02_character}")
    with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "There. That ion field created by the fourth and fifth planets."
    mc "Bring us there, Lieutenant Solo."
    scene sm1mv02s08-47 red-alert_tl_talk with dissolve
    play voice5 girl24_yes_happy noloop
    tl "Aye sir."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-49 red-alert_{sm1mv02_character}_talk")
    with dissolve
    play voice7 min_hey_greeting noloop volume 1.6
    play voice8 dahlia_thinking_oh noloop
    mhmes "Captain, I must suggest an alternate course. Going into the ion field will peel our shields off like an orange rind."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-50 red-alert_mc_talk_{sm1mv02_character}_movechair")
    with dissolve
    play voice2 mc_yes_yes3 noloop volume 2.0
    mc "Exactly, Commander."
    play sound sfx_leg_kick8
    scene sm1mv02s08-52 red-alert_mc_talk_sitfingers with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "And it will rob them of their stealth capability."
    mc "Give them a show, Lieutenant Solo. We don't want them losing that killer instinct."
    mc "Make our ass shake."
    scene sm1mv02s08-53 red-alert_tl_talk_smile with dissolve
    play voice5 girl24_yes_calm noloop volume 2.0
    tl "Yes, Captain. Commencing the Wiggle Wiggle Wah."
    scene sm1mv02s08-54 red-alert_mc_talk_smile with dissolve
    pause
    play sound sfx_spaceship_timetravel2
    scene sm1mv02s08-55 red-alert_mc_talk_leaning with dissolve
    "KRAKOW!"
    play sound2 sfx_spaceship_timetravel1 noloop
    scene sm1mv02s08-56 red-alert_mc_talk_hit with dissolve
    "ZKAOW!"
    scene sm1mv02s08-57 red-alert_mc_talk_nrrhl with dissolve
    play voice2 mc_pain_rrrr noloop volume 2.0
    mc "Nrrrh!"
    scene sm1mv02s08-58 red-alert_sy_talk with dissolve
    play voice3 stacy_pain_mmm2 noloop volume 1.6
    sy "Graah!"
    play sound sfx_boat_accident1
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-60 red-alert_{sm1mv02_character}_talk")
    with vpunch
    play voice7 min_scared_ah2 noloop
    play voice8 dahlia_angry_argh1 noloop
    mhmes "Fuck!"
    scene sm1mv02s08-61 red-alert_sy_talk_knees with dissolve
    play voice3 stacy_pain_mmm1 noloop
    sy "Nrrrnhnha."
    sy "Captain. Sorry sir... It's kicking in again."
    scene sm1mv02s08-62 red-alert_mc_talk_nod with dissolve
    play voice2 d14s16_smell noloop
    mc "*nods silently*"
    play sound sfx_leg_kick7
    scene sm1mv02s08-63 red-alert_mc_talk_pull with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "I need you, Orion. Don't give up yet."
    scene sm1mv02s08-64 red-alert_sy_talk_stand with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Aye, sir!"
    play sound sfx_heels_steps1
    scene sm1mv02s08-65 red-alert_mc_talk_lookforward with dissolve
    pause
    stop sound fadeout 1.0
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-67 red-alert_{sm1mv02_character}_talk")
    with dissolve
    play voice7 min_hey_angry2 noloop
    play voice8 dahlia_surprised_huh1 noloop
    mhmes "Captain. We just hit the ion storm."
    scene sm1mv02s08-68 red-alert_shields_fizzle with dissolve
    pause
    play sound sfx_spaceship_shield_off1
    scene sm1mv02s08-69 red-alert_shields_fizzle with dissolve
    pause
    scene sm1mv02s08-70 red-alert_mc_talk with dissolve
    play voice2 mc_arrogant_huh1 noloop volume 1.6
    mc "Course change, Solo."
    scene sm1mv02s08-71 red-alert_tl_talk with dissolve
    play voice5 girl24_yes_yeah noloop
    tl "I read you, Captain."
    scene sm1mv02s08-72 red-alert_sy_talk_grip with dissolve
    play voice3 stacy_angry_argh1 noloop
    sy "We just got here!"
    scene sm1mv02s08-73 red-alert_mc_talk with dissolve
    play voice2 mc_yes_aga1 noloop volume 2.0
    mc "We've got them right where we want them, Orion."
    scene sm1mv02s08-76 red-alert_sy_talk with dissolve
    play voice3 stacy_thinking_oh1 noloop
    sy "...Aye, Captain."
    scene sm1mv02s08-77 red-alert_mc_talk with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Gotcha."
    scene sm1mv02s08-78 red-alert_mc_talk_sy_grinning with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Commander, send them our regards."
    scene sm1mv02s08-79 red-alert_sy_talk with dissolve
    play voice3 stacy_angry noloop
    sy "Happy to, Captain."
    play sound sfx_spaceship_turret_start1
    scene sm1mv02s08-80 red-alert_sy_talk_torpedos with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Torpedos away."
    play sound2 sfx_spaceship_turret_shot1 noloop volume 2.0
    play sound3 sfx_spaceship_breakdown2 noloop volume 2.0
    play sound5 sfx_blaster_shot4 noloop
    scene sm1mv02s08-81 red-alert_kaboom with dissolve
    "KABOOM."
    scene sm1mv02s08-82 red-alert_tl_talk with dissolve
    play voice5 girl24_happy_yeah2 noloop
    tl "Take that..."
    scene sm1mv02s08-83 red-alert_sy_talk with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "Both torpedos hit. Kasarua 'Wingblade' is breaking up."
    scene sm1mv02s08-84 red-alert_mc_talk_sigh_sycheer with dissolve
    play voice2 mc_happy_wooh1 noloop
    play voice3 stacy_happy_relief1 noloop
    play voice4 girl24_happy_wooh noloop
    "Crew" "*cheers*"
    play voice2 mc_happy_oof3 noloop
    mc "Incredible work, everyone."
    mc "Solo, get us out of the ion storm if you will."
    scene sm1mv02s08-85 red-alert_tl_talk with dissolve
    play voice5 girl24_yes_aga noloop
    tl "Aye, Captain."
    play sound sfx_spaceship_timetravel2
    stop sound4 fadeout 4.0
    play sound3 sfx_spaceship_ambience1 fadein 2.0 volume 0.5
    scene sm1mv02s08-86 red-alert_planet_outofstorm with dissolve
    play voice5 girl24_thinking_hmm3 noloop
    tl "Leaving the ion storm."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-88 red-alert_{sm1mv02_character}_talk")
    with dissolve
    play voice7 min_thinking_oh noloop
    play voice8 dahlia_surprised_huh2 noloop
    mhmes "Captain. Another contact just popped up on sensors."
    mhmes "It can't be..."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-90 red-alert_mc_talk_concerned_{sm1mv02_character}")
    with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Hnh..."
    play sound sfx_spaceship_innerdamage1
    scene sm1mv02s08-91 red-alert_screen_hit with dissolve
    pause
    play sound2 sfx_apocalypse noloop
    scene sm1mv02s08-92 red-alert_tl_talk_fling with vpunch
    play voice5 girl24_scared_ah2 noloop
    tl "Ahhuaaaah!"
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-93 red-alert_{sm1mv02_character}_talk_blocklight")
    with hpunch
    play sound2 sfx_spaceship_innerdamage2 noloop
    play voice7 min_scared_ah4 noloop
    play voice8 dahlia_pain_argh noloop
    mhmes "Nrraaaah!"
    play sound3 sfx_spaceship_innerdamage3 noloop
    play sound4 sfx_spaceship_siren1 fadein 1.0 volume 0.5
    scene sm1mv02s08-95 red-alert_mc_talk with vpunch
    play voice2 mc_pain_ou6 noloop
    mc "Nrraaah!"
    play sound sfx_fall_down1 volume 1.5
    scene sm1mv02s08-96 red-alert_mc_talk_floor with dissolve
    play voice2 mc_pain_argh1 noloop
    mc "*groaning*"
    scene sm1mv02s08-97 red-alert_sy_talk_helpup with dissolve
    play voice3 stacy_hey noloop
    sy "Captain."
    scene sm1mv02s08-98 red-alert_mc_talk_standing with dissolve
    play voice2 mc_pain_ffff noloop
    mc "Damage report?"
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-100 red-alert_{sm1mv02_character}_talk_blood")
    with dissolve
    play voice7 min_scared_ah3 noloop
    play voice8 dahlia_pain_ah3 noloop
    mhmes "Damage to the jump core."
    mhmes "We've got Dickium leaks causing power fluctuations across the ship."
    scene sm1mv02s08-101 red-alert_tl_talk_calling with dissolve
    play voice5 girl24_scared_oof noloop
    tl "Captain. We've lost the shields."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-102 red-alert_{sm1mv02_character}_talk_lookscreen")
    with dissolve
    play voice7 min_surprised_ehh1 noloop
    play voice8 dahlia_old_upset noloop
    mhmes "Incoming enemy transporter signals, Captain."
    scene sm1mv02s08-104 red-alert_mc_talk_blaster with dissolve
    play voice2 mc_angry_oof noloop
    mc "Intrepid. This is the Captain. Boarders are incoming."
    mc "Prepare for battle!"
    scene sm1mv02s08-105 red-alert_sy_talk_blaster with dissolve
    pause
    play sound sfx_spaceship_shield_on1
    play sound2 [sfx_blaster_shot1, sfx_blaster_shot2, sfx_blaster_shot3, sfx_blaster_shot4]
    play sound3 ["<silence 0.4>", sfx_blaster_shot4, sfx_blaster_shot3, sfx_blaster_shot2, sfx_blaster_shot1]
    play sound5 ["<silence 0.8>", sfx_blaster_shot4, sfx_blaster_shot3, sfx_blaster_shot2, sfx_blaster_shot1]
    scene sm1mv02s08-106 red-alert_kasarubridge with dissolve
    play voice4 boy5_angry_ergh3 noloop volume 1.5
    pause
    scene sm1mv02s08-107 red-alert_kasarubridge_fire with dissolve
    play voice5 boy9_scared_ah4 noloop
    pause
    scene sm1mv02s08-108 red-alert_mc_talk_blasting with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "We have to get you to the lab, Spectre."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-110 red-alert_{sm1mv02_character}_talk")
    with dissolve
    play voice7 min_yes_serious noloop
    play voice8 dahlia_yes_yeah3 noloop
    mhmes "Aye, Captain!"
    scene sm1mv02s08-111 red-alert_ks1_talk with dissolve
    play voice4 boy5_angry_dagh1 noloop volume 1.6
    "Kasaru Warrior" "Blood and death!"
    play voice4 boy5_pain_argh2 noloop volume 1.6
    scene sm1mv02s08-112 red-alert_ks1_shot with vpunch
    pause
    scene sm1mv02s08-113 red-alert_tl_talk with dissolve
    play voice5 girl24_arrogant_kgh1 noloop
    tl "Go Captain!"
    play sound sfx_epic_jump1 volume 2.0
    play sound3 sfx_leg_kick2 noloop
    scene sm1mv02s08-114 red-alert_tl_talk_tackle with dissolve
    play voice4 boy5_pain_arrr noloop
    play voice5 girl24_angry_argh2 noloop
    tl "Nraaah!"
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-115 red-alert_{sm1mv02_character}_talk_to_corridor")
    with dissolve
    play voice7 min_old_disgusted noloop
    play voice8 dahlia_happy_relief noloop
    mhmes "Come on!"
    play sound sfx_heels_run2 loop
    play sound3 sfx_heels_run1 loop
    scene sm1mv02s08-117 red-alert_run_corridor with dissolve
    pause
    stop sound2 fadeout 2.0
    stop sound5 fadeout 2.0
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-119 red-alert_{sm1mv02_character}_talk_leading")
    with dissolve
    pause
    play voice7 min_angry_breath noloop
    play voice8 dahlia_disappointed_ehh2 noloop
    mhmes "Stars save us."
    play voisex5 boy4_sex_moans2 volume 1.5
    play voisex6 girl22_sex_openmoans1 volume 1.5
    scene sm1mv02s08-120 red-alert_mc_talk_crewsex with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "The virus is spreading."
    scene sm1mv02s08-121 red-alert_sy_talk with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Nrraaah... Yes..."
    sy "And it's so powerful, the crew can't stop fucking to fight."
    scene sm1mv02s08-122 red-alert_mc_talk_press ahead with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Come on!"
    play sound2 sfx_epic_jump1 noloop volume 2.0
    scene sm1mv02s08-123 red-alert_sy_mc_jump with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "Hup."
    play voice3 stacy_angryhuh noloop
    sy "Mmm."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-125 red-alert_{sm1mv02_character}_talk_to_smiling")
    with dissolve
    play voice7 min_disappointed_mph noloop
    play voice8 dahlia_happy_hmm1 noloop
    mhmes "Fascinating."
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1mv02s08-126 red-alert_mc_talk_shotbehind with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "Holy shatner."
    stop voisex5 fadeout 3.5
    stop voisex6 fadeout 3.5
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-127 red-alert_{sm1mv02_character}_talk")
    with dissolve
    play voice7 min_angry_cough noloop
    play voice8 dahlia_angry_argh1 noloop
    mhmes "Damn."
    scene sm1mv02s08-129 red-alert_kv_talk_point with dissolve
    play voice6 kanya_arrogant_huh noloop volume 1.6
    kv "End of the line, Alliance scum!"
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-130 red-alert_thinkwayout_{sm1mv02_character}")
    with dissolve
    pause
    if in_a_replay:
        jump sm1mv02_movie_replay_3_continue
    jump sm1mv02s08_mid_cut
label sm1mv02s08_mid_cut:
    scene sm1mv02s08-132 red-alert_kv_talk_point_monologue with dissolve
    play voice6 kanya_angry_breathing noloop volume 1.6
    kv "You destroyed our sister ship, and now we will destroy-"
    play voice6 kanya_scared_ah1 noloop
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    stop sound4 fadeout 1.0
    play sound sfx_music_shutdown1
    play sound2 sfx_blaster_shot3 noloop
    scene sm1mv02s08-133 red-alert_kv_talk_mannequin_fall with hpunch
    play sound3 sfx_leg_kick1 noloop
    queue music music_stacy_time
    kv "Ow!"
    play sound sfx_fall_down1 volume 1.6
    scene sm1mv02s08-134 red-alert_kv_talk_nofilmingmode with dissolve
    play voice6 kanya_happy_laugh5 noloop
    kv "Hahaha."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-136 red-alert_sy_talk_{sm1mv02_character}_laugh")
    with dissolve
    if player.get_choice("sm1mv02s02_recruit_mes"):
        play voice7 min_old_laugh noloop
        mes "Heheh."
        play sound2 sfx_videocamera_finish noloop
        play voice3 stacy_happy_laugh2 noloop
        sy "Haha. Cut."
    elif player.get_choice("sm1mv02s02_recruit_mh"):
        play voice8 lissa_laugh noloop
        mh "Haha. You don't see that every day."
        play voice3 stacy_thinking_oh2 noloop
        sy "Oh no. Haha."
        play sound2 sfx_videocamera_finish noloop
        sy "Let's cut."
    play sound sfx_heels_steps1 loop
    scene sm1mv02s08-137 red-alert_mc_talk_walkover with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "You okay, Kanya?"
    play sound sfx_cloth_rustling3 volume 1.6
    scene sm1mv02s08-138 red-alert_mc_talk_pull_mannequin with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Anything hurt?"
    scene sm1mv02s08-139 red-alert_kv_talk_helpup with dissolve
    play voice6 kanya_arrogant_laugh noloop
    kv "Just my pride. I thought I the mannequins all secured for the shot."
    kv "I guess this guy was loose."
    play sound sfx_skirt_off2
    scene sm1mv02s08-140 red-alert_mc_talk_mannequinbackup with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "There we go. Good as new."
    play voice6 kanya_disappointed_hm noloop
    kv "Thanks, [mcname]."
    scene sm1mv02s08-141 red-alert_ns_talk_camera with dissolve
    play voice4 nari_surprised_ehh noloop
    ns "Everything okay?"
    scene sm1mv02s08-142 red-alert_mc_talk_thumbsup with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, Nari. Just some technical difficulties."
    scene sm1mv02s08-143 red-alert_mc_talk_tl_checkcamera with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "We good to start again, Taisia?"
    scene sm1mv02s08-144 red-alert_tl_talk with dissolve
    play voice5 girl24_yes_ugu noloop
    tl "I think so. I only know so much about being a camera girl."
    scene sm1mv02s08-145 red-alert_tl_thinking with dissolve
    play voice5 girl24_arrogant_huh1 noloop
    tl "Funny that I haven't tried out being a camgirl."
    play sound sfx_heels_steps1 loop
    scene sm1mv02s08-146 red-alert_sy_talk_walktl with dissolve
    play voice3 stacy_mmm2 noloop
    sy "Well, you're only being a camera girl for a few more shots."
    stop sound fadeout 1.0
    scene sm1mv02s08-147 red-alert_tl_talk with dissolve
    play voice5 girl24_arrogant_yeah2 noloop
    tl "Yeah yeah."
    scene sm1mv02s08-148 red-alert_tl_talk_look camera with dissolve
    play voice5 girl24_thinking_hmm4 noloop
    tl "Alright. I'm set."
    tl "You guys set?"
    play sound sfx_heels_steps1 loop
    scene sm1mv02s08-149 red-alert_mc_talk_walkback with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "Let's do this."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-150 red-alert_{sm1mv02_character}_talk_ready")
    with dissolve
    if player.get_choice("sm1mv02s02_recruit_mes"):
        play voice7 min_yes_aga noloop
        mes "Always ready."
    elif player.get_choice("sm1mv02s02_recruit_mh"):
        play voice8 dahlia_thinking_hmm1 noloop
        mh "Ready and willing, Miss Lindvuist."
    stop music fadeout 3.0
    stop sound fadeout 1.0
    scene sm1mv02s08-152 red-alert_tl_talk with dissolve
    play voice5 girl24_disappointed_eeh1 noloop
    tl "And...{w} Action!"
    play sound2 sfx_videocamera_start noloop
    jump sm1mv02s08_mid_continue
label sm1mv02_movie_replay_3_continue:
label sm1mv02s08_mid_continue:
    if in_a_replay:
        pass
    else:
        play sound4 sfx_spaceship_siren1 volume 0.4
        $ renpy.music.play(audio.music_evilcoming_main, "music" , True, None, True, 0.0)
        $ renpy.music.play(audio.music_evilcoming_drums, "music2", True, None, True, 0.0)
    scene sm1mv02s08-132 red-alert_kv_talk_point_monologue with dissolve
    play voice6 kanya_angry_breathing noloop volume 1.6
    kv "You destroyed our sister ship, and now we will destroy you."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-161 {sm1mv02_character}-sy-grim-look_c1")
    with dissolve
    play voice3 stacy_arrogant_hmm2 noloop
    sy "Hngh..."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-162 {sm1mv02_character}-sy-shooting-blaster-eat-phaser-gorgeous_c1")
    with dissolve
    play voice3 stacy_arrogant_laugh1 noloop
    sy "Eat phaser, 'gorgeous'!"
    play sound sfx_blaster_shot4
    scene sm1mv02s08-163 kv-hit-baster-gaah_c1 with dissolve
    play voice6 kanya_scared_ah2 noloop
    kv "Graaah!"
    play sound2 sfx_heels_run2 volume 1.5
    play sound [sfx_blaster_shot1, sfx_blaster_shot2, sfx_blaster_shot3, sfx_blaster_shot4] loop
    play voice3 stacy_angry_breath1 noloop
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-164 {sm1mv02_character}-sy-shooting-starts-running-airlock_c1")
    with dissolve
    pause
    stop sound fadeout 1.0
    play sound3 sfx_armored_footsteps1
    scene sm1mv02s08-165 aliens-chase-sy-down-corridor_c1 with dissolve
    pause
    scene sm1mv02s08-166 mc-calls-sy-lientenant_c1 with dissolve
    play voice2 mc_hey_hey1 noloop volume 1.7
    mc "Lientenant!"
    scene sm1mv02s08-167 sy-running-away-laughing-haha-aliens-chase_c1 with dissolve
    play voice3 stacy_laugh noloop
    sy "Hahaha."
    play sound2 sfx_fall_mud1 noloop
    stop sound3 fadeout 1.0
    scene sm1mv02s08-168 aliens-corner-sy_c1 with dissolve
    pause
    play sound sfx_epic_jump1 volume 2.0
    scene sm1mv02s08-169 sy-slides-beneath-aliens_c1 with dissolve
    pause
    play sound2 ["<silence 0.3>", sfx_blaster_shot3] noloop
    play sound3 sfx_blaster_shot3 noloop
    scene sm1mv02s08-170 sy-other-side-airlockaliens-point-her_c1 with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    pause
    scene sm1mv02s08-171 sy-looks-back-mc-badass_c1 with dissolve
    pause
    scene sm1mv02s08-172 sy-it-alright-captain_c1 with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "It's alright, Captain."
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-173 {sm1mv02_character}-mc-watch-sy_c1")
    with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "..."
    scene sm1mv02s08-174 sy-points-blaster-panel-no-one-puts-corner_c1 with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "No one puts Commander Luffie Orion in a corner!"
    play sound sfx_blaster_shot2
    scene sm1mv02s08-175 sy-blasts-control-panel_c1 with dissolve
    "CLICK"
    play sound sfx_apocalypse
    play sound2 sfx_weather_tornado1
    play sound3 sfx_boat_accident1 noloop
    scene sm1mv02s08-176 sy-traps-herself-with-aliens_c1 with dissolve
    "ZAPP!"
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-177 {sm1mv02_character}-mc-looking-helpless_c1")
    with dissolve
    play voice4 otherchar_spaceshipcomputer_alert1 noloop volume 2.0
    "Computer" "Alert. Catostrophic damage to airlock safety locks."
    scene sm1mv02s08-178 mc-grim-sad_c1 with dissolve
    pause
    scene sm1mv02s08-179 mc-salutes-god-speed-orion_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop volume 2.5
    mc "Good speed, Orion."
    scene sm1mv02s08-180 computer-announce-alert_c1 with dissolve
    play voice4 otherchar_spaceshipcomputer_alert2 noloop volume 2.0
    "Computer" "Alert! Airlock decompressing. All personnel should evacuate immediately."
    scene sm1mv02s08-a200 airlock-explosion-000 with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "Heh.{w} That's the plan."
    play sound sfx_sm1mv02s08_glambot2 volume 2.0
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-a200-glam-{sm1mv02_character}")
    stop sound2 fadeout 2.0
    play sound5 sfx_door_scifi_open1 noloop
    pause
    play voice2 mc_scared_huuuh1 noloop
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-182 {sm1mv02_character}-mc-cant-believe-shocked_c1")
    with dissolve
    pause
    stop sound fadeout 3.0
    scene sm1mv02s08-183 mc-fist-hand-arnold-meme_c1 with dissolve
    pause
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-184 {sm1mv02_character}-captain-synthesizer-mc-know_c1")
    with dissolve
    play voice7 min_surprised_ehh1 noloop
    play voice8 dahlia_disappointed_hmm2 noloop
    mhmes "Captain. The Synthesizer."
    play voice2 mc_yes_yeah5 noloop
    mc "I know, Spectre.{w} I know..."
    play sound sfx_heels_run1 loop
    play sound2 sfx_heels_run2
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-185 {sm1mv02_character}-mc-running-towards-lab_c1")
    with dissolve
    pause
    stop sound2 fadeout 1.0
    play sound sfx_bleepbloopbleep1
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-186 {sm1mv02_character}-guards-mc-enters-code-lab_c1")
    with dissolve
    pause
    $ renpy.music.set_volume(0.5, 6.5, "music" )
    $ renpy.music.set_volume(0.0, 1.5, "music2" )
    stop sound4 fadeout 1.0
    if in_a_replay:
        $ renpy.music.set_volume(1.0, 0.0, "voice7" )
        $ renpy.music.set_volume(1.0, 0.0, "voisex7" )
        $ renpy.music.set_volume(1.0, 0.0, "voice8" )
        $ renpy.music.set_volume(1.0, 0.0, "voisex8" )
        $ renpy.music.set_volume(1.0, 1.5, "music" )
        $ renpy.music.set_volume(1.0, 1.5, "music2" )
        stop music fadeout 3.0
        stop music2 fadeout 3.0
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
        $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
        $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
        jump sm1mv02_movie_replay_4
    jump sm1mv02s08_cut
label sm1mv02s08_cut:
    play sound2 sfx_videocamera_finish noloop volume 1.6
    scene sm1mv02s08-187 sy-calls-cut_c1 with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "And cut!"
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s08-188 mc-phew-that-intense_c1 with dissolve
    elif player.get_choice("sm1mv02s02_recruit_mh"):
        scene sm1mv02s08-192 mc-got-intense-mh-was-looked-easy-you_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Phew. That got intense."
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s08-189 mes-really-good-work-mc-yeah_c1 with dissolve
        play voice7 min_thinking_hmm3 noloop
        mes "Really good work, [mcname]."
        scene sm1mv02s08-190 mc-strange-seeing-stacy-spaced-or-imagining-it_c1 with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "Yeah."
        if persistent.is_special:
            mc "Strange seeing my sister get sucked out into space."
        else:
            mc "Strange seeing my girlfriend get sucked out into space."
        mc "Or imagining it and acting like I saw it."
        scene sm1mv02s08-191 mes-supportive-think-did-great-painful-focused_c1 with dissolve
        play voice7 min_thinking_hmm1 noloop
        mes "I think you did great. Painful, but still grimly focused."
    else:
        mh "It was? It looked so easy for you, [mcname]."
        scene sm1mv02s08-193 mh-mean-all-saw-stacy-but-had-me-believe_c1 with dissolve
        play voice8 lissa_thinking2 noloop
        mh "I mean all we saw was Stacy sitting down."
        mh "But you had me believing I was seeing exactly what's in the script."
        scene sm1mv02s08-194 mh-you-real-knack-this-stuff_c1 with dissolve
        play voice8 lissa_hey noloop
        mh "You've got a real knack for this stuff."
        scene sm1mv02s08-195 mc-thanks-lyssa-did-great-too_c1 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Thanks, Lyssa."
        mc "You did great too."
        scene sm1mv02s08-196 mh-smiles-did-didnt-i_c1 with dissolve
        play voice8 lissa_haha noloop
        mh "I did, didn't I?"
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-197 {sm1mv02_character}-gang-gathered-sy-great-work-everybody_c1")
    with dissolve
    play voice3 stacy_hey_angry1 noloop
    sy "Great work, everyone. That's a wrap for today."
    scene sm1mv02s08-198 sy-think-outdid-ourselves-hopefully-epic-death-look-cool_c1 with dissolve
    play voice3 stacy_surprised_ah1 noloop
    sy "I think we outdid ourselves."
    sy "And hopefully my epic death scene will look as cool as I imagined it."
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s08-199 mes-previs-badass-death-sy-aah-tnx-min_c1 with dissolve
        play voice7 min_arrogant_heh2 noloop
        mes "If those pre-vis you showed are anything to judge by, it will be a death worthy of a badass, Stacy."
        play voice3 stacy_disappointed_oh3 noloop
        sy "Ahhh. Thanks, Min."
    else:
        scene sm1mv02s08-199 mh-previs-badass-death-sy-aah-tnx-min_c1 with dissolve
        play voice8 dahlia_thinking_hmm4 noloop
        mh "I'm still not sure about the scene going that direction, Stacy."
        mh "I didn't imagine much death in a porno."
        scene sm1mv02s08-201 sy-cocky-smile-this-our-style-pron_c1 with dissolve
        play voice3 stacy_thinking_emm4 noloop
        sy "Well this is {i}our{/i} style of porno, and every Sci-Fi epic needs some epic deaths."
        scene sm1mv02s08-202 sy-laughs-besides-bunch-scifi-who-knows-happens-next-one_c1 with dissolve
        play voice3 stacy_happy_laugh2 noloop
        sy "Besides, a bunch of Sci-Fi shows always figure out a way to bring people back."
        sy "Who knows what might happen on the next 'Star Voyage' flick?"
        scene sm1mv02s08-203 mh-agrees-guess-true-mc-haha-one-movie-time_c1 with dissolve
        play voice8 dahlia_thinking_mmm2 noloop
        mh "I guess that's true."
        play voice2 d3s11b_mcheh noloop volume 1.6
        mc "Haha. Hey. One movie at a time you two."
    jump sm1mv02s08_end_talk
label sm1mv02s08_end_talk:
    scene sm1mv02s08-204 mc-ahem-gets-attention_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Ahem."
    scene sm1mv02s08-205 mc-talking-just-want-second-stacy-this-was-big-one_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Just want to second everything Stacy said."
    mc "This was the big scene, and everyone did amazing!"
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-206 {sm1mv02_character}-sy-kv-listen-mc_c1")
    with dissolve
    pause
    scene sm1mv02s08-208 mc-stacy-i-go-through-everything-that-leaves-one-more-scene_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Stacy and I will go through everything and make sure we have all the pieces we need, but I'm feeling confident on this one."
    mc "So that leaves us with one more scene to do."
    scene sm1mv02s08-209 mc-lucky-us-naughty-one_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "And lucky for us, its a naughty one."
    scene sm1mv02s08-210 mc-whoo_c1 with dissolve
    play voice3 stacy_happy_wooh1 noloop
    sy "Woohoo."
    scene sm1mv02s08-211 mc-till-then-just-make-sure-put-costumes-back-looking-you-tl_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "But until then, you're all free to head home. Just make sure we put our costumes back where they belong."
    mc "Looking at you, Taisia."
    scene sm1mv02s08-212 tl-pops-smiling_c1 with dissolve
    play voice5 girl24_arrogant_kgh2 noloop
    pause
    scene sm1mv02s08-213 tl-such-meanie-was-about-go-clubbing_c1 with dissolve
    play voice5 girl24_arrogant_huh2 noloop
    tl "You're such a meanie, [mcname]."
    tl "I was just about to rock the club in this getup."
    scene sm1mv02s08-214 mc-laughs_c1 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "Hahaha."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    $ renpy.scene()
    $ renpy.show(f"sm1mv02s08-216 {sm1mv02_character}-gang-leaves-set_c1")
    with dissolve
    pause
    $ renpy.music.set_volume(1.0, 0.0, "voice7" )
    $ renpy.music.set_volume(1.0, 0.0, "voisex7" )
    $ renpy.music.set_volume(1.0, 0.0, "voice8" )
    $ renpy.music.set_volume(1.0, 0.0, "voisex8" )
    $ renpy.music.set_volume(1.0, 1.5, "music" )
    $ renpy.music.set_volume(1.0, 1.5, "music2" )
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(MOVIE_SCIFI, 3, 0, 5)
    return