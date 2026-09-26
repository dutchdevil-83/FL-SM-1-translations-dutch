image sm1fs-i002-glambot-1 = Movie(play = "images/FS_IT/s002/anim/sm1fs-i002-a03-2x-60fps.webm", start_image = "sm1fs-i002-a03 glambot-000", image = "sm1fs-i002-a03 glambot-108", loop = False)
label sm1fs_i002:
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1fs-i002-01 mc-enters-it-office-cw-next-to-entrance_c1 with dissolve
    $ renpy.music.set_volume(0.7, 0.0, "music" )
    play music take_the_ride_calm
    pause
    scene sm1fs-i002-02 cw-greets-mc-ask-if-him-he-tells-yes_c1 with dissolve
    play voice3 girl29_thinking_hmm3 noloop
    cw "You must be [mcname]."
    play sound ["<silence 0.25>", sfx_camera_fly1] volume 2.0
    scene sm1fs-i002-glambot-1 with dissolve
    pause
    stop sound fadeout 1.0
    play sound2 sfx_cloth_rustling1 noloop
    scene sm1fs-i002-03 handshake-cw-introduces-herself-her-position_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I am."
    play voice3 girl29_yes_aga2 noloop
    cw "My name is Claire Watts, during business hours I prefer Ms. Watts however."
    cw "I am the division head for Cloud User Management here at Orbix."
    play voice2 mc_happy_a1 noloop
    mc "It's wonderful to meet you Ms. Watts."
    scene sm1fs-i002-04 mc-great-meeting-cw-she-smiles-follow-me_c1 with dissolve
    play voice3 girl29_arrogant_ha noloop
    cw "Great. Follow me."
    scene sm1fs-i002-05 mc-cw-walk-through-office-approach-meeting-room_c1 with dissolve
    play voice3 girl29_thinking_mmm1 noloop
    cw "All right Mr. [mcname] Young, it seems you've passed the proficiency test."
    play voice2 mc_yes_yeah2 noloop
    mc "I did."
    play sound sfx_door_open5
    scene sm1fs-i002-06 cw-opens-door-meeting-room-taken_c1 with dissolve
    pause
    scene sm1fs-i002-07 cw-suggest-using-another-meeting-room_c1 with dissolve
    play voice3 girl29_thinking_hmm5 noloop
    cw "Which means you are technically qualified to work here at Orbix."
    play voice2 mc_arrogant_huh3 noloop
    mc "Technically?"
    scene sm1fs-i002-08 ag-thumbs-up-encourages-mc_c1 with dissolve
    pause
    play sound sfx_door_closed7
    scene sm1fs-i002-09 cw-mc-walk-to-other-meeting-room_c1 with dissolve
    play voice3 girl29_yes_questioning noloop
    cw "Yes, technically. My job today is to see if you'll be a good fit for the team and for the company."
    play sound sfx_door_open6
    scene sm1fs-i002-10 mc-opens-door-for-cw-enters-meeting-room-mc-follows-her_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, I see. This is part of that '21st century company' thing that Anna told me about."
    play voice3 girl29_yes_aga1 noloop
    cw "That's correct."
    $ renpy.music.set_volume(0.2, 2.0, "sound2" )
    play sound sfx_door_closed10
    scene sm1fs-i002-11 mc-cw-take-sit-cw-talk-mc-passed-first-interview_c1 with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "Unlike many of our competitors, we value our employees. We want to ensure that work is just one part of your life."
    scene sm1fs-i002-12 cw-technically-mc-qualified-work-orbix-mc-ask-technically_c1 with dissolve
    cw "We try to avoid the crunch and burnout. Our goals are instead to foster healthy work habits and grow company loyalty."
    scene sm1fs-i002-14 cw-value-employees-unlike-competators-aim-healthy-work-habits_c1 with dissolve
    play voice3 girl29_hey_happy noloop
    cw "So tell me a little bit of yourself."
    play voice2 d2s9_confused noloop volume 1.6
    mc "Well, uhm-"
    scene sm1fs-i002-13 cw-explains-her-job-determine-mc-compatibility-team_c1 with dissolve
    play voice3 girl29_thinking_oh noloop
    cw "And remember, this is the part of the interview where you convince me to hire you."
    scene sm1fs-i002-15 cw-wants-mc-tell-about-herself_c1 with dissolve
    if player.get_choice("sm1fs_i001_books") is True:
        play voice2 mc_thinking_hmm2 noloop
        mc "Well I love reading."
        scene sm1fs-i002-16 books-mc-loves-reading_c1 with dissolve
        play voice3 girl29_thinking_hmm4 noloop
        cw "Anything in particular?"
        play voice2 mc_no_no2 noloop
        mc "No, I'll read pretty much everything. I think... The last thing I read was 'Start with How'."
    elif player.get_choice("sm1fs_i001_sports") is True:
        play voice2 mc_thinking_hmm2 noloop
        mc "I always enjoy turning on a sports game."
        scene sm1fs-i002-17 sports-mc-loves-sports-mostly-basketball_c1 with dissolve
        play voice3 girl29_thinking_hmm4 noloop
        cw "Any particular sport?"
        play voice2 mc_arrogant_hm1 noloop
        mc "I used to like basketball but... Nowadays I like baseball and volleyball most."
    elif player.get_choice("sm1fs_i001_gaming") is True:
        play voice2 mc_thinking_hmm2 noloop
        mc "I've always loved playing video games."
        scene sm1fs-i002-18 videogames-mc-loves-gaming-stereotype-but-likes_c1 with dissolve
        play voice3 girl29_thinking_hmm4 noloop
        cw "That's fairly typical in this industry."
        play voice2 mc_arrogant_hm1 noloop
        mc "I know it's a bit of a stereotype, but you like what you like."
    elif player.get_choice("sm1fs_i001_cars") is True:
        play voice2 mc_thinking_hmm2 noloop
        mc "I'm actually hoping to find a car to work on."
        scene sm1fs-i002-19 cars-mc-looking-for-car-minor-restorations_c1 with dissolve
        play voice3 girl29_surprised_oh noloop
        cw "Oh really?"
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah. Something small, maybe a tune up or minor restoration."
    scene sm1fs-i002-20 cw-sits-up-ask-how-unwind_c1 with dissolve
    play voice3 girl29_thinking_mmm2 noloop
    cw "Well that's great. What about after work? How do you unwind after a stressful day?"
    menu:
        "Going out"(hint="sm1fs_i002_m01_h01"):
            call sm1fs_i002_m01_c01 from _call_sm1fs_i002_m01_c01
            scene sm1fs-i002-21 mc-loves-going-out-somewhere-good-music_c1 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "I love going out for a drink."
            play voice3 girl29_happy_relief noloop
            cw "You don't say."
            mc "Yeah, and if it's somewhere with good music, even better."
        "Online shopping"(hint="sm1fs_i002_m01_h02"):
            call sm1fs_i002_m01_c02 from _call_sm1fs_i002_m01_c02
            scene sm1fs-i002-22 online-shopping-mc-fashion-trends-cw-impressed-on-same-page_c1 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "I might do a little online shopping. I'm always trying to stay up with the latest fashion trends."
            play voice3 girl29_yes_happy noloop
            cw "A little online shopping never hurt anyone."
            mc "Exactly!"
        "Watching TV"(hint="sm1fs_i002_m01_h03"):
            call sm1fs_i002_m01_c03 from _call_sm1fs_i002_m01_c03
            scene sm1fs-i002-23 watching-tv-mc-happy-chill-cw-not-impressed-it-helps-relax_c1 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "I like to just plop on the couch, kick my shoes off, and turn on some mindless tv."
            play voice3 girl29_disappointed_eh noloop
            cw "There's nothing better to do with your time?"
            mc "All I know is that it helps me relax."
        "Playing video games"(hint="sm1fs_i002_m01_h04"):
            call sm1fs_i002_m01_c04 from _call_sm1fs_i002_m01_c04
            scene sm1fs-i002-24 gaming-mc-relaxes-playing-games-cw-stereotype-mc-not-bad-one_c1 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "Sometimes when I get stressed I like to play video games."
            play voice3 girl29_disappointed_ehh noloop
            cw "What a stereotypical IT employee response."
            mc "I don't think that's necessarily bad though."
    scene sm1fs-i002-25 cw-looks-laptop-anna-mentioned-something-mc-ask-which-part_c1 with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "That's good. It's important to Orbix that we have employees with well rounded lives."
    scene sm1fs-i002-26 cw-any-part-mc-begins-involved-app-cw-ask-what-app_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Hmm, that is an unusual requirement..."
    play voice3 girl29_yes_serious noloop
    cw "For us a well rounded individual brings a lot of value to Orbix."
    scene sm1fs-i002-25 cw-looks-laptop-anna-mentioned-something-mc-ask-which-part_c1 with dissolve
    play voice3 girl29_disappointed_oh noloop
    cw "Now that we're through that. Anna mentioned something in her interview with you about why you got interested in IT. Care to explain?"
    play voice2 mc_thinking_hmm5 noloop
    mc "Which part?"
    cw "Any of it really. Sounds... Highly unusual at the very least."
    scene sm1fs-i002-28 mc-rather-not-say-cw-not-ideal-continue_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "I got involved with this app-"
    play voice3 girl29_arrogant_huh noloop
    cw "What kind of an app?"
    menu:
        "Dating"(hint="sm1fs_i002_m02_h01"):
            call sm1fs_i002_m02_c01 from _call_sm1fs_i002_m02_c01
            scene sm1fs-i002-18 videogames-mc-loves-gaming-stereotype-but-likes_c1 with dissolve
            play voice2 d1s5_mchappy noloop volume 1.8
            mc "I guess you could call it a dating app."
            play voice3 girl29_yes_aga1 noloop
            cw "Okay, continuing on."
        "Party"(hint="sm1fs_i002_m02_h02"):
            call sm1fs_i002_m02_c02 from _call_sm1fs_i002_m02_c02
            scene sm1fs-i002-18 videogames-mc-loves-gaming-stereotype-but-likes_c1 with dissolve
            play voice2 d1s5_mchappy noloop volume 1.8
            mc "It was a way for me to find parties."
            play voice3 girl29_yes_aga3 noloop
            cw "Parties? Really... I'm interested, keep going."
        "Kinky"(hint="sm1fs_i002_m02_h03"):
            call sm1fs_i002_m02_c03 from _call_sm1fs_i002_m02_c03
            scene sm1fs-i002-18 videogames-mc-loves-gaming-stereotype-but-likes_c1 with dissolve
            play voice2 d1s5_mchappy noloop volume 1.8
            mc "The app was based around kinks and-"
            scene sm1fs-i002-26 cw-any-part-mc-begins-involved-app-cw-ask-what-app_c1 with dissolve
            play voice3 girl29_angry_argh1 noloop
            cw "Mr. Young! We're at work and I'd ask you refrain from talking about that part of your personal life."
            play voice2 mc_pain_ou1 noloop
            mc "I'm sorry Ms. Watts."
            cw "It's fine, lets just try to keep it... Less personal than that. Continue on."
        "I'd rather not say"(hint="sm1fs_i002_m02_h04"):
            call sm1fs_i002_m02_c04 from _call_sm1fs_i002_m02_c04
            scene sm1fs-i002-18 videogames-mc-loves-gaming-stereotype-but-likes_c1 with dissolve
            play voice2 mc_no_nah2 noloop
            mc "I'd rather not talk about the app."
            scene sm1fs-i002-26 cw-any-part-mc-begins-involved-app-cw-ask-what-app_c1 with dissolve
            play voice3 girl29_happy_laugh2 noloop
            cw "Avoidant? Not the best strategy, but continue."
    scene sm1fs-i002-31 mc-explains-business-school-cw-ask-finish-college_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "After I had it for awhile I... Realized it could be made better."
    mc "I learned a few things that made me realize that I kind of enjoyed doing IT work."
    scene sm1fs-i002-17 sports-mc-loves-sports-mostly-basketball_c1 with dissolve
    play voice3 girl29_surprised_ah noloop
    cw "This is relatively new then?"
    play voice2 mc_yes_yes1 noloop
    mc "Yes. To be totally honest, it's a pretty radical shift in what I planned to do with my life."
    cw "What was the plan?"
    scene sm1fs-i002-21 mc-loves-going-out-somewhere-good-music_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I was in college for business."
    scene sm1fs-i002-32 cw-changes-pose-mc-sees-her-panties_c1 with dissolve
    play voice3 girl29_thinking_hm noloop
    cw "Did you finish college?"
    play voice2 mc_no_no5 noloop
    mc "No..."
    scene sm1fs-i002-33 cw-explains-why-good-fit_c1 with dissolve
    play voice3 girl29_happy_laugh1 noloop
    cw "You'll fit right in, don't worry Mr. Young."
    play voice2 d1s2_hmm noloop volume 2.0
    mc "Why do you say that?"
    play sound sfx_cloth_rustling2
    scene sm1fs-i002-35 good-question-cw-starts-explaining_c1 with dissolve
    play voice3 girl29_yes_yeah noloop
    cw "Plenty of people at Orbix dropped out from college. Some never even went."
    cw "Like we've said. We're more interested in our employees than in degrees or accolades."
    scene sm1fs-i002-34 cw-stands-up-no-more-questions-mc-any-he-ask-his-duties_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "That's good to know."
    scene sm1fs-i002-36 cw-tells-ag-new-team-lead-team-up-running-right-away_c1 with dissolve
    play voice3 girl29_arrogant_he noloop
    cw "I think that's most of my questions for you Mr. Young. Did you have any for me?"
    play voice2 mc_thinking_hmm1 noloop
    mc "What exactly would I be doing?"
    cw "That's a good question. Here at Orbix we're rapidly expanding our division to reflect the growth of the company."
    cw "As a part of that growth, we've had to expand our teams."
    scene sm1fs-i002-38 cw-ask-other-questions-mc-ask-when-can-start_c1 with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "Anna, who you interviewed with already, is our newest team lead. She was promoted from within and is in need of a new team."
    cw "Especially considering that we have enough interest to get her team up and running immediately."
    play voice2 mc_happy_a1 noloop
    mc "And I would be a part of Anna's team?"
    play voice3 girl29_yes_arrogant noloop
    cw "That's correct. You'd be working under her. I see your main task as helping Anna complete her project goals."
    cw "Most of your job would be coding, but it will be up to her discretion under my supervision."
    cw "Any other questions?"
    play voice2 mc_thinking_hmm4 noloop
    mc "Just when can I start?"
    scene sm1fs-i002-39 cw-hold-horses-no-decision-mc-misunderstood_c1 with dissolve
    play voice3 girl29_no_uhuh noloop
    cw "Hold your horses there. I haven't made a final decision yet."
    play voice2 mc_disappointed_off2 noloop
    mc "I thought-"
    cw "You've pitched me on the idea of hiring you Mr. Young. Now I need to think about it."
    cw "We've had a lot of applicants and we're currently only hiring two people."
    mc "I see."
    scene sm1fs-i002-40 cw-reminds-just-pitched-idea-only-hiring-two-people_c1 with dissolve
    play voice3 girl29_arrogant_ha noloop
    cw "If we do decide to hire you, you'll be placed in our rapidly expanding Cloud User Management division."
    play voice2 mc_yes_okay3 noloop
    mc "That sounds great."
    play voice3 girl29_disgust_meh noloop
    cw "If we do decide to hire you, you don't need to wear something so... Stiff."
    scene sm1fs-i002-37 mc-ask-he-on-her-team-cw-confirms_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Is something wrong with my outfit?"
    play voice3 girl29_thinking_mmm2 noloop
    cw "Well... The office is a bit more casual than a tucked in button up shirt. Plus, it's not really doing anything for you."
    mc "You sound like you know what you're talking about."
    scene sm1fs-i002-41 decision-tomorrow-will-give-call_c1 with dissolve
    play voice3 girl29_arrogant_hm noloop
    cw "As time goes on, you'll realize I almost always do."
    scene sm1fs-i002-42 mc-stands-up-thanks-cw-welcome_c1 with dissolve
    play voice3 girl29_yes_aga2 noloop
    cw "I will be making a final decision by tomorrow morning."
    cw "After I've made my decision [gt.next_day!t] by 8:00 am I'll give you a call."
    play sound sfx_door_open6 volume 1.5
    scene sm1fs-i002-43 mc-leaves-meeting-room-will-wait-cw-call-she-smiles_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Thank you Claire- sorry, Ms. Watts."
    play voice3 girl29_thinking_hmm5 noloop
    cw "You're welcome Mr. [mcname] Young."
    mc "I look forward to your call at [gt.next_day!t] 8:00 am!"
    scene sm1fs-i002-44 mc-leaves-office-sees-ag_c1 with dissolve
    pause
    scene sm1fs-i002-45 mc-thumbs-up-ag_c1 with dissolve
    pause
    scene sm1fs-i002-46 mc-leaves-it-office_c1 with dissolve
    pause
    stop music fadeout 3.0
    stop sound2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(IT_STORY_LINE, 8, 0, 2)
    call sm1fs_i002_quest_line_unlock from _call_sm1fs_i002_quest_line_unlock
    return
