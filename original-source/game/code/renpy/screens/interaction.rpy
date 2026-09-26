screen character_interaction_menu():
    style_prefix "quick_interaction"

    vbox:
        for interaction_option in InteractionCharacterOption.get_visible_interaction_options(interaction_options):
            textbutton interaction_option.get_name():
                xalign 0.5
                yalign 0.5
                if interaction_option.get_action() != DISABLED_ACTION:
                    action Function(interaction_option.click)
        textbutton _("Back") action Jump("location_reenter") xalign 0.5 yalign 0.5 keysym "game_menu"
    use game_ui
screen object_interaction_menu():
    style_prefix "quick_interaction"

    vbox:
        for interaction_option in InteractionObjectOption.get_visible_interaction_options(interaction_options):
            textbutton interaction_option.get_name():
                xalign 0.5
                yalign 0.5
                if interaction_option.get_action() != DISABLED_ACTION:
                    action Function(interaction_option.click)
        textbutton _("Back") action Jump("location_reenter") xalign 0.5 yalign 0.5 keysym "game_menu"
    use game_ui
screen location_interaction_menu(location, sublocation, position_):
    style_prefix "quick_interaction"

    $ renpy.pop_call()
    vbox:
        for interaction_option in InteractionLocationOption.get_visible_interaction_options(interaction_options):
            textbutton interaction_option.get_name():
                xalign 0.5
                yalign 0.5
                if interaction_option.get_action() != DISABLED_ACTION:
                    action Function(interaction_option.click)
        if LocationController.check_location_open(location, sublocation, position_):
            textbutton _("Enter") action Function(LocationController.enter_location, curr_location, sublocation, position_, True)
        textbutton _("Back") action Return() xalign 0.5 yalign 0.5 keysym "game_menu"
    use game_ui
style quick_interaction_vbox:
    xalign 0.98
    yalign 0.25
    spacing 40
style quick_interaction_button:
    ypadding 15
    xpadding 25
    xsize 650
    idle_background Frame("images/ui/buttons/quick_interaction_choice_idle.webp", 25, 15, 25, 15)
    hover_background Frame("images/ui/buttons/quick_interaction_choice_hover.webp", 25, 15, 25, 15)
    insensitive_background Frame("images/ui/buttons/quick_interaction_choice_insensitive.webp", 25, 15, 25, 15)
    activate_sound audio.sfx_submenu_hover
    hover_sound audio.sfx_menu_button_hover
style quick_interaction_button_text:
    idle_color "#FFFFFF"
    hover_color "#FFFFFF"
    insensitive_color "#FFFFFF"
    xalign 0.5
    text_align 0.5