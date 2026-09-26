label sm1fs_t005:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound sfx_heels_steps2 loop
    scene sm1fs_t005-00 creating_the_pizza_show with dissolve
    play music music_tricky_topic
    play voice2 mc_thinking_hmm1 noloop
    mct "I wonder what's going on."
    stop sound fadeout 1.0
    scene sm1fs_t005-01 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_hey_angry1 noloop
    dvh "Gather up everyone. Gather up, please."
    dvh "I know all of you have been waiting for me to announce our new show."
    dvh "Well, that moment is finally here."
    scene sm1fs_t005-02 creating_the_pizza_show_km_talk_excited with dissolve
    play voice4 girl31_surprised_huh1 noloop
    km "So what will the next show be?"
    scene sm1fs_t005-03 creating_the_pizza_show_tl_talk with dissolve
    play voice5 girl24_arrogant_yeah3 noloop
    tl "Yeah, hurry up and spill it. I'm already getting bored."
    scene sm1fs_t005-04 creating_the_pizza_show_kw_talk_looktl with dissolve
    play voice6 boy10_disgust_oof noloop
    kw "Oh hush, Taisia."
    scene sm1fs_t005-05 creating_the_pizza_show_tl_grin with dissolve
    pause
    scene sm1fs_t005-06 creating_the_pizza_show_dvh_talk_clearsthroat with dissolve
    play voice3 girl34_angry_ahem4 noloop
    dvh "*clears throat*"
    play sound sfx_cloth_rustling1
    scene sm1fs_t005-07 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_happy_relief5 noloop
    dvh "If you all would stop interrupting me, I'll be happy to tell you."
    dvh "Our next play..."
    scene sm1fs_t005-08 creating_the_pizza_show_dvh_talk_buildup with dissolve
    play voice3 girl34_thinking_eeh1 noloop
    dvh "Will be..."
    scene sm1fs_t005-09 creating_the_pizza_show_dvh_talk_announcement with dissolve
    play voice3 girl34_happy_yay1 noloop
    dvh "\"Some kind of love story about pizza!\""
    play sound sfx_pen_writing1
    scene sm1fs_t005-10 creating_the_pizza_show_quiet_confused with dissolve
    pause
    scene sm1fs_t005-11 creating_the_pizza_show_km_talk with dissolve
    play voice4 girl31_thinking_emm3 noloop
    km "Some kind of-"
    km "I don't think I've heard of that one, Denise."
    scene sm1fs_t005-12 creating_the_pizza_show_tl_talk with dissolve
    play voice5 girl24_arrogant_huh2 noloop
    tl "It sounds made up."
    scene sm1fs_t005-13 creating_the_pizza_show_vs_talk with dissolve
    play voice6 girl33_yes_yeah noloop
    vs "I was going to say the same thing."
    scene sm1fs_t005-14 creating_the_pizza_show_km_talk with dissolve
    play voice4 girl31_no_laughing2 noloop
    km "It can't be. Denise wouldn't announce a play that isn't well known."
    scene sm1fs_t005-15 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_happy_laugh4 noloop
    dvh "Well, normally I would agree with you, Kellie."
    scene sm1fs_t005-16 creating_the_pizza_show_km_talk with dissolve
    play voice4 girl31_surprised_what3 noloop
    km "What?"
    scene sm1fs_t005-17 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_arrogant_ugu1 noloop
    dvh "So as I said, right now the working title is \"Some kind of love story about pizza\"."
    scene sm1fs_t005-18 creating_the_pizza_show_dvh_talk_nothappy with dissolve
    play voice3 girl34_disappointed_eeh2 noloop
    dvh "This goes hand in hand with announcing our new sponsor, Pizza World."
    dvh "They agreed to support us so long as we come up with a story that is focused around..."
    dvh "One of their stores."
    scene sm1fs_t005-19 creating_the_pizza_show_km_talk_shocked with dissolve
    play voice4 girl31_thinking_emm1 noloop
    km "A pizza parlor..."
    scene sm1fs_t005-20 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_hey_angry7 noloop
    dvh "Don't look at me like that, Kellie."
    scene sm1fs_t005-21 creating_the_pizza_show_ec_talk with dissolve
    play voice6 girl32_happy_yeah noloop
    ec "I think it's going to be wonderful, Denise."
    scene sm1fs_t005-22 creating_the_pizza_show_tl_talk_ec with dissolve
    play voice5 girl24_hey_angry noloop
    tl "You're not even an actor, Eileen. We're the ones people will be laughing at."
    scene sm1fs_t005-23 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_angry_ahem1 noloop
    dvh "Ahem. Times are tough."
    scene sm1fs_t005-24 creating_the_pizza_show_ec_talk with dissolve
    play voice6 girl32_yes_irritated noloop
    ec "So tough."
    scene sm1fs_t005-25 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_angry_breath1 noloop
    dvh "And I did what was needed to keep the theater open."
    scene sm1fs_t005-26 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_arrogant_ha3 noloop
    dvh "Unless everyone here wants to quit and try your luck slinging burgers."
    menu:
        "Do you know anyone hiring?"(hint="sm1fs_t005_m01_h01"):
            call sm1fs_t005_m01_c01 from _call_sm1fs_t005_m01_c01
            play sound sfx_cloth_rustling2
            scene sm1fs_t005-27 creating_the_pizza_show_mc_talk_handup with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "Do you know anyone hiring, Denise?"
            scene sm1fs_t005-28 creating_the_pizza_show_tl_talk_giggle with dissolve
            play voice5 girl24_happy_laugh1 noloop
            tl "*chuckles*"
            scene sm1fs_t005-29 creating_the_pizza_show_dvh_talk with dissolve
            play voice3 girl34_no_angry1 noloop
            dvh "As a matter of fact, no, I don't, [mcname]."
            dvh "But if your work here isn't fulfilling you..."
            play sound sfx_throw_something1
            scene sm1fs_t005-30 creating_the_pizza_show_dvh_talk_pointdoor with dissolve
            play voice3 girl34_angry_errr noloop
            dvh "You know where the exit is."
            scene sm1fs_t005-31 creating_the_pizza_show_mc_talk_waveoff with dissolve
            play voice2 mc_no_nah2 noloop
            mc "That's cool. Forget I said anything."
            scene sm1fs_t005-32 creating_the_pizza_show_tl_talk_lean with dissolve
            play voice5 girl24_happy_laugh2 noloop
            tl "Smooth moves, idiot."
        "I'm sure you did your best, Denise."(hint="sm1fs_t005_m01_h02"):
            call sm1fs_t005_m01_c02 from _call_sm1fs_t005_m01_c02
            scene sm1fs_t005-33 creating_the_pizza_show_mc_talk with dissolve
            play voice2 mc_happy_a1 noloop
            mc "I'm sure you did your best, Denise."
            scene sm1fs_t005-34 creating_the_pizza_show_dvh_talk_relax with dissolve
            play voice3 girl34_happy_relief4 noloop
            dvh "Thank you, [mcname]."
            dvh "It certainly was a feat convincing the sponsor that we would be worth the investment."
        "Say nothing."(hint="sm1fs_t005_m01_h03"):
            call sm1fs_t005_m01_c03 from _call_sm1fs_t005_m01_c03
            pass
    scene sm1fs_t005-35 creating_the_pizza_show_vs_talk with dissolve
    play voice6 girl33_disappointed_aah noloop
    vs "I have a question, what kind of story are we going to do... with that kind of setting."
    scene sm1fs_t005-36 creating_the_pizza_show_dvh_talk_thinking with dissolve
    play voice3 girl34_thinking_emm1 noloop
    dvh "I haven't landed on a concept yet."
    dvh "It's been... a rough period since I found out they would sponsor us."
    scene sm1fs_t005-37 creating_the_pizza_show_dvh_talk_annoyed with dissolve
    play voice3 girl34_disappointed_ehh2 noloop
    dvh "And no matter what I've tried, the muses have not spoken to me. Not even about anchovies and pineapples."
    scene sm1fs_t005-38 creating_the_pizza_show_tl_talk_disgusted with dissolve
    play voice5 girl24_disgust_ooh1 noloop
    tl "Guh. Keep your pineapples off my pizza."
    scene sm1fs_t005-39 creating_the_pizza_show_km_talk with dissolve
    play voice4 girl31_surprised_what2 noloop
    km "What? That's the best kind of pizza."
    scene sm1fs_t005-40 creating_the_pizza_show_vs_talk with dissolve
    play voice6 girl33_thinking_eem2 noloop
    vs "I try to only eat thin-crust with cheese and just one pepperoni per slice."
    scene sm1fs_t005-41 creating_the_pizza_show_dvh_talk_wave with dissolve
    play voice3 girl34_angry_argh5 noloop
    dvh "This isn't the time for a contest on everyone's favorite pizza."
    dvh "I called you here to introduce the show and to pick your brains on what kind of story we should make."
    play sound sfx_cloth_rustling3
    scene sm1fs_t005-42 creating_the_pizza_show_km_thinking_vsphone_tlsighing with dissolve
    pause
    scene sm1fs_t005-43 creating_the_pizza_show_tl_talk_speaksup with dissolve
    play voice5 girl24_arrogant_kgh1 noloop
    tl "Why don't we do a parody on the classic porn movie with a pizza delivery guy."
    scene sm1fs_t005-44 creating_the_pizza_show_dvh_talk_vs_giggling with dissolve
    play voice3 girl34_disappointed_oh1 noloop
    dvh "I normally say that there is no such thing as a bad idea, Taisia.{w} But that one is testing that rule."
    scene sm1fs_t005-45 creating_the_pizza_show_vs_talkdea with dissolve
    play voice6 girl33_surprised_huh2 noloop
    vs "What about we do Hamilton, but with pizza?"
    scene sm1fs_t005-46 creating_the_pizza_show_km_talk_rolleyes with dissolve
    play voice4 girl31_disappointed_ehh9 noloop
    km "*whispering* Oh brother."
    scene sm1fs_t005-47 creating_the_pizza_show_tl_talk with dissolve
    play voice5 girl24_yes_yeah noloop
    tl "Hamilton is that one that got sold out every night, right?"
    scene sm1fs_t005-48 creating_the_pizza_show_dvh_talk_wave with dissolve
    play voice3 girl34_no_nouh3 noloop
    dvh "We're not doing Hamilton. For one, I don't see it being easily modified."
    dvh "And two, it's a pretty intense show with a lot of powerful vocal work."
    play sound sfx_pen_writing5
    scene sm1fs_t005-49 creating_the_pizza_show_dvh_talk_lookaround with dissolve
    play voice3 girl34_arrogant_huh1 noloop
    dvh "Any other ideas?"
    scene sm1fs_t005-50 creating_the_pizza_show_km_tryspeak_mcnotice with dissolve
    play voice4 girl31_disappointed_mff1 noloop
    pause
    play sound sfx_cloth_rustling4
    scene sm1fs_t005-51 creating_the_pizza_show_mc_talk_km with dissolve
    play voice2 mc_hey_hey6 noloop
    mc "*whispers* What's your idea, Kellie?"
    scene sm1fs_t005-52 creating_the_pizza_show_km_talk_embarrassed with dissolve
    play voice4 girl31_disappointed_ehh5 noloop
    km "I... I don't have an idea."
    scene sm1fs_t005-53 creating_the_pizza_show_mc_talk_notbuying with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Are you sure? You look like you've got something good in mind."
    scene sm1fs_t005-54 creating_the_pizza_show_km_talk with dissolve
    play voice4 girl31_no_simple noloop
    km "Denise won't go for it."
    scene sm1fs_t005-55 creating_the_pizza_show_mc_talk_urges with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Come on, how do you know that if you don't say something."
    scene sm1fs_t005-56 creating_the_pizza_show_km_talk_annoyed with dissolve
    pause
    scene sm1fs_t005-57 creating_the_pizza_show_km_expression_change_hand with dissolve
    pause
    play sound sfx_heels_steps2
    scene sm1fs_t005-58 creating_the_pizza_show_dvh_talk_km_handraised with dissolve
    play voice3 girl34_yes_aga2 noloop
    dvh "Kellie, go ahead."
    stop sound fadeout 1.0
    scene sm1fs_t005-59 creating_the_pizza_show_km_talk with dissolve
    play voice4 girl31_thinking_emm2 noloop
    km "We haven't done anything like Romeo and Juliet lately."
    km "It's a classic, and I'm sure we could just modify the rival families to be competing business."
    scene sm1fs_t005-60 creating_the_pizza_show_km_talk_confident_tllook_vs_excited with dissolve
    play voice4 girl31_arrogant_huh1 noloop
    km "One business can be the pizza parlor, and the other can be some other food place, I guess."
    scene sm1fs_t005-61 creating_the_pizza_show_dvh_talkmpressed with dissolve
    play voice3 girl34_surprised_wow4 noloop
    dvh "Not bad, Kellie. I think you're right. We use the sponsor as set dressing and other swaps."
    dvh "There are no songs, so we can just focus on the lines, the romance, and the duels."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t005-62 creating_the_pizza_show_dvh_talk_edgestage with dissolve
    play voice3 girl34_yes_happy3 noloop
    dvh "Yes, yes... It might just work."
    stop sound fadeout 1.0
    scene sm1fs_t005-63 creating_the_pizza_show_dvh_talk_turn with dissolve
    play voice3 girl34_yes_yeah7 noloop
    dvh "Alright, we're going to do a modern take on the classic tragedy, mixing in our sponsor."
    play sound sfx_cloth_rustling1
    scene sm1fs_t005-64 creating_the_pizza_show_dvh_talk_pointkelly with dissolve
    play voice3 girl34_thinking_hmm2 noloop
    dvh "Kellie, you're going to be working closely with Eileen and I on the script, so I'll need you around more."
    scene sm1fs_t005-65 creating_the_pizza_show_km_talk_excited with dissolve
    play voice4 girl31_happy_yay4 noloop
    km "T-Thank you, Denise."
    scene sm1fs_t005-66 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_no_nah4 noloop
    dvh "Don't thank me yet. A writer's credit is earned in sweat, blood, and tears."
    dvh "And then I'm going to need you to act as well."
    scene sm1fs_t005-67 creating_the_pizza_show_vs_talk_cheers with dissolve
    play voice6 girl33_happy_great noloop
    vs "Great thinking, Kellie. I've never done a tragedy before. It sounds like a lot of fun."
    scene sm1fs_t005-68 creating_the_pizza_show_km_unsure with dissolve
    pause
    scene sm1fs_t005-69 creating_the_pizza_show_tl_talk_unenthused with dissolve
    play voice5 girl24_disappointed_neh noloop
    tl "I can't believe we're actually going to do this. Can we just skip to the part where the two idiots kill themselves at the end?"
    scene sm1fs_t005-70 creating_the_pizza_show_dvh_talk_smile with dissolve
    play voice3 girl34_disappointed_oh2 noloop
    dvh "Taisia, just because no one has looked at you with love in their eyes doesn't mean people in the audience don't still believe in romance."
    scene sm1fs_t005-71 creating_the_pizza_show_tl_talkmpressed with dissolve
    play voice5 girl24_arrogant_hah noloop
    tl "Heh. Sure, boss."
    scene sm1fs_t005-72 creating_the_pizza_show_dvh_talk_kellie with dissolve
    play voice3 girl34_hey_scandalized2 noloop
    dvh "Kellie, the first thing we need to think up is the rival food company."
    dvh "It can't just be two pizza parlors feuding."
    play sound sfx_cloth_rustling2
    scene sm1fs_t005-73 creating_the_pizza_show_mc_talk_thought_speakup with dissolve
    play voice2 mc_thinking_hm noloop
    mct "Wait a minute."
    mc "Wurst Delivery!"
    scene sm1fs_t005-74 creating_the_pizza_show_dvh_talk with dissolve
    play voice3 girl34_surprised_huh5 noloop
    dvh "Huh?"
    scene sm1fs_t005-75 creating_the_pizza_show_km_talk with dissolve
    play voice4 girl31_surprised_what1 noloop
    km "Worst what?"
    scene sm1fs_t005-76 creating_the_pizza_show_mc_talk with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "I know another restaurant that could get involved. The Wurst Delivery, it's a bratwurst place."
    scene sm1fs_t005-77 creating_the_pizza_show_vs_talk with dissolve
    play voice6 girl33_surprised_oh noloop
    vs "Oh, I know that place. Their sausages are really thick and long."
    scene sm1fs_t005-78 creating_the_pizza_show_vs_talk_rub_belly with dissolve
    play voice6 girl33_happy_mmm noloop
    vs "I always feel so full after ordering from there."
    scene sm1fs_t005-79 creating_the_pizza_show_tl_talk_sarcastic with dissolve
    play voice5 girl24_arrogant_huh1 noloop
    tl "A pizzeria versus a hotdog place. It's pretty fresh."
    scene sm1fs_t005-80 creating_the_pizza_show_dvh_talk_seriously with dissolve
    play voice3 girl34_thinking_hmm5 noloop
    dvh "Hmmm. That could work. Do you think this Wursthaus would be interested in sponsoring the play for a bit of cash, [mcname]?"
    scene sm1fs_t005-81 creating_the_pizza_show_mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "I don't know, but I can go find out."
    scene sm1fs_t005-82 creating_the_pizza_show_dvh_talk_excited with dissolve
    play voice3 girl34_yes_aga6 noloop
    dvh "Good. Get to it."
    dvh "One sponsor is enough to keep the lights on, but two would mean we can actually get proper costumes and sets done."
    play sound sfx_heels_steps2
    scene sm1fs_t005-83 creating_the_pizza_show_dvh_talk_focused_mc with dissolve
    play voice3 girl34_happy_relief2 noloop
    dvh "It would mean a lot to me if you can get this done, [mcname]."
    play sound sfx_cloth_rustling5
    scene sm1fs_t005-84 creating_the_pizza_show_dvh_talk_moving_backstage with dissolve
    play voice3 girl34_disappointed_eem3 noloop
    dvh "So uh... try your best, I guess."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1fs_t005-85 creating_the_pizza_show_dvh_walkoff_stage with dissolve
    play voice3 girl34_hey_bye1 noloop
    dvh "I'll be around my office."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(1.0, 3.5, "music" )
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1fs_t005_end
label sm1fs_t005_end:
    $ StoryController.end_scene(THEATER_STORY_LINE, 2, 0, 1)
    return
label sm1fs_t005_m01_c01:
    $ player.set_choice("sm1fs_t005_be_dumb")
    return
label sm1fs_t005_m01_c02:
    $ player.set_choice("sm1fs_t005_dvh_did_best")
    return
label sm1fs_t005_m01_c03:
    $ player.set_choice("sm1fs_t005_say_nothing")
    return