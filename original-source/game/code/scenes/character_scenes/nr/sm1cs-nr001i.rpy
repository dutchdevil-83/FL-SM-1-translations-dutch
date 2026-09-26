label sm1cs_nr001i:
    $ LocationController.draw_current_location("nr")
    show expression cc.get_expression_image("nr", "serious1") as lwd_nr_serious_1
    play voice3 boy7_hey_simple noloop
    nr "Welcome to Wurst Delivery. How many sausages you need, son?"
    play voice2 d2s9_confused noloop volume 1.7
    mc "I actually heard you were hiring."
    hide lwd_nr_serious_1
    show expression cc.get_expression_image("nr", "annoyed1") as lwd_nr_annoyed_1
    play voice3 boy7_thinking_oh noloop
    nr "Oh yeah. Last delivery guy got discovered or something. Lazy millennial won't take my calls anymore."
    play voice2 mc_arrogant_heh2 noloop
    mc "Uh cool."
    hide lwd_nr_annoyed_1
    show expression cc.get_expression_image("nr", "serious1") as lwd_nr_serious_1
    play voice3 boy7_thinking_hmm1 noloop
    nr "You know how to ride a bike with a big delivery bag on your back?"
    play voice2 mc_yes_yeah4 noloop
    mc "I'm sure I'll manage."
    hide lwd_nr_serious_1
    show expression cc.get_expression_image("nr", "smile1") as lwd_nr_smile_1
    play voice3 boy7_yes_aga1 noloop
    nr "Great. Here's your first order list. I'll pay you at the end of the shift."
    hide lwd_nr_smile_1
    show expression cc.get_expression_image("nr", "serious1") as lwd_nr_serious_1
    play voice3 boy7_angry_hmm noloop
    nr "Now get moving, no one likes a cold wiener."
    play voice2 mc_yes_sure1 noloop
    mc "No problem."
    call play_wurst_delivery from _call_play_wurst_delivery
    $ StoryController.activate_story_line(MAS_STORY)
    $ StoryController.end_scene(MS)
    return