label sm1mv01s11i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_happy_oof3 noloop
    mc "So is it finally done. My eyes need a break."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    play voice3 stacy_laugh4 noloop
    sy "Ah... it is a lot of hard work isn't it."
    play voice2 mc_yes_yeah9 noloop
    mc "I had no idea."
    sy "To answer your question. Yes, the post-editing for the Pirate movie is complete."
    sy "Thanks for all your help, [mcname]."
    hide lst_sy_laugh01
    show expression cc.get_expression_image("sy", "neutral02") as lst_sy_neutral02
    play voice2 mc_hey_hey9 noloop
    mc "Hey I just followed your lead."
    play voice3 stacy_happy_laugh2 noloop
    sy "Hehe."
    hide lst_sy_neutral02
    show expression cc.get_expression_image("sy", "laugh01") as lst_sy_laugh01
    if player.get_choice("first_movie") == "pirates_movie":
        play voice3 stacy_disappointed_mmm1 noloop
        sy "And this is great."
        sy "Now that all the editing is done, I just need to finish the website."
        play voice2 d1s2_hmm noloop
        mc "The website?"
        hide lst_sy_laugh01
        show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
        play voice3 stacy_yes_simple1 noloop
        sy "Yes! The website with our whole porn library on it."
        sy "Once it's ready, you can watch the films we've made."
        sy "And customers can check out the previews to see if they want to buy our stuff."
        play voice2 mc_thinking_oh1 noloop
        mc "Awesome. I can't wait to see it."
    else:
        play voice3 stacy_disappointed_mmm1 noloop
        sy "I'm going to put the movie on the shop and post a preview clip."
        sy "I wonder if it will make more money than the sci-fi movie."
        hide lst_sy_laugh01
        show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
        play voice2 mc_thinking_hmm4 noloop
        mc "Maybe. We'll see."
        play voice3 stacy_hey_happy1 noloop
        sy "Don't forget, if you want to watch the movie, you can check it out on the laptop."
        mc "Cool!"
    $ player.set_choice("pirates_movie_done")
    $ StoryController.end_scene(MOVIE_PIRATES, 0, 15, 0)
    return