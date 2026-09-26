screen scifi_movie_commons(from_phone=False):
    style_prefix "scifi_movie_progress"

    $ sm1mv02_char = player.get_choice("sm1mv02_char")
    add "images/ui/movie_progress/scifi_movie/scifi_movie_bg_landscape.webp" xalign 0.5
    add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_bar_float.webp" xcenter 530 ypos 782
    add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_bar_float.webp" xcenter 815 ypos 782
    add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_bar_float.webp" xcenter 1100 ypos 782
    add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_bar_float.webp" xcenter 1385 ypos 782
    add "images/ui/movie_progress/scifi_movie/scifi_movie_bg.webp"
    add "images/ui/movie_progress/scifi_movie/scifi_movie_empty_progress.webp" xalign 0.5
    for _sl2_i in enumerate(scifi_movie.progress_steps):
        $ index, step  = _sl2_i
        if player.is_storyline_item_finished(MOVIE_SCIFI, step):
            add f"images/ui/movie_progress/scifi_movie/progress/scifi_movie_progress_{index + 1}.webp"
    vbox:
        for scene in scifi_movie.extra_scenes_list:
            fixed:
                xsize 245
                ysize 245
                if player.is_storyline_item_finished(MOVIE_SCIFI, scene):
                    if scene == "Q-MV02S02":
                        add f"images/ui/movie_progress/scifi_movie/scene_images/scifi_movie_{sm1mv02_char}_image.webp" xpos 14 ypos 13
                    else:
                        add f"images/ui/movie_progress/scifi_movie/scene_images/scifi_movie_{scene}_image.webp" xpos 14 ypos 13
                else:
                    if scene in ["Q-MV02S02", "sm1mv02s02"]:
                        add "images/ui/movie_progress/scifi_movie/scene_images/scifi_movie_char_image_locked.webp" xpos 14 ypos 13
                    else:
                        add f"images/ui/movie_progress/scifi_movie/scene_images/scifi_movie_{scene}_image.webp" xpos 14 ypos 13 at blur_image(15)
                add "images/ui/movie_progress/scifi_movie/scifi_movie_character_frame.webp"
                if player.is_storyline_item_finished(MOVIE_SCIFI, scene):
                    add "images/ui/movie_progress/scifi_movie/scifi_movie_done.webp" xalign 1.0 yalign 1.0
    hbox:
        for movie in scifi_movie.main_scenes_list:
            fixed:
                xsize 207
                ysize 207
                if player.is_storyline_item_finished(MOVIE_SCIFI, movie):
                    if movie in ["sm1mv02s06", "sm1mv02s08"]:
                        add f"images/ui/movie_progress/scifi_movie/scene_images/scifi_movie_{movie}_{sm1mv02_char}_image.webp" xpos 12 ypos 11
                    else:
                        add f"images/ui/movie_progress/scifi_movie/scene_images/scifi_movie_{movie}_image.webp" xpos 12 ypos 11
                else:
                    add f"images/ui/movie_progress/scifi_movie/scene_images/scifi_movie_{movie}_image.webp" xpos 12 ypos 11 at blur_image(15)
                add "images/ui/movie_progress/scifi_movie/scifi_movie_scene_frame.webp"
                if player.is_storyline_item_finished(MOVIE_SCIFI, movie):
                    add "images/ui/movie_progress/scifi_movie/scifi_movie_done.webp" xalign 1.0 yalign 1.0
    frame:
        style_prefix "scifi_movie_data"
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            style_prefix "phone_stats"
            hbox:
                add "images/ui/phone/phone_stats_money.webp"
                text "$[player.money]"
            hbox:
                add "images/ui/phone/phone_stats_energy.webp"
                text "[player.energy]/[player.max_energy]"
    textbutton _("BACK"):
        keysym "game_menu"
        style "scifi_movie_back_button"
        if from_phone:
            action Hide()
        else:
            action Return()
