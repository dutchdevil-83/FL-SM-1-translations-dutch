screen topics_screen():
    tag menu

    default topic_number = 0
    add "images/ui/topics/topics_bg.webp"
    label _("TOPICS") style "difficulty_choice_label"
    grid 2 9:
        style_prefix "topic_names"
        for topic in ALL_TOPICS:
            $ style_name = "odd" if (topic_number % 2 == 1) else "even"
            $ topic_number += 1
            frame:
                style_prefix "topic_name_" + style_name
                text topic
    grid 2 9:
        style_prefix "topic_icons"
        $ topic_prefix = TOPIC.lower()
        for topic in ALL_TOPICS:
            $ topic_suffix = topic.lower().replace(" ", "_")
            frame:
                add topic_prefix + "_" + topic_suffix xalign 0.5 yalign 0.5
    grid 2 9:
        style_prefix "topic_points"
        for topic in ALL_TOPICS:
            frame:
                text str(player.get_topic(topic))
    imagebutton auto "back_%s" focus_mask True xalign 0.99 yalign 0.985 action Return()
style topic_names_grid:
    xalign 0.5
    yalign 0.8
    xspacing 250
    yspacing 10
style topic_name_even_frame:
    right_padding 200
    xalign 1.0
    ysize 86
    background Frame("images/ui/topics/topic_name_even_bg.webp", 0, 0, 175, 0)
style topic_name_odd_frame:
    left_padding 200
    xalign 0.0
    ysize 86
    background Frame("images/ui/topics/topic_name_odd_bg.webp", 175, 0, 0, 0)
style topic_name_even_text:
    yalign 0.5
    size 48
    color "#96c6ea"
style topic_name_odd_text:
    yalign 0.5
    size 48
    color "#96c6ea"
style topic_icons_grid:
    xalign 0.5
    yalign 0.8
    xspacing 420
    yspacing 10
style topic_icons_frame:
    xsize 86
    ysize 86
    background None
style topic_points_grid:
    xalign 0.5
    yalign 0.8
    xspacing 250
    yspacing 10
style topic_points_frame:
    xsize 86
    ysize 86
    background None
style topic_points_text:
    xalign 0.5
    yalign 0.6
    size 48
    color "#d4eaff"