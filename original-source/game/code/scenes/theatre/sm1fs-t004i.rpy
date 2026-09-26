label sm1fs_t004i:
    $ LocationController.draw_current_location("dvh")
    show expression cc.get_expression_image("dvh", "serious01") as lth_dvh_serious01
    play voice2 mc_hey_hey7 noloop
    mc "Hey, Denise-"
    play voice3 girl34_disappointed_oh1 noloop
    dvh "Oh good, you're here."
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Huh?"
    play voice3 girl34_disappointed_mmf1 noloop
    dvh "Get on the stage."
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    hide lth_dvh_serious01
    show expression cc.get_expression_image("dvh", "annoyed01") as lth_dvh_annoyed01
    play voice3 girl34_angry_argh1 noloop
    dvh "We are all meeting on the stage. Go."
    jump sm1fs_t004i_end
label sm1fs_t004i_end:
    $ StoryController.end_scene(THEATER_STORY_LINE)
    return