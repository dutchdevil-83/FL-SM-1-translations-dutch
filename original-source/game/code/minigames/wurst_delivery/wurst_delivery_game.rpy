screen wurst_delivery():
    tag wurst_delivery

    add "city_map"
    for p in delivery_points:
        if p.end_location is True:
            if delivery_finished is False:
                add "lwd_icon_idle" xcenter p.posx ycenter p.posy
            else:
                imagebutton auto "lwd_icon_%s" xcenter p.posx ycenter p.posy action [SetVariable("delivery_clicked_button", p.num), Function(p.click_button), Function(renpy.show_screen, "delivery_wait_time", p.posx + 25, p.posy + 55)] focus_mask True style "wurst_delivery_location" at time_bar
    for p in delivery_points:
        if p.end_location is False:
            if p.done is True:
                add "delivery_done_position" xcenter p.posx ycenter p.posy
            else:
                imagebutton auto "delivery_next_%s" xcenter p.posx ycenter p.posy action [SetVariable("delivery_clicked_button", p.num), Function(p.click_button), Function(renpy.show_screen, "delivery_wait_time", p.posx + 20, p.posy + 50)] focus_mask True style "wurst_delivery_location"
    add "delivery_self_location" yanchor 0.4 xcenter delivery_current_x ypos delivery_current_y
    use delivery_timer
screen delivery_wait_time(posx, posy):
    modal True

    timer 0.05 repeat True action If(delivery_time > 0, true = SetScreenVariable("delivery_time", delivery_time - 0.05), false = (If(delivery_finished, true = (Function(WurstDelivery.retrurned_to_wd), Hide("delivery_wait_time")), false = (Function(WurstDelivery.check_delivery_done), Hide("delivery_wait_time")))))
    text _("Travelling to location") color "#FFF" size 80 xalign 0.5 yalign 0.1 outlines [(3, "#000000", 0, 0)]
    bar value delivery_time range delivery_bar_range yanchor 1.0 xcenter posx - 20 ypos posy xsize 100 ysize 15
screen delivery_timer():
    style_prefix "wurst_delivery_timer"

    timer 0.1 action If(retrurned_to_wd, true = (Hide("wurst_delivery"), Function(WurstDelivery.end_game, mt)), false = Function(mt.add, 0, 0, 0.1)) repeat True
    frame:
        hbox:
            image "minigame_timer_icon" yalign 0.52
            text "[mt.minigame_timer]" color "#FFFFFF" size 50 yalign 0.8
style wurst_delivery_location activate_sound audio.sfx_map_destination_click hover_sound audio.sfx_map_destination_hover
style wurst_delivery_timer_frame:
    xalign 0.0
    yalign 0.0
    background "#00000060"
    xsize 225
style wurst_delivery_timer_hbox spacing 10
transform time_bar:
    subpixel True
    zoom 1.0 xanchor 0.5 yanchor 0.5
    easein 0.4 zoom 0.97
    easein 0.4 zoom 1.03
    repeat