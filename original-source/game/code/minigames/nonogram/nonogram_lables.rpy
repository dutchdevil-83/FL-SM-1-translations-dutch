label nonogram_game:
    $ nonogram_puzzle_solved = False
    if only_story_mode is True:
        $ player.log_action("Skipped 'IT Job' minigame because of 'Story Mode'")
        jump nonogram_only_story
    else:
        $ player.log_action("Started 'IT Job' minigame")
    $ renpy.block_rollback()
    $ quick_menu = False
    $ mt = SMGameTime("01 Jan Mon 00 00 00")
    $ nonogram_timer_pause = False
    $ nonogram_submit = False
    call screen nonogram_game()
label nonogram_done:
    if Nonogram.check_puzzle(nono_buttons_list, grid_rows, grid_cols):
        $ nonogram_puzzle_solved = True
        $ player.log_action("Passed 'IT Job' minigame")
    else:
        $ player.log_action("Failed 'IT Job' minigame")
    $ renpy.block_rollback()
    $ quick_menu = True
    jump expression nonogram_end_jump
label nonogram_only_story:
    scene black
    show expression nonogram_background + "-code"
    show screen wait_screen(IT_WORK)
    pause 5.0
    hide screen wait_screen
    $ nonogram_puzzle_solved = True
    jump expression nonogram_end_jump