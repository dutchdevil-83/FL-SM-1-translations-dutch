label sm1cs_km002:
    $ renpy.music.set_volume(0.6, 3.0, "freeroam_music1" )
    play sound sfx_heels_steps2 loop
    scene sm1cs-km002-01-km-dvh with dissolve
    pause
    scene sm1cs-km002-02-dvh-talk-mc with dissolve
    play voice4 girl34_hey_angry7 noloop
    dvh "You. [mcname], come here please."
    scene sm1cs-km002-03-mc-talk-dvh with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay."
    stop sound fadeout 1.0
    scene sm1cs-km002-04-dvh-talk with dissolve
    play voice4 girl34_arrogant_ha4 noloop
    dvh "Listen, I know you're new here, [mcname], so you might not know it, but in {i}my{/i} theater, we are supposed to carry ourselves with a bit of decorum."
    scene sm1cs-km002-05-mc-talk-dvh with dissolve
    play voice2 d1s2_hmm noloop volume 1.4
    mc "Decorum? Are you talking about decorations?"
    scene sm1cs-km002-06-dvh-talk-mc with dissolve
    play voice4 girl34_no_angry7 noloop
    dvh "No you... Ahem. Decorum means proper and polite behavior."
    scene sm1cs-km002-07-dvh-talk with dissolve
    play voice4 girl34_arrogant_hm1 noloop
    dvh "Something our dear, Kellie Moore forgot about."
    dvh "And I believe she has something she'd like to say to you."
    scene sm1cs-km002-08-km-looks-dvh with dissolve
    km "..."
    scene sm1cs-km002-09-dvh-talk-km with dissolve
    play voice4 girl34_no_nonono1 noloop
    dvh "No no. Take your time. Not like I'm trying to direct a theater or anything."
    scene sm1cs-km002-10-km-talk-mc with dissolve
    play voice3 girl31_disappointed_ehh3 noloop
    km "I'm very sorry for how I acted towards you. I didn't mean to hurt you, but it will never happen again."
    scene sm1cs-km002-11-dvh-talk-mc with dissolve
    play voice4 girl34_arrogant_huh1 noloop
    dvh "Stupendous. Everything good, [mcname]?"
    scene sm1cs-km002-12-mc-talk-dvh with dissolve
    play voice2 d2s12_emmm noloop volume 1.3
    mc "Well I-"
    play sound sfx_heels_steps1 loop
    scene sm1cs-km002-13-dvh-talk with dissolve
    play voice4 girl34_yes_aga8 noloop
    dvh "Wonderful. I knew you two could patch things up. Now if you'll excuse me, I have other matters to see to."
    stop sound fadeout 2.5
    scene sm1cs-km002-14-mc-km-talk with dissolve
    play voice2 d3s7_mcemm noloop
    play voice3 girl31_arrogant_nrgh noloop
    mc "You know-"
    km "I just-"
    scene sm1cs-km002-15-mc-talk with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "You go first."
    scene sm1cs-km002-16-km-talk-mc with dissolve
    play voice3 girl31_disappointed_ehh1 noloop
    km "*deep breath*"
    km "You know I wasn't actually trying to hurt you."
    scene sm1cs-km002-17-mc-talk-km with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "*scoffs* Could have fooled me."
    scene sm1cs-km002-18-km-talk-mc with dissolve
    play voice3 girl31_thinking_emm3 noloop
    km "In the end, I wanted you to be sure you had what it takes to be here with us."
    play voice2 mc_thinking_hmm1 noloop
    mc "That's not your decision, is it?"
    scene sm1cs-km002-19-km-talk-mc with dissolve
    play voice3 girl31_yes_cute noloop
    km "I already said I was worried. When we were training, I went a little over the top."
    km "It's happened to me before. Typical theater girl, getting overly dramatic at the worst possible time."
    scene sm1cs-km002-20-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Hmmm. Guess she just wants to move forward."
    mct "But should I let her off that easily?"
    menu:
        "Ask her if that was her apologizing"(hint="sm1cs_km002_m01_h01"):
            call sm1cs_km002_m01_c01 from _call_sm1cs_km002_m01_c01
            jump sm1cs_km002_push_km
        "Compliment her energy"(hint="sm1cs_km002_m01_h02"):
            call sm1cs_km002_m01_c02 from _call_sm1cs_km002_m01_c02
            jump sm1cs_km002_complement_km
        "I am ready for more lessons"(hint="sm1cs_km002_m01_h03"):
            call sm1cs_km002_m01_c03 from _call_sm1cs_km002_m01_c03
            jump sm1cs_km002_ready_for_more
