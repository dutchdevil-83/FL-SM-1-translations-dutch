image sm1cs-ag002-glambot-1 = Movie(play = "images/FS_IT/AG/s002/anim/sm1cs-ag002-a98-2x-60fps.webm", start_image = "sm1cs-ag002-a98 ag-mc-dance-glambot-00", image = "sm1cs-ag002-a98 ag-mc-dance-glambot-80", loop = False)
label sm1cs_ag002:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound4 sfx_cafe_crowd fadein 3.0
    play music music_miami_reggae3_radio fadein 1.5
    play sound sfx_double_door1
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene sm1cs-ag002-07 ag-mc-walking-in with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "Huh... not the kind of bar I was expecting Anna to be into..."
    scene sm1cs-ag002-08 ag-telling-him with dissolve
    play voice3 girl27_hey_serious noloop
    ag "I know what you're thinking, but this place is close to the office and everyone kind of sticks to themselves."
    ag "Plus the drinks are cheap."
    scene sm1cs-ag002-09 mc-agreeing with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I like cheap drinks!"
    scene sm1cs-ag002-10 ag-smiling with dissolve
    play voice3 girl27_arrogant_right2 noloop
    ag "I thought you might."
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-ag002-11 ag-summoning-barmaid with dissolve
    play voice3 girl27_hey_active noloop
    ag "Hey, bartender?"
    scene sm1cs-ag002-12 ag-telling-her with dissolve
    play voice3 girl27_thinking_emm5 noloop
    ag "Can I get a mojito, and for my friend..."
    scene sm1cs-ag002-13 mc-talking with dissolve
    menu:
        "Old Fashioned"(hint="sm1cs_ag002_m01_h01"):
            call sm1cs_ag002_m01_c01 from _call_sm1cs_ag002_m01_c01
            play voice2 mc_thinking_hmm2 noloop
            mc "How about an Old Fashioned for me?"
        "Manhattan"(hint="sm1cs_ag002_m01_h02"):
            call sm1cs_ag002_m01_c02 from _call_sm1cs_ag002_m01_c02
            play voice2 mc_thinking_hmm2 noloop
            mc "I'll have a Manhattan."
        "Mojito"(hint="sm1cs_ag002_m01_h03"):
            call sm1cs_ag002_m01_c03 from _call_sm1cs_ag002_m01_c03
            play voice2 mc_thinking_hmm2 noloop
            mc "You know what, a mojito sounds great."
    play sound sfx_glass_bottles_shuffle1
    scene sm1cs-ag002-14 br-noding with dissolve
    stop sound fadeout 1.5
    play voice4 girl26_yes_ugu noloop
    pause
    scene sm1cs-ag002-15 mc-asking with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "So... is happy hour a thing people at the office do often, or..."
    scene sm1cs-ag002-16 ag-answering with dissolve
    play voice3 girl27_no_nah1 noloop
    ag "Not really. Well, we used to. Claire is a big fan of new or hip food and drink spots. So she used to do them all the time."
    ag "But since things have gotten busy at Orbix, she's not really been doing it much."
    scene sm1cs-ag002-17 ag-disappointed with dissolve
    play voice3 girl27_disappointed_ehh1 noloop
    ag "And April really isn't much for socializing."
    scene sm1cs-ag002-18 ag-talking with dissolve
    play voice3 girl27_thinking_mmm noloop
    ag "But I like to go sometimes. It's one of the ways I unwind after work."
    scene sm1cs-ag002-19 mc-talking with dissolve
    play voice2 d9s2_yeah noloop volume 1.8
    mc "And unwinding is important!"
    scene sm1cs-ag002-20 ag-smiling with dissolve
    play voice3 girl27_yes_happy2 noloop
    ag "Yes! You get it!"
    play sound sfx_heels_steps2 loop
    scene sm1cs-ag002-21 br-coming-with-drinks with dissolve
    pause
    play sound sfx_plate_place1
    play sound2 sfx_cup_slide1 noloop
    scene sm1cs-ag002-22 br-serving-them with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1cs-ag002-23 ag-holding-her-drink with dissolve
    pause
    if not player.get_choice("sm1cs_ag002_mojito"):
        scene sm1cs-ag002-24 ag-confused with dissolve
        play voice3 girl27_arrogant_huh3 noloop
        ag "Wait... my friend didn't order a mojito."
        scene sm1cs-ag002-25 br-oops with dissolve
        play voice4 girl26_disappointed_eeh noloop
        "Bartender" "Really? Shit..."
        scene sm1cs-ag002-26 mc-itz-ok with dissolve
        play voice2 mc_no_nah1 noloop
        mc "It's fine, don't worry about it."
        scene sm1cs-ag002-27 br-sowwy with dissolve
        play voice4 girl26_disappointed_mmh1 noloop
        "Bartender" "Sorry about that..."
    play sound sfx_cloth_rustling1
    scene sm1cs-ag002-28 mc-picking-his-drink with dissolve
    pause
    scene sm1cs-ag002-29 ag-asking with dissolve
    play voice3 girl27_yes_ya noloop
    ag "So, tell me something about yourself, [mcname]!"
    scene sm1cs-ag002-30 mc-eh with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "Erm... like what?"
    scene sm1cs-ag002-31 ag-being-clear with dissolve
    play voice3 girl27_happy_hmm1 noloop
    ag "I don't know, like, what do you do with your free time?"
    scene sm1cs-ag002-32 mc-thinking with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Shit... do I do anything other than trying to run a porn studio with my free time?"
    scene sm1cs-ag002-33 mc-telling-her with dissolve
    play voice2 d2s12_emmm noloop volume 1.6
    mc "Erm... I guess you could say I'm a bit obsessed with my work right now."
    scene sm1cs-ag002-34 ag-talking with dissolve
    play voice3 girl27_yes_aga2 noloop
    ag "I know the feeling."
    scene sm1cs-ag002-35 mc-asking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh? You been working long days at the office?"
    scene sm1cs-ag002-36 ag-embarrased with dissolve
    play voice3 girl27_yes_yeah4 noloop
    ag "Something like that..."
    scene sm1cs-ag002-37 mc-thinking with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mct "Huh... does she look... embarrassed? Why would she be embarrassed about coding?"
    scene sm1cs-ag002-38 mc-asking with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Well what about you? What do you like to do to unwind?"
    scene sm1cs-ag002-39 ag-answering with dissolve
    play voice3 girl27_disappointed_ah1 noloop
    ag "This! And sometimes playing video games."
    scene sm1cs-ag002-40 mc-surprised with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Really? I didn't take you as the gaming type."
    scene sm1cs-ag002-41 ag-talking with dissolve
    play voice3 girl27_yes_yeah noloop
    ag "Oh yeah. I, uhm... I kind of love gaming, actually."
    scene sm1cs-ag002-43 mc-asking with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "What's your game?"
    play sound sfx_straw_drink5
    scene sm1cs-ag002-42 mc-thinking with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mct "I bet it's something like Animal Junction, or-"
    scene sm1cs-ag002-44 ag-serious with dissolve
    play voice3 girl27_arrogant_hah noloop
    ag "First person shooters. Hardcore, team death matches."
    ag "I've been in a milsim mood lately, definitely have done arcade shooters a few different times, but I always come back to milsims."
    stop sound fadeout 1.0
    scene sm1cs-ag002-45 mc-surprised with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Oh, wow..."
    scene sm1cs-ag002-46 ag-still-serious with dissolve
    play voice3 girl27_surprised_what6 noloop
    ag "Wow, what?"
    scene sm1cs-ag002-47 mc-explaining with dissolve
    play voice2 d1s5b_emmm noloop volume 1.5
    mc "I just... wasn't expecting you to be that into first person shooters."
    scene sm1cs-ag002-48 mc-ag-talking with dissolve
    play voice3 girl27_arrogant_huh1 noloop
    ag "Is this the part where you tell me girls can't game?"
    play voice2 mc_no_no2 noloop
    mc "No-"
    scene sm1cs-ag002-49 ag-serious with dissolve
    play voice3 girl27_angry_mmm noloop
    ag "Because you can come over anytime and I'll kick your digital ass."
    scene sm1cs-ag002-50 mc-thinking with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Did Anna just invite me over?"
    play sound sfx_straw_drink1
    scene sm1cs-ag002-51 ag-drinking with dissolve
    pause
    scene sm1cs-ag002-52 mc-talking with dissolve
    play voice2 mc_happy_a1 noloop volume 1.6
    mc "I'll have to take you up on that. I think it would be fun to play some video games... it's been a long time since I've been able to just game."
    stop sound fadeout 1.0
    scene sm1cs-ag002-53 ag-smiling with dissolve
    play voice3 girl27_arrogant_ha noloop
    ag "I should warn you, I can be pretty competitive."
    scene sm1cs-ag002-54 mc-accepting with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I think I'm up for the challenge!"
    scene sm1cs-ag002-55 ag-whispering with dissolve
    play voice3 girl27_disappointed_mff noloop
    ag "{size=*0.6}Oh, I doubt that...{/size}"
    scene sm1cs-ag002-56 mc-confused with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "What was that?"
    scene sm1cs-ag002-57 ag-blushing with dissolve
    play voice3 girl27_disappointed_oh3 noloop
    ag "Oh... nothing."
    play sound sfx_straw_drink6
    scene sm1cs-ag002-58 ag-drinking with dissolve
    pause
    scene sm1cs-ag002-59 mc-asking with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "So, competitive... is that why you and April have your beef?"
    stop sound fadeout 1.0
    scene sm1cs-ag002-60 ag-agreeing with dissolve
    play voice3 girl27_disappointed_ehh2 noloop
    ag "Erm... kind of."
    scene sm1cs-ag002-61 mc-curious with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Is that how you got the nickname?"
    scene sm1cs-ag002-62 ag-pretending with dissolve
    play voice3 girl27_angry_cough2 noloop
    ag "I, uhm, don't know what you're talking about."
    scene sm1cs-ag002-63 mc-hinting with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "You know, \"Aubergine Annie\"?"
    play sound sfx_straw_drink4
    scene sm1cs-ag002-64 ag-embarassed with dissolve
    play voice3 girl27_thinking_hmm7 noloop
    ag "Nope. Erm... definitely nope."
    scene sm1cs-ag002-65 mc-thinking with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mct "I don't think she wants to talk about it."
    scene sm1cs-ag002-66 mc-talking with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.7
    mc "We don't have to talk about it if you don't want."
    scene sm1cs-ag002-67 ag-talking with dissolve
    play voice3 girl27_surprised_oh3 noloop
    ag "Oh - it's totally, like totally cool. It's just because I like to, uhm, eat veggies. You know?"
    ag "Like salads, and, uhm... other veggies."
    ag "But, uh, what did you do before coming to Orbix, [mcname]?"
    scene sm1cs-ag002-68 mc-uncomfortable with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I was actually in college."
    scene sm1cs-ag002-69 ag-curious with dissolve
    play voice3 girl27_surprised_oh2 noloop
    ag "Oh right. What was your major again?"
    scene sm1cs-ag002-70 mc-word with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Business."
    scene sm1cs-ag002-71 ag-surprised with dissolve
    play voice3 girl27_arrogant_huh4 noloop
    ag "Huh, from business to coding... not the craziest leap, but definitely a little unexpected."
    ag "Did you get your Associate's or your Bachelor's?"
    scene sm1cs-ag002-72 mc-uncomfortable with dissolve
    play voice2 d3s7_mcemm noloop
    mc "Actually... I kind of dropped out."
    scene sm1cs-ag002-73 ag-uncomfy with dissolve
    play voice3 girl27_surprised_eh noloop
    ag "Oh! Shit. That's..."
    ag "That's in your file too. Totally forgot. Sorry, [mcname]."
    scene sm1cs-ag002-74 mc-itz-ok with dissolve
    play voice2 mc_no_no6 noloop
    mc "No, it's okay. You've got a lot on your plate."
    scene sm1cs-ag002-75 ag-asking with dissolve
    play voice3 girl27_surprised_eh2 noloop
    ag "Erm... well, where were you going to college?"
    scene sm1cs-ag002-76 mc-close-up with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Here, in Crowning."
    scene sm1cs-ag002-77 ag-shocked with dissolve
    play voice3 girl27_surprised_ohmy2 noloop
    ag "Oh my - were you going to school there while..."
    play sound sfx_cloth_rustling2
    scene sm1cs-ag002-78 ag-leaning-in with dissolve
    play voice3 girl27_thinking_emm4 noloop
    ag "{size=*0.6}While Fetish Locator was a thing?{/size}"
    scene sm1cs-ag002-79 mc-agreeing with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Uhm... yep, I was."
    scene sm1cs-ag002-80 ag-excited with dissolve
    play voice3 girl27_happy_relief3 noloop
    ag "That must have been so exciting! A whole scandal happening all around you-!"
    ag "A scandal happening at your school... and then you dropped out."
    scene sm1cs-ag002-81 mc-uncomfy with dissolve
    play voice2 mc_angry_huh1 noloop
    mct "Uh oh... did she-?"
    play sound sfx_cloth_rustling4
    scene sm1cs-ag002-83 ag-comforting with dissolve
    play voice3 girl27_disappointed_eh1 noloop
    ag "I'm sorry, I guess that probably had something to do with you dropping out?"
    scene sm1cs-ag002-84 mc-looking-down with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah... just a bit."
    scene sm1cs-ag002-85 ag-feels-bad-man with dissolve
    play voice3 girl27_disappointed_mmm noloop
    ag "I can't imagine. That would probably be a lot to deal with, especially while you're trying to go to class, study... and the whole time, people were out there sexing it up all over the place!"
    scene sm1cs-ag002-86 mc-thinking with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Did she just say \"sexing\"?"
    play voice3 girl27_thinking_emm3 noloop
    ag "I bet you probably don't want to talk about it."
    scene sm1cs-ag002-87 mc-looking-up with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah... it's come up a few times since I stopped going to school. And it's a... tough subject every time."
    play sound sfx_drink_slurp1 volume 0.6
    scene sm1cs-ag002-88 ag-finishing-her-drink with dissolve
    pause
    play sound sfx_plate_place1
    play sound2 sfx_cup_place1 noloop
    scene sm1cs-ag002-89 ag-slamming-it with dissolve
    pause
    scene sm1cs-ag002-90 ag-smiling with dissolve
    play voice3 girl27_happy_relief2 noloop
    ag "Well one awkward moment should be traded for another! {w}Let's dance!"
    scene sm1cs-ag002-91 mc-talking with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "Wait - what? I don't think this is a dancing bar."
    scene sm1cs-ag002-92 ag-talking with dissolve
    play voice3 girl27_disappointed_ah2 noloop
    ag "Eh - they've got enough space for it over there! Come on!"
    stop music fadeout 4.0
    play sound sfx_cloth_rustling5
    play sound2 sfx_heels_steps1
    scene sm1cs-ag002-93 ag-holding-his-hand with dissolve
    pause
    scene sm1cs-ag002-94 ag-mc-going-towards-the-dance-floor with dissolve
    $ renpy.music.set_volume(1.0, 0.0, "music2" )
    $ renpy.music.set_volume(0.5, 0.0, "music3" )
    $ renpy.music.play(audio.music_rock_n_drive, "music2" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_rock_n_drive_radio, "music3", True, None, True, 0.0)
    pause
    stop sound2 fadeout 1.0
    play sound sfx_socks_dancing2 loop volume 0.2
    scene sm1cs-ag002-95 ag-mc-dancing-montage with dissolve
    pause
    scene sm1cs-ag002-96 ag-mc-dancing-montage with dissolve
    pause
    scene sm1cs-ag002-97 ag-mc-dancing-montage with dissolve
    pause
    scene sm1cs-ag002-a98 ag-mc-dance-glambot-00 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    scene sm1cs-ag002-glambot-1
    pause
    scene sm1cs-ag002-99 ag-mc-dancing-montage with dissolve
    pause
    $ renpy.music.set_volume(0.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "music3" )
    stop sound fadeout 1.0
    scene sm1cs-ag002-100 ag-mc-standing-down with fade
    play voice3 girl27_surprised_wow1 noloop
    ag "Wow, that was fun!"
    play sound sfx_phone_buzz
    scene sm1cs-ag002-101 ag-looking-at-her-phone with dissolve
    play voice3 girl27_scared_oh1 noloop
    ag "Oh no! [mcname], I am so sorry but I have to take off?"
    scene sm1cs-ag002-102 mc-asking with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Oh, is everything okay?"
    scene sm1cs-ag002-103 ag-informing with dissolve
    play voice3 girl27_yes_yeah3 noloop
    ag "Yeah, everything is totally fine! I just promised to participate in this game tournament and it starts soon!"
    play sound sfx_cloth_rustling2
    scene sm1cs-ag002-104 ag-happy with dissolve
    play voice3 girl27_happy_laugh4 noloop
    ag "But I had a lot of fun tonight."
    scene sm1cs-ag002-105 mc-half-happy with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "You know what... I kind of did too."
    scene sm1cs-ag002-106 ag-sorry with dissolve
    play voice3 girl27_thinking_emm noloop
    ag "Sorry about bringing up... well, apparently all of your awkward shit."
    scene sm1cs-ag002-107 mc-thinking with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Oh, it definitely wasn't all of it..."
    scene sm1cs-ag002-108 ag-letz-hug with dissolve
    play voice3 girl27_happy_relief1 noloop
    ag "Goodbye hug?"
    scene sm1cs-ag002-109 mc-sure with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Absolutely."
    play sound sfx_cloth_rustling4
    scene sm1cs-ag002-110 mc-ag-hugging with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1cs-ag002-111 mc-ag-hugging with dissolve
    pause
    scene sm1cs-ag002-112 mc-ag-hugging with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "Wow... Anna is really holding onto this hug..."
    scene sm1cs-ag002-113 mc-thinking with dissolve
    mct "It seems like she doesn't want to let go..."
    mct "Hmm... it's probably nothing. Just the mojito she drank."
    play sound sfx_skirt_off2
    scene sm1cs-ag002-114 ag-smiling with dissolve
    play voice3 girl27_hey_interested noloop
    ag "And I was serious about you coming over to game with me sometime. That would be a ton of fun."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_cloth_rustling1 noloop
    scene sm1cs-ag002-115 ag-bye with dissolve
    play voice3 girl27_hey_bye6 noloop
    ag "Ciao, [mcname]!"
    scene sm1cs-ag002-116 mc-bye with dissolve
    play voice2 mc_hey_bye1 noloop
    mc "See you, Anna!"
    scene sm1cs-ag002-117 ag-going with dissolve
    pause
    play sound sfx_door_closed6 volume 0.4
    scene sm1cs-ag002-118 mc-thinking with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "Hopefully it won't be too long before we can make that video game hang out happen."
    play sound sfx_heels_steps2 loop
    scene sm1cs-ag002-119 mc-leaving with dissolve
    pause
    stop sound fadeout 2.0
    stop sound4 fadeout 2.0
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "music3" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    call sm1_unlock_gr_bar from _call_sm1_unlock_gr_bar
    jump sm1cs_ag002_exit_to_map
label sm1cs_ag002_exit_to_map:
    $ StoryController.end_scene_in_time(AG_STORY, 22, 15, 4, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1cs_ag002_m01_c01:
    $ player.set_choice("sm1cs_ag002_old_fashioned")
    return
label sm1cs_ag002_m01_c02:
    $ player.set_choice("sm1cs_ag002_manhattan")
    return
label sm1cs_ag002_m01_c03:
    $ player.set_choice("sm1cs_ag002_mojito")
    return