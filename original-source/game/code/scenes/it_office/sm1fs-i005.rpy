image sm1fs-i005-glambot-1 = Movie(play = "images/FS_IT/s005/anim/sm1fs-i005-a26-2x-60fps.webm", start_image = "sm1fs-i005-a26 infected-glambot-000", image = "sm1fs-i005-a26 infected-glambot-119", loop = False)
label sm1fs_i005:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play sound4 sfx_office_ambience1 fadein 1.0
    scene sm1fs-i005-00 infected_office_full with dissolve
    play sound sfx_keyboard_typing2 volume 2.0
    play music lofi1
    pause
    play sound2 sfx_heels_steps2
    scene sm1fs-i005-01 infected_office_full_ag_talk_desk with dissolve
    stop sound2 fadeout 2.0
    play voice3 girl27_hey_simple3 noloop
    ag "Morning, [mcname]."
    scene sm1fs-i005-02 infected_office_full_mc_talk with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey, Anna."
    scene sm1fs-i005-03 infected_office_full_ag_talk_desk with dissolve
    play voice3 girl27_thinking_hmm3 noloop
    ag "Have a good evening?"
    scene sm1fs-i005-04 infected_office_full_mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah I guess.{w} You?"
    play sound sfx_throw_something1
    scene sm1fs-i005-05 infected_office_full_ag_talk_excited with dissolve
    play voice3 girl27_yes_ya noloop
    ag "Not too bad. Was working on a problem for a while. A real brain teaser."
    ag "Decided to play the new update for Skelstorm: Komach's Revenge to take my mind off the problem."
    ag "I finally loaded onto the server, and it hit me."
    play sound sfx_hands_clap3
    scene sm1fs-i005-06 infected_office_full_ag_talk_pow with dissolve
    play voice3 girl27_pain_ah2 noloop
    ag "Pow."
    scene sm1fs-i005-07 infected_office_full_ag_talk_smile with dissolve
    play voice3 girl27_happy_laugh4 noloop
    ag "I can do all of it in the wedding chapter."
    mct "Wedding chapter?"
    scene sm1fs-i005-08 infected_office_full_mc_talk_unsure with dissolve
    mct "I have no idea what she is talking about."
    mct "It certainly doesn't sound like Orbix work."
    play voice2 mc_happy_yay1 noloop
    mc "Sounds great, Anna."
    scene sm1fs-i005-09 infected_office_full_ag_talk_relieved with dissolve
    play voice3 girl27_yes_yap2 noloop
    ag "It is. It will be."
    scene sm1fs-i005-10 infected_office_full_ag_talk_nervous with dissolve
    play voice3 girl27_thinking_emm2 noloop
    ag "At least I hope so."
    play sound sfx_heels_steps2 loop
    scene sm1fs-i005-11 infected_office_full_ag_talk_walk_away with dissolve
    pause
    stop sound fadeout 2.0
    play sound2 sfx_chair_slide1 noloop
    scene sm1fs-i005-12 infected_office_full_jaydengetsup with dissolve
    pause
    play sound sfx_cloth_rustling3 volume 1.6
    scene sm1fs-i005-13 infected_office_full_jaydenlunge with dissolve
    play voice4 boy10_pain_ahh1 noloop
    jh "*grunting* One. Two."
    scene sm1fs-i005-14 infected_office_full_ siennatriesignore with dissolve
    play voice5 girl35_disappointed_mff1 noloop
    pause
    play sound sfx_cloth_rustling5 volume 1.6
    scene sm1fs-i005-15 infected_office_full_jh_talk_both with dissolve
    play voice4 boy10_disgust_oof noloop
    jh "Six. Seven."
    jh "Come on. Feel that burn."
    play voice5 girl35_angry_cough1 noloop
    play sound sfx_cloth_planket2
    scene sm1fs-i005-16 infected_office_full_sr_talk with hpunch
    sr "Jayden, please."
    sr "I'm trying to scan this new config and I can't concentrate."
    play sound sfx_cloth_rustling3
    scene sm1fs-i005-17 infected_office_full_jh_talk_squat with dissolve
    play voice4 boy10_surprised_oh noloop
    jh "If you don't squat, Sienna, you drop."
    play sound sfx_cloth_rustling2
    scene sm1fs-i005-18 infected_office_full_jh_talk_standing with dissolve
    play voice4 boy10_arrogant_hm noloop
    jh "Just put on some headphones."
    scene sm1fs-i005-19 infected_office_full_sr_talk_look with dissolve
    play voice5 girl35_yes_angry1 noloop
    sr "Or you could do your squatting outside?"
    sr "Ever heard of tai chi?"
    scene sm1fs-i005-20 infected_office_full_jh_talk_smiling with dissolve
    play voice4 boy10_happy_mmm noloop volume 1.7
    jh "Sure. Let's do some tai chi together."
    jh "But I gotta finish my squats."
    play sound sfx_cloth_rustling1
    scene sm1fs-i005-17 infected_office_full_jh_talk_squat with dissolve
    play voice4 boy10_disappointed_ohh noloop
    jh "One.{w} Two."
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1fs-i005-21 infected_office_full_sr_talk_sigh with dissolve
    play voice5 girl35_disappointed_mff2 noloop
    pause
    play sound2 sfx_cloth_rustling5 noloop
    scene sm1fs-i005-22 infected_office_full_squatting with dissolve
    play voice4 boy10_disgust_boeagh noloop
    pause
    scene sm1fs-i005-23 infected_office_full_sr_talk_lookup with hpunch
    play voice5 girl35_angry_argh5 noloop
    sr "Oh my god, that's disgusting!"
    scene sm1fs-i005-24 infected_office_full_jh_talk_ with dissolve
    play voice4 boy10_hey_scandalized noloop
    jh "Get real. I'm almost done."
    play voice5 girl35_scared_ah8 noloop
    scene sm1fs-i005-25 infected_office_full_sr_talk_shock with hpunch
    sr "Not you, Jayden."
    stop music fadeout 4.0
    sr "That!"
    queue music music_sirens_transition1
    scene sm1fs-i005-a26 infected-glambot-000 with dissolve
    pause 0.01
    play sound sfx_camera_fly1 volume 2.0
    scene sm1fs-i005-glambot-1
    play voice4 boy10_surprised_huh noloop
    jh "Huh?"
    scene sm1fs-i005-27 infected_office_full_jh_talk_grinning with dissolve
    queue music music_pornergency volume 0.8
    play voice4 boy10_surprised_ohmy noloop
    jh "Oh..."
    jh "Sienna. I never thought you'd be into this."
    scene sm1fs-i005-28 infected_office_full_sr_talk_angry with dissolve
    play voice5 girl35_surprised_what3 noloop
    sr "What?"
    sr "I didn't put this on."
    sr "I'd never watch something like this."
    scene sm1fs-i005-29 infected_office_full_jh_talk with dissolve
    play voice4 boy10_yes_aga noloop volume 1.5
    jh "Sure. Then what's it doing on your computer?"
    play sound sfx_heels_steps1
    scene sm1fs-i005-30 infected_office_full_mc_talk_walkover with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "What's going on?"
    stop sound fadeout 1.0
    scene sm1fs-i005-31 infected_office_full_jh_talk_pointscreenlaugh with dissolve
    play voice4 boy10_hey_happy noloop volume 1.5
    jh "Hey, new guy."
    jh "Check it out."
    if player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS) >= 15:
        scene sm1fs-i005-32 infected_office_full_mc_talk_annoyed with dissolve
        play voice2 mc_angry_huh1 noloop
        mc "Uh, I've been here a while now, Jayden."
        mc "My name is-"
    scene sm1fs-i005-33 infected_office_full_jh_talk_waving_srnervous with dissolve
    play voice4 boy10_yes_yeah noloop
    jh "Yeah, yeah. Just watch."
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1fs-i005-34 infected_office_full_sr_talk with dissolve
    play voice5 girl35_scared_oof3 noloop
    sr "I can't remove it."
    scene sm1fs-i005-35 infected_office_full_mc_talk_shock with dissolve
    play voice2 mc_surprised_wtf1 noloop
    mc "What the?"
    mct "Now that's something you don't see every day."
    menu:
        "Could be fun":
            $ player.set_choice("sm1fs_i005_double_penetration")
            scene sm1fs-i005-36 infected_office_full_mc_thought_menu_horny with dissolve
            play voice2 mc_thinking_mmm7 noloop
            mct "Maybe I should figure out doing that with Stacy sometime."
        "Not really for me":
            scene sm1fs-i005-37 infected_office_full_mc_thought_menu_notintoit with dissolve
            play voice2 mc_thinking_mmm4 noloop
            mct "Not really my style."
    play sound sfx_throw_something1
    scene sm1fs-i005-38 infected_office_full_sr_talk_lookmcjh with dissolve
    play voice5 girl35_hey_angry1 noloop
    sr "You two should get back to your seats."
    scene sm1fs-i005-39 infected_office_full_sr_talk_focus_screen with dissolve
    play voice5 girl35_arrogant_hm2 noloop
    sr "You're not helping me here."
    scene sm1fs-i005-40 infected_office_full_jh_talk_laugh with dissolve
    play voice4 boy10_pain_sobs noloop
    jh "Oh yeah. She doesn't need our help."
    jh "She's a soloist."
    play voice5 girl35_angry_dough3 noloop
    scene sm1fs-i005-41 infected_office_full_sr_talk with vpunch
    sr "Shut up, Jayden."
    scene sm1fs-i005-42 infected_office_full_jh_talk with dissolve
    play voice4 boy10_no_nonono noloop
    jh "Don't tell me to shut up."
    scene sm1fs-i005-43 infected_office_full_sr_talk_eyes_widen with dissolve
    play voice6 otherchar_boy5_argh3_phoned noloop
    "Actor 1" "Yeah take that bitch."
    play voice5 girl35_scared_huh1 noloop
    play sound sfx_leg_kick5
    play sound2 sfx_fall_down1 noloop
    play sound3 sfx_bed_slide1 noloop
    scene sm1fs-i005-44 infected_office_full_jh_talk_on_ass_sr_standingover with vpunch
    play voice4 boy10_pain_ouch noloop
    sr "What did you just call me?"
    scene sm1fs-i005-45 infected_office_full_jh_talk with dissolve
    play voice4 boy10_disgust_oof noloop
    jh "That wasn't me."
    scene sm1fs-i005-46 infected_office_full_sr_talk_pointing with dissolve
    play voice5 girl35_angry_err2 noloop
    sr "I'm going to grab Maureen right now."
    sr "You're an insect to me, Jayden. A fly about to be splattered."
    scene sm1fs-i005-47 infected_office_full_mc_talk_realizing with dissolve
    play voice2 d2s12_emmm noloop
    mc "I don't think he called you-"
    scene sm1fs-i005-48 infected_office_full_sr_intense_look with dissolve
    play voice5 girl35_disappointed_mmm1 noloop
    sr "..."
    play voice2 d2s9_confused noloop
    mc "*nervous* That word."
    scene sm1fs-i005-49 infected_office_full_mc_talk_nervous with dissolve
    play sound5 otherchar_sex_sucking1_phoned
    pause
    scene sm1fs-i005-50 infected_office_full_mc_jh_lookat_jh_computer with dissolve
    play voice6 otherchar_boy5_fuck_phoned noloop
    "Actor 1" "Yeah. Kiss it.{w} Suck on those balls."
    scene sm1fs-i005-51 infected_office_full_jh_talk_lookup with dissolve
    play voice4 boy10_pain_ahh2 noloop
    jh "That can't be good."
    scene sm1fs-i005-52 infected_office_full_sr_talk_lookingdown with dissolve
    play voice5 girl35_pain_ah3 noloop
    sr "It's spreading."
    play voice4 boy10_scared_huh noloop
    play sound [sfx_keyboard_enter1, sfx_keyboard_enter1, sfx_keyboard_enter1]
    play sound2 ["<silence 0.15>", sfx_keyboard_enter1, "<silence 0.15>", sfx_keyboard_enter1, sfx_keyboard_enter1] noloop
    scene sm1fs-i005-53 infected_office_full_jh_talk_rushesover with hpunch
    jh "Fuck. Control alt delete."
    jh "Come on. Task Manager. Open damnit."
    menu:
        "Tease him":
            $ player.set_choice("sm1fs_i005_tease_jh")
            scene sm1fs-i005-54 infected_office_full_mc_talk_teasing with dissolve
            play voice2 mc_happy_laugh2 noloop
            mc "Looks like we got to see your interests too."
            scene sm1fs-i005-55 infected_office_full_jh_talk with dissolve
            play voice4 boy10_no_happy noloop
            jh "No. I never look at porn."
            scene sm1fs-i005-56 infected_office_full_jh_talk_biggame with dissolve
            play voice4 boy10_happy_laugh2 noloop
            jh "I don't need it. I get nines.{w} All the time."
            scene sm1fs-i005-57 infected_office_full_mc_talk_surebuddy with dissolve
            play voice2 mc_yes_sure1 noloop
            mc "Sure, buddy."
            play voice4 boy10_scared_ah3 noloop volume 1.4
            play sound sfx_cloth_rustling1
            scene sm1fs-i005-58 infected_office_full_jh_talk with hpunch
            jh "Screw you."
        "Focus":
            pass
    scene sm1fs-i005-59 infected_office_full_am_talk_pm_look with dissolve
    pause
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1fs-i005-60 infected_office_full_am_talk with dissolve
    play voice3 girl22_happy_laugh1 noloop
    am "Petey's looking up porn too."
    scene sm1fs-i005-61 infected_office_full_pm_talk with dissolve
    play voice4 boy7_disgust_ooh noloop
    pm "April. Jesus..."
    play sound sfx_straw_drink5 volume 1.6
    scene sm1fs-i005-62 infected_office_full_am_slurping with dissolve
    am "*noisy slurping*"
    scene sm1fs-i005-63 infected_office_full_am_talk with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "You're the one watching a foursome in the middle of the workday."
    scene sm1fs-i005-64 infected_office_full_pm_talk with dissolve
    play voice4 boy7_no_serious noloop
    pm "I never did that."
    scene sm1fs-i005-65 infected_office_full_am_talk_smirk with dissolve
    play voice3 girl22_arrogant_hm noloop
    pause
    scene sm1fs-i005-66 infected_office_full_pm_talk_look_am with dissolve
    play voice4 boy7_hey_simple noloop
    pm "Sienna. You're Dev Ops.{w} Stop this."
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1fs-i005-67 infected_office_full_sr_talk_keyboard with dissolve
    play voice5 girl35_angry_hmm2 noloop
    sr "I'm trying. It's unlike anything I've seen before."
    scene sm1fs-i005-68 infected_office_full_pm_talk_nervous with dissolve
    play voice4 boy7_disappointed_oof noloop
    pm "Hurry."
    scene sm1fs-i005-70 infected_office_full_pm_talk with dissolve
    play voice4 boy7_thinking_emm1 noloop
    pm "Please hurry."
    scene sm1fs-i005-69 infected_office_full_sr_glare with dissolve
    play voice5 girl35_hey_irritated noloop
    sr "April, I could use some help."
    scene sm1fs-i005-72 infected_office_full_am_talk with dissolve
    play voice3 girl22_yes_aga1 noloop
    am "You {i}sure{/i} could."
    play sound sfx_straw_drink4 volume 1.6
    scene sm1fs-i005-71 infected_office_full_sr_talk_am_slurp with dissolve
    play sound2 sfx_keyboard_typing2 volume 2.0 noloop
    play voice5 girl35_disappointed_geh5 noloop
    sr "I think it's a Dark Kernel Cavein."
    scene sm1fs-i005-74 infected_office_full_am_talk_talk down with dissolve
    play voice3 girl22_surprised_huh2 noloop
    am "*scoffs* This fast? Are we pretending like we're back in high school and we don't know anything about coding?"
    scene sm1fs-i005-75 infected_office_full_sr_talk_pleading with dissolve
    play voice5 girl35_disappointed_mff3 noloop
    sr "Ugh. April, come on."
    scene sm1fs-i005-76 infected_office_full_am_talk with dissolve
    play voice3 girl22_arrogant_ha noloop
    am "You're the DevOps Specialist."
    am "Specialize."
    scene sm1fs-i005-77 infected_office_full_cw_talk_ around with dissolve
    play voice4 girl29_arrogant_huh noloop
    cw "What is going on here?"
    play sound sfx_heels_steps1 volume 1.5
    scene sm1fs-i005-78 infected_office_full_ag_talk with dissolve
    play voice5 girl27_hey_greeting noloop
    ag "[mcname]. Don't you have those TPS reports to-"
    stop sound fadeout 1.0
    scene sm1fs-i005-79 infected_office_full_ag_talk_notice screen with dissolve
    play voice5 girl27_surprised_eh2 noloop
    ag "File..."
    scene sm1fs-i005-81 infected_office_full_cw_talk_ with dissolve
    play voice4 girl29_surprised_huh1 noloop
    cw "What in the Chrome fuckery is that?"
    scene sm1fs-i005-82 infected_office_full_sr_talk with dissolve
    play voice5 girl35_thinking_eem4 noloop
    sr "Porn showed up on Peter's computer."
    play voice6 boy7_no_nonono noloop
    scene sm1fs-i005-83 infected_office_full_pm_talk with hpunch
    pm "I swear it's not mine!"
    scene sm1fs-i005-84 infected_office_full_sr_talk_cw with dissolve
    play voice5 girl35_disappointed_aah noloop
    sr "It's appearing on all our systems."
    sr "Ms. Watts.{w} We are being penetrated."
    am "*chuckling* Again and again."
    scene sm1fs-i005-85 infected_office_full_cw_talk_look_fixit with dissolve
    play voice4 girl29_angry_ehh noloop
    cw "Well, fix it!"
    scene sm1fs-i005-86 infected_office_full_sr_talk with dissolve
    play voice5 girl35_scared_huh4 noloop
    sr "What do you think I'm trying to do?"
    play sound sfx_cloth_rustling2 volume 1.5
    scene sm1fs-i005-87 infected_office_full_am_talk_drink_mc with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "Hold this and look pretty."
    scene sm1fs-i005-88 infected_office_full_mc_talk_drink_mc with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Huh?"
    scene sm1fs-i005-89 infected_office_full_am_talk_movepmchair with dissolve
    play voice3 girl22_hey_simple noloop
    am "Move Petey."
    scene sm1fs-i005-90 infected_office_full_pm_talk with dissolve
    play voice4 boy7_hey_serious noloop
    pm "Hey."
    play sound sfx_keyboard_typing2 volume 2.0
    play sound2 sfx_chair_slide1 noloop
    scene sm1fs-i005-91 infected_office_full_am_talk_desk with dissolve
    play voice3 girl22_yes_aga11 noloop
    am "We'll call you when we need some dead weight with a nice haircut."
    play sound sfx_keyboard_typing2
    scene sm1fs-i005-92 infected_office_full_am_talk_pop with dissolve
    pause
    play sound2 sfx_chupachups3 volume 1.6
    scene sm1fs-i005-93 infected_office_full_am_talk_suck with dissolve
    am "*sucking*"
    play sound2 sfx_chupachups1 noloop volume 1.5
    scene sm1fs-i005-94 infected_office_full_am_talk with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "Shortcuts aren't working."
    scene sm1fs-i005-95 infected_office_full_sr_talk_suck_explaining with dissolve
    play voice4 girl35_yes_simple1 noloop
    sr "Already tried that."
    sr "I can't even open the kernel."
    scene sm1fs-i005-96 infected_office_full_am_talk with dissolve
    play voice3 girl22_disappointed_mmf noloop
    am "Shit."
    am "[mcname]. See if anyone's computer is not being affected."
    scene sm1fs-i005-98 infected_office_full_mc_talk_nod with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.5
    mc "Okay."
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1fs-i005-97 infected_office_full_am_talk_turn with dissolve
    pause
    scene sm1fs-i005-99 infected_office_full_lm_talk_sip with dissolve
    play sound2 sfx_drink_slurp2 noloop
    pause
    scene sm1fs-i005-100 infected_office_full_lm_talk with dissolve
    play voice4 girl37_thinking_hmm2 noloop
    lm "I mean, I'm not saying those are the biggest tits I've seen."
    lm "But they are big and juicy."
    scene sm1fs-i005-101 infected_office_full_ml_talk_popsin with dissolve
    play voice5 girl9_disappointed_oof noloop
    ml "All I see is a lawsuit waiting to happen."
    ml "This is why our country is going down the pipes."
    scene sm1fs-i005-102 infected_office_full_lm_talk_annoyed with dissolve
    play voice4 girl37_disappointed_ehh noloop
    lm "*sighs* Please, Maureen. Not now."
    scene sm1fs-i005-103 infected_office_full_lm_talk_gesturing with dissolve
    lm "Sienna will figure this out soon."
    scene sm1fs-i005-104 infected_office_full_lm_talk_lookingatscreen with dissolve
    pause
    scene sm1fs-i005-105 infected_office_full_lm_talk with dissolve
    play voice4 girl37_thinking_oh noloop
    lm "Oh. Yeah she is sucking one and jerking off the other."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    stop sound4 fadeout 10.0
    scene sm1fs-i005-106 infected_office_full_lm_talk with dissolve
    lm "Just fucking... going to town."
    play voice5 girl9_angry_eh noloop
    ml "So many people are about to be fired."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1fs-i005-107 infected_office_full_lm_talk_lookmc with dissolve
    play voice4 girl37_hey_happy1 noloop
    lm "Oh hey, [mcname]."
    scene sm1fs-i005-108 infected_office_full_ml_talk_lookmc with dissolve
    play voice5 girl9_arrogant_ha2 noloop
    ml "Can we help you? Libby's screen is still corrupted by smut."
    scene sm1fs-i005-110 infected_office_full_eg_talk with dissolve
    play voice3 boy5_surprised_huh4 noloop
    en "What is problem?"
    en "This is just beautiful and natural expression of love."
    scene sm1fs-i005-112 infected_office_full_ml_talk_disgusted with dissolve
    play voice5 girl9_no_uhuh noloop
    ml "Love? This isn't love. This is just unadulterated lust."
    scene sm1fs-i005-110 infected_office_full_eg_talk with dissolve
    play voice3 boy5_yes_simple2 noloop
    en "Yes. That is what I said."
    en "Just pure joy and love. We should all have more of this in our lives."
    scene sm1fs-i005-111 infected_office_full_lm_talk with dissolve
    play voice4 girl37_happy_phewhaha noloop
    lm "Grow titties like hers Eugene and I'm sure you'll find someone to suck on them."
    play sound sfx_heels_run2
    scene sm1fs-i005-113 infected_office_full_lm_talk_ml_leaving with hpunch
    play voice5 girl9_disgust_boeah noloop
    ml "I'm going to pretend I didn't hear that, Libby."
    play voice4 girl37_happy_relief noloop
    scene sm1fs-i005-114 infected_office_full_eg_talk_lookscreen with dissolve
    lm "I thought she'd never leave."
    play voice3 boy5_thinking_oh1 noloop
    en "Ah, now they are commencing the 'Beast with three backs'."
    scene sm1fs-i005-115 infected_office_full_lm_talk with dissolve
    play voice4 girl37_arrogant_ha noloop
    lm "Good eye, Eugene."
    scene sm1fs-i005-116 infected_office_full_eg_talk_disappointed with dissolve
    play voice3 boy5_disappointed_oof1 noloop
    en "This is much better than what {b}my{/b} screen had."
    scene sm1fs-i005-117 infected_office_full_mc_talk_mc_lm_look_eg with dissolve
    play voice2 mc_disgust_ooh2 noloop
    mc "Don't."
    scene sm1fs-i005-118 infected_office_full_lm_talk with dissolve
    play voice4 girl37_no_happy noloop
    lm "No, I'm curious."
    scene sm1fs-i005-119 infected_office_full_lm_talk_gesture with dissolve
    play voice4 girl37_arrogant_laugh noloop
    lm "Why don't you show [mcname] your screen, Eugene."
    scene sm1fs-i005-120 infected_office_full_eg_talk_studyingmc_mmh with dissolve
    play voice3 boy5_thinking_hmm2 noloop
    en "Mmmm."
    scene sm1fs-i005-121 infected_office_full_eg_talk with dissolve
    play voice3 boy5_no_nonono noloop
    en "I am not a wicked man, Libby."
    scene sm1fs-i005-122 infected_office_full_lm_talk with dissolve
    play voice4 girl37_arrogant_laughing noloop
    lm "Haha."
    stop sound2 fadeout 1.0
    scene sm1fs-i005-123 infected_office_full_mc_talk_point with dissolve
    play sound4 sfx_error_countdown1
    play voice2 mc_pain_ou1 noloop
    mc "Oh shit. What's that?"
    scene sm1fs-i005-123-1 infected_office_full_mc_talk_point_5seconds with dissolve
    pause
    play voice2 mc_hey_hey1 noloop
    scene sm1fs-i005-124 infected_office_full_mc_talk_shout_am with hpunch
    mc "April!"
    scene sm1fs-i005-125 infected_office_full_am_talk_typing with dissolve
    play sound2 sfx_chupachups3
    play voice4 girl22_yes_aga5 noloop
    am "We see it."
    play sound sfx_keyboard_typing2 volume 2.5 loop
    scene sm1fs-i005-126 infected_office_full_am_talk_screen with dissolve
    play voice4 girl22_angry_argh1 noloop
    am "Come on."
    am "You squirrely bastard."
    am "Where are you?"
    scene sm1fs-i005-127 infected_office_full_sr_talk_worried with dissolve
    play voice5 girl35_disappointed_mmm2 noloop
    sr "I'm going to get fired for this."
    scene sm1fs-i005-128 infected_office_full_am_talk with dissolve
    play voice4 girl22_yes_yeah3 noloop
    am "Yeah, probably."
    stop sound fadeout 1.0
    play sound2 sfx_box_placed1 noloop
    scene sm1fs-i005-129 infected_office_full_am_talk_screen with dissolve
    pause
    play voice3 girl27_hey_expressive noloop
    scene sm1fs-i005-130 infected_office_full_ag_talk_excited with hpunch
    ag "April, I found it."
    ag "It's in file directory sales flash two-thousand-twenty slash Oh Bee Jay slash archive."
    play sound sfx_chupachups2
    play sound2 sfx_biologic_spit1 noloop volume 1.4
    scene sm1fs-i005-131 infected_office_full_sr_talk_spit with dissolve
    queue sound sfx_keyboard_typing2 volume 2.5 loop
    am "*spitting*"
    play voice4 girl35_disgust_moeagh noloop
    sr "Ewww. April!"
    play voice3 girl22_angry_argh3 noloop
    scene sm1fs-i005-132 infected_office_full_am_talk with hpunch
    am "Fuck fuck fuck."
    scene sm1fs-i005-133 infected_office_full_am_talk_screen with dissolve
    play voice3 girl22_arrogant_he noloop
    am "Gotchu."
    stop sound fadeout 1.0
    play sound5 sfx_jail_notification noloop volume 0.5
    stop sound4 fadeout 1.0
    play voice3 girl22_angry_cough noloop
    queue sound4 sfx_tv_porn1
    am "Shit."
    play voice4 girl27_disappointed_oh2 noloop
    ag "Oh darn."
    scene sm1fs-i005-134 infected_office_full_eg_talk_smile with dissolve
    play voice6 boy5_happy_laugh1 noloop
    en "Heh heh."
    scene sm1fs-i005-135 infected_office_full_eg_talk_sad with dissolve
    play voice6 boy5_disappointed_oof1 noloop
    en "Oh."
    play voice6 boy5_angry_argh3 noloop
    scene sm1fs-i005-136 infected_office_full_eg_talk_screen_shows_bodiesblock with hpunch
    en "Oh. Mother of god!"
    en "What is oblivion is that?!"
    scene sm1fs-i005-137 infected_office_full_jh_talk_shocked with dissolve
    play voice5 boy10_scared_ah1 noloop
    jh "Nah... nah man."
    jh "I don't want to see {i}that{/i}."
    scene sm1fs-i005-138 infected_office_full_ml_talk with dissolve
    play voice4 girl9_scared_ah4 noloop
    ml "Is the man..."
    play voice5 boy10_scared_ah2 noloop
    scene sm1fs-i005-139 infected_office_full_jh_talk with hpunch
    jh "Don't look at it!"
    play voice3 girl27_pain_ah3 noloop
    scene sm1fs-i005-140 infected_office_full_ag_talk_freakingout with hpunch
    ag "My eyes!"
    play voice4 nari_sex_scream8 noloop
    scene sm1fs-i005-141 infected_office_full_ns_talk_freakingout_cry with vpunch
    ns "Why?!"
    play sound sfx_light_turn2 volume 3.5
    scene sm1fs-i005-142 infected_office_full_cw_switch with dissolve
    "CLICK"
    play sound2 sfx_light_shutdown1 noloop volume 2.0
    play sound sfx_light_podium_3
    stop sound4 fadeout 1.0
    scene sm1fs-i005-143 infected_office_full_screensdark with dissolve
    "Dooooooommm..."
    scene sm1fs-i005-144 infected_office_full_ag_talk_relaxing with dissolve
    play voice3 girl27_angry_breathing noloop
    ag "*sighing heavily*"
    stop voice3 fadeout 2.0
    scene sm1fs-i005-145 infected_office_full_mc_lookingaround with dissolve
    pause
    scene sm1fs-i005-146 infected_office_full_am_stunned with dissolve
    play voice4 girl22_disappointed_ehh2 noloop
    pause
    play sound sfx_door_slide4
    scene sm1fs-i005-147 infected_office_full_am_fishing with dissolve
    pause
    play sound sfx_bottle_chponk1
    scene sm1fs-i005-148 infected_office_full_am_bottle with dissolve
    pause
    play sound [sfx_drink_gulp, "<silence 0.3>", sfx_drink_gulp, "<silence 0.3>", sfx_drink_gulp]
    scene sm1fs-i005-149 infected_office_full_am_drink with dissolve
    am "*gulp gulp*"
    play sound sfx_cloth_rustling2
    scene sm1fs-i005-150 infected_office_full_sr_talk_bottle with dissolve
    play voice5 girl35_surprised_oh1 noloop
    sr "Oh.{w} That's Peters."
    scene sm1fs-i005-151 infected_office_full_am_talk with dissolve
    play voice4 girl22_yes_yep4 noloop
    am "I'll pay him back."
    am "You need something for brain bleach."
    scene sm1fs-i005-152 infected_office_full_sr_talk_nervous with dissolve
    pause
    play sound sfx_cloth_rustling1
    scene sm1fs-i005-153 infected_office_full_sr_talk_takebottle with dissolve
    play voice5 girl35_happy_mmm4 noloop
    pause
    play sound [sfx_drink_gulp, "<silence 0.3>", sfx_drink_gulp, "<silence 0.3>", sfx_drink_gulp]
    scene sm1fs-i005-154 infected_office_full_sr_talk_drink with dissolve
    sr "*glug*"
    play sound sfx_glass_bottle_bonk
    scene sm1fs-i005-155 infected_office_full_am_sr_bothsigh with dissolve
    play voice5 girl35_happy_relief2 noloop
    pause
    stop music fadeout 3.0
    scene sm1fs-i005-156 infected_office_full_cw_talk_conference with Fade(0.5, 0.5, 0.5)
    queue music music_pornorgency_interrogation
    play voice3 girl29_thinking_hmm1 noloop
    cw "Here is the thing. I don't judge."
    cw "I will leave that to the judges of our country."
    scene sm1fs-i005-157 infected_office_full_cw_talk_worried with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "And hopefully not to any lawyers who get involved with this."
    scene sm1fs-i005-158 infected_office_full_cw_talk_confident with dissolve
    cw "And I've done things."
    scene sm1fs-i005-159 infected_office_full_cw_talk_gestures with dissolve
    play voice3 girl29_thinking_hmm3 noloop
    cw "I {i}mean{/i} I've seen things."
    scene sm1fs-i005-160 infected_office_full_cw_talk_darkness with dissolve
    play voice3 girl29_arrogant_he noloop
    cw "I mean everyone has seen things. It's the internet."
    cw "You see things by pure accident sometimes."
    scene sm1fs-i005-161 infected_office_full_cw_talk_brave with dissolve
    play voice3 girl29_thinking_hmm2 noloop
    cw "But..."
    cw "Some things."
    scene sm1fs-i005-162 infected_office_full_cw_talk_sigh with dissolve
    play voice3 girl29_surprised_ehh noloop
    cw "Some of the things I saw on those screens before I shut down the power..."
    scene sm1fs-i005-163 infected_office_full_cw_talk_speak_again with dissolve
    play voice3 girl29_happy_relief noloop
    cw "*sighs*"
    cw "Well..."
    play sound sfx_cloth_rustling2
    scene sm1fs-i005-164 infected_office_full_cw_talk_cough with dissolve
    play voice3 girl29_pain_cough1 noloop
    cw "Mmm-hmm."
    scene sm1fs-i005-165 infected_office_full_cw_talk_relaxes with dissolve
    play voice3 girl29_thinking_mmm1 noloop
    cw "They don't belong on Orbix monitors."
    scene sm1fs-i005-166 infected_office_full_cw_talk with dissolve
    play voice3 girl29_yes_aga2 noloop
    cw "And some will say that hitting the kill switch didn't stop the virus and that I only added more work for Sienna, Anna, and April."
    scene sm1fs-i005-167 infected_office_full_cw_talk_madather with dissolve
    play voice3 girl29_thinking_hmm5 noloop
    cw "Well..."
    play sound sfx_cloth_rustling4
    scene sm1fs-i005-168 infected_office_full_cw_talk_thinking with dissolve
    play voice3 girl29_arrogant_ha noloop
    cw "You know. Many heroes are misunderstood in their time."
    scene sm1fs-i005-169 infected_office_full_cw_talk_justdontgetit with dissolve
    play voice3 girl29_arrogant_yeah noloop
    cw "It's not till later on that their brave acts truly get recognized."
    scene sm1fs-i005-170 infected_office_full_cw_talk_smile with dissolve
    play voice3 girl29_thinking_oh noloop
    cw "But I'm no hero."
    cw "End of the day, I was just trying to put an end to the panic."
    scene sm1fs-i005-171 infected_office_full_cw_talk_smile_neutral with dissolve
    play voice3 girl29_thinking_hmm4 noloop
    cw "So I guess, in a way."
    cw "I {i}was{/i} the hero.{w} Hmm."
    scene sm1fs-i005-172 infected_office_full_mc_talk with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Is that why I'm recording this?"
    mc "To explain what went down?"
    scene sm1fs-i005-173 infected_office_full_cw_talk with dissolve
    play voice3 girl29_yes_serious noloop
    cw "Exactly. I'm hoping not to need it, but you never know with {i}my{/i} boss."
    cw "Thanks for your help, [mcname]."
    cw "You can turn it off now."
    scene sm1fs-i005-172 infected_office_full_mc_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    jump sm1fs_i005_conference
