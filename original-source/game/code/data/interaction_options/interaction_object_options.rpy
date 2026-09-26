init 1 python:
    INTERACTIONS_OBJECT_CATALOGUE = {
            "io-interact_with_object": {
                NAME: _("Interact"),
                ACTION: DISABLED_ACTION
                },

            "io-Sleep-with-time-skip": {
                NAME: _("Go to sleep"),
                ACTION: FUNCTION,
                TARGET: SMPlayer.skip_and_sleep,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8],
                DISABLED_HIDDEN: True
                },

            "io-read_photography_book": {
                NAME: _("Read Photography-101"),
                ACTION: FUNCTION,
                TARGET: PlayerController.read_book,
                PARAMS: PHOTOGRAPHY_101,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7],
                ENERGY_LIMIT: 1,
                DAILY_LIMIT: "io-read_photography_book"
                },

            "io-read_an_actor_prepares_book": {
                NAME: _("Read An Actor Prepares"),
                ACTION: FUNCTION,
                TARGET: PlayerController.read_book,
                PARAMS: AN_ACTOR_PREPARES,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7],
                ENERGY_LIMIT: 1,
                DAILY_LIMIT: "io-read_an_actor_prepares_book"
                },
            "io-read_stars_weekly_magazine": {
                NAME: _("Read Stars Weekly"),
                ACTION: FUNCTION,
                TARGET: PlayerController.read_book,
                PARAMS: STARS_WEEKLY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7],
                ENERGY_LIMIT: 1,
                DAILY_LIMIT: "io-read_stars_weekly_magazine"
                },

            "io-Buy_Energy_Drink": {
                NAME: _("Buy Energy Drink - $25"),
                ACTION: FUNCTION,
                TARGET: PlayerController.buy_item,
                PARAMS: ENERGY_DRINK,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8]
                },

            "io-fashion-magazine": {
                NAME: _("Read Fashion Magazine"),
                ACTION: FUNCTION,
                TARGET: THController.read_magazine,
                DAILY_LIMIT: "io-fashion-magazine"
                },

            "io-tech-magazine": {
                NAME: _("Read Tech Magazine"),
                ACTION: FUNCTION,
                TARGET: SCController.read_magazine,
                DAILY_LIMIT: "io-tech-magazine"
                },

            "io-animal-magazine": {
                NAME: _("Read Animal Magazine"),
                ACTION: FUNCTION,
                TARGET: ITController.read_magazine,
                DAILY_LIMIT: "io-animal-magazine"
                },

            "io-work-on-PC": {
                NAME: _("Start working"),
                ACTION: FUNCTION,
                TARGET: ITController.work_it_job,
                ENERGY_LIMIT: 4,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                DAYS: WORKDAYS_LIST,
                DAILY_LIMIT: "io-work-on-PC"
                },

            "io-studio-laptop": {
                NAME: _("Check Laptop"),
                ACTION: JUMP,
                TARGET: "studio_laptop",
                },

            "io-get-ns-panty": {
                NAME: _("Take panties"),
                ACTION: FUNCTION,
                TARGET: ITController.take_ns_panty
                },

            "io-pee_in_st_toilet": {
                NAME: _("Pee in the toilet"),
                ACTION: JUMP,
                TARGET: "pee_in_st_toilet"
                },

            "io-st_take_a_shower": {
                NAME: _("Take a shower"),
                ACTION: JUMP,
                TARGET: "st_take_a_shower"
                },
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
            }
