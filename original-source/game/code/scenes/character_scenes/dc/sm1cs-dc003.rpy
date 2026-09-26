label sm1cs_dc003:
    $ renpy.music.set_volume(0.8, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.5, "sound4" )
    play sound4 sfx_parkday_birds
    $ renpy.music.play(audio.music_starducks1, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_starducks1_radio, "music2", True, None, True, 0.0)
    scene sm1cs-dc003-00-5 mc-dc-cafe_c2 with fade
    pause
    stop sound4 fadeout 1.5
    $ renpy.music.set_volume(0.0, 1.5, "music" )
    $ renpy.music.set_volume(1.0, 1.5, "music2" )
    if LocationController.get_map_location(STARDUCKS).get_location().get_discovered_status() is False:
        scene sm1cs-dc003-00-6 mc-dc-cs-entry2_c1 with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "Let me grab some coffee for both of us, I insist."
        scene sm1cs-dc003-00-6 mc-dc-cs-entry2_c2 with dissolve
        play voice3 girl36_surprised_aah noloop
        dc "But..."
        play voice2 mc_no_no1 noloop
        mc "No buts."
        dc "Dark roast then... Please."
        scene sm1cs-cs001-02 mc-cs-start2_c1 with dissolve
        call sm1cs_cs001 from _call_sm1cs_cs001
        stop sound fadeout 1.0
        scene smcs-am003-25 mc-am-cs-wait3_c1 with dissolve
        play voice4 girl37_happy_relief noloop
        cs "And here you go."
        play voice2 mc_happy_yay3 noloop
        mc "Thank you!"
    else:
        scene sm1cs-dc003-01 mc-dc-cs-start1_c1 with dissolve
        pause
        play sound sfx_cloth_rustling1
        scene sm1cs-dc003-02 mc-dc-cs-start2_c2 with dissolve
        play voice3 girl36_hey_greeting3 noloop
        dc "Here you go! One medium coffee."
        scene sm1cs-dc003-02 mc-dc-cs-start2_c1 with dissolve
        play voice2 mc_happy_yay1 noloop
        mc "Thank you!"
        play sound sfx_bed_slide3 volume 0.7
        scene sm1cs-dc003-03 mc-dc-cs-sit1_c2 with dissolve
        play voice3 girl36_thinking_eem noloop
        dc "You know, you could have gotten something fancier."
        scene sm1cs-dc003-03 mc-dc-cs-sit1_c1 with dissolve
        play voice2 mc_no_no2 noloop
        mc "Well I like just regular coffee."
        play sound sfx_cloth_rustling2
        scene sm1cs-dc003-04 mc-dc-cs-sit2_c2 with dissolve
        play voice3 girl36_disappointed_aah noloop
        dc "So... You regularly get this?"
        scene sm1cs-dc003-04 mc-dc-cs-sit2_c1 with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "Yep! Just a regular old drip coffee."
        scene sm1cs-dc003-06 mc-dc-cs-sit4_c2 with dissolve
        play voice3 girl36_surprised_huh2 noloop
        dc "Not even like an americano?"
        play sound sfx_drink_loop1 volume 2.0
        scene sm1cs-dc003-07 mc-dc-cs-sit5_c1 with dissolve
        play voice2 mc_no_nope1 noloop
        mc "I'm a man of simple tastes."
        play voice3 girl36_surprised_oh noloop
        stop sound fadeout 1.0
        dc "Oh boy, well it sounds like we may have to get coffee more often. I need to expand your horizons, [mcname]."
        play voice2 mc_yes_yeah8 noloop
        mc "Oh yeah? What do you normally get?"
        scene sm1cs-dc003-06 mc-dc-cs-sit4_c2 with dissolve
        play voice3 girl36_thinking_oh noloop
        dc "Depends. If I'm having a particularly long or rough work day, I'll get a red eye. Otherwise, I'm a sucker for a good white chocolate mocha."
        mct "I'll have to remember that."
    scene sm1cs-dc003-07 mc-dc-cs-sit5_c1 with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Well thanks for bringing me here!"
    scene sm1cs-dc003-07 mc-dc-cs-sit5_c2 with dissolve
    play voice3 girl36_yes_aga noloop
    dc "Of course. Have you been here before?"
    scene sm1cs-dc003-08 mc-dc-cs-sit6_c1 with dissolve
    if player.has_played_scene("sm1cs-am001"):
        play voice2 mc_yes_aga1 noloop
        mc "I have! A friend brought me here a bit ago."
    else:
        play voice2 mc_no_nope2 noloop
        mc "Nope! This is my first time."
    scene sm1cs-dc003-05 mc-dc-cs-sit3_c1 with dissolve
    play sound sfx_drink_slurp2
    pause
    scene sm1cs-dc003-09 mc-dc-cs-sit7_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "But I'm happy to be here, they've got great coffee."
    scene sm1cs-dc003-09 mc-dc-cs-sit7_c2 with dissolve
    play voice3 girl36_happy_yeah noloop
    dc "Good! I'm happy to be here with you.{w} And I can't say sorry enough about what happened the other night in the park."
    play sound sfx_cup_slide1
    scene sm1cs-dc003-10 mc-dc-cs-sit8_c1 with dissolve
    play voice2 mc_no_nono1 noloop
    mc "You've got nothing to apologize for. Hindsight being 20-20, probably shouldn't have been sneaking around the park while the Midnight Creep is on the loose."
    scene sm1cs-dc003-10 mc-dc-cs-sit8_c2 with dissolve
    play voice3 girl36_happy_laugh1 noloop
    dc "Definitely wasn't your brightest idea."
    dc "But I am happy you were there."
    play sound sfx_cup_slide1
    scene sm1cs-dc003-11 mc-dc-cs-sit9_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "But we didn't catch the guy."
    scene sm1cs-dc003-11 mc-dc-cs-sit9_c2 with dissolve
    play voice3 girl36_hey_greeting1 noloop
    dc "But that's the closest I've gotten to catching him! So it was progress."
    scene sm1cs-dc003-12 mc-dc-cs-sit10_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Well I'm glad I was able to help."
    if player.get_choice("sm1cs_dc002_backup") is True:
        mc "Partner."
    play sound sfx_door_openclosed2
    scene sm1cs-dc003-13 mc-dc-cs-talk1_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "So, Debbie! How long have you been the park cop?"
    scene sm1cs-dc003-13 mc-dc-cs-talk1_c2 with dissolve
    play voice3 girl36_arrogant_hmf noloop
    dc "It's... Pretty new."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    dc "Yeah. I just got transferred to Crowning from a small, coastal town and this is my first assignment with my new department."
    scene sm1cs-dc003-14 mc-dc-cs-talk2_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "You just got transferred?"
    scene sm1cs-dc003-14 mc-dc-cs-talk2_c2 with dissolve
    play voice3 girl36_yes_yep noloop
    dc "Uh huh. Being out on the coast was a treat, but I wanted to move closer to where I grew up. I just missed being close to home."
    play voice2 mc_hey_hey10 noloop
    mc "Welcome back then!"
    dc "Thank you! It's nice to be here."
    scene sm1cs-dc003-15 mc-dc-cs-talk3_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Where'd you grow up?"
    scene sm1cs-dc003-15 mc-dc-cs-talk3_c2 with dissolve
    play voice3 girl36_disappointed_eeh noloop
    dc "Maybe an hour outside of Crowning. Small, little town you've probably never heard of."
    play sound sfx_heels_steps2 loop
    scene sm1cs-dc003-16 mc-dc-cs-talk4_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Why move here instead of there?"
    scene sm1cs-dc003-16 mc-dc-cs-talk4_c2 with dissolve
    play voice3 girl36_disappointed_oof noloop
    dc "Where I grew up, there isn't a lot of crime... It's just the same group of guys getting arrested for the same thing over, and over. I wanted to live somewhere where I could make a difference."
    stop sound fadeout 2.0
    scene sm1cs-dc003-17 mc-dc-cs-talk5_c1 with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Being a cop is really important to you, isn't it?"
    play voice3 girl36_yes_calm2 noloop
    dc "It is."
    mc "Can I ask why you wanted to be a cop?"
    dc "Uhm..."
    scene sm1cs-dc003-17 mc-dc-cs-talk5_c2 with dissolve
    play voice3 girl36_disgust_mneagh noloop
    dc "It's not the happiest of tales."
    scene sm1cs-dc003-18 mc-dc-cs-talk6_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "That's okay! Life isn't always super happy, you know?"
    scene sm1cs-dc003-18 mc-dc-cs-talk6_c2 with dissolve
    play voice3 girl36_thinking_iknow noloop
    dc "Okay, well... When I was growing up, there was an old sheriff who worked in our town."
    dc "He was well liked enough, but... When I was in high school it turned out that the sheriff was actually making and selling a whole bunch of drugs."
    scene sm1cs-dc003-20 mc-dc-cs-talk8_c2 with dissolve
    play voice3 girl36_disappointed_geh noloop
    dc "He got away with it for a long time because of the badge."
    dc "That was the moment I knew. I wanted to become a cop to arrest bad guys, even if they hid behind a badge. I wanted to make a real difference and help people."
    scene sm1cs-dc003-19 mc-dc-cs-talk7_c1 with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow..."
    play voice3 girl36_surprised_huh1 noloop
    dc "What?"
    mc "That's just super noble. It's also incredible."
    scene sm1cs-dc003-19 mc-dc-cs-talk7_c2 with dissolve
    play voice3 girl36_happy_relief2 noloop
    dc "Thanks, [mcname]."
    play voice2 mc_yes_sure1 noloop
    mc "Of course! {w}What's it like being a cop?"
    dc "You know, it's mostly paperwork. And long shifts of just observing."
    scene sm1cs-dc003-20 mc-dc-cs-talk8_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mc "What do you observe?"
    scene sm1cs-dc003-18 mc-dc-cs-talk6_c2 with dissolve
    play voice3 girl36_thinking_oh noloop
    dc "Oh, just people. Looking for anyone suspicious, or doing something suspicious. Talking to people you see regularly."
    scene sm1cs-dc003-21 mc-dc-cs-talk9_c1 with dissolve
    play voice2 mc_happy_thatsgood noloop
    mc "That doesn't seem so bad. And you've got yourself a case! That's pretty cool!"
    scene sm1cs-dc003-21 mc-dc-cs-talk9_c2 with dissolve
    play voice3 girl36_yes_yeah noloop
    dc "Yeah..."
    scene sm1cs-dc003-22 mc-dc-cs-talk10_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Something wrong?"
    scene sm1cs-dc003-22 mc-dc-cs-talk10_c2 with dissolve
    play voice3 girl36_thinking_eem noloop
    dc "Well..."
    dc "I know we kind of just met, so it feels weird to just... Dump all this on you."
    play voice2 d2s9_confused noloop
    mc "If you don't want-"
    play voice3 girl36_no_calm2 noloop
    dc "No, that's not it. I do need someone to talk to and... You seem like a good person to talk to. I just don't want to overshare, you know?"
    scene sm1cs-dc003-12 mc-dc-cs-sit10_c1 with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.5
    mc "I get that. You can share if you want to, but you don't have to."
    scene sm1cs-dc003-21 mc-dc-cs-talk9_c2 with dissolve
    play voice3 girl36_thinking_hmm noloop
    dc "Well..."
    dc "I thought transferring here would be a step forward. I did a few years there, learned some things."
    dc "Like, I've put in my time. So I thought when I transferred, I'd continue with where I was. Maybe make detective, do something that {i}actually{/i} makes a difference."
    scene sm1cs-dc003-22 mc-dc-cs-talk10_c2 with dissolve
    play voice3 girl36_angry_breath noloop
    dc "Instead, I'm walking the park beat. Chasing some weird creep in the middle of the night."
    dc "It's just... Not what I expected."
    scene sm1cs-dc003-22 mc-dc-cs-talk10_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "That sucks, Debbie."
    mc "Why'd they put you in the park?"
    scene sm1cs-dc003-20 mc-dc-cs-talk8_c2 with dissolve
    play voice3 girl36_arrogant_he noloop
    dc "I've heard some people whispering by the water cooler... They all think I'm some country bumpkin who can't handle {i}real{/i} crime."
    scene sm1cs-dc003-20 mc-dc-cs-talk8_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "That's dumb!"
    scene sm1cs-dc003-19 mc-dc-cs-talk7_c2 with dissolve
    play voice3 girl36_arrogant_huh2 noloop
    dc "You know, you're right! It is dumb! They have no idea what I'm capable of."
    dc "Thank you, [mcname]."
    scene sm1cs-dc003-19 mc-dc-cs-talk7_c1 with dissolve
    play voice2 mc_surprised_what7 noloop
    mc "What'd I do?"
    scene sm1cs-dc003-18 mc-dc-cs-talk6_c2 with dissolve
    play voice3 girl36_arrogant_laugh noloop
    dc "You just knew exactly what to say to cheer me up."
    scene sm1cs-dc003-18 mc-dc-cs-talk6_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, I just told you what everyone would think."
    scene sm1cs-dc003-17 mc-dc-cs-talk5_c2 with dissolve
    play voice3 girl36_no_nah1 noloop
    dc "Not what {i}everyone{/i} would think."
    scene sm1cs-dc003-17 mc-dc-cs-talk5_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Well, at least what everyone with half a brain would think."
    scene sm1cs-dc003-18 mc-dc-cs-talk6_c2 with dissolve
    play voice3 girl36_happy_laugh3 noloop
    dc "That's exactly what I mean! You know how to perk me right up."
    scene sm1cs-dc003-21 mc-dc-cs-talk9_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I think you're a good cop, Debbie."
    play voice3 girl36_happy_mmm noloop
    dc "Thank you, [mcname]."
    play voice2 mc_thinking_mmm6 noloop
    mc "And it's good to see more women in uniform!"
    scene sm1cs-dc003-18 mc-dc-cs-talk6_c2 with dissolve
    play voice3 girl36_disappointed_oh noloop
    dc "Oh, is it?"
    menu:
        "Flirt"(hint="sm1cs_dc003_m01_h01"):
            call sm1cs_dc003_m01_c01 from _call_sm1cs_dc003_m01_c01
            mct "Might as well shoot my shot!"
            scene sm1cs-dc003-19 mc-dc-cs-talk7_c1 with dissolve
            play voice2 mc_yes_yes7 noloop
            mc "Of course! Especially when the uniform looks so good on you."
        "Compliment"(hint="sm1cs_dc003_m01_h02"):
            scene sm1cs-dc003-19 mc-dc-cs-talk7_c1 with dissolve
            play voice2 mc_yes_yes7 noloop
            mc "Of course! I've always thought the police needed more women."
    mc "How can anyone resist a woman in uniform?"
    play sound sfx_drink_slurp2
    scene sm1cs-dc003-07 mc-dc-cs-sit5_c2 with dissolve
    stop sound fadeout 1.0
    play voice3 girl36_pain_cough5 noloop
    dc "Oh, uh. Ahem. Yeah."
    play voice2 mc_thinking_mmm5 noloop
    mc "Debbie, everything okay?"
    dc "I, uhm, yep."
    play sound sfx_bed_slide2
    scene sm1cs-dc003-23 mc-dc-cs-stand1_c2 with dissolve
    play voice3 girl36_surprised_eeh noloop
    dc "I'm just realizing that, uh, I need to get back to the park. I've... I've been gone too long."
    scene sm1cs-dc003-23 mc-dc-cs-stand1_c1 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, well I'm sorry I kept you too long."
    scene sm1cs-dc003-24 mc-dc-cs-stand2_c2 with dissolve
    play sound sfx_heels_steps1 loop
    play voice3 girl36_no_happy noloop
    dc "Uhm - yeah, no. It-it's okay."
    scene sm1cs-dc003-24 mc-dc-cs-stand2_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Well we should do this again-"
    scene sm1cs-dc003-24 mc-dc-cs-stand2_c2 with dissolve
    play voice3 girl36_arrogant_yeah2 noloop
    dc "Uh, yeah. We'll - uhm. Uh huh!"
    scene sm1cs-dc003-25 mc-dc-cs-walk1_c1 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mct "Did I say something weird?"
    play sound sfx_door_open5
    play sound4 sfx_distanttraffic_city fadein 4.5
    scene sm1cs-dc003-25 mc-dc-cs-walk1_c2 with dissolve
    mct "Do I have bad breath or something?"
    scene sm1cs-dc003-26 mc-dc-cs-walk2_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mct "Nope, smells minty fresh... I wonder what happened?"
    scene sm1cs-dc003-26 mc-dc-cs-walk2_c2 with dissolve
    mct "I should ask Debbie... Maybe give her a day or two though before I do."
    play sound sfx_heels_steps2
    scene sm1cs-dc003-27 mc-dc-cs-end_c1 with dissolve
    pause
    scene sm1cs-dc003-27 mc-dc-cs-end_c2 with dissolve
    pause
    stop sound4 fadeout 2.0
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(DC_STORY, 1, 0, 1)
    return
label sm1cs_dc003_m01_c01:
    $ player.set_choice("sm1cs_dc003_flirt")
    $ CharacterController.get_character("dc").add_point()
    return
label sm1cs_dc003_unlocks:
    call sm1cs_dc003_m01_c01 from _call_sm1cs_dc003_m01_c01_1
    call sm1cs_cs001_discover_starducks from _call_sm1cs_cs001_discover_starducks_1
    if config_storyline_mode is True:
        $ execute_storyline_config(DC_STORY)
    return