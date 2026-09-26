screen money_statement(money_log_index=0, animation_done=False):
    modal True
    zorder 150
    style_prefix "money_statement"

    default money_log = player.get_concentrated_money_log()
    $ current_log = money_log[money_log_index]
    add "images/ui/money_statement/money_background.webp"
    add "images/ui/money_statement/money_grids.webp"
    button:
        focus_mask "images/ui/money_statement/money_grids_button_mask.webp"
        if not animation_done:
            action If(money_log_index < len(money_log) - 1, [Hide(), Show("money_statement", money_log_index = min(money_log_index + 1, len(money_log) - 1))], [Hide(), Show("money_statement", money_log_index = 0, animation_done = True)])
        else:
            action Return()
    text "$[player.money]" style "money_statement_label"
    if not animation_done:
        frame:
            at money_statement_left
            text f"{current_log[REASON]}" xpos 35 style "money_statement_text"
            text f"{'-' if current_log[AMOUNT] < 0 else ''}${abs(current_log[AMOUNT])}" xanchor 1.0 xpos 457 color ("#78CF77FF" if current_log[AMOUNT] > 0 else "#FA7378FF") style "money_statement_text"
        vbox:
            xcenter 1402
            ypos 220
            for _sl2_i in enumerate(money_log[max(0, money_log_index - 8):money_log_index + 1]):
                $ display_index, statement  = _sl2_i
                frame:
                    style "money_statement_right_frame"
                    text f"{statement[REASON]}" xpos 25 size 35 style "money_statement_text"
                    text f"{'-' if statement[AMOUNT] < 0 else ''}${abs(statement[AMOUNT])}" xanchor 1.0 xpos 625 size 35 color ("#78CF77FF" if statement[AMOUNT] > 0 else "#FA7378FF") style "money_statement_text"
                    if display_index == (money_log_index - max(0, money_log_index - 8)):
                        at money_statement_right
        timer 2.0 action If(money_log_index < len(money_log) - 1, [Hide(), Show("money_statement", money_log_index = min(money_log_index + 1, len(money_log) - 1))], [Hide(), Show("money_statement", money_log_index = 0, animation_done = True)])
    else:
        viewport:
            id "money_statement_vp"
            scrollbars None
            mousewheel True
            arrowkeys True
            pagekeys True
            yinitial 1.0
            draggable True
            vbox:
                for statement in money_log:
                    frame:
                        style "money_statement_right_frame"
                        text f"{statement[REASON]}" xpos 25 size 35 style "money_statement_text"
                        text f"{'-' if statement[AMOUNT] < 0 else ''}${abs(statement[AMOUNT])}" xanchor 1.0 xpos 625 size 35 color ("#78CF77FF" if statement[AMOUNT] > 0 else "#FA7378FF") style "money_statement_text"
        imagebutton idle "images/ui/money_statement/money_arrow_up_idle.webp" hover "images/ui/money_statement/money_arrow_up_hover.webp" insensitive Null() focus_mask True action Scroll("money_statement_vp", "vertical decrease", amount=72, delay=0.0) xcenter 1402 yalign 0.155
        imagebutton idle "images/ui/money_statement/money_arrow_down_idle.webp" hover "images/ui/money_statement/money_arrow_down_hover.webp" insensitive Null() focus_mask True action Scroll("money_statement_vp", "vertical increase", amount=72, delay=0.0) xcenter 1402 yalign 0.845
    hbox:
        textbutton _("BACK") action Rollback() style "money_statement_small_button"
        textbutton (_("NEXT") if not animation_done else _("HIDE")):
            style "money_statement_big_button"
            if not animation_done:
                action If(money_log_index < len(money_log) - 1, [Hide(), Show("money_statement", money_log_index = min(money_log_index + 1, len(money_log) - 1))], [Hide(), Show("money_statement", money_log_index = 0, animation_done = True)])
            else:
                action Return()
        textbutton _("SKIP ALL") action [Hide(), Show("money_statement", money_log_index = 0, animation_done = True)] sensitive not animation_done style "money_statement_small_button"
transform money_statement_left:
    alpha 0.0 zoom 0.5
    pause 0.3
    easein 0.3 alpha 1.0 zoom 1.0
    pause 0.9
    easeout 0.3 alpha 0.0 zoom 0.5
transform money_statement_right:
    alpha 0.0 zoom 0.5
    pause 1.8
    easein 0.2 alpha 1.0 zoom 1.0
style money_statement_label:
    xcenter 525
    ypos 165
    size 65
    color "#7ACF77FF"
    font "fonts/barlow-condensed-semi-bold.ttf"
    kerning 3
style money_statement_frame:
    background Frame("images/ui/money_statement/money_money_bg.webp", 10, 10, 10, 10)
    xcenter 525
    yalign 0.5
    xsize 492
    ysize 99
style money_statement_right_frame:
    background Frame("images/ui/money_statement/money_money_bg.webp")
    xalign 0.5
    yalign 0.5
    xsize 665
    ysize 57
style money_statement_text:
    size 40
    yalign 0.5
    color "#ffffffff"
    font "fonts/barlow-condensed-semi-bold.ttf"
style money_statement_viewport:
    xcenter 1402
    ypos 220
    xsize 665
    ysize 633
style money_statement_vbox spacing 15
style money_statement_hbox:
    xcenter 525
    yalign 0.84
    spacing 15
style money_statement_small_button:
    idle_background Frame("images/ui/money_statement/money_small_button_bg_idle.webp", 52, 36, 52, 36)
    hover_background Frame("images/ui/money_statement/money_small_button_bg_hover.webp", 52, 36, 52, 36)
    insensitive_background Frame("images/ui/money_statement/money_small_button_bg_insensitive.webp", 52, 36, 52, 36)
    xminimum 220
    yalign 0.5
    xpadding 20
    ypadding 10
style money_statement_small_button_text:
    font "fonts/viga-regular.ttf"
    color "#e3e3e3"
    size 40
    xalign 0.5
style money_statement_big_button:
    idle_background Frame("images/ui/money_statement/money_big_button_bg_idle.webp", 35, 23, 35, 23)
    hover_background Frame("images/ui/money_statement/money_big_button_bg_hover.webp", 35, 23, 35, 23)
    xminimum 220
    xpadding 50
    ypadding 15
style money_statement_big_button_text:
    font "fonts/viga-regular.ttf"
    color "#e3e3e3"
    size 50
    xalign 0.5