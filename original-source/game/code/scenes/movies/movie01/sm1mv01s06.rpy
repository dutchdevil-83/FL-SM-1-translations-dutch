image sm1mv01s06-a110-glambot = Movie(play = "images/MV/mv01/s06/anim/sm1mv01s06-a110-2x-60fps.webm", start_image = "sm1mv01s06-a110 canon-shot-glambot-000", image = "sm1mv01s06-a110 canon-shot-glambot-200", loop = False)
image sm1mv01s06-a153-glambot = Movie(play = "images/MV/mv01/s06/anim/sm1mv01s06-a153-2x-60fps.webm", start_image = "sm1mv01s06-a153 swordfight-glambot-000", image = "sm1mv01s06-a153 swordfight-glambot-180", loop = False)
label sm1mv01s06:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    scene sm1mv01s06-00 clashing_swords_mc_talk with dissolve
    play sound sfx_pen_writing4 volume 1.6
    play music vidala_en_verde volume 0.75
    play voice2 mc_yes_okay2 noloop
    mc "Time for the epic duel between Captain Dickhart and the Pirate Queen Tempstra!"
    scene sm1mv01s06-01 clashing_swords_sy_talk with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "We can finally see who is better with a sword."
    scene sm1mv01s06-02 clashing_swords_mc_talk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Stacy, we're not just going to be whacking each other to see surrenders first."
    mc "We're going to plan it out. Every step, every feint, every lunge."
    scene sm1mv01s06-03 clashing_swords_sy_talk_not_enthused with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "Oh pooo."
    scene sm1mv01s06-04 clashing_swords_sy_talk_brightenup with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "Maybe we can try that on another movie."
    scene sm1mv01s06-05 clashing_swords_kv_talk_fightingpose with dissolve
    play voice5 kanya_yes_long noloop
    kv "Yes. A full melee.{w} Oooh! Maybe something with gladiators."
    scene sm1mv01s06-06 clashing_swords_kv_talk_title_hands with dissolve
    play voice5 kanya_happy_relief2 noloop
    kv "Gladiators Unchained: An Erotic Adventure."
    scene sm1mv01s06-07 clashing_swords_tl_talk with dissolve
    play voice4 girl24_yes_yeah noloop
    tl "I'd watch it."
    scene sm1mv01s06-08 clashing_swords_mc_talk_focus_back with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Alright. I have watched about twenty hours of classic scallywag movie fights, and just as much time watching lessons on modern fighting techniques."
    scene sm1mv01s06-09 clashing_swords_mc_talk_gesturing_sy with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "We're going to make the best sword fight since 'Booty Buccaneers of the Bahamas."
    scene sm1mv01s06-10 clashing_swords_mc_talk_cannonnball with fade
    play sound sfx_throw_something1
    play voice2 mc_happy_oof2 noloop
    mc "-and then I'll get hit by the cannonball."
    play sound sfx_fall_down1
    scene sm1mv01s06-11 clashing_swords_mc_talk_cannonnball_down with dissolve
    play voice2 mc_angry_errr3 noloop
    mc "Ahhh!"
    play sound sfx_sand_jump1
    scene sm1mv01s06-12 clashing_swords_mc_talk_cannonnball_getsup with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "And Stacy will think I'm down."
    scene sm1mv01s06-13 clashing_swords_mc_talk_walk with dissolve
    play voice2 d2s9_confused noloop volume 1.4
    mc "And then-"
    scene sm1mv01s06-14 clashing_swords_mc_talk_gestures with dissolve
    play voice2 mc_hey_hey6 noloop
    mc "Taisia, you will be over here."
    scene sm1mv01s06-15 clashing_swords_tl_talk_walk with dissolve
    play voice4 girl24_yes_ugu noloop
    tl "Alright."
    scene sm1mv01s06-16 clashing_swords_tl_talk_walk_position with dissolve
    play voice4 girl24_thinking_hmm6 noloop
    tl "Good?"
    play sound sfx_cloth_rustling2
    scene sm1mv01s06-17 clashing_swords_mc_talk_frame with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Yes!"
    play sound sfx_throw_something1
    scene sm1mv01s06-18 clashing_swords_mc_talk_playacting with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Taisia will be fighting Kanya and Skeleton Bob at the same time."
    scene sm1mv01s06-19 clashing_swords_mc_talk_skeleton with dissolve
    play voice4 girl24_surprised_oh1 noloop
    tl "Nice. Showing off my amazing cutlass skills."
    play sound sfx_sword_equiped1
    scene sm1mv01s06-20 clashing_swords_mc_talk_skeleton with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Bingo."
    scene sm1mv01s06-21 clashing_swords_mc_talk_directing with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "And then Slash! You cut off Bob's arm."
    play sound sfx_sword_hit_metal2
    scene sm1mv01s06-22 clashing_swords_mc_talk_tlslash with dissolve
    play voice4 girl24_angry_argh2 noloop
    pause
    scene sm1mv01s06-23 clashing_swords_mc_talk_screaming with dissolve
    play voice2 mc_pain_argh1 noloop
    mc "Bahuaah!"
    play sound sfx_bones_twist1
    play sound2 sfx_bones_wrench noloop
    scene sm1mv01s06-24 clashing_swords_mc_talk_point with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "He goes down, screaming in pain."
    scene sm1mv01s06-25 clashing_swords_tl_talk_raisehand with dissolve
    play voice5 kanya_thinking_eeh3 noloop
    kv "Question. The skeleton pirate feels pain?"
    scene sm1mv01s06-26 clashing_swords_mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yup. It's all part of his curse."
    scene sm1mv01s06-27 clashing_swords_mc_talk_ask with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "And then what happens next, Kanya?"
    scene sm1mv01s06-28 clashing_swords_kv_talk_pretend with dissolve
    play voice5 kanya_yes_aga4 noloop
    kv "My character manages to stab Taisia."
    play sound sfx_socks_dancing1
    scene sm1mv01s06-29 clashing_swords_kv_talk_stabbed with dissolve
    play voice5 kanya_angry_argh noloop
    kv "Arrrgh!"
    play sound sfx_sword_hit_human1
    scene sm1mv01s06-30 clashing_swords_tl_talk_pain with dissolve
    play voice4 girl24_pain_ah noloop
    tl "Ahhuaah!"
    tl "*dramatically* The pain!"
    scene sm1mv01s06-31 clashing_swords_tl_talk_pain_angry with dissolve
    play voice4 girl24_angry_err1 noloop
    tl "You bitch. I'll kill you!"
    scene sm1mv01s06-32 clashing_swords_mc_talk_directing with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "In a fit of rage, Scarlet Searose headbutts Tempesta's helmsman."
    play sound sfx_leg_kick8
    scene sm1mv01s06-33 clashing_swords_tl_talk_headbutt with dissolve
    play voice4 girl24_disappointed_oof noloop
    tl "Boop."
    scene sm1mv01s06-34 clashing_swords_kv_talk_laugh with dissolve
    play voice5 kanya_happy_laugh2 noloop
    kv "Hahaha."
    play sound sfx_fall_down1 volume 1.5
    scene sm1mv01s06-35 clashing_swords_kv_talk_fall with dissolve
    play voice5 kanya_pain_aah2 noloop
    kv "Kiah!{w} I am knocked out."
    scene sm1mv01s06-36 clashing_swords_mc_talk_gesture_sy with dissolve
    play voice2 mc_thinking_mmm4 noloop volume 1.8
    mc "The threat is over...{w} But just for a moment."
    mc "The music intensifies, the battle rages on..."
    scene sm1mv01s06-37 clashing_swords_mc_talk_sy_enter with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "And the dread Pirate Queen Tempestra arrives."
    mc "Ready to strike the killing blow on Searose."
    play sound sfx_sword_whoosh4
    scene sm1mv01s06-38 clashing_swords_sy_talk_behind with dissolve
    play voice4 girl24_scared_ah1 noloop
    tl "No..."
    scene sm1mv01s06-40 clashing_swords_sy_talk_blow with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "It be..."
    scene sm1mv01s06-42 clashing_swords_sy_talk_look_mc with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "Crap."
    sy "What is the line again, [mcname]?"
    play sound sfx_paper_rustl2
    scene sm1mv01s06-43 clashing_swords_mc_talk_frustrated with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "Come on, Stacy. We've been practicing this every day."
    scene sm1mv01s06-44 clashing_swords_sy_talk_reply with dissolve
    play voice3 stacy_yeahno noloop
    sy "I know, but it's a little strange with all this positioning."
    sy "It's more and more stuff to remember."
    play sound sfx_sword_whoosh3
    scene sm1mv01s06-45 clashing_swords_sy_talk_swing with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Can't we just do freestyle?"
    scene sm1mv01s06-46 clashing_swords_kv_talk with dissolve
    play voice4 girl24_surprised_huh2 noloop
    tl "Freestyle?"
    scene sm1mv01s06-47 clashing_swords_mc_talk with dissolve
    play voice2 mc_no_no6 noloop
    mc "No, we can't just do it freestyle."
    mc "We want things to look good, tight, and skilled."
    mc "We're not just going to be whacking away at each other with swords and shouting our lines and hoping it will look good."
    scene sm1mv01s06-48 clashing_swords_tl_talk with dissolve
    play voice4 girl24_thinking_ah noloop
    tl "That {i}does{/i} sound like fun, though."
    scene sm1mv01s06-49 clashing_swords_sy_talk with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "See. Thanks Taisia."
    scene sm1mv01s06-50 clashing_swords_mc_talk_irritated with dissolve
    play voice2 mc_no_no1 noloop
    mc "We're not doing that."
    mc "I planned out every step of this battle, and it has the rhythm and flow of a fight from a legit movie."
    mc "End of discussion."
    scene sm1mv01s06-51 clashing_swords_sy_talk_tongue_out with dissolve
    play voice3 stacy_arrogant_laugh1 noloop
    sy "Okay, okay, Mister Bossy."
    play sound sfx_hair_scratch1
    scene sm1mv01s06-52 clashing_swords_mc_talk_hair with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Phew."
    scene sm1mv01s06-53 clashing_swords_mc_talk_turn with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay, where were we?"
    scene sm1mv01s06-54 clashing_swords_sy_talk_smirk with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "You still haven't given me my line, [mcname]."
    play voice2 mc_surprised_oh2 noloop
    mc "Shit. Sorry."
    sy "It's okay, [mcname]."
    scene sm1mv01s06-57 clashing_swords_mc_talk_check_clipboard with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Line line line."
    mc "Ah, right here."
    scene sm1mv01s06-58 clashing_swords_mc_talk_point_sy with dissolve
    play voice2 mc_angry_errr6 noloop
    mc "\"It be time you returned to the sea, Searose.\""
    mc "Go."
    scene sm1mv01s06-59 clashing_swords_sy_talk_point_position with dissolve
    play voice3 stacy_angryhuh noloop
    sy "It be time you returned to the sea, Searose."
    scene sm1mv01s06-60 clashing_swords_mc_talk_happy with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "Perfect. Then I'll come in."
    play sound sfx_skirt_off2
    scene sm1mv01s06-61 clashing_swords_mc_talk_check_phone with dissolve
    pause
    play sound [sfx_hands_clap3, sfx_hands_clap4]
    scene sm1mv01s06-62 clashing_swords_mc_talk_clap with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Nice work, everyone."
    scene sm1mv01s06-63 clashing_swords_mc_talk_break with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Let's break for ten, then we'll get suited up and run it live."
    scene sm1mv01s06-64 clashing_swords_tl_talk_excited with dissolve
    play voice4 girl24_happy_phew2 noloop
    tl "Finally!"
    scene sm1mv01s06-65 clashing_swords_sy_talk_kv_tl_walkoff with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "Hey, you okay?"
    scene sm1mv01s06-66 clashing_swords_mc_talk_smile_menu with dissolve
    menu:
        "I wish everyone were more focused":
            scene sm1mv01s06-67 clashing_swords_mc_talk_frustrated_menu with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "I'll feel better if we ran into less problems."
            scene sm1mv01s06-68 clashing_swords_sy_talk_menu with dissolve
            play voice3 stacy_thinking_hmm1 noloop
            sy "Fewer."
            scene sm1mv01s06-69 clashing_swords_mc_talk_menu_notamused with dissolve
            play voice2 mc_yes_yes3 noloop
            mc "Fewer. Yes."
            scene sm1mv01s06-70 clashing_swords_sy_talk_menu_reminding with dissolve
            play voice3 stacy_thinking_emm4 noloop
            sy "This is probably the biggest action scene until the next one."
            sy "We knew it would take a lot out of us."
            scene sm1mv01s06-71 clashing_swords_sy_talk_menu_thinking with dissolve
            play voice3 stacy_arrogant_huh1 noloop
            sy "Do we want to hit pause and take a stab at it another day."
            scene sm1mv01s06-72 clashing_swords_mc_talk_menu_nodhead with dissolve
            play voice2 mc_no_no8 noloop
            mc "No. Can't do that."
            mc "We gotta keep working. If we lose a day of work, that's hours we don't get back."
            scene sm1mv01s06-73 clashing_swords_sy_talk_menu with dissolve
            play voice3 stacy_disappointed_oh2 noloop
            sy "I know. But... at the end of the day, this isn't supposed to be super stressful."
            scene sm1mv01s06-74 clashing_swords_mc_talk_menu_smiles with dissolve
            play voice2 mc_arrogant_hm3 noloop
            mc "I'll relax once we're done with work."
            scene sm1mv01s06-75 clashing_swords_sy_talk_menu_glad with dissolve
            play voice3 stacy_yes_yap1 noloop
            sy "Good. Alright, I'm going to go get suited up."
        "It is a lot to handle, but we're doing good":
            $ player.set_choice("sm1mv01s06_doing_good")
            scene sm1mv01s06-76 clashing_swords_mc_talk_menu_doing_good with dissolve
            play voice2 mc_arrogant_heh2 noloop
            mc "Heh. You know, when we were just writing things out."
            mc "It all felt a lot simpler."
            scene sm1mv01s06-78 clashing_swords_sy_talk_menu_doing_good_kisscheek with dissolve
            play voice3 stacy_suckmoan1 noloop
            play sound mc_kiss1
            pause
            scene sm1mv01s06-77 clashing_swords_sy_talk_menu_doing_good_smile with dissolve
            play voice3 stacy_disappointed_ehh2 noloop
            sy "It's a lot to take on, [mcname]."
            scene sm1mv01s06-79 clashing_swords_sy_talk_menu_doing_good with dissolve
            play voice3 stacy_happy_relief1 noloop
            sy "I'm glad you're directing this part, but I think it's really going to turn into something special."
            scene sm1mv01s06-80 clashing_swords_mc_talk_menu_doing_good with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "Yeah. Everyone is doing a good job."
            mc "I'm excited to film it in costume."
            scene sm1mv01s06-81 clashing_swords_sy_talk_menu_doing_good_kisscheek with dissolve
            play voice3 stacy_suckmoan3 noloop
            play sound mc_kiss3
            pause
            scene sm1mv01s06-82 clashing_swords_sy_talk_menu_doing_good_chinup with dissolve
            play voice3 stacy_arrogant_huh2 noloop
            sy "Keep your chin up, [mcname]."
    jump sm1mv01s06_dressed_up
