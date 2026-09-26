label splashscreen:
    play music config.main_menu_music
    if renpy.get_autoreload() is True:
        return
    $ renpy.invoke_in_thread(GameAnalytics.session_start_event)
    scene black
    pause(0.2)
    show team-logo with Fade(0.6, 0.4, 0.6)
    pause(3.5)
    scene black
    show sm_logo_full
    with Fade(0.6, 0.4, 0.6)
    pause(3.5)
    return
label after_load:
    $ _preferences.show_empty_window = False
    $ player = SMPlayer()
    $ renovation_controller = RenovationController()
    $ DressCodeController.initialize_persistent_dress_codes()
    $ compatibility()
    if compatibility_trigger is True:
        $ print_verbose("Blocked rollback because of compatibility")
        $ renpy.block_rollback()
        $ compatibility_trigger = False
    return
label start:
    $ _preferences.show_empty_window = False
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    call screen difficulty_choice("difficulty_choice_done") with fade
    jump difficulty_choice_done
label difficulty_choice_done:
    call create_first_storyline from _call_create_first_storyline
    jump lst_1_overview
label create_first_storyline:
    $ player.create_storyline(MS)
    $ player.track_storyline(MS)
    $ StoryController.activate_story_line(MS)
    return
label city_map:
    scene black
    call screen city_map
    jump location_reenter
label location_reenter:
    scene black
    $ LocationController.enter()
    $ StoryController.location_reenter_sanity_check()
    call screen location_screen
    jump location_reenter
label buzz:
    play sound sfx_phone_buzz
    "Bzzzzz" with hpunch
    return
label knock:
    play sound sfx_knock_wood1
    "*knock knock*"
    return