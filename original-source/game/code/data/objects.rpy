init python:
    sm_objects_list = [
            SMObject(BED, [ALLDAYS], [TIMESLOT_8, TIMESLOT_1, TIMESLOT_2], True),
            SMObject(RENOVATED_BED, [ALLDAYS], [ANYTIME], False),
            SMObject(COUCH, [ALLDAYS], [ANYTIME], True),
            SMObject(STUDIO_LAPTOP, [ALLDAYS], [ANYTIME], False),
            SMObject(DRINKMACHINE, [ALLDAYS], [TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8], True),
        
            SMObject(IT_PC, [ALLDAYS], [ANYTIME], True),
            SMObject(DRINKMACHINE_IT, [ALLDAYS], [ANYTIME], True),
            SMObject("ns_panty", [ALLDAYS], [ANYTIME], True, False),
            SMObject(ST_TOILET, [ALLDAYS], [ANYTIME], True, True),
            SMObject(ST_SHOWER, [ALLDAYS], [ANYTIME], True, True),
        
            SMObject(TH_FASHION_MAG, [ALLDAYS], [ANYTIME], True, False),
            SMObject(SC_TECH_MAG, [ALLDAYS], [ANYTIME], True, False),
            SMObject(IT_ANIMAL_MAG, [ALLDAYS], [ANYTIME], True, False),
            SMObject(TH_SIGN_REHEARSAL, [TUESDAY, WEDNESDAY, FRIDAY], [TIMESLOT_5, TIMESLOT_6, TIMESLOT_7], False, False),
            SMObject(TH_SIGN_SHOW, [SATURDAY], [TIMESLOT_5, TIMESLOT_6, TIMESLOT_7], False, False),
            ]

    indexed_sm_objects_list = {}
    for obj in sm_objects_list:
        indexed_sm_objects_list[obj.codename] = obj

    default_object_interactions = {
            IT_PC: ["io-work-on-PC"],
            STUDIO_LAPTOP: ["io-studio-laptop"],
            }

    for obj_codename, interactions in default_object_interactions.items():
        for interaction in interactions:
            ObjectController.get_object(obj_codename).add_default_interaction_options(interaction)
