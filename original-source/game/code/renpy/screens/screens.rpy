init -501:
    screen navigation():
        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            yalign 0.5
            spacing gui.navigation_spacing
            if config.developer is True:
                textbutton "Test" action Start("test_label")
            if main_menu and config.developer is True:
                textbutton _("Start from release 2") action Start("jump_to_release_1_end")
            if main_menu:
                textbutton _("Start") action Start()
            else:
                textbutton _("History") action ShowMenu("history")
                textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)
            elif not main_menu:
                textbutton _("Main Menu") action MainMenu()
            textbutton _("About") action ShowMenu("about")
            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Help") action ShowMenu("help")
            textbutton _("Quit") action Quit(confirm=not main_menu)
init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text
init -1:
    style navigation_button:
        size_group "navigation"
        properties gui.button_properties("navigation_button")
        activate_sound audio.sfx_menu_button_click
        hover_sound audio.sfx_menu_button_hover
init -1 style navigation_button_text properties gui.button_text_properties("navigation_button")
init -1:
    image main_menu_background:
        subpixel True
        "gui/mainmenu/main_menu_bg_1.webp" with Dissolve(1.0, alpha=False)
        pause 10.0
        "gui/mainmenu/main_menu_bg_3.webp" with Dissolve(1.0, alpha=False)
        pause 10.0
        "gui/mainmenu/main_menu_bg_2.webp" with Dissolve(1.0, alpha=False)
        pause 10.0
        repeat
init -1:
    image main_menu_particles:
        xalign 0.0 yalign 0.0
        "gui/mainmenu/main_menu_particles_1.webp" with Dissolve(1.0, alpha=True)
        linear 10.0 xalign 1.0 yalign 1.0
        xalign 0.0 yalign 0.0
        "gui/mainmenu/main_menu_particles_2.webp" with Dissolve(1.0, alpha=True)
        linear 10.0 xalign 1.0 yalign 1.0
        xalign 0.0 yalign 0.0
        "gui/mainmenu/main_menu_particles_3.webp" with Dissolve(1.0, alpha=True)
        linear 10.0 xalign 1.0 yalign 1.0
        repeat
init -501:
    screen main_menu():
        tag menu

        add "main_menu_background"
        add "main_menu_particles"
        frame style "main_menu_frame"
        add "gui/mainmenu/main_menu_logo.webp" xalign 0.04 yalign 0.05
        use navigation
        if gui.show_name:
            vbox:
                style "main_menu_vbox"
                text "[config.version]" style "main_menu_version"
init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text
init -1:
    style main_menu_frame:
        xsize 420
        yfill True
        background "gui/overlay/main_menu.png"
init -1:
    style main_menu_vbox:
        xalign 0.99
        yalign 0.99
        xmaximum 1200
init -1 style main_menu_text properties gui.text_properties("main_menu", accent=True)
init -1 style main_menu_title properties gui.text_properties("title")
init -1 style main_menu_version properties gui.text_properties("version")
init -501:
    screen game_menu(title, scroll=None, yinitial=0.0):
        style_prefix "game_menu"

        on "show" action Function(pause_all_sound)
        on "show" action Function(hide_hover_notify)
        add "main_menu_background"
        frame:
            style "game_menu_outer_frame"
            hbox:
                frame style "game_menu_navigation_frame"
                frame:
                    style "game_menu_content_frame"
                    if scroll == "viewport":
                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True
                            side_yfill True
                            vbox:
                                transclude
                    elif scroll == "vpgrid":
                        vpgrid:
                            cols 1
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True
                            side_yfill True
                            transclude
                    else:
                        transclude
        use navigation
        textbutton _("Return") style "return_button" action Return()
        label title
        if main_menu:
            key "game_menu" action ShowMenu("main_menu")
init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar
init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text
init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text
init -1:
    style game_menu_outer_frame:
        bottom_padding 45
        top_padding 180
        background "gui/overlay/game_menu.png"
