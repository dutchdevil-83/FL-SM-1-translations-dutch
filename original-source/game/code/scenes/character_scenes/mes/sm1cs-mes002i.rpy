label sm1cs_mes002i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "ask01") as lst_sy_ask01
    play voice2 d2s9_confused noloop
    mc "Min is back in town."
    play voice3 stacy_surprised_huh1 noloop
    sy "Min?"
    hide lst_sy_ask01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_surprised_oh1 noloop
    sy "Oh, Min. I almost forgot about her."
    sy "Where was she?"
    play voice2 mc_thinking_hmm2 noloop
    mc "In South Korea."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_thinking_hmm4 noloop
    sy "Oh, cool. When did she get in?"
    play voice2 mc_thinking_hmm4 noloop
    mc "I think about a month ago."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "angry01") as lst_sy_angry01
    play voice3 stacy_thinking_emm1 noloop
    sy "A month? You made her wait a month before going and meeting her."
    play voice2 mc_no_no2 noloop
    mc "No. That's not what happened."
    hide lst_sy_angry01
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice2 mc_thinking_hmm5 noloop
    mc "If I knew she was back, I would have tried to meet up much earlier."
    mc "She told me that since she got back, she didn't reach out to anyone from college or anyone from the Fetish Locator parties."
    mc "Talking to her, it was like. I'm not sure, but she looked a bit lost."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "ask01") as lst_sy_ask01
    play voice3 stacy_arrogant_huh2 noloop
    sy "Lost?"
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah. Adrift. Unfocused. I think all that stuff with Lydia hit her harder than I thought."
    mc "I barely recognized her at first."
    hide lst_sy_ask01
    show expression cc.get_expression_image("sy", "neutral02") as lst_sy_neutral02
    play voice3 stacy_disappointed_oh1 noloop
    sy "I can imagine. They were best friends, right?"
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. I mean, Lydia did a number on me, but it wasn't like she was with me for years before she broke my heart."
    hide lst_sy_neutral02
    show expression cc.get_expression_image("sy", "serious01") as lst_sy_serious01
    play voice3 stacy_disappointed_ehh2 noloop
    sy "Maybe Min feels guilty because she didn't see it during all those years."
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "*sighs* Lydia was good at telling people what they wanted to hear."
    mc "And making them feel how she wanted them to."
    sy "Well, that's all in the past now."
    mc "Yeah. I'm thinking of inviting her here to hang out."
    mc "That cool with you?"
    hide lst_sy_serious01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_yes_yeah1 noloop
    sy "Sure, [mcname]."
    sy "I bet Min will enjoy seeing the studio and knowing that at least some good stuff came out of the Fetish Locator Fiasco."
    play voice2 d3s11b_mcheh noloop volume 1.5
    mc "Haha. Fetish Locator Fiasco."
    hide lst_sy_smile01
    show expression cc.get_expression_image("sy", "smile02") as lst_sy_smile02
    play voice3 stacy_yes_simple1 noloop
    sy "FLF. I came up with it."
    play voice2 mc_happy_a1 noloop
    mc "Cute."
    mc "I guess I'll give Min a text when I have some time."
    hide lst_sy_smile02
    show expression cc.get_expression_image("sy", "neutral01") as lst_sy_neutral01
    play voice3 stacy_yes_yap1 noloop
    sy "Yup."
    hide lst_sy_neutral01
    show expression cc.get_expression_image("sy", "serious01") as lst_sy_serious01
    play voice3 stacy_thinking_hmm2 noloop
    sy "And who knows, maybe one day she'll want to show off some of her old Fetish Locator tricks on camera."
    play voice2 d4s4_mclaugh noloop
    mc "*chuckles* Maybe. Stranger things have happened."
    hide lst_sy_serious01
    show expression cc.get_expression_image("sy", "smile01") as lst_sy_smile01
    play voice3 stacy_yes_ugu1 noloop
    sy "Mmhmm."
    hide lst_sy_smile01
    $ StoryController.end_scene(MES_STORY)
    return