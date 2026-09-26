screen pirates_movie_progress(from_phone=False):
    modal True
    zorder 350
    style_prefix "movie_progress"
    tag phone

    $ movie_progress_title = Text(_("PIRATES MOVIE"), font="fonts/consola.ttf", size=90, xalign=0.5)
    $ costume_budget_var = pirates_movie.get_curr_budget_energy("costume_budget")
    $ actress_budget_var = pirates_movie.get_curr_budget_energy("actress_budget")
    $ props_budget_var = pirates_movie.get_curr_budget_energy("props_budget")
    $ props_energy_var = pirates_movie.get_curr_budget_energy("props_energy")
    $ travel_budget_var = pirates_movie.get_curr_budget_energy("travel_budget")
    $ editing_energy_var = pirates_movie.get_curr_budget_energy("editing_energy")
    add "images/ui/movie_progress/pirates_movie/movie_progress_bg_langscape.webp" xalign 0.5
    add "images/ui/movie_progress/pirates_movie/movie_progress_bg.webp"
    vbox:
        for scene in pirates_movie.extra_scenes_list:
            fixed:
                if scene == "sm1mv01s03_2":
                    if player.get_choice("sm1mv01s03_2_tl_costume"):
                        add "images/ui/movie_progress/pirates_movie/scene_images/movie_progress_sm1mv01s03_2_image.webp"
                    else:
                        add "images/ui/movie_progress/pirates_movie/scene_images/movie_progress_sm1mv01s03_2_image_locked.webp"
                    add "images/ui/movie_progress/pirates_movie/movie_progress_character_frame.webp"
                    if player.get_choice("sm1mv01s03_2_tl_costume"):
                        add "images/ui/movie_progress/pirates_movie/movie_progress_done.webp" xalign 0.98 yalign 1.0
                else:
                    if player.has_played_scene(scene):
                        add f"images/ui/movie_progress/pirates_movie/scene_images/movie_progress_{scene}_image.webp"
                    else:
                        add f"images/ui/movie_progress/pirates_movie/scene_images/movie_progress_{scene}_image.webp" at black_n_white
                    add "images/ui/movie_progress/pirates_movie/movie_progress_character_frame.webp"
                    if player.has_played_scene(scene):
                        add "images/ui/movie_progress/pirates_movie/movie_progress_done.webp" xalign 0.98 yalign 1.0
    hbox:
        style_prefix "movie_progress_bars"
        fixed:
            vbar value AnimatedValue(value=costume_budget_var, range=pirates_movie.total_costume_budget, delay=1.0) style "movie_progress_money_vbar"
            add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
            textbutton [_(f"Add ${pirates_movie.add_money_value}") if pirates_movie.is_add_money_available("costume_budget") else _("Done")]:
                tooltip pirates_movie.get_add_money_tooltip("costume_budget")
                style "movie_progress_bar_button"
                if pirates_movie.is_add_money_available("costume_budget"):
                    action [Function(pirates_movie.add_budget_energy, "costume_budget", pirates_movie.add_money_value), Function(spawn_text, f"+ ${pirates_movie.add_money_value}", 540, 450)]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55)
            text _("Costume Budget") xalign 0.5 ypos 220 style "movie_progress_bar_button_text"
        fixed:
            vbar value AnimatedValue(value=actress_budget_var, range=pirates_movie.total_actress_budget, delay=1.0) style "movie_progress_money_vbar"
            add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
            textbutton [_(f"Add ${pirates_movie.add_money_value}") if pirates_movie.is_add_money_available("actress_budget") else _("Done")]:
                tooltip pirates_movie.get_add_money_tooltip("actress_budget")
                style "movie_progress_bar_button"
                if pirates_movie.is_add_money_available("actress_budget"):
                    action [Function(pirates_movie.add_budget_energy, "actress_budget", pirates_movie.add_money_value), Function(spawn_text, f"+ ${pirates_movie.add_money_value}", 845, 450)]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55)
            text _("Actress Budget") xalign 0.5 ypos 220 style "movie_progress_bar_button_text"
        if player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s04i"):
            fixed:
                vbar value AnimatedValue(value=props_budget_var, range=pirates_movie.total_props_budget, delay=1.0) style "movie_progress_vbar"
                add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
                textbutton _("Add $50") action Function(pirates_movie.add_budget_energy, "props_budget", 50) style "movie_progress_bar_button"
        if player.is_storyline_item_finished(MOVIE_PIRATES, "Q-MV01Q04_1"):
            fixed:
                vbar value AnimatedValue(value=props_energy_var, range=pirates_movie.total_props_energy, delay=1.0) style "movie_progress_vbar"
                add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
                textbutton _("+ 2") action Function(pirates_movie.add_budget_energy, "props_energy", 5) style "movie_progress_bar_button"
        if player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s06"):
            fixed:
                vbar value AnimatedValue(value=travel_budget_var, range=pirates_movie.total_travel_budget, delay=1.0) style "movie_progress_money_vbar"
                add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
                textbutton _("Add $50") action Function(pirates_movie.add_budget_energy, "travel_budget", 50) style "movie_progress_bar_button"
    hbox:
        for movie in pirates_movie.main_scenes_list:
            fixed:
                if player.is_storyline_item_finished(MOVIE_PIRATES, movie):
                    add f"images/ui/movie_progress/pirates_movie/scene_images/movie_progress_{movie}_image.webp"
                else:
                    add f"images/ui/movie_progress/pirates_movie/scene_images/movie_progress_{movie}_image.webp" at black_n_white
                add "images/ui/movie_progress/pirates_movie/movie_progress_scene_frame.webp"
                if player.is_storyline_item_finished(MOVIE_PIRATES, movie):
                    add "images/ui/movie_progress/pirates_movie/movie_progress_done.webp" xalign 0.9 yalign 0.9
    if player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s10"):
        vbox:
            style_prefix "movie_final_progress_bar"
            fixed:
                vbar value AnimatedValue(value=editing_energy_var, range=pirates_movie.total_editing_energy, delay=1.0) xalign 0.5 yalign 0.5 style "movie_progress_vbar"
                add "images/ui/movie_progress/pirates_movie/movie_progress_bar_frame.webp"
            textbutton _("Editing Work") action Function(pirates_movie.add_budget_energy, "editing_energy", 5) style "movie_progress_bar_button"
    else:
        add "images/ui/movie_progress/pirates_movie/movie_progress_post_work_block.webp" xpos 1570
    add "images/ui/movie_progress/pirates_movie/movie_progress_title_frame.webp" xalign 0.5 ycenter 65
    add AlphaMask("images/ui/renovation/renovation_label_gradient.webp", movie_progress_title) xalign 0.5 ycenter 62
    fixed:
        style_prefix "movie_progress_data"
        add "images/ui/movie_progress/pirates_movie/movie_progress_character_mask.webp" at zoom(0.8)
        add "images/ui/movie_progress/pirates_movie/movie_progress_character_frame.webp" at zoom(0.8)
        vbox:
            xpos 20
            yalign 0.5
            spacing 25
            style_prefix "phone_stats"
            hbox:
                add "images/ui/phone/phone_stats_money.webp"
                text "$[player.money]"
            hbox:
                add "images/ui/phone/phone_stats_energy.webp"
                text "[player.energy]/[player.max_energy]"
    textbutton _("BACK"):
        keysym "game_menu"
        style "movie_progress_back_button"
        if from_phone:
            action Hide()
        else:
            action Return()
    use tooltip_screen
