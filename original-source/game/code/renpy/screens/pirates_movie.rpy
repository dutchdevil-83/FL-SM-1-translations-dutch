screen pirates_movie_commons(from_phone=False):
    style_prefix "movie_progress"

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
        for movie in pirates_movie.main_scenes_list:
            fixed:
                if player.is_storyline_item_finished(MOVIE_PIRATES, movie):
                    add f"images/ui/movie_progress/pirates_movie/scene_images/movie_progress_{movie}_image.webp"
                else:
                    add f"images/ui/movie_progress/pirates_movie/scene_images/movie_progress_{movie}_image.webp" at black_n_white
                add "images/ui/movie_progress/pirates_movie/movie_progress_scene_frame.webp"
                if player.is_storyline_item_finished(MOVIE_PIRATES, movie):
                    add "images/ui/movie_progress/pirates_movie/movie_progress_done.webp" xalign 0.9 yalign 0.95
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
    $ sm1mv01s07_done = player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s07")
    if not pirates_movie.sm1mv01s06_animation_done and sm1mv01s07_done:
        if from_phone:
            on "replace" action Show("pirates_movie_progress_animation", from_phone=True)
        else:
            on "show" action Show("pirates_movie_progress_animation")
    use pirates_movie_commons(from_phone=from_phone)
    if not sm1mv01s07_done:
        fixed:
            xcenter 530
            style_prefix "movie_progress_bars"
            vbar value AnimatedValue(value=costume_budget_var, range=pirates_movie.total_costume_budget, delay=1.0) style "movie_progress_money_vbar"
            add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
            textbutton [_(f"Add ${pirates_movie.add_money_value}") if not pirates_movie.is_budget_energy_filled("costume_budget") else _("Done")]:
                tooltip pirates_movie.get_add_money_tooltip("costume_budget")
                style "movie_progress_bar_button"
                if pirates_movie.is_add_money_available("costume_budget"):
                    action [Function(pirates_movie.add_budget_energy, "costume_budget", pirates_movie.add_money_value), Function(spawn_text, f"+ ${pirates_movie.add_money_value}", 530, 450)]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55)
            add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
            text _("COSTUME BUDGET") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
        fixed:
            xcenter 815
            style_prefix "movie_progress_bars"
            vbar value AnimatedValue(value=actress_budget_var, range=pirates_movie.total_actress_budget, delay=1.0) style "movie_progress_money_vbar"
            add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
            textbutton [_(f"Add ${pirates_movie.add_money_value}") if not pirates_movie.is_budget_energy_filled("actress_budget") else _("Done")]:
                tooltip pirates_movie.get_add_money_tooltip("actress_budget")
                style "movie_progress_bar_button"
                if pirates_movie.is_add_money_available("actress_budget"):
                    action [Function(pirates_movie.add_budget_energy, "actress_budget", pirates_movie.add_money_value), Function(spawn_text, f"+ ${pirates_movie.add_money_value}", 815, 450)]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55)
            add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
            text _("ACTRESS BUDGET") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
    if player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s04i"):
        fixed:
            xcenter (1100 if not sm1mv01s07_done else 530)
            style_prefix "movie_progress_bars"
            vbar value AnimatedValue(value=props_budget_var, range=pirates_movie.total_props_budget, delay=1.0) style "movie_progress_money_vbar"
            add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
            textbutton [_(f"Add ${pirates_movie.add_money_value}") if not pirates_movie.is_budget_energy_filled("props_budget") else _("Done")]:
                tooltip pirates_movie.get_add_money_tooltip("props_budget")
                style "movie_progress_bar_button"
                if pirates_movie.is_add_money_available("props_budget"):
                    action [Function(pirates_movie.add_budget_energy, "props_budget", pirates_movie.add_money_value), Function(spawn_text, f"+ ${pirates_movie.add_money_value}", 1100, 450)]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55)
            add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
            text _("PROPS BUDGET") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
    if player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s04i"):
        fixed:
            xcenter (1385 if not sm1mv01s07_done else 815)
            style_prefix "movie_progress_bars"
            vbar value AnimatedValue(value=props_energy_var, range=pirates_movie.total_props_energy, delay=1.0) style "movie_progress_vbar"
            add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
            textbutton [_(f"Add {pirates_movie.add_energy_value}E") if not pirates_movie.is_budget_energy_filled("props_energy") else _("Done")]:
                tooltip pirates_movie.get_add_energy_tooltip("props_energy")
                style "movie_progress_bar_button"
                if pirates_movie.is_add_energy_available("props_energy"):
                    action [Function(pirates_movie.add_budget_energy, "props_energy", pirates_movie.add_energy_value), Function(spawn_text, f"+ {pirates_movie.add_energy_value}", 1385, 450)]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55)
            add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
            text _("BUILD PROPS") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
    if sm1mv01s07_done:
        fixed:
            xcenter 1100
            style_prefix "movie_progress_bars"
            vbar value AnimatedValue(value=travel_budget_var, range=pirates_movie.total_travel_budget, delay=1.0) style "movie_progress_money_vbar"
            add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
            textbutton [_(f"Add ${pirates_movie.add_money_value}") if not pirates_movie.is_budget_energy_filled("travel_budget") else _("Done")]:
                tooltip pirates_movie.get_add_money_tooltip("travel_budget")
                style "movie_progress_bar_button"
                if pirates_movie.is_add_money_available("travel_budget"):
                    action [Function(pirates_movie.add_budget_energy, "travel_budget", pirates_movie.add_money_value), Function(spawn_text, f"+ ${pirates_movie.add_money_value}", 1100, 450)]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55)
            add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
            text _("TRAVEL BUDGET") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
    if player.is_storyline_item_finished(MOVIE_PIRATES, "sm1mv01s10"):
        vbox:
            style_prefix "movie_final_progress_bar"
            fixed:
                vbar value AnimatedValue(value=editing_energy_var, range=pirates_movie.total_editing_energy, delay=1.0) xalign 0.5 yalign 0.5 style "movie_progress_vbar"
                add "images/ui/movie_progress/pirates_movie/movie_progress_bar_frame.webp"
                add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 62
                text _("MOVIE EDITING") xalign 0.5 ycenter 65 style "movie_progress_bar_text"
            textbutton [_("Editing Work") if not pirates_movie.is_budget_energy_filled("editing_energy") else _("Done")]:
                tooltip pirates_movie.get_add_energy_tooltip("editing_energy")
                style "movie_progress_bar_button"
                if pirates_movie.is_add_energy_available("editing_energy"):
                    action [Function(pirates_movie.add_budget_energy, "editing_energy", pirates_movie.add_energy_value), Function(spawn_text, f"+ {pirates_movie.add_energy_value}", 1750, 320)]
                else:
                    action NullAction()
                    background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55)
    else:
        add "images/ui/movie_progress/pirates_movie/movie_progress_post_work_block.webp" xpos 1570
    add "images/ui/movie_progress/pirates_movie/movie_progress_title_frame.webp" xalign 0.5 ycenter 65
    add AlphaMask("images/ui/renovation/renovation_label_gradient.webp", movie_progress_title) xalign 0.5 ycenter 62
    use tooltip_screen
