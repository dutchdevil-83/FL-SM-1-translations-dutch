label sm1cs_ns011i:
    $ LocationController.draw_current_location("ns")
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smilel
    play voice2 mc_hey_hey5 noloop
    mc "Hello Nari."
    play voice3 nari_hey_high noloop
    ns "Hi [mcname]!"
    mc "Are you ready to move in?"
    hide lit_ns_smilel
    show expression cc.get_expression_image("ns", "excited01") as lit_ns_excitedl
    play voice3 nari_sexphrase_yes2 noloop
    ns "YES!"
    hide lit_ns_excitedl
    show expression cc.get_expression_image("ns", "embarrassed01") as lit_ns_embarrassedl
    play voice3 nari_disappointed_eeh noloop
    ns "Sorry."
    play voice2 mc_yes_aga1 noloop
    mc "It's okay. Are you nervous?"
    hide lit_ns_embarrassedl
    show expression cc.get_expression_image("ns", "nervous01")
    play voice3 nari_no_expressive noloop
    ns "No. I've just been so excited to move in with you."
    ns "Now it's finally happening!"
    play voice2 d9s2_ugu noloop volume 1.6
    mc "Let's go."
    $ StoryController.end_scene(NS_STORY)
    return