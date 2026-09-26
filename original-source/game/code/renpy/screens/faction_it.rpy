screen it_faction():
    style_prefix "it_faction"
    tag menu

    default it_progress_percent = player.get_storyline_progress_percent(IT_STORY_LINE)
    default it_days_worked = 0 if player.get_data(DATA_IT_JOB_WORKED_DAYS) is False else player.get_data(DATA_IT_JOB_WORKED_DAYS)
    default it_characters = ["cw", "ag", "ns", "am"]
    default it_button_pos_list = get_char_btn_pos(len(it_characters))
    add "images/ui/factions/it_faction_bg.webp"
    label _("ORBIX")
    frame:
        xoffset 40
        style_prefix "neutral_characters"
        for _sl2_i in enumerate(it_characters):
            $ i, char  = _sl2_i
            fixed:
                xpos it_button_pos_list[i][0]
                ypos it_button_pos_list[i][1]
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
        vbox:
            yalign 0.25
            spacing 30
            style_prefix "it_faction_data"
            text _("Days worked this week:") xalign 0.98
            text str(it_days_worked) + " " + _("Days") style "it_faction_money_text"
        vbox:
            yalign 0.52
            spacing 30
            style_prefix "it_faction_data"
            text _("Pay per day:") xalign 0.98
            text "$" + str(ITController.get_current_pay_per_day()) style "it_faction_money_text"
        vbox:
            yalign 0.795
            style_prefix "it_faction_data"
            text _("Work tutorial") xalign 0.98
            imagebutton auto "it_faction_tutorial_%s" action Show("nonogram_tutorial") xalign 1.0 focus_mask True tooltip _("Get IT minigame help") hover_sound audio.sfx_menu_button_hover activate_sound audio.sfx_phone_knob1
    text _("Progress ") + str(it_progress_percent) + "%"
    bar value it_progress_percent range 100 style "it_faction_bar"
    imagebutton auto "back_%s" xalign 0.99 yalign 0.985 action Return() focus_mask True
    use tooltip_screen
style it_faction_label xalign 0.5 yalign 0.03
style it_faction_label_text:
    font "fonts/sm-main.ttf"
    size 100
    color "#ffe5e5"
style it_faction_vbox:
    spacing - 70
    xsize 330
    xalign 0.1
    yalign 0.5
style it_faction_data_vbox spacing 5 xalign 0.99
style it_faction_data_text size 42 color "#ffe5e5"
style it_faction_money_text:
    xanchor 1.0
    xalign 0.98
    size 75
    color "#ffa8b7"
style it_faction_text:
    xalign 0.5
    yalign 0.9
    size 65
    color "#f8828d"
style it_faction_bar:
    right_bar Frame("images/ui/factions/it_faction_bar_frame.webp", 6, 6, 6, 6)
    left_bar Frame("images/ui/factions/it_faction_bar.webp", 6, 6, 6, 6)
    xalign 0.5
    yalign 0.95
    xsize 1600
    ysize 25