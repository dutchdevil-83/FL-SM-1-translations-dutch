image sm1fs-i001-glambot-1 = Movie(play = "images/FS_IT/s001/anim/sm1fs-i001-a35-3x-60fps.webm", start_image = "sm1fs-i001-a35 glambot-00", image = "sm1fs-i001-a35 glambot-99", loop = False)
label sm1fs_i001:
    if sm1fs_i001_first_interview is True:
        jump sm1fs_i001_fail_try_again
    $ sm1fs_i001_first_interview = True
    $ renpy.music.set_volume(0.7, 0.0, "sound2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1fs-i001-01 mc-arrives-it-office_c1 with dissolve
    pause
    scene sm1fs-i001-02 ag-sees-mc-approaches-him_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.8, 0.0, "music" )
    play music lofi1
    $ renpy.music.set_volume(1.0, 10.0, "sound2" )
    scene sm1fs-i001-03 ag-welcomes-mc-ask-here-to-interview_c1 with dissolve
    play voice3 girl27_hey_interested noloop
    ag "Hello! Are you looking to interview for Orbix?"
    play voice2 mc_yes_yes3 noloop
    mc "Actually, yes. That would be awesome."
    play voice3 girl27_happy_great1 noloop
    ag "Great!"
    play sound sfx_cloth_rustling1
    scene sm1fs-i001-04 ag-mc-introduces-themselves-she-follow-him_c1 with dissolve
    play voice3 girl27_thinking_hmm3 noloop
    ag "My name is Anna Goodwin, I'm in charge of the first round interviews."
    play voice2 mc_yes_okay1 noloop
    mc "It's nice to meet you Anna, my name is [mcname]."
    ag "Wonderful, follow me!"
    scene sm1fs-i001-05 ag-walk-mc-towards-meeting-room-talks-to-him_c1 with dissolve
    play voice3 girl27_happy_yeah4 noloop
    ag "I am the team lead for a growing part of the company."
    ag "The last few quarters we've been growing by leaps and bounds, and when demand increases."
    play sound sfx_door_open1
    scene sm1fs-i001-06 ag-opens-door-meeting-room_c1 with dissolve
    play voice3 girl27_thinking_hmm3 noloop
    ag "We have to grow our capacity."
    scene sm1fs-i001-07 mc-ag-enter-meeting-room_c1 with dissolve
    ag "We're looking to hire some new people to help out, real self-starters and go-getters."
    $ renpy.music.set_volume(0.2, 2.0, "sound2" )
    play sound sfx_door_closed8 volume 3.0
    scene sm1fs-i001-08 ag-invites-mc-take-seat_c1 with dissolve
    play voice3 girl27_yes_ugu2 noloop
    ag "Please have a sit."
    play sound sfx_cloth_rustling3
    scene sm1fs-i001-09 ag-mc-sit-ag-ask-why-interested-mc-answers_c1 with dissolve
    play voice3 girl27_thinking_emm5 noloop
    ag "All right [mcname], why are you interested in working for Orbix?"
    play voice2 mc_thinking_hmm4 noloop
    mc "I got interested in tech a few weeks ago when... I encountered the most bizarre and unique app I've ever come across."
    scene sm1fs-i001-10 ag-wants-know-more-mc-long-story-she-has-time_c1 with dissolve
    play voice3 girl27_surprised_oh2 noloop
    ag "Oh? Tell me more."
    play sound sfx_hair_scratch1
    scene sm1fs-i001-11 mc-starts-story-looks-uncomfortable_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "It's a really long story."
    scene sm1fs-i001-10 ag-wants-know-more-mc-long-story-she-has-time_c1 with dissolve
    play voice3 girl27_yes_yeah6 noloop
    ag "I've got a little bit of time."
    scene sm1fs-i001-12 mc-continues-his-story_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "*coughs* Okay, well, uhm... I downloaded this app and couldn't delete it. I kept using it and it led to some of the best moments of my life."
    mc "And some of the worst. But I couldn't delete it. I was stuck."
    scene sm1fs-i001-11 mc-starts-story-looks-uncomfortable_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Someone very close to me started to show me some things we could do with coding and technology."
    mc "And because of her help, I was able to delete it and start moving on. It was all because she knew a lot about technology."
    scene sm1fs-i001-13 ag-curious-impressed-want-long-story-mc-cut-parts_c1 with dissolve
    play voice3 girl27_arrogant_hah noloop
    ag "Didn't seem like that long of a story."
    play voice2 mc_yes_yeah1 noloop
    mc "I skipped a few parts."
    scene sm1fs-i001-14 ag-would-love-full-story-mc-starts-interupted_c1 with dissolve
    play voice3 girl27_hey_greeting noloop
    ag "You'll have to tell me the full story one day."
    play voice2 d2s12_emmm noloop
    mc "I-"
    play sound sfx_knocking_glass1 volume 1.5
    scene sm1fs-i001-15 knocking-door-ag-excuses-one-second_c1 with dissolve
    play voice3 girl27_disgust_mff noloop
    ag "Sorry, one second."
    $ renpy.music.set_volume(0.7, 1.5, "sound2" )
    play sound sfx_door_open6
    scene sm1fs-i001-16 ag-how-can-help-am-waiting-last-part-project_c1 with dissolve
    play voice3 girl27_hey_sexy noloop
    ag "Hi, What can I help you with, April?"
    play voice4 girl22_disappointed_geh noloop
    am "I'm still waiting on your part of the last project."
    scene sm1fs-i001-17 ag-will-have-end-of-day-am-reminds-she-told-yesterday_c1 with dissolve
    play voice3 girl27_arrogant_yeah4 noloop
    ag "I told you, I'd have it by the end of the day."
    play voice4 girl22_yes_aga11 noloop
    am "I know. You also said that yesterday."
    scene sm1fs-i001-18 ag-gets-closer-am-doing-lead-stuff-am-insults-her_c1 with dissolve
    play voice3 girl27_angry_mmm noloop
    ag "I'm doing team leader stuff. You know, because I got the promotion."
    play voice4 girl22_arrogant_hm noloop
    am "You know that a fucking illiterate orphan with a stolen Maqbook from 2004 could have finished this by now."
    scene sm1fs-i001-19 ag-whisper-am-sucks-only-when-feels-like-it_c1 with dissolve
    play voice3 girl27_disgust_ergh4 noloop
    ag "*Whispers* You suck."
    play voice4 girl22_yes_yep4 noloop
    am "Only when I feel like it, Aubergine Anna."
    $ renpy.music.set_volume(0.2, 1.5, "sound2" )
    play sound sfx_door_closed7 volume 1.6
    scene sm1fs-i001-20 ag-closes-door-flustered_c1 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1fs-i001-21 ag-sits-still-affected-mc-ask-okay-she-fine_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "You okay?"
    play voice3 girl27_yes_yeah3 noloop
    ag "Yeah, I'm fine."
    mc "Who was that?"
    scene sm1fs-i001-22 mc-ask-who-that-ag-looks-at-am-direction-no-worries_c1 with dissolve
    play voice3 girl27_disappointed_mmm noloop
    ag "Don't worry about it. Anyway."
    play sound sfx_paper_rustl1
    scene sm1fs-i001-23 mc-gives-ag-cv_c1 with dissolve
    pause
    play sound sfx_paper_slide1 volume 1.5
    scene sm1fs-i001-24 ag-looks-papers-mc-would-be-qualified-ask-hobbies_c1 with dissolve
    play voice3 girl27_happy_hmm3 noloop
    ag "With your experience, albeit a little unusual, sounds like you'd be qualified for the job."
    ag "We're a 21st century company though. We also want to make sure our employees have something beyond work."
    ag "What kind of hobbies do you have outside of work?"
    scene sm1fs-i001-25 mc-little-shocked-ag-ask-if-expected-that_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Oh."
    play voice3 girl27_arrogant_hm2 noloop
    ag "You weren't expecting that?"
    scene sm1fs-i001-26 mc-never-been-asked-ag-asks-now_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I've never really been in a working environment that's asked me what I like to do."
    play voice3 girl27_yes_ugu1 noloop
    ag "Well now I'm asking."
    scene sm1fs-i001-27 mc-thinks-about-it-menu_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I guess I like..."
    menu:
        "Books"(hint="sm1fs_i001_m01_h01"):
            call sm1fs_i001_m01_c01 from _call_sm1fs_i001_m01_c01
            scene sm1fs-i001-28 answer-books-mc-likes-books-ag-ask-what-reading-now_c1 with dissolve
            play voice2 mc_yes_okay2 noloop
            mc "I guess I like books more than anything."
            play voice3 girl27_scared_oh2 noloop
            ag "Oh! You don't say? What are you reading right now?"
            scene sm1fs-i001-29 mc-struggles-book-name-ag-better-not-get-distracted_c1 with dissolve
            play voice2 d2s9_confused noloop volume 1.7
            mc "I'm currently reading, uhm-"
            play voice3 girl27_no_uhuh2 noloop
            ag "Sorry, actually don't tell me. I'll get distracted and we won't finish the interview."
        "Sports"(hint="sm1fs_i001_m01_h02"):
            call sm1fs_i001_m01_c02 from _call_sm1fs_i001_m01_c02
            scene sm1fs-i001-30 answer-sports-mc-enjoyed-playing-sports-ag-sounds-relaxing_c1 with dissolve
            play voice2 mc_arrogant_huh1 noloop
            mc "I've really enjoyed sports when I get the time to play."
            play voice3 girl27_happy_hmm2 noloop
            ag "Sounds... Relaxing?"
        "Gaming"(hint="sm1fs_i001_m01_h03"):
            call sm1fs_i001_m01_c03 from _call_sm1fs_i001_m01_c03
            scene sm1fs-i001-31 answer-gaming-mc-plays-games-for-hours_c1 with dissolve
            play voice2 mc_arrogant_huh1 noloop
            mc "From time to time, I sit and just play video games for a few hours."
            scene sm1fs-i001-32 ag-leans-forwards-ask-what-games-mc-mostly-fps_c1 with dissolve
            play voice3 girl27_scared_oh2 noloop
            ag "What games are you playing right now?"
            play voice2 d2s9_confused noloop
            mc "Uhhhh, mostly FPS games. Every once in awhile I'll pull up-"
            scene sm1fs-i001-33 ag-swagger-pretty-good-cs-mc-havent-played-recently_c1 with dissolve
            play voice3 girl27_happy_yes noloop
            ag "I absolutely adore FPS games. I'm killer at Contrary Strike."
            play voice2 mc_arrogant_heh1 noloop
            mc "It's been a long time since I've played that."
        "Cars"(hint="sm1fs_i001_m01_h04"):
            call sm1fs_i001_m01_c04 from _call_sm1fs_i001_m01_c04
            scene sm1fs-i001-34 answer-cars-mc-loves-cars-ag-not-impressed_c1 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "I really like cars. Muscle cars, pony cars, or rust buckets. I just love them."
            play voice3 girl27_disappointed_eh1 noloop
            ag "That's probably a good thing to like. It'll help you get to work."
    play sound ["<silence 0.5>", sfx_camera_fly1] volume 2.0
    scene sm1fs-i001-glambot-1 with dissolve
    pause
    stop sound fadeout 1.0
    play voice3 girl27_arrogant_hm4 noloop
    ag "That's good though. Having a way to unwind after work is important."
    play sound sfx_gadgets_laptop_closed
    scene sm1fs-i001-36 ag-puts-laptop-table-important-part-interview_c1 with dissolve
    play voice3 girl27_arrogant_huh1 noloop
    ag "Now for the important part of the interview."
    play sound sfx_gadgets_laptop_opened
    scene sm1fs-i001-37 ag-opens-laptop-nonogram_c1 with dissolve
    pause
    jump sm1fs_i001_setup_nonogram
