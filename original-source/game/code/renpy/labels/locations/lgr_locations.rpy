label lgr_sba_01_entrance:
    scene black
    $ curr_location = GR_BAR
    $ curr_sublocation = LGR_SUB_BAR
    $ curr_position = LGR_ENTRANCE
    $ LocationController.enter()
    call screen location_screen
    jump lgr_sba_01_entrance
label lgr_sba_02_billiard:
    scene black
    $ curr_location = GR_BAR
    $ curr_sublocation = LGR_SUB_BAR
    $ curr_position = LGR_BILLIARD
    $ LocationController.enter()
    call screen location_screen
    jump lgr_sba_02_billiard
label lgr_sba_03_middle:
    scene black
    $ curr_location = GR_BAR
    $ curr_sublocation = LGR_SUB_BAR
    $ curr_position = LGR_MIDDLE
    $ LocationController.enter()
    call screen location_screen
    jump lgr_sba_03_middle
label lgr_sba_04_bar:
    scene black
    $ curr_location = GR_BAR
    $ curr_sublocation = LGR_SUB_BAR
    $ curr_position = LGR_BAR
    $ LocationController.enter()
    call screen location_screen
    jump lgr_sba_04_bar
label lgr_sba_05_stage:
    scene black
    $ curr_location = GR_BAR
    $ curr_sublocation = LGR_SUB_BAR
    $ curr_position = LGR_STAGE
    $ LocationController.enter()
    call screen location_screen
    jump lgr_sba_05_stage