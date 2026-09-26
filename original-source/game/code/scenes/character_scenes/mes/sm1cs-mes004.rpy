label sm1cs_mes004:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound3 sfx_crowd_fightclub_ambient1 fadein 3.5 volume 0.3
    play sound4 sfx_distanttraffic_city fadein 2.0
    scene sm1cs-mes004-01 mc-mes-street1_c1 with dissolve
    $ renpy.music.play(audio.music_under_the_moonsky, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_under_the_moonsky_reverbed, "music2", True, None, True, 0.0)
    play voice2 mc_hey_hey8 noloop
    mc "Hey Min. What's eating you?"
    scene sm1cs-mes004-01 mc-mes-street1_c2 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "Promise not to laugh?"
    scene sm1cs-mes004-02 mc-mes-street2_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Huh?"
    scene sm1cs-mes004-02 mc-mes-street2_c2 with dissolve
    play voice3 min_arrogant_pff noloop
    mes "Promise not to laugh, [mcname]."
    scene sm1cs-mes004-03 mc-mes-street3_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, I promise not to laugh."
    play sound sfx_hair_scratch1
    scene sm1cs-mes004-03 mc-mes-street3_c2 with dissolve
    play voice3 min_thinking_emm noloop
    mes "I want to ask you out on a date."
    scene sm1cs-mes004-04 mc-mes-look_c1 with dissolve
    play voice2 mc_surprised_what6 noloop
    mc "Woah? What?"
    play sound sfx_cloth_rustling2
    scene sm1cs-mes004-04 mc-mes-look_c2 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "I-..."
    mes "Oh my god, I can't believe I said that."
    scene sm1cs-mes004-05 mc-mes-look2_c1 with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "I just... I was excited to come out and be with you again."
    scene sm1cs-mes004-05 mc-mes-look2_c2 with dissolve
    mes "It was like I had a boyfriend again, and then I realized that neither of us asked each other out."
    scene sm1cs-mes004-05 mc-mes-look2_c1 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "It felt like a failure on my part.{w} So instead of just talking about it, I went with the most direct..."
    scene sm1cs-mes004-06 mc-mes-look3_c1 with dissolve
    play voice3 min_arrogant_heh1 noloop
    mes "Most foolish... approach."
    mes "What do you think?"
    scene sm1cs-mes004-07 mc-mes-look4_c1 with dissolve
    menu:
        "Not foolish":
            call sm1cs_mes004_m01_c01 from _call_sm1cs_mes004_m01_c01
            play voice2 mc_no_no2 noloop
            mc "It wasn't foolish at all, Min."
        "Crazy, but I love it":
            play voice2 d4s4_mclaugh noloop volume 1.7
            mc "Haha. You're crazy, but I love your style."
            scene sm1cs-mes004-07 mc-mes-look4_c2 with dissolve
            play voice3 min_angry_mmh noloop
            mes "*annoyed* [mcname]..."
            play sound sfx_cloth_rustling1
            scene sm1cs-mes004-08 mc-mes-look5_c1 with dissolve
            play voice2 d3s11b_mcheh noloop
            mc "*chuckles*"
    scene sm1cs-mes004-11 mc-mes-talk_c2 with dissolve
    mes "..."
    play voice3 min_arrogant_huh2 noloop
    mes "Well, don't just stand there. You can {i}still{/i} ask me out."
    scene sm1cs-mes004-09 mc-mes-look6_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.7
    mct "Hmmm. I guess we never did this step back when we were hanging out during Fetish Locator."
    mct "And I guess making things official is something she wants, and I don't want to let Min down."
    scene sm1cs-mes004-10 mc-mes-ask_c1 with dissolve
    play voice2 mc_happy_a1 noloop volume 1.4
    mc "Min, I'd love to take you out for a drink tonight."
    scene sm1cs-mes004-10 mc-mes-ask_c2 with dissolve
    play voice3 min_old_laugh noloop
    mes "*soft giggle*"
    mes "Ahem. I accept."
    scene sm1cs-mes004-12 mc-mes-talk2_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "Oooh. Classic vibe."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mes004-13 mc-mes-walk_c2 with dissolve
    play voice3 min_arrogant_heh2 noloop
    mes "Don't worry."
    mes "It will be a nice relaxing evening."
    stop sound4 fadeout 2.0
    stop sound fadeout 1.5
    stop sound2 fadeout 1.5
    stop sound3 fadeout 2.0
    jump sm1cs_mes004_bar