label sm1fs_i001_setup_nonogram:
    $ nono_row_hints = []
    $ nono_col_hints = []
    $ nono_match_col = []
    $ nono_match_row = []
    $ nono_hints_max = 0
    $ grid_padding = 5
    $ nonogram_end_jump = "sm1fs_i001_nonogram_result"
    $ nonogram_background = "sm1fs-i001-37-01_laptop-monitor"
    $ random.seed()
    $ random_nonogram = renpy.random.choice(nonogram_puzzle_list_3x3)
    $ base64_string = random_nonogram[0]
    $ grid_cols = random_nonogram[1]
    $ grid_rows = random_nonogram[2]
    $ grid_size = grid_rows * grid_cols
    $ Nonogram.generate_hints(base64_string, grid_rows, grid_cols)
    $ nono_buttons_list = []
    $ Nonogram.generate_buttons()
    jump nonogram_game
label sm1fs_i001_nonogram_result:
    if nonogram_puzzle_solved is True:
        jump sm1fs_i001_first_success
    else:
        if sm1fs_i001_first_interview is True:
            jump sm1fs_i001_first_fail
        else:
            jump sm1fs_i001_fail
label sm1fs_i001_first_success:
    if sm1fs_i001_first_interview is False:
        call sm1fs_i001_choice_first_success from _call_sm1fs_i001_choice_first_success
    scene sm1fs-i001-38 first-success-ag-checks-results_c1 with dissolve
    play voice3 girl27_surprised_ohmy2 noloop
    ag "Oh, wow! Fantastic!"
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    scene sm1fs-i001-39 ag-excited-mc-did-great_c1 with dissolve
    play voice3 girl27_yes_yap2 noloop
    ag "You did great. I think you'd be a wonderful addition to the team."
    jump sm1fs_i001_got_hired
