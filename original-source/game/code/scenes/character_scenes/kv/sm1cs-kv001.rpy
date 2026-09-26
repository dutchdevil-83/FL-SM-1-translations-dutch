image sm1cs_kv001-glambot-1 = Movie(play = "images/Character-Scenes/kv/s001/anim/sm1cs-kv001-a01-2x-50fps.webm", start_image = "sm1cs-kv001-a01 mc-walks-into-dojo-glambot-01-000_i", image = "sm1cs-kv001-a01 mc-walks-into-dojo-glambot-01-149_i", loop = False)
image sm1cs_kv001-glambot-2 = Movie(play = "images/Character-Scenes/kv/s001/anim/sm1cs-kv001-a55-2x-50fps.webm", start_image = "sm1cs-kv001-a55 kv-aproach-mc-standing-back-glambot-55-000_i", image = "sm1cs-kv001-a55 kv-aproach-mc-standing-back-glambot-55-298_i", loop = False)
label sm1cs_kv001:
    $ kanyas_book_name = _("BOOK NAME")
    $ renpy.music.set_volume(0.5, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music action_tension_extended
    scene sm1cs-kv001-a01 mc-walks-into-dojo-glambot-01-000_i with dissolve
    pause
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] noloop volume 2.0
    scene sm1cs_kv001-glambot-1
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-kv001-02 mc-walks-closer-kv_c1 with dissolve
    pause
    scene sm1cs-kv001-03 mc-hi-is-kv-she-just-a-minute-mc-sure_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hi, are you Kanya Vu?"
    play voice3 kanya_yes_yeah1 noloop
    kv "Yeah, just a minute. We're just about to take a break."
    play voice2 mc_yes_sure1 noloop
    mc "Sure, not a problem."
    scene sm1cs-kv001-04 zh-winks-mc_c1 with dissolve
    pause
    scene sm1cs-kv001-05 zh-pose-camera-click_c1 with dissolve
    play sound sfx_photocamera_flash2 volume 1.5
    "*CLICK*"
    scene sm1cs-kv001-06 zh-pose-better-camera-click_c1 with dissolve
    play sound sfx_photocamera_flash2 volume 1.5
    "*CLICK*"
    scene sm1cs-kv001-07 kv-steps-side-camera-take-five-zh-happy_c1 with dissolve
    play voice3 kanya_thinking_eeh1 noloop
    kv "I think this is a good spot to take a break."
    play voice4 girl30_yes_aga1 noloop
    zh "Great, I'll go grab some water and change."
    $ renpy.music.set_volume(1.0, 2.0, "music" )
    play sound sfx_heels_steps1_slow volume 0.6
    scene sm1cs_kv001-glambot-2 with dissolve
    pause
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.5, 1.3, "music" )
    scene sm1cs-kv001-09 mc-introduces-himself-has-business-proposition-kv-only-works-people-know_c1 with dissolve
    play voice3 kanya_hey_arrogant noloop
    kv "Hey, what can I help you with?"
    play voice2 mc_hey_hey3 noloop
    mc "Hi, I'm [mcname]. I have a business proposition for you."
    play voice3 kanya_disappointed_ohh noloop
    kv "Oh? Well I only like to get into business with people I know."
    play sound sfx_cloth_rustling2
    scene sm1cs-kv001-10 kv-sits-couch-wants-know-more-about-mc-he-starts_c1 with dissolve
    play voice3 kanya_disappointed_hm noloop
    kv "Tell me about yourself, [mcname]."
    play voice2 d2s9_confused noloop volume 1.7
    mc "Well, I used to be a student at the college here-"
    scene sm1cs-kv001-11 kv-also-student-there-beats-university-mc-agrees_c1 with dissolve
    play voice3 kanya_yes_yeah2 noloop
    kv "I'm a student there too! Beats the university, right?"
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah it does!"
    scene sm1cs-kv001-12 mc-kv-discuss-prof-nordin_c1 with dissolve
    play voice3 kanya_disappointed_neh noloop
    kv "God, did you have Nordin as a professor?"
    play voice2 mc_disgust_ooh1 noloop
    mc "I did. He was the actual worst to have as a professor."
    kv "Oh, yeah. I hate his classes."
    scene sm1cs-kv001-13 kv-ask-mc-part-fl-he-was-guy-bring-it-down_c1 with dissolve
    play voice3 kanya_arrogant_ha noloop
    kv "Were you a part of Fetish Locator?"
    play voice2 mc_thinking_emm1 noloop
    mc "Actually, yeah I was. I'm actually the guy who helped bring it down."
    scene sm1cs-kv001-14 kv-had-fun-on-fl-was-bummer-bad-things_c1 with dissolve
    play voice3 kanya_surprised_ohmy noloop
    kv "Really. Man, I was having a {i}ton of fun{/i} on that app. Even found a couple of photo models on it."
    kv "It was a real bummer to hear about all the bad things happening behind the scenes."
    scene sm1cs-kv001-15 mc-being-dragged-sucked-kv-heard-hana-report-about-him_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "I can tell you that being dragged into it really sucked."
    play voice3 kanya_yes_aga3 noloop
    kv "I heard. I watched all of Hana's in-depth reporting on it."
    kv "That was all about you?"
    scene sm1cs-kv001-16 mc-akward-some-was-yeah-not-here-about-fl_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I mean, some of it was. Yeah."
    mc "But I'm not here about FL."
    scene sm1cs-kv001-17 kv-right-business-she-deff-want-hear-about-it_c1 with dissolve
    play voice3 kanya_disappointed_oof noloop
    kv "Right, right. Business proposition and all that. You've got me interested, [mcname]."
    kv "Anything involving the \"heroic student\" that brought down Fetish Locator definitely is something I want to hear about."
    play sound sfx_cloth_rustling4
    scene sm1cs-kv001-18 mc-sit-next-kv-tied-to-app-workin-on-porn-studio_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "It's funny that you brought up the app, that's actually kind of tied to what I wanted to talk to you about."
    mc "I am working right now on opening up my own porn studio."
    scene sm1cs-kv001-19 kv-leans-forward-porn-studio-not-first-guess-mc-ask-what-was_c1 with dissolve
    play voice3 kanya_happy_relief2 noloop
    kv "Huh, porn studio was definitely not my first guess."
    play voice2 mc_thinking_hmm2 noloop
    mc "What was your first guess?"
    scene sm1cs-kv001-20 kv-no-guess-more-interested-where-so-far_c1 with dissolve
    play voice3 kanya_thinking_eeh3 noloop
    kv "... I didn't actually have one."
    kv "Okay, so porn studio. I'm now even more interested. What have you got so far?"
    scene sm1cs-kv001-21 mc-more-of-warehouse-kv-less-than-ideal_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "We're renting a studio thing that we want to fix up."
    play voice3 kanya_surprised_wowohmy noloop
    kv "Oh wow! Already got access to a film studio. I'm impressed."
    play voice2 mc_disappointed_off2 noloop
    mc "Uhhh... It's more of a warehouse we want to turn into a studio, and a mattress in the corner."
    scene sm1cs-kv001-22 mc-have-grand-plans-will-fix-up-kv-heard-we-who-is-we_c1 with dissolve
    play voice3 kanya_disappointed_oh noloop
    kv "Oh... That is less than ideal."
    play voice2 mc_hey_hey5 noloop
    mc "But we have grand plans! We're going to fix it up and turn it into a real space."
    kv "That's a good plan! I heard you say \"we\". Have you got another business partner?"
    scene sm1cs-kv001-23 mc-nervous-answer-kv-wasnt-expecting-that_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    if persistent.is_special is True:
        mc "I do... It's actually my sister, Stacy."
    else:
        mc "I do! My best friend, Stacy, is also in this with me."
    play voice3 kanya_happy_relief3 noloop
    kv "Huh, wasn't expecting that either."
    scene sm1cs-kv001-24 mc-ask-bad-thing-kv-not-at-all_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "That a bad thing?"
    play voice3 kanya_no_happy noloop
    kv "No, it's just good to know what is involved."
    scene sm1cs-kv001-25 that-covered-what-about-gear-mc-asking-sex-toys_c1 with dissolve
    play voice3 kanya_hey_simple2 noloop
    kv "Now that we've got that, what about gear?"
    play voice2 mc_thinking_mmm4 noloop
    mc "Gear... Like sex toys?"
    scene sm1cs-kv001-26 kv-talks-sound-lights-camera-mc-has-phone_c1 with dissolve
    play voice3 kanya_no_nonono1 noloop
    kv "No, like camera, lighting, sound."
    play voice2 d2s12_emmm noloop
    mc "... I have my phone?"
    scene sm1cs-kv001-27 kv-shrugs-all-good-ask-what-mc-knows-filmmaking_c1 with dissolve
    play voice3 kanya_yes_yeah3 noloop
    kv "That'll work to get started. A lot of people do it that way when they start."
    kv "What do you all know about photography and filmmaking?"
    scene sm1cs-kv001-28 mc-needs-camera-actors-stuff-kv-before-they-go-deep-into_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I know you need a camera, and actors and actresses, and... Other stuff?"
    play voice3 kanya_thinking_eeh5 noloop
    kv "Well before we get too deep into gear and space and everything else..."
    scene sm1cs-kv001-29 kv-suggest-mc-pick-book-from-store_c1 with dissolve
    play voice3 kanya_thinking_hmm1 noloop
    kv "You should go and pick up a book on photography. Really explore some of the theory."
    kv "It will help you out a lot in the future."
    play sound sfx_cloth_rustling1
    scene sm1cs-kv001-30 kv-gives-mc-her-business-card_c1 with dissolve
    play voice3 kanya_thinking_hmm3 noloop
    kv "The store should have one. Here's my number. Text me so I have yours, and I'll tell you what book to get."
    scene sm1cs-kv001-33 mc-looking-at-card-thinks-cool-got-number-kv-talk-after-read-book_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Hell yeah, I got her number."
    scene sm1cs-kv001-34 mc-sounds-like-plan-kv-dont-keep-too-long_c1 with dissolve
    play voice3 kanya_hey_simple1 noloop
    kv "After you read up a bit, why don't you come back and we'll talk some more about your business."
    play voice2 mc_happy_yes1 noloop
    mc "That sounds like a plan to me! I'll get to reading then I guess."
    play voice3 kanya_happy_laugh3 noloop
    kv "And don't keep me waiting too long."
    scene sm1cs-kv001-35 kv-winks-mc_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "What the hell?! Nobody said anything about needing to read to make porn..."
    scene sm1cs-kv001-36 zh-walks-over-ready-kv-says-yeah_c1 with dissolve
    play voice4 girl30_surprised_huh1 noloop
    zh "Ready to get back to shooting Kanya?"
    play voice3 kanya_happy_yeah noloop
    kv "Yeah! Let's get to it."
    $ renpy.music.set_volume(1.0, 1.0, "music" )
    scene sm1cs-kv001-37 kv-zh-go-back-shooting_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.5, 1.0, "music" )
    scene sm1cs-kv001-38 kv-turns-mc-invites-him-stay-if-zh-okay_c1 with dissolve
    play voice3 kanya_surprised_eeh2 noloop
    kv "[mcname], you want to hang out and see how a photo shoot works?"
    scene sm1cs-kv001-39 zh-shrugs-no-problems-likes-audience_c1 with dissolve
    kv "If that's cool with you."
    play voice4 girl30_yes_yeah1 noloop
    zh "Not problem. I like having an audience."
    scene sm1cs-kv001-40 menu-choice-screen_c1 with dissolve
    menu:
        "Sure, I'm interested in how a photoshoot like this works."(hint="sm1cs_kv001_m01_h01"):
            call sm1cs_kv001_m01_c01 from _call_sm1cs_kv001_m01_c01
            scene sm1cs-kv001-41 choice-stay-mct-come-to-learn-after-all_c1 with dissolve
            play voice2 mc_arrogant_heh2 noloop
            mct "I did come here to learn after all..."
            jump sm1cs_kv001_photoshoot
        "Oh, I'll give you some space."(hint="sm1cs_kv001_m01_h02"):
            scene sm1cs-kv001-42 choice-give-space-mc-will-wait-over-there_c1 with dissolve
            play voice2 mc_arrogant_nah1 noloop
            mc "I'll just... Wait over here."
            jump sm1cs_kv001_ending
