screen phone_chat(arg_char=None):
    modal True
    zorder 200
    style_prefix "phone_chat"
    tag phone

    default characters = CharacterController.get_characters_for_phone_chat()
    default selected_charcter = characters[0] if not arg_char else CharacterController.get_character(arg_char)
    $ chat_history = ChatController.get_chat_history(selected_charcter)
    on "show":
        if not vn_mode:
            action SetVariable("_rollback", False)
        else:
            action SetVariable("quick_menu", False)
    on "hide":
        if not vn_mode:
            action [ClearFocus(None), SetVariable("_rollback", True)]
        else:
            action [ClearFocus(None), SetVariable("quick_menu", True)]
    if not vn_mode:
        use phone_bottom_parts(mask="images/ui/phone_chat/phone_chat_return_mask.webp")
    else:
        add "images/ui/phone/phone_overlay.webp"
    add "images/ui/phone_chat/chat_shadow.webp" yalign 0.5 xalign 0.2
    add "images/ui/phone_chat/chat_background.webp" xalign 0.5 yalign 0.43
    add "images/ui/phone_chat/chat_top_bottom_overlay.webp" xalign 0.5 yalign 0.43
    text "{}".format(selected_charcter.name) style "phone_chat_char_name"
    add "images/ui/phone_chat/phone_chat_picture_bg.webp" xalign 0.59 yalign 0.07
    add AlphaMask(Transform(f"images/utilities/profile_pictures/profiile_picture_{selected_charcter.codename}.webp", fit="contain", xsize=82, ysize=82), "images/ui/phone_chat/phone_chat_picture_mask.webp") xalign 0.59 yalign 0.07
    add "images/ui/phone_chat/phone_chat_read_border.webp" xalign 0.59 yalign 0.07
    viewport:
        id "phone_chat_vp"
        scrollbars None
        mousewheel True
        arrowkeys True
        pagekeys True
        yinitial 1.0
        draggable True
        vbox:
            for _sl2_i in enumerate(chat_history):
                $ index, message  = _sl2_i
                $ content = message.get(CONTENT)
                if ChatController.is_same_message_group(chat_history, index):
                    null height 10
                else:
                    null height 20
                frame:
                    if message[SENDER] == YOU:
                        background Frame("images/ui/phone_chat/phone_chat_bubble_right.webp", 15, 15, 35, 15)
                        right_padding 35
                        xanchor 1.0
                        xpos 445
                    else:
                        background Frame("images/ui/phone_chat/phone_chat_bubble_left.webp", 35, 15, 15, 15)
                        left_padding 35
                        xpos 10
                    if message[TYPE] == MESSAGE:
                        text content xalign (1.0 if message[SENDER] == YOU else 0.0) style "phone_chat_message"
                    else:
                        fixed:
                            imagebutton idle content action ShowMenu("phone_chat_media", content) hovered CaptureFocus(f"{index}") unhovered ClearFocus(f"{index}") focus_mask True at phone_chat_media
                            if GetFocusRect(f"{index}"):
                                if message[TYPE] == VIDEO:
                                    add "images/ui/phone_chat/phone_chat_play_icon.webp" xalign 0.5 yalign 0.5
                                else:
                                    add "images/ui/phone_chat/phone_chat_view_icon.webp" xalign 0.5 yalign 0.5
                if ChatController.is_last_message(chat_history, index):
                    null height 20
    vbox:
        style_prefix "phone_chat_choices"
        if ChatController.is_next_message_player_reply(selected_charcter):
            for choice in ChatController.get_chat_choices(selected_charcter):
                textbutton choice[CONTENT] action [Function(ChatController.select_chat_choice, selected_charcter, choice[CONTENT]), Hide("phone_chat"), Show("phone_chat", arg_char = selected_charcter.codename)] sensitive choice[SENSITIVE] style "quick_interaction_button"
    if ChatController.is_next_message_from_recipient(selected_charcter):
        timer 0.5 action [Function(ChatController.progress_active_chat, selected_charcter), Hide("phone_chat"), Show("phone_chat", arg_char = selected_charcter.codename)] repeat True
    if not vn_mode:
        use phone_top_parts
        use phone_chat_characters(characters)
        imagebutton auto "images/ui/buttons/back_%s.webp" action Show("phone_main_ui") focus_mask True xalign 0.67 yalign 0.18
    else:
        add "images/ui/phone/phone_body.webp" xalign 0.5 yalign 0.5
        add "images/ui/phone/phone_nav_bar.webp" xalign 0.5 yalign 0.92
    if vn_mode and ChatController.is_chat_end(selected_charcter):
        button action Return()
