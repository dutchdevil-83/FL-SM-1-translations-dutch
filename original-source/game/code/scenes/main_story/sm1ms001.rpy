image sm1ms001-glambot-1 = Movie(play = "images/ms/s001/anim/sm1ms001-a01.webm", start_image = "sm1ms001-a01-p1 hr-finish-000", image = "sm1ms001-a01-p2 sy-laptop-179", loop = False)
image sm1ms001-glambot-2 = Movie(play = "images/ms/s001/anim/sm1ms001-a33-2x-30fps.webm", start_image = "sm1ms001-a33 sy-tells-thing-two-list-need-camera-mc-asking-about-phones-glambot-00000", image = "sm1ms001-a33 sy-tells-thing-two-list-need-camera-mc-asking-about-phones-glambot-00089", loop = False)
label sm1ms001:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    $ renpy.music.set_volume(1.0, 0.0, "sound4" )
    $ renpy.music.set_volume(1.0, 0.0, "sound5" )
    $ renpy.music.set_volume(1.0, 0.0, "voice2" )
    $ renpy.music.set_volume(1.0, 0.0, "voice3" )
    $ renpy.music.set_volume(1.0, 0.0, "voice4" )
    $ renpy.music.set_volume(1.0, 0.0, "voice5" )
    play sound2 sfx_parkday_birds fadein 2.0
    $ renpy.music.play(audio.music_breaking_news, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_breaking_news_radio, "music2", True, None, True, 0.0)
    scene sm1ms001-01 hr-reporting-park_c1 with dissolve
    play voice4 girl15_arrogant_heh1 noloop
    hr "Despite only existing for a few weeks, the Fetish Locator app devastated dozens of lives."
    hr "The application pretended to be a simple dating app - connecting people with similar sexual fetishes and offering them challenges."
    scene sm1ms001-01-01 hr-moves-towards-park-continues-report_c1 with dissolve
    play voice4 girl15_disappointed_ehh7 noloop
    hr "Behind the scenes it proved much more devious - manipulating and exploiting people for the sexual gratification of a single person."
    hr "It was the investigation of yours truly, with the help of a heroic male student at this college, that brought this dangerous abuse of technology to an end."
    scene sm1ms001-01-02 hr-finishes-report_c1 with dissolve
    play voice4 girl15_disappointed_ehh5 noloop
    hr "While the mastermind behind it is safely behind bars, we can only speculate at the traumatic experiences of the victims and how they may be coping."
    queue voice4 girl15_arrogant_okay_processed1 noloop
    $ renpy.music.set_volume(0.1, 7.8, "sound2" )
    $ renpy.music.set_volume(0.0, 2.5, "music" )
    $ renpy.music.set_volume(1.0, 1.5, "music2" )
    play sound ["<silence 4.4>", sfx_keyboard_enter1]
    play sound3 [sfx_camera_fly1, sfx_camera_fly1] volume 1.7 noloop fadein 3.0
    play sound4 ["<silence 2.0>", sfx_camera_fly1, sfx_camera_fly1] noloop volume 1.7
    show screen stop_sound_with_delay(4.4)
    scene sm1ms001-glambot-1 with dissolve
    hr "This is Hana Rivera, Channel Six News, reporting-"
    stop music fadeout 2.0
    stop music2 fadeout 2.0
    stop sound3 fadeout 2.0
    stop sound4 fadeout 2.0
    hide screen stop_sound_with_delay
    scene sm1ms001-01-04 sy-turns-laptop-towards-her_c1 with dissolve
    $ renpy.music.set_volume(1.0, 0.0, "music" )
    play music lofi4
    play voice3 stacy_angry noloop
    sy "She called you a \"heroic student\" this time. Each time it becomes less surprising that she forgets the rest of us."
    play voice2 d9s2_yeah noloop volume 2.5
    mo "I {i}was{/i} the only one of us they called as a witness in court."
    play sound sfx_drink_slurp3
    scene sm1ms001-01-05 mc-eating-cereal_c1 with dissolve
    pause
    scene sm1ms001-01-06 mc-sy-sitting-table-talking_c1 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "She could at least admit that AmRose and I helped."
    play voice2 mc_arrogant_heh1 noloop
    mo "What can I say? I'm the protagonist."
    play sound sfx_doorbell_lyssa
    scene sm1ms001-01-07 sound-door-mc-sy-turn_c1 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    pause
    scene sm1ms001-01-08 sy-wants-mc-open-door_c1 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Alright, mister protagonist. You can answer the door this time."
    play voice2 mc_arrogant_nah1 noloop
    scene sm1ms001-01-09 mc-goes-opens-door_c1 with dissolve
    pause
    play sound sfx_door_open1
    scene sm1ms001-01-10 mc-opens-door-tries-speak_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mo "Hi, how can I help-?"
    play sound sfx_cloth_rustling1
    scene sm1ms001-01-11 delivery-person-gives-mc-documents_c1 with dissolve
    play voice4 boy5_thinking_hm noloop
    "Delivery Person" "I have a parcel.{w} Sign here, please."
    play voice2 mc_thinking_oh1 noloop
    mo "Oh, sure."
    play sound sfx_pen_writing3 volume 2.5
    scene sm1ms001-01-12 mc-signs-name_c1 with dissolve
    pause
    jump name_input
