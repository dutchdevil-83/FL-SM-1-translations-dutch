label sm1cs_ns012i:
    $ LocationController.draw_current_location("ns")
    show expression cc.get_expression_image("ns", "curious01") as lit_ns_curious01
    play voice3 nari_hey_asking noloop
    if curr_position == SD_NARI:
        ns "Hi [mcname]. Come to check out my finished room?"
        play voice2 mc_yes_sure1 noloop
        mc "That's why I'm here."
    else:
        ns "Hi, [mcname]. Do you want to check out my room?"
        ns "It's all finished now."
        play voice2 mc_yes_sure1 noloop
        mc "Sure let's go."
        hide lit_ns_curious01
        show expression cc.get_expression_image("ns", "excited01")
        play voice3 nari_happy_relief noloop
        ns "Great."
    $ StoryController.end_scene(NS_STORY)
    return
label sm1cs_ns012i_repeatable:
    $ LocationController.draw_current_location("ns")
    show expression cc.get_expression_image("ns", "curious01") as lit_ns_curious01
    play voice2 mc_thinking_hmm2 noloop
    if curr_position == SD_NARI:
        mc "I want to have some fun with you, Nari."
        hide lit_ns_curious01
        show expression cc.get_expression_image("ns", "naughty01")
        play voice3 nari_happy_mmm noloop
        ns "Mmmm. I like the sound of that."
    else:
        mc "Let's go to your room, Nari."
        hide lit_ns_curious01
        show expression cc.get_expression_image("ns", "excited01")
        play voice3 nari_yes_aga1 noloop
        ns "Sure!"
    menu:
        "Be aggressive with Nari":
            $ sm1cs_ns012_aggressive = True
        "Be relaxed with Nari":
            $ sm1cs_ns012_aggressive = False
    jump sm1cs_ns012_repeatable