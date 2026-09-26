label sm1mv01s02i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral02") as lst_sy_neutral02
    play voice2 mc_happy_yay2 noloop
    mc "Hey, let's go get the costumes."
    play voice3 stacy_yes_yap1 noloop
    sy "Sure, I'm free."
    hide lst_sy_neutral02
    show expression cc.get_expression_image("sy", "smile02") as lst_sy_smile02
    play voice2 mc_thinking_hm noloop
    mc "I'll text Kanya. Would be good to have her eye on these."
    play voice3 stacy_yes_okay1 noloop
    sy "Good thinking."
    play sound sfx_message_in1
    mc "She says she'll meet us at the shop."
    hide lst_sy_smile02
    show expression cc.get_expression_image("sy", "angry01") as lst_syangry01
    play voice3 stacy_angry_argh5 noloop
    sy "Avast mi hearties. Their's raiding to be done!"
    sy "Forward!{w}To the foul and rum-stenched land known as our local sexshop."
    hide lst_syangry01
    show expression cc.get_expression_image("sy", "laugh01")
    play voice2 mc_happy_yes1 noloop
    mc "Aye, Captain!"
    play voice3 stacy_happy_laugh4 noloop
    sy "*giggles*"
    jump sm1mv01s02