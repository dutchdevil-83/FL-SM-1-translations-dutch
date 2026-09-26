image sm1cs_km005-a82-1 = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a82-1-2x-50fps.webm", start_image = "sm1cs-km005-a82-1 km-mc-hj-anim-01")
image sm1cs_km005-a82-1-f = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a82-1-2x-60fps.webm", start_image = "sm1cs-km005-a82-1 km-mc-hj-anim-01")
image sm1cs_km005-a82-2 = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a82-2-2x-50fps.webm", start_image = "sm1cs-km005-a82-2 km-mc-hj-anim-01")
image sm1cs_km005-a82-2-f = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a82-2-2x-60fps.webm", start_image = "sm1cs-km005-a82-2 km-mc-hj-anim-01")
image sm1cs_km005-a91-1 = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a91-1-2x-50fps.webm", start_image = "sm1cs-km005-a91-1 mc-km-hj-anim-01")
image sm1cs_km005-a91-1-f = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a91-1-2x-60fps.webm", start_image = "sm1cs-km005-a91-1 mc-km-hj-anim-01")
image sm1cs_km005-a91-2 = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a91-2-2x-50fps.webm", start_image = "sm1cs-km005-a91-2 mc-km-hj-anim-01")
image sm1cs_km005-a91-2-f = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a91-2-2x-60fps.webm", start_image = "sm1cs-km005-a91-2 mc-km-hj-anim-01")
image sm1cs_km005-a114-1 = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a114-1-2x-50fps.webm", start_image = "sm1cs-km005-a114-1 mc-km-boobjob-anim-01")
image sm1cs_km005-a114-1-f = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a114-1-2x-60fps.webm", start_image = "sm1cs-km005-a114-1 mc-km-boobjob-anim-01")
image sm1cs_km005-a114-2 = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a114-2-2x-50fps.webm", start_image = "sm1cs-km005-a114-2 mc-km-boobjob-anim-01")
image sm1cs_km005-a114-2-f = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a114-2-2x-60fps.webm", start_image = "sm1cs-km005-a114-2 mc-km-boobjob-anim-01")
image sm1cs_km005-a114-3 = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a114-3-2x-50fps.webm", start_image = "sm1cs-km005-a114-3 mc-km-boobjob-anim-01")
image sm1cs_km005-a114-3-f = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a114-3-2x-60fps.webm", start_image = "sm1cs-km005-a114-3 mc-km-boobjob-anim-01")
image sm1cs_km005-a114-4 = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a114-4-2x-50fps.webm", start_image = "sm1cs-km005-a114-4 mc-km-boobjob-anim-01")
image sm1cs_km005-a114-4-f = Movie(play = "images/FS_T/KM/s005/anim/sm1cs-km005-a114-4-2x-60fps.webm", start_image = "sm1cs-km005-a114-4 mc-km-boobjob-anim-01")
label sm1cs_km005:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music thinking_music_2
    play sound sfx_door_openclosed2
    scene sm1cs-km005-00 hot_in_the_directors_office with Fade(0.5, 0.5, 0.5)
    pause
    play sound2 sfx_heels_steps2
    scene sm1cs-km005-01 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey Kellie."
    mc "Everything alright?"
    stop sound2 fadeout 1.0
    scene sm1cs-km005-02 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_yes_yeah3 noloop
    km "Totally. Why wouldn't they be?"
    scene sm1cs-km005-03 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I don't know. You just look a little flush."
    scene sm1cs-km005-04 hot_in_the_directors_office_km_talk_hair with dissolve
    play voice3 girl31_no_laughing2 noloop
    km "I'm not flush. You just surprised me. I thought it would take you longer to get here."
    play sound2 sfx_heels_steps2
    scene sm1cs-km005-05 hot_in_the_directors_office_mc_talk_move_chair with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure and... what are you doing in Denise's office anyhow?"
    play sound2 sfx_bed_slide3 noloop
    scene sm1cs-km005-06 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_thinking_emm1 noloop
    km "She lets me practice here sometimes."
    km "Helps me avoid {i}her{/i}."
    scene sm1cs-km005-07 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Her?"
    scene sm1cs-km005-08 hot_in_the_directors_office_km_talk_awkward with dissolve
    play voice3 girl31_thinking_mmm1 noloop
    km "Veronica."
    play sound sfx_bed_slide2
    scene sm1cs-km005-09 hot_in_the_directors_office_mc_talk_up_grinning with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Huh. Funny you should mention her."
    play sound sfx_door_slam1 volume 0.7
    scene sm1cs-km005-10 hot_in_the_directors_office_mc_talk_lean with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Denise asked me to tell you that she wants you and Veronica to put together a workshop for the crew to do."
    scene sm1cs-km005-11 hot_in_the_directors_office_km_talk_skeptical with dissolve
    play voice3 girl31_thinking_oh noloop
    km "Oh, did she?"
    scene sm1cs-km005-12 hot_in_the_directors_office_mc_talk_keep with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Uh. Yeah. She thinks the two of you can come up with something unique."
    play sound sfx_throw_something1
    scene sm1cs-km005-13 hot_in_the_directors_office_km_talk_point with dissolve
    play voice3 girl31_angry_argh noloop
    km "Why are you lying to me, [mcname]?"
    scene sm1cs-km005-14 hot_in_the_directors_office_mc_talk_handup with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "Huh-I... I'm not lying."
    mct "Okay, this is starting off rough."
    play sound sfx_heels_steps1
    scene sm1cs-km005-15 hot_in_the_directors_office_km_talk_walk with dissolve
    play voice3 girl31_arrogant_huh2 noloop
    km "Really? Because I just saw Denise a little while ago, and she didn't say anything about an assignment with Veronica."
    stop sound fadeout 1.0
    scene sm1cs-km005-16 hot_in_the_directors_office_km_talk_corner with dissolve
    play voice3 girl31_angry_cough4 noloop
    km "So how about you tell me exactly what is going on?"
    scene sm1cs-km005-17 hot_in_the_directors_office_mc_talk_corner with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay. Just...{w} keep an open mind, okay?"
    scene sm1cs-km005-18 hot_in_the_directors_office_km_talk_silent with dissolve
    km "..."
    scene sm1cs-km005-19 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Great."
    mc "So... Veronica figured out that the reason you have been avoiding her is because of her getting all the lead roles."
    scene sm1cs-km005-20 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_happy_mmm1 noloop
    km "And how did Veronica figure that out?"
    play sound sfx_hair_scratch1
    scene sm1cs-km005-21 hot_in_the_directors_office_mc_talk_head with dissolve
    play voice2 mc_no_nah2 noloop
    mc "No clue. But she is very sincere about finding some common ground between you two."
    play sound sfx_cloth_rustling4
    scene sm1cs-km005-22 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_no_angry noloop
    km "You're lying again."
    scene sm1cs-km005-23 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_no_nope1 noloop
    mc "Nope. She is really committed to it, Kellie. I promise."
    scene sm1cs-km005-24 hot_in_the_directors_office_km_talk_angry with dissolve
    play voice3 girl31_arrogant_hm1 noloop
    km "Not going to happen."
    km "It's just some trick. I know it is."
    scene sm1cs-km005-25 hot_in_the_directors_office_mc_talk_getit with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "A trick? Why would she be tricking you?"
    scene sm1cs-km005-26 hot_in_the_directors_office_km_talk_lookaway with dissolve
    play voice3 girl31_disappointed_ehh5 noloop
    km "Because she..."
    km "Forget about it."
    scene sm1cs-km005-27 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Come on, Kellie. You can tell me."
    play sound sfx_heels_steps1
    scene sm1cs-km005-28 hot_in_the_directors_office_km_talk_rolleyes with dissolve
    play voice3 girl31_yes_confident noloop
    km "Oh yes, because you're so good at keeping secrets. Just..."
    km "Leave me alone, [mcname]."
    play sound sfx_bed_slide2
    scene sm1cs-km005-29 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "I don't get you. Veronica wants to figure out a better way going forward so you can get some of the lead roles and you just want to shut her down."
    mc "Don't you owe her a chance to help out?"
    mc "Or are you that stubborn?"
    scene sm1cs-km005-30 hot_in_the_directors_office_km_talk_soften with dissolve
    play voice3 girl31_thinking_emm2 noloop
    km "I'm..."
    km "No. It's a trick. I know it is. She must have figured out what I was doing."
    play sound sfx_phone_tapping1 loop
    scene sm1cs-km005-31 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Uh, what have you been doing?"
    scene sm1cs-km005-32 hot_in_the_directors_office_km_talk_embarassed with dissolve
    play voice3 girl31_thinking_hmm1 noloop
    km "Liking all of her photos on Gram."
    km "Damn. I should have been stronger. I don't know what's wrong with me."
    play sound sfx_cloth_rustling1
    scene sm1cs-km005-33 hot_in_the_directors_office_km_talk_rubhead_phonedesk with dissolve
    play voice3 girl31_angry_ergh1 noloop
    km "And now Veronica knows, and she's going to lord it over my head."
    km "Admit it, [mcname]."
    scene sm1cs-km005-34 hot_in_the_directors_office_mc_talk_lost with dissolve
    play voice2 d3s7_mcemm noloop volume 1.6
    mc "..."
    mc "You have lost me."
    play sound sfx_cloth_rustling2
    scene sm1cs-km005-35 hot_in_the_directors_office_km_talk_recover with dissolve
    play voice3 girl31_no_nah noloop
    km "It's nothing. Forget I said anything."
    scene sm1cs-km005-36 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait. Liking her photos? You've been looking through Veronica's photos on Gram?"
    scene sm1cs-km005-37 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_no_simple noloop
    km "No."
    scene sm1cs-km005-38 hot_in_the_directors_office_km_talk_nervous with dissolve
    play voice3 girl31_arrogant_hm2 noloop
    km "*nervously* Why would I ever like Veronica's photos? She's just an airhead who keeps stealing the lead roles and looks really good in jeans and a low cut-"
    play voice3 girl31_arrogant_geh noloop
    scene sm1cs-km005-39 hot_in_the_directors_office_km_talk_believes with hpunch
    km "Gah. Never mind. I'm not falling for it. Nice try, [mcname]. But you failed your mission. So goodbye."
    mct "She is covering something up."
    play sound sfx_heels_steps2
    scene sm1cs-km005-40 hot_in_the_directors_office_mc_talk_focused with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Kellie."
    mc "Were you looking up photos of Veronica just now?"
    scene sm1cs-km005-41 hot_in_the_directors_office_km_talk_blush with dissolve
    pause
    scene sm1cs-km005-42 hot_in_the_directors_office_look_phone with dissolve
    pause
    scene sm1cs-km005-43 hot_in_the_directors_office_km_confused_eyes with dissolve
    pause
    stop music fadeout 3.0
    scene sm1cs-km005-44 hot_in_the_directors_office_mc_eyes with dissolve
    pause
    play music music_lightjazz_success3
    play voice2 mc_thinking_hm noloop
    play sound sfx_leg_kick8
    scene sm1cs-km005-45 hot_in_the_directors_office_km_talk_mc_grabphone with vpunch
    play voice3 girl31_pain_ah1 noloop
    km "That's my phone."
    scene sm1cs-km005-46 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "I'll give it back when you tell me the truth."
    play sound sfx_epic_jump1
    play sound2 sfx_sand_jump1 noloop
    scene sm1cs-km005-47 hot_in_the_directors_office_km_talk_wrsetle with dissolve
    play voice3 girl31_scared_ah4 noloop
    km "Quit it, [mcname]."
    scene sm1cs-km005-48 hot_in_the_directors_office_mc_talk_wrsetle with dissolve
    play voice2 mc_no_uhuhno noloop
    mc "If you relax and just fess up, I'll give it back."
    play sound sfx_cloth_rustling3
    scene sm1cs-km005-49 hot_in_the_directors_office_km_talk_check_phone with dissolve
    play voice3 girl31_disappointed_ehh2 noloop
    km "Whatever. I have nothing to hide from you."
    play sound sfx_phone_button1
    scene sm1cs-km005-50 hot_in_the_directors_office_km_talk_showphone with dissolve
    pause
    play sound sfx_remote_button1
    scene sm1cs-km005-51 hot_in_the_directors_office_km_talk_showphone_otherphoto with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mct "She liked this one too."
    play sound sfx_remote_button1
    scene sm1cs-km005-52 hot_in_the_directors_office_km_talk_showphone_otherphoto with dissolve
    pause
    play sound sfx_remote_button1
    scene sm1cs-km005-53 hot_in_the_directors_office_km_talk_showphone_otherphoto with dissolve
    pause
    scene sm1cs-km005-54 hot_in_the_directors_office_mc_talk_lower_phone with dissolve
    pause
    play sound sfx_skirt_off2
    scene sm1cs-km005-55 hot_in_the_directors_office_km_talk_phone_back with hpunch
    play voice3 girl31_angry_hmrr noloop
    km "Perv."
    scene sm1cs-km005-56 hot_in_the_directors_office_mc_talk_befuddled with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Kellie...{w} Are you into Veronica?"
    scene sm1cs-km005-57 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_angry_cough3 noloop
    km "Shut up."
    scene sm1cs-km005-58 hot_in_the_directors_office_km_talk_embarrassed with dissolve
    play voice3 girl31_angry_dagh noloop
    km "This wasn't supposed to happen."
    scene sm1cs-km005-59 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. I mean, you've been so worked up about her taking the lead roles."
    mc "And now you're... 'worked up' for her."
    scene sm1cs-km005-60 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_surprised_oof1 noloop
    km "It's not funny!"
    scene sm1cs-km005-61 hot_in_the_directors_office_mc_talk_laugh with dissolve
    play voice2 mc_happy_laugh1 noloop
    mc "Sorry. I just. Sorry."
    scene sm1cs-km005-62 hot_in_the_directors_office_km_talk_headdown with dissolve
    play voice3 girl31_arrogant_huh1 noloop
    km "I hate feeling like this. I can't even get mad at her anymore."
    km "That's why I looked at the pictures. At first."
    scene sm1cs-km005-63 hot_in_the_directors_office_km_talk_raisehead with dissolve
    play voice3 girl31_arrogant_yeah1 noloop
    km "This is your fault. You should have stopped me."
    km "After I saw her naked, it started."
    scene sm1cs-km005-64 hot_in_the_directors_office_km_talk_horny with dissolve
    play voice3 girl31_thinking_hmm2 noloop
    km "And then when she saw me..."
    km "It looked like... like she might enjoy it."
    scene sm1cs-km005-65 hot_in_the_directors_office_km_talk_pretendangry with dissolve
    play voice3 girl31_angry_kghh2 noloop
    km "But this is stupid. She's my rival."
    play sound sfx_phone_tapping1 loop volume 2.5
    scene sm1cs-km005-66 hot_in_the_directors_office_km_talk_look_phone with dissolve
    play voice3 girl31_disappointed_ehh3 noloop
    km "I tried to look at the photos and imagine her stealing my thunder. But..."
    km "Instead of wanting to wipe the floor with her."
    km "I just started...{w} Wanting her."
    stop sound fadeout 1.0
    scene sm1cs-km005-67 hot_in_the_directors_office_mc_talk_cool with dissolve
    play voice2 d2s12_emmm noloop volume 1.7
    mc "I'm... I mean, this is just crazy. I didn't even know you liked girls."
    play sound sfx_throw_something1 volume 1.5
    scene sm1cs-km005-66 hot_in_the_directors_office_mc_talk_cool with hpunch
    play voice3 girl31_angry_ergh2 noloop
    km "I didn't! I mean, I don't."
    km "Read my lips, [mcname]. I don't like girls.{w} And I don't like Veronica."
    scene sm1cs-km005-68 hot_in_the_directors_office_km_talk_panicking with dissolve
    play voice3 girl31_hey_high noloop
    km "I'll prove it to you."
    play sound sfx_jeans_fly1 volume 2.0
    scene sm1cs-km005-69 hot_in_the_directors_office_km_knees with dissolve
    pause
    scene sm1cs-km005-70 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Woah. Hold on, Kellie."
    play sound sfx_throw_something1
    scene sm1cs-km005-71 hot_in_the_directors_office_km_talk_angry with vpunch
    play voice3 girl31_surprised_uh2 noloop
    km "What. Am I not hot enough for you?"
    scene sm1cs-km005-72 hot_in_the_directors_office_km_talk_focus_pants with dissolve
    play voice3 girl31_arrogant_yeah2 noloop
    km "Besides, I know you're a manslut. Veronica already told me how you hooked up."
    km "So now I want a slice."
    play sound sfx_jeans_on1 volume 2.0
    scene sm1cs-km005-73 hot_in_the_directors_office_mc_talk_lookaway with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, that's just pretty surprising. Given everything we've been through."
    scene sm1cs-km005-74 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_surprised_ah1 noloop
    km "Buh..."
    play sound sfx_skirt_off2 volume 2.0
    scene sm1cs-km005-75 hot_in_the_directors_office_mc_talk_notice with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Kellie?{w} Kellie?"
    scene sm1cs-km005-76 hot_in_the_directors_office_km_talk_thinking with dissolve
    play voice3 girl31_angry_ergh8 noloop
    km "Shut up. I'm thinking."
    scene sm1cs-km005-77 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "We don't have to do anything."
    scene sm1cs-km005-78 hot_in_the_directors_office_km_talk_frowns with dissolve
    play voice3 girl31_surprised_oh noloop
    km "Oh, like you don't want to. All those times you helped me to prank Veronica."
    scene sm1cs-km005-79 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_no_no9 noloop
    mc "That wasn't..."
    mct "Well, was it? Did I do those things to help Kellie, or did I do it to get closer to her?"
    mc "All I'm saying is, you don't have to do this if you don't want to."
    play sound sfx_handjob_cream1 loop volume 2.0
    scene sm1cs-km005-80 hot_in_the_directors_office_km_talk_focus_km with dissolve
    play voice3 girl31_arrogant_he noloop
    km "Heh. Easy for you to say. If I don't, you'll keep thinking I'm into Veronica."
    km "I mean that I don't like girls."
    km "I won't let that happen."
    scene sm1cs-km005-a82-1 km-mc-hj-anim-01 with dissolve
    pause
    scene sm1cs_km005-a82-1
    play voisex2 mc_sex_painmoans1
    play voisex3 girl22_sex_closedmoans1
    play sound sfx_handjob_cream1 loop
    mct "Oh wow. She's going really rough at it."
    pause
    mc "Easy there."
    km "What?"
    scene sm1cs_km005-a82-2 with dissolve
    pause
    mc "You're just... nrrggh... It's not a race."
    mc "Eeeowuh."
    mc "You gotta take your time, or you'll just bruise my dick."
    scene sm1cs_km005-a82-1-f with dissolve
    km "Maybe you deserve a little pain, perv."
    pause
    mc "I'm not the one who started this."
    km "Then..."
    scene sm1cs_km005-a82-2-f with dissolve
    km "Teach me."
    mc "Really?"
    km "Tell me what to do. You can do that, at least."
    pause
    stop voisex2 fadeout 1.0
    stop voisex3 fadeout 1.0
    stop sound fadeout 1.0
    scene sm1cs-km005-83 hot_in_the_directors_office_mc_talk_km_onehand with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "Well first, just try to do it with one hand instead of both."
    mc "You were totally mashing it."
    scene sm1cs-km005-84 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_surprised_uh1 noloop
    km "That's not good?"
    scene sm1cs-km005-85 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_no_no5 noloop
    mc "No. It was...{w}. It could just be better."
    scene sm1cs-km005-86 hot_in_the_directors_office_km_talk_base with dissolve
    play voice3 girl31_thinking_mmf2 noloop
    km "Like this."
    scene sm1cs-km005-87 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Even slower. But just a bit."
    scene sm1cs-km005-88 hot_in_the_directors_office_km_talk_horny with dissolve
    play voice3 girl31_disappointed_ehh9 noloop
    km "Maybe it's because your cock is so big."
    scene sm1cs-km005-89 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    mc "I've never heard complaints."
    scene sm1cs-km005-90 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_disappointed_mff2 noloop
    km "Hmmmph. Hey, focus. You're supposed to be teaching me."
    play voisex2 mc_yes_yes1 noloop
    scene sm1cs-km005-a91-1 mc-km-hj-anim-01 with dissolve
    pause
    scene sm1cs_km005-a91-1
    queue voisex2 mc_sex_openmoans2
    play voisex3 girl22_sex_closedmoans1
    play sound sfx_handjob_cream1 loop
    mc "I know. Just keep going like that."
    mc "*softly* There..."
    mc "Just go nice and slow."
    mc "Much better."
    scene sm1cs_km005-a91-2 with dissolve
    mc "If you like, squeezing at the bottom and the top always really gets me going."
    km "You're such a perv."
    mc "I'm not the one who is stalking Veronica on Gram."
    pause
    scene sm1cs_km005-a91-1-f with dissolve
    km "Shut up. Just keep..."
    km "Guiding me I guess."
    mc "You're doing really good. It's a big improvement."
    km "Really?"
    pause
    scene sm1cs_km005-a91-2-f with dissolve
    mc "Yes, Kellie."
    km "You made it sound super hard to do, but I picked it up quickly."
    mc "*chuckles* Well it is {i}pretty{/i} hard."
    km "Oh my god. You're so disgusting. Mrmmmm."
    mc "How about we do a special technique?"
    km "..."
    km "Like what?"
    pause
    stop sound fadeout 1.0
    stop voisex3 fadeout 1.0
    stop voisex2 fadeout 1.0
    scene sm1cs-km005-92 hot_in_the_directors_office_mc_talk_animation end with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "You could..."
    scene sm1cs-km005-93 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_surprised_what3 noloop
    km "I could what?"
    scene sm1cs-km005-94 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "Use your boobs and give me a boobjob."
    scene sm1cs-km005-95 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_surprised_ohmy noloop
    km "Oh my god. You're the worst."
    scene sm1cs-km005-96 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "Says the girls with hard nipples poking at her top."
    scene sm1cs-km005-97 hot_in_the_directors_office_km_thinking with dissolve
    play voice3 girl31_thinking_mmm5 noloop
    pause
    scene sm1cs-km005-98 hot_in_the_directors_office_km_shirt off with dissolve
    pause
    play sound sfx_skirt_off2 volume 1.4
    scene sm1cs-km005-99 hot_in_the_directors_office_km_bra_off with dissolve
    play voice3 girl31_disappointed_mff1 noloop
    km "If you tell anyone about this, I will kill you and bury you under the stage."
    play sound sfx_skirt_off1 volume 1.5
    scene sm1cs-km005-100 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I'll take this one to the grave, Kellie."
    play sound sfx_handjob_cream1 loop
    scene sm1cs-km005-101 hot_in_the_directors_office_km_talk_position with dissolve
    play voice3 girl31_thinking_emm3 noloop
    km "So I just... go in like this?"
    scene sm1cs-km005-102 hot_in_the_directors_office_mc_talk_moan with dissolve
    play voisex2 mc_sex_openmoans1 noloop
    mc "*moans softly*"
    scene sm1cs-km005-103 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_surprised_huh1 noloop
    km "Did I hurt you?"
    scene sm1cs-km005-104 hot_in_the_directors_office_mc_talk with dissolve
    play voisex2 mc_no_no2 noloop
    mc "No. It's great, Kellie."
    scene sm1cs-km005-105 hot_in_the_directors_office_km_talk_smile with dissolve
    play voice3 girl31_happy_relief noloop
    km "Thank you. So... what do I do next?"
    scene sm1cs-km005-106 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_thinking_wait3 noloop
    mc "Wait, you've never done a boobjob?"
    scene sm1cs-km005-107 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_surprised_why5 noloop volume 0.7
    km "I hadn't done a handjob until now too, why do you think I've done a boobjob?"
    scene sm1cs-km005-108 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_angry_errr6 noloop
    mc "I mean, it's just because of how amazing your tits are."
    scene sm1cs-km005-109 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_disappointed_ehh4 noloop
    km "Mrmmm...{w} Just tell me what I should be doing so we can be done."
    scene sm1cs-km005-110 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 d9s2_ugu noloop volume 1.6
    mc "Okay. Well I guess you just kind of squeeze your tits together like they're bread for a sandwich."
    scene sm1cs-km005-111 hot_in_the_directors_office_km_talk with dissolve
    play voice3 kanya_sex_closedmoan3 noloop
    km "And your...{w} cock is the meat."
    scene sm1cs-km005-112 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Bingo."
    scene sm1cs-km005-a114-1 mc-km-boobjob-anim-01 with dissolve
    pause
    scene sm1cs_km005-a114-1
    play voisex2 mc_sex_openmoans2
    play voisex3 girl22_sex_closedmoans1
    play sound sfx_handjob_cream1 loop
    mc "That's the good stuff."
    mc "Oh momma."
    pause
    scene sm1cs_km005-a114-2 with dissolve
    km "Don't be gross, [mcname]."
    mc "Haha. Sorry. Your tits just feel really good."
    km "Don't tease me."
    pause
    scene sm1cs_km005-a114-3 with dissolve
    mc "I'm not. Your tits are really perfect for this."
    km "..."
    pause
    scene sm1cs_km005-a114-4 with dissolve
    km "What about Veronica?"
    mc "Huh?"
    km "Does Veronica give good boobjobs? Does she enjoy that?"
    pause
    scene sm1cs_km005-a114-1-f with dissolve
    mc "Uhmmm. We haven't done one."
    mc "To tell you the truth, I think you get the gold medal for this between you two."
    pause
    scene sm1cs_km005-a114-2-f with dissolve
    mc "You've got quite the unfair advantage."
    km "Why?"
    km "Oh."
    pause
    scene sm1cs_km005-a114-3-f with dissolve
    km "Hehehe. I guess so."
    pause
    scene sm1cs_km005-a114-4-f with dissolve
    play voisex2 mc_sex_openmoans3
    mc "Oh shit. Keep going."
    mc "You're going to make me cum."
    pause
    play voisex3 girl31_scared_ah3 noloop
    play voisex2 mc_sex_orgasm4 noloop
    play sound mc_cum_sound1 volume 2.0
    scene sm1cs-km005-116 hot_in_the_directors_office_mc_talk_cum_km_backoff with hpunch
    mc "Wha-"
    play sound mc_cum_sound1 volume 2.0
    scene sm1cs-km005-117 hot_in_the_directors_office_mc_talk_cum_desk with dissolve
    mc "Gruaaah."
    scene sm1cs-km005-118 hot_in_the_directors_office_km_talk_cum_desk with dissolve
    play voice3 girl31_surprised_ah2 noloop
    km "*gasping*"
    stop voisex2 fadeout 1.0
    scene sm1cs-km005-119 hot_in_the_directors_office_mc_talk_recover with dissolve
    play voice2 d7s4_mcbreathing noloop volume 2.0
    mc "*heavy breathing*"
    menu:
        "Why did you do that?"(hint="sm1cs_km005_m01_h01"):
            scene sm1cs-km005-120 hot_in_the_directors_office_mc_talk_why_menu with dissolve
            play voice2 mc_angry_oof noloop
            mc "Why did you pull away at the last minute?"
            scene sm1cs-km005-121 hot_in_the_directors_office_km_talk_why_menu with dissolve
            play voice3 girl31_disappointed_ehh6 noloop
            km "I don't know. I didn't want your cum all over my face and tits."
            scene sm1cs-km005-122 hot_in_the_directors_office_km_talk_why_menu_notice_cum with dissolve
            play voice3 girl31_arrogant_pff noloop
            km "Oh my god."
        "That was good. But now we've got a little mess to clean up."(hint="sm1cs_km005_m01_h02"):
            call sm1cs_km005_m01_c02 from _call_sm1cs_km005_m01_c02
            scene sm1cs-km005-123 hot_in_the_directors_office_mc_talk_good_menu_smile with dissolve
            play voice2 mc_happy_oof1 noloop
            mc "That felt so good, Kellie."
            scene sm1cs-km005-124 hot_in_the_directors_office_mc_talk_good_menu_lookcum with dissolve
            play voice2 mc_thinking_hmm3 noloop
            mc "Now we just have a little mess to clean up."
            scene sm1cs-km005-125 hot_in_the_directors_office_km_talk_good_menu with dissolve
            play voice3 girl31_surprised_huh2 noloop
            km "Huh?"
    scene sm1cs-km005-126 hot_in_the_directors_office_km_talk_bothhandsmouth with dissolve
    play voice3 girl31_scared_ah6 noloop
    km "This can't be happening."
    km "Denise is going to kill me."
    scene sm1cs-km005-127 hot_in_the_directors_office_mc_talk_wave with dissolve
    play voice2 mc_no_nono1 noloop
    mc "It's okay. It's not my first rodeo."
    scene sm1cs-km005-128 hot_in_the_directors_office_mc_talk_look_bottle_tissue with dissolve
    pause
    play sound sfx_bottle_pouring1
    scene sm1cs-km005-129 hot_in_the_directors_office_mc_talk_tissue_bottle with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Here goes nothing. Watch the door, make sure Denise isn't coming."
    scene sm1cs-km005-130 hot_in_the_directors_office_km_talk_tissue_bottle with dissolve
    play voice3 girl31_yes_simple2 noloop
    km "Okay."
    scene sm1cs-km005-131 hot_in_the_directors_office_km_talk_door_worriedbreathing with dissolve
    play voice3 girl15_angry_breath noloop
    km "*worried breathing*"
    play sound sfx_paint_smearing1
    scene sm1cs-km005-132 hot_in_the_directors_office_mc_talk_finishing with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Little elbow grease."
    scene sm1cs-km005-133 hot_in_the_directors_office_mc_talk_cum gone with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "And we're golden."
    play sound sfx_heels_steps2 loop
    scene sm1cs-km005-134 hot_in_the_directors_office_mc_talk_putaway_noticeundressed with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "Kellie."
    stop sound fadeout 1.0
    scene sm1cs-km005-135 hot_in_the_directors_office_km_talk_worried with dissolve
    play voice3 girl31_disappointed_ehh1 noloop
    km "What?"
    scene sm1cs-km005-136 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "You gotta get dressed."
    scene sm1cs-km005-137 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_scared_ah8 noloop
    km "Oh shit."
    play sound sfx_cloth_rustling2
    play sound2 sfx_jeans_on1 noloop
    $ renpy.music.set_volume(0.5, 3.0, "music" )
    scene sm1cs-km005-138 hot_in_the_directors_office_getting_dressed with dissolve
    pause
    scene sm1cs-km005-139 hot_in_the_directors_office_km_talk_shirt with dissolve
    play voice3 girl31_hey_angry noloop
    km "Promise me."
    km "Promise me that you won't tell Veronica I was looking through her stuff, [mcname]."
    scene sm1cs-km005-140 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_no_no6 noloop
    mc "I don't think I can do that."
    mc "You really should just talk to her about this, Kellie."
    scene sm1cs-km005-141 hot_in_the_directors_office_mc_talk_depressed with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "It's no good keeping this sort of thing bottled up."
    scene sm1cs-km005-142 hot_in_the_directors_office_km_talk_thinks with dissolve
    play voice3 girl31_arrogant_ha noloop
    km "Like you know anything about pining after someone who barely notices you."
    scene sm1cs-km005-143 hot_in_the_directors_office_mc_talk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "You'd actually be surprised."
    mc "This doubt. It's all mental, Kellie. And if you like Veronica, like, really like her."
    mc "You owe it to yourself to at least try."
    scene sm1cs-km005-144 hot_in_the_directors_office_km_talk_thinking with dissolve
    play voice3 girl31_happy_yeah4 noloop
    km "Or I can just keep avoiding her."
    scene sm1cs-km005-145 hot_in_the_directors_office_mc_talk_annoyed with dissolve
    play voice2 mc_surprised_what4 noloop
    mc "No. What? I thought we were past this?"
    scene sm1cs-km005-146 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_no_nope2 noloop
    km "Nope. I like my way better."
    scene sm1cs-km005-147 hot_in_the_directors_office_mc_talk_palm with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "You two work together in a theater troupe."
    scene sm1cs-km005-148 hot_in_the_directors_office_km_talk with dissolve
    play voice3 girl31_disappointed_ehh7 noloop
    km "Maybe I'll just quit and I'll never have to embarrass myself in front of her."
    km "That way, I can go find a new job and eventually..."
    km "*sadly* Forget all about her."
    play sound sfx_heels_steps2 loop
    scene sm1cs-km005-149 hot_in_the_directors_office_km_talk_walkdoor with dissolve
    play voice3 girl31_hey_bye1 noloop
    km "I have to go, [mcname]."
    scene sm1cs-km005-151 hot_in_the_directors_office_mc_talk_thinking with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "I should talk to Denise about getting the AC checked in the theater."
    mct "I swear there must be something in the air that makes this place insane."
    play sound2 sfx_door_openclosed1 noloop
    play sound sfx_heels_steps1 fadein 3.0
    scene sm1cs-km005-152 hot_in_the_directors_office_mc_talk_thinking_hallway with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "Maybe it's just the magic of the theater that brings out the drama."
    mct "There has to be a way that I can fix things between Kellie and Veronica."
    mct "Or at least, a way for me to get them back to normal."
    stop sound fadeout 3.0
    scene sm1cs-km005-153 hot_in_the_directors_office_mc_talk_thinking_hallway with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mct "Well, I certainly didn't think Kellie would change her mind about Veronica in this direction."
    mct "What if this has been the case the whole time?"
    scene sm1cs-km005-154 hot_in_the_directors_office_mc_talk_thinking_hallway_corner with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "Was she jealous of Veronica, or was she just wanting to get Veronica's attention and she didn't know what to do?"
    mct "Well, I guess the only thing to do is to tell Veronica about this new development."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1cs_km005_end
label sm1cs_km005_end:
    $ StoryController.end_scene(KM_STORY, 2, 0, 3, THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR)
    return
label sm1cs_km005_m01_c02:
    $ player.set_choice("sm1cs_km005_that_was_good")
    $ CharacterController.get_character("km").add_point()
    return