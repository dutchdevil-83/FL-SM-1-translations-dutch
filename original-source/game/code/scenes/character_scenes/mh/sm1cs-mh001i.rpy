label sm1cs_mh001i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice2 mc_thinking_mmm4 noloop
    mc "Hmmm."
    play voice3 stacy_arrogant_huh1 noloop
    sy "What's up?"
    mc "I just realized that we're getting pretty close to being able to make movies."
    mc "But if I remember my business classes, all of our employees will need contracts that spell out all the details of their work."
    hide lst_sy_naughty1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_yes_yeah1 noloop
    sy "Right."
    play voice2 d2s9_confused noloop
    mc "So you'll get started on those?"
    sy "Huh? I'm a big-picture gal, [mcname]. I thought you'd know all the nitty-gritty stuff because of your major."
    mc "Uh... I think I skipped those classes. I don't know how to write contracts."
    hide lst_sy_excited1
    show expression cc.get_expression_image("sy", "sad1") as lst_sy_sad1
    play voice3 stacy_oh2 noloop
    sy "Oh shit."
    play voice2 mc_yes_yeah3 noloop
    mc "Shit is right."
    mc "Wait!"
    hide lst_sy_sad1
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice3 stacy_surprised_huh1 noloop
    sy "What?"
    play voice2 mc_thinking_hmm4 noloop
    mc "We're not screwed yet. We should go ask Lyssa for help with this."
    sy "Hey, you're right. Lyssa is the best! She probably knows all about boring stuff like that."
    mc "And it will be good to see her again."
    mc "Should we go talk to her at her office?"
    play voice3 stacy_yes_ugu1 noloop
    if gt.curr_day in WORKDAYS_LIST:
        sy "Great. We can go there tomorrow in the morning."
    else:
        sy "Great. We should go to her office Monday morning."
    $ StoryController.end_scene(MH_STORY, 0, 30, 0)
    return