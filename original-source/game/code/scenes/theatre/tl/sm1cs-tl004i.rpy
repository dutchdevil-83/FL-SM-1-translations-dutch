label sm1cs_tl004i:
    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "ask01") as lth_tl_ask01
    play voice2 mc_hey_hey5 noloop
    mc "Hey, Taisia."
    play voice3 girl24_thinking_ah noloop
    tl "Oh, hey [mcname]."
    mc "How are you?"
    hide lth_tl_ask01
    show expression cc.get_expression_image("tl", "curious01") as lth_tl_curious01
    play voice3 girl24_disappointed_eeh1 noloop
    tl "I'm... fine."
    tl "I was wondering, you wanna go get a beer or something?"
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    hide lth_tl_curious01
    show expression cc.get_expression_image("tl", "annoyed01") as lth_tl_annoyed01
    play voice3 girl24_angry_cough2 noloop
    tl "I'm asking a guy I work with if he wants to get a beer. What's so weird about that?"
    play voice2 d2s12_emmm noloop volume 1.5
    mc "Uhm, nothing-"
    hide lth_tl_annoyed01
    show expression cc.get_expression_image("tl", "smile01")
    play voice3 girl24_yes_ugu noloop
    tl "Good, then come on."
    $ StoryController.end_scene(TL_STORY)
    return