init python:
    def interaction_is_disabled_ms008(data):
        if player.is_storyline_item_finished(KV_STORY, "sm1cs_kv004") == False:
            return _("You need to progress Kanya storyline first")
        return False

    def io_is_hidden_MS015(io):
        return player.get_choice("io_MS015_first")
    def io_is_hidden_MS018(io):
        return player.get_choice("io_MS018_first")
    def io_is_hidden_NS_RENO(io):
        return player.get_choice("io_ns_renovation")
    def io_is_hidden_TL_RENO(io):
        return player.get_choice("io_tl_renovation")
    def io_is_hidden_KV_RENO(io):
        return player.get_choice("io_kv_renovation")
    def io_is_hidden_AM_RENO(io):
        return player.get_choice("io_am_renovation") or player.get_choice("sm1cs_am005_failed_am")
    def io_is_hidden_VS_RENO(io):
        return player.get_choice("io_vs_renovation")
    def io_is_hidden_DC_RENO(io):
        return player.get_choice("io_dc_renovation")


    def io_is_hidden_SY002(io):
        return gt.curr_timeslot != TIMESLOT_8 or (player.get_choice("io_sy002_clicked") and not player.completion_log_compare_date_for_item("sm1cs_sy002_repeatable", 3))
    def io_is_hidden_SY003(io):
        return gt.curr_timeslot != TIMESLOT_8 or (player.get_choice("io_sy003_clicked") and not player.completion_log_compare_date_for_item("sm1cs_sy003_repeatable", 2))





















    def is_hidden_NS_sex_repeatable01(io):
        if curr_location == STUDIO and gt.curr_timeslot in [TIMESLOT_7, TIMESLOT_8]:
            return False
        return True
























    def is_hidden_TL_sex_repeatable01(io):
        if curr_location == STUDIO and gt.curr_timeslot in [TIMESLOT_6, TIMESLOT_7, TIMESLOT_8]:
            return False
        return True

    def io_not_bathroom_pee01(io):
        return "pee01" in CharacterController.get_character(interaction_character.codename).get_schedule_in_location(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position).state









    def io_is_hidden_mv01s02(io):
        if player.has_played_scene("sm1mv01s02"):
            return True
        if pirates_movie.is_budget_energy_filled("costume_budget"):
            return False
        return True

    def io_is_hidden_mv01s03_1(io):
        if player.has_played_scene("sm1mv01s03_1"):
            return True
        if pirates_movie.is_budget_energy_filled("actress_budget"):
            return False
        return True

    def io_is_hidden_mv01s03_2(io):
        return not player.has_played_scene("sm1mv01s03_1")
