label sm1cs_rd001i:
    $ LocationController.draw_current_location("rd")
    show expression cc.get_expression_image("rd", "smile01") as lst_rd_smile
    play voice3 girl26_hey_confused noloop
    rd "Hi I'm Ridley. Welcome to Guns and Rosettes."
    rd "I got a drink with your name on it."
    play voice2 mc_yes_aga2 noloop
    mc "Thanks. The name's [mcname]."
    $ StoryController.end_scene(RD_STORY, 0, 15, 0)
    return