screen renovation_screen(from_phone=False):
    modal True
    zorder 350
    style_prefix "renovation"
    tag phone

    default left_chars = renovation_controller.left_chars
    default right_chars = renovation_controller.right_chars
    $ mc_work_percent = renovation_controller.get_work_power("mc")
    $ sy_work_percent = renovation_controller.get_work_power("sy")
    $ renovation_progress = min(100, round(renovation_controller.get_progress(), 1))
    $ renovation_label = Text(_("RENOVATION PROGRESS") + f"-{renovation_progress:.1f}%", font="fonts/consola.ttf", size=90, xalign=0.5)
    add "images/ui/renovation/renovation_bg.webp"
    add AlphaMask("images/ui/renovation/renovation_label_gradient.webp", renovation_label) xalign 0.5 yalign 0.012
    bar value AnimatedValue(value=renovation_progress, range=100, delay=1.0) range 100 style "renovation_bar"
    add "images/ui/renovation/progress_bar_shadow.webp" xalign 0.5 yalign 0.19
    for _sl2_i in RenovationController.get_ms_scenes_and_pos():
        $ scene_name, posx  = _sl2_i
        fixed:
            xpos posx
            yalign 0.115
            add RenovationController.get_ms_scene_image(scene_name)
            if player.has_played_scene(scene_name):
                add "images/ui/renovation/renovation_complete.webp" xalign 0.5 yalign 0.5
    add "images/ui/renovation/renovation_scenes.webp" xalign 0.5 yalign 0.06
    add "images/ui/renovation/renovation_braket.webp" xalign 0.5 yalign 0.3
    for _sl2_i in [("left", left_chars, 85, 0.0), ("right", right_chars, 1835, 1.0)]:
        $ side, chars, xpos, xanchor  = _sl2_i
        vbox:
            xpos xpos
            xanchor xanchor
            for char in chars:
                fixed:
                    imagebutton idle f"images/ui/renovation/character_cell_{side}.webp" action NullAction() focus_mask True tooltip _(renovation_controller.get_char_tooltip(char, side))
                    add RenovationController.get_char_scene_image(char) xalign xanchor
                    textbutton CharacterController.get_character(char[NAME]).name action ShowMenu("character_screen", char[NAME]) tooltip _(renovation_controller.get_char_tooltip(char, side)) xanchor xanchor xpos (170 if side == "left" else 278) style "renovation_char_name"
                    if player.has_played_scene(char[SCENE]):
                        add "images/ui/renovation/renovation_complete.webp" xalign (0.1 if side == "left" else 0.9) yalign 0.5
                    elif (renovation_progress >= 50 and side == "left") or (renovation_progress >= 100 and side == "right"):
                        add "images/ui/renovation/renovation_failed.webp" xalign (0.1 if side == "left" else 0.9) yalign 0.5
    add "images/ui/renovation/gradient_under_upgrade.webp" xalign 0.5 yalign 0.445
    add "images/ui/renovation/gradient_under_upgrade.webp" xalign 0.45 yalign 0.69
    text _("{}%\nper energy").format(mc_work_percent) xalign 0.53 yalign 0.45 style "renovation_workforce"
    text _("{}%\nper day").format(sy_work_percent) xalign 0.45 yalign 0.67 style "renovation_workforce"
    fixed:
        xalign 0.35
        yalign 0.45
        add "images/ui/renovation/renovation_char_bg.webp" yalign 0.5
        add AlphaMask(Transform(f"images/utilities/profile_pictures/profiile_picture_mc.webp", fit="contain", xsize=260, ysize=260), "images/ui/renovation/renovation_char_mask.webp")
        add "images/ui/renovation/renovation_char_border.webp" yalign 0.5
    fixed:
        xalign 0.275
        yalign 0.7
        add "images/ui/renovation/renovation_char_bg.webp" yalign 0.5
        add AlphaMask(Transform(f"images/utilities/profile_pictures/profiile_picture_sy.webp", fit="contain", xsize=260, ysize=260), "images/ui/renovation/renovation_char_mask.webp")
        add "images/ui/renovation/renovation_char_border.webp" yalign 0.5
    for character in ["mc", "sy"]:
        textbutton renovation_controller.upgrade_button_name(character):
            tooltip renovation_controller.upgrade_button_tooltip(character)
            focus_mask True
            style "renovation_upgrade_button"
            if renovation_controller.work_upgradeable(character):
                action Function(renovation_controller.upgrade_work, character)
            else:
                action NullAction()
                background Frame("images/ui/renovation/button_upgrade_insensitive.webp", 50, 50, 50, 50)
            if character == "mc":
                align (0.68, 0.44)
            else:
                align (0.6, 0.7)
    imagebutton idle "images/ui/renovation/energy_money_frame.webp" focus_mask True action NullAction() tooltip _("Energy: {}/{}").format(player.energy, player.max_energy) xalign 0.03 yalign 0.95
    add "sm_energy_meter_renovation" xalign 0.03 yalign 0.95
    text "$[player.money]" style "renovation_money"
    if renovation_progress < 100:
        textbutton _("WORK"):
            tooltip renovation_controller.renovation_button_tooltip()
            style "renovation_work_button"
            if renovation_controller.is_renovation_work_restricted():
                idle_background Frame("images/ui/renovation/work_button_frame_ins_idle.webp", 50, 50, 50, 50)
                hover_background Frame("images/ui/renovation/work_button_frame_ins_hover.webp", 50, 50, 50, 50)
                action NullAction()
            else:
                action Function(renovation_controller.renovation_work)
    else:
        text _("DONE") xalign 0.5 yalign 0.95 style "renovation_done_text"
    textbutton _("BACK"):
        keysym "game_menu"
        style "renovation_back_button"
        if from_phone:
            action Hide()
        else:
            action Return()
    use tooltip_screen
    if is_dev_environment is True:
        textbutton "+ 5% Progress" action Function(renovation_controller.set_progress, 5) text_size 20 xalign 0.5 yalign 1.0
