label sm1cs_km003_2i:
    $ LocationController.draw_current_location("km")
    if player.is_storyline_item_finished(THEATER_STORY_LINE, "sm1fs_t005"):
        show expression cc.get_expression_image("km", "annoyed01") as lth_km_annoyed01
        play voice2 d2s9_mchey noloop
        mc "Hey Kellie."
        play voice3 girl31_thinking_mmf1 noloop
        km "[mcname]."
        mc "So what do you think about the new show?"
        hide lth_km_annoyed01
        show expression cc.get_expression_image("km", "neutral01") as lth_km_neutral01
        play voice3 girl31_thinking_emm3 noloop
        km "I think it's too early to tell. But I'm glad Denise took my idea to make something like Romeo and Juliet."
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah, you looked excited about it."
        km "I guess so. But we'll see how it turns out when Denise shows us a script."
        mc "Why did you pick Romeo and Juliet? Are you a hopeless romantic?"
        hide lth_km_neutral01
        show expression cc.get_expression_image("km", "embarrassed01") as lth_km_embarrassed01
        play voice3 girl31_surprised_what3 noloop
        km "What? No. It's a classic play. It should be easy to add the elements the sponsor wants."
        play voice2 d9s2_ugu noloop
        mc "Cool."
        if False:
            play voice3 girl31_thinking_hmm1 noloop
            km "Even an amateur like yourself will manage it."
            play voice2 mc_arrogant_hm3 noloop
            mc "Gee, thanks."
            hide lth_km_embarrassed01
            show expression cc.get_expression_image("km", "neutral01") as lth_km_neutral01
            km "You know what I mean."
            km "Come on, I'm free. Let's do some more practice."
            mc "Uh..."
            km "Unless you're scared."
            mc "Of course not. I just have to make sure my health insurance still works."
            hide lth_km_neutral01
            show expression cc.get_expression_image("km", "laugh01") as lth_km_laugh01
            km "It won't be like last time, [mcname]."
            mc "Promise?"
            play voice3 girl31_happy_laugh1 noloop
            km "*soft chuckle*"
            play voice2 mc_hey_hey2 noloop
            mc "Kellie, do you promise?"
            jump sm1cs_km003_2i_end
        else:
            hide lth_km_embarrassed01
            show expression cc.get_expression_image("km", "laugh01") as lth_km_laugh01
            play voice3 girl31_thinking_hmm1 noloop
            km "And since it's easy, that means you might actually have a chance to become an actor for the show."
            km "How have you been doing with your training?"
    else:
        show expression cc.get_expression_image("km", "annoyed01") as lth_km_annoyed01
        play voice2 d2s9_mchey noloop
        mc "Hey Kellie."
        play voice3 girl31_thinking_mmf1 noloop
        km "[mcname]."
        mc "Everything alright?"
        hide lth_km_annoyed01
        show expression cc.get_expression_image("km", "neutral01") as lth_km_neutral01
        play voice3 girl31_thinking_emm3 noloop
        km "Well I've recovered from our last disaster together."
        km "If that's what you're asking."
        play voice2 d3s11b_mcheh noloop volume 1.6
        mc "Haha. Yeah. Veronica really is one of a kind, isn't she?"
        play voice3 girl31_arrogant_fff noloop
        km "Scoffs."
        hide lth_km_neutral01
        show expression cc.get_expression_image("km", "laugh01") as lth_km_laugh01
        play voice3 girl31_thinking_hmm1 noloop
        km "Let's talk about something else. How is your training to be an actor coming along?"
    jump sm1cs_km003_2i_menu
