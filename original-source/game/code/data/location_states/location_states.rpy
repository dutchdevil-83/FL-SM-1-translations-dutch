init 1 python:
    DEFAULT_LOCATION_STATES["lst_sde_states"] = {
            BASE04:     {STORYLINE: (MS, "sm1ms020")},
            BASE03:     {STORYLINE: (MS, "sm1ms017")},
            BASE02:     {STORYLINE: (MS, "sm1ms014")},
        }

    DEFAULT_LOCATION_STATES["lst_sns_states"] = {
            POSE01: {POSE: ("ns", ["gaming02", "gaming01"])},
            SLEEP01: {POSE: ("ns", ["sleep02", "sleep01"])}
        }
    DEFAULT_LOCATION_STATES["lst_stl_states"] = {
            SLEEP01: {POSE: ("tl", ["sleep02", "sleep01"])}
        }

    DEFAULT_LOCATION_STATES["lth_sst_states"] = {
            BASE02: {CHARACTERS: ("tl", "vs", "dvh", "km", "sb")},
        }
    DEFAULT_LOCATION_STATES["lth_ssh_states"] = {
            BASE02: {CHARACTERS: ("tl", "vs", "dvh", "km", "ec", "sj")},
        }