style renovation_label xalign 0.5 yalign 0.012
style renovation_label_text:
    font "fonts/consola.ttf"
    size 90
    color "#D378B0"
    outlines [(4, "#000000", 0, 0)]
style renovation_bar:
    right_bar "images/ui/renovation/progress_bar_bg.webp"
    left_bar "images/ui/renovation/progress_bar_top.webp"
    xalign 0.5
    yalign 0.19
    xsize 1734
    ysize 144
style renovation_vbox ypos 400 spacing 25
style renovation_fixed fit_first True
style renovation_char_name yalign 0.5
style renovation_char_name_text size 50
style renovation_fixed fit_first True
style renovation_workforce:
    size 45
    color "#FFFFFF"
    text_align 0.5
    line_spacing 5
style renovation_upgrade_button:
    idle_background Frame("images/ui/renovation/button_upgrade_idle.webp", 50, 50, 50, 50)
    hover_background Frame("images/ui/renovation/button_upgrade_hover.webp", 50, 50, 50, 50)
    xpadding 25
    xminimum 216
    ysize 239
style renovation_upgrade_button_text:
    size 45
    color "#FFFFFF"
    xmaximum 200
    text_align 0.5
    line_spacing 5
style renovation_money:
    xanchor 1.0
    xpos 320
    ycenter 975
    size 40
style renovation_work_button:
    xalign 0.5
    yalign 0.97
    idle_background Frame("images/ui/renovation/work_button_frame_idle.webp", 50, 20, 50, 20)
    hover_background Frame("images/ui/renovation/work_button_frame_hover.webp", 50, 20, 50, 20)
    xpadding 85
    ypadding 20
style renovation_work_button_text:
    font "fonts/viga-regular.ttf"
    color "#FFFFFF"
    size 92
style renovation_back_button:
    xalign 0.97
    yalign 0.95
    idle_background Frame("images/ui/renovation/back_button_frame_idle.webp", 50, 20, 50, 20)
    hover_background Frame("images/ui/renovation/back_button_frame_hover.webp", 50, 20, 50, 20)
    xpadding 60
    ypadding 10
style renovation_back_button_text:
    font "fonts/viga-regular.ttf"
    color "#f1e9eb"
    size 65
style renovation_done_text:
    font "fonts/viga-regular.ttf"
    color "#f1e9eb"
    size 92