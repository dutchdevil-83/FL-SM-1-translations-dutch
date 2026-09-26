label sm1cs_mes005:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound4 sfx_crowd_fightclub_ambient2 fadein 2.0 volume 0.4
    play music music_hardrock_spark
    scene sm1cs-mes005-03 mc-mes-look_c2 with dissolve
    play voice3 min_hey_simple noloop
    mes "Fancy meeting you here, [mcname]."
    scene sm1cs-mes005-04 mc-mes-look2_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Haha. Am I becoming tedious?"
    scene sm1cs-mes005-04 mc-mes-look2_c2 with dissolve
    play voice3 min_no_happy noloop
    mes "Never. Tedious is... laundry."
    mes "And working out at the gym. And studying."
    mes "But certainly not you."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes005-05 mc-mes-ask_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Right back at you."
    scene sm1cs-mes005-05 mc-mes-ask_c2 with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "So how are things? How is the studio going?"
    if player.has_played_scene("sm1ms022"):
        play sound sfx_bed_slide2
        scene sm1cs-mes005-06 mc-mes-look_c1 with dissolve
        play voice2 mc_thinking_mmm6 noloop
        mc "Really good. We actually just filmed a new scene for our client."
        scene sm1cs-mes005-06 mc-mes-look_c2 with dissolve
        play voice3 min_thinking_oh noloop
        mes "Really?"
        play sound sfx_cup_slide1 volume 1.5
        scene sm1cs-mes005-07 mc-mes-look2_c1 with dissolve
        play voice2 d9s2_yeah noloop volume 1.6
        mc "Yeah."
        scene sm1cs-mes005-07 mc-mes-look2_c2 with dissolve
        play voice3 min_happy_mmm noloop
        mes "Give me the juicy, naughty details."
        scene sm1cs-mes005-08 mc-mes-look3_c1 with dissolve
        play voice2 mc_surprised_oh1 noloop
        mc "Stacy and I did the scene, with this nice red wig.{w} And a lot of anal play."
        scene sm1cs-mes005-08 mc-mes-look3_c2 with dissolve
        play voice3 min_arrogant_huh1 noloop
        mes "I love the sound of that."
        mes "Will the client be happy?"
        scene sm1cs-mes005-09 mc-mes-ask_c1 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "We'll know after post production."
    else:
        play sound sfx_bed_slide2
        scene sm1cs-mes005-10 mc-mes-talk_c1 with dissolve
        play voice2 mc_thinking_mmm6 noloop
        if player.has_played_scene("sm1ms021i"):
            mc "Not too bad. We're gearing up for the second film from our first client."
            scene sm1cs-mes005-10 mc-mes-talk_c2 with dissolve
            play voice3 min_thinking_oh noloop
            mes "Impressive. So, a repeat customer. Very good."
            scene sm1cs-mes005-11 mc-mes-talk2_c1 with dissolve
            play voice2 d9s2_yeah noloop volume 1.6
            mc "Yup. Hopefully the first of many."
        else:
            mc "Same old same old."
            mc "I'm starting to get excited for our next piece."
            mc "Whenever we start that one."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes005-11 mc-mes-talk2_c2 with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "So when you and Stacy are acting..."
    mes "And really in the heat of things..."
    mes "Does one of you hold the camera? Or do you set it up on a tripod and just move it around a lot?"
    scene sm1cs-mes005-12 mc-mes-talk3_c1 with dissolve
    play voice2 mc_no_no1 noloop
    mc "Oh no, we found someone for that."
    scene sm1cs-mes005-12 mc-mes-talk3_c2 with dissolve
    play voice3 min_arrogant_heh2 noloop
    mes "Let me guess. You found a college student who was tired of doing unpaid internships?"
    scene sm1cs-mes005-13 mc-mes-talk4_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "No, but that is still the backup plan."
    mc "But really, we found someone. A real professional."
    mc "Her name is Kanya, she's an up-and-coming photographer, but her style is great and she's worked extremely well with us so far."
    scene sm1cs-mes005-13 mc-mes-talk4_c2 with dissolve
    play voice3 min_thinking_emm noloop
    mes "Kanya. Was she part of the Fetish Locator parties at all?"
    scene sm1cs-mes005-14 mc-mes-talk5_c1 with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "I don't think so. But she's certainly kink-positive and takes some real pride in her work."
    scene sm1cs-mes005-14 mc-mes-talk5_c2 with dissolve
    play voice3 min_happy_laugh3 noloop
    mes "Hahaha."
    scene sm1cs-mes005-15 mc-mes-talk6_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene sm1cs-mes005-15 mc-mes-talk6_c2 with dissolve
    play voice3 min_old_hmm noloop volume 1.7
    mes "Already got your pen in the company ink, [mcname]?"
    play sound sfx_cloth_rustling2
    scene sm1cs-mes005-16 mc-mes-talk7_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Ah. Heh heh."
    mc "Well Kanya and I just work {i}really{/i} well together."
    scene sm1cs-mes005-10 mc-mes-talk_c2 with dissolve
    play voice3 min_yes_aga noloop
    mes "I'll bet."
    scene sm1cs-mes005-11 mc-mes-talk2_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "You should meet her."
    scene sm1cs-mes005-11 mc-mes-talk2_c2 with dissolve
    play voice3 min_surprised_huh1 noloop
    mes "Huh?"
    scene sm1cs-mes005-12 mc-mes-talk3_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. Get to know the crew more and all that."
    mc "Maybe one day you'll want a spot on the team for yourself."
    mc "If you already knew everyone, you'd probably just slide right in."
    scene sm1cs-mes005-13 mc-mes-talk4_c2 with dissolve
    play voice3 min_happy_relief noloop
    mes "That sounds fun, but-"
    mes "It's kind of late. I don't want to bug anyone."
    scene sm1cs-mes005-13 mc-mes-talk4_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "What bugging? It's just a simple meet and greet."
    mc "I can text her to see if she's around."
    mc "Unless you prefer to just hang out here drinking for the evening."
    play sound sfx_cloth_rustling2
    scene sm1cs-mes005-16 mc-mes-talk7_c2 with dissolve
    play voice3 min_angry_argh2 noloop
    mes "Grrr."
    mes "When did you end up being the logical one?"
    scene sm1cs-mes005-17 mc-mes-talk8_c1 with dissolve
    play voice2 mc_happy_laugh3 noloop
    mc "Haha, I'm sure it's a fleeting thing. {w}So?"
    play sound sfx_hands_clap3
    scene sm1cs-mes005-17 mc-mes-talk8_c2 with dissolve
    play voice3 min_yes_yeah1 noloop
    mes "Sure. You can text her."
    play sound sfx_message_in1 volume 1.5
    scene sm1cs-mes005-18 mc-mes-talk9_c1 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "So long as she understands there is no pressure for her to meet me."
    play voice2 mc_yes_aga1 noloop
    mc "She's already replied."
    scene sm1cs-mes005-18 mc-mes-talk9_c2 with dissolve
    play voice3 min_surprised_what noloop
    mes "She's already replied?"
    play sound sfx_bed_slide3
    scene sm1cs-mes005-19 mc-mes-stand_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Hup. She's that helpful."
    scene sm1cs-mes005-19 mc-mes-stand_c2 with dissolve
    play voice3 min_yes_simple noloop
    mes "Helpful, helpful girl, I see."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes005-20 mc-mes-stand2_c1 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Come on. She says she's finishing up a session."
    mc "Pay your bill and let's go meet Kanya"
    scene sm1cs-mes005-20 mc-mes-stand2_c2 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "*unenthusiastically* Yay..."
    play sound sfx_bed_slide2
    scene sm1cs-mes005-21 mc-mes-stand3_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Come on.{w} It will be fun."
    play sound3 sfx_door_openclosed1 noloop
    $ renpy.music.set_volume(1.0, 0.5, "music2" )
    stop sound4 fadeout 2.5
    stop music fadeout 3.0
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mes005-22 mc-mes-walk_c1 with Fade(0.5, 0.5, 0.5)
    play music2 music_disco_funk_reverbed
    play voice2 mc_hey_hey5 noloop
    mc "Kanya?"
    scene sm1cs-mes005-22 mc-mes-walk_c2 with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "Maybe she went home."
    play voice2 mc_no_noway noloop
    mc "And didn't lock up? No way."
    scene sm1cs-mes005-23 mc-mes-look_c1 with dissolve
    pause
    scene sm1cs-mes005-23 mc-mes-look_c2 with dissolve
    pause
    scene sm1cs-mes005-24 mc-mes-look2_c1 with dissolve
    pause
    scene sm1cs-mes005-24 mc-mes-look2_c2 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mes005-25 mc-mes-ask_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Anything?"
    play voice3 min_no_nope noloop
    mes "Nope?"
    play sound sfx_heels_steps1 loop
    scene sm1cs-mes005-25 mc-mes-ask_c2 with dissolve
    pause
    play sound sfx_leg_kick8
    scene sm1cs-mes005-26 mc-mes-look_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Ah. Found her."
    play voice2 d6s1_pain noloop
    play sound sfx_throw_something1
    scene sm1cs-mes005-26 mc-mes-look_c2 with vpunch
    mc "Hey Kanya-oh my god!"
    play voice2 d9s5_auch2 noloop
    play sound sfx_throw_something1
    scene sm1cs-mes005-27 mc-mes-look2_c1 with hpunch
    mc "Dah!"
    play voice3 min_scared_ah1 noloop
    scene sm1cs-mes005-28 mc-mes-look3_c1 with hpunch
    mes "Woah!"
    scene sm1cs-mes005-27 mc-mes-look2_c2 with dissolve
    play voice4 kanya_horse_neighing noloop
    kv "Hahaha!"
    kv "Oh the look on your face, [mcname]."
    menu:
        "Trying to give me a heart attack?":
            scene sm1cs-mes005-27 mc-mes-look2_c1 with dissolve
            play voice2 mc_happy_oof2 noloop
            mc "Jeez. You trying to give me a heart attack?"
            play sound sfx_skirt_off2
            scene sm1cs-mes005-29 mc-mes-look4_c2 with dissolve
            play voice4 kanya_no_happy noloop
            kv "Course not."
            kv "Just keeping you on your toes."
        "Oh, I'm going to have to get you for that...":
            call sm1cs_mes004_m01_c02 from _call_sm1cs_mes004_m01_c02
            scene sm1cs-mes005-27 mc-mes-look2_c1 with dissolve
            play voice2 mc_arrogant_huh1 noloop
            mc "Fun stuff, Kanya."
            mc "But you know I'm going to have to get you back."
            play sound sfx_skirt_off2
            scene sm1cs-mes005-29 mc-mes-look4_c2 with dissolve
            play voice4 kanya_happy_laugh1 noloop
            kv "Haha.{w}Looking forward to it, [mcname]."
    play sound sfx_cloth_rustling4
    scene sm1cs-mes005-30 mc-mes-look5_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Why do you even have a zebra mask out?"
    scene sm1cs-mes005-30 mc-mes-look5_c2 with dissolve
    play voice4 kanya_no_uhuh2 noloop
    kv "Can't tell you."
    kv "Photographer-client privilege."
    scene sm1cs-mes005-31 mc-mes-grin_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh like you don't tell people about what 'we' do."
    play sound sfx_cloth_rustling2
    scene sm1cs-mes005-31 mc-mes-grin_c2 with dissolve
    play voice4 kanya_happy_laugh2 noloop
    kv "I never said that.{w} You know I like to make people blush."
    kv "Reveal and play with their hidden desires gets me all tingly..."
    scene sm1cs-mes005-32 mc-mes-talk_c2 with dissolve
    play voice4 kanya_thinking_hmm1 noloop
    kv "Speaking of clients. Who's your friend, [mcname]?"
    scene sm1cs-mes005-32 mc-mes-talk_c1 with dissolve
    play voice3 min_hey_greeting noloop
    mes "Hello.{w} I am Min Eun-Soo."
    scene sm1cs-mes005-33 mc-mes-look_c1 with dissolve
    play voice3 min_disappointed_ehh3 noloop
    mes "[mcname] is one of my best friends."
    scene sm1cs-mes005-34 mc-mes-look2_c2 with dissolve
    play voice4 kanya_happy_relief3 noloop
    kv "Great."
    kv "Any friend of [mcname]'s is a friend of mine."
    kv "Kanya Vu. A pleasure."
    play sound sfx_hands_clap1
    scene sm1cs-mes005-35 mc-mes-look3_c1 with dissolve
    pause
    scene sm1cs-mes005-35 mc-mes-look3_c2 with dissolve
    play voice4 kanya_thinking_eeh5 noloop
    kv "So.. uh... you know about..."
    kv "The stuff?"
    scene sm1cs-mes005-35 mc-mes-look3_c3 with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.7
    mc "Haha.{w} Yes, she knows about the studio."
    mc "I wanted to bring Min around and show her what you do here so she could meet the number one camera girl in the city."
    scene sm1cs-mes005-36 mc-mes-waving_c2 with dissolve
    play voice4 kanya_happy_relief2 noloop
    kv "Oh phew."
    kv "I was trying to figure out what my kink filter should be set to."
    scene sm1cs-mes005-36 mc-mes-waving_c1 with dissolve
    play voice3 min_old_laugh noloop
    mes "*giggles* You can wave your flag freely, Kanya. No need to censor yourself on my account."
    scene sm1cs-mes005-36 mc-mes-waving_c2 with dissolve
    play voice4 kanya_yes_yep2 noloop
    kv "Thanks Min. And by the way, I'm probably the best camera girl in [mcname]'s mind because I'm the only one he knows."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes005-37 mc-mes-talk_c1 with dissolve
    play voice3 min_happy_laugh2 noloop
    mes "Haha."
    scene sm1cs-mes005-37 mc-mes-talk_c3 with dissolve
    play voice2 mc_hey_hey8 noloop
    mc "Hey. There was no need to look elsewhere after I met you, Kanya."
    scene sm1cs-mes005-37 mc-mes-talk_c2 with dissolve
    play voice4 kanya_arrogant_hm noloop
    kv "Mmm. Always the charmer."
    scene sm1cs-mes005-38 mc-mes-talk2_c2 with dissolve
    play voice4 kanya_arrogant_huh noloop
    kv "So, Min, you thinking of joining the crew?"
    kv "We're going to need all the sexy people we can get to make a porn studio to stand the test of time."
    scene sm1cs-mes005-39 mc-mes-talk3_c1 with dissolve
    play voice3 min_disappointed_off noloop
    mes "Oh... I don't think that's an option, unfortunately."
    scene sm1cs-mes005-39 mc-mes-talk3_c2 with dissolve
    play voice4 kanya_surprised_what noloop
    kv "What? That sucks."
    scene sm1cs-mes005-40 mc-mes-talk4_c1 with dissolve
    play voice3 min_yes_yeah2 noloop
    mes "Yeah. I think... if things were different, it's something I'd enjoy trying."
    mes "But there is no way I could work at a porn studio."
    mes "It would just kill my parents."
    scene sm1cs-mes005-40 mc-mes-talk4_c2 with dissolve
    play voice4 kanya_yes_aga3 noloop
    kv "I get that. But it's not like hiding [mcname]'s sausage is not the only job there is."
    kv "I mean, I've done that, but ninety percent of the time, I'm doing the camera work or other behind-the-scenes stuff."
    scene sm1cs-mes005-41 mc-mes-look_c1 with dissolve
    play voice3 min_thinking_mhh noloop
    mes "That's a good point."
    mes "Show me around?"
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mes005-42 mc-mes-walk_c1 with dissolve
    play voice3 kanya_yes_yeah2 noloop
    kv "Sure."
    kv "Got the lounge. Nice spot for everyone to relax or pre-game."
    kv "The owner wanted to make sure people can get mentally and physically ready for the show before stepping into the light."
    scene sm1cs-mes005-43 mc-mes-walk2_c1 with dissolve
    play voice3 min_surprised_wow noloop
    mes "Impressive. I imagine this kind of setup is pretty top of the line."
    play voice4 kanya_yes_yeah3 noloop
    kv "Oh yeah. The owner spared no expense, and it paid off."
    scene sm1cs-mes005-44 mc-mes-talk_c2 with dissolve
    play voice4 kanya_happy_laugh3 noloop
    kv "People love coming here."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mes005-45 mc-mes-talk2_c2 with dissolve
    kv "And of course, this is where the magic happens."
    play voice3 min_happy_yeah noloop
    mes "Very nice."
    mes "So have you done any scenes here?"
    scene sm1cs-mes005-45 mc-mes-talk2_c1 with dissolve
    play voice2 mc_no_no10 noloop
    mc "Not yet, but you never know what the future might hold."
    play sound sfx_cloth_rustling5
    scene sm1cs-mes005-46 mc-mes-talk3_c1 with dissolve
    play voice4 kanya_thinking_hmm3 noloop
    kv "We've already done a lot of work together at the dojo."
    kv "As you can see."
    play sound sfx_remote_button1 volume 2.0
    scene sm1cs-mes005-48 mc-mes-look_c2 with dissolve
    play voice3 min_pain_ah noloop
    mes "Oh wow."
    play sound sfx_remote_button1 volume 2.0
    scene sm1cs-mes005-48 mc-mes-look_c3 with dissolve
    pause
    play sound sfx_remote_button1 volume 2.0
    scene sm1cs-mes005-48-2 mc-mes-look_c3 with dissolve
    pause
    scene sm1cs-mes005-49 mc-mes-look2_c2 with dissolve
    play voice3 min_disappointed_mph noloop
    mes "You really are a {b}naughty{/b} boy, aren't you."
    scene sm1cs-mes005-49 mc-mes-look2_c3 with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "I think it's something to do with the lights around here."
    mc "Makes me all horny."
    play voice4 kanya_happy_laugh5 noloop
    play voice3 min_happy_laugh2 noloop
    scene sm1cs-mes005-50 mc-mes-talk_c2 with dissolve
    "Min and Kanya" "*laughing*"
    mes "You would have sex on the moon if you could."
    play sound sfx_cloth_rustling1
    scene sm1cs-mes005-50 mc-mes-talk_c3 with dissolve
    play voice2 mc_surprised_huh7 noloop
    pause
    scene sm1cs-mes005-51 mc-mes-look_c2 with dissolve
    play voice3 min_arrogant_heh1 noloop
    mes "Well it's certainly not the photo shack I was worried it would be."
    mes "Looks like you two really know what you're doing."
    scene sm1cs-mes005-52 mc-mes-look2_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yup."
    play sound sfx_cloth_rustling2
    scene sm1cs-mes005-53 mc-mes-talk_c1 with dissolve
    play voice4 kanya_arrogant_ha noloop
    kv "I wouldn't be allowed in here if I didn't have the chops, Min."
    kv "In fact... I think I know how to set all fears aside."
    kv "Why don't I take some snaps of you. On the house."
    scene sm1cs-mes005-53 mc-mes-talk_c2 with dissolve
    play voice3 min_disgust_off noloop
    mes "Oh, you don't have to do that, Kanya. I don't want to waste your time."
    scene sm1cs-mes005-54 mc-mes-talk2_c1 with dissolve
    play voice3 kanya_no_nonono1 noloop
    kv "It's never a waste of time getting to photograph a beautiful woman."
    kv "And the only way I can keep my skills sharp is using what I know to capture the essence of new subjects."
    kv "If you'll allow me."
    scene sm1cs-mes005-54 mc-mes-talk2_c2 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "Uh..."
    mes "Sure. Why not?{w} It will be good for a laugh."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mes005-55 mc-mes-walk_c1 with dissolve
    play voice4 kanya_yes_aga2 noloop
    kv "Follow me. We'll find something nice for you."
    scene sm1cs-mes005-55 mc-mes-walk_c2 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "Lead the way."
    stop sound fadeout 2.5
    stop sound2 fadeout 3.0
    scene sm1cs-mes005-55 mc-mes-walk_c3 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mct "Heh. Seems like the old Min is back. She was always taking on whatever challenges came in front of her."
    mct "I'm glad she's getting along so well with Kanya."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes005-56 mc-mes-walk2_c3 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mct "That means they'd work well together if Min ever changes her mind about joining the team."
    mct "But even if that doesn't happen, it's all good.{w} I don't want to push Min into something she's not prepared for."
    play sound sfx_heels_steps1
    scene sm1cs-mes005-57 mc-mes-look_c1 with fade
    stop sound fadeout 2.5
    play voice3 min_happy_woohoo noloop
    mes "So...{w} How do I look?"
    play voice2 mc_surprised_wow4 noloop
    mc "Oh wow."
    mc "You look great, Min."
    play voice3 min_happy_laugh3 noloop
    mes "Haha. You have to say that, [mcname]."
    scene sm1cs-mes005-57 mc-mes-look_c3 with dissolve
    play voice2 mc_no_no2 noloop
    mc "No really. I wish we were going to a Fetish Locator party after this."
    play voice3 min_yes_ugu noloop
    mes "Well, then you'll enjoy this ."
    stop music2 fadeout 1.5
    play sound sfx_phone_button1 volume 2.5
    scene sm1cs-mes005-58 mc-mes-look2_c2 with dissolve
    play music music_sexy_workout
    pause
    scene sm1cs-mes005-59 mc-mes-camera_c1 with dissolve
    play voice4 kanya_yes_yeah1 noloop
    kv "Already, let's keep things nice and loose."
    scene sm1cs-mes005-60 mc-mes-photo_c1 with dissolve
    play voice4 kanya_yes_yep3 noloop
    kv "That's a good start."
    scene sm1cs-mes005-60 mc-mes-photo_c2 with dissolve
    play voice4 kanya_thinking_hmm4 noloop
    kv "But try to drop your guard a little. Let the inner animal out."
    scene sm1cs-mes005-60 mc-mes-photo_c3 with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "That's uh..."
    mes "I'll do my best."
    scene sm1cs-mes005-61 mc-mes-photo2_c1 with dissolve
    menu:
        "Support Min":
            call sm1cs_mes005_m02_c01 from _call_sm1cs_mes005_m02_c01
            scene sm1cs-mes005-64 mc-mes-cheering_c2 with dissolve
            play voice2 mc_happy_wooh3 noloop
            mc "Come on, Min. You got this."
            scene sm1cs-mes005-61 mc-mes-photo2_c3 with dissolve
            play voice3 min_arrogant_heh1 noloop
            pause
            scene sm1cs-mes005-64 mc-mes-cheering_c1 with dissolve
            play voice2 mc_thinking_hmm9 noloop
            mc "Shake that cute bootie."
            mc "It's just us. No one is judging you."
        "Say nothing":
            pass
    play sound sfx_cloth_rustling4
    scene sm1cs-mes005-65 mc-mes-photo_c1 with fade
    pause
    play sound2 sfx_photocamera_flash2 noloop
    scene sm1cs-mes005-65 mc-mes-photo_c3 with dissolve
    pause
    play sound sfx_cloth_rustling3
    scene sm1cs-mes005-66 mc-mes-photo2_c1 with fade
    pause
    play sound2 sfx_photocamera_flash2 noloop
    scene sm1cs-mes005-66 mc-mes-photo2_c2 with dissolve
    pause
    play sound sfx_cloth_rustling5
    scene sm1cs-mes005-67 mc-mes-photo3_c1 with fade
    pause
    play sound2 sfx_photocamera_flash2 noloop
    scene sm1cs-mes005-67 mc-mes-photo3_c2 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1cs-mes005-68 mc-mes-photo4_c1 with fade
    pause
    play sound2 sfx_photocamera_flash2 noloop
    scene sm1cs-mes005-68 mc-mes-photo4_c2 with dissolve
    pause
    if player.get_topic(TOPIC_PHOTOGRAPHY) > 6:
        scene sm1cs-mes005-69 mc-mes-suggestion_c2 with dissolve
        play voice2 mc_hey_hey6 noloop
        mc "Hey, Kanya, what if you stopped down a bit? To, maybe, a 5.6 f-stop? I feel like more of her body should be in focus."
        play sound sfx_photocamera_zoom1
        play voice4 kanya_disappointed_ohh noloop
        kv "Good thinking, [mcname]."
        scene sm1cs-mes005-69 mc-mes-suggestion_c1 with dissolve
        play voice4 kanya_surprised_oh noloop
        kv "Oh fuck yeah, [mcname]. Good tip."
        kv "That really did the trick."
        play sound sfx_photocamera_flash2
        "CLICK"
        play voice2 mc_arrogant_hm1 noloop
        mct "Nice."
        play sound sfx_photocamera_flash2
        "CLICK"
    play sound sfx_cloth_rustling1
    scene sm1cs-mes005-70 mc-mes-sit_c1 with fade
    pause
    play sound2 sfx_photocamera_flash2 noloop
    scene sm1cs-mes005-70 mc-mes-sit_c2 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1cs-mes005-71 mc-mes-stand_c1 with fade
    pause
    play sound2 sfx_photocamera_flash2 noloop
    scene sm1cs-mes005-71 mc-mes-stand_c2 with dissolve
    pause
    scene sm1cs-mes005-72 mc-mes-stand2_c2 with dissolve
    play voice4 kanya_arrogant_laugh noloop
    kv "And that's all she wrote."
    kv "Excellent work, Min."
    play sound sfx_hair_scratch1
    scene sm1cs-mes005-72 mc-mes-stand2_c1 with dissolve
    play voice3 min_surprised_huh2 noloop
    mes "Really?"
    play voice4 kanya_yes_long noloop
    kv "Absolutely. You're a natural."
    mes "You're too kind. I think in my case, half the success was audience participation."
    mes "Either way, it was a blast."
    scene sm1cs-mes005-73 mc-mes-look_c2 with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "I'm going to go get changed."
    scene sm1cs-mes005-73 mc-mes-look_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yup. Changed. Good idea."
    $ renpy.music.set_volume(0.6, 6.0, "music" )
    play sound sfx_barefoot_steps1
    scene sm1cs-mes005-75 mc-mes-sit_c1 with dissolve
    pause
    play sound sfx_remote_button1 volume 2.0
    scene sm1cs-mes005-75 mc-mes-sit_c2 with dissolve
    play voice4 girl31_thinking_mmm3 noloop volume 0.75
    kv "*humming*"
    scene sm1cs-mes005-76 mc-mes-sit2_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "What's up?"
    play voice4 kanya_disappointed_eeh noloop
    kv "Oh nothing. Just wondering when you two are going to bang like animals on my floor."
    play sound sfx_cloth_rustling2
    scene sm1cs-mes005-77 mc-mes-talk_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Haha. We're not that wild and uncontrollable."
    scene sm1cs-mes005-77 mc-mes-talk_c2 with dissolve
    play voice4 kanya_arrogant_pff noloop
    kv "Pssh. I think you two have it bad for each other."
    scene sm1cs-mes005-78 mc-mes-look_c1 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "I mean, it's not like we haven't done stuff."
    mc "But you think it's deeper?"
    scene sm1cs-mes005-79 mc-mes-ask_c2 with dissolve
    play voice4 kanya_thinking_eeh1 noloop
    kv "To quote 'half the success was audience participation'."
    kv "I think she got to really step into her confident spot when she knew you were there, watching her."
    kv "Enjoying her..."
    play sound sfx_cloth_rustling3 volume 2.0
    scene sm1cs-mes005-80 mc-mes-stand_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "I appreciate your advice, Dr. Kanya."
    scene sm1cs-mes005-80 mc-mes-stand_c2 with dissolve
    play voice4 kanya_happy_laugh4 noloop
    kv "*giggles* Anytime."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mes005-80 mc-mes-stand_c3 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-mes005-81 mc-mes-talk_c3 with dissolve
    play voice3 min_yes_aga noloop
    mes "Alright."
    mes "I hope there were some salvageable pictures in the lot, Kanya."
    scene sm1cs-mes005-81 mc-mes-talk_c2 with dissolve
    play voice4 kanya_disappointed_oh noloop
    kv "Oh, you don't have to worry about that, Min. By the time I'm done with them, they'll be exquisite."
    play voice3 min_old_laugh noloop
    mes "*laughs* Thank you."
    scene sm1cs-mes005-82 mc-mes-talk2_c2 with dissolve
    play voice4 kanya_yes_yep1 noloop
    kv "I'll send them along to [mcname] once they're all ready. Or I'm sure I can share them with you if we all end up at the studio one day."
    scene sm1cs-mes005-81 mc-mes-talk_c3 with dissolve
    play voice3 min_yes_happy noloop
    mes "Sure. Stranger things have happened."
    mes "Thanks again for the photoshoot."
    play voice4 kanya_arrogant_yeah noloop
    kv "My pleasure."
    scene sm1cs-mes005-82 mc-mes-talk2_c3 with dissolve
    play voice3 min_thinking_emm noloop
    mes "I should get going back home."
    scene sm1cs-mes005-82 mc-mes-talk2_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I'll walk you back."
    play voice3 min_no_nah noloop
    mes "It's okay, I can handle it."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mes005-83 mc-mes-walk_c2 with dissolve
    play voice3 min_happy_laugh3 noloop
    mes "This was a lot of fun. I've never been photographed like that before, [mcname]."
    scene sm1cs-mes005-84 mc-mes-ask_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Kanya's alright, right?"
    scene sm1cs-mes005-84 mc-mes-ask_c2 with dissolve
    play voice3 min_yes_simple noloop
    mes "Oh yes. I can see why you wanted to hire her."
    mes "She makes it seem so easy."
    mes "It makes it...{w} seductive."
    mes "Like stepping into a warm pool."
    mes "She'll be an asset to your team."
    scene sm1cs-mes005-85 mc-mes-walk_c1 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "She and other people I know..."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mes005-85 mc-mes-walk_c2 with dissolve
    pause
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-mes005-87 mc-mes-kiss_c1 with dissolve
    play voice3 min_old_mff noloop
    play voice2 mc_thinking_mmm1 noloop
    play sound dahlia_kiss_french1
    mes "Mmm."
    scene sm1cs-mes005-87 mc-mes-kiss_c2 with dissolve
    queue sound mc_kiss2
    pause
    scene sm1cs-mes005-88 mc-mes-close_c2 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "I am sure you have more than enough assets for what you need."
    mes "Good night, [mcname]."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mes005-89 mc-mes-walk_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Damn. Sounds like she's pretty set on not joining the studio."
    mct "But that's alright. It doesn't change things between us."
    play sound sfx_door_open1
    scene sm1cs-mes005-90 mc-mes-door_c2 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "That's the most important thing."
    jump sm1cs_mes005_end_scene
label sm1cs_mes005_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(MES_STORY, 4, 0, 2, STUDIO, DEFAULT_SUBLOCATION, SD_COUCH)
    return
label sm1cs_mes004_m01_c02:
    $ player.set_choice("sm1cs_mes004_get_kv_back")
    return
label sm1cs_mes005_m02_c01:
    $ player.set_choice("sm1cs_mes005_support_min")
    $ CharacterController.get_character("mes").add_point()
    return