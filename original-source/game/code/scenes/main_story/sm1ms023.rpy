label sm1ms023:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music music_convo_ver1
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1ms023-01 mc-asking with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "So what's the problem?"
    scene sm1ms023-02 sy-talking with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Let me show you."
    play sound sfx_chair_slide1
    stop sound2 fadeout 1.0
    scene sm1ms023-03 sy-sitting with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "So, I think I've almost got a picture lock on the last video."
    scene sm1ms023-04 mc-talking with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "That's great!... But?"
    scene sm1ms023-05 mc-looking-at-the-screen with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "But..."
    sy "I'm not sure about this part here."
    scene sm1ms023-06 mc-asking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "What aren't you sure about?"
    scene sm1ms023-07 sy-pointing with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "This..."
    play sound sfx_keyboard_enter1
    scene sm1ms023-08 sy-looking-at-the-screen with dissolve
    play sound2 sfx_tv_porn1 volume 0.4
    play voice3 stacy_angryhuh noloop
    sy "So my first problem is I'm not sure how long to play this part out."
    sy "Because I think it's hot, but I'm a little biased."
    sy "Because it also feels a little long."
    stop sound2 fadeout 0.5
    play sound sfx_keyboard_enter1
    scene sm1ms023-09 sy-asking with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "What do you think?"
    menu:
        "Cut it"(hint="sm1ms023_m01_h01"):
            call sm1ms023_m01_c01 from _call_sm1ms023_m01_c01
            scene sm1ms023-10 mc-cut-it with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "I think cut it down. Don't want too much bloat in the video."
            mc "Keep it tight, you know?"
            scene sm1ms023-11 sy-teasing with dissolve
            play voice3 stacy_arrogant_hmm3 noloop
            sy "Tight like me?"
            scene sm1ms023-12 mc-smiling with dissolve
            play voice2 mc_yes_yes7 noloop
            mc "Yes, Stacy, tight like you."
        "Leave it"(hint="sm1ms023_m01_h02"):
            scene sm1ms023-13 mc-leave-it with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "I think you're right about it being hot."
            mc "Keep it in the cut."
            scene sm1ms023-14 sy-agreeing with dissolve
            play voice3 stacy_happy_yay1 noloop
            sy "Hell yeah."
    scene sm1ms023-15 sy-looking-at-screen-again with dissolve
    play sound sfx_remote_button1 volume 1.5
    play voice3 stacy_thinking_hmm3 noloop
    sy "Cool, that should be easy to do."
    sy "I'm still in the middle of doing the fine cut, so I'm not quite there with the edit yet."
    play sound sfx_remote_button1 volume 1.5
    scene sm1ms023-16 sy-looking-at-screen-again with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "Because like, right here, Kanya got two different angles."
    scene sm1ms023-16-02 sy-looking-at-screen-again with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "And I'm not sure which one to use."
    menu:
        "Use the first angle"(hint="sm1ms023_m02_h01"):
            call sm1ms023_m02_c01 from _call_sm1ms023_m02_c01
            scene sm1ms023-17 mc-talking with dissolve
            play voice2 mc_happy_a1 noloop
            mc "I think the first angle. I like that one more."
        "Use the second angle"(hint="sm1ms023_m02_h02"):
            scene sm1ms023-17 mc-talking with dissolve
            play voice2 mc_happy_a1 noloop
            mc "The second angle is better. At least I think so."
    scene sm1ms023-18 sy-cool with dissolve
    play voice3 stacy_yes_yap2 noloop
    sy "Cool. Cool, cool, cool."
    sy "Well, I think I have a few more changes to make, but nothing crazy."
    scene sm1ms023-19 mc-talking-with-a-but with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah? Well what else do you need to do?"
    play sound sfx_remote_button1
    scene sm1ms023-20 sy-talking with dissolve
    play voice3 stacy_hmm noloop volume 1.6
    sy "I'll show you."
    $ renpy.music.set_volume(1.0, 1.5, "music" )
    scene sm1ms023-22 mc-sy-editing-montage with dissolve
    pause
    scene sm1ms023-23 mc-sy-editing-montage with dissolve
    pause
    scene sm1ms023-24 mc-sy-editing-montage with dissolve
    pause
    scene sm1ms023-25 mc-sy-editing-montage with dissolve
    pause
    scene sm1ms023-26 mc-sy-editing-montage with dissolve
    pause
    $ renpy.music.set_volume(0.7, 2.5, "music" )
    scene sm1ms023-27 mc-sy-talking with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "And yeah, that's most of the video editing to do. I mean, there's definitely some more fine tuning I want to do, but-"
    scene sm1ms023-28 sy-talking with dissolve
    play voice3 stacy_disappointed_oh2 noloop
    sy "Shit, I forgot. I still need to color correct all of the footage."
    play sound sfx_cloth_rustling2
    scene sm1ms023-29 mc-asking with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Why do you have to color correct it? We shot it on a set?"
    scene sm1ms023-30 sy-telling with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "We didn't cover the windows, so the outside light changed the ambient color temp."
    sy "So it's nothing crazy, but it's - shit, let me show you."
    play sound sfx_remote_button1 volume 1.6
    scene sm1ms023-31 sy-looking-at-screen-again with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Let's see..."
    play sound sfx_keyboard_typing2
    scene sm1ms023-32 sy-looking-at-screen-again with dissolve
    sy "..."
    play sound sfx_keyboard_enter1
    scene sm1ms023-32-02 sy-looking-at-screen-again with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "Here we go."
    sy "See what I mean?"
    scene sm1ms023-33 mc-i-see with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, I see what you mean."
    play sound sfx_remote_button1 volume 1.6
    scene sm1ms023-34 sy-looking-at-screen-again with dissolve
    play voice3 stacy_mmm2 noloop
    sy "But..."
    play sound sfx_keyboard_enter1
    scene sm1ms023-34-02 sy-looking-at-screen-again with dissolve
    pause
    scene sm1ms023-35 sy-happy with dissolve
    play voice3 stacy_happy_phew1 noloop
    sy "All fixed. But I have to do this for a lot of the clips."
    scene sm1ms023-36 mc-happy with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, I see that now."
    mc "Should we, I don't know, invest in some blinds or something?"
    scene sm1ms023-37 sy-mc-talking with dissolve
    play voice3 stacy_disappointed_mmm2 noloop
    sy "We would need light control blinds, or blackout blinds, and those are expeeeeensive."
    scene sm1ms023-38 sy-mc-talking with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, you got a good point there."
    scene sm1ms023-39 mc-asking with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "So... how much longer do you need for the edit?"
    scene sm1ms023-40 sy-telling with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "For the picture lock... maybe 3 more days?"
    scene sm1ms023-41 sy-mc-talking with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Sweet, I'll check in with you later."
    play voice3 stacy_yes_yeah1 noloop
    sy "Sounds good."
    play sound sfx_cloth_rustling3
    scene sm1ms023-42 mc-bye with dissolve
    play voice2 mc_hey_bye1 noloop
    mc "Later, Stacy!"
    scene sm1ms023-43 sy-bye with dissolve
    play voice3 stacy_hey_seeya noloop
    sy "Later, [mcname]."
    jump sm1ms023_end_scene
label sm1ms023_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(MS, 4, 0, 2, STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS)
    return
label sm1ms023_m01_c01:
    $ player.set_choice("sm1ms023_trim_video")
    return
label sm1ms023_m02_c01:
    $ player.set_choice("sm1ms023_first_angle")
    return