label sm1fs_i001_first_fail:
    scene sm1fs-i001-48 first-fail-ag-checks-results-sees-where-mc-wrong_c1 with dissolve
    play sound sfx_keyboard_typing2
    play voice3 girl27_disappointed_ah1 noloop
    ag "Ahhh, I see what you did wrong."
    play voice2 mc_angry_huh1 noloop
    mc "What's that?"
    scene sm1fs-i001-49 ag-no-wiggling-answer-mc-had-try_c1 with dissolve
    play voice3 girl27_disappointed_oh2 noloop
    ag "Tsk, tsk, tsk. Trying to wriggle the answer out of me?"
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "I had to try."
    scene sm1fs-i001-50 ag-ask-another-try-mc-would-love_c1 with dissolve
    play voice3 girl27_thinking_hmm5 noloop
    ag "Want to give it another go?"
    play voice2 mc_yes_yes1 noloop
    mc "That would be great."
    jump sm1fs_i001_setup_nonogram_2
label sm1fs_i001_setup_nonogram_2:
    $ nono_row_hints = []
    $ nono_col_hints = []
    $ nono_match_col = []
    $ nono_match_row = []
    $ nono_hints_max = 0
    $ grid_padding = 5
    $ nonogram_end_jump = "sm1fs_i001_nonogram_result_2"
    $ nonogram_background = "sm1fs-i001-37-01_laptop-monitor"
    $ base64_string = random_nonogram[0]
    $ grid_cols = random_nonogram[1]
    $ grid_rows = random_nonogram[2]
    $ grid_size = grid_rows * grid_cols
    $ Nonogram.generate_hints(base64_string, grid_rows, grid_cols)
    $ nono_buttons_list = []
    $ Nonogram.generate_buttons()
    jump nonogram_game
