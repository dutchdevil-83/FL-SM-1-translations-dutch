image sm1cs_km004-a136-glm = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a136-2x-50fps.webm", start_image = "sm1cs-km004-a136 vs-putting-on-clothes-glambot-00000", image = "sm1cs-km004-a136 vs-putting-on-clothes-glambot-00089", loop = False)
image sm1cs_km004-a204-glm = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a204-6x-30fps.webm", start_image = "sm1cs-km004-a204 mc-vs-entering-glambot-00", image = "sm1cs-km004-a204 mc-vs-entering-glambot-79", loop = False)
image sm1cs_km004-a208-1 = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a208-1-2x-50fps.webm", start_image = "sm1cs-km004-a208-1 km-masturbating-anim-01")
image sm1cs_km004-a208-1-f = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a208-1-2x-60fps.webm", start_image = "sm1cs-km004-a208-1 km-masturbating-anim-01")
image sm1cs_km004-a208-2 = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a208-2-2x-50fps.webm", start_image = "sm1cs-km004-a208-2 km-masturbating-anim-01")
image sm1cs_km004-a208-2-f = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a208-2-2x-60fps.webm", start_image = "sm1cs-km004-a208-2 km-masturbating-anim-01")
image sm1cs_km004-a208-3 = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a208-3-2x-50fps.webm", start_image = "sm1cs-km004-a208-3 km-masturbating-anim-01")
image sm1cs_km004-a208-3-f = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a208-3-2x-60fps.webm", start_image = "sm1cs-km004-a208-3 km-masturbating-anim-01")
image sm1cs_km004-a208-4 = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a208-4-2x-50fps.webm", start_image = "sm1cs-km004-a208-4 km-masturbating-anim-01")
image sm1cs_km004-a208-4-f = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a208-4-2x-60fps.webm", start_image = "sm1cs-km004-a208-4 km-masturbating-anim-01")
image sm1cs_km004-a215-1 = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a215-1-2x-50fps.webm", start_image = "sm1cs-km004-a215-1 km-moan-anim-01")
image sm1cs_km004-a215-1-f = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a215-1-2x-60fps.webm", start_image = "sm1cs-km004-a215-1 km-moan-anim-01")
image sm1cs_km004-a215-2 = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a215-2-2x-50fps.webm", start_image = "sm1cs-km004-a215-2 km-moan-anim-01")
image sm1cs_km004-a215-2-f = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a215-2-2x-60fps.webm", start_image = "sm1cs-km004-a215-2 km-moan-anim-01")
image sm1cs_km004-a215-3 = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a215-3-2x-50fps.webm", start_image = "sm1cs-km004-a215-3 km-moan-anim-01")
image sm1cs_km004-a215-3-f = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a215-3-2x-60fps.webm", start_image = "sm1cs-km004-a215-3 km-moan-anim-01")
image sm1cs_km004-a215-4 = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a215-4-2x-50fps.webm", start_image = "sm1cs-km004-a215-4 km-moan-anim-01")
image sm1cs_km004-a215-4-f = Movie(play = "images/FS_T/KM/s004/anim/sm1cs-km004-a215-4-2x-60fps.webm", start_image = "sm1cs-km004-a215-4 km-moan-anim-01")
label sm1cs_km004:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_impossible_mission
    scene sm1cs-km004-01 km-excited with dissolve
    play voice3 girl31_hey_excited noloop
    km "This is going to be great, [mcname]."
    menu:
        "Yeah, it's exciting."(hint="sm1cs_km004_m01_h01"):
            call sm1cs_km004_m01_c01 from _call_sm1cs_km004_m01_c01
            scene sm1cs-km004-02 mc-excited with dissolve
            play voice2 mc_yes_yeah2 noloop
            mc "Yeah, it's pretty exciting."
            scene sm1cs-km004-03 km-thanking with dissolve
            play voice3 girl31_disappointed_ehh1 noloop
            km "Thanks again for helping."
            scene sm1cs-km004-04 mc-sure with dissolve
            play voice2 mc_yes_sure1 noloop
            mc "Sure."
        "What is my role again?"(hint="sm1cs_km004_m01_h02"):
            pass
    scene sm1cs-km004-05 mc-asking with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "What is my role for the prank again?"
    scene sm1cs-km004-06 km-talking with dissolve
    play voice3 girl31_thinking_oh noloop
    km "Nothing major. I just need you to watch out for people."
    km "Make sure that the coast is clear. Stuff like that."
    scene sm1cs-km004-07 mc-okay with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay. Cool."
    scene sm1cs-km004-08 km-excited with dissolve
    play voice3 girl31_happy_laugh8 noloop
    km "I can't wait to hear her freaking out."
    scene sm1cs-km004-09 mc-concerned with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "But we're not hurting Veronica, right?"
    scene sm1cs-km004-10 km-evil with dissolve
    play voice3 girl31_no_laughing1 noloop
    km "Of course not. We just need to get her so embarrassed that she quits the group and regrets ever joining."
    scene sm1cs-km004-11 mc-shocked with dissolve
    pause
    scene sm1cs-km004-12 km-alright-alright with dissolve
    play voice3 girl31_disappointed_ehh2 noloop
    km "Okay, I just want to throw her off her game so that I get the lead in the next show."
    scene sm1cs-km004-13 mc-thanking with dissolve
    play voice2 d2s12_emmm noloop volume 1.6
    mc "Thank you. Much less, wicked witch vibe."
    scene sm1cs-km004-14 km-spotting with dissolve
    play voice3 girl31_thinking_hmm1 noloop
    km "Alright, here we go."
    scene sm1cs-km004-15 km-ordering with dissolve
    play voice3 girl31_yes_aga noloop
    km "You're up, [mcname]."
    km "Watch the door, I'll be done in two minutes."
    scene sm1cs-km004-16 mc-curious with dissolve
    play voice2 mc_surprised_how2 noloop
    mc "How do you know that?"
    scene sm1cs-km004-17 km-talking with dissolve
    play voice3 girl31_arrogant_ha noloop
    km "I practiced last night."
    play sound sfx_cloth_shuffle1
    scene sm1cs-km004-18 km-going-through-her-purse with dissolve
    menu:
        "This is harmless fun"(hint="sm1cs_km004_m02_h01"):
            call sm1cs_km004_m02_c01 from _call_sm1cs_km004_m02_c01
            scene sm1cs-km004-19 mc-watching with dissolve
            play voice2 d1s5_mcthinks noloop volume 1.5
            mct "No problem with a little harmless fun now and then."
            scene sm1cs-km004-20 mc-smiling with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mct "I never got to do any college pranks."
            scene sm1cs-km004-21 mc-thinking with dissolve
            play voice2 mc_thinking_mmm1 noloop
            mct "Then again I got to fuck some of my teachers, so maybe you either get to do one or the other..."
            scene sm1cs-km004-22 mc-thinking with dissolve
            play voice2 d14s16_smell noloop volume 0.8
            mct "A discussion for wiser men than I."
            mct "I wonder what she's doing over there with Veronica's purse."
        "I wish Kellie would just talk to Veronica"(hint="sm1cs_km004_m02_h02"):
            scene sm1cs-km004-23 mc-worried with dissolve
            play voice2 d14s16_smell noloop volume 0.8
            mct "I don't get Kellie."
            mct "Instead of just talking to Veronica about their differences, she thinks this is the right solution."
            scene sm1cs-km004-24 mc-thinking with dissolve
            play voice2 d1s5_mcthinks noloop volume 1.5
            mct "I can't say too much. I agreed to help after all."
            mct "Hopefully, if this doesn't work, maybe I can push Kellie to just talk things out with Veronica."
    play sound sfx_skirt_off2
    scene sm1cs-km004-25 km-messing-with-lipstick with dissolve
    pause
    scene sm1cs-km004-26 mc-curious with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "That's the prank? Mixing up her lipstick?"
    scene sm1cs-km004-27 km-laughing with dissolve
    play voice3 girl31_happy_laugh7 noloop
    km "She's such a ditz, she won't notice until it's too late."
    km "*evil chuckling*"
    scene sm1cs-km004-28 mc-fuck with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Crap. Someone is coming."
    mct "And Kellie isn't done yet."
    play sound sfx_heels_steps1 loop
    scene sm1cs-km004-29 tl-walking with dissolve
    play voice2 mc_angry_errr8 noloop
    mct "Shit. It's Taisia. Sounds like she's coming this way."
    stop sound fadeout 1.0
    scene sm1cs-km004-30 mc-whispering with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "*whispers* Kellie. Abort. Bad day. Pull the plug."
    scene sm1cs-km004-31 km-almost-done with dissolve
    play voice3 girl31_yes_yep noloop
    km "I've almost got it."
    scene sm1cs-km004-32 mc-hurry-up with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Come on. Taisia is coming."
    play sound sfx_cloth_shuffle1
    scene sm1cs-km004-33 km-stall-her with dissolve
    play voice3 girl31_arrogant_yeah2 noloop
    km "Well, stall her. That's your job. Just keep her outside."
    play sound sfx_door_open5
    scene sm1cs-km004-34 tl-opening-door with dissolve
    pause
    scene sm1cs-km004-35 mc-hey with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Hey, Taisia. What's up?"
    scene sm1cs-km004-36 tl-hey with dissolve
    play voice4 girl24_hey_simple noloop
    tl "Hey, [mcname]. Want to move aside? I need something."
    play sound sfx_door_creak4
    scene sm1cs-km004-37 mc-keeping-his-hand with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "You know, uh...."
    play sound2 sfx_cloth_shuffle1 volume 0.4
    scene sm1cs-km004-38 mc-looking-at-her with dissolve
    pause
    stop sound2 fadeout 1.0
    scene sm1cs-km004-39 km-figure-it-out with dissolve
    pause
    scene sm1cs-km004-40 mc-talking with dissolve
    play voice2 d1s5b_emmm noloop volume 1.7
    mc "You know, I just ripped a big one in here."
    mc "You should keep clear for a few minutes."
    scene sm1cs-km004-41 mc-nu-uh with dissolve
    play voice2 mc_disgust_ooh1 noloop
    mc "Trust me, you don't want none of this."
    scene sm1cs-km004-42 tl-asking with dissolve
    play voice4 girl24_surprised_huh1 noloop
    tl "Are you telling me..."
    tl "That you violated my dressing room..."
    play voice4 girl24_scared_ah7 noloop
    play sound sfx_skirt_off2
    scene sm1cs-km004-43 tl-asking-srsly with vpunch
    tl "With a fucking fart?"
    scene sm1cs-km004-44 mc-talking with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I mean, technically, it's {i}our{/i} dressing room."
    scene sm1cs-km004-45 tl-growling with dissolve
    play voice4 girl24_angry_err1 noloop
    tl "*low growling*"
    scene sm1cs-km004-46 mc-thinking with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "This is bad. We were just supposed to be pranking Veronica, but now Taisia is in the mix."
    scene sm1cs-km004-47 mc-talking with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Come on. Better out than in, right?"
    play sound sfx_cloth_rustling1
    scene sm1cs-km004-48 tl-sticking-up-a-finger with dissolve
    play voice4 girl24_no_simple1 noloop
    tl "No. Not when you share a room with girls."
    tl "Now move out of the way. I have to smell the damage."
    scene sm1cs-km004-49 mc-why with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What? Why?"
    play sound sfx_door_creak4
    scene sm1cs-km004-50 tl-angry with dissolve
    play voice4 girl24_angry_cough1 noloop
    tl "To see if this is a bannable offense, you uncivilized orge."
    if False:
        scene sm1cs-km004-51 tl-angry with dissolve
        play voice4 girl24_arrogant_hah noloop
        tl "I'll have no problem convincing Denise to bust you back down to stagehand."
        tl "And you'll be lucky enough to stay backstage after then."
        scene sm1cs-km004-52 mc-but with dissolve
        play voice2 mc_disappointed_off2 noloop
        mc "Oh, come on. It's just a-"
        scene sm1cs-km004-53 tl-angry with dissolve
        play voice4 girl24_angry_argh1 noloop
        tl "Don't even finish that sentence."
    else:
        scene sm1cs-km004-54 tl-angry with dissolve
        play voice4 girl24_arrogant_hah noloop
        tl "You don't really need a dressing room anyhow. You're a stagehand."
        tl "And you'll be lucky if I don't make it my life's work to keep you tied up backstage if this thing is a stinker and a lurker."
    play sound sfx_door_closed7 volume 1.6
    scene sm1cs-km004-55 tl-inside with dissolve
    pause
    stop music fadeout 6.0
    scene sm1cs-km004-56 tl-noticing-her with dissolve
    play voice4 girl24_surprised_what1 noloop
    tl "What's going on? It smells fine in here."
    tl "Nice even."
    scene sm1cs-km004-57 tl-angry with dissolve
    pause
    scene sm1cs-km004-58 km-hi with dissolve
    play voice3 girl31_hey_attention noloop
    km "Hi, Taisia. I was just getting something for Veronica. She asked me to get it from her purse."
    queue music music_impossible_fight
    scene sm1cs-km004-59 tl-thats-mine with dissolve
    play voice4 girl24_angry_cough2 noloop
    tl "Like hell you are."
    tl "That's my bag!"
    scene sm1cs-km004-60 km-whattttt with dissolve
    play voice3 girl31_surprised_huh3 noloop
    km "Yes but-"
    km "Your bag?{w} It was at Veronica's station."
    scene sm1cs-km004-61 tl-not-the-point with dissolve
    play voice4 girl24_angry_argh2 noloop
    tl "That's not the point. You're the one in the hot seat, not me."
    scene sm1cs-km004-62 mc-trying-to-leave with dissolve
    play voice2 d3s7_mcemm noloop volume 1.8
    mc "I should get going."
    scene sm1cs-km004-63 tl-no with dissolve
    play voice4 girl24_no_uhuh noloop
    tl "Not a chance, dick."
    scene sm1cs-km004-64 tl-no with dissolve
    play voice4 girl24_arrogant_hm1 noloop
    tl "Not till I get some answers."
    scene sm1cs-km004-65 mc-ow with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Ow."
    scene sm1cs-km004-66 km-explaining with dissolve
    play voice3 girl31_surprised_ah2 noloop
    km "It was just going to be a harmless prank."
    scene sm1cs-km004-67 tl-narrowing-eyes with dissolve
    play voice4 girl24_angry_geh noloop
    tl "{b}You{/b} were messing with {b}my{/b} makeup."
    scene sm1cs-km004-68 km-blaming-her with dissolve
    play voice3 girl31_disappointed_ehh3 noloop
    km "Again. You really shouldn't leave stuff on people's stations."
    scene sm1cs-km004-69 tl-youre-dead with dissolve
    play voice4 girl24_angry_argh5 noloop
    tl "That's it. You're dead."
    play sound sfx_cloth_planket2
    scene sm1cs-km004-70 km-mc-taking-cover with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "Whah-"
    scene sm1cs-km004-71 km-talking with dissolve
    play voice3 girl31_hey_angry noloop
    km "Let's just talk about this."
    scene sm1cs-km004-72 tl-fist-you with dissolve
    play voice4 girl24_yes_angry noloop
    tl "Sure. I hope you don't mind if I let my fists do the talking."
    scene sm1cs-km004-73 km-worried with dissolve
    play voice3 girl31_surprised_ah3 noloop
    km "Uh oh."
    play sound sfx_epic_jump1
    play voice4 girl24_angry_argh3 noloop
    play voice3 girl31_scared_oof2 noloop
    play voice2 mc_scared_huuuh3 noloop
    scene sm1cs-km004-74 km-mc-tl-montage with hpunch
    pause
    play voice4 girl24_angry_argh4 noloop
    play voice3 girl31_scared_ah7 noloop
    play voice2 mc_pain_ou3 noloop
    play sound sfx_leg_kick5
    play sound2 sfx_heels_run2
    scene sm1cs-km004-75 km-mc-tl-montage with vpunch
    tl "Come on. You're only making it worse."
    play voice4 girl24_angry_breath noloop
    play voice3 girl31_scared_ah2 noloop
    play sound sfx_cloth_shuffle1
    scene sm1cs-km004-76 km-mc-tl-montage with dissolve
    stop sound fadeout 3.5
    play voice2 mc_pain_argh1 noloop
    mc "I'm not really a part of this."
    stop sound2 fadeout 1.0
    scene sm1cs-km004-77 km-flattering with dissolve
    play voice3 girl31_scared_huh noloop
    km "Just chill, Taisia."
    km "You've got great taste in makeup, Taisia."
    scene sm1cs-km004-78 km-flattering with dissolve
    play voice3 girl31_surprised_oof1 noloop
    km "Very dark, and uh... intimidating."
    km "I just love your whole look."
    scene sm1cs-km004-79 tl-threatening with dissolve
    play voice4 girl24_surprised_oh1 noloop
    tl "Thanks. I'll give you some tips after I'm done with you."
    scene sm1cs-km004-80 mc-kl-amused with dissolve
    play voice4 girl24_arrogant_huh2 noloop
    tl "And just think of this, do you really think I won't just pound my way through [mcname] to get to you?"
    scene sm1cs-km004-81 kl-thinking with dissolve
    play voice3 girl31_surprised_uh1 noloop
    km "Uh... Yes, I suppose that is something to-"
    play voice3 girl31_angry_argh noloop
    play voice2 mc_pain_ou1 noloop
    play sound sfx_leg_kick7
    play sound2 sfx_epic_jump1 volume 2.0 noloop
    scene sm1cs-km004-82 kl-pushing with hpunch
    km "Consider!"
    play voice2 mc_pain_ou5 noloop
    play voice4 girl24_pain_ou1 noloop
    play sound sfx_leg_kick6
    scene sm1cs-km004-83 mc-tl-crashing with hpunch
    mc "Ah!"
    tl "Hey!"
    play sound sfx_heels_run2 loop
    play sound2 sfx_door_open1 noloop
    scene sm1cs-km004-84 kl-running with dissolve
    play voice3 girl31_happy_laugh6 noloop
    pause
    scene sm1cs-km004-85 tl-damnit with dissolve
    play voice4 girl24_angry_argh1 noloop
    tl "Dammit."
    play sound sfx_heels_run1
    scene sm1cs-km004-86 tl-yelling with dissolve
    play voice4 girl24_angry_mmm noloop
    tl "Come back here, you little pest."
    scene sm1cs-km004-87 tl-praising-her with dissolve
    play voice4 girl24_happy_laugh1 noloop
    tl "Man. Love her or hate her, she's got moves."
    scene sm1cs-km004-88 mc-agreeing with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Yes, she does."
    play sound sfx_cloth_rustling1
    scene sm1cs-km004-89 tl-accusing-him with dissolve
    play voice4 girl24_hey_angry noloop
    tl "You're not off the hook either, [mcname]."
    scene sm1cs-km004-90 mc-surprised with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Me?"
    scene sm1cs-km004-91 tl-warning with dissolve
    play voice4 girl24_yes_simple1 noloop
    tl "Yes. And if any part of this was your idea, I'm kicking your ass after hers."
    menu:
        "Bring it on"(hint="sm1cs_km004_m03_h01"):
            call sm1cs_km004_m03_c01 from _call_sm1cs_km004_m03_c01
            play sound sfx_cloth_rustling2
            scene sm1cs-km004-92 mc-bring-it with dissolve
            play voice2 mc_thinking_mmm6 noloop
            mc "Bring it on, Taisia."
            scene sm1cs-km004-93 tl-grinning with dissolve
            play voice4 girl24_arrogant_huh1 noloop
            tl "Heh."
        "Nope, it was all Kellie"(hint="sm1cs_km004_m03_h02"):
            call sm1cs_km004_m03_c02 from _call_sm1cs_km004_m03_c02
            scene sm1cs-km004-94 mc-nope with dissolve
            play voice2 mc_no_nope2 noloop
            mc "Nope. It was all Kellie."
            scene sm1cs-km004-95 tl-good with dissolve
            play voice4 girl24_disappointed_neh noloop
            tl "Good."
    play sound sfx_heels_steps1 loop
    scene sm1cs-km004-96 tl-leaving with dissolve
    pause
    stop sound fadeout 3.0
    scene sm1cs-km004-97 mc-thinking with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "That was close."
    mct "Now where did Kellie run off to?"
    stop music fadeout 5.0
    jump sm1cs_km004_warehouse
