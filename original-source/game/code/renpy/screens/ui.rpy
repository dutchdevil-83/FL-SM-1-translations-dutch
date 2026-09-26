screen game_ui():
    $ rotation_angle = SMGameTime.calculate_rotation(gt.curr_hour, gt.curr_minute)
    $ current_day = gt.curr_day[:2]
    if gt.curr_timeslot not in [TIMESLOT_1, TIMESLOT_2] and not renpy.get_screen("character_interaction_menu") and not renpy.get_screen("object_interaction_menu") and not renpy.get_screen("location_interaction_menu"):
        imagebutton auto "skip_time_%s" xpos 210 ypos 1 focus_mask True action Function(gt.skip_time_button_action) tooltip _("Skip time") style "time_skip_button"
    if len(QuestController.get_active_quest_hint()) > 0 and not renpy.get_screen("character_interaction_menu") and not renpy.get_screen("object_interaction_menu") and not renpy.get_screen("location_interaction_menu"):
        if show_quest_list is False:
            imagebutton auto "images/ui/buttons/quest_show_%s.webp" action SetVariable("show_quest_list", True) focus_mask True tooltip _("Show Quests") yalign 0.11 xalign 0.995
        else:
            imagebutton auto "images/ui/buttons/quest_hide_%s.webp" action SetVariable("show_quest_list", False) focus_mask True tooltip _("Hide Quests") yalign 0.112 xalign 0.89
            add "images/ui/quests/quest_frame.webp" xalign 1.0 yalign 0.23
            vbox:
                style_prefix "quest_ui"
                for _sl2_i in QuestController.get_active_quest_hint().items():
                    $ storyline, hint  = _sl2_i
                    hbox:
                        add "images/ui/quests/quest_icon.webp"
                        textbutton hint yalign 0.5 action ShowMenu("quests_screen", storyline)
    frame:
        style_prefix "ui_clock"
        add "images/ui/time/watch_base.webp" xcenter 0.5 ycenter 0.5
        add "sm_watchface" xcenter 0.5 ycenter 0.5
        add "images/ui/time/watch_times.webp" xcenter 0.5 ycenter 0.5
        add "images/ui/time/watch_hand.webp" xcenter 0.5 ycenter 0.5 at watch_hand(rotation_angle)
        text "[gt.curr_time!t]" xalign 0.5 yalign 0.92
        text "[current_day!t]" xalign 0.08 yalign 0.5
        button focus_mask "images/ui/time/watch_button_mask.webp" action NullAction() tooltip _("Timeslot: {}").format(gt.curr_timeslot)
    imagebutton idle "images/ui/energy/energy_frame.webp" focus_mask True action NullAction() tooltip _("Energy: {}/{}").format(player.energy, player.max_energy)
    add "sm_energy_meter" xalign 0.0 yalign 0.0
    if config.developer is True:
        use dev_controls
    use tooltip_screen
style time_skip_button activate_sound audio.sfx_ui_time_skip1 hover_sound audio.sfx_submenu_click
style ui_clock_frame:
    background None
    xsize 250
    ysize 250
    xpos 10
    ypos -5
style ui_clock_text:
    font "fonts/consola.ttf"
    size 16
    color "#a55758"
style quest_ui_vbox:
    xsize 200
    yanchor 0.0
    xalign 0.99
    yalign 0.145
    spacing 10
style quest_ui_hbox spacing 5
style quest_ui_button_text:
    yalign 0.5
    font "fonts/consola.ttf"
    size 18
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]