label sm1fs_i001_nonogram_result_2:
    if nonogram_puzzle_solved is True:
        jump sm1fs_i001_second_success
    else:
        jump sm1fs_i001_fail
label sm1fs_i001_second_success:
    scene sm1fs-i001-51 second-success-mc-shows-screen-to-ag_c1 with dissolve
    play voice3 girl27_yes_aga noloop
    ag "That looks better."
    play voice2 mc_happy_oof3 noloop
    mc "Phew, had me sweating there!"
    scene sm1fs-i001-52 ag-happy-results-welcomes-mc-firm_c1 with dissolve
    play voice3 girl27_no_happy noloop volume 0.8
    ag "No worries at all [mcname]. It looks like you've got the skills to work here at Orbix!"
    jump sm1fs_i001_got_hired
label sm1fs_i001_got_hired:
    scene sm1fs-i001-40 got-hired-mc-excited-when-start_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Awesome, when do I start?"
    scene sm1fs-i001-41 ag-remembers-second-interview_c1 with dissolve
    play voice3 girl27_thinking_emm5 noloop
    ag "Actually, there's a second interview."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh. I thought you were the team lead?"
    scene sm1fs-i001-42 ag-nervous-smile-hires-must-aproved-claire-mc-ask-she-around_c1 with dissolve
    play voice3 girl27_yes_simple noloop
    ag "I am, but all of the new hires need to be approved by my boss, Claire."
    play voice2 mc_thinking_hmm5 noloop
    mc "Is she around right now?"
    ag "She's in meetings for the rest of the day. But..."
    scene sm1fs-i001-43 ag-looks-up-laptop-tells-mc-when-second-interview_c1 with dissolve
    play voice3 girl27_thinking_emm3 noloop
    ag "If you come tomorrow, [gt.next_day] at 8:00am you should be able to meet with her."
    scene sm1fs-i001-44 ag-mc-both-happy-met-each-other_c1 with dissolve
    play voice3 girl27_happy_relief3 noloop
    ag "It's been absolutely delightful [mcname]."
    play voice2 mc_yes_yeah4 noloop
    mc "I feel the same Anna!"
    scene sm1fs-i001-45 ag-mc-shake-hands_c1 with dissolve
    play voice3 girl27_yes_ugu3 noloop
    ag "I'm looking forward to working with you!"
    $ renpy.music.set_volume(1.0, 2.0, "sound2" )
    play sound sfx_door_open6 volume 1.5
    scene sm1fs-i001-46 ag-jokes-upset-claire-mc-smiles-will-do-best_c1 with dissolve
    play voice3 girl27_disappointed_mff noloop
    ag "As long as you don't upset Claire when you meet with her."
    play voice2 mc_yes_sure1 noloop
    mc "I'll do my best."
    scene sm1fs-i001-47 mc-leaves-office-end-scene_c1 with dissolve
    pause
    scene sm1fs-i001-60 mc-leaves-office_c1 with dissolve
    pause
    stop music fadeout 3.0
    stop sound2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    jump sm1fs_i001_exit_to_free_roam
