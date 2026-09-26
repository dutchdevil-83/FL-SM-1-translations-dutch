label simon_says_start:
    if only_story_mode is True:
        $ player.log_action("Skipped 'TH Job' minigame because of 'Story Mode'")
        jump simon_says_only_story
    else:
        $ player.log_action("Started 'TH Job' minigame")
    $ renpy.block_rollback()
    $ simon_says_win = False
    $ quick_menu = False
    $ ss_anim_end = False
    $ ss_input_hint = False
    $ ss_buttons_list = SimonSays.generate_buttons()
    $ ss_pattern_list = []
    $ ss_pattern_list_for_hint = []
    $ ss_pattern_list_for_anim = []
    $ ss_input_list = []
    $ SimonSays.generate_pattern()
    $ ss_buttons_list = SimonSays.shuffle_with_seed(ss_buttons_list)
    call screen simon_says
label simon_says_end:
    if not SimonSays.check_input():
        $ simon_says_win = True
        $ player.log_action("Passed 'TH Job' minigame")
    else:
        $ player.log_action("Failed 'TH Job' minigame")
    $ renpy.block_rollback()
    $ quick_menu = True
    jump expression simon_says_end_jump
label simon_says_only_story:
    scene ss_window_no_minigame
    show screen wait_screen(THEATER_JOB)
    pause 5.0
    hide screen wait_screen
    $ simon_says_win = True
    jump expression simon_says_end_jump