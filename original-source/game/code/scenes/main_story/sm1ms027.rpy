label sm1ms027:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play voice2 d7s6_snoring fadein 2.0
    scene sm1ms027-01 mc-sleeping_c1 with dissolve
    pause
    play voice3 stacy_hey noloop
    play music music_whenitsdone_itsdone volume 0.8
    scene sm1ms027-02 sy-wake-up_c1 with hpunch
    sy "[mcname]!{w} Wakeup!"
    sy "Wakie wakie wakie wakie!"
    scene sm1ms027-02 sy-wake-up_c2 with dissolve
    play voice2 d7s6_awake noloop volume 1.6
    mc "Mmmph... whuh...?"
    mc "Stacy what is wrong? Is the studio on fire?"
    scene sm1ms027-03 mc-sy-telling-him_c1 with dissolve
    play voice3 stacy_no_nope4 noloop
    sy "No! Better! I just finished it!"
    play sound sfx_cloth_rustling4
    scene sm1ms027-03 mc-sy-telling-him_c2 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "Finished what...?"
    scene sm1ms027-04 mc-sy-half-asleep_c2 with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "The site! The landing page, the trailer, the subscription system, even the sexy little launch button."
    sy "It's all done."
    scene sm1ms027-04 mc-sy-half-asleep_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "You... finished it? The whole site?"
    mc "I thought that would take a little longer."
    play sound sfx_cloth_rustling3
    scene sm1ms027-05 mc-sy-cuddling_c1 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "I couldn't wait. I pulled an all-nighter."
    scene sm1ms027-05 mc-sy-cuddling_c2 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "So our porn website is live?"
    scene sm1ms027-05 mc-sy-cuddling_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Almost. I was just waiting for {i}you{/i}."
    sy "I needed you awake so that you can press the launch button with me!"
    play voice2 mc_happy_a1 noloop
    mc "You're so sweet to wait for me."
    play sound2 sfx_cloth_rustling5 noloop
    scene sm1ms027-06 mc-kissing_c1 with dissolve
    play voice3 stacy_moan4 noloop
    play sound mc_kiss1
    sy "Ahhh."
    play sound sfx_keyboard_typing1 volume 1.5
    scene sm1ms027-07 mc-looking-at-the-laptop_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay okay. Let's see what we got."
    stop sound fadeout 1.0
    scene sm1ms027-08 mc-sy-looking-at-the-website_c1
    show sm1ms027-website-screenshot_pirates_movie
    with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Looks good."
    scene sm1ms027-09 mc-sy-ready_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Ready?"
    play voice3 stacy_yes_simple1 noloop
    sy "Ready!"
    scene sm1ms027-10 mc-sy-clicking_c1
    show sm1ms027-website-screenshot_pirates_movie_2
    with dissolve
    play voice2 d14s16_smell noloop
    "Stacy and [mcname]" "Three... two... one..."
    play sound sfx_keyboard_enter1 volume 1.6
    scene sm1ms027-11 mc-sy-clicking_c1
    show sm1ms027-website-screenshot_pirates_movie_2
    with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "Launch!"
    scene sm1ms027-08 mc-sy-looking-at-the-website_c1
    show sm1ms027-website-screenshot_pirates_movie
    with dissolve
    pause
    play voice3 stacy_happy_wooh1 noloop
    play voice2 mc_happy_laugh1 noloop
    scene sm1ms027-12 mc-sy-excited_c1 with hpunch
    sy "Woohoo."
    mc "We did it."
    scene sm1ms027-13 mc-thinking_c1 with dissolve
    play voice3 stacy_surprised_ohmy1 noloop
    sy "It's amazing. Our first Feature Film is out, on our own personal porn website."
    sy "Next stop... global domination."
    play voice2 d1s1_mmm noloop
    if persistent.is_special:
        mct "Ah, my beautiful little sister."
    else:
        mct "Ah, my amazing girlfriend."
    mct "I'm not sure I've ever loved her as much as I do right now."
    play sound sfx_cloth_rustling3
    scene sm1ms027-14 mc-sy-hugging_c1 with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "Come here, you ridiculous genius."
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1ms027-15 mc-sy-kissing_c1 with dissolve
    play voice3 stacy_suckmoan3 noloop
    play sound mc_kiss2
    sy "Mmm..."
    scene sm1ms027-16 sy-talking_c1 with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Best launch party ever."
    sy "Hey—just so you know, if you ever wanna rewatch it or show it to someone, you can use this laptop. Just open the site, it's right there."
    play sound sfx_cloth_rustling2
    scene sm1ms027-17 mc-sy-cuddling_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Awesome. It will be cool reviewing what we've done so far as we work on future stuff."
    mc "But that can wait."
    scene sm1ms027-18 mc-sy- yawning_c1 with dissolve
    play voice2 d7s6_moan1 noloop
    mc "I'm going back to sleep."
    scene sm1ms027-18 mc-sy- yawning_c2 with dissolve
    play voice3 stacy_yes_yap2 noloop
    sy "I think I'll join you."
    play sound sfx_cloth_rustling5 volume 1.6
    scene sm1ms027-19 mc-sy-sleeping_c1 with dissolve
    play voice2 d7s6_snoring
    pause
    scene sm1ms027-19 mc-sy-sleeping_c2 with dissolve
    pause
    play voice3 stacy_scared_ah4 noloop
    play voice2 d4s8_scared noloop
    play sound sfx_skirt_off2
    scene sm1ms027-20 mc-sy-freaked-out_c1 with vpunch
    sy "OH MY GOD—"
    scene sm1ms027-20 mc-sy-freaked-out_c2 with dissolve
    play voice2 mc_surprised_what8 noloop
    mc "Wha—what!?"
    play voice3 stacy_angry_aah1 noloop
    scene sm1ms027-21 mc-sy-freaked-out_c1 with hpunch
    sy "I forgot to set up the damn storage bucket permissions! The movie won't even play!"
    scene sm1ms027-21 mc-sy-freaked-out_c2 with dissolve
    play voice3 stacy_angry_fuck1 noloop
    sy "People will click on the link and it'll just... not be there!"
    play sound sfx_gadgets_laptop_opened
    scene sm1ms027-22 mc-sy-typing-thinking_c2 with dissolve
    play sound2 sfx_keyboard_typing2 volume 2.0
    play voice3 stacy_pain_mmm1 noloop
    sy "It'll 404! Like a sad, dead link in the middle of the night!"
    play sound sfx_hair_scratch1
    scene sm1ms027-23 mc-complimenting_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mc "No one's awake right now to watch it, right...?"
    scene sm1ms027-22 mc-sy-typing-thinking_c2 with dissolve
    play voice3 stacy_hey noloop
    sy "There are always horny people searching for hot stuff at every hour of every day, [mcname]!"
    play sound sfx_cloth_rustling1
    scene sm1ms027-24 mc-sleeping_c2 with dissolve
    play voice2 mc_happy_oof3 noloop
    mct "She's typing like the fate of humanity depends on it."
    mc "You got this, baby... Just... patch the thing... sshh... cyber magic..."
    mc "Hot code-goblin of my dreams..."
    stop sound2 fadeout 1.5
    scene sm1ms027-25 mc-sy-in-the-kitchen-morning_c1 with Fade(0.5, 0.5, 0.5)
    play sound sfx_barefoot_steps1 volume 2.0 loop
    play sound2 sfx_keyboard_typing2 volume 2.0
    "Rapid typing noises"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.5
    scene sm1ms027-25 mc-sy-in-the-kitchen-morning_c2 with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "Morning... or... is it still night?"
    scene sm1ms027-26 sy-talking_c1 with dissolve
    pause
    play sound sfx_bed_slide2 volume 0.7
    scene sm1ms027-27 mc-sy-talking_c1 with dissolve
    play voice3 stacy_disappointed_moan1 noloop
    sy "[mcname]! The launch! It went amazing! We've got traffic! People are watching it! Commenting! Sharing! I can't— I can't even sit still!"
    scene sm1ms027-27 mc-sy-talking_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, that's probably because you have enough Red Mongoose inside you that your DNA might be getting irrevocably changed."
    scene sm1ms027-27 mc-sy-talking_c1 with dissolve
    play voice3 stacy_uhuh noloop
    sy "Not enough! I mean, clearly, because I still have emails to reply to, and someone wants a BTS blog post, and there's a meme thread."
    sy "Oh my god, someone made a meme out when Taisia throws me around at the end."
    play sound sfx_bed_slide3
    scene sm1ms027-28 mc-sy-sitting_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Maybe you need a nap? Or just close your eyes for like... ten seconds?"
    play sound2 sfx_keyboard_typing2 volume 2.0
    scene sm1ms027-29 mc-sy-still-focused-talking_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "She's running on caffeine, adrenaline, and pure love for this project."
    play sound sfx_leg_kick6
    scene sm1ms027-30 sy-asleep_c1 with dissolve
    play voice3 stacy_disappointed_moan3 noloop
    sy "Must keep typing. Need to update packet transfer... to increase.... speed."
    sy "Need... 4k... streaming quality."
    scene sm1ms027-30 sy-asleep_c2 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "There she goes..."
    play sound sfx_cloth_rustling2 volume 2.0
    play sound2 sfx_barefoot_steps1 volume 2.0
    scene sm1ms027-31 mc-sy-carrying_c1 with dissolve
    play voice3 stacy_angry_breath2 noloop
    sy "...CDN fallback caching... bucket rules... mm... gzip all the things..."
    scene sm1ms027-32 mc-sy-carrying_c1 with dissolve
    pause
    play sound sfx_cloth_planket3
    stop sound2 fadeout 1.0
    scene sm1ms027-33 mc-sy-sleeping_c1 with dissolve
    pause
    scene sm1ms027-34 mc-kissing-her_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    play sound mc_kiss3
    mc "Goodnight, my sexy code goblin. You earned it."
    scene sm1ms027-35 mc-looking-at-the-studio_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Well, I guess I should do a little work of my own."
    mc "Hard to get back to sleep after that."
    jump sm1ms027_end_scene
label sm1ms027_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ ObjectController.get_object(STUDIO_LAPTOP).unlock()
    $ StoryController.end_scene(MS)
    return