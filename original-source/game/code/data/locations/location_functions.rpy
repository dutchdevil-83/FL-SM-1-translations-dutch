init 1 python:
    sm_sublocations_list = []
    sm_locations_list = []
    for data_item in sm_locations_data:
        sm_locations_list.append(SMLocation.init_location(data_item))
        if data_item[SUBLOCATION] not in sm_sublocations_list:
            sm_sublocations_list.append(data_item[SUBLOCATION])

    indexed_locations_list = {}
    for location in sm_locations_list:
        indexed_locations_list[f"{location.location}_{location.sublocation}_{location.position}"] = location
