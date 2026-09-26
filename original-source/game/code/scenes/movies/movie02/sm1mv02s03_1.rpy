image sm1mv02s03-a41-glam = Movie(play = "images/MV/mv02/s03/anim/sm1mv02s03-a41-3x-60fps.webm",  start_image = "sm1mv02s03-a41 set-montage-finish-glambot-000", image = "sm1mv02s03-a41 set-montage-finish-glambot-120", loop = False)
label sm1mv02s03_1:
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.0, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 0.5, "music2" )
    $ renpy.music.play(audio.lofi4, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.lofi4_reverbed, "music2", True, None, True, 0.0)
    scene sm1mv02s03-00 building_the_set_mc_talk_sy_walkin_neutral with Fade(0.5, 0.5, 0.5)
    play sound sfx_door_openclosed1
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    $ renpy.music.set_audio_filter("voice3", renpy.audio.filter.Reverb(0.9))
    scene sm1mv02s03-00 building_the_set_mc_talk_sy_walkin_neutral with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1mv02s03-02 building_the_set_sy_talk_lucy with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Luuuuucy! I'm hoooooome!"
    scene sm1mv02s03-03 building_the_set_sy_talk_confused_mc with dissolve
    $ renpy.music.set_audio_filter("voice3", None)
    play voice3 stacy_arrogant_ha1 noloop
    sy "What, I've always wanted to do that."
    scene sm1mv02s03-04 building_the_set_mc_talk_confused with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course you did."
    play sound2 sfx_heels_steps2
    scene sm1mv02s03-05 building_the_set_kv_talk_walk with dissolve
    play voice4 kanya_hey_simple1 noloop
    kv "Hey, you two."
    kv "I'm guessing you're ready to start your build?"
    stop sound2 fadeout 1.0
    scene sm1mv02s03-06 building_the_set_sy_talk with dissolve
    play voice3 stacy_yes_yap2 noloop
    sy "Yep!"
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene sm1mv02s03-07 building_the_set_walknextroom with dissolve
    pause
    play sound sfx_door_openclosed2 volume 1.5
    scene sm1mv02s03-08 building_the_set_walknextspareroom with dissolve
    play voice4 kanya_yes_aga1 noloop
    kv "Here you go! You two have free reign of the space."
    scene sm1mv02s03-09 building_the_set_sy_talk with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "Awesome!"
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1mv02s03-10 building_the_set_sy_talk_wideshot with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "..."
    sy "So... how do you start building a set?"
    scene sm1mv02s03-11 building_the_set_mc_talk with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "I don't know, don't ask me."
    scene sm1mv02s03-12 building_the_set_kv_talk with dissolve
    play voice4 kanya_arrogant_ha noloop
    kv "You two have already built plenty of sets."
    scene sm1mv02s03-13 building_the_set_sy_talk_lookkv with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "I mean, that was different. You know, we just built small stuff in the studio. But this... this is supposed to be huge!"
    scene sm1mv02s03-14 building_the_set_kv_talk with dissolve
    play voice4 kanya_no_nah2 noloop
    kv "It's really not that different from what you've already done. It's just... bigger."
    scene sm1mv02s03-15 building_the_set_mc_talk with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "And probably a bit more structurally sound."
    scene sm1mv02s03-16 building_the_set_kv_talk_look_mc with dissolve
    play voice4 kanya_yes_yep1 noloop
    kv "Exactly. You just want walls that are going to stay up, and then it's all painting and decoration."
    kv "Kind of like your studio renovation. Same basic skills, just, you know, building a pretend spaceship."
    scene sm1mv02s03-17 building_the_set_sy_talk_look_mc with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, you sound confident in being able to do this."
    scene sm1mv02s03-18 building_the_set_mc_talk with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Together, I don't think there's anything we can't do."
    scene sm1mv02s03-19 building_the_set_sy_talk with dissolve
    play voice3 stacy_happy_wooh1 noloop
    if persistent.is_special:
        sy "I agree, big bro. Me and you, we're an unstoppable duo!"
    else:
        sy "I agree. The two of us are unstoppable!"
    scene sm1mv02s03-20 building_the_set_mc_talk with dissolve
    play voice2 mc_thinking_hm noloop
    mc "All right, so I think we should-"
    scene sm1mv02s03-21 building_the_set_sy_talk_stepaway with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "Kanya and I are going to go over storyboards, have fun building the set!"
    scene sm1mv02s03-22 building_the_set_mc_talk_shocked with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, didn't we just have a moment about doing this together? Like, literally five seconds ago?"
    scene sm1mv02s03-23 building_the_set_sy_talk with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Uhm, maybe!"
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene sm1mv02s03-24 building_the_set_sy_talk_walkaway with dissolve
    play voice3 stacy_hey_happy1 noloop
    sy "But you've got this! You were so confident about walls before, you can totally do this!"
    scene sm1mv02s03-25 building_the_set_mc_talk with dissolve
    play voice2 d3s7_mcemm noloop volume 1.6
    mc "This is a lot of work for one pers-"
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1mv02s03-26 building_the_set_sy_talk_door with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Then we'll leave you to it!"
    scene sm1mv02s03-27 building_the_set_kv_talk_door with dissolve
    play voice4 kanya_hey_simple2 noloop
    kv "Later, [mcname]!"
    play sound sfx_door_openclosed1
    scene sm1mv02s03-28 building_the_set_kv_sy_gone with dissolve
    pause
    scene sm1mv02s03-29 building_the_set_mc_thought_dumbstruck with dissolve
    play voice2 d1s5_orgasm noloop
    mct "Do they really expect me to do this all by myself?"
    mct "This is a shit ton of work..."
    scene sm1mv02s03-30 building_the_set_mc_thought_turn with dissolve
    play voice2 d14s16_smell noloop
    mct "Building a whole set by myself... why is it always me?"
    mct "Have I spurned some malevolent God? Some fiend that controls my very fate?"
    mct "Cursing me to toil away, to suffer an unjust fate?"
    mct "For what? Comedy? Righteous fury? Unjust vengeance?"
    scene sm1mv02s03-31 building_the_set_mc_thought_shakeoff with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mct "Woah, that was a weird inner monologue."
    mct "I think I need to take a break from writing scripts..."
    play sound sfx_throw_something1
    scene sm1mv02s03-32 building_the_set_mc_thought_staring_space with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "Welp. Might as well get to it."
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    $ renpy.music.set_volume(0.5, 4.5, "music2" )
    play sound sfx_box_slide
    scene sm1mv02s03-33 building_the_set_montage_walkntospace_holding tools with fade
    pause
    play sound2 sfx_hammer_loop1
    scene sm1mv02s03-34 building_the_set_montage_fake_wall with fade
    pause
    play sound sfx_epic_jump1
    play sound3 sfx_heels_steps1
    stop sound2 fadeout 1.5
    scene sm1mv02s03-35 building_the_set_montage_hold_plywood with fade
    pause
    stop sound3 fadeout 1.0
    play sound sfx_hammer_loop1 loop
    scene sm1mv02s03-36 building_the_set_montage_hold_hammer with fade
    pause
    stop sound fadeout 1.5
    play sound2 sfx_paint_hand_in3 noloop
    play sound3 sfx_heels_steps1
    scene sm1mv02s03-37 building_the_set_montage_paintcan with fade
    pause
    stop sound3 fadeout 1.0
    play sound sfx_bottle_cap_open
    scene sm1mv02s03-38 building_the_set_montage_water with fade
    pause
    play sound2 sfx_paint_smearing1 noloop volume 0.5
    play sound3 sfx_brush_painting4
    scene sm1mv02s03-39 building_the_set_montage_painting with fade
    pause
    stop sound3 fadeout 2.0
    play sound sfx_screwdriver_drill6
    stop sound2 fadeout 1.0
    scene sm1mv02s03-40 building_the_set_montage_hammering with fade
    pause
    $ renpy.music.set_volume(0.0, 4.5, "music" )
    $ renpy.music.set_volume(1.0, 2.5, "music2" )
    scene sm1mv02s03-a41 set-montage-finish-glambot-000 with fade
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1mv02s03-a41-glam
    pause
    play voice2 mc_disappointed_ah2 noloop
    mct "God, I'm exhausted..."
    mct "I think that's enough for today."
    play sound sfx_heels_steps2 loop
    stop sound2 fadeout 1.0
    scene sm1mv02s03-42 building_the_set_montage_walkout with dissolve
    pause
    play sound2 sfx_door_openclosed1 noloop
    scene sm1mv02s03-43 building_the_set_montage_dogo_kv_sytalking with fade
    pause
    stop sound fadeout 1.0
    scene sm1mv02s03-44 building_the_set_sy_talk_excited with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Is it all done!?"
    scene sm1mv02s03-45 building_the_set_mc_talk with dissolve
    play voice2 mc_no_no1 noloop
    mc "Not yet."
    scene sm1mv02s03-46 building_the_set_sy_talk with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "Awwww."
    scene sm1mv02s03-47 building_the_set_mc_talk with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "It's a lot of work. It would go a lot faster if I had some help."
    scene sm1mv02s03-48 building_the_set_sy_talk with dissolve
    play voice3 stacy_hey_angry1 noloop
    sy "Hey, we've been doing stuff too! We got the alien look kind of figured out."
    scene sm1mv02s03-49 building_the_set_mc_talk with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Really?"
    scene sm1mv02s03-50 building_the_set_sy_talk with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Yep! And we worked all the way through the storyboards, {i}and{/i} started planning out the CGI."
    scene sm1mv02s03-51 building_the_set_mc_talk_surprised with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow, you two have been busy."
    scene sm1mv02s03-52 building_the_set_sy_talk with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "What, did you think we were just sitting in here, gossiping, and drinking coffee?"
    scene sm1mv02s03-53 building_the_set_mc_talk with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "I mean..."
    scene sm1mv02s03-54 building_the_set_kv_talk with dissolve
    play voice4 kanya_thinking_eeh2 noloop
    kv "To be fair-"
    scene sm1mv02s03-55 building_the_set_sy_talk with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "\"To be faaaaair!\""
    scene sm1mv02s03-56 building_the_set_kv_talk with dissolve
    play voice4 kanya_yes_yeah2 noloop
    kv "Yeah, to be fair, we did do a little bit of gossiping, and a whole lot of coffee."
    scene sm1mv02s03-57 building_the_set_sy_talk_smile with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "That we did."
    scene sm1mv02s03-58 building_the_set_mc_talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Well, I'm glad all three of us had a productive day."
    scene sm1mv02s03-59 building_the_set_sy_talk with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "Me too!"
    scene sm1mv02s03-60 building_the_set_kv_talk with dissolve
    play voice4 kanya_yes_yep2 noloop
    kv "Same."
    scene sm1mv02s03-61 building_the_set_mc_talk_tired with dissolve
    play voice2 d7s6_moan2 noloop volume 1.8
    mc "But I'm definitely going to have to come back another day to finish things up."
    scene sm1mv02s03-62 building_the_set_kv_talk with dissolve
    play voice4 kanya_thinking_hmm3 noloop
    kv "How much longer do you think it'll take?"
    scene sm1mv02s03-63 building_the_set_mc_talk with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Probably just one more day."
    scene sm1mv02s03-64 building_the_set_kv_talk with dissolve
    play voice4 kanya_disappointed_oh noloop
    kv "Well, when you're done, you think you could help me set up the green screens?"
    scene sm1mv02s03-65 building_the_set_mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, that shouldn't be a problem."
    scene sm1mv02s03-66 building_the_set_kv_talk_stand_awesome with dissolve
    play voice4 kanya_happy_wooh noloop
    kv "Awesome! I'm getting really excited!"
    scene sm1mv02s03-67 building_the_set_sy_talk with dissolve
    play voice3 stacy_happy_laugh3 noloop
    sy "Me too!"
    scene sm1mv02s03-68 building_the_set_mc_talk with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "I am getting really excited...{w} for my bed."
    scene sm1mv02s03-69 building_the_set_sy_talk_standmc with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Well then let's get you home, sleepy head!"
    scene sm1mv02s03-70 building_the_set_mc_talk with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Please."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1mv02s03-71 building_the_set_sy_talk_arms with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Come on, you."
    scene sm1mv02s03-72 building_the_set_sy_talk_bye with dissolve
    play voice3 stacy_hey_seeya noloop
    sy "See you later, Kanya!"
    scene sm1mv02s03-73 building_the_set_kv_talk_wave with dissolve
    play voice4 kanya_yes_yeah3 noloop
    kv "Yeah, see ya'! And [mcname], stop by whenever you're ready to finish the set!"
    scene sm1mv02s03-74 building_the_set_mc_talk with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Will do!"
    $ renpy.music.set_volume(0.7, 1.5, "music" )
    $ renpy.music.set_volume(0.0, 3.5, "music2" )
    play sound sfx_door_openclosed1
    scene sm1mv02s03-75 building_the_set_sy_talk_studio with Fade(0.5, 0.5, 0.5)
    queue sound sfx_heels_steps2 loop
    play voice3 stacy_arrogant_huh3 noloop
    sy "You had a long day, huh."
    scene sm1mv02s03-76 building_the_set_mc_talk with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh yeah..."
    scene sm1mv02s03-77 building_the_set_sy_talk with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "You know, we could probably hire someone to finish things up for you."
    scene sm1mv02s03-78 building_the_set_mc_talk with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Nah..."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1mv02s03-79 building_the_set_mc_talk_bed with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "We can save a few bucks if we do the work."
    scene sm1mv02s03-80 building_the_set_sy_talk with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "That's true... and {i}we{/i} are hard workers!"
    scene sm1mv02s03-81 building_the_set_mc_talk with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh..."
    play sound sfx_bed_fall1 volume 1.6
    scene sm1mv02s03-82 building_the_set_mc_talk_bed with dissolve
    play voice2 mc_disgust_meh3 noloop
    mc "Definitely \"we\"."
    scene sm1mv02s03-83 building_the_set_sy_talk with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah! The two of us!"
    play sound sfx_cloth_rustling4
    scene sm1mv02s03-84 building_the_set_sy_talk_lay with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Both working hard to make this movie."
    scene sm1mv02s03-85 building_the_set_mc_talk with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah... we both are..."
    play sound sfx_cloth_rustling3
    scene sm1mv02s03-86 building_the_set_sy_talk with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "But you really kicked ass today, [mcname]."
    scene sm1mv02s03-87 building_the_set_mc_talk with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.8
    mc "I know..."
    scene sm1mv02s03-88 building_the_set_sy_talk with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "This is going to be a kick ass movie, [mcname]."
    scene sm1mv02s03-89 building_the_set_mc_talk with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Mmhmmm..."
    scene sm1mv02s03-90 building_the_set_sy_talk with dissolve
    play voice3 stacy_moan4 noloop
    sy "I'm so happy we're doing this together. You're... you're my favorite person in the world, do you know that?"
    scene sm1mv02s03-91 building_the_set_mc_talk with dissolve
    mc "..."
    play sound sfx_cloth_rustling5
    scene sm1mv02s03-92 building_the_set_sy_talk_elbow with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "[mcname]?"
    play voice2 d7s6_snoring
    mc "..."
    play sound sfx_cloth_rustling2
    scene sm1mv02s03-93 building_the_set_sy_talk_cuddle with dissolve
    play voice3 stacy_disappointed_moan1 noloop
    sy "Sleep well, [mcname]."
    stop voice2 fadeout 2.0
    scene black with dissolve
    pause
    jump sm1mv02s03_01_next_day
label sm1mv02s03_01_next_day:
    $ renpy.music.set_volume(1.0, 1.5, "music" )
    $ renpy.music.set_volume(1.0, 1.5, "music2" )
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    if vn_mode:
        $ StoryController.end_scene(MOVIE_SCIFI)
        return
    $ gt.add((7 + (24 - gt.curr_hour)), 0, 0)
    $ player.sleep_common_function()
    $ player.progress_storyline(MOVIE_SCIFI)
    return