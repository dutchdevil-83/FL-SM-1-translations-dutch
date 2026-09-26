init -498:
    screen replay_gallery(page=1):
        tag menu

        default gallery_page = page
        use gallery(_("Replay Gallery"), "replay", gallery_page)
init -498:
    screen achievements(page=1):
        tag menu

        default gallery_page = page
        use gallery(_("Achievements"), "achievement", gallery_page)
init -498:
    screen gallery(title, gallery, page):
        style_prefix "gallery"

        default character_filter = "None"
        $ total_pages = SMGallery.get_gallery_page_count(gallery, character_filter)
        $ data = SMGallery.get_gallery_page(gallery, page, character_filter)
        $ hint_label = _("Hints on") if persistent.gallery_hint else _("Hints off")
        use game_menu(title):
            hbox:
                style_prefix "gallery_options"
                if gallery == "achievement":
                    textbutton hint_label action ToggleVariable("persistent.gallery_hint") selected (persistent.gallery_hint)
                textbutton _("Character Filter: [character_filter!t]") action CaptureFocus("char_filter") selected (character_filter != "None")
            if is_dev_environment is True:
                hbox:
                    style_prefix "gallery_lock_unlock"
                    imagebutton auto "images/ui/gallery/gallery_unlock_%s.webp" action Function(SMGallery.unlock_everything, gallery) sensitive not SMGallery.gallery_all_unlocked(gallery)
                    text "  |  " yalign 0.5 style "gallery_lock_unlock_seperator"
                    imagebutton auto "images/ui/gallery/gallery_lock_%s.webp" action Function(SMGallery.lock_everything, gallery) sensitive not SMGallery.gallery_all_locked(gallery)
            hbox:
                style_prefix "gallery_page"
                text __("Page [page]")
            grid 3 2:
                style_prefix "slot"
                for _sl2_i in data:
                    $ (slot, title, hint, thumbnail, character_list)  = _sl2_i
                    if slot:
                        if SMGallery.is_gallery_slot_unlocked(gallery, slot):
                            button:
                                vbox:
                                    if thumbnail is None:
                                        add SMGallery.get_gallery_thumb(gallery, slot) xalign 0.5
                                    elif gallery == "achievement":
                                        add thumbnail
                                    else:
                                        add thumbnail at thumbnail_transform
                                    null height 20
                                    text title style "slot_name_text"
                                    if gallery == "achievement" and persistent.gallery_hint:
                                        text hint style "slot_hint_text"
                                if gallery == "achievement":
                                    action achievement_gallery.Action(slot)
                                else:
                                    action [Function(SMGallery.set_replay_scope, slot, main_menu), Replay(replay_gallery[slot]["label"], replay_gallery[slot]["scope"], False)]
                        else:
                            button:
                                action NullAction()
                                vbox:
                                    fixed:
                                        if thumbnail is None:
                                            add SMGallery.get_gallery_thumb(gallery, slot) xalign 0.5 at blur_image(27)
                                        elif gallery == "achievement":
                                            add thumbnail at blur_image(27)
                                        else:
                                            add thumbnail at thumbnail_transform(27)
                                        add "images/ui/gallery/gallery_locked_button.webp" xalign 0.5
                                    null height 20
                                    text title style "slot_name_text"
                                    if gallery == "achievement" and persistent.gallery_hint:
                                        text hint style "slot_hint_text"
            hbox:
                style_prefix "page"
                textbutton _("<") action SetScreenVariable("gallery_page", page - 1) sensitive page > 1
                for i in range(1, total_pages + 1):
                    textbutton "[i]" action SetScreenVariable("gallery_page", i)
                textbutton _(">") action SetScreenVariable("gallery_page", page + 1) sensitive page < total_pages
            if GetFocusRect("char_filter"):
                dismiss action ClearFocus("char_filter")
                frame:
                    style_prefix "char_filter"
                    modal True
                    vbox:
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            vbox:
                                textbutton _("None") action (SetLocalVariable("character_filter", "None"), SetScreenVariable("gallery_page", 1), ClearFocus("char_filter")) selected (character_filter == "None")
                                for character in SMGallery.get_characters_in_gallery(gallery):
                                    textbutton character action (SetLocalVariable("character_filter", character), SetScreenVariable("gallery_page", 1), ClearFocus("char_filter")) selected (character_filter == character)
                        textbutton _("Close") action ClearFocus("char_filter") style "char_filter_close"
