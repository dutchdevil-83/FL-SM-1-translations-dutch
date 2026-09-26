screen neutral_characters():
    style_prefix "neutral_characters"
    tag menu

    default character_list = ["sy", "arj", "mh", "my", "mes", "kv", "bg", "dc", "ms"]
    default button_pos_list = get_char_btn_pos(len(character_list))
    add "images/ui/factions/neutral_chars_bg.webp"
    label _("Neutral Characters")
    frame:
        for _sl2_i in enumerate(character_list):
            $ i, char  = _sl2_i
            fixed:
                xpos button_pos_list[i][0]
                ypos button_pos_list[i][1]
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
    imagebutton auto "back_%s" xalign 0.99 yalign 0.985 action Return() focus_mask True
    use tooltip_screen
style neutral_characters_label xalign 0.5 yalign 0.03
style neutral_characters_label_text:
    font "fonts/sm-main.ttf"
    size 100
    color "#ffe5e5"
style neutral_characters_frame:
    background None
    xsize 1700
    ysize 830
    xalign 0.5
    yalign 0.55
style neutral_characters_fixed fit_first True
style neutral_characters_text:
    xalign 0.5
    yalign 0.9
    size 65
    color "#f8828d"