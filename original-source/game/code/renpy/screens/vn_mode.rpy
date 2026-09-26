screen vn_mode_map():
    style_prefix "vn_map"

    default selected_location = None
    default hovered_button = None
    default data_type_dict = False
    $ offramp_quests = VNModeController.get_offramp_quests()
    add "city_map"
    $ renpy.music.play(audio.music_freeroam_light1,    channel = "freeroam_music1", loop = True, fadeout = 0.5, fadein = 1.0 , if_changed = True, relative_volume = 1)
    $ renpy.music.stop("freeroam_sound1", fadeout = 1.0)
    $ renpy.music.stop("freeroam_sound2", fadeout = 1.0)
    if selected_location:
        button action [SetScreenVariable("selected_location", None), ClearFocus()] keysym "game_menu"
    for location in map_locations_list:
        if location.get_location().get_implemented_status() and location.get_location().get_discovered_status():
            $ scenes_in_location = VNModeController.get_storylines_in_location(location.codename)
            vbox:
                xpos location.posx
                ypos location.posy
                imagebutton:
                    focus_mask True
                    xalign 0.5
                    style "map_locations"
                    if scenes_in_location:
                        auto location.get_location_button_image()
                        action [SetScreenVariable("selected_location", location.codename), CaptureFocus(location.codename)]
                    else:
                        idle f"images/ui/map/{location.codename}_map_button_idle.webp"
                        action NullAction()
                        hovered Notify(_("No scenes available in this location right now"))
                        unhovered Hide("notify")
                        at black_n_white
                frame:
                    text location.name
                    if not scenes_in_location:
                        at black_n_white
    if offramp_quests:
        vbox:
            xpos 20
            ypos 20
            imagebutton auto "images/ui/map/rejected_chars_map_button_%s.webp" action [SetScreenVariable("selected_location", "rejected_chars"), CaptureFocus("rejected_chars")] focus_mask True xalign 0.5 style "map_locations"
            frame:
                text _("Rejected Characters")
    if selected_location:
        nearrect:
            focus selected_location
            preferred_side "right"
            frame:
                style_prefix "vn_menu"
                modal True
                vbox:
                    if selected_location == "rejected_chars":
                        for quest_name in offramp_quests:
                            $ character = VNModeController.get_offramp_character(quest_name)
                            button:
                                action [Hide(), Call("vn_mode_offramp_scene", quest_name)]
                                fixed:
                                    style_prefix "vn_menu_btn"
                                    hbox:
                                        fixed:
                                            add "images/ui/vn_mode/vn_mode_char_photo_mask.webp"
                                            if character:
                                                add AlphaMask(Transform(f"images/utilities/profile_pictures/profiile_picture_{character}.webp", fit="contain", xsize=60, ysize=60), "images/ui/vn_mode/vn_mode_char_photo_mask.webp")
                                            else:
                                                add AlphaMask(Transform("images/utilities/profile_pictures/profiile_picture_sm.webp", fit="contain", xsize=60, ysize=60), "images/ui/vn_mode/vn_mode_char_photo_mask.webp")
                                        text VNModeController.get_offramp_option_name(quest_name) yalign 0.5
                    else:
                        for item in VNModeController.get_storylines_in_location(selected_location):
                            $ scene_without_storyline = True if isinstance(item, dict) else False
                            $ character = QuestController.get_char_from_quest(item[STORYLINE]) if scene_without_storyline else QuestController.get_char_from_quest(item)
                            $ is_next_scene_available = VNModeController.is_next_scene_available(item, scene_without_storyline)
                            button:
                                action [Hide(), Call("vn_mode_control", item, scene_without_storyline)]
                                sensitive is_next_scene_available
                                fixed:
                                    style_prefix "vn_menu_btn"
                                    hbox:
                                        fixed:
                                            add "images/ui/vn_mode/vn_mode_char_photo_mask.webp"
                                            if character:
                                                add AlphaMask(Transform(f"images/utilities/profile_pictures/profiile_picture_{character}.webp", fit="contain", xsize=60, ysize=60), "images/ui/vn_mode/vn_mode_char_photo_mask.webp")
                                            else:
                                                add AlphaMask(Transform("images/utilities/profile_pictures/profiile_picture_sm.webp", fit="contain", xsize=60, ysize=60), "images/ui/vn_mode/vn_mode_char_photo_mask.webp")
                                        text VNModeController.get_next_scene_name(item, scene_without_storyline):
                                            yalign 0.5
                                            if not is_next_scene_available:
                                                xmaximum 225
                                    if not is_next_scene_available:
                                        imagebutton:
                                            idle "images/ui/vn_mode/vn_mode_hint_link.webp"
                                            action NullAction()
                                            xanchor 1.0
                                            xpos 352
                                            yalign 0.5
                                            if scene_without_storyline:
                                                hovered [SetScreenVariable("hovered_button", item[NAME]), SetScreenVariable("data_type_dict", True), CaptureFocus(item[NAME])]
                                                unhovered [SetScreenVariable("hovered_button", None), SetScreenVariable("data_type_dict", False), ClearFocus(item[NAME])]
                                            else:
                                                hovered [SetScreenVariable("hovered_button", item), CaptureFocus(item)]
                                                unhovered [SetScreenVariable("hovered_button", None), ClearFocus(item)]
    if hovered_button:
        nearrect:
            focus hovered_button
            preferred_side "right"
            frame:
                style_prefix "vn_hint"
                text VNModeController.get_next_scene_hint(hovered_button, data_type_dict) yalign 0.5
transform black_n_white:
    matrixcolor SaturationMatrix(0)
style vn_map_vbox spacing 2
style vn_map_frame:
    background Frame("gui/notify.png", 5, 5, 5, 5)
    left_padding 10
    top_padding 8
    right_padding 10
    bottom_padding 8
    xalign 0.5
style vn_map_text:
    size 22
    xsize 80
    text_align 0.5
style vn_menu_frame:
    yalign 0.3
    background Frame("images/ui/vn_mode/vn_mode_quests_bg.webp", 38, 54, 38, 54)
    xsize 395
    yminimum 100
    ypadding 14
style vn_menu_vbox:
    xalign 0.5
    yalign 0.5
    spacing 10
style vn_menu_button:
    xsize 362
    ysize 71
    idle_background Frame("images/ui/vn_mode/vn_mode_quest_button_idle.webp", 25, 34, 25, 34)
    hover_background Frame("images/ui/vn_mode/vn_mode_quest_button_hover.webp", 25, 34, 25, 34)
    insensitive_background Frame("images/ui/vn_mode/vn_mode_quest_button_insensitive.webp", 25, 34, 25, 34)
style vn_menu_btn_hbox spacing 10
style vn_menu_btn_fixed fit_first True yalign 0.5
style vn_menu_btn_text:
    xmaximum 250
    size 25
    hover_color "#000"
style vn_hint_frame:
    background Frame("images/ui/vn_mode/vn_mode_quest_hint_bg.webp", 25, 34, 25, 34)
    xpadding 30
    xmaximum 400
    yalign 0.5
    ysize 71
style vn_hint_text is vn_menu_btn_text