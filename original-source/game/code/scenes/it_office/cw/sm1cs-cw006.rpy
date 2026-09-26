image sm1cs_cw006-a157-1 = Movie(play = "images/FS_IT/CW/s006/anim/sm1cs-cw006-a157-1-2x-50fps.webm", start_image = "sm1cs-cw006-a157-1 mc-licks-cw-anim-01")
image sm1cs_cw006-a157-1-f = Movie(play = "images/FS_IT/CW/s006/anim/sm1cs-cw006-a157-1-2x-60fps.webm", start_image = "sm1cs-cw006-a157-1 mc-licks-cw-anim-01")
image sm1cs_cw006-a157-2 = Movie(play = "images/FS_IT/CW/s006/anim/sm1cs-cw006-a157-2-2x-50fps.webm", start_image = "sm1cs-cw006-a157-2 mc-licks-cw-anim-01")
image sm1cs_cw006-a157-2-f = Movie(play = "images/FS_IT/CW/s006/anim/sm1cs-cw006-a157-2-2x-60fps.webm", start_image = "sm1cs-cw006-a157-2 mc-licks-cw-anim-01")
image sm1cs_cw006-a157-3 = Movie(play = "images/FS_IT/CW/s006/anim/sm1cs-cw006-a157-3-2x-50fps.webm", start_image = "sm1cs-cw006-a157-3 mc-licks-cw-anim-01")
image sm1cs_cw006-a157-3-f = Movie(play = "images/FS_IT/CW/s006/anim/sm1cs-cw006-a157-3-2x-60fps.webm", start_image = "sm1cs-cw006-a157-3 mc-licks-cw-anim-01")
image sm1cs_cw006-a157-4 = Movie(play = "images/FS_IT/CW/s006/anim/sm1cs-cw006-a157-4-2x-50fps.webm", start_image = "sm1cs-cw006-a157-4 mc-licks-cw-anim-01")
image sm1cs_cw006-a157-4-f = Movie(play = "images/FS_IT/CW/s006/anim/sm1cs-cw006-a157-4-2x-60fps.webm", start_image = "sm1cs-cw006-a157-4 mc-licks-cw-anim-01")
label sm1cs_cw006:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music music_youarehired volume 0.85
    play sound4 sfx_office_ambience1 fadein 1.0
    scene sm1cs-cw006-01 mc-working-office_c1 with dissolve
    pause
    play sound sfx_heels_steps1 loop
    scene sm1cs-cw006-02 cw-approach-mc-workstation_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.45, 1.0, "sound" )
    scene sm1cs-cw006-03 am-notices-cw-coming-over_c1 with dissolve
    pause
    scene sm1cs-cw006-04 am-focused-on-work-speaks-bad-news-coming-in_c1 with dissolve
    play voice4 girl22_disappointed_ehh2 noloop
    am "Bad news. Coming in."
    scene sm1cs-cw006-05 mc-look-over-claire-hmm_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Hmmm."
    scene sm1cs-cw006-06 am-what-do-this-time-mc-relax-nothing_c1 with dissolve
    play voice4 girl22_surprised_huh1 noloop
    am "What did you do this time, [mcname]?"
    play voice2 mc_disappointed_ehh5 noloop
    mc "Nothing."
    scene sm1cs-cw006-07 am-smiles-fine-dont-tell-me_c1 with dissolve
    play voice4 girl22_yes_aga1 noloop
    am "Sure. Don't tell me."
    $ renpy.music.set_volume(1.0, 1.5, "sound" )
    scene sm1cs-cw006-08 cw-arrives-desk-mryoung-mc-mswatts_c1 with dissolve
    play voice3 girl29_hey_angry noloop
    cw "Mr. Young."
    play voice2 mc_yes_aga1 noloop
    mc "Ms. Watts."
    stop sound fadeout 1.0
    scene sm1cs-cw006-09 cw-talking-follow-me-conference-room_c1 with dissolve
    play voice3 girl29_thinking_mmm2 noloop
    cw "Come with me to the conference room."
    scene sm1cs-cw006-10 am-there-meeting-dont-know-come-too_c1 with dissolve
    play voice4 girl22_surprised_eh2 noloop
    am "Is there a meeting I forgot about?"
    am "I'll come too."
    scene sm1cs-cw006-11 cw-surprised-ah-ms-mercer_c1 with dissolve
    play voice3 girl29_surprised_ehh noloop
    cw "Ah. Ms. Mercer."
    scene sm1cs-cw006-12 cw-nothing-like-that-just-need_c1 with dissolve
    play voice3 girl29_no_questioning noloop
    cw "Oh no. Nothing like that."
    cw "I just need..."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw006-13 cw-need-help-phone_c1 with dissolve
    play voice3 girl29_disappointed_oh noloop
    cw "A little technical help with my phone."
    play sound sfx_chair_slide1
    scene sm1cs-cw006-14 am-stands-can-give-crack-cw-no-mean-no-need_c1 with dissolve
    play voice4 girl22_yes_yeah4 noloop
    am "I can give it a crack, Claire."
    scene sm1cs-cw006-15 cw-sure-can-handle-it_c1 with dissolve
    play voice3 girl29_no_active noloop
    cw "No.{w} I mean. Thank you."
    cw "But I'm sure we can handle it."
    play sound sfx_cloth_rustling3
    scene sm1cs-cw006-16 am-sits-down-whatever-sure-mc-likely-brick-it_c1 with dissolve
    play voice4 girl22_disappointed_geh noloop
    am "Whatever."
    am "But I'm sure [mcname] is just as likely to fix your phone as to brick it."
    scene sm1cs-cw006-17 mc-thanks-am-welcome_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Thanks."
    play voice3 girl22_yes_yeah3 noloop
    am "You're welcome."
    scene sm1cs-cw006-18 cw-nods-towards-conference-room_c1 with dissolve
    pause
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-cw006-19 mc-follows-up-cw-towards-conference_c1 with dissolve
    pause
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    scene sm1cs-cw006-20 am-looks-bored-looing-them-walk-away_c1 with dissolve
    pause
    play sound sfx_straw_drink5 volume 1.4
    scene sm1cs-cw006-21 mc-takes-sip-big-gulp_c1 with dissolve
    am "*noisy slurping*"
    play sound2 sfx_door_open1 noloop
    stop sound fadeout 1.5
    play sound3 sfx_heels_steps1
    stop sound4 fadeout 3.0
    scene sm1cs-cw006-22 cw-mc-enter-conference-room_c1 with dissolve
    pause
    scene sm1cs-cw006-23 cw-sighs-seems-only-yesterday-second-interview_c1 with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "*sighs* Seems like only yesterday I was doing your second interview here."
    stop sound3 fadeout 1.0
    play sound sfx_door_closed2
    scene sm1cs-cw006-24 cw-hope-working-orbix-been-your-liking_c1 with dissolve
    play voice3 girl29_thinking_mmm1 noloop
    cw "I hope working at Orbix has been to your liking, [mcname]."
    scene sm1cs-cw006-25 mc-choice-menu-screen_c1 with dissolve
    menu:
        "It has its perks":
            $ player.set_choice("sm1ms_cw006_has_perks")
            $ CharacterController.get_character("cw").add_point(1)
            scene sm1cs-cw006-26 choice-perks-mc-nice-look-has-perks-always-curious-what-happens-next_c1 with dissolve
            play voice2 d9s2_yeah noloop volume 1.7
            mc "It has its perks."
            mc "I'm always curious what will happen next."
        "Yes, I have enjoyed it":
            $ player.set_choice("sm1ms_cw006_enjoyed")
            scene sm1cs-cw006-27 choice-enjoyed-mc-oh-yes-beed-the-right-job_c1 with dissolve
            play voice2 mc_yes_yes7 noloop
            mc "Oh yes, I have enjoyed it."
            mc "I think it's been the right job at the right time for me."
            scene sm1cs-cw006-28 mc-hope-performance-good-cw-oh-would-know_c1 with dissolve
            mc "I hope my performance has been good."
            play voice3 girl29_thinking_oh noloop
            cw "Oh, you would know if your performance for the company has been {b}lacking{/b}."
        "It's about what I expected":
            $ player.set_choice("sm1ms_cw006_expected")
            $ CharacterController.get_character("cw").deduct_point(1)
            scene sm1cs-cw006-29 choice-expected-mc-yeah-what-expected-cw-hm-nothing-impressed-you_c1 with dissolve
            play voice2 mc_yes_yeah3 noloop
            mc "Yeah it's about what I expected it to be."
            play voice3 girl29_thinking_hmm2 noloop
            cw "Hmmm. So nothing about it has really impressed you?"
            play sound sfx_hair_scratch1
            scene sm1cs-cw006-30 mc-not-really-mean-not-yet_c1 with dissolve
            play voice2 mc_no_no2 noloop
            mc "Not really."
            mc "I mean, at least not yet."
            scene sm1cs-cw006-31 cw-silently-stares-mc-he-uncomfortable_c1 with dissolve
            pause
    play sound sfx_bed_slide3 volume 0.7
    scene sm1cs-cw006-32 cw-sits-down-should-get-point-mc-sure_c1 with dissolve
    play voice3 girl29_thinking_hmm3 noloop
    cw "I suppose I should get to the point of why I brought you in."
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    play sound sfx_bed_slide2
    scene sm1cs-cw006-33 cw-afraid-bad-news-mc-you-fired_c1 with dissolve
    play voice3 girl29_thinking_hmm5 noloop
    cw "I'm afraid I have bad news."
    cw "{b}You're fired{/b}."
    scene sm1cs-cw006-34 mc-shocked-whaat_c1 with dissolve
    play voice2 mc_surprised_what8 noloop
    mc "What?"
    scene sm1cs-cw006-35 cw-smiling-relax-fired-from-fake-boyfriend_c1 with dissolve
    play voice3 girl29_no_nah noloop
    cw "Relax. I should have been clearer."
    cw "You are fired from being my fake boyfriend."
    scene sm1cs-cw006-36 mc-relaxes-oh-sheesh_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Oh.{w} Sheesh."
    scene sm1cs-cw006-37 cw-enjoying-haha-sorry-couldnt-resist-mc-it-fine_c1 with dissolve
    play voice3 girl29_happy_laugh1 noloop
    cw "Hahaha. Sorry. I couldn't resist."
    scene sm1cs-cw006-38 mc-will-send-for-his-things_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "It's fine."
    mc "Well, it was interesting. I'll send for my things."
    scene sm1cs-cw006-39 cw-smiling-haha-cute-now-officially-breakup-right-moment_c1 with dissolve
    play voice3 girl29_happy_laugh2 noloop
    cw "Haha. Cute."
    cw "Now officially, our breakup won't go into effect until the right time."
    scene sm1cs-cw006-40 cw-tapping-finger-table-maybe-next-season-if-find-right-spot_c1 with dissolve
    play voice3 girl29_thinking_hmm4 noloop
    cw "Maybe in the new season."
    cw "I'm going to go to the park, then my allergies will give me the perfect not-so-fake tears to really sell the breakup to my parents."
    scene sm1cs-cw006-41 mc-impressed-sounds-thought-through_c1 with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Sounds like you've thought this all out."
    scene sm1cs-cw006-42 cw-worried-silent-yes-also-right-decision_c1 with dissolve
    cw "..."
    play voice3 girl29_yes_serious noloop
    cw "Yes.{w} And it is the right decision."
    scene sm1cs-cw006-43 least-best-decision-at-hand_c1 with dissolve
    play voice3 girl29_thinking_hm noloop
    cw "Or at least the best decision with the problem at hand."
    play sound sfx_cloth_rustling1
    scene sm1cs-cw006-44 mc-have-ask-did-something-wrong-trip_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I have to ask..."
    mc "Did I do something wrong on the trip?"
    scene sm1cs-cw006-45 cw-how-can-ask-put-position-twice_c1 with dissolve
    play voice3 girl29_arrogant_huh noloop
    cw "How can you ask me that after the {i}position{/i} you put me in on the boat."
    play voice3 girl29_angry_dough noloop
    scene sm1cs-cw006-45 cw-how-can-ask-put-position-twice_c1 with hpunch
    cw "Twice?"
    scene sm1cs-cw006-46 mc-choice-menu-screen_c1 with dissolve
    menu:
        "You didn't mind":
            $ player.set_choice("sm1ms_cw006_didnt_mind")
            scene sm1cs-cw006-47 choice-didnt-mind-mc-grin-you-really-seem-not-mind_c1 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "{i}You{/i} didn't really seem to mind it that much."
            scene sm1cs-cw006-49 cw-lying-was-just-pretending-for-parents_c1 with dissolve
            play voice3 girl29_disappointed_mff noloop
            cw "Oh I was just putting on a good show..."
            cw "For my {b}parents{/b}."
            scene sm1cs-cw006-50 mc-not-believing-mct-riiight_c1 with dissolve
            play voice2 mc_thinking_mmm6 noloop
            mct "{b}Riiiiiigggghhhhtt{/b}."
        "Apologize to Claire":
            $ player.set_choice("sm1ms_cw006_apologize")
            $ CharacterController.get_character("cw").add_point(2)
            play sound sfx_cloth_rustling2
            scene sm1cs-cw006-51 choice-apologize-mc-sorry-about-that-claire-was-first-time_c1 with dissolve
            play voice2 d2s9_confused noloop volume 1.7
            mc "I am sorry about that, Claire."
            mc "It was my first time being a fake boyfriend."
            scene sm1cs-cw006-52 mc-guess-out-depth-cw-i-know_c1 with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.7
            mc "I guess I was a little out of my depth."
            play voice3 girl29_yes_aga1 noloop
            cw "I know, [mcname]."
            scene sm1cs-cw006-53 cw-certainly-share-some-blame-wouldnt-be-in-position_c1 with dissolve
            play voice3 girl29_arrogant_he noloop
            cw "I'm not blaming you for anything. It was my idea."
            cw "You would never have had to play the role so {b}physically{/b}..."
            scene sm1cs-cw006-54 cw-back-normal-mean-didnt-put-there_c1 with dissolve
            play voice3 girl29_thinking_mmm2 noloop
            cw "If I didn't need you help in the first place..."
        "I was just playing the role":
            $ player.set_choice("sm1ms_cw006_playing_role")
            play sound sfx_cloth_rustling2
            scene sm1cs-cw006-55 choice-playing-role-mc-just-playing-role-you-gave-cw-yes-well_c1 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "I was just playing the role you put me in."
            play voice3 girl29_yes_arrogant noloop
            cw "Yes. Well, your... {b}unit{/b}... seemed to be overly excited with it."
            scene sm1cs-cw006-56 mc-coder-not-actor-can-only-control-body_c1 with dissolve
            play voice2 mc_thinking_hmm1 noloop
            mc "My unit?"
            mc "Oh you mean my dick."
            cw "*gasps*"
            mc "I can only control my body so much, Claire.."
            scene sm1cs-cw006-57 cw-raises-hand-stop_c1 with hpunch
            play voice3 girl29_angry_breath noloop
            cw "Stop."
            scene sm1cs-cw006-58 cw-yout-right-you-reacting-there-only_c1 with dissolve
            play voice3 girl29_yes_aga2 noloop
            cw "You're right, [mcname]."
            cw "You were only there... reacting like...{w} {i}That{/i}..."
            scene sm1cs-cw006-59 cw-because-of-me_c1 with dissolve
            play voice3 girl34_disappointed_mmf4 noloop
            cw "Because of me..."
    play sound sfx_cloth_rustling3
    scene sm1cs-cw006-60 cw-leans-back-breathes-heavily_c1 with dissolve
    play voice3 stacy_smell noloop
    cw "*breathing deeply*"
    scene sm1cs-cw006-61 cw-talking-any-case-falsehood-behind-cw-any-your-shortcommings-outweighted_c1 with dissolve
    play voice3 girl29_happy_relief noloop
    cw "In any case, the falsehood is behind us."
    cw "And any of your shortcomings during the trip were outweighed by the assistance you gave me."
    cw "My parents will be satisfied that I'm... {w}open to settling down with someone."
    scene sm1cs-cw006-62 cw-you-credit-orbix-many-men-take-lesson_c1 with dissolve
    play voice3 girl34_thinking_hmm6 noloop
    cw "You are a credit to Orbix, [mcname]."
    cw "And many men could take a lesson from you."
    scene sm1cs-cw006-64 cw-if-lindt-ask-about-talk-me-mc-sure_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "People always say I'm in a league of my own."
    play voice3 girl29_arrogant_ha noloop
    cw "I've added a special note of appreciation to your file here at Orbix."
    scene sm1cs-cw006-63 cw-added-note-orbix-file-mc-alright_c1 with dissolve
    cw "If Ms. Lindt asked about it, just tell her to talk to me."
    play voice2 mc_yes_ugu1 noloop
    mc "Sure."
    scene sm1cs-cw006-65 cw-do-have-any-other-questions_c1 with dissolve
    play voice3 girl34_thinking_hmm7 noloop
    cw "Do you have any other questions, or shall I consider this matter closed and behind us?"
    scene sm1cs-cw006-66 mc-umm-need-help-stage-breakup_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Ummm. So, will you need my help to stage the breakup? Or anything like that?"
    scene sm1cs-cw006-67 cw-neutral-talking-no-thought-about-that_c1 with dissolve
    play voice3 girl29_no_nope noloop
    cw "No. I thought about that."
    cw "And I decided that I will just call my parents and start with the aftermath."
    scene sm1cs-cw006-68 cw-thought-decided-call-parent-aftermath-mc-you-make-sure-dad-not-shoot_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "And you'll help make sure your dad doesn't shoot me after you break the news."
    scene sm1cs-cw006-69 cw-ofc-i-breaker-you-breakee-had-end-number-reasons_c1 with dissolve
    play voice3 girl29_yes_aga3 noloop
    cw "Of course. I will be the breaker and you will be the breakee."
    cw "I'll just tell them that I had to end it with you for a number of reasons."
    cw "Including the fact that we work together, I think that will be a solid foundation to build a convincing argument."
    scene sm1cs-cw006-70 cw-including-work-together-mc-been-thinking-this_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "You've been thinking about this."
    scene sm1cs-cw006-71 cw-grins-yes-even-practiced-tears_c1 with dissolve
    play voice3 girl29_yes_happy noloop
    cw "Yes. I've even been practicing my tears."
    play sound sfx_cloth_rustling5
    scene sm1cs-cw006-72 cw-acting-crying-sniffing-just-not-meant-be-he-made-happy-not-work_c1 with dissolve
    play voice3 girl29_pain_sobs2 noloop
    cw "*sniff* It just wasn't meant to be."
    cw "*sniff* He made me happy, but it just couldn't work."
    scene sm1cs-cw006-73 mc-very-convincing_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Very convincing."
    scene sm1cs-cw006-74 mc-frowning-little-manipulative_c1 with dissolve
    play voice2 mc_angry_oof noloop
    mc "And a little manipulative."
    scene sm1cs-cw006-75 cw-sighs-bold-but-astute_c1 with dissolve
    play voice3 girl34_angry_breath1 noloop
    cw "*sighs* Bold, but astute."
    play sound sfx_cloth_rustling1
    scene sm1cs-cw006-76 mc-neutral-brings-hands-together-wish-there-another-option_c1 with dissolve
    play voice3 girl29_thinking_hmm5 noloop
    cw "I wish there were another option, but I have made up my mind about this."
    scene sm1cs-cw006-77 mc-choice-menu-screen_c1 with dissolve
    label cw006_choice1:
    menu:
        "I'm kind of interested in continuing":
            jump sm1cs_cw006_continue_relationship
        "Let things end with Claire":
            $ player.set_choice("sm1ms_cw006_offramp_1")
            $ player.set_choice("sm1ms_cw006_selected_offramp_1")
            scene sm1cs-cw006-78 choice-end-things-mc-well-fun-while-lasted-but-right_c1 with dissolve
            play voice2 mc_thinking_hmm4 noloop
            mc "Well, it was pretty fun while it lasted."
            mc "But you're right. The smart thing to do is put an end to this."
            mc "So things don't get messy."
            scene sm1cs-cw006-79 mc-things-not-get-messy_c1 with dissolve
            play voice3 girl34_angry_hmf noloop
            cw "I couldn't agree with you more, [mcname]."
            play sound sfx_bed_slide2
            scene sm1cs-cw006-80 cw-stands-up-offers-hand-appriciate-time-attention_c1 with dissolve
            play voice3 girl29_yes_yeah noloop
            cw "I really appreciate your time today, and your attention."
            play sound sfx_hands_clap2
            scene sm1cs-cw006-81 mc-shakes-hand-ofc-claire_c1 with dissolve
            play voice2 mc_yes_yes2 noloop
            mc "Of course, Ms. Claire."
            scene sm1cs-cw006-82 mc-akward-should-get-back-work-cw-naturally_c1 with dissolve
            play voice2 mc_thinking_hmm7 noloop
            mc "I should get back to my seat."
            play voice3 girl29_yes_questioning noloop
            cw "Naturally."
            play sound sfx_heels_steps2
            scene sm1cs-cw006-83 mc-walks-away-end-scene_c1 with dissolve
            pause
            jump sm1cs_cw006_break_up
