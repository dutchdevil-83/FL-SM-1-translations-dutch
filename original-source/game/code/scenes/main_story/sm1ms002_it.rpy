label sm1ms002_it:
    scene sm1ms002-09 sy-looking-away-disapointed_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Well, I got you a nice, cushy, air-conditioned office job."
    play sound sfx_cup_place1 volume 1.6
    scene sm1ms002-10 mc-heard-of-some-code-macros-didnt-come-up_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Sounds too good to be true. Is it?"
    scene sm1ms002-11 sy-amused-might-be-harder-mc-ask-coding-job-sy-data-analysis_c1 with dissolve
    play voice3 stacy_laugh4 noloop
    sy "Depends. How are your programming skills?"
    play voice2 mc_surprised_what1 noloop
    mc "My what?"
    sy "Perl, Python, C, C#...?"
    scene sm1ms002-12 mc-in-doubt-how-simple_c1 with dissolve
    sy "Ruby on Rails? PHP? JavaScript?"
    play voice2 d2s9_confused noloop volume 2.0
    mc "I was a business administration major."
    scene sm1ms002-13 sy-confident-wants-start-over_c1 with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "Do you at least know how to use spreadsheets?"
    play voice2 mc_yes_sure1 noloop
    mc "Of course."
    sy "What about SAS or SQL?"
    mc "I've heard of them."
    scene sm1ms002-14 sy-explains-like-teacher_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "At the very least you must know how to write Macros and VisualBasic code."
    play voice2 mc_no_no2 noloop
    mc "Um, no.{w} Didn't come up."
    sy "This might be harder than I thought."
    play sound sfx_gadgets_laptop_opened
    scene sm1ms002-15 sy-opens-computer-shows-him-screen-begin-tutorial_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Did you get me some sort of programming job?"
    play voice3 stacy_no_simple3 noloop
    sy "No. It's a simple data analysis job."
    play voice2 mc_thinking_hmm2 noloop
    mc "How simple?"
    if only_story_mode is False:
        scene sm1ms002-16-01 laptop-close-up_c1
        show sm1ms002_tutorial_1_mini
        with dissolve
    else:
        scene sm1ms002-18 mc-simple-enough_c1 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Well, it seems like it will be harder than I thought."
    mc "...?"
    play sound sfx_keyboard_typing1
    scene sm1ms002-16 sy-ask-how-does-that-sound_c1 with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "Okay, let's start over. You know how to do spreadsheets, right?"
    play voice2 mc_yes_yes1 noloop
    mc "Of course.{w} Excel, LibreOffice, BedSheets... they're all basically the same."
    play voice3 stacy_yes_ugu1 noloop
    sy "Good. Well, there's that, at least. Now you just need to learn how to code."
    stop sound fadeout 1.0
    scene sm1ms002-17 mc-choice-menu_c1 with dissolve
    mc "...?"
    play voice3 stacy_yes_fine4 noloop
    sy "Let's try a simple example."
    $ renpy.music.set_volume(0.8, 2.5, "music" )
    if only_story_mode is False:
        scene sm1ms002-16-01 laptop-close-up_c1
        show sm1ms002_tutorial_1_mini
        with dissolve
        pause
        jump sm1ms002_it_tutorial
    else:
        jump sm1ms002_it_only_story_mode
