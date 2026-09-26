label sm1cs_ns007i:
    $ LocationController.draw_current_location("ns")
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral1
    play voice2 d2s9_mchey noloop
    mc "Hey, Nari. You free tonight?"
    hide lit_ns_neutral1
    show expression cc.get_expression_image("ns", "ask01") as lit_ns_askl
    play voice3 nari_yes_yep noloop
    ns "I'm free most nights. I'm not a prisoner, [mcname]."
    hide lit_ns_askl
    show expression cc.get_expression_image("ns", "sad01") as lit_ns_sadl
    play voice3 nari_surprised_ehh noloop
    ns "Wait, did I commit a crime, and I'm supposed to be in jail right now?"
    ns "No one told me. I'm so sorry. I'll just-"
    play voice2 mc_no_no8 noloop
    mc "Nari, relax. It's fine. You didn't do any crime, and you're not supposed to be in jail."
    mct "At least, I'm pretty sure that's right."
    mc "Ahem. I meant, are you available to go out on a date."
    hide lit_ns_sadl
    show expression cc.get_expression_image("ns", "excited01") as lit_ns_excitedl
    play voice3 nari_thinking_oh noloop
    ns "Oh, you're really asking me out on a date?"
    play voice2 mc_yes_yes1 noloop
    mc "Yes."
    hide lit_ns_excitedl
    show expression cc.get_expression_image("ns", "ask01") as lit_ns_askl
    play voice3 nari_thinking_hmm1 noloop
    ns "Meaning we'll go out somewhere and talk about our interests away from work?"
    play voice2 mc_disappointed_ah1 noloop
    mc "Uh... that was the plan. There is a seafood place at the harbor, and I can take you on a tour of the historical lighthouse after."
    hide lit_ns_askl
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smilel
    play voice3 nari_yes_emotional noloop
    ns "Yes, I'd love that."
    ns "I was beginning to worry that you'd forgotten about that."
    play voice2 mc_no_noway noloop
    mc "Not a chance."
    hide lit_ns_smilel
    show expression cc.get_expression_image("ns", "embarrassed01") as lit_ns_embarrassedl
    play voice2 mc_thinking_hmm5 noloop
    mc "How about I pick you up at your place tonight at Six."
    hide lit_ns_embarrassedl
    show expression cc.get_expression_image("ns", "ask01") as lit_ns_askl
    play voice3 nari_thinking_emm noloop
    ns "Actually, could you pick me up here?"
    mct "Strange. Does she not want me to know where she lives?"
    play voice2 mc_yes_sure1 noloop
    mc "Uh, okay sure."
    hide lit_ns_askl
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smilel
    play voice3 nari_happy_relief noloop
    ns "Thanks, [mcname]."
    $ StoryController.end_scene(NS_STORY)
    return