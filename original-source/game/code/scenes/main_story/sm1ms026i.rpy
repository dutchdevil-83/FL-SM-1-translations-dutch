label sm1ms026i:
    $ LocationController.draw_current_location("sy")
    if not player.get_choice("sm1ms026_second_movie"):
        show expression cc.get_expression_image("sy", "neutral02") as sy_neutral02
        play voice3 stacy_yes_simple1 noloop
        sy "Yes?"
        play voice2 mc_thinking_hmm2 noloop
        mc "All right, what do we need to do to start making our first movie?"
        hide sy_neutral02
        show expression cc.get_expression_image("sy", "excited01")
        play voice3 stacy_yay noloop
        sy "Yay! It's happening!"
        sy "Let's go talk on the couch!"
    else:
        show expression cc.get_expression_image("sy", "neutral02") as sy_neutral02
        play voice3 stacy_hey_happy2 noloop
        sy "Yo'."
        play voice2 mc_thinking_hmm2 noloop
        mc "I think we should plan out the other movie."
        hide sy_neutral02
        show expression cc.get_expression_image("sy", "excited01")
        play voice3 stacy_yes noloop
        sy "Yes! To the coooouch!"
    $ StoryController.end_scene(MS)
    return
label sm1ms026_2i:
    $ player.set_choice("sm1ms026_second_movie")
    jump sm1ms026i