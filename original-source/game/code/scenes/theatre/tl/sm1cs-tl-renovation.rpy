label sm1cs_tl_renovation:
    $ renpy.music.set_volume(0.5, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.5, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.5, 1.0, "freeroam_sound2" )
    play sound sfx_heels_steps2 loop
    scene sm1cs-tl-00 renovation with dissolve
    play voice3 girl24_arrogant_huh2 noloop
    tl "And how long is that going to take?"
    stop sound fadeout 1.0
    scene sm1cs-tl-01 renovation_mc_talk with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "I don't know... there's a lot of stuff to do."
    scene sm1cs-tl-02 renovation_tl_talk with dissolve
    play voice3 girl24_arrogant_yeah3 noloop
    tl "Yeah, like what."
    scene sm1cs-tl-03 renovation_mc_talk with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "I don't know... moving stuff, and, uh painting, and-"
    play sound2 sfx_leg_kick8 noloop
    scene sm1cs-tl-04 renovation_mc_talk_shoulder with dissolve
    play sound sfx_drink_gulp
    mc "*Gulp*"
    mc "And, uhm... putting in the stairs."
    scene sm1cs-tl-05 renovation_tl_talk_shoulder with dissolve
    play voice3 girl24_hey_angry noloop
    tl "You know, my landlord is getting kind of pissy. And I don't want to give that dude another penny."
    tl "So why don't we try to speed things up a bit, aye?"
    scene sm1cs-tl-06 renovation_mc_talk_nervous with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I'm doing the best I can!"
    scene sm1cs-tl-07 renovation_tl_talk with dissolve
    play voice3 girl24_angry_argh1 noloop
    tl "Ugggggggh..."
    play sound sfx_cloth_rustling1
    scene sm1cs-tl-08 renovation_tl_talk_stepback with dissolve
    play voice3 girl24_arrogant_yeah1 noloop
    tl "Fine."
    scene sm1cs-tl-09 renovation_mc_talk with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Okay?...{w} Well then, I'm just going to go..."
    play sound2 sfx_heels_steps2
    scene sm1cs-tl-10 renovation_tl_talk_mc_walkaway with dissolve
    play voice3 girl24_arrogant_hm1 noloop
    tl "I'll help."
    stop sound fadeout 1.0
    scene sm1cs-tl-11 renovation_mc_talk_mc_lookback with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait..."
    mc "What?"
    scene sm1cs-tl-12 renovation_tl_talk with dissolve
    play voice3 girl24_arrogant_hm3 noloop
    tl "I'll help. Come on."
    play sound sfx_heels_steps1 loop
    scene sm1cs-tl-13 renovation_mc_talk_tl_walkpast with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "Come on, what?"
    stop sound fadeout 1.0
    scene sm1cs-tl-14 renovation_tl_talk with dissolve
    play voice3 girl24_disappointed_neh noloop
    tl "You said there's work to do. So let's go do it."
    scene sm1cs-tl-15 renovation_mc_talk with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Like, you're going to come help me work on the studio?"
    scene sm1cs-tl-16 renovation_tl_talkrritated with dissolve
    play voice3 girl24_angry_geh noloop
    tl "Are you not paying attention? You got shit in your ears?"
    scene sm1cs-tl-17 renovation_mc_talk with dissolve
    play voice2 mc_no_no10 noloop
    mc "Uhm... no?"
    scene sm1cs-tl-18 renovation_tl_talk with dissolve
    play voice3 girl24_arrogant_huh1 noloop
    tl "Then I don't see what's so hard to understand. Let's go."
    play sound sfx_heels_steps1 loop
    scene sm1cs-tl-19 renovation_mc_thought with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Well, she's definitely determined, I'll give her that."
    mct "..."
    mct "Oh, she's really leaving."
    play sound2 sfx_heels_steps2
    scene sm1cs-tl-20 renovation_mc_follow with dissolve
    play voice2 mc_hey_hey8 noloop
    mc "Taisia! Wait up!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    jump sm1cs_tl_renovation_studio