label sm1cs_km004_warehouse:
    scene sm1cs-km004-98 mc-walking with Fade(0.5, 0.5, 0.5)
    play sound sfx_heels_steps2 loop
    pause
    scene sm1cs-km004-98-02 mc-walking with dissolve
    pause
    play voice3 girl31_hey_high noloop
    play voice2 d6s1_pain noloop
    play music music_never_too_much
    play sound sfx_leg_kick7
    play sound2 sfx_cloth_tear1 noloop
    play sound3 sfx_sand_jump1 noloop volume 2.0
    scene sm1cs-km004-99 mc-km-jumpscare with vpunch
    mc "Ahh! Not the face."
    scene sm1cs-km004-100 mc-km-calm-down with dissolve
    play voice3 girl31_happy_laugh4 noloop
    km "Calm down. It's just me."
    play sound sfx_skirt_off2
    scene sm1cs-km004-101 mc-ugh with dissolve
    play voice2 mc_angry_off noloop
    mc "You say that like it's a good thing."
    mc "You screwed up, and now Taisia is out for blood."
    scene sm1cs-km004-102 km-talking with dissolve
    play voice3 girl31_arrogant_he noloop
    km "Hah. I've known her longer than you."
    km "Her bark is worse than her bite."
    scene sm1cs-km004-103 km-evil with dissolve
    play voice3 girl31_arrogant_hm1 noloop
    km "Plus, I know one of her weaknesses."
    scene sm1cs-km004-104 mc-oh with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, you do?"
    scene sm1cs-km004-105 km-grinning with dissolve
    play voice3 girl31_yes_yep noloop
    km "Yup. If you gave her a twenty, I bet she'd forget she ever saw us."
    scene sm1cs-km004-106 mc-unwilling with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I'm not willing to take that chance."
    scene sm1cs-km004-107 km-checking-left-and-right with dissolve
    play voice3 girl31_disappointed_ehh6 noloop
    km "It's fine. It's not important now."
    scene sm1cs-km004-108 km-checking-left-and-right with dissolve
    play voice3 girl31_thinking_hmm5 noloop
    km "What is important is that when I was running away, I figured out a new plan to prank Veronica."
    scene sm1cs-km004-109 km-smiling with dissolve
    play voice3 girl31_happy_yeah4 noloop
    km "And this one is guaranteed to work."
    menu:
        "What is this surefire plan?"(hint="sm1cs_km004_m04_h01"):
            call sm1cs_km004_m04_c01 from _call_sm1cs_km004_m04_c01
            scene sm1cs-km004-110 mc-asking with dissolve
            play voice2 mc_yes_okay1 noloop
            mc "Okay, what is this surefire plan?"
            scene sm1cs-km004-121 km-whispering with dissolve
            play voice3 amrose_old_psst2 noloop
        "I'm starting to get worried"(hint="sm1cs_km004_m04_h02"):
            scene sm1cs-km004-111 mc-too-much with dissolve
            play voice2 mc_disappointed_ehh5 noloop
            mc "I don't know. This whole thing is starting to feel a bit crazy."
            scene sm1cs-km004-112 km-reminding with dissolve
            play voice3 girl31_arrogant_huh1 noloop volume 0.8
            km "You said that you would help me, [mcname]."
            play sound sfx_hair_scratch1
            scene sm1cs-km004-113 mc-sighing with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.7
            mc "*sighs* I know that, but..."
            scene sm1cs-km004-114 km-defeated with dissolve
            play voice3 girl31_happy_relief noloop
            km "*sighs* It's fine..."
            km "It was a stupid idea anyway."
            km "I just..."
            scene sm1cs-km004-115 km-puppy-eyes with dissolve
            play voice3 girl31_pain_sobs1 noloop
            km "I need this, [mcname]."
            km "If I don't get a lead role soon, I think I'm going to be trapped playing second fiddle forever."
            scene sm1cs-km004-116 km-upset with dissolve
            km "..."
            scene sm1cs-km004-117 mc-fine with dissolve
            play voice2 mc_yes_okay1 noloop
            mc "Okay. We can do one more prank."
            scene sm1cs-km004-118 km-happy with dissolve
            play voice3 girl31_surprised_uh2 noloop
            km "Really?"
            scene sm1cs-km004-119 mc-yes with dissolve
            play voice2 mc_yes_yes2 noloop
            mc "Yes, just... Let's make extra sure everyone is far away when we do."
            scene sm1cs-km004-120 km-you-got-it with dissolve
            play voice3 girl31_happy_yay1 noloop
            km "You got it."
            scene sm1cs-km004-121 km-whispering with dissolve
            play voice3 amrose_old_psst2 noloop
            km "Here is the plan."
    km "*whispers*"
    jump sm1cs_km004_locker
