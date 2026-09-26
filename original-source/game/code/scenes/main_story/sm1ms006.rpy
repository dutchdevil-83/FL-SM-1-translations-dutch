image sm1ms006-a74-1 = Movie(play = "images/ms/s006/anim/sm1ms006-a74-1-2x-50fps.webm", start_image = "sm1ms006-a74-1 mc-spank-sy-anim-01")
image sm1ms006-a74-1-f = Movie(play = "images/ms/s006/anim/sm1ms006-a74-1-2x-60fps.webm", start_image = "sm1ms006-a74-1 mc-spank-sy-anim-01")
image sm1ms006-a74-2 = Movie(play = "images/ms/s006/anim/sm1ms006-a74-2-2x-50fps.webm", start_image = "sm1ms006-a74-2 mc-spank-sy-anim-01")
image sm1ms006-a74-2-f = Movie(play = "images/ms/s006/anim/sm1ms006-a74-2-2x-60fps.webm", start_image = "sm1ms006-a74-2 mc-spank-sy-anim-01")
image sm1ms006-a74-3 = Movie(play = "images/ms/s006/anim/sm1ms006-a74-3-2x-50fps.webm", start_image = "sm1ms006-a74-3 mc-spank-sy-anim-01")
image sm1ms006-a74-3-f = Movie(play = "images/ms/s006/anim/sm1ms006-a74-3-2x-60fps.webm", start_image = "sm1ms006-a74-3 mc-spank-sy-anim-01")
label sm1ms006:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.1, 0.0, "sound4" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound4 sfx_parkday_birds fadein 1.0
    play voice2 d7s6_snoring
    play voice3 stacy_disappointed_snoring volume 0.6
    scene sm1ms006-00 answers_and_consequences with dissolve
    pause
    play voice2 d7s6_awake noloop
    scene sm1ms006-01 answers_and_consequences_mc_open_eyes_smile with dissolve
    pause
    scene sm1ms006-02 answers_and_consequences_mc_thought_open wide with vpunch
    play music music_morning_horror
    play voice2 mc_pain_mff3 noloop
    mct "Oh shit, the USB!"
    play sound sfx_cloth_rustling2
    scene sm1ms006-03 answers_and_consequences_mc_thought_sit_up with dissolve
    play voice2 mc_pain_rrrr noloop
    mct "I have to do this quiet... Don't need Stacy figuring out what happened to it."
    play sound sfx_cloth_rustling1
    stop voice3 fadeout 3.0
    scene sm1ms006-04 answers_and_consequences_mc_thought_stand with dissolve
    queue sound sfx_barefoot_steps1 loop
    pause
    stop sound fadeout 1.0
    scene sm1ms006-05 answers_and_consequences_mc_look_sy_kitchen with dissolve
    pause
    scene sm1ms006-06 answers_and_consequences_mc_thought_phone with dissolve
    play sound [sfx_phone_call2, "<silence 1.2>"] loop
    play voice2 mc_angry_huh2 noloop
    mct "God... This is my worst nightmare..."
    play sound sfx_phone_hungup1
    scene sm1ms006-07 answers_and_consequences_mc_talk_fake_friendly with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Heyyyyy, AmRose. What's up?"
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene sm1ms006-08 answers_and_consequences_arj_talk_fake_friendly with dissolve
    play voice4 amrose_arrogant_huh1 noloop
    arj "[mcname]. What do I owe the pleasure to?"
    $ renpy.music.set_volume(0.1, 1.0, "sound4" )
    scene sm1ms006-09 answers_and_consequences_mc_talk_kictchen with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Listen, when you were here... You didn't happen to see a USB on the table, did you?"
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene sm1ms006-10 answers_and_consequences_arj_talk_darkroom with dissolve
    play voice4 amrose_yes_yeah1 noloop
    arj "Maybe."
    $ renpy.music.set_volume(0.1, 1.0, "sound4" )
    scene sm1ms006-11 answers_and_consequences_mc_talk with dissolve
    play voice2 d2s12_emmm noloop
    mc "Did you happen... To take it?"
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene sm1ms006-12 answers_and_consequences_arj_talk_darkroom with dissolve
    play voice4 amrose_surprised_what noloop
    arj "Accusing me of stealing from you, really? {i}Really?{/i} After everything you two have done!?"
    $ renpy.music.set_volume(0.1, 1.0, "sound4" )
    scene sm1ms006-13 answers_and_consequences_mc_talk_kitchen with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "AmRose, please, I don't know what you want me to say anymore."
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene sm1ms006-14 answers_and_consequences_arj_talk_darkroom with dissolve
    play voice4 amrose_angry_ehh noloop
    arj "How about the truth, [mcname]?"
    $ renpy.music.set_volume(0.1, 1.0, "sound4" )
    scene sm1ms006-15 answers_and_consequences_mc_talk_kitchen with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "I already told you the truth."
    if player.has_played_scene("sm1fs_t001"):
        mc "Well... At least what I knew. There's a chance Stacy kept one or two of the videos. For research purposes."
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene sm1ms006-16 answers_and_consequences_arj_talk_darkroom with dissolve
    play voice4 amrose_arrogant_huh3 noloop
    arj "Huh."
    $ renpy.music.set_volume(0.1, 1.0, "sound4" )
    scene sm1ms006-17 answers_and_consequences_mc_talk_kitchen with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.4
    mc "What?"
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene sm1ms006-18 answers_and_consequences_arj_talk_darkroom with dissolve
    play voice4 amrose_arrogant_yeah2 noloop
    arj "You actually believe that, don't you?"
    $ renpy.music.set_volume(0.1, 1.0, "sound4" )
    scene sm1ms006-19 answers_and_consequences_mc_talk_kitchen_confused with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "Why wouldn't I? It's the truth."
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene sm1ms006-20 answers_and_consequences_arj_talk_darkroom_mad with dissolve
    play voice4 amrose_arrogant_hmm2 noloop
    arj "Really. You should ask Stacy just {i}how much{/i} data she kept."
    $ renpy.music.set_volume(0.1, 1.0, "sound4" )
    scene sm1ms006-21 answers_and_consequences_mc_talk_kitchen_confused with dissolve
    play voice2 mc_surprised_what8 noloop
    mc "What do you-"
    play sound sfx_phone_hungup2
    "*Click*"
    mc "AmRose, hello?"
    scene sm1ms006-22 answers_and_consequences_mc_look_phone with dissolve
    pause
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    play sound sfx_keyboard_typing2 volume 1.5
    scene sm1ms006-23 answers_and_consequences_arj_call_ended_look_screen with dissolve
    pause
    play sound sfx_keyboard_enter1
    scene sm1ms006-24-01 d16s05-62_sy-toilet1_c1 with dissolve
    pause
    play sound sfx_keyboard_enter1
    scene sm1ms006-24-02 d14s14-066 with dissolve
    pause
    play sound sfx_keyboard_enter1
    scene sm1ms006-25-01 d14s06-04_mes-mc-lc-talk-in-shower with dissolve
    pause
    play sound sfx_keyboard_enter1
    scene sm1ms006-25-02 d10p2s09-14_mc-aw_merged with dissolve
    pause
    play sound sfx_keyboard_enter1
    scene sm1ms006-25-03 d10p2s09-14_mc-aw_merged_2 with dissolve
    play voice4 amrose_angry_breath1 noloop
    pause
    $ renpy.music.set_volume(0.1, 1.0, "sound4" )
    stop music fadeout 3.0
    scene sm1ms006-26 answers_and_consequences_mc_thought with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Well that was weird... I wonder what AmRose meant?"
    play sound sfx_cloth_rustling4
    scene sm1ms006-27 answers_and_consequences_mc_thought_sy_waking with dissolve
    queue music music_bubblegum_casual
    play voice2 mc_arrogant_hm3 noloop
    mct "I guess there's no time like the present."
    play sound sfx_barefoot_steps1 loop
    scene sm1ms006-28 answers_and_consequences_sy_talk_walking with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Morning, [mcname]."
    scene sm1ms006-29 answers_and_consequences_mc_talk_walking with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Morning, Stacy."
    stop sound fadeout 1.0
    scene sm1ms006-30 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_disappointed_moan1 noloop
    sy "Coffee on yet?"
    scene sm1ms006-31 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_no_no6 noloop
    mc "Uh, not yet."
    scene sm1ms006-32 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "What's the hold-up?"
    scene sm1ms006-33 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Well... I got some bad news."
    scene sm1ms006-34 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_disappointed_oh3 noloop
    sy "Can't you wait until I've had some coffee?"
    scene sm1ms006-35 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "Not really. AmRose stole your flash drive."
    play voice3 stacy_ah noloop
    scene sm1ms006-36 answers_and_consequences_sy_talk_shocked with hpunch
    sy "Noooooooooo! That's not good."
    play voice3 stacy_no_nonono6 noloop
    sy "How could this have happened!? This is super not good."
    scene sm1ms006-37 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah... I guess when she broke in she just slipped it into her pockets."
    scene sm1ms006-38 answers_and_consequences_sy_talk_look_door with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "We really need some better locks."
    scene sm1ms006-39 answers_and_consequences_mc_talk_look_door with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "I do too. But... AmRose said something kind of interesting."
    scene sm1ms006-40 answers_and_consequences_sy_talk_lookmc with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "Like what?"
    scene sm1ms006-41 answers_and_consequences_mc_talk_uncomfortable with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "How much of the data did you keep from Fetish Locator, Stacy?"
    scene sm1ms006-42 answers_and_consequences_sy_talk_nervous with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "You know... Just the geo-data.{w} And usernames."
    scene sm1ms006-43 answers_and_consequences_mc_talk_menufelse with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.4
    if player.has_played_scene("sm1fs_t001"):
        mc "Well we both know that's not entirely true. What about Taisia's video?"
    else:
        mc "Come on, Stacy. We both know that's not true."
    scene sm1ms006-44 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_disappointed_ehh2 noloop
    sy "Okay, so maybe I kept a little more than that..."
    scene sm1ms006-45 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Stacy."
    scene sm1ms006-46 answers_and_consequences_sy_talk with hpunch
    play voice3 stacy_thinking_emm1 noloop
    sy "Okay, maybe {i}a lot more{/i} than that."
    scene sm1ms006-47 answers_and_consequences_mc_talk_pinch_nose with dissolve
    play voice2 mc_angry_errr6 noloop
    mc "Jesus, Stacy."
    scene sm1ms006-48 answers_and_consequences_mc_talk_sy_look_down with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "How much?"
    scene sm1ms006-49 answers_and_consequences_sy_talk_sy_look_down with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "Uhhhh..."
    scene sm1ms006-50 answers_and_consequences_mc_talk_sy_look_down with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "How much, Stacy?"
    scene sm1ms006-51 answers_and_consequences_sy_talk_sy_look_down with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "... Okay, I only kept data from around Crowning. Everything from the college I did a hard wipe on."
    scene sm1ms006-52 answers_and_consequences_mc_talk_sy_look_down with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Including AmRose's stuff?"
    scene sm1ms006-53 answers_and_consequences_sy_talk_sy with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Especially AmRose's. I double, triple checked that it was deleted."
    scene sm1ms006-54 answers_and_consequences_mc_talk_shake_head with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "Damn it, Stacy."
    scene sm1ms006-55 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "What! It was a veritable treasure trove of porn! And it's coming in super handy for the talent scouting we have to do for the studio!"
    sy "Without it, we would have been starting with nothing."
    scene sm1ms006-56 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "But you lied to me."
    scene sm1ms006-57 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "It's not a big deal? I mean you lied about the metric ton of of porn you had hidden under your bed, [mcname]."
    scene sm1ms006-58 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "I never lied about that, I just never told you about it."
    scene sm1ms006-59 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_arrogant_huh5 noloop
    sy "What's the difference?"
    scene sm1ms006-60 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "You lied to my face, Stacy."
    mc "And all of my porn was of porn stars, not of people we know personally."
    scene sm1ms006-61 answers_and_consequences_sy_talk_guilty with dissolve
    play voice3 stacy_disappointed_oh4 noloop
    sy "Okay... You've got a point there."
    scene sm1ms006-62 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_angry_off noloop
    mc "You've been a bad girl, Stacy. You know what that means."
    scene sm1ms006-63 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "Uhmmm, coffee?"
    scene sm1ms006-64 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_no_no5 noloop
    mc "Nope.{w} Bend over the table."
    scene sm1ms006-65 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Ooooo, kinky."
    stop music fadeout 3.0
    play sound sfx_door_slide5
    scene sm1ms006-66 answers_and_consequences_sy_talk_bends_over with dissolve
    queue sound sfx_plates_moving1
    queue music music_sexy_discipline
    "*DRAWER OPENS*"
    play voice3 stacy_pain_huh1 noloop
    sy "Ooooo, what're you doing back there?"
    scene sm1ms006-67 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Grab onto the table, and if your hands come off the table you're going to be in twice as much trouble."
    scene sm1ms006-68 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "Ooooo, so commanding. I like this side of you, [mcname]."
    play sound sfx_barefoot_steps1 loop
    scene sm1ms006-69 answers_and_consequences_sy_ass_over_shoulder with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1ms006-70 answers_and_consequences_sy_talk with dissolve
    play voisex3 stacy_thinking_hmm3 noloop
    sy "I think-"
    play voisex3 stacy_scared_ah1 noloop
    play sound sfx_woodenspoon_slap1
    scene sm1ms006-71 answers_and_consequences_sy_talk_smack with hpunch
    "*WHACK*"
    play voisex3 stacy_angry_fuck1 noloop
    sy "HOLY FUCK!"
    scene sm1ms006-72 answers_and_consequences_mc_talk_serious with dissolve
    play voisex2 mc_arrogant_huh2 noloop
    mc "Now how many spankings is appropriate for the punishment?"
    scene sm1ms006-73 answers_and_consequences_sy_talk with dissolve
    play voisex3 stacy_thinking_emm2 noloop
    sy "Well hang on a second-"
    play voisex2 mc_angry_errr5 noloop
    play voisex3 stacy_pain_ou1 noloop
    play sound sfx_woodenspoon_slap2
    scene sm1ms006-74 answers_and_consequences_sy_talk_spank_animation with hpunch
    sy "Ouch! Why so hard!?"
    scene sm1ms006-a74-1 mc-spank-sy-anim-01 with dissolve
    play voisex2 mc_angry_errr2 noloop
    mc "Because I'm upset with you."
    play voisex3 "<silence 0.7>" noloop
    queue voisex3 stacy_moans3
    queue voisex2 mc_sex_openmoans2
    play sound ["<silence 0.7>", sfx_woodenspoon_slap1, "<silence 1.1>", sfx_woodenspoon_slap2, "<silence 1.3>", sfx_woodenspoon_slap3, "<silence 1.1>", sfx_woodenspoon_slap4, "<silence 1.1>", sfx_woodenspoon_slap5, "<silence 0.46>"] loop
    scene sm1ms006-a74-1
    pause
    sy "You don't need to take it out on my ass! Come on, you like my ass!"
    play sound ["<silence 0.7>", sfx_woodenspoon_slap1, "<silence 1.1>", sfx_woodenspoon_slap2, "<silence 1.3>", sfx_woodenspoon_slap3, "<silence 1.1>", sfx_woodenspoon_slap4, "<silence 1.1>", sfx_woodenspoon_slap5, "<silence 0.46>"] loop
    scene sm1ms006-a74-2 with dissolve
    mc "But the person that ass is attached to has brought on a world of pain for herself."
    pause
    play sound ["<silence 0.7>", sfx_woodenspoon_slap1, "<silence 1.1>", sfx_woodenspoon_slap2, "<silence 1.3>", sfx_woodenspoon_slap3, "<silence 1.1>", sfx_woodenspoon_slap4, "<silence 1.1>", sfx_woodenspoon_slap5, "<silence 0.46>"] loop
    scene sm1ms006-a74-3 with dissolve
    queue voisex2 mc_sex_openmoans2
    queue voisex3 stacy_moans3
    sy "Please, [mcname]! It was just one little lie."
    pause
    play voisex2 d9s5_auch2 noloop
    queue voisex2 mc_sex_openmoans2
    play sound ["<silence 0.35>", sfx_woodenspoon_slap1, "<silence 0.6>", sfx_woodenspoon_slap2, "<silence 0.7>", sfx_woodenspoon_slap3, "<silence 0.5>", sfx_woodenspoon_slap4, "<silence 0.6>", sfx_woodenspoon_slap5, "<silence 0.05>"] loop
    scene sm1ms006-a74-1-f with dissolve
    mc "You're still doing it, Stacy. The punishment will continue until you start being honest."
    play sound ["<silence 0.35>", sfx_woodenspoon_slap1, "<silence 0.6>", sfx_woodenspoon_slap2, "<silence 0.7>", sfx_woodenspoon_slap3, "<silence 0.5>", sfx_woodenspoon_slap4, "<silence 0.6>", sfx_woodenspoon_slap5, "<silence 0.05>"] loop
    scene sm1ms006-a74-2-f with dissolve
    pause
    play voisex3 stacy_yes_fine1 noloop
    queue voisex3 stacy_moans3
    sy "Okay, {i}fine!{/i} It was kind of a big lie."
    stop voisex3 fadeout 1.0
    stop sound fadeout 1.0
    scene sm1ms006-81 answers_and_consequences_mc_talk with dissolve
    play voisex2 mc_yes_yeah7 noloop
    mc "And?"
    scene sm1ms006-82 answers_and_consequences_sy_talk with dissolve
    play voisex3 stacy_mmm1 noloop
    sy "And..."
    play voisex3 stacy_angry_fuck2 noloop
    play sound ["<silence 0.35>", sfx_woodenspoon_slap1, "<silence 0.6>", sfx_woodenspoon_slap2, "<silence 0.7>", sfx_woodenspoon_slap3, "<silence 0.5>", sfx_woodenspoon_slap4, "<silence 0.6>", sfx_woodenspoon_slap5, "<silence 0.05>"] loop
    scene sm1ms006-a74-3-f with dissolve
    play voisex3 stacy_moans3
    sy "FUCK! I won't do it again!"
    play voisex2 mc_angry_errr4 noloop
    mc "Is that a promise?"
    sy "Yes, yes. I promise I won't lie to you anymore."
    stop sound fadeout 1.0
    scene sm1ms006-86 answers_and_consequences_mc_talk with dissolve
    play voisex3 stacy_angry_breath2 noloop
    play voisex2 mc_yes_aga2 noloop
    mc "Good."
    play voisex3 stacy_pain_ou2 noloop
    play sound sfx_woodenspoon_slap2
    scene sm1ms006-87 answers_and_consequences_sy_talk with hpunch
    sy "Ouch, [mcname]! I promised!"
    scene sm1ms006-88 answers_and_consequences_mc_talk with dissolve
    play voisex2 mc_happy_hah1 noloop
    mc "That one was so you remember your promise."
    scene sm1ms006-89 answers_and_consequences_sy_talk_forehead_table with dissolve
    play voisex3 stacy_orgasmed noloop
    sy "*sighs* Thank God..."
    scene sm1ms006-90 answers_and_consequences_sy_closeup with dissolve
    pause
    scene sm1ms006-91 answers_and_consequences_mc_talk_look with dissolve
    play voice2 mc_surprised_what6 noloop
    mc "Thank God for what? It looks like you were enjoying this."
    scene sm1ms006-92 answers_and_consequences_sy_talk with dissolve
    play voisex3 stacy_breathing2 noloop
    sy "Maybe... Just a little bit."
    play voisex3 stacy_angry_argh3 noloop
    play voice2 mc_pain_argh1 noloop
    play sound sfx_woodenspoon_slap3
    scene sm1ms006-77 answers_and_consequences_mc_talk with hpunch
    sy "God, [mcname]! I don't know how much more of this I can take."
    play sound mc_kiss1
    scene sm1ms006-93 answers_and_consequences_mc_talk_kiss_cheek with dissolve
    pause
    scene sm1ms006-94 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_happy_a1 noloop
    mc "To make it all better."
    scene sm1ms006-95 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_angryhuh noloop
    sy "*Quietly* That's not what I want you to be kissing right now."
    scene sm1ms006-96 answers_and_consequences_mc_talk with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What was that?"
    scene sm1ms006-97 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_no_nonono5 noloop
    sy "Nothing!"
    scene sm1ms006-98 answers_and_consequences_sy_talk_standing with dissolve
    play voice3 stacy_disgust_oof1 noloop
    sy "I'm going to have trouble sitting all day."
    scene sm1ms006-99 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Good. I hope that means and you learned your lesson."
    play sound sfx_barefoot_steps1 loop
    scene sm1ms006-100 answers_and_consequences_sy_walk_to_bed_mc_confused with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Speaking of lessons, Stacy sure likes getting spanked. I wonder what other BDSM things we can get into..."
    scene sm1ms006-101 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Stacy... I'm curious about something."
    stop sound fadeout 1.0
    scene sm1ms006-102 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yes?"
    scene sm1ms006-103 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "If you downloaded all the porn off the servers, why did you have the USB delivered? Shouldn't you have already had it?"
    scene sm1ms006-104 answers_and_consequences_sy_talk_embarassed with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Uhm... I-"
    play sound sfx_throw_something1
    scene sm1ms006-105 answers_and_consequences_mc_hold_spoon with dissolve
    play voice2 mc_angry_hm1 noloop
    pause
    scene sm1ms006-106 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_upset1 noloop
    sy "Okay, please don't tell anyone... But the encryption was too hard for me to crack. I had to get a little help."
    scene sm1ms006-107 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Huh..."
    scene sm1ms006-108 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "And it's not \"gone\" gone. I made a backup of some of the spicier things."
    play sound sfx_barefoot_steps1 loop
    scene sm1ms006-109 answers_and_consequences_sy_dress_spoon_down with dissolve
    pause
    play sound2 sfx_cloth_planket2 noloop
    play sound sfx_heels_steps2
    scene sm1ms006-110 answers_and_consequences_sy_dressed with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "Man, getting spanked first thing in the morning is better than a cup of coffee."
    stop sound fadeout 1.0
    scene sm1ms006-111 answers_and_consequences_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I'll keep that in mind."
    scene sm1ms006-112 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "I'm really sorry, [mcname]."
    mc "I know."
    sy "And... maybe next time you should pull out some nipple clamps. Those always sound fun."
    scene sm1ms006-113 answers_and_consequences_mc_talk with dissolve
    play voice2 d2s9_confused noloop
    mct "Even after getting punished, Stacy is still the best."
    scene sm1ms006-114 answers_and_consequences_sy_talk with dissolve
    play voice3 stacy_arrogant_hmm3 noloop
    sy "You doing to get dressed?"
    play sound sfx_barefoot_steps1 loop
    scene sm1ms006-115 answers_and_consequences_mc_talk_walk_to_bed with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Shit. You got me all worked up, I almost forgot about all the stuff I need to do."
    sy "*giggles* Little old me? Distracting? Never."
    stop sound fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 5.0, "sound4" )
    stop sound4 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    call sm1ms006_dicover_trait_spanking from _call_sm1ms006_dicover_trait_spanking
    $ StoryController.end_scene(MS, 1, 0, 0)
    return
label sm1ms006_dicover_trait_spanking:
    $ CharacterController.get_character("sy").discover_trait(SPANKING)
    return
label sm1ms006_unlocks:
    call sm1ms006_dicover_trait_spanking from _call_sm1ms006_dicover_trait_spanking_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MS)
    return