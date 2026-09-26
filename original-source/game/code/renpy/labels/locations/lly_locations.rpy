label lly_sde_01_outside:
    scene black
    $ curr_location = LYSSAS_HOUSE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LLY_OUTSIDE
    $ LocationController.enter()
    call screen location_screen
    jump lly_sde_01_outside
label lly_sde_02_door:
    scene black
    $ curr_location = LYSSAS_HOUSE
    $ curr_sublocation = DEFAULT_SUBLOCATION
    $ curr_position = LLY_DOOR
    $ LocationController.enter()
    call screen location_screen
    jump lly_sde_02_door
label lly_sin_03_overview:
    scene black
    $ curr_location = LYSSAS_HOUSE
    $ curr_sublocation = LLY_SUB_INSIDE
    $ curr_position = LLY_OVERVIEW
    $ LocationController.enter()
    call screen location_screen
    jump lly_sin_03_overview