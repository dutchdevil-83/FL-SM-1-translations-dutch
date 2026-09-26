label lst_read_book_on_couch:
    $ base = LocationController.get_location(curr_location, curr_sublocation, curr_position).get_base_state()
    show expression cc.get_expression_image("mc", f"reading{base[-2:]}")
    show screen wait_screen(READ_BOOK)
    pause 5.0
    hide screen wait_screen
    $ gt.add(1, 0, 0)
    $ player.consume_energy(1)
    jump location_reenter
label purchase_item:
    jump interaction_menu
label pee_in_st_toilet:
    play sound sfx_jeans_fly1
    scene sm1cs-sy001-01-01 mc-peeing-toilet_c1 with dissolve
    queue sound sfx_piss_loop1 loop
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_piss_loop2 fadein 0.5
    pause
    stop sound2 fadeout 1.0
    play sound sfx_toilet_flush1
    pause
    stop sound fadeout 1.0
    $ gt.add(0, 15, 0)
    $ player.increment_data(DATA_PEED_IN_ST_TOILET)
    $ player.log_action("Peed in 'Studio Toilet'")
    jump location_reenter
label st_take_a_shower:
    play sound sfx_shower_ambience1 fadein 1.0
    scene sm1-studio mc-showering_c1 with dissolve
    pause
    stop sound fadeout 1.0
    $ gt.add(0, 30, 0)
    $ player.increment_data(DATA_TOOK_SHOWER_IN_ST)
    $ player.log_action("Took shower in 'Studio Toilet'")
    jump location_reenter
label check_stacy_in_shower:
    play sound sfx_shower_ambience1 fadein 1.0
    play voice3 stacy_moan4 noloop
    scene lst_sde_td_char01_sy_shower01_91_shower_closeup with dissolve
    pause
    stop sound fadeout 1.0
    $ player.increment_data(DATA_CHECK_SY_SHOWRING)
    $ player.log_action("Peeked on Stacy showring in 'Studio Toilet'")
    jump location_reenter
label peek_on_stacy_peeing:
    queue sound sfx_piss_loop1 loop volume 0.5
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_piss_loop2 fadein 0.5 volume 0.5
    scene lst_sde_t7_bathpeek_sy-pee01_90-bathroom-peek with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound fadeout 1.0
    $ player.increment_data(DATA_PEEK_ON_SY_PEEING)
    $ player.log_action("Peeked on Stacy peeing in 'Studio Toilet'")
    jump location_reenter
label sleep_transition:
    scene black
    show screen scene_transistion("[gt.curr_day!t]")
    with Fade(0.0, 0.2, 0.2)
    $ renpy.force_autosave(True, False)
    pause
    hide screen scene_transistion
    call get_money_statement from _call_get_money_statement
    $ renpy.invoke_in_thread(GameAnalytics.submit_events)
    $ EventController.action(ACTION_AFTER_SLEEP)
    $ ChatController.get_waiting_chats()
    jump location_reenter
label sleep_transition_with_penalty:
    scene black
    show screen scene_transistion("[gt.curr_day!t]")
    with Fade(0.0, 0.2, 0.2)
    $ renpy.force_autosave(True, False)
    pause
    hide screen scene_transistion
    call get_money_statement from _call_get_money_statement_1
    call sm1cs_sy001i_rent_penalty from _call_sm1cs_sy001i_rent_penalty
    $ EventController.action(ACTION_AFTER_SLEEP)
    $ ChatController.get_waiting_chats()
    jump location_reenter
label after_sleep_in_scene(show_transition=False, show_money_statement=False):
    if vn_mode:
        return
    if show_transition:
        scene black
        show screen scene_transistion("[gt.curr_day!t]")
        with Fade(0.0, 0.2, 0.2)
        pause
        hide screen scene_transistion
    $ renpy.force_autosave(True, False)
    $ player.sleep_common_function()
    $ player.new_week()
    call get_money_statement(show_money_statement) from _call_get_money_statement_2
    $ ChatController.get_waiting_chats()
    return
label get_money_statement(show_money_statement=False):
    if (gt.curr_day == SUNDAY or show_money_statement) and player.get_money_log():
        call screen money_statement with Fade(0.1, 0.1, 0.1)
        $ player.reset_money_log()
    return
label renovation_screen:
    call screen renovation_screen
    jump location_reenter
label studio_laptop:
    scene black
    call screen studio_laptop with dissolve
    jump location_reenter
label sm_website:
    scene black
    call screen sm_website(0.83) with dissolve
    jump location_reenter
label pirate_movie_screen:
    call screen pirates_movie_progress(from_phone=False)
    jump location_reenter
