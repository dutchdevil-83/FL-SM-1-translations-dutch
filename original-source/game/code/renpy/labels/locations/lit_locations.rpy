label lit_sen_01_entrance:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = IT_SUB_ENTRANCE
    $ curr_position = IT_ENTRANCE
    $ LocationController.enter()
    call screen location_screen
    jump lit_sen_01_entrance
label lit_sde_02_openview:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_OPENVIEW
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_02_openview
label lit_sde_03_corridor:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_CORRIDOR
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_03_corridor
label lit_sde_04_couch:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_COUCH
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_04_couch
label lit_sde_05_toilet:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_TOILET
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_05_toilet
label lit_sde_06_clairedesk:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_CWDESK
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_06_clairedesk
label lit_sde_07_desks:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_DESKS
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_07_desks
label lit_sde_08_mcdesk:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_MCDESK
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_08_mcdesk
label lit_sde_09_beanbags:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_BEANBAGS
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_09_beanbags
label lit_sde_10_kitchen:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_KITCHEN
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_10_kitchen
label lit_sde_11_meeting:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = IT_MEETING
    $ LocationController.enter()
    call screen location_screen
    jump lit_sde_11_meeting
label lit_sto_12_bathroom:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = IT_SUB_TOILET
    $ curr_position = IT_BATHROOM
    $ LocationController.enter()
    call screen location_screen
    jump lit_sto_12_bathroom
label lit_sto_12_br_stall_1:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = IT_SUB_TOILET
    $ curr_position = IT_BR_STALL_1
    $ LocationController.enter()
    call screen location_screen
    jump lit_sto_12_br_stall_1
label lit_sto_12_br_stall_2:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = IT_SUB_TOILET
    $ curr_position = IT_BR_STALL_2
    $ LocationController.enter()
    call screen location_screen
    jump lit_sto_12_br_stall_2
label lit_sto_12_br_stall_3:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = IT_SUB_TOILET
    $ curr_position = IT_BR_STALL_3
    $ LocationController.enter()
    call screen location_screen
    jump lit_sto_12_br_stall_3
label lit_sto_12_br_stall_4:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = IT_SUB_TOILET
    $ curr_position = IT_BR_STALL_4
    $ LocationController.enter()
    call screen location_screen
    jump lit_sto_12_br_stall_4
label lit_sto_12_br_stall_5:
    scene black
    $ curr_location = IT_OFFICE
    $ curr_sublocation = IT_SUB_TOILET
    $ curr_position = IT_BR_STALL_5
    $ LocationController.enter()
    call screen location_screen
    jump lit_sto_12_br_stall_5
label lit_01_entrance:
    jump lit_sen_01_entrance
label lit_02_openview:
    jump lit_sde_02_openview
label lit_03_corridor:
    jump lit_sde_03_corridor
label lit_04_couch:
    jump lit_sde_04_couch
label lit_05_toilet:
    jump lit_sde_05_toilet
label lit_06_clairedesk:
    jump lit_sde_06_clairedesk
label lit_07_desks:
    jump lit_sde_07_desks
label lit_08_mcdesk:
    jump lit_sde_08_mcdesk
label lit_09_beanbags:
    jump lit_sde_09_beanbags
label lit_10_kitchen:
    jump lit_sde_10_kitchen
label lit_11_meeting:
    jump lit_sde_11_meeting
label lit_12_bathroom:
    jump lit_sto_12_bathroom
label lit_12_br_stall_1:
    jump lit_sto_12_br_stall_1
label lit_12_br_stall_2:
    jump lit_sto_12_br_stall_2
label lit_12_br_stall_3:
    jump lit_sto_12_br_stall_3
label lit_12_br_stall_4:
    jump lit_sto_12_br_stall_4
label lit_12_br_stall_5:
    jump lit_sto_12_br_stall_5