init -1 style game_menu_navigation_frame xsize 420 yfill True
init -1:
    style game_menu_content_frame:
        left_margin 60
        right_margin 30
        top_margin 15
init -1 style game_menu_viewport xsize 1380
init -1 style game_menu_vscrollbar unscrollable gui.unscrollable
init -1 style game_menu_side spacing 15
init -1 style game_menu_label xpos 75 ysize 180
init -1:
    style game_menu_label_text:
        size gui.title_text_size
        color gui.accent_color
        yalign 0.5
init -1:
    style return_button:
        xpos gui.navigation_xpos
        yalign 1.0
        yoffset -45
init -501:
    screen confirm(message, yes_action, no_action):
        modal True
        zorder 200
        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        frame:
            vbox:
                xalign .5
                yalign .5
                spacing 45
                label _(message) style "confirm_prompt" xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 150
                    textbutton _("Yes") action yes_action keysym ("K_RETURN", "K_KP_ENTER")
                    textbutton _("No") action no_action
        key "game_menu" action no_action
init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text
init -1:
    style confirm_frame:
        background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        padding gui.confirm_frame_borders.padding
        xalign .5
        yalign .5
init -1 style confirm_prompt_text text_align 0.5 layout "subtitle"
init -1:
    style confirm_button:
        properties gui.button_properties("confirm_button")
        activate_sound audio.sfx_submenu_click
        hover_sound audio.sfx_submenu_hover
init -1 style confirm_button_text properties gui.button_text_properties("confirm_button")
init -501:
    screen save():
        tag menu

        use file_slots(_("Save"))
init -501:
    screen load():
        tag menu

        use file_slots(_("Load"))
init -501:
    screen file_slots(title):
        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
        $ pager = Pager()
        use game_menu(title):
            fixed:
                hbox:
                    style_prefix "renamer"
                    hbox:
                        style "page_label"
                        button:
                            style style.button["gm_rename"]
                            key_events True
                            xalign 0.0
                            action page_name_value.Toggle()
                            input style "page_label_text" value page_name_value
                    hbox:
                        style_prefix "save_name_toggle"
                        if CurrentScreenName() == "save":
                            text (_("Naming save file:"))
                            textbutton _("Enabled" ) selected (persistent.save_name_prompt) action SetVariable("persistent.save_name_prompt", True)
                            text "/"
                            textbutton _("Disabled") selected (not persistent.save_name_prompt) action [SetVariable("persistent.save_name_prompt", False), SetVariable("save_name", "")]
                        else:
                            if config.has_sync:
                                textbutton _("Ren'Py Save Sync") action ShowMenu("save_sync_menu")
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"
                    for i in range(gui.file_slot_cols * gui.file_slot_rows):
                        $ slot = i + 1
                        button:
                            if title == "Load":
                                action FileAction(slot)
                            else:
                                if persistent.save_name_prompt is True and FileCurrentPage() != "auto":
                                    action [SetVariable("slot_name", slot), ShowMenu("save_name")]
                                else:
                                    action FileAction(slot)
                            vbox:
                                spacing -4
                                add FileScreenshot(slot) xalign 0.5
                                null height 10
                                text FileTime(slot, format=_("{#file_time}%b %d %Y, %H:%M"), empty=_("Empty Slot")) style "slot_time_text"
                                text FileSaveName(slot) style "slot_name_text"
                                if FileLoadable(slot):
                                    imagebutton auto "images/ui/buttons/delete_%s.webp" action FileDelete(slot) focus_mask "images/ui/buttons/delete_mask.webp" xalign 0.03 ypos -250
                                key "save_delete" action FileDelete(slot)
                hbox:
                    style_prefix "page"
                    if pager.int > 10:
                        textbutton _("«") action FilePage(pager.int - 10)
                    if pager.int > 1:
                        textbutton _("<") action FilePagePrevious()
                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")
                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")
                    for page in pager.rng:
                        textbutton "[page]" action FilePage(page)
                    textbutton _(">") action FilePageNext()
                    textbutton _("»") action FilePage(pager.int + 10)
