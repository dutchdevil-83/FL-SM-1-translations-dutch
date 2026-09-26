screen location_screen():
    default show_game_ui = True
    $ renpy.music.play(get_location_music()[0],    channel = "freeroam_music1", loop = True, fadeout = 0.5, fadein = 1.0 , if_changed = True, relative_volume = get_location_music()[1])
    $ renpy.music.play(get_location_ambience()[0], channel = "freeroam_sound1", loop = True, fadeout = 0.15, fadein = 0.12 , if_changed = True, relative_volume = get_location_ambience()[1])
    $ renpy.music.play(get_location_subambience()[0], channel = "freeroam_sound2", loop = True, fadeout = 0.15, fadein = 0.12 , if_changed = True, relative_volume = get_location_subambience()[1])
    $ location = LocationController.get_current_location_data()
    add location.get_location_image()
    if location.buttons:
        for btn in location.buttons:
            if location.is_nvagation_button_visible(btn):
                imagebutton idle "empty_image" hover location.get_hover_button_image(btn) focus_mask location.get_mask_button_image(btn) action Function(LocationController.enter_location, location.location, location.get_direction_target_sublocation(btn), location.get_direction_target_position(btn))
    for item in LocationController.get_characters_and_objects_for_sandbox():
        if isinstance(item, SMObject):
            add item.get_object_image(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
            if item.get_object_interactable(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                imagebutton idle "empty_image" hover item.get_object_image(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position, HOVER) focus_mask item.get_object_image(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position, MASK) action Function(ObjectController.click, item) activate_sound audio.sfx_ui_char_appear1 hover_sound audio.sfx_ui_char_hover1
        elif isinstance(item, SMCharacter):
            add item.get_character_image(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
            if item.get_character_interactable(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                imagebutton idle "empty_image" hover item.get_character_image(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position, HOVER) focus_mask item.get_character_image(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position, MASK) action Function(CharacterController.click, item) activate_sound audio.sfx_ui_char_appear1 hover_sound audio.sfx_ui_char_hover1
    if show_game_ui:
        use sandbox_navigation(location)
        use game_ui
    if is_dev_environment:
        key "noshift_K_g" action ToggleLocalVariable("show_game_ui")
screen sandbox_navigation(location):
    style_prefix "sandbox_navigation"

    imagebutton auto "map_button_%s" xpos 1710 ypos 1 action Jump("city_map") tooltip _("Open map") style "map_button"
    if location.can_move_forward():
        imagebutton auto location.get_arrow_button_image(FORWARD_MOVE) action Function(LocationController.enter_location, location.location, location.get_direction_target_sublocation(location.forward_move), location.get_direction_target_position(location.forward_move)) focus_mask True keysym ("K_UP") xpos 910 ypos 750
    if location.can_move_left():
        imagebutton auto location.get_arrow_button_image(LEFT_MOVE) action Function(LocationController.enter_location, location.location, location.get_direction_target_sublocation(location.left_move), location.get_direction_target_position(location.left_move)) focus_mask True keysym ("K_LEFT") xpos 835 ypos 825
    if location.can_move_right():
        imagebutton auto location.get_arrow_button_image(RIGHT_MOVE) action Function(LocationController.enter_location, location.location, location.get_direction_target_sublocation(location.right_move), location.get_direction_target_position(location.right_move)) focus_mask True keysym ("K_RIGHT") xpos 985 ypos 825
    if location.can_move_back():
        imagebutton auto location.get_arrow_button_image(BACK_MOVE) action Function(LocationController.enter_location, location.location, location.get_direction_target_sublocation(location.back_move), location.get_direction_target_position(location.back_move)) focus_mask True keysym ("K_DOWN") xpos 910 ypos 900
    if location.show_navigation_list is True and not renpy.get_screen("character_interaction_menu") and not renpy.get_screen("object_interaction_menu") and not renpy.get_screen("location_interaction_menu"):
        if show_navigation_list is False:
            imagebutton auto "images/ui/sandbox/navigation_show_%s.webp" action SetVariable("show_navigation_list", True) focus_mask True tooltip _("Show Navigation") yalign 0.22 xalign 0.005
        else:
            imagebutton auto "images/ui/sandbox/navigation_hide_%s.webp" action SetVariable("show_navigation_list", False) focus_mask True tooltip _("Hide Navigation") yalign 0.242 xalign 0.11
            add "images/ui/sandbox/navigation_frame.webp" xalign 0.0 yalign 0.5
            vbox:
                for nav_location in sm_locations_list:
                    if nav_location.location == curr_location and nav_location.is_in_navigation_list is True and nav_location.get_discovered_status():
                        $ position_name = nav_location.position_name.lstrip("0123456789_").capitalize()
                        textbutton position_name action Function(LocationController.enter_location, nav_location.location, nav_location.sublocation, nav_location.position) selected (nav_location.position == curr_position and nav_location.sublocation == curr_sublocation) tooltip CharacterController.get_characters_for_side_menu(nav_location.location, nav_location.sublocation, nav_location.position)
    use tooltip_screen
style map_button activate_sound audio.sfx_phone_map1 hover_sound audio.sfx_submenu_click
style sandbox_navigation_image_button activate_sound audio.sfx_submenu_click
style sandbox_navigation_vbox:
    xsize 240
    xpos 10
    ypos 290
style sandbox_navigation_vbox spacing 8
style sandbox_navigation_button_text:
    size 22
    hover_color "#92c3e9"
    selected_color "#fe8b9a"
    kerning 1
    outlines [(2.2, "#000000", 0, 0)]