label sm1cs_cw006_continue_relationship:
    scene sm1cs-cw006-84 cw-pretends-dissapointed-obv-even-if-curious-afraid-out-question_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "What about the option where we just keep seeing each other?"
label sm1cs_cw006_onramp_1a:
    play voice3 girl29_thinking_hmm4 noloop
    cw "Well, obviously, even if I was... {i}curious{/i}... to see how we would work together as an actual couple."
    cw "I am afraid that is out of the question."
    scene sm1cs-cw006-85 mc-bummed-mct-feels-like-cant-convince-this-sucks_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.6
    mct "Feels like I can't convince her to change her mind on that."
    mct "This sucks."
    play sound sfx_bed_slide2
    scene sm1cs-cw006-86 cw-acting-corpo-see-disappointment-witness_c1 with dissolve
    play voice3 girl29_hey_happy noloop
    cw "I see your disappointment, and I witness it."
    cw "But... there was one other thing I wanted to mention."
    scene sm1cs-cw006-87 cw-one-other-thing-mention-mc-yeah-what-that_c1 with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Yeah. What is that?"
    play sound sfx_cloth_rustling2
    scene sm1cs-cw006-88 cw-considering-special-assignmnet-mr-young_c1 with dissolve
    play voice3 girl34_arrogant_huh1 noloop
    cw "I was considering putting you on a {i}special{/i} assignment."
    cw "Mr. Young..."
    cw "Both..."
    scene sm1cs-cw006-89 cw-both-times-think-clearly-post-phase_c1 with dissolve
    play voice3 girl29_pain_cough1 noloop
    cw "*clears throat* Both times that we {b}played{/b} our role on the yacht, I was able to think more clearly in the..."
    scene sm1cs-cw006-90 cw-being-around-helps-workflow-prefer-analyzing_c1 with dissolve
    play voice3 girl29_thinking_hmm3 noloop
    cw "{i}Post{/i} phase."
    cw "Being around you...{w} appears to help with my workflow."
    cw "I think a little further analysis would be good.{w} Neccesary even."
    play sound sfx_cloth_rustling1
    scene sm1cs-cw006-91 cw-increse-focus-after-related-something-else-but-if-not_c1 with dissolve
    play voice3 girl29_yes_aga2 noloop
    cw "The increase in my focus after... our play time, is certainly related to something else."
    cw "But... if it's not."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw006-92 cw-like-said-special-assignment-probation-ofc_c1 with dissolve
    play voice3 girl34_arrogant_hm2 noloop
    cw "Like I said, I'm willing to engage you in a special assignment."
    cw "On a purely probationary, of course."
    scene sm1cs-cw006-93 mc-not-sure-what-saying-claire-cw-ms-watts-here_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "I'm not quite sure what you're saying, Claire."
    play voice3 girl29_angry_hmf noloop
    play sound sfx_cloth_planket2
    scene sm1cs-cw006-94 mc-right-still-not-sure-cw-coming-weeks-help-details-project_c1 with hpunch
    cw "Ms. Watts. {i}Here{/i}."
    play voice2 mc_yes_yeah1 noloop
    mc "Right. I'm not sure what you are saying, Ms. Watts."
    cw "In the weeks ahead, I may be calling on you to help me out with some technical details about a project I am working on."
    cw "And by helping me out, I mean I'd need you help with activities vaguely similar to the ones we {i}completed{/i} on the yacht."
    mc "Huh?"
    play voice2 mc_scared_oh4 noloop
    scene sm1cs-cw006-94 mc-right-still-not-sure-cw-coming-weeks-help-details-project_c1 with hpunch
    mc "Oooooohhhh."
    scene sm1cs-cw006-95 cw-if-agree-this-proejct-only-us-not-sahre-any-details_c1 with dissolve
    mct "I can't believe it.{w} Claire is asking me to be like her..."
    mct "Secret work sex buddy?"
    play voice3 girl29_thinking_hm noloop
    cw "If you agree, then the project would be limited to just the two of us."
    cw "You would be required to never share any details with anyone in the office."
    scene sm1cs-cw006-96 mc-still-dumb-not-even-hr_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Not even HR?"
    scene sm1cs-cw006-97 cw-especially-not-hr-if-continue-will-make-arrangements_c1 with dissolve
    play voice3 girl34_angry_ahem1 noloop
    cw "Especially not HR."
    cw "Ahem. I mean, if this special project continues for an extended time, I will make the correct arrangements with HR."
    scene sm1cs-cw006-98 cw-already-printed-all-docs-but-can-trust-her_c1 with dissolve
    play voice3 girl29_thinking_hmm2 noloop
    cw "I've actually already printed out all the documents, so we can adjust as necessary."
    cw "But you can trust that I won't use this against you for any kind of dismissal event, [mcname]."
    scene sm1cs-cw006-99 mc-sure-choice-menu-screen_c1 with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Sure."
    menu:
        "Believe her":
            $ player.set_choice("sm1ms_cw006_believe_her")
            scene sm1cs-cw006-100 choice-believe-her-mct-sounds-claire-wants-what-got_c1 with dissolve
            play voice2 mc_thinking_hmm9 noloop
            mct "It sounds like Claire wants what I've got."
            mct "And it's not like she fired me after the lunch date, or the trip."
            mct "So I feel like she's being genuine."
        "Don't believe her":
            scene sm1cs-cw006-101 choice-not-believe-mct-she-says-that-now_c1 with dissolve
            play voice2 mc_thinking_hmm3 noloop
            mct "She says this now, but what happens if in two weeks from now, she changes her mind?"
            mct "She could get rid of me like that."
            mct "I need to think about this. Hard."
    play sound sfx_bed_slide3 volume 0.6
    scene sm1cs-cw006-102 mc-can-speak-plainly-cw-what-is-ti-you-expect-me_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Can we talk plainly, Ms. Watts?"
    mc "What is it you expect of me?"
    scene sm1cs-cw006-103 cw-explaining-would-work-close-project-first-task-involve-using-mouth_c1 with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "Well, we would be working very closely together on this project."
    cw "One of the first tasks, a test really, would involve you using that handsome mouth of yours."
    scene sm1cs-cw006-104 cw-horny-to-interface-body-specific-part-can-guess-which_c1 with dissolve
    play voice3 girl29_arrogant_he noloop
    cw "To... interface with my {i}body{/i}. One specific part of my body."
    cw "I wonder if you can guess which part?"
    scene sm1cs-cw006-105 mc-choice-menu-screen_c1 with dissolve
    menu:
        "You're lips?":
            $ player.set_choice("sm1ms_cw006_cw_lips")
            play sound sfx_cloth_rustling2
            scene sm1cs-cw006-106 choice-lips-mc-unsure-your-lips_c1 with dissolve
            play voice2 mc_arrogant_huh3 noloop
            mc "Your lips?"
            scene sm1cs-cw006-107 cw-in-manner-speaking-yes-lower-lips_c1 with dissolve
            play voice3 girl34_disappointed_mmf4 noloop
            cw "In a manner of speaking."
            cw "I was thinking my {i}lower{/i} lips."
            scene sm1cs-cw006-108 mc-shocked-your-you-want-pussy-eaten_c1 with dissolve
            play voice2 mc_angry_huh2 noloop
            mc "Your..."
            mc "Your pussy.{w} You want me to eat your pussy."
        "Your ass?":
            $ player.set_choice("sm1ms_cw006_cw_ass")
            scene sm1cs-cw006-109 choice-ass-mc-lick-ass_c1 with dissolve
            play voice2 mc_thinking_hmm6 noloop
            mc "You want me to lick your asshole?"
            play sound sfx_throw_something1
            scene sm1cs-cw006-110 cw-surprsied-what-no-ofc_c1 with hpunch
            play voice3 girl29_scared_ah4 noloop
            cw "What? No."
            scene sm1cs-cw006-111 cw-laughing-that-so-dirty-surch-bad-boy_c1 with dissolve
            play voice3 girl29_happy_laugh3 noloop
            cw "That's so dirty, [mcname]."
            cw "You're such a bad boy."
            scene sm1cs-cw006-112 cw-no-want-eat-pussy_c1 with dissolve
            play voice3 girl29_no_simple noloop
            cw "No... I want you to eat my pussy."
        "Your pussy?":
            $ player.set_choice("sm1ms_cw006_cw_pussy")
            play sound sfx_cloth_rustling2
            scene sm1cs-cw006-113 choice-pussy-mc-want-me-eat-pussy_c1 with dissolve
            play voice2 mc_arrogant_heh2 noloop
            mc "You want me to eat your pussy."
            scene sm1cs-cw006-114 cw-excellent-deduction_c1 with dissolve
            play voice3 girl29_yes_yep noloop
            cw "Excellent deduction, [mcname]."
    play sound sfx_heels_steps2
    scene sm1cs-cw006-115 cw-mmm-only-question-do-what-ask_c1 with dissolve
    play voice3 girl34_arrogant_hm3 noloop
    cw "Mmmm. Yes.{w} The only question is..."
    cw "Will you do what I ask?"
    play sound sfx_cloth_rustling4
    scene sm1cs-cw006-116 cw-sits-back-down-want-make-feel-good_c1 with dissolve
    play voice3 girl29_thinking_mmm1 noloop
    cw "I want you to make me feel {b}good{/b}."
    scene sm1cs-cw006-117 cw-mc-eyes-shock-mct-am-in-dream_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Am I in a dream?"
    scene sm1cs-cw006-118 zoom-out-mc-face-mct-did-run-over-by-claire-in-conference-room_c1 with dissolve
    play voice2 mc_angry_huh1 noloop
    mct "Did I get run over by Claire and now I'm in a fever dream state where it just seems like she is asking me to munch on her pussy?!"
    mct "In the office conference room!"
    scene sm1cs-cw006-119 mc-looking-claire-this-this-trick-right_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "This is..."
    mc "... A trick, right?"
    play sound sfx_cloth_rustling1
    scene sm1cs-cw006-120 mc-holding-arm-this-some-kind-joke-yes_c1 with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Some kind of joke?"
    scene sm1cs-cw006-121 cw-dead-serious-dont-joke-about-oral-sex_c1 with dissolve
    play voice3 girl29_no_nonono noloop
    cw "I don't joke about oral sex."
    scene sm1cs-cw006-122 cw-prefer-simple-clean-when-desire-someone-eager_c1 with dissolve
    play voice3 girl29_arrogant_hm noloop
    cw "I prefer a simple, clean operation."
    cw "When I desire it, and there is someone eager to give it to me, I ask for it."
    scene sm1cs-cw006-123 cw-expression-focus-repeats-simple-clean_c1 with dissolve
    play voice3 girl29_yes_aga1 noloop
    cw "Simple... and clean."
    play sound sfx_cloth_rustling3
    scene sm1cs-cw006-124 mc-smirking-and-very-dirty_c1 with dissolve
    play voice2 mc_angry_errr7 noloop
    mct "And very fucking kinky."
    scene sm1cs-cw006-125 cw-leans-towards-mc-thought-long-time-want-see-how-do_c1 with dissolve
    play voice3 girl29_angry_breath noloop
    cw "I thought about this for a long time before breathing a single word of it to you, [mcname]."
    cw "I want to see how you do as..."
    scene sm1cs-cw006-126 cw-close-up-good-boy_c1 with dissolve
    play voice3 girl24_sex_closedmoan1 noloop
    cw "A good boy."
    scene sm1cs-cw006-127 focus-lips-cw-my-good-boy_c1 with dissolve
    play voice3 girl24_sex_closedmoan3 noloop
    cw "{b}My{/b} good boy..."
    scene sm1cs-cw006-128 mc-silent-thinking-things-through_c1 with dissolve
    mc "..."
    scene sm1cs-cw006-129 cw-back-workmode-this-be-too-much-basic-point-not-central-point_c1 with dissolve
    play voice3 girl29_surprised_ehh noloop
    cw "Now, this may be too much for you, and I could understand if you are not open to this."
    cw "But the basic point, no, the central point...{w} is that I am interested in you doing more physical things with me."
    scene sm1cs-cw006-130 mc-choice-menu-screen_c1 with dissolve
