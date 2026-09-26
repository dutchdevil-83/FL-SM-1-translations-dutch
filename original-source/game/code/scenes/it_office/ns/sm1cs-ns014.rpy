image sm1cs-ns014-a17-glam = Movie(play = "images/FS_IT/NS/s014/anim/sm1cs-ns014-a17-3x-60fps.webm", start_image = "sm1cs-ns014-a17 mc-nari-glambot-000", image = "sm1cs-ns014-a17 mc-nari-glambot-119", loop = False)
label sm1cs_ns014:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.8, 3.0, "music" )
    scene black
    show screen scene_transistion(_("Near the end of your shift"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play music music_chilled_fun
    play sound4 sfx_office_ambience1 fadein 1.0
    play sound2 sfx_heels_steps2 noloop
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1cs-ns014-01 mc-nari-office1_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-ns014-01 mc-nari-office1_c2 with dissolve
    play voice3 nari_hey_asking noloop
    ns "Hey [mcname], you still here?"
    scene sm1cs-ns014-02 mc-nari-office2_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, still wrestling with these last few tickets."
    if True:
        mc "It feels like we have been buried in work since we got hacked."
        mc "Kind of making me fall out of love with this."
        scene sm1cs-ns014-02 mc-nari-office2_c2 with dissolve
        play voice3 nari_arrogant_hm noloop
        ns "It's going to be okay. We just have to keep at it, and eventually will be better."
        scene sm1cs-ns014-03 mc-nari-smile_c1 with dissolve
        play voice2 mc_arrogant_hm3 noloop
        mc "No dark clouds for you, eh Nari?"
        scene sm1cs-ns014-03 mc-nari-smile_c2 with dissolve
        play voice3 nari_disappointed_huh noloop
        ns "After meeting you, my life has been a net positive."
        play sound sfx_hair_scratch1
        scene sm1cs-ns014-04 mc-nari-smile2_c1 with dissolve
        play voice2 mc_arrogant_heh3 noloop
        mc "Thanks."
    else:
        scene sm1cs-ns014-03 mc-nari-smile_c2 with dissolve
        play voice3 nari_disappointed_oh noloop
        ns "Still? I already finished all of mine."
        play sound sfx_hair_scratch1
        scene sm1cs-ns014-04 mc-nari-smile2_c1 with dissolve
        play voice2 mc_arrogant_heh3 noloop
        mc "Look at you."
        scene sm1cs-ns014-04 mc-nari-smile2_c2 with dissolve
        play voice3 nari_happy_laugh1 noloop
        ns "Hehe. Aren't you already looking at me?"
        scene sm1cs-ns014-05 mc-nari-look_c1 with dissolve
        play voice2 mc_yes_yes1 noloop
        mc "Always."
        scene sm1cs-ns014-06 mc-nari-close_c2 with dissolve
        play voice3 nari_happy_laugh2 noloop
        ns "*giggling* I hope I'm not too distracting."
    scene sm1cs-ns014-05 mc-nari-look_c2 with dissolve
    play voice3 nari_disappointed_eeh noloop
    ns "I wish you were already done with your work, [mcname]."
    ns "I was hoping you were finished and then we could walk home together."
    play sound sfx_cloth_rustling1
    scene sm1cs-ns014-04 mc-nari-smile2_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Ah, that's sweet."
    mc "How did you finish yours so fast, Nari?"
    scene sm1cs-ns014-06 mc-nari-close_c2 with dissolve
    play voice3 nari_disappointed_eh noloop
    ns "There {b}were{/b} a lot of tickets."
    ns "But you know me, once I finish one, I just keep powering through until they're all gone."
    play sound sfx_comic_woopwoop1
    scene sm1cs-ns014-07 mc-nari-close2_c2 with dissolve
    pause
    play sound sfx_comic_woopwoop2
    scene sm1cs-ns014-07 mc-nari-close2_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What are you doing?"
    play voice3 nari_thinking_emm noloop
    ns "Making sure no one is watching."
    play sound2 sfx_cloth_rustling4 noloop volume 1.4
    scene sm1cs-ns014-08 mc-nari-kiss_c2 with dissolve
    play voice3 nari_sex_closedmoan3 noloop
    play voice2 mc_surprised_huh4 noloop
    play sound mc_kiss2
    pause
    scene sm1cs-ns014-08 mc-nari-kiss_c1 with dissolve
    play sound mc_kiss3
    play voice3 nari_sex_closedmoan2 noloop
    ns "Mwah."
    scene sm1cs-ns014-09 mc-nari-look_c2 with dissolve
    play voice3 nari_thinking_hm noloop
    ns "That should give you some more pep."
    menu:
        "Make powering up noise":
            $ player.set_choice("sm1cs_ns014_power_up_noise")
            scene sm1cs-ns014-09 mc-nari-look_c1 with dissolve
            play voice2 mc_thinking_mmm7 noloop
            pause
        "I might need more than that later":
            scene sm1cs-ns014-10 mc-nari-look2_c1 with dissolve
            play voice2 mc_arrogant_hm3 noloop
            mc "I might need more where that comes from."
            scene sm1cs-ns014-11 mc-nari-talk_c2 with dissolve
            play voice3 nari_no_nah noloop
            ns "[mcname]... we're supposed to behave around work."
            ns "But maybe we can do something later."
            ns "In my room."
    scene sm1cs-ns014-12 mc-nari-talk2_c2 with dissolve
    play voice3 nari_thinking_hmm3 noloop
    ns "Keep working hard and it will be done before you know it, [mcname]."
    ns "Unless you want me to stay and help you code?"
    ns "Cause I can do that."
    scene sm1cs-ns014-13 mc-nari-talk3_c1 with dissolve
    play voice2 mc_no_no1 noloop
    mc "No way, Nari. You've already done all the work you needed to do."
    mc "I got to carry my own weight."
    play sound sfx_hair_scratch1
    scene sm1cs-ns014-13 mc-nari-talk3_c2 with dissolve
    play voice3 nari_surprised_ehh noloop
    ns "Oh."
    ns "What does carrying weights have to do with me helping you?"
    scene sm1cs-ns014-14 mc-nari-talk4_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.4
    mc "Haha."
    mc "I'll see you at home, cutie."
    play sound sfx_heels_steps2
    scene sm1cs-ns014-14 mc-nari-talk4_c2 with dissolve
    play voice3 nari_yes_sad noloop
    ns "Until then..."
    mc "..."
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    $ renpy.music.set_volume(1.0, 1.5, "music" )
    stop sound fadeout 1.0
    scene black
    show screen scene_transistion(_("Two hours later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.8, 1.0, "music" )
    $ renpy.music.set_volume(1.0, 1.0, "sound4" )
    play sound sfx_mouse_clicks1
    scene sm1cs-ns014-15 mc-nari-stand_c1
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_thinking_hmm3 noloop
    mct "Time to clock out."
    stop sound fadeout 1.5
    jump sm1cs_ns014_studio
label sm1cs_ns014_studio:
    stop sound4 fadeout 2.5
    stop music fadeout 4.5
    queue sound sfx_door_open1
    play sound2 sfx_heels_steps1 fadein 1.5
    scene sm1cs-ns014-16 mc-nari-walk_c1 with Fade(0.5, 0.5, 0.5)
    play voice2 mc_hey_hey5 noloop
    mc "I'm home."
    stop sound2 fadeout 1.0
    scene sm1cs-ns014-16 mc-nari-walk_c2 with dissolve
    mc "..."
    play sound sfx_photocamera_flash2
    "Click"
    scene sm1cs-ns014-17 mc-nari-walk2_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mct "What was that?"
    play sound4 sfx_light_podium_1 noloop volume 0.6
    play music music_photo_velvet fadein 0.2
    scene sm1cs-ns014-a17 mc-nari-glambot-000 with dissolve
    pause 0.1
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    play sound3 ["<silence 4.5>", sfx_photocamera_flash1] noloop
    scene sm1cs-ns014-a17-glam
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    play sound sfx_heels_steps1
    scene sm1cs-ns014-19 mc-nari-wave_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mct "There they are."
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.6, 6.0, "music" )
    scene sm1cs-ns014-19 mc-nari-wave_c3 with dissolve
    play voice4 stacy_hey_happy1 noloop
    sy "Welcome home, superstar."
    scene sm1cs-ns014-20 mc-nari-ask_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Hey."
    mc "What's goin on here?"
    scene sm1cs-ns014-20 mc-nari-ask_c2 with dissolve
    play voice3 nari_happy_yay noloop
    ns "Surprise! Stacy was taking naughty pictures of me."
    scene sm1cs-ns014-21 mc-nari-point_c2 with dissolve
    play voice4 stacy_happy_hmm1 noloop
    sy "With you, Nari. I'm taking naughty pictures with you."
    play voice3 nari_happy_laugh3 noloop
    ns "*giggles* Sorry. Yes. {i}With{/i} me."
    scene sm1cs-ns014-23 mc-nari-talk_c1 with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "How did this get started?"
    scene sm1cs-ns014-21 mc-nari-point_c2 with dissolve
    play voice4 stacy_thinking_well1 noloop
    sy "Well, Nari saw me checking out the equipment. And she asked me what it was for."
    scene sm1cs-ns014-22 mc-nari-close_c2 with dissolve
    play voice4 stacy_laugh4 noloop
    sy "Since I didn't know how to answer that loaded question, I asked her if she wanted to take some sexy photos for you."
    sy "Because you've been working so hard."
    scene sm1cs-ns014-23 mc-nari-talk_c1 with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "Right."
    mc "Good thinking."
    scene sm1cs-ns014-24 mc-nari-talk2_c2 with dissolve
    play voice3 nari_disappointed_huh noloop
    ns "Were you surprised, [mcname]."
    scene sm1cs-ns014-24 mc-nari-talk2_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "You could say that."
    scene sm1cs-ns014-24 mc-nari-talk2_c2 with dissolve
    play voice3 nari_hey_unsure noloop
    ns "I wanted to make something nice for you because you let me stay here."
    ns "And I knew you'd be working hard to get out of Orbix today."
    menu:
        "I love it":
            play voice2 mc_happy_yay1 noloop
            mc "I love it. It's a really nice idea, Nari."
        "Maybe I can surprise you later":
            $ player.set_choice("sm1cs_ns014_surprise_later")
            play voice2 mc_thinking_hmm8 noloop
            mc "I'm thinking I'll have to make a surprise for you later."
            play voice3 nari_disgust_oogh noloop
            ns "Ooooh. I like the sound of that."
    play sound sfx_cloth_rustling1 volume 1.6
    scene sm1cs-ns014-26 mc-nari-phone2_c1 with dissolve
    play voice4 stacy_disappointed_mmm1 noloop
    sy "Here, you take over, [mcname].{w} You can be the director for a little."
    scene sm1cs-ns014-30 mc-nari-montage_c1 with dissolve
    play voice4 stacy_arrogant_ha1 noloop
    sy "Now. How would you like to see us?"
    scene sm1cs-ns014-27 mc-nari-talk_c2 with dissolve
    play voice3 nari_arrogant_yeah noloop
    ns "I think I know the answer to that question."
    ns "Naked."
    scene sm1cs-ns014-29 mc-nari-close_c1 with dissolve
    play voice4 stacy_arrogant_huh3 noloop
    sy "Well obviously. But for now, we're going to keep our lingerie on, Nari."
    sy "Leave him something to look forward to."
    sy "Build up...{w} the anticipation."
    scene sm1cs-ns014-29 mc-nari-close_c2 with dissolve
    play voice3 nari_disappointed_oh noloop
    ns "Oooh. I {b}like{/b} that idea too!"
    scene sm1cs-ns014-30 mc-nari-montage_c2 with dissolve
    menu:
        "Ask for cute poses":
            $ player.set_choice("sm1cs_ns014_cute_poses")
            $ renpy.music.set_volume(1.0, 3.0, "music" )
            scene sm1cs-ns014-31 mc-nari-montage2_c1 with dissolve
            pause
            scene sm1cs-ns014-31 mc-nari-montage2_c2 with dissolve
            pause
            scene sm1cs-ns014-32 mc-nari-montage3_c1 with dissolve
            pause
            scene sm1cs-ns014-32 mc-nari-montage3_c2 with dissolve
            pause
            scene sm1cs-ns014-35 mc-nari-montage6_c2 with dissolve
            pause
        "Ask for naughty poses":
            $ renpy.music.set_volume(1.0, 3.0, "music" )
            scene sm1cs-ns014-33 mc-nari-montage4_c1 with dissolve
            pause
            scene sm1cs-ns014-33 mc-nari-montage4_c2 with dissolve
            pause
            scene sm1cs-ns014-34 mc-nari-montage5_c2 with dissolve
            pause
            scene sm1cs-ns014-35 mc-nari-montage6_c1 with dissolve
            pause
            scene sm1cs-ns014-35 mc-nari-montage6_c2 with dissolve
            pause
    $ renpy.music.set_volume(0.6, 2.0, "music" )
    scene sm1cs-ns014-36 mc-nari-look_c1 with dissolve
    play voice4 stacy_scared_oof3 noloop
    sy "Oooh! Stay right there. I just had a wonderful idea."
    play sound sfx_barefoot_run1
    scene sm1cs-ns014-37 mc-nari-talk_c1 with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "You doing okay?"
    scene sm1cs-ns014-37 mc-nari-talk_c2 with dissolve
    play voice3 nari_yes_aga1 noloop
    ns "Of course. I love looking sexy for you."
    stop sound fadeout 3.0
    scene sm1cs-ns014-38 mc-nari-talk2_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah but, you don't have to just keep doing this for me."
    scene sm1cs-ns014-38 mc-nari-talk2_c2 with dissolve
    play voice3 nari_happy_mmm noloop
    ns "I know silly. It's also... quite liberating."
    play sound sfx_hair_scratch1
    scene sm1cs-ns014-39 mc-nari-talk3_c2 with dissolve
    play voice3 nari_thinking_hm noloop
    ns "I enjoy Orbix, but it means I have to spend a large share of my day wearing boring office clothes."
    ns "I mean, imagine how much fun I'd have at work if I could wear this?"
    scene sm1cs-ns014-39 mc-nari-talk3_c1 with dissolve
    menu:
        "I don't think I'd get any work done":
            $ player.set_choice("sm1cs_ns014_no_work_done")
            play voice2 mc_happy_hah2 noloop
            mc "I know {b}someone{/b} who wouldn't get any work done at all."
            scene sm1cs-ns014-40 mc-nari-talk4_c2 with dissolve
            play voice3 nari_disgust_ergh noloop
            ns "Ooooh. I like thinking of distracting you."
            ns "Making you so hard you couldn't work."
            play sound sfx_cloth_rustling2 volume 2.0
            scene sm1cs-ns014-41 mc-nari-close_c1 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "I like it too."
        "Anna might have a problem":
            play voice2 mc_thinking_hmm2 noloop
            mc "I'm not sure Anna would approve."
            scene sm1cs-ns014-40 mc-nari-talk4_c2 with dissolve
            play voice3 nari_happy_laugh5 noloop
            ns "Haha. Yes. But it would be worth it if I left April speechless."
            ns "*giggles*"
    play voice4 stacy_arrogant_huh1 noloop
    sy "I'm back."
    scene sm1cs-ns014-42 mc-nari-montage_c1 with fade
    play sound sfx_pillow_fight1 loop
    play voice3 nari_happy_wooh noloop
    pause
    scene sm1cs-ns014-42 mc-nari-montage_c2 with dissolve
    play voice4 stacy_angry noloop
    pause
    play sound2 sfx_epic_jump1 noloop
    scene sm1cs-ns014-43 mc-nari-montage2_c1 with dissolve
    play voice3 nari_scared_ah4 noloop
    pause
    scene sm1cs-ns014-43 mc-nari-montage2_c2 with dissolve
    play voice4 stacy_scared_ah4 noloop
    pause
    scene sm1cs-ns014-44 mc-nari-montage3_c1 with dissolve
    play voice3 nari_happy_laugh4 noloop
    pause
    scene sm1cs-ns014-44 mc-nari-montage3_c2 with dissolve
    pause
    play sound sfx_skirt_off2 volume 1.7
    scene sm1cs-ns014-45 mc-nari-top_c1 with dissolve
    play voice4 stacy_arrogant_laugh1 noloop
    sy "Mu-ha-hah."
    sy "You may have won, but I have your top."
    scene sm1cs-ns014-45 mc-nari-top_c2 with dissolve
    play sound sfx_phonecamera_flash1
    "CLICK"
    play voice3 nari_scared_ah1 noloop
    play sound sfx_cloth_planket3
    scene sm1cs-ns014-46 mc-nari-top2_c1 with hpunch
    ns "No fair. You're too sneaky. Stacy.."
    scene sm1cs-ns014-46 mc-nari-top2_c2 with dissolve
    play voice4 stacy_happy_laugh4 noloop
    sy "Hehehe."
    scene sm1cs-ns014-47 mc-nari-top3_c1 with dissolve
    play sound sfx_phonecamera_flash1
    "CLICK."
    scene sm1cs-ns014-47 mc-nari-top3_c2 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "I think that's the perfect end to a pillow fight."
    mct "Or the perfect beginning."
    mct "Nari really is good in front of the camera."
    mct "I guess it's finally time for me to pop the question."
    mct "She's living here after all."
    mct "She is very open-minded but she's bound to ask questions if she comes down for breakfast and there is a full porn movie production in her home."
    scene sm1cs-ns014-48 mc-nari-talk_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "You’re a natural, Nari."
    scene sm1cs-ns014-48 mc-nari-talk_c2 with dissolve
    play voice3 nari_happy_laugh3 noloop
    ns "Heehee, stop it. I’m shy!"
    scene sm1cs-ns014-49 mc-nari-talk2_c1 with dissolve
    play voice4 stacy_no_uhuh1 noloop
    sy "Lies! You’re eating this up."
    scene sm1cs-ns014-49 mc-nari-talk2_c3 with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "The camera loves you."
    scene sm1cs-ns014-50 mc-nari-talk3_c1 with dissolve
    play voice4 stacy_arrogant_ha2 noloop
    sy "And the cameraman wants to fuck you."
    scene sm1cs-ns014-50 mc-nari-talk3_c3 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Stacy?"
    scene sm1cs-ns014-50 mc-nari-talk3_c2 with dissolve
    play voice3 nari_happy_laugh6 noloop
    ns "*giggles*"
    play sound sfx_cloth_planket2
    play sound2 sfx_barefoot_steps1
    scene sm1cs-ns014-51 mc-nari-talk4_c1 with dissolve
    play voice4 stacy_thinking_hmm1 noloop
    sy "I'll put these back."
    sy "And leave you to to..."
    sy "Discuss..."
    scene sm1cs-ns014-51 mc-nari-talk4_c2 with dissolve
    play voice3 nari_surprised_huh2 noloop
    ns "Discuss? Discuss what?"
    play sound sfx_heels_steps1 loop
    scene sm1cs-ns014-52 mc-nari-walk_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "I'm going to grab a glass of water."
    mc "Would you like one."
    scene sm1cs-ns014-52 mc-nari-walk_c2 with dissolve
    play voice3 nari_thinking_mff noloop
    ns "Sure."
    play sound sfx_bed_slide3
    stop sound2 fadeout 1.0
    scene sm1cs-ns014-53 mc-nari-glass_c2 with dissolve
    play voice3 nari_arrogant_huh noloop
    ns "Is everything alright? You look like you're not feeling well?"
    scene sm1cs-ns014-53 mc-nari-glass_c1 with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "I'm fine. Well, I'm sure I'll feel better in a moment."
    play sound sfx_cloth_rustling3
    scene sm1cs-ns014-54 mc-nari-talk_c2 with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Okay..."
    scene sm1cs-ns014-54 mc-nari-talk_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Nari, you know that I care deeply about you. And would never want to hurt you."
    mc "Or lie to you."
    scene sm1cs-ns014-55 mc-nari-talk2_c2 with dissolve
    play voice3 nari_yes_confident noloop
    ns "Of course."
    scene sm1cs-ns014-55 mc-nari-talk2_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well, there is a problem. Something I've been keeping from you."
    mc "Something I should have said earlier."
    play sound sfx_drink_loop1 loop volume 1.6
    scene sm1cs-ns014-56 mc-nari-talk3_c2 with dissolve
    play voice3 nari_arrogant_hm noloop
    ns "Well... then it's good you're telling me now."
    ns "What is it, [mcname]?"
    scene sm1cs-ns014-56 mc-nari-talk3_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "The whole purpose of Stacy and I having a home like this. Is to make movies."
    mc "Well. To make adult movies, to be specific."
    scene sm1cs-ns014-56 mc-nari-talk3_c3 with dissolve
    play voice3 nari_thinking_hmm1 noloop
    ns "Wait—like... porn movies? You're saying that you are going to film porn here?"
    play sound sfx_cup_slide1 volume 1.6
    scene sm1cs-ns014-57 mc-nari-talk4_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah. I should’ve told you sooner."
    scene sm1cs-ns014-57 mc-nari-talk4_c2 with dissolve
    play voice3 nari_surprised_ohmy noloop
    ns "Oh my god!"
    ns "That’s so wild, [mcname]. So all this camera gear is for... wow."
    ns "All of the decorations make a lot more sense now."
    scene sm1cs-ns014-58 mc-nari-talk5_c1 with dissolve
    play voice2 d9s2_mcyes2 noloop volume 2.5
    mc "I’m sorry for keeping it from you. Can you forgive me?"
    scene sm1cs-ns014-58 mc-nari-talk5_c2 with dissolve
    play voice3 nari_happy_yeah noloop
    ns "Of course!"
    ns "I mean, I can tell that this wasn't an easy thing for you."
    ns "It feels like you've worked hard to follow this path. Like it's a dream you want to turn into reality."
    scene sm1cs-ns014-60 mc-nari-talk7_c1 with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "It is."
    scene sm1cs-ns014-60 mc-nari-talk7_c2 with dissolve
    play voice3 nari_yes_aga2 noloop
    ns "Then I understand, [mcname]. And I accept your apology."
    ns "It's totally fine with me that you wanted to make sure you could trust me before sharing something so private."
    menu:
        "That is part of it":
            scene sm1cs-ns014-58 mc-nari-talk5_c1 with dissolve
            play voice2 mc_arrogant_hm1 noloop
            mc "That was definitely part of it. I'm not sure how people tell their friends and family that they're on sites like Fansly or OnlyFans."
            mc "But I'm sure they have to gauge if they think the person can keep a secret."
            scene sm1cs-ns014-58 mc-nari-talk5_c2 with dissolve
            play voice3 nari_disappointed_woof noloop
            ns "And you believe that I can keep this a secret."
            scene sm1cs-ns014-60 mc-nari-talk7_c1 with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "Yes, I do. I know you're a hard worker, and that you won't just blurt this out."
            mc "But apart from all that, I know how kinky you are."
            scene sm1cs-ns014-60 mc-nari-talk7_c2 with dissolve
            play voice3 nari_happy_laugh1 noloop
            ns "Hehehe. Thank you, [mcname]."
            play voice2 mc_thinking_hm noloop
            mc "But I didn't know if that would mean accept that I am doing this as well as working for Orbix."
        "I trust you":
            $ player.set_choice("sm1cs_ns014_trust_ns")
            scene sm1cs-ns014-58 mc-nari-talk5_c1 with dissolve
            play voice2 mc_no_no2 noloop
            mc "Not at all. I trust you, Nari. I had no issue thinking that I could share this secret with you and you would keep it between us."
            play voice3 nari_happy_relief noloop
            ns "Thank you. That means a lot to me."
            mc "No, I held off... well... because I know how kinky you are."
            scene sm1cs-ns014-58 mc-nari-talk5_c2 with dissolve
            play voice3 nari_thinking_emm noloop
            ns "I don't understand."
            scene sm1cs-ns014-60 mc-nari-talk7_c1 with dissolve
            play voice2 d1s5_mcthinks noloop volume 1.6
            mc "Just because someone is good at baseball, doesn't mean they want to watch it all the time."
            mc "I didn't know how you'd react to find out that I make porn on the side."
            scene sm1cs-ns014-60 mc-nari-talk7_c2 with dissolve
            play voice3 nari_thinking_hmm1 noloop
            ns "Ah... that's what you were worried about."
            ns "But you didn't need to be, [mcname]."
    scene sm1cs-ns014-61 mc-nari-talk8_c2 with dissolve
    play voice3 nari_hey_asking noloop
    ns "I think it's amazing."
    scene sm1cs-ns014-61 mc-nari-talk8_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "You do?"
    play sound sfx_barefoot_steps1 loop volume 2.0
    scene sm1cs-ns014-62 mc-nari-talk9_c2 with dissolve
    play voice3 nari_yes_yep noloop
    ns "Yes. This also explains why your productivity is so below the curve of April and I."
    ns "I was starting to worry that you were just lazy. But now I see that you have a whole other job you do."
    stop sound fadeout 1.0
    scene sm1cs-ns014-62 mc-nari-talk9_c3 with dissolve
    play voice4 stacy_happy_laugh3 noloop
    sy "Hahahaha."
    sy "The look on your face."
    if persistent.is_special:
        sy "My lazy brother. Good thing you're sexy and handsome too."
    else:
        sy "Haha. My lazy boyfriend. Good thing you're sexy and handsome too."
    scene sm1cs-ns014-63 mc-nari-talk10_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Hardy har har."
    scene sm1cs-ns014-63 mc-nari-talk10_c2 with dissolve
    play voice3 nari_disgust_brrgh noloop
    ns "I'm sorry, [mcname]. That came out wrong."
    scene sm1cs-ns014-64 mc-nari-talk11_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Nuh nuh. Cat's out of the bag now, Nari."
    play sound sfx_hair_scratch1
    scene sm1cs-ns014-65 mc-nari-talk12_c2 with dissolve
    play voice3 nari_surprised_ah noloop
    ns "Hmmm. What cat?"
    play voice2 mc_thinking_mmm6 noloop
    mc "Nevermind."
    scene sm1cs-ns014-65 mc-nari-talk12_c3 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Phew. Well I'm glad that everything is out there in the open."
    scene sm1cs-ns014-64 mc-nari-talk11_c2 with dissolve
    play voice3 nari_yes_emotional noloop
    ns "Me too, [mcname]."
    ns "Couples shouldn't keep secrets from each other."
    scene sm1cs-ns014-64 mc-nari-talk11_c1 with dissolve
    play voice2 mc_yes_yes5 noloop
    mc "I agree."
    play sound sfx_bed_slide2
    play sound2 sfx_barefoot_steps1 volume 2.0
    scene sm1cs-ns014-66 mc-nari-stand_c2 with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Now, I do have some questions."
    scene sm1cs-ns014-67 mc-nari-stand2_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    stop sound2 fadeout 2.0
    scene sm1cs-ns014-67 mc-nari-stand2_c2 with dissolve
    play voice3 nari_surprised_ehh noloop
    ns "First. Can I help film too?"
    scene sm1cs-ns014-68 mc-nari-talk_c1 with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "Really? You’d want to? As in actually be filmed in scenes with me?"
    scene sm1cs-ns014-68 mc-nari-talk_c2 with dissolve
    play voice3 nari_arrogant_hm noloop
    ns "Why not? You already improve my days with boyfriend girlfriend sex."
    ns "Sex on camera is just a new frontier for me to explore."
    play sound2 sfx_barefoot_steps1 volume 1.5
    scene sm1cs-ns014-69 mc-nari-talk2_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "I'm just surprised you're so gung-ho about it."
    scene sm1cs-ns014-69 mc-nari-talk2_c2 with dissolve
    play voice3 nari_hey_calm noloop
    ns "I am no hoe, [mcname]."
    ns "But part of why I chose America is because a lot of naughty stuff came from here."
    stop sound2 fadeout 1.0
    scene sm1cs-ns014-70 mc-nari-talk3_c2 with dissolve
    play voice3 nari_thinking_mff noloop
    ns "I know that some Korean porn stars have made it big here, so..."
    ns "It would be a bit like a dream coming true."
    scene sm1cs-ns014-70 mc-nari-talk3_c1 with dissolve
    play voice3 nari_surprised_huh2 noloop
    ns "But I do have one reqeust. I will want to keep my face covered for most of my roles."
    ns "Is that alright?"
    scene sm1cs-ns014-71 mc-nari-talk4_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Of course. Whatever you’re comfortable with."
    play sound sfx_throw_something1
    scene sm1cs-ns014-71 mc-nari-talk4_c2 with dissolve
    play voice3 nari_happy_wooh noloop
    ns "Perfect! And... you know..."
    scene sm1cs-ns014-71 mc-nari-talk4_c3 with dissolve
    play voice4 stacy_happy_yay1 noloop
    sy "I’m so excited! We’re gonna have so much fun, Nari."
    play sound sfx_cloth_rustling2
    scene sm1cs-ns014-73 mc-nari-talk6_c2 with dissolve
    play voice3 nari_yes_aga2 noloop
    ns "I'm already looking forward to it, Stacy. And who knows."
    ns "If this company you are making is successful, maybe I can use my share to make another one of my dreams come true."
    scene sm1cs-ns014-73 mc-nari-talk6_c3 with dissolve
    play voice4 stacy_arrogant_huh2 noloop
    sy "What dream is that."
    play voice3 nari_disappointed_eeh noloop
    ns "Apologies. If I tell you, it might not become true."
    sy "Fair enough."
    play sound sfx_cloth_rustling4 volume 2.0
    scene sm1cs-ns014-74 mc-nari-talk7_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Come here."
    scene sm1cs-ns014-74 mc-nari-talk7_c2 with dissolve
    pause
    scene sm1cs-ns014-75 mc-nari-talk8_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I'll do my best to make sure all your dreams come true, Nari."
    scene sm1cs-ns014-75 mc-nari-talk8_c2 with dissolve
    play voice3 nari_sex_closedmoan1 noloop
    ns "[mcname]..."
    scene sm1cs-ns014-76 mc-nari-hug_c2 with dissolve
    play voice4 stacy_disappointed_oh2 noloop
    sy "Awww."
    scene sm1cs-ns014-76 mc-nari-hug_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Come here."
    play sound sfx_cloth_rustling4 volume 1.7
    scene sm1cs-ns014-77 mc-nari-hug2_c2 with dissolve
    play voice4 stacy_mmm1 noloop
    sy "Mmmm. I wasn't feeling left out."
    scene sm1cs-ns014-77 mc-nari-hug2_c1 with dissolve
    play voice3 nari_yes_sad noloop
    ns "I know Stacy."
    ns "But this is like, a team-bonding hug. And all three of us are on a team."
    play voice4 stacy_arrogant_huh1 noloop
    sy "Great thinking, Nari."
    scene sm1cs-ns014-78 mc-nari-talk2_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Alright. To make it official. I just need to have you fill out some paperwork."
    mc "But once that is done, and we have a role for you, it will be great seeing you on camera, Nari."
    scene sm1cs-ns014-78 mc-nari-talk2_c2 with dissolve
    play voice3 nari_happy_yay noloop
    ns "I can't wait. Thanks so much for the opportunity, [mcname]."
    scene sm1cs-ns014-79 mc-nari-thumb_c2 with dissolve
    play voice3 nari_happy_woohoo noloop
    ns "Thumbs up!"
    scene sm1cs-ns014-80 mc-nari-thumb2_c1 with dissolve
    play voice2 mc_happy_yay3 noloop
    mc "Right back at you, cutie."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ StoryController.end_scene(NS_STORY, 4, 0, 3, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return