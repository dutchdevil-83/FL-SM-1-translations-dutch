init -501:
    screen say(who, what):
        style_prefix "say"

        window:
            id "window"
            background Transform(Frame("gui/textbox.png", xalign = 0.5, yalign = 1.0), alpha = persistent.dialogueboxopacity)
            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"
            text what id "what"
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0
init -1 default persistent.dialogueboxopacity = 1.0
init -1 python:
    config.character_id_prefixes.append("namebox")

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue
init -1 style namebox is default
init -1 style namebox_label is say_label
init -1:
    style window:
        xalign 0.5
        xfill True
        yalign gui.textbox_yalign
        ysize gui.textbox_height
init -1:
    style namebox:
        xpos gui.name_xpos
        xanchor gui.name_xalign
        xsize gui.namebox_width
        ypos gui.name_ypos
        ysize gui.namebox_height
        background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
        padding gui.namebox_borders.padding
init -1:
    style say_label:
        properties gui.text_properties("name", accent=True)
        xalign gui.name_xalign
        yalign 0.5
        outlines [(2, "#000000", 1, 1)]
init -1:
    style say_dialogue:
        properties gui.text_properties("dialogue")
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos
        outlines [(2, "#000000", 1, 1)]
        adjust_spacing False
init -501:
    screen input(prompt):
        style_prefix "input"

        window:
            vbox:
                xanchor gui.dialogue_text_xalign
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos
                text prompt style "input_prompt"
                input id "input"
init -1 style input_prompt is default
init -1 style input_prompt xalign gui.dialogue_text_xalign properties gui.text_properties("input_prompt")
init -1 style input xalign gui.dialogue_text_xalign xmaximum gui.dialogue_width
init -501:
    screen choice(items):
        style_prefix "choice"

        vbox:
            for i in items:
                $ hint = i.kwargs.get("hint", None)
                $ variable = i.kwargs.get("var", None)
                hbox:
                    if persistent.menu_hints and is_hint_available(hint):
                        imagebutton auto "gui/button/menu_hint_%s.webp" yalign 0.5 action [Function(hide_hover_notify), i.action] hovered Function(show_menu_hint, hint, variable) unhovered Function(hide_hover_notify) focus_mask True
                    else:
                        null height 46 width 46
                    textbutton i.caption action i.action
init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text
init -1:
    style choice_vbox:
        xalign 0.5
        ycenter 405
        spacing gui.choice_spacing
init -1:
    style choice_hbox:
        xanchor 1.0
        xpos 1250
        spacing 60
init -1 style choice_button is default properties gui.button_properties("choice_button")
init -1 style choice_button_text is default properties gui.button_text_properties("choice_button")
init -501:
    screen quick_menu():
        zorder 100
        style_prefix "quick"

        default show_call_stack_depth = False
        if quick_menu:
            hbox:
                textbutton _("Back") action Rollback()
                textbutton _("History") action ShowMenu("history")
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Save") action ShowMenu("save")
                textbutton _("Q.Save") action QuickSave()
                textbutton _("Q.Load") action QuickLoad()
                textbutton _("Prefs") action ShowMenu("preferences")
            if phone_button is True and player.get_storyline(MS) > 0:
                imagebutton auto "images/ui/phone/phone_button_%s.webp" action Show("phone_main_ui") tooltip _("Open phone") focus_mask True
                $ active_chats_count = ChatController.get_active_chats_number()
                if active_chats_count and not in_a_scene and not vn_mode:
                    frame:
                        xpos 1860
                        ypos 60
                        style_prefix "unred_chat_count"
                        text str(active_chats_count)
                if show_call_stack_depth:
                    text str(renpy.call_stack_depth()) xpos 1850 ypos 40
        if is_dev_environment:
            key "noshift_K_c" action ToggleLocalVariable("show_call_stack_depth")
        use tooltip_screen
init -1 python:
    config.overlay_screens.append("quick_menu")

init -1 default quick_menu = True
init -1 default phone_button = True
init -1 style quick_button is default
init -1 style quick_button_text is button_text
init -1 style quick_hbox xalign 0.5 yalign 1.0
init -1:
    style quick_button:
        properties gui.button_properties("quick_button")
        activate_sound audio.sfx_submenu_click
        hover_sound audio.sfx_submenu_click
init -1:
    style quick_image_button:
        xpos 1815
        activate_sound audio.sfx_phone_open1
        hover_sound audio.sfx_submenu_click
init -1 style quick_button_text properties gui.button_text_properties("quick_button")
init -1:
    style unred_chat_count_frame:
        background Frame("images/ui/buttons/message_count_frame.webp", 18, 18, 18, 18)
        xpadding 15
        ypadding 10
init -1 style unred_chat_count_text size 22
init -501:
    screen nvl(dialogue, items=None):
        window:
            style "nvl_window"
            vbox:
                spacing gui.nvl_spacing
                if gui.nvl_height:
                    vpgrid:
                        cols 1
                        yinitial 1.0
                        use nvl_dialogue(dialogue)
                else:
                    use nvl_dialogue(dialogue)
                for i in items:
                    textbutton i.caption action i.action style "nvl_button"
        add SideImage() xalign 0.0 yalign 1.0
init -501:
    screen nvl_dialogue(dialogue):
        for d in dialogue:
            window:
                id d.window_id
                fixed:
                    yfit gui.nvl_height is None
                    if d.who is not None:
                        text d.who id d.who_id
                    text d.what id d.what_id
init -1 define config.nvl_list_length = gui.nvl_list_length
init -1 style nvl_window is default
init -1 style nvl_entry is default
init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue
init -1 style nvl_button is button
init -1 style nvl_button_text is button_text
init -1:
    style nvl_window:
        xfill True
        yfill True
        background "gui/nvl.png"
        padding gui.nvl_borders.padding
init -1 style nvl_entry xfill True ysize gui.nvl_height
init -1:
    style nvl_label:
        xpos gui.nvl_name_xpos
        xanchor gui.nvl_name_xalign
        ypos gui.nvl_name_ypos
        yanchor 0.0
        xsize gui.nvl_name_width
        min_width gui.nvl_name_width
        text_align gui.nvl_name_xalign
init -1:
    style nvl_dialogue:
        xpos gui.nvl_text_xpos
        xanchor gui.nvl_text_xalign
        ypos gui.nvl_text_ypos
        xsize gui.nvl_text_width
        min_width gui.nvl_text_width
        text_align gui.nvl_text_xalign
        layout ("subtitle" if gui.nvl_text_xalign else "tex")
init -1:
    style nvl_thought:
        xpos gui.nvl_thought_xpos
        xanchor gui.nvl_thought_xalign
        ypos gui.nvl_thought_ypos
        xsize gui.nvl_thought_width
        min_width gui.nvl_thought_width
        text_align gui.nvl_thought_xalign
        layout ("subtitle" if gui.nvl_text_xalign else "tex")
init -1:
    style nvl_button:
        properties gui.button_properties("nvl_button")
        xpos gui.nvl_button_xpos
        xanchor gui.nvl_button_xalign
init -1 style nvl_button_text properties gui.button_text_properties("nvl_button")