label sm1fs_i001_fail:
    scene sm1fs-i001-53 fail-mc-shows-screen-ag-worried_c1 with dissolve
    play voice3 girl27_disappointed_mmh noloop
    ag "Unfortunately [mcname], you didn't get it."
    scene sm1fs-i001-54 ag-checks-results-not-good-enought-but-potential_c1 with dissolve
    play voice3 girl27_hey_simple1 noloop
    ag "But we are always testing potential candidates!"
    scene sm1fs-i001-55 ag-suggest-mc-comes-try-another-time-he-ask-if-can_c1 with dissolve
    play voice3 girl27_thinking_hmm4 noloop
    ag "Why don't you come back and try again another time?"
    play voice2 mc_arrogant_huh3 noloop
    mc "I can do that?"
    scene sm1fs-i001-56 ag-shrugs-why-not-mc-thanks-her_c1 with dissolve
    play voice3 girl27_yes_yap3 noloop
    ag "We're actively looking to hire someone. If you can come back and show me what you're doing, you've got a good shot."
    play sound sfx_cloth_rustling2
    scene sm1fs-i001-58 mc-ag-shake-hands_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thank you, Anna."
    play voice3 girl27_no_short noloop
    ag "Don't thank me yet."
    ag "Thank me when you pass the interview."
    play sound sfx_door_open6
    scene sm1fs-i001-59 mc-leaves-meeting-room_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Don't worry, you'll be seeing me again."
    play voice3 girl27_yes_ugu3 noloop
    ag "Good."
    scene sm1fs-i001-60 mc-leaves-office_c1 with dissolve
    pause
    stop music fadeout 3.0
    stop sound2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene_without_progressing(IT_STORY_LINE, 8, 0, 2)
    return
