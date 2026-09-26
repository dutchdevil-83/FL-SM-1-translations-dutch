screen studio_laptop():
    modal True
    zorder 350

    $ rotation_angle = SMGameTime.calculate_rotation(gt.curr_hour, gt.curr_minute)
    $ current_day = gt.curr_day[:2]
    button action Return() focus_mask "images/ui/studio_laptop/studio_laptop_close_focus_mask.webp"
    add "images/ui/studio_laptop/studio_laptop_wallpaper.webp"
    imagebutton auto "images/ui/studio_laptop/studio_laptop_browser_%s.webp" action Jump("sm_website") xcenter 240 ypos 105
    text _("S&M Website") xcenter 240 ypos 180 style "phone_menu_text"
    frame:
        xalign 0.9
        yalign 0.1
        style_prefix "ui_clock"
        add "images/ui/time/watch_base.webp" xcenter 0.5 ycenter 0.5
        add "sm_watchface" xcenter 0.5 ycenter 0.5
        add "images/ui/time/watch_times.webp" xcenter 0.5 ycenter 0.5
        add "images/ui/time/watch_hand.webp" xcenter 0.5 ycenter 0.5 at watch_hand(rotation_angle)
        text "[gt.curr_time!t]" xalign 0.5 yalign 0.92
        text "[current_day!t]" xalign 0.08 yalign 0.5
        button focus_mask "images/ui/time/watch_button_mask.webp" action NullAction()
    use studio_laptop_border
screen studio_laptop_border():
    add "images/ui/studio_laptop/studio_laptop_taskbar.webp" xalign 0.5 ypos 917
    imagebutton auto "images/ui/studio_laptop/studio_laptop_home_%s.webp" action [Jump("studio_laptop") if CurrentScreenName() != "studio_laptop" else NullAction()] keysym "game_menu" xpos 180 ycenter 945
    imagebutton auto "images/ui/studio_laptop/studio_laptop_power_%s.webp" action Return() keysym "game_menu" xpos 1710 ycenter 945
    add f"images/ui/studio_laptop/studio_laptop_border_{gt.curr_display_time_short}.webp"
    add f"images/ui/studio_laptop/studio_laptop_screen_{gt.curr_display_time_short}.webp" alpha 0.2