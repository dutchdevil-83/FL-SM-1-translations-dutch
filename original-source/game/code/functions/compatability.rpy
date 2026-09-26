init python:
    def compatibility():
    
        if not hasattr(renpy.store, "curr_position") or getattr(renpy.store, "curr_sublocation") not in sm_sublocations_list:
            setattr(renpy.store, "curr_location", STUDIO)
            setattr(renpy.store, "curr_sublocation", DEFAULT_SUBLOCATION)
            setattr(renpy.store, "curr_position", SD_OVERVIEW)
            print_verbose("Fix curr_position in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if len(player.get_completion_log()) == 0 and len(getattr(renpy.store, player.var + SCENES)) > 0:
            scene_list = getattr(renpy.store, player.var + SCENES)
            for item in scene_list:
                player.completion_log_add_item_date(item)
            print_verbose("Fix completion log in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MS, "sm1ms001_02"):
            if player.get_storyline(DC_STORY) is False:
                StoryController.activate_story_line(DC_STORY)
                print_verbose("Fix Debbie story in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
            if LocationController.get_map_location(PARK).get_location().get_discovered_status() is False or LocationController.get_map_location(SHOP_71STORE).get_location().get_discovered_status() is False:
                event_q_ms002_4_unlocks()
                print_verbose("Unlock Park and 71 Store in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(IT_STORY_LINE, "Q-FSIT001-1") and LocationController.get_map_location(IT_OFFICE).get_location().get_discovered_status() is False:
            event_ms003_0_unlocks()
            print_verbose("Discover IT Office in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(IT_STORY_LINE, "Q-FSIT004") and player.get_storyline(AM_STORY) is False:
            StoryController.activate_story_line(AM_STORY)
            print_verbose("Activate AM Story in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(IT_STORY_LINE, "sm1fs_i003") and LocationController.get_location(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW).get_lock_status() is not False:
            LocationController.unlock_position(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW)
            print_verbose("Unlock IT Office Openview in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MS, "sm1ms005") and player.get_storyline(SY_STORY) is False:
            StoryController.activate_story_line(SY_STORY)
            print_verbose("Activate SY Story in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(KV_STORY, "sm1cs_kv000i") and LocationController.get_map_location(PHOTO_DOJO).get_location().get_discovered_status() is False:
            player.discover_map_location(PHOTO_DOJO)
            print_verbose("Discover Photo Dojo in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(THEATER_STORY_LINE, "sm1fs_t002") and LocationController.get_map_location(THEATER).get_location().get_discovered_status() is False:
            player.discover_map_location(THEATER)
            print_verbose("Discover Theatre in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MH_STORY, "sm1cs_mh003") and LocationController.get_map_location(LYSSAS_HOUSE).get_location().get_discovered_status() is False:
            player.discover_map_location(LYSSAS_HOUSE)
            print_verbose("Discover Lyssa's House in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
    
    
    
    
    
    
    
        if "io-SD_Peek_On_Stacy" not in LocationController.get_location(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM).get_override_interaction_options():
            LocationController.get_location(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM).add_override_interaction_option("io-SD_Peek_On_Stacy")
            print_verbose("Add Peek on Stacy override interaction in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(KV_STORY, "sm1cs_kv001"):
            if LocationController.get_location(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW).get_lock_status() != False:
                LocationController.get_location(PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW).unlock()
                print_verbose("Unlock Photo Dojo in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(KV_STORY, "sm1cs_kv004"):
            if player.get_storyline(BG_STORY) is False:
                StoryController.activate_story_line(BG_STORY)
                print_verbose("Activate BG Story in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MH_STORY, "sm1cs_mh003"):
            if LocationController.get_location(LYSSAS_HOUSE, LLY_SUB_INSIDE, LLY_OVERVIEW).get_discovered_status() is False:
                player.discover_map_location(LYSSAS_HOUSE)
                print_verbose("Discover Lyssa's House in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(THEATER_STORY_LINE, "sm1fs_t003"):
            if "io-TH_Work" not in LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE).get_override_interaction_options():
                LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE).add_override_interaction_option("io-TH_Work")
                print_verbose("Add TH Work override interaction for LTH_FRONT_STAGE in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
            if "io-TH_Work" not in LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE).get_override_interaction_options():
                LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE).add_override_interaction_option("io-TH_Work")
                print_verbose("Add TH Work override interaction for LTH_STAGE_ENTRANCE in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
            if "io-TH_Work" not in LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW).get_override_interaction_options():
                LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW).add_override_interaction_option("io-TH_Work")
                print_verbose("Add TH Work override interaction for LTH_SUB_STAGE in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
            if "io-TH_Rehearsal" not in LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE).get_override_interaction_options():
                LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE).add_override_interaction_option("io-TH_Rehearsal")
                print_verbose("Add TH Rehearsal override interaction for LTH_STAGE_ENTRANCE in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MS, "sm1cs_nr001i"):
            if player.get_storyline(MAS_STORY) is False:
                StoryController.activate_story_line(MAS_STORY)
                print_verbose("Activate MAS Story in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MS, "sm1ms007"):
            if player.get_storyline(ARJ_STORY) is False:
                StoryController.activate_story_line(ARJ_STORY)
                print_verbose("Activate ARJ Story in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(KV_STORY, "sm1cs_kv004"):
            if player.is_storyline_item_finished(KV_STORY, "Q-KV004_2") is False:
                if player.get_choice("sm1cs_kv004_practice_skills"):
                    player.progress_storyline(KV_STORY, 2)
                    player.set_choice("sm1cs_kv004_repeatable_unlocked")
                    CharacterController.get_character("kv").add_override_interaction_option("io-KV004_repeatable")
                    print_verbose("Advance KV Story to compensate off ramp and added kv004 repeatable")
                    setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(SY_STORY, "sm1cs_sy001") and player.get_choice("sm1cs_sy001_watersports"):
            if WATERSPORTS not in CharacterController.get_character("sy").get_traits():
                CharacterController.get_character("sy").discover_trait(WATERSPORTS)
                print_verbose("Discover Stacy Watersports trait in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MS, "sm1ms003") and getattr(renpy.store, "sm1ms003_fuck_throat", False) is True:
            if DEEP_THROAT not in CharacterController.get_character("sy").get_traits():
                CharacterController.get_character("sy").discover_trait(DEEP_THROAT)
                print_verbose("Discover Stacy Deepthroat trait in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MS, "sm1ms006"):
            if SPANKING not in CharacterController.get_character("sy").get_traits():
                CharacterController.get_character("sy").discover_trait(SPANKING)
                print_verbose("Discover Stacy Spanking trait in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MS, "sm1ms004"):
            if not player.get_choice("sm1ms004_got_arj_points"):
                CharacterController.get_character("arj").add_point()
                player.set_choice("sm1ms004_got_arj_points")
                print_verbose("Add AmRose RP for scene \"sm1ms004\"")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MH_STORY, "sm1cs_mh004"):
            if not player.get_choice("sm1cs_mh004_got_point"):
                CharacterController.get_character("mh").add_point()
                player.set_choice("sm1cs_mh004_got_point")
                print_verbose("Add Lyssa RP for scene \"sm1cs_mh004\"")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MH_STORY, "sm1cs_mh005"):
            if not player.get_choice("sm1cs_mh005_get_point_1"):
                if player.get_choice("sm1cs_mh005_kiss"):
                    CharacterController.get_character("mh").add_point()
                    player.set_choice("sm1cs_mh005_get_point_1")
                    print_verbose("Add Lyssa RP for scene \"sm1cs_mh005_choice_1\"")
                    setattr(renpy.store, "compatibility_trigger", True)
            if not player.get_choice("sm1cs_mh005_get_point_2"):
                if player.get_choice("sm1cs_mh005_let_mh_win"):
                    CharacterController.get_character("mh").add_point()
                    player.set_choice("sm1cs_mh005_get_point_2")
                    print_verbose("Add Lyssa RP for scene \"sm1cs_mh005_choice_2\"")
                    setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(MH_STORY, "sm1cs_mh006"):
            if not player.get_choice("sm1cs_mh006_got_point"):
                CharacterController.get_character("mh").add_point(2)
                player.set_choice("sm1cs_mh006_got_point")
                print_verbose("Add Lyssa RP for scene \"sm1cs_mh006\"")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(CW_STORY, "sm1cs_cw003"):
            if not player.is_storyline_item_finished(CW_STORY, "sm1cs_cw004"):
                if CharacterController.get_character("cw").get_points_limit()<10:
                    CharacterController.get_character("cw").update_points_limit(10)
                    CharacterController.get_character("cw").add_point(1)
                    print_verbose("Update CW RPLimit 10")
                    setattr(renpy.store, "compatibility_trigger", True)
            if player.is_storyline_item_finished(NS_STORY, "sm1cs_ns005") and not player.is_storyline_item_finished(NS_STORY, "sm1cs_ns006"):
                if CharacterController.get_character("ns").get_points_limit()==10:
                    CharacterController.get_character("ns").update_points_limit(12)
                    CharacterController.get_character("ns").add_point(1)
                    print_verbose("Update NS RPLimit 12")
                    setattr(renpy.store, "compatibility_trigger", True)
            elif player.is_storyline_item_finished(NS_STORY, "sm1cs_ns006") and not player.is_storyline_item_finished(NS_STORY, "sm1cs_ns011"):
                if CharacterController.get_character("ns").get_points_limit()<20:
                    CharacterController.get_character("ns").update_points_limit(20)
                    CharacterController.get_character("ns").add_point(8)
                    print_verbose("Update NS RPLimit 20")
                    setattr(renpy.store, "compatibility_trigger", True)
    
        if QuestController.get_current_quest(AM_STORY) == "Q-AM005_03" and player.get_choice("sm1cs_am005_failed_am") is False:
            player.progress_storyline(AM_STORY, 2)
            print_verbose("Fix stuck April storyline for release 6")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(NS_STORY, "sm1cs_ns012i"):
            if not hasattr(renpy.store, "nspetlabel") or nspetlabel == "":
                setattr(renpy.store, "nspetlabel", None)
                print_verbose("Fix \"nspetlabel\" petlabel variable")
                setattr(renpy.store, "compatibility_trigger", True)
            if not hasattr(renpy.store, "nsmcpetlabel") or nsmcpetlabel == "":
                setattr(renpy.store, "nsmcpetlabel", None)
                print_verbose("Fix \"nsmcpetlabel\" petlabel variable")
                setattr(renpy.store, "compatibility_trigger", True)
            if nspetlabel == None and nsmcpetlabel == None and not player.has_choosen("sm1cs_ns012_no_pet_label"):
                player.set_choice("sm1cs_ns012_no_pet_label")
                print_verbose("Fix Naris missing petlabel variables")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if LocationController.get_map_location(GR_BAR).get_location().get_discovered_status() is False:
            if player.is_storyline_item_finished(AG_STORY, "sm1cs_ag002") or player.is_storyline_item_finished(AM_STORY, "sm1cs_am004") or player.is_storyline_item_finished(TL_STORY, "sm1cs_tl004") or player.is_storyline_item_finished(MS, "sm1ms020"):
                renpy.call("sm1_unlock_gr_bar")
                print_verbose("Unlock bar in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(TL_STORY, "sm1cs_tl008") and "io-TL-sex-repeatable01" not in CharacterController.get_character("tl").get_override_interaction_options():
            CharacterController.get_character("tl").add_override_interaction_option("io-TL-sex-repeatable01")
            print_verbose("Add Taisia repeatable sex scene")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(NS_STORY, "sm1cs_ns012") and "io-NS-sex-repeatable01" not in CharacterController.get_character("ns").get_override_interaction_options():
            CharacterController.get_character("ns").add_override_interaction_option("io-NS-sex-repeatable01")
            print_verbose("Add Nari repeatable sex scene")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(DC_STORY, "sm1cs_dc006") and not player.get_choice("sm1cs_dc006_date_dc") and not player.get_choice("sm1ms_dc006_selected_offramp"):
            player.set_choice("sm1ms_dc006_offramp")
            player.set_choice("sm1ms_dc006_selected_offramp")
            all_story_lines = player.get_storylines_progress()
            all_story_lines[DC_STORY] = 18
            setattr(renpy.store, player.var + STORYLINES_PROGRESS, all_story_lines)
            print_verbose("Fix Debbie Rejection")
            setattr(renpy.store, "compatibility_trigger", True)
    
        if player.is_storyline_item_finished(THEATER_STORY_LINE, "sm1fs_t003"):
            if not ObjectController.get_object(TH_SIGN_SHOW).get_lock_status():
                ObjectController.get_object(TH_SIGN_SHOW).unlock()
                print_verbose("Unlock \"TH_SIGN_SHOW\" in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
            if not ObjectController.get_object(TH_SIGN_REHEARSAL).get_lock_status():
                ObjectController.get_object(TH_SIGN_REHEARSAL).unlock()
                print_verbose("Unlock \"TH_SIGN_REHEARSAL\" in compatibility")
                setattr(renpy.store, "compatibility_trigger", True)
    
        if renpy.has_label("after_launch_patch"):
            print_verbose("Jumped to \"after_launch_patch\" in compatibility")
            setattr(renpy.store, "compatibility_trigger", True)
            renpy.call("after_launch_patch")
    
        return
