label play_wurst_delivery:
    $ wurst_delivery_base_reward = 50
    if only_story_mode is True:
        $ player.log_action("Skipped 'Wurst Delivery' minigame because of 'Story Mode'")
        jump wurst_delivery_only_story
    else:
        $ player.log_action("Started 'Wurst Delivery' minigame")
    $ quick_menu = False
    $ delivery_start_x = 650
    $ delivery_start_y = 715
    $ delivery_num_points = 7
    $ delivery_points = WurstDelivery.generate_random_points(delivery_start_x, delivery_start_y, delivery_num_points)
    $ delivery_current_x = delivery_start_x + 5
    $ delivery_current_y = delivery_start_y - 25
    $ delivery_score = 0
    $ delivery_time = 10
    $ delivery_bar_range = 10
    $ delivery_clicked_button = 0
    $ wurst_delivery_average_time = 13
    $ wurst_delivery_tip = 5
    $ wurst_delivery_tip_time_range = 5
    $ delivery_finished = False
    $ retrurned_to_wd = False
    $ mt = SMGameTime("01 Jan Mon 00 00 00")
    $ stop_all_sound()
    play music music_wurstdelivery_electro1
    call screen wurst_delivery()
label wurst_delivery_done:
    stop music fadeout 1.5
    $ quick_menu = True
    $ renpy.block_rollback()
    call wurst_delivery_increment_data from _call_wurst_delivery_increment_data
    $ LocationController.draw_current_location("nr")
    show expression cc.get_expression_image("nr", "serious1")
    play voice3 boy7_yes_aga2 noloop
    nr "Good job. Here is your money."
    return
label wurst_delivery_only_story:
    scene black
    show city_map
    show screen wait_screen(WURST_WORK)
    pause 5.0
    hide screen wait_screen
    call wurst_delivery_increment_data from _call_wurst_delivery_increment_data_1
    $ player.add_money(wurst_delivery_base_reward, _("Wurst Delivery"), _("You earned ${} for working at Wurst Delivery").format(wurst_delivery_base_reward))
    $ StoryController.consume_time_energy(4, 0, WURST_DELIVERY_ENERGY_COST)
    $ LocationController.draw_current_location("nr")
    show expression cc.get_expression_image("nr", "serious1")
    play voice3 boy7_yes_aga2 noloop
    nr "Good job. Here is your money."
    return
label wurst_delivery_increment_data:
    $ player.increment_data(DATA_WURST_DELIVERY_WORKED_DAYS)
    return