label sm1cs_tl008i:
    $ LocationController.draw_current_location("tl")
    play voice2 mc_hey_hey5 noloop
    mc "How are you settling in, Taisia?"
    tl "..."
    play voice2 mc_thinking_emm1 noloop
    mc "Taisia?"
    tl "..."
    play voice2 mc_hey_hey1 noloop
    mc "Taisia, hellllooooo?"
    tl "..."
    $ StoryController.end_scene(TL_STORY)
label sm1cs_tl008i_repeatable:
    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "smile01") as lth_tl_smile01
    play voice2 mc_happy_hah2 noloop
    mc "You really liked the video Stacy and I made, didn't you."
    hide lth_tl_smile01
    show expression cc.get_expression_image("tl", "excited01") as lth_tl_excited01
    play voice3 girl24_yes_simple2 noloop
    tl "It definitely turns me on."
    hide lth_tl_excited01
    show expression cc.get_expression_image("tl", "naughty01") as lth_tl_naughty01
    play voice3 girl24_thinking_mff noloop
    tl "At least it turns me on enough that I need to fuck my pussy."
    tl "You want to help me out?"
    menu:
        "Hell yes":
            hide lth_tl_naughty01
            show expression cc.get_expression_image("tl", "excited01") as lth_tl_excited01
            play voice2 mc_happy_yes1 noloop
            mc "Hell yeah I do!"
            play voice3 girl24_happy_yeah1 noloop
            if curr_position == SD_TAISIA:
                tl "Let's get started."
            else:
                tl "Let's go to my room."
            $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
            $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
            $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
            $ renpy.music.set_volume(1.0, 1.0, "music" )
            play music music_sexyfunkytime
            jump sm1cs_tl008_repeatable
        "Can't right now":
            play voice2 mc_thinking_emm1 noloop
            mc "I actually was just stopping in to say hi. I've got some things I need to do."
            hide lth_tl_naughty01
            show expression cc.get_expression_image("tl", "annoyed01") as lth_tl_annoyed01
            play voice3 girl24_disappointed_neh noloop
            tl "Whatever."
            return