label sm1cs_km004_locker:
    scene sm1cs-km004-122 km-mc-in-the-locker-room with Fade(0.5, 0.5, 0.5)
    play sound sfx_keys_open1
    pause
    scene sm1cs-km004-123 mc-thinking with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "I can think of a dozen ways this won't work."
    mct "At least we know Veronica won't be coming anytime soon. I can still hear the shower."
    play sound sfx_locker_open1
    scene sm1cs-km004-124 mc-km-asking with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "How did you learn to pick locks, again?"
    scene sm1cs-km004-125 km-secret with dissolve
    play voice3 girl31_arrogant_hm2 noloop
    km "Trade secret."
    scene sm1cs-km004-126 mc-uh-huh with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Uh-huh."
    play sound sfx_vending_door1
    scene sm1cs-km004-127 km-pulling-stuff-out with dissolve
    play voice3 girl31_angry_ergh1 noloop
    km "If these are mysteriously Taisia's clothes in Veronica's locker, I'm quitting."
    scene sm1cs-km004-128 mc-talking with dissolve
    play voice2 mc_no_no6 noloop
    mc "No, those are all very bubbly and distinctly non-Taisia."
    play sound sfx_skirt_off2
    scene sm1cs-km004-129 km-lets-go with dissolve
    play voice3 girl31_thinking_mmf1 noloop
    km "Good."
    scene sm1cs-km004-130 km-lets-go with dissolve
    play voice3 girl31_yes_yeah3 noloop
    km "Let's go."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    play sound3 sfx_door_open1 noloop
    scene sm1cs-km004-131 km-mc-going with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-km004-132 vs-coming with Fade(0.5, 0.5, 0.5)
    play sound sfx_vending_door1
    pause
    play sound2 sfx_cloth_wiping1
    scene sm1cs-km004-133 vs-hmm with dissolve
    play voice4 girl33_thinking_hmm1 noloop
    vs "Hmmm."
    scene sm1cs-km004-135 vs-looking-at-undies with dissolve
    pause
    stop sound2 fadeout 1.0
    scene sm1cs-km004-134 mc-km-vs-peeking with dissolve
    play voice4 girl33_surprised_huh4 noloop
    vs "How strange."
    vs "I swear I had more clothes in here than just these."
    play sound sfx_cloth_rustling3
    scene sm1cs-km004-a136 vs-putting-on-clothes-glambot-00000 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    scene sm1cs_km004-a136-glm
    pause
    play voice4 girl33_arrogant_laugh noloop
    vs "Oh well. I'm sure they'll turn up."
    scene sm1cs-km004-137 vs-done with dissolve
    pause
    scene sm1cs-km004-138 km-surprised with dissolve
    play voice3 girl31_surprised_ah1 noloop
    pause
    scene sm1cs-km004-139 mc-talking with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Uh, Kellie. She's coming this way."
    play sound sfx_door_closed7
    scene sm1cs-km004-140 km-baffled with dissolve
    play voice3 girl31_surprised_what3 noloop
    km "What is she doing? How is she not freaking out?"
    scene sm1cs-km004-139 mc-talking with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "We gotta move."
    scene sm1cs-km004-140 km-baffled with dissolve
    play voice3 girl31_angry_argh noloop
    km "But it doesn't make sense."
    km "What manner of beast is she?"
    jump sm1cs_km004_stage
