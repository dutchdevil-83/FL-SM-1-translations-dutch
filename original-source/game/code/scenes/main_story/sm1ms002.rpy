image sm1ms002-glambot-1 = Movie(play = "images/ms/s002/anim/sm1ms002-a27-3x-60fps.webm", start_image = "sm1ms002-a27-00", image = "sm1ms002-a27-99", loop = False)
label sm1ms002:
    $ renpy.music.set_volume(0.5, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    if player.get_choice("sm1msi001_immediate_start"):
        scene sm1ms002-02 sy-working-laptop_c1 with fade
    else:
        scene sm1ms002-02 sy-working-laptop_c1 with dissolve
    play sound sfx_keyboard_typing2
    play music music_everybody_got_aproblem
    pause
    if player.get_choice("sm1msi001_immediate_start") == False:
        scene sm1ms002-03 sy-good-mc-here-he-exhausted_c1 with dissolve
        play voice3 stacy_surprised_oh1 noloop
        sy "Oh good, you're here."
        play voice2 mc_disgust_meh4 noloop
        mc "Why is that good? I'm exhausted."
    if player.get_choice("NUMBER_OF_JOBS_UNLOCKED") > 0:
        if player.get_choice("Current_job_to_unlock") == IT_STORY_LINE:
            call sm1ms002_it from _call_sm1ms002_it
        elif player.get_choice("Current_job_to_unlock") == THEATER_STORY_LINE:
            call sm1ms002_t from _call_sm1ms002_t
        jump sm1ms002_end
    play sound sfx_gadgets_laptop_closed
    scene sm1ms002-04 sy-good-has-something-new-mc-ask-rent-camera-she-answers_c1 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "It's good because I have something new you can do tomorrow."
    play sound sfx_bed_slide2 volume 0.5
    scene sm1ms002-05 mc-sarcastic-what-next-endure-sy-ask-delivery-job-bad_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Great. Does that mean we can afford rent and the camera and all of that?"
    play sound sfx_cloth_rustling3
    scene sm1ms002-06 mc-not-cut-himself-sy-got-him-office-job-mc-hesitant_c1 with dissolve
    if player.money >= RENT_WEEKLY_AMOUNT + camera_price:
        play voice3 stacy_yes_simple1 noloop
        sy "Yes, but that's not important now."
    elif player.money >= RENT_WEEKLY_AMOUNT:
        play voice3 stacy_thinking_well1 noloop
        sy "Well, we can pay the rent. But that's not why I'm excited to see you."
    else:
        play voice3 stacy_no1 noloop
        sy "No, but I'm still excited to see you."
    play voice2 mc_angry_huh2 noloop
    mc "Fantastic.{w} Incredible."
    play sound sfx_glass_bottle_bonk volume 0.4
    scene sm1ms002-07 sy-casual-look-explains-depends-coding-skills_c1 with dissolve
    mc "What the hell is the next thing I need to endure for our dream?"
    play voice3 stacy_arrogant_huh3 noloop
    sy "Is the delivery job that bad?"
    scene sm1ms002-08 mc-blank-face-reminds-business-administration_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "I haven't started cutting on myself yet."
    play voice3 stacy_arrogant_huh3 noloop
    sy "Not funny, [mcname]."
    scene sm1ms002-07 sy-casual-look-explains-depends-coding-skills_c1 with dissolve
    sy "On the bright side, I think I've figured out two places for you work at."
    mc "Really?"
    scene sm1ms002-11 sy-amused-might-be-harder-mc-ask-coding-job-sy-data-analysis_c1 with dissolve
    sy "Yes. One avenue is that you work at an IT company."
    sy "The other is that you work your way into the crew of a local Theater."
    scene sm1ms002-12 mc-in-doubt-how-simple_c1 with dissolve
    sy "What do you say?"
    if vn_mode:
        jump sm1ms002_choice_it
    menu:
        "Start job in IT":
            jump sm1ms002_choice_it
        "Start job in Theater":
            jump sm1ms002_choice_theater
label sm1ms002_choice_it:
    mc "Tell me about the IT job."
    call sm1ms002_choice_job_unlock_it from _call_sm1ms002_choice_job_unlock_it
    call sm1ms002_it from _call_sm1ms002_it_1
    jump sm1ms002_continue_convo
label sm1ms002_choice_theater:
    mc "Tell me about the Theater."
    call sm1ms002_choice_job_unlock_theater from _call_sm1ms002_choice_job_unlock_theater
    call sm1ms002_t from _call_sm1ms002_t_1
    jump sm1ms002_continue_convo
label sm1ms002_continue_convo:
    scene sm1ms002-32 mc-calls-sy-one-more-thing_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Oh, Stacy... just one more thing."
    scene sm1ms002-33 sy-explain-mc-calls-lies-sy-she-implied_c1 with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "Yes?"
    scene sm1ms002-34 mc-calls-sy-spock-why-pays-rent-every-week-she-explains-expenses_c1 with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "About the rent. You said it was $[RENT_WEEKLY_AMOUNT] per month... but you're asking for that amount every week."
    scene sm1ms002-35 mc-want-see-breakdown-sy-ofc-go-back-to-laptop_c1 with dissolve
    play voice3 stacy_no_uhuh3 noloop
    sy "I said it was $[RENT_WEEKLY_AMOUNT]. I didn't say whether it was per month or per week."
    mc "You lied."
    sy "I implied."
    scene sm1ms002-34 mc-calls-sy-spock-why-pays-rent-every-week-she-explains-expenses_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Thanks, Spock.{w} Why am I paying you $[RENT_WEEKLY_AMOUNT] every week?"
    play voice3 stacy_arrogant_hmm1 noloop
    sy "Expenses. Food, rent, utilities, other things..."
    mc "I'd like to see how that breaks down."
    scene sm1ms002-33 sy-explain-mc-calls-lies-sy-she-implied_c1 with dissolve
    play voice3 stacy_angry noloop
    sy "Of course. Let me pull up that spreadsheet."
    play sound sfx_keyboard_typing2
    scene sm1ms002-36 looking-computer-mc-ask-why-furniture-weekly-sy-explains-total-they-need_c1 with dissolve
    stop sound fadeout 1.0
    play voice2 mc_scared_huuuh3 noloop
    mc "Fuck... wait a second... why are we paying that much every week for furniture? We sleep on a mattress on the floor."
    play voice3 stacy_mmm2 noloop
    sy "This isn't every week. It's also the total expenses we'll need."
    mc "So, some of what I am making goes into savings for..."
    scene sm1ms002-37 mc-figures-out-savings-sy-confirms_c1 with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "Future expenditures. Yes."
    play voice2 mc_yes_okay2 noloop
    mc "Okay.{w} I don't like it, but I guess that makes sense."
    play voice3 stacy_hey_happy2 noloop
    sy "Don't worry your pretty little head about it. Stacy will take care of everything."
    scene sm1ms002-38 mc-walk-away-sy-tells-she-got-this-mct-except-work_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Everything except the actual work."
    scene sm1ms002-39 sy-heard-mc-thoughts-he-tells-didnt-say-anything_c1 with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "I heard that."
    scene sm1ms002-40 sy-tells-mc-thinking-loud-he-thinks-a-scream-end-scene_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "I didn't say anything."
    play voice3 stacy_laugh2 noloop
    sy "I know, but you were thinking loudly."
    mct "Gah!"
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    jump sm1ms002_end
label sm1ms002_end:
    call sm1ms002_quest_line_unlock from _call_sm1ms002_quest_line_unlock
    $ StoryController.end_scene(MS, 2, 0, 0)
    return
label sm1ms002_choice_job_unlock_it:
    $ player.set_choice("first_job_to_unlock", IT_STORY_LINE)
    $ player.set_choice("Current_job_to_unlock", IT_STORY_LINE)
    return
label sm1ms002_choice_job_unlock_theater:
    $ player.set_choice("first_job_to_unlock", THEATER_STORY_LINE)
    $ player.set_choice("Current_job_to_unlock", THEATER_STORY_LINE)
    return
label sm1ms002_quest_line_unlock:
    $ StoryController.activate_story_line(player.get_choice("Current_job_to_unlock"), True)
    return
label sm1ms002_unlocks:
    call sm1ms002_choice_job_unlock_it from _call_sm1ms002_choice_job_unlock_it_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MS)
    return