label sm1mv02s07b_1i:
    $ LocationController.draw_current_location("ns")
    show expression cc.get_expression_image("ns", "excited01") as lit_ns_excited01
    play voice2 mc_hey_hey5 noloop
    mc "Hey Nari! I was just thinking about you and wanted to see how you're feeling about your first big movie!"
    play voice4 nari_hey_high noloop
    ns "Hello, [mcname]! I think it is going very well! I'm having a lot of fun working in adult entertainment with you."
    play voice2 mc_happy_a1 noloop
    mc "That's good to hear!"
    hide lit_ns_excited01
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    play voice4 nari_yes_questioning noloop
    ns "It is funny, because I was thinking about you today, too. I was wondering if you would want to do something today together?"
    play voice2 mc_happy_yay2 noloop
    mc "That sounds awesome!"
    mct "Hmm...We could really use some R&R, and that new spa place looks great..."
    mct "Plus, it would be a great way for Nari and Lyssa to spend some more time together."
    hide lit_ns_smile01
    show expression cc.get_expression_image("ns", "embarrassed01") as lit_ns_embarrassed01
    play voice2 mc_thinking_emm1 noloop
    mc "You want to go out on a date with Lyssa and I? I have a place in mind and everything."
    play voice4 nari_thinking_oh noloop
    ns "Oh! With Lyssa? She is the woman who transitioned, yes? That sounds wonderful!"
    play voice2 mc_yes_sure1 noloop
    mc "Let me talk to her and see how she feels about the spa."
    $ StoryController.end_scene(MOVIE_SCIFI, 0, 15, 0)
    return