label sm1mv01s06_dressed_up:
    play sound sfx_heels_steps1 loop
    scene sm1mv01s06-83 clashing_swords_kv_talk_walkin_pirate with fade
    pause
    scene sm1mv01s06-84 clashing_swords_kv_talk_set_mc_walksin with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1mv01s06-85 clashing_swords_kv_talk with dissolve
    play voice5 kanya_thinking_eeh1 noloop
    kv "You're going to need a bigger boat."
    scene sm1mv01s06-86 clashing_swords_mc_talk_hmm with dissolve
    play voice2 d1s2_hmm noloop volume 1.4
    mc "Hmm?"
    scene sm1mv01s06-87 clashing_swords_kv_talk with dissolve
    play voice5 kanya_disappointed_neh noloop
    kv "Don't get me wrong. It's a solid set, but it's really small."
    play sound sfx_heels_steps1
    play sound2 sfx_heels_steps2
    scene sm1mv01s06-88 clashing_swords_kv_talk_sy_tl_walkin with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1mv01s06-89 clashing_swords_kv_talk with dissolve
    play voice5 kanya_thinking_hmm3 noloop
    kv "The fight is going to be very intimate."
    scene sm1mv01s06-90 clashing_swords_mc_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "We know, we already figured out a plan for that."
    scene sm1mv01s06-91 clashing_swords_mc_talk_gesture_stacy with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Stacy found out a really cool workaround."
    play sound sfx_gadgets_laptop_opened
    play sound2 sfx_keyboard_typing2
    scene sm1mv01s06-92 clashing_swords_sy_talk_laptop with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "[mcname] is burying the lead, it took a lot of elbow grease to figure it out."
    stop sound2 fadeout 1.0
    scene sm1mv01s06-93 clashing_swords_sy_talk_laptop_kvlook with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "Kanya, check it out."
    scene sm1mv01s06-94 clashing_swords_sy_talk_point with dissolve
    play voice3 stacy_hey noloop
    sy "[mcname] and Taisia, go on stage."
    play sound sfx_throw_something1
    scene sm1mv01s06-95 clashing_swords_tl_talk with dissolve
    play voice4 girl24_yes_simple1 noloop
    tl "Yes, El Capitan."
    scene sm1mv01s06-96 clashing_swords_sy_talk_mc_tl_stage with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "So we'll film the scenes on our set, and then we'll go through and overlay some movie magic."
    play sound sfx_keyboard_enter1
    play sound2 sfx_reminiscence_gone noloop volume 2.0
    scene sm1mv01s06-97 clashing_swords_sy_talk_bigship with image_dissolve_1
    play sound4 sfx_seawaves_ambience1 volume 2.0
    play voice3 stacy_yes_fine4 noloop
    sy "And obviously, we're going to need some water."
    sy "They're sea pirates, not land pirates."
    scene sm1mv01s06-98 clashing_swords_kv_talk_water with dissolve
    play voice5 kanya_surprised_wow noloop
    kv "Ah... Impressive."
    scene sm1mv01s06-99 clashing_swords_sy_talk_smile with dissolve
    play voice3 stacy_thinking_hmm2 noloop
    sy "I even found assets to add a second ship, ergo, {i}my{/i} ship."
    sy "It will be in the background, firing on our main ship."
    scene sm1mv01s06-100 clashing_swords_kv_talk_smiles with dissolve
    play voice5 kanya_disappointed_hm noloop
    kv "Most impressive."
    play sound sfx_memory_cloud_change1
    stop sound4 fadeout 1.0
    scene sm1mv01s06-101 clashing_swords_mc_talk_backsmallship with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Alright, everyone satisfied?"
    scene sm1mv01s06-102 clashing_swords_tl_talk_joking with dissolve
    play voice4 girl24_no_nah noloop
    tl "I'm never satisfied, but I am ready to cook this goose."
    play sound sfx_heels_steps1
    scene sm1mv01s06-103 clashing_swords_kv_talk_set with dissolve
    play voice5 kanya_yes_simple noloop
    kv "Yes. I am ready. What point are we starting from?"
    stop sound fadeout 1.0
    scene sm1mv01s06-104 clashing_swords_sy_talk with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "Let's take it from Point 3A."
    scene sm1mv01s06-105 clashing_swords_mc_talk_tl_holdsidesword with dissolve
    pause
    scene sm1mv01s06-106 clashing_swords_sy_talk_nod with dissolve
    sy "..."
    scene sm1mv01s06-107 clashing_swords_mc_talk_smile with dissolve
    pause
    stop music fadeout 3.0
    scene sm1mv01s06-108 clashing_swords_mc_talk_signal with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "And... action!"
    jump sm1mv01s06_movie_start
