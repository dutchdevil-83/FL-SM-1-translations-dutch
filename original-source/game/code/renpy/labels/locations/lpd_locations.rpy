label lpd_sde_01_door:
    scene black
    $ curr_location = PHOTO_DOJO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LPD_DOOR
    $ LocationController.enter()
    call screen location_screen
    jump lpd_sde_01_door
label lpd_sin_01_overview:
    scene black
    $ curr_location = PHOTO_DOJO
    $ curr_sublocation = LPD_SUB_INSIDE
    $ curr_position = LPD_OVERVIEW
    $ LocationController.enter()
    call screen location_screen
    jump lpd_sin_01_overview
label lpd_sin_02_photospace:
    scene black
    $ curr_location = PHOTO_DOJO
    $ curr_sublocation = LPD_SUB_INSIDE
    $ curr_position = LPD_PHOTOSPACE
    $ LocationController.enter()
    call screen location_screen
    jump lpd_sin_02_photospace
label lpd_sin_03_kitchen:
    scene black
    $ curr_location = PHOTO_DOJO
    $ curr_sublocation = LPD_SUB_INSIDE
    $ curr_position = LPD_KITCHEN
    $ LocationController.enter()
    call screen location_screen
    jump lpd_sin_03_kitchen
label lpd_sin_04_upstairs:
    scene black
    $ curr_location = PHOTO_DOJO
    $ curr_sublocation = LPD_SUB_INSIDE
    $ curr_position = LPD_UPSTAIRS
    $ LocationController.enter()
    call screen location_screen
    jump lpd_sin_04_upstairs
label lpd_1_door:
    jump lpd_sde_01_door
label lpd_2_entrance:
    jump lpd_sin_01_overview