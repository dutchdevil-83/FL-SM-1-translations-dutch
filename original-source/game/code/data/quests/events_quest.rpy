init python:
    def event_click_sy_simple(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "sy"):
            return 1
        return False
    def event_enter_it(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == IT_OFFICE):
            return 1
        return False
    def event_click_sy(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "sy" and gt.curr_timeslot not in [TIMESLOT_1, TIMESLOT_2]):
            return 1
        return False
    def event_talk_sy(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_TALK and action_sm[TARGET] == "sy" and gt.curr_timeslot not in [TIMESLOT_1, TIMESLOT_2]):
            return 1
        return False
    def event_talk_sy_in_bed(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_TALK and action_sm[TARGET] == "sy" and gt.curr_timeslot in [TIMESLOT_1, TIMESLOT_2] and curr_position == SD_MATTRESS):
            return 1
        return False
    def event_go_home(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == STUDIO):
            return 1
        return False
    def event_enter_photo_dojo(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == PHOTO_DOJO):
            return 1
        return False
    def event_enter_71_store(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == SHOP_71STORE):
            return 1
        return False
    def event_next_morning_working_day(action_sm):
        if (action_sm and action_sm["type"] == ACTION_AFTER_SLEEP and gt.curr_day not in [SATURDAY, SUNDAY]):
            return 1
        return False
    def event_after_it_work(action_sm):
        if (action_sm and action_sm["type"] == IT_JOB_FINISHED):
            return 1
        return False
    def event_talk_ag(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_TALK and action_sm[TARGET] == "ag" and gt.curr_timeslot in [TIMESLOT_5, TIMESLOT_6]):
            return 1
        return False
    def event_talk_ag(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_TALK and action_sm[TARGET] == "ag" and gt.curr_timeslot in [TIMESLOT_5, TIMESLOT_6]):
            return 1
        return False
    def event_enter_theater(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == THEATER):
            return 1
        return False
    def event_talk_km_in_dressigroom(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_TALK and action_sm[TARGET] == "km" and curr_location == THEATER and curr_position == LTH_DRESSINGROOM_2):
            return 1
        return False
    def event_talk_dvh_in_office(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_TALK and action_sm[TARGET] == "dvh" and curr_location == THEATER and curr_position == LTH_DIRECTORS_OFFICE):
            return 1
        return False
    def event_enter_lly(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == LYSSAS_HOUSE and gt.curr_timeslot in [TIMESLOT_6, TIMESLOT_7]):
            return 1
        return False
    def event_renovation_finished(action_sm):
        if (action_sm and player.is_storyline_item_finished(MS, "sm1ms020")):
            return 1
        return False


    def event_q_ms002_4(action_sm):
        if (action_sm and action_sm["type"] == ACTION_AFTER_SLEEP):
            event_q_ms002_4_unlocks()
            return 1
        return False
    def event_ms002_6(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_TALK and action_sm[TARGET] == "sy" and gt.curr_timeslot not in [TIMESLOT_1, TIMESLOT_2] and curr_position == SD_KITCHEN) and CharacterController.get_character("sy").get_character_pose(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position) not in SY_CUSTOM_POSES_LIST:
            return 1
        return False
    def event_ms002_0(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == WURST_DELIVERY):
            return 1
        return False
    def event_ms002(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "nr"):
            return 1
        return False
    def event_q_ms002_3(action_sm):
        if (gt.curr_timeslot in [TIMESLOT_8, TIMESLOT_1, TIMESLOT_2]):
            event_q_ms002_3_unlocks()
            return 1
        return False
    def event_ms002_5(action_sm):
        if (action_sm and action_sm["type"] == MONEY_RECEIVED and player.money >= 200):
            return 1
        return False
    def event_ms003_0(action_sm):
        if (action_sm and action_sm["type"] == ACTION_SLEEP):
            event_ms003_0_unlocks()
            return 1
        return False
    def event_ms003_2(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == IT_OFFICE and gt.curr_timeslot == TIMESLOT_4):
            return 1
        return False
    def event_ms006(action_sm):
        if (action_sm and action_sm["type"] == ACTION_AFTER_SLEEP): 
            return 1
        return False
    def event_ms011_1(action_sm):
        if (action_sm and player.is_storyline_item_finished(TL_STORY, "sm1cs_tl001") and player.is_storyline_item_finished(DVH_STORY, "sm1cs_dvh001") and player.is_storyline_item_finished(KM_STORY, "sm1cs_km001") and player.is_storyline_item_finished(VS_STORY, "sm1cs_vs001")) and player.is_storyline_item_finished(IT_STORY_LINE, "sm1fs_i004"):
        
        
            return 1
        return False
    def event_ms010_1(action_sm):
        if (player.is_storyline_item_finished(ARJ_STORY, "sm1cs_arj001") and action_sm["type"] == ENTER_LOCATION):
            return 1
        return False
    def event_ms010_2(action_sm):
        if (player.completion_log_compare_date_for_item("sm1cs_arj001", 1) and action_sm["type"] == ENTER_LOCATION):
            return 1
        return False
    def event_ms016_2(action_sm):
        if ((player.get_choice("io_MS015_first") or player.get_choice("io_MS018_first")) and renovation_controller.get_progress() >= 50):
        
            return 1
        return False
    def event_ms019_2(action_sm):
        if (renovation_controller.get_progress() >= 100 and (player.get_choice("io_MS015_second") or player.get_choice("io_MS018_second"))):
            return 1
        return False
    def event_ms027(action_sm):
        if player.get_choice("first_movie") == "pirates_movie" and player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s11i"):
            return 1
        return False
    def event_ms027_2(action_sm):
        if player.get_choice("first_movie") == "pirates_movie" and player.completion_log_compare_date_for_item("sm1mv01s11i", 2) and action_sm and action_sm["type"] == ACTION_AFTER_SLEEP:
            return 1
        return False


    def event_arj001_1(action_sm):
        if (player.completion_log_compare_date_for_item("sm1ms007") and action_sm["type"] == ENTER_LOCATION):
            return 1
        return False
    def event_arj001_3(action_sm):
        if (action_sm and action_sm["type"] == MAP_LOCATION_CLICK and action_sm[TARGET] == LocationController.get_location(STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE).get_codename() and gt.curr_timeslot in [TIMESLOT_3, TIMESLOT_4]) or (LocationController.get_map_location(STARDUCKS).get_location().get_discovered_status() is False) :
            return 1
        return False
    def event_arj002(action_sm):
        if (player.is_storyline_item_finished(MS, "sm1ms010") and action_sm["type"] == ENTER_LOCATION):
            return 1
        return False


    def event_kv002_02(action_sm):
        if (action_sm and action_sm["type"] == ITEM_PURCHASED and action_sm[TARGET] == PHOTOGRAPHY_101):
            return 1
        return False
    def event_kv002_03(action_sm):
        if (action_sm and action_sm["type"] == USE_ITEM and action_sm[TARGET] == PHOTOGRAPHY_101):
            return 1
        return False
    def event_kv002_04(action_sm):
        if (action_sm and action_sm["type"] == TOPIC_REACHED_VALUE and action_sm[TARGET] == TOPIC_PHOTOGRAPHY and action_sm[VALUE] >= 5):
            return 1
        return False
    def event_kv005_1(action_sm):
        if (action_sm and action_sm["type"] == ACTION_AFTER_SLEEP):
            if player.completion_log_compare_date_for_item("sm1cs_kv004", 2):
                return 1
        return False
    def event_kv005_2(action_sm):
        if player.has_played_scene("sm1cs_kv005_start"):
            if player.completion_log_compare_date_for_item("sm1cs_kv005_start"):
                if player.has_played_scene("sm1cs_kv005_part_2"):
                    if player.completion_log_compare_date_for_item("sm1cs_kv005_part_2"):
                        return 1
                    else:
                        return False
                else:
                    return 1
            else:
                return False
        else:
            return 1


    def event_mas001_1(action_sm):
        if (action_sm and action_sm["type"] == ACTION_AFTER_SLEEP and CharacterController.get_character("ms").points >= 3):
            return 1
        return False
    def event_mas001_2(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == WURST_DELIVERY) and curr_position == WD_OUTSIDE and gt.curr_timeslot in [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6]:
            return 1
        return False
    def event_mas002(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "ms" and CharacterController.get_character("ms").points >= 6) and curr_location == WURST_DELIVERY and curr_position == WD_SEATS and gt.curr_timeslot in [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7]:
            return 1
        return False
    def event_mas003(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == WURST_DELIVERY) and curr_location == WURST_DELIVERY and gt.curr_timeslot in [TIMESLOT_6, TIMESLOT_7, TIMESLOT_8] and CharacterController.get_character("ms").points >= 9:
            return 1
        return False


    def event_mh_005(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == LYSSAS_HOUSE and gt.curr_timeslot in [TIMESLOT_7, TIMESLOT_8]):
            return 1
        return False
    def event_mh_006(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == LYSSAS_HOUSE and gt.curr_timeslot in [TIMESLOT_6, TIMESLOT_7] and gt.curr_day in [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SUNDAY]):
            return 1
        return False
    def event_mh_008_3(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == LYSSAS_HOUSE and gt.curr_timeslot in [TIMESLOT_6]):
            return 1
        return False


    def event_bg001(action_sm):
        if(action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == PHOTO_DOJO and gt.curr_timeslot in [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8]):
            if player.completion_log_compare_date_for_item("sm1cs_kv004"):
                return 1
        return False
    def event_bg002_time(action_sm):
        if player.completion_log_compare_date_for_item("sm1cs_bg001"):
            return 1
        return False
    def event_bg003_time(action_sm):
        if player.completion_log_compare_date_for_item("sm1cs_bg002"):
            return 1
        return False
    def event_bg002(action_sm):
        if(action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "bg" and gt.curr_timeslot in [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8]):
            if curr_position == LPD_KITCHEN and CharacterController.get_character("bg").get_character_pose(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position) == "sit01" and player.completion_log_compare_date_for_item("sm1cs_bg001"):
                return 1
        return False
    def event_bg004(action_sm):
        if(action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == PHOTO_DOJO):
            if player.completion_log_compare_date_for_item("sm1cs_bg003"):
                return 1
        return False


    def event_dc001(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == PARK and SMCharacter.get_specific_character_in_position("dc") and player.is_storyline_item_finished(MS, "sm1ms002")):
            return 1
        return False
    def event_dc002(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == PARK and gt.curr_timeslot == TIMESLOT_1):
            return 1
        return False
    def event_dc003(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "dc" and curr_location == PARK and gt.curr_timeslot in [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6]):
            return 1
        return False
    def event_dc004_01(action_sm):
        if (player.completion_log_compare_date_for_item("sm1cs_dc003", 2)):
            return 1
        return False
    def event_dc004_02(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "dc" and curr_location == PARK and gt.curr_timeslot in [TIMESLOT_5, TIMESLOT_6]):
            return 1
        return False
    def event_dc007_4(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == PARK and gt.curr_timeslot in [TIMESLOT_8, TIMESLOT_1]):
            return 1
        return False


    def event_mes001(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "mes"):
            return 1
        return False
    def event_mes004_1(action_sm):
        if (action_sm and CharacterController.get_character("mes").points >= 3):
            return 1
        return False
    def event_mes005_1(action_sm):
        if (action_sm and CharacterController.get_character("mes").points >= 5):
            return 1
        return False
    def event_mes005_2(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "mes" and curr_location == GR_BAR):
            return 1
        return False


    def event_i001(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == IT_OFFICE):
            if player.completion_log_compare_date_for_item("sm1fs_i001"):
                return 1
            return 1
        return False
    def event_fs_it004_done(action_sm):
    
        if (player.is_storyline_item_finished(IT_STORY_LINE, "sm1fs_i004")):
            return 1
        return False

    def event_fsit004_2(action_sm):
        if player.get_choice("first_job_to_unlock") == THEATER_STORY_LINE or player.is_storyline_item_finished(MS, "sm1ms011"):
            return 1
        return False

    def event_fsit004_1(action_sm):
        if (action_sm["type"] == ENTER_LOCATION and player.is_storyline_item_finished(NS_STORY, "sm1cs_ns003") and player.is_storyline_item_finished(AG_STORY, "sm1cs_ag001")):
            return 1
        return False
    def event_fsit005(action_sm):
        if (player.is_storyline_item_finished(MS, "sm1ms020") and player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS) >= 40):
            return 1
        return False
    def event_fsit005_2(action_sm):
        if (CharacterController.get_character("ns").points + CharacterController.get_character("cw").points + CharacterController.get_character("ag").points + CharacterController.get_character("am").points) >= 15:
            return 1
        return False


    def event_ns001(action_sm):
        if (action_sm and action_sm["type"] == RELATIONSHIP_POINTS_ADDED and action_sm[TARGET] == "ns" and action_sm[TOTAL] >= 2):
            return 1
        return False
    def event_ns002(action_sm):
        if (action_sm and action_sm["type"] == RELATIONSHIP_POINTS_ADDED and action_sm[TARGET] == "ns" and action_sm[TOTAL] >= 4 and player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS) >= 3):
            return 1
        if (action_sm and action_sm["type"] == IT_JOB_FINISHED and action_sm[TOTAL] >= 3 and CharacterController.get_character("ns").points >= 4):
            return 1
        return False
    def event_ns004_points(action_sm):
        if (CharacterController.get_character("ns").points >= 8):
            return 1
        return False
    def event_ns004(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "ns" and gt.curr_timeslot in [TIMESLOT_4, TIMESLOT_3] and CharacterController.get_character("ns").points >= 8 and curr_position == IT_BEANBAGS):
            return 1
        return False
    def event_ns006(action_sm):
        if (action_sm and action_sm["type"] == IT_JOB_FINISHED and CharacterController.get_character("ns").points >= 10):
            return 1
        return False
    def event_ns007_01(action_sm):
        if (CharacterController.get_character("ns").points >= 12):
            return 1
        return False
    def event_ns007_03(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == IT_OFFICE and gt.curr_timeslot in [TIMESLOT_7, TIMESLOT_8]):
            return 1
        return False
    def event_ns009(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "ns" and gt.curr_timeslot in [TIMESLOT_8] and curr_location == IT_OFFICE):
            return 1
    def event_ns0012_1(action_sm):
        if (CharacterController.get_character("ns").points >= 22):
            return 1
        return False


    def event_ag001(action_sm):
        if (action_sm and player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS) >= 5):
            return 1
        return False
    def event_ag002(action_sm):
        if (action_sm and action_sm["type"] == IT_JOB_FINISHED and player.is_storyline_item_finished(IT_STORY_LINE, "sm1fs_i004") and player.get_data(DATA_IT_TOTAL_JOB_WORKED_DAYS) >= 20):
            return 1
        return False
    def event_ag003(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "ag"):
            return 1
        return False



    def event_cw001_01(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == IT_OFFICE and curr_position == IT_MCDESK and gt.curr_timeslot in [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5]):
            return 1
        return False
    def event_cw002(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "cw" and curr_location == IT_OFFICE and CharacterController.get_character("cw").points >= 5 and CharacterController.get_character("cw").get_character_pose(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position) not in CW_CUSTOM_POSES_LIST and curr_position == IT_CWDESK):
            return 1
        return False
    def event_cw002_2(action_sm):
        if ((gt.curr_timeslot in [TIMESLOT_5] or action_sm and action_sm["type"] == IT_JOB_FINISHED) and player.completion_log_compare_date_for_item("sm1cs_cw002", 1)):
            return 1
        return False
    def event_cw004(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "cw" and curr_location == IT_OFFICE and CharacterController.get_character("cw").points >= 8 and CharacterController.get_character("cw").get_character_pose(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position) not in CW_CUSTOM_POSES_LIST):
            return 1
        return False
    def event_cw004_2(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "cw" and curr_location == IT_OFFICE and gt.curr_day in [FRIDAY] and gt.curr_timeslot in [TIMESLOT_6, TIMESLOT_7]):
            return 1
        return False
    def event_cw004_3(action_sm):
        if (action_sm):
            return 1
        return False


    def event_am001(action_sm):
        if (action_sm and action_sm["type"] == IT_JOB_FINISHED and CharacterController.get_character("am").points >= 2):
            return 1
        return False
    def event_am002(action_sm):
        if (action_sm and action_sm["type"] == IT_JOB_FINISHED and CharacterController.get_character("am").points >= 4):
            return 1
        return False
    def event_am003(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "am" and curr_location == PARK and curr_position == LPA_CENTER and gt.curr_timeslot in [TIMESLOT_5, TIMESLOT_6] and gt.curr_day in [WEDNESDAY, FRIDAY]):
            return 1
        return False
    def event_am004(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "am" and curr_location == IT_OFFICE and curr_position == IT_BEANBAGS and gt.curr_timeslot == TIMESLOT_7 and gt.curr_day in [MONDAY, THURSDAY]):
            return 1
        return False
    def event_am005_1(action_sm):
        if (player.completion_log_compare_date_for_item("sm1cs_am004")):
            return 1
        return False
    def event_am007_2(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "am" and curr_location == IT_OFFICE and curr_position == IT_MCDESK and gt.curr_timeslot in [TIMESLOT_4,TIMESLOT_5,TIMESLOT_6]):
            return 1
        return False


    def event_t003(action_sm):
        if (action_sm and action_sm["type"] == MAP_LOCATION_CLICK and action_sm[TARGET] == LocationController.get_location(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR).get_codename() and gt.curr_timeslot in [TIMESLOT_5, TIMESLOT_6]):
            return 1
        return False
    def event_t004_1(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and player.is_storyline_item_finished(TL_STORY, "sm1cs_tl001") and player.is_storyline_item_finished(DVH_STORY, "sm1cs_dvh001") and player.is_storyline_item_finished(VS_STORY, "sm1cs_vs001") and player.is_storyline_item_finished(KM_STORY, "sm1cs_km001")):
            return 1
        return False
    def event_t004_2(action_sm):
        if (player.completion_log_compare_date_for_item("sm1cs_tl001") and player.completion_log_compare_date_for_item("sm1cs_dvh001") and player.completion_log_compare_date_for_item("sm1cs_vs001") and player.completion_log_compare_date_for_item("sm1cs_km001")):
            return 1
        return False
    def event_t004_3(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "dvh" and curr_location == THEATER and curr_sublocation != LTH_SUB_SHOWER):
            return 1
        return False
    def event_t005_1(action_sm):
        if action_sm and player.is_storyline_item_finished(VS_STORY, "sm1cs_vs002") and int(player.get_data(DATA_TH_SHOWS_SUCCESS)) >= 3:
            points = CharacterController.get_character("km").points + CharacterController.get_character("dvh").points + CharacterController.get_character("tl").points + CharacterController.get_character("vs").points
            if points >= 10:
                return 1
        return False
    def event_t005_2(action_sm):
        if action_sm and action_sm["type"] == ENTER_LOCATION and curr_location == THEATER and curr_sublocation == LTH_SUB_STAGE:
            return 1
        return False


    def event_km002_01(action_sm):
        if (player.is_storyline_item_finished(THEATER_STORY_LINE, "sm1fs_t004")):
            return 1
        return False
    def event_km002_02(action_sm):
        if (player.completion_log_compare_date_for_item("sm1fs_t004")):
            return 1
        return False
    def event_km002_03(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == THEATER and action_sm[SUBLOCATION] == LTH_SUB_STAGE and SMCharacter.get_specific_character_in_location("km", True) and curr_location == THEATER):
            return 1
        return False
    def event_km003_01(action_sm):
        if (action_sm and action_sm["type"] == ITEM_PURCHASED and action_sm[TARGET] == AN_ACTOR_PREPARES):
            return 1
        return False
    def event_km003_02(action_sm):
        if (player.get_topic(TOPIC_LITERATURE) > 4):
            return 1
        return False
    def event_km003_03(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[SUBLOCATION] == LTH_SUB_STAGE and SMCharacter.get_specific_character_in_location("km", True)):
            return 1
        return False
    def event_km005_1(action_sm):
        if player.is_storyline_item_finished(VS_STORY, "sm1cs_vs004"):
            return 1
        return False
    def event_km006(action_sm):
        if player.is_storyline_item_finished(VS_STORY, "sm1cs_vs005"):
            return 1
        return False


    def event_vs001(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[SUBLOCATION] == LTH_SUB_STAGE and SMCharacter.get_specific_character_in_location("vs", True)):
            return 1
        return False
    def event_vs002_01(action_sm):
        if (action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "vs" and curr_location == THEATER and curr_sublocation != LTH_SUB_SHOWER):
            return 1
        return False
    def event_vs002_02(action_sm):
        if (action_sm and action_sm["type"] == ITEM_PURCHASED and action_sm[TARGET] == STARS_WEEKLY):
            return 1
        return False
    def event_vs002_03(action_sm):
        if (player.get_topic(TOPIC_FILM_AND_TV)>2):
            return 1
        return False
    def event_vs002_04(action_sm):
        if (player.is_storyline_item_finished(KM_STORY, "sm1cs_km003")):
            return 1
        return False
    def event_vs002_05(action_sm):
        if (player.completion_log_compare_date_for_item("sm1cs_km003")):
            return 1
        return False
    def event_vs002_06(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[SUBLOCATION] == LTH_SUB_STAGE and SMCharacter.get_specific_character_in_location("vs", True)):
            return 1
        return False
    def event_vs003(action_sm):
        if (action_sm and action_sm["type"] == TH_REHEARSALS_DONE and gt.curr_day == player.get_choice("sm1cs_vs002_alarm_day")):
            return 1
        return False
    def event_vs004_1(action_sm):
        if (player.is_storyline_item_finished(KM_STORY, "sm1cs_km004")):
            return 1
        return False


    def event_tl002(action_sm):
        if(action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "tl" and player.money > 49 and curr_location == THEATER and curr_sublocation == LTH_SUB_STAGE and curr_position == LTH_FRONT_STAGE):
            if player.completion_log_compare_date_for_item("sm1cs_tl001"):
                return 1
        return False

    def event_tl003(action_sm):
        if(action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "tl" and curr_location == THEATER and player.money >= 100):
            if player.completion_log_compare_date_for_item("sm1cs_tl002"):
                return 1
        return False
    def event_tl008_2(action_sm):
        if(action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[POSITION] == SD_TAISIA and curr_location == STUDIO and gt.curr_timeslot == TIMESLOT_7):
            return 1
        return False


    def event_q_sy001(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[POSITION] == SD_BATHROOM and gt.curr_timeslot == TIMESLOT_5 and not player.is_rent_penalty()):
            return 1
        return False
    def event_sy002_1(action_sm):
        if (action_sm and action_sm["type"] == ACTION_AFTER_SLEEP and player.is_storyline_item_finished(MS, "sm1ms014")):
            return 1
        return False
    def event_sy002_2(action_sm):
        if (action_sm and action_sm["type"] == ACTION_AFTER_SLEEP and player.is_storyline_item_finished(MS, "sm1ms020")):
            return 1
        return False


    def event_mh004(action_sm):
        if (action_sm and action_sm["type"] == OBJECT_CLICK and action_sm[TARGET] == "lly_front_door" and gt.curr_timeslot == TIMESLOT_7):
            return 1
        return False

    def event_rd_000(action_sm):
        if(action_sm and action_sm["type"] == CHARACTER_CLICK and action_sm[TARGET] == "rd"):
            return 1
        return False



    def event_ms003_0_unlocks():
        player.discover_map_location(IT_OFFICE)

    def event_q_ms002_4_unlocks():
        player.discover_map_location(PARK)
        player.discover_map_location(SHOP_71STORE)

    def event_q_ms002_3_unlocks():
        ObjectController.get_object(BED).add_override_interaction_option("io-Sleep-with-time-skip")



    def event_mv01Q01(action_sm):
        if (action_sm and action_sm["type"] == ENTER_LOCATION and action_sm[LOCATION] == STUDIO) and gt.curr_timeslot == TIMESLOT_3:
            return 1
        return False

    def event_mv01Q02(action_sm):
        if player.has_played_scene("sm1mv01s02") and player.has_played_scene("sm1mv01s03_1") and player.has_played_scene("sm1mv01s03_2"):
            return 1
        return False

    def event_mv01Q04_2(action_sm):
        if (action_sm and action_sm["type"] == FILL_BUDGET_ENERGY and pirates_movie.is_budget_energy_filled("actress_budget")):
            return 1
        return False

    def event_mv01Q04_1(action_sm):
        if (action_sm and action_sm["type"] == FILL_BUDGET_ENERGY and pirates_movie.is_budget_energy_filled("props_budget") and pirates_movie.is_budget_energy_filled("props_energy")):
            return 1
        return False

    def event_mv01Q07(action_sm):
        if (action_sm and action_sm["type"] == FILL_BUDGET_ENERGY and pirates_movie.is_budget_energy_filled("travel_budget")):
            return 1
        return False

    def event_mv01Q11(action_sm):
        if (action_sm and action_sm["type"] == FILL_BUDGET_ENERGY and pirates_movie.is_budget_energy_filled("editing_energy")):
            return 1
        return False
