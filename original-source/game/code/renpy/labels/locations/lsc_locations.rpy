label lsc_sde_01_entrance:
    scene black
    $ curr_location = STARDUCKS
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LSC_ENTRANCE
    $ LocationController.enter()
    call screen location_screen
    jump lsc_sde_01_entrance
label lsc_sde_02_counter:
    scene black
    $ curr_location = STARDUCKS
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LSC_COUNTER
    $ LocationController.enter()
    call screen location_screen
    jump lsc_sde_02_counter
label lsc_sde_03_center:
    scene black
    $ curr_location = STARDUCKS
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LSC_CENTER
    $ LocationController.enter()
    call screen location_screen
    jump lsc_sde_03_center
label lsc_sde_04_corridor:
    scene black
    $ curr_location = STARDUCKS
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LSC_CORRIDOR
    $ LocationController.enter()
    call screen location_screen
    jump lsc_sde_04_corridor
label lsc_sde_05_toilet:
    scene black
    $ curr_location = STARDUCKS
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LSC_TOILET
    $ LocationController.enter()
    call screen location_screen
    jump lsc_sde_05_toilet