screen pirates_movie_progress_animation(from_phone=False):
    modal True
    zorder 351
    style_prefix "movie_progress"

    $ movie_progress_title = Text(_("PIRATES MOVIE"), font="fonts/consola.ttf", size=90, xalign=0.5)
    use pirates_movie_commons(from_phone=from_phone)
    fixed:
        xcenter 530
        at pirates_movie_bar_disapppear
        style_prefix "movie_progress_bars"
        vbar value 1 range 1 style "movie_progress_money_vbar"
        add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
        textbutton _("Done") action NullAction() background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55) style "movie_progress_bar_button"
        add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
        text _("COSTUME BUDGET") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
    fixed:
        xcenter 815
        at pirates_movie_bar_disapppear
        style_prefix "movie_progress_bars"
        vbar value 1 range 1 style "movie_progress_money_vbar"
        add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
        textbutton _("Done") action NullAction() background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55) style "movie_progress_bar_button"
        add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
        text _("ACTRESS BUDGET") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
    fixed:
        xcenter 1100
        at pirates_movie_bar_move
        style_prefix "movie_progress_bars"
        vbar value 1 range 1 style "movie_progress_money_vbar"
        add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
        textbutton _("Done") action NullAction() background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55) style "movie_progress_bar_button"
        add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
        text _("PROPS BUDGET") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
    fixed:
        xcenter 1385
        at pirates_movie_bar_move
        style_prefix "movie_progress_bars"
        vbar value 1 range 1 style "movie_progress_vbar"
        add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
        textbutton _("Done") action NullAction() background Frame("images/ui/movie_progress/pirates_movie/movie_progress_work_insensitive.webp", 70, 55, 70, 55) style "movie_progress_bar_button"
        add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
        text _("BUILD PROPS") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
    fixed:
        xcenter 1100
        at pirates_movie_bar_apppear
        style_prefix "movie_progress_bars"
        vbar value 0 range 1 style "movie_progress_money_vbar"
        add "images/ui/movie_progress/pirates_movie/movie_progress_bar_chain_frame.webp"
        textbutton _(f"Add ${pirates_movie.add_money_value}") action NullAction() style "movie_progress_bar_button"
        add "images/ui/movie_progress/pirates_movie/movie_progress_name_frame.webp" xalign 0.5 ycenter 210
        text _("TRAVEL BUDGET") xalign 0.5 ycenter 207 style "movie_progress_bar_text"
    add "images/ui/movie_progress/pirates_movie/movie_progress_post_work_block.webp" xpos 1570
    add "images/ui/movie_progress/pirates_movie/movie_progress_title_frame.webp" xalign 0.5 ycenter 65
    add AlphaMask("images/ui/renovation/renovation_label_gradient.webp", movie_progress_title) xalign 0.5 ycenter 62
    if from_phone:
        timer 2.0 action [Function(pirates_movie.set_sm1mv01s06_animation_done), Show("pirates_movie_progress", from_phone=True), Hide()]
    else:
        timer 2.0 action [Function(pirates_movie.set_sm1mv01s06_animation_done), Hide()]
transform pirates_movie_bar_disapppear:
    pause 0.5
    easeout 0.5 yoffset -1000
transform pirates_movie_bar_move:
    pause 1.0
    easein 0.5 xoffset -570
transform pirates_movie_bar_apppear:
    yoffset -1000
    pause 1.5
    easein 0.5 yoffset 0
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
style movie_progress_bars_fixed:
    xpos 420
    xsize 250
    ysize 740
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
style movie_progress_bar_text:
    font "fonts/barlow-condensed-semi-bold.ttf"
    color "#FFFFFF"
    size 26
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