label sm1fs_i005_conference:
    $ renpy.music.set_volume(0.2, 0.0, "sound4" )
    play sound4 sfx_classroom_ambience
    scene sm1fs-i005-175 infected_office_full_cw_talk_conference with Fade(0.5, 0.5, 0.5)
    play voice3 girl29_thinking_mmm2 noloop
    cw "Okay."
    cw "Just so I understand completely."
    scene sm1fs-i005-176 infected_office_full_cw_talk_worried with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "We were hacked."
    if player.has_played_scene("sm1cs_ns008"):
        scene sm1fs-i005-177 infected_office_full_cw_talk_look_ag with dissolve
        play voice3 girl29_arrogant_hm noloop
        cw "And our lead suspect is this troll that Angela warned us about."
        scene sm1fs-i005-178 infected_office_full_cw_talk_look_am with dissolve
        play voice3 girl29_arrogant_pff noloop
        cw "Meaning we were unprepared."
        scene sm1fs-i005-179 infected_office_full_am_talk_onus with dissolve
        play voice4 girl22_disappointed_ehh3 noloop
        am "No one said anything about the guy being some fucking Neo combined with Mr. Robot."
        scene sm1fs-i005-180 infected_office_full_cw_talk_annoyed with dissolve
        play voice3 girl29_surprised_huh2 noloop
        cw "Are you... are you impressed by the troll?"
        scene sm1fs-i005-181 infected_office_full_am_talk_shrug with dissolve
        play voice4 girl22_yes_yep1 noloop
        am "Game respects game."
        play sound sfx_hands_clap3
        scene sm1fs-i005-182 infected_office_full_cw_talk_handhead with dissolve
        play voice3 girl29_angry_breath noloop
        cw "*sighs*"
        scene sm1fs-i005-183 infected_office_full_am_talk with dissolve
        play voice5 girl27_surprised_oh1 noloop
        ag "Try to look on the bright side."
        ag "Thanks to Nari's system, we'll be able to track down who attacked Orbix in a much shorter time than if we didn't have her system."
        scene sm1fs-i005-184 infected_office_full_cw_talk_victory with dissolve
        play voice3 girl29_happy_phew noloop
        cw "Well thank god for that at least."
        scene sm1fs-i005-185 infected_office_full_cw_talk_nari with dissolve
        play voice3 girl29_hey_happy noloop
        cw "Good work, Ms. Song."
        scene sm1fs-i005-186 infected_office_full_ns_talk with dissolve
        play voice4 nari_yes_aga1 noloop
        ns "Thank you, Ms. Watts."
    else:
        scene sm1fs-i005-177 infected_office_full_cw_talk_look_ag with dissolve
        play voice3 girl29_arrogant_hm noloop
        cw "And at this point, we don't have any suspects."
        scene sm1fs-i005-187 infected_office_full_ag_talk_shake head with dissolve
        play voice4 girl27_no_simple1 noloop
        ag "Not yet."
        ag "But it's just a matter of time until Sienna or one of us can find a fix."
    scene sm1fs-i005-188 infected_office_full_cw_talk with dissolve
    play voice3 girl29_disappointed_mff noloop
    cw "Circling back around, you're saying that our current solution is not a long-term one?"
    scene sm1fs-i005-189 infected_office_full_am_talk_sarcastic with dissolve
    play voice5 girl22_thinking_oh noloop
    am "Oh yeah.{w} No, that will definitely stop the problem."
    scene sm1fs-i005-190 infected_office_full_cw_talk_really with dissolve
    play voice3 girl29_surprised_oh noloop
    cw "Really?"
    scene sm1fs-i005-191 infected_office_full_ag_talk with dissolve
    play voice4 girl27_no_short noloop
    ag "She's teasing you, Claire."
    play voice3 girl29_angry_dough noloop
    play sound sfx_throw_something1
    scene sm1fs-i005-192 infected_office_full_cw_talk_angry with hpunch
    cw "April!"
    scene sm1fs-i005-193 infected_office_full_am_talk_amused with dissolve
    play voice5 girl22_surprised_eh1 noloop
    am "I'm only human."
    scene sm1fs-i005-194 infected_office_full_cw_talk_howfix with dissolve
    play voice3 girl29_arrogant_he noloop
    cw "So then how do we fix this?"
    scene sm1fs-i005-195 infected_office_full_am_talk_drummingfingers with dissolve
    play voice5 girl22_thinking_eeh noloop
    am "Sienna is doing her best to bring back-up systems online so that our main functions can...{w} Function."
    scene sm1fs-i005-196 infected_office_full_ag_talk with dissolve
    play voice4 girl27_yes_aga noloop
    ag "April and I will begin sweeping through every line of code in the corrupted appendix."
    ag "Once that is done, then yes, it is possible to completely fix our systems."
    scene sm1fs-i005-197 infected_office_full_am_talk_chimesin with dissolve
    play voice5 girl22_yes_simple noloop
    am "But it will take time."
    am "And we're still make the new's website."
    am "Taking me off that means everything is delayed."
    scene sm1fs-i005-198 infected_office_full_cw_talk_no with dissolve
    play voice3 girl29_no_angry noloop
    cw "No.{w} Impossible.{w} That's not going to happen."
    cw "It would be a blackmark on the C.U.M Division for the whole quarter."
    scene sm1fs-i005-199 infected_office_full_cw_talk_anna with dissolve
    play voice3 girl29_hey_angry noloop
    cw "Anna. There has to be something we can do?"
    scene sm1fs-i005-200 infected_office_full_ag_talk with dissolve
    play voice4 girl27_yes_simple2 noloop
    ag "There is."
    ag "We do a code excisement."
    scene sm1fs-i005-201 infected_office_full_cw_talk_explanation with dissolve
    play voice3 girl29_arrogant_huh noloop
    cw "In English?"
    scene sm1fs-i005-202 infected_office_full_ag_talk_explaining with dissolve
    play voice4 girl27_thinking_emm5 noloop
    ag "Sienna and April can build up new firewalls and squeeze down the corrupted systems as much as possible."
    play sound sfx_cloth_rustling2
    scene sm1fs-i005-203 infected_office_full_ag_talk_leaning with dissolve
    play voice4 girl27_thinking_hmm noloop
    ag "If we're lucky, they can figure out the root code and burn out the corrupted data."
    play sound sfx_cloth_rustling1
    scene sm1fs-i005-204 infected_office_full_cw_talk_worried with dissolve
    play voice3 girl29_disgust_ergh noloop
    cw "What is plan B? What is the faster option."
    scene sm1fs-i005-205 infected_office_full_ag_talk_planb with dissolve
    play voice4 girl27_yes_yeah3 noloop
    ag "We can load up the backup systems."
    ag "But real talk? Without spending the time to find out the vulnerabilities and plugging them?"
    scene sm1fs-i005-206 infected_office_full_am_talk_impressed with dissolve
    play voice5 girl22_yes_yeah1 noloop
    am "We could get hacked all over again."
    scene sm1fs-i005-207 infected_office_full_cw_talk_surprised with dissolve
    play voice3 girl29_angry_kgh noloop
    cw "Do it. We don't have time for a delay."
    play voice5 girl22_yes_aga4 noloop
    am "Your funeral."
    scene sm1fs-i005-208 infected_office_full_ag_talk_pointmcnari with dissolve
    play voice4 girl27_thinking_hmm8 noloop
    ag "So Nari and [mcname]. You two just keep doing what you're doing."
    play voice2 mc_yes_okay1 noloop
    mc "Okay."
    play voice3 nari_yes_aga2 noloop
    ns "If you say so."
    scene sm1fs-i005-210 infected_office_full_ag_talk_awkward with dissolve
    play voice4 girl27_thinking_mmm noloop
    ag "But Ms. Watts. The moment we finish the website, we have to find the hole and plug it."
    scene sm1fs-i005-212 infected_office_full_am_talk_grinning with dissolve
    play voice4 girl22_yes_yep3 noloop
    am "Yeah. Or we'll be right back at square one."
    scene sm1fs-i005-213 infected_office_full_cw_talk_understanding with dissolve
    play voice3 girl29_yes_happy noloop
    cw "It's going to be fine.{w} Besides, we don't have a better option."
    $ renpy.music.set_volume(1.0, 3.0, "sound4" )
    play sound sfx_bed_slide2
    scene sm1fs-i005-214 infected_office_full_cw_talk_leaving with dissolve
    play voice3 girl29_hey_provocative noloop
    cw "We were already under pressure before."
    cw "Now we've lost an entire day and who knows what because of this hack."
    scene sm1fs-i005-215 infected_office_full_cw_talk_leaving with dissolve
    play voice3 girl29_thinking_hm noloop
    cw "Whatever it takes, we need to get the website project complete."
    play sound sfx_door_open2
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps1
    scene sm1fs-i005-216 infected_office_full_cw_talk_leaving with dissolve
    play voice3 girl29_no_uhuh noloop
    cw "Failure is not an option."
    stop sound4 fadeout 3.0
    play sound5 sfx_office_ambience1 fadein 1.5
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    play sound sfx_door_closed1
    scene sm1fs-i005-217 infected_office_full_am_talk_outsideroom with dissolve
    play voice5 girl22_thinking_hmm2 noloop
    am "You'll tell Sienna the plan?"
    scene sm1fs-i005-218 infected_office_full_ag_talk with dissolve
    play voice4 girl27_yes_confident noloop
    ag "Yes. And I presume you're going for a caffiene run?"
    scene sm1fs-i005-219 infected_office_full_am_talk_grinning with dissolve
    play voice5 girl22_arrogant_he noloop
    am "Rockets don't fly without fuel. I'll be back from the convenience store in thirty."
    scene sm1fs-i005-220 infected_office_full_ag_talk with dissolve
    play voice4 girl27_yes_ugu1 noloop
    ag "Pick me up a Thunderblast when you're there."
    scene sm1fs-i005-221 infected_office_full_am_talk_pause with dissolve
    play voice5 girl22_happy_mmm noloop
    pause
    scene sm1fs-i005-222 infected_office_full_am_talk_smiling with dissolve
    play voice5 girl22_yes_yeah4 noloop
    am "You got it."
    play sound sfx_heels_steps1 loop
    scene sm1fs-i005-223 infected_office_full_am_talk_walkout with dissolve
    pause
    play sound2 sfx_heels_steps2
    scene sm1fs-i005-224 infected_office_full_ag_talk_lead_mc_ns with dissolve
    play voice4 girl27_hey_serious noloop
    ag "[mcname]. Nari."
    play sound sfx_chair_slide1
    play sound2 sfx_chair_slide1 noloop
    scene sm1fs-i005-225 infected_office_full_ag_talk_mc_ns_sitting with dissolve
    play voice4 girl27_happy_relief3 noloop
    ag "I know this isn't what you signed up for."
    play sound sfx_keyboard_typing2
    scene sm1fs-i005-226 infected_office_full_ag_talk_narityping with dissolve
    play voice4 girl27_thinking_hmm4 noloop
    ag "But I am sure that the worst is over."
    scene sm1fs-i005-228 infected_office_full_ag_talk_epicpose with dissolve
    play voice4 girl27_angry_mmm noloop
    ag "So let's get back on our horses and make the C.U.M Division proud."
    play sound sfx_heels_steps1 loop
    scene sm1fs-i005-229 infected_office_full_ag_talk_walkaway with dissolve
    play voice4 girl27_yes_aga3 noloop
    ag "I'll send you updated code packets in twenty."
    play voice3 nari_sexphrase_yes1 noloop
    scene sm1fs-i005-230 infected_office_full_ns_talk_shout with hpunch
    ns "Yes, Ms. Goodwin!"
    scene sm1fs-i005-231 infected_office_full_ag_talk_smile with dissolve
    play voice4 girl27_happy_laugh6 noloop
    ag "Very good."
    stop sound fadeout 1.0
    jump sm1fs_i005_end
label sm1fs_i005_end:
    stop music fadeout 3.0
    stop sound5 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(IT_STORY_LINE, 2, 0, 2)
    return