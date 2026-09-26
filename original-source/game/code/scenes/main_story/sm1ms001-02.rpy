label sm1ms001_02:
    $ renpy.music.set_volume(0.5, 0.0, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_freeroam_light2 fadein 3.0
    scene sm1ms005-01 mc-sitting-mattress-laptop_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Man, what a day. This bed feels so good."
    play sound sfx_barefoot_steps1
    scene sm1ms005-02 sy-walks-to-mc_c1 with dissolve
    pause
    play sound sfx_cloth_rustling4
    scene sm1ms005-03 mc-ask-extra-butten-popcorn-sy-ofc-it-is_c1 with dissolve
    play voice3 stacy_no_uhuh3 noloop
    sy "You can't go to sleep yet, buster."
    play sound sfx_popcorn_grab2 volume 0.5
    scene sm1ms005-05 mc-reaches-popcorn-sy-better-share-mc-makes-no-promises_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Huh? Why not?"
    scene sm1ms005-06 mc-asking-what-movie-picked-up-sy-let-him-decide_c1 with dissolve
    play voice3 stacy_angry noloop
    sy "Did you forget? It's movie night, tonight."
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Haha. That does sound perfect after a long day. Let's do it."
    play sound sfx_keyboard_enter1
    scene sm1ms005-07 movie-choice-menu-screen_c1 with dissolve
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_tv_film1 volume 0.4
    pause
    play voice2 mc_scared_huuuh3 noloop
    scene sm1ms005-19 mc-sy-reaction-adventure-sex_c1 with dissolve
    play voice3 stacy_surprised_wow1 noloop
    sy "Woah. I've never seen a fat dragon."
    queue voice2 mc_angry_errr1 noloop
    mc "It may be fat but it still moves fast. Run!"
    play voice3 stacy_laugh noloop
    sy "*giggles*"
    stop sound2 fadeout 2.0
    scene sm1ms005-16 sy-surprised-how-now-mc-tonight-about-them_c1 with Fade(0.6, 0.3, 0.6)
    play voice3 stacy_disappointed_moan1 noloop
    sy "*yawns* That was great."
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. Oh... I didn't even realize how late it is. Guess we're sleeping in tomorrow."
    scene sm1ms005-17 sy-rolls-eyes-mc-shh-starting_c1 with dissolve
    play voice3 stacy_laugh4 noloop
    sy "*giggles* Some things never change."
    scene sm1ms005-21 sy-thanks-doing-wiht-her-mc-always_c1 with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "But you should be careful. If you stay up late and sleep in, that means you'll lose part of the day."
    play voice2 mc_yes_aga2 noloop
    mc "I know. I'll be careful."
    play voice3 stacy_yes_ugu1 noloop
    sy "Good. Let's put this away and go to sleep."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.activate_story_line(DC_STORY)
    $ StoryController.end_scene_in_time(MS, 1, 0, 0, STUDIO, DEFAULT_SUBLOCATION, SD_MATTRESS)
    return