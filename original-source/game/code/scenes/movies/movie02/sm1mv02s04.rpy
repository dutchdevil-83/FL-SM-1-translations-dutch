image sm1mv02s04-a46-glam = Movie(play = "images/MV/mv02/s04/anim/sm1mv02s04-a46-3x-60fps.webm",   start_image = "sm1mv02s04-a46 mh-glambot-00",  image = "sm1mv02s04-a46 mh-glambot-90",  loop = False)
image sm1mv02s04-a46-2-glam = Movie(play = "images/MV/mv02/s04/anim/sm1mv02s04-a46-2-3x-60fps.webm", start_image = "sm1mv02s04-a46-2 mes-glambot-00", image = "sm1mv02s04-a46-2 mes-glambot-90", loop = False)
label sm1mv02s04:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music music_disco_delight
    scene sm1mv02s04-01 mc-sy-phone1_c2 with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "Okay, it looks like Kanya emailed back to confirm that the photodojo is available."
    scene sm1mv02s04-01 mc-sy-phone1_c1 with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "Great. And..."
    play sound sfx_message_in1 volume 2.0
    scene sm1mv02s04-02 mc-sy-phone2_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    if player.get_choice("sm1mv02s02_recruit_mes"):
        mc "Min just replied back. She can join us this afternoon."
    else:
        mc "Lyssa just texted back. She just finished her brief so she has some time for us."
    scene sm1mv02s04-02 mc-sy-phone2_c2 with dissolve
    play voice3 stacy_happy_yay2 noloop
    sy "Excellent.{w} I'll text Taisia. You text Nari."
    play sound sfx_barefoot_steps1 volume 2.0 loop
    scene sm1mv02s04-03 mc-sy-look_c1 with dissolve
    play voice4 nari_arrogant_huh noloop
    ns "Text me about what?"
    stop sound fadeout 1.0
    scene sm1mv02s04-04 mc-sy-talk_c2 with dissolve
    play voice2 d1s2_mchey noloop volume 1.5
    mc "Hi Nari."
    play voice3 stacy_hey_attention1 noloop
    sy "Hey."
    mc "I was just going to text you to see if you could come and do a table read with us."
    scene sm1mv02s04-05 mc-sy-talk2_c1 with dissolve
    play voice4 nari_disappointed_mff noloop
    ns "A table read? Is that like when people decipher the meanings of leaves in tea?"
    scene sm1mv02s04-05 mc-sy-talk2_c3 with dissolve
    play voice2 mc_no_no2 noloop
    mc "Not really."
    mc "It's just like the first time the cast gets together and does a dry run of the script."
    scene sm1mv02s04-05 mc-sy-talk2_c2 with dissolve
    play voice3 stacy_yes_yap2 noloop
    sy "It's nice and simple and low pressure. But it's also a super-necessary step to make sure we find problems before we're filming a scene."
    scene sm1mv02s04-06 mc-sy-talk3_c1 with dissolve
    play voice4 nari_thinking_oh noloop
    ns "Oh, it is almost like we are beta testing the script."
    scene sm1mv02s04-05 mc-sy-talk2_c3 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Bingo."
    scene sm1mv02s04-07 mc-sy-talk4_c1 with dissolve
    play voice4 nari_disappointed_eeh noloop
    ns "I... I'm not sure I'm ready for that."
    play sound sfx_hair_scratch1
    scene sm1mv02s04-06 mc-sy-talk3_c2 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Huh?"
    scene sm1mv02s04-07 mc-sy-talk4_c3 with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Nari?"
    scene sm1mv02s04-07 mc-sy-talk4_c1 with dissolve
    play voice4 nari_arrogant_fff noloop
    ns "I have been preparing. Looking at tutorials online on how to be a better actress."
    ns "But each time I try to do the drills they suggest, it feels like my legs are going to lock up."
    menu:
        "It's natural to be a little nervous":
            $ player.set_choice("sm1mv02s04_normal_to_be_nervous")
            $ CharacterController.get_character("ns").add_point()
            scene sm1mv02s04-08 mc-sy-talk5_c2 with dissolve
            play voice2 mc_hey_hey7 noloop
            mc "Nari, it's totally natural to be a little nervous."
            mc "I was the same way when Stacy and I filmed our first scene."
            mc "Heck I was nervous the first time we recorded ourselves having sex."
            scene sm1mv02s04-08 mc-sy-talk5_c1 with dissolve
            play voice4 nari_surprised_huh1 noloop
            ns "You were?"
            scene sm1mv02s04-07 mc-sy-talk4_c3 with dissolve
            play voice2 mc_yes_yes3 noloop
            mc "Yes. But it gets easier each time."
            mc "But we all have to start somewhere."
            scene sm1mv02s04-07 mc-sy-talk4_c1 with dissolve
            play voice4 nari_happy_laugh3 noloop
            ns "Okay. Well... I guess if everyone gets nervous, this is just part of the tutorial. *giggles nervously*"
        "I won't let anything happen to you, Nari":
            scene sm1mv02s04-08 mc-sy-talk5_c2 with dissolve
            play voice2 mc_hey_hey7 noloop
            mc "Nari, it's me. I'm not going to let anything happen to you."
            scene sm1mv02s04-07 mc-sy-talk4_c1 with dissolve
            play voice4 nari_thinking_emm noloop
            ns "I know... but I fear my body will betray me."
            scene sm1mv02s04-07 mc-sy-talk4_c3 with dissolve
            play voice2 mc_thinking_hmm3 noloop
            mc "Don't let it. You're the one in control."
            play sound sfx_chair_slide1
            play sound2 sfx_cloth_rustling2 noloop
            scene sm1mv02s04-09 mc-sy-stand_c1 with dissolve
            play voice3 stacy_yes_yap1 noloop
            sy "Plus, we know some tricks to help with your nerves. Little breathing exercises and other things."
            scene sm1mv02s04-09 mc-sy-stand_c2 with dissolve
            play voice4 nari_happy_mmm noloop
            ns "Okay. Thanks, Stacy. I feel a little better."
    play sound sfx_hands_clap2
    play sound2 ["<silence 0.2>", sfx_hands_clap1] noloop
    scene sm1mv02s04-12 mc-sy-talk2_c2 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Alright, let's get a move on then."
    sy "No one else is going to run through this script for us."
    scene sm1mv02s04-12 mc-sy-talk2_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Did you get in touch with Taisia?"
    play sound sfx_cloth_rustling1
    scene sm1mv02s04-13 mc-sy-phone_c1 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "I think so. She texted back an emoji of a mouth eating something, the word 'my' and then an emoji of a clam."
    sy "But then she also sent a laughing face with a thumbs up emoji."
    scene sm1mv02s04-13 mc-sy-phone_c2 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "I think in Taisia talk, that means she is in."
    scene sm1mv02s04-14 mc-sy-talk_c1 with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Yup. Even if she's not, her role is much smaller than ours."
    play voice2 mc_yes_aga2 noloop
    mc "Cool. I'll order a rideshare."
    play sound sfx_throw_something1
    scene sm1mv02s04-14 mc-sy-talk_c2 with dissolve
    play voice4 nari_surprised_ehh noloop
    ns "We are actually doing {i}this{/i}."
    play sound sfx_door_openclosed1
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene sm1mv02s04-15 mc-sy-kv-tl-ns-dojo1_c1 with Fade(0.5, 0.5, 0.5)
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-16-2 mc-sy-kv-tl-ns-dojo2_c1 with dissolve
        play voice2 mc_hey_hey3 noloop
        mc "Hey everyone. Your fearless leader has arrived."
        scene sm1mv02s04-16-2 mc-sy-kv-tl-ns-dojo2_c2 with dissolve
        play voice5 min_happy_laugh3 noloop
        mes "Haha. I am eager to see how impressive you can be in a role like this, [mcname]."
        scene sm1mv02s04-17-2 mc-sy-kv-tl-ns-dojo2_c2 with dissolve
        play voice5 min_surprised_huh2 noloop
        mes "And who is this?"
        scene sm1mv02s04-17-2 mc-sy-kv-tl-ns-dojo2_c1 with dissolve
        pause
    else:
        scene sm1mv02s04-16 mc-sy-kv-tl-ns-dojo2_c1 with dissolve
        play voice2 mc_hey_hey3 noloop
        mc "Hey everyone. Your fearless leader has arrived."
        scene sm1mv02s04-16 mc-sy-kv-tl-ns-dojo2_c2 with dissolve
        play voice5 lissa_hey noloop
        mh "Good to see you, [mcname]."
        scene sm1mv02s04-17 mc-sy-kv-tl-ns-dojo2_c2 with dissolve
        play voice5 dahlia_thinking_hmm1 noloop
        mh "And who might you be, my dear?"
        scene sm1mv02s04-17 mc-sy-kv-tl-ns-dojo2_c1 with dissolve
        pause
    if player.get_choice("sm1mv02s02_recruit_mes"):
        play sound sfx_cloth_rustling4
        scene sm1mv02s04-18-2 mc-sy-kv-tl-ns-talk_c1 with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "I almost forgot."
        mc "Min, this is Nari."
        mc "Nari, this is Min Eun-Soo."
        mc "We took business classes together and became good friends."
        scene sm1mv02s04-21-2 mc-sy-kv-tl-ns-look2_c2 with dissolve
        play voice5 min_thinking_hmm3 noloop
        mes "Nice to meet you, Nari."
        scene sm1mv02s04-21-2 mc-sy-kv-tl-ns-look2_c1 with dissolve
        play voice4 nari_happy_yeah noloop
        ns "Yes. You too, Min!{w} I am sorry, I am just very excited."
        scene sm1mv02s04-21-2 mc-sy-kv-tl-ns-look2_c2 with dissolve
        play voice5 min_happy_laugh2 noloop
        mes "Haha. I may have you beat."
        mes "[mcname] and I have done plenty together."
        mes "But never something like this."
        scene sm1mv02s04-21-2 mc-sy-kv-tl-ns-look2_c1 with dissolve
        play voice4 nari_hey_asking noloop
        ns "I hope we can all make something wonderful together."
        play voice5 min_yes_ugu noloop
        mes "Mmhmm."
    else:
        play sound sfx_cloth_rustling4
        scene sm1mv02s04-18 mc-sy-kv-tl-ns-talk_c1 with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "I almost forgot."
        mc "Nari, this is Lyssa Harris. We met at a party and have been friends ever since."
        play sound sfx_cloth_rustling5 volume 1.4
        scene sm1mv02s04-19 mc-sy-kv-tl-ns-handshake_c2 with dissolve
        play voice5 dahlia_yes_yeah2 noloop
        mh "Lovely to meet you, Nari."
        scene sm1mv02s04-19 mc-sy-kv-tl-ns-handshake_c1 with dissolve
        play voice4 nari_surprised_huh2 noloop
        ns "Thank you. And are you also a professional porn actress? Like [mcname]?"
        scene sm1mv02s04-20 mc-sy-kv-tl-ns-look_c2 with dissolve
        play voice5 lissa_oh2 noloop
        mh "Oh {i}you're{/i} professional already?"
        scene sm1mv02s04-20 mc-sy-kv-tl-ns-look_c1 with dissolve
        play voice2 mc_happy_hah2 noloop
        mc "Haha. Doing my best."
        scene sm1mv02s04-21 mc-sy-kv-tl-ns-look2_c2 with dissolve
        play voice5 dahlia_thinking_hmm4 noloop
        mh "I can happily say that I am a professional, but not a professional porn actress."
        mh "I'm actually just a lawyer."
        scene sm1mv02s04-21 mc-sy-kv-tl-ns-look2_c1 with dissolve
        play voice4 nari_thinking_oh noloop
        ns "Oh. So you're here just for the legal stuff."
        scene sm1mv02s04-21 mc-sy-kv-tl-ns-look2_c2 with dissolve
        play voice5 dahlia_happy_hmm1 noloop
        mh "At first, that was the extent of my involvement."
        mh "But now..."
        scene sm1mv02s04-23 mc-sy-kv-tl-ns-talk1_c2 with dissolve
        play voice5 dahlia_thinking_hmm2 noloop
        mh "... well let's just say that [mcname] convinced me to dip my toes in the water a bit more."
        mh "I guess a little part of me has been very keen to at least try things out."
        mh "At least once."
        scene sm1mv02s04-23 mc-sy-kv-tl-ns-talk1_c1 with dissolve
        play voice4 nari_happy_laugh1 noloop
        ns "That sounds great. We're going to be porn actress virgins."
        play voice5 dahlia_yes_ugu noloop
        mh "I guess we will be, Nari."
    scene sm1mv02s04-24 mc-sy-kv-tl-ns-talk2_c2 with dissolve
    play voice7 kanya_happy_wooh noloop
    kv "Welcome to the team, Nari."
    kv "I'm Kanya, I'll be your photographer, camera girl, pretty much anything with a lens."
    scene sm1mv02s04-24 mc-sy-kv-tl-ns-talk2_c1 with dissolve
    play voice4 nari_hey_unsure noloop
    ns "Hello Kanya."
    scene sm1mv02s04-25 mc-sy-kv-tl-ns-talk3_c1 with dissolve
    play voice4 nari_thinking_hmm3 noloop
    ns "Is there uh... anything I should know to maximize my potential for {i}this{/i}?"
    scene sm1mv02s04-25 mc-sy-kv-tl-ns-talk3_c2 with dissolve
    play voice7 kanya_happy_laugh3 noloop
    kv "Hahah. I was going to ask you the same thing."
    kv "We want everyone on set to be completely comfortable and in cohesion with the script and the camerawork."
    scene sm1mv02s04-26 mc-sy-kv-tl-ns-talk4_c2 with dissolve
    play voice7 kanya_happy_relief3 noloop
    kv "And since I'm also your host, it will be my pleasure to help make your first porn journey as memorable and perfect as I can."
    play voice4 nari_happy_relief noloop
    ns "Thank you so much, Kanya. That makes me feel so much better."
    kv "I aim to please."
    if player.has_played_scene("sm1cs_tl007") and player.has_played_scene("sm1cs_ns014") and player.get_choice("ns_has_met_tl"):
        scene sm1mv02s04-27 mc-sy-kv-tl-ns-talk5_c2 with dissolve
        play voice6 girl24_surprised_huh2 noloop
        tl "How's it hanging, Nari?"
        scene sm1mv02s04-27 mc-sy-kv-tl-ns-talk5_c1 with dissolve
        play voice4 nari_disappointed_huh noloop
        ns "How is... {i}what{/i} hanging?"
        scene sm1mv02s04-28 mc-sy-kv-tl-ns-talk6_c2 with dissolve
        play voice6 girl24_happy_laugh3 noloop
        tl "Haha."
        tl "Looks like I'm finally going to see what is hidden under those pencil skirts of yours."
        scene sm1mv02s04-28 mc-sy-kv-tl-ns-talk6_c1 with dissolve
        play voice4 nari_thinking_hmm1 noloop
        ns "I guess so."
        menu:
            "Tell Taisia to play nice":
                $ player.set_choice("sm1mv02s04_tl_play_nice")
                scene sm1mv02s04-29 mc-sy-kv-tl-ns-talk3_c3 with dissolve
                play voice2 mc_arrogant_nah1 noloop
                mc "Don't tease your costar and neighbor, Taisia."
                scene sm1mv02s04-29 mc-sy-kv-tl-ns-talk3_c2 with dissolve
                play voice6 girl24_happy_laugh1 noloop
                tl "Haha. She likes it."
                scene sm1mv02s04-29 mc-sy-kv-tl-ns-talk3_c1 with dissolve
                play voice4 nari_happy_laugh4 noloop
                ns "*nervous laughter*"
            "Leave them be":
                scene sm1mv02s04-30 mc-sy-kv-tl-ns-talk8_c1 with dissolve
                play voice4 nari_yes_emotional noloop
                ns "I have noticed that you have a very nice looking ass."
                ns "And you seem to enjoy it when [mcname] fucks it."
                ns "Are you... a big fan of anal?"
                scene sm1mv02s04-30 mc-sy-kv-tl-ns-talk8_c2 with dissolve
                play voice6 girl24_surprised_oh1 noloop
                tl "Oh."
                tl "I mean, I don't usually think of it like that."
                tl "It just kind of comes up and then boom, [mcname] is dicking me down and probably spanking me too."
                scene sm1mv02s04-31 mc-sy-kv-tl-ns-talk9_c1 with dissolve
                play voice4 nari_surprised_ohmy noloop
                ns "Oh. That does sound nice."
                scene sm1mv02s04-31 mc-sy-kv-tl-ns-talk9_c2 with dissolve
                play voice6 girl24_hey_greeting noloop
                tl "You enjoy a little rough touch... don't you?"
                scene sm1mv02s04-32 mc-sy-kv-tl-ns-set1_c1 with dissolve
                play voice4 nari_thinking_hmm2 noloop
                ns "With, [mcname]. But... if he'd like... Maybe I could try with you."
                scene sm1mv02s04-32 mc-sy-kv-tl-ns-set1_c2 with dissolve
                play voice6 girl24_thinking_hmm4 noloop
                tl "Heh heh. Well, we shouldn't keep them waiting."
    else:
        $ player.set_choice("ns_has_met_tl")
        scene sm1mv02s04-33 mc-sy-kv-tl-ns-set2_c1 with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "And you may have seen this character around home."
        mc "Taisia Lindquist. We met at the theater."
        scene sm1mv02s04-33-3 mc-sy-kv-tl-ns-set4_c1 with dissolve
        play voice4 nari_yes_emotional noloop
        ns "And now she lives with us."
        scene sm1mv02s04-33-3 mc-sy-kv-tl-ns-set4_c2 with dissolve
        play voice6 girl24_yes_yap noloop
        tl "I'm always good at finding perks."
        play voice4 nari_sex_closedmoan1 noloop
        ns "Mmmm."
        scene sm1mv02s04-33-2 mc-sy-kv-tl-ns-set3_c1 with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "And this is Taisia, a colleague from the local theater."
        scene sm1mv02s04-33-2 mc-sy-kv-tl-ns-set3_c2 with dissolve
        play voice6 girl24_surprised_huh1 noloop
        tl "'Colleague'? So formal."
        tl "You sure you came to the right spot, Nari?"
        scene sm1mv02s04-33-3 mc-sy-kv-tl-ns-set4_c1 with dissolve
        play voice4 nari_sex_closedmoan6 noloop
        ns "Ummm. I mean, [mcname] is here..."
        scene sm1mv02s04-33-3 mc-sy-kv-tl-ns-set4_c2 with dissolve
        play voice6 girl24_yes_yeah noloop
        tl "Yeah but you look a bit shy and nervous. Not exactly porn actress material."
        scene sm1mv02s04-34 mc-sy-kv-tl-ns-gestur_c1 with dissolve
        play voice2 mc_yes_sure1 noloop
        mc "Rest assured, Nari is a naughty as they come."
        scene sm1mv02s04-33-2 mc-sy-kv-tl-ns-set3_c2 with dissolve
        play voice6 girl24_thinking_mff noloop
        tl "Hmm. Guess we'll see."
    play sound sfx_sport_run1 volume 2.5 loop
    scene sm1mv02s04-35 mc-sy-kv-tl-ns-run_c2 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay everyone. Let's get used to our seats and stations."
    play sound sfx_lean_glassdoor volume 2.5
    scene sm1mv02s04-35 mc-sy-kv-tl-ns-run_c1 with dissolve
    play voice3 stacy_moan7 noloop
    sy "Awesome."
    play voice4 nari_sex_closedmoan2 noloop
    ns "I can't wait."
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-36-2 mc-sy-kv-tl-ns-walk_c2 with dissolve
        play voice5 min_arrogant_huh2 noloop
        mes "I may have already peaked a little."
        play voice3 stacy_hey noloop
        sy "Min!"
        mes "I couldn't resist."
    else:
        scene sm1mv02s04-36 mc-sy-kv-tl-ns-walk_c2 with dissolve
        play voice5 dahlia_disappointed_hmm1 noloop
        mh "And a hush falls over the crowd."
        scene sm1mv02s04-36 mc-sy-kv-tl-ns-walk_c1 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "You're going to love it."
    play sound sfx_chair_slide1
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-37-2 mc-sy-kv-tl-ns-look_c2 with dissolve
        play voice5 min_thinking_mhh noloop
        mes "Hmmm."
    else:
        scene sm1mv02s04-37 mc-sy-kv-tl-ns-look_c2 with dissolve
        play voice5 lissa_ha noloop
        mh "Hah. Fine craftsmanship."
    scene sm1mv02s04-39 mc-sy-kv-tl-ns-look_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Awww yeah."
    scene sm1mv02s04-37 mc-sy-kv-tl-ns-look_c3 with dissolve
    play voice4 nari_happy_relief noloop
    ns "Woah."
    scene sm1mv02s04-38 mc-sy-kv-tl-ns-sit_c1 with dissolve
    play sound sfx_phonecamera_flash1
    play voice4 nari_thinking_hmm1 noloop
    ns "So cool."
    scene sm1mv02s04-39 mc-sy-kv-tl-ns-look_c2 with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Thanks, Nari. But make sure to just keep that photo yourself."
    mc "No sharing yet."
    scene sm1mv02s04-39 mc-sy-kv-tl-ns-look_c1 with dissolve
    play voice4 nari_thinking_mff noloop
    ns "I know. Maybe after the movie is done."
    ns "And where do I sit?"
    scene sm1mv02s04-40 mc-sy-kv-tl-ns-point_c2 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "For some of the scenes, you will probably be setup at one of the sub consoles."
    mc "Ah."
    mc "Why don't you have a seat on the command couch for now."
    play sound sfx_cloth_rustling4 volume 1.6
    scene sm1mv02s04-40 mc-sy-kv-tl-ns-point_c1 with dissolve
    play voice4 nari_yes_yep noloop
    ns "Okay."
    if player.get_choice("sm1mv02s02_recruit_mes"):
        play voice5 min_hey_simple noloop
        mes "This is all prety impressive."
        mes "I actually feel like I'm on some space age battleship."
    else:
        scene sm1mv02s04-42 mc-sy-kv-tl-ns-talk_c2 with dissolve
        play voice5 dahlia_hey_active1 noloop
        mh "This is all prety impressive."
        mh "I actually feel like I'm on some space age battleship."
        scene sm1mv02s04-42 mc-sy-kv-tl-ns-talk_c1 with dissolve
    play voice2 mc_yes_yes8 noloop
    mc "It's powerful yes, but the {i}Intrepid{/i} is a vessel of discovery first and foremost."
    play sound sfx_chair_slide1 volume 1.6
    scene sm1mv02s04-43 mc-sy-kv-tl-ns-stand_c2 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Derp. I forgot the scripts."
    play sound sfx_paper_rustl1 volume 2.0
    $ renpy.music.set_volume(1.0, 3.5, "music" )
    scene sm1mv02s04-44 mc-sy-kv-tl-ns-script_c2 with dissolve
    pause
    if player.get_choice("sm1mv02s02_recruit_mes"):
        play sound sfx_paper_rustl2
        scene sm1mv02s04-45-2 mc-sy-kv-tl-ns-script2_c1 with dissolve
        pause
        play sound sfx_paper_rustl3
        scene sm1mv02s04-45 mc-sy-kv-tl-ns-script2_c2 with dissolve
        pause
        play sound sfx_cloth_rustling5
        scene sm1mv02s04-a46-2 mes-glambot-00 with dissolve
        pause
        play sound ["<silence 0.3>", sfx_camera_fly1] volume 3.0
        scene sm1mv02s04-a46-2-glam
        pause
    else:
        play sound sfx_paper_rustl2
        scene sm1mv02s04-45 mc-sy-kv-tl-ns-script2_c1 with dissolve
        pause
        play sound sfx_paper_rustl3
        scene sm1mv02s04-45 mc-sy-kv-tl-ns-script2_c2 with dissolve
        pause
        play sound sfx_cloth_rustling5
        scene sm1mv02s04-a46 mh-glambot-00 with dissolve
        pause
        play sound ["<silence 0.3>", sfx_camera_fly1] volume 3.0
        scene sm1mv02s04-a46-glam
        pause
    $ renpy.music.set_volume(0.7, 1.5, "music" )
    play voice2 mc_yes_okay1 noloop
    mc "Alright. Let's get cracking."
    $ renpy.music.set_volume(1.0, 2.0, "music" )
    jump sm1mv02s04_later