label sm1cs_km002_push_km:
    scene sm1cs-km002-21-c1-mc-talk-km with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Uh... was that really the best apology you could come up with after beating me up with a sword?"
    scene sm1cs-km002-22-c1-km-talk-mc with dissolve
    play voice3 girl31_hey_angry noloop
    km "It was a wooden prop sword, and I didn't beat you up. I held back a lot."
    km "I've trained in all kinds of stage fighting, [mcname]. If I wanted to beat you up, you'd still be limping."
    scene sm1cs-km002-23-c1-km-talk-mc with dissolve
    play voice3 girl31_disappointed_ehh2 noloop
    km "*sighs* I really am sorry for how I acted. Not just because Denise made me apologize."
    scene sm1cs-km002-24-c1-mc-talk-km with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Apology accepted. And... I think you would have come to your senses before smashing my face if Veronica and Denise didn't show up."
    scene sm1cs-km002-25-c1-mc-talk-km with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Uh, right, Kellie?"
    scene sm1cs-km002-26-c1-km-talk-mc with dissolve
    play voice3 girl31_yes_excited noloop
    km "Yes. Totally, and I promise it will never happen again."
    km "We're supposed to be a team here at the theater. All-for-one style."
    km "Not beat up on the new guy because of how-"
    scene sm1cs-km002-27-c1-mc-talk-km with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "How what?"
    scene sm1cs-km002-28-c1-km-talk-mc with dissolve
    play voice3 girl31_thinking_emm2 noloop
    km "Never mind that. Look, are you still interested in trying to become a better actor?"
    scene sm1cs-km002-29-c1-mc-talk-km with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "That's what I'm here for."
    scene sm1cs-km002-30-c1-km-talk-mc with dissolve
    play voice3 girl31_thinking_hmm1 noloop
    km "Good."
    jump sm1cs_km002_after_choice
label sm1cs_km002_complement_km:
    scene sm1cs-km002-31-c2-mc-talk-km with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's all good, Kellie. You were impressive in the battle."
    mc "You were probably drawing on something you really hate to get into the zone."
    scene sm1cs-km002-32-c2-km-talk-mc with dissolve
    play voice3 girl31_yes_excited noloop
    km "Something like that."
    scene sm1cs-km002-33-c2-mc-talk-km with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I bet you've had a bunch of roles as the hero or a powerful warrior in some of the shows here."
    scene sm1cs-km002-34-c2-km-talk-mc with dissolve
    play voice3 girl31_no_simple noloop
    km "Not as many as you'd think. Lately, Veronica has taken all the lead roles."
    play voice2 mc_thinking_hmm3 noloop
    mc "Never say never."
    scene sm1cs-km002-35-c2-km-talk-mc with dissolve
    play voice3 girl31_disappointed_ehh6 noloop
    km "I guess. I... I appreciate you being so understanding about earlier, [mcname]."
    km "It won't happen again."
    km "And maybe we can just... act like it never happened?"
    menu:
        "We're cool, Kellie"(hint="sm1cs_km002_m02_h01"):
            call sm1cs_km002_m02_c01 from _call_sm1cs_km002_m02_c01
            scene sm1cs-km002-36-c2-mc-talk-km with dissolve
            play voice2 mc_yes_yeah2 noloop
            mc "Yeah. We're cool, Kellie."
            scene sm1cs-km002-37-c2-km-talk-mc with dissolve
            play voice3 girl31_happy_nice3 noloop
            km "Thanks. I really appreciate that."
        "Yeah, maybe"(hint="sm1cs_km002_m02_h02"):
            scene sm1cs-km002-36-c2-mc-talk-km with dissolve
            play voice2 mc_yes_yeah3 noloop
            mc "Yeah. Maybe."
    scene sm1cs-km002-38-c2-km-talk-mc with dissolve
    play voice3 girl31_surprised_oh noloop
    km "[mcname], are you still interested in learning to be a better actor."
    scene sm1cs-km002-39-c2-mc-talk-km with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure, if you're still down to teach me."
    scene sm1cs-km002-40-c2-km-talk-mc with dissolve
    play voice3 girl31_yes_simple1 noloop
    km "I am."
    jump sm1cs_km002_after_choice
