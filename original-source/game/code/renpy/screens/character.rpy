screen character_screen(character_codename):
    style_prefix "character_screen"
    tag menu

    default character = CharacterController.get_character(character_codename)
    default all_traits = CharacterController.get_character(character_codename).get_traits()
    default traits = [trait for trait in all_traits if sm_indexed_traits_list[trait][TYPE] == TYPE_PHYSIC]
    default fetishes = [trait for trait in all_traits if sm_indexed_traits_list[trait][TYPE] == TYPE_FETISH]
    default topics = CharacterController.get_character(character_codename).get_topics()
    default storyline = CharacterController.get_character(character_codename).storyline
    default storyline_progress_percent = player.get_storyline_progress_percent(storyline)
    default charcater_image = character.char_image
    if character.faction:
        add "images/ui/character/character_" + character.faction + "_bg.webp"
        imagebutton auto "images/ui/phone/phone_" + character.faction + "_%s.webp" focus_mask True action ShowMenu(character.faction) xalign 0.995 yalign 0.015
    else:
        add "images/ui/character/character_neutral_bg.webp"
    add charcater_image yalign 1.0
    label character.full_name
    if not vn_mode:
        frame:
            style_prefix "character_point"
            imagebutton idle "images/ui/character/relation_point_frame.webp" xalign 0.5 focus_mask True action NullAction() tooltip _("Relationship Points")
            text ("∞" if character_codename == "sy" else str(character.points)) xalign 0.5 yalign 0.62 size (90 if character_codename == "sy" else 63)
    if topics:
        vbox:
            style_prefix "character_topics"
            text _("Topics") xalign 0.5
            for topic in topics:
                frame:
                    background Frame("images/utilities/topic_frames/topic_" + topic.lower().replace(" ", "_") + "_frame.webp", 60, 10, 12, 10)
                    text topic xalign 0.5
    if traits:
        vbox:
            style_prefix "character_traits"
            text _("Traits") xalign 0.5
            for trait in traits:
                frame:
                    text sm_indexed_traits_list[trait][NAME] xalign 0.5
    if fetishes:
        vbox:
            style_prefix "character_fetishes"
            text _("Fetishes") xalign 0.5
            for fetish in fetishes:
                frame:
                    background Frame("images/utilities/fetish_frames/fetish_" + fetish + "_frame.webp", 12, 10, 60, 10)
                    text sm_indexed_traits_list[fetish][NAME] xalign 0.5
    if storyline:
        text _("Progress ") + str(storyline_progress_percent) + "%"
        bar value storyline_progress_percent range 100 style "character_progress_bar"
    use tooltip_screen
    imagebutton auto "back_%s" xalign 0.93 yalign 0.985 focus_mask True action ShowMenu(character.faction)
    imagebutton auto "close_%s" xalign 0.99 yalign 0.985 focus_mask True action Return()
style character_screen_label xcenter 1267 yalign 0.07
style character_screen_label_text size 100 color "#eff2fc"
style character_point_frame:
    background None
    xsize 180
    ysize 118
    xcenter 1267
    yalign 0.2
style character_point_text color "#ffeaf2"
style character_topics_vbox:
    xsize 305
    spacing 20
    xcenter 942
    ypos 370
style character_topics_frame:
    xsize 305
    left_padding 62
    top_padding 15
    right_padding 20
    bottom_padding 15
style character_topics_text size 25
style character_traits_vbox:
    xsize 305
    spacing 20
    xcenter 1267
    ypos 370
style character_traits_frame:
    background Frame("images/ui/character/character_traits_frame.webp", 12, 12, 12, 12)
    xsize 305
    left_padding 12
    top_padding 15
    right_padding 12
    bottom_padding 15
style character_traits_text size 25
style character_fetishes_vbox:
    xsize 305
    spacing 20
    xcenter 1593
    ypos 370
style character_fetishes_frame:
    xsize 305
    left_padding 20
    top_padding 15
    right_padding 62
    bottom_padding 15
style character_fetishes_text size 25
style character_screen_text:
    xcenter 1267
    yalign 0.9
    size 50
    color "#f8828d"
style character_progress_bar:
    right_bar Frame("images/ui/factions/it_faction_bar_frame.webp", 6, 6, 6, 6)
    left_bar Frame("images/ui/factions/it_faction_bar.webp", 6, 6, 6, 6)
    xcenter 1267
    yalign 0.95
    xsize 800
    ysize 25