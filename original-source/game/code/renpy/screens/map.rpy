screen city_map():
    style_prefix "city_map"
    tag menu

    add "city_map"
    for location in map_locations_list:
        if location.get_location().get_implemented_status() and location.get_location().get_discovered_status():
            imagebutton auto location.get_location_button_image() xpos location.posx ypos location.posy action Function(location.click, gt.curr_day, gt.curr_timeslot) focus_mask True tooltip location.get_tooltip(gt.curr_day, gt.curr_timeslot, True) style "map_locations"
    if LocationController.check_location_open(curr_location, curr_sublocation, curr_position):
        imagebutton auto "back_%s" action Jump("location_reenter") tooltip _("Go back") focus_mask True style "map_back_button"
    use game_ui
    use tooltip_screen
style map_locations activate_sound audio.sfx_map_destination_click hover_sound audio.sfx_map_destination_hover
style map_back_button:
    xpos 1710
    ypos 1
    activate_sound audio.sfx_phone_closed1
style city_map_button_text:
    idle_color "#000000"
    hover_color gui.accent_color
    outlines [(1, "#FFFFFF", 0, 0)]