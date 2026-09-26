label final_theater_job_setup:
    $ ss_rehearsal_mode = False
    $ ss_buttons_count = 12
    $ ss_pattern_length = 9
    $ ss_animtion_timer = 1.5
    $ ss_buttons_set = "theater1"
    $ simon_says_end_jump = "after_theater_job"
    jump simon_says_start
label rehearsal_theater_job_setup:
    $ ss_rehearsal_mode = True
    $ ss_buttons_count = 12
    $ ss_pattern_length = 9
    $ ss_animtion_timer = 1.5
    $ ss_buttons_set = "theater1"
    $ simon_says_end_jump = "after_theater_job"
    jump simon_says_start
label after_theater_job:
    $ THController.after_th_job()
    jump location_reenter