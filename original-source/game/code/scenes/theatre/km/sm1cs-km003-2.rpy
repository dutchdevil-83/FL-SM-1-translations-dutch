image sm1cs_km003-a59-glm = Movie(play = "images/FS_T/KM/s003/anim/sm1cs-km003-a59-2x-50fps.webm", start_image = "sm1cs-km003-a59 km-help-veronica-mc-veronica-lost-here-glambot-000_i", image = "sm1cs-km003-a59 km-help-veronica-mc-veronica-lost-here-glambot-219_i", loop = False)
label sm1cs_km003_2:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_sharpminds_dance fadein 1.5
    scene sm1cs-km003-01 mc-km-alone-middle-stage_c1 with dissolve
    pause
    scene sm1cs-km003-02 km-first-thing-start-loosen-up_c1 with dissolve
    play voice3 girl31_thinking_emm2 noloop
    km "The first thing you should do is loosen up."
    play sound sfx_cloth_rustling2
    scene sm1cs-km003-03 km-shakes-body-prepare-body-mc-sure_c1 with dissolve
    play voice3 girl31_happy_mmm3 noloop
    km "Prepare your body."
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    scene sm1cs-km003-04 km-and-tongue-mc-confused-what_c1 with dissolve
    play voice3 girl31_thinking_hmm1 noloop
    km "And your tongue. The tongue is very important."
    play voice2 mc_surprised_uh1 noloop
    mc "Uh. How do I ready my tongue?"
    scene sm1cs-km003-05 km-testing-him-how-think-do-that_c1 with dissolve
    play voice3 girl31_disappointed_ehh1 noloop
    km "How do you think?"
    scene sm1cs-km003-06 mc-thinks-choice-menu-screen_c1 with dissolve
    menu:
        "Practicing kisses?"(hint="sm1cs_km003_m01_h01"):
            call sm1cs_km003_m01_c01 from _call_sm1cs_km003_m01_c01
            scene sm1cs-km003-07 choice-practice-kissing-mc-got-it-practice-french_c1 with dissolve
            play voice2 mc_thinking_hmm8 noloop
            mc "I got it. We practice French kissing."
            scene sm1cs-km003-08 km-laughs-half-embarrased-omg-no-what-not-practice-kissing_c1 with dissolve
            play voice3 girl31_happy_laugh1 noloop
            km "Oh my god. No, [mcname]. What?"
            km "Ahem. No, we do not practice kissing."
            scene sm1cs-km003-09 mc-so-what-we-do-mk-tongue-twisters_c1 with dissolve
            play voice2 d2s9_confused noloop volume 1.3
            mc "So what do we do?"
            play voice3 girl31_disappointed_ehh3 noloop
            km "Tongue twisters."
        "There must be a special form."(hint="sm1cs_km003_m01_h02"):
            scene sm1cs-km003-10 choice-special-form-mc-thinking-some-trick-to-it_c1 with dissolve
            play voice2 d1s5_mcthinks noloop volume 1.6
            mct "There must be some trick to it."
            scene sm1cs-km003-11 mc-what-bout-tongue-twisters-km-impressed-very-good_c1 with dissolve
            play voice2 mc_surprised_oh1 noloop
            mc "Wait, what about tongue twisters?"
            play voice3 girl31_yes_simple2 noloop
            km "Very good. That's correct."
    scene sm1cs-km003-12 km-vocal-exercises-but-tongue-twister-especially-helpful_c1 with dissolve
    play voice3 girl31_thinking_hmm2 noloop
    km "There are a lot of vocal exercises but tongue twisters are especially helpful."
    scene sm1cs-km003-13 km-recites-twister-perfectly_c1 with dissolve
    play voice3 girl31_happy_relief noloop
    km "Red leather, yellow leather."
    km "Red leather, yellow leather."
    scene sm1cs-km003-14 mc-starts-reciting-loses-pace-ugh_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Read leather, yell-"
    mc "Ugh."
    scene sm1cs-km003-15 km-grins-not-so-easy-km-again-red-leather_c1 with dissolve
    play voice3 girl31_arrogant_hm2 noloop
    km "Not so easy is it? Try again."
    km "Red leather, yellow leather."
    scene sm1cs-km003-16 mc-deep-breath-yellow-damn-it_c1 with dissolve
    play voice2 d14s16_smell noloop
    mc "*deep breath*"
    queue voice2 mc_angry_errr7 noloop
    mc "Yellow. Damn, that's wrong."
    scene sm1cs-km003-17 km-giggle-looking-cute_c1 with dissolve
    play voice3 girl31_happy_laugh8 noloop
    pause
    play sound sfx_cloth_rustling4
    scene sm1cs-km003-18 km-behind-mc-just-relax-focus-entirely-words_c1 with dissolve
    play voice3 girl31_hey_interesting noloop
    km "Just relax, [mcname]. Get out of your own head and just focus entirely on the words."
    scene sm1cs-km003-19 mc-close-eyes-mct-got-this-mc-redleather-yellow-leather_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "You got this."
    scene sm1cs-km003-20 mc-more-confident_c1 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Red leather,{w} yellow leather."
    mc "*faster* Red leather, yellow leather."
    play voice2 d3s11b_mcheh noloop
    mc "Haha. Nailed it."
    scene sm1cs-km003-21 km-happy-one-more-time-mc-repeats-it_c1 with dissolve
    play voice3 girl31_yes_happy1 noloop
    km "Yes. Now one more time."
    play voice2 mc_arrogant_hm1 noloop
    mc "Red leather, yellow leather."
    play sound sfx_cloth_rustling1
    scene sm1cs-km003-22 km-nodding-great-work-now-tongue-lose-work-stand_c1 with dissolve
    play voice3 girl31_happy_great noloop volume 0.7
    km "Great work. Usually before a practice, I practice that one and a few others at least five to ten times."
    km "Now that we've got your tongue loose, we can work on how you stand."
    scene sm1cs-km003-23 km-posture-importnat-mc-why_c1 with dissolve
    play voice3 girl31_thinking_hmm5 noloop
    km "Your posture is very important for theater."
    play voice2 mc_surprised_why3 noloop
    mc "Why?"
    scene sm1cs-km003-24 km-ahead-mc-facing-seating-biggest-difference-stage-actors_c1 with dissolve
    play voice3 girl31_thinking_oh noloop
    km "One of the biggest differences between actors on stage and film is that when we're here, it's not like all the focus is on us."
    $ renpy.music.set_audio_filter("voice3", renpy.audio.filter.Reverb(0.3))
    scene sm1cs-km003-25 km-waves-towards-imaginery-audience-have-reach-audience-become-larger_c1 with dissolve
    play voice3 girl31_happy_yeah2 noloop
    km "We have to reach the audience. We have to stand tall."
    km "And become larger than life."
    $ renpy.music.set_audio_filter("voice3", None)
    scene sm1cs-km003-26 mc-how-do-that-km-teach-you_c1 with dissolve
    play voice2 mc_surprised_how2 noloop
    mc "How do we do that?"
    play voice3 girl31_thinking_hmm3 noloop
    km "I'll teach you."
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1cs-km003-27 posture-montage-one_c1 with fade
    pause
    scene sm1cs-km003-28 posture-montage-two_c1 with fade
    pause
    scene sm1cs-km003-29 posture-montage-three_c1 with fade
    pause
    $ renpy.music.set_volume(0.6, 2.5, "music" )
    jump sm1cs_km003_2_after_montage
