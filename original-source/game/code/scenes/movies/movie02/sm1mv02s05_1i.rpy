label sm1mv02s05_1i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 d1s2_hmm noloop
    mc "Are we all set for filming the first scene?"
    play voice3 stacy_yes_simple1 noloop
    sy "Yes. Just need to light up the bat signal and summon everyone."
    sy "You sure Nari is ready for this?"
    mc "I think so, but we'll be there to help if she isn't."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "excited01") as lit_sy_excited01
    play voice3 stacy_yes_yeah1 noloop
    sy "Totally. I can't wait to start filming."
    play voice2 mc_yes_aga2 noloop
    mc "I'll text Nari and let her know we'll need to get into wardrobe as soon as she gets to the Photo Dojo."
    sy "Nice. Big day for our sexy coder girl."
    mc "Yes, it is."
    $ StoryController.end_scene(MOVIE_SCIFI)
    return