label sm1cs_km003_2i_menu:
    menu:
        "To be honest, I've been slacking. Lots of stuff going on."(hint="sm1cs_km003_2i_m01_h01"):
            call sm1cs_km003_2i_m01_c01 from _call_sm1cs_km003_2i_m01_c01
            play voice2 mc_disappointed_ah2 noloop
            mc "Sadly, I haven't been focusing on it too much, Kellie. Kind of forgot I guess."
            hide lth_km_laugh01
            show expression cc.get_expression_image("km", "angry01") as lth_km_angry01
            play voice3 girl31_arrogant_geh noloop
            km "How could you forget?!"
            play voice2 d2s9_confused noloop
            mc "I have a lot of stuff-"
            hide lth_km_angry01
            show expression cc.get_expression_image("km", "ask01") as lth_km_ask01
            play voice3 girl31_surprised_uh2 noloop
            km "Are you just planning to stay a stagehand forever?"
            play voice2 mc_no_no7 noloop
            mc "No, of course not."
            km "*sighs*"
            hide lth_km_ask01
        "I've been doing alright. But I could use help."(hint="sm1cs_km003_2i_m01_h02"):
            play voice2 mc_disappointed_ah2 noloop
            mc "I've been doing so-so, but I could probably use some help."
            mc "Being a stagehand is great. But..."
            hide lth_km_laugh01
            show expression cc.get_expression_image("km", "smile01") as lth_km_smile01
            play voice3 girl31_happy_laugh2 noloop
            km "Your soul hungers for the stage and lights."
            km "I know the feeling."
            hide lth_km_smile01
    show expression cc.get_expression_image("km", "curious01") as lth_km_curious01
    play voice3 girl31_arrogant_huh2 noloop
    km "How come you haven't asked me for help practicing anymore?"
    play voice2 mc_thinking_hmm2 noloop
    mc "Well, first, you kind of scare me."
    km "The theater should be scary."
    mc "Really?"
    hide lth_km_curious01
    show expression cc.get_expression_image("km", "smile01") as lth_km_smile01
    play voice3 girl31_no_fun noloop
    km "No. I mean, not really."
    km "But it should be intense. When you're up here, you're meant to be putting everything into your character and your lines."
    km "That's what the greats do. They practice for hours to make sure the end product is spectacular."
    menu:
        "Alright, let's do another lesson."(hint="sm1cs_km003_2i_m02_h01"):
            call sm1cs_km003_2i_m02_c01 from _call_sm1cs_km003_2i_m02_c01
            play voice2 mc_thinking_hmm3 noloop
            mc "If that's what it takes, maybe you can give me another lesson."
            hide lth_km_smile01
            show expression cc.get_expression_image("km", "neutral01") as lth_km_neutral01
            play voice3 girl31_yes_aga noloop
            km "Sure. I've got time."
        "Veronica doesn't seem to do that."(hint="sm1cs_km003_2i_m02_h02"):
            call sm1cs_km003_2i_m02_c02 from _call_sm1cs_km003_2i_m02_c02
            play voice2 mc_thinking_hmm3 noloop
            mc "I never get that feeling from Veronica. It's almost like this stuff just comes naturally to her."
            hide lth_km_smile01
            show expression cc.get_expression_image("km", "annoyed01") as lth_km_annoyed01
            play voice3 girl31_arrogant_hm1 noloop
            km "Hmph. Maybe, but natural talent only takes you so far."
            km "Practice makes perfect, as they say."
            play voice2 mc_yes_yeah2 noloop
            mc "Yeah, then how about you give me another lesson."
            hide lth_km_annoyed01
            show expression cc.get_expression_image("km", "neutral01") as lth_km_neutral01
            play voice3 girl31_yes_aga noloop
            km "Well... since you asked. Sure."
    if curr_sublocation != LTH_SUB_STAGE:
        play voice3 girl31_hey_interesting noloop
        km "Let's go to the main stage"
        play voice2 mc_yes_ugu1 noloop
        mc "Right."
    jump sm1cs_km003_2i_end
label sm1cs_km003_2i_end:
    $ StoryController.end_scene(KM_STORY)
    return
label sm1cs_km003_2i_m01_c01:
    $ player.set_choice("sm1cs_km003_2i_be_honest")
    return
label sm1cs_km003_2i_m02_c01:
    $ player.set_choice("sm1cs_km003_2i_another_lesson")
    $ CharacterController.get_character("km").add_point()
    return
label sm1cs_km003_2i_m02_c02:
    $ player.set_choice("sm1cs_km003_2i_vs_dont_do_it")
    $ CharacterController.get_character("km").deduct_point()
    return