label sm1ms002_it_only_story_mode:
    scene black
    show screen scene_transistion(_("One eternity later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    jump sm1ms002_it_simple_enough
label sm1ms002_it_tutorial:
    call screen nonogram_tutorial("sm1ms002_it_continue")
    return
label sm1ms002_it_continue:
    $ renpy.music.set_volume(0.5, 2.5, "music" )
    scene sm1ms002-20 mc-didnt-get-whole-thing-sy-lets-try-again_c1 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "How does that sound?"
    menu:
        "Simple Enough"(hint="sm1ms002_it_m01_h01"):
            scene sm1ms002-18 mc-simple-enough_c1 with dissolve
            play voice2 d1s2_mchey noloop volume 1.6
            mc "Looks dead simple."
            play voice3 stacy_yay noloop
            sy "Excellent."
            jump sm1ms002_it_simple_enough
        "Still Confused"(hint="sm1ms002_it_m01_h02"):
            scene sm1ms002-19 mc-still-confused-mc-doesnt-get-it-sy-ask-which-part_c1 with dissolve
            play voice2 d2s12_emmm noloop
            mc "I... don't get it."
            play voice3 stacy_thinking_hmm3 noloop
            sy "Which part?"
            mc "The whole thing. I'm confused."
            scene sm1ms002-20 mc-didnt-get-whole-thing-sy-lets-try-again_c1 with dissolve
            play voice3 stacy_upset1 noloop
            sy "Okay, let's try this again."
            $ renpy.music.set_volume(0.8, 2.5, "music" )
            jump sm1ms002_it_tutorial
label sm1ms002_it_simple_enough:
    scene sm1ms002-21 sy-happy-mc-got-it-put-it-in-phone_c1
    if only_story_mode is False:
        with dissolve
    else:
        with Fade(0.5, 0.5, 0.5)
    play voice2 mc_arrogant_huh2 noloop
    mc "That's all there is to coding?"
    play voice3 stacy_no_nope4 noloop
    sy "Not at all, but it should be enough to get you this job."
    scene sm1ms002-22 sy-ask-anything-else-mc-gets-it-has-question_c1 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "I've sent that tutorial to your phone so you can review it again at any time."
    $ renpy.music.set_volume(0.8, 2.5, "music" )
    jump sm1ms002_it_end
label sm1ms002_it_end:
    $ renpy.music.set_volume(0.5, 2.5, "music" )
    scene sm1ms002-23 mc-ask-question_c1 with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "While I'm here, is there anything else you need to know?"
    play voice2 mc_yes_yeah4 noloop
    mc "I think I understand the task, but I do have a question."
    sy "Go ahead."
    scene sm1ms002-24 sy-ofc-computer-better-mc-thinks-like-mailroom-gig_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Wouldn't this be the sort of thing that a computer program could do more effectively than a human being?"
    play voice3 stacy_yes_yeah1 noloop
    sy "Of course. In fact, they probably have a computer program checking your results."
    play voice2 mc_disappointed_off2 noloop
    mc "Oh, so this job is like the mailroom."
    scene sm1ms002-25 sy-think-how-so-mc-exlpains-mailroom-proccess_c1 with dissolve
    play voice3 stacy_surprised_how1 noloop
    sy "How's that?"
    play voice2 mc_arrogant_heh1 noloop
    mc "Back in the day, people would start in the mailroom as a test of their skills and thought processing."
    mc "They would then get promoted to other parts of the company... or just stay in the mailroom."
    scene sm1ms002-26 sy-looks-back-smug_c1 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "That makes sense. Yeah, although I think there might be another reason."
    play voice2 d1s5_mchappy noloop volume 2.0
    mc "Someone to blame?"
    sy "Exactly. Even computers aren't flawless.{w} If something goes wrong, there needs to be someone to blame."
    mc "So I should try to avoid being someone to blame, and try to be someone they promote."
    play sound sfx_camera_fly1 volume 1.7
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound3 ["<silence 2.5>", sfx_camera_fly1] noloop volume 1.7
    scene sm1ms002-glambot-1 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1ms002-27 sy-leans-back-chair-mc-should-look-be-promoted_c1 with dissolve
    play voice3 stacy_yeahno noloop
    sy "Sure, I guess. Mostly you should focus on making money there so you can make even more money here."
    play voice2 mc_yes_aga2 noloop
    mc "It takes money to make money. Got it."
    scene sm1ms002-28 sy-tells-interviews-every-week-no-conflict_c1 with dissolve
    play voice3 stacy_hmm noloop
    sy "Alright, they have interviews on the regular every weekday. You just need to show up and exceed expectations."
    sy "However, this will conflict with your delivery schedule. You can only do so many things in a day."
    scene sm1ms002-29 mc-stands-up-jokes-captain-obvs_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Thank you, Captain Obvious."
    mc "With your permission, I'll grab something to eat and hit the sack."
    scene sm1ms002-30 sy-mock-solutes-mc-permission-granted_c1 with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "Permission granted, Ensign [mcname]."
    scene sm1ms002-31 mc-walks-towards-bed_c1 with dissolve
    pause
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    return