label sm1cs_cw006_choice_2:
    menu:
        "Agree to try out Claire's special assignment":
            jump sm1cs_cw006_eat_pussy
        "Do not do Claire's special assignment":
            $ player.set_choice("sm1ms_cw006_offramp_2")
            $ player.set_choice("sm1ms_cw006_selected_offramp_2")
            play sound sfx_cloth_rustling1
            scene sm1cs-cw006-131 choice-no-mc-thanks-cant-do-that-life-complicated_c1 with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "Thank you, Ms. Watts, but I can't do that."
            mc "My life is very complicated as it is."
            scene sm1cs-cw006-132 mc-sorry-let-down_c1 with dissolve
            play voice2 mc_disgust_meh3 noloop
            mc "I'm sorry to let you down."
            scene sm1cs-cw006-133 cw-professional-no-need-appologize-mryoung_c1 with dissolve
            play voice3 girl29_no_questioning noloop
            cw "No need to apologize, Mr. Young."
            play sound sfx_cloth_rustling2
            scene sm1cs-cw006-143 cw-checking-phone-completely-understand-thanks-being-professional_c1 with dissolve
            play voice3 girl34_thinking_hmm7 noloop
            cw "I completely understand."
            cw "Thank you being professional and understanding about this."
            play sound sfx_bed_slide2
            scene sm1cs-cw006-144 cw-offers-hand-mc-silent_c1 with dissolve
            mc "..."
            play sound sfx_hands_clap2
            scene sm1cs-cw006-145 mc-shakes-hand-ofcourse_c1 with dissolve
            play voice2 mc_yes_yes2 noloop
            mc "Of course."
            play sound [sfx_phone_tapping1, sfx_phone_tapping1, sfx_phone_tapping1, sfx_phone_tapping1]
            scene sm1cs-cw006-146 cw-again-on-phone-can-go-end-scene_c1 with dissolve
            play voice3 girl29_hey_bye1 noloop
            cw "Very good. You can return to your desk now."
            jump sm1cs_cw006_break_up
