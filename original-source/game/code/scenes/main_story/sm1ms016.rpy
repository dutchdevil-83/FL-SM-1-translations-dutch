image sm1ms016-a61-glm = Movie(play = "images/ms/s016/anim/sm1ms016-a61-3x-60fps.webm", start_image = "sm1ms016-a61 sy-slide-glambot-000", image = "sm1ms016-a61 sy-slide-glambot-120", loop = False)
label sm1ms016:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    scene sm1ms016-01 mc-sy-sy-entry1_c1 with dissolve
    play music music_newdayoflife fadein 0.5
    play voice2 d1s5_mchappy noloop
    mct "Alright, time to continue working on the renovation."
    play voice2 sfx_sneeze1 noloop
    scene sm1ms016-02 mc-sy-sy-entry2_c1 with hpunch
    mc "Achooo!"
    scene sm1ms016-02 mc-sy-sy-entry2_c2 with dissolve
    play voice4 girl34_surprised_oh3 noloop
    my "God bless you."
    play sound sfx_nose_blowing1
    scene sm1ms016-03 mc-sy-sy-entry3_c1 with dissolve
    play sound2 sfx_cloth_rustling1 noloop
    stop sound fadeout 0.8
    play voice2 ["<silence 0.3>", mc_angry_off] noloop
    if persistent.is_special:
        mc "Thanks, Mom."
    else:
        mc "Thank you."
    play sound sfx_heels_steps1
    scene sm1ms016-06 mc-sy-sy-look_c1 with dissolve
    stop sound fadeout 2.5
    play voice2 mc_arrogant_heh1 noloop
    mct "Well the place is certainly turning out nice."
    mct "But we still have a long way to go."
    mct "And the dust. I can't believe how much there can be sometimes."
    mct "We vacuum each day, and it's still like my nose hairs are coated in the shit."
    scene sm1ms016-05 mc-sy-sy-ask_c2 with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "You going to survive over there?"
    scene sm1ms016-02 mc-sy-sy-entry2_c1 with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "I hope so."
    mc "Almost done."
    play sound sfx_keyboard_typing2
    scene sm1ms016-04 mc-sy-sy-entry4_c2 with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Mmm. Maybe halfway done."
    sy "But each day we're making progress."
    play sound d14s16_smell
    scene sm1ms016-03 mc-sy-sy-entry3_c1 with dissolve
    stop sound fadeout 1.0
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. I just wish we could snap our fingers and be done."
    mc "Hopefully then I'll stop waking up with dust in my nose."
    play sound sfx_heels_steps2 loop
    scene sm1ms016-11 mc-sy-sy-talk_c2 with dissolve
    play voice4 girl34_disappointed_eeh1 noloop
    my "I shouldn't say anything, but if you went back to your old dorm, you probably wouldn't be having this issue."
    scene sm1ms016-12 mc-sy-sy-talk2_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    if persistent.is_special:
        mc "I thought that we were getting past this, Mom?"
    else:
        mc "Melony, I thought that we were moving past this?"
    scene sm1ms016-12 mc-sy-sy-talk2_c2 with dissolve
    play voice4 girl34_arrogant_yeah noloop
    my "I know I know. You've have made up your mind."
    my "But it is just important to keep other options open."
    my "You never want to wake up one day and only have one path forward."
    scene sm1ms016-15 mc-sy-sy-talk5_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Mmm. There is some wisdom to that."
    stop sound fadeout 1.0
    scene sm1ms016-14 mc-sy-sy-talk4_c3 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "What are you talking about?"
    sy "We... I mean {i}you've{/i} already come this far."
    scene sm1ms016-14 mc-sy-sy-talk4_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah. I'm not stopping for anything."
    mc "But nothing is saying that this place wouldn't be a great apartment once we're done."
    mc "No matter what we're using it for."
    scene sm1ms016-15 mc-sy-sy-talk5_c3 with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "Well, and you just gotta keep moving forward on the renovation."
    sy "Especially since we're getting the stairs in today."
    sy "Once those are in, this place will really start taking shape."
    scene sm1ms016-15 mc-sy-sy-talk5_c2 with dissolve
    play voice4 girl34_yes_aga4 noloop
    my "That will be nice."
    my "Then you can finally stop sleeping on the floor and set up in one of the rooms upstairs."
    play voice2 d3s11b_mcheh noloop
    mct "Haha. Yeah, she doesn't know that Stacy and I are planning to make a nice love nest upstairs."
    play sound sfx_heels_steps1 loop
    scene sm1ms016-16 mc-sy-sy-stand_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Totally."
    stop sound fadeout 2.0
    scene sm1ms016-16 mc-sy-sy-stand_c2 with dissolve
    play voice3 amrose_old_psst2 noloop
    sy "*whispers* I can't wait till we're done so she can finally leave us alone."
    scene sm1ms016-17 mc-sy-sy-look_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "*whispers* Hey be nice. She just wants the best for us."
    mc "*whispers* And she's going to make that painting for us. I think it's a sign she's coming around."
    scene sm1ms016-18 mc-sy-sy-talk_c3 with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "*whispers* I hope you're right about that."
    sy "*whispers* But she's really cramping my style."
    sy "*whispers* With her over all the time, there is hardly time for you to smash my booty."
    play sound sfx_cloth_rustling2
    scene sm1ms016-19 mc-sy-sy-talk2_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "*whispers* Patience. We'll be sure to catch up once she's out of our hair."
    scene sm1ms016-19 mc-sy-sy-talk2_c2 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "*whispers* I'll hold you to that."
    sy "*whispers* Alright, why don't you go make sure she's not up to no good."
    sy "*whispers* I'm pretty sure I saw her eyeing my bras earlier."
    scene sm1ms016-20 mc-sy-sy-talk3_c2 with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "*whispers* I think she thinks they're too racy. I'm worried she's going to burn them or give them away."
    scene sm1ms016-21 mc-sy-sy-talk4_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "*whispers* Alright."
    play sound sfx_heels_steps2
    scene sm1ms016-25 mc-sy-sy-talk2_c1 with dissolve
    stop sound fadeout 1.0
    play sound2 sfx_brush_painting2
    play voice2 mc_surprised_wow3 noloop
    mc "This coming along nicely."
    scene sm1ms016-25 mc-sy-sy-talk2_c2 with dissolve
    play voice4 girl34_yes_ugu2 noloop
    my "Thank you."
    my "Stacy had such specific instructions for what she wanted to see."
    scene sm1ms016-26 mc-sy-sy-talk3_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Yeah, I think she'll love it. {w}I almost forgot how good you are at art."
    scene sm1ms016-26 mc-sy-sy-talk3_c2 with dissolve
    play voice4 girl34_disappointed_oh2 noloop
    my "Oh this is nothing. Some of the artists working in my gallery would be much better suited for this."
    scene sm1ms016-27 mc-sy-sy-talk4_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "You shouldn't sell yourself short."
    scene sm1ms016-27 mc-sy-sy-talk4_c2 with dissolve
    play voice4 girl34_yes_yeap1 noloop
    my "I could say the same about you."
    scene sm1ms016-28 mc-sy-sy-talk5_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What's that supposed to mean?"
    queue sound2 sfx_brush_painting3
    scene sm1ms016-28 mc-sy-sy-talk5_c2 with dissolve
    play voice4 girl34_disappointed_eeh2 noloop
    my "Nothing."
    my "Just me looking out for you."
    scene sm1ms016-29 mc-sy-sy-look_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "I know it still seems risky, but I am going to succeed."
    mc "Trust me."
    scene sm1ms016-29 mc-sy-sy-look_c2 with dissolve
    play voice4 girl34_disappointed_huh noloop
    my "I..."
    my "I do trust you, [mcname]."
    my "But... well at the end of the day, what you're trying to do is..."
    my "Well, some might call it a form of art."
    queue sound2 sfx_brush_painting4
    scene sm1ms016-30 mc-sy-sy-look2_c2 with dissolve
    play voice4 girl34_disappointed_oof1 noloop
    my "Speaking of {i}your{/i} art, I just realized another problem."
    scene sm1ms016-30 mc-sy-sy-look2_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "What is it?"
    scene sm1ms016-30 mc-sy-sy-look2_c2 with dissolve
    play voice4 girl34_thinking_emm1 noloop
    my "Well if you making adult films, then you're going to need... well actresses, I guess."
    my "And you can't just go and find sexy girls on the internet to film with. You need people that you can trust."
    scene sm1ms016-31 mc-sy-sy-talk_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "I've already got that handled."
    scene sm1ms016-31 mc-sy-sy-talk_c2 with dissolve
    play voice4 girl34_surprised_what4 noloop
    my "What? What do you mean?"
    scene sm1ms016-32 mc-sy-sy-talk2_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "I know people from Fetish Locator. And people from college."
    mc "But I'm also hoping to meet people at my jobs who might be interested."
    if player.has_played_scene("sm1ms015"):
        scene sm1ms016-34 mc-sy-sy-talk4_c1 with dissolve
        play voice2 mc_thinking_hmm1 noloop
        mc "According to some Fetish Locator data, a lot of people at the IT office used the app."
        mc "Obviously, my first priority is just the work. But I'm keeping my ears open to see if anyone is interested in joining the team here."
        scene sm1ms016-34 mc-sy-sy-talk4_c2 with dissolve
        play voice4 girl34_thinking_hmm2 noloop
        my "Alright. I supposed everyone needs some extra money these days."
        my "But make sure you don't corrupt people. Especially that shy girl Nari. She's so sweet and cute."
        queue sound2 sfx_brush_painting5
        scene sm1ms016-36 mc-sy-sy-look_c1 with dissolve
        play voice2 mc_yes_sure1 noloop
        mc "Of course. I'd never ask someone to do something they aren't comfortable with."
        scene sm1ms016-35 mc-sy-sy-talk5_c1 with dissolve
        play voice4 girl34_yes_ugu1 noloop
        my "Good."
    else:
        scene sm1ms016-34 mc-sy-sy-talk4_c1 with dissolve
        mc "The theater is kind of the perfect place for me to find like-minded people."
        mc "Most of the people are already actors, and plenty could use the work."
        scene sm1ms016-34 mc-sy-sy-talk4_c2 with dissolve
        play voice4 girl34_thinking_hmm2 noloop
        my "Well, you're not wrong about that. I've certainly met more starving actors than starving artists."
        my "But just be sure you're not pushing your business on people who don't want it."
        my "Like that Veronica girl. She's so kind and eager."
        queue sound2 sfx_brush_painting5
        scene sm1ms016-35 mc-sy-sy-talk5_c1 with dissolve
        play voice4 girl34_yes_yeah5 noloop
        my "You shouldn't do anything that might risk her acting career."
        scene sm1ms016-36 mc-sy-sy-look_c1 with dissolve
        play voice2 mc_yes_sure1 noloop
        mc "Of course. I'd never ask someone to do something they aren't comfortable with."
        scene sm1ms016-37 mc-sy-sy-look2_c2 with dissolve
        play voice4 girl34_yes_ugu1 noloop
        my "Good."
    my "Maybe I was acting too rash earlier."
    stop sound2 fadeout 1.0
    scene sm1ms016-38 mc-sy-sy-ask_c1 with dissolve
    mc "It's okay. You're looking out for me. I get it."
    scene sm1ms016-38 mc-sy-sy-ask_c2 with dissolve
    play voice4 girl34_happy_relief3 noloop
    my "Yes. But after talking with you about it, it does seem like this wasn't any sort of spur-of-the-moment decision."
    my "Seems like you're really being serious about this."
    play sound sfx_cloth_rustling3
    scene sm1ms016-39 mc-sy-sy-close_c1 with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "That's the plan."
    mc "Woah, you did all this while we were talking?"
    scene sm1ms016-39 mc-sy-sy-close_c2 with dissolve
    play voice4 girl34_happy_great2 noloop
    my "Hehe. I guess the muses were with me."
    my "*sighs* Let me tell you one more lesson you should hear that I've picked up in my experience."
    play sound sfx_keyboard_typing2
    scene sm1ms016-39 mc-sy-sy-close_c3 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1ms016-40 mc-sy-sy-close2_c2 with dissolve
    play voice4 girl34_thinking_emm2 noloop
    my "The art that is picked up and appreciated by many people is the exception."
    my "A lot of art gets left on the side of the road. Or worse."
    my "And I don't want that to happen to you..."
    scene sm1ms016-40 mc-sy-sy-close2_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "It won't..."
    play sound sfx_doorbell_lyssa
    scene sm1ms016-41 mc-sy-sy-look_c1 with dissolve
    "*Doorbell ringing*"
    play sound2 sfx_doorbell_lyssa noloop
    scene sm1ms016-43 mc-sy-sy-door_c2 with dissolve
    "*Doorbell ringing*"
    play voice3 stacy_arrogant_huh5 noloop
    sy "Sounds like the stairs are here."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1ms016-44 mc-sy-sy-door2_c2 with dissolve
    pause
    play sound sfx_door_openclosed1
    play sound2 sfx_box_slide noloop
    scene sm1ms016-45 mc-sy-sy-stand_c1 with fade
    play voice4 girl34_arrogant_ha3 noloop
    my "Alright, so those are the stairs."
    play sound sfx_paper_bag_2
    scene sm1ms016-46 mc-sy-sy-look_c3 with dissolve
    play voice4 girl34_disappointed_eh noloop
    my "But what is that?"
    play sound sfx_book_pushin1
    scene sm1ms016-47 mc-sy-sy-look2_c2 with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "That's the studio's logo!"
    scene sm1ms016-48 mc-sy-sy-look3_c2 with dissolve
    play voice3 stacy_surprised_wow1 noloop
    sy "It looks fantastic!"
    sy "[mcname], you install the logo outside the front door, and we'll start to work on the stairs."
    $ renpy.music.set_volume(1.0, 2.0, "music" )
    scene sm1ms016-49 mc-sy-sy-montage1_c1 with fade
    play sound sfx_screwdriver_drill6
    pause
    scene sm1ms016-50 mc-sy-sy-montage2_c1 with dissolve
    play sound2 sfx_metal_fence1 noloop
    play sound sfx_screwdriver_drill2
    pause
    scene sm1ms016-51 mc-sy-sy-montage3_c1 with dissolve
    play sound3 sfx_metal_fence2 noloop
    pause
    scene sm1ms016-52 mc-sy-sy-montage4_c1 with dissolve
    play sound sfx_screwdriver_drill4 volume 0.6
    pause
    scene sm1ms016-53 mc-sy-sy-montage5_c1 with dissolve
    play sound2 sfx_heels_steps1 noloop
    pause
    scene sm1ms016-54 mc-sy-sy-look_c1 with dissolve
    play sound2 sfx_bed_slide3 noloop
    pause
    scene sm1ms016-54 mc-sy-sy-look_c2 with dissolve
    pause
    play sound2 sfx_wrench_long1
    scene sm1ms016-55 mc-sy-sy-logo_c1 with dissolve
    pause
    scene sm1ms016-56 mc-sy-sy-logo2_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.6, 2.0, "music" )
    stop sound2 fadeout 1.5
    scene sm1ms016-58 mc-sy-sy-talk_c1 with fade
    play voice2 mc_happy_yay1 noloop
    mc "All set. Not too shabby, right?"
    play voice3 stacy_happy_yay3 noloop
    sy "Yay."
    sy "It looks perfect."
    if persistent.is_special:
        sy "What do you think, Mom?"
    else:
        sy "What do you think, Melony?"
    play voice4 girl34_happy_nice1 noloop
    my "[mcname] did very nice."
    my "I must admit, the design is very unique."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1ms016-59 mc-sy-sy-walk_c1 with dissolve
    play voice3 stacy_hey noloop
    sy "Come on. You gotta check out the stairs."
    play voice2 mc_yes_aga1 noloop
    mc "Alright, alright."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms016-60 mc-sy-sy-thumbsup_c2 with dissolve
    play voice2 mc_sexy_whistle noloop
    mc "*whistles* Not bad."
    mc "The whole place looks different."
    mc "You two did great."
    play sound sfx_metal_fence1
    scene sm1ms016-61 mc-sy-sy-slide_c1 with dissolve
    play voice3 stacy_hey_angry1 noloop
    sy "Heads up, [mcname]."
    play voice3 stacy_happy_wooh1 noloop
    play sound sfx_metal_fence2
    play sound2 sfx_snowboard_slide1 volume 0.6
    play sound3 sfx_camera_fly1 volume 2.0 noloop
    scene sm1ms016-a61 sy-slide-glambot-000 with hpunch
    scene sm1ms016-a61-glm
    play voice2 mc_surprised_uh3 noloop
    play voice4 girl34_surprised_huh6 noloop
    sy "Weee!"
    stop sound3 fadeout 3.0
    scene sm1ms016-62 mc-sy-sy-slide2_c1 with dissolve
    pause
    stop sound2 fadeout 1.0
    play sound sfx_leg_kick6
    play voice2 mc_pain_ou1 noloop
    scene sm1ms016-63 mc-sy-sy-catch_c1 with vpunch
    mc "Fuuaah!"
    play sound sfx_leg_kick1
    play sound2 sfx_fall_down1 noloop
    play voice2 mc_pain_mff3 noloop
    scene sm1ms016-64 mc-sy-sy-look_c1 with vpunch
    pause
    play voice4 girl34_scared_ah8 noloop
    scene sm1ms016-65 mc-sy-sy-look2_c3 with hpunch
    my "[mcname]!"
    play voice2 mc_happy_laugh1 noloop
    play voice3 stacy_happy_laugh5 noloop
    scene sm1ms016-65 mc-sy-sy-look2_c1 with dissolve
    "[mcname] and Stacy" "*laughing*"
    mc "Did you have fun?"
    scene sm1ms016-66 mc-sy-sy-ask_c2 with dissolve
    play voice3 stacy_yes_yap2 noloop
    sy "Always."
    play sound sfx_cloth_rustling3
    scene sm1ms016-67 mc-sy-sy-stand_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Looks like the stairs are good to go."
    scene sm1ms016-67 mc-sy-sy-stand_c3 with dissolve
    play voice4 girl34_yes_happy2 noloop
    my "Yes. Turned out building them was pretty straightforward."
    scene sm1ms016-67 mc-sy-sy-stand_c2 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah."
    queue voice3 stacy_laugh4 noloop
    sy "*laughing* Stairs by IKEA."
    play sound sfx_phone_buzz
    scene sm1ms016-69 mc-sy-sy-look_c2 with dissolve
    play voice4 girl34_thinking_hmm6 noloop
    my "Hmm."
    my "And perfect timing too. I've got an appointment to get my nails done."
    scene sm1ms016-70 mc-sy-sy-talk_c2 with dissolve
    play voice4 girl34_disappointed_mmf4 noloop
    my "Mmm. So what's next on the list?"
    play sound sfx_cloth_rustling2
    scene sm1ms016-72 mc-sy-sy-look_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Probably some R and R. I could use some time on the couch."
    scene sm1ms016-73 mc-sy-sy-look2_c2 with dissolve
    play voice3 stacy_no_sad1 noloop
    sy "Not just yet. We still need to spend some time painting the columns and walls."
    play voice2 mc_thinking_mmm5 noloop
    mc "Do we have to?"
    play voice3 stacy_no_nah1 noloop
    sy "Don't worry. We don't have to do all of it today."
    sy "But I want to get a start on it."
    play sound2 sfx_heels_steps1
    scene sm1ms016-74 mc-sy-sy-wave_c2 with dissolve
    play voice4 girl34_hey_bye3 noloop
    my "Well you two have fun."
    my "I'll swing by tomorrow and check in."
    scene sm1ms016-74 mc-sy-sy-wave_c1 with dissolve
    play voice2 mc_hey_bye1 noloop
    if persistent.is_special:
        mc "Bye mom."
        play voice3 stacy_yes_ugu1 noloop
        sy "Bye mom."
    else:
        mc "Bye Melony."
        play voice3 stacy_yes_ugu1 noloop
        sy "Later. Thanks for all the help."
    play sound2 sfx_door_openclosed2 noloop
    scene sm1ms016-76 mc-sy-sy-look2_c1 with dissolve
    play sound sfx_cloth_rustling1
    play voice2 mc_thinking_mmm2 noloop
    mc "Well, after all that work, I think I'm ready for a hot shower."
    scene sm1ms016-76 mc-sy-sy-look2_c2 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Hold your horses, Mister."
    sy "I wasn't kidding about painting."
    scene sm1ms016-77 mc-sy-sy-look3_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Alright. But just a little."
    mc "I gotta save some energy for work."
    play sound sfx_chains_swings1
    scene sm1ms016-77 mc-sy-sy-look3_c2 with dissolve
    stop sound fadeout 1.0
    play voice3 stacy_yes_yap1 noloop
    sy "Just a little paint."
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    stop music fadeout 3.0
    $ StoryController.end_scene(MS)
    return