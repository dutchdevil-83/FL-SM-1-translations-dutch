label sm1cs_am005b:
    scene sm1cs-am005b-01 mc-am-standing-away-from-desks_c1 with fade
    play voice2 d2s9_mchey noloop
    mc "Hey, April."
    scene sm1cs-am005b-02 mc-hey-am-what-what_c1 with dissolve
    play voice3 girl22_arrogant_huh noloop
    am "What do you want?"
    scene sm1cs-am005b-03 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Try out things with April."(hint="sm1cs_am005b_m01_h01"):
            call sm1cs_am005b_m01_c01 from _call_sm1cs_am005b_m01_c01
            play sound sfx_hair_scratch1
            scene sm1cs-am005b-06 choice-resume-mc-wanting-try-thing-with-am_c1 with dissolve
            play voice2 d1s5_mcthinks noloop volume 1.8
            mc "I think. I think I want to try out things..."
            mc "With you."
        "Nevermind."(hint="sm1cs_am005b_m01_h02"):
            play sound sfx_cloth_rustling1
            scene sm1cs-am005b-04 mc-choice-nevermind-mc-nvm_c1 with dissolve
            play voice2 mc_arrogant_nah1 noloop
            mc "Nevermind."
            play sound sfx_heels_steps2 loop
            scene sm1cs-am005b-05 mc-leaving-end_c1 with dissolve
            pause
            stop sound fadeout 1.0
            jump sm1cs_am005b_end
    scene sm1cs-am005b-07 am-scoffs-looks-away-why-think-still-interested-mc-that-fair_c1 with dissolve
    play voice3 girl22_arrogant_pff noloop
    am "*scoffs* And what makes you think I'm still interested."
    play voice2 d9s2_yeah noloop volume 1.8
    mc "That's fair."
    scene sm1cs-am005b-06 choice-resume-mc-wanting-try-thing-with-am_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "But... if you are..."
    scene sm1cs-am005b-08 mc-but-if-am-dont-like-being-jerked_c1 with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "I don't appreciate getting jerked around, [mcname]."
    scene sm1cs-am005b-09 mc-nods-yeah-no-surprise_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah. No surprise there."
    jump sm1cs_am005b_end
label sm1cs_am005b_end:
    $ StoryController.end_scene(AM_STORY, 0, 15, 0)
    return
label sm1cs_am005b_m01_c01:
    $ player.set_choice("sm1cs_am005b_try_things_am")
    return