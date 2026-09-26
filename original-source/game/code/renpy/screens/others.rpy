screen spawn_text_screen(spawned_text, x, y, text_size=30, time=1.0, tag=None):
    zorder 500

    fixed:
        xcenter x
        ycenter y
        fit_first True
        at spawn_text_anim
        text spawned_text size text_size outlines [(1, "#000000", 1, 1)]
    timer time action Hide(tag)
transform spawn_text_anim:
    on show:
        yoffset 20 alpha 0.0
        easein 0.25 yoffset 0 alpha 1.0
    on hide:
        easein 0.25 yoffset -20 alpha 0.0
screen save_sync_menu():
    modal True

    add "gui/overlay/confirm.png"
    frame:
        style_prefix "save_sync_menu"
        vbox:
            text _("Sync your saves using Ren'Py Sync server")
            null height 5
            textbutton _("Upload Saves") action UploadSync()
            textbutton _("Download Saves") action DownloadSync()
            textbutton _("Back") action Hide("save_sync_menu")
    key "game_menu" action Hide()
style save_sync_menu_frame:
    top_padding 50
    bottom_padding 40
    left_padding 50
    right_padding 50
    xalign 0.5
    yalign 0.5
style save_sync_menu_vbox xalign 0.5 spacing 20
style save_sync_menu_text is gui_label_text
style save_sync_menu_text size 40 xalign 0.5
style save_sync_menu_button xalign 0.5
default trying_skip_cutscene = False
screen cutscene_skip(jump_label):
    key "mouseup_1" action SetVariable("trying_skip_cutscene", True)
    key "mouseup_3" action SetVariable("trying_skip_cutscene", True)
    key "K_ESCAPE" action SetVariable("trying_skip_cutscene", True)
    key "K_MENU" action SetVariable("trying_skip_cutscene", True)
    key "K_RETURN" action SetVariable("trying_skip_cutscene", True)
    key "K_KP_ENTER" action SetVariable("trying_skip_cutscene", True)
    key "K_PAUSE" action SetVariable("trying_skip_cutscene", True)
    key "K_SPACE" action SetVariable("trying_skip_cutscene", True)
    if trying_skip_cutscene is True:
        hbox:
            style_prefix "skip_cutscene"
            textbutton _("SKIP"):
                action [Hide("cutscene_skip"), Jump(jump_label)]
                if config.developer is True:
                    keysym "K_q"
        timer 3.0 action SetVariable("trying_skip_cutscene", False)
style skip_cutscene_hbox yalign 0.952 xalign 0.971
style skip_cutscene_button:
    idle_background Frame("images/ui/phone_chat/chat_char_button_idle.webp", 38, 38, 38, 38)
    hover_background Frame("images/ui/phone_chat/chat_char_button_hover.webp", 38, 38, 38, 38)
    xpadding 40
    top_padding 20
    bottom_padding 15
style skip_cutscene_button_text size 40 hover_color gui.selected_color
screen tooltip_screen():
    zorder 400

    $ returned_tooltip = GetTooltip()
    if returned_tooltip:
        if isinstance(returned_tooltip, list):
            $ tooltip_hint = False
            $ tooltip_list = returned_tooltip
        elif isinstance(returned_tooltip, tuple):
            $ tooltip_hint = returned_tooltip[0]
            $ tooltip_list = returned_tooltip[1]
        else:
            $ tooltip_hint = returned_tooltip
            $ tooltip_list = None
        nearrect:
            focus "tooltip"
            if tooltip_hint is False:
                preferred_side "right"
                xoffset -10
                yoffset -20
            else:
                prefer_top True
            frame:
                style_prefix "tooltip_outer"
                vbox:
                    if tooltip_list:
                        hbox:
                            spacing 5 - (len(tooltip_list) * 2)
                            for charcter in tooltip_list:
                                fixed:
                                    add "images/ui/map/map_character_bg.webp"
                                    add AlphaMask(Transform(f"images/utilities/profile_pictures/profiile_picture_{charcter.codename}.webp", fit="contain", xsize=52, ysize=52), "images/ui/map/map_character_mask.webp")
                                    add "images/ui/map/map_character_border.webp"
                    if tooltip_hint != False:
                        frame:
                            style_prefix "tooltip"
                            xalign 0.5
                            vbox:
                                text tooltip_hint
