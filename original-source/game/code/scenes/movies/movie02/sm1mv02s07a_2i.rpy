label sm1mv02s07a_2i:
    $ LocationController.draw_current_location("ns")
    show expression cc.get_expression_image("ns", "excited01") as lit_ns_excited01
    play voice4 nari_hey_high noloop
    ns "Hi, [mcname]!"
    ns "How are you doing?"
    play voice2 mc_happy_a1 noloop
    mc "I am good, Nari. How about you?"
    play voice4 nari_happy_mmm noloop
    ns "Can't complain. I love my room, my job, and boyfriend."
    play voice2 mc_happy_laugh2 noloop
    mc "*chuckles warmly* Same."
    mc "Just with boyfriend swapped with girlfriend."
    hide lit_ns_excited01
    show expression cc.get_expression_image("ns", "laugh01") as lit_ns_laugh01
    play voice4 nari_happy_laugh1 noloop
    ns "Hehehe."
    ns "Do you have something on your mind, [mcname]?"
    hide lit_ns_laugh01
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice2 mc_yes_yes1 noloop
    mc "Yes, as a matter of fact."
    mc "Min just invited you and me to the spa."
    hide lit_ns_neutral01
    show expression cc.get_expression_image("ns", "embarrassed01") as lit_ns_embarrassed01
    play voice4 nari_surprised_ehh noloop
    ns "A spa? That sounds expensive."
    play voice2 mc_no_nah2 noloop
    mc "Nah, it's all expenses paid. Min's treat to us."
    play voice4 nari_thinking_oh noloop
    ns "Oh? That is so generous. But..."
    ns "I shouldn't go if she just wants to spend time with you."
    play voice2 mc_thinking_hmm4 noloop
    mc "That is not the case. She actually wants to get to know you a little better."
    hide lit_ns_embarrassed01
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice4 nari_yes_questioning noloop
    ns "She does?"
    play voice2 mc_yes_yes2 noloop
    mc "Yes. She'd like to make sure you two are on good terms before filming your first sex scene."
    play voice4 nari_surprised_huh1 noloop
    ns "Really? Well, I can't fault her logic.{w} And you'll be there?"
    hide lit_ns_neutral01
    show expression cc.get_expression_image("ns", "embarrassed01") as lit_ns_embarrassed01
    ns "Just in case..."
    play voice2 mc_surprised_why1 noloop
    mc "In case what?"
    play voice4 nari_thinking_emm noloop
    ns "I'm not sure. Maybe she is the jealous type."
    play voice2 mc_yes_sure1 noloop
    mc "She is not. And I'll be there in case she tries anything."
    mc "Which she won't."
    hide lit_ns_embarrassed01
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice4 nari_yes_yep noloop
    ns "Okay. I'll go get ready."
    $ StoryController.end_scene(MOVIE_SCIFI)
    return