label sm1cs_tl006i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral02") as lst_sy_neutral02
    play voice2 d2s9_mchey noloop
    mc "So there's something I want to talk to you about."
    hide lst_sy_neutral02
    show expression cc.get_expression_image("sy", "curious01") as lst_sy_curious01
    play voice3 stacy_thinking_oh1 noloop
    sy "Oh? What's up?"
    play voice2 d1s5_mcthinks noloop
    mc "I was talking to Taisia the other day, and-"
    hide lst_sy_curious01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_surprised_huh4 noloop
    sy "We're filming another movie with her!?"
    play voice2 mc_surprised_what2 noloop
    mc "What? No- I mean, yes, at some point, but that's not what I wanted to talk to you about."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "sad01") as lst_sy_sad01
    play voice3 stacy_disappointed_oh2 noloop
    sy "Oh... well, what is it?"
    play voice2 mc_thinking_mmm5 noloop
    mc "Taisia is looking for a place to live, and-"
    hide lst_sy_sad01
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_yes noloop
    sy "YES!"
    play voice2 d2s9_confused noloop volume 1.7
    mc "I didn't-"
    sy "I don't care, yes! She can live here!"
    mc "We should-"
    hide lst_sy_excited01
    show expression cc.get_expression_image("sy", "annoyed01") as lst_sy_annoyed01
    play voice3 stacy_angry_aah1 noloop
    sy "Shut up, let's just make it happen!"
    play voice2 mc_yes_okay2 noloop
    mc "All right, next chance we get we can go and talk to her."
    hide lst_sy_annoyed01
    show expression cc.get_expression_image("sy", "excited01") as lst_sy_excited01
    play voice3 stacy_happy_yay3 noloop
    sy "YAAAYYYYY!"
    $ StoryController.end_scene(TL_STORY, 0, 10, 0)
    return