screen scifi_movie_progress(from_phone=False):
    modal True
    zorder 350
    style_prefix "scifi_movie_progress"
    tag phone

    $ set_budget_var = scifi_movie.get_curr_budget_energy("set_budget")
    $ set_energy_var = scifi_movie.get_curr_budget_energy("set_energy")
    $ actress_budget_var = scifi_movie.get_curr_budget_energy("actress_budget")
    $ outfit_energy_var = scifi_movie.get_curr_budget_energy("outfit_energy")
    $ cgi_budget_var = scifi_movie.get_curr_budget_energy("cgi_budget")
    $ editing_energy_var = scifi_movie.get_curr_budget_energy("editing_energy")
    $ sm1mv02s08i_done = player.is_storyline_item_finished(MOVIE_SCIFI, "sm1mv02s08i")
    if not scifi_movie.first_animation_done and sm1mv02s08i_done:
        if from_phone:
            on "replace" action Show("scifi_movie_progress_animation", from_phone=True)
        else:
            on "show" action Show("scifi_movie_progress_animation")
    use scifi_movie_commons(from_phone=from_phone)
    if player.is_storyline_item_finished(MOVIE_SCIFI, "Q-MV02S03") and not sm1mv02s08i_done:
        fixed:
            xcenter 530
            style_prefix "scifi_movie_progress_bars"
            add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
            vbar value AnimatedValue(value=set_budget_var, range=scifi_movie.total_set_budget, delay=1.0) style "scifi_movie_progress_money_vbar"
            textbutton [_(f"Add ${scifi_movie.add_money_value}") if not scifi_movie.is_budget_energy_filled("set_budget") else _("Done")]:
                tooltip scifi_movie.get_add_money_tooltip("set_budget")
                style "scifi_movie_progress_bar_button"
                if scifi_movie.is_add_money_available("set_budget"):
                    action [Function(scifi_movie.add_budget_energy, "set_budget", scifi_movie.add_money_value), Function(spawn_text, f"+ ${scifi_movie.add_money_value}", 530, 450, "fonts/mr-amazin-regular-type.otf")]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28)
            add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
            text _("SET BUDGET") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
        add "scifi_movie_lightning_1" xcenter 530 ypos 730
        fixed:
            xcenter 815
            style_prefix "scifi_movie_progress_bars"
            add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
            vbar value AnimatedValue(value=set_energy_var, range=scifi_movie.total_set_energy, delay=1.0) style "scifi_movie_progress_vbar"
            textbutton [_(f"Add {scifi_movie.add_energy_value}E") if not scifi_movie.is_budget_energy_filled("set_energy") else _("Done")]:
                tooltip scifi_movie.get_add_energy_tooltip("set_energy")
                style "scifi_movie_progress_bar_button"
                if scifi_movie.is_add_energy_available("set_energy"):
                    action [Function(scifi_movie.add_budget_energy, "set_energy", scifi_movie.add_energy_value), Function(spawn_text, f"+ {scifi_movie.add_energy_value}E", 815, 450, "fonts/mr-amazin-regular-type.otf")]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28)
            add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
            text _("SET DESIGN") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
        add "scifi_movie_lightning_2" xcenter 815 ypos 730
    if player.is_storyline_item_finished(MOVIE_SCIFI, "sm1mv02s05i"):
        fixed:
            xcenter (1100 if not sm1mv02s08i_done else 530)
            style_prefix "scifi_movie_progress_bars"
            add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
            vbar value AnimatedValue(value=actress_budget_var, range=scifi_movie.total_actress_budget, delay=1.0) style "scifi_movie_progress_money_vbar"
            textbutton [_(f"Add ${scifi_movie.add_money_value}") if not scifi_movie.is_budget_energy_filled("actress_budget") else _("Done")]:
                tooltip scifi_movie.get_add_money_tooltip("actress_budget")
                style "scifi_movie_progress_bar_button"
                if scifi_movie.is_add_money_available("actress_budget"):
                    action [Function(scifi_movie.add_budget_energy, "actress_budget", scifi_movie.add_money_value), Function(spawn_text, f"+ ${scifi_movie.add_money_value}", 1100, 450, "fonts/mr-amazin-regular-type.otf")]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28)
            add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
            text _("ACTRESS BUDGET") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
        add "scifi_movie_lightning_3" xcenter (1100 if not sm1mv02s08i_done else 530) ypos 730
        fixed:
            xcenter (1385 if not sm1mv02s08i_done else 815)
            style_prefix "scifi_movie_progress_bars"
            add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
            vbar value AnimatedValue(value=outfit_energy_var, range=scifi_movie.total_outfit_energy, delay=1.0) style "scifi_movie_progress_vbar"
            textbutton [_(f"Add {scifi_movie.add_energy_value}E") if not scifi_movie.is_budget_energy_filled("outfit_energy") else _("Done")]:
                tooltip scifi_movie.get_add_energy_tooltip("outfit_energy")
                style "scifi_movie_progress_bar_button"
                if scifi_movie.is_add_energy_available("outfit_energy"):
                    action [Function(scifi_movie.add_budget_energy, "outfit_energy", scifi_movie.add_energy_value), Function(spawn_text, f"+ {scifi_movie.add_energy_value}E", 1385, 450, "fonts/mr-amazin-regular-type.otf")]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28)
            add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
            text _("OUTFIT DESIGN") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
        add "scifi_movie_lightning_4" xcenter (1385 if not sm1mv02s08i_done else 815) ypos 730
    if sm1mv02s08i_done:
        fixed:
            xcenter 1100
            style_prefix "scifi_movie_progress_bars"
            add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
            vbar value AnimatedValue(value=cgi_budget_var, range=scifi_movie.total_cgi_budget, delay=1.0) style "scifi_movie_progress_money_vbar"
            textbutton [_(f"Add ${scifi_movie.add_money_value}") if not scifi_movie.is_budget_energy_filled("cgi_budget") else _("Done")]:
                tooltip scifi_movie.get_add_money_tooltip("cgi_budget")
                style "scifi_movie_progress_bar_button"
                if scifi_movie.is_add_money_available("cgi_budget"):
                    action [Function(scifi_movie.add_budget_energy, "cgi_budget", scifi_movie.add_money_value), Function(spawn_text, f"+ ${scifi_movie.add_money_value}", 1100, 450, "fonts/mr-amazin-regular-type.otf")]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28)
            add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
            text _("CGI BUDGET") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
        add "scifi_movie_lightning_3" xcenter 1100 ypos 730
    if player.is_storyline_item_finished(MOVIE_SCIFI, "sm1mv02s09"):
        vbox:
            style_prefix "scifi_movie_final_progress_bar"
            fixed:
                add "images/ui/movie_progress/scifi_movie/movie_progress_editing_bar_frame.webp"
                vbar value AnimatedValue(value=editing_energy_var, range=scifi_movie.total_editing_energy, delay=1.0) xalign 0.5 yalign 0.5 style "scifi_movie_progress_vbar"
                add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 62
                text _("MOVIE EDITING") xalign 0.5 ycenter 62 style "scifi_movie_progress_bar_text"
            textbutton [_("Editing Work") if not scifi_movie.is_budget_energy_filled("editing_energy") else _("Done")]:
                tooltip scifi_movie.get_add_energy_tooltip("editing_energy")
                style "scifi_movie_progress_bar_button"
                if scifi_movie.is_add_energy_available("editing_energy"):
                    action [Function(scifi_movie.add_budget_energy, "editing_energy", scifi_movie.add_energy_value), Function(spawn_text, f"+ {scifi_movie.add_energy_value}E", 1750, 320, "fonts/mr-amazin-regular-type.otf")]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28)
    else:
        add "images/ui/movie_progress/scifi_movie/movie_progress_post_work_block.webp" xpos 1585 ypos 30
    add "images/ui/movie_progress/scifi_movie/scifi_movie_title_frame.webp" xalign 0.5 yanchor 0.5 ypos 65
    text _("SCIFI MOVIE") style "scifi_movie_title"
    use tooltip_screen
