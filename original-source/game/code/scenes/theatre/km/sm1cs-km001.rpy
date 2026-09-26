image sm1cs-km001-glambot-1 = Movie(play = "images/FS_T/KM/s001/anim/sm1cs-km001-a64-2x-50fps.webm", start_image = "sm1cs-km001-a64 mc-back-his-ass-000", image = "sm1cs-km001-a64 mc-back-his-ass-171", loop = False)
label sm1cs_km001:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound sfx_heels_steps2 loop
    scene sm1cs-km001-01 km-going-for-stage-mc-following_c1 with fade
    play music music_shopping_causal
    pause
    scene sm1cs-km001-02 mc-sees-sb-looking-through-stuff_c1 with dissolve
    play sound sfx_toilet_paper_rip1 volume 0.6
    play voice2 d1s5_mcthinks noloop volume 1.4
    mct "Sam should know where the prop weapons are."
    stop sound fadeout 1.5
    scene sm1cs-km001-03 mc-hey-sam-sb-call-bruce_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey Sam."
    play voice4 boy5_arrogant_hm1 noloop
    sb "Call me Bruce, kid. Everyone does around here."
    scene sm1cs-km001-04 mc-sure-need-help-sb-what-can-do-for-you_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure. I need a little help."
    play voice4 boy5_disappointed_mmf1 noloop
    sb "What can I do you for?"
    scene sm1cs-km001-05 mc-tells-km-asked-roman-swords-shields_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "Kellie asked me to get two sets of prop swords and shields. She specified 'Roman' ones?"
    play voice4 boy5_happy_laugh1 noloop
    sb "Haha. Sounds like little Kellie is up to some good old-fashioned hazing."
    scene sm1cs-km001-06 mc-huh-sb-find-out_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh?"
    play voice4 boy5_disappointed_mmm1 noloop
    sb "Eh you'll find out."
    scene sm1cs-km001-07 sb-point-off-screen-where-mc-find-stuff_c1 with dissolve
    play voice4 boy5_thinking_hmm7 noloop
    sb "Right over there. Just make sure to bring em back when you're done."
    play sound sfx_heels_steps2 loop
    scene sm1cs-km001-08 mc-walks-away-thanks-sb-good-luck_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Thanks Bruce."
    play voice4 boy5_arrogant_heh1 noloop
    sb "Good luck."
    play sound sfx_armored_footsteps1 loop fadein 2.0
    scene sm1cs-km001-09 mc-appears-stage-carrying-shields-swords-km-on-phone_c1 with fade
    pause
    scene sm1cs-km001-10 mc-little-heavier-km-here-learn-complain_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "*grunts* Man, these are a little heavier than I imagined."
    play voice3 girl31_arrogant_geh noloop
    km "Are you here to learn or complain?"
    play sound sfx_armor_fall1
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_sword_equiped1 noloop
    scene sm1cs-km001-11 mc-grabs-sword-grunts_c1 with dissolve
    play voice2 mc_angry_errr5 noloop
    mc "Phew."
    scene sm1cs-km001-12 mct-they-heavy-look-cool_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "They may be heavy, but they sure look cool."
    play sound sfx_sword_whoosh1
    scene sm1cs-km001-13 mc-makes-pose-avast-thinks-wrong_c1 with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "Avast yee!"
    mct "Oh wait, that's a pirate."
    scene sm1cs-km001-14 km-hmmm-mct-what-snooping_c1 with dissolve
    play voice3 girl31_thinking_hmm3 noloop
    km "Hmmm."
    play voice2 d1s1_mmm noloop volume 1.7
    mct "Why is she shopping?"
    scene sm1cs-km001-15 mc-that-your-costume-km-none-your-business_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Is that for your costume?"
    play voice3 girl31_angry_ergh8 noloop
    km "None of your business, new guy."
    scene sm1cs-km001-16 mc-appologize-km_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Sorry."
    play sound sfx_heels_steps2 loop
    scene sm1cs-km001-17 km-head-for-shields-sword-still-angry_c1 with dissolve
    play voice3 girl31_disappointed_mff1 noloop
    km "You've really got some nerve. I don't get what Taisia sees in you."
    play sound sfx_armor_equiped1
    scene sm1cs-km001-18 km-picks-up-sword-shield_c1 with dissolve
    pause
    scene sm1cs-km001-19 mc-talks-based-job_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    if True:
        mc "Listen, I'm just trying to find steady work, and getting to be on stage sounds a hell of a lot better than bagging groceries or working the night shift at a gas station."
    else:
        mc "Well she obviously sees something in me. And Denise seems to agree with her, or I wouldn't have gotten a stage role."
        scene sm1cs-km001-20 km-ppl-make-mistakes-mc-start-over-please_c1 with dissolve
        play voice3 girl31_yes_simple1 noloop
        km "People make mistakes."
    play voice2 mc_disappointed_ehh4 noloop
    mc "Can we please start over?"
    play sound sfx_cloth_rustling2
    scene sm1cs-km001-21 km-hmm-can-try-points-shiled-pick-up-shield_c1 with dissolve
    play voice3 girl31_thinking_hmm1 noloop
    km "Hmm. You can try."
    km "Pick up your shield."
    play sound sfx_armor_equiped1
    scene sm1cs-km001-22 km-takes-practice-swing-mc-hold-shield-hm_c1 with dissolve
    pause
    scene sm1cs-km001-23 km-need-practice-help-her-mc-dont-know-swordfight-good-idea_c1 with dissolve
    play voice3 girl31_thinking_emm3 noloop
    km "Okay, I need to practice for the next fight scene. You're gonna help me."
    play voice2 mc_yes_okay2 noloop
    mc "Okay. I don't really know how to fight with a sword and shield like this. Are you sure this is a good idea?"
    scene sm1cs-km001-24 km-stone-cold-face-answers-no_c1 with hpunch
    play voice3 girl31_no_simple noloop
    km "No."
    scene sm1cs-km001-25 km-evil-smile-great-idea_c1 with dissolve
    play voice3 girl31_happy_laugh3 noloop
    km "It's a great idea. Especially if you want to show me that you truly belong with the rest of us on this stage."
    scene sm1cs-km001-26 km-mc-standoff-km-talks-mc-unless-afraid-lose-girl_c1 with dissolve
    queue voice3 girl31_thinking_mmf2 noloop
    if True:
        km "You're trying to join a theater troupe, not a high-school drama class."
    else:
        km "You might have passed Denises' bar. But not mine."
    km "Unless you're afraid to lose to a girl"
    scene sm1cs-km001-27 mc-choice-menu-screen_c1 with dissolve
    menu:
        "I'll go easy on you."(hint="sm1cs_km001_m01_h01"):
            call sm1cs_km001_m01_c01 from _call_sm1cs_km001_m01_c01
            stop music fadeout 3.0
            scene sm1cs-km001-28 mc-responds_c1 with hpunch
            play voice2 mc_arrogant_huh3 noloop
            mc "Heh. I'll go easy on you."
        "Let's dance, Kellie."(hint="sm1cs_km001_m01_h02"):
            call sm1cs_km001_m01_c02 from _call_sm1cs_km001_m01_c02
            stop music fadeout 3.0
            scene sm1cs-km001-28 mc-responds_c1 with hpunch
            play voice2 mc_arrogant_huh3 noloop
            mc "Let's dance, Kellie."
    play voice3 girl31_angry_hmrr noloop
    play sound sfx_armored_whoosh1
    play sound2 sfx_stone_run1
    scene sm1cs-km001-29 km-raaghrrs-charges-mc_c1 with hpunch
    $ renpy.music.set_volume(0.8, 0.0, "music" )
    play music music_tatakai_fight
    km "Rauaagh!"
    stop sound2
    play sound sfx_sword_hit_metal2
    scene sm1cs-km001-30 mc-km-lock-swords-mc-why-so-intense-km-method-acting_c1 with hpunch
    play voice2 mc_surprised_huh8 noloop
    mc "Wow. Why so intense?"
    play voice3 girl31_angry_breathing noloop
    km "*grunting* A true thespian has to put it all out on the stage."
    play voice2 d1s5b_emmm noloop volume 2.0
    play sound sfx_armor_equiped2
    scene sm1cs-km001-31 mc-worried-sure-teach-fake-hit-kind-of-stuff_c1 with vpunch
    mc "Uh sure. But... nurrgh... shouldn't you teach me about like... fake-hits and taking a dive?"
    mc "That kind of stuff?"
    scene sm1cs-km001-32 km-plenty-time-if-mc-survives_c1 with dissolve
    play voice3 girl31_angry_cough4 noloop
    km "There will be plenty of time for that.{w} If you survive."
    play voice2 mc_scared_huh1 noloop
    play sound sfx_sword_hit_wood2
    scene sm1cs-km001-33 fighting-montage-one_c1 with hpunch
    pause
    play voice3 girl31_angry_argh noloop
    play sound sfx_epic_jump1
    scene sm1cs-km001-34 fighting-montage-two_c1 with dissolve
    pause
    play voice2 mc_angry_errr2 noloop
    play voice3 girl31_angry_ergh3 noloop
    play sound sfx_sword_hit_wood2
    scene sm1cs-km001-35 fighting-montage-three_c1 with hpunch
    pause
    play voice2 mc_scared_huuuh1 noloop
    play voice3 girl31_angry_dagh noloop
    play sound sfx_sword_hit_metal3
    scene sm1cs-km001-36 fighting-montage-four_c1 with vpunch
    mct "This may have been a mistake."
    play voice3 girl31_angry_ergh2 noloop
    play sound sfx_leg_kick1
    scene sm1cs-km001-37 fighting-montage-five-montage-ends_c1 with hpunch
    pause
    scene sm1cs-km001-38 mc-drops-knee-thinks-need-change-choice-menu_c1 with dissolve
    play voice2 mc_pain_rrrr noloop
    mct "I need to try changing things up."
    menu:
        "Distract her with flirting"(hint="sm1cs_km001_m02_h01"):
            call sm1cs_km001_m02_c01 from _call_sm1cs_km001_m02_c01
            scene sm1cs-km001-39 choice-flirt-mc-must-say-enchanting-killing-face-km-dont-be-wierd_c1 with dissolve
            play voice2 mc_thinking_hmm8 noloop
            mc "I must say, the face you make when you're trying to kill me is enchanting."
            play voice3 girl31_arrogant_hm1 noloop
            km "Don't be weird, [mcname]."
            play voice2 mc_surprised_wow1 noloop
            play sound sfx_sword_hit_wood3
            scene sm1cs-km001-40 mc-shocked-by-attack-wow-easy_c1 with vpunch
            mc "Woah. Easy Kellie!"
            scene sm1cs-km001-41 km-grins-acting-warriors-fighting-over-love-not-meant-easy_c1 with dissolve
            play voice3 girl31_arrogant_yeah1 noloop
            km "We're acting like two warriors fighting over their love."
            km "It's not meant to be easy."
            scene sm1cs-km001-42 km-mc-square-off-again_c1 with dissolve
            pause
        "Attack her high with heavy strikes"(hint="sm1cs_km001_m02_h02"):
            call sm1cs_km001_m02_c02 from _call_sm1cs_km001_m02_c02
            play voice2 d9s5_auch2 noloop
            play sound sfx_armored_whoosh2
            play sound2 sfx_stone_run1
            scene sm1cs-km001-43 choice-attack-mc-lunges-in-attack_c1 with dissolve
            pause
            stop sound2 fadeout 0.2
            play sound sfx_sword_whoosh1
            scene sm1cs-km001-44 mc-attacks-high-screams-yah_c1 with dissolve
            play voice2 mc_angry_errr4 noloop
            mc "Yiaaaaah!"
            play voice3 girl31_angry_hmrr noloop
            play sound sfx_sword_hit_wood1
            scene sm1cs-km001-45 km-blocks-barely-high-attack_c1 with vpunch
            km "*grunts*"
            scene sm1cs-km001-46 km-pushed-back-from-attack-one-knee-grunts_c1 with dissolve
            play voice3 girl31_arrogant_pff noloop
            km "Pffff."
            scene sm1cs-km001-47 km-assume-position-good-not-good-enough_c1 with dissolve
            play voice3 girl31_arrogant_ha noloop
            km "Okay. You've got some skill. But not enough to take me on!"
        "Be sneaky and go low"(hint="sm1cs_km001_m02_h03"):
            call sm1cs_km001_m02_c03 from _call_sm1cs_km001_m02_c03
            play sound sfx_armored_whoosh2
            scene sm1cs-km001-48 choice-sneaky-mct-try-catching-off-guard-swings-side-km_c1 with dissolve
            play voice2 mc_angry_hm2 noloop
            mct "Gotta try catching her off-guard."
            play sound sfx_armored_whoosh3
            scene sm1cs-km001-49 mc-does-fient-tries-attack-exposed-lower-leg-km_c1 with dissolve
            play voice2 mc_happy_hah2 noloop
            mct "I have you now."
            play voice3 girl31_arrogant_huh1 noloop
            play sound sfx_sword_whoosh1
            scene sm1cs-km001-50 km-jumps-over-mc-slash-mc-like-what_c1 with vpunch
            play voice2 mc_surprised_what3 noloop
            mc "What?!"
            play sound sfx_sword_hit_wood1
            scene sm1cs-km001-51 km-lands-front-mc-face-not-bad-for-noob_c1 with dissolve
            play voice3 girl31_arrogant_hm1 noloop
            km "Hmmm. Not bad for a amateur."
    play voice2 mc_pain_argh1 noloop
    play sound sfx_sword_hit_wood4
    scene sm1cs-km001-52 mc-one-final-lunge-attack-km-dips-dodges_c1 with vpunch
    mct "Okay. Enough screwing around. She'll never see this coming."
    play voice2 mc_pain_ou6 noloop
    play sound sfx_leg_kick2
    scene sm1cs-km001-53 km-shield-bashes-mc-in-the-back-sending-him-ground_c1 with hpunch
    mc "Whuaah!"
    play sound sfx_armor_fall1
    scene sm1cs-km001-54 mc-knocked-on-ass-km-tells-should-quit-while-ahead_c1 with dissolve
    play voice3 girl31_disappointed_mff2 noloop
    km "*panting lightly* You should quit while you're ahead."
    scene sm1cs-km001-55 km-you-dont-belong-stage-with-me-mc-didnt-hear-no-bells_c1 with dissolve
    km "You don't belong on the stage with me. Why don't you check if any sets need a new coat of paint."
    play voice2 mc_no_no8 noloop
    mc "I didn't hear no bell."
    play sound sfx_armor_equiped1
    scene sm1cs-km001-56 mc-back-in-fighting-position_c1 with dissolve
    play voice3 girl31_arrogant_hm1 noloop
    km "Hmmm."
    play voice3 girl31_angry_ergh4 noloop
    play sound sfx_sword_whoosh3
    scene sm1cs-km001-57 continue-montage-fight-one_c1 with dissolve
    pause
    play sound sfx_sword_hit_metal2
    scene sm1cs-km001-58 continue-montage-fight-two_c1 with hpunch
    pause
    scene sm1cs-km001-59 mc-blocks-attack-thinks-come-on_c1 with dissolve
    play voice2 d1s5_orgasm noloop
    mct "Come on!"
    play voice3 girl31_pain_ah3 noloop
    play sound sfx_sword_hit_human1
    scene sm1cs-km001-60 mc-hits-km-arm-she-growls-pain_c1 with hpunch
    km "Graaah!"
    play voice2 mc_happy_oof3 noloop
    mct "Phew. Started to worry I'd never get a hit in."
    play voice3 girl31_angry_argh noloop
    play sound sfx_armored_whoosh2
    scene sm1cs-km001-61 km-goes-full-attack-mc-easy-tries-call-km-out_c1 with vpunch
    play voice2 mc_surprised_wow2 noloop
    mc "Woah. Easy. I just got a little excited."
    mc "Kellie. Kellie?"
    play voice3 girl31_angry_dagh noloop
    play sound sfx_sword_hit_metal2
    scene sm1cs-km001-62 km-tells-mc-shouldve-quit-knocks-sword-away-mct-shit_c1 with hpunch
    km "You should have quit!"
    play voice2 mc_pain_ou1 noloop
    play sound sfx_sword_fall1
    scene sm1cs-km001-63 km-disarms-shield-while-talking_c1 with hpunch
    mct "Shitballs!"
    scene sm1cs-km001-a64 mc-back-his-ass-000 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
    play sound3 ["<silence 3.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs-km001-glambot-1
    pause
    play voice3 girl31_angry_kghh1 noloop
    km "You just come in and think you're going to be a pro?"
    km "You're so arrogant!"
    stop sound2 fadeout 1.0
    play sound sfx_sword_whoosh4
    scene sm1cs-km001-65 mc-ask-kelie-she-prepares-swing-again_c1 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Okay. I know when I'm beat. I give up, Kellie."
    scene sm1cs-km001-65 mc-ask-kelie-she-prepares-swing-again_c1 with hpunch
    mc "Kellie?"
    play sound sfx_heels_steps1 loop
    scene sm1cs-km001-66 dvh-vs-appear-stage-from-side_c1 with dissolve
    play voice4 girl34_thinking_emm1 noloop
    pause
    stop sound fadeout 1.0
    scene sm1cs-km001-67 vs-oh-my-god-dvh-god-stop_c1 with dissolve
    play voice5 girl33_surprised_ohmy noloop
    play voice4 girl34_surprised_huh2 noloop
    vs "Oh my god!"
    play voice4 girl34_hey_angry6 noloop
    dvh "Kellie! Stop!"
    scene sm1cs-km001-68 km-snaps-out-look-girls-huh_c1 with dissolve
    play voice3 girl31_surprised_uh1 noloop
    km "Huh?"
    scene sm1cs-km001-69 dvh-what-you-doing-km-cant-find-words_c1 with dissolve
    play voice4 girl34_angry_argh6 noloop
    dvh "What are you doing? He's down."
    play voice3 girl31_surprised_ah2 noloop
    km "Denise I..."
    play voice3 girl31_scared_ah8 noloop
    play sound sfx_sword_fall1
    play sound2 sfx_armor_fall1 noloop
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound3 sfx_heels_run2
    scene sm1cs-km001-70 km-drops-sword-runs-away-stage_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.4, 3.0, "music" )
    stop sound3 fadeout 1.0
    scene sm1cs-km001-71 vs-you-ok-mc-yeah-totally_c1 with dissolve
    play voice5 girl33_hey_scared noloop
    vs "Are you okay, [mcname]?"
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah. Totally. Just got the wind knocked out of me."
    play sound sfx_cloth_rustling2
    scene sm1cs-km001-72 dvh-talks-about-excusing-km_c1 with dissolve
    play voice4 girl34_thinking_emm2 noloop
    dvh "You'll have to forgive Kellie, [mcname]."
    dvh "I don't know what's gotten into her lately, but she's become a little high-strung."
    scene sm1cs-km001-73 vs-turns-mc-all-have-bad-days_c1 with dissolve
    play voice5 girl33_disappointed_oh noloop
    vs "We all have our bad days, but that is no reason to try to rage-stomp anyone."
    scene sm1cs-km001-74 dvh-pomises-will-talk-km_c1 with dissolve
    play voice4 girl34_yes_neutral4 noloop
    dvh "I know. I'll talk to her, [mcname]. I can promise you that."
    play sound sfx_heels_steps2 loop
    scene sm1cs-km001-75 dvh-vs-both-leave-stage_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.6, 3.0, "music" )
    stop sound fadeout 1.0
    scene sm1cs-km001-76 mc-left-alone-his-thoughts-end-scene_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mct "I usually have an effect on women, but never something quite like that."
    mct "Still, if I want to make the most of my time here, I should figure out what's got Kellie so worked up about me."
    mct "Hopefully, without dying."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(KM_STORY, 3, 0, 4, THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR)
    return
label sm1cs_km001_m01_c01:
    $ player.set_choice("sm1cs_km001_go_easy")
    $ CharacterController.get_character("km").deduct_point()
    return
label sm1cs_km001_m01_c02:
    $ CharacterController.get_character("km").add_point()
    return
label sm1cs_km001_m02_c01:
    $ player.set_choice("sm1cs_km001_distract")
    $ CharacterController.get_character("km").deduct_point()
    return
label sm1cs_km001_m02_c02:
    $ player.set_choice("sm1cs_km001_heavy_strike")
    $ CharacterController.get_character("km").add_point()
    return
label sm1cs_km001_m02_c03:
    $ player.set_choice("sm1cs_km001_go_low")
    $ CharacterController.get_character("km").add_point()
    return
label sm1cs_km001_unlocks:
    call sm1cs_km001_m01_c02 from _call_sm1cs_km001_m01_c02_1
    call sm1cs_km001_m02_c02 from _call_sm1cs_km001_m02_c02_1
    if config_storyline_mode is True:
        $ execute_storyline_config(KM_STORY)
    return