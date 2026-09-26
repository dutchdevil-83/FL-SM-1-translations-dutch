label sm1ms011_02i:
    $ LocationController.draw_current_location("sy")
    if player.get_choice("first_job_to_unlock") == THEATER_STORY_LINE:
        show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
        play voice3 stacy_arrogant_huh1 noloop
        sy "Alright, spill it. How did your first day at Orbix go?"
        play voice2 d1s5_mcthinks noloop volume 1.7
        mc "It was... different. Definitely a lot to take in."
        sy "Different? Come on, give me more than that. What about the people there?"
        hide lst_sy_excited1
        show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
        play voice3 stacy_hey_happy1 noloop
        sy "Let's start with the girls. There are girls, right?"
        play voice2 mc_yes_yes1 noloop
        mc "Of course."
        sy "Good! Now, details."
        mc "There's Nari. She's super smart and eager—almost too eager. She's already memorized the employee handbook."
        hide lst_sy_naughty1
        show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
        play voice3 stacy_surprised_oh1 noloop
        sy "Wow. She sounds intense."
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah, but she's also really sweet. She left South Korea to work here, so she's got guts."
        sy "I like her already."
        mc "Then there's Anna. She's got great energy. Very confident, and honestly, she's kind of a mystery."
        hide lst_sy_excited1
        show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
        play voice3 stacy_happy_laugh2 noloop
        sy "Mysteries are fun. Anything kinky hiding under that confidence?"
        play voice2 mc_thinking_hmm2 noloop
        mc "Nothing obvious, but who knows?"
        sy "We'll keep an eye on her."
        mc "April... well, she's a lot."
        hide lst_sy_naughty1
        show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
        play voice3 stacy_surprised_how1 noloop
        sy "How so?"
        play voice2 d1s5b_ehhh noloop volume 1.7
        mc "She wasn't exactly welcoming. She made it pretty clear she doesn't think much of newbies."
        sy "Sounds like a challenge."
        mc "Yeah, but I'm up for it."
        hide lst_sy_ask1
        show expression cc.get_expression_image("sy", "smile2") as lst_sy_smile2
        play voice3 stacy_arrogant_hmm1 noloop
        sy "What about your boss's boss? Claire."
        play voice2 mc_surprised_uh2 noloop
        mc "What about her?"
        sy "Don't act dumb. Is she hot?"
        mc "She is, but that's not the point. She's my boss's boss, Stacy. It's complicated."
        hide lst_sy_smile2
        show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
        play voice3 stacy_arrogant_ha2 noloop
        sy "Complicated is our specialty. Don't rule her out."
        sy "Well, it sounds like you've got a colorful group there. Don't get lost in the ones and zeroes too much, okay?"
        play voice2 mc_yes_sure1 noloop
        mc "I won't."
    else:
        show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
        play voice2 mc_surprised_oh3 noloop
        mc "I almost forgot to talk to you about the theater."
        hide lst_sy_naughty1
        show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
        play voice3 stacy_yes_yeah2 noloop
        sy "Oh yeah. What's it like. Did they make you do some super theater geek ritual to join them?"
        play voice2 d3s11b_mcheh noloop
        mc "Haha. No but they did make me audition."
        hide lst_sy_excited1
        show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
        play voice3 stacy_arrogant_huh1 noloop
        sy "And?"
        play voice2 mc_arrogant_heh1 noloop
        mc "And they basically told me not to quit my day job."
        sy "What? They didn't let you join?"
        mc "It wasn't that bad. The director, Denise, said I have some potential."
        mc "She didn't give me an acting role, at least not yet."
        sy "So what happened?"
        hide lst_sy_ask1
        show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
        play voice2 mc_thinking_hmm4 noloop
        mc "She assigned me to be a stagehand. I help this guy Bruce around back stage."
        mc "Should be easy enough, but it's got me feeling like I should work out more."
        play voice3 stacy_happy_hmm1 noloop
        sy "You're always strong enough for me, [mcname]."
        play voice2 mc_happy_a1 noloop
        mc "Thanks."
        hide lst_sy_smile1
        show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
        play voice3 stacy_thinking_hmm1 noloop
        sy "Well at least you're kind of 'in'. So that must mean you still met some of the girls there."
        play voice2 mc_yes_yeah4 noloop
        mc "I did. Like I said, Denise is the director. Probably least likely to join us."
        mc "Then there is Veronica and Kellie. Now Veronica is super friendly."
        mc "I get the feelings she's the kind of girl who loved unicorns and ponies growing up."
        mc "And still does."
        hide lst_sy_naughty1
        show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
        play voice3 stacy_arrogant_huh2 noloop
        sy "Alright. And what about Kellie?"
        play voice2 mc_disappointed_ehh1 noloop
        mc "Kellie is a little harder to read. I don't think she was happy with Taisia bringing me in."
        hide lst_sy_ask1
        show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
        play voice3 stacy_thinking_well1 noloop
        sy "Well, it sounds like you'll just have to go on a charm offensive and win her over."
        play voice2 d4s4_mclaugh noloop
        mc "Hahah. we'll see."
        hide lst_sy_smile1
        show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
        play voice3 stacy_yes_ugu1 noloop
        sy "Mmmhmm. Well, all in all, I'm glad you got the foot in the door."
        sy "But I'm sure if you want to get one of these actresse to join us, you'll have to get on stage yourself."
        play voice2 d9s2_yeah noloop volume 2.5
        mc "That's the plan."
    $ StoryController.end_scene(MS)
    return