label sm1cs_vs_renovation:
    $ renpy.music.set_volume(0.4, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_silly_naive_b
    play sound sfx_heels_steps1 loop
    scene sm1cs-vs-01 mc-vs-entry1_c2 with dissolve
    pause
    scene sm1cs-vs-02 mc-vs-entry2_c2 with dissolve
    play voice3 girl33_hey_involved noloop
    vs "Hey [mcname]. What's new with you?"
    stop sound fadeout 1.0
    scene sm1cs-vs-12 mc-vs-look_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Not much."
    play sound sfx_cloth_rustling1
    scene sm1cs-vs-04 mc-vs-look_c1 with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Should I even ask what you're doing? Is this for one of those VidVok videos?"
    scene sm1cs-vs-04 mc-vs-look_c2 with dissolve
    play voice3 girl33_arrogant_huh1 noloop
    vs "As if. I start trends, I don't follow them."
    play sound sfx_cloth_rustling2
    scene sm1cs-vs-05 mc-vs-look2_c2 with dissolve
    play voice3 girl33_thinking_eem2 noloop
    vs "But I might need your help."
    vs "I started thinking that maybe I should add some photos of me with props onto my Gram."
    play sound sfx_cloth_rustling3
    scene sm1cs-vs-07 mc-vs-look_c2 with dissolve
    play voice3 girl33_thinking_hmm1 noloop
    vs "Once people see me looking all dramatic, I'm sure a big movie person will reach out."
    scene sm1cs-vs-07 mc-vs-look_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh. And what makes these poses dramatic?"
    play sound sfx_cloth_rustling5
    scene sm1cs-vs-08 mc-vs-look2_c2 with dissolve
    play voice3 girl33_arrogant_hm noloop
    vs "The candle holder, duh. What is it being used for?"
    vs "Am I exploring a spooky house, all on my lonesome?"
    play sound sfx_epic_jump1
    scene sm1cs-vs-09 mc-vs-look3_c2 with hpunch
    play voice3 girl33_surprised_oh noloop
    vs "Or could it be a murder tool and I'm playing the detective."
    vs "Oh no! I was the murderer all along."
    menu:
        "Pretend to be scared."(hint="sm1cs_vs_renovation_m01_h01"):
            scene sm1cs-vs-09 mc-vs-look3_c1 with hpunch
            play voice2 mc_surprised_huh5 noloop volume 1.7
            mc "Ayieee. Please spare my life."
            scene sm1cs-vs-10 mc-vs-smile_c2 with dissolve
            play voice3 girl33_happy_laugh1 noloop
            vs "Haha. It's alright, [mcname]. I was just acting."
        "Act impressed."(hint="sm1cs_vs_renovation_m01_h02"):
            call sm1cs_vs_renovation_m01_c02 from _call_sm1cs_vs_renovation_m01_c02
            play sound sfx_applause_oneperson1
            scene sm1cs-vs-11 mc-vs-clap_c1 with dissolve
            play voice2 d1s5_mchappy noloop volume 2.0
            mc "Not bad at all."
            stop sound fadeout 1.0
    play sound2 sfx_cloth_rustling2 noloop
    scene sm1cs-vs-12 mc-vs-look_c2 with dissolve
    play voice3 girl33_happy_nice noloop
    vs "I never knew there were so many things you can do with a candle holder."
    vs "The name is very deceiving."
    scene sm1cs-vs-15 mc-vs-look4_c2 with dissolve
    play voice3 girl33_happy_laugh3 noloop
    vs "Haha. See, even you can hardly take your eyes off me."
    scene sm1cs-vs-15 mc-vs-look4_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Guilty as charged."
    scene sm1cs-vs-14 mc-vs-look3_c2 with dissolve
    play voice3 girl33_happy_laugh2 noloop
    vs "*giggles* I challenge anyone on the cast to look as hot as me with a prop."
    play voice2 mc_yes_yes7 noloop
    mc "You've certainly got my vote."
    play sound sfx_bag_fall1 volume 1.6
    scene sm1cs-vs-16 mc-vs-look5_c3 with dissolve
    play voice3 girl33_happy_relief noloop
    vs "You know... I'm getting a little excited thinking about when the next Blitz alert will go off."
    vs "Maybe it will go off when I'm on stage."
    scene sm1cs-vs-17 mc-vs-talk_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I don't think you should have your phone with you if you're actually doing a show."
    scene sm1cs-vs-17 mc-vs-talk_c2 with dissolve
    play voice3 girl33_disappointed_off noloop
    vs "Oh come on, [mcname]. Like you've never broken a rule."
    scene sm1cs-vs-19 mc-vs-talk3_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    if True:
        mc "Oh I definitely have, but I'm not going to do something that might keep me from becoming a actor in the group."
        scene sm1cs-vs-19 mc-vs-talk3_c2 with dissolve
        play voice3 girl33_yes_yeah noloop
        vs "You'll get there one day. I know it."
    else:
        mc "I'll leave the rule-breaking to you."
        mc "Now that I'm with the cast, I don't want to give Denise the excuse to bump me down."
        scene sm1cs-vs-19 mc-vs-talk3_c2 with dissolve
        play voice3 girl33_yes_yeah noloop
        vs "I guess that's the smart thing to do."
    scene sm1cs-vs-20 mc-vs-talk4_c2 with dissolve
    play voice3 girl33_happy_mmm noloop
    vs "In the meantime, you can just imagine me, with my phone buzzing on my hip, at the best or worst moment."
    scene sm1cs-vs-21 mc-vs-talk5_c2 with dissolve
    play voice3 girl33_thinking_hmm3 noloop
    vs "It gets me excited... thinking about when it will go off."
    vs "Like a sexy bomb, but it's not filled with c4."
    vs "It's filled with orgasms."
    scene sm1cs-vs-21 mc-vs-talk5_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "That's certainly one way to look at it."
    scene sm1cs-vs-21 mc-vs-talk5_c3 with dissolve
    play voice3 girl33_arrogant_laugh noloop
    vs "I hope you'll be able to get free when it goes off, mister."
    vs "I'd hate to have to do my Blitz challenge with Taisia."
    play sound sfx_hands_clap1
    scene sm1cs-vs-22 mc-vs-talk6_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Oh, don't worry. I'll come running if the Blitz alarm goes off."
    mc "Or at least I'll try."
    scene sm1cs-vs-22 mc-vs-talk6_c2 with dissolve
    play voice3 girl33_surprised_huh4 noloop
    vs "You'll try? What do you mean? Did I do something wrong?"
    scene sm1cs-vs-17 mc-vs-talk_c1 with dissolve
    play voice2 d9s3_no noloop volume 2.0
    mc "No no at all, Veronica."
    mc "Nothing is wrong. I'm just in the middle of a remodel right now, so I'm spread a little thin."
    scene sm1cs-vs-17 mc-vs-talk_c2 with dissolve
    play voice3 girl33_scared_oh noloop
    vs "A remodel? Sounds like fun."
    play voice2 mc_disappointed_ehh4 noloop
    mc "Eh, not the word I'd use for it."
    vs "If it's not fun, why are you doing it?"
    mc "Just something that needed to happen."
    scene sm1cs-vs-18 mc-vs-talk2_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "My roommate and I needed to improve things. We're planning to do some video projects from home."
    if player.has_played_scene("sm1ms018"):
        mc "You remember Stacy? She came to visit the theater."
        scene sm1cs-vs-18 mc-vs-talk2_c2 with dissolve
        play voice3 girl33_happy_yeah noloop
        if persistent.is_special:
            vs "Oh yeah, she's your sister right?"
        else:
            vs "Oh yeah, she's your best friend, right?"
        scene sm1cs-vs-19 mc-vs-talk3_c1 with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "Yup. We actually live together. Used to be a warehouse but we're making it our own."
    scene sm1cs-vs-19 mc-vs-talk3_c2 with dissolve
    play voice3 girl33_thinking_hmm2 noloop
    vs "That is pretty cool. I mean, I have my dorm room, but it's hardly a home."
    vs "So what are you fixing up?"
    scene sm1cs-vs-20 mc-vs-talk4_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "It's kind of a top-to-bottom fix. Lots of new furniture, but also just fixing it up so we can get to the second floor without risking any broken bones."
    scene sm1cs-vs-20 mc-vs-talk4_c2 with dissolve
    play voice3 girl33_surprised_huh1 noloop
    vs "Do you need help?"
    vs "I'm not much for heavy lifting, but my arms are flexible like the rest of me."
    vs "If you need someone to get into those tight, hard-to-reach spots, I'm your girl."
    scene sm1cs-vs-21 mc-vs-talk5_c1 with dissolve
    play voice2 mc_yes_yes8 noloop
    mc "We could use all the help we can get."
    scene sm1cs-vs-21 mc-vs-talk5_c2 with dissolve
    play voice3 girl33_arrogant_he noloop
    vs "How about now?"
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    scene sm1cs-vs-21 mc-vs-talk5_c3 with dissolve
    play voice3 girl33_yes_yep noloop
    vs "Sure, I'm done with the theater today anyhow."
    vs "Actually, Denise might be in trouble if she doesn't announce our new thing soon."
    vs "I'm starting to get bored."
    scene sm1cs-vs-22 mc-vs-talk6_c1 with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "Well, we can't have that."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1cs-vs-36 mc-vs-walk_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "{i}🎶Come with me, and you'll be-🎶{/i}"
    mc "{i}🎶In a world of scaffolding and exposed wi-ir-i-ng!🎶{/i}"
    scene sm1cs-vs-36 mc-vs-walk_c2 with dissolve
    play voice3 girl33_happy_laugh4 noloop
    vs "Haha. You did not just sully Willy Wonka with a joke about exposed wiring."
    scene sm1cs-vs-36 mc-vs-walk_c3 with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "I did. Still coming?"
    play voice3 girl33_yes_aga noloop
    vs "Sure. If only to see what you sing about next."
    stop sound2 fadeout 1.0
    play sound sfx_door_open1
    scene sm1cs-vs-39 mc-vs-walk4_c1 with Fade(0.5, 0.5, 0.5)
    play voice3 girl33_surprised_ohmy noloop
    vs "My God, [mcname]. When you said you had a space, you didn't say you had a fucking 'space'."
    scene sm1cs-vs-39 mc-vs-walk4_c2 with dissolve
    play voice3 girl33_surprised_wow noloop
    vs "I remember music videos being filmed in a space this big."
    vs "How can you afford this?"
    scene sm1cs-vs-41 mc-vs-look_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I know a really great real estate agent."
    play sound sfx_box_slide
    scene sm1cs-vs-42 mc-vs-look2_c2 with dissolve
    play voice3 girl33_surprised_huh3 noloop
    vs "A box full of pillows."
    play sound sfx_cloth_planket3
    scene sm1cs-vs-43 mc-vs-look3_c2 with dissolve
    play voice3 girl33_happy_laugh6 noloop
    vs "Mr. Fancy over here."
    scene sm1cs-vs-44 mc-vs-look4_c1 with dissolve
    play voice3 girl33_disappointed_mmf1 noloop
    vs "Let's see. Which one is the best pillow."
    play voice2 mc_arrogant_heh1 noloop
    mc "You're not really being helpful."
    play voice2 mc_pain_mff2 noloop volume 1.7
    play sound sfx_cloth_planket3
    play sound2 sfx_leg_kick2 noloop
    scene sm1cs-vs-45 mc-vs-pillow_c1 with hpunch
    mc "Uffh."
    scene sm1cs-vs-47 mc-vs-pillow3_c2 with dissolve
    play voice3 girl33_happy_laugh5 noloop
    vs "Hehehe. Lighten up."
    vs "You said you've been super busy, so Dr. Veronica is here to give you 10 cc's of fun."
    play sound sfx_kick_wack1
    scene sm1cs-vs-49 mc-vs-close_c1 with dissolve
    stop sound fadeout 1.0
    play voice3 girl33_arrogant_laugh noloop
    vs "Boop."
    play voice2 mc_angry_errr2 noloop
    play sound sfx_throw_something1 volume 2.0
    play sound2 sfx_stone_run1
    play sound3 sfx_socks_dancing1
    scene sm1cs-vs-50 mc-vs-chasing_c1 with hpunch
    mc "Come here, you!"
    scene sm1cs-vs-50 mc-vs-chasing_c2 with dissolve
    play voice3 girl33_scared_ah3 noloop volume 0.7
    vs "Woop woop woop woop!"
    scene sm1cs-vs-51 mc-vs-chasing2_c1 with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "You said you came here to help out."
    scene sm1cs-vs-51 mc-vs-chasing2_c2 with dissolve
    play voice3 girl33_happy_yeah noloop
    vs "Yeah, but this is way more fun."
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1cs-vs-52 mc-vs-chasing3_c1 with fade
    pause
    play sound sfx_cloth_planket3
    scene sm1cs-vs-52 mc-vs-chasing3_c2 with fade
    pause
    play sound sfx_epic_jump1
    scene sm1cs-vs-54 mc-vs-pillow2_c1 with fade
    pause
    play sound sfx_epic_kick2
    scene sm1cs-vs-54 mc-vs-pillow2_c2 with fade
    pause
    scene sm1cs-vs-55 mc-vs-pillow3_c2 with dissolve
    pause
    $ renpy.music.set_volume(0.4, 2.5, "music" )
    play sound sfx_cloth_rustling4 volume 1.6
    scene sm1cs-vs-56 mc-vs-pillow4_c1 with fade
    play voice2 mc_happy_oof2 noloop
    mc "Okay, this was fun."
    scene sm1cs-vs-56 mc-vs-pillow4_c2 with dissolve
    play voice3 girl33_hey_serious noloop
    vs "Told you. I'm a professional."
    play voice2 mc_surprised_what7 noloop
    mc "A professional what?"
    play sound sfx_box_slide
    scene sm1cs-vs-57 mc-vs-look_c2 with fade
    play voice3 girl33_surprised_huh2 noloop
    vs "Oh, what's that?"
    play voice2 mc_arrogant_hm1 noloop
    mc "A box of prints for the upstairs."
    vs "I gotta see them."
    play sound sfx_paper_bag_1
    scene sm1cs-vs-58 mc-vs-look2_c2 with dissolve
    stop sound fadeout 3.0
    play voice3 girl33_happy_relief noloop
    vs "Woah. So this is kind of like a Fetish Locator thing."
    scene sm1cs-vs-59 mc-vs-look3_c1 with dissolve
    play voice2 mc_no_no10 noloop
    mc "Umm. No, not really."
    mc "My roommate is just a really kinky girl."
    play sound sfx_paper_bag_2
    scene sm1cs-vs-59 mc-vs-look3_c2 with dissolve
    play voice3 girl33_surprised_oh noloop
    vs "Oooouh. I see why you live with her."
    vs "Are you two doing Blitz challenges too?"
    scene sm1cs-vs-60 mc-vs-ask_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What? No. That's just with you."
    scene sm1cs-vs-60 mc-vs-ask_c2 with dissolve
    play voice3 girl33_arrogant_huh2 noloop
    vs "Really?{w} Well, I am very special after all."
    vs "I'll have to figure out some way to honor you back in return."
    play sound sfx_hair_scratch1
    scene sm1cs-vs-61 mc-vs-look_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "That sounds good. But before that time, maybe you can help me clean up the place a bit."
    mc "I never knew a ceiling could leak so much dust before we started fixing up things."
    scene sm1cs-vs-61 mc-vs-look_c2 with dissolve
    play voice3 girl33_happy_laugh1 noloop
    vs "Haha. Alright, I guess I should actually help a little bit."
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1cs-vs-62 mc-vs-sweeping_c1 with fade
    play sound sfx_cleaning_floor2
    play sound2 sfx_cleaning_floor1
    pause
    scene sm1cs-vs-63 mc-vs-sweeping2_c1 with dissolve
    pause
    scene sm1cs-vs-64 mc-vs-sweeping3_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.4, 2.5, "music" )
    stop sound fadeout 1.5
    stop sound2 fadeout 1.5
    scene sm1cs-vs-65 mc-vs-ask_c2 with fade
    play voice3 girl33_happy_phew noloop
    vs "Phew. These hands were not meant for sweeping."
    scene sm1cs-vs-66 mc-vs-look_c1 with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah, what was that? Like ten, twelve minutes?"
    play sound sfx_throw_something1
    scene sm1cs-vs-67 mc-vs-look2_c2 with dissolve
    play voice3 girl33_hey_angry noloop
    vs "These are the hands of a future movie star, [mcname]."
    vs "Not a janitor."
    scene sm1cs-vs-68 mc-vs-talk_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 2.4
    mc "Hehe. Fair enough. Still, even just a little clean up means I don't wake up with lungs full of dust."
    mc "So thanks for your help, Veronica."
    scene sm1cs-vs-68 mc-vs-talk_c2 with dissolve
    play voice3 girl33_yes_simple noloop
    vs "Any time."
    vs "And by any time, I mean I'm down to help you out so long as I never have to clean up for you again."
    vs "Unless it's Blitz related."
    play sound sfx_hands_clap3
    scene sm1cs-vs-69 mc-vs-close_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Haha. Deal."
    play sound sfx_cloth_rustling1 volume 1.6
    scene sm1cs-vs-70 mc-vs-phone_c1 with dissolve
    play voice3 girl33_disappointed_oh noloop
    vs "Wow. Time flies when you're slaving away behind a broom. I should get going."
    play sound sfx_cloth_rustling4
    scene sm1cs-vs-71 mc-vs-hug_c1 with dissolve
    play voice3 girl33_disappointed_mmf2 noloop
    vs "I'll see you at the theater next time, [mcname]."
    scene sm1cs-vs-71 mc-vs-hug_c2 with dissolve
    play voice3 girl33_thinking_hmm3 noloop
    vs "Unless the Blitz alarm goes off before then..."
    play voice2 mc_yes_yes4 noloop
    mc "One can hope."
    play voice3 girl33_happy_laugh2 noloop
    vs "*giggles*"
    play sound sfx_heels_steps1 loop
    scene sm1cs-vs-73 mc-vs-walk_c2 with dissolve
    play voice3 girl33_hey_bye3 noloop
    vs "Time for my exit."
    scene sm1cs-vs-74 mc-vs-walk2_c1 with dissolve
    play voice2 mc_hey_bye1 noloop
    mc "Bye, Veronica."
    scene sm1cs-vs-74 mc-vs-walk2_c2 with dissolve
    pause
    play sound sfx_door_openclosed1
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2")
    jump sm1cs_vs_renovation_end
label sm1cs_vs_renovation_end:
    $ renovation_controller.set_progress(renovation_controller.get_renovation_scenes_progress())
    $ renovation_controller.set_daily_limit()
    $ StoryController.end_scene_without_storyline("sm1cs_vs_renovation", 2, 0, 2, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1cs_vs_renovation_m01_c02:
    $ player.set_choice("sm1cs_vs_renovation_act_impressed")
    return