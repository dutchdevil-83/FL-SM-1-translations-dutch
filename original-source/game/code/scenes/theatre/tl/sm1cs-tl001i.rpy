label sm1cs_tl001i:
    $ LocationController.draw_current_location("tl")
    show expression cc.get_expression_image("tl", "excited01") as lth_tl_excited01
    play voice2 mc_hey_hey3 noloop
    mc "Hey, Taisia. I wanted to talk to you-"
    play voice3 girl24_surprised_huh4 noloop
    tl "Are you telling me I'm a part of the team?"
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah! That you are."
    play voice3 girl24_happy_yeah3 noloop
    tl "Hell yeah! So when are we filming our first porn?"
    hide lth_tl_excited01
    show expression cc.get_expression_image("tl", "naughty01")
    play voice2 d2s9_confused noloop volume 1.6
    mc "Woah, uh, maybe we shouldn't talk about this {i}here{/i}."
    play voice3 girl24_arrogant_hm2 noloop
    tl "Fucking whatever."
    mc "But if you have some time, we can go to the studio and talk some more about it?"
    tl "Lead the way, leading man."
    $ StoryController.end_scene(TL_STORY)
    return