label sm1cs_cw006_eat_pussy:
    play sound sfx_cloth_rustling1
    scene sm1cs-cw006-147 choice-agree-mc-will-take-assignment-all-perks_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I'll take the assignment."
    mc "And all the perks it comes with."
    scene sm1cs-cw006-148 mc-rubbing-jaw-will-there-perks_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "There are perks aren't there?"
    scene sm1cs-cw006-149 cw-opens-legs-oh-yes-many-perks_c1 with dissolve
    play voice3 girl29_surprised_oh noloop
    cw "Oh yes.{w} Many perks..."
    cw "Now, your boss."
    cw "Ahem... your partner has put in a specific request."
    scene sm1cs-cw006-150 cw-wont-help-dont-make-beg-again_c1 with dissolve
    play voice3 girl24_sex_closedmoan4 noloop
    cw "Won't you help me?{w} Please don't make me ask twice."
    scene sm1cs-cw006-151 mc-looking-away-cw-we-clear-if-move-quickly_c1 with dissolve
    play voice3 girl29_thinking_hmm4 noloop
    cw "We're in the clear."
    cw "If you move quickly."
    scene sm1cs-cw006-152 mct-fck-me-hundred-way-can-go-but-claire-needs-me_c1 with dissolve
    play voice2 d1s5_orgasm noloop
    mct "Fuck me. There are a hundred ways this can go bad."
    mct "No not bad.{w} Grade-A Terrible!"
    mct "But... Claire needs me."
    stop music fadeout 3.0
    scene sm1cs-cw006-153 mct-need-lick-taste-fuck-it_c1 with dissolve
    queue music beat_one_extended
    play voice2 mc_thinking_mmm7 noloop
    mct "Needs me to lick her. To taste her."
    mct "Fuck it!"
    play sound sfx_cloth_rustling3
    scene sm1cs-cw006-154 mc-crawls-under-table_c1 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1cs-cw006-155 mc-takes-off-cw-pantyhose_c1 with dissolve
    play voice2 mc_angry_errr8 noloop
    mct "Here goes nothing."
    play sound sfx_underpants_off1 volume 1.6
    scene sm1cs-cw006-156 mc-moves-panties-aside_c1 with dissolve
    pause
    scene sm1cs-cw006-a157-1 mc-licks-cw-anim-01 with dissolve
    pause 0.01
    scene sm1cs_cw006-a157-1
    play voisex2 mc_sex_closedmoans1
    play sound mc_sex_sucking_slow1 loop
    play voisex3 girl24_sex_openmoans3
    cw "Mmmmm. Not too hard."
    cw "We... nuah... We are both performing here."
    pause
    scene sm1cs_cw006-a157-2 with dissolve
    cw "Oh yes..."
    cw "That is..."
    cw "My... you certainly know your stuff, [mcname]."
    pause
    scene sm1cs_cw006-a157-3 with dissolve
    cw "You can go harder."
    mct "She's getting so wet."
    cw "Yes."
    pause
    scene sm1cs_cw006-a157-4 with dissolve
    cw "Right there."
    cw "I didn't realize how much I needed this."
    pause
    scene sm1cs_cw006-a157-1-f with dissolve
    mct "This taste. I could eat Claire up all day."
    cw "Yes... *moaning* Keep going."
    pause
    scene sm1cs_cw006-a157-2-f with dissolve
    cw "Oh fuck. Jesus. Oh no."
    cw "This... huaah... nuraah... this is a bad idea."
    pause
    scene sm1cs_cw006-a157-3-f with dissolve
    cw "*muffled moaning*"
    pause
    scene sm1cs_cw006-a157-4-f with dissolve
    pause
    cw "Mmm-rhuaaah... ffffffuaaah..."
    play voisex3 girl24_sex_orgasm4 noloop
    stop sound fadeout 1.0
    stop voisex2 fadeout 1.0
    scene sm1cs-cw006-162 cw-cums-hard-soft-gasping_c1 with vpunch
    cw "Oooohua... *soft gasping*... Huhaahh..."
    scene sm1cs-cw006-163 mct-watching-cw-pussy-what-pretty-sight-mct-should-get-moving_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "What a pretty sight."
    mct "But I should get moving. Don't want to be caught here."
    play sound [sfx_cloth_rustling4, sfx_cloth_rustling5]
    scene sm1cs-cw006-164 mc-crawls-out-of-table_c1 with dissolve
    play voice2 mc_angry_errr1 noloop
    mc "*grunting*"
    play sound sfx_skirt_off2
    scene sm1cs-cw006-165 mc-stands-up-hup-dust-himself-off_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Hup."
    scene sm1cs-cw006-166 cw-fixes-her-clothes-quite-showman-mc-oh-yeah_c1 with dissolve
    play voice3 girl29_thinking_hmm5 noloop
    cw "Hmmmm. Quite the showman, aren't you?"
    scene sm1cs-cw006-167 mc-sure-see-more-assignment_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Oh yeah."
    mc "I'm sure you'll see more as we try out this {i}special{/i} assignment."
    scene sm1cs-cw006-168 cw-mmm-hold-you-that_c1 with dissolve
    play voice3 girl24_sex_closedmoan5 noloop
    cw "Mmmm. I will hold you to that, Mister."
    cw "I'm looking forward to working {i}very{/i} close to you in the future."
    scene sm1cs-cw006-169 cw-looking-forward-working-closer-mc-too-watts_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Me too, Ms. Watts."
    scene sm1cs-cw006-170 cw-looking-through-glass_c1 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1cs-cw006-171 cw-strokes-mc-cheek-when-just-us-claire_c1 with dissolve
    play voice3 girl24_sex_closedmoan2 noloop
    cw "*whispers* When it's just us."
    cw "Just {i}Claire{/i} will do..."
    play sound sfx_cloth_rustling1
    scene sm1cs-cw006-172 cw-pulls-phone-now-should-return-work_c1 with dissolve
    play voice3 girl29_pain_cough1 noloop
    cw "Now... *ahem*"
    cw "You should return to your desk and I should figure out what I was actually {i}doing{/i} during this exercise."
    scene sm1cs-cw006-173 mc-hehe-understood_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Heh heh.{w} Understood."
    play sound sfx_heels_steps2
    scene sm1cs-cw006-174 mc-leaving-conference-rood_c1 with dissolve
    pause
    play sound sfx_door_openclosed1
    jump sm1cs_cw006_at_desk
