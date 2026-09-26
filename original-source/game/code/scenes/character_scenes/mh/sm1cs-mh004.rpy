image sm1cs_mh004-glambot-1 = Movie(play = "images/Character-Scenes/mh/s004/anim/sm1cs-mh004-a05-4x-60fps.webm", start_image = "sm1cs-mh004-a05 mh-talk-mc-glambot-000", image = "sm1cs-mh004-a05 mh-talk-mc-glambot-120", loop = False)
label sm1cs_mh004:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.6, 1.5, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    $ renpy.music.set_volume(1.0, 0.0, "sound4" )
    play sound2 sfx_parkday_birds fadein 1.5 volume 0.5
    play sound sfx_heels_steps1 fadein 1.0 loop
    scene sm1cs-mh004-01-mc-door with dissolve
    $ renpy.music.play(audio.music_romantic_conundrum, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_romantic_conundrum_reverbed, "music2", True, None, True, 0.0)
    pause
    play sound sfx_heels_steps2 loop
    scene sm1cs-mh004-02-lc-walk with dissolve
    pause
    play sound sfx_door_open1
    scene sm1cs-mh004-03-mh-talk-mc with dissolve
    play voice3 lissa_hey noloop
    mh "Looking sharp, [mcname]."
    scene sm1cs-mh004-04-mc-talk-mh with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thanks, Lyssa. Ready to go?"
    scene sm1cs-mh004-a05 mh-talk-mc-glambot-000 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound3 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    play sound4 ["<silence 4.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs_mh004-glambot-1
    pause
    play voice3 lissa_aga noloop
    mh "Of course, lead the way."
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(0.4, 3.0, "sound2" )
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    stop sound4 fadeout 1.0
    scene sm1cs-mh004-06-mc-mh-restaurant with fade
    $ renpy.music.set_volume(0.0, 4.0, "music" )
    play sound sfx_bed_slide2 volume 0.5
    pause
    scene sm1cs-mh004-07-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "You picked a nice place for dinner."
    scene sm1cs-mh004-08-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Thank you. I learned about it from a beautiful woman."
    play sound sfx_cloth_rustling2
    scene sm1cs-mh004-09-mc-talk-mh with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.5
    mc "I'm really happy that we're doing this."
    scene sm1cs-mh004-10-mh-talk-mc with dissolve
    play voice3 lissa_ugu2 noloop
    mh "I'm... Happy we are too."
    play sound sfx_cloth_rustling4
    scene sm1cs-mh004-11-mc-talk-mh with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "So... How have things been?"
    scene sm1cs-mh004-12-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "Good. My practice has been steady, good clients. Been staying busy."
    scene sm1cs-mh004-13-mc-talk-mh with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "That's good! I'm happy to hear that, Lyssa."
    scene sm1cs-mh004-14-mh-talk-mc with dissolve
    play voice3 lissa_thinking1 noloop volume 1.5
    mh "And you? How's... Your newest thing going."
    scene sm1cs-mh004-13-mc-talk-mh with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    if True:
        mc "Well! I think it's going well at least. The foundation of it is strong though."
    else:
        mc "Well! Better than we could have even hoped for."
    play sound sfx_carpet_footsteps2 loop
    mh "Good."
    stop sound fadeout 1.0
    scene sm1cs-mh004-15-waiter-talk with dissolve
    play voice4 boy9_hey_easy noloop volume 1.4
    "Waiter" "Good evening. Can I interest either of you in some wine?"
    scene sm1cs-mh004-16-mh-talk-waiter with dissolve
    play voice3 lissa_yes noloop
    mh "Yes, please."
    scene sm1cs-mh004-17-mc-talk-waiter with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Me too."
    scene sm1cs-mh004-18-waiter-talk with dissolve
    play voice4 boy9_yes_aga1 noloop
    "Waiter" "I'll bring that out right away then. Do you two need some more time with the menu?"
    scene sm1cs-mh004-19-mc-talk-waiter with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, that would be great."
    scene sm1cs-mh004-15-waiter-talk with dissolve
    play voice4 boy9_yes_yep1 noloop
    "Waiter" "Then I shall check back in with you in a bit."
    play sound sfx_carpet_footsteps2 volume 1.5
    scene sm1cs-mh004-20-mc-talk-mh with dissolve
    stop sound fadeout 3.0
    play voice2 mc_thinking_hmm4 noloop
    mc "How's, uhm, Oliver doing?"
    scene sm1cs-mh004-21-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "He's good. He's become an excellent paralegal, even being scouted by some bigger firms."
    scene sm1cs-mh004-22-mc-talk-mh with dissolve
    play voice2 mc_angry_really noloop
    mc "Really? They do that?"
    scene sm1cs-mh004-23-mh-talk-mc with dissolve
    play voice3 dahlia_yes_aga noloop volume 0.8
    mh "They do. You get seen in court enough times, and you win enough cases, every major firm in town wants to know why."
    scene sm1cs-mh004-24-mh-talk-mc with dissolve
    mh "It's cheaper to hire a paralegal than to buy out a lawyer."
    scene sm1cs-mh004-25-mc-talk-mh with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Ahhh. Is he... Thinking about it?"
    play sound sfx_carpet_footsteps2 fadein 3.5 loop
    scene sm1cs-mh004-26-mh-talk-mc with dissolve
    play voice3 dahlia_no_simple noloop
    mh "I don't think so. Even though I've told him to. He'll have more opportunities at a bigger firm."
    mh "However, he is enamored with working for me. Truthfully, I don't think I could lose him and keep doing as well as I am, but I want him to do well."
    mh "So we'll see what the future brings."
    scene sm1cs-mh004-25-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Hopefully he stays around then. At least for a bit. You really do deserve to have all the success you are having."
    scene sm1cs-mh004-23-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "Thanks, [mcname]."
    stop sound fadeout 1.0
    scene sm1cs-mh004-27-waiter-talk with dissolve
    play voice4 boy9_hey_positive noloop
    "Waiter" "Your wine."
    play sound sfx_cup_slide1 volume 1.7
    scene sm1cs-mh004-28-mh-talk-waiter with dissolve
    play voice3 lissa_ugu noloop
    mh "Thank you."
    scene sm1cs-mh004-29-waiter-talk with dissolve
    play voice4 boy9_thinking_emm2 noloop
    "Waiter" "Have you two made any decisions yet?"
    scene sm1cs-mh004-30-mc-talk-waiter with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Uhm, I think I'll take the house special."
    scene sm1cs-mh004-31-mh-talk-waiter with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    mh "I'll do the same."
    scene sm1cs-mh004-32-waiter-talk with dissolve
    play voice4 boy9_happy_nice3 noloop
    "Waiter" "Wonderful, you both will not be disappointed. We've had a lot of rave reviews about it lately."
    play sound3 sfx_carpet_footsteps2
    scene sm1cs-mh004-33-mh-wine with dissolve
    stop sound3 fadeout 2.0
    play sound sfx_drink_loop1 loop volume 1.7
    pause
    scene sm1cs-mh004-34-mc-wine with dissolve
    pause
    play sound sfx_cup_place1
    scene sm1cs-mh004-35-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "*Sighs*"
    scene sm1cs-mh004-36-mc-talk-mh with dissolve
    play voice2 mc_surprised_huh7 noloop
    pause
    scene sm1cs-mh004-37-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "What are we doing here, [mcname]?"
    scene sm1cs-mh004-38-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Uhm..."
    scene sm1cs-mh004-40-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "Do you remember what we had?"
    scene sm1cs-mh004-39-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Of course I do."
    jump sm1cs_mh004_flashback
label sm1cs_mh004_flashback:
    $ renpy.music.set_volume(1.0, 2.4, "music" )
    $ renpy.music.set_volume(0.0, 8.0, "music2" )
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    play sound sfx_memory_cloud_change1
    scene d15s06-02_mc_mh_montage_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    play sound sfx_memory_cloud_change1
    scene d15s06-15_mc_mh_cookingmontage_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    play sound sfx_memory_cloud_change1
    scene d12s04-71-01 mh-mc-lyssa-stand-touch-dick_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    play sound sfx_memory_cloud_change1
    scene d17s05a-40 mh-lyssa-solo_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    play sound sfx_memory_cloud_change1
    scene d14s04-34 mh-hits-puck-2_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    play sound sfx_memory_cloud_change1
    scene d19s03-23 mc-kiss-mh-passionately_c1_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    play sound sfx_memory_cloud_change1
    scene d10s04-68 mc-mh-he-cum_c3_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    play sound sfx_memory_cloud_change1
    scene d19s03-47 mc-spreads-mh-legs_c1_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    play sound sfx_memory_cloud_change1
    scene d19s03-87 mh-cums-on-wall-mh-cums-back_c1_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    play sound sfx_memory_cloud_change1
    scene d19s03-103 mc-kisses-mh-forehead_c1_flashback
    show screen flashback_screen(True, False)
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    pause
    hide screen flashback_screen
    $ renpy.music.set_volume(0.0, 4.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(0.5, 2.0, "sound2" )
    play sound sfx_memory_cloud_change1
    scene sm1cs-mh004-39-mc-talk-mh
    with Fade(0.25, 0.05, 0.5, color="#fffefd")
    play voice2 mc_disappointed_ehh3 noloop
    mc "I miss what we had."
    scene sm1cs-mh004-40-mh-talk-mc with dissolve
    play voice3 lissa_ugu3 noloop
    mh "I do too."
    scene sm1cs-mh004-41-mh-talk-mc with dissolve
    play voice3 lissa_moan1 noloop
    mh "I was really hurt, you know?"
    mh "When I asked if you'd leave town with me, I..."
    mh "I didn't think you'd choose to open a porn studio with Stacy instead."
    scene sm1cs-mh004-42-mc-talk-mh with dissolve
    play voice2 d2s12_emmm noloop
    mc "The opportunity was there, and-"
    scene sm1cs-mh004-43-mh-talk-mc with dissolve
    play voice3 dahlia_sex_closedmoan2 noloop
    mh "And what, [mcname]? What about what we had?"
    scene sm1cs-mh004-44-mc-talk-mh with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "Lyssa..."
    scene sm1cs-mh004-45-mc-talk-mh with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I never meant to hurt you. The choice I made, I... I've always given up on everything halfway through, my whole life."
    mc "Hell, I'm a college dropout, and I was almost done with that."
    mc "Shutting down Fetish Locator was the first thing I feel like I ever really finished. Then Stacy proposed this and... It felt like something I could actually do."
    scene sm1cs-mh004-39-mc-talk-mh with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I never meant to make you think I was choosing something over you. This was just... Something I had to do."
    scene sm1cs-mh004-46-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "I can understand that."
    scene sm1cs-mh004-47-mh-talk-mc with dissolve
    play voice3 lissa_haha noloop
    mh "You don't become a successful lawyer like me without a drive to prove something."
    scene sm1cs-mh004-48-mh-talk-mc with dissolve
    play voice3 lissa_thinking2 noloop volume 1.6
    mh "What about Stacy?"
    scene sm1cs-mh004-49-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "What about her?"
    scene sm1cs-mh004-50-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "Aren't you two dating?"
    scene sm1cs-mh004-51-mc-talk-mh with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Yeah, we are."
    scene sm1cs-mh004-52-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "How would she feel about this?"
    scene sm1cs-mh004-53-mc-talk-mh with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Stacy all but jumped for joy when I left for this date."
    scene sm1cs-mh004-54-mh-talk-mc with dissolve
    play voice3 lissa_oh2 noloop
    mh "She knows you're here?"
    scene sm1cs-mh004-55-mc-talk-mh with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh."
    scene sm1cs-mh004-56-mh-talk-mc with dissolve
    play voice3 lissa_moan3 noloop
    mh "How can we be together while you're dating Stacy?"
    scene sm1cs-mh004-57-mc-talk-mh with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Stacy's cool-"
    scene sm1cs-mh004-58-mh-talk-mc with dissolve
    play voice3 dahlia_angry_oh noloop
    mh "Maybe I'm not."
    scene sm1cs-mh004-59-mc-talk-mh with dissolve
    play voice2 mc_disappointed_ah2 noloop
    if persistent.is_special:
        mc "Lyssa... Stacy is my sister, and she's always going to be a part of my life."
    else:
        mc "Lyssa... Stacy is my best friend, and she's always going to be a part of my life."
    scene sm1cs-mh004-60-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "I know..."
    scene sm1cs-mh004-62-mc-talk-mh with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "But I want you to be a part of my life too."
    scene sm1cs-mh004-61-mh-talk-mc with dissolve
    play voice3 dahlia_sex_closedmoan3 noloop
    mh "[mcname], I..."
    mh "..."
    mh "I don't know if I can do this, [mcname]."
    scene sm1cs-mh004-63-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "You're asking a lot of me. I don't know if I can handle you dating Stacy, and God knows who else. Or the fact that you're starting a porn studio."
    scene sm1cs-mh004-64-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "I understand..."
    scene sm1cs-mh004-60-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "But I miss what we had, and... I have my reservations, and I'm still hurt, but..."
    mh "I want to try. Maybe what's required is that I grow to accept you, like you accepted me."
    scene sm1cs-mh004-65-mc-talk-mh with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Lyssa, I don't know what to say."
    scene sm1cs-mh004-66-mh-talk-mc with dissolve
    play voice3 dahlia_hey_active1 noloop
    mh "Just because I agreed to try this, doesn't mean anything's changed though. You still need to woo me, [mcname]."
    scene sm1cs-mh004-64-mc-talk-mh with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I promise you, you're getting maximum effort from here on out."
    scene sm1cs-mh004-66-mh-talk-mc with dissolve
    play voice3 dahlia_yes_yeah3 noloop
    mh "Good. I'm excited to see you at your best."
    play sound sfx_carpet_footsteps2 fadein 1.5
    scene sm1cs-mh004-67-waiter with dissolve
    pause
    scene sm1cs-mh004-68-mh-talk-mc with dissolve
    play voice3 dahlia_surprised_oh noloop
    mh "Oh, it looks like the food has arrived."
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.6, 3.5, "music" )
    $ renpy.music.set_volume(1.0, 1.5, "sound2" )
    $ renpy.music.set_volume(1.0, 1.5, "sound3" )
    stop sound2 fadeout 1.5
    play sound3 sfx_parknight_crickets fadein 3.0 volume 0.5
    scene sm1cs-mh004-69-mc-mh with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.0, 3.0, "music2" )
    pause
    scene sm1cs-mh004-70-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "Thank you for a wonderful date, [mcname]."
    scene sm1cs-mh004-71-mc-talk-mh with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Thank you for letting me take you on this wonderful date, Lyssa."
    scene sm1cs-mh004-72-mh-talk-mc with dissolve
    play voice3 lissa_aga noloop
    mh "I'm looking forward to the next one."
    scene sm1cs-mh004-71-mc-talk-mh with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Me too!"
    scene sm1cs-mh004-70-mh-talk-mc with dissolve
    play voice3 lissa_laugh noloop
    mh "It better be a doozy."
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-mh004-73-mh-kiss-mc with dissolve
    play voice2 mc_thinking_mmm7 noloop
    play voice3 lissa_moan1 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-mh004-74-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "Get home safe."
    scene sm1cs-mh004-75-mc-inner-talk with dissolve
    pause
    play sound sfx_door_closed2
    scene sm1cs-mh004-76-mc-inner-talk with dissolve
    play voice2 mc_happy_yes1 noloop
    mct "Nailed it."
    mct "Now I just need to figure out how the hell I'm going to top that."
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop sound3 fadeout 1.5
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    call sm1cs_mh004_get_point from _call_sm1cs_mh004_get_point
    jump sm1cs_mh004_exit
label sm1cs_mh004_exit:
    $ StoryController.end_scene(MH_STORY, 3, 0, 3)
    return
label sm1cs_mh004_get_point:
    $ CharacterController.get_character("mh").add_point()
    $ player.set_choice("sm1cs_mh004_got_point")
    return
label sm1cs_mh004_unlocks:
    call sm1cs_mh004_get_point from _call_sm1cs_mh004_get_point_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MH_STORY)
    return