label sm1cs_km004_stage:
    play sound sfx_heels_steps1 volume 0.6 loop fadein 3.0
    play sound2 sfx_heels_steps2 volume 0.6 fadein 3.0
    scene sm1cs-km004-141 km-mc-mainstage with Fade(0.5, 0.5, 0.5)
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-km004-142 ec-get-out with dissolve
    play voice6 girl32_hey_happy noloop
    ec "Hi, you two. Can you keep the stage clear? We're about to have a little practice with Veronica."
    scene sm1cs-km004-143 mc-np with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "Uh... sure."
    scene sm1cs-km004-144 km-sure with dissolve
    play voice3 girl31_yes_simple2 noloop
    km "No problem."
    scene sm1cs-km004-145 dvh-let-them-stay with dissolve
    play voice5 girl34_no_nah3 noloop
    dvh "No. They can stay. They'll be our audience."
    scene sm1cs-km004-146 dvh-where-is-she with dissolve
    play voice5 girl34_thinking_hmm7 noloop
    dvh "Now we just need our actress. She should be here already."
    scene sm1cs-km004-147 dvh-asking with dissolve
    play voice5 girl34_hey_simple3 noloop
    dvh "Have you two seen her?"
    scene sm1cs-km004-148 km-panicing with dissolve
    play voice3 girl31_surprised_huh1 noloop
    km "Who? Veronica. No, we haven't seen her. Nope."
    scene sm1cs-km004-149 mc-way-to-go with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "Great job, Kellie. Very natural."
    scene sm1cs-km004-150 dvh-about-to-say-something with dissolve
    pause
    play sound sfx_barefoot_steps1 volume 1.5
    scene sm1cs-km004-151 vs-entry with dissolve
    play voice4 girl33_hey_involved noloop
    vs "Here I am."
    stop sound fadeout 1.0
    scene sm1cs-km004-152 dvh-finally with dissolve
    play voice5 girl34_yes_ugu1 noloop
    dvh "Finally, we-"
    scene sm1cs-km004-153 mc-km-surprised with dissolve
    play voice2 mc_scared_huuuh1 noloop
    mc "..."
    play voice3 girl31_scared_ah3 noloop
    km "She..."
    scene sm1cs-km004-154 dvh-curious with dissolve
    play voice5 girl34_surprised_huh6 noloop
    dvh "What {b}is{/b} going on?"
    scene sm1cs-km004-155 vs-casually-taking-it with dissolve
    play voice4 girl33_disappointed_oh noloop
    vs "Oh nothing. My clothes just kind of wandered off. But I didn't want to be late."
    play sound sfx_hair_scratch1
    scene sm1cs-km004-156 dvh-sighing with dissolve
    play voice5 girl34_disappointed_eeh2 noloop
    dvh "It's fine."
    play sound sfx_paper_rustl2 volume 1.6
    scene sm1cs-km004-157 dvh-read-this with dissolve
    play voice5 girl34_thinking_hmm6 noloop
    dvh "Just... read the lines I highlighted for you."
    play sound sfx_paper_rustl1 volume 1.6
    scene sm1cs-km004-158 vs-sure with dissolve
    play voice4 girl33_yes_yeah noloop
    vs "Okay-dokey."
    scene sm1cs-km004-159 vs-hey with dissolve
    play voice4 girl33_hey_serious noloop
    vs "Oh hey, [mcname]. I didn't see you there."
    vs "Hey have you seen my clothes?"
    scene sm1cs-km004-160 mc-nope with dissolve
    play voice2 mc_no_nope1 noloop
    mc "Nope. Sorry, Veronica."
    scene sm1cs-km004-161 vs-its-ok with dissolve
    play voice4 girl33_no_nah noloop
    vs "That's okay. It's so strange."
    scene sm1cs-km004-162 dvh-asking with dissolve
    play voice5 girl34_angry_ahem4 noloop
    dvh "Ahem. If you please, Veronica."
    scene sm1cs-km004-163 vs-ok with dissolve
    play voice4 girl33_surprised_oh noloop
    vs "Oh right."
    scene sm1cs-km004-164 vs-rehersing with fade
    play voice4 girl33_disappointed_off noloop
    if player.has_played_scene("sm1fs_t005"):
        vs "What's Montague? It is nor hand nor foot."
        scene sm1cs-km004-165 vs-rehersing with dissolve
        play voice4 girl33_disappointed_mmf1 noloop
        vs "Nor arm nor face nor any other part."
    else:
        vs "Three days ago, I loathed you. I used to dream about you getting hit by a cab, or poisoned."
        scene sm1cs-km004-165 vs-rehersing with dissolve
        play voice4 girl33_disappointed_mmf1 noloop
        vs "Then we had our little adventure up in Alaska and things started to change."
    scene sm1cs-km004-166 vs-rehersing with dissolve
    if player.has_played_scene("sm1fs_t005"):
        play voice4 girl33_happy_relief noloop
        vs "Belonging to a man. Oh, be some other name!"
        scene sm1cs-km004-167 vs-rehersing with dissolve
        play voice4 girl33_thinking_hmm2 noloop
        vs "What's in a name? That which we call a rose"
        scene sm1cs-km004-168 vs-rehersing with dissolve
        play voice4 girl33_happy_mmm noloop
        vs "By any other word would smell as sweet."
    else:
        play voice4 girl33_happy_relief noloop
        vs "Things changed when we kissed. And when you told me about your tattoo."
        scene sm1cs-km004-167 vs-rehersing with dissolve
        play voice4 girl33_happy_laugh1 noloop
        vs "Even when you checked me out when we were naked."
    scene sm1cs-km004-169 dh-amazed with dissolve
    play voice5 girl34_surprised_ohmy1 noloop
    dvh "My god."
    scene sm1cs-km004-170 dh-clapping with dissolve
    play voice5 girl34_surprised_wow1 noloop
    dvh "Exquisite Veronica."
    dvh "Have you been practicing more?"
    scene sm1cs-km004-171 vs-talking with dissolve
    play voice4 girl33_no_nope noloop
    vs "Nope. Maybe it's because I'm just in my underwear."
    play sound sfx_hair_scratch1
    scene sm1cs-km004-172 vs-feeling-free with dissolve
    play voice4 girl33_happy_laugh2 noloop
    vs "We should all just do our scenes in our underwear. It feels so liberating."
    scene sm1cs-km004-173 dh-talking with dissolve
    play voice5 girl34_yes_aga3 noloop
    dvh "I'll keep that in mind."
    dvh "Alright, let's go over some more lines."
    play sound sfx_heels_run1
    scene sm1cs-km004-174 mc-watching-her-go with dissolve
    pause
    play sound2 sfx_heels_steps1
    scene sm1cs-km004-175 mc-walking with dissolve
    pause
    stop sound2 fadeout 1.0
    scene sm1cs-km004-176 km-baffled with dissolve
    play voice3 girl31_angry_breathing noloop
    km "I can't believe it. Not only is she not embarrassed by prancing around on the stage in a thong!"
    km "Denise thinks she's even better than normal because of it."
    km "God is laughing at me, [mcname]."
    scene sm1cs-km004-177 mc-talking with dissolve
    play voice2 mc_no_no5 noloop
    mc "God is not laughing at you, Kellie."
    mc "Veronica is just a very... special girl, I guess."
    scene sm1cs-km004-178 km-talking with dissolve
    play voice3 girl31_surprised_oof2 noloop
    km "There has to be something."
    km "What else can I do?"
    play voice3 girl31_surprised_oh noloop
    play sound sfx_cloth_rustling1
    scene sm1cs-km004-179 km-wait-a-min with vpunch
    km "Wait. I think I got it."
    play voice3 girl31_happy_yeah2 noloop
    scene sm1cs-km004-180 km-copycat with vpunch
    km "I'll fight fire with fire.{w} Yes..."
    scene sm1cs-km004-181 mc-thinking with dissolve
    play voice2 mc_angry_errr7 noloop
    mct "Oh this is not going to be good."
    scene sm1cs-km004-182 km-talking with dissolve
    play voice3 girl31_happy_mmm2 noloop
    km "I bet that the reason she's so comfortable with her own body is because other bodies make her super uncomfortable."
    km "That's gotta be her weakness.{w} That's how I'll break her."
    scene sm1cs-km004-183 mc-talking with dissolve
    play voice2 mc_disappointed_meh1 noloop
    mc "Kellie, listen. I'm sorry your other plans didn't work, but I think we're heading towards doing something you'll regret."
    scene sm1cs-km004-184 km-determined with dissolve
    play voice3 girl31_no_angry noloop
    km "No. It's going to work.{w} It has to work."
    scene sm1cs-km004-185 km-determined with dissolve
    play voice3 girl31_arrogant_nrgh noloop
    km "I know it will."
    play sound sfx_cloth_rustling2
    scene sm1cs-km004-186 km-talking with dissolve
    play voice3 girl31_happy_mmm1 noloop
    km "Give me twenty minutes, and then you need to go find Veronica."
    scene sm1cs-km004-187 mc-requesting with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Kellie please."
    scene sm1cs-km004-188 km-ignoring-him with dissolve
    play voice3 girl31_happy_nice3 noloop
    km "And then you bring her to the storage room."
    scene sm1cs-km004-189 mc-curious with dissolve
    play voice2 mc_surprised_why1 noloop
    mc "The storage room. Why?"
    scene sm1cs-km004-190 km-requesting with dissolve
    play voice3 girl31_disappointed_ehh9 noloop
    km "Please, [mcname]. Just trust me. I {b}need{/b} you to do it."
    km "Then we're done. I won't ask you for another favor."
    play sound sfx_hair_scratch1
    scene sm1cs-km004-191 mc-worried with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Okay. One last favor."
    play sound sfx_cloth_rustling4 volume 1.6
    scene sm1cs-km004-192 km-hugging with dissolve
    play voice3 girl31_happy_yay2 noloop
    km "Thank you!"
    scene sm1cs-km004-193 km-hugging with dissolve
    pause
    scene sm1cs-km004-194 km-ahem with dissolve
    play voice3 girl31_angry_cough1 noloop
    km "*ahem* Thank you."
    play sound sfx_heels_steps2 volume 1.5 loop
    scene sm1cs-km004-195 km-going with dissolve
    pause
    stop sound fadeout 3.0
    scene sm1cs-km004-196 mc-thinking with dissolve
    play voice2 d1s1_mmm noloop volume 1.5
    mct "What is up with these theater girls?"
    jump sm1cs_km004_later
