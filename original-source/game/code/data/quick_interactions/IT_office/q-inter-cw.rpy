init 3 python:
    CharacterController.get_character("cw").interactions = [
            {LABEL: "q_inter_cw_1", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_cw_2", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_cw_3", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_cw_4", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_cw_5", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_cw_6", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_cw_7", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_cw_8", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_cw_9", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [CW_STORY, "sm1cs_cw002"]},
            {LABEL: "q_inter_cw_10", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [CW_STORY, "sm1cs_cw002"]},
            {LABEL: "q_inter_cw_11", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [CW_STORY, "sm1cs_cw002"]},
            ]
    CharacterController.get_character("cw").default_expression = "neutral01"

label q_inter_cw_1:
    show expression cc.get_expression_image("cw", "smile01")
    play voice3 girl29_hey_happy noloop
    cw "[mcname], how are you settling in?"
    play voice2 mc_thinking_hmm5 noloop volume 1.3
    mc "Uh, good? I think. I get along with pretty much everyone."
    cw "Happy to hear that."
    $ CharacterController.get_character("cw").add_point()
    return
label q_inter_cw_2:
    show expression cc.get_expression_image("cw", "annoyed01")
    play voice3 girl29_arrogant_huh noloop
    cw "Our deadline is coming up, [mcname]. You better have your portion of the project done."
    play voice2 mc_pain_ou1 noloop volume 1.3
    mc "Uhhhh, yep! No need to worry about me, Claire."
    mct "Shit, I should get back to work!"
    return
label q_inter_cw_3:
    show expression cc.get_expression_image("cw", "annoyed01") as lst_cw_annoyed01
    play voice3 girl29_angry_argh1 noloop
    cw "Mmmmmgh."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What's wrong, Claire?"
    hide lst_cw_annoyed01
    show expression cc.get_expression_image("cw", "neutral01")
    play voice3 girl29_thinking_oh noloop
    cw "Oh, I didn't see you there. Erm, nothing."
    play voice2 mc_yes_okay2 noloop
    mc "Okay?"
    cw "*Quietly* That's really what's passing for fashion this season?"
    return
label q_inter_cw_4:
    show expression cc.get_expression_image("cw", "smile01")
    play voice3 girl29_hey_provocative noloop
    cw "[mcname], do you like Cuban Russian fusion food?"
    play voice2 mc_surprised_what1 noloop
    mc "... What?"
    play voice3 girl29_thinking_hmm4 noloop
    cw "I went to a new restaurant last night and wasn't a fan. I've got some promo coupons I can give you if you like Cuban Russian fusion."
    mc "I think I'll pass, thanks though."
    cw "After having their food, you're making the right call."
    $ CharacterController.get_character("cw").add_point()
    return
label q_inter_cw_5:
    show expression cc.get_expression_image("cw", "annoyed01")
    play voice3 girl29_yes_questioning noloop
    cw "Can I help you, [mcname]?"
    play voice2 mc_hey_hey5 noloop
    mc "Just wanted to say hi."
    play voice3 girl29_disappointed_oh noloop
    cw "Oh. Well, hi [mcname]."
    cw "..."
    cw "Get back to work."
    return
label q_inter_cw_6:
    show expression cc.get_expression_image("cw", "neutral01")
    play voice3 girl29_disappointed_ehh noloop
    cw "I'm heading out the door, is it urgent?"
    play voice2 mc_no_nope2 noloop
    mc "Nope, nothing pressing."
    play voice3 girl29_yes_aga1 noloop
    cw "Good. I'm meeting a potential client at s new gastro-pub I've heard a lot about and don't want to be late."
    cw "If anything comes up while I'm out, talk to Anna."
    $ CharacterController.get_character("cw").add_point()
    return
label q_inter_cw_7:
    show expression cc.get_expression_image("cw", "neutral01")
    play voice3 girl29_arrogant_huh noloop
    cw "[mcname], how do you think Anna's team is performing?"
    play voice2 mc_thinking_mmm7 noloop
    mc "I think we're doing well."
    cw "Good. I need you all to really shine over the next few weeks."
    return
label q_inter_cw_8:
    show expression cc.get_expression_image("cw", "curious01") as q_inter_cw8_curious01
    play voice3 girl29_thinking_hmm5 noloop
    cw "Hmm...."
    play voice2 mc_thinking_hmm5 noloop
    mc "What's up, Claire?"
    hide q_inter_cw8_curious01
    show expression cc.get_expression_image("cw", "embarrassed01")
    play voice3 girl29_thinking_oh noloop
    cw "Oh, just a Jimmy Beerd award winning chef is in town, and I want to go..."
    cw "But the waitlist is a mile long and I'm not sure I can get in."
    return
label q_inter_cw_9:
    show expression cc.get_expression_image("cw", "neutral01") as q_inter_cw_neutral01
    play voice2 d2s9_mchey noloop
    mc "Hello Claire."
    hide q_inter_cw_neutral01
    show expression cc.get_expression_image("cw", "annoyed01") as q_inter_cw_annoyed01
    play voice3 girl29_angry_hm noloop
    cw "Mrs. Watts."
    play voice2 mc_yes_yeah3 noloop
    mc "Right, I keep forgetting."
    mc "*whispers* Because of our lunch."
    hide q_inter_cw_annoyed01
    show expression cc.get_expression_image("cw", "serious01")
    play voice3 girl29_thinking_hmm1 noloop
    cw "Some women might find that issue endearing."
    cw "Your clumsiness."
    cw "I do not, Mr. Young."
    return
label q_inter_cw_10:
    show expression cc.get_expression_image("cw", "neutral01") as q_inter_cw_neutral01
    play voice2 mc_thinking_emm1 noloop
    mc "You know if I see your parents again, maybe we need to work out more backstory details."
    play voice3 girl29_no_active noloop
    cw "No. We not. Keep it vague, Mr. Young."
    cw "That is one of the hallmarks of marketing."
    hide q_inter_cw_neutral01
    show expression cc.get_expression_image("cw", "serious01") as q_inter_cw_serious01
    play voice3 girl29_thinking_mmm1 noloop
    cw "Promise a ship, but a ship made of fog so that when you have to come up with details, you can figure out what the ship was made of."
    cw "Right on the spot."
    hide q_inter_cw_serious01
    show expression cc.get_expression_image("cw", "neutral02")
    play voice3 girl29_thinking_oh noloop
    cw "It might not even have been a ship at all."
    play voice2 d2s9_confused noloop
    mc "Uh... sure."
    $ CharacterController.get_character("cw").add_point()
    return
label q_inter_cw_11:
    show expression cc.get_expression_image("cw", "neutral01") as q_inter_cw_neutral01
    play voice2 mc_hey_hey10 noloop
    mc "*cutesy* Hey Honey. When is our next lunch?"
    hide q_inter_cw_neutral01
    show expression cc.get_expression_image("cw", "annoyed01")
    play voice3 girl29_angry_argh2 noloop
    cw "Go away. Now."
    play voice2 mc_yes_aga1 noloop
    mc "Message recieved."
    return