screen scifi_movie_progress_animation(from_phone=False):
    modal True
    zorder 351
    style_prefix "movie_progress"

    use scifi_movie_commons(from_phone=from_phone)
    fixed:
        xcenter 530
        at pirates_movie_bar_disapppear
        style_prefix "scifi_movie_progress_bars"
        add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
        vbar value 1 range 1 style "scifi_movie_progress_money_vbar"
        textbutton _("Done") action NullAction() background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28) style "scifi_movie_progress_bar_button"
        add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
        text _("SET BUDGET") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
    fixed:
        xcenter 815
        at pirates_movie_bar_disapppear
        style_prefix "scifi_movie_progress_bars"
        add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
        vbar value 1 range 1 style "scifi_movie_progress_vbar"
        textbutton _("Done") action NullAction() background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28) style "scifi_movie_progress_bar_button"
        add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
        text _("SET DESIGN") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
    fixed:
        xcenter 1100
        at pirates_movie_bar_move
        style_prefix "scifi_movie_progress_bars"
        add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
        vbar value 1 range 1 style "scifi_movie_progress_money_vbar"
        textbutton _("Done") action NullAction() background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28) style "scifi_movie_progress_bar_button"
        add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
        text _("ACTRESS BUDGET") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
    fixed:
        xcenter 1385
        at pirates_movie_bar_move
        style_prefix "scifi_movie_progress_bars"
        add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
        vbar value 1 range 1 style "scifi_movie_progress_vbar"
        textbutton _("Done") action NullAction() background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_insensitive.webp", 28, 28, 28, 28) style "scifi_movie_progress_bar_button"
        add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
        text _("OUTFIT DESIGN") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
    fixed:
        xcenter 1100
        at pirates_movie_bar_apppear
        style_prefix "scifi_movie_progress_bars"
        add "images/ui/movie_progress/scifi_movie/movie_progress_bar_frame.webp"
        vbar value 0 range 1 style "scifi_movie_progress_money_vbar"
        textbutton _(f"Add ${scifi_movie.add_money_value}") action NullAction() style "scifi_movie_progress_bar_button"
        add "images/ui/movie_progress/scifi_movie/scifi_movie_progress_name_frame.webp" xalign 0.5 ycenter 60
        text _("CGI BUDGET") xalign 0.5 ycenter 61 style "scifi_movie_progress_bar_text"
    add "images/ui/movie_progress/scifi_movie/movie_progress_post_work_block.webp" xpos 1585 ypos 30
    add "images/ui/movie_progress/scifi_movie/scifi_movie_title_frame.webp" xalign 0.5 yanchor 0.5 ypos 65
    text _("SCIFI MOVIE") style "scifi_movie_title"
    if from_phone:
        timer 2.0 action [Function(scifi_movie.set_animation_done), Show("scifi_movie_progress", from_phone=True), Hide()]
    else:
        timer 2.0 action [Function(scifi_movie.set_animation_done), Hide()]
