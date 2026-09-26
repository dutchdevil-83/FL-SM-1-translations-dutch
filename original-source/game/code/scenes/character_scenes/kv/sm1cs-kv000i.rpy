label sm1cs_kv000i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_hey noloop
    sy "Hey [mcname]! There's something I wanted to mention to you."
    play voice2 mc_yes_yeah8 noloop
    mc "What's up Stacy?"
    sy "I think I might have found someone who could help us get the studio up and running."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, great! Who?"
    hide lst_sy_excited1
    show expression cc.get_expression_image("sy", "smile2") as lst_sy_smile2
    play voice3 stacy_thinking_hmm4 noloop
    sy "Her name is Kanya. She goes to college here in town, and she is an incredible photographer."
    play voice2 d2s9_confused noloop
    mc "Just because-"
    hide lst_sy_smile2
    show expression cc.get_expression_image("sy", "angry1") as lst_sy_angry1
    play voice3 stacy_angry_argh1 noloop
    sy "Let me finish! She takes these super hot, kinky pics all the time. If there's anyone that could help us become the best porn studio in the world, it's her."
    play voice2 mc_yes_okay2 noloop
    mc "Okay, okay. Where is she?"
    hide lst_sy_angry1
    show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
    play voice3 stacy_mmm1 noloop
    sy "She works a lot at this place called... Shit I can't remember..."
    sy "It's something like Ken's Casa House? It's ridiculous."
    play voice2 mc_thinking_mmm4 noloop
    mc "Do you mean Ken's Photo Dojo?"
    hide lst_sy_ask1
    show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
    play voice3 stacy_yes_yeah2 noloop
    sy "Yes! That's it!"
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, I think I've been past it once or twice."
    sy "Why don't you see if you can find her there?"
    play voice2 mc_thinking_hmm4 noloop
    mc "Well... It can't hurt, right?"
    play voice3 stacy_yes_ugu1 noloop
    sy "Right!"
    call sm1cs_kv000i_unlock_dojo from _call_sm1cs_kv000i_unlock_dojo
    $ StoryController.end_scene(KV_STORY, 0, 30, 0)
    return
label sm1cs_kv000i_unlock_dojo:
    $ player.discover_map_location(PHOTO_DOJO)
    return
label sm1cs_kv000i_unlocks:
    call sm1cs_kv000i_unlock_dojo from _call_sm1cs_kv000i_unlock_dojo_1
    if config_storyline_mode is True:
        $ execute_storyline_config(KV_STORY)
    return