label sm1mv01_movie_replay_2:
    scene black
    show screen scene_transistion(_("On the high seas"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    jump sm1mv01s06_movie_start
label sm1mv01s06_movie_start:
    play sound4 sfx_seawaves_ambience1 volume 2.0 fadein 0.5
    queue music music_black_sails fadein 0.5 volume 0.8
    if in_a_replay:
        scene sm1mv01s06-109 clashing_swords_mc_talk_transition
        with Fade(0.5, 0.5, 0.5)
    else:
        scene sm1mv01s06-109 clashing_swords_mc_talk_transition with dissolve
    pause
    scene sm1mv01s06-a110 canon-shot-glambot-000 with dissolve
    pause 0.01
    play sound sfx_sm1mv01s06_glambot1
    scene sm1mv01s06-a110-glambot
    pause
    play voice2 mc_pain_ou3 noloop
    play sound sfx_boat_accident1
    play sound2 sfx_fall_down1 noloop
    scene sm1mv01s06-112 clashing_swords_mc_talk_transition_cannonball_shake with vpunch
    pause
    play sound sfx_sword_whoosh4
    scene sm1mv01s06-113 clashing_swords_sy_talk_prowling with dissolve
    play voice3 stacy_angry_argh2 noloop
    sy "It be time you returned to the sea, Searose!"
    scene sm1mv01s06-114 clashing_swords_sy_talk_ready_explosion with dissolve
    pause
    scene sm1mv01s06-115 clashing_swords_sy_talk_ready_upshot with dissolve
    play voice4 girl24_angry_err2 noloop
    tl "Your powers are weak, my Queen."
    scene sm1mv01s06-116 clashing_swords_sy_talk_slash with dissolve
    play voice3 stacy_angry noloop
    sy "If wishing it would only make it so."
    play sound sfx_sword_whoosh2
    scene sm1mv01s06-117 clashing_swords_sy_talk_sword down with dissolve
    play voice3 stacy_angry_aah1 noloop
    sy "Arrrrgh!"
    play voice4 girl24_scared_ah2 noloop
    tl "No!"
    play voice2 mc_angry_errr2 noloop
    play sound sfx_sword_hit_metal2
    scene sm1mv01s06-118 clashing_swords_mc_talk_block with hpunch
    "Clang!"
    scene sm1mv01s06-119 clashing_swords_sy_talk_backoff with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "Hah!"
    sy "Didn't I kill you already?"
    play sound sfx_sword_hit_metal1
    scene sm1mv01s06-121 clashing_swords_sy_talk_fightmontage with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I got better."
    play sound sfx_sword_whoosh1
    scene sm1mv01s06-120 clashing_swords_sy_talk_fightmontage with dissolve
    pause
    play sound sfx_sword_whoosh2
    scene sm1mv01s06-122 clashing_swords_sy_talk_fightmontage with dissolve
    pause
    play sound sfx_sword_hit_metal3
    scene sm1mv01s06-123 clashing_swords_sy_talk_lockswords with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Nrrn."
    scene sm1mv01s06-124 clashing_swords_mc_talk_lockswords with dissolve
    play voice2 mc_angry_errr1 noloop
    mc "Mmnn."
    scene sm1mv01s06-125 clashing_swords_sy_talk_snarls with dissolve
    play voice3 stacy_disappointed_ehh3 noloop
    sy "Dickhart..."
    scene sm1mv01s06-126 clashing_swords_mc_talk_smile with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Tempestra."
    play sound sfx_sword_whoosh4
    scene sm1mv01s06-127 clashing_swords_sy_talk_dodge with dissolve
    play voice3 stacy_angry_argh5 noloop
    sy "Why are you are interfering with my work?"
    play sound sfx_epic_jump1
    play sound2 sfx_socks_dancing2
    scene sm1mv01s06-128 clashing_swords_sy_talk_chasing with dissolve
    play voice3 stacy_angry_aah2 noloop
    sy "I thought we agreed that if I saw you again, I'd turn you into chum for the sharks!."
    play sound sfx_sword_hit_metal1
    stop sound2 fadeout 0.5
    scene sm1mv01s06-129 clashing_swords_mc_talk_block with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Listening was never my strongest skill."
    play sound sfx_sword_hit_metal2
    scene sm1mv01s06-130 clashing_swords_sy_talk_block with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "Then you won't be missing your ears!"
    scene sm1mv01s06-131 clashing_swords_mc_talk_cackling with dissolve
    play voice2 mc_happy_laugh4 noloop
    mc "*pirate cackling*"
    play sound2 sfx_socks_dancing2
    play sound3 sfx_socks_dancing1
    scene sm1mv01s06-132 clashing_swords_mc_talk_montage with dissolve
    pause
    play sound sfx_sword_hit_metal1
    scene sm1mv01s06-133 clashing_swords_mc_talk_montage with dissolve
    play voice3 stacy_pain_mmm1 noloop
    sy "*grunting*"
    play sound sfx_sword_whoosh3
    scene sm1mv01s06-134 clashing_swords_mc_talk_montage with dissolve
    pause
    play sound sfx_sword_whoosh2
    scene sm1mv01s06-135 clashing_swords_mc_talk_recovering with dissolve
    play voice2 mc_angry_errr8 noloop
    mc "You're outmatched, Tempestra."
    scene sm1mv01s06-136 clashing_swords_tl_talk_cannon with dissolve
    play voice3 stacy_arrogant_huh5 noloop
    sy "Hah! Maybe outnumbered."
    sy "Tempestra is never {b}outmatched!{/b}"
    scene sm1mv01s06-137 clashing_swords_tl_talk_smile with dissolve
    play voice4 girl24_thinking_hmm5 noloop
    tl "Idea..."
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1mv01s06-138 clashing_swords_sy_talk_fight with dissolve
    play voice3 stacy_surprised_huh3 noloop
    sy "You're using Bonetti's defense against me, ah?"
    scene sm1mv01s06-139 clashing_swords_mc_talk_fight with dissolve
    play voice2 d9s2_yeah noloop volume 2.2
    mc "I thought it fitting, considering the ship is rocking and exploding all around us."
    play sound sfx_shotgun_shot1
    scene sm1mv01s06-140 clashing_swords_mc_talk_ship_hit with dissolve
    pause
    play voice3 stacy_angry_argh3 noloop
    play sound3 sfx_boat_accident1 noloop
    scene sm1mv01s06-141 clashing_swords_sy_talk_attack with vpunch
    sy "Naturally, you must expect me to attack with Capo Ferro."
    play sound sfx_sword_whoosh4
    scene sm1mv01s06-142 clashing_swords_nc_talk_fendingoff with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Naturally... {w} But I find Thibault cancels out Capo Ferro, don't you?"
    scene sm1mv01s06-143 clashing_swords_sy_talk_thinkfast with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "Unless the enemy has studied his Agrippa-"
    play sound sfx_sword_whoosh4 volume 1.8
    scene sm1mv01s06-144 clashing_swords_sy_talk_duck with dissolve
    play voice3 stacy_pain_mmm2 noloop
    pause
    play sound2 sfx_rope_spin1 noloop volume 1.6
    play sound sfx_sword_whoosh4
    scene sm1mv01s06-145 clashing_swords_sy_talk_rope with dissolve
    "Snip!"
    play sound sfx_other_rooftop_down1
    scene sm1mv01s06-146 clashing_swords_mc_talk_slashes_syair with dissolve
    play voice2 mc_surprised_huh8 noloop
    "Woosh!"
    scene sm1mv01s06-148 clashing_swords_mc_talk_stilllooking with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Buh?"
    play sound sfx_epic_jump1 volume 1.6
    scene sm1mv01s06-149 clashing_swords_sy_talk_behind with dissolve
    play voice3 stacy_angry_aah3 noloop
    sy "Which I have."
    play sound sfx_throw_something1 volume 1.6
    play sound2 sfx_sword_whoosh3 noloop
    scene sm1mv01s06-150 clashing_swords_mc_talk_rigging with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "You haven't changed a bit."
    mc "What do you say we open a Spanish Red and talk this over, Tempestra."
    scene sm1mv01s06-151 clashing_swords_sy_talk_smiling with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "We were always better at fighting and fucking than talking, Dickhart."
    play sound sfx_sword_hit_metal1
    scene sm1mv01s06-152 clashing_swords_mc_talk_worried with dissolve
    pause
    scene sm1mv01s06-a153 swordfight-glambot-000 with dissolve
    pause 0.01
    play sound sfx_sm1mv01s06_glambot2
    scene sm1mv01s06-a153-glambot
    play voice3 stacy_angry_argh4 noloop
    sy "I should have killed you at Nassau."
    play sound2 sfx_rope_stretch noloop volume 2.0
    scene sm1mv01s06-154 clashing_swords_mc_talk_mcjumpmiss with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "Ha-huh!"
    play sound sfx_sand_jump1 volume 2.0
    scene sm1mv01s06-155 clashing_swords_mc_talk_outside with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Aye, you should have."
    play sound sfx_sword_hit_metal3
    scene sm1mv01s06-156 clashing_swords_mc_talk_fighting with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "But you would have robbed yourself of the greatest sex of your life."
    play sound sfx_sword_hit_wood3
    scene sm1mv01s06-157 clashing_swords_sy_talk_fighting_smiling with dissolve
    play voice3 stacy_uhuh noloop
    sy "You bloat your skills, you selfish knave!"
    play sound sfx_epic_jump1
    play sound2 sfx_throw_something1 noloop
    scene sm1mv01s06-158 clashing_swords_mc_talk_somersault with dissolve
    pause
    play sound2 sfx_leg_kick7 noloop
    play sound sfx_sword_hit_metal1
    scene sm1mv01s06-159 clashing_swords_sy_talk_onhim with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "You're not the only one who can spin a deception."
    play sound sfx_sword_hit_metal2
    scene sm1mv01s06-160 clashing_swords_mc_talk_worried with dissolve
    play voice2 d2s12_emmm noloop volume 1.6
    mc "Tempestra...{w} You can't mean..."
    scene sm1mv01s06-161 clashing_swords_sy_talk_cackling with dissolve
    play voice3 stacy_yes noloop
    sy "That's right."
    sy "That night in the governor's mansion."
    sy "I WAS FAKING IT!"
    scene sm1mv01s06-162 clashing_swords_mc_talk_distraught with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "Foul harpy!{w} You lie!"
    play sound sfx_sword_hit_metal3
    scene sm1mv01s06-163 clashing_swords_sy_talk with dissolve
    play voice3 stacy_arrogant_hmm2 noloop
    sy "Watch these lips and look for a lie."
    play sound sfx_sword_whoosh4
    play sound2 sfx_epic_jump1 noloop
    scene sm1mv01s06-164 clashing_swords_mc_talk_disarmed with dissolve
    play voice2 mc_scared_huuuh3 noloop
    "Clang!"
    play sound sfx_sword_hit_wood3
    play sound2 sfx_comic_attention3 noloop volume 4.0
    scene sm1mv01s06-165 clashing_swords_mc_talk_sword ground with dissolve
    pause
    scene sm1mv01s06-166 clashing_swords_mc_talk_theend with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "*grunting*"
    play sound sfx_throw_something1
    scene sm1mv01s06-167 clashing_swords_mc_talk_handsup with dissolve
    play voice2 d1s5b_emmm noloop volume 2.0
    mc "Parlay?"
    scene sm1mv01s06-168 clashing_swords_sy_talk with dissolve
    play voice3 stacy_no_nonono3 noloop
    sy "Not this time, Dickhart."
    play sound sfx_torch_lightup1
    scene sm1mv01s06-169 clashing_swords_tl_talk with dissolve
    play voice4 girl24_hey_angry noloop
    tl "Sorry to butt in, but I still need him, my queen."
    scene sm1mv01s06-170 clashing_swords_sy_talk_turn with dissolve
    play voice3 stacy_angry_argh1 noloop
    sy "How dare you-"
    scene sm1mv01s06-171 clashing_swords_tl_talk_ready with dissolve
    play voice4 girl24_happy_laugh1 noloop
    tl "Heh."
    scene sm1mv01s06-172 clashing_swords_sy_talk_disbelief with dissolve
    play voice3 stacy_disappointed_ehh4 noloop
    sy "You're mad. You'll kill us all."
    scene sm1mv01s06-173 clashing_swords_tl_talk_smile with dissolve
    play voice4 girl24_arrogant_yeah2 noloop
    tl "Only if I miss."
    scene sm1mv01s06-174 clashing_swords_mc_talk_map with dissolve
    pause
    scene sm1mv01s06-175 clashing_swords_mc_talk_map with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "The map."
    play sound sfx_throw_something1
    scene sm1mv01s06-176 clashing_swords_mc_talk_dash with dissolve
    pause
    play sound sfx_throw_something1 volume 2.5
    play sound2 sfx_paper_rustl3 noloop
    play sound3 sfx_leg_kick8 noloop
    scene sm1mv01s06-176-2 clashing_swords_mc_talk_dash with dissolve
    mct "Got it!"
    play sound sfx_heels_run2
    scene sm1mv01s06-177 clashing_swords_sy_talk_glaring with dissolve
    play voice3 stacy_angry_fuck2 noloop
    sy "Blackguard!"
    play sound sfx_wick_lightup1
    scene sm1mv01s06-178 clashing_swords_tl_talk_light with dissolve
    pause
    play sound sfx_shotgun_shot2
    play sound2 sfx_thunder_1 noloop
    scene sm1mv01s06-179 clashing_swords_tl_talk_boom with hpunch
    "BOOM!"
    scene sm1mv01s06-180 clashing_swords_sy_talk_face with dissolve
    play voice3 stacy_surprised_ah1 noloop
    pause
    play sound sfx_throw_something1
    play sound2 sfx_epic_jump1 noloop
    scene sm1mv01s06-181 clashing_swords_sy_talk_jump with dissolve
    pause
    play sound sfx_water_splash2 volume 5.0
    scene sm1mv01s06-182 clashing_swords_sy_talk_explosion with dissolve
    pause
    scene sm1mv01s06-183 clashing_swords_mc_talk_side with dissolve
    pause
    scene sm1mv01s06-184 clashing_swords_tl_talk with dissolve
    play voice4 girl24_surprised_huh4 noloop
    tl "Think she's dead?"
    scene sm1mv01s06-185 clashing_swords_mc_talk_shakehead with dissolve
    play voice2 mc_no_nah1 noloop
    mc "Nay. The sea has spat her back before."
    mc "But at least she's gone for now."
    scene sm1mv01s06-186 clashing_swords_tom_talk_offscreen with dissolve
    play voice5 boy5_hey_angry noloop
    "Toms" "Captain! the {i}Siren{/i} is breaking off."
    scene sm1mv01s06-187 clashing_swords_mc_talk_gladtohear with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Aye, Mister Toms, and so are we."
    mc "Find us some wind to fill these sails."
    play voice5 boy5_happy_yeah1 noloop
    "Toms" "Aye Captain!"
    scene sm1mv01s06-188 clashing_swords_mc_talk_lookingout with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Well, find that treasure in no time, and the Pirate Queen will find us vanished before she ever catches up."
    scene sm1mv01s06-189 clashing_swords_tl_talk with dissolve
    play voice4 girl24_thinking_emm2 noloop
    tl "Aren't you forgetting something, Captain."
    scene sm1mv01s06-190 clashing_swords_mc_talk_leanturn with dissolve
    play voice2 mc_no_no9 noloop
    mc "I don't think so."
    scene sm1mv01s06-191 clashing_swords_tl_talk_pointmap with dissolve
    play voice4 girl24_arrogant_hm1 noloop
    tl "My map."
    scene sm1mv01s06-192 clashing_swords_mc_talk_smile with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "I'll be holding onto it. Safe keeping."
    mc "You already lost it once."
    scene sm1mv01s06-193 clashing_swords_tl_talk_angry with dissolve
    play voice4 girl24_arrogant_hm3 noloop
    tl "I just saved your skin."
    scene sm1mv01s06-194 clashing_swords_mc_talk_arrogant with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Aye, you did, and I salute you for it."
    mc "But as I am still Captain of the {i}Black Diamond{/i} I'll be holding onto the map."
    mc "You'll still get your share, no worries there."
    play sound sfx_throw_something1
    scene sm1mv01s06-195 clashing_swords_tl_talk_mad with dissolve
    play voice4 girl24_angry_argh5 noloop
    tl "I should have let her gut you."
    scene sm1mv01s06-196 clashing_swords_mc_talk with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Come now, you'd be missing my devlishly good looks now, wouldn't you?"
    scene sm1mv01s06-197 clashing_swords_tl_talk_seduce with dissolve
    play voice4 girl24_thinking_emm1 noloop
    tl "Perhaps."
    tl "Give me back my map and I'll have time to consider it."
    scene sm1mv01s06-198 clashing_swords_mc_talk with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Nice try, Miss Searose."
    scene sm1mv01s06-199 clashing_swords_mc_talk_turn with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Now if you'll excuse me, we've got a treasure to find."
    scene sm1mv01s06-200 clashing_swords_mc_talk_shout with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "All hands. Slacken your braces."
    play sound sfx_heels_steps1
    scene sm1mv01s06-201 clashing_swords_mc_talk_tl_stormsoff with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Put some distance between us and those craven dogs."
    stop sound4 fadeout 2.0
    stop music fadeout 3.0
    if in_a_replay:
        stop sound fadeout 2.0
        stop music fadeout 2.0
        jump sm1mv01_movie_replay_3
    jump sm1mv01s06_done_recording
label sm1mv01s06_done_recording:
    queue music music_hammership_process
    play sound sfx_reminiscence_gone
    scene sm1mv01s06-202 clashing_swords_kv_talk_transition_evening with image_dissolve_1
    play sound2 sfx_videocamera_finish noloop
    play voice5 kanya_yes_yep1 noloop
    kv "And... cut."
    scene sm1mv01s06-203 clashing_swords_mc_talk_relax with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Phew."
    scene sm1mv01s06-204 clashing_swords_tl_talk with dissolve
    play voice4 girl24_happy_relief noloop
    tl "*sighing happily*"
    scene sm1mv01s06-205 clashing_swords_mc_talk_kv with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Sure we don't need to go over the last part again."
    scene sm1mv01s06-206 clashing_swords_sy_talk_climb with dissolve
    play voice3 stacy_no_angry1 noloop
    sy "No!"
    scene sm1mv01s06-207 clashing_swords_mc_talk_jeez with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Alright, alright."
    mc "But we really want to get it perfect."
    play sound sfx_leg_kick7
    scene sm1mv01s06-208 clashing_swords_sy_talk_deck with dissolve
    play voice3 stacy_pain_mmm1 noloop
    pause
    scene sm1mv01s06-209 clashing_swords_sy_talk_reassuring with dissolve
    play voice3 stacy_disappointed_oh3 noloop
    sy "[mcname]. I love you."
    sy "But we did it six times!"
    sy "My back hurts and my tits have been stuffed in this corset for hours."
    scene sm1mv01s06-210 clashing_swords_tl_talk with dissolve
    play voice4 girl24_happy_yeah3 noloop
    tl "I could really use a drink too."
    scene sm1mv01s06-211 clashing_swords_kv_talk with dissolve
    play voice5 kanya_yes_yeah2 noloop
    kv "I'm actually in Taisia's boat. It looks great, [mcname]."
    kv "We have plenty of footage to comb through in post."
    kv "But I guarantee you, you'll be using the third take. It was the best."
    scene sm1mv01s06-212 clashing_swords_mc_talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "The best is not {i}perfect{/i}."
    scene sm1mv01s06-213 clashing_swords_kv_talk_sigh with dissolve
    play voice5 kanya_surprised_eeh2 noloop
    kv "Did I say best? I meant it's perfect."
    scene sm1mv01s06-214 clashing_swords_sy_talk_lookmc with dissolve
    sy "..."
    scene sm1mv01s06-215 clashing_swords_mc_talk_relaxes with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "Alright, if you guys think we got it."
    scene sm1mv01s06-216 clashing_swords_tl_talk with dissolve
    play voice4 girl24_yes_happy noloop
    tl "We did, [mcname]."
    scene sm1mv01s06-217 clashing_swords_kv_talk with dissolve
    play voice5 kanya_thinking_eeh5 noloop
    kv "I admire your ferver, but let's not forget what we're making."
    scene sm1mv01s06-218 clashing_swords_mc_talk_peeved with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Just because it's porn doesn't mean we should half-ass it."
    scene sm1mv01s06-219 clashing_swords_kv_talk_relax with dissolve
    play voice5 kanya_no_angry noloop
    kv "I didn't say that."
    scene sm1mv01s06-220 clashing_swords_sy_talk_calm with dissolve
    play voice3 stacy_hey_happy1 noloop
    if persistent.is_special:
        sy "Relax, bro."
    else:
        sy "Take it easy, [mcname]."
    scene sm1mv01s06-221 clashing_swords_sy_talk_gesturekv with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "Kanya knows what she is doing."
    scene sm1mv01s06-222 clashing_swords_kv_talk_apologize with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "You're right. You're right."
    mc "Sorry, Kanya."
    scene sm1mv01s06-223 clashing_swords_mc_talk_group with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    if player.get_choice("first_movie") == "pirates_movie":
        mc "I just really want to make the film rock."
        mc "We're putting a lot into this."
        scene sm1mv01s06-224 clashing_swords_sy_talk_group with dissolve
        play voice3 stacy_yes_yap2 noloop
        sy "I know. It's alright."
    else:
        mc "We just don't want to slip up just because this is our second film."
        mc "I want to show people that the studio can be depended on for good stuff."
        scene sm1mv01s06-224 clashing_swords_sy_talk_group with dissolve
        play voice3 stacy_yes_yap2 noloop
        sy "They will."
    scene sm1mv01s06-225 clashing_swords_mc_talk_relax with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Phew..."
    play sound sfx_cloth_rustling1
    scene sm1mv01s06-226 clashing_swords_mc_talk_phone with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh shit."
    scene sm1mv01s06-227 clashing_swords_mc_talk_embarrased with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Heh. It really is late."
    scene sm1mv01s06-228 clashing_swords_mc_talk_kv_tl_beer with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Thank you both for all your hard work today."
    mc "This was definitely the big kahuna."
    play sound sfx_beer_open1
    scene sm1mv01s06-229 clashing_swords_kv_talk_smiles with dissolve
    play voice5 kanya_no_nah2 noloop
    kv "Don't mention it."
    scene sm1mv01s06-230 clashing_swords_tl_talk_grinning with dissolve
    play voice4 girl24_thinking_huh1 noloop
    tl "Does that mean we get paid double?"
    scene sm1mv01s06-231 clashing_swords_kv_talk_tl with dissolve
    play voice5 kanya_arrogant_huh noloop
    kv "Taisia."
    scene sm1mv01s06-232 clashing_swords_tl_talk_innocent with dissolve
    play voice4 girl24_surprised_what2 noloop
    tl "What? I was just curious."
    scene sm1mv01s06-233 clashing_swords_tl_talk_walksaway with dissolve
    play voice4 girl24_hey_bye2 noloop
    tl "See you guys later. I need to get out of this hot costume."
    scene sm1mv01s06-234 clashing_swords_sy_talk with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Make sure to hang it up."
    scene sm1mv01s06-235 clashing_swords_tl_talk with dissolve
    play voice4 girl24_yes_aga noloop
    tl "I'll think about it."
    play sound sfx_heels_steps1 loop
    scene sm1mv01s06-236 clashing_swords_kv_talk_waves_tlwalksaaway with dissolve
    play voice5 kanya_yes_yeah3 noloop
    kv "I started importing everything from the camera to the laptop."
    kv "I can't wait to see how it turns out."
    scene sm1mv01s06-237 clashing_swords_mc_talk_agrees with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "Same."
    play sound2 sfx_heels_steps2
    scene sm1mv01s06-238 clashing_swords_mc_talk_waving with dissolve
    play voice2 mc_hey_bye1 noloop
    mc "Until next time, Kanya."
    play voice5 kanya_yes_aga1 noloop
    kv "Later."
    stop sound2 fadeout 1.0
    play sound sfx_door_closed1
    scene sm1mv01s06-239 clashing_swords_mc_talk_stretching with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Woooh. That was a long day."
    scene sm1mv01s06-240 clashing_swords_sy_talk_stretch with dissolve
    play voice3 stacy_disappointed_moan1 noloop
    sy "I don't know how normal porn stars do it."
    scene sm1mv01s06-241 clashing_swords_mc_talk_smile with dissolve
    pause
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1mv01s06-242 clashing_swords_mc_talk_kisscheek with dissolve
    play voice2 d1s5_orgasm noloop
    play sound mc_kiss1
    mc "Mmm."
    scene sm1mv01s06-243 clashing_swords_sy_talk_smile with dissolve
    play voice3 stacy_mmm2 noloop
    sy "What was that for?"
    scene sm1mv01s06-244 clashing_swords_mc_talk_happy with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "I was getting bent out of shape and you helped me out."
    scene sm1mv01s06-245 clashing_swords_mc_talk_nice_menu with dissolve
    play voice2 mc_thinking_hmm2 noloop
    if persistent.is_special:
        mc "I owe you one, sis."
        play sound sfx_cloth_rustling3
        scene sm1mv01s06-247 clashing_swords_sy_talk_hugs with dissolve
        play voice3 stacy_no_nonono2 noloop
        sy "You don't owe me anything, bro."
    else:
        mc "I owe you one, Stacy."
        play sound sfx_cloth_rustling3
        scene sm1mv01s06-247 clashing_swords_sy_talk_hugs with dissolve
        play voice3 stacy_no_nonono2 noloop
        sy "You don't owe me anything, [mcname]."
    sy "But now that I think of it, I {i}could{/i} use a new swimsuit."
    scene sm1mv01s06-248 clashing_swords_mc_talk_hugs with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Consider it done."
    scene sm1mv01s06-249 clashing_swords_sy_talk_hugs_enjoy with dissolve
    play voice3 stacy_suckmoan2 noloop
    if player.get_choice("first_movie") == "pirates_movie":
        sy "I'm sure there will be more days like this. We know that."
        sy "But we also know that we're in this together."
    else:
        sy "In some ways this feels harder than the first film."
        sy "But I know that we'll make it through."
        sy "Because we're in this together."
    play sound sfx_cloth_rustling1
    scene sm1mv01s06-250 clashing_swords_mc_talk_shoulder with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "And if we're together, nothing is off the table."
    scene sm1mv01s06-251 clashing_swords_mc_talk_smiling with dissolve
    play voice2 mc_yes_yes5 noloop
    mc "That's right."
    play sound sfx_cloth_rustling2
    scene sm1mv01s06-252 clashing_swords_mc_talk_touch_costume with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I'm going to go take off my costume and probably get some rest."
    scene sm1mv01s06-253 clashing_swords_sy_talk_sexy_look with dissolve
    play voice3 stacy_laugh4 noloop
    sy "Haha. Okay."
    sy "Maybe tonight we should cuddle up."
    scene sm1mv01s06-254 clashing_swords_mc_talk with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "I'd like that."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(MOVIE_PIRATES, 4, 0, 5)
    return