init 1 python:
    INTERACTIONS_LOCATION_CATALOGUE = {
            "io-TH_Work": {
                NAME: _("Work as a stagehand"),
                ACTION: FUNCTION,
                TARGET: THController.work_th_job,
                ENERGY_LIMIT: 3,
                TIMESLOTS: [TIMESLOT_7],
                DAYS: [THController.final_show_day],
                DAILY_LIMIT: "io-final_show_at_th"
                },
            "io-TH_Rehearsal": {
                NAME: _("Rehearsal for the show"),
                ACTION: FUNCTION,
                TARGET: THController.work_th_job,
                ENERGY_LIMIT: 3,
                TIMESLOTS: [TIMESLOT_7],
                DAYS: [THController.rehearsal_day_1, THController.rehearsal_day_2, THController.rehearsal_day_3],
                DAILY_LIMIT: "io-rehearsal_at_th"
                },
            "io-SD_Peek_On_Stacy": {
                NAME: _("Peek on Stacy"),
                ACTION: JUMP,
                TARGET: "peek_on_stacy_peeing",
                TIMESLOTS: [TIMESLOT_7],
                DAYS: [FRIDAY]
                },
            "io-MH003_01": {
                NAME: _("Romance Lyssa"),
                ACTION: CALL,
                TARGET: "sm1cs_mh003_1i",
                TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7],
                DAYS: ALLDAYS_LIST
                },
            "io-lly-Q-MH004": {
                NAME: _("Take Lyssa on a date"),
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
                TIMESLOTS: [TIMESLOT_7],
                DAYS: ALLDAYS_LIST
                },
            }