label sm1cs_cw006_at_desk:
    scene sm1cs-cw006-175 mc-working-desk_c1 with Fade(0.5, 0.5, 0.5)
    queue sound sfx_keyboard_typing2
    pause
    play sound sfx_throw_something1
    play voice3 girl22_arrogant_huh noloop
    scene sm1cs-cw006-176 am-appears-what-that-about_c1 with hpunch
    am "What was all that about?"
    play voice2 mc_happy_oof2 noloop
    scene sm1cs-cw006-177 mc-startled-jeez_c1 with hpunch
    mc "Jeez!"
    scene sm1cs-cw006-178 am-why-so-nervous-mc_c1 with dissolve
    play voice3 girl22_arrogant_hm noloop
    am "I smell {b}fear{/b} on you, [mcname]."
    scene sm1cs-cw006-179 mc-most-not-jump-am-they-do-when-bored_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Most people don't just jump out at their co-workers like that."
    play sound sfx_chair_slide1
    scene sm1cs-cw006-180 am-sits-back-so-what-about-mc-just-computer-stuff_c1 with dissolve
    play voice3 girl22_arrogant_he noloop
    am "They do when they complete all their tasks and get bored."
    am "Spill it. What did Claire want?"
    play voice2 mc_arrogant_nah1 noloop
    mc "Just computer stuff."
    scene sm1cs-cw006-181 am-right-instead-best-coder-not-even-boss-comes-you_c1 with dissolve
    play voice3 girl22_yes_aga4 noloop
    am "Right. So instead of coming to her hotshot best in the entire state coder, Claire, who is not even our boss..."
    am "Comes to you..."
    scene sm1cs-cw006-182 mc-yep-am-silent_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Maybe you're not as good as you think you are."
    scene sm1cs-cw006-183 am-fine-get-truth-one-way-another_c1 with dissolve
    play voice3 girl22_disappointed_mmf noloop
    am "Impossible.{w} You're just hiding something."
    mc "..."
    scene sm1cs-cw006-184 mc-ignoring-am-you-sound-confident_c1 with dissolve
    play voice3 girl22_yes_yeah3 noloop
    am "Fine, but I'll get the truth out of you one way or another."
    play voice2 mc_thinking_mmm1 noloop
    mc "You sound confident."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw006-185 am-confiden-know-how-weak-mc-am-if-turn-pressure_c1 with dissolve
    play voice3 girl22_yes_angry noloop
    am "I am. I know how weak you are."
    am "If I turn up the pressure even just a few degrees..."
    play sound sfx_straw_drink5 volume 1.6
    scene sm1cs-cw006-186 am-slurps-slurping-sounds_c1 with dissolve
    am "*slurps*"
    stop sound fadeout 1.0
    scene sm1cs-cw006-187 am-finished-drinking-you-crack-like-rage-game-tv_c1 with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "You'll crack."
    am "Like a rage gamer's 4k TV when he didn't put on his controller strap like an idiot."
    scene sm1cs-cw006-188 mc-you-crazy-am-mmmhm_c1 with dissolve
    play voice2 mc_angry_off noloop
    mc "You're crazy."
    play voice3 girl22_yes_aga10 noloop
    am "Mmhmm."
    scene sm1cs-cw006-189 mc-nervous-looking-screen-end-scene_c1 with dissolve
    pause
    jump sm1cs_cw006_end_scene