init -498:
    screen _gallery(locked, displayables, index, count, gallery, **properties):
        if locked:
            add "#000"
            text _("Image [index] of [count] locked.") align (0.5, 0.5)
        else:
            for d in displayables:
                add d
        key "game_menu" action gallery.Return()
        if gallery.navigation:
            use gallery_navigation(gallery=gallery, count=count)
init -498:
    screen gallery_navigation(gallery, count):
        hbox:
            spacing 20
            style_group "gallery_navigation"
            xalign 0.98
            yalign 0.98
            if count > 1:
                textbutton _("Prev") action gallery.Previous(unlocked = gallery.unlocked_advance)
                textbutton _("Next") action gallery.Next(unlocked = gallery.unlocked_advance)
            textbutton _("Return") action gallery.Return() keysym "game_menu"
init -498:
    screen gallery_unlock_notify(message, gallery, slot_name):
        zorder 100
        style_prefix "notify"
        tag notify

        button:
            at notify_appear
            if gallery == "replay":
                action [ShowMenu("replay_gallery", SMGallery.get_slot_page(gallery, slot_name)), Hide("gallery_unlock_notify")]
            elif gallery == "achievement":
                action [ShowMenu("achievements", SMGallery.get_slot_page(gallery, slot_name)), Hide("gallery_unlock_notify")]
            frame:
                text "[message!t]{color=#d18fe7}[slot_name!t]{/color}"
        timer 3.25 action Hide("gallery_unlock_notify")
init 2:
    transform thumbnail_transform(b=0):
        xalign 0.5 crop (0, 27, 1920, 1027) xsize 384 ysize 216 blur b
init 2:
    transform blur_image(amount):
        blur amount
init 2 style gallery_navigation_button_text is gallery_button_text
init 2 style gallery_lock_unlock_hbox xanchor 1.0 xpos 1115
init 2:
    style gallery_lock_unlock_seperator:
        color gui.idle_color
        font "fonts/Arial-Unicode.ttf"
        yoffset -7
init 2 style gallery_options_hbox xpos 80 spacing 50
init 2:
    style gallery_page_hbox:
        xanchor 1.0
        xpos 1315
        yalign 0.0
        spacing 10
init 2:
    style gallery_page_text:
        yalign 1.0
        color gui.interface_text_color
        font gui.interface_text_font
init 2:
    style hint_text:
        selected_color gui.selected_color
        idle_color gui.idle_color
        hover_color gui.hover_color
        selected_hover_color gui.hover_color
        insensitive_color "#636261"
        font gui.interface_text_font
init 2 style slot_fixed fit_first True
init 2 style slot_hint_text is slot_button_text
init 2 style slot_hint_text size 20
init 2:
    style char_filter_frame:
        background Solid("#2F2F2F")
        xmaximum 250
        ymaximum 800
        xpos 450
init 2 style char_filter_vbox spacing 20
init 2 style char_filter_viewport ymaximum 700
init 2:
    style char_filter_button:
        selected_color gui.selected_color
        idle_color gui.idle_color
        hover_color gui.hover_color
        selected_hover_color gui.hover_color
        xpos 20
init 2:
    style char_filter_vscrollbar:
        ysize 650
        ypos 60
        unscrollable gui.unscrollable
init 2 style char_filter_close xalign 0.99
init 2:
    style char_filter_close_text:
        idle_color gui.idle_color
        hover_color gui.hover_color
        font gui.interface_text_font