label interaction_menu:
    $ interaction_character_image = interaction_character.get_default_interaction_for_timeslot(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
    scene black
    if interaction_character_image == "empty_image":
        $ LocationController.draw_current_location(bg_blur = False)
    else:
        $ LocationController.draw_current_location(interaction_character.codename)
        show expression interaction_character_image
    call screen character_interaction_menu
    jump location_reenter
label interaction_menu_object:
    $ LocationController.draw_current_location(bg_blur = False)
    call screen object_interaction_menu
    jump location_reenter
label interaction_menu_location(location, sublocation, position_):
    $ LocationController.draw_current_location(bg_blur = False)
    call screen location_interaction_menu(location, sublocation, position_)
    jump location_reenter
label quick_interaction:
    $ interaction_character_image = interaction_character.get_default_interaction_for_timeslot(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
    $ print_verbose("Entered quick interaction with - " + interaction_character.codename)
    scene black
    if interaction_character_image == "empty_image":
        $ LocationController.draw_current_location(bg_blur = False)
    else:
        $ LocationController.draw_current_location(interaction_character.codename)
    $ renpy.call(interaction_character.get_quick_interaction())
    $ interaction_character.after_quick_interaction()
    jump location_reenter
label busy_interaction:
    call random_busy_interactions from _call_random_busy_interactions
    $ interaction_character_image = interaction_character.get_default_interaction_for_timeslot(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
    $ print_verbose("Entered busy interaction with - " + interaction_character.codename)
    scene black
    if interaction_character_image == "empty_image":
        $ LocationController.draw_current_location(bg_blur = False)
    else:
        $ LocationController.draw_current_location(interaction_character.codename)
    play voice3 CharacterController.get_default_busy_sound(interaction_character.codename) noloop
    show expression interaction_character_image
    $ interaction_character.constant(busy_interaction_dialogue)
    jump location_reenter
label random_busy_interactions:
    if interaction_character.get_random_interaction_dialogue("busy_interaction"):
        $ busy_interaction_dialogue = interaction_character.get_random_interaction_dialogue("busy_interaction")
        return
    python:
        busy_interactions_list = [
                "Excuse me.",
                "Maybe we can talk later.",
                "I need to go.",
                "Sorry, someone is calling me.",
                "We can catch up later.",
                "I'm swamped.",
                "Let's chat later. Maybe another time.",
                "I'm busy."
                ]
    $ busy_interaction_dialogue = renpy.random.choice(busy_interactions_list)
    return
label angry_peek_interaction:
    call random_angry_peek_interactions from _call_random_angry_peek_interactions
    $ interaction_character_image = CharacterController.get_expression_image(interaction_character.codename, "angry01")
    $ print_verbose("Entered angry peek interaction with - " + interaction_character.codename)
    scene black
    if interaction_character_image == "empty_image":
        $ LocationController.draw_current_location(bg_blur = False)
    else:
        $ LocationController.draw_current_location(interaction_character.codename)
    play voice3 CharacterController.get_default_busy_sound(interaction_character.codename) noloop
    show expression interaction_character_image
    $ interaction_character.constant(angry_peek_interaction_dialogue)
    jump location_reenter
label random_angry_peek_interactions:
    if interaction_character.get_random_interaction_dialogue("angry_peek"):
        $ angry_peek_interaction_dialogue = interaction_character.get_random_interaction_dialogue("angry_peek")
        return
    python:
        angry_peek_interactions_list = [
                "[mcname], you pervert!",
                "Can't you see I'm wet...",
                "Do you want to join or something?!",
                "Didn't you see enough already?{w} Turn around!",
                "Nothing to see here, move along.",
                "You need a shower too...",
                "Stop staring, you pervert.",
                "Like what you see?!",
                "You horny monkey..."
                ]
    $ angry_peek_interaction_dialogue = renpy.random.choice(angry_peek_interactions_list)
    return
label studio_watch_pee:
    scene black
    $ LocationController.draw_current_location(bg_blur = False)
    call screen character_interaction_menu
    jump location_reenter
label studio_renovation_work_stage_1:
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s1-{gt.curr_display_time_short}-01_c1")
    with dissolve
    play sound sfx_paint_hand_in3 volume 0.7
    pause 0.5
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s1-{gt.curr_display_time_short}-02_c1")
    with dissolve
    play sound sfx_rope_stretch
    pause 0.5
    play sound sfx_hammer_loop1
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s1-{gt.curr_display_time_short}-03_c1")
    with dissolve
    pause 0.5
    play sound sfx_metal_fence1
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s1-{gt.curr_display_time_short}-04_c1")
    with dissolve
    pause 0.5
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s1-{gt.curr_display_time_short}-05_c1")
    with dissolve
    play sound sfx_metal_fence2
    pause 0.5
    play sound sfx_cleaning_floor1
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s1-{gt.curr_display_time_short}-06_c1")
    with dissolve
    pause 0.5
    return
label studio_renovation_work_stage_2:
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s2-{gt.curr_display_time_short}-01_c1")
    with dissolve
    play sound sfx_paint_hand_in1
    pause 0.5
    play sound sfx_screwdriver_drill4 volume 0.7
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s2-{gt.curr_display_time_short}-02_c1")
    with dissolve
    pause 0.5
    play sound sfx_screwdriver_drill5 volume 0.7
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s2-{gt.curr_display_time_short}-03_c1")
    with dissolve
    pause 0.5
    play sound sfx_screwdriver_drill2
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s2-{gt.curr_display_time_short}-04_c1")
    with dissolve
    pause 0.5
    play sound sfx_paint_smearing5
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s2-{gt.curr_display_time_short}-05_c1")
    with dissolve
    pause 0.5
    play sound sfx_cleaning_floor1
    $ renpy.scene()
    $ renpy.show(f"sm1ms renovation-s2-{gt.curr_display_time_short}-06_c1")
    with dissolve
    pause 0.5
    return
label pirate_movie_build_props:
    $ random_number = renpy.random.choice(["01", "02", "03"])
    $ renpy.scene()
    $ renpy.show(f"sm1mv01-{gt.curr_display_time_short}-{random_number}_c1")
    with dissolve
    pause 1.0
    return
label pirate_movie_editing_work:
    $ random_number = renpy.random.choice(["04", "05", "06", "07", "08"])
    $ renpy.scene()
    $ renpy.show(f"sm1mv01-{gt.curr_display_time_short}-{random_number}_c1")
    with dissolve
    pause 1.0
    return