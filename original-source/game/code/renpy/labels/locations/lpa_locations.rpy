label lpa_sde_01_entrance:
    scene black
    $ curr_location = PARK
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LPA_ENTRANCE
    $ LocationController.enter()
    call screen location_screen
    jump lpa_sde_01_entrance
label lpa_sde_02_fountain:
    scene black
    $ curr_location = PARK
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LPA_FOUNTAIN
    $ LocationController.enter()
    call screen location_screen
    jump lpa_sde_02_fountain
label lpa_sde_03_hotdog:
    scene black
    $ curr_location = PARK
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LPA_HOTDOG
    $ LocationController.enter()
    call screen location_screen
    jump lpa_sde_03_hotdog
label lpa_sde_04_center:
    scene black
    $ curr_location = PARK
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LPA_CENTER
    $ LocationController.enter()
    call screen location_screen
    jump lpa_sde_04_center
label lpa_sde_05_fork:
    scene black
    $ curr_location = PARK
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LPA_FORK
    $ LocationController.enter()
    call screen location_screen
    jump lpa_sde_05_fork
label lpa_sde_06_toilets:
    scene black
    $ curr_location = PARK
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LPA_TOILETS
    $ LocationController.enter()
    call screen location_screen
    jump lpa_sde_06_toilets
label lpa_sde_07_exit:
    scene black
    $ curr_location = PARK
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LPA_EXIT
    $ LocationController.enter()
    call screen location_screen
    jump lpa_sde_07_exit
label lpa_1_entrance:
    jump lpa_sde_01_entrance
label lpa_2_fountain:
    jump lpa_sde_02_fountain
label lpa_3_hotdog:
    jump lpa_sde_03_hotdog
label lpa_4_center:
    jump lpa_sde_04_center
label lpa_5_fork:
    jump lpa_sde_05_fork
label lpa_6_toilets:
    jump lpa_sde_06_toilets
label lpa_7_exit:
    jump lpa_sde_07_exit