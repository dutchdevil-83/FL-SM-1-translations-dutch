screen th_faction():
    style_prefix "th_faction"
    tag menu

    default th_progress_percent = player.get_storyline_progress_percent(THEATER_STORY_LINE)
    default th_characters = ["dvh", "tl", "vs", "km"]
    default th_button_pos_list = get_char_btn_pos(len(th_characters))
    add "images/ui/factions/th_faction_bg.webp"
    label _("THEATER")
    frame:
        xoffset 40
        style_prefix "neutral_characters"
        for _sl2_i in enumerate(th_characters):
            $ i, char  = _sl2_i
            fixed:
                xpos th_button_pos_list[i][0]
                ypos th_button_pos_list[i][1]
                imagebutton:
                    focus_mask True
                    hover_sound audio.sfx_menu_button_hover
                    activate_sound audio.sfx_phone_knob1
                    if CharacterController.get_character(char).get_is_unlocked():
                        idle "images/ui/character/char_button_idle.webp"
                        hover "images/ui/character/char_button_hover.webp"
                        action ShowMenu("character_screen", char)
                        tooltip _(CharacterController.get_character(char).full_name)
                    else:
                        idle "images/ui/character/char_locked_idle.webp"
                        action NullAction()
                        tooltip _("Character not unlocked")
                if CharacterController.get_character(char).get_is_unlocked():
                    add AlphaMask(Transform(f"images/utilities/profile_pictures/profiile_picture_{char}.webp", fit="contain", xsize=200, ysize=200), "images/ui/character/char_button_mask.webp") xalign 0.5 yalign 0.5
    if not vn_mode:
        frame:
            style_prefix "th_faction_schedule"
            vbox:
                text _("Theater schedule") xalign 0.5
                grid 7 1:
                    style_prefix "th_faction_schedule_data"
                    for day in ALLDAYS_LIST:
                        frame:
                            vbox:
                                text day[:3] xalign 0.5
                                text _("6 PM") xalign 0.5
                                if day == THController.rehearsal_day_1:
                                    add THController.get_rehearsal_1_icon()
                                elif day == THController.rehearsal_day_2:
                                    add THController.get_rehearsal_2_icon()
                                elif day == THController.rehearsal_day_3:
                                    add THController.get_rehearsal_3_icon()
                                elif day == THController.final_show_day:
                                    add THController.get_final_show_icon()
                                else:
                                    null height 65 width 63
        vbox:
            yalign 0.52
            spacing 30
            style_prefix "it_faction_data"
            text _("Pay after show on ") + THController.final_show_day + ":" xalign 0.98
            text "$" + str(THController.get_current_pay()) style "it_faction_money_text"
        vbox:
            yalign 0.795
            spacing 30
            style_prefix "it_faction_data"
            text _("Extra pay for successful show:") xalign 0.98
            text "$200" style "it_faction_money_text"
    text _("Progress ") + str(th_progress_percent) + "%"
    bar value th_progress_percent range 100 style "th_faction_bar"
    imagebutton auto "back_%s" xalign 0.99 yalign 0.985 action Return() focus_mask True
    use tooltip_screen
style th_faction_label xalign 0.5 yalign 0.03
style th_faction_label_text:
    font "fonts/sm-main.ttf"
    size 100
    color "#ffe5e5"
style th_faction_schedule_frame:
    background None
    top_padding 15
    bottom_padding 15
    xalign 0.995
    ycenter 0.288
style th_faction_schedule_vbox spacing 10
style th_faction_schedule_text size 28 color "#ffe5e5"
style th_faction_vbox:
    spacing -70
    xsize 330
    xalign 0.1
    yalign 0.5
style th_faction_schedule_data_frame background Frame("images/ui/factions/th_faction_grid_block.webp") xsize 68
style th_faction_schedule_data_grid xsize 68 spacing 10
style th_faction_schedule_data_vbox spacing 10 xalign 0.5
style th_faction_schedule_data_text size 22 color "#ffe5e5"
style th_faction_text:
    xalign 0.5
    yalign 0.9
    size 65
    color "#f8828d"
style th_faction_bar:
    right_bar Frame("images/ui/factions/th_faction_bar_frame.webp", 6, 6, 6, 6)
    left_bar Frame("images/ui/factions/it_faction_bar.webp", 6, 6, 6, 6)
    xalign 0.5
    yalign 0.95
    xsize 1600
    ysize 25