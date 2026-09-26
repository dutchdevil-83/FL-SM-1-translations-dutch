screen quests_screen(storyline=False):
    style_prefix "quests_screen"
    tag menu

    default available_storyline = QuestController.get_quests_for_menu()
    default selected_storyline = (list(available_storyline.keys())[0] if available_storyline else False) if not storyline else storyline
    add "images/ui/quests/quests_screen_bg.webp"
    label _("STORYLINES") xcenter 250
    label _("QUESTS") xcenter 1200
    viewport:
        style_prefix "quests_name"
        scrollbars "vertical"
        yinitial 0.0
        mousewheel True
        draggable True
        vbox:
            for _sl2_i in available_storyline.items():
                $ storyline, progress  = _sl2_i
                hbox:
                    textbutton sm_quest_lines_list[storyline][NAME]:
                        action SetScreenVariable("selected_storyline", storyline)
                        if storyline in player.get_tracked_storylines():
                            idle_background "images/ui/quests/quest_tracked_idle.webp"
                            hover_background "images/ui/quests/quest_tracked_hover.webp"
                            selected_background "images/ui/quests/quest_tracked_hover.webp"
                        else:
                            idle_background "images/ui/quests/quest_untracked_idle.webp"
                            hover_background "images/ui/quests/quest_untracked_hover.webp"
                            selected_background "images/ui/quests/quest_untracked_hover.webp"
                        if QuestController.is_quest_line_end(storyline):
                            text_idle_color "#818181"
                            text_selected_idle_color gui.selected_color
    viewport:
        style_prefix "quests_old_hint"
        scrollbars "vertical"
        yinitial 0.0
        mousewheel True
        draggable True
        vbox:
            for _sl2_i in available_storyline.items():
                $ storyline, progress  = _sl2_i
                if selected_storyline == storyline:
                    hbox:
                        style_prefix "quests_curr_hint"
                        add "images/ui/quests/bullet_point_icon.webp"
                        text QuestController.get_current_quest_hint(storyline, progress) yalign 0.5
                    null height 5
                    for hint in QuestController.get_quest_old_hints(storyline, progress):
                        hbox:
                            add "images/ui/quests/bullet_point_old_icon.webp"
                            text hint yalign 0.5
    hbox:
        if selected_storyline is not False:
            if selected_storyline in player.get_tracked_storylines():
                textbutton _("Untrack Quest") action Function(player.untrack_storyline, selected_storyline)
            else:
                textbutton _("Track Quest") action Function(player.track_storyline, selected_storyline)
            if QuestController.get_char_from_quest(selected_storyline):
                $ character = QuestController.get_char_from_quest(selected_storyline)
                if character != "pmv":
                    fixed:
                        imagebutton:
                            auto f"images/ui/quests/quest_button_frame_%s.webp"
                            focus_mask True
                            if character in FACTION_STORYLINE_CODES:
                                action ShowMenu(f"{character}_faction")
                                tooltip _("Go to faction page")
                            else:
                                action ShowMenu("character_screen", character)
                                tooltip _("Go to character page")
                        add Transform(f"images/utilities/profile_pictures/profiile_picture_{character}.webp", fit="contain", xsize=72, ysize=72) xalign 0.5 yalign 0.5
        imagebutton auto "back_%s" action Return() focus_mask True
    use tooltip_screen
screen new_quest_animation():
    zorder 300

    add "images/ui/quests/quest_icon_big.webp" at new_quest
    timer 4.0 action Hide("new_quest_animation")
transform watch_hand(rotation):
    rotate rotation
transform new_quest:
    xpos -100 ypos -100
    xanchor 0.5 yanchor 0.5
    on show:
        parallel:
            xalign 0.83 yalign 0.12 zoom 1.2 alpha 1.5
            pause 0.2
            easeout 1.3 xalign 0.9 yalign 0.15 zoom 0.5
            linear 0.1 alpha 0.0
        parallel:
            easein 0.05 rotate 10
            easein 0.1 rotate -10
            easein 0.1 rotate 10
            easein 0.1 rotate -10
            easein 0.05 rotate 00
            pause 0.4
            repeat
style quests_screen_label yalign 0.04
style quests_screen_label_text:
    font "fonts/sm-main.ttf"
    size 60
    color "#b4afb2"
style quests_name_button:
    hover_sound audio.sfx_menu_button_hover
    activate_sound audio.sfx_phone_closed1
    left_padding 65
    top_padding 7
    yalign 0.13
    xsize 410
style quests_name_button_text:
    hover_color gui.selected_color
    outlines [(1, "#000000", 0, 0)]
    kerning 1
style quests_name_viewport:
    yanchor 0.0
    xanchor 0.0
    xpos 30
    ypos 130
    xsize 465
    ysize 934
style quests_name_vscrollbar:
    unscrollable gui.unscrollable
    yalign 0.0
    ypos 140
    ysize 914
style quests_name_vbox spacing 20
style quests_name_hbox:
    ysize 50
    xsize 250
    spacing 15
style quests_old_hint_viewport:
    yanchor 0.0
    xanchor 0.0
    xpos 520
    ypos 124
    xsize 1895
    ysize 934
style quests_old_hint_vscrollbar:
    unscrollable gui.unscrollable
    yalign 0.0
    ypos 134
    ysize 914
style quests_old_hint_vbox spacing 20
style quests_old_hint_hbox spacing 15 ysize 50
style quests_old_hint_text strikethrough True color "#595959"
style quests_curr_hint_hbox ysize 50 spacing 15
style quests_curr_hint_text size 40 xmaximum 1300
style quests_screen_hbox:
    xanchor 1.0
    xpos 1870
    yalign 0.98
    spacing 15
style quests_screen_fixed fit_first True
style quests_screen_button:
    idle_background Frame("images/ui/quests/quest_button_frame_idle.webp", 16, 16, 16, 16)
    hover_background Frame("images/ui/quests/quest_button_frame_hover.webp", 16, 16, 16, 16)
    hover_sound audio.sfx_menu_button_hover
    activate_sound audio.sfx_phone_knob1
    left_padding 30
    right_padding 30
    top_padding 20
    bottom_padding 20
style quests_screen_button_text:
    size 57
    idle_color "#fab7c2"
    hover_color "#ffdfe1"