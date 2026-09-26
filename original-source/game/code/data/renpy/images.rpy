image black = Solid((0, 0, 0, 255))
image white = Solid((255, 255, 255, 255))
image empty_image = Null()
image sm_watchface = ConditionSwitch(
    "gt.curr_timeslot == TIMESLOT_1", "night_watchface",
    "gt.curr_timeslot == TIMESLOT_2", "late_night_watchface",
    "gt.curr_timeslot == TIMESLOT_3", "early_morning_watchface",
    "gt.curr_timeslot == TIMESLOT_4", "morning_watchface",
    "gt.curr_timeslot == TIMESLOT_5", "noon_watchface",
    "gt.curr_timeslot == TIMESLOT_6", "afternoon_watchface",
    "gt.curr_timeslot == TIMESLOT_7", "evening_watchface",
    "gt.curr_timeslot == TIMESLOT_8", "nightfall_watchface",
    )
image sm_energy_meter = ConditionSwitch(
    "player.get_energy_percent == 100", "images/ui/energy/energy_100.webp",
    "player.get_energy_percent >= 90" , "images/ui/energy/energy_90.webp",
    "player.get_energy_percent >= 80" , "images/ui/energy/energy_80.webp",
    "player.get_energy_percent >= 70" , "images/ui/energy/energy_70.webp",
    "player.get_energy_percent >= 60" , "images/ui/energy/energy_60.webp",
    "player.get_energy_percent >= 50" , "images/ui/energy/energy_50.webp",
    "player.get_energy_percent >= 40" , "images/ui/energy/energy_40.webp",
    "player.get_energy_percent >= 30" , "images/ui/energy/energy_30.webp",
    "player.get_energy_percent >= 20" , "images/ui/energy/energy_20.webp",
    "player.get_energy_percent >= 10" , "images/ui/energy/energy_10.webp",
    "player.get_energy_percent >= 0"  , "images/ui/energy/energy_0.webp",
    )
image city_map = ConditionSwitch(
    "gt.curr_time_of_day == IS_NIGHT", "city_map_night",
    "gt.curr_time_of_day == IS_DAY",   "city_map_day",
    )
image sm_energy_meter_renovation = ConditionSwitch(
    "player.get_energy_percent == 100", "images/ui/renovation/energy/energy_10.webp",
    "player.get_energy_percent >= 90" , "images/ui/renovation/energy/energy_9.webp",
    "player.get_energy_percent >= 80" , "images/ui/renovation/energy/energy_8.webp",
    "player.get_energy_percent >= 70" , "images/ui/renovation/energy/energy_7.webp",
    "player.get_energy_percent >= 60" , "images/ui/renovation/energy/energy_6.webp",
    "player.get_energy_percent >= 50" , "images/ui/renovation/energy/energy_5.webp",
    "player.get_energy_percent >= 40" , "images/ui/renovation/energy/energy_4.webp",
    "player.get_energy_percent >= 30" , "images/ui/renovation/energy/energy_3.webp",
    "player.get_energy_percent >= 20" , "images/ui/renovation/energy/energy_2.webp",
    "player.get_energy_percent >= 10" , "images/ui/renovation/energy/energy_1.webp",
    "player.get_energy_percent >= 0"  , "images/ui/renovation/energy/energy_0.webp",
    )
image sand_clock_anim:
    "sand_clock_1"
    pause 0.05
    "sand_clock_2"
    pause 0.05
    "sand_clock_3"
    pause 0.05
    "sand_clock_4"
    pause 0.05
    "sand_clock_5"
    pause 0.05
    "sand_clock_6"
    pause 0.05
    "sand_clock_7"
    pause 0.05
    "sand_clock_8"
    pause 0.05
    "sand_clock_9"
    pause 0.05
    "sand_clock_10"
    pause 0.05
    "sand_clock_11"
    pause 0.05
    "sand_clock_12"
    pause 0.05
    "sand_clock_13"
    pause 0.05
    "sand_clock_14"
    pause 0.05
    "sand_clock_15"
    pause 0.05
    "sand_clock_16"
    pause 0.05
    "sand_clock_17"
    pause 0.05
    "sand_clock_18"
    pause 0.05
    "sand_clock_19"
    pause 0.05
    "sand_clock_20"
    pause 0.05
    "sand_clock_21"
    pause 0.05
    "sand_clock_22"
    pause 0.05
    "sand_clock_23"
    pause 0.05
    "sand_clock_24"
    pause 0.05
    "sand_clock_25"
    pause 0.05
    "sand_clock_26"
    pause 0.05
    "sand_clock_27"
    pause 0.05
    "sand_clock_28"
    pause 0.05
    "sand_clock_29"
    pause 0.05
    repeat
transform interaction_bg_blur:
    blur 7.0