screen difficulty_choice(jump_label):
    zorder 200
    style_prefix "difficulty_choice"

    default selected_points = None
    add "images/ui/difficulty/difficulty_choice_bg.webp"
    label _("GAME MODE")
    button:
        action [SetVariable("only_story_mode", False), Hide(), Jump(jump_label)]
        hovered SetScreenVariable("selected_points", 0)
        unhovered SetScreenVariable("selected_points", None)
        idle_background "difficulty_choice_1_idle"
        hover_background "difficulty_choice_1_hover"
        focus_mask True
        xpos 10
        yalign 0.4
        fixed:
            text _("Full Experience")
    button:
        action [SetVariable("only_story_mode", True ), Hide(), Jump(jump_label)]
        hovered SetScreenVariable("selected_points", 1)
        unhovered SetScreenVariable("selected_points", None)
        idle_background "difficulty_choice_2_idle"
        hover_background "difficulty_choice_2_hover"
        focus_mask True
        xpos 610
        yalign 0.4
        fixed:
            text _("No Minigames")
    button:
        action Jump("vn_mode_start")
        hovered SetScreenVariable("selected_points", 2)
        unhovered SetScreenVariable("selected_points", None)
        idle_background "difficulty_choice_3_idle"
        hover_background "difficulty_choice_3_hover"
        focus_mask True
        xpos 1220
        yalign 0.4
        fixed:
            text _("No Sandbox")
    use difficulty_choice_tooltip(selected_points)
screen difficulty_choice_tooltip(selected_points=None):
    style_prefix "difficulty_choice"

    default bullet_points = [
            ["Full story with exploration and player choice", "Sandbox-style free roaming", "Minigames and quests", "Character stats and progression"],
            ["Full story with exploration and player choice", "Sandbox-style free roaming", "Minigames are skipped or auto-resolved", "Quests and character progression"],
            ["Most of the story with player-driven progression", "No free roaming or open exploration", "Minigames and sandbox activities removed", "A streamlined experience focusing on narrative"]
        ]
    if selected_points is not None:
        $ display_bullet_points = bullet_points[selected_points]
        vbox:
            for point in display_bullet_points:
                text f" • {point}" style "difficulty_choice_bullet_text"
style difficulty_choice_label xalign 0.5 yalign 0.046
style difficulty_choice_label_text:
    font "fonts/sm-main.ttf"
    size 85
    color "#9f4664"
style difficulty_choice_button xsize 700 ysize 702
style difficulty_choice_text:
    font "fonts/sm-main.ttf"
    xalign 0.5
    size 55
    idle_color "#9f4664"
    hover_color "#ffffff"
    text_align 0.5
    line_spacing -5
style difficulty_choice_vbox:
    xalign 0.0
    xpos 600
    ypos 950
    spacing 10
style difficulty_choice_bullet_text xalign 0.0 size 32