label sm1cs_kv001_photoshoot:
    scene sm1cs-kv001-43 kv-great-watch-carefully_c1 with dissolve
    play voice3 kanya_yes_yep1 noloop
    kv "Great, then watch carefully."
    play sound sfx_cloth_rustling1
    scene sm1cs-kv001-44 zh-takes-off-robe-reveals-strappy-outfit_c1 with dissolve
    pause
    scene sm1cs-kv001-45 mc-stunned-by-zh-outfit_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "Damn, she's super hot."
    $ renpy.music.set_volume(0.8, 3.0, "music" )
    scene sm1cs-kv001-46 photoshoot-pose-one_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv001-47 photoshoot-pose-two_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv001-48 kv-takes-photos_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Holy shit, I should have become a photographer."
    scene sm1cs-kv001-49 mc-sees-zh-pussy-thinks-had-become-photographer_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv001-50 photoshoot-last-pose_c1 with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    $ renpy.music.set_volume(0.5, 2.0, "music" )
    scene sm1cs-kv001-51 kv-tells-enough-zh-great-ask-how-photos-turned_c1 with dissolve
    play voice3 kanya_yes_long noloop
    kv "Looks good to me! I think that's a wrap for today."
    play voice4 girl30_happy_great1 noloop
    zh "Great! How'd the photos turn out?"
    scene sm1cs-kv001-52 kv-photos-great-zh-aswesome-will-see-edits_c1 with dissolve
    play voice3 kanya_disappointed_oof noloop
    kv "Good, real good. Super happy with how they're looking so far."
    play voice4 girl30_happy_oh2 noloop
    zh "Awesome, well I'm going to get changed. Looking forward to seeing the edits!"
    play sound sfx_heels_steps1
    scene sm1cs-kv001-53 zh-walks-away_c1 with dissolve
    stop sound fadeout 4.0
    pause
    scene sm1cs-kv001-54 mc-kv-step-away-from-photoshoot-spot_c1 with dissolve
    pause
    jump sm1cs_kv001_ending
