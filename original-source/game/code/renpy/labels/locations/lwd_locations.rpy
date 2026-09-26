label lwd_sde_01_outside:
    scene black
    $ curr_location = WURST_DELIVERY
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = WD_OUTSIDE
    $ LocationController.enter()
    call screen location_screen
    jump lwd_sde_01_outside
label lwd_sde_02_entrance:
    scene black
    $ curr_location = WURST_DELIVERY
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = WD_ENTRANCE
    $ LocationController.enter()
    call screen location_screen
    jump lwd_sde_02_entrance
label lwd_sde_03_counter:
    scene black
    $ curr_location = WURST_DELIVERY
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = WD_COUNTER
    $ LocationController.enter()
    call screen location_screen
    jump lwd_sde_03_counter
label lwd_sde_04_seats:
    scene black
    $ curr_location = WURST_DELIVERY
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = WD_SEATS
    $ LocationController.enter()
    call screen location_screen
    jump lwd_sde_04_seats
label lwd_1_outside:
    jump lwd_sde_01_outside
label lwd_2_entrance:
    jump lwd_sde_02_entrance
label lwd_3_counter:
    jump lwd_sde_03_counter
label lwd_4_seats:
    jump lwd_sde_04_seats