label sm1fs_i001_fail_try_again:
    $ renpy.music.set_volume(0.7, 0.0, "sound2" )
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1fs-i001-61 mc-comes-again-nervous-waiting-ag_c1 with dissolve
    pause
    scene sm1fs-i001-02 ag-sees-mc-approaches-him_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.8, 0.0, "music" )
    play music lofi1
    scene sm1fs-i001-03 ag-welcomes-mc-ask-here-to-interview_c1 with dissolve
    play voice3 girl27_hey_interested noloop
    ag "Hello! [mcname], right?"
    scene sm1fs-i001-04 ag-mc-introduces-themselves-she-follow-him_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes! I'm surprised you remembered."
    play voice3 girl27_happy_relief2 noloop
    ag "Of course I remembered, you're a, uhm, great potential candidate."
    scene sm1fs-i001-05 ag-walk-mc-towards-meeting-room-talks-to-him_c1 with dissolve
    play voice3 girl27_thinking_hmm noloop
    ag "Shall we get to the test?"
    play voice2 mc_yes_okay2 noloop
    mc "Lead the way."
    $ renpy.music.set_volume(0.2, 1.5, "sound2" )
    play sound sfx_door_openclosed1
    scene sm1fs-i001-08 ag-invites-mc-take-seat_c1 with dissolve
    play voice3 girl27_disappointed_eh2 noloop
    ag "Feeling better about the test?"
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, much better in fact."
    play sound sfx_cloth_rustling3
    scene sm1fs-i001-09 ag-mc-sit-ag-ask-why-interested-mc-answers_c1 with dissolve
    play voice3 girl27_arrogant_mhm noloop
    ag "Good. Let's get right to it."
    scene sm1fs-i001-35 hobbies-good-to-unwind-ag-holds-laptop_c1 with dissolve
    pause
    play sound sfx_gadgets_laptop_closed
    scene sm1fs-i001-36 ag-puts-laptop-table-important-part-interview_c1 with dissolve
    play voice3 girl27_thinking_hmm5 noloop
    ag "Start whenever you're ready."
    play sound sfx_gadgets_laptop_opened
    scene sm1fs-i001-37 ag-opens-laptop-nonogram_c1 with dissolve
    jump sm1fs_i001_setup_nonogram
label sm1fs_i001_exit_to_free_roam:
    $ StoryController.end_scene(IT_STORY_LINE, 8, 0, 2)
    return
label sm1fs_i001_m01_c01:
    $ player.set_choice("sm1fs_i001_books")
    $ CharacterController.get_character("ag").add_point()
    $ CharacterController.get_character("ag").discover_topic(TOPIC_LITERATURE)
    return
label sm1fs_i001_m01_c02:
    $ player.set_choice("sm1fs_i001_sports")
    return
label sm1fs_i001_m01_c03:
    $ player.set_choice("sm1fs_i001_gaming")
    $ CharacterController.get_character("ag").add_point()
    $ CharacterController.get_character("ag").discover_topic(TOPIC_GAMING)
    return
label sm1fs_i001_m01_c04:
    $ player.set_choice("sm1fs_i001_cars")
    return
label sm1fs_i001_choice_first_success:
    $ player.set_choice("sm1fs_i001_first_success")
    return
label sm1fs_i001_unlocks:
    call sm1fs_i001_m01_c01 from _call_sm1fs_i001_m01_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(IT_STORY_LINE)
    return