label sm1ms011:
    $ sm1ms011_talk_ns = False
    $ sm1ms011_talk_ag = False
    $ sm1ms011_talk_am = False
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    scene black
    show screen scene_transistion("Thirty minutes later")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play music cute_times
    play sound sfx_door_open1
    scene sm1ms011-01 mc-sy-entry1_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1ms011-01 mc-sy-entry1_c2 with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "What's up?"
    scene sm1ms011-02 mc-sy-entry2_c1 with dissolve
    mct "It's late. I should tell her about AmRose's visit another time."
    play voice2 d1s2_mchey noloop volume 1.5
    mc "Not much. Just another day in the city with the best girl ever."
    scene sm1ms011-02 mc-sy-entry2_c2 with dissolve
    play voice3 stacy_disappointed_oh2 noloop
    pause
    scene sm1ms011-03 mc-sy-entry3_c1 with dissolve
    play sound mc_kiss1
    $ renpy.music.set_volume(1.0, 0.5, "sound3" )
    play sound3 sfx_cloth_rustling2 noloop
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Mwaaah."
    scene sm1ms011-03 mc-sy-entry3_c2 with dissolve
    play sound mc_kiss2
    pause
    scene sm1ms011-04 mc-sy-point_c2 with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Oh right, I almost forgot."
    sy "I found someone who might be a worthy addition to our crew."
    scene sm1ms011-04 mc-sy-point_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Our crew?"
    scene sm1ms011-05 mc-sy-ask_c2 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah. Every top porn studio has a crew to handle making a scene. This new person could be our camera girl."
    sy "She's super skilled, probably very in demand."
    scene sm1ms011-05 mc-sy-ask_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay?"
    call sm1ms011_unlock_kv_storyline from _call_sm1ms011_unlock_kv_storyline
    if player.get_choice("Current_job_to_unlock") == IT_STORY_LINE:
        call sm1ms011_it from _call_sm1ms011_it
    if player.get_choice("Current_job_to_unlock") == THEATER_STORY_LINE:
        call sm1ms011_t from _call_sm1ms011_t
    scene sm1ms011-04 mc-sy-point_c1 with dissolve
    queue voice3 stacy_thinking_hmm1 noloop
    sy "One more thing for you to keep in mind."
    sy "I've discovered some other {b}jobs{/b} in the city."
    scene sm1ms011-04 mc-sy-point_c2 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "So if you want to expand your horizons, come check in with me."
    play voice2 mc_yes_yes3 noloop
    mc "Totally."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    call sm1ms011_unlock_more_factions from _call_sm1ms011_unlock_more_factions
    $ StoryController.end_scene(MS, 3, 0, 2)
    return
label sm1ms011_unlock_kv_storyline:
    $ StoryController.activate_story_line(KV_STORY, True)
    return
label sm1ms011_unlock_more_factions:
    $ StoryController.activate_story_line(MORE_FACTIONS, True)
    return
label sm1ms011_unlocks:
    if player.get_choice("Current_job_to_unlock") == IT_STORY_LINE:
        call sm1ms011_it_unlocks from _call_sm1ms011_it_unlocks
    if config_storyline_mode is True:
        $ execute_storyline_config(MS)
    return