label name_input:
    $ mcname = ""
    scene sm1ms001-01-12-01 paper-closeup_c1
    call screen name_input
    with dissolve
    jump name_done
label name_done:
    $ mcname = mcname.strip()
    if not mcname:
        call sm1ms001_set_name from _call_sm1ms001_set_name
    hide screen name_input
    scene sm1ms001-01-12-01 mc-returns-signed-clipboard_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Here you go."
    play voice4 boy5_thinking_mmf noloop
    "Delivery Person" "Thank you, uhh, Mr.{w} [mcname] Young."
    play sound sfx_door_closed2
    scene sm1ms001-01-13 mc-gives-package-sy_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "It is pretty lightweight.{w} Did you order an empty package?"
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh! Bring that here!! I've been waiting for that."
    scene sm1ms001-01-14 sy-puts-drive-computer-teases-mc_c1 with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "Thank you, [mcname]. You're my hero."
    play voice2 mc_arrogant_hm1 noloop
    mc "Are you still stuck on Hana's broadcast?{w} Stacy, she didn't even say my name."
    play sound sfx_gadgets_laptop_closed
    scene sm1ms001-01-15 sy-closes-laptop_c1 with dissolve
    play voice3 stacy_angryhuh noloop volume 1.4
    sy "Maybe she's just trying to keep you to herself."
    sy "Tempt you with fame and accolades and what she could do for you now that she's on TV."
    play voice2 mc_no_nah2 noloop
    if persistent.is_special is True:
        mc "No matter how famous I get, you know I could never forget about my sister."
    else:
        mc "We've known each other ever since we were kids. I could never forget about you - no matter how famous I get."
    play sound sfx_drink_slurp3
    scene sm1ms001-02 mc-eating-cereal-watches-tv_c1 with dissolve
    pause
    scene sm1ms001-09 sy-knew-mc-entire-life-where-she-ranks_c1 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Sure, but how do I know where I really rank among all those other people you've been with lately?"
    scene sm1ms001-10 mc-ask-who-spends-all-his-time-with_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Who am I living with and spending 99%% of my time with these days?"
    mc "Sure, there have been other women, but there has never been anyone like you."
    scene sm1ms001-11 sy-ask-what-about-arj-mc-never-any-competition_c1 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Yeah? What about AmRose? The three of us seemed inseparable."
    play voice2 mc_thinking_mmm4 noloop
    mc "There was never any competition between you two."
    play sound sfx_cloth_rustling2
    scene sm1ms001-12 sy-reminds-fl-database-mc-recaps-agreed-with-sy_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "Except when it came to what we did with the Fetish Locator database."
    play voice2 mc_yes_ugu1 noloop
    mc "And even then, I agreed with you. We kept the database."
    scene sm1ms001-13 sy-wishes-arj-stuck-she-determined-ghosted-them_c1 with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "Yeah, and AmRose... I wish she could have stuck around, but she was so damn stubborn."
    scene sm1ms001-14 mc-tells-sy-no-worries-arj-always-comes-back_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Don't worry too much about that, Stacy."
    mc "I've known AmRose for a few years now. She's impulsive and has a fiery temper, but she always comes back."
    scene sm1ms001-15 sy-worried-they-pushed-far-mc-tells-they-deleted-arj-files_c1 with dissolve
    play voice3 stacy_disappointed_oh2 noloop
    sy "I don't know, [mcname]. We might have pushed her too far this time."
    play voice2 mc_thinking_hmm1 noloop
    mc "You deleted all of the files with what she did for Fetish Locator, right?"
    scene sm1ms001-16 sy-explains-what-she-did-crushed-drive-at-machine-shop_c1 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "I never even copied them."
    sy "I even pulled that hard drive from the server room, took it apart with my toolkit, and shredded the platter over at the machine shop."
    scene sm1ms001-17 mc-surprised-they-have-machine-shop-sy-explains-he-good-to-know_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "We have a machine shop?"
    play voice3 stacy_yes_ugu1 noloop
    sy "Back when we were on campus, yeah. It's closed during Summer Break."
    mc "Good to know."
    scene sm1ms001-18 sy-ask-finished-breakfast-mc-has-clean-dish_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Have you finished your breakfast?"
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, I just need to wash up."
    play sound sfx_cup_slide1
    scene sm1ms001-19 sy-goes-over-list-item-one_c1 with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "Okay, then let's go over the list."
    sy "Item one - Clean up the space. I'll take care of that..."
    play voice2 mc_yes_aga1 noloop
    mc "Sounds good to me."
    scene sm1ms001-20 mc-fine-that-sy-wants-review-what-need-first-movie_c1 with dissolve
    play voice3 stacy_mmm2 noloop
    sy "...with your help."
    play voice2 mc_angry_hm1 noloop
    mct "Of course."
    sy "Then we'll review what we need for our first movie."
    play sound sfx_plates_moving1
    play sound3 sfx_tap_water1
    scene sm1ms001-21 mc-tells-sy-call-it-porn-she-prefers-adult-fiction_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "You can call it a porn film."
    play voice3 stacy_no_uhuh4 noloop
    sy "We will be creating Adult Fiction with Erotic content. Please don't call it porn."
    scene sm1ms001-22 mc-jokes-about-porn-games_c1 with dissolve
    play voice2 d4s4_mclaugh noloop volume 2.5
    mc "Sorta like how porn games refer to themselves as Adult Interactive Fiction..."
    stop sound3 fadeout 1.0
    play sound sfx_shower_off1
    scene sm1ms001-23 sy-shushes-mc_c1 with dissolve
    play voice3 stacy_shhh noloop
    sy "Shhh! That's enough from you on that subject."
    sy "Do you remember what you need to do while I convert this place into a professional film studio?"
    scene sm1ms001-24 mc-means-porn-studio-sy-corrects-its-not-porn-studio_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "You mean a porn studio?"
    play voice3 stacy_angry_breath1 noloop
    sy "It is not porn! We will be creating aesthetic and emotional feelings, not just erotic content!"
    scene sm1ms001-25 mc-ask-his-role-sy-silence_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "Fine! Fine. What's my role at this stage?"
    sy "..."
    scene sm1ms001-26 mc-ask-what-sy-he-never-listens-will-clean-up_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "What?"
    play voice3 stacy_arrogant_huh4 noloop
    sy "You never pay attention. Your first job is to help me clean this place up."
    play sound sfx_cleaning_floor2 volume 1.7
    scene sm1ms001-27 cleaning-montage-one_c1 with dissolve
    pause
    scene sm1ms001-28 cleaning-montage-two_c1 with dissolve
    pause
    stop sound fadeout 2.0
    scene sm1ms001-29 cleaning-montage-three_c1 with dissolve
    play voice3 stacy_happy_phew3 noloop
    pause
    play sound sfx_bed_slide2
    scene sm1ms001-30 cleaning-montage-four_c1 with dissolve
    pause
    scene sm1ms001-31 sy-likes-look-of-it-mc-ask-can-stop_c1 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "That looks good enough for now."
    play voice2 mc_thinking_hmm2 noloop
    mc "I can stop?"
    play sound sfx_cloth_rustling4
    scene sm1ms001-32 sy-agrees-mc-can-stop_c1 with dissolve
    play voice3 stacy_no_sad1 noloop
    sy "No...{w} Okay, fine. You can stop."
    play voice2 mc_happy_oof3 noloop
    mc "Praise be. I need some water."
    play sound sfx_camera_fly1 volume 1.7
    play sound3 ["<silence 2.5>", sfx_camera_fly1] noloop volume 1.7
    scene sm1ms001-glambot-2 with dissolve
    pause
    play voice2 stacy_arrogant_huh1 noloop
    sy "The next thing on the list... We need a camera."
    play voice2 mc_surprised_what1 noloop
    mc "What's wrong with our phones?"
    stop sound3 fadeout 1.0
    stop sound fadeout 1.0
    scene sm1ms001-34 sy-wants-quality-video-mc-guesses-they-broke_c1 with dissolve
    play voice3 stacy_hey_angry1 noloop
    sy "We need better quality. This all has to be done professionally."
    play voice2 mc_disappointed_ehh1 noloop
    mc "Let me guess. We don't have enough money on-hand to afford the camera you want."
    sy "Bingo."
    scene sm1ms001-35 mc-bingo-mc-guesses-look-jobs_c1 with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "Also, there's food, utility bills - water, electric, four railroads - not to mention rent."
    play voice2 mc_angry_huh1 noloop
    mc "Rent? I thought we were squatting in a condemned building."
    sy "This fine establishment is a bit of a fixer upper, but that's why we can afford it."
    sy "Each week, we need to have $[RENT_WEEKLY_AMOUNT] in the bank."
    mc "Understood."
    play sound sfx_cloth_rustling2
    scene sm1ms001-36 sy-suggests-simple-start-mc-ask-what-for-now_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I guess I can look at jobs around town."
    play voice3 stacy_yes_yap1 noloop
    sy "For now, try something simple. Like a delivery job."
    play voice2 mc_surprised_huh6 noloop
    mc "What do you mean, \"For now\"?"
    scene sm1ms001-37 sy-nothing-much-will-need-lot-stuff-mc-complains-he-will-work_c1 with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "Nothing much. We're going to need money for a lot of things."
    play voice2 mc_thinking_mmm2 noloop
    mc "And I'm going to be the only one working."
    scene sm1ms001-38 sy-tells-mc-will-work-outside-she-look-actresses_c1 with dissolve
    play voice3 stacy_no_uhuh3 noloop
    sy "You're going to be the only one working outside of these walls."
    sy "I'll continue fixing this place up. Also, I'll be looking for potential leads for actresses to work with you."
    scene sm1ms001-39 mc-ask-only-guy-in-porn-sy-stop-calling-them-porn_c1 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "I'm going to be the only guy in our porn films?"
    play voice3 stacy_angry_argh3 noloop
    sy "Stop calling them-"
    scene sm1ms001-40 sy-gives-up-calls-porn-mc-glad_c1 with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "Fine, yes. You'll be the only guy in our porn films.{w} At least as far as I have planned right now."
    play voice2 d3s11b_mcheh noloop volume 2.5
    mc "That's all you had to say."
    scene sm1ms001-41 mc-will-work-delivery-sy-tells-she-will-do-marketing_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Alright, I'll go looking for something simple that has decent pay - like a delivery job."
    play voice3 stacy_yes_yap3 noloop
    sy "Perfect. If you need me, I'll be managing the business from here."
    scene sm1ms001-42 mc-point-out-business-major-sy-jokes-now-delivery-boy_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "What? I was a business management major!"
    play voice3 stacy_yeahno noloop
    sy "And now you're a delivery boy. Go make us some money!"
    play sound sfx_heels_steps1 loop
    scene sm1ms001-43 sy-walks-towards-computer-end-scene_c1 with dissolve
    pause
    call sm1ms001_add_override_interaction_option from _call_sm1ms001_add_override_interaction_option
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 2.0, "music" )
    $ renpy.music.set_volume(1.0, 2.0, "music2" )
    $ renpy.music.set_volume(1.0, 2.0, "sound" )
    $ renpy.music.set_volume(1.0, 2.0, "sound2" )
    $ renpy.music.set_volume(1.0, 2.0, "sound3" )
    $ renpy.music.set_volume(1.0, 2.0, "sound4" )
    $ renpy.music.set_volume(1.0, 2.0, "sound5" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(MS, 1, 0, 0)
    return
label sm1ms001_set_name:
    $ mcname = _("Mike")
    return
label sm1ms001_add_override_interaction_option:
    $ LocationController.get_location(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM).add_override_interaction_option("io-SD_Peek_On_Stacy")
    return
label sm1ms001_unlocks:
    call sm1ms001_add_override_interaction_option from _call_sm1ms001_add_override_interaction_option_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MS)
    return