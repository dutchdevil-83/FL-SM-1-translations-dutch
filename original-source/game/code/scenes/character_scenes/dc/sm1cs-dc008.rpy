image sm1cs_dc008-glambot-1 = Movie(play = "images/Character-Scenes/DC/s008/anim/sm1cs-dc008-a02-2x-50fps.webm", start_image = "sm1cs-dc008-a02 mc-dc-entry2-glambot-001_i", image = "sm1cs-dc008-a02 mc-dc-entry2-glambot-138_i", loop = False)
label sm1cs_dc008:
    $ renpy.music.set_volume(1.0, 1.0, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_endless_questions_reverbed
    play sound sfx_heels_steps1 loop
    play sound4 sfx_cafe_crowd fadein 2.0
    scene sm1cs-dc008-01 mc-dc-entry_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.7
    mct "Man... this date has been a long time coming. I'm pretty excited that this is {b}finally{/b} happening."
    mct "All that's left to do is... well, go on the date!"
    mct "I wonder if Debbie is already here..."
    stop sound fadeout 1.0
    scene sm1cs-dc008-01 mc-dc-entry_c2 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.8
    mct "There she is! Punctual as ever..."
    mct "And looking {b}damn{/b} good."
    play voice4 boy9_arrogant_hm2 noloop
    "Waiter" "And I will make sure your date joins you as soon as he arrives."
    play voice3 girl36_no_happy noloop
    dc "No need! This is him."
    play sound3 sfx_heels_steps1 loop
    scene sm1cs-dc008-a02 mc-dc-entry2-glambot-001_i with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Wow..."
    stop sound3 fadeout 4.0
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] noloop volume 2.0
    play voice3 ["<silence 5.1>", girl36_surprised_huh3] noloop
    scene sm1cs_dc008-glambot-1
    pause
    dc "Hmm?"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop voice3 fadeout 1.0
    scene sm1cs-dc008-03 mc-dc-talk_c1 with dissolve
    play voice2 d3s7_mcemm noloop volume 1.7
    mc "It's just..."
    scene sm1cs-dc008-03 mc-dc-talk_c2 with dissolve
    play voice3 girl36_hey_angry1 noloop
    dc "Just what? What's the matter, [mcname]?"
    scene sm1cs-dc008-04 mc-dc-talk2_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    if player.has_played_scene("sm1cs_dc_renovation"):
        mc "I thought you always looked best in uniform."
    else:
        mc "I didn't think you could look better out of uniform."
    mc "But I was wrong - you look incredible, Debbie."
    mc "I'm sorry - Officer Callahan."
    scene sm1cs-dc008-04 mc-dc-talk2_c2 with dissolve
    play voice3 girl36_pain_ergh noloop
    dc "Oh, knock it off, [mcname]!{w} You had me worried there!"
    play sound sfx_hair_scratch1
    scene sm1cs-dc008-05 mc-dc-look_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I have to keep you guessing! Keep things interesting, you know?"
    scene sm1cs-dc008-05 mc-dc-look_c2 with dissolve
    play voice3 girl36_disappointed_oof noloop
    dc "They don't need to be {i}that{/i} interesting!"
    scene sm1cs-dc008-06 mc-dc-look2_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "All right, all right - I promise to take... 20 percent off the top."
    scene sm1cs-dc008-06 mc-dc-look2_c2 with dissolve
    play voice3 girl36_arrogant_he noloop
    dc "Thank you, Squirrely [mcname]."
    play sound sfx_bed_slide3
    scene sm1cs-dc008-07 mc-dc-sit_c2 with dissolve
    play voice3 girl36_happy_laugh1 noloop
    dc "This is quite the nice restaurant!"
    play sound sfx_bed_slide2
    scene sm1cs-dc008-08 mc-dc-sit2_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "I think so too. I hope you like it!"
    scene sm1cs-dc008-08 mc-dc-sit2_c2 with dissolve
    play voice3 girl36_surprised_eeh noloop
    dc "I..."
    dc "It's definitely nice!"
    play sound sfx_cloth_rustling2
    scene sm1cs-dc008-10 mc-dc-ask_c1 with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Oh? Is something wrong?"
    scene sm1cs-dc008-10 mc-dc-ask_c2 with dissolve
    play voice3 girl36_no_nonono noloop
    dc "No, no! It's nothing like that!"
    play sound2 sfx_heels_steps2
    scene sm1cs-dc008-11 mc-dc-walk_c1 with dissolve
    pause
    stop sound2 fadeout 1.0
    scene sm1cs-dc008-12 mc-dc-look_c2 with dissolve
    play voice4 boy9_hey_easy noloop
    "Waiter" "Good evening. Would either of you like to begin your meal with a glass of wine?"
    play voice3 girl36_yes_happy1 noloop
    dc "Yes!"
    dc "Uhm, that sounds wonderful. I'll take a glass of... red?"
    scene sm1cs-dc008-12 mc-dc-look_c1 with dissolve
    play voice4 boy9_yes_yeah7 noloop
    "Waiter" "Of course. And for you, sir?"
    play voice2 mc_yes_aga2 noloop
    mc "I'll also take a glass of your house red."
    "Waiter" "Excellent choices. I will have that right out."
    play sound2 sfx_heels_steps2 noloop
    scene sm1cs-dc008-13 mc-dc-walk_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "You seem pretty excited about getting a glass of wine, Debbie."
    scene sm1cs-dc008-13 mc-dc-walk_c2 with dissolve
    play voice3 girl36_disgust_oof noloop
    dc "I..."
    play sound sfx_cloth_rustling3
    scene sm1cs-dc008-14 mc-dc-ask_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Anything you want to tell me?"
    scene sm1cs-dc008-14 mc-dc-ask_c2 with dissolve
    play voice3 girl36_arrogant_hmf noloop
    dc "I..."
    play voice2 d2s9_confused noloop volume 1.6
    mc "If you want to call this off, Deb-"
    dc "No, no! That's not - that's not what I want at all!"
    scene sm1cs-dc008-15 mc-dc-look_c1 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Okay, okay! I just had to check."
    play voice3 girl36_disgust_neh noloop
    dc "It's just, erm..."
    play sound2 sfx_heels_steps2 noloop
    scene sm1cs-dc008-16 mc-dc-walk_c1 with dissolve
    play voice4 boy9_hey_simple1 noloop
    "Waiter" "Your wine."
    play voice3 girl36_happy_relief1 noloop
    dc "Thank you!"
    play sound sfx_plate_place1
    scene sm1cs-dc008-17 mc-dc-look_c1 with dissolve
    play voice4 boy9_yes_aga2 noloop
    "Waiter" "Of course. Do you two still need a moment with the menu? Or are you ready to order?"
    play voice2 mc_thinking_hmm2 noloop
    mc "I think we need a few more minutes."
    "Waiter" "Of course, sir."
    play sound sfx_drink_horse1
    scene sm1cs-dc008-19 mc-dc-wine2_c2 with dissolve
    play voice3 girl36_disgust_mmm noloop
    play voice2 mc_angry_huh2 noloop
    mct "Man, Debbie really wanted that glass of wine."
    mct "Maybe she's thirsty? Or maybe... it's something else."
    play sound sfx_cup_place1 volume 2.5
    scene sm1cs-dc008-20 mc-dc-look_c2 with dissolve
    play voice3 girl36_happy_phew2 noloop
    dc "Wooo..."
    scene sm1cs-dc008-21 mc-dc-ask_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah? Tell me how you really feel about that glass of wine."
    scene sm1cs-dc008-21 mc-dc-ask_c2 with dissolve
    play voice3 girl36_surprised_oh noloop
    dc "Oh, I- that was rude, wasn't it?{w} I am so sorry."
    scene sm1cs-dc008-22 mc-dc-look_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "It's fine, Debbie, seriously."
    mc "Whenever you're ready to tell me what's going, I'm here."
    scene sm1cs-dc008-22 mc-dc-look_c2 with dissolve
    play voice3 girl36_angry_breath noloop
    dc "I... it's really not that serious, [mcname]."
    scene sm1cs-dc008-22 mc-dc-look_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Either way, whenever you're ready to tell me."
    scene sm1cs-dc008-23 mc-dc-look2_c1 with dissolve
    play voice3 girl36_disappointed_geh noloop
    dc "It's...{w} I've never been to such a nice restaurant, probably ever. Especially not on a date."
    dc "In fact... I'm not sure if I've ever really been on a proper first date."
    dc "Heck, I can't even remember the last time I put on a dress."
    scene sm1cs-dc008-23 mc-dc-look2_c2 with dissolve
    play voice3 girl36_disgust_mneagh noloop
    dc "This thing was tucked in the way back of my closet, I had a hard time even finding it."
    dc "And my stomach has been doing somersaults ever since you texted me."
    dc "I'm too nervous to eat, I think the only thing I can put in me is this glass of wine."
    scene sm1cs-dc008-24 mc-dc-look3_c2 with dissolve
    play voice3 girl36_happy_mmm noloop
    dc "And, I don't know...{w} it feels kind of... embarrassing to be this nervous."
    dc "I just... I really want this date to go well."
    play sound sfx_bed_slide2 volume 0.6
    scene sm1cs-dc008-25 mc-dc-close_c1 with dissolve
    play sound2 sfx_cloth_rustling2 noloop
    play voice2 mc_happy_a1 noloop
    mc "You have nothing to be worried about, Debbie."
    play sound sfx_cloth_rustling3
    scene sm1cs-dc008-26 mc-dc-look_c1 with dissolve
    play voice2 d9s2_ugu noloop volume 1.5
    mc "I think this date is going to go great, and that you have nothing to worry about."
    dc "..."
    scene sm1cs-dc008-26 mc-dc-look_c2 with dissolve
    play voice3 girl36_happy_relief2 noloop
    dc "Thanks, [mcname]."
    play sound sfx_bed_slide3 volume 0.5
    scene sm1cs-dc008-30 mc-dc-wine_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course, Officer Callahan."
    scene sm1cs-dc008-31 mc-dc-talk_c2 with dissolve
    play voice3 girl36_thinking_hmm noloop
    dc "You really do know just the right thing to say to perk me up."
    play sound sfx_cloth_rustling4
    scene sm1cs-dc008-32 mc-dc-wine_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "What can I say, I'm better than a cup of coffee!"
    play voice3 girl36_happy_laugh2 noloop
    dc "Hahahaha!"
    play sound sfx_heels_steps2
    scene sm1cs-dc008-35 mc-dc-walk_c1 with dissolve
    play voice4 boy9_thinking_emm1 noloop
    "Waiter" "Have you two had a chance to look over the menu?"
    scene sm1cs-dc008-36 mc-dc-look_c2 with dissolve
    play voice3 girl36_surprised_ohmy1 noloop
    dc "Oh my! Not at all, actually, uhm-"
    play voice2 mc_angry_oof noloop
    mc "I'm actually realizing that I'm not really hungry. Could we just put in an order for your most popular appetizer?"
    play sound sfx_heels_steps2
    scene sm1cs-dc008-37 mc-dc-look2_c1 with dissolve
    play voice4 boy9_yes_aga3 noloop
    "Waiter" "Of course, sir."
    play sound2 sfx_cloth_rustling2 noloop
    scene sm1cs-dc008-32 mc-dc-wine_c2 with dissolve
    play voice3 girl36_disappointed_aah noloop
    dc "[mcname]..."
    scene sm1cs-dc008-33 mc-dc-talk_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene sm1cs-dc008-34-1 mc-dc-speak1_c2 with dissolve
    play voice3 girl36_thinking_eem noloop
    dc "You didn't need to cover for me like that."
    play voice2 mc_thinking_hmm1 noloop
    mc "Well what if I'm not hungry anymore?"
    scene sm1cs-dc008-34-3 mc-dc-speak3_c2 with dissolve
    play voice3 girl36_arrogant_fff noloop
    dc "Pffft!"
    mc "It's fine, Debbie.{w} Don't even worry about it."
    play voice3 girl36_hey_angry1 noloop
    dc "But I do. You picked such a nice restaurant, and..."
    play voice2 mc_arrogant_hm3 noloop
    mc "And it's just a little stuffy in here."
    play voice3 girl36_happy_laugh4 noloop
    dc "Hehehehe. You're right about that."
    mc "That's better."
    scene sm1cs-dc008-34-5 mc-dc-speak5_c2 with dissolve
    play voice3 girl36_surprised_huh2 noloop
    dc "What's better?"
    play voice2 mc_thinking_hmm6 noloop
    mc "You - you're smiling now!"
    scene sm1cs-dc008-34-6 mc-dc-speak6_c2 with dissolve
    play voice3 girl36_disappointed_oh noloop
    dc "Oh, [mcname]..."
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Okay, so I've learned some important things. Next time, maybe a less fancy place for our date?"
    dc "I wouldn't mind that."
    play sound sfx_cloth_rustling3
    scene sm1cs-dc008-34-9 mc-dc-speak9_c2 with dissolve
    play voice3 girl36_arrogant_huh1 noloop
    dc "Wait, you want to go on {i}another{/i} date?"
    scene sm1cs-dc008-38 mc-dc-talk_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. Why wouldn't I?"
    mc "I mean, I don't want to start thinking too far ahead, but yeah. Another date would be great."
    scene sm1cs-dc008-38 mc-dc-talk_c2 with dissolve
    play voice3 girl36_surprised_huh1 noloop
    dc "Even though we haven't even really talked about anything?"
    play voice2 mc_hey_hey7 noloop
    mc "Well we can change that! Uhm, what's your favorite movie?"
    play sound sfx_cloth_rustling2
    scene sm1cs-dc008-34-4 mc-dc-speak4_c2 with dissolve
    play voice3 girl36_arrogant_laugh noloop
    dc "My favorite movie?"
    play voice2 mc_happy_yes1 noloop
    mc "Yeah!"
    dc "Oh, uhm... I... well this is a little embarrassing but..."
    scene sm1cs-dc008-34-8 mc-dc-speak8_c2 with dissolve
    play voice3 girl36_arrogant_hm noloop
    dc "I do really like the \"Die Hard\" movies.{w} You know, just a rogue cop getting things done."
    dc "And also the \"Lethal Weapon\" movies..."
    dc "Honestly, any action movies where you can sit back and cheer, and cry, and turn off your brain and enjoy the ride."
    dc "Like that train action movie that came out! That one was {i}a lot{/i} of fun!"
    play voice2 mc_happy_hah2 noloop
    mc "I should've guessed that you liked action movies."
    scene sm1cs-dc008-34-7 mc-dc-speak7_c2 with dissolve
    play voice3 girl36_surprised_why1 noloop
    dc "And why's that?"
    play voice2 mc_thinking_hmm5 noloop
    mc "Well most of our time together has been filled with our own little action packed adventures."
    play voice3 girl36_happy_laugh3 noloop
    dc "Hahaha, that's very true."
    mc "How about your favorite meal?"
    scene sm1cs-dc008-34-1 mc-dc-speak1_c2 with dissolve
    play voice3 girl36_scared_oof noloop
    dc "Oh boy..."
    play voice2 mc_surprised_what7 noloop
    mc "What?"
    dc "It's... I'm a simple girl."
    mc "Okay?"
    dc "And... I really like simple things."
    mc "All right?"
    play sound sfx_cloth_rustling1
    scene sm1cs-dc008-34-2 mc-dc-speak2_c2 with dissolve
    play voice3 girl36_angry_errr noloop
    dc "And so... my favorite food is a hot dog with the works."
    dc "Which feels... dirty to say in such a nice restaurant."
    play voice2 mc_no_no2 noloop
    mc "It's totally fine! I also like hot dogs. I get it."
    dc "Really?"
    mc "Really really."
    scene sm1cs-dc008-34 mc-dc-ask_c2 with dissolve
    play voice3 girl36_surprised_wow noloop
    dc "I'm... I'm happy to hear that!"
    play voice2 mc_thinking_hmm4 noloop
    mc "And what's your favorite color?"
    dc "My favorite color?"
    scene sm1cs-dc008-34 mc-dc-ask_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yeah, everyone has a favorite color!"
    play voice3 girl36_surprised_aah noloop
    dc "Erm, pink?"
    play sound2 sfx_heels_steps2
    scene sm1cs-dc008-35 mc-dc-walk_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "And look at that! A successful date!"
    play voice3 girl36_surprised_what2 noloop
    dc "That's all it takes?"
    mc "I mean, pretty much!"
    stop sound2 fadeout 1.0
    scene sm1cs-dc008-36 mc-dc-look_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "I think we'll take the check."
    scene sm1cs-dc008-36 mc-dc-look_c2 with dissolve
    play voice4 boy9_arrogant_huh2 noloop
    "Waiter" "Your appetizer, sir?"
    play voice2 mc_thinking_mmm4 noloop
    mc "Can we take it to go?"
    play voice3 boy9_yes_yep2 noloop
    "Waiter" "Of course, sir."
    play sound2 sfx_heels_steps2 noloop
    scene sm1cs-dc008-37 mc-dc-look2_c1 with dissolve
    pause
    stop sound2 fadeout 1.0
    scene sm1cs-dc008-37 mc-dc-look2_c2 with dissolve
    play voice3 girl36_hey_scandalized noloop
    dc "Wait, [mcname], we can eat the appetizer here!"
    scene sm1cs-dc008-38 mc-dc-talk_c1 with dissolve
    play voice2 mc_no_nono1 noloop
    mc "It's fine, Debbie! Seriously."
    play voice3 girl36_angry_ugh2 noloop
    dc "But-"
    mc "Debbie."
    scene sm1cs-dc008-38 mc-dc-talk_c2 with dissolve
    play voice3 girl36_yes_questioning noloop
    dc "Yes?"
    play voice2 mc_thinking_mmm6 noloop
    mc "This has been a lovely date."
    dc "Woah, [mcname]-"
    play sound2 sfx_heels_steps2
    scene sm1cs-dc008-39 mc-dc-talk2_c1 with dissolve
    play voice3 boy9_hey_simple4 noloop
    "Waiter" "And here you are, sir."
    stop sound2 fadeout 1.0
    play sound sfx_paper_bag_2
    scene sm1cs-dc008-40 mc-dc-talk3_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Thank you."
    scene sm1cs-dc008-40 mc-dc-talk3_c2 with dissolve
    play voice3 boy9_happy_mmm2 noloop
    "Waiter" "I hope you and your date enjoy the rest of your evening."
    play sound sfx_pen_writing4
    scene sm1cs-dc008-41 mc-dc-bill_c2 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Thank you!"
    scene sm1cs-dc008-42 mc-dc-ask_c2 with dissolve
    play voice3 girl36_arrogant_yeah2 noloop
    dc "I really enjoyed this, [mcname]."
    dc "But next time, I'll have to learn more about you for a change."
    scene sm1cs-dc008-43 mc-dc-stand_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Ooooh. Something to look forward to."
    mc "I should warn you, I'm a steel trap."
    mc "You'll work hard to pry my secrets from me."
    scene sm1cs-dc008-44 mc-dc-look_c2 with dissolve
    play voice3 girl36_surprised_what1 noloop
    dc "Haha. Good thing I'm a police officer."
    dc "I know a thing or two about questioning a suspect."
    play sound sfx_cloth_rustling4
    scene sm1cs-dc008-45 mc-dc-stand_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Movies. Jeans and questioning."
    mc "Our next date is going to be a blast!"
    scene sm1cs-dc008-45 mc-dc-stand_c2 with dissolve
    play voice3 girl36_yes_yeah noloop
    dc "Heheh.{w} Looking forward to it."
    scene sm1cs-dc008-46 mc-dc-stand2_c1 with dissolve
    mc "Man. You really do look stunning tonight, Debbie."
    scene sm1cs-dc008-46 mc-dc-stand2_c2 with dissolve
    play voice3 girl36_happy_mmm noloop
    dc "Thanks, [mcname]. I lke your outfit too."
    dc "This dress is nice.{w} But there is one {b}big{/b} problem..."
    scene sm1cs-dc008-46 mc-dc-stand2_c1 with dissolve
    mc "Mmmhmmm. What's that?"
    scene sm1cs-dc008-46 mc-dc-stand2_c2 with dissolve
    play voice3 girl36_happy_mmm noloop
    dc "There is no where to put my gun!"
    scene sm1cs-dc008-47 mc-dc-close_c1 with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.6
    mc "Hahahahaha!"
    scene sm1cs-dc008-47 mc-dc-close_c2 with dissolve
    dc "Mmmm..."
    scene sm1cs-dc008-48 mc-dc-look_c1 with dissolve
    pause
    play sound2 sfx_cloth_rustling2 noloop
    scene sm1cs-dc008-49 mc-dc-kiss_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    play voice3 girl36_disappointed_moan noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-dc008-49 mc-dc-kiss_c2 with dissolve
    queue sound mc_kiss2
    pause
    scene sm1cs-dc008-50 mc-dc-look_c2 with dissolve
    play voice3 girl36_surprised_wow noloop
    dc "*softly* Wow..."
    scene sm1cs-dc008-50 mc-dc-look_c1 with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "I agree."
    scene sm1cs-dc008-50 mc-dc-look_c2 with dissolve
    play voice3 girl36_happy_laugh1 noloop
    dc "If this is how every date with you ends, maybe I will be wearing this dress more often."
    play voice2 mc_thinking_oh1 noloop
    mc "You don't need to wear the dress to get a kiss like that."
    dc "Even better."
    play sound dahlia_kiss_french1
    play sound2 sfx_hair_scratch1 noloop
    scene sm1cs-dc008-51 mc-dc-kiss_c1 with dissolve
    pause
    scene sm1cs-dc008-52 mc-dc-look_c2 with dissolve
    play voice3 girl36_happy_phew2 noloop
    dc "It's such a relief being with someone who accepts me as I am, [mcname]."
    dc "It's kind of exciting, having you know the {b}real{/b} me..."
    scene sm1cs-dc008-53 mc-dc-talk_c1 with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "I'm greatful that you shared that part of you with me, Debbie."
    mc "And I can't wait to see where we go next."
    scene sm1cs-dc008-53 mc-dc-talk_c2 with dissolve
    play voice3 girl36_happy_yay noloop
    dc "Mmmmhmm. {w}That's what I like to hear!"
    dc "Well, until you call about our next date..."
    play sound sfx_heels_steps1 loop
    scene sm1cs-dc008-54 mc-dc-walk_c2 with dissolve
    play voice3 girl36_yes_aga noloop
    dc "...You know where to find me."
    scene sm1cs-dc008-55 mc-dc-walk2_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "She's really a one-of-a-kind gal."
    scene sm1cs-dc008-55 mc-dc-walk2_c2 with dissolve
    play voice2 mc_thinking_hm noloop
    mct "Now I just need to figure out what to do for our next date..."
    mct "Whatever it is, it probably shouldn't involve catching bad guys in the park."
    stop sound fadeout 1.0
    scene sm1cs-dc008-56 mc-dc-walk3_c2 with dissolve
    queue sound sfx_heels_steps2
    play voice2 d14s16_smell noloop volume 0.8
    mct "Hopefully..."
    stop sound4 fadeout 2.5
    stop sound fadeout 1.0
    jump sm1cs_dc008_end_scene
label sm1cs_dc008_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(DC_STORY, 3, 0, 4)
    return