label sm1cs_kv001_ending:
    if player.get_choice("sm1cs_kv001_give_space") is True:
        scene black
        show screen scene_transistion("After the photoshoot")
        with Fade(0.5, 0.5, 0.5)
        pause
        hide screen scene_transistion
        scene sm1cs-kv001-55 kv-aproach-mc-standing-back_c1
        with Fade(0.5, 0.5, 0.5)
        pause
    scene sm1cs-kv001-56 kv-good-talking-excited-future-mc-also-excited_c1 with dissolve
    play voice3 kanya_arrogant_yeah noloop
    kv "Good talk, [mcname]. I'm excited for our future plans."
    play voice2 mc_yes_yeah4 noloop
    mc "Me too! I'll get to reading and I'll text you."
    play sound sfx_cloth_rustling2
    scene sm1cs-kv001-57 kv-smiles-see-mc-around-he-later_c1 with dissolve
    play voice3 kanya_disappointed_hm noloop
    kv "I'll see ya around."
    play voice2 mc_yes_okay2 noloop
    mc "Later Kanya."
    scene sm1cs-kv001-58 mc-leavs-kv-studio-she-waves-back_c1 with dissolve
    pause
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    call sm1cs_kv001_unlock_lpd from _call_sm1cs_kv001_unlock_lpd
    $ StoryController.end_scene(KV_STORY, 2, 0, 2)
    return
label sm1cs_kv001_m01_c01:
    $ player.set_choice("sm1cs_kv001_interested")
    return
label sm1cs_kv001_unlock_lpd:
    $ LocationController.get_location(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW).unlock()
    return
label sm1cs_kv001_unlocks:
    call sm1cs_kv001_m01_c01 from _call_sm1cs_kv001_m01_c01_1
    call sm1cs_kv001_unlock_lpd from _call_sm1cs_kv001_unlock_lpd_1
    if config_storyline_mode is True:
        $ execute_storyline_config(KV_STORY)
    return