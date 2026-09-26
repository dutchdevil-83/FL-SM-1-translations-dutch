init 3 python:
    CharacterController.get_character("am").interactions = [
            {LABEL: "q_inter_am_1", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_am_2", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_am_3", LOCATIONS: [IT_OFFICE], SUBLOCATIONS: [DEFAULT_SUBLOCATION] },
            {LABEL: "q_inter_am_4", LOCATIONS: [IT_OFFICE], SUBLOCATIONS: [DEFAULT_SUBLOCATION]},
            {LABEL: "q_inter_am_5", LOCATIONS: [IT_OFFICE], DAYS: [WEDNESDAY, THURSDAY]},
            {LABEL: "q_inter_am_6", LOCATIONS: [IT_OFFICE]},
            {LABEL: "q_inter_am_7", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i004"]},
            {LABEL: "q_inter_am_8", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i004"]},
            {LABEL: "q_inter_am_9", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i004"]},
            {LABEL: "q_inter_am_10", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i004"]},
            {LABEL: "q_inter_am_11", LOCATIONS: [PARK], AFTER_SCENE: [IT_STORY_LINE, "sm1fs_i004"]},
            {LABEL: "q_inter_am_12", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am004"]},
            {LABEL: "q_inter_am_13", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am004"]},
            {LABEL: "q_inter_am_14", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am004"]},
            {LABEL: "q_inter_am_15", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am004"]},
            {LABEL: "q_inter_am_16", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am004"], DAYS: [FRIDAY] },
            {LABEL: "q_inter_am_17", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am004"]},
            {LABEL: "q_inter_am_18", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am004"]},
            {LABEL: "q_inter_am_19", AFTER_SCENE: [AM_STORY, "sm1cs_am006"], TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8, TIMESLOT_1]},
            {LABEL: "q_inter_am_20", AFTER_SCENE: [AM_STORY, "sm1cs_am006"], TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8, TIMESLOT_1]},
            {LABEL: "q_inter_am_21", AFTER_SCENE: [AM_STORY, "sm1cs_am006"], TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8, TIMESLOT_1]},
            {LABEL: "q_inter_am_22", LOCATIONS: [GR_BAR]},
            {LABEL: "q_inter_am_23", LOCATIONS: [GR_BAR]},
            {LABEL: "q_inter_am_24", LOCATIONS: [GR_BAR], AFTER_SCENE: [AM_STORY, "sm1cs_am002"]},
            {LABEL: "q_inter_am_25", LOCATIONS: [GR_BAR], AFTER_SCENE: [AM_STORY, "sm1cs_am002"], BEFORE_SCENE: [AM_STORY, "sm1cs_am003"]},
            {LABEL: "q_inter_am_26", LOCATIONS: [GR_BAR, IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am005b"], TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8, TIMESLOT_1]},
            {LABEL: "q_inter_am_27", LOCATIONS: [GR_BAR, IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am005b"], TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6, TIMESLOT_7, TIMESLOT_8, TIMESLOT_1]},
            {LABEL: "q_inter_am_28", LOCATIONS: [IT_OFFICE], AFTER_SCENE: [AM_STORY, "sm1cs_am005b"], TIMESLOTS: [TIMESLOT_4, TIMESLOT_5, TIMESLOT_6]},
            ]
    CharacterController.get_character("am").default_expression = "neutral01"

label q_inter_am_1:
    show expression cc.get_expression_image("am", "annoyed01")
    play voice3 girl22_arrogant_hm noloop
    am "This better be good."
    play voice2 d2s9_confused noloop volume 1.4
    mc "I just wanted to ask-"
    am "I'm not your babysitter, [mcname]."
    return
label q_inter_am_2:
    show expression cc.get_expression_image("am", "neutral02") as lst_am_neutral02
    play voice3 girl22_surprised_what noloop
    am "Whaaat?"
    play voice2 mc_hey_hey2 noloop
    mc "Everything alright with you?"
    hide lst_am_neutral02
    show expression cc.get_expression_image("am", "smile01")
    play voice3 girl22_yes_simple noloop
    am "Yes. Perfect. Why?"
    play voice2 mc_thinking_emm1 noloop
    mc "You just seem a bit... hostile."
    play voice3 girl22_arrogant_he noloop
    am "Haha. You wouldn't survive me being hostile, [mcname]."
    $ CharacterController.get_character("am").add_point()
    return
label q_inter_am_3:
    show expression cc.get_expression_image("am", "neutral01")
    play voice3 girl22_hey_attention noloop
    am "That music you were listening to wasn't hot garbage for a change."
    am "What was it?"
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, \"YOLO SWAGGO\" by Darin Danger."
    am "..."
    play voice3 girl22_yes_aga1 noloop
    am "Thanks."
    $ CharacterController.get_character("am").add_point()
    return
label q_inter_am_4:
    show expression cc.get_expression_image("am", "annoyed01")
    play voice2 mc_hey_hey5 noloop
    mc "Hey April."
    am "..."
    mc "So what kind of music do you like?"
    play voice3 girl22_angry_argh1 noloop
    am "Get lost. Can't you see I'm working?"
    play voice2 mc_yes_okay1 noloop
    mc "Okay."
    return
label q_inter_am_5:
    show expression cc.get_expression_image("am", "neutral02")
    play voice2 d2s9_mchey noloop
    mc "Hey."
    play voice3 girl22_hey_simple noloop
    am "Hey."
    mct "I think that's the nicest she's ever talked to me."
    return
label q_inter_am_6:
    show expression cc.get_expression_image("am", "neutral02") as lst_am_neutral02
    play voice3 girl22_angry_argh2 noloop
    am "What?"
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Nothing, I was just thinking, that you and Anna kind of have a thing going on."
    am "A thing?"
    mc "I don't know, like uh, a rivalry? Or something. What happened?"
    hide lst_am_neutral02
    show expression cc.get_expression_image("am", "annoyed01")
    play voice3 girl22_disappointed_ehh3 noloop
    am "Let me think. You're right. We do have a thing."
    am "It's called none of your business. Now stop wasting my time."
    $ CharacterController.get_character("am").add_point()
    return
label q_inter_am_7:
    show expression cc.get_expression_image("am", "annoyed01") as lst_am_annoyed01
    play voice2 mc_hey_hey3 noloop
    mc "Hello April."
    play voice3 girl22_arrogant_huh noloop
    am "What are you doing here?"
    mc "Uh. Just taking a walk."
    hide lst_am_annoyed01
    show expression cc.get_expression_image("am", "smile01")
    play voice3 girl22_arrogant_he noloop
    am "Are you sure you're allowed to be withing a hundred feet of a park?"
    play voice2 mc_arrogant_heh1 noloop
    mc "I could ask you the same thing. I imagine your personality scares off any kids who get close."
    am "That's true. Kids suck, no respect for the devices in their disgusting hands."
    $ CharacterController.get_character("am").add_point()
    return
label q_inter_am_8:
    show expression cc.get_expression_image("am", "annoyed01") as lst_am_annoyed01
    play voice2 mc_hey_hey5 noloop
    mc "How you doing?"
    play voice3 girl22_disgust_boeagh noloop
    am "Blergh. The only thing that makes all this fresh air worse is seeing your mug."
    play voice2 mc_happy_yay2 noloop
    mc "I'm still surprised you leave your cave."
    hide lst_am_annoyed01
    show expression cc.get_expression_image("am", "neutral02")
    play voice3 girl22_yes_aga1 noloop
    am "I'm on my way to pick up food and this is the shortest route."
    mc "See you later then."
    return
label q_inter_am_9:
    show expression cc.get_expression_image("am", "neutral02")
    play voice3 girl22_hey_simple noloop
    am "Hey."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh. Hey April."
    mct "And she's gone."
    return
label q_inter_am_10:
    show expression cc.get_expression_image("am", "neutral02")
    play voice2 mc_hey_hey3 noloop
    mc "Oh hey, April. Did you need something?"
    play voice3 girl22_surprised_huh2 noloop
    am "If you owned a dog, would you always keep them on a leash? Even at a park?"
    mc "Ummm. I guess it would depend on how well behaved they were."
    am "Fair enough."
    $ CharacterController.get_character("am").add_point()
    return
label q_inter_am_11:
    show expression cc.get_expression_image("am", "neutral02") as lst_am_neutral02
    am "..."
    play voice2 mc_arrogant_huh2 noloop
    mc "Are you walking beside me?"
    play voice3 girl22_no_high noloop
    am "No, I was walking this way and now you're walking besides me."
    hide lst_am_neutral02
    show expression cc.get_expression_image("am", "annoyed01")
    play voice3 girl22_disappointed_geh noloop
    am "Don't make a big deal about it."
    play voice2 mc_yes_aga2 noloop
    mc "Alright."
    return
label q_inter_am_12:
    show expression cc.get_expression_image("am", "neutral02")
    am "..."
    play voice2 d2s9_mchey noloop
    mc "Hey April. I was-"
    play voice3 girl22_no_uhuh1 noloop
    am "If it's not work stuff, then zip it."
    return
label q_inter_am_13:
    show expression cc.get_expression_image("am", "neutral01") as lst_am_neutral01
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Do you want to talk-"
    play voice3 girl22_no_simple noloop
    am "If I did, you would know."
    hide lst_am_neutral01
    show expression cc.get_expression_image("am", "embarrassed01")
    play voice3 girl22_disappointed_ehh1 noloop
    am "So unless the room is on fire, we don't need to talk right now."
    am "Got it?"
    play voice2 mc_yes_okay2 noloop
    mc "Okay okay."
    return
label q_inter_am_14:
    show expression cc.get_expression_image("am", "neutral02") as lst_am_neutral02
    play voice2 mc_surprised_wow3 noloop
    mc "Your band was really good, April."
    mc "I can see why you like it."
    hide lst_am_neutral02
    show expression cc.get_expression_image("am", "embarrassed01")
    play voice3 girl22_disappointed_ehh2 noloop
    am "..."
    am "Don't mention it."
    return
label q_inter_am_15:
    show expression cc.get_expression_image("am", "neutral02") as lst_am_neutral02
    play voice2 mc_surprised_huh7 noloop
    mc "And that's it?"
    play voice3 girl22_yes_simple noloop
    am "Yes. You just needed to switch those settings."
    mc "I thought I could make it more effecient."
    hide lst_am_neutral02
    show expression cc.get_expression_image("am", "neutral01")
    play voice3 girl22_thinking_eeh noloop
    am "Well, this time, it didn't work."
    play voice2 mc_yes_yeah5 noloop
    mc "Right. Thanks for your help."
    am "Mmm."
    return
label q_inter_am_16:
    show expression cc.get_expression_image("am", "neutral01") as lst_am_neutral01
    play voice2 mc_thinking_hmm2 noloop
    mc "Big weekend plans?"
    play voice3 girl22_no_uhuh1 noloop
    am "I don't know yet."
    mc "Maybe we can-"
    hide lst_am_neutral01
    show expression cc.get_expression_image("am", "neutral02")
    play voice3 girl22_no_angry noloop
    am "I'm busy."
    play voice2 mc_thinking_mmm5 noloop
    mc "Right..."
    return
label q_inter_am_17:
    show expression cc.get_expression_image("am", "neutral02") as lst_am_neutral02
    play voice2 mc_disappointed_ah1 noloop
    mc "Want... uh."
    play voice3 girl22_disappointed_geh noloop
    am "For god's sake, spit it out."
    mc "I was thinking you looked like you could use some 'stress relief'."
    hide lst_am_neutral02
    show expression cc.get_expression_image("am", "annoyed01")
    play voice3 girl22_arrogant_pff noloop
    am "Dream on."
    return
label q_inter_am_18:
    show expression cc.get_expression_image("am", "neutral02") as lst_am_neutral02
    play voice2 mc_thinking_mmm3 noloop
    mc "Are we good?"
    play voice3 girl22_yes_yep4 noloop
    am "Yup."
    mc "You're not mad at me?"
    play voice3 girl22_no_nope4 noloop
    am "Nope."
    hide lst_am_neutral02
    show expression cc.get_expression_image("am", "neutral01")
    play voice2 mc_disappointed_ehh1 noloop
    mc "Are we ever going to talk normal again."
    play voice3 girl22_yes_yep4 noloop
    am "Yup."
    mc "*sighs*"
    return
label q_inter_am_19:
    show expression cc.get_expression_image("am", "neutral02") as lst_am_neutral02
    play voice2 mc_thinking_mmm3 noloop
    am "I know what you're thinking."
    mc "What am I thinking?"
    hide lst_am_neutral02
    show expression cc.get_expression_image("am", "naughty01") as lst_am_naughty01
    play voice3 girl22_arrogant_he noloop
    am "That you want to kiss me."
    mc "What?"
    hide lst_am_naughty01
    show expression cc.get_expression_image("am", "smile01") as lst_am_smile01
    play voice3 girl22_disappointed_mmf noloop
    am "I get it. I'm a very desirable female. But here at work, we need to act professional."
    am "That's not going to be a problem right?"
    play voice2 mc_no_no9 noloop
    mc "Not for me."
    hide lst_am_smile01
    show expression cc.get_expression_image("am", "neutral01") as lst_am_neutral01
    play voice3 girl22_yes_aga1 noloop
    am "Good. Just... glad we're clear."
    return
label q_inter_am_20:
    show expression cc.get_expression_image("am", "neutral01") as lst_am_neutral01
    play voice2 mc_hey_hey7 noloop
    mc "Hey."
    play voice3 girl22_hey_simple noloop
    am "Hey yourself."
    hide lst_am_neutral01
    show expression cc.get_expression_image("am", "embarrassed01") as lst_am_embarrassed01
    play voice3 girl22_thinking_oh noloop
    am "Oh. I'm uh... I'm thinking of what we can do next."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    am "Yeah. Like, our next date. So... yeah. Now you know."
    return
label q_inter_am_21:
    show expression cc.get_expression_image("am", "embarrassed01") as lst_am_embarrassed01
    play voice3 girl22_thinking_eeh noloop
    am "I have a band practice coming up."
    am "You wouldn't want to come watch, would you?"
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I'd love to."
    hide lst_am_embarrassed01
    show expression cc.get_expression_image("am", "curious01") as lst_am_curious01
    play voice3 girl22_yes_questioning noloop
    am "Really?"
    hide lst_am_curious01
    show expression cc.get_expression_image("am", "embarrassed01") as lst_am_embarrassed01
    play voice3 girl22_disappointed_geh noloop
    am "Uh... nevermind. It might be awkward. And you'd just be sitting there."
    play voice2 mc_arrogant_heh3 noloop
    mc "It sounds fun."
    hide lst_am_embarrassed01
    show expression cc.get_expression_image("am", "annoyed01") as lst_am_annoyed01
    play voice3 girl22_no_uhuh1 noloop
    am "Nah I changed my mind."
    mc "Okay."
    return
label q_inter_am_22:
    show expression cc.get_expression_image("am", "neutral01")
    play voice2 mc_hey_hey7 noloop
    mc "Hey April."
    play voice3 girl22_arrogant_hm noloop
    am "Mmhmm."
    return
label q_inter_am_23:
    show expression cc.get_expression_image("am", "annoyed01")
    play voice2 mc_hey_hey7 noloop
    mc "Hello April. Any weekend plans?"
    play voice3 girl22_thinking_oh noloop
    am "You're looking at it."
    return
label q_inter_am_24:
    show expression cc.get_expression_image("am", "annoyed01")
    play voice2 mc_hey_hey5 noloop
    mc "Hey you moved from the park."
    play voice3 girl22_thinking_oh noloop
    am "Of course. I'm not a degenerate."
    $ CharacterController.get_character("am").add_point()
    return
label q_inter_am_25:
    show expression cc.get_expression_image("am", "neutral01") as lgr_am_neutral01
    play voice2 mc_hey_hey5 noloop
    play voice3 girl22_hey_simple noloop
    am "Hey [mcname]."
    play voice2 mc_hey_hey5 noloop
    mc "Hi April."
    mc "You do shows here right."
    hide lgr_am_neutral01
    show expression cc.get_expression_image("am", "embarrassed01") as lgr_am_embarrassed01
    play voice3 girl22_disappointed_geh noloop
    am "Yeah. They're nothing special."
    mc "Still sounds cool."
    $ CharacterController.get_character("am").add_point(2)
    return
label q_inter_am_26:
    show expression cc.get_expression_image("am", "neutral01") as lst_am_neutral01
    play voice3 girl22_thinking_eeh noloop
    am "Uh."
    am "I keep thinking about things."
    mc "Alright. Do you... need help or something?"
    hide lst_am_neutral01
    show expression cc.get_expression_image("am", "annoyed01") as lst_am_annoyed01
    play voice3 girl22_no_high noloop
    am "No. It's just annoying. Thinking about other people doesn't usually occupy my brain so much."
    hide lst_am_annoyed01
    mct "Uh... is that some kind of strange April compliment?"
    $ CharacterController.get_character("am").add_point()
    return
label q_inter_am_27:
    show expression cc.get_expression_image("am", "neutral01") as lst_am_neutral01
    play voice3 girl22_thinking_eeh noloop
    am "I saw the report on the last ticket you did."
    am "Nice work, [mcname]."
    return
label q_inter_am_28:
    show expression cc.get_expression_image("am", "naughty01") as lst_am_naughty01
    play voice3 girl22_thinking_eeh noloop
    am "Hmmm."
    play voice2 mc_arrogant_heh1 noloop
    mc "Heh."
    hide lst_am_naughty01
    show expression cc.get_expression_image("am", "ask01") as lst_am_ask01
    play voice3 girl22_surprised_huh1 noloop
    am "What?"
    play voice2 mc_thinking_hmm1 noloop
    mc "I see you. Checking out your sexy worker bee again."
    mc "Don't think I don't see you."
    hide lst_am_ask01
    show expression cc.get_expression_image("am", "embarrassed01") as lst_am_embarrassed01
    play voice3 girl22_disappointed_geh noloop
    am "I think you're drinking too much Liquid Bull."
    $ CharacterController.get_character("am").add_point()
    return