init -1:
    style renamer_hbox:
        xsize 1250
        xpos 80
        ypos 0
init -1:
    style save_name_toggle_hbox:
        xalign 1.0
        xanchor 1.0
        spacing 10
init -1 style save_name_toggle_text xalign 1.0 yalign 0.5
init -1 style save_sync_hbox xalign 0.5 yalign 0.91
init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text
init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text
init -1:
    style slot_grid:
        xalign 0.5
        yalign 0.5
        spacing gui.slot_spacing
init -1:
    style page_hbox:
        xalign 0.5
        yalign 1.0
        spacing gui.page_spacing
init -1 style page_label xpadding 75 ypadding 5
init -1:
    style page_label_text:
        text_align 0.5
        layout "subtitle"
        hover_color gui.hover_color
init -1 style page_button properties gui.button_properties("page_button")
init -1 style page_button_text properties gui.button_text_properties("page_button")
init -1 style slot_button properties gui.button_properties("slot_button")
init -1 style slot_button_text properties gui.button_text_properties("slot_button")
init -501:
    screen preferences():
        tag menu

        use game_menu(_("Preferences"), scroll="viewport"):
            vbox:
                hbox:
                    box_wrap True
                    if renpy.variant("pc") or renpy.variant("web"):
                        vbox:
                            style_prefix "radio"
                            label _("Display")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                            textbutton "1920 x 1080" action Preference("display", 1.0)
                            textbutton "1600 x 900" action Preference("display", 0.83333333333)
                            textbutton "1280 x 720" action Preference("display", 0.666666666667)
                            textbutton "960 × 540" action Preference("display", 0.5)
                    vbox:
                        style_prefix "check"
                        label _("Skip")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                    if config.developer is True:
                        vbox:
                            style_prefix "radio"
                            label _("Minigames")
                            textbutton _("Enabled") action SetVariable("only_story_mode", False)
                            textbutton _("Disabled") action SetVariable("only_story_mode", True)
                    if collect_analytics is True:
                        if is_steam_edition is True or is_dev_environment is True:
                            vbox:
                                style_prefix "radio"
                                label _("Analytics")
                                textbutton _("Enable") action Function(renpy.invoke_in_thread, GameAnalytics.enable_analytics) selected persistent.analytics_enabled
                                textbutton _("Disable") action Function(renpy.invoke_in_thread, GameAnalytics.disable_analytics) selected not persistent.analytics_enabled
                null height (4 * gui.pref_spacing)
                hbox:
                    style_prefix "slider"
                    box_wrap True
                    vbox:
                        label _("Text Speed")
                        bar value Preference("text speed")
                        label _("Auto-Forward Time")
                        bar value Preference("auto-forward time")
                        label _("Dialogue Box Opacity")
                        bar value FieldValue(persistent, "dialogueboxopacity", range = 1.0, style = "slider")
                    vbox:
                        if config.has_music:
                            label _("Music Volume")
                            hbox:
                                bar value Preference("music volume")
                        if config.has_sound:
                            label _("Sound Volume")
                            hbox:
                                bar value Preference("sound volume")
                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)
                        if config.has_voice:
                            label _("Voice Volume")
                            hbox:
                                bar value Preference("voice volume")
                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice)
                        label _("Sex Voice Volume")
                        hbox:
                            bar value Preference("voisex volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voisex", config.sample_voice)
                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing
                            textbutton _("Mute All") action Preference("all mute", "toggle") style "mute_all_button"
init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox
init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox
init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox
init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox
init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text
init -1 style pref_label top_margin gui.pref_spacing bottom_margin 3
init -1 style pref_label_text yalign 1.0
init -1 style pref_vbox xsize 338
init -1 style radio_vbox spacing gui.pref_button_spacing
init -1:
    style radio_button:
        properties gui.button_properties("radio_button")
        foreground "gui/button/radio_[prefix_]foreground.png"
        activate_sound audio.sfx_submenu_hover
        hover_sound audio.sfx_submenu_click
