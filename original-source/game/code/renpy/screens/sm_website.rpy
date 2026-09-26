screen sm_website(zoom_factor=1.0):
    style_prefix "website"

    button action Return() focus_mask "images/ui/studio_laptop/studio_laptop_close_focus_mask.webp"
    fixed:
        at zoom(zoom_factor)
        add "images/ui/website/website_bg.webp"
        add "images/ui/website/website_logo.webp" xalign 0.02 ycenter 0.05
        fixed:
            style_prefix "website_search"
            add "images/ui/website/website_search_bar.webp"
            add "images/ui/website/website_search_icon.webp" xalign 0.01 yalign 0.5
        add "images/ui/website/website_hamburger_menu.webp" xalign 0.98 ycenter 0.05
        hbox:
            style_prefix "website_top_menu"
            textbutton _("HOME") action NullAction()
            textbutton _("VIDEOS") action NullAction()
            textbutton _("CATEGORIES") action NullAction()
            textbutton _("ACTRESS") action NullAction()
            textbutton _("COMMUNITY") action NullAction()
            textbutton _("PHOTOS") action NullAction()
        fixed:
            style_prefix "website_new_banner"
            at zoom(0.6)
            add "images/ui/website/website_hot_bar.webp" yalign 0.5
            fixed:
                fit_first True
                xpos 240
                yalign 0.5
                add "images/ui/website/website_small_frame.webp"
                add "images/ui/website/website_small_example_1.webp" xalign 0.5 yalign 0.5
            fixed:
                fit_first True
                xanchor 1.0
                xpos 1680
                yalign 0.5
                add "images/ui/website/website_small_frame.webp"
                add "images/ui/website/website_small_example_2.webp" xalign 0.5 yalign 0.5
            fixed:
                fit_first True
                xpos 440
                yalign 0.5
                add "images/ui/website/website_big_frame.webp"
                add "images/ui/website/website_big_example_1.webp" xalign 0.5 yalign 0.5
            fixed:
                fit_first True
                xanchor 1.0
                xpos 1480
                yalign 0.5
                add "images/ui/website/website_big_frame.webp"
                add "images/ui/website/website_big_example_2.webp" xalign 0.5 yalign 0.5
            text _("NEW HOT VIDEOS") xalign 0.5 yalign 0.5
        vbox:
            ysize 250
            xpos 100
            ypos 370
            box_justify "all"
            style_prefix "website_side_buttons"
            textbutton _("New") action NullAction() selected True
            textbutton _("Top") action NullAction()
            textbutton _("Library") action NullAction()
            textbutton _("Categories") action NullAction()
            textbutton _("Tags") action NullAction()
        frame:
            style_prefix "website_videos"
            vpgrid:
                cols 3
                draggable True
                mousewheel True
                scrollbars "vertical"
                for video in sm_website_videos:
                    if player.is_storyline_item_finished(video[UNLOCK_CONDITION][0], video[UNLOCK_CONDITION][1]):
                        button:
                            action Function(SMGallery.start_replay, video[CODENAME])
                            vbox:
                                add f"{video[THUMBNAIL]}" xsize 395 ysize 224
                                text video[NAME]
    use studio_laptop_border
style website_fixed:
    xsize 1920
    ysize 1080
    xalign 0.5
    ycenter 525
style website_search_fixed:
    fit_first True
    xalign 0.5
    ycenter 0.05
style website_top_menu_hbox:
    xsize 1680
    xalign 0.5
    yalign 0.1
    box_justify "all"
style website_top_menu_button_text is website_button_text
style website_new_banner_fixed:
    xsize 1920
    ysize 260
    xalign 0.5
    ypos 160
style website_new_banner_text font "fonts/arial-unicode.ttf" size 50
style website_side_button_text is website_button_text
style website_button_text:
    idle_color "#d1d1d1"
    hover_color "#ec7057"
    selected_idle_color "#ec7057"
    selected_hover_color "#ec7057"
    size 22
style website_videos_frame:
    background None
    xsize 1400
    ysize 670
    xpos 320
    ypos 340
style website_videos_vpgrid xspacing 70 yspacing 20
style website_videos_vscrollbar unscrollable gui.unscrollable xpos 20
style website_videos_vbox:
    xsize 395
    ysize 300
    spacing 20
style website_videos_text:
    idle_color "#d1d1d1"
    hover_color "#ec7057"
    selected_idle_color "#ec7057"
    selected_hover_color "#ec7057"
    xalign 0.5
    text_align 0.5
    xmaximum 395
    size 30