screen phone_chat_characters(characters):
    style_prefix "phone_chat_chars"

    viewport:
        id "phone_chars_vp"
        scrollbars None
        mousewheel True
        arrowkeys True
        draggable True
        vbox:
            for character in characters:
                fixed:
                    textbutton character.full_name:
                        if character.get_active_chat():
                            action [SetScreenVariable("selected_charcter", character), Hide(character.get_active_chat()[UUID])]
                        else:
                            action SetScreenVariable("selected_charcter", character)
                        if not character.get_chat_history() and not character.get_unread_chat():
                            idle_background Frame("images/ui/phone_chat/chat_char_button_idle_empty.webp", 38, 38, 38, 38)
                    add "images/ui/phone_chat/phone_chat_picture_bg.webp" xpos 5 yalign 0.5
                    add AlphaMask(Transform(f"images/utilities/profile_pictures/profiile_picture_{character.codename}.webp", fit="contain", xsize=82, ysize=82), "images/ui/phone_chat/phone_chat_picture_mask.webp") xpos 5 yalign 0.5
                    if not character.get_unread_chat():
                        add "images/ui/phone_chat/phone_chat_read_border.webp" xpos 5 yalign 0.5
                    else:
                        add "images/ui/phone_chat/phone_chat_unread_border.webp" xpos 5 yalign 0.5
                        frame:
                            style_prefix "unred_chat_count"
                            xpadding 16
                            text "!" size 20
    imagebutton idle "images/ui/phone_chat/chat_arrow_down_idle.webp" hover "images/ui/phone_chat/chat_arrow_down_hover.webp" insensitive Null() focus_mask True action Scroll("phone_chars_vp", "vertical increase", amount=97, delay=0.0) xalign 0.23 yalign 0.985
    imagebutton idle "images/ui/phone_chat/chat_arrow_up_idle.webp" hover "images/ui/phone_chat/chat_arrow_up_hover.webp" insensitive Null() focus_mask True action Scroll("phone_chars_vp", "vertical decrease", amount=97, delay=0.0) xalign 0.23 yalign 0.015
screen phone_chat_media(media):
    add "black"
    add media at phone_chat_media_full
    key ["game_menu", "K_RETURN", "mouseup_1", "mouseup_3", "K_ESCAPE", "K_MENU", "K_PAUSE"] action Return()
transform phone_chat_media:
    xsize 280
    fit "scale-down"
transform phone_chat_media_full:
    xsize 1920
    ysize 1080
    fit "scale-down"
    xalign 0.5
    yalign 0.5
style phone_chat_char_name:
    font "fonts/barlow-condensed-semi-bold.ttf"
    outlines [(2, "#FFFFFF", 0, 0)]
    color "#000000"
    kerning 1
    xpos 780
    yalign 0.08
    size 50
style phone_chat_viewport:
    xsize 450
    ysize 770
    xalign 0.5
    yalign 0.57
style phone_chat_frame:
    xmaximum 350
    xpadding 15
    ypadding 15
style phone_chat_fixed fit_first True
style phone_chat_message size 25
style phone_chat_choices_vbox:
    xpos 1230
    yanchor 1.0
    ypos 1000
    spacing 40
style phone_chat_chars_viewport:
    xsize 450
    ysize 865
    xalign 0.2
    yalign 0.5
style phone_chat_chars_vbox xsize 450 spacing 10
style phone_chat_chars_fixed fit_first True
style phone_chat_chars_button:
    idle_background Frame("images/ui/phone_chat/chat_char_button_idle.webp", 38, 38, 38, 38)
    hover_background Frame("images/ui/phone_chat/chat_char_button_hover.webp", 38, 38, 38, 38)
    selected_idle_background Frame("images/ui/phone_chat/chat_char_button_hover.webp", 38, 38, 38, 38)
    left_padding 90
    bottom_padding 15
    xsize 403
    ysize 87
style phone_chat_chars_button_text:
    font "fonts/barlow-condensed-semi-bold.ttf"
    color "#000000"
    size 38