transform zoom(zoom_value):
    zoom zoom_value
style movie_progress_vbox:
    xpos 50
    ypos 25
    spacing 12
style movie_progress_hbox:
    xalign 0.5
    yalign 0.98
    spacing 40
style movie_progress_bars_hbox:
    xpos 420
    ysize 808
    spacing 50
style movie_progress_bars_fixed xsize 250 ysize 740
style movie_progress_vbar:
    top_bar "images/ui/movie_progress/pirates_movie/movie_progress_bar_bottom.webp"
    bottom_bar "images/ui/movie_progress/pirates_movie/movie_progress_bar_front.webp"
    xalign 0.5
    yanchor 1.0
    ypos 717
    xsize 204
    ysize 545
style movie_progress_money_vbar is movie_progress_vbar bottom_bar "images/ui/movie_progress/pirates_movie/movie_progress_bar_front_money.webp"
style movie_progress_bar_button:
    xalign 0.5
    yalign 0.92
    idle_background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_idle.webp", 70, 55, 70, 55)
    hover_background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_hover.webp", 70, 55, 70, 55)
    xpadding 55
    ypadding 45
style movie_progress_bar_button_text color "#FFFFFF" size 20
style movie_progress_fixed fit_first True
style movie_final_progress_bar_vbox:
    xalign 0.98
    yalign 0.12
    spacing 10
style movie_final_progress_bar_fixed xsize 250 ysize 592
style movie_progress_data_fixed:
    fit_first True
    xpos 60
    yalign 0.97
style movie_progress_back_button:
    xalign 0.99
    yalign 0.95
    idle_background Frame("images/ui/movie_progress/pirates_movie/movie_progress_back_idle.webp", 20, 42, 20, 42)
    hover_background Frame("images/ui/movie_progress/pirates_movie/movie_progress_back_hover.webp", 20, 42, 20, 42)
    xpadding 30
    ypadding 40
style movie_progress_back_button_text:
    font "fonts/viga-regular.ttf"
    color "#f1e9eb"
    size 40