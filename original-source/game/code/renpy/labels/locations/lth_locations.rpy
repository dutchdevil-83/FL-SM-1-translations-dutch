label lth_sco_01_entrance:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_CORRIDOR
    $ curr_position = LTH_CORRIDOR_ENTR
    $ LocationController.enter()
    call screen location_screen
    jump lth_sco_01_entrance
label lth_sco_02_first_corridor:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_CORRIDOR
    $ curr_position = LTH_FIRST_CORRIDOR
    $ LocationController.enter()
    call screen location_screen
    jump lth_sco_02_first_corridor
label lth_sco_03_second_corridor:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_CORRIDOR
    $ curr_position = LTH_SECOND_CORRIDOR
    $ LocationController.enter()
    call screen location_screen
    jump lth_sco_03_second_corridor
label lth_sco_04_end_corridor:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_CORRIDOR
    $ curr_position = LTH_END_CORRIDOR
    $ LocationController.enter()
    call screen location_screen
    jump lth_sco_04_end_corridor
label lth_sst_05_stage_entrance:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_STAGE
    $ curr_position = LTH_STAGE_ENTRANCE
    $ LocationController.enter()
    call screen location_screen
    jump lth_sst_05_stage_entrance
label lth_sst_06_front_stage:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_STAGE
    $ curr_position = LTH_FRONT_STAGE
    $ LocationController.enter()
    call screen location_screen
    jump lth_sst_06_front_stage
label lth_sst_07_first_row:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_STAGE
    $ curr_position = LTH_FIRST_ROW
    $ LocationController.enter()
    call screen location_screen
    jump lth_sst_07_first_row
label lth_sbs_01_corridor_entrance:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_BACKSTAGE
    $ curr_position = LTH_BACKSTAGE_ENTR
    $ LocationController.enter()
    call screen location_screen
    jump lth_sbs_01_corridor_entrance
label lth_sbs_02_center:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_BACKSTAGE
    $ curr_position = LTH_BACKSTAGE_CENTER
    $ LocationController.enter()
    call screen location_screen
    jump lth_sbs_02_center
label lth_sbs_03_to_stage:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_BACKSTAGE
    $ curr_position = LTH_TO_STAGE
    $ LocationController.enter()
    call screen location_screen
    jump lth_sbs_03_to_stage
label lth_sd1_01_dressingroom_1:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_DRESSING_1
    $ curr_position = LTH_DRESSINGROOM_1
    $ LocationController.enter()
    call screen location_screen
    jump lth_sd1_01_dressingroom_1
label lth_sd2_01_dressingroom_2:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_DRESSING_2
    $ curr_position = LTH_DRESSINGROOM_2
    $ LocationController.enter()
    call screen location_screen
    jump lth_sd2_01_dressingroom_2
label lth_sdo_01_directors_office:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_OFFICE
    $ curr_position = LTH_DIRECTORS_OFFICE
    $ LocationController.enter()
    call screen location_screen
    jump lth_sdo_01_directors_office
label lth_sso_01_entrance_corridor:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_STORAGE
    $ curr_position = LTH_ENTRANCE_CORRIDOR
    $ LocationController.enter()
    call screen location_screen
    jump lth_sso_01_entrance_corridor
label lth_sso_02_shelves_1:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_STORAGE
    $ curr_position = LTH_SHELVES_1
    $ LocationController.enter()
    call screen location_screen
    jump lth_sso_02_shelves_1
label lth_sso_03_shelves_2:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_STORAGE
    $ curr_position = LTH_SHELVES_2
    $ LocationController.enter()
    call screen location_screen
    jump lth_sso_03_shelves_2
label lth_sso_04_shelves_3:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_STORAGE
    $ curr_position = LTH_SHELVES_3
    $ LocationController.enter()
    call screen location_screen
    jump lth_sso_04_shelves_3
label lth_sso_05_entrance_backstage:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_STORAGE
    $ curr_position = LTH_ENTRANCE_BACKSTAGE
    $ LocationController.enter()
    call screen location_screen
    jump lth_sso_05_entrance_backstage
label lth_ssl_01_lockers:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_LOCKERS
    $ curr_position = LTH_LOCKERS
    $ LocationController.enter()
    call screen location_screen
    jump lth_ssl_01_lockers
label lth_ssh_01_showers_entrance:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_SHOWER
    $ curr_position = LTH_SHOWERS_ENTRANCE
    $ LocationController.enter()
    call screen location_screen
    jump lth_ssh_01_showers_entrance
label lth_ssh_02_showers_middle:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_SHOWER
    $ curr_position = LTH_SHOWERS_MIDDLE
    $ LocationController.enter()
    call screen location_screen
    jump lth_ssh_02_showers_middle
label lth_ssh_03_showers_end:
    scene black
    $ curr_location = THEATER
    $ curr_sublocation = LTH_SUB_SHOWER
    $ curr_position = LTH_SHOWERS_END
    $ LocationController.enter()
    call screen location_screen
    jump lth_ssh_03_showers_end