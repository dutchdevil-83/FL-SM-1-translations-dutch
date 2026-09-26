label sm1ms005_02i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    play voice3 stacy_hey noloop
    sy "Hey, [mcname], coming to bed?"
    play voice2 mc_yes_yeah2 noloop
    mc "Yep! Long day, and could use some rest."
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "smile2") as lst_sy_smile2
    play voice3 stacy_arrogant_huh2 noloop
    sy "How about a little pre-bed sex?"
    menu:
        "Have sex with Stacy"(hint="sm1ms005_02i_m01_h01"):
            play voice2 mc_thinking_mmm2 noloop
            mc "I could go for a little sexy time right now."
            hide lst_sy_smile2
            show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
            play voice3 stacy_happy_relief1 noloop
            sy "Are you feeling adventurous tonight? Or are you feeling like some love-making?"
        "Go to sleep"(hint="sm1ms005_02i_m01_h02"):
            play voice2 mc_disappointed_ah2 noloop
            mc "I'm beat... I think I'm just going to pass out."
            hide lst_sy_smile2
            show expression cc.get_expression_image("sy", "sad1") as lst_sy_sad1
            play voice3 stacy_disappointed_oh1 noloop
            sy "Okay..."
            return
    menu:
        "Adventurous Sex"(hint="sm1ms005_02i_m02_h01"):
            $ sm1ms005_adventure_sex = True
            play voice2 mc_happy_hah2 noloop
            mc "Let's have a little bedroom expedition!"
        "Love Making"(hint="sm1ms005_02i_m02_h02"):
            $ sm1ms005_adventure_sex = False
            play voice2 mc_thinking_mmm5 noloop
            mc "I think we slow it down and have some of that romantic passion."
    play voice3 stacy_yes_yap1 noloop
    sy "Alright. Lets do it."
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_cherry_pop
    jump sm1ms005_repeatable