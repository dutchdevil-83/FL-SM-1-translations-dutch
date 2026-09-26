label sm1cs_bg002i:
    $ LocationController.draw_current_location("bg")
    show expression cc.get_expression_image("bg", "smile01") as lpd_bg_smile
    play voice3 girl26_hey_greeting noloop
    bg "Oh, hey [mcname]. Kanya was looking for you."
    play voice2 mc_surprised_why3 noloop
    mc "Why was she looking for me?"
    hide lpd_bg_smile
    show expression cc.get_expression_image("bg", "neutral01") as lpd_bg_neutral
    play voice3 girl26_thinking_ehh2 noloop
    bg "I don't know. She said she had something to talk to us about."
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Huh... that's kind of weird right?"
    bg "Oh - there she is. You can ask her yourself."
    hide lpd_bg_neutral
    $ StoryController.end_scene(BG_STORY)
    return