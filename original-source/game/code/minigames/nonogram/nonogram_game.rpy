screen nonogram_game():
    add nonogram_background
    frame:
        style_prefix "nonogram_base"
        vbox:
            frame:
                style_prefix "nonogram_top"
                grid grid_cols nono_hints_max:
                    allow_underfull True
                    spacing grid_padding
                    transpose True
                    for h in nono_row_hints:
                        frame:
                            style_prefix "nonogram_hints"
                            xsize 73
                            ysize 50
                            text "[h]" xalign 0.5 yalign 0.5
            hbox:
                frame:
                    style_prefix "nonogram_left"
                    grid nono_hints_max grid_rows:
                        allow_underfull True
                        spacing grid_padding
                        for h in nono_col_hints:
                            frame:
                                style_prefix "nonogram_hints"
                                xsize 50
                                ysize 73
                                text "[h]" xalign 0.5 yalign 0.5
                frame:
                    style_prefix "nonogram_blocks"
                    grid grid_cols grid_rows:
                        spacing grid_padding
                        transpose True
                        for b in nono_buttons_list:
                            imagebutton idle b.get_button_image() action Function(b.button_function) alternate Function(b.button_alt_function) focus_mask True
    use nonogram_ui
screen nonogram_ui():
    if nonogram_submit is False:
        timer 1 action If(nonogram_timer_pause, true = NullAction(), false = Function(mt.add, 0, 0, 1)) repeat True
    frame:
        style_prefix "nonogram_controls"
        frame:
            style_prefix "nonogram_timer"
            text "[mt.minigame_timer]"
        hbox:
            imagebutton auto "images/minigames/nonogram/nonogram_help_%s.webp" action [SetVariable("nonogram_timer_pause", True), Show("nonogram_tutorial")] tooltip _("Show Minigame help") focus_mask True
            imagebutton auto "images/minigames/nonogram/nonogram_reset_%s.webp" action Function(Nonogram.clear_puzzle, nono_buttons_list) tooltip _("Reset the puzzle") focus_mask True
            imagebutton auto "images/minigames/nonogram/nonogram_submit_%s.webp" action [SetVariable("nonogram_submit", True), Show("nonogram_result")] tooltip _("Submit the solution") focus_mask True
    use tooltip_screen
screen nonogram_result():
    modal True

    add "black" at opacity(0.6)
    frame:
        style_prefix "nonogram_result"
        if Nonogram.check_puzzle(nono_buttons_list, grid_rows, grid_cols):
            text _("You have coded the solution in [mt.minigame_timer]")
        else:
            text _("You have failed to code the solution")
        textbutton _("Continue") action [Hide("nonogram_result"), Jump("nonogram_done")]
style nonogram_controls_image_button activate_sound audio.sfx_submenu_hover hover_sound audio.sfx_submenu_click
style nonogram_result_text:
    xalign 0.5
    yalign 0.3
    text_align 0.5
style nonogram_result_button xalign 0.5 yalign 0.8
style nonogram_result_button_text idle_color "#FFFFFF" hover_color gui.accent_color
style nonogram_result_frame:
    background Frame("images/minigames/nonogram/nonogram_controls_window.webp", 20, 16, 20, 18)
    xsize 600
    ysize 300
    xalign 0.5
    yalign 0.5
style nonogram_base_frame:
    xalign 0.33
    yalign 0.45
    left_padding 0
    top_padding 0
    right_padding 0
    bottom_padding 0
    background Frame("images/minigames/nonogram/nonogram_base_frame.webp", 8, 8, 8, 8)
style nonogram_top_frame:
    xalign 1.0
    left_padding 18
    top_padding 27
    right_padding 28
    bottom_padding 16
    background Frame("images/minigames/nonogram/nonogram_top_frame.webp", 16, 26, 26, 15)
style nonogram_left_frame:
    yalign 1.0
    left_padding 27
    top_padding 16
    right_padding 16
    bottom_padding 26
    background Frame("images/minigames/nonogram/nonogram_left_frame.webp", 26, 15, 15, 25)
style nonogram_hints_frame background Frame("images/minigames/nonogram/nonogram_hint_block.webp")
style nonogram_blocks_frame:
    left_padding 19
    top_padding 17
    right_padding 27
    bottom_padding 27
    background Frame("images/minigames/nonogram/nonogram_blocks_frame.webp", 17, 15, 25, 25)
style nonogram_controls_frame:
    background Frame("images/minigames/nonogram/nonogram_controls_window.webp", 20, 16, 20, 18)
    xsize 300
    ysize 265
    xalign 0.7
    yalign 0.5
style nonogram_timer_frame:
    background Frame("images/minigames/nonogram/nonogram_timer_frame.webp", 10, 10, 10, 10)
    left_padding 25
    top_padding 25
    right_padding 25
    bottom_padding 25
    xalign 0.5
    yalign 0.2
style nonogram_timer_text:
    font "fonts/e1234.ttf"
    color "#527f42"
    size 40
style nonogram_controls_hbox xalign 0.5 yalign 0.86