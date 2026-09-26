screen simon_says():
    default get_xoffset = 0
    default ss_input_ready = False
    timer ss_animtion_timer action [Function(SimonSays.animate_ss_icon), SetScreenVariable("get_xoffset", get_xoffset + 141.1)] repeat If(ss_anim_end, true = False, false = True)
    add "images/minigames/simon_says/ss_window_bg.webp"
    if ss_input_ready is False:
        hbox:
            xalign 0.5
            yalign 0.27
            for _sl2_i in enumerate(ss_pattern_list):
                $ idx, icon  = _sl2_i
                if ss_rehearsal_mode is True:
                    add icon.get_idle_image() at change_size(0.85)
                else:
                    add icon.get_adaptive_image(idx) at change_size(0.85)
        if len(ss_pattern_list_for_anim) > 0:
            if ss_rehearsal_mode is True:
                add ss_pattern_list_for_anim[0].get_idle_image() xpos 395 ycenter 0.3 xoffset get_xoffset at animate_ss_icon
            else:
                add ss_pattern_list_for_anim[0].get_adaptive_image(ss_pattern_length - len(ss_pattern_list_for_anim)) xpos 395 ycenter 0.3 xoffset get_xoffset at animate_ss_icon
            add "images/minigames/simon_says/ss_button_wire_frame.webp" xpos 332 ycenter 0.3 xoffset (141.1 * (ss_pattern_length - len(ss_pattern_list_for_anim))) at change_size(0.85)
            $ renpy.play(ss_pattern_list_for_anim[0].get_button_audio(), "sound3")
    else:
        hbox:
            xalign 0.5
            yalign 0.27
            for icon in ss_pattern_list_for_hint:
                add icon.get_insensitive_image() at change_size(0.85)
        if len(ss_input_list) < ss_pattern_length:
            add "images/minigames/simon_says/ss_input_arrow.webp" xoffset (141.1 * len(ss_input_list)) at ss_arrow_anim
    add "images/minigames/simon_says/ss_window.webp"
    hbox:
        style_prefix "ss_ready_button"
        if ss_input_ready is False:
            textbutton _("Ready!") action SetScreenVariable("ss_input_ready", True) style "ss_ready_button"
        else:
            if len(ss_input_list) >= ss_pattern_length:
                textbutton _("Submit") action Show("simon_says_result") activate_sound audio.sfx_submenu_click hover_sound audio.sfx_submenu_hover style "ss_ready_button"
            if len(ss_input_list) > 0:
                textbutton _("Reset") action Function(SimonSays.reset_input) activate_sound audio.sfx_submenu_click hover_sound audio.sfx_submenu_hover style "ss_ready_button"
    use simon_says_buttons(ss_input_ready)
    if ss_rehearsal_mode is True and len(ss_input_list) != ss_pattern_length and ss_input_ready is True and ss_input_hint is True:
        imagebutton auto SimonSays.get_nxt_btn_img() action Function(SimonSays.nxt_btn_action) xoffset SimonSays.get_hint_btn_pos()[0] yoffset SimonSays.get_hint_btn_pos()[1] focus_mask True hover_sound audio.sfx_menu_button_hover at ss_pulse
    hbox:
        xpos 325
        yalign 0.27
        for icon in ss_input_list:
            add icon.get_idle_image() at change_size(0.85)
    if ss_rehearsal_mode is True:
        text "Rehearsal" color "#FFF" size 80 xalign 0.5 yalign 0.02 outlines [(3, "#000000", 0, 0)]
    else:
        text "Final Show" color "#FFF" size 80 xalign 0.5 yalign 0.02 outlines [(3, "#000000", 0, 0)]
screen simon_says_buttons(input_ready=False):
    grid 4 3:
        xpos 630
        ypos 550
        for btn in ss_buttons_list:
            imagebutton auto btn.get_button_image() action Function(btn.button_action) focus_mask True sensitive input_ready hover_sound audio.sfx_menu_button_hover
screen simon_says_result():
    modal True

    add "black" at opacity(0.6)
    frame:
        style_prefix "simonsays_result"
        if not SimonSays.check_input():
            if ss_rehearsal_mode is True:
                text _("You finished the rehearsal!")
            else:
                text _("You finished the show successfully!")
        else:
            text _("You made " + str(SimonSays.check_input()) + " mistakes in the show")
        textbutton _("Continue") action [Hide("simon_says"), Hide("simon_says_result"), Jump("simon_says_end")] activate_sound audio.sfx_submenu_click hover_sound audio.sfx_submenu_hover
style simonsays_result_text:
    xalign 0.5
    yalign 0.3
    text_align 0.5
style ss_ready_button_hbox xalign 0.5 yalign 0.41
style ss_ready_button:
    idle_background Frame("images/minigames/simon_says/ss_button_frame_idle.webp", 31, 31, 31, 31)
    hover_background Frame("images/minigames/simon_says/ss_button_frame_hover.webp", 31, 31, 31, 31)
    padding (31, 31, 31, 31)
    activate_sound audio.sfx_submenu_click
    hover_sound audio.sfx_submenu_hover
style ss_ready_button_text hover_color "#FFFFFF"
style simonsays_result_button xalign 0.5 yalign 0.8
style simonsays_result_button_text idle_color "#FFFFFF" hover_color gui.accent_color
style simonsays_result_frame:
    background Frame("images/minigames/simon_says/ss_info_frame.webp", 68, 68, 68, 68)
    xsize 600
    ysize 300
    xalign 0.5
    yalign 0.5
transform opacity(opc):
    alpha opc
transform change_size(zoom):
    zoom zoom
transform animate_ss_icon():
    subpixel True
    zoom 0.85 xanchor 0.5
    block:
        easein 0.75 zoom 1.0
        easein 0.75 zoom 0.85
        repeat
transform ss_arrow_anim():
    subpixel True
    zoom 0.85 xcenter 395 ycenter 0.41
    block:
        easein 0.75 yoffset -5
        easein 0.75 yoffset 5
        repeat
transform ss_pulse():
    subpixel True
    xcenter 630 ycenter 550 zoom 1.0
    block:
        easein 0.4 zoom 1.1
        easein 0.4 zoom 1.0
        repeat