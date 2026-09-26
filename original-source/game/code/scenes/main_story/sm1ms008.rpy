image sm1ms008-glambot-1 = Movie(play = "images/ms/s008/anim/sm1ms008-a76-01-4x-48fps.webm", start_image = "sm1ms008-a76-01 red_wig_acquired_sy_walks_back-glambot-76-01-00_i", image = "sm1ms008-a76-01 red_wig_acquired_sy_walks_back-glambot-76-01-39_i", loop = False)
image sm1ms008-glambot-2 = Movie(play = "images/ms/s008/anim/sm1ms008-a81-2x-50fps.webm", start_image = "sm1ms008-a81 red_wig_acquired_sy_wig-glambot-81-009_i", image = "sm1ms008-a81 red_wig_acquired_sy_wig-glambot-81-099_i", loop = False)
label sm1ms008:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    scene black
    show screen scene_transistion(_("At the Photo Dojo"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.0, 0.0, "music" )
    $ renpy.music.set_volume(0.55, 0.0, "music2" )
    $ renpy.music.play(audio.music_disco_funk, "music" , True, None, True, 1.0)
    $ renpy.music.play(audio.music_disco_funk_reverbed, "music2", True, None, True, 1.0)
    scene sm1ms008-00 red_wig_acquired_kv_talk_clean
    with Fade(0.5, 0.5, 0.5)
    play voice4 kanya_angry_argh noloop
    kv "Gah. Last time I work for a food influencer. Mayonnaise doesn't play nice with a camera."
    kv "Still looks sexy as a thong though."
    play sound sfx_door_closed7 volume 1.6
    queue sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1ms008-01 red_wig_acquired_mc_stacy_walkin with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms008-02 red_wig_acquired_sy_talk_wave_nervous with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Hi, Kanya!"
    scene sm1ms008-03 red_wig_acquired_kv_talk_surprised with dissolve
    play voice4 kanya_hey_simple2 noloop
    kv "Hey! I wasn't expecting you today, [mcname]. What's up?"
    scene sm1ms008-04 red_wig_acquired_mc_talk with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "We have some good news. We-"
    scene sm1ms008-05 red_wig_acquired_sy_talknterrupts with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "We landed our first big client!"
    scene sm1ms008-06 red_wig_acquired_mc_talk_deflatedsmile with dissolve
    play voice2 mc_angry_off noloop
    mc "Thunder stealer. I wanted to tell her."
    scene sm1ms008-07 red_wig_acquired_sy_talk_laughs with dissolve
    play voice3 stacy_happy_laugh3 noloop
    sy "Hahaha."
    play sound kanya_arrogant_pff
    play voice3 stacy_arrogant_hmm2 noloop
    scene sm1ms008-08 red_wig_acquired_sy_talk_tongue with dissolve
    pause
    scene sm1ms008-09 red_wig_acquired_kv_talk_chuckles with dissolve
    play voice4 kanya_happy_laugh3 noloop
    kv "*chuckles softly*"
    scene sm1ms008-10 red_wig_acquired_sy_talk with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "I'm the one handling our email, so it was my news to share, right?"
    scene sm1ms008-11 red_wig_acquired_mc_talk_shake with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Alright. It's not a competition."
    scene sm1ms008-12 red_wig_acquired_sy_talk with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "I know, cause I kicked your butt."
    scene sm1ms008-13 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_surprised_ohmy noloop
    kv "You must be Stacy. I was beginning to think we'd never meet up."
    scene sm1ms008-14 red_wig_acquired_sy_talk_surprised with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "Haha. What makes you say that?"
    scene sm1ms008-15 red_wig_acquired_kv_talk_shrug with dissolve
    play voice4 kanya_surprised_eeh2 noloop
    kv "Well, I guess it's been a while since [mcname] and I started working together, and we just..."
    kv "Hadn't got the chance yet."
    scene sm1ms008-16 red_wig_acquired_sy_talk_flourish with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "Mmhmm. {w}Well, here I am."
    if persistent.is_special:
        sy "[mcname]'s little sister, in the flesh."
    else:
        sy "[mcname]'s best friend, in the flesh."
    scene sm1ms008-17 red_wig_acquired_kv_talk_warmup with dissolve
    play voice4 kanya_yes_yeah2 noloop
    kv "It's very good to meet you, Stacy."
    play sound sfx_bed_fall1 volume 1.7
    scene sm1ms008-18 red_wig_acquired_kv_talk_holdout_hand with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1ms008-19 red_wig_acquired_sy_talk_shakehand with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Samsies, Kanya. I've really enjoyed your photos online, and I'm sure you'll do great on the scenes."
    scene sm1ms008-20 red_wig_acquired_kv_talk_smiling with dissolve
    play voice4 kanya_yes_long noloop
    kv "I'll do my best. I don't want to let [mcname] down."
    scene sm1ms008-21 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I'm sure you'll do good."
    scene sm1ms008-22 red_wig_acquired_kv_talk_awkward_silence with dissolve
    pause
    play sound sfx_hands_clap2
    scene sm1ms008-23 red_wig_acquired_kv_talk_clap with dissolve
    play voice4 kanya_happy_relief2 noloop
    kv "I'm pumped that you guys got your first job already. I remember how excited I got when I was starting out."
    scene sm1ms008-24 red_wig_acquired_kv_talk_finger with dissolve
    play voice4 kanya_disappointed_ohh noloop
    kv "After I got the down payment I ignored all my classes for a solid week."
    kv "Every day I was working my tail off to get the client a perfect photoshoot."
    kv "It was so bad, I think I missed two exams. Almost had to retake a class."
    scene sm1ms008-25 red_wig_acquired_kv_talk_relaxing with dissolve
    play voice4 kanya_arrogant_laugh noloop
    kv "But in the end, I survived and got my grades back up while starting my photography career."
    play sound sfx_hair_scratch1
    scene sm1ms008-26 red_wig_acquired_sy_talk_mc_palm with dissolve
    play voice3 stacy_happy_laugh4 noloop
    sy "You should have just dropped out like we did."
    scene sm1ms008-27 red_wig_acquired_kv_talk_sure with dissolve
    play voice4 kanya_no_nah2 noloop
    kv "That's not really my style. I like to see things through."
    scene sm1ms008-28 red_wig_acquired_kv_talk_mcglance with dissolve
    play voice4 kanya_arrogant_ha noloop
    kv "So, what's the lowdown boss? What kind of job are we looking at? A gangbang? A cosplay bukkake scene?"
    kv "Don't leave me in suspense, [mcname]."
    scene sm1ms008-29 red_wig_acquired_mc_talk_excited with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "It's pretty straightforward, just a one on one scene. The client has a couple of criteria."
    scene sm1ms008-30 red_wig_acquired_mc_talk_motionstacy with dissolve
    play voice2 mc_znames_stacy1 noloop
    mc "Stacy."
    scene sm1ms008-31 red_wig_acquired_sy_talk_smiles with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Thank you, [mcname]. It sounds like the client is into a little rough stuff. They want some spanking and maybe a little choking, little man-handling."
    scene sm1ms008-32 red_wig_acquired_kv_talk_lick with dissolve
    play voice4 kanya_sex_closedmoan5 noloop
    pause
    scene sm1ms008-33 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_happy_laugh1 noloop
    kv "I like their taste already."
    play sound sfx_jeans_fly1 volume 1.7
    scene sm1ms008-34 red_wig_acquired_sy_talk_bag with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "Thre is one last request. It's a little strange. They want the girl to be a redhead. So [mcname] picked up this wig."
    play sound sfx_skirt_off2
    scene sm1ms008-35 red_wig_acquired_kv_talk_wig with dissolve
    play voice4 kanya_disappointed_oh noloop
    kv "Interesting. Well, we should definitely have the actress try it on before the shoot. Want to make sure it looks good."
    kv "Wigs can look perfect on their own. But if a girl is moving around in one, it can get messy."
    scene sm1ms008-36 red_wig_acquired_sy_talk_wink with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "Good idea. I'll definitely be moving around."
    scene sm1ms008-37 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_surprised_oh noloop
    kv "Oh... so you're going to be the redhead Stacy?"
    scene sm1ms008-38 red_wig_acquired_sy_talk with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Of course. Who else?"
    scene sm1ms008-39 red_wig_acquired_kv_talk_thinking with dissolve
    play voice4 kanya_arrogant_huh noloop
    kv "Ah-hah. I thought that you two might be fooling around together."
    scene sm1ms008-40 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Really? What made you think that?"
    jump sm1ms008_special
label sm1ms008_special:
    if persistent.is_special:
        scene sm1ms008-41 red_wig_acquired_kv_talk_smile_more with dissolve
        play voice4 kanya_happy_laugh2 noloop
        kv "How many times have you heard of a brother and sister working together at a porn studio?"
        kv "And knowing how kinky you are, [mcname], I imagined your sister might be cut from the same cloth."
        scene sm1ms008-40 red_wig_acquired_sy_talk with dissolve
        play voice3 stacy_hey_angry1 noloop
        sy "Hey, I was sweet and innocent before he left me his porn collection."
        mct "Not sure I'd frame it like that."
        play sound sfx_cloth_rustling3
        scene sm1ms008-44 red_wig_acquired_sy_talk_sexypose with dissolve
        play voice3 stacy_happy_laugh1 noloop
        sy "But now I'm the horny kitty that he can't keep his eyes off of."
        scene sm1ms008-45 red_wig_acquired_kv_talk_excited with dissolve
        play voice4 kanya_happy_yeah noloop
        kv "I love it! I've done a lot, but never taken pictures of siblings getting down and dirty."
        scene sm1ms008-46 red_wig_acquired_mc_talk_kanya with dissolve
        play voice2 d1s2_hmm noloop volume 1.5
        mc "So you're cool with it, Kanya?"
        scene sm1ms008-47 red_wig_acquired_kv_talk with dissolve
        play voice4 kanya_yes_yeah3 noloop
        kv "Totally. When you do this all the time like I do, it's great when something pops up on your feed."
        scene sm1ms008-48 red_wig_acquired_kv_talk_kinky with dissolve
        play voice4 kanya_thinking_hmm1 noloop
        kv "And I promise to keep from getting too hot and bothered while I watch you two in action."
        scene sm1ms008-49 red_wig_acquired_mc_talk with dissolve
        play voice2 mc_arrogant_huh1 noloop
        mc "That's good to know."
        scene sm1ms008-50 red_wig_acquired_kv_talk_fingerchin with dissolve
        play voice4 kanya_disappointed_oof noloop
        kv "Ooooh, and the brother-sister angle will help our films do better on the market too."
        scene sm1ms008-51 red_wig_acquired_sy_talk with dissolve
        play voice3 stacy_yes_yeah1 noloop
        sy "Oh yeah! I don't think any other studio around will have that on their bingo card."
    else:
        scene sm1ms008-41 red_wig_acquired_kv_talk_smile_more with dissolve
        play voice4 kanya_happy_laugh2 noloop
        kv "When you talked about your 'best' friend, I had a feeling you might be friends with benefits by the way you talked about her."
        scene sm1ms008-31 red_wig_acquired_sy_talk_smiles with dissolve
        play voice3 stacy_disappointed_oh2 noloop
        sy "Awww, you're so sweet, [mcname]."
        scene sm1ms008-42 red_wig_acquired_silence_kv_talk_clap with dissolve
        play voice4 kanya_hey_long noloop
        kv "How long have you been dating?"
        scene sm1ms008-46 red_wig_acquired_mc_talk_kanya with dissolve
        play voice2 mc_thinking_hmm1 noloop
        mc "Hmm. I guess technically, it's only been a few weeks."
        mc "But we were best friends for years before we finally took things to the next level."
        scene sm1ms008-43 red_wig_acquired_sy_talk_playful_mc_thought with dissolve
        play voice3 stacy_disappointed_ehh1 noloop
        sy "Ugh. Don't remind me. We should have gotten together years ago, [mcname]."
        sy "So much wasted time."
        play sound sfx_cloth_rustling4
        scene sm1ms008-54 red_wig_acquired_mc_talk with dissolve
        play voice2 mc_thinking_hmm8 noloop
        mc "Well, we're together now. that's the important part."
        scene sm1ms008-53 red_wig_acquired_sy_talk_laugh with dissolve
        play voice3 stacy_yes_ugu1 noloop
        sy "Mmhmm."
    scene sm1ms008-55 red_wig_acquired_kv_talk_focus with dissolve
    play voice4 kanya_thinking_eeh1 noloop
    kv "Alright, so to recap, for this scene, it will be you two together, and I will be operating the camera."
    scene sm1ms008-56 red_wig_acquired_kv_talk_bragging with dissolve
    play voice4 kanya_disappointed_hm noloop
    kv "I can promise you both you will not be disappointed when we see the final cut."
    kv "The studio's first film is going to knock the client's socks off."
    scene sm1ms008-57 red_wig_acquired_sy_talk_fist with dissolve
    play voice3 stacy_happy_yay2 noloop
    sy "Brilliant! I can't wait to see you in action, Kanya."
    scene sm1ms008-58 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "She's going to do great. I've already seen some of her magic at the photo dojo."
    mc "I think we'll be in for a treat when we see the final product."
    scene sm1ms008-59 red_wig_acquired_kv_talk_kinky with dissolve
    play voice4 kanya_happy_relief3 noloop
    kv "Thanks [mcname]. There will probably be a lot of treats for us all to enjoy."
    scene sm1ms008-60 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "And don't worry about not getting to act with me this time, Kanya."
    mc "If you want to be in front of the camera some time, I'm sure there will be an opening for that down the line."
    scene sm1ms008-61 red_wig_acquired_kv_talk_smiles with dissolve
    play voice4 kanya_arrogant_yeah noloop
    kv "You read my mind, [mcname]. Maybe we'll do a threesome scene sometime."
    scene sm1ms008-62 red_wig_acquired_sy_talk with dissolve
    play voice3 stacy_surprised_ohmy1 noloop
    sy "Oh my..."
    scene sm1ms008-63 red_wig_acquired_sy_talk_all_exceited with dissolve
    pause
    scene sm1ms008-64 red_wig_acquired_sy_talk_mc with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "So, should I try the wig on now, [mcname]?"
    scene sm1ms008-65 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Couldn't hurt. Like Kanya said, we don't want to wait till we start and see a problem."
    scene sm1ms008-66 red_wig_acquired_sy_talk_mc with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Right."
    scene sm1ms008-67 red_wig_acquired_sy_talk_walks_away with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "Give me a minute."
    play sound sfx_heels_steps2 loop volume 1.4
    scene sm1ms008-68 red_wig_acquired_kv_talk_walks_away with dissolve
    if persistent.is_special:
        play voice4 kanya_arrogant_laugh noloop
        kv "Your sister is very nice, [mcname]."
        stop sound fadeout 2.0
        scene sm1ms008-69 red_wig_acquired_mc_talk_grinning with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "She can be a handful. But I love her."
    else:
        play voice4 kanya_arrogant_laugh noloop
        kv "Stacy is very nice. You two have been friends for a long time?"
        stop sound fadeout 2.0
        scene sm1ms008-69 red_wig_acquired_mc_talk_grinning with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "Yup. Pretty much since we were growing up."
        scene sm1ms008-70 red_wig_acquired_mc_talk with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "She can be a lot to handle, but when something is important to her, she always puts her best foot forward."
        scene sm1ms008-71 red_wig_acquired_kv_talk_smiles with dissolve
        play voice4 kanya_yes_aga4 noloop
        kv "That's good to know."
    scene sm1ms008-72 red_wig_acquired_kv_talk_question with dissolve
    play voice4 kanya_thinking_eeh5 noloop
    kv "So what about location? Are you wanting to do it here?"
    scene sm1ms008-73 red_wig_acquired_kv_talk_thinking with dissolve
    play voice4 kanya_thinking_hmm3 noloop
    kv "It's possible I can block out enough time for one scene to be filmed here."
    scene sm1ms008-74 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_no_nono1 noloop
    mc "That's cool Kanya, but we'll shoot the scene in our studio."
    mc "But I appreciate the thought."
    scene sm1ms008-75 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_yes_yep2 noloop
    kv "You got it, [mcname]."
    play sound sfx_door_closed7 volume 1.6
    scene sm1ms008-a76-01 red_wig_acquired_sy_walks_back-glambot-76-01-00_i with fade
    pause
    play sound2 sfx_heels_steps2 loop volume 1.6
    play sound3 sfx_camera_fly1 volume 2.0 noloop
    play sound4 ["<silence 1.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1ms008-glambot-1
    pause
    stop sound3 fadeout 1.0
    stop sound4 fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms008-77 red_wig_acquired_sy_talks_flourish with dissolve
    play voice3 stacy_surprised_huh5 noloop
    sy "So, how do I look?"
    scene sm1ms008-78 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_surprised_wow noloop
    kv "Great, Stacy. It looks solid. Let me grab my camera."
    play sound sfx_cloth_rustling1
    scene sm1ms008-79 red_wig_acquired_sy_talk_camera_pose with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "What do you think, [mcname]?"
    menu:
        "You should stick with red hair."(hint="sm1ms008_m01_h01"):
            call sm1ms008_m01_c01 from _call_sm1ms008_m01_c01
            scene sm1ms008-80 red_wig_acquired_mc_talk_menu with dissolve
            play voice2 mc_surprised_wow3 noloop
            mc "Wow. Very sexy and fiery. You might have to stick with red hair for a bit."
            play sound3 sfx_camera_fly1 volume 2.7 noloop
            scene sm1ms008-glambot-2 with dissolve
            pause
            play voice3 stacy_arrogant_huh1 noloop
            sy "Really? It's that hot?"
            stop sound3 fadeout 1.0
            scene sm1ms008-82 red_wig_acquired_mc_talk_menu with dissolve
            play voice2 mc_yes_yes5 noloop
            mc "You might even say 'red-hot'."
            scene sm1ms008-83 red_wig_acquired_sy_talk_menu_sexy_pose with dissolve
            play voice3 stacy_happy_hmm1 noloop
            sy "Hahaha. Hmmm."
        "I think it will do nicely for the scene."(hint="sm1ms008_m01_h02"):
            call sm1ms008_m01_c02 from _call_sm1ms008_m01_c02
            scene sm1ms008-84 red_wig_acquired_mc_talk_menu_nicely with dissolve
            play voice2 d9s2_yeah noloop volume 2.5
            mc "It looks great, Stacy. I think it will fit perfectly for the scene."
            scene sm1ms008-85 red_wig_acquired_sy_talk_menu_nicely_playhair with dissolve
            play voice3 stacy_arrogant_huh1 noloop
            sy "Good. But that's it? Just for the scene?"
            scene sm1ms008-86 red_wig_acquired_mc_talk_menu_nicely_shrug with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "What do you think?"
            scene sm1ms008-87 red_wig_acquired_sy_talk_menu_nicely_shrug with dissolve
            play voice3 stacy_disappointed_mmm2 noloop
            sy "I don't know. Maybe once I see it in action, I'll have a better feel for it."
            play voice2 mc_yes_ugu1 noloop
            mc "Mmhmm."
        "I'm glad it's temporary":
            call sm1ms008_m01_c03 from _call_sm1ms008_m01_c03
            scene sm1ms008-89 red_wig_acquired_mc_talk_menu_temporary_reassuring with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "I'm glad it's just for a scene."
            scene sm1ms008-88 red_wig_acquired_sy_talk_menu_likewhat with dissolve
            play voice3 stacy_surprised_huh1 noloop
            sy "What? It's that bad?"
            scene sm1ms008-86 red_wig_acquired_mc_talk_menu_nicely_shrug with dissolve
            play voice2 mc_no_no6 noloop
            mc "It's not bad."
            mc "I just like you with your green hair."
            scene sm1ms008-90 red_wig_acquired_sy_talk_menu_temporary_smile with dissolve
            play voice3 stacy_happy_hmm1 noloop
            pause
    jump sm1ms008_after_choice
label sm1ms008_after_choice:
    scene sm1ms008-91 red_wig_acquired_kv_talk_camera_ready with dissolve
    play voice4 kanya_hey_arrogant noloop
    kv "Already Stacy, why don't you give me some poses."
    scene sm1ms008-92 red_wig_acquired_sy_talk_camera_ready with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "Poses?"
    scene sm1ms008-93 red_wig_acquired_kv_talk_camera with dissolve
    play voice4 kanya_yes_yeah1 noloop
    kv "Yeah, just move around. We're doing like a stress test for the wig."
    scene sm1ms008-94 red_wig_acquired_mc_talk_grinning with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I know how we could do a proper stress test."
    scene sm1ms008-95 red_wig_acquired_sy_talk_wink with dissolve
    play voice3 stacy_angry noloop
    sy "Keep it your pants, Mister. I'm a classy redheaded lady, today."
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    scene sm1ms008-96 red_wig_acquired_pose montage with dissolve
    play sound sfx_photocamera_flash2
    $ renpy.music.set_volume(0.2, 3.0, "music2" )
    pause
    scene sm1ms008-97 red_wig_acquired_pose montage with dissolve
    play sound sfx_photocamera_flash2
    pause
    scene sm1ms008-98 red_wig_acquired_pose montage with dissolve
    play sound sfx_photocamera_flash2
    pause
    scene sm1ms008-99 red_wig_acquired_pose montage with dissolve
    play sound sfx_photocamera_flash2
    pause
    scene sm1ms008-100 red_wig_acquired_pose montage with dissolve
    play sound sfx_photocamera_flash2
    pause
    $ renpy.music.set_volume(0.55, 3.0, "music2" )
    scene sm1ms008-101 red_wig_acquired_kv_talk_lowercamera with dissolve
    $ renpy.music.set_volume(0.0, 3.0, "music" )
    play voice4 kanya_happy_relief1 noloop
    kv "And done. Should be more than enough to see if there are any issues."
    scene sm1ms008-102 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Looks good to me."
    scene sm1ms008-103 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_yes_yep1 noloop
    kv "Yup. Very promising so far."
    play sound sfx_cloth_rustling5
    scene sm1ms008-104 red_wig_acquired_kv_cameradown with dissolve
    pause
    scene sm1ms008-105 red_wig_acquired_kv_clap with dissolve
    play voice4 kanya_thinking_hmm4 noloop
    kv "Okay, so we will work on the scene details once we set up a rehearsal time."
    kv "I think the only thing left before we can start rehearsing and filming is getting our hands on the right camera."
    scene sm1ms008-106 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, don't you have any camera we would ever need, Kanya?"
    scene sm1ms008-107 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_disappointed_ohh noloop
    kv "Oh I've got tons of cameras, just not the kind we need for a scene like this."
    kv "Most of my cameras are for photos. For something like this we're going to want to get a video camera."
    kv "The Soh-Ni Venus would probably be great."
    scene sm1ms008-105 red_wig_acquired_kv_clap with dissolve
    play voice4 kanya_thinking_eeh3 noloop
    kv "Dual native ISO, with their top-of-the-line sensor, comes out in a raw format that's pretty manageable."
    kv "Plus they use the E mounts, which are what all my lenses are, so we can use what I've already got."
    kv "Does low light well... Real versatile camera that's not that expensive."
    play sound sfx_cloth_rustling1
    scene sm1ms008-108 red_wig_acquired_sy_talk_phone with dissolve
    play voice3 stacy_mmm1 noloop
    sy "What about using my phone? It has a good camera, right?"
    scene sm1ms008-109 red_wig_acquired_kv_talk_amused with dissolve
    play voice4 kanya_no_nah1 noloop
    kv "Come on, Stacy. You don't want us to look like some amateurs, do you? Your client will be very impressed if we go the extra mile."
    play voice3 stacy_disappointed_ehh2 noloop
    sy "I don't know..."
    scene sm1ms008-110 red_wig_acquired_kv_talk_turn_mc with dissolve
    play voice4 kanya_hey_simple1 noloop
    kv "You two need to think of this as an investment in the studio's future."
    scene sm1ms008-111 red_wig_acquired_sy_talk_chimen with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "I'm thinking about the extra work you'll have to do to get this super camera."
    scene sm1ms008-112 red_wig_acquired_kv_talk_turn_sy with dissolve
    play voice4 kanya_no_nonono1 noloop
    kv "I wouldn't bring it up if it weren't worth it, Stacy. Trust me."
    scene sm1ms008-113 red_wig_acquired_sy_look_mc with dissolve
    pause
    scene sm1ms008-114 red_wig_acquired_mc_thinking with dissolve
    play voice2 mc_thinking_mmm4 noloop volume 1.4
    pause
    scene sm1ms008-115 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_yes_okay3 noloop volume 1.5
    mc "Alright, you convinced me. Let's get this super camera."
    scene sm1ms008-116 red_wig_acquired_sy_talk_nod with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "If it's going to make a difference, then I'm in. Let's make this project the best it can be."
    scene sm1ms008-117 red_wig_acquired_kv_talk_smiles with dissolve
    play voice4 kanya_happy_woohoo noloop
    kv "Great! I'll text you the exact model and specifications. There are many cameras like it, but this one is top tier."
    scene sm1ms008-118 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "If you insist."
    scene sm1ms008-119 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_yes_simple noloop
    kv "I certainly do, [mcname]."
    kv "If you can't do something right, don't do it at all."
    scene sm1ms008-120 red_wig_acquired_sy_talk_chuckle with dissolve
    play voice3 stacy_laugh2 noloop
    sy "Haha. Good thing that's not, [mcname]'s motto."
    scene sm1ms008-121 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "Hey."
    scene sm1ms008-122 red_wig_acquired_mc_thought_syamused with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "I'll have to get back at her later."
    scene sm1ms008-123 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Alright, looks like we've got an update to our plan."
    scene sm1ms008-124 red_wig_acquired_sy_talk with dissolve
    play voice3 stacy_yes_fine3 noloop
    sy "I'll find the camera online, maybe we'll get lucky and get a deal."
    sy "Once we have it, we'll give you a call to set up a time for filming."
    scene sm1ms008-125 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_yes_yeah2 noloop
    kv "Got it, let me give you my number. In case you need to call me."
    play sound sfx_cloth_rustling2
    scene sm1ms008-126 red_wig_acquired_sy_talk_hand_phone with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Sure."
    play sound sfx_phone_tapping1 volume 2.3 loop
    scene sm1ms008-127 red_wig_acquired_svnput_number with dissolve
    pause
    play sound sfx_cloth_rustling3
    scene sm1ms008-128 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_disappointed_hm noloop
    kv "Good. All set."
    scene sm1ms008-129 red_wig_acquired_mc_talk_arms_crossed with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "With any luck, we'll be ready to film in a week."
    scene sm1ms008-130 red_wig_acquired_sy_talk_cheer with dissolve
    play voice3 stacy_happy_wooh1 noloop
    sy "Woohoo! It's almost here!"
    scene sm1ms008-131 red_wig_acquired_kv_talk with dissolve
    play voice4 kanya_disappointed_oof noloop
    kv "I for one, am very excited for our first wrap party."
    scene sm1ms008-132 red_wig_acquired_mc_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Alright, we'll get out of your hair for now. But hope to see you soon."
    scene sm1ms008-133 red_wig_acquired_kv_talk_winks with dissolve
    play voice4 kanya_happy_laugh2 noloop
    kv "You know I don't mind you messing around with my hair, [mcname]."
    scene sm1ms008-134 red_wig_acquired_mc_talk_motions with dissolve
    play voice2 mc_thinking_hm noloop
    pause
    scene sm1ms008-135 red_wig_acquired_kv_talk_waves with dissolve
    play voice4 kanya_hey_long noloop
    kv "Nice to meet you, Stacy."
    scene sm1ms008-136 red_wig_acquired_sy_talk_waves with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Yeah, you too. We'll be in touch as soon as we get the camera."
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 4.0, "music" )
    $ renpy.music.set_volume(1.0, 4.0, "music2" )
    scene black with fade
    jump sm1ms008_end
label sm1ms008_end:
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(MS, 4, 0, 2)
    return
label sm1ms008_m01_c01:
    $ player.set_choice("sm1ms008_love_red_hair")
    return
label sm1ms008_m01_c02:
    $ player.set_choice("sm1ms008_like_red_hair")
    return
label sm1ms008_m01_c03:
    $ player.set_choice("sm1ms008_hate_red_hair")
    return
label sm1ms008_unlocks:
    call sm1ms008_m01_c01 from _call_sm1ms008_m01_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MS)
    return