style tooltip_outer_frame xalign 0.5 background None
style tooltip_frame:
    background Frame("gui/notify.png", 5, 5, 5, 5)
    left_padding 10
    top_padding 8
    right_padding 10
    bottom_padding 8
style tooltip_vbox spacing 10
style tooltip_outer_hbox xalign 0.5 ypos 5
style tooltip_outer_fixed fit_first True
style tooltip_text:
    xalign 0.5
    size 25
    xsize 400
    text_align 0.5
screen scene_transistion(message):
    vbox:
        style_prefix "scene_transistion"
        text message
style scene_transistion_vbox xalign 0.5 yalign 0.5
style scene_transistion_text:
    font "fonts/sm-decorative.ttf"
    text_align 0.5
    line_spacing 30
    size 120
    xsize 1250
    color "#F9EEEF"
    outlines [(4, "#ac5373", 3, 3)]
screen info_text(message):
    vbox:
        style_prefix "info_text"
        text message
style info_text_vbox xalign 0.5 yalign 0.5
style info_text_text:
    font "fonts/consola.ttf"
    text_align 0.5
    line_spacing 20
    size 80
    xsize 1700
    color "#F9EEEF"
    outlines [(3, "#ac5373", 2, 2)]
screen name_input():
    style_prefix "name_input"

    frame:
        vbox:
            vbox:
                text _("Please enter your name here!")
            vbox:
                input pixel_width (600) value VariableInputValue("mcname")
            vbox:
                textbutton _("{u}DONE{/u}") action Jump("name_done") keysym ("K_RETURN", "K_KP_ENTER") xpos 25
style name_input_frame:
    xpos 400
    ypos 200
    xsize 897
    ysize 480
    background None
style name_input_vbox:
    xalign 0.47
    yalign 0.5
    spacing 150
style name_input_text size 45 color "#000000"
style name_input_input xalign 0.5 size 70
style name_input_button_text:
    xalign 0.5
    size 45
    idle_color "#000000"
    hover_color gui.selected_color
default slot_name = None
screen save_name():
    modal True

    default dummy = str(save_name)
    add "gui/overlay/confirm.png"
    frame:
        style_prefix "save_name"
        vbox:
            frame:
                style_prefix "save_name_label"
                text (_("How do you want to name your save?")) xalign 0.5
            frame:
                xsize 620
                ysize 60
                xalign 0.5
                input style "save_name_input" value ScreenVariableInputValue("dummy", True, False) pixel_width 450 allow ("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890!@#$&-_+?.,\'\":)(%;*/")
            frame:
                style_prefix "save_name_buttons"
                fixed:
                    button:
                        style "save_name_return"
                        action Hide("save_name")
                        keysym ("K_ESCAPE", "mouseup_3")
                        text _("Back")
                    button:
                        style "save_name_save"
                        action [Function(save_namer, dummy), FileAction(slot_name), Hide("save_name")]
                        keysym ("K_RETURN", "K_KP_ENTER")
                        text _("Save")
    key "game_menu" action Hide()
style save_name_frame:
    xsize 1000
    ysize 250
    xalign 0.5
    yalign 0.5
    xpadding 25
    ypadding 25
style save_name_vbox order_reverse False spacing 25
style save_name_label_frame xsize 950 background None
style save_name_input:
    xanchor 0.0
    xalign 0.03
    yalign 0.5
    xfill True
    font gui.interface_text_font
style save_name_buttons_frame:
    xsize 950
    ysize 55
    background None
style save_name_return xalign 0.0
style save_name_save xanchor 1.0 xalign 1.0
style save_name_buttons_text:
    font gui.interface_text_font
    size 35
    idle_color gui.hover_color
    hover_color gui.selected_color
screen stop_sound_with_delay(t):
    timer t action [Function(stop_sound_with_delay), Hide("stop_sound_with_delay")]