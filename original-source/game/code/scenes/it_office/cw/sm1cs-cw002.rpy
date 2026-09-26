image sm1cs-cw002-a16-glambot = Movie(play = "images/FS_IT/CW/s002/anim/sm1cs-cw002-a16-2x-50fps.webm", start_image = "sm1cs-cw002-a16 cw-boss-lady-pose-text-details-wear-nice-batter-business-casual-glambot-16-000_i", image = "sm1cs-cw002-a16 cw-boss-lady-pose-text-details-wear-nice-batter-business-casual-glambot-16-149_i", loop = False)
label sm1cs_cw002:
    $ renpy.music.set_volume(0.5, 3.0, "freeroam_music1" )
    play sound sfx_keyboard_typing2 volume 2.0 loop
    scene sm1cs-cw002-01 mc-approach-cw_c1 with dissolve
    pause
    play voice2 mc_hey_hey5 noloop
    mc "Hi, Ms. Watts."
    scene sm1cs-cw002-02 mc-hello-cw-annoyed-what-is-it-busy_c1 with dissolve
    play voice3 girl29_arrogant_yeah noloop
    cw "What is it, Mr. Young? I'm busy."
    scene sm1cs-cw002-03 mc-just-saying-hello-cw-yes_c1 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh sorry. Just saying 'hello'."
    play voice3 girl29_yes_serious noloop
    cw "Yes."
    play sound sfx_chair_slide1
    play sound2 sfx_heels_steps2
    scene sm1cs-cw002-04 mc-starts-walking-away-cw-has-idea_c1 with dissolve
    pause
    play sound sfx_skirt_off2
    stop sound2 fadeout 1.0
    scene sm1cs-cw002-05 cw-stand-up-wait-moment-mc-turns-back-yes_c1 with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "Mr. Young. Wait a moment."
    play voice2 mc_yes_yes8 noloop
    mc "Uh... yes?"
    scene sm1cs-cw002-06 cw-looking-mc-over-eyeing-him_c1 with dissolve
    pause
    scene sm1cs-cw002-07 cw-talking-mc-allows-ask-personal-question-plans-tomorrow-lunch_c1 with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "Allow me to ask you a personal question."
    cw "Do you already have lunch plans tomorrow?"
    scene sm1cs-cw002-08 mct-strange-choice-menu-screen_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Strange that she didn't really ask me for permission before asking the 'personal question'."
    menu:
        "I like it."(hint="sm1cs_cw002_m01_m01"):
            call sm1cs_cw002_m01_c01 from _call_sm1cs_cw002_m01_c01
            scene sm1cs-cw002-09 choice-like-it-mc-grinning_c1 with dissolve
            play voice2 mc_thinking_mmm1 noloop
            mct "My kind of woman."
        "I don't like it."(hint="sm1cs_cw002_m01_m02"):
            scene sm1cs-cw002-10 choice-dont-like-it-mc-neutral_c1 with dissolve
            play voice2 mc_angry_hm2 noloop
            mct "Not sure why she's being pushy toward me. Especially about my lunch plans."
    scene sm1cs-cw002-11 cw-annoyed-mc-not-respond-ask-listening-mc-totally_c1 with dissolve
    play voice3 girl29_arrogant_huh noloop
    cw "Are you listening to me, Mr. Young?"
    scene sm1cs-cw002-12 mc-lunch-tomorrow-no-plans-yet_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes. Totally."
    mc "Lunch tomorrow?"
    mc "No. I don't have any plans yet."
    if player.has_played_scene("sm1cs_am006"):
        scene sm1cs-cw002-13 mct-inviting-am-lunch-date_c1 with dissolve
        play voice2 mc_thinking_hm noloop
        mct "I wonder if I should invite April out on a lunch date sometime."
        mct "Nah. April is always super focused earlier in the work day."
        mct "Probably should just stick to evening plans."
    if player.has_played_scene("sm1cs_ns007"):
        scene sm1cs-cw002-14 mct-wonder-nari-enjoy-lunch-date_c1 with dissolve
        play voice2 mc_thinking_mmm6 noloop
        mct "I wonder if Nari would enjoy a lunch date sometime."
    scene sm1cs-cw002-15 cw-focused-talking-mc-excellent-would-like-take-lunch-tomorrow_c1 with dissolve
    play voice3 girl29_yes_aga2 noloop
    cw "Excellent."
    cw "I... *ahem* I would like to take you out to lunch tomorrow."
    play sound sfx_cloth_rustling4
    scene sm1cs-cw002-a16 cw-boss-lady-pose-text-details-wear-nice-batter-business-casual-glambot-16-000_i with dissolve
    pause 0.1
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs-cw002-a16-glambot
    pause
    play voice3 girl29_thinking_hmm5 noloop
    cw "I'll text you the details. It's important that you wear something nice."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-cw002-17 cw-absolutely-critical-item-dont-be-late_c1 with dissolve
    play voice3 girl29_arrogant_ha noloop
    cw "Better than business casual."
    cw "But the absolutely critical item on the agenda is that you are not late to arrive."
    scene sm1cs-cw002-18 mc-chuckling-never-had-date-agenda-cw-intense-that-not-date_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Uh... *chuckles* I've never had a lunch date agenda."
    scene sm1cs-cw002-19 cw-require-assistance-difficult-client-meeting_c1 with dissolve
    play voice3 girl29_no_angry noloop
    cw "This is absolutely not a {i}date{/i} of any kind."
    cw "I require someone to assist me for a..."
    cw "Difficult client meeting."
    cw "Do you think you can handle that?"
    scene sm1cs-cw002-20 cw-think-handle-that-mc-wont-let-down_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course. I won't let you down, Claire."
    mc "But this sounds important. Shouldn't you bring Anna?"
    play voice3 girl29_no_uhuh noloop
    cw "I have already selected you, Mr. Young."
    play sound sfx_cloth_rustling5
    scene sm1cs-cw002-21 mc-sounds-important-bring-anna-cw-chosen-him_c1 with dissolve
    play voice3 girl29_thinking_mmm2 noloop
    cw "Consider it a test, one that is important for your future here at Orbix."
    scene sm1cs-cw002-22 cw-smiles-consider-test_c1 with dissolve
    play voice3 girl29_disappointed_oh noloop
    cw "Is that clear?"
    play sound sfx_heels_steps1
    scene sm1cs-cw002-23 cw-clear-mc-crystal-clear_c1 with dissolve
    stop sound fadeout 1.5
    play voice2 mc_yes_yes1 noloop
    mc "Yes. I mean, crystal. Crystal clear."
    play sound sfx_throw_something1 volume 0.5
    scene sm1cs-cw002-24 cw-excellent-get-back-work_c1 with dissolve
    play voice3 girl29_yes_yep noloop
    cw "Excellent. Now, return to your work."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw002-25 cw-need-practice-forget-it_c1 with dissolve
    play voice3 girl29_surprised_ehh noloop
    cw "I need to practice my..."
    play sound sfx_message_in1
    cw "Forget it."
    play sound2 sfx_heels_steps2
    scene sm1cs-cw002-26 mc-walking-away-thinking_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "This {i}really{/i} must be a difficult client. I don't think I've ever seen Claire acting like this before."
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(1.0, 2.0, "freeroam_music1" )
    jump sm1cs_cw002_end
label sm1cs_cw002_end:
    $ StoryController.end_scene(CW_STORY, 0, 15, 0)
    return
label sm1cs_cw002_m01_c01:
    $ player.set_choice("sm1cs_cw002_like_cw")
    return