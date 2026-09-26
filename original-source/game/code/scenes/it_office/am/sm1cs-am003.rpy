image sm1cs-am003-glambot-1 = Movie(play = "images/FS_IT/AM/s003/anim/smcs-am003-a19-5-2x-50fps.webm", start_image = "smcs-am003-a19-5 mc-am-phone5-glambot-19-5-000", image = "smcs-am003-a19-5 mc-am-phone5-glambot-19-5-219", loop = False)
label sm1cs_am003:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.6, 0.0, "music2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.6, 0.5, "sound4" )
    $ renpy.music.set_volume(1.0, 0.5, "sound3" )
    play sound4 sfx_parkday_birds fadein 2.0
    scene smcs-am003-01 mc-am-entry1_c1 with dissolve
    play sound sfx_heels_steps2 loop
    play music music_lullaby_acoustic1
    pause
    play music2 music_adroids_metal_headphoned fadein 1.0
    scene smcs-am003-01 mc-am-entry1_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene smcs-am003-02 mc-am-entry2_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey April."
    scene smcs-am003-02 mc-am-entry2_c2 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I emailed you earlier, saying I would meet you here."
    $ renpy.music.set_volume(1.0, 1.0, "music2" )
    scene smcs-am003-03 mc-am-talk1_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "You never replied back."
    scene smcs-am003-03 mc-am-talk1_c2 with dissolve
    play voice3 girl3_disappointed_geh2 noloop
    pause
    stop music2 fadeout 1.0
    scene smcs-am003-04 mc-am-talk2_c1 with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "Do you ever wonder if we went too far?"
    play voice2 mc_surprised_huh7 noloop
    mc "Huh?"
    scene smcs-am003-04 mc-am-talk2_c2 with dissolve
    play voice3 girl22_disappointed_geh noloop
    am "Humans. We have created all this technology. It can do incredible things."
    am "But then those things cost great amounts of time and sweat to maintain. And all the time we put into those things makes us unable to do other things."
    scene smcs-am003-05 mc-am-talk3_c1 with dissolve
    am "Maybe the animals know something we don't."
    play voice2 mc_thinking_oh1 noloop
    mc "Living like animals does sound simpler."
    scene smcs-am003-05 mc-am-talk3_c2 with dissolve
    play voice3 girl22_yes_aga2 noloop
    am "Yup. If we didn't work together, you wouldn't be bothering my afternoon, that's for sure."
    menu:
        "Bothering you is my new favorite pastime, April"(hint="sm1cs_am003_m01_h01"):
            call sm1cs_am003_m01_c01 from _call_sm1cs_am003_m01_c01
            scene smcs-am003-09 mc-am-talk7_c1 with dissolve
            play voice2 mc_no_nah2 noloop
            mc "Nah. Bothering you is my new favorite pastime, April."
            scene smcs-am003-18 mc-am-talk16_c2 with dissolve
            play voice3 girl22_angry_heergh noloop
            am "Stop."
            scene smcs-am003-10 mc-am-talk8_c1 with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "I'm actually pretty sure it's part of my job."
            am "..."
            mct "Hmm. I almost thought she was going to laugh."
        "We can agree on that"(hint="sm1cs_am003_m01_h02"):
            scene smcs-am003-09 mc-am-talk7_c1 with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "So we can agree on something."
            scene smcs-am003-09 mc-am-talk7_c2 with dissolve
            play voice3 girl22_yes_yeah2 noloop
            am "Heh. Imagine that."
    scene smcs-am003-11 mc-am-talk9_c2 with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "So {i}why{/i} are you bothering me again, [mcname]?"
    menu:
        "I had to come here for work."(hint="sm1cs_am003_m02_h01"):
            call sm1cs_am003_m02_c01 from _call_sm1cs_am003_m02_c01
            scene smcs-am003-12 mc-am-talk10_c1 with dissolve
            play voice2 d1s5_mchappy noloop volume 1.6
            mc "I am only here because someone decided to work from a park instead of her station."
            scene smcs-am003-19 mc-am-talk17_c2 with dissolve
            play voice3 girl22_yes_aga1 noloop
            am "Good."
        "I wanted to check on you"(hint="sm1cs_am003_m02_h02"):
            scene smcs-am003-12 mc-am-talk10_c1 with dissolve
            play voice2 d1s5_mchappy noloop volume 1.6
            mc "I wanted to check on you, April."
            scene smcs-am003-12 mc-am-talk10_c2 with dissolve
            play voice3 girl22_thinking_oh noloop
            am "You mean Anna asked you to check on me."
            scene smcs-am003-14 mc-am-talk12_c1 with dissolve
            play voice2 mc_no_no2 noloop
            mc "She did not."
            scene smcs-am003-14 mc-am-talk12_c2 with dissolve
            play voice3 girl22_arrogant_hm noloop
            am "Hmmph. Sounds like you wasted your afternoon. I'm fine."
            scene smcs-am003-15 mc-am-talk13_c1 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "Checking on a friend is not a waste of time, April."
            scene smcs-am003-15 mc-am-talk13_c2 with dissolve
            play voice3 girl22_surprised_what noloop
            am "Who said we were friends?"
            scene smcs-am003-16 mc-am-talk14_c1 with dissolve
            play voice2 mc_arrogant_huh2 noloop
            mc "Well if we're not friends, your teasing feels a lot like bullying."
            scene smcs-am003-16 mc-am-talk14_c2 with dissolve
            play voice3 girl22_yes_yeah3 noloop
            am "It's bullying to say someone sucks at their job?"
            scene smcs-am003-17 mc-am-talk15_c1 with dissolve
            play voice2 mc_angry_errr2 noloop
            mc "Maybe the first time is teasing. I think you're into the double digits now."
            scene smcs-am003-13 mc-am-talk11_c2 with dissolve
            play voice3 girl22_happy_laugh4 noloop
            am "I didn't know you could count that high."
            scene smcs-am003-18 mc-am-talk16_c1 with dissolve
            play voice2 mc_angry_huh2 noloop
            mct "This girl. It's like Anna said. If she wasn't so good, her attitude would have gotten her kicked right out of Orbix."
            mct "Why does she pick on me so much?"
            scene smcs-am003-18 mc-am-talk16_c2 with dissolve
            play voice3 girl22_disappointed_ehh3 noloop
            am "What, did that break you?"
            scene smcs-am003-19 mc-am-talk17_c1 with dissolve
            play voice2 mc_arrogant_hm2 noloop
            mc "You were right. I didn't come to check on you. I need help with a work problem and this is where you are working now. Simple as that."
            scene smcs-am003-19 mc-am-talk17_c2 with dissolve
            play voice3 girl22_yes_yeah1 noloop
            am "Well yeah. I knew that from the start."
    scene smcs-am003-16 mc-am-talk14_c2 with dissolve
    play voice3 girl22_thinking_hmm2 noloop
    am "After that work session, I... I figured you would have either quit or just do the bare minimum with your assignments."
    am "But here you are."
    scene smcs-am003-15 mc-am-talk13_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Here I am."
    scene smcs-am003-14 mc-am-talk12_c2 with dissolve
    play voice3 girl22_happy_yeah noloop
    am "Yeah.{w} Maybe I was wrong about you, [mcname]."
    scene smcs-am003-14 mc-am-talk12_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "You were. I can be a screwup, but I can also work incredibly hard to get what I want. Sometimes I stumble, but I never stay on the ground for long."
    mc "I didn't study IT at college, but I've always been a fast learner. Teach me, I'm ready to learn at your feet, April."
    scene smcs-am003-13 mc-am-talk11_c2 with dissolve
    play voice3 girl22_happy_laugh2 noloop
    am "Learn at my feet? You really are a dork."
    scene smcs-am003-13 mc-am-talk11_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, I'm serious."
    scene smcs-am003-11 mc-am-talk9_c2 with dissolve
    play voice3 girl22_happy_relief noloop
    am "*sighs* Okay, you certainly got the energy. But you're not going near my feet."
    am "Despite my better judgment, I'll try to give you some pointers here and there."
    scene smcs-am003-15 mc-am-talk13_c2 with dissolve
    play voice3 girl22_arrogant_he noloop
    am "Just don't you dare slow me down."
    menu:
        "I'll surpass you in no time"(hint="sm1cs_am003_m03_h01"):
            call sm1cs_am003_m03_c01 from _call_sm1cs_am003_m03_c01
            scene smcs-am003-18 mc-am-talk16_c1 with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "I won't slow you down. In fact, I'm sure in a little while, I'll surpass your skills."
            scene smcs-am003-18 mc-am-talk16_c2 with dissolve
            play voice3 girl22_disappointed_ehh1 noloop
            am "I thought you were being serious..."
        "If you teach me well, I'm sure I'll do great"(hint="sm1cs_am003_m03_h02"):
            call sm1cs_am003_m03_c02 from _call_sm1cs_am003_m03_c02
            scene smcs-am003-18 mc-am-talk16_c1 with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "If you teach me well, I'm sure I'll do great."
            scene smcs-am003-18 mc-am-talk16_c2 with dissolve
            play voice3 girl22_disappointed_ehh1 noloop
            am "I am not your teacher, [mcname]. that's not my job."
            am "The only thing I'm going to do for you is give you some tips and tricks."
            am "We have a shared assignment, but you still have to pull your weight."
            play sound sfx_cloth_rustling1
            scene smcs-am003-19 mc-am-talk17_c1 with dissolve
            play voice2 mc_yes_yeah3 noloop
            mc "Sure, sure. I got it."
    scene smcs-am003-19 mc-am-talk17_c2 with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "Okay. Show me what problems you're having with the website."
    scene smcs-am003-19-1 mc-am-phone1_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    mct "Shit. Bad signal. The file isn't loading."
    scene smcs-am003-19-2 mc-am-phone2_c1 with dissolve
    play voice3 girl22_surprised_huh2 noloop
    am "What are you doing now?"
    play voice2 mc_thinking_emm1 noloop
    mc "Trying to get a signal. Shit. It's still not working."
    scene smcs-am003-19-2 mc-am-phone2_c2 with dissolve
    play voice3 girl22_disappointed_oh noloop
    am "You didn't download a copy of the file to show me?"
    play voice2 mc_yes_yes6 noloop
    mc "I didn't think it would be a problem."
    scene smcs-am003-19-3 mc-am-phone3_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Hey, there is a coffee shop nearby. They gotta have better wifi than the park."
    scene smcs-am003-19-3 mc-am-phone3_c2 with dissolve
    play voice3 girl22_arrogant_yeah noloop
    am "And?"
    play sound sfx_cloth_rustling3
    scene smcs-am003-19-4 mc-am-phone4_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "And you could come with me. It's only a short walk."
    scene smcs-am003-19-4 mc-am-phone4_c2 with dissolve
    play voice3 girl22_yes_yep4 noloop
    am "Okay. But I can only look through the stuff for an hour today."
    play sound sfx_heels_steps2 loop
    scene smcs-am003-19-5 mc-am-phone5_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Then there is no time to waste."
    stop sound fadeout 1.0
    scene smcs-am003-a19-5 mc-am-phone5-glambot-19-5-000 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
    play sound3 ["<silence 4.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs-am003-glambot-1
    pause
    stop sound2 fadeout 1.0
    stop sound fadeout 1.0
    stop music fadeout 3.0
    stop sound4 fadeout 3.0
    play sound3 sfx_distanttraffic_city fadein 2.0
    scene smcs-am003-21 mc-am-cs-entry1_c1 with Fade(1.0, 0.5, 1.0)
    play sound sfx_door_open2
    $ renpy.music.set_volume(1.0, 5.0, "sound4" )
    play voice2 mc_yes_okay2 noloop
    mc "Grab a seat somewhere. What would you like to drink?"
    scene smcs-am003-21 mc-am-cs-entry1_c2 with dissolve
    $ renpy.music.set_volume(0.0, 1.0, "music" )
    play voice3 girl22_happy_mmm noloop
    am "Dark roast coffee."
    $ renpy.music.set_volume(0.4, 3.0, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.play(audio.music_starducks2, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_starducks2_reverbed, "music2", True, None, True, 0.0)
    stop sound3 fadeout 4.0
    if LocationController.get_map_location(STARDUCKS).get_location().get_discovered_status() is False:
        scene sm1cs-cs001-01 mc-cs-start1_c1 with dissolve
        call sm1cs_cs001 from _call_sm1cs_cs001_1
        $ renpy.music.set_volume(0.4, 2.0, "music" )
        $ renpy.music.set_volume(0.0, 2.0, "music2" )
        scene smcs-am003-22 mc-am-cs-entry2_c2 with dissolve
        pause
        scene smcs-am003-23 mc-am-cs-wait1_c1 with dissolve
        pause
        scene smcs-am003-24 mc-am-cs-wait2_c1 with dissolve
        pause
        scene smcs-am003-24 mc-am-cs-wait2_c2 with dissolve
        pause
    else:
        $ renpy.music.set_volume(0.0, 2.0, "music" )
        $ renpy.music.set_volume(0.6, 2.0, "music2" )
        play sound sfx_heels_steps2 loop
        scene smcs-am003-22 mc-am-cs-entry2_c1 with dissolve
        play voice2 mc_hey_hey7 noloop
        mc "One vento light roast and one dark roast please."
        play voice4 girl37_yes_yep noloop
        cs "Sure."
        $ renpy.music.set_volume(0.4, 2.0, "music" )
        $ renpy.music.set_volume(0.0, 2.0, "music2" )
        stop sound fadeout 1.0
        scene smcs-am003-22 mc-am-cs-entry2_c2 with dissolve
        pause
        scene smcs-am003-23 mc-am-cs-wait1_c1 with dissolve
        pause
        play sound sfx_coffee_pouring
        scene smcs-am003-24 mc-am-cs-wait2_c1 with dissolve
        pause
        scene smcs-am003-24 mc-am-cs-wait2_c2 with dissolve
        pause
    $ renpy.music.set_volume(0.0, 2.0, "music" )
    $ renpy.music.set_volume(0.7, 2.0, "music2" )
    scene smcs-am003-25 mc-am-cs-wait3_c1 with dissolve
    stop sound fadeout 1.0
    play voice4 girl37_happy_relief noloop
    cs "And here you go."
    play voice2 mc_happy_yay3 noloop
    mc "Thank you!"
    play sound sfx_heels_steps2
    scene smcs-am003-26 mc-am-cs-walk1_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Ohe dark roast coffee for the girl who roasts me every day."
    scene smcs-am003-26 mc-am-cs-walk1_c2 with dissolve
    play voice3 girl22_hey_attention noloop
    am "Thank you for the drink."
    play sound sfx_bed_slide3 volume 0.5
    scene smcs-am003-27 mc-am-cs-sit1_c1 with dissolve
    play voice2 mc_no_nah1 noloop
    mc "No problem."
    scene smcs-am003-28 mc-am-cs-sit2_c2 with dissolve
    play sound sfx_drink_slurp2
    pause
    scene smcs-am003-28 mc-am-cs-sit2_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.4
    mct "Ah. That is the spot."
    scene smcs-am003-29-2 mc-am-cs-sit3_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Alright let's see."
    scene smcs-am003-29 mc-am-cs-sit3_c2 with dissolve
    play voice3 girl22_surprised_eh1 noloop
    am "You better not be swiping girls on Ember right now."
    scene smcs-am003-30 mc-am-cs-sit4_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Huh? No, I'm getting onto their wifi."
    mc "There. The file is downloaded."
    scene smcs-am003-29 mc-am-cs-sit3_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Is something the matter, April?"
    scene smcs-am003-30 mc-am-cs-sit4_c2 with dissolve
    play voice3 girl22_no_questioning noloop
    am "No. Nothing."
    play sound sfx_drinking_passionately
    scene smcs-am003-34 mc-am-cs-talk3_c2 with dissolve
    pause
    call buzz from _call_buzz_5
    stop sound fadeout 1.0
    scene smcs-am003-36 mc-am-cs-phone1_c2 with dissolve
    play voice3 girl22_pain_cough1 noloop
    am "..."
    play sound sfx_phone_call1
    scene smcs-am003-37 mc-am-cs-phone2_c1 with dissolve
    play voice3 girl22_surprised_eh2 noloop
    am "Hold on one sec."
    scene smcs-am003-37 mc-am-cs-phone2_c2 with dissolve
    play voice3 girl22_hey_happy noloop
    am "Hey Pepper. Yeah, they texted me."
    am "It's going to be great.{w} I'm thinking some face paint.{w} I know, I'm excited."
    scene smcs-am003-38 mc-am-cs-phone3_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "What is going on here? While she's talking to this 'Pepper', its like April is a completely different person."
    scene smcs-am003-38 mc-am-cs-phone3_c2 with dissolve
    play voice3 girl22_yes_yeah3 noloop
    am "Yeah. He just needs to chill."
    am "You know me. I've been practicing during all my free time."
    scene smcs-am003-39 mc-am-cs-phone4_c1 with dissolve
    am "Because I'm {i}with{/i} a guy from work right now."
    scene smcs-am003-39 mc-am-cs-phone4_c2 with dissolve
    play voice3 girl22_surprised_oh noloop
    am "Shut up. Okay.{w} Okay, I don't know about that."
    am "Yes, I will see you later. Bye."
    play sound sfx_phone_hungup1
    scene smcs-am003-40 mc-am-cs-phone5_c2 with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "Pepper is one of my bandmates. We uh... we're going through a rough spot right now, and if someone on the band calls, you pretty much have to pick it up."
    scene smcs-am003-40 mc-am-cs-phone5_c1 with dissolve
    play voice2 mc_surprised_oh1 noloop
    am "I didn't mean to get distracted. You came to me with a problem."
    mc "That's cool. I didn't know you were even in a band. What do you play?"
    scene smcs-am003-41 mc-am-cs-talk1_c2 with dissolve
    play voice3 girl22_yes_aga4 noloop
    am "Guitar. And I sing a bit too. I love it. But lately... lately, it's felt more like work than usual."
    scene smcs-am003-41 mc-am-cs-talk1_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Like it's not fun anymore?"
    scene smcs-am003-42 mc-am-cs-talk2_c2 with dissolve
    play voice3 girl22_yes_simple noloop
    am "Yes. There is a lot of stuff going on. Decisions I... we have to make. Hard decisions."
    am "*clears throat*"
    am "Nobody has asked me out for coffee in a while."
    scene smcs-am003-43 mc-am-cs-talk3_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Uhhh, right."
    scene smcs-am003-43 mc-am-cs-talk3_c2 with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "You wanted to ask me something?"
    play sound sfx_cloth_rustling2
    scene smcs-am003-44 mc-am-cs-phone1_c1 with dissolve
    mc "I needed your help to figure out some code issues on this ticket."
    scene smcs-am003-44 mc-am-cs-phone1_c2 with dissolve
    play voice3 girl22_thinking_oh noloop
    am "Right. But... I thought you were trying to like... turn this into a date or something."
    scene smcs-am003-45 mc-am-cs-phone2_c1 with dissolve
    play voice2 mc_no_no10 noloop
    mc "I think we've got our signals mixed up. If I wanted to ask you on a date, I'd ask you on a date."
    scene smcs-am003-45 mc-am-cs-phone2_c2 with dissolve
    play voice3 girl22_arrogant_ha noloop
    am "Totally. And you wouldn't ask me on a date because you know I'm out of your league."
    play sound sfx_leg_kick8 volume 0.7
    scene smcs-am003-46 mc-am-cs-talk1_c2 with dissolve
    play voice3 girl22_arrogant_he noloop
    am "You're probably too low-maintenance for me anyhow."
    scene smcs-am003-46 mc-am-cs-talk1_c1 with dissolve
    play voice2 mc_pain_auh1 noloop
    mct "Ouch."
    play sound sfx_drink_slurp2
    scene smcs-am003-47 mc-am-cs-talk2_c1 with dissolve
    pause
    scene smcs-am003-33 mc-am-cs-talk2_c2 with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "Listen. I'm not... {w}I tend to keep people at an arm's length."
    scene smcs-am003-47 mc-am-cs-talk2_c2 with dissolve
    play voice3 girl22_thinking_hmm2 noloop
    am "But... I see you now. You're being serious about getting better at coding, aren't you?"
    scene smcs-am003-48 mc-am-cs-talk3_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Is that a big surprise?"
    scene smcs-am003-48 mc-am-cs-talk3_c2 with dissolve
    play voice3 girl22_arrogant_he noloop
    am "I've worked with a lot of assholes, and I thought you'd just be like them. But you're not just sitting around. You're-"
    scene smcs-am003-46 mc-am-cs-talk1_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Trying to not suck all the time."
    scene smcs-am003-48 mc-am-cs-talk3_c2 with dissolve
    play voice3 girl22_happy_laugh3 noloop
    am "Looks that way."
    am "Okay. Let me load up the code, and we can find the problems."
    play sound sfx_cloth_planket2
    scene smcs-am003-49 mc-am-cs-stand1_c2 with dissolve
    play voice3 girl22_yes_aga6 noloop
    am "Come over and sit besides me. You can't see the screen from there."
    scene smcs-am003-49 mc-am-cs-stand1_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    pause
    scene smcs-am003-50 mc-am-cs-sit1_c1 with fade
    play sound sfx_keyboard_typing2 volume 1.6
    play voice2 mc_arrogant_huh1 noloop
    mc "That's it?"
    scene smcs-am003-50 mc-am-cs-sit1_c2 with dissolve
    play voice3 girl22_yes_yep1 noloop
    am "That's it. Nice work."
    scene smcs-am003-52 mc-am-cs-laptop2_c2 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "It was mostly you."
    play voice3 girl22_yes_yeah1 noloop
    am "Well yeah, but you still noticed that line forty-two was the root issue of why the first batch wasn't connecting to the second one."
    scene smcs-am003-53 mc-am-cs-laptop3_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "So I'm a elite-code-monkey now, right?"
    scene smcs-am003-53 mc-am-cs-laptop3_c2 with dissolve
    play voice3 girl22_happy_yeah noloop
    am "Oh yeah. A future Wozniak."
    play sound sfx_gadgets_laptop_closed
    scene smcs-am003-54 mc-am-cs-laptop4_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "That guy is super smart right?"
    play sound sfx_cloth_rustling1
    scene smcs-am003-54 mc-am-cs-laptop4_c2 with dissolve
    play voice3 girl22_arrogant_hm noloop
    am "Yes. Very smart."
    scene smcs-am003-57 mc-am-cs-talk3_c1 with dissolve
    play sound sfx_message_in1
    pause
    scene smcs-am003-56 mc-am-cs-talk2_c1 with dissolve
    play voice3 girl22_hey_simple noloop
    am "I need to get going. But I'll see you at work. Either at the park or back in the mines."
    scene smcs-am003-56 mc-am-cs-talk2_c2 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah."
    play sound sfx_heels_steps2 loop
    $ renpy.music.set_volume(0.4, 2.0, "music" )
    $ renpy.music.set_volume(0.0, 2.0, "music2" )
    scene smcs-am003-58 mc-am-cs-walk1_c1 with dissolve
    pause
    scene smcs-am003-58 mc-am-cs-walk1_c2 with dissolve
    pause
    $ renpy.music.set_volume(0.0, 2.0, "music" )
    $ renpy.music.set_volume(0.7, 2.0, "music2" )
    scene smcs-am003-59 mc-am-cs-walk2_c2 with dissolve
    play voice3 girl22_hey_attention noloop
    if gt.curr_day == WEDNESDAY:
        am "Hey. If you're not busy sucking at night on Mondays or Thursdays my band is playing at a local bar near here."
    elif gt.curr_day == FRIDAY:
        am "Hey. If you're not busy sucking at night on Mondays or Thursdays my band is playing at a local bar near here."
    scene smcs-am003-59 mc-am-cs-walk2_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Are you inviting me to see you rock out?"
    stop sound fadeout 1.0
    scene smcs-am003-60 mc-am-cs-look_c2 with dissolve
    play voice3 girl22_yes_questioning noloop
    am "Yes. Or is that too weird?"
    scene smcs-am003-60 mc-am-cs-look_c1 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "I'm down. I can check my calendar."
    scene smcs-am003-61 mc-am-cs-talk1_c2 with dissolve
    play voice3 girl22_happy_mmm noloop
    am "Cool.{w} It's a pagan rock band so be prepared. You might see me... looking a bit crazy. And I may or may not have warpaint on my face."
    scene smcs-am003-62 mc-am-cs-talk2_c2 with dissolve
    play voice3 girl22_disappointed_oh noloop
    am "So... don't come if you're too straight-laced. Our music can be a lot for squares like you."
    scene smcs-am003-63 mc-am-cs-talk3_c1 with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "I'll make sure to wear laceless shoes."
    scene smcs-am003-63 mc-am-cs-talk3_c2 with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    am "Good plan."
    play sound3 sfx_distanttraffic_city fadein 5.0
    play sound sfx_heels_steps2 loop
    play sound2 sfx_door_open2 noloop
    scene smcs-am003-64 mc-am-cs-end1_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    if CharacterController.get_character("am").points > 2:
        mct "It's so hard to get a read on this girl. I mean it feels like there is something here."
        mct "Or was she just acting out because of the coffee and that call from Pepper."
    else:
        mct "Even money she's about to get weird again and call me a name."
    scene smcs-am003-64 mc-am-cs-end1_c2 with dissolve
    pause
    stop music fadeout 5.0
    stop music2 fadeout 5.0
    scene smcs-am003-65 mc-am-cs-walk3_c1 with dissolve
    play voice3 girl22_yes_aga4 noloop
    am "I'm going now.{w} Bye."
    mc "Later April."
    play voice2 mc_thinking_hm noloop
    mct "And I thought Nari was weird. Maybe it's because of that call from her band."
    mct "Sounds like there is some baggage attached to it."
    scene smcs-am003-65 mc-am-cs-walk3_c2 with dissolve
    mct "Maybe I should check out the show. At least then both of us know it's totally not a work thing."
    mct "Whatever this \"thing\" we're doing is..."
    stop sound3 fadeout 2.0
    stop music fadeout 3.0
    stop sound fadeout 1.0
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(AM_STORY, 3, 0, 2)
    return
label sm1cs_am003_m01_c01:
    $ player.set_choice("sm1cs_am003_favourite_pastime")
    $ CharacterController.get_character("am").add_point()
    return
label sm1cs_am003_m02_c01:
    $ player.set_choice("sm1cs_am003_for_work")
    $ CharacterController.get_character("am").deduct_point()
    return
label sm1cs_am003_m03_c01:
    $ player.set_choice("sm1cs_am003_surpass_you")
    $ CharacterController.get_character("am").add_point()
    return
label sm1cs_am003_m03_c02:
    $ CharacterController.get_character("am").deduct_point()
    return
label sm1cs_am003_unlocks:
    call sm1cs_am003_m01_c01 from _call_sm1cs_am003_m01_c01_1
    call sm1cs_am003_m02_c01 from _call_sm1cs_am003_m02_c01_1
    call sm1cs_am003_m03_c01 from _call_sm1cs_am003_m03_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(AM_STORY)
    return