init -1 style radio_button_text properties gui.button_text_properties("radio_button")
init -1 style check_vbox spacing gui.pref_button_spacing
init -1:
    style check_button:
        properties gui.button_properties("check_button")
        foreground "gui/button/check_[prefix_]foreground.png"
        activate_sound audio.sfx_submenu_hover
        hover_sound audio.sfx_submenu_click
init -1 style check_button_text properties gui.button_text_properties("check_button")
init -1 style slider_slider xsize 525
init -1:
    style slider_button:
        properties gui.button_properties("slider_button")
        yalign 0.5
        left_margin 15
init -1 style slider_button_text properties gui.button_text_properties("slider_button")
init -1 style slider_vbox xsize 675
init -501:
    screen about():
        tag menu

        use game_menu(_("About"), scroll="viewport"):
            style_prefix "about"
            vbox:
                add "gui/mainmenu/main_menu_logo.webp" xpos -18
                text _("Version [config.version!t]\n")
                if gui.about:
                    text "[gui.about!t]\n"
                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
                text "[gui.credits_more!t]"
init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text
init -1 style about_label_text size gui.label_text_size
init -1:
    define gui.about = _p("""
        """)
init -501:
    screen history():
        predict False
        tag menu

        use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
            style_prefix "history"
            for h in _history_list:
                window:
                    fixed:
                        yfit True
                        if h.who:
                            label h.who:
                                style "history_name"
                                substitute False
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]
                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what substitute False
            if not _history_list:
                label _("The dialogue history is empty.")
init -1 define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }
init -1 style history_window is empty
init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text
init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text
init -1 style history_window xfill True ysize gui.history_height
init -1:
    style history_name:
        xpos gui.history_name_xpos
        xanchor gui.history_name_xalign
        ypos gui.history_name_ypos
        xsize gui.history_name_width
init -1 style history_name_text min_width gui.history_name_width text_align gui.history_name_xalign
init -1:
    style history_text:
        xpos gui.history_text_xpos
        ypos gui.history_text_ypos
        xanchor gui.history_text_xalign
        xsize gui.history_text_width
        min_width gui.history_text_width
        text_align gui.history_text_xalign
        layout ("subtitle" if gui.history_text_xalign else "tex")
init -1 style history_label xfill True
init -1 style history_label_text xalign 0.5
init -501:
    screen help():
        tag menu

        default device = "keyboard"
        use game_menu(_("Help"), scroll="viewport"):
            style_prefix "help"
            vbox:
                spacing 23
                hbox:
                    textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                    textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                    if GamepadExists():
                        textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help
init -501:
    screen keyboard_help():
        hbox:
            label _("Enter")
            text _("Advances dialogue and activates the interface.")
        hbox:
            label _("Space")
            text _("Advances dialogue without selecting choices.")
        hbox:
            label _("Arrow Keys")
            text _("Navigate the interface.")
        hbox:
            label _("Escape")
            text _("Accesses the game menu.")
        hbox:
            label _("Ctrl")
            text _("Skips dialogue while held down.")
        hbox:
            label _("Tab")
            text _("Toggles dialogue skipping.")
        hbox:
            label _("Page Up")
            text _("Rolls back to earlier dialogue.")
        hbox:
            label _("Page Down")
            text _("Rolls forward to later dialogue.")
        hbox:
            label "H"
            text _("Hides the user interface.")
        hbox:
            label "S"
            text _("Takes a screenshot.")
        hbox:
            label "V"
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
        hbox:
            label "Shift+A"
            text _("Opens the accessibility menu.")
