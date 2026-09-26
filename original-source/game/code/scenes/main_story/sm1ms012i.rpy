label sm1ms012i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_hey noloop
    sy "[mcname!u]!"
    play voice2 mc_angry_errr2 noloop
    mc "What? Jesus, you don't need to yell."
    sy "It's done!"
    mc "What's done?"
    hide lst_sy_excited1
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice3 stacy_happy_wooh1 noloop
    sy "The film! It's done!"
    play voice2 mc_thinking_wait1 noloop
    mc "Wait - really?"
    sy "Come here to the table! Let's watch it on my laptop!"
    $ StoryController.end_scene(MS)
    return