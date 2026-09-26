label sm1cs_tl_renovation_i:
    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "smile01") as lth_tl_smile01
    play voice3 girl24_thinking_emm1 noloop
    tl "So, [mcname], when can I move in?"
    if player.get_choice("sm1ms_renovation_started"):
        play voice2 mc_thinking_hmm1 noloop
        mc "Well, you see..."
    else:
        play voice2 mc_thinking_hmm1 noloop
        mc "Well, we haven't started fixing up the studio yet, but as soon as we do, I'll let you know."
        tl "Tick, tock, [mcname]."
    jump sm1cs_tl_renovation