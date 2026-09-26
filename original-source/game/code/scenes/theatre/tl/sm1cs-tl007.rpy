image sm1cs_tl007-glambot-1 = Movie(play = "images/FS_T/TL/s007/anim/sm1cs-tl007-a66-2x-50fps.webm", start_image = "sm1cs-tl007-a66 mc-sy-look2-glambot-_c1_nn", image = "sm1cs-tl007-a66 mc-sy-look2-glambot-00089_nn", loop = False)
label sm1cs_tl007:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 1.0, "music" )
    play sound sfx_door_closed1
    play sound2 sfx_heels_steps2
    scene sm1cs-tl007-01 mc-sy-entry_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Stacy!"
    play voice3 stacy_arrogant_ha2_muffled noloop
    sy "In the bathroom, [mcname]!"
    scene sm1cs-tl007-02 mc-sy-entry2_c1 with dissolve
    pause
    play sound2 sfx_door_creak2 noloop
    play sound sfx_tap_water1 loop
    play sound3 sfx_shower_ambience1
    scene sm1cs-tl007-03 mc-sy-look_c1 with dissolve
    play voice2 mc_surprised_wtf1 noloop
    mc "What's the-"
    play voice3 stacy_scared_ah1 noloop
    play music music_stacy_time
    play sound sfx_water_hosepipe1 volume 1.6 loop
    scene sm1cs-tl007-01 mc-sy-entry_c2 with vpunch
    sy "This isn't my fault, I swear!"
    scene sm1cs-tl007-04 mc-sy-ask_c1 with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "What the hell happened!?"
    scene sm1cs-tl007-04 mc-sy-ask_c2 with dissolve
    play voice3 stacy_pain_sobs1 noloop
    sy "I don't know!{w} I just came in here to shower, and then water started spraying everywhere, and-"
    scene sm1cs-tl007-05 mc-sy-look_c2 with dissolve
    play voice3 stacy_pain_au2 noloop
    sy "Halp."
    scene sm1cs-tl007-05 mc-sy-look_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "All right, well let's see what I can do..."
    play sound2 sfx_hammer_loop1
    scene sm1cs-tl007-06 mc-sy-pause_c1 with dissolve
    pause
    play sound2 sfx_wrench_long1 noloop
    scene sm1cs-tl007-07 mc-sy-pause2_c1 with dissolve
    pause
    scene sm1cs-tl007-08 mc-sy-pause3_c1 with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound fadeout 1.0
    scene sm1cs-tl007-09 mc-sy-talk_c2 with fade
    play voice3 stacy_surprised_huh3 noloop
    sy "Didn't we already try that, [mcname]?"
    scene sm1cs-tl007-09 mc-sy-talk_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I don't know, maybe? But I have no idea what I'm doing."
    scene sm1cs-tl007-10 mc-sy-talk2_c2 with dissolve
    call knock from _call_knock_5
    play voice3 stacy_surprised_oh1 noloop
    sy "Were you expecting company?"
    play voice2 mc_surprised_uh1 noloop
    mc "Huh?"
    sy "Don't worry, I got it!"
    scene sm1cs-tl007-10 mc-sy-talk2_c1 with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, Stacy-"
    stop sound3 fadeout 1.0
    play sound sfx_door_open1
    scene sm1cs-tl007-11 mc-sy-door_c1 with dissolve
    play voice3 stacy_hey_happy1 noloop
    sy "Hi!"
    play sound sfx_door_creak4
    scene sm1cs-tl007-12 mc-sy-door2_c2 with dissolve
    play voice4 girl24_arrogant_huh2 noloop
    tl "Do you always come to the door, butt-ass naked?"
    scene sm1cs-tl007-12 mc-sy-door2_c1 with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "Wait-"
    scene sm1cs-tl007-13 mc-sy-door3_c1 with dissolve
    play voice3 stacy_scared_ah4 noloop
    sy "Holy shit, I totally forgot I wasn't wearing clothes!"
    play voice3 stacy_hey noloop
    play sound sfx_barefoot_run1 volume 1.5
    play sound2 sfx_door_closed1 noloop
    scene sm1cs-tl007-14 mc-sy-run_c1 with hpunch
    sy "[mcname]!{w} Taisia is here!"
    scene sm1cs-tl007-14 mc-sy-run_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-tl007-15 mc-sy-look_c1 with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Hey, Taisia. What's up?"
    scene sm1cs-tl007-15 mc-sy-look_c2 with dissolve
    play voice4 girl24_thinking_emm1 noloop
    tl "Uhhh, I'm moving in?"
    play sound sfx_heels_steps2 loop
    scene sm1cs-tl007-16 mc-sy-walk_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Wait - shit."
    play sound sfx_cloth_rustling2
    play sound3 sfx_shower_ambience1 fadein 1.0
    scene sm1cs-tl007-16 mc-sy-walk_c3 with dissolve
    play voice3 stacy_surprised_huh4 noloop
    sy "You're moving in!?{w} Today!?!"
    stop sound3 fadeout 1.0
    scene sm1cs-tl007-17 mc-sy-ask_c2 with dissolve
    play voice4 girl24_arrogant_yeah2 noloop
    tl "Yeah, I told [mcname] earlier today at the theater.{w} Did you forget? I literally told you like two hours ago."
    play voice2 d2s9_confused noloop volume 1.7
    mc "Uhm..."
    tl "Why the hell are you soaking wet?"
    play sound sfx_barefoot_steps1
    scene sm1cs-tl007-17 mc-sy-ask_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.8
    mc "Somehow Stacy broke one of our pipes."
    stop sound fadeout 1.0
    scene sm1cs-tl007-18 mc-sy-talk_c2 with dissolve
    play voice3 stacy_no_angry2 noloop
    sy "It wasn't my fault!"
    scene sm1cs-tl007-18 mc-sy-talk_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Uh huh, suuuuuuurrrrrrre."
    play voice3 stacy_angry_aah1 noloop
    sy "It wasn't!"
    play sound sfx_armored_whoosh1
    scene sm1cs-tl007-19 mc-sy-talk2_c2 with dissolve
    play voice4 girl24_arrogant_hm1 noloop
    tl "Give me that."
    play voice2 mc_surprised_huh7 noloop
    mc "What're you doing?"
    tl "Just - shut up."
    play sound sfx_heels_steps1 loop
    play sound3 sfx_shower_ambience1 fadein 1.0
    scene sm1cs-tl007-20 mc-sy-walk_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I've tried, like, everything-"
    play voice2 mc_surprised_what3 noloop
    stop sound3 fadeout 1.0
    play sound sfx_armored_whoosh2
    play sound2 sfx_shower_off1 noloop
    play sound4 sfx_wrench_long1 noloop
    scene sm1cs-tl007-21 mc-sy-look_c1 with vpunch
    mc "Wait... what? How'd you do that?"
    stop sound4 fadeout 1.0
    play sound sfx_heels_steps1
    scene sm1cs-tl007-22 mc-sy-look2_c2 with dissolve
    stop sound fadeout 1.0
    play voice4 girl24_arrogant_kgh1 noloop
    tl "Your connector got loose, and the joint got pinched open. Cleared that, closed it up, bada bing, bada boom."
    scene sm1cs-tl007-22 mc-sy-look2_c1 with dissolve
    play voice2 mc_angry_huh2 noloop volume 1.4
    mc "Huh..."
    scene sm1cs-tl007-23 mc-sy-look3_c1 with dissolve
    play voice3 stacy_happy_phew2 noloop
    sy "Thank God you're moving in."
    scene sm1cs-tl007-23 mc-sy-look3_c2 with dissolve
    play voice4 girl24_arrogant_yeah1 noloop
    tl "Yeah, it looks like you two need all the help you can get."
    tl "One of you want to show me my room?"
    scene sm1cs-tl007-24 mc-sy-ask_c1 with dissolve
    play voice3 stacy_yes noloop
    sy "I can!"
    scene sm1cs-tl007-25 mc-sy-talk_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Maybe you should put some pants on, Stacy."
    play sound sfx_hair_scratch1 volume 1.4
    scene sm1cs-tl007-25 mc-sy-talk_c2 with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "Ughhhh, fine."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-tl007-26 mc-sy-walk_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I'll show you your room, and then get changed myself."
    stop music fadeout 6.0
    scene sm1cs-tl007-27 mc-sy-walk2_c1 with dissolve
    queue music music_lofispers
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-tl007-28 mc-sy-ask_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Are you ready?"
    scene sm1cs-tl007-28 mc-sy-ask_c2 with dissolve
    play voice4 girl24_surprised_huh2 noloop
    tl "For?"
    scene sm1cs-tl007-29 mc-sy-talk_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Your new room!"
    scene sm1cs-tl007-29 mc-sy-talk_c2 with dissolve
    play voice4 girl24_arrogant_yeah3 noloop
    tl "I mean, yeah. That's why I'm here. With my stuff."
    play sound sfx_door_open1
    scene sm1cs-tl007-30 mc-sy-door_c1 with dissolve
    play voice2 mc_happy_wooh1 noloop
    mc "Well, without further ado then-"
    mc "Tadaaaaaaa!"
    scene sm1cs-tl007-30 mc-sy-door_c2 with dissolve
    play voice3 girl24_arrogant_hah noloop
    tl "Sweet. Looks good. Cozy."
    tl "And it's already furnished, which I wasn't expecting. But, sick."
    play sound sfx_heels_steps1
    scene sm1cs-tl007-31 mc-sy-look_c1 with dissolve
    stop sound fadeout 2.5
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, we had a few things laying around. We weren't using them, so we figured we could put them in one of the rooms."
    play voice3 girl24_yes_aga noloop
    tl "Well, I appreciate it."
    scene sm1cs-tl007-32 mc-sy-talk_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Well, cool. I'll let you settle in, and I'm going to go put on some dry clothes."
    scene sm1cs-tl007-32 mc-sy-talk_c2 with dissolve
    play voice3 girl24_thinking_huh1 noloop
    tl "Cool."
    play sound sfx_heels_steps2 loop
    scene sm1cs-tl007-34 mc-sy-walk_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Coooool."
    play sound sfx_skirt_off2
    scene sm1cs-tl007-35 mc-sy-ask_c2 with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "How's Taisia settling in?"
    scene sm1cs-tl007-35 mc-sy-ask_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 1.8
    mc "Good so far."
    play sound sfx_cloth_rustling4
    scene sm1cs-tl007-36 mc-sy-sit_c2 with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Yeah? Does she like the room?"
    scene sm1cs-tl007-36 mc-sy-sit_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "I think so? She seemed nonplussed."
    play sound sfx_cloth_planket2
    scene sm1cs-tl007-37 mc-sy-talk_c2 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Nonplussed?"
    scene sm1cs-tl007-37 mc-sy-talk_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Yeah, you like that? New fancy word I learned."
    scene sm1cs-tl007-37 mc-sy-talk_c2 with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "I... what do you think that word means?"
    scene sm1cs-tl007-38 mc-sy-talk2_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "You know, not excited. Uhhh, apathetic, even."
    scene sm1cs-tl007-38 mc-sy-talk2_c2 with dissolve
    play voice3 stacy_no_nah3 noloop
    sy "I don't think you know what that word means."
    sy "Nonplussed is like, if she's so surprised she has no idea what to do."
    play sound sfx_cloth_rustling5
    scene sm1cs-tl007-39 mc-sy-talk3_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I mean... she didn't seem like she knew what to do?"
    scene sm1cs-tl007-39 mc-sy-talk3_c2 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah, but that doesn't mean she's nonplussed. I think she's just, I don't know, chill?"
    scene sm1cs-tl007-39-1 mc-sy-talk4_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, maybe."
    play sound sfx_heels_steps2 loop
    scene sm1cs-tl007-39-2 mc-sy-walk_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I'm going to go see if she needs any help moving."
    scene sm1cs-tl007-39-2 mc-sy-walk_c2 with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Ooooo, that sounds like hard work. I'm going to... hang out here!"
    play voice2 mc_arrogant_heh2 noloop
    mc "Can't say I'm surprised."
    scene sm1cs-tl007-40 mc-sy-walk_c1 with dissolve
    pause
    play sound sfx_door_creak2
    scene sm1cs-tl007-41 mc-sy-stand_c1 with dissolve
    play sound2 sfx_roller_measure1 noloop
    play voice2 d2s9_mchey noloop volume 1.4
    mc "So, everything to your liking so far?"
    scene sm1cs-tl007-41 mc-sy-stand_c2 with dissolve
    play voice3 girl24_yes_yeah noloop
    tl "Yeah, it's nice in here."
    play sound sfx_socks_dancing2
    scene sm1cs-tl007-42 mc-sy-look_c1 with dissolve
    stop sound fadeout 1.0
    play voice2 mc_thinking_hmm3 noloop
    mc "Do you need any help grabbing your stuff?"
    scene sm1cs-tl007-42 mc-sy-look_c2 with dissolve
    play voice3 girl24_no_nah noloop
    tl "Nah, it's all already here."
    play voice2 mc_surprised_uh3 noloop
    mc "Huh?"
    play voice3 girl24_thinking_mff noloop
    tl "That's all my stuff."
    play sound sfx_skirt_off2
    scene sm1cs-tl007-43 mc-sy-talk_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "That... that can't be {i}all{/i} your stuff."
    play voice3 girl24_surprised_why3 noloop
    tl "Why not?"
    mc "It's just... it's not a lot, is all."
    mc "I was expecting, I don't know. At least two duffel bags."
    scene sm1cs-tl007-43 mc-sy-talk_c2 with dissolve
    play voice3 girl24_thinking_emm2 noloop
    tl "I like to be mobile. Having too much shit slows you down."
    play sound sfx_vending_button
    scene sm1cs-tl007-44 mc-sy-talk2_c2 with dissolve
    play voice3 girl24_disappointed_neh noloop
    tl "And I've also never really had a stable place to live... so there'd be a chance I'd have to ditch half my stuff anyway."
    tl "So, stay light, keep a bag packed, don't get too attached to things or places."
    play sound sfx_heels_steps2
    scene sm1cs-tl007-45 mc-sy-talk3_c1 with dissolve
    stop sound fadeout 2.0
    play voice2 mc_disappointed_ah1 noloop
    mc "Well, hopefully this place will help you break that pattern."
    scene sm1cs-tl007-45 mc-sy-talk3_c2 with dissolve
    play voice3 girl24_yes_yap noloop
    tl "Mmm. That would be nice..."
    scene sm1cs-tl007-46 mc-sy-talk4_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Well, can I help you unpack, or anything?"
    scene sm1cs-tl007-46 mc-sy-talk4_c2 with dissolve
    play voice3 girl24_no_questioning noloop
    tl "Nah, I got it. But could you get me a beer or something?"
    scene sm1cs-tl007-46-2 mc-sy-talk5_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, let me go see what we have in the fridge!"
    play sound sfx_heels_steps2 loop
    scene sm1cs-tl007-47 mc-sy-walk_c1 with dissolve
    pause
    play sound sfx_cloth_rustling1
    scene sm1cs-tl007-48 mc-sy-close_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "Man, I never realized how... tough Taisia's life has been."
    mct "Having to move from place to place... that's no way to live."
    scene sm1cs-tl007-49 mc-sy-look_c1 with dissolve
    mct "I should work hard to make this a decent place for her. Be a good landlord."
    mct "Right, I guess I'm kind of a landlord now."
    play sound [sfx_fridge_open1, sfx_fridge_closed1]
    scene sm1cs-tl007-50 mc-sy-bear_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mct "That's going to be something I have to think about going forward."
    play sound2 sfx_heels_steps2
    scene sm1cs-tl007-51 mc-sy-walk_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mct "Who would've thought, me - a landlord."
    mct "What a time to be alive."
    stop sound2 fadeout 1.0
    scene sm1cs-tl007-52 mc-sy-stand_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "You're in luck, we had some beers tucked in the back of the fridge."
    scene sm1cs-tl007-53 mc-sy-look_c1 with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Damn, that was fast!"
    play sound sfx_glass_bottle_bonk
    scene sm1cs-tl007-54 mc-sy-bear_c2 with dissolve
    play voice3 girl24_yes_ugu noloop
    tl "I've had lots of practice."
    tl "Thanks."
    play sound sfx_beer_open1
    scene sm1cs-tl007-55 mc-sy-bear2_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "No problem."
    scene sm1cs-tl007-56 mc-sy-sip_c2 with dissolve
    play sound2 sfx_drink_loop1
    play voice3 girl24_disappointed_oh noloop
    tl "And thanks for the spot. I... {w}appreciate it, [mcname]."
    scene sm1cs-tl007-56 mc-sy-sip_c1 with dissolve
    play voice2 mc_no_nono1 noloop
    mc "It's not a problem, Taisia. I'm happy this worked out!"
    tl "Come inside..."
    play sound sfx_heels_steps1
    play sound2 sfx_heels_steps2
    scene sm1cs-tl007-57 mc-sy-walk_c2 with dissolve
    play voice3 girl24_arrogant_huh1 noloop
    if persistent.is_special:
        tl "So, you and your sister, huh."
    else:
        tl "So, you and Stacy, huh."
    play sound sfx_cloth_rustling4
    play sound2 sfx_chair_slide1 noloop
    scene sm1cs-tl007-58 mc-sy-sits_c1 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, uhm..."
    scene sm1cs-tl007-58 mc-sy-sits_c2 with dissolve
    play voice3 girl24_hey_sexy noloop
    tl "You don't need to stress, [mcname]. It's chill."
    tl "She's hot, I get it."
    if persistent.is_special:
        tl "If she was my sister, I'd fuck her too."
    else:
        tl "She's hot as fuck, and if I lived with her, I'd fuck her too."
    scene sm1cs-tl007-59 mc-sy-look_c1 with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "Well, now that you live here, there's a pretty good chance you'll have another chance to end up in bed with her."
    play voice3 girl24_arrogant_hm2 noloop
    tl "I wouldn't mind a repeat of the bar.{w} That was pretty hot."
    mc "Yeah, I had a good time too."
    scene sm1cs-tl007-59 mc-sy-look_c2 with dissolve
    play voice3 girl24_surprised_eeh2 noloop
    tl "Well, anytime you're both free..."
    tl "Or if you're ever bored.{w} You know how I like {i}it{/i}."
    scene sm1cs-tl007-58 mc-sy-sits_c1 with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "That I do. But, this doesn't have to feel like the playboy mansion."
    mc "The most important thing I want is for you to have a place you can relax at and do whatever you like."
    scene sm1cs-tl007-58 mc-sy-sits_c2 with dissolve
    play voice3 girl24_thinking_hmm5 noloop
    tl "Thanks, [mcname]. I get you."
    play sound sfx_cloth_rustling1
    scene sm1cs-tl007-60 mc-sy-stand_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Well I'm going to check in with Stacy. Yell if you need anything."
    scene sm1cs-tl007-60 mc-sy-stand_c2 with dissolve
    play voice3 girl24_yes_simple1 noloop
    tl "Will do."
    play sound sfx_carpet_footsteps1 loop
    scene sm1cs-tl007-61 mc-sy-walk_c1 with dissolve
    pause
    stop sound fadeout 0.2
    scene sm1cs-tl007-62 mc-sy-look_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, and thanks for helping out with the bathroom.{w} I think I would have drowned before I got the sink fixed."
    play voice3 girl24_happy_laugh1 noloop
    tl "Happy to help. And if you ever need more shit done around the studio, I'm down to help with that."
    mc "I'll keep that in mind!"
    play sound sfx_heels_steps2 loop
    scene sm1cs-tl007-63 mc-sy-walk_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "I think having Taisia around is going to be good for us."
    stop sound fadeout 1.0
    scene sm1cs-tl007-65 mc-sy-look_c2 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "So, how's she settling in?"
    scene sm1cs-tl007-65 mc-sy-look_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Good. She's already unpacked and chilling."
    play voice3 stacy_thinking_emm3 noloop
    sy "Wait, she's already got all of her stuff here?"
    mc "Yeah, she doesn't have a lot, apparently."
    play sound2 sfx_door_open1 noloop
    scene sm1cs-tl007-a66 mc-sy-look2-glambot-_c1_nn with dissolve
    pause 0.1
    play sound sfx_camera_fly1 volume 2.0
    scene sm1cs_tl007-glambot-1
    pause
    stop sound fadeout 1.0
    scene sm1cs-tl007-66 mc-sy-look2_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "Damn..."
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah. But otherwise she seems happy with the spot!"
    sy "Good! I'm glad she likes it."
    play sound2 sfx_barefoot_steps1
    scene sm1cs-tl007-66 mc-sy-look2_c2 with dissolve
    pause
    stop sound2 fadeout 1.0
    scene sm1cs-tl007-67 mc-sy-look3_c2 with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Mmmm, I think I'm going to like having more roommates."
    scene sm1cs-tl007-68 mc-sy-stand_c1 with dissolve
    play sound sfx_cloth_rustling2
    play voice2 mc_yes_yes6 noloop
    mc "I definitely don't think I'm going to have too many complaints."
    mc "Except when I need to shower."
    scene sm1cs-tl007-68 mc-sy-stand_c2 with dissolve
    play voice3 stacy_scared_oof1 noloop
    sy "Oh shit, showering!"
    sy "I was going to shower, I have to get in there before we run out of hot water!"
    play sound sfx_heels_steps1
    scene sm1cs-tl007-69 mc-sy-walk_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "I don't think we're going to magically run out of hot water?"
    scene sm1cs-tl007-69 mc-sy-walk_c2 with dissolve
    play voice3 stacy_uhuh noloop
    sy "We have a roommate, [mcname]! That's never a guarantee now!"
    scene sm1cs-tl007-70 mc-sy-walk2_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Stacy, Stacy, Stacy... what would I do without you?"
    scene black with dissolve
    jump sm1cs_tl007_end_scene
label sm1cs_tl007_end_scene:
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1.0, 1.5, "music" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    stop music fadeout 3.0
    call sm1cs_tl007_moved_in_unlocks from _call_sm1cs_tl007_moved_in_unlocks
    $ StoryController.end_scene(TL_STORY, 3, 0, 5, STUDIO, DEFAULT_SUBLOCATION, SD_KITCHEN)
    return
label sm1cs_tl007_moved_in_unlocks:
    python:
        LocationController.get_location(STUDIO, SD_SUB_TAISIA, SD_TAISIA).discover()
        LocationController.get_location(STUDIO, SD_SUB_TAISIA, SD_TAISIA).unlock()
        CharacterController.get_character("tl").add_point(3) 
        CharacterController.get_character("tl").add_schedule("default_tl2")
        CharacterController.get_character("tl").remove_schedule("default_tl")

    return