label sm1cs_km004_later:
    scene black
    show screen scene_transistion("Twenty minutes later")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_heels_steps2 fadein 1.5
    play sound2 sfx_heels_steps1 fadein 1.5
    scene sm1cs-km004-197 mc-vs-together
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-km004-198 mc-vs-thanking with dissolve
    play voice4 girl33_hey_scared noloop
    vs "Thanks again for helping me find my clothes, [mcname]."
    scene sm1cs-km004-199 mc-awkward with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.5
    mc "Haha. Yeah... it was no big deal."
    scene sm1cs-km004-200 vs-asking with dissolve
    play voice4 girl33_arrogant_huh2 noloop
    vs "Now can you tell me what's up?"
    scene sm1cs-km004-201 mc-nope with dissolve
    play voice2 mc_no_no2 noloop
    mc "Not yet. Kellie wanted it to be a surprise."
    scene sm1cs-km004-202 mc-thinking with dissolve
    mct "For you and me I guess."
    scene sm1cs-km004-203 vs-excited with dissolve
    play voice3 girl33_happy_nice noloop
    vs "Nice. I love surprises."
    play sound sfx_door_open1
    scene sm1cs-km004-a204 mc-vs-entering-glambot-00 with dissolve
    pause
    stop sound2 fadeout 5.0
    play sound sfx_camera_fly2 volume 1.6
    scene sm1cs_km004-a204-glm
    pause
    stop sound fadeout 2.0
    scene sm1cs-km004-205 km-sitting with dissolve
    pause
    scene sm1cs-km004-206 vs-hmm with dissolve
    play voice4 girl33_thinking_hmm3 noloop
    vs "Hmmm. So mysterious."
    scene sm1cs-km004-207 mc-thinking with dissolve
    play voice2 mc_surprised_huh5 noloop
    mct "Holy shit. It's Kellie."
    mct "She's naked. And-"
    scene sm1cs-km004-a208-1 km-masturbating-anim-01 with dissolve
    pause
    scene sm1cs_km004-a208-1
    play sound sfx_vagina_penetration1 loop
    play voisex3 kanya_sex_openmoans1
    km "Mmwaah... Nuraahhh..."
    pause
    scene sm1cs_km004-a208-2 with dissolve
    play voice4 girl33_surprised_wow noloop
    vs "Woah."
    pause
    scene sm1cs_km004-a208-3 with dissolve
    pause
    scene sm1cs_km004-a208-4 with dissolve
    pause
    play sound3 sfx_door_open7 noloop volume 2.0
    "*door opening*"
    scene sm1cs_km004-a208-1-f with dissolve
    play voice2 mc_angry_huh1 noloop
    mct "As far as plans go, I definitely didn't see this coming."
    pause
    scene sm1cs_km004-a208-2-f with dissolve
    km "*light moaning*"
    pause
    scene sm1cs_km004-a208-3-f with dissolve
    pause
    scene sm1cs_km004-a208-4-f with dissolve
    pause
    play voisex3 girl31_hey_interesting noloop
    stop sound fadeout 1.0
    scene sm1cs-km004-209 km-hey with vpunch
    km "Hey there, Veronica..."
    play sound3 sfx_door_closed7 noloop
    "*door closing*"
    scene sm1cs-km004-210 vs-what-are-you-doing with dissolve
    play voice4 girl33_surprised_huh3 noloop
    vs "Kellie... what are you-"
    vs "I don't know what to say..."
    play sound sfx_cloth_shuffle1
    scene sm1cs-km004-211 km-taking-out-dildo with dissolve
    stop sound fadeout 1.5
    play voice3 girl31_happy_laugh1 noloop
    km "Now, every time you look at me..."
    scene sm1cs-km004-212 vs-surprised with dissolve
    play voice4 girl33_scared_oof noloop
    pause
    scene sm1cs-km004-213 km-talking with dissolve
    play voice3 girl31_angry_kghh2 noloop
    km "You're going to get distracted and think about this."
    scene sm1cs-km004-a215-1 km-moan-anim-01 with dissolve
    pause
    scene sm1cs_km004-a215-1
    play sound sfx_vagina_penetration1_fast loop
    play voisex3 kanya_sex_openmoans2
    km "Nuhaaaah..."
    pause
    scene sm1cs_km004-a215-2 with dissolve
    km "Yes. I hope this image is seared into your memory forever!"
    pause
    scene sm1cs_km004-a215-3 with dissolve
    pause
    scene sm1cs-km004-212 vs-surprised with dissolve
    play voice4 girl33_pain_aah1 noloop
    vs "Kellie, this...."
    vs "I mean."
    scene sm1cs_km004-a215-4 with dissolve
    km "*moaning*"
    pause
    scene sm1cs_km004-a215-1-f with dissolve
    play voice2 mc_angry_fuck3 noloop
    mct "Fuck me. I didn't think I'd ever see Kellie acting like this."
    pause
    scene sm1cs_km004-a215-2-f with dissolve
    mct "I mean, I know that Veronica likes to get freaky, but Kellie has always seemed chaste by comparison."
    pause
    scene sm1cs_km004-a215-3-f with dissolve
    pause
    scene sm1cs_km004-a215-4-f with dissolve
    pause
    play voice4 girl33_happy_yay noloop
    scene sm1cs-km004-210 vs-what-are-you-doing with hpunch
    vs "I love this new side of you."
    play voisex3 girl31_scared_ah9 noloop
    stop sound fadeout 1.0
    scene sm1cs-km004-217 km-shocked with vpunch
    km "Muhah... what?"
    scene sm1cs-km004-210 vs-what-are-you-doing with dissolve
    play voice4 girl33_happy_woohoo noloop
    vs "Rock on Kellie. I had no idea you were so kinky."
    scene sm1cs-km004-221 km-shocked with dissolve
    play voice3 girl31_no_angry noloop
    km "No. This isn't your one weakness?"
    scene sm1cs-km004-218 vs-what with dissolve
    play voice4 girl33_arrogant_huh1 noloop
    vs "Huh? Weakness?"
    play sound sfx_heels_steps2
    scene sm1cs-km004-219 vs-talking with dissolve
    play voice4 girl33_no_fun noloop
    vs "No, I love kinky stuff like this."
    scene sm1cs-km004-220 vs-smiling with dissolve
    play voice4 girl33_happy_laugh3 noloop
    vs "And I've already seen [mcname] naked, so now it's like I've got the full set after seeing you naked."
    play voice3 girl31_scared_ah4 noloop
    scene sm1cs-km004-221 km-shocked with vpunch
    km "Buh... I... I mean..."
    scene sm1cs-km004-222 vs-how-about-a-threesome with dissolve
    play voice4 girl33_surprised_ohmy noloop
    vs "Oh my god. What if we tried a threesome sometime?"
    scene sm1cs-km004-223 km-game-over with dissolve
    pause
    scene sm1cs-km004-224 vs-excited with dissolve
    play voice4 girl33_scared_oh noloop
    vs "Oh my god. We could make it a Blitz Alert!"
    play voice3 girl31_angry_cough3 noloop
    play sound sfx_bed_slide1
    scene sm1cs-km004-225 km-curious with hpunch
    km "What are you talking about?"
    play voice3 girl31_surprised_huh3 noloop
    scene sm1cs-km004-226 km-shocked with hpunch
    km "I can't. Wait... where are my clothes?"
    scene sm1cs-km004-227 tl-hey-there with dissolve
    play voice5 girl24_hey_greeting noloop
    tl "Looking for these?"
    play sound sfx_throw_something1
    scene sm1cs-km004-228 km-shy with dissolve
    play voice3 girl31_scared_ah1 noloop
    km "Ahaaah! Taisia. Give them back this instant."
    scene sm1cs-km004-229 tl-nope with dissolve
    play voice5 girl24_arrogant_yeah3 noloop
    tl "Yeah, I don't think so."
    tl "That will teach you for messing around with my stuff."
    play sound sfx_heels_run2 loop
    play voice5 girl24_happy_laugh5 noloop
    scene sm1cs-km004-230 tl-running with dissolve
    pause
    play sound2 sfx_barefoot_run1
    scene sm1cs-km004-231 km-running-behing-her with dissolve
    play voice3 girl31_pain_ah3 noloop
    km "Come back, right now!"
    stop sound fadeout 3.0
    stop sound2 fadeout 4.0
    scene sm1cs-km004-232 mc-vs-talking with dissolve
    play voice4 girl33_thinking_eem2 noloop
    vs "Mmmmm."
    vs "Did I just blank out for a minute, or did Taisia steal Kellie's clothes?"
    scene sm1cs-km004-233 mc-talking with dissolve
    play voice2 mc_no_no10 noloop
    mc "No, your eyes work fine. There is a naked Kellie running down the halls of the theater right now."
    scene sm1cs-km004-234 vs-realizing with dissolve
    play voice4 girl33_yes_aga noloop
    vs "Cool cool."
    vs "Oh, so Taisia must have taken my clothes too."
    scene sm1cs-km004-235 vs-laughing with dissolve
    play voice4 girl33_happy_laugh4 noloop
    vs "Hahaha. What a prankster."
    scene sm1cs-km004-236 mc-talking with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "You're taking this very well."
    scene sm1cs-km004-237 vs-grinning with dissolve
    play voice4 girl33_happy_laugh5 noloop
    vs "Haha. Hey, that's show business. You gotta be able to roll with the punches."
    play sound sfx_cloth_rustling2
    scene sm1cs-km004-238 vs-holding-her-stuff with dissolve
    pause
    play sound sfx_cloth_planket2
    scene sm1cs-km004-239 vs-talking with dissolve
    play voice4 girl33_happy_phew noloop
    vs "I better wash and clean this for Kellie."
    vs "Little \"thank you\" for the free show, hehe."
    play sound sfx_heels_steps2 loop
    scene sm1cs-km004-240 vs-bye with dissolve
    play voice4 girl33_hey_bye1 noloop
    vs "See you around, [mcname]."
    scene sm1cs-km004-241 mc-thinking with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Classic Veronica."
    stop sound fadeout 2.0
    scene sm1cs-km004-242 mc-thinking with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mct "I just hope that Taisia doesn't charge Kellie for the return of her clothes."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1cs_km004_end
label sm1cs_km004_end:
    call sm1cs_km004_unlocks from _call_sm1cs_km004_unlocks
    $ StoryController.end_scene(KM_STORY, 5, 0, 2)
    return
label sm1cs_km004_m01_c01:
    $ player.set_choice("sm1cs_km004_excited")
    return
label sm1cs_km004_m02_c01:
    $ player.set_choice("sm1cs_km004_harmless_fun")
    return
label sm1cs_km004_m03_c01:
    $ player.set_choice("sm1cs_km004_bring_it_on")
    $ CharacterController.get_character("tl").add_point()
    return
label sm1cs_km004_m03_c02:
    $ CharacterController.get_character("tl").deduct_point()
    return
label sm1cs_km004_m04_c01:
    $ player.set_choice("sm1cs_km004_surefire_plan")
    return
label sm1cs_km004_unlocks:
    $ CharacterController.get_character("km").add_schedule("shower_after_km004")
    return