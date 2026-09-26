image sm1cs_kv002-glambot-1 = Movie(play = "images/Character-Scenes/kv/s002/anim/sm1cs-kv002-a01-2x-60fps.webm", start_image = "sm1cs-kv002-a01 mc-walk-into-dojo-glambot-01-000", image = "sm1cs-kv002-a01 mc-walk-into-dojo-glambot-01-358", loop = False)
image sm1cs_kv002-glambot-2 = Movie(play = "images/Character-Scenes/kv/s002/anim/sm1cs-kv002-a38-01-2x-50fps.webm", start_image = "sm1cs-kv002-a38-01 ms-walks-back-studio-glambot-38-01-00_i", image = "sm1cs-kv002-a38-01 ms-walks-back-studio-glambot-38-01-79_i", loop = False)
image sm1cs_kv002-glambot-3 = Movie(play = "images/Character-Scenes/kv/s002/anim/sm1cs-kv002-a38-02-2x-50fps.webm", start_image = "sm1cs-kv002-a38-02 ms-walks-back-studio-glambot-38-02-00_i", image = "sm1cs-kv002-a38-02 ms-walks-back-studio-glambot-38-02-79_i", loop = False)
label sm1cs_kv002:
    $ renpy.music.set_volume(0.8, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_blind_date
    scene sm1cs-kv002-a01 mc-walk-into-dojo-glambot-01-000 with dissolve
    pause
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound ["<silence 0.5>", sfx_camera_fly1] volume 2.5
    play sound2 ["<silence 3.2>", sfx_camera_fly1] noloop volume 2.5
    scene sm1cs_kv002-glambot-1
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(0.5, 1.5, "music" )
    scene sm1cs-kv002-02 mc-walks-closer-kv-responds_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey Kanya."
    play voice3 kanya_hey_arrogant noloop
    kv "Hey [mcname]. Haha. You have a talent for showing up just at the end of my shoots."
    scene sm1cs-kv002-03 mc-what-can-say-kv-like-heads-up-next-time_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "What can I say?"
    play voice3 kanya_thinking_hmm1 noloop
    kv "That you'll give me some heads up next time so we can just hang out?"
    play sound sfx_skirt_off2
    scene sm1cs-kv002-04 mc-promises-kv-grab-seat-while-finish_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "I promise to next time."
    play voice3 kanya_arrogant_yeah noloop
    kv "Good. Grab a seat while I finish this up."
    scene sm1cs-kv002-05 kv-asking-ms-okay-she-totaly-fine_c1 with dissolve
    play voice3 kanya_disappointed_oh noloop
    kv "As long as that's cool with you."
    play voice4 girl26_yes_aga noloop
    "Model" "Sure, I totally don't care. Super cool with me. Uh huh."
    scene sm1cs-kv002-06 mc-sits-next-kv-camera-ms-prepared-shoot_c1 with dissolve
    pause
    scene sm1cs-kv002-07 ms-photoshoot-pose-one_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv002-08 ms-strikes-better-pose_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv002-09 mct-where-he-know-model-from_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mct "Why does she look kind of familiar?"
    scene sm1cs-kv002-10 ms-bends-over-stool_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv002-11 kv-talk-mc-while-taking-photos_c1 with dissolve
    play voice3 kanya_hey_long noloop
    kv "Did you learn a little bit about photography since I saw you last?"
    play voice2 mc_yes_yeah4 noloop
    mc "I think so. Not sure how much of it stuck, but I read that book you recommended!"
    scene sm1cs-kv002-12 kv-ask-about-iso-mc-didnt-know-there-be-test_c1 with dissolve
    play voice3 kanya_arrogant_laugh noloop
    kv "Great, what's an ISO?"
    play voice2 d1s5b_emmm noloop
    mc "Wait, I didn't know there was a test!"
    scene sm1cs-kv002-13 kv-wink-ask-again-mc-answer_c1 with dissolve
    play voice3 kanya_arrogant_huh noloop
    kv "Art is all about suffering. Now come on, what's an ISO?"
    play voice2 mc_disappointed_ehh1 noloop
    mc "The sensitivity of the sensor to light."
    play voice3 kanya_yes_yeah2 noloop
    kv "That's correct!"
    scene sm1cs-kv002-14 kv-makes-kiss-face-camera_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv002-15 kv-ask-dof-mc-f-stop-kv-correct_c1 with dissolve
    play voice3 kanya_arrogant_ha noloop
    kv "How do you determine what your depth of field is?"
    play voice2 mc_thinking_mmm5 noloop
    mc "F Stop?"
    play voice3 kanya_yes_aga1 noloop
    kv "That's right!"
    scene sm1cs-kv002-16 kv-looking-her-camera-killing-it-mc-thanks_c1 with dissolve
    play voice3 kanya_surprised_ohmy noloop
    kv "You're killing it in front of the camera, by the way."
    play voice4 girl26_happy_laugh2 noloop
    "Model" "Thanks, Kanya."
    scene sm1cs-kv002-17 kv-takes-another-photo_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv002-18 kv-last-question-mc-answer-correct-again_c1 with dissolve
    play voice3 kanya_hey_simple2 noloop
    kv "Last Question; when do you start to see lens distortion from your focal length, often called the 'fishbowl effect'?"
    play voice2 mc_thinking_hmm4 noloop
    mc "Under 35mm, right?"
    play voice3 kanya_yes_yep1 noloop
    kv "Yep! Once you're under 35mm you start to see distortion in the corners."
    scene sm1cs-kv002-19 kv-looking-at-camera-deff-read-book_c1 with dissolve
    play voice3 kanya_thinking_hmm3 noloop
    kv "I mean, you definitely read the book which is great."
    scene sm1cs-kv002-20 kv-ask-turn-theory-practice-mc-what_c1 with dissolve
    kv "But I just had a fun idea. Why don't you try to take some of that theory and turn it into practice?"
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    play voice3 kanya_disappointed_hm noloop
    kv "Well I got all the photos I need, and I feel good about it. So if it's okay with her, she could do some modelling for us and you can try getting behind the camera."
    scene sm1cs-kv002-21 kv-why-not-asking-ms-cool-with-it_c1 with dissolve
    play voice3 kanya_hey_simple1 noloop
    kv "You cool with that?"
    scene sm1cs-kv002-22 ms-unsure-kv-free-photos_c1 with dissolve
    play voice4 girl26_thinking_ehh2 noloop
    "Model" "Didn't think I was going to be helping some new photographer today."
    play voice3 kanya_arrogant_pff noloop
    kv "It's some free photos! Besides, after you see them you'll understand why I charge what I do."
    scene sm1cs-kv002-23 ms-good-point-kv-cool-mc-grab-cam_c1 with dissolve
    play voice4 girl26_arrogant_hah noloop
    "Model" "Eh, good point. Sure, why not. It's better than going back to my shitty job."
    play voice3 kanya_yes_yeah1 noloop
    kv "Cool. [mcname], come grab the camera."
    play sound sfx_remote_button1 volume 2.0
    scene sm1cs-kv002-24 mc-gets-camera-kv-stands-behind-him-tells-him-about-shutter-button_c1 with dissolve
    play voice3 kanya_thinking_eeh5 noloop
    kv "Okay so that's the shutter release button. You know, to take the pictures."
    kv "That's how you control the shutter speed. That one is for your f stop."
    scene sm1cs-kv002-25 kv-talk-approach-viewfinder-composition_c1 with dissolve
    play voice3 kanya_happy_laugh3 noloop
    kv "But everything should be pretty set for you. Just need to point and shoot!"
    kv "But don't actually point and shoot. Look through the viewfinder and compose your shots."
    scene sm1cs-kv002-26 mc-okay-kv-will-do-great_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Uhm, okay."
    scene sm1cs-kv002-27 kv-arm-mc-shoulder-can-do-it_c1 with dissolve
    play voice3 kanya_disappointed_oof noloop
    kv "You've got nothing to worry about, you'll do great."
    kv "Show me what you've got."
    scene sm1cs-kv002-28 mc-shoots-first-pose-ms_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv002-29 mc-shoots-another-pose_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv002-30 mc-sees-ms-pussy-thinks-holy-shit_c1 with dissolve
    mct "Holy shit..."
    scene sm1cs-kv002-31 ms-looking-mc-want-close-up_c1 with dissolve
    play voice2 mc_pain_ffff noloop
    mc "Uhhh..."
    scene sm1cs-kv002-32 choice-menu-screen_c1 with dissolve
    play voice3 kanya_yes_aga4 noloop
    kv "She wants you to get a close up."
    menu:
        "Okay"(hint="sm1cs_kv002_m01_h01"):
            call sm1cs_kv002_m01_c01 from _call_sm1cs_kv002_m01_c01
            scene sm1cs-kv002-33 mc-choice-okay-he-agrees-kv-do-what-client-wants_c1 with dissolve
            play voice2 mc_thinking_oh1 noloop
            mc "Oh, I guess."
            play voice3 kanya_disappointed_ohh noloop
            kv "Got to do what the client wants!"
            scene sm1cs-kv002-34 mc-takes-shot-ms-pussy_c1 with dissolve
            play voice2 mc_pain_mff1 noloop
            mct "Here goes nothing."
            scene sm1cs-kv002-35 pussy-shot-close-up_c1 with dissolve
            play sound sfx_photocamera_flash2
            "*CLICK*"
        "I don't know..."(hint="sm1cs_kv002_m01_h02"):
            scene sm1cs-kv002-36 choice-don_t-know-mc-unsure-kv-fine-but-in-future-he-have-to_c1 with dissolve
            play voice2 d2s12_emmm noloop
            mc "Do... We have to?"
            play voice3 kanya_no_simple2 noloop
            kv "No, but in the future you might have to. But we can skip it today."
            play voice2 mc_yes_okay3 noloop
            mc "Okay, cool."
    scene sm1cs-kv002-37 ms-ask-about-photos-mc-thinks-good_c1 with dissolve
    play voice4 girl26_thinking_hmm1 noloop
    "Model" "Great, how do you feel about the photos?"
    play voice2 d2s9_confused noloop volume 1.7
    mc "Good? I think?"
    play voice4 girl26_happy_laugh1 noloop
    "Model" "Awesome. I have to get to work now. See ya' around!"
    play sound sfx_heels_steps1_slow
    scene sm1cs_kv002-glambot-2 with dissolve
    stop sound fadeout 7.5
    play voice2 mc_thinking_mmm4 noloop
    mct "I swear I know her from somewhere..."
    play sound sfx_heels_steps1_slow
    scene sm1cs_kv002-glambot-3 with dissolve
    stop sound fadeout 7.5
    pause
    scene sm1cs-kv002-39 kv-checks-mc-photos-not-bad-mc-ask-really_c1 with dissolve
    play voice3 kanya_surprised_wowohmy noloop
    kv "Not bad, not bad at all. Still have a little bit more to learn, but it looks like you've got an eye for photography."
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Really?"
    scene sm1cs-kv002-40 kv-explains-mc-proud-himself_c1 with dissolve
    play voice3 kanya_yes_yeah3 noloop
    kv "Yeah! With a little bit of training you could be a really good photographer I think."
    scene sm1cs-kv002-41 not-always-hot-naked-people-sometimes-weddings_c1 with dissolve
    play voice2 mc_happy_wooh3 noloop
    mc "If I get to take photos of hot naked chicks all day, I'm in!"
    play voice3 kanya_happy_laugh2 noloop
    kv "It's not always hot naked people. Sometimes it's weddings and bar mitzvahs."
    scene sm1cs-kv002-42 menu-choice-screen_c1 with dissolve
    menu:
        "You must get bored at those"(hint="sm1cs_kv002_m02_h01"):
            call sm1cs_kv002_m02_c01 from _call_sm1cs_kv002_m02_c01
            scene sm1cs-kv002-43 mc-responds_c1 with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "Oh, that seems way less fun."
            play voice3 kanya_yes_long noloop
            kv "But it pays my rent, so I'm not complaining."
        "Beats sitting in an office"(hint="sm1cs_kv002_m02_h02"):
            scene sm1cs-kv002-43 mc-responds_c1 with dissolve
            play voice2 mc_disappointed_ah2 noloop
            mc "I'd take a bar mitzvah over a cubicle any day."
            play voice3 kanya_yes_long noloop
            kv "That's exactly how I feel!"
    scene sm1cs-kv002-44 kv-walks-towards-back-area-talk-mc_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Then what do you do the naked stuff for?"
    play voice3 kanya_thinking_eeh1 noloop
    kv "It pays a little bit. And it's waaaaay more fun than the other stuff."
    mct "Shit, if it's like today I believe that."
    play sound sfx_plate_place1
    scene sm1cs-kv002-45 kv-puts-stuff-table-got-talent-open-studio_c1 with dissolve
    play voice3 kanya_thinking_hmm4 noloop
    kv "Well, you've definitely got a good eye. It's no Guy Bourdin, but there's a bit of talent in these photos."
    kv "Maybe you do have what it takes to open a porn studio."
    scene sm1cs-kv002-46 mc-that-dream-kv-thinks-should-check-it-mc-hell-yeah_c1 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "It is the dream."
    play voice3 kanya_hey_attention noloop
    kv "I think I should stop by and check it out."
    play voice2 mc_happy_yes1 noloop
    mc "Hell yeah."
    play sound sfx_bed_slide3 volume 0.6
    scene sm1cs-kv002-47 kv-laughs-ridiculous-mc-prob-best-trait_c1 with dissolve
    play voice3 kanya_happy_laugh1 noloop
    kv "You're ridiculous."
    play voice2 d9s2_yeah noloop volume 1.9
    mc "It's probably my best trait, if I'm honest."
    scene sm1cs-kv002-48 kv-not-sure-best-trait-but-up-there-mct-flirting_c1 with dissolve
    play voice3 kanya_disappointed_neh noloop
    kv "I don't know if it's your {i}best{/i} trait, but it's up there."
    mct "Is she... Flirting with me?"
    scene sm1cs-kv002-49 kv-let-know-when-stop-by-mc-deff-types-on-phone_c1 with dissolve
    play voice3 kanya_happy_relief3 noloop
    kv "You just let me know when I can stop by."
    play voice2 mc_yes_sure1 noloop
    mc "Definitely! I'll call you. In fact..."
    play sound sfx_message_in1
    scene sm1cs-kv002-50 kv-checks-phone-mc-his-address-kv-will_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "That's my address. Send me a message when you want to stop by."
    play voice2 kanya_disappointed_hm noloop
    kv "Oh, I will!"
    scene sm1cs-kv002-51 kv-has-other-session-will-have-to-go-soon-mc-shit-sorry_c1 with dissolve
    play voice3 kanya_thinking_eeh3 noloop
    kv "But I've actually got to get going. I've got an at home session to run too."
    play voice2 mc_pain_ou1 noloop
    mc "Oh, shit, sorry!"
    kv "Don't worry about it. It's a long time client of mine and... It's a bit of an unusual shoot. But you should give me a call soon!"
    scene sm1cs-kv002-52 mc-start-leaving-he-will-kv-he-better_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "I will!"
    play voice3 kanya_arrogant_huh noloop
    kv "You better!"
    scene sm1cs-kv002-53 kv-gives-flirty-smile-as-mc-leaves_c1 with dissolve
    pause
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(KV_STORY, 2, 0, 3)
    return
label sm1cs_kv002_m01_c01:
    $ player.set_choice("sm1cs_kv002_close_up")
    return
label sm1cs_kv002_m02_c01:
    $ player.set_choice("sm1cs_kv002_get_bored")
    return
label sm1cs_kv002_unlocks:
    call sm1cs_kv002_m01_c01 from _call_sm1cs_kv002_m01_c01_1
    call sm1cs_kv002_m02_c01 from _call_sm1cs_kv002_m02_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(KV_STORY)
    return