label it_job_setup_nonogram:
    $ nono_row_hints = []
    $ nono_col_hints = []
    $ nono_match_col = []
    $ nono_match_row = []
    $ nono_hints_max = 0
    $ grid_padding = 5
    $ nonogram_background = "sm1fs-i003-monitor-render"
    $ nonogram_end_jump = "after_it_job"
    $ random.seed()
    $ nonogram_difficulity = player.get_choice("it_job_difficulity")
    $ nonogram_selected_list = nonogram_puzzle_dict.get(nonogram_difficulity)
    $ random_nonogram = renpy.random.choice(nonogram_selected_list)
    $ base64_string = random_nonogram[0]
    $ grid_cols = random_nonogram[1]
    $ grid_rows = random_nonogram[2]
    $ grid_size = grid_rows * grid_cols
    $ Nonogram.generate_hints(base64_string, grid_rows, grid_cols)
    $ nono_buttons_list = []
    $ Nonogram.generate_buttons()
    jump nonogram_game
label after_it_job:
    if nonogram_puzzle_solved:
        $ ITController.it_job_daily_reward()
    $ ITController.after_it_job()
    jump location_reenter