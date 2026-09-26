init 3 python:
    CharacterController.get_character("kv").interactions = [
            {LABEL: "q_inter_kv_1", LOCATIONS: [PHOTO_DOJO]},
            {LABEL: "q_inter_kv_2", LOCATIONS: [PHOTO_DOJO]},
            {LABEL: "q_inter_kv_3", LOCATIONS: [PHOTO_DOJO]},
            {LABEL: "q_inter_kv_4", LOCATIONS: [PHOTO_DOJO], AFTER_SCENE: [BG_STORY, "sm1cs_bg001"]},

            ]
    CharacterController.get_character("kv").default_expression = "neutral01"

label q_inter_kv_1:
    show expression cc.get_expression_image("kv", "smile01") as q_inter_kv1_smile01
    play voice3 kanya_hey_simple1 noloop
    kv "Hey [mcname]!"
    return
label q_inter_kv_2:
    show expression cc.get_expression_image("kv", "smile01") as q_inter_kv1_smile01
    play voice3 kanya_hey_simple1 noloop
    kv "[mcname]! You get any practice in since I last saw you?"
    play voice2 mc_thinking_mmm7 noloop
    mc "Practice... Like sex?"
    hide q_inter_kv1_smile01
    show expression cc.get_expression_image("kv", "angry01")
    play voice3 kanya_no_angry noloop
    kv "No, you perv! Behind the camera!"
    play voice2 mc_surprised_oh2 noloop
    mc "OH. Uhm... No."
    return
label q_inter_kv_3:
    show expression cc.get_expression_image("kv", "neutral01") as q_inter_kv2_neutral01
    play voice3 kanya_thinking_hmm4 noloop
    kv "Hmmm. Do I really want to upgrade to a mirrorless system?"
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Whatcha' thinking about, Kanya?"
    hide q_inter_kv2_neutral01
    show expression cc.get_expression_image("kv", "neutral02") as q_inter_kv2_neutral02
    play voice3 kanya_disappointed_neh noloop
    kv "Just this new camera..."
    play voice2 mc_thinking_mmm5 noloop
    mc "I think of you as an SLR chick. I can't imagine you as a mirrorless person."
    hide q_inter_kv2_neutral02
    show expression cc.get_expression_image("kv", "smile02") as q_inter_kv2_smile02
    play voice3 kanya_sex_closedmoan1 noloop
    kv "Mmmm, keep talking like that [mcname] and you might have to free up your afternoon for me."
    $ CharacterController.get_character("kv").add_point()
    return
label q_inter_kv_4:
    show expression cc.get_expression_image("kv", "neutral01") as q_inter_kv3_neutral01
    play voice2 d1s2_hmm noloop
    mc "Got any fun shoots coming up?"
    play voice3 kanya_yes_yeah2 noloop
    kv "I think I have a few more with Amore. Zuzu is planning to come back sometime soon, as well."
    mc "That'll be fun!"
    hide q_inter_kv3_neutral01
    show expression cc.get_expression_image("kv", "smile01")
    play voice3 kanya_happy_laugh3 noloop
    kv "Oh, you know it will be."
    return