label sm1cs_km002_ready_for_more:
    scene sm1cs-km002-41-c3-mc-talk-km with dissolve
    play voice2 mc_no_nah1 noloop
    mc "Nah, it wasn't too much for me. I'm down to learn more, if you have the time."
    scene sm1cs-km002-42-c3-km-talk-mc with dissolve
    play voice3 girl31_arrogant_huh2 noloop
    km "Really?"
    scene sm1cs-km002-43-c3-mc-talk-km with dissolve
    menu:
        "Joke"(hint="sm1cs_km002_m03_h01"):
            call sm1cs_km002_m03_c01 from _call_sm1cs_km002_m03_c01
            play voice2 mc_angry_off noloop
            mc "What kind of actor would I be if I quit after one disastrous lesson?"
            scene sm1cs-km002-44-c3-km-talk-mc with dissolve
            play voice3 girl31_happy_laugh1 noloop
            km "I guess it was kind of a disaster."
        "Neutral"(hint="sm1cs_km002_m03_h02"):
            play voice2 mc_yes_yes7 noloop
            mc "Totally. I've come here to learn how to master the stage."
            scene sm1cs-km002-45-c3-mc-inner-talk with dissolve
            play voice2 mc_thinking_mmm1 noloop
            mct "And maybe screen one day."
            scene sm1cs-km002-43-c3-mc-talk-km with dissolve
            play voice2 mc_thinking_hmm4 noloop
            mc "I want you to teach me. Unless you don't think you're up to the challenge."
            scene sm1cs-km002-46-km-talk-mc with dissolve
            play voice3 girl31_thinking_oh noloop
            km "Oh I'm up to the challenge of teaching {i}you{/i}, [mcname]."
    jump sm1cs_km002_after_choice
label sm1cs_km002_after_choice:
    scene sm1cs-km002-47-km-talk-mc with dissolve
    play voice3 girl31_thinking_mmm6 noloop
    km "But allow me to share one crucial thing about me before we go any further."
    scene sm1cs-km002-48-km-talk-mc with dissolve
    play voice3 girl31_disappointed_mff1 noloop
    km "The theater has been my life for years, and I take it very seriously."
    km "And I don't stomach fools."
    km "The stage gives us a chance to bare the deepest shades of humanity into the world."
    scene sm1cs-km002-49-km-talk-mc with dissolve
    play voice3 girl31_arrogant_hm1 noloop
    km "If you're not prepared to give this your all, you should find another teacher."
    scene sm1cs-km002-50-km-talk-mc with dissolve
    play voice3 girl31_surprised_uh1 noloop
    km "So, are you sure you're prepared?"
    scene sm1cs-km002-51-mc-talk-km with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Okay-dokey."
    scene sm1cs-km002-52-km-talk-mc with dissolve
    play voice3 girl31_happy_relief noloop
    km "*sighs*"
    km "Good. Then the first thing you should do is get a copy of {u}An Actor Prepares{/u} by Constantin Stanislavsky."
    km "Do not return to me without reading the first two chapters. Is that clear?"
    scene sm1cs-km002-53-mc-talk-km with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Uh... sounds doable."
    scene sm1cs-km002-54-km-talk-mc with dissolve
    play voice3 girl31_angry_cough1 noloop
    km "Then what are you standing around for? Go. Now."
    scene sm1cs-km002-55-mc-talk-km with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Yes ma'am!"
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    jump sm1cs_km002_end
label sm1cs_km002_end:
    $ StoryController.end_scene(KM_STORY, 1, 0, 2)
    return
label sm1cs_km002_m01_c01:
    $ player.set_choice("sm1cs_km002_push_km")
    return
label sm1cs_km002_m01_c02:
    $ player.set_choice("sm1cs_km002_complement_km")
    $ CharacterController.get_character("km").add_point()
    return
label sm1cs_km002_m01_c03:
    $ player.set_choice("sm1cs_km002_ready_for_more")
    $ CharacterController.get_character("km").add_point(2)
    return
label sm1cs_km002_m02_c01:
    $ player.set_choice("sm1cs_km002_km_cool")
    $ CharacterController.get_character("km").add_point()
    return
label sm1cs_km002_m03_c01:
    $ player.set_choice("sm1cs_km002_joke")
    $ CharacterController.get_character("km").deduct_point(2)
    return