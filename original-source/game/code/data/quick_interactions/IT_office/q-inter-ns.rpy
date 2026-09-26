init 3 python:
    CharacterController.get_character("ns").interactions = [
            {LABEL: "q_inter_ns_1", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ns_2", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ns_3", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ns_4", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ns_5", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ns_6", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_ns_7", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ns_8", LOCATIONS: [PARK], AFTER_SCENE: [NS_STORY, "sm1cs_ns003"]},
            {LABEL: "q_inter_ns_9", LOCATIONS: [PARK], AFTER_SCENE: [NS_STORY, "sm1cs_ns001"]},
            {LABEL: "q_inter_ns_10", LOCATIONS: [PARK], AFTER_SCENE: [NS_STORY, "sm1cs_ns003"]},
            {LABEL: "q_inter_ns_11", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i004"]},
            {LABEL: "q_inter_ns_12", LOCATIONS: [SHOP_71STORE], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ns_13", LOCATIONS: [SHOP_71STORE], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ns_14", LOCATIONS: [SHOP_71STORE], AFTER_SCENE: [NS_STORY, "sm1cs_ns003"]},
            {LABEL: "q_inter_ns_15", LOCATIONS: [SHOP_71STORE], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i003"]},
            {LABEL: "q_inter_ns_16", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns005"]},
            {LABEL: "q_inter_ns_17", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns005"]},
            {LABEL: "q_inter_ns_18", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns005"]},
            {LABEL: "q_inter_ns_19", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns005"]},
            {LABEL: "q_inter_ns_20", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns005"]},
            {LABEL: "q_inter_ns_21", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns006"]},
            {LABEL: "q_inter_ns_22", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns006"]},
            {LABEL: "q_inter_ns_23", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns006"]},
            {LABEL: "q_inter_ns_24", LOCATIONS: [STUDIO], AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_25", LOCATIONS: [STUDIO], AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_26", LOCATIONS: [STUDIO], AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_27", LOCATIONS: [STUDIO], AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_28", AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_29", AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_30", AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_31", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_32", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_33", LOCATIONS: [IT_OFFICE, PARK, SHOP_71STORE], AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_34", AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_35", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns011"]},
            {LABEL: "q_inter_ns_36", LOCATIONS: [STUDIO, IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns006"]},
            {LABEL: "q_inter_ns_37", LOCATIONS: [STUDIO, IT_OFFICE], AFTER_SCENE: [NS_STORY, "sm1cs_ns006"]},
            ]
    CharacterController.get_character("ns").default_expression = "smile01"

label q_inter_ns_1:
    show expression cc.get_expression_image("ns", "smile02")
    play voice3 nari_hey_asking noloop
    ns "Hello [mcname]."
    return
label q_inter_ns_2:
    show expression cc.get_expression_image("ns", "nervous01")
    play voice3 nari_hey_high noloop
    ns "Oh. Hey [mcname]."
    play voice2 mc_hey_hey2 noloop
    mc "Hey Nari. Everything alright?"
    play voice3 nari_yes_emotional noloop
    ns "Yes. No. I mean it will be. I just need to reopen my last ticket."
    ns "I think I forgot something. I don't want April to see."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_3:
    show expression cc.get_expression_image("ns", "sad01")
    play voice2 mc_hey_hey5 noloop
    mc "What's new, Nari?"
    play voice3 nari_disappointed_mff noloop
    ns "Hmm. Well, I was just about to check out my stocks."
    ns "Oh... "
    play voice2 mc_thinking_mmm5 noloop
    mc "Bad news?"
    play voice3 nari_thinking_mff noloop
    ns "Mmhmm."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_4:
    show expression cc.get_expression_image("ns", "smile01")
    play voice3 nari_happy_relief noloop
    ns "I've been listening to a new podcast called Dog Day Money, [mcname]."
    ns "If you're interested in becoming a millionaire quick, you should listen in."
    play voice2 mc_arrogant_heh1 noloop
    mc "Heh. Sounds a bit like a scam."
    ns "You're wise to be cautious, but Dr. Dog is a professional. He says so himself."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_5:
    show expression cc.get_expression_image("ns", "worried01") as lst_ns_worried01
    play voice3 nari_disappointed_huh noloop
    ns "Do you think that one day I could be in charge of my own company, [mcname]?"
    play voice2 d9s2_yeah noloop volume 2.5
    mc "You're pretty smart and very hard-working, Nari."
    mc "With enough time, I think you could totally become a CEO."
    hide lst_ns_worried01
    show expression cc.get_expression_image("ns", "smile02")
    play voice3 nari_surprised_huh1 noloop
    ns "Really? Thanks [mcname]!"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_6:
    show expression cc.get_expression_image("ns", "smile02")
    play voice3 nari_happy_yay noloop
    ns "This place is really amazing."
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    ns "Mmhmm! A lot of potential. Most of the offices I worked in Korea were a lot more compact."
    mc "Glad you like it, Nari."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_7:
    show expression cc.get_expression_image("ns", "smile01")
    play voice3 nari_hey_high noloop
    ns "Oh hey there. How's it going , [mcname]?"
    play voice2 d9s2_yeah noloop volume 1.8
    mc "Not bad, Nari. What are you up to?"
    play voice3 nari_happy_relief noloop
    ns "*sniffs* Nothing much, just taking a stroll and enjoying some fresh air."
    ns "I'll catch you next time, [mcname]."
    return
label q_inter_ns_8:
    show expression cc.get_expression_image("ns", "smile02")
    play voice2 mc_hey_hey3 noloop
    mc "Hey Nari. You're looking perky."
    play voice3 nari_yes_aga1 noloop
    ns "Mmhmm!"
    ns "I love just strolling through the park. Especially after work."
    ns "It's great to stretch out my legs and feel the breeze on my nip-"
    play voice3 nari_happy_laugh1 noloop
    ns "Well... you know *giggles*"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_9:
    show expression cc.get_expression_image("ns", "sad01") as lst_ns_sad01
    play voice2 mc_happy_yay2 noloop
    mc "Hey Nari."
    play voice3 nari_disappointed_oh noloop
    ns "Oh hey, [mcname]."
    mc "Something on your mind?"
    hide lst_ns_sad01
    show expression cc.get_expression_image("ns", "nervous01")
    play voice3 nari_happy_mmm noloop
    ns "Mmm. If I could just figure out some groundbreaking tech, I could buy a home and turn my big backyard into something beautiful like this."
    play voice2 mc_happy_a1 noloop
    mc "I hope I get an invite when you do."
    ns "Of course!"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_10:
    show expression cc.get_expression_image("ns", "smile01")
    mct "There's Nari. She's looking sneaky."
    play voice3 nari_happy_laugh2 noloop
    ns "*giggles*"
    play voice2 mc_arrogant_huh1 noloop
    mc "What's up, Nari?"
    play voice3 nari_arrogant_heh noloop
    ns "I keep thinking about our little experiment in the bathroom over there, [mcname]."
    ns "Maybe we can try that again some time."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_11:
    show expression cc.get_expression_image("ns", "smile02")
    play voice2 d1s2_mchey noloop volume 1.6
    mc "Hey Nari. What's new with you?"
    play voice3 nari_no_nah noloop
    ns "Nothing new. Just trying to clear my mind a bit."
    ns "I shouldn't say anything, but working with April can get a little frustrating."
    play voice2 mc_yes_yeah5 noloop
    mc "I know the feeling."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_12:
    show expression cc.get_expression_image("ns", "smile02")
    play voice3 nari_happy_yeah noloop
    ns "[mcname]! This is my first time having candy outside of Seoul and it's AMAZING!"
    return
label q_inter_ns_13:
    show expression cc.get_expression_image("ns", "worried01")
    play voice3 nari_surprised_huh1 noloop
    ns "Is this where you go to get food?"
    play voice2 mc_disappointed_ah2 noloop
    mc "Uh, it's usually better to get food from a grocery store."
    ns "Oh, back home we have small stores like this where we do most of our shopping."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_14:
    show expression cc.get_expression_image("ns", "smile02")
    play voice3 nari_surprised_wow noloop
    ns "Did you know they sell lube here!?"
    return
label q_inter_ns_15:
    show expression cc.get_expression_image("ns", "smile02")
    play voice3 nari_happy_relief noloop
    ns "[mcname]! This is the only store I've been able to find seaweed chips in!"
    ns "They are absolutely disgusting, but they remind me of home."
    return
label q_inter_ns_16:
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    play voice3 nari_hey_unsure noloop
    ns "Hey, [mcname]. *sniffs* Such a wonderful day isn't it?"
    play voice2 mc_yes_yes1 noloop
    mc "It really is. Especially around you."
    hide lit_ns_smile01
    show expression cc.get_expression_image("ns", "laugh01")
    play voice3 nari_happy_laugh3 noloop
    ns "Hehehe."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_17:
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    play voice3 nari_hey_calm noloop
    ns "Nice work on that transfer error ticket, [mcname]. I think you're improving a lot."
    play voice2 mc_surprised_huh7 noloop
    mc "Really?"
    hide lit_ns_smile01
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice3 nari_yes_aga1 noloop
    ns "Totally. I mean, your skills were pretty non-existent earlier, so it's not too hard."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh."
    hide lit_ns_neutral01
    show expression cc.get_expression_image("ns", "embarrassed01")
    play voice3 nari_thinking_hmm3 noloop
    ns "But. I mean, you've shown a lot of improvement."
    ns "I bet Anna will say the same during your next review."
    return
label q_inter_ns_18:
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice3 nari_hey_calm noloop
    ns "Mmm. Hey."
    play voice2 mc_happy_yay2 noloop
    mc "Hey."
    hide lit_ns_neutral01
    show expression cc.get_expression_image("ns", "naughty01") as lit_ns_naughty01
    play voice3 nari_thinking_hmm2 noloop
    ns "It's a little late, and people are heading home soon."
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah."
    ns "Remind you of anything."
    mc "Hehehe. Yeah."
    hide lit_ns_naughty01
    show expression cc.get_expression_image("ns", "laugh01")
    play voice3 nari_happy_laugh6 noloop
    ns "*giggles*"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_19:
    show expression cc.get_expression_image("ns", "naughty01") as lit_ns_naughty01
    play voice2 mc_hey_hey7 noloop
    mc "I see you."
    play voice3 nari_surprised_huh1 noloop
    ns "Huh? What do you mean?"
    mc "I see you making sexy eyes at me."
    mc "How is a man supposed to work around a cute little thing like you."
    hide lit_ns_naughty01
    show expression cc.get_expression_image("ns", "embarrassed01") as lit_ns_embarrassed01
    play voice3 nari_happy_laugh5 noloop
    ns "Hehe. Well I hope that your financial stability is a good enough reason."
    ns "I'd hate for you to get fired."
    hide lit_ns_embarrassed01
    show expression cc.get_expression_image("ns", "laugh01")
    play voice3 nari_happy_laugh1 noloop
    ns "Then again, that might mean more 'playtime'."
    play voice2 d3s11b_mcheh noloop
    mc "Haha."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_20:
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice2 mc_thinking_hmm3 noloop
    mc "What are you thinking about?"
    play voice3 nari_happy_mmm noloop
    ns "Mmmm."
    hide lit_ns_neutral01
    show expression cc.get_expression_image("ns", "naughty01")
    play voice3 nari_happy_laugh1 noloop
    ns "You. Hehe."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_21:
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice3 nari_disappointed_eh noloop
    ns "I still can't believe how close Megan came to finding us being so bad."
    ns "*whispers* Oooh. I probably shouldn't talk so loud about it."
    return
label q_inter_ns_22:
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice3 amrose_old_psst2 noloop
    ns "*whispers* Pssst. [mcname]."
    play voice2 mc_yes_yes7 noloop
    mc "Yes, Nari?"
    hide lit_ns_neutral01
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    play voice3 nari_happy_laugh1 noloop
    ns "Hehehe. Nevermind. I just wanted you to look at me."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_23:
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice3 nari_surprised_huh1 noloop
    ns "You don't think... Was Megan cockblocking us that night?"
    play voice2 mc_no_no2 noloop
    mc "No. And we gotta be careful, Nari."
    mc "Some stuff is open to misinterpretation, but cockblocking is pretty universal."
    hide lit_ns_neutral01
    show expression cc.get_expression_image("ns", "annoyed01") as lit_ns_annoyed01
    play voice3 nari_arrogant_fff noloop
    ns "Okay."
    return
label q_inter_ns_24:
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    play voice2 mc_surprised_wow2 noloop
    mc "That's quite a computer set up you've got there, Nari."
    play voice3 nari_yes_emotional noloop
    ns "Yes, [mcname]. I do a little bit of crypto mining and it requires quite the computer set up."
    hide lit_ns_smile01
    show expression cc.get_expression_image("ns", "smile02") as lit_ns_smile02
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah... {w}Wait, doesn't that take a lot of power, too?"
    play voice3 nari_yes_aga1 noloop
    ns "It does, yes."
    mc "Is that going to make our electric bill go crazy?"
    hide lit_ns_smile02
    show expression cc.get_expression_image("ns", "embarrassed01")
    play voice3 nari_thinking_emm noloop
    ns "Uhm..."
    play voice2 d1s1_mmm noloop volume 1.6
    mct "Oh boy..."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_25:
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    play voice2 mc_happy_yay2 noloop
    mc "I like the poster you have on your wall."
    play voice3 nari_happy_yeah noloop
    ns "I like it too! Isn't she so cool!?!"
    mc "Yeah, and... also a little naked."
    hide lit_ns_smile01
    show expression cc.get_expression_image("ns", "embarrassed01")
    play voice3 nari_surprised_what noloop
    ns "What! Her outfit isn't - wait, is that-"
    ns "Oh my! How did I never realize her nipple was showing!"
    play voice2 d2s9_confused noloop
    mc "Uhm..."
    play voice3 nari_surprised_ehh noloop
    ns "I'm not a pervert! I swear!"
    mc "But you kind of are, Nari."
    ns "That is not the point!"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_26:
    show expression cc.get_expression_image("ns", "smile02") as lit_ns_smile02
    play voice2 mc_surprised_wow4 noloop
    mc "I didn't realize you like plants, Nari."
    play voice3 nari_yes_aga2 noloop
    ns "I do! They act as natural air purifiers."
    mc "I feel like I've heard that be-"
    hide lit_ns_smile02
    show expression cc.get_expression_image("ns", "neutral01") as lit_ns_neutral01
    play voice3 nari_thinking_hmm2 noloop
    ns "And NASA found that a single plant can effectively purify 30 square meters of a space."
    ns "And since this is roughly a 120 square foot room, 4 plants should effectively purify the whole space."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, well that's-"
    hide lit_ns_neutral01
    show expression cc.get_expression_image("ns", "smile01")
    play voice3 nari_happy_mmm noloop
    ns "However, other studies suggest that plants are not as effective as suggested in air purification, and that they can only improve a space by 25%%."
    play voice2 mc_yes_aga1 noloop
    mc "Cool-"
    ns "Some of these studies focus on specific plants, and each plants..."
    mct "I didn't realize I had opened such a big can of worms..."
    mct "Should probably just... leave her be?"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_27:
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    play voice2 d1s2_hmm noloop volume 1.6
    mc "How do you like your new room, Nari?"
    play voice3 nari_happy_mmm noloop
    ns "It's wonderful! Much nicer than where I was before."
    mc "Good! I'm happy to hear that!"
    ns "Mmmhmmm! And, it comes with a fun utility included."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh? Is there some secret about the studio I don't know?"
    hide lit_ns_smile01
    show expression cc.get_expression_image("ns", "smile02")
    play voice3 nari_thinking_oh noloop
    ns "Oh, I think you are aware of it.{w} Living here means I get to be closer to you."
    ns "Which means we can have more \"fun\" together!"
    play voice2 mc_happy_a1 noloop
    mc "I like the sound of that."
    ns "Me too!"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_28:
    show expression cc.get_expression_image("ns", "neutral01")
    play voice3 nari_disappointed_huh noloop
    ns "[mcname]. Do you have a portfolio?"
    play voice2 mc_thinking_mmm4 noloop
    mc "Like... an artist's portfolio?"
    play voice3 nari_no_nah noloop
    ns "No, a stock portfolio."
    play voice2 mc_no_no2 noloop
    mc "Uhm, no."
    ns "You really need to get one."
    return
label q_inter_ns_29:
    show expression cc.get_expression_image("ns", "smile02") as lit_ns_smile02
    play voice3 nari_hey_high noloop
    ns "[mcname], what are you doing for dinner tonight?"
    play voice2 mc_arrogant_nah1 noloop
    mc "No idea."
    ns "Hmmmm. I've been thinking about going to a KBBQ restaurant that I saw online, but I am unsure."
    mc "KBBQ?"
    hide lit_ns_smile02
    show expression cc.get_expression_image("ns", "laugh01")
    play voice3 nari_happy_laugh1 noloop
    ns "Korean barbecue! It's amazing!"
    play voice2 mc_thinking_hm noloop
    mct "Crowning has a Korean barbeque place?"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_30:
    show expression cc.get_expression_image("ns", "smile01")
    play voice3 nari_happy_relief noloop
    ns "Oh, [mcname], I believe a package will be arriving for me today!"
    play voice2 mc_yes_aga2 noloop
    mc "Good to know. I'll make sure Stacy keeps an eye out for it."
    ns "Thank you!"
    return
label q_inter_ns_31:
    show expression cc.get_expression_image("ns", "smile02") as lit_ns_smile02
    play voice2 mc_hey_hey7 noloop
    mc "How are you doing, Nari?"
    play voice3 nari_happy_relief noloop
    ns "Pretty good."
    ns "Happy to not be worried about my living situation."
    ns "April seemed to notice that something has changed."
    hide lit_ns_smile02
    show expression cc.get_expression_image("ns", "laugh01")
    play voice3 nari_happy_laugh1 noloop
    ns "She complained that I am smiling more than normal. *giggles*"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_32:
    show expression cc.get_expression_image("ns", "naughty01") as lit_ns_naughty01
    play voice3 nari_thinking_hmm1 noloop
    ns "I wonder if we are breaking any Orbix rules by living together?"
    ns "It's kind of fun to think about it."
    return
label q_inter_ns_33:
    show expression cc.get_expression_image("ns", "smile01") as lit_ns_smile01
    play voice3 nari_yes_aga1 noloop
    ns "See you at home, [mcname]."
    return
label q_inter_ns_34:
    show expression cc.get_expression_image("ns", "curious01") as lit_ns_curious01
    play voice3 nari_thinking_oh noloop
    ns "Maybe we should think of doing some meal prep together, [mcname]."
    play voice2 mc_yes_yeah2 noloop
    mc "That could be fun. And we'd probably save on lunches."
    hide lit_ns_curious01
    show expression cc.get_expression_image("ns", "smile02")
    play voice3 nari_yes_emotional noloop
    ns "That's what I was thinking about."
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_35:
    show expression cc.get_expression_image("ns", "naughty01") as lit_ns_naughty01
    play voice3 nari_happy_laugh6 noloop
    ns "Hehehe."
    ns "It's so funny, keeping a secret from everyone."
    play voice2 mc_yes_yeah1 noloop
    mc "It is, but let's still be careful about talking too much about it, Nari."
    ns "Mmhmm!"
    $ CharacterController.get_character("ns").add_point()
    return
label q_inter_ns_36:
    show expression cc.get_expression_image("ns", "serious01") as lit_ns_serious01
    play voice3 nari_thinking_emm noloop
    ns "I'm really conflicted about which video driver company to invest in."
    ns "They both seem to be rollercoasters."
    play voice2 mc_surprised_uh2 noloop
    mc "You're talking about... video drivers, like for video games?"
    hide lit_ns_serious01
    show expression cc.get_expression_image("ns", "neutral01")
    play voice3 nari_yes_confident noloop
    ns "Oh yes. The top two are constantly dancing with one another."
    play voice2 mc_thinking_hmm7 noloop
    mc "Interesting."
    return
label q_inter_ns_37:
    show expression cc.get_expression_image("ns", "curious01") as lit_ns_curious01
    play voice3 nari_thinking_hmm3 noloop
    ns "With all these advances in AI scrip modules, I wonder if I would have used them in classes."
    ns "What about you, [mcname]?"
    play voice2 mc_no_nah2 noloop
    mc "I haven't given it much thought."
    mc "But I'm glad I'm not a teacher right now."
    hide lit_ns_curious01
    show expression cc.get_expression_image("ns", "laugh01")
    play voice3 nari_happy_laugh3 noloop
    ns "*giggles* Yeah."
    $ CharacterController.get_character("ns").add_point()
    return