label sm1cs_cw006_onramp_1:
    scene sm1cs-cw006-67 cw-neutral-talking-no-thought-about-that_c1 with dissolve
    play voice3 girl34_arrogant_hm3 noloop
    cw "What exactly was it that you wanted to talk about, Mr. Young?"
    play voice2 d2s12_emmm noloop
    mc "Well."
    mc "I guess I wanted to say that I was not satisfied with how our last conversation ended."
    scene sm1cs-cw006-75 cw-sighs-bold-but-astute_c1 with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "I hope you didn't come to whine. It wouldn't be a good look on you."
    play voice2 mc_no_no1 noloop
    mc "No. No whining, I just."
    scene sm1cs-cw006-70 cw-including-work-together-mc-been-thinking-this_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mc "What if I told you I changed my mind?"
    play voice3 girl29_thinking_mmm2 noloop
    cw "Mmm. It doesn't matter.{w} Didn't we both agree it could get messy?"
    scene sm1cs-cw006-65 cw-do-have-any-other-questions_c1 with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "It might. But I also think, it could be amazing."
    play voice3 girl29_disappointed_ehh noloop
    cw "You don't know what you're talking about."
    menu:
        "I want to be with you":
            $ player.set_choice("sm1ms_cw006_offramp_1", False)
            scene sm1cs-cw006-52 mc-guess-out-depth-cw-i-know_c1 with dissolve
            play voice2 mc_disappointed_ah2 noloop
            mc "I know I want to keep seeing you, Claire."
            mc "In whatever shape that takes."
            jump sm1cs_cw006_onramp_1a
        "Then I have my answer":
            scene sm1cs-cw006-52 mc-guess-out-depth-cw-i-know_c1 with dissolve
            play voice2 mc_disappointed_ehh5 noloop
            mc "I guess that's your answer."
            play voice3 girl29_yes_aga2 noloop
            cw "It is."
            jump sm1cs_cw006_break_up
label sm1cs_cw006_onramp_2:
    $ player.set_choice("sm1ms_cw006_offramp_2", False)
    scene sm1cs-cw006-52 mc-guess-out-depth-cw-i-know_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "I wanted to talk to you about that special assignement you mentioned?"
    play voice3 girl29_thinking_hmm3 noloop
    cw "Hmmm. What makes you think it is still on the table?"
    scene sm1cs-cw006-53 cw-certainly-share-some-blame-wouldnt-be-in-position_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well, I've had more time to think of it."
    mc "And, I'm sure you can appreciate not rushing into things, Ms. Watts."
    scene sm1cs-cw006-71 cw-grins-yes-even-practiced-tears_c1 with dissolve
    play voice3 girl29_thinking_mmm1 noloop
    cw "Hmm."
    cw "So... you would like to join my {i}special project?{/i}"
    jump sm1cs_cw006_choice_2
label sm1cs_cw006_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(CW_STORY, 1, 0, 3)
    return
label sm1cs_cw006_break_up:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(CW_STORY, 1, 0, 1)
    return