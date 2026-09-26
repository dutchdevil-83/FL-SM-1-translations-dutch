image sm1ms023-a92-glm = Movie(play = "images/ms/s023/anim/sm1ms023-a92-4x-60fps.webm", start_image = "sm1ms023-a92 sy-bye-glambot-00", image = "sm1ms023-a92 sy-bye-glambot-90", loop = False)
label sm1ms023_02:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music music_convo_ver1
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1ms023-44 mc-sy-walking with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Did something go wrong?"
    scene sm1ms023-45 mc-sy-walking with dissolve
    play voice3 stacy_no_nope1 noloop
    sy "Nope, the video is all good."
    scene sm1ms023-46 mc-sy-walking with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "So what's wrong?"
    play sound sfx_chair_slide1
    stop sound2 fadeout 1.0
    scene sm1ms023-47 sy-sitting with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "Nothing is {i}wrong{/i}, but there's still some more work to do."
    scene sm1ms023-48 mc-asking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh? What's next?"
    scene sm1ms023-49 sy-audio-mixing with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "Audio mixing."
    play sound sfx_cloth_rustling2
    scene sm1ms023-50 mc-sitting with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Shit, I didn't even think about that."
    scene sm1ms023-51 sy-wink with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "And that's why I'm the editor!"
    scene sm1ms023-52 mc-happy with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Best damn editor I've ever met."
    scene sm1ms023-53 sy-side-eye with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Ain't I the only editor you know?"
    scene sm1ms023-54 mc-speechless with dissolve
    mc "..."
    scene sm1ms023-55 mc-maybe with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "Maybe."
    scene sm1ms023-56 sy-rolling-eyes with dissolve
    pause
    play sound sfx_keyboard_typing1
    scene sm1ms023-57 sy-working with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "Anyway, now I just need to balance the audio out."
    scene sm1ms023-58 mc-asking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "What do you mean by balance?"
    scene sm1ms023-59 sy-explaining with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "So sometimes people make noises..."
    scene sm1ms023-60 mc-asking with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Oh really? People make sounds?"
    play sound sfx_cloth_rustling1
    scene sm1ms023-61 sy-explaining with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Hardy har, [mcname]."
    sy "What I'm trying to say is that some noises are louder than others."
    sy "And since we don't have an audio mixer, we have some weird audio problems."
    scene sm1ms023-62 mc-confused with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "What do you mean?"
    play voice3 stacy_happy_hmm1 noloop
    sy "So right now our only audio comes from Kanya's camera."
    $ renpy.music.set_volume(0.0, 0.0, "sound2" )
    mc "Uh huh..."
    $ renpy.music.set_volume(1.0, 10.0, "sound2" )
    play sound2 sfx_tv_porn2
    play sound sfx_keyboard_enter1
    scene sm1ms023-63 sy-working with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "So as Kanya moves closer or farther away from us, the audio level goes up or down. So sometimes it's louder, sometimes it's quieter."
    $ renpy.music.set_volume(0.2, 10.0, "sound2" )
    sy "And then sometimes, we get louder or quieter."
    play sound sfx_keyboard_enter1
    stop sound2 fadeout 0.2
    $ renpy.music.set_volume(1.0, 3.0, "sound2" )
    scene sm1ms023-64 mc-confused with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "\"We\"?"
    scene sm1ms023-65 sy-pissed-a-bit with dissolve
    play voice3 stacy_yes_fine3 noloop
    sy "Okay, me. I get louder, asshat."
    scene sm1ms023-66 sy-sexy with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "Because you're fucking me with your great cock and making me moan your name."
    scene sm1ms023-67 sy-mc-talking with dissolve
    mc "..."
    play voice2 mc_yes_okay2 noloop
    mc "Okay, good point."
    play voice3 stacy_yes_ugu1 noloop
    sy "So, at some point, we're going to want to find someone to set up some mics or something so we can record cleaner audio."
    scene sm1ms023-68 mc-thinking with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "That's probably a good idea."
    mc "Do we even know anyone who knows how to do audio?"
    scene sm1ms023-69 sy-mc-talking with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Maybe. That's your job to figure out."
    play voice2 mc_arrogant_huh1 noloop
    mc "Why is it my job?"
    sy "You're the people person."
    mc "But you like talking to people too."
    scene sm1ms023-70 sy-talking with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Yeah, but I do enough around here."
    scene sm1ms023-71 sy-talking with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "So you get to be in charge of recruitment."
    sy "Which means you'll need to find us an audio person."
    scene sm1ms023-72 mc-fine with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "...{w} Fine."
    play sound sfx_chair_slide1
    scene sm1ms023-73 sy-leaning-back with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "I think that's it!"
    scene sm1ms023-74 mc-surprised with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Really?"
    scene sm1ms023-75 sy-talking with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah, I had done a lot of it as I was working through, but needed to put the final touches on it."
    play sound sfx_cloth_rustling2
    scene sm1ms023-76 mc-impressed with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Wow... I'm impressed."
    scene sm1ms023-77 sy-as-you-should-be with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "As you should be."
    if persistent.is_special:
        sy "Because you've got the best damn sister in the world."
    else:
        sy "Because you've got the best damn friend in the world."
    scene sm1ms023-78 mc-smiling with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Yes, yes."
    play sound sfx_cloth_rustling3
    scene sm1ms023-79 mc-bowing with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "I bow before your magnificence and splendor, Stacy."
    scene sm1ms023-80 sy-good with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Good."
    scene sm1ms023-81 sy-smirking with dissolve
    play voice3 stacy_suckmoan1 noloop
    sy "And I hope I get a reward for doing such a good job."
    play sound sfx_cloth_rustling4
    scene sm1ms023-82 mc-talking with dissolve
    play voice2 mc_scared_oh2 noloop
    mc "Oh, you absolutely will."
    scene sm1ms023-83 mc-sy-talking with dissolve
    play voice3 stacy_arrogant_hmm3 noloop
    sy "Right now?"
    play voice2 mc_arrogant_heh3 noloop
    mc "I think you need to finish the video and send it to the client."
    play sound sfx_cloth_rustling1
    scene sm1ms023-84 sy-groaning with dissolve
    play voice3 stacy_angry_fuck2 noloop
    sy "Fuck meeeeeee."
    scene sm1ms023-85 sy-please with dissolve
    play voice3 stacy_disappointed_oh2 noloop
    sy "Please?"
    scene sm1ms023-86 mc-come-on with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Come on, Stacy."
    play sound sfx_cloth_rustling2
    scene sm1ms023-87 sy-groaning with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "Ugggggggh!"
    play sound sfx_keyboard_enter1
    play sound2 sfx_tv_porn2
    scene sm1ms023-88 sy-getting-back-on-pc with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "Fiiiiiiiine."
    sy "But I'm probably going to rub one out while I finish rendering the final."
    scene sm1ms023-89 mc-not-stopping-you with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Hey, I ain't going to stop you."
    scene sm1ms023-90 sy-challenging with dissolve
    play voice3 stacy_angry noloop
    sy "Nothing on God's green earth could stop me from masturbating to this hot ass footage."
    play sound sfx_heels_steps2 loop
    scene sm1ms023-91 mc-thinking with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "God, Stacy is wild."
    scene sm1ms023-a92 sy-bye-glambot-00 with dissolve
    pause
    play sound3 sfx_camera_fly1 noloop volume 2.0
    play sound4 ["<silence 2.0>", sfx_camera_fly1] noloop volume 2.0
    scene sm1ms023-a92-glm
    pause
    play voice3 stacy_hey_seeya noloop
    sy "Later, [mcname]!"
    stop sound3 fadeout 1.0
    stop sound4 fadeout 1.0
    scene sm1ms023-93 mc-bye with dissolve
    play voice2 mc_hey_bye1 noloop
    mc "See you, Stacy."
    stop sound2 fadeout 1.0
    stop sound fadeout 1.0
    jump sm1ms023_02_end_scene
label sm1ms023_02_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(MS, 2, 0, 2, STUDIO, DEFAULT_SUBLOCATION, SD_STAIRS)
    return