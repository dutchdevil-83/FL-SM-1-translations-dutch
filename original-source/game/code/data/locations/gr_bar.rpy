init python:
    sm_locations_data += [
            {
                LOCATION: GR_BAR, SUBLOCATION: LGR_SUB_BAR, POSITION: LGR_ENTRANCE,
                DISCOVERED: False, LOCKED: False, P_NAME: LGR_ENTRANCE,
                FORWARD_MOVE: LGR_MIDDLE, LEFT_MOVE: False, BACK_MOVE: MAP, RIGHT_MOVE: LGR_BILLIARD,
                IS_IN_NAVIGATION_LIST: True, SHOW_NAVIGATION_LIST: True, NAVIGATION_BUTTONS: [LGR_BILLIARD, LGR_MIDDLE, LGR_BAR, LGR_STAGE],
                SCHEDULE:"LSCHEDULE_GR_DEFAULT",
                },
            {
                LOCATION: GR_BAR, SUBLOCATION: LGR_SUB_BAR, POSITION: LGR_BILLIARD,
                DISCOVERED: True, LOCKED: False, P_NAME: LGR_BILLIARD,
                FORWARD_MOVE: False, LEFT_MOVE: False, BACK_MOVE: LGR_ENTRANCE, RIGHT_MOVE: False,
                IS_IN_NAVIGATION_LIST: True, SHOW_NAVIGATION_LIST: True,
                SCHEDULE:"LSCHEDULE_GR_DEFAULT",
                },
            {
                LOCATION: GR_BAR, SUBLOCATION: LGR_SUB_BAR, POSITION: LGR_MIDDLE,
                DISCOVERED: True, LOCKED: False, P_NAME: LGR_MIDDLE,
                FORWARD_MOVE: LGR_STAGE, LEFT_MOVE: False, BACK_MOVE: LGR_ENTRANCE, RIGHT_MOVE: LGR_BAR,
                IS_IN_NAVIGATION_LIST: True, SHOW_NAVIGATION_LIST: True, NAVIGATION_BUTTONS: [LGR_STAGE, LGR_BAR],
                SCHEDULE:"LSCHEDULE_GR_DEFAULT",
                },
            {
                LOCATION: GR_BAR, SUBLOCATION: LGR_SUB_BAR, POSITION: LGR_BAR,
                DISCOVERED: True, LOCKED: False, P_NAME: LGR_BAR,
                FORWARD_MOVE: False, LEFT_MOVE: LGR_STAGE, BACK_MOVE: LGR_MIDDLE, RIGHT_MOVE: LGR_ENTRANCE,
                IS_IN_NAVIGATION_LIST: True, SHOW_NAVIGATION_LIST: True,
                SCHEDULE:"LSCHEDULE_GR_DEFAULT",
                },
            {
                LOCATION: GR_BAR, SUBLOCATION: LGR_SUB_BAR, POSITION: LGR_STAGE,
                DISCOVERED: True, LOCKED: False, P_NAME: LGR_STAGE,
                FORWARD_MOVE: False, LEFT_MOVE: False, BACK_MOVE: LGR_MIDDLE, RIGHT_MOVE: False,
                IS_IN_NAVIGATION_LIST: True, SHOW_NAVIGATION_LIST: True,
                SCHEDULE:"LSCHEDULE_GR_DEFAULT",
                },
        ]