style scifi_movie_progress_bars_fixed:
    ypos 130
    xsize 250
    ysize 618
style scifi_movie_progress_vbar:
    top_bar "images/ui/movie_progress/scifi_movie/scifi_movie_progress_bar_bottom.webp"
    bottom_bar "images/ui/movie_progress/scifi_movie/scifi_movie_progress_bar_front.webp"
    xalign 0.5
    ypos 575
    xsize 214
    ysize 556
style scifi_movie_progress_money_vbar is scifi_movie_progress_vbar bottom_bar "images/ui/movie_progress/scifi_movie/scifi_movie_progress_bar_front_money.webp"
style scifi_movie_progress_bar_button:
    xalign 0.5
    yalign 0.9
    idle_background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_idle.webp", 28, 28, 28, 28)
    hover_background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_work_hover.webp", 28, 28, 28, 28)
    xpadding 40
    ypadding 40
style scifi_movie_final_progress_bar_vbox:
    xalign 0.98
    yalign 0.12
    spacing 10
style scifi_movie_final_progress_bar_fixed xsize 261 ysize 602
style scifi_movie_final_progress_bar_text_button_text:
    font "fonts/mr-amazin-regular-type.otf"
    color "#000000"
    size 22
    yoffset 5
style scifi_movie_progress_bar_button_text:
    font "fonts/mr-amazin-regular-type.otf"
    color "#000000"
    size 22
    yoffset 5
style scifi_movie_progress_bar_text:
    font "fonts/mr-amazin-regular-type.otf"
    color "#FFFFFF"
    size 20
style scifi_movie_title:
    font "fonts/mr-amazin-regular-type.otf"
    color "#A2CCFE"
    size 80
    xalign 0.5
    yanchor 0.5
    ypos 70
style scifi_movie_progress_vbox spacing 50
style scifi_movie_progress_hbox:
    xalign 0.5
    yalign 0.95
    spacing 70
style scifi_movie_data_frame:
    background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_back_idle.webp", 28, 28, 28, 28)
    xpadding 35
    ypadding 35
    xanchor 0.5
    yanchor 0.5
    xpos 180
    ypos 955
style scifi_movie_back_button:
    xanchor 0.5
    yanchor 0.5
    xpos 1745
    ypos 955
    idle_background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_back_idle.webp", 28, 28, 28, 28)
    hover_background Frame("images/ui/movie_progress/scifi_movie/scifi_movie_back_hover.webp", 28, 28, 28, 28)
    xpadding 30
    top_padding 45
    bottom_padding 40
style scifi_movie_back_button_text:
    font "fonts/mr-amazin-regular-type.otf"
    color "#F0EAEC"
    size 45