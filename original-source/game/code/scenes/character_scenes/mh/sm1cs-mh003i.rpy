label sm1cs_mh003i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice2 d2s9_mchey noloop
    mc "Hey, you heard anything from Lyssa?"
    hide lst_sy_naughty1
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    play voice3 stacy_no_simple1 noloop
    sy "No. I figured she'd text you first."
    play voice2 mc_thinking_hmm5 noloop
    mc "I know, but I haven't heard anything yet and so-"
    call buzz from _call_buzz_4
    $ StoryController.end_scene(MH_STORY)
    return