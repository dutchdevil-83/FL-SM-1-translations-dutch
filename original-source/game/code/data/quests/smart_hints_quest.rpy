init python:
    def hint_fsit002_weekend(action_sm):
        if (gt.curr_weekday in [5, 6]):
            return True
        return False


    def hint_fsit003_ms006_done(action_sm):
        if player.get_choice("first_job_to_unlock") == THEATER_STORY_LINE and player.is_storyline_item_finished(MS, "sm1ms006") == False:
            return True
        return False

    def hint_ms011_theater(action_sm):
        if player.is_storyline_item_finished(IT_STORY_LINE, "sm1fs_i004"):
            return True
        return False

    def hint_ms011_it_job(action_sm):
        if player.is_storyline_item_finished(TL_STORY, "sm1cs_tl001") and player.is_storyline_item_finished(DVH_STORY, "sm1cs_dvh001") and player.is_storyline_item_finished(KM_STORY, "sm1cs_km001") and player.is_storyline_item_finished(VS_STORY, "sm1cs_vs001"):
            return True
        return False

    def hint_ms011_post_it_job(action_sm):
        if player.get_choice("first_job_to_unlock") == THEATER_STORY_LINE:
            return True
        return False
    def hint_ms013(action_sm):
        if player.is_storyline_item_finished(TL_STORY, "sm1cs_tl002"):
            return False
        return True
    def hint_ms026(action_sm):
        if player.is_storyline_item_finished(TL_STORY, "sm1cs_tl007"):
            return False
        return True






    def hint_kv002_04(action_sm):
        return player.get_topic(TOPIC_PHOTOGRAPHY)
    def hint_kv004_lyssa(action_sm):
        if player.is_storyline_item_finished(MH_STORY, "sm1cs_mh001i"):
            return True
        return False

    def hint_bg004(action_sm):
        if player.completion_log_compare_date_for_item("sm1cs_bg003"):
            return False
        return True


    def hint_mas003(action_sm):
        points = CharacterController.get_character("ms").points
        if points >= 9:
            return False
        else:
            return int(points)









    def hint_fsit004_1_nari(action_sm):
        if player.is_storyline_item_finished(AG_STORY, "sm1cs_ag001") == False or player.is_storyline_item_finished(NS_STORY, "sm1cs_ns003") == True:
            return False
        return hint_fsit004_1_both([])

    def hint_fsit004_1_anna(action_sm):
        if player.is_storyline_item_finished(NS_STORY, "sm1cs_ns003") == False or player.is_storyline_item_finished(AG_STORY, "sm1cs_ag001") == True:
            return False
        return True
    def hint_fsit005(action_sm):
        if player.is_storyline_item_finished(MS, "sm1ms020") == False and player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS) < 40:
            return (1, player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS))
        if player.is_storyline_item_finished(MS, "sm1ms020") == False:
            return 2
        if player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS) < 40:
            return (3, player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS))
        return 0
    def hint_fsit005_2(action_sm):
        return CharacterController.get_character("ns").points + CharacterController.get_character("cw").points + CharacterController.get_character("ag").points + CharacterController.get_character("am").points


    def hint_fsit004_1_both(action_sm):
        if player.is_storyline_item_finished(AG_STORY, "sm1cs_ag001") == True and player.is_storyline_item_finished(NS_STORY, "sm1cs_ns003") == True:
            return False
        if player.is_storyline_item_finished(NS_STORY, "sm1cs_ns002"):
            return 2
        if player.is_storyline_item_finished(NS_STORY, "sm1cs_ns001"):
            return 1
        return 0





    def hint_ag002(a):
        if player.is_storyline_item_finished(IT_STORY_LINE, "sm1fs_i004"):
            return False
        return True
    def hint_ag002_2(a):
        if player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS) >= 20:
            return False
        return player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS)










    def hint_t005_1_0(a):
        if player.is_storyline_item_finished(VS_STORY, "sm1cs_vs002"):
            return False
        return True
    def hint_t005_1_1(a):
        worked = int(player.get_data(DATA_TH_SHOWS_SUCCESS))
        points = CharacterController.get_character("km").points + CharacterController.get_character("dvh").points + CharacterController.get_character("tl").points + CharacterController.get_character("vs").points
        if worked < 3 and points >= 10:
            return worked
        return False
    def hint_t005_1_2(a):
        worked = int(player.get_data(DATA_TH_SHOWS_SUCCESS))
        points = CharacterController.get_character("km").points + CharacterController.get_character("dvh").points + CharacterController.get_character("tl").points + CharacterController.get_character("vs").points
        if worked >= 3 and points < 10:
            return points
        return False
    def hint_t005_1_3(a):
        worked = int(player.get_data(DATA_TH_SHOWS_SUCCESS))
        points = CharacterController.get_character("km").points + CharacterController.get_character("dvh").points + CharacterController.get_character("tl").points + CharacterController.get_character("vs").points
        if worked < 3 and points < 10:
            return [worked, points]
        return False




    def hint_vs003_challenge_day(action_sm):
        return player.get_choice("sm1cs_vs002_alarm_day") if player.get_choice("sm1cs_vs002_alarm_day") else "Yo, game be broken"



    def hint_tl002(action_sm):
        if player.money > 50:
            return 50
        return [player.money]

    def hint_tl003(action_sm):
        if player.money > 100:
            return 100
        return player.money








    def hint_mv01Q02(action_sm):
        costume_budget_percentage = (pirates_movie.get_curr_budget_energy("costume_budget") / pirates_movie.total_costume_budget) * 100
        actress_budget_percentage = (pirates_movie.get_curr_budget_energy("actress_budget") / pirates_movie.total_actress_budget) * 100
        if pirates_movie.get_curr_budget_energy("costume_budget") == 0 and pirates_movie.get_curr_budget_energy("actress_budget") == 0:
            return 1
        if player.has_played_scene("sm1mv01s02"):
            if not pirates_movie.is_budget_energy_filled("actress_budget"):
                return 3
            if not player.has_played_scene("sm1mv01s03_1"):
                return 5
            if not player.has_played_scene("sm1mv01s03_2"):
                return 6
        if player.has_played_scene("sm1mv01s03_1"):
            if not player.has_played_scene("sm1mv01s03_2"):
                return 6
            if not pirates_movie.is_budget_energy_filled("costume_budget"):
                return 2
            if not player.has_played_scene("sm1mv01s02"):
                return 4
        if pirates_movie.is_budget_energy_filled("costume_budget") and not player.has_played_scene("sm1mv01s02"):
            return 4
        if pirates_movie.is_budget_energy_filled("actress_budget") and not player.has_played_scene("sm1mv01s03_1"):
            return 5
        if costume_budget_percentage > actress_budget_percentage:
            return 2
        if costume_budget_percentage < actress_budget_percentage:
            return 3
        return 0

    def hint_mv01Q04_1(action_sm):
        if pirates_movie.is_budget_energy_filled("props_budget"):
            return 2
        if pirates_movie.is_budget_energy_filled("props_energy"):
            return 1
        return 0
