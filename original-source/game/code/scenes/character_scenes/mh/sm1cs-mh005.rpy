image sm1cs_mh005-a145-1 = Movie(play = "images/Character-Scenes/mh/s005/anim/sm1cs-mh005-a145-1-2x-50fps.webm", start_image = "sm1cs-mh005-a145-1 mc-mh-bj-anim-01")
image sm1cs_mh005-a145-1-f = Movie(play = "images/Character-Scenes/mh/s005/anim/sm1cs-mh005-a145-1-2x-60fps.webm", start_image = "sm1cs-mh005-a145-1 mc-mh-bj-anim-01")
image sm1cs_mh005-a145-2 = Movie(play = "images/Character-Scenes/mh/s005/anim/sm1cs-mh005-a145-2-2x-50fps.webm", start_image = "sm1cs-mh005-a145-2 mc-mh-bj-anim-01")
image sm1cs_mh005-a145-2-f = Movie(play = "images/Character-Scenes/mh/s005/anim/sm1cs-mh005-a145-2-2x-60fps.webm", start_image = "sm1cs-mh005-a145-2 mc-mh-bj-anim-01")
image sm1cs_mh005-a145-3 = Movie(play = "images/Character-Scenes/mh/s005/anim/sm1cs-mh005-a145-3-2x-50fps.webm", start_image = "sm1cs-mh005-a145-3 mc-mh-bj-anim-01")
image sm1cs_mh005-a145-3-f = Movie(play = "images/Character-Scenes/mh/s005/anim/sm1cs-mh005-a145-3-2x-60fps.webm", start_image = "sm1cs-mh005-a145-3 mc-mh-bj-anim-01")
label sm1cs_mh005:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.6, 1.0, "music" )
    $ renpy.music.set_volume(1.0, 1.0, "sound3" )
    play sound3 sfx_casino_ambience1 fadein 3.0
    play sound sfx_heels_steps1 loop fadein 1.0
    scene sm1cs-mh005-00 whats_on_second with dissolve
    play music retro_nostalgy
    pause
    scene sm1cs-mh005-01 whats_on_second_mh_talk with dissolve
    play voice3 lissa_oh2 noloop
    mh "The arcade?"
    scene sm1cs-mh005-02 whats_on_second_mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yep! I thought it would be nice."
    scene sm1cs-mh005-03 whats_on_second_mh_talk with dissolve
    play voice3 lissa_haha2 noloop
    mh "I wouldn't mind kicking your ass in air hockey again."
    scene sm1cs-mh005-04 whats_on_second_mc_talk with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "It won't be as easy this time. I've been practicing."
    scene sm1cs-mh005-05 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "Oh have you now?"
    mh "You'll have to show me these new skills of yours then."
    scene sm1cs-mh005-06 whats_on_second_mh_talk_walktotable with dissolve
    pause
    scene sm1cs-mh005-07 whats_on_second_mc_talk_follow with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Oh don't you worry. I'm going to being it."
    $ renpy.music.set_volume(0.4, 5.0, "sound3" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    stop sound fadeout 1.0
    play sound2 sfx_airhockey_hum fadein 1.0 volume 0.5
    scene sm1cs-mh005-08 whats_on_second_mc_talk_at_table with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I promised you maximum effort."
    scene sm1cs-mh005-09 whats_on_second_mh_talk_at_table with dissolve
    play voice3 lissa_aga noloop
    mh "Less talking, and more showing, [mcname]."
    scene sm1cs-mh005-10 whats_on_second_mh_talk_bothgrab with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "I'll give you first serve."
    play sound sfx_airhockey_smash2
    scene sm1cs-mh005-11 whats_on_second_mc_talk_smile with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.6
    mc "Sounds good to me."
    play sound sfx_airhockey_smash3
    scene sm1cs-mh005-12 whats_on_second_mc_hits with dissolve
    pause
    play sound sfx_airhockey_score1
    scene sm1cs-mh005-13 whats_on_second_puck_goesin with hpunch
    pause
    play voice3 dahlia_surprised_huh2 noloop
    scene sm1cs-mh005-14 whats_on_second_mh_talkmpressed with dissolve
    pause
    play voice2 mc_happy_laugh2 noloop volume 1.3
    scene sm1cs-mh005-15 whats_on_second_mh_talk_mc_smiles with dissolve
    pause
    play sound sfx_vending_cola
    scene sm1cs-mh005-16 whats_on_second_mh_talk_puts_puck with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    mh "You weren't bluffing about practicing."
    mh "I guess I'll also have to bring my A game."
    play sound sfx_airhockey_smash1
    scene sm1cs-mh005-17 whats_on_second_mh_talk_hits with vpunch
    pause
    play voice2 mc_scared_huh1 noloop
    play sound sfx_airhockey_score2
    scene sm1cs-mh005-18 whats_on_second_mh_tall_goesin with hpunch
    pause
    play voice2 mc_angry_errr7 noloop
    scene sm1cs-mh005-19 whats_on_second_mc_focused with dissolve
    pause
    scene sm1cs-mh005-25 whats_on_second_mh_talk with dissolve
    play voice3 lissa_ha noloop
    mh "Looks like it's one to one, now."
    play sound sfx_cup_slide1 volume 1.3
    scene sm1cs-mh005-27 whats_on_second_mc_puck with dissolve
    pause
    play sound sfx_airhockey_smash4
    scene sm1cs-mh005-20 whats_on_second_mc_hit with hpunch
    pause
    play sound sfx_airhockey_smash5
    scene sm1cs-mh005-21 whats_on_second_mh_hit with hpunch
    pause
    play sound sfx_airhockey_smash1
    scene sm1cs-mh005-22 whats_on_second_mc_block with hpunch
    pause
    play sound sfx_airhockey_smash3
    scene sm1cs-mh005-23 whats_on_second_mh_returns with hpunch
    pause
    play voice2 mc_pain_rrrr noloop
    play sound sfx_airhockey_score3
    scene sm1cs-mh005-24 whats_on_second_mh_scores with hpunch
    pause
    scene sm1cs-mh005-25 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_disgust_oof noloop
    mh "Two unanswered points. Maybe you should have practiced more."
    scene sm1cs-mh005-26 whats_on_second_mc_talk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "The game has just started."
    play sound sfx_cup_slide1 volume 1.3
    scene sm1cs-mh005-27 whats_on_second_mc_puck with dissolve
    pause
    play sound sfx_airhockey_smash1
    scene sm1cs-mh005-28 whats_on_second_mc_hit with hpunch
    pause
    play voice3 nora_huh noloop
    play sound sfx_airhockey_score1
    scene sm1cs-mh005-29 whats_on_second_mc_score with hpunch
    pause
    play voice2 mc_thinking_mmm7 noloop
    scene sm1cs-mh005-30 whats_on_second_mc_smile with dissolve
    pause
    play voice3 lissa_moan8 noloop
    scene sm1cs-mh005-31 whats_on_second_sliding_past_mh
    play sound sfx_airhockey_score2
    with hpunch
    pause
    play voice2 mc_pain_ou6 noloop
    scene sm1cs-mh005-32 whats_on_second_sliding_past_mc
    play sound sfx_airhockey_score3
    with hpunch
    pause
    play voice3 nora_arghh noloop
    scene sm1cs-mh005-33 whats_on_second_sliding_past_mh
    play sound sfx_airhockey_score1
    with hpunch
    pause
    scene sm1cs-mh005-34 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_arrogant_ha noloop
    mh "Tied game, 5 to 5. You're doing better this time."
    scene sm1cs-mh005-35 whats_on_second_mc_talk with dissolve
    play voice2 mc_yes_yes6 noloop volume 0.8
    mc "I'm trying."
    scene sm1cs-mh005-44 whats_on_second_take position with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "But holy shit, I forgot how good Lyssa was at air hockey..."
    scene sm1cs-mh005-36 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_arrogant_huh noloop
    mh "How about we make things more interesting?"
    scene sm1cs-mh005-37 whats_on_second_mc_talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, proposing a bet?"
    scene sm1cs-mh005-38 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_yes_yeah3 noloop
    mh "Maybe... If I win... You need to get us the first round of drinks."
    scene sm1cs-mh005-39 whats_on_second_mc_talk with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "Hmmm... And if I win..."
    menu:
        "The drinks are on you"(hint="sm1cs_mh005_m01_h01"):
            scene sm1cs-mh005-40 whats_on_second_mc_talk_menu with dissolve
            play voice2 mc_happy_a1 noloop
            mc "And I would like my drink with ice."
            scene sm1cs-mh005-41 whats_on_second_mh_talk_menu with dissolve
            play voice3 dahlia_disappointed_hmm1 noloop
            mh "Oh, confident are we?"
        "I would like a kiss"(hint="sm1cs_mh005_m01_h02"):
            call sm1cs_mh005_m01_c02 from _call_sm1cs_mh005_m01_c02
            scene sm1cs-mh005-40 whats_on_second_mc_talk_menu with dissolve
            play voice2 mc_happy_a1 noloop
            mc "Just a little kiss. Nothing crazy."
            scene sm1cs-mh005-41 whats_on_second_mh_talk_menu with dissolve
            play voice3 dahlia_disappointed_hmm1 noloop
            mh "Uh huh. Smooth operator over there, I see."
    mh "But first, you have to win."
    scene sm1cs-mh005-42 whats_on_second_mc_talk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Easy."
    scene sm1cs-mh005-43 whats_on_second_mh_talk with dissolve
    play voice3 lissa_laugh2 noloop
    mh "Oh ho ho. Show me, then."
    scene sm1cs-mh005-44 whats_on_second_take position with dissolve
    pause
    jump sm1cs_mh005_after_game
label sm1cs_mh005_after_game:
    play sound [sfx_airhockey_smash4, sfx_airhockey_score2]
    scene sm1cs-mh005-45 whats_on_second_mc_talk_tied with Fade(0.3, 0.5, 0.3)
    play voice2 mc_happy_oof1 noloop
    mc "Tied game. 9 to 9."
    scene sm1cs-mh005-46 whats_on_second_mh_talk_tied with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    mh "You have learned, my young padawan. But you have not yet earned the title of master."
    scene sm1cs-mh005-47 whats_on_second_mc_talk with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Soon, the student will become the teacher."
    scene sm1cs-mh005-48 whats_on_second_mh_narrow_eyes with dissolve
    pause
    play sound sfx_vending_cola
    scene sm1cs-mh005-49 whats_on_second_mc_thought_puckdown with dissolve
    play voice2 d1s1_mmm noloop
    mct "I think I can win this. But should I?"
    menu:
        "Let Lyssa win"(hint="sm1cs_mh005_m02_h01"):
            call sm1cs_mh005_m02_c01 from _call_sm1cs_mh005_m02_c01
            mct "Maybe... I'll just take a little off the top. Not throw the game, but..."
            play sound sfx_airhockey_smash1
            scene sm1cs-mh005-50 whats_on_second_mc_hits_puck with hpunch
            pause
            play sound sfx_airhockey_smash2
            scene sm1cs-mh005-51 whats_on_second_mh_blocks with hpunch
            pause
            play sound sfx_airhockey_smash3
            scene sm1cs-mh005-52 whats_on_second_mc_returns with hpunch
            pause
            play voice3 nora_huh noloop
            play sound sfx_airhockey_smash1
            scene sm1cs-mh005-53 whats_on_second_mh_blocks_barely with hpunch
            pause
            play voice2 mc_surprised_huh8 noloop
            play sound sfx_airhockey_score1
            scene sm1cs-mh005-54 whats_on_secondf_lyssa_wins with hpunch
            pause
        "Try and win it all"(hint="sm1cs_mh005_m02_h02"):
            mct "Time to win this... I can do it..."
            play sound sfx_airhockey_smash1
            scene sm1cs-mh005-50 whats_on_second_mc_hits_puck with hpunch
            pause
            play sound sfx_airhockey_smash2
            scene sm1cs-mh005-51 whats_on_second_mh_blocks with hpunch
            pause
            play sound sfx_airhockey_smash3
            scene sm1cs-mh005-52 whats_on_second_mc_returns with hpunch
            pause
            play sound sfx_airhockey_smash1
            scene sm1cs-mh005-53 whats_on_second_mh_blocks_barely with hpunch
            pause
            play voice2 mc_arrogant_huh2 noloop
            play sound sfx_airhockey_smash2
            scene sm1cs-mh005-55 whats_on_second_else_mc_blocks with hpunch
            pause
            play sound sfx_airhockey_score1
            scene sm1cs-mh005-56 whats_on_second_else_past_mh with hpunch
            play voice3 nora_huh noloop
            pause
    scene sm1cs-mh005-57 whats_on_second_mc_talk_lookup with dissolve
    play voice2 mc_thinking_mmm6 noloop volume 1.6
    mc "Well it looks like that's the game."
    scene sm1cs-mh005-58 whats_on_second_mh_talk_lookup with dissolve
    play voice3 lissa_yes noloop
    mh "That is does. Good game, [mcname]."
    scene sm1cs-mh005-60 whats_on_second_mv_talk_look with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "Now to the winner go the spoils."
    if player.get_choice("sm1cs_mh005_let_mh_win"):
        mh "Even if you threw the game a little bit."
        scene sm1cs-mh005-61 whats_on_second_mc_talkf_win with dissolve
        play voice2 mc_surprised_what3 noloop
        mc "What!? I would never!"
        mct "Holy shit, she is observant."
        scene sm1cs-mh005-62 whats_on_second_mh_talkf_win with dissolve
        play voice3 dahlia_thinking_hmm4 noloop
        mh "Would you check to see if they have anything diet?"
        play sound sfx_heels_steps1 loop
        scene sm1cs-mh005-63 whats_on_second_mc_talkf_win with dissolve
        play voice2 mc_yes_sure1 noloop
        mc "Of course."
        play voice3 lissa_thinking1 noloop volume 1.6
        mh "And, [mcname]?"
        play voice2 mc_yes_yeah8 noloop
        mc "Yeah?"
        play sound4 sfx_cloth_rustling1 noloop
        scene sm1cs-mh005-64 whats_on_second_mh_kissf_win with dissolve
        play voice3 lissa_moan1 noloop
        play voice2 mc_thinking_mmm2 noloop
        play sound dahlia_kiss_french1
        pause
        scene sm1cs-mh005-65 whats_on_second_mh_kissf_win with dissolve
        play sound mc_kiss2
        pause
        scene sm1cs-mh005-66 whats_on_second_mh_talkf_win with dissolve
        play voice3 dahlia_disappointed_ehh3 noloop
        mh "I decided I also wanted a kiss for winning. That okay?"
        scene sm1cs-mh005-67 whats_on_second_mc_talkf_win_smiles with dissolve
        play voice2 mc_yes_yes2 noloop
        mc "Always."
    else:
        if player.get_choice("sm1cs_mh005_kiss"):
            mh "I believe someone asked for a kiss."
            scene sm1cs-mh005-61 whats_on_second_mc_talkf_win with dissolve
            play voice2 mc_yes_yes2 noloop
            mc "I might have..."
            scene sm1cs-mh005-62 whats_on_second_mh_talkf_win with dissolve
            play voice3 dahlia_disappointed_ehh3 noloop
            mh "Who am I to deny such a request?"
            scene sm1cs-mh005-64 whats_on_second_mh_kissf_win with dissolve
            play voice3 lissa_moan1 noloop
            play voice2 mc_thinking_mmm2 noloop
            play sound dahlia_kiss_french1
            pause
            scene sm1cs-mh005-65 whats_on_second_mh_kissf_win with dissolve
            play sound mc_kiss2
            pause
            scene sm1cs-mh005-67 whats_on_second_mc_talkf_win_smiles with dissolve
            play voice2 d1s5_mchappy noloop volume 2.0
            mc "I think that's worth a couple of drinks. Something diet?"
            scene sm1cs-mh005-66 whats_on_second_mh_talkf_win with dissolve
            play voice3 dahlia_yes_ugu noloop
            mh "Yes, please."
        else:
            scene sm1cs-mh005-61 whats_on_second_mc_talkf_win with dissolve
            play voice2 mc_arrogant_hm1 noloop
            mc "I'll take mine with light ice, please."
            scene sm1cs-mh005-62 whats_on_second_mh_talkf_win with dissolve
            play voice3 dahlia_thinking_hmm3 noloop
            mh "Anything else?"
            play voice2 mc_thinking_hmm6 noloop
            mc "Hmmm... Not off the top of my head."
            mh "Can I make a request?"
            play sound sfx_heels_steps1 loop
            scene sm1cs-mh005-63 whats_on_second_mc_talkf_win with dissolve
            play voice2 mc_yes_yeah8 noloop
            mc "Of course, Lyssa."
            play sound4 sfx_cloth_rustling1 noloop
            scene sm1cs-mh005-64 whats_on_second_mh_kissf_win with dissolve
            play voice3 lissa_moan1 noloop
            play voice2 mc_thinking_mmm2 noloop
            play sound dahlia_kiss_french1
            pause
            scene sm1cs-mh005-65 whats_on_second_mh_kissf_win with dissolve
            play sound mc_kiss2
            pause
            scene sm1cs-mh005-67 whats_on_second_mc_talkf_win_smiles with dissolve
            play voice2 mc_surprised_oh1 noloop
            mc "That wasn't really a request..."
            scene sm1cs-mh005-66 whats_on_second_mh_talkf_win with dissolve
            play voice3 lissa_shyoh noloop
            mh "Oh, so I shouldn't have done it?"
            scene sm1cs-mh005-69 whats_on_second_mc_talkf_win with dissolve
            play voice2 mc_no_no5 noloop
            mc "That's not what I said."
            scene sm1cs-mh005-70 whats_on_second_mh_talkf_win with dissolve
            play voice3 lissa_thinking1 noloop volume 1.4
            mh "Good. I'll-"
            scene sm1cs-mh005-71 whats_on_second_mc_talkf_win with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "Oh no. For a kiss that good, I'll go get the drinks. Diet, right?"
            scene sm1cs-mh005-72 whats_on_second_mh_talk_hmm with dissolve
            play voice3 lissa_ugu3 noloop
            mh "Mmhmmm."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh005-73 whats_on_second_mc_walks_for_drinks with dissolve
    pause
    stop sound fadeout 1.5
    stop sound2 fadeout 1.5
    $ renpy.music.set_volume(0.2, 1.5, "sound3" )
    $ renpy.music.set_volume(0.45, 2.5, "music" )
    scene sm1cs-mh005-74 whats_on_second_mh_talk_sitting with fade
    play voice3 dahlia_thinking_hmm2 noloop
    mh "Wow, I'm just realizing that when we walked in I zeroed in on the air hockey table and didn't even ask you about your day."
    scene sm1cs-mh005-75 whats_on_second_mc_talk_sitting with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "That's okay! I was pretty excited about air hockey too."
    scene sm1cs-mh005-76 whats_on_second_mh_talk_sitting with dissolve
    play voice3 lissa_haha noloop
    mh "Well, how are things at... The studio."
    scene sm1cs-mh005-77 whats_on_second_mc_talk_sitting with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Good! Busy. I have been real busy."
    scene sm1cs-mh005-78 whats_on_second_mh_talk_sitting with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh, a lot of... shoots, or..."
    scene sm1cs-mh005-79 whats_on_second_mc_talk_sitting with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Oh, shooting isn't the part of my job that makes me busy."
    scene sm1cs-mh005-80 whats_on_second_mh_talk_surprised with dissolve
    play voice3 nora_huh noloop
    mh "Really?"
    scene sm1cs-mh005-81 whats_on_second_mc_talk_surprised with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Uh huh. It's all of the other stuff. Hiring people, figuring out equipment and coming up with ideas to film."
    mc "And Stacy is keeping busy with location stuff, along with props and wardrobe."
    scene sm1cs-mh005-79 whats_on_second_mc_talk_sitting with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "And that's not even getting into distribution and markets, and-"
    mc "Sorry, I will drone on all night about this if you let me. The short version is, there's a lot of things to do when you run a porn studio."
    scene sm1cs-mh005-82 whats_on_second_mh_talk_thoughtful with dissolve
    play voice3 dahlia_arrogant_heh noloop
    mh "Huh..."
    scene sm1cs-mh005-83 whats_on_second_mc_talk_thoughtful with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "What?"
    scene sm1cs-mh005-84 whats_on_second_mh_talk_thoughtful with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "I just... Never imagined that running a... studio like yours would make you so busy."
    scene sm1cs-mh005-85 whats_on_second_mc_talk_thoughtful with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah... Honestly, I didn't either."
    scene sm1cs-mh005-86 whats_on_second_mc_talk_smiles with dissolve
    play voice2 mc_happy_a1 noloop
    mc "But I like it. I really enjoy this work."
    mc "Which reminds me! I don't know if I ever thanked you for helping out with that paperwork."
    scene sm1cs-mh005-87 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_no_nah noloop
    mh "Oh, it was nothing. Just some boiler plate agreements."
    scene sm1cs-mh005-88 whats_on_second_mc_talk with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Still it was a big help.{w} And I know how you feel about my new job."
    scene sm1cs-mh005-89 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "[mcname], I..."
    scene sm1cs-mh005-90 whats_on_second_mc_talk with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey, it's okay. I wasn't trying to be passive aggressive about it. I just know how you feel, and it's probably not your favorite thing about me."
    mc "And I just want you to know I appreciate the help, and you."
    scene sm1cs-mh005-91 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_angry_oof noloop
    mh "Look, it's not... the job that bugs me."
    scene sm1cs-mh005-92 whats_on_second_mc_talk_confused with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "But, I thought-"
    scene sm1cs-mh005-93 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "I know, that's what I made it sound like, but..."
    mh "I just figured that after all of the sex, and kinks, and everything with Fetish Locator that you just kind of... Fell into this."
    scene sm1cs-mh005-91 whats_on_second_mh_talk with dissolve
    mh "That you were just phoning it in. This was what you were going to do, because it didn't require any more work."
    mh "I think... That's what bugged me the most about it."
    scene sm1cs-mh005-94 whats_on_second_mc_talk_thoughtful with dissolve
    play voice2 mc_yes_yes8 noloop
    mc "I mean... You're partially right."
    scene sm1cs-mh005-95 whats_on_second_mh_confused_mc_talk with dissolve
    pause
    scene sm1cs-mh005-96 whats_on_second_mc_talk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "This hasn't been as easy as I thought it would be. *sighs* How do I put this?"
    mc "You know how you're only really born with one or two natural talents?"
    scene sm1cs-mh005-97 whats_on_second_mh_talk_smile with dissolve
    play voice3 lissa_ugu noloop volume 1.3
    mh "Mmhmmm."
    scene sm1cs-mh005-98 whats_on_second_mc_talk_smile with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Yours being that you're incredibly smart and good with words and gorgeous, mine ended up being... Well, sex."
    mc "And this is the thing that made the most sense to do with that talent."
    play sound sfx_cloth_rustling4 volume 1.5
    scene sm1cs-mh005-99 whats_on_second_mh_talk_lean with dissolve
    play voice3 lissa_laugh noloop
    mh "Well, you're not wrong about the sex."
    scene sm1cs-mh005-100 whats_on_second_mc_talk with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "That's why we're doing this. Sure, it fell into my lap. But I also think that we can make something special here."
    scene sm1cs-mh005-101 whats_on_second_mh_talk with dissolve
    play voice3 lissa_moan3 noloop
    mh "You know, I... I'm happy to see you care so passionately about this."
    scene sm1cs-mh005-102 whats_on_second_mc_talk with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Really?"
    scene sm1cs-mh005-103 whats_on_second_mh_talk with dissolve
    play voice3 lissa_ugu2 noloop
    mh "Mmhmmm. When you care about something, you get this spark behind your eye. You can see the care and love and passion shining out into the world."
    mh "That's how I like to picture you, always. Looking at me, with that tiny little fire in your eyes..."
    scene sm1cs-mh005-104 whats_on_second_mc_talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Lyssa, I still care about you that way."
    scene sm1cs-mh005-105 whats_on_second_mh_talk_closer with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "I'll believe it when that little spark comes back."
    play voice2 mc_angry_huh2 noloop
    mc "It's in there, trust me."
    mh "I believe you."
    scene sm1cs-mh005-106 whats_on_second_mh_talkfelse_lean_back with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    if gt.curr_day in [SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY]:
        mh "Thank you for this wonderful date, [mcname], but I should get home. I do have work tomorrow."
    else:
        mh "Thank you for this wonderful date, [mcname], but I should get home. I do have things I need to take care of tomorrow."
    scene sm1cs-mh005-107 whats_on_second_mc_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course, I also probably need to get going."
    play sound sfx_cloth_rustling2 volume 1.5
    scene sm1cs-mh005-108 whats_on_second_mc_talk_stands with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "May I walk you home, ma'am?"
    scene sm1cs-mh005-109 whats_on_second_mh_talk_chuckles with dissolve
    play voice3 dahlia_disgust_yah noloop
    mh "As long as you promise never to call me ma'am again."
    scene sm1cs-mh005-110 whats_on_second_mc_talk with dissolve
    play voice2 mc_happy_laugh3 noloop volume 0.7
    mc "Of course{w}, miss."
    play sound sfx_cloth_rustling3
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1cs-mh005-111 whats_on_second_mh_talk_stand with dissolve
    pause
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh005-112 whats_on_second_mh_walk_door with dissolve
    pause
    play sound sfx_car_startmove
    stop music fadeout 6.0
    stop sound3 fadeout 1.5
    jump sm1cs_mh005_blowjob
label sm1cs_mh005_blowjob:
    $ renpy.music.set_volume(1.0, 3.0, "sound3" )
    $ renpy.music.set_volume(1.0, 1.5, "sound2" )
    play sound2 sfx_parknight_crickets fadein 3.0
    queue sound sfx_heels_steps2 loop
    scene sm1cs-mh005-113 whats_on_second_mh_house with Fade(0.5, 0.5, 0.5)
    pause
    play voice3 lissa_moan8 noloop
    play sound sfx_leg_kick8
    scene sm1cs-mh005-114 whats_on_second_mh_talk_winces with hpunch
    mh "Damnit!"
    scene sm1cs-mh005-115 whats_on_second_mc_talk with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "What's wrong!?"
    scene sm1cs-mh005-116 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_angry_oh noloop
    mh "Oh, it's just these stupid shoes. Wearing them all day hurts, and I think there may be a pebble or something in them, hang on."
    play sound sfx_planket_off_anim
    scene sm1cs-mh005-117 whats_on_second_mh_leans with dissolve
    pause
    play music music_midnight_blow fadein 2.0
    play sound3 sfx_hair_scratch1 noloop
    scene sm1cs-mh005-118 whats_on_second_mc_talk_leansn with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "Why, hello there."
    scene sm1cs-mh005-119 whats_on_second_mh_talk_leansn with dissolve
    play voice3 lissa_mmm1 noloop
    mh "Ooo, you been watching k-dramas lately, [mcname]?"
    scene sm1cs-mh005-120 whats_on_second_mc_talk with dissolve
    play voice2 mc_no_nope1 noloop
    mc "Nope. Just putting the moves on the prettiest woman in here."
    scene sm1cs-mh005-121 whats_on_second_mh_talk with dissolve
    play voice3 lissa_haha2 noloop
    mh "I think I'm the only woman in here."
    scene sm1cs-mh005-122 whats_on_second_mc_talk with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "That may be the case, but the important thing is that I get to talk to her."
    scene sm1cs-mh005-123 whats_on_second_mh_talk_giggles with dissolve
    play voice3 lissa_oh2 noloop
    mh "Wow, you really are giving me maximum effort now, huh."
    scene sm1cs-mh005-124 whats_on_second_mc_talk with dissolve
    play voice2 d2s9_mchey noloop
    mc "You said I needed to woo you, right?"
    play voice3 lissa_ugu3 noloop
    mh "I did."
    mc "Well, this is me wooing you."
    scene sm1cs-mh005-125 whats_on_second_mc_kiss with dissolve
    play voice3 lissa_moan1 noloop
    play voice2 d1s1_mmm noloop volume 1.5
    play sound dahlia_kiss_french1
    pause
    play voice3 lissa_mmm2 noloop
    scene sm1cs-mh005-126 whats_on_second_mc_kiss with dissolve
    play sound mc_kiss2
    mh "Mmmm..."
    scene sm1cs-mh005-127 whats_on_second_mh_talk_eyes_closed_content with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "That was... Nice..."
    scene sm1cs-mh005-128 whats_on_second_mh_kiss_again with dissolve
    play voice3 dahlia_sex_closedmoan2 noloop
    play voice2 mc_thinking_mmm1 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-mh005-129 whats_on_second_mc_pullaway_mh_eyesclosed with dissolve
    pause
    scene sm1cs-mh005-130 whats_on_second_mc_pullaway_mh_talk_eyes_halfopen with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "...There it is..."
    scene sm1cs-mh005-131 whats_on_second_mc_pullaway_mc_talk with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene sm1cs-mh005-132 whats_on_second_mh_talk with dissolve
    play voice3 nora_hmm noloop
    mh "That spark..."
    play sound3 sfx_cloth_rustling4 noloop
    scene sm1cs-mh005-133 whats_on_second_mh_kiss_arm with dissolve
    play voice3 lissa_moan1 noloop
    play voice2 d1s1_mmm noloop volume 1.5
    play sound dahlia_kiss_french1
    pause
    play sound sfx_cloth_rustling5
    scene sm1cs-mh005-134 whats_on_second_mc_talk_mh_handcrotch with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Lyssa..."
    scene sm1cs-mh005-135 whats_on_second_mh_talk_mh with dissolve
    play voice3 stacy_shhh noloop
    mh "Shhhhh, I want this..."
    play sound sfx_cloth_rustling1
    scene sm1cs-mh005-136 whats_on_second_mc_talk_mh_knees with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Lyssa..."
    scene sm1cs-mh005-137 whats_on_second_mh_talk_mh_knees with dissolve
    play voice3 lissa_moan2 noloop
    mh "[mcname]..."
    scene sm1cs-mh005-138 whats_on_second_mc_talk_mh_knees with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Are you sure?"
    scene sm1cs-mh005-139 whats_on_second_mc_talk_mmmmmh with dissolve
    play voice3 lissa_ugu noloop
    mh "Mmhmmm..."
    scene sm1cs-mh005-140 whats_on_second_mh_talk_mc_closeup with dissolve
    play voice3 lissa_hey noloop
    mh "Are you going to help me out with these pants?"
    play sound sfx_jeans_on1
    scene sm1cs-mh005-141 whats_on_second_mh_talk_mc_talk with dissolve
    play voice2 mc_yes_yes5 noloop
    mc "Of course."
    play sound sfx_skirt_off2
    scene sm1cs-mh005-142 whats_on_second_mh_talk_pants_off with dissolve
    play voice3 lissa_moan4 noloop
    mh "Oh, how I've missed you..."
    scene sm1cs-mh005-143 whats_on_second_mc_talk_mh_lick with dissolve
    play voisex3 lissa_sucking
    play voisex2 mc_scared_oh1 noloop
    mc "Oh, God..."
    scene sm1cs-mh005-144 whats_on_second_mh_talk with dissolve
    play voisex3 lissa_haha noloop
    mh "Seems like I'm not the only one..."
    scene sm1cs-mh005-a145-1 mc-mh-bj-anim-01 with dissolve
    pause 0.1
    scene sm1cs_mh005-a145-1
    play sound mc_sex_sucking_slow2 loop volume 0.6
    play voisex2 mc_sex_openmoans2
    play voisex3 nora_sucks_mouth
    mc "Oh- Lyssa-!"
    pause
    scene sm1cs_mh005-a145-2 with dissolve
    mc "OH fuhh- Lyssa!"
    pause
    scene sm1cs_mh005-a145-3 with dissolve
    play voisex2 mc_sex_openmoans3
    mc "This is amazing, holy shiiiit."
    mc "I-I almost forgot how good you are at this-"
    pause
    play sound mc_sex_sucking_fast2 loop volume 0.6
    scene sm1cs_mh005-a145-1-f with dissolve
    mc "Your lips - your tongue - fuuuuhhhnnnnngggg!"
    pause
    scene sm1cs_mh005-a145-2-f with dissolve
    mc "Oh, God - Lyssa - Lyssa, I'm going to cum."
    pause
    mc "Ly-Lyssa! I'm going to - I'm going to-!"
    scene sm1cs_mh005-a145-3-f with dissolve
    mc "Lyssa- I'm going to-!"
    pause
    play voisex2 mc_sex_orgasm4 noloop
    play voisex3 nora_sucking2 noloop
    stop sound fadeout 1.0
    scene sm1cs-mh005-150 whats_on_second_bj_mc_talk_cumface with hpunch
    mc "I'm cuummmMMMMING!"
    play voisex3 nora_sucking3 noloop
    scene sm1cs-mh005-151 whats_on_second_bj_mc_talk_mh_grab_ass with hpunch
    pause
    play voisex3 nora_sucking1 noloop
    play sound mc_cum_sound1
    scene sm1cs-mh005-152 whats_on_second_bj_cun_throat with hpunch
    pause
    scene sm1cs-mh005-153 whats_on_second_mc__talk_pullout with dissolve
    play voisex2 mc_happy_wow1 noloop
    mc "Lyssa... Wow. Just... Wow."
    scene sm1cs-mh005-154 whats_on_second_mh_talk_embarassed with dissolve
    play voice3 nora_huh noloop
    mh "Uhm... I..."
    mh "I need to get going, [mcname]."
    scene sm1cs-mh005-155 whats_on_second_mc_talk with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "Lyssa, I-"
    scene sm1cs-mh005-156 whats_on_second_mh_talk with dissolve
    play voice3 dahlia_no_high3 noloop
    mh "No need, I can get inside just fine. I-... I'll talk to you later."
    play sound sfx_keys_open1
    scene sm1cs-mh005-157 whats_on_second_mc_thought_door with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "What the hell?"
    play sound sfx_door_closed1
    scene sm1cs-mh005-158 whats_on_second_mc_thought_mh_gone with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "What... What just happened?{w} I guess... I'll give her some time and ask her what that was all about..."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh005-159 whats_on_second_mc_walks_away with dissolve
    pause
    stop sound fadeout 1.5
    stop sound2 fadeout 2.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    jump sm1cs_mh005_exit
label sm1cs_mh005_exit:
    $ StoryController.end_scene_in_time(MH_STORY, 23, 45, 5)
    return
label sm1cs_mh005_m01_c02:
    $ player.set_choice("sm1cs_mh005_kiss")
    $ CharacterController.get_character("mh").add_point()
    $ player.set_choice("sm1cs_mh005_get_point_1")
    return
label sm1cs_mh005_m02_c01:
    $ player.set_choice("sm1cs_mh005_let_mh_win")
    $ CharacterController.get_character("mh").add_point()
    $ player.set_choice("sm1cs_mh005_get_point_2")
    return
label sm1cs_mh005_unlocks:
    call sm1cs_mh005_m01_c02 from _call_sm1cs_mh005_m01_c02_1
    call sm1cs_mh005_m02_c01 from _call_sm1cs_mh005_m02_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MH_STORY)
    return