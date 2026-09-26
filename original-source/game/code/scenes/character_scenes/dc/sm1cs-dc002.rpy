label sm1cs_dc002:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.6, 0.0, "sound4" )
    play sound4 sfx_parknight_crickets
    $ renpy.music.play(audio.music_midnightcreep1_calm, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_midnightcreep1_active, "music2", True, None, True, 0.0)
    scene sm1cs-dc002-02 mc-dc-walk1_c1 with dissolve
    play sound sfx_footsteps_grass2 loop volume 0.7
    play voice2 d1s5_mcthinks noloop
    mct "That lady cop said I should keep an eye out for that creep."
    scene sm1cs-dc002-02 mc-dc-walk1_c2 with dissolve
    mct "I wonder what he's doing here late at night..."
    stop sound fadeout 1.0
    scene sm1cs-dc002-03 mc-dc-walk2_c1 with dissolve
    play voice2 mc_surprised_huh8 noloop
    mct "Wait, is that him over there?"
    scene sm1cs-dc002-03 mc-dc-walk2_c2 with dissolve
    pause
    scene sm1cs-dc002-04 mc-dc-hide1_c2 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mct "I think..."
    play sound sfx_nature_bushes1
    scene sm1cs-dc002-05 mc-dc-hide2_c1 with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "That's the creep! It has to be. Who else wears a trench coat to a park?"
    mct "Shit. What do I do now? Do I call someone? Tackle him?"
    mct "What if he isn't wearing clothes under that trench coat? Or has a knife or something?"
    scene sm1cs-dc002-05 mc-dc-hide2_c2 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "I can probably take him. Right?"
    mct "Okay, do I sneak up on him? Do I charge? Maybe like a full on bull rush-"
    play voice3 girl36_angry_cough noloop
    play sound sfx_throw_something1
    scene sm1cs-dc002-05-2 mc-dc-hide3_c1 with hpunch
    play voice2 mc_scared_huh1 noloop
    "???" "Freeze, dirtbag."
    scene sm1cs-dc002-05-2 mc-dc-hide3_c2 with dissolve
    play voice3 girl36_angry_hmm noloop
    "???" "Now turn around. {i}Slowly.{/i}"
    play voice2 mc_thinking_mmm3 noloop
    mct "Please, don't tell me I have a purty mouth. Please don't tell me-"
    play sound sfx_footsteps_grass2
    scene sm1cs-dc002-06 mc-dc-talk1_c2 with dissolve
    stop sound fadeout 1.0
    play voice3 girl36_surprised_what1 noloop
    dc "Wait... It's you!"
    scene sm1cs-dc002-06 mc-dc-talk1_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yep, just little old me..."
    scene sm1cs-dc002-07 mc-dc-talk2_c2 with dissolve
    play voice3 girl36_surprised_huh1 noloop
    dc "[mcname], right? What the hell are you doing here?"
    scene sm1cs-dc002-07 mc-dc-talk2_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Well you said to keep an eye out for anything suspicious, so I thought I'd come and look and-"
    scene sm1cs-dc002-08 mc-dc-talk3_c2 with dissolve
    play voice3 girl36_angry_rrr noloop
    dc "Damn. I thought I had you dead to rights. I really needed this..."
    scene sm1cs-dc002-11 mc-dc-walk1_c1 with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "I'm pretty sure the guy you're looking for is over there."
    scene sm1cs-dc002-11 mc-dc-walk1_c2 with dissolve
    play voice3 girl36_surprised_what2 noloop
    dc "What!?"
    scene sm1cs-dc002-10 mc-dc-talk5_c2 with dissolve
    play voice3 girl36_surprised_ohmy2 noloop
    dc "You're right, I think that's him!"
    scene sm1cs-dc002-08 mc-dc-talk3_c1 with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "What should we do?"
    scene sm1cs-dc002-08 mc-dc-talk3_c2 with dissolve
    play voice3 girl36_surprised_huh2 noloop
    dc "{i}We?{/i}{w} When did we become a {i}we{/i}?"
    play voice2 mc_thinking_oh1 noloop
    mc "I just figured, since I'm here..."
    scene sm1cs-dc002-06 mc-dc-talk1_c2 with dissolve
    play voice3 girl36_no_angry1 noloop
    dc "We aren't going to do anything. {i}I{/i} am going to try and apprehend the suspect. You should stay here."
    scene sm1cs-dc002-06 mc-dc-talk1_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "But I can help!"
    dc "..."
    menu:
        "Suggest cutting him off"(hint="sm1cs_dc002_m01_h01"):
            scene sm1cs-dc002-11 mc-dc-walk1_c1 with dissolve
            play voice2 mc_arrogant_huh3 noloop
            mc "What if I sneak around towards one of the exits? I can try and block him from making an escape."
            scene sm1cs-dc002-11 mc-dc-walk1_c2 with dissolve
            play voice3 girl36_angry_errr noloop
            dc "Absolutely not! Gah, if you are going to insist on helping, you'll be my backup."
        "Offer to be her backup"(hint="sm1cs_dc002_m01_h02"):
            call sm1cs_dc002_m01_c02 from _call_sm1cs_dc002_m01_c02
            scene sm1cs-dc002-11 mc-dc-walk1_c1 with dissolve
            play voice2 mc_thinking_hmm7 noloop
            mc "What about backup?"
            scene sm1cs-dc002-11 mc-dc-walk1_c2 with dissolve
            play voice3 girl36_arrogant_huh1 noloop
            dc "Huh?"
            play voice2 d2s9_confused noloop
            mc "You know, backup. Everyone needs a partner, right?"
            play voice3 girl36_angry_ugh2 noloop
            dc "Fine, you can be my backup."
    scene sm1cs-dc002-12 mc-dc-walk2_c1 with dissolve
    play sound sfx_footsteps_grass2 loop
    play voice3 girl36_angry_breath noloop
    dc "We'll try and sneak closer, and then we'll rush him!"
    play voice2 mc_yes_aga1 noloop
    mc "Sounds like a plan to me!"
    scene sm1cs-dc002-13 mc-dc-walk2-2_c1 with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mct "I was kind of right! I needed to bum rush him {i}and{/i} sneak closer!"
    scene sm1cs-dc002-13 mc-dc-walk2-2_c2 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "This is exciting!"
    scene sm1cs-dc002-14 mc-dc-walk3_c2 with dissolve
    play voice3 girl36_arrogant_huh3 noloop
    dc "What, catching a creep?"
    play sound sfx_heels_steps1 loop
    scene sm1cs-dc002-15 mc-dc-walk4_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, being on my very first police stakeout! Or... I guess this isn't a stakeout."
    play sound sfx_nature_bushes1
    scene sm1cs-dc002-16 mc-dc-sit1_c2 with dissolve
    queue sound sfx_nature_bushes2
    play voice3 stacy_shhh noloop
    dc "Shhh, we're getting close."
    scene sm1cs-dc002-17 mc-dc-sit2_c1 with dissolve
    play voice2 d1s2_hey noloop
    mc "Hey, I've been meaning to ask; why is this guy creeping around the park?"
    scene sm1cs-dc002-18 mc-dc-sit3_c2 with dissolve
    mct "I guess that answers my question. I'll need to remember to come back and check her out when I'm not doing police work."
    scene sm1cs-dc002-17 mc-dc-sit2_c2 with dissolve
    play voice3 girl36_arrogant_hm noloop
    dc "Now's our chance!"
    play sound sfx_sand_fallen1
    play voice3 girl36_hey_scandalized noloop
    scene sm1cs-dc002-19 mc-dc-stand1_c1 with hpunch
    dc "FREEZE, DIRTBAG!"
    play voice2 mc_pain_mff5 noloop
    mct "Jesus, give me more warning!"
    scene sm1cs-dc002-19 mc-dc-stand1_c2 with dissolve
    pause
    play sound sfx_footsteps_grass2 loop
    scene sm1cs-dc002-20 mc-dc-stand2_c1 with dissolve
    pause
    scene sm1cs-dc002-20 mc-dc-stand2_c2 with dissolve
    play voice3 girl36_angry_cough noloop
    dc "You are under-"
    play voice4 boy9_angry_breath3 noloop
    "Creep" "You'll never take me alive, coppers!"
    play voice3 girl36_angry_argh4 noloop
    $ renpy.music.set_volume(1.0, 1.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound sfx_grass_run1 loop
    play sound2 sfx_footsteps_grass1
    with hpunch
    dc "I SAID FREEZE!"
    play voice3 girl36_pain_ergh noloop
    scene sm1cs-dc002-21 mc-dc-run1_c1 with hpunch
    pause
    scene sm1cs-dc002-21 mc-dc-run1_c2 with dissolve
    pause
    play voice2 d7s4_mcbreathing
    play sound2 sfx_stone_run1
    scene sm1cs-dc002-22 mc-dc-run2_c1 with dissolve
    pause
    play sound sfx_heels_run1 loop
    scene sm1cs-dc002-20 mc-dc-stand3_c3 with dissolve
    menu:
        "Stay Focused"(hint="sm1cs_dc002_m02_h01"):
            call sm1cs_dc002_m02_c01 from _call_sm1cs_dc002_m02_c01
            scene sm1cs-dc002-22 mc-dc-run2_c2 with dissolve
            play voice2 mc_angry_errr1 noloop
            mct "Focus, [mcname], focus! You're on the job!"
            scene sm1cs-dc002-22 mc-dc-run2_c3 with dissolve
            pause
            scene sm1cs-dc002-23 mc-dc-run3_c2 with dissolve
            pause
            scene sm1cs-dc002-24 mc-dc-run4_c2 with dissolve
            play voice3 girl36_angry_argh1 noloop
            pause
            scene sm1cs-dc002-25 mc-dc-run5_c2 with dissolve
            pause
            scene sm1cs-dc002-25 mc-dc-run5_c3 with dissolve
            play voice3 girl36_scared_huh5 noloop
            pause
            scene sm1cs-dc002-26 mc-dc-run6_c2 with dissolve
            pause
        "Check out the nude jogger"(hint="sm1cs_dc002_m02_h02"):
            scene sm1cs-dc002-23 mc-dc-run3_c1 with dissolve
            play voice2 mc_thinking_hmm9 noloop
            mct "A little peek couldn't hurt..."
            scene sm1cs-dc002-23 mc-dc-run3_c3 with dissolve
            play voice3 girl36_angry_argh1 noloop
            pause
            play sound sfx_fall_mud1
            scene sm1cs-dc002-24 mc-dc-run4_c1 with dissolve
            play voice2 mc_scared_huh1 noloop
            pause
            play voice2 mc_pain_ou6 noloop
            play sound sfx_fall_down1
            scene sm1cs-dc002-25 mc-dc-run5_c1 with hpunch
            pause
            play sound sfx_heels_run1 loop
            scene sm1cs-dc002-24 mc-dc-run4_c2 with dissolve
            pause
            scene sm1cs-dc002-25 mc-dc-run5_c2 with dissolve
            pause
            scene sm1cs-dc002-25 mc-dc-run5_c3 with dissolve
            play voice3 girl36_scared_huh5 noloop
            pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-dc002-26 mc-dc-run6_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mct "Shit - I think I need to hit a gym."
    play sound sfx_heels_run2 loop volume 0.5
    scene sm1cs-dc002-27 mc-dc-run7_c1 with dissolve
    play voice2 d7s4_mcbreathing
    mct "I'm failing Rule Number One right now; cardio! God, Maybe we should get a treadmill for the studio..."
    stop sound fadeout 1.0
    scene sm1cs-dc002-28 mc-dc-stand1_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Don't... Worry... About me... I'll... Catch up!..."
    $ renpy.music.set_volume(0.0, 5.0, "music2" )
    $ renpy.music.set_volume(0.2, 5.0, "music" )
    scene sm1cs-dc002-29 mc-dc-stand2_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.4
    mc "Did ya'... Get him?"
    play sound sfx_heels_steps1 loop
    scene sm1cs-dc002-29 mc-dc-stand2_c2 with dissolve
    play voice3 girl36_no_angry2 noloop
    dc "No... The dirtbag is slipperier than I thought he was. Wiggled his way through a fence that I wouldn't fit through."
    stop sound fadeout 1.0
    scene sm1cs-dc002-30 mc-dc-talk1_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Drats, partner... We'll get him... Next time!"
    scene sm1cs-dc002-30 mc-dc-talk1_c2 with dissolve
    play voice3 girl36_arrogant_huh2 noloop
    dc "Next time?"
    scene sm1cs-dc002-31 mc-dc-talk2_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah! I won't rest... Until the Midnight Creep is caught!"
    scene sm1cs-dc002-31 mc-dc-talk2_c2 with dissolve
    play voice3 girl36_happy_laugh1 noloop
    dc "Midnight Creep, I like that."
    if player.get_choice("sm1cs_dc002_stay_focused") is False:
        scene sm1cs-dc002-32 mc-dc-talk3_c2 with dissolve
        play voice3 girl36_hey_happy noloop
        dc "What happened to you? One second you were right behind me, and the next you had disappeared."
        scene sm1cs-dc002-32 mc-dc-talk3_c1 with dissolve
        play voice2 d2s12_emmm noloop
        mc "My... Uhm... Shoelaces were untied?"
        play voice3 girl24_arrogant_kgh2 noloop
        dc "Uh huh, sure they were."
    scene sm1cs-dc002-33 mc-dc-talk4_c2 with dissolve
    play voice3 girl36_arrogant_yeah3 noloop
    dc "But we need to get you into the gym to do more cardio if you want to keep up with me."
    scene sm1cs-dc002-33 mc-dc-talk4_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "Me? Oh no, I am a paragon of fitness!"
    play voice2 mc_pain_argh1 noloop
    play sound sfx_cloth_planket2
    scene sm1cs-dc002-34 mc-dc-pain_c1 with hpunch
    mc "Ouch! Stitch, stitch, stitch!"
    scene sm1cs-dc002-34 mc-dc-pain_c2 with dissolve
    play voice3 girl36_arrogant_laugh noloop
    dc "Come on, paragon. You need some potassium. I've got some in my bag."
    scene sm1cs-dc002-37 mc-dc-stand1_c2 with fade
    play sound sfx_cloth_rustling5
    pause
    scene sm1cs-dc002-37 mc-dc-stand1_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "You just leave that here?"
    scene sm1cs-dc002-38 mc-dc-stand2_c2 with dissolve
    play sound sfx_cloth_rustling3
    play voice3 girl36_arrogant_yeah1 noloop
    dc "When I'm on a stakeout, yeah. Can't be lugging this along with me."
    play sound sfx_skirt_off1
    scene sm1cs-dc002-39 mc-dc-stand3_c2 with dissolve
    play voice3 girl36_thinking_hmm noloop
    dc "Here."
    scene sm1cs-dc002-40 mc-dc-talk1_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "'Is that a banana in your pocket, or are you just happy to see me.'"
    scene sm1cs-dc002-40 mc-dc-talk1_c2 with dissolve
    play voice3 girl36_scared_huh1 noloop
    dc "It's just the banana!"
    scene sm1cs-dc002-41 mc-dc-talk2_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.3
    mct "Huh... I didn't think that would get that kind of a reaction..."
    mc "Sorry, lame joke. But I do have a degree in{w} joke-ology!"
    scene sm1cs-dc002-41 mc-dc-talk2_c2 with dissolve
    play voice3 girl36_happy_laugh3 noloop
    dc "That's pretty good!"
    scene sm1cs-dc002-42 mc-dc-talk3_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Thanks! And thank you for the banana. Seriously, I thought that cramp was going to be the end of me."
    scene sm1cs-dc002-42 mc-dc-talk3_c2 with dissolve
    play voice3 girl36_arrogant_yeah2 noloop
    dc "And I was serious too. If you want to join me more often, you'll need to hit the gym."
    if player.get_choice("sm1cs_dc002_backup") is True:
        dc "Partner."
    play sound sfx_heels_steps1 loop volume 0.7
    scene sm1cs-dc002-43 mc-dc-walk1_c1 with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "As long as you teach me your cardio routine!"
    scene sm1cs-dc002-43 mc-dc-walk1_c2 with dissolve
    play voice3 girl36_disappointed_aah noloop
    dc "And listen, sorry for scaring you earlier.{w} And calling you a dirtbag."
    play voice2 mc_no_nah2 noloop
    mc "It's okay, don't worry about it. You're trying to stop a creep from harassing women, and I love women! Don't even think twice about it."
    dc "Good. But I owe you one for helping out."
    scene sm1cs-dc002-43 mc-dc-walk1_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I'll have to take you up on that."
    play voice3 girl36_yes_aga noloop
    dc "Please do! I, uh, don't have any ideas right now of how to pay you back, but I'll think of something!"
    scene sm1cs-dc002-43 mc-dc-walk1_c2 with dissolve
    play voice3 girl36_disappointed_eeh noloop
    dc "But I should get home. Technically I'm not on duty right now."
    dc "But you can always find me on the park beat. Don't be a stranger!"
    scene sm1cs-dc002-44 mc-dc-walk2_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I won't!"
    scene sm1cs-dc002-44 mc-dc-walk2_c2 with dissolve
    pause
    stop sound fadeout 1.5
    stop sound4 fadeout 1.5
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(DC_STORY, 0, 50, 2)
    return
label sm1cs_dc002_m01_c02:
    $ player.set_choice("sm1cs_dc002_backup")
    $ CharacterController.get_character("dc").add_point()
    return
label sm1cs_dc002_m02_c01:
    $ player.set_choice("sm1cs_dc002_stay_focused")
    $ CharacterController.get_character("dc").add_point()
    return
label sm1cs_dc002_unlocks:
    call sm1cs_dc002_m01_c02 from _call_sm1cs_dc002_m01_c02_1
    call sm1cs_dc002_m02_c01 from _call_sm1cs_dc002_m02_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(DC_STORY)
    return