label sm1mv02s04_later:
    scene black
    show screen scene_transistion(_("About thirty minutes later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.7, 2.0, "music" )
    scene sm1mv02s04-48 mc-sy-kv-tl-ns-talk_c2 with dissolve
    play voice3 stacy_hey_happy1 noloop
    sy "Great work everyone. We're halfway done."
    sy "Let's have everyone just stretch out a bit. Keep the blood flowing."
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-49-2 mc-sy-kv-tl-ns-talk2_c1 with dissolve
        play voice5 min_yes_yeah1 noloop
        mes "These chairs look good, but they're a bit hell on my back."
    else:
        scene sm1mv02s04-49 mc-sy-kv-tl-ns-talk2_c1 with dissolve
        play voice5 dahlia_disappointed_ehh3 noloop
        mh "Perfect time for a break. I sit around enough as it is."
    $ renpy.music.set_volume(1.0, 1.0, "music" )
    scene sm1mv02s04-47 mc-sy-kv-tl-ns-stretche_c1
    with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.7, 5.0, "music" )
    play sound sfx_cloth_rustling1
    pause
    play sound sfx_rope_stretch
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-47-2 mc-sy-kv-tl-ns-stretche_c2 with dissolve
        pause
    else:
        scene sm1mv02s04-47 mc-sy-kv-tl-ns-stretche_c2 with dissolve
        pause
    scene sm1mv02s04-50 mc-sy-kv-tl-ns-talk3_c2 with dissolve
    play voice3 stacy_yes_fine4 noloop
    sy "Are we all set?"
    play voice6 girl24_yes_aga noloop
    tl "Light it up."
    scene sm1mv02s04-52 mc-sy-kv-tl-ns-talk5_c2 with dissolve
    play voice4 nari_yes_aga2 noloop
    ns "Sure."
    scene sm1mv02s04-50 mc-sy-kv-tl-ns-talk3_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Hit it."
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-51-2 mc-sy-kv-tl-ns-talk4_c3 with dissolve
        play voice5 min_yes_simple noloop
        mes "I'm ready to fly."
    else:
        scene sm1mv02s04-51 mc-sy-kv-tl-ns-talk4_c3 with dissolve
        play voice5 lissa_ugu2 noloop
        mh "Aye aye, Captain Stacy."
    play sound sfx_paper_rustl1
    scene sm1mv02s04-53 mc-sy-kv-tl-ns-ask_c1 with dissolve
    play voice3 stacy_happy_laugh4 noloop
    sy "*giggles*"
    sy "Alright. Scene Four. Interior {i}Intrepid{/i} Bridge."
    scene sm1mv02s04-52 mc-sy-kv-tl-ns-talk5_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Status report Number One."
    play voice3 stacy_angry noloop
    sy "The ship is still in orbit over Planet Vemtyral."
    sy "The ion storm is getting closer, but should pass us without complication."
    mc "Good, Commander Orion."
    play sound sfx_chair_slide1 volume 1.6
    scene sm1mv02s04-54 mc-sy-kv-tl-ns-stand_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Lieutenant Spectre, how's that cure coming along?"
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-53-2 mc-sy-kv-tl-ns-ask_c3 with dissolve
        play voice5 min_thinking_oh noloop
        mes "We are making good progress, Captain."
        mes "With Doctor Jelerra's expert help, we should have results within a cycle."
    else:
        scene sm1mv02s04-53 mc-sy-kv-tl-ns-ask_c3 with dissolve
        play voice5 lissa_oh noloop volume 1.4
        mh "We are making good progress, Captain."
        mh "With Doctor Jelerra's expert help, we should have results within a cycle."
    scene sm1mv02s04-54 mc-sy-kv-tl-ns-stand_c2 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Good to have you with us, Doctor."
    play voice4 nari_thinking_hm noloop
    ns "You are welcome, Captain."
    ns "Your ship and its crew are amazing by the way. I believe that working together, we will be able to save my people."
    mc "Of course. But until then, consider yourself a guest aboard the {i}Intrepid{/i}."
    $ renpy.music.set_volume(1.0, 2.0, "music" )
    scene black
    show screen scene_transistion(_("About an hour later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 2.0, "music" )
    scene sm1mv02s04-56 mc-sy-kv-tl-ns-ask_c1
    with Fade(0.5, 0.5, 0.5)
    play voice3 stacy_thinking_emm4 noloop
    sy "And cut.{w} Or at least that is what I'd be saying if we were filming."
    scene sm1mv02s04-53 mc-sy-kv-tl-ns-ask_c2 with dissolve
    play voice4 nari_happy_laugh6 noloop
    ns "Hehe. So this is how it goes for you guys?"
    ns "It is just pretend, but like, serious pretending?"
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-57-2 mc-sy-kv-tl-ns-talk_c2 with dissolve
        play voice5 min_yes_yeah2 noloop
        mes "It looks that way. It's funny, it's almost exactly how I imagined it."
    else:
        scene sm1mv02s04-57 mc-sy-kv-tl-ns-talk_c2 with dissolve
        play voice5 lissa_laugh noloop
        mh "Haha, I like that phrase. 'Serious pretending', sounds like what most of my opponents try to do when they know their client is cooked."
    play sound sfx_hands_clap2
    play sound2 ["<silence 0.2>", sfx_hands_clap1] noloop
    scene sm1mv02s04-55 mc-sy-kv-tl-ns-stand2_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "I just wanted to say that everyone did great."
    if player.get_choice("pirates_movie_done"):
        if player.get_choice("sm1mv02s02_recruit_mes"):
            scene sm1mv02s04-54-2 mc-sy-kv-tl-ns-stand_c3 with dissolve
            play voice5 min_thinking_hmm2 noloop
            pause
            scene sm1mv02s04-59 mc-sy-kv-tl-ns-talk3_c2 with dissolve
        else:
            scene sm1mv02s04-54 mc-sy-kv-tl-ns-stand_c3 with dissolve
            play voice5 lissa_moan1 noloop
            pause
            scene sm1mv02s04-58 mc-sy-kv-tl-ns-talk2_c1 with dissolve
        play voice2 mc_arrogant_heh2 noloop
        mc "This is certainly a bigger team than the pirate film, and I know it might be harder for our veterans."
        mc "But I think we learned a lot before and that will make this film even better."
    else:
        if player.get_choice("sm1mv02s02_recruit_mes"):
            scene sm1mv02s04-57-2 mc-sy-kv-tl-ns-talk_c2 with dissolve
            play voice5 min_thinking_hmm2 noloop
            pause
        else:
            scene sm1mv02s04-58 mc-sy-kv-tl-ns-talk2_c2 with dissolve
            play voice5 lissa_moan1 noloop
            pause
        scene sm1mv02s04-59 mc-sy-kv-tl-ns-talk3_c2 with dissolve
        play voice2 mc_arrogant_heh2 noloop
        mc "This movie is far more than just your parents' thematic porn movie."
        mc "But I am sure that we will all pitch in to make it something special."
    scene sm1mv02s04-59-2 mc-sy-kv-tl-ns-talk4_c2 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "Now we just need to memorize our lines and do it with the camera rolling."
    play voice4 nari_happy_yay noloop
    ns "Excellent."
    scene sm1mv02s04-59 mc-sy-kv-tl-ns-talk3_c2 with dissolve
    play voice2 d2s9_mchey noloop volume 1.3
    mc "Kanya, you have a line on some nice costumes, right?"
    scene sm1mv02s04-59-2 mc-sy-kv-tl-ns-talk4_c1 with dissolve
    play voice7 kanya_yes_yep1 noloop
    kv "Yup. I think you'll be pleasantly surprised, [mcname]."
    play voice2 mc_thinking_mmm1 noloop
    mc "You never let me down."
    scene sm1mv02s04-58 mc-sy-kv-tl-ns-talk2_c3 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Do we have any questions before we break for today?"
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-57-2 mc-sy-kv-tl-ns-talk_c2 with dissolve
        play voice5 min_no_happy noloop
        mes "No, I think I will be good."
        mes "Memorizing lines on a script is just like memorizing sheet music for a piano recital, like when I was young."
        play voice3 stacy_yes_ugu1 noloop
        sy "Excellent, Min."
    else:
        scene sm1mv02s04-57 mc-sy-kv-tl-ns-talk_c2 with dissolve
        play voice5 lissa_lno noloop
        mh "I prepare to read in front of a full courthouse all the time."
        mh "These lines should be a piece of cake, Stacy."
        scene sm1mv02s04-57 mc-sy-kv-tl-ns-talk_c1 with dissolve
        play voice3 stacy_yes_ugu1 noloop
        sy "Awesome, Lyssa. I know you'll be incredible."
        scene sm1mv02s04-54 mc-sy-kv-tl-ns-stand_c3 with dissolve
        play voice5 lissa_haha2 noloop
        mh "I didn't say that, don't quote me on that."
        mh "Hehee."
        mh "I will settle for at least being enticing."
        scene sm1mv02s04-58 mc-sy-kv-tl-ns-talk2_c1 with dissolve
        play voice2 d1s5_mcthinks noloop volume 1.7
        mc "I don't think there will be any problem hitting that mark."
    scene sm1mv02s04-59 mc-sy-kv-tl-ns-talk3_c1 with dissolve
    play voice7 kanya_yes_aga4 noloop
    kv "Sounds like we're all ready for the next step, which is good because I have to kick you guys out shortly."
    kv "Studio is being used for an antiacid commercial."
    scene sm1mv02s04-59 mc-sy-kv-tl-ns-talk3_c2 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Thanks again for all your help on this one, Kanya."
    mc "We'll be in touch when we're ready to start filming."
    scene sm1mv02s04-59-2 mc-sy-kv-tl-ns-talk4_c1 with dissolve
    play voice7 kanya_arrogant_laugh noloop
    kv "I can't wait."
    scene sm1mv02s04-59-2 mc-sy-kv-tl-ns-talk4_c2 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Until then, everyone, I'll see you around."
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    if player.get_choice("sm1mv02s02_recruit_mes"):
        scene sm1mv02s04-60 mc-sy-kv-tl-ns-walk_c1 with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "And I'll see you back at home."
        stop sound2 fadeout 1.5
        stop sound3 fadeout 1.5
        scene sm1mv02s04-61-2 mc-sy-kv-tl-ns-wave_c1 with dissolve
        play voice2 mc_arrogant_huh1 noloop
        mc "And you, come to think about it."
        scene sm1mv02s04-61-2 mc-sy-kv-tl-ns-wave_c2 with dissolve
        play voice5 min_happy_laugh4 noloop
        mes "Am I so easily forgotten."
        play voice2 mc_no_nah2 noloop
        mc "Not a chance."
    else:
        scene sm1mv02s04-60 mc-sy-kv-tl-ns-walk_c1 with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "And I'll see you back at home."
        stop sound2 fadeout 1.5
        stop sound3 fadeout 1.5
        scene sm1mv02s04-61 mc-sy-kv-tl-ns-wave_c1 with dissolve
        play voice2 mc_arrogant_huh1 noloop
        mc "I'm so excited to show you more of the process, Lyssa."
        mc "You still interested?"
        scene sm1mv02s04-61 mc-sy-kv-tl-ns-wave_c2 with dissolve
        play voice5 lissa_yes noloop
        mh "Very, [mcname]. Now that I've breathed life into the character, I cannot fathom letting Commander Spectre down."
        scene sm1mv02s04-62 mc-sy-kv-tl-ns-wave2_c1 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Happy to hear it. Goodbye, Lyssa."
        play voice5 dahlia_yes_ugu noloop
        mh "Ciao [mcname]."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(MOVIE_SCIFI, 3, 0, 5)
    return