label sm1cs_tl_renovation_studio:
    scene black
    show screen scene_transistion(_("Back at the Studio"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_door_openclosed2
    scene sm1cs-tl-21 renovation_tl_studio
    $ renpy.music.set_volume(0.5, 3.0, "music" )
    play music music_nailed_the_nail fadein 1.5
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-tl-22 renovation_tl_talk with dissolve
    play voice3 girl24_surprised_wow2 noloop
    tl "Wow, [mcname]... you weren't kidding."
    scene sm1cs-tl-23 renovation_mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah. I was trying to tell you that there was a bunch of stuff to do."
    scene sm1cs-tl-24 renovation_tl_talk with dissolve
    play voice3 girl24_disappointed_eeh1 noloop
    tl "This place is still nicer than mine though."
    play sound sfx_heels_steps1 loop
    scene sm1cs-tl-25 renovation_mcl_talk_tl_walk with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I - wait, I have no idea what your place looks like."
    scene sm1cs-tl-26 renovation_tl_talk with dissolve
    play voice3 girl24_yes_yap noloop
    tl "Yep."
    play sound2 sfx_heels_steps2
    scene sm1cs-tl-27 renovation_mc_talk with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "I'd like-"
    scene sm1cs-tl-28 renovation_tl_talk with dissolve
    play voice3 girl24_no_nope noloop
    tl "Nope."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-tl-29 renovation_mc_talk_confused with dissolve
    play voice2 mc_no_no9 noloop
    mc "Nope?"
    scene sm1cs-tl-30 renovation_tl_talk with dissolve
    play voice3 girl24_yes_ugu noloop
    tl "Remember how I'm trying to {i}move{/i} out of that place?"
    scene sm1cs-tl-31 renovation_mc_talk with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "I guess... you've got a point there."
    play sound sfx_cloth_rustling1
    scene sm1cs-tl-32 renovation_tl_talk with dissolve
    play voice3 girl24_thinking_hmm1 noloop
    tl "So... where should we start?"
    scene sm1cs-tl-33 renovation_mc_talk with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Uhm... help me move these boxes?"
    scene sm1cs-tl-34 renovation_tl_talk with dissolve
    play voice3 girl24_thinking_hmm3 noloop
    tl "All right."
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    play sound sfx_box_slide
    play sound2 sfx_heels_steps2
    scene sm1cs-tl-35 renovation_montage_box with fade
    pause
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-tl-36 renovation_montage_lay tarp with fade
    pause
    play sound sfx_cloth_wiping1
    scene sm1cs-tl-37 renovation_montage_wipe with fade
    pause
    play sound sfx_cleaning_floor1
    play sound2 sfx_cleaning_floor2 volume 0.5
    scene sm1cs-tl-38 renovation_montage_sweep with fade
    pause
    play sound3 sfx_paint_smearing2
    stop sound fadeout 1.5
    stop sound2 fadeout 1.5
    scene sm1cs-tl-39 renovation_montage_painting with fade
    pause
    $ renpy.music.set_volume(0.5, 3.0, "music" )
    stop sound3 fadeout 1.5
    scene sm1cs-tl-40 renovation_tl_talk_standing_back with dissolve
    play voice3 girl24_disappointed_oof noloop
    tl "Wow... it doesn't look like we did shit around here."
    scene sm1cs-tl-41 renovation_mc_talk_standing_back with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "We did! We just spent... I don't know, how long does a montage usually last?"
    scene sm1cs-tl-42 renovation_tl_talk with dissolve
    play voice3 girl24_happy_mmm noloop
    tl "Like two, or three hours."
    scene sm1cs-tl-43 renovation_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. Which honestly is a huge help. We got a lot done."
    scene sm1cs-tl-44 renovation_tl_talk_soft_look with dissolve
    play voice3 girl24_yes_aga noloop
    tl "Uh huh..."
    tl "I just want to... uhm..."
    scene sm1cs-tl-45 renovation_mc_talk with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "What?"
    scene sm1cs-tl-46 renovation_tl_talk with dissolve
    play voice3 girl24_disappointed_hmf noloop
    tl "Thanks, [mcname]."
    scene sm1cs-tl-47 renovation_mc_talk_surprised with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Did you just... thank me?"
    play voice3 girl24_angry_argh5 noloop
    play voice2 mc_pain_auh6 noloop
    play sound sfx_leg_kick3
    scene sm1cs-tl-48 renovation_mc_talk_tl_punch with hpunch
    mc "Ouch!"
    scene sm1cs-tl-49 renovation_tl_talk with dissolve
    play voice3 girl24_angry_cough1 noloop
    tl "Way to ruin the moment, [mcname]."
    scene sm1cs-tl-50 renovation_mc_talk with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "What can I say, that's my one, true talent. Ruining moments."
    play sound sfx_cloth_rustling1
    scene sm1cs-tl-51 renovation_tl_talk_lookaround with dissolve
    play voice3 girl24_yes_angry noloop
    tl "You can say that again."
    tl "So, just that much closer to getting my own room here, huh."
    scene sm1cs-tl-52 renovation_mc_talk with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Yeah. Next we need to get those stairs installed so we can get to all the rooms up there."
    play voice3 girl24_thinking_huh1 noloop
    tl "There are rooms up there?"
    scene sm1cs-tl-53 renovation_tl_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. When we first moved in Stacy crawled up there and found them."
    play voice3 girl24_surprised_huh3 noloop
    tl "Crawled up there?"
    scene sm1cs-tl-54 renovation_mc_talk_lookup with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yeah, no stairs, you know?"
    scene sm1cs-tl-57 renovation_tl_talk_smiles with dissolve
    play voice3 girl24_happy_laugh1 noloop
    tl "You got a point there."
    tl "I wouldn't mind seeing Stacy crawl her tight ass up there... mmm, I'm going to think about that later."
    tl "Which, speaking of-"
    play sound sfx_heels_steps1 loop
    scene sm1cs-tl-58 renovation_tl_talk_walkbackdoor with dissolve
    play voice3 girl24_thinking_emm1 noloop
    tl "I've got to jet. Got some shit I have to do."
    scene sm1cs-tl-59 renovation_mc_talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, cool. I guess I'll see you around."
    play sound sfx_door_open1
    scene sm1cs-tl-60 renovation_tl_talk_bydoor with dissolve
    play voice3 girl24_thinking_ah noloop
    tl "Oh you definitely will."
    tl "I'll see you later... roomie."
    play sound sfx_door_closed1
    scene sm1cs-tl-61 renovation_mc_thoughtdoor with dissolve
    pause
    play voice2 mc_thinking_hmm1 noloop
    mct "Man, having Taisia live here is going to be a lot of fun. It's also probably going to drive me bananas..."
    mct "Only time will tell."
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    stop music fadeout 3.0
    jump sm1cs_tl_renovation_end
label sm1cs_tl_renovation_end:
    $ renovation_controller.set_progress(renovation_controller.get_renovation_scenes_progress())
    $ renovation_controller.set_daily_limit()
    $ StoryController.end_scene_without_storyline("sm1cs_tl_renovation", 2, 0, 4, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return