label sm1fs_i002_m01_c01:
    $ player.set_choice("sm1fs-i002_going_out")
    $ CharacterController.get_character("cw").add_point()
    $ CharacterController.get_character("cw").discover_topic(TOPIC_FOOD_AND_DRINK)
    return
label sm1fs_i002_m01_c02:
    $ player.set_choice("sm1fs-i002_online_shopping")
    $ CharacterController.get_character("cw").discover_topic(TOPIC_FASHION)
    return
label sm1fs_i002_m01_c03:
    $ player.set_choice("sm1fs-i002_watching_tv")
    return
label sm1fs_i002_m01_c04:
    $ player.set_choice("sm1fs-i002_video_games")
    return
label sm1fs_i002_m02_c01:
    $ player.set_choice("sm1fs-i002_dating_app")
    return
label sm1fs_i002_m02_c02:
    $ player.set_choice("sm1fs-i002_party_app")
    $ CharacterController.get_character("cw").add_point()
    $ CharacterController.get_character("cw").discover_topic(TOPIC_FOOD_AND_DRINK)
    return
label sm1fs_i002_m02_c03:
    $ player.set_choice("sm1fs-i002_kinky_app")
    return
label sm1fs_i002_m02_c04:
    $ player.set_choice("sm1fs-i002_dont_say")
    return
label sm1fs_i002_quest_line_unlock:
    $ StoryController.activate_story_line(MS, True)
    return
label sm1fs_i002_unlocks:
    call sm1fs_i002_m01_c01 from _call_sm1fs_i002_m01_c01_1
    call sm1fs_i002_m02_c02 from _call_sm1fs_i002_m02_c02_1
    if config_storyline_mode is True:
        $ execute_storyline_config(IT_STORY_LINE)
    return