label lst_sde_01_overview:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_OVERVIEW
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_01_overview
label lst_sde_02_kitchen:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_KITCHEN
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_02_kitchen
label lst_sde_03_mattress:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_MATTRESS
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_03_mattress
label lst_sde_04_corner:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_CORNER
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_04_corner
label lst_sde_05_couch:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_COUCH
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_05_couch
label lst_sde_06_stairs:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_STAIRS
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_06_stairs
label lst_sde_07_bathroom:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_BATHROOM
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_07_bathroom
label lst_sde_08_upstairs_1:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_UPSTAIRS_1
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_08_upstairs_1
label lst_sde_09_upstairs_2:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_UPSTAIRS_2
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_09_upstairs_2
label lst_sde_10_upstairs_3:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_UPSTAIRS_3
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_10_upstairs_3
label lst_sde_11_upstairs_4:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_UPSTAIRS_4
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_11_upstairs_4
label lst_sde_12_upstairs_bed:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = SD_UPSTAIRS_BED
    $ LocationController.enter()
    call screen location_screen
    jump lst_sde_12_upstairs_bed
label lst_sns_01_nari:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = SD_SUB_NARI
    $ curr_position = SD_NARI
    $ LocationController.enter()
    call screen location_screen
    jump lst_sns_01_nari
label lst_stl_01_taisia:
    scene black
    $ curr_location = STUDIO
    $ curr_sublocation = SD_SUB_TAISIA
    $ curr_position = SD_TAISIA
    $ LocationController.enter()
    call screen location_screen
    jump lst_stl_01_taisia
label lst_1_overview:
    jump lst_sde_01_overview
label lst_2_kitchen:
    jump lst_sde_02_kitchen
label lst_3_mattress:
    jump lst_sde_03_mattress
label lst_4_corner:
    jump lst_sde_04_corner
label lst_5_couch:
    jump lst_sde_05_couch
label lst_6_stairs:
    jump lst_sde_06_stairs