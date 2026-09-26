screen notification_screen(msg_type, message, target=None, timeout=None, tag=None):
    zorder 300
    style_prefix "notification"

    frame:
        at notification_appear
        modal True
        hbox:
            imagebutton:
                idle f"images/ui/buttons/notification_{msg_type}_icon.webp"
                yalign 0.5
                if target and not in_a_scene:
                    action [Show("phone_chat", arg_char=target), Hide(tag)]
            textbutton "[message!t!i]":
                yalign 0.5
                if target and not in_a_scene:
                    action [Show("phone_chat", arg_char=target), Hide(tag)]
            imagebutton auto "images/ui/buttons/notification_hide_%s.webp" action Hide(tag) yalign 0.5
    if msg_type == PAYMENT and not timeout:
        $ timeout = 10
    if timeout:
        timer timeout action Hide(tag)
transform notification_appear:
    on show:
        xanchor 0.0 xpos 2000
        easein 0.25 xanchor 1.0 xpos 1900
    on hide:
        easein 0.25 xanchor 0.0 xpos 2000
style notification_frame:
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
    xmaximum 550
    yanchor 1.0
    ypos 1060
style notification_hbox:
    xmaximum 550
    first_spacing 0
    spacing 10
style notification_button_text:
    color "#FFFFFF"
    xmaximum 400
    size 26
    yalign 0.5