label sm1cs_km003_2_after_montage:
    scene sm1cs-km003-30 km-stands-away-mc-now-try-one-more-time-mc-really_c1 with fade
    play voice3 girl31_yes_aga noloop volume 0.8
    km "Now try the line one more time."
    play voice2 mc_angry_really noloop
    mc "Really?"
    scene sm1cs-km003-31 km-just-do-it_c1 with dissolve
    play voice3 girl31_arrogant_hm1 noloop
    km "Just do it."
    play sound sfx_cloth_rustling2
    scene sm1cs-km003-32 mc-sighs-speaking-boldly_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "*sighs*"
    mc "\"The clouds me thought would open and show riches. {w}Ready to drop upon me, that when I waked,{w} I cried to dream again.\""
    scene sm1cs-km003-33 km-can-sense-difference-mc-skeptical_c1 with dissolve
    play voice3 girl31_happy_nice1 noloop
    km "See, can't you sense how much different that was from the first time you read the line."
    play voice2 mc_arrogant_hm3 noloop
    mc "I guess. I still don't understand what the line meant."
    scene sm1cs-km003-34 km-no-worries-from-tempest_c1 with dissolve
    play voice3 girl31_no_nah noloop volume 0.8
    km "Don't worry about that. It's from {i}The Tempest{/i}. Pretty old play, but one of my favorites."
    play sound sfx_phone_tapping1 volume 2.5 loop
    scene sm1cs-km003-35 km-does-stuff-phon_c1 with dissolve
    pause
    play sound sfx_phone_button1
    scene sm1cs-km003-36 km-looking-mc-texted-script-will-practice_c1 with dissolve
    play voice3 girl31_yes_yep noloop
    km "I just texted you a link to a new script."
    km "We're going to practice what we've gone over first with a brand new section."
    play sound sfx_cloth_rustling1
    scene sm1cs-km003-37 mc-looking-script-try-best-km-do-do-not_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I'll try my best."
    play voice3 girl31_no_questioning noloop
    km "No. Do or do not."
    scene sm1cs-km003-38 km-there-no-try-mc-chuckles-add-star-wars-list_c1 with dissolve
    play voice3 girl31_arrogant_nrgh noloop
    km "There is no try."
    play voice2 mc_angry_huh2 noloop
    mct "Guess we can add Star Wars to her favorite list."
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1cs-km003-39 practice-montage-one_c1 with fade
    pause
    scene sm1cs-km003-40 practice-montage-two_c1 with fade
    pause
    scene sm1cs-km003-41 practice-montage-three_c1 with fade
    pause
    scene sm1cs-km003-42 practice-montage-four_c1 with fade
    pause
    scene sm1cs-km003-43 practice-montage-five_c1 with fade
    pause
    $ renpy.music.set_volume(0.6, 2.5, "music" )
    scene sm1cs-km003-44 km-one-more-time_c1 with fade
    play voice3 girl31_arrogant_yeah2 noloop
    km "One more time, [mcname]."
    scene sm1cs-km003-45 km-watch-mc-do-war-games-scene_c1 with dissolve
    pause
    $ renpy.music.set_audio_filter("voice2", renpy.audio.filter.Reverb(0.3))
    scene sm1cs-km003-46 mc-wish-didnt-know-about-this_c1 with dissolve
    play voice2 mc_happy_oof1 noloop volume 2.0
    mc "I wish I didn't know about any of this.{w} I wish I was like everybody else in the world, and tomorrow it would just be over."
    scene sm1cs-km003-47 mc-no-time-be-sorry_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "There wouldn't be any time to be sorry about anything."
    play sound sfx_leg_kick6
    scene sm1cs-km003-48 mc-oh-jesus-really-wanted-learn-swim_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh, Jesus! I really wanted to learn how to swim. I swear to God I did."
    $ renpy.music.set_audio_filter("voice2", None)
    play sound sfx_applause_oneperson1
    scene sm1cs-km003-49 km-clapping-not-bad-not-bad-at-all_c1 with dissolve
    play voice3 girl31_surprised_wow2 noloop
    km "No bad. Not bad at all, [mcname]."
    scene sm1cs-km003-50 mc-smiling-really-km-deff_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Really?"
    play voice3 girl31_yes_yeah2 noloop
    km "Definitely."
    play sound sfx_cloth_rustling3
    if True:
        scene sm1cs-km003-51 if-actor-km-maybe-denise-right-call-mc-you-helping-out-kellie_c1 with dissolve
        play voice3 girl31_thinking_mmm6 noloop
        km "Maybe I was wrong about you. Denise made the right call to promote you to an actor."
        play voice2 d1s5b_ehhh noloop volume 1.7
        mc "I hope. But it's not like she's been the one helping me out, Kellie."
    else:
        scene sm1cs-km003-52 km-just-matter-time-denise-make-actor-mc-hope-fo_c1 with dissolve
        play voice3 girl31_thinking_mmm6 noloop
        km "I think it's only a matter of time before Denise sees your true potential."
        play voice2 d1s5b_ehhh noloop volume 1.7
        mc "I hope so. And if she does, it will be because of your help, Kellie."
    scene sm1cs-km003-53 km-mc-charged-moment-mct-wow-that-new_c1 with dissolve
    play voice2 mc_thinking_hm noloop volume 0.6
    mct "Wow. This is new. Kellie has never looked at me like this."
    play sound sfx_hair_scratch1 volume 1.5
    scene sm1cs-km003-54 km-turns-away-mc-confused-mc-what-wrong_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Something wrong?"
    scene sm1cs-km003-55 km-glance-mc-not-patronized-mc-dont-understand_c1 with dissolve
    play voice3 girl31_disappointed_ehh9 noloop
    km "I don't like being patronized, [mcname]."
    play voice2 mc_thinking_mmm5 noloop
    mc "I don't understand."
    scene sm1cs-km003-56 km-nothing-forget-what-said_c1 with dissolve
    play voice3 girl31_no_uhuh noloop
    km "It's... it's nothing. Forget I said anything."
    play sound sfx_heels_steps2 loop
    scene sm1cs-km003-57 km-flustered-dont-know-what-doing-here-not-job-train-mc-ofc-not_c1 with dissolve
    play voice3 girl31_angry_ergh1 noloop
    km "I don't know what I'm doing here. It's not my job to help you."
    play voice2 mc_no_no2 noloop
    mc "Of course not, but I really appreciate the help."
    scene sm1cs-km003-58 km-who-help-her-mc-help-you-with-what_c1 with dissolve
    play voice3 girl31_disappointed_ehh8 noloop
    km "And who is going to help me, [mcname]?"
    play voice2 mc_surprised_what1 noloop
    mc "Help you? With what?"
    play sound sfx_skirt_off2
    scene sm1cs-km003-a59 km-help-veronica-mc-veronica-lost-here-glambot-000_i with dissolve
    pause 0.1
    play sound ["<silence 1.0>", sfx_camera_fly1] volume 2.0
    play sound2 ["<silence 4.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs_km003-a59-glm
    pause
    play voice3 girl31_disappointed_mff2 noloop
    km "With Veronica."
    play voice2 mc_disappointed_ah2 noloop
    mc "Veronica? I'm lost here."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-km003-60 km-then-no-worries-mc-no-kellie-stop_c1 with dissolve
    play voice3 girl31_thinking_mmf1 noloop
    km "Then don't worry about it."
    play voice2 mc_no_no6 noloop
    mc "No, Kellie. Stop."
    play sound sfx_heels_steps1
    scene sm1cs-km003-61 mc-talking-from-distance-spend-hour-helping-me-there-problem-lemme-help_c1 with dissolve
    stop sound fadeout 1.5
    play voice2 mc_thinking_mmm3 noloop
    mc "Listen, you just spent an hour helping me. If there is a problem, maybe there is something I can do."
    scene sm1cs-km003-62 km-you-cant-should-not-be-mad-mc-well-sure-feel-something-off-chest_c1 with dissolve
    play voice3 girl31_thinking_mmm7 noloop
    km "You can't. I... I shouldn't have gotten mad at you, [mcname]."
    play voice2 mc_yes_yeah7 noloop
    mc "Well, sure, but I still feel like you want to get something off your chest."
    scene sm1cs-km003-63 km-sighs-embarassed-no-one-else-knows-about-this_c1 with dissolve
    play voice3 girl31_disappointed_ehh7 noloop
    km "*sighs*"
    km "No one else knows about this."
    play sound sfx_cloth_rustling3
    scene sm1cs-km003-64 mc-will-keep-secret-km-promise_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "I'll keep it a secret."
    play voice3 girl31_thinking_emm3 noloop
    km "You promise?"
    play sound sfx_leg_kick8
    scene sm1cs-km003-65 mc-swears-scouts-i-promise_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "I promise."
    scene sm1cs-km003-66 km-starts-story-back-highschool-boyfriend-breakup_c1 with dissolve
    play voice3 girl31_disappointed_ehh4 noloop
    km "Back in high school, my last year felt like I was lost in a storm."
    km "Things started off well, but then my boyfriend broke up with me. After that, everything in my life went sour overnight."
    scene sm1cs-km003-67 km-then-found-theater-group_c1 with dissolve
    play voice3 girl31_thinking_mmm4 noloop
    km "Then I found the theater group. They welcomed me in, and I started getting really good at it."
    scene sm1cs-km003-68 km-happy-thinking-days-doing-shows-helped-build-confidence-during-college-found-denise-group_c1 with dissolve
    play voice3 girl31_happy_relief noloop
    km "Being there, doing the shows, all of it just helped me build up my confidence. It felt like I could finally look myself in the mirror again."
    km "During college, I found Denise and this group, and it was great. I got to show off everything I worked so hard on during my senior year."
    scene sm1cs-km003-69 km-worried-again-now-veronica-in-picture-getting-all-top-roles_c1 with dissolve
    play voice3 girl31_disappointed_ehh5 noloop
    km "But now Veronica is in the picture. Almost as soon as she came in, she started getting all the top roles and I started getting pushed to the side."
    play sound sfx_cloth_rustling1
    scene sm1cs-km003-70 km-look-mc-talking-theater-everything-me-cant-bear-think-that_c1 with dissolve
    play voice3 girl31_scared_ah8 noloop
    km "The theater is everything to me. I'm worried that if things keep going on as they are, I'm going to fall into that sorrow again."
    km "I can't bear to think of it."
    scene sm1cs-km003-71 mc-really-rough-ask-tried-talking-veronica-about-it_c1 with dissolve
    play voice2 mc_angry_oof noloop
    mc "That's really rough, Kellie."
    mc "Have you tried talking to Veronica about this? If she knew, I bet she could, I don't know, go for smaller roles and leave space for you."
    scene sm1cs-km003-72 km-angry-not-want-charity-if-can-ruin-next-audition-lead-spot-mine_c1 with dissolve
    play voice3 girl31_no_angry noloop
    km "I don't want charity from her, [mcname]. I just need to figure out some way to knock her off her game."
    km "If I can ruin her next audition, the lead spot will be mine for sure."
    play sound sfx_cloth_rustling2
    scene sm1cs-km003-73 mc-but-we-all-team-km-sure-but-not-benched-longer_c1 with dissolve
    play voice2 d3s7_mcemm noloop volume 1.7
    mc "But we're a team. We all play for the same side, right?"
    play voice3 girl31_yes_simple1 noloop
    km "Sure, but I'm not going to sit on the bench any longer. I have to figure out what buttons to push."
    scene sm1cs-km003-74 km-it-is-the-only-way_c1 with dissolve
    play voice3 girl31_disappointed_ehh2 noloop
    km "It's the only way..."
    scene sm1cs-km003-75 km-looking-mc-ask-will-help-me_c1 with dissolve
    play voice3 girl31_surprised_huh1 noloop
    km "Will you help me?"
    scene sm1cs-km003-76 mc-suggestion-teach-confidence-one-his-best-traits_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "What if I just try teaching you to be more confident?"
    mc "It's one of my best traits."
    play sound sfx_heels_steps2
    play sound2 sfx_cloth_rustling5 noloop
    scene sm1cs-km003-77 km-not-issue-if-want-help-figure-plan_c1 with dissolve
    play voice3 girl31_no_simple noloop
    km "That's not the issue."
    km "But if you {i}really{/i} want to help me, you can help me when I figure out a plan to deal with Veronica."
    scene sm1cs-km003-78 mct-not-sure-like-idea-can-figure-middle-ground-issue_c1 with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "I'm not sure how I feel about this."
    mct "Then again, if I'm in on Kellie's plans, maybe I can figure out some sort of middle ground for this issue."
    play sound sfx_cloth_rustling3
    scene sm1cs-km003-79 mc-bad-idea-do-what-can_c1 with dissolve
    play voice2 mc_angry_off noloop
    mc "I think this is a bad idea, but I'll do what I can."
    play voice3 girl31_happy_yeah3 noloop
    km "Thank you, [mcname]."
    scene sm1cs-km003-80 km-you-good-guy-mc-end-scene_c1 with dissolve
    play voice3 girl31_thinking_mmm2 noloop
    km "You're a good guy..."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1cs_km003_2_end
label sm1cs_km003_2_end:
    $ StoryController.end_scene(KM_STORY)
    return
label sm1cs_km003_m01_c01:
    $ player.set_choice("sm1cs_km003_practice_kissing")
    return