init -501:
    screen mouse_help():
        hbox:
            label _("Left Click")
            text _("Advances dialogue and activates the interface.")
        hbox:
            label _("Middle Click")
            text _("Hides the user interface.")
        hbox:
            label _("Right Click")
            text _("Accesses the game menu.")
        hbox:
            label _("Mouse Wheel Up\nClick Rollback Side")
            text _("Rolls back to earlier dialogue.")
        hbox:
            label _("Mouse Wheel Down")
            text _("Rolls forward to later dialogue.")
init -501:
    screen gamepad_help():
        hbox:
            label _("Right Trigger\nA/Bottom Button")
            text _("Advances dialogue and activates the interface.")
        hbox:
            label _("Left Trigger\nLeft Shoulder")
            text _("Rolls back to earlier dialogue.")
        hbox:
            label _("Right Shoulder")
            text _("Rolls forward to later dialogue.")
        hbox:
            label _("D-Pad, Sticks")
            text _("Navigate the interface.")
        hbox:
            label _("Start, Guide")
            text _("Accesses the game menu.")
        hbox:
            label _("Y/Top Button")
            text _("Hides the user interface.")
        textbutton _("Calibrate") action GamepadCalibrate()
init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text
init -1 style help_button properties gui.button_properties("help_button") xmargin 12
init -1 style help_button_text properties gui.button_text_properties("help_button")
init -1 style help_label xsize 375 right_padding 30
init -1:
    style help_label_text:
        size gui.text_size
        xalign 1.0
        text_align 1.0
init -501:
    screen skip_indicator():
        zorder 100
        style_prefix "skip"

        frame:
            hbox:
                spacing 9
                text _("Skipping")
                text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
                text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
                text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
init -1:
    transform delayed_blink(delay, cycle):
        alpha .5
        pause delay
        block:
            linear .2 alpha 1.0
            pause .2
            linear .2 alpha 0.5
            pause (cycle - .4)
            repeat
init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text
init -1:
    style skip_frame:
        ypos gui.skip_ypos
        background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
        padding gui.skip_frame_borders.padding
init -1 style skip_text size gui.notify_text_size
init -1 style skip_triangle font "DejaVuSans.ttf"
init -1 default notify_timeout = True
init -501:
    screen notify(message):
        zorder 300
        style_prefix "notify"

        frame:
            at notify_appear
            text "[message!t]"
        if notify_timeout is True:
            timer 3.25 action Hide("notify")
init -1:
    transform notify_appear:
        on show:
            ypos -100
            easein 0.25 ypos 20
        on hide:
            easein 0.25 ypos -100
init -1 style notify_frame is empty
init -1 style notify_text is gui_text
init -1:
    style notify_frame:
        xalign 0.5
        background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
        padding gui.notify_frame_borders.padding
init -1 style notify_text properties gui.text_properties("notify")
init -1 style default properties gui.text_properties() language gui.language
init -1 style input properties gui.text_properties("input", accent=True) adjust_spacing False
init -1 style hyperlink_text properties gui.text_properties("hyperlink", accent=True) hover_underline True
init -1 style gui_text properties gui.text_properties("interface")
init -1 style button properties gui.button_properties("button")
init -1 style button_text is gui_text properties gui.text_properties("button") yalign 0.5
init -1 style label_text is gui_text properties gui.text_properties("label", accent=True)
init -1 style prompt_text is gui_text properties gui.text_properties("prompt")
init -1:
    style bar:
        ysize gui.bar_size
        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
init -1:
    style vbar:
        xsize gui.bar_size
        top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
        bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
init -1:
    style scrollbar:
        ysize gui.scrollbar_size
        base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
init -1:
    style vscrollbar:
        xsize gui.scrollbar_size
        base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
init -1:
    style slider:
        ysize gui.slider_size
        base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
        thumb "gui/slider/horizontal_[prefix_]thumb.png"
init -1:
    style vslider:
        xsize gui.slider_size
        base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
        thumb "gui/slider/vertical_[prefix_]thumb.png"
init -1 style frame padding gui.frame_borders.padding background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)