label sm1cs_vs005i:
    $ LocationController.draw_current_location("vs")
    show expression cc.get_expression_image("vs", "excited01") as lth_vs_excited01
    play voice3 girl33_happy_wooh noloop
    vs "It finally went off, [mcname]."
    vs "Ths Blitz alert."
    play voice2 mc_happy_a1 noloop
    mc "Nice."
    vs "So... you want to come over to my dorm room real quick?"
    hide lth_vs_excited01
    show expression cc.get_expression_image("vs", "smile01") as lth_vs_smile01
    play voice3 girl33_happy_mmm noloop
    vs "I think you're going to love what I have in mind for your challenge."
    menu:
        "Yes":
            play voice2 mc_yes_yes1 noloop
            mc "Yes. Let's do it."
            jump sm1cs_vs005i_progress
        "What's the challenge?":
            $ player.set_choice("sm1cs_vs005i_what_is_the_challenge")
            play voice2 d1s2_hmm noloop volume 1.7
            mc "What is the challenge?"
            play voice3 girl33_happy_laugh6 noloop
            vs "No way. I'm not spoiling the surprise."
            vs "*giggles*"
            jump sm1cs_vs005i_progress
        "I'm busy right now" if not vn_mode:
            play voice2 d1s5b_ehhh noloop volume 1.7
            mc "Sorry, I'm a little busy right now."
            hide lth_vs_smile01
            show expression cc.get_expression_image("vs", "sad01")
            play voice3 girl33_disappointed_oh noloop
            vs "Oh, that's cool I guess."
            play voice2 mc_thinking_mmm3 noloop
            mc "I'm sorry, Veronica."
            play voice3 girl33_disappointed_mmf1 noloop
            vs "I know. But like... half the fun was that we would drop everything and have fun."
            vs "I guess I should reset the alert."
            jump sm1cs_vs005i_delay
label sm1cs_vs005i_progress:
    $ StoryController.end_scene(VS_STORY)
    return
label sm1cs_vs005i_delay:
    return