label sm1cs_mes004_bar:
    queue sound4 sfx_crowd_fightclub_ambient2 fadein 2.0 volume 0.4
    $ renpy.music.set_volume(0.0, 5.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    scene sm1cs-mes004-14 mc-mes-bar_c2 with long_fade
    play voice3 min_happy_wooh noloop
    mes "SHOTS!"
    scene sm1cs-mes004-14 mc-mes-bar_c1 with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Shots?"
    scene sm1cs-mes004-14 mc-mes-bar_c2 with dissolve
    play voice3 min_happy_yeah noloop
    mes "Shots."
    menu:
        "I didn't think you were into shots":
            scene sm1cs-mes004-15 mc-mes-ask_c1 with dissolve
            play voice2 mc_surprised_oh3 noloop
            mc "I didn't know you were a shots girl."
            scene sm1cs-mes004-15 mc-mes-ask_c2 with dissolve
            play voice3 min_no_nonono noloop
            mes "I'm not, but this girl at campus said that they were best for when your brain is the problem."
            scene sm1cs-mes004-16 mc-mes-ask2_c1 with dissolve
            play voice2 d1s5_mchappy noloop volume 1.6
            mc "What's the problem?"
            scene sm1cs-mes004-16 mc-mes-ask2_c2 with dissolve
            play voice3 min_angry_cough noloop
            mes "My problem is that I haven't done shots with you, [mcname]."
            play sound sfx_cloth_rustling3
            scene sm1cs-mes004-17 mc-mes-shot_c1 with dissolve
            play voice2 mc_happy_oof1 noloop
            mc "Sounds deadly. Let's fix it."
        "Let's do it!":
            call sm1cs_mes004_m02_c02 from _call_sm1cs_mes004_m02_c02
            play sound sfx_cloth_rustling3
            scene sm1cs-mes004-17 mc-mes-shot_c1 with dissolve
            play voice2 mc_happy_wooh3 noloop
            mc "Let's do it."
    scene sm1cs-mes004-18 mc-mes-shot2_c2 with dissolve
    play voice3 min_happy_yay noloop
    mes "To new beginnings."
    scene sm1cs-mes004-18 mc-mes-shot2_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "And old friends."
    play sound sfx_celebration_ding1
    scene sm1cs-mes004-19 mc-mes-shot3_c1 with dissolve
    play voice3 min_happy_woohoo noloop
    mes "Woohoo."
    scene sm1cs-mes004-20 mc-mes-look_c2 with dissolve
    play sound sfx_drink_gulp
    pause
    scene sm1cs-mes004-20-1 mc-mes-shot_c2 with dissolve
    play sound sfx_drink_gulp
    pause
    scene sm1cs-mes004-20-1 mc-mes-shot_c1 with dissolve
    play sound sfx_drink_gulp
    pause
    scene sm1cs-mes004-21 mc-mes-look2_c2 with dissolve
    play voice3 min_disgust_boeah noloop
    mes "Buh..."
    scene sm1cs-mes004-21 mc-mes-look2_c1 with dissolve
    play voice2 mc_disgust_ooh1 noloop
    mc "Ooooh."
    mc "*strained* Good shit."
    scene sm1cs-mes004-22 mc-mes-point_c2 with dissolve
    play voice3 min_happy_laugh3 noloop
    mes "Haha."
    mes "Go get the next round."
    scene sm1cs-mes004-21 mc-mes-look2_c1 with dissolve
    menu:
        "You want more of that poison?":
            call sm1cs_mes004_m03_c01 from _call_sm1cs_mes004_m03_c01
            play voice2 mc_arrogant_huh2 noloop
            mc "Huh? You want more of that poison?"
            scene sm1cs-mes004-21 mc-mes-look2_c2 with dissolve
            play voice3 min_yes_yeah2 noloop
            mes "Yup. I need more until I can put tests and studying out of my mind."
            scene sm1cs-mes004-22 mc-mes-point_c1 with dissolve
            play voice2 mc_yes_okay3 noloop
            mc "Got it. Just don't go crazy."
            scene sm1cs-mes004-22 mc-mes-point_c2 with dissolve
            play voice3 min_happy_laugh2 noloop
            mes "Haha, if anyone's going crazy, it's you."
        "Got it":
            play voice2 mc_yes_yes7 noloop
            mc "Got it. Don't go anywhere."
    scene sm1cs-mes004-24 mc-mes-talk_c2 with fade
    play voice2 mc_happy_wooh1 noloop
    mc "Let's get this party started."
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    $ renpy.music.set_volume(0.0, 5.0, "music2" )
    $ renpy.music.set_volume(0.2, 3.5, "sound4" )
    scene sm1cs-mes004-25 mc-mes-look_c2 with dissolve
    play sound sfx_drink_gulp
    pause
    scene sm1cs-mes004-26 mc-mes-talk2_c2 with dissolve
    play sound sfx_drink_gulp
    pause
    scene sm1cs-mes004-27 mc-mes-point_c2 with dissolve
    pause
    scene sm1cs-mes004-28 mc-mes-dance_c2 with dissolve
    pause
    scene sm1cs-mes004-29 mc-mes-dance2_c2 with dissolve
    pause
    scene sm1cs-mes004-30 mc-mes-dance3_c2 with dissolve
    pause
    scene sm1cs-mes004-31 mc-mes-dance4_c2 with dissolve
    pause
    scene sm1cs-mes004-31-1 mc-mes-dance5_c2 with dissolve
    pause
    jump sm1cs_mes004_after_dance
label sm1cs_mes004_after_dance:
    $ renpy.music.set_volume(1.0, 3.5, "sound4" )
    $ renpy.music.set_volume(0.0, 5.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    scene sm1cs-mes004-32 mc-mes-sit_c1 with long_fade
    play voice2 d7s4_mcbreathing noloop
    pause
    scene sm1cs-mes004-32 mc-mes-sit_c2 with dissolve
    play voice3 min_angry_breath noloop
    pause
    stop voice2 fadeout 1.0
    scene sm1cs-mes004-33 mc-mes-ask_c1 with dissolve
    play voice3 min_hey_greeting noloop
    mes "Two glasses of water, please."
    play sound sfx_plates_moving1 volume 0.6
    scene sm1cs-mes004-34 mc-mes-water_c1 with dissolve
    play voice4 girl26_yes_aga noloop
    rd "Here you go."
    scene sm1cs-mes004-35 mc-mes-water2_c1 with dissolve
    play sound sfx_drink_loop1 volume 3.0 loop
    pause
    scene sm1cs-mes004-36 mc-mes-water3_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-mes004-36 mc-mes-water3_c2 with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "So come on. Tell me."
    scene sm1cs-mes004-38 mc-mes-talk2_c1 with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "I think it was summer camp."
    mc "There was this end-of-the-camp dance, and I worked up the nerve to ask a girl to dance."
    scene sm1cs-mes004-37 mc-mes-talk_c1 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "I suck.{w} I can't remember her name. But I'll always remember her boobs."
    mc "They were like two small apples, and that was the highlight of the whole summer."
    scene sm1cs-mes004-38 mc-mes-talk2_c2 with dissolve
    play voice3 min_happy_laugh4 noloop
    mes "Haha."
    scene sm1cs-mes004-39 mc-mes-look_c2 with dissolve
    play voice3 min_no_happy noloop
    mes "That's not what I asked."
    scene sm1cs-mes004-40 mc-mes-ask_c1 with dissolve
    play voice2 mc_no_no10 noloop
    mc "It's not?"
    scene sm1cs-mes004-40 mc-mes-ask_c2 with dissolve
    play voice3 min_no_uhuh noloop
    mes "Haha. No, I asked about your first kiss, [mcname]."
    menu:
        "It's not polite to kiss and tell":
            call sm1cs_mes004_m04_c01 from _call_sm1cs_mes004_m04_c01
            play sound sfx_cloth_rustling1
            scene sm1cs-mes004-41 mc-mes-talk_c1 with dissolve
            play voice2 mc_angry_off noloop
            mc "It's not polite to kiss and tell."
            scene sm1cs-mes004-41 mc-mes-talk_c2 with dissolve
            play voice3 min_yes_aga noloop
            mes "And I doubt you really believe that."
            play sound sfx_cloth_rustling2
            scene sm1cs-mes004-42 mc-mes-talk2_c2 with dissolve
            play voice3 min_hey_simple noloop
            mes "Come on, we're getting to know each other better."
            scene sm1cs-mes004-42 mc-mes-talk2_c1 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "Alright, then you can go first."
        "You go first":
            scene sm1cs-mes004-42 mc-mes-talk2_c1 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "Alright. You can go first."
    scene sm1cs-mes004-43 mc-mes-talk3_c2 with dissolve
    play voice3 min_surprised_oh noloop
    mes "Let's see. Mine was with my neighbor at the park."
    scene sm1cs-mes004-43 mc-mes-talk3_c1 with dissolve
    play voice2 mc_disgust_meh2 noloop
    mc "Gross. You kissed some old man."
    play sound sfx_cloth_rustling5
    scene sm1cs-mes004-44 mc-mes-talk4_c2 with dissolve
    play voice3 min_surprised_ohmy noloop
    mes "Oh my god no!"
    scene sm1cs-mes004-45 mc-mes-talk5_c2 with dissolve
    play voice3 min_thinking_mhh noloop
    mes "He was my neighbor, but he was my age."
    mes "Both of our families were there for a little picnic."
    mes "I saw my chance and took it."
    scene sm1cs-mes004-45 mc-mes-talk5_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop volume 1.5
    mc "Took it. Bold Min was bold."
    scene sm1cs-mes004-45 mc-mes-talk5_c2 with dissolve
    play voice3 min_yes_happy noloop
    mes "Damn right."
    mes "But my brother saw us and told our parents."
    play sound sfx_cup_slide1
    scene sm1cs-mes004-46 mc-mes-talk6_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "What a little weasel."
    scene sm1cs-mes004-46 mc-mes-talk6_c2 with dissolve
    play voice3 min_old_laugh noloop
    mes "Haha. He was.{w} Still is sometimes."
    mes "But at least he wasn't pushing me for an arranged marriage."
    play sound sfx_drink_loop1 loop volume 2.5 loop
    scene sm1cs-mes004-47 mc-mes-water_c2 with dissolve
    play voice3 min_disappointed_mph noloop
    mes "*softly* At least not this time."
    scene sm1cs-mes004-47 mc-mes-water_c1 with dissolve
    pause
    play sound sfx_cloth_rustling3
    scene sm1cs-mes004-48 mc-mes-water2_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Do you want to talk about it?"
    scene sm1cs-mes004-48 mc-mes-water2_c2 with dissolve
    play voice3 min_no_simple noloop
    mes "No. It's."
    play sound sfx_cup_slide1
    scene sm1cs-mes004-49 mc-mes-gesturing_c2 with dissolve
    play voice3 min_disappointed_ehh3 noloop
    mes "*sighs* I don't want to ruin our fun."
    scene sm1cs-mes004-49 mc-mes-gesturing_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Sometimes people have fun just by supporting their friends."
    scene sm1cs-mes004-50 mc-mes-look_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Or girlfriends."
    scene sm1cs-mes004-50 mc-mes-look_c2 with dissolve
    play voice3 min_yes_ugu noloop
    mes "I know.{w} But... I don't want to feel like a burden to you, [mcname]."
    mes "That's not me."
    play sound sfx_cup_slide1 volume 2.0
    scene sm1cs-mes004-51 mc-mes-look2_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I know it's not."
    mc "Now get it off your chest."
    scene sm1cs-mes004-50 mc-mes-look_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Do that, and the next round is on me."
    scene sm1cs-mes004-51 mc-mes-look2_c2 with dissolve
    play voice3 min_happy_relief noloop
    mes "*sighs* Studying isn't the hardest thing since I've come back."
    mes "The occasional calls, the little \"check ins\" from my family are driving me nuts."
    play sound sfx_cloth_rustling1
    scene sm1cs-mes004-52 mc-mes-look3_c2 with dissolve
    play voice3 min_disappointed_off noloop
    mes "My parents speak very fluent double speak."
    mes "The words all sound super caring, supportive. But there are snakes in the pool."
    scene sm1cs-mes004-52 mc-mes-look3_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "What? You should call a plumber."
    mc "Or an exterminator?"
    play sound sfx_cloth_rustling2
    scene sm1cs-mes004-53 mc-mes-talk_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "You would definitely call someone."
    scene sm1cs-mes004-53 mc-mes-talk_c2 with dissolve
    play voice3 min_old_hmm noloop volume 1.7
    mes "Figurative snakes, [mcname].{w} Figurative."
    scene sm1cs-mes004-54 mc-mes-talk2_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Ah. Good."
    play sound sfx_cloth_rustling4
    scene sm1cs-mes004-54 mc-mes-talk2_c2 with dissolve
    play voice3 min_arrogant_hm noloop
    mes "So when I figured out they were subtly trying to get me to accept that I would be better off coming home, I let them have it."
    mes "Told them that they were hypocrites and that it's {b}my{/b} life.{w} Not theirs."
    scene sm1cs-mes004-55 mc-mes-talk3_c2 with dissolve
    play voice3 min_happy_laugh3 noloop
    mes "They didn't like that.{w} Figures."
    mes "I'll take that shot now."
    scene sm1cs-mes004-55 mc-mes-talk3_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah..."
    mc "Sorry for pushing you about it."
    scene sm1cs-mes004-55 mc-mes-talk3_c2 with dissolve
    play voice3 min_no_nope noloop
    mes "Relax. You can get me to do a lot when I'm naked, but you never make me do anything I don't want to do, [mcname]."
    play voice2 mc_yes_ugu1 noloop
    mc "Mmhmm."
    scene sm1cs-mes004-56 mc-mes-talk4_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Two more shots, please."
    play sound sfx_plates_moving1 volume 0.5
    scene sm1cs-mes004-57 mc-mes-shots_c1 with dissolve
    pause
    play sound sfx_celebration_ding1
    scene sm1cs-mes004-58 mc-mes-shots2_c1 with dissolve
    play voice2 mc_angry_oof noloop
    mc "Fuck your parents."
    scene sm1cs-mes004-58 mc-mes-shots2_c2 with dissolve
    play voice3 min_happy_laugh1 noloop
    mes "*giggles* Fuck my parents!"
    stop voice3 fadeout 1.0
    scene sm1cs-mes004-59 mc-mes-shots3_c1 with dissolve
    play sound sfx_drink_gulp
    mc "*gulps*"
    scene sm1cs-mes004-59 mc-mes-shots3_c2 with dissolve
    play sound sfx_drink_gulp
    play voice2 mc_pain_mff1 noloop
    mct "Oh my god."
    scene sm1cs-mes004-60 mc-mes-look_c1 with dissolve
    play voice2 mc_pain_auh1 noloop
    mc "*weakly* My brain."
    play voice2 mc_pain_cough1 noloop
    with vpunch
    mc "*coughs*"
    play sound sfx_cup_place1 volume 2.0
    scene sm1cs-mes004-61 mc-mes-look2_c2 with dissolve
    play voice3 min_yes_yeah2 noloop
    mes "Yeah. No more."
    mes "Besides, I have something else I want to talk to {i}you{/i} about."
    play sound sfx_cloth_rustling1
    scene sm1cs-mes004-62 mc-mes-look3_c2 with dissolve
    play voice3 min_happy_mmm noloop
    mes "And I need you to be clear-headed."
    mes "Or as clear-headed as you can be right now."
    scene sm1cs-mes004-63 mc-mes-talk_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What are you talking about?"
    mc "My head is always clear."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes004-64 mc-mes-talk2_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "This is a steel tarp."
    mc "Rain resilient."
    scene sm1cs-mes004-64 mc-mes-talk2_c2 with dissolve
    play voice3 min_happy_laugh4 noloop
    mes "*chuckling* Shut up.{w} I'm trying to be serious."
    scene sm1cs-mes004-65 mc-mes-talk3_c1 with dissolve
    play voice2 mc_disgust_pfe1 noloop
    mc "Serious Squizzle."
    play sound sfx_cloth_rustling2
    scene sm1cs-mes004-65 mc-mes-talk3_c2 with dissolve
    play voice3 min_happy_laugh2 noloop
    mes "*giggling*"
    mes "I know you like watersports."
    mes "What do you think about it?"
    menu:
        "Love it":
            call sm1cs_mes004_m05_c01 from _call_sm1cs_mes004_m05_c01
            play sound sfx_cloth_rustling3
            scene sm1cs-mes004-66 mc-mes-talk4_c1 with dissolve
            play voice2 mc_thinking_hmm9 noloop
            mc "Love it. One of my faves from the last game."
            scene sm1cs-mes004-66 mc-mes-talk4_c2 with dissolve
            play voice3 min_surprised_what noloop
            mes "What?"
            scene sm1cs-mes004-66 mc-mes-talk4_c1 with dissolve
            play voice2 d9s2_yeah noloop volume 1.8
            mc "I said I love it."
        "I could live without it":
            play sound sfx_cloth_rustling3
            scene sm1cs-mes004-67 mc-mes-talk5_c1 with dissolve
            play voice2 mc_disappointed_meh1 noloop volume 1.7
            mc "Meh. I could live without it."
            scene sm1cs-mes004-67 mc-mes-talk5_c2 with dissolve
            play voice3 min_old_mff noloop volume 1.8
            mes "Mmm."
            mes "I think I could too."
    scene sm1cs-mes004-68 mc-mes-talk6_c2 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "Thinking about how chaotic my life has been since I came back, I thought of something I'd like to try."
    mes "With your help."
    play sound sfx_cloth_rustling5
    scene sm1cs-mes004-69 mc-mes-talk7_c2 with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "I mean, I'd have you do it to me."
    scene sm1cs-mes004-69 mc-mes-talk7_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "And... what kind of thing do you want me to {i}do{/i} to you?"
    scene sm1cs-mes004-70 mc-mes-talk8_c2 with dissolve
    play voice3 min_old_shy noloop volume 1.6
    mes "Orgasm control."
    scene sm1cs-mes004-70 mc-mes-talk8_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mc "For you?"
    scene sm1cs-mes004-70 mc-mes-talk8_c2 with dissolve
    play voice3 min_yes_simple noloop
    mes "Yes."
    mes "I figured, even when I'm being submissive, it would still be me fighting against my weakness."
    mes "A confrontation of wills."
    play sound sfx_hair_scratch1
    scene sm1cs-mes004-71 mc-mes-talk9_c2 with dissolve
    play voice3 min_arrogant_heh2 noloop
    mes "But... *giggles* You and I can definitely have a contest between ourselves."
    mes "Like that first party."
    scene sm1cs-mes004-71 mc-mes-talk9_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I'd like that."
    play sound sfx_bed_slide3
    scene sm1cs-mes004-72 mc-mes-stand_c2 with dissolve
    play voice3 min_happy_yay noloop
    mes "Excellent. Sounds like we figured out what to do for our next date."
    scene sm1cs-mes004-72 mc-mes-stand_c1 with dissolve
    play voice2 d9s2_ugu noloop
    mc "I'm up for anything."
    mc "Except more shots."
    scene sm1cs-mes004-73 mc-mes-stand2_c2 with dissolve
    play voice3 min_happy_laugh3 noloop
    mes "Haha. Yeah. Good plan."
    mes "I should get going."
    play sound sfx_bed_slide2
    scene sm1cs-mes004-73 mc-mes-stand2_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "I'll walk you out."
    stop sound4 fadeout 2.0
    jump sm1cs_mes004_street
label sm1cs_mes004_street:
    play sound3 sfx_crowd_fightclub_ambient1 fadein 3.5 volume 0.3
    queue sound4 sfx_distanttraffic_city fadein 2.0
    $ renpy.music.set_volume(1.0, 3.5, "music" )
    $ renpy.music.set_volume(0.0, 5.0, "music2" )
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mes004-74 mc-mes-walk_c2 with long_fade
    play voice3 min_disgust_off noloop
    mes "Brrrr."
    scene sm1cs-mes004-74 mc-mes-walk_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Come here."
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-mes004-75 mc-mes-walk2_c2 with dissolve
    queue sound2 sfx_heels_steps2
    play voice3 min_happy_mmm noloop
    mes "Mrmmm."
    scene sm1cs-mes004-76 mc-mes-walk3_c2 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "I'm a lucky girl to have you in my life, [mcname]."
    scene sm1cs-mes004-76 mc-mes-walk3_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I was thinking the same."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mes004-77 mc-mes-look_c2 with dissolve
    play voice3 min_disappointed_off noloop
    mes "I'm serious."
    mes "Sex is sex, but what we have goes deeper."
    mes "Doesn't it?"
    scene sm1cs-mes004-77 mc-mes-look_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "It does, Min."
    scene sm1cs-mes004-78 mc-mes-close_c1 with dissolve
    play voice3 min_old_upset noloop volume 2.4
    mes "[mcname]..."
    scene sm1cs-mes004-78 mc-mes-close_c2 with dissolve
    call buzz from _call_buzz_6
    play voice3 min_angry_argh1 noloop
    mes "Sonuva."
    play sound sfx_phone_buzz
    scene sm1cs-mes004-79 mc-mes-phone_c2 with dissolve
    play voice3 min_angry_argh2 noloop
    mes "Nuts.{w} Looks like I screwed up part of my introduction for a paper."
    mes "The professor says I've got to get it fixed right away."
    scene sm1cs-mes004-79 mc-mes-phone_c1 with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "And this is why I'm glad to be done with college."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes004-80 mc-mes-close_c2 with dissolve
    play voice3 min_yes_active noloop
    mes "You say that now, but you're going to be crying like a baby when I'm making three times what you make."
    scene sm1cs-mes004-81 mc-mes-close2_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "Fair enough."
    scene sm1cs-mes004-82 mc-mes-talk_c2 with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "Good night, [mcname]."
    scene sm1cs-mes004-82 mc-mes-talk_c1 with dissolve
    play voice2 mc_hey_bye2 noloop
    mc "Good night, Min."
    stop sound4 fadeout 2.5
    stop sound3 fadeout 2.0
    jump sm1cs_mes004_end_scene
label sm1cs_mes004_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(MES_STORY, 4, 0, 2, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1cs_mes004_m01_c01:
    $ player.set_choice("sm1cs_mes004_not_foolish")
    return
label sm1cs_mes004_m02_c02:
    $ player.set_choice("sm1cs_mes004_do_shots")
    return
label sm1cs_mes004_m03_c01:
    $ player.set_choice("sm1cs_mes004_more_shots")
    return
label sm1cs_mes004_m04_c01:
    $ player.set_choice("sm1cs_mes004_kiss_and_tell")
    return
label sm1cs_mes004_m05_c01:
    $ player.set_choice("sm1cs_mes004_love_watersports")
    return