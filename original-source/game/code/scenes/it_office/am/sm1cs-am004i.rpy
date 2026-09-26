label sm1cs_am004i:
    $ LocationController.draw_current_location("am")
    show expression cc.get_expression_image("am", "curious01") as lst_am_curious01
    play voice2 d2s9_mchey noloop volume 1.4
    mc "Hey, April."
    play voice3 girl22_yes_questioning noloop
    am "Yes?"
    mc "That concert you invited to, it's tonight, right?"
    hide lst_am_curious01
    show expression cc.get_expression_image("am", "ask01") as lst_am_ask01
    play voice3 girl22_surprised_oh noloop
    am "Huh? Oh yeah. I thought you might have forgotten about that."
    play voice2 mc_no_nope1 noloop volume 1.5
    mc "Nope."
    am "So you're for sure coming?"
    menu:
        "Of course I am"(hint="sm1cs_am004i_m01_h01"):
            play voice2 mc_yes_yes7 noloop
            mc "Yes, of course, I'm coming. I'm excited to see you rock out."
            hide lst_am_ask01
            show expression cc.get_expression_image("am", "naughty01") as naughty01
            play voice3 girl22_arrogant_he noloop
            am "Well, don't forget, it's pagon rock. I don't want to hear you whining later."
            play voice2 mc_yes_sure1 noloop
            mc "Woudln't dream of it. See you tonight."
            am "Later."
            jump sm1cs_am004i_end
        "On second thought, I have something I need to do"(hint="sm1cs_am004i_m01_h02"):
            play voice2 mc_pain_ou1 noloop
            mc "Oh shit. I actually have something going on tonight."
            hide lst_am_ask01
            show expression cc.get_expression_image("am", "angry01") as lst_am_angry01
            play voice3 girl22_arrogant_pff noloop
            am "Whatever. If you don't want to come, just say that."
            am "Bye."
            jump sm1cs_am004i_return
label sm1cs_am004i_end:
    $ StoryController.end_scene(AM_STORY)
    return
label sm1cs_am004i_return:
    $ StoryController.end_scene_without_progressing(AM_STORY, 0, 15, 0)
    return