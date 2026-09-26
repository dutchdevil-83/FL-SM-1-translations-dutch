screen phone_main_ui():
    modal True
    zorder 200
    style_prefix "phone_menu"
    tag phone

    on "show" action SetVariable("_rollback", False)
    on "hide" action SetVariable("_rollback", True)
    on "replaced" action SetVariable("_rollback", True)
    use phone_bottom_parts
    add "images/ui/phone/phone_wallpaper_1.webp" xalign 0.5 yalign 0.43
    grid 3 3:
        yalign 0.2
        allow_underfull True
        if is_dev_environment or not vn_mode:
            vbox:
                imagebutton auto "images/ui/phone/phone_quests_%s.webp" xalign 0.5 focus_mask True action ShowMenu("quests_screen")
                text _("Quests")
        if not vn_mode:
            vbox:
                imagebutton auto "images/ui/phone/phone_topics_%s.webp" xalign 0.5 focus_mask True action ShowMenu("topics_screen")
                text _("Topics")
        vbox:
            imagebutton auto "images/ui/phone/phone_neutral_chars_%s.webp" xalign 0.5 focus_mask True action ShowMenu("neutral_characters")
            text _("Neutral Characters")
        if player.is_storyline_item_finished(IT_STORY_LINE, "sm1fs_i003"):
            vbox:
                imagebutton auto "images/ui/phone/phone_it_faction_%s.webp" xalign 0.5 focus_mask True action ShowMenu("it_faction")
                text _("Orbix")
        if player.is_storyline_item_finished(THEATER_STORY_LINE, "sm1fs_t003"):
            vbox:
                imagebutton auto "images/ui/phone/phone_th_faction_%s.webp" xalign 0.5 focus_mask True action ShowMenu("th_faction")
                text _("Theater")
        if not in_a_scene and not vn_mode:
            if player.is_storyline_item_finished(MS, "sm1ms014") and not player.is_storyline_item_finished(MS, "sm1ms020"):
                vbox:
                    imagebutton auto "images/ui/phone/phone_renovation_%s.webp" xalign 0.5 focus_mask True action Show("renovation_screen", from_phone=True)
                    text _("Renovation")
        if not in_a_scene and not vn_mode:
            fixed:
                vbox:
                    imagebutton auto "images/ui/phone/phone_chat_%s.webp" xalign 0.5 focus_mask True action Show("phone_chat")
                    text _("Messenger")
                $ active_chats_count = ChatController.get_active_chats_number()
                if active_chats_count:
                    frame:
                        style_prefix "unred_chat_count"
                        text str(active_chats_count)
        if not in_a_scene and not vn_mode:
            if player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s01") and not player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s11i"):
                vbox:
                    imagebutton auto "images/ui/phone/phone_pirates_movie_%s.webp" xalign 0.5 focus_mask True action Show("pirates_movie_progress", from_phone=True)
                    text _("Pirates Movie")
        if is_dev_environment:
            if not in_a_scene and not vn_mode:
                vbox:
                    imagebutton auto "images/ui/phone/phone_vn_%s.webp" xalign 0.5 focus_mask True action [Hide(), Jump("switch_to_vn_mode")]
                    text _("VN Mode")
    grid 3 2:
        yalign 0.85
        vbox:
            imagebutton auto "images/ui/phone/phone_qsave_%s.webp" xalign 0.5 focus_mask True action QuickSave()
            text _("Quick Save")
        vbox:
            imagebutton auto "images/ui/phone/phone_qload_%s.webp" xalign 0.5 focus_mask True action QuickLoad()
            text _("Quick Load")
        vbox:
            imagebutton auto "images/ui/phone/phone_history_%s.webp" xalign 0.5 focus_mask True action [Hide("phone_main_ui"), ShowMenu("history")]
            text _("History")
        vbox:
            imagebutton auto "images/ui/phone/phone_save_%s.webp" xalign 0.5 focus_mask True action [Hide("phone_main_ui"), ShowMenu("save")]
            text _("Save")
        vbox:
            imagebutton auto "images/ui/phone/phone_load_%s.webp" xalign 0.5 focus_mask True action [Hide("phone_main_ui"), ShowMenu("load")]
            text _("Load")
        vbox:
            imagebutton auto "images/ui/phone/phone_pref_%s.webp" xalign 0.5 focus_mask True action [Hide("phone_main_ui"), ShowMenu("preferences")]
            text _("Settings")
    use phone_top_parts
    if not vn_mode:
        use phone_stats_screen
screen phone_stats_screen():
    add "images/ui/phone/phone_stats_background.webp" xalign 0.28 yalign 1.0
    vbox:
        style_prefix "phone_stats_frame"
        vbox:
            style_prefix "phone_stats"
            add "images/ui/phone/phone_stats_devider.webp"
            hbox:
                add "images/ui/phone/phone_stats_money.webp"
                text "$[player.money]"
        vbox:
            style_prefix "phone_stats"
            add "images/ui/phone/phone_stats_devider.webp"
            hbox:
                add "images/ui/phone/phone_stats_energy.webp"
                text "[player.energy]/[player.max_energy]"
screen phone_top_parts():
    add "images/ui/phone/phone_body.webp" xalign 0.5 yalign 0.5
    imagebutton idle "images/ui/phone/phone_nav_bar.webp" action Show("phone_main_ui") xalign 0.5 yalign 0.92
    imagebutton auto "images/ui/buttons/close_%s.webp" action Hide() xalign 0.67 yalign 0.07
screen phone_bottom_parts(mask="images/ui/phone/phone_return_mask.webp"):
    add "images/ui/phone/phone_overlay.webp"
    button action Hide() focus_mask mask style "phone_return_button"
    key "game_menu" action Hide()
style phone_menu_grid spacing 25 xalign 0.50
style phone_menu_fixed fit_first True
style phone_menu_vbox spacing 2
style phone_menu_text:
    xsize 110
    xalign 0.5
    line_spacing 5
    text_align 0.5
    color "#FFF"
    size 20
    font "fonts/consola.ttf"
style phone_return_button activate_sound audio.sfx_phone_closed1 hover_sound audio.sfx_menu_button_hover
style phone_menu_image_button activate_sound audio.sfx_phone_knob1 hover_sound audio.sfx_menu_button_hover
style phone_stats_frame_vbox:
    yanchor 0.0
    xalign 0.29
    yalign 0.09
    spacing 80
style phone_stats_vbox spacing 10
style phone_stats_hbox spacing 15
style phone_stats_text:
    size 32
    color "#FFFFFF"
    yalign 0.5