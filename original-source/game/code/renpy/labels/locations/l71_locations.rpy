label l71_sde_01_overview:
    scene black
    $ curr_location = SHOP_71STORE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = L71_OVERVIEW
    $ LocationController.enter()
    call screen location_screen
    jump l71_sde_01_overview
label l71_sde_02_fridges:
    scene black
    $ curr_location = SHOP_71STORE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = L71_FRIDGES
    $ LocationController.enter()
    call screen location_screen
    jump l71_sde_02_fridges
label l71_sde_03_counter:
    scene black
    $ curr_location = SHOP_71STORE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = L71_COUNTER
    $ LocationController.enter()
    call screen location_screen
    jump l71_sde_03_counter
label l71_1_overview:
    jump l71_sde_01_overview
label l71_2_fridges:
    jump l71_sde_02_fridges
label l71_3_counter:
    jump l71_sde_03_counter