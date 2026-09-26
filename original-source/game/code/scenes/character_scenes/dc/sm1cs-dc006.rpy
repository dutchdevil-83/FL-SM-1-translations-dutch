label sm1cs_dc006:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.7, 3.0, "music2" )
    play music2 music_starducks2_reverbed
    play sound4 sfx_cafe_crowd volume 0.6
    scene sm1cs-dc006-01 mc-dc-waiting with dissolve
    pause
    play sound sfx_cup_slide1
    scene sm1cs-dc006-02 mc-dc-done-with-her-order with dissolve
    pause
    scene sm1cs-dc006-03 mc-ordering with dissolve
    play voice4 girl37_hey_simple noloop
    cs "Good morning, and welcome to Starducks. What would you like to order?"
    scene sm1cs-dc006-04 mc-ordering with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I'll... have a white chocolate mocha, and the officer will have a red eye."
    play voice4 girl37_yes_yep noloop
    cs "Sounds great, I'll have that up in a second."
    play sound sfx_heels_steps1
    play sound2 sfx_heels_steps2
    scene sm1cs-dc006-05 dc-speaking with dissolve
    play voice3 girl36_surprised_huh1 noloop
    dc "I thought you said you were a black coffee only type of person."
    scene sm1cs-dc006-06 mc-speaking with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "I am, er, at least was. But you said you needed to 'expand my horizons', so I thought I'd try something new."
    mc "I also hope it's okay I got you the red eye. I figured if you have more work to do, that you want to be bright eyed and bushy tailed."
    scene sm1cs-dc006-07 dc-talking with dissolve
    play voice3 girl36_thinking_oh noloop
    dc "I, uhm - yeah, I like red eyes..."
    play voice2 mc_happy_yes1 noloop
    mc "I remember!"
    play sound sfx_cloth_rustling4
    stop sound2 fadeout 1.0
    scene sm1cs-dc006-08 dc-blushing with dissolve
    play voice3 girl36_surprised_eeh noloop
    dc "Yeah, I'm... a little surprised you do."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh? Why would I forget?"
    scene sm1cs-dc006-09 dc-leaning-in with dissolve
    play voice3 girl36_surprised_oh noloop
    dc "Oh, you know... some guys are just forgetful."
    dc "I've also learned in my time on the force that memory is not reliable as you'd like it to be most times."
    play sound sfx_cloth_rustling2
    scene sm1cs-dc006-11 mc-wincing with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh?"
    scene sm1cs-dc006-16 dc-confessing with dissolve
    play voice3 girl36_arrogant_huh1 noloop
    dc "Oh, it's just... a fact they teach at the academy. Eyewitness testimony is the least reliable. People forget things, or misremember them all the time."
    scene sm1cs-dc006-17 mc-surprised with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Huh... well, I thought I had a great memory."
    scene sm1cs-dc006-18 dc-leaning-in with dissolve
    play voice3 girl36_disappointed_eeh noloop
    dc "But sometimes you miss what's right in front of your eyes. I think you'd understand that, [mcname]."
    scene sm1cs-dc006-10 mc-speaking with dissolve
    play voice2 mc_pain_auch1 noloop
    mc "You've got a good point there."
    play sound sfx_cloth_rustling1
    scene sm1cs-dc006-12 dc-whoops with dissolve
    play voice3 girl36_surprised_ohmy1 noloop
    dc "Oh my God, [mcname]. I am {i}so, so sorry.{/i} I... that just slipped out. I didn't mean to dredge up Lydia and Fetish Locator, I-"
    scene sm1cs-dc006-13 mc-saying with dissolve
    play voice2 mc_no_nono1 noloop
    mc "It's okay, Debbie. Seriously, it's a part of my life now. There's no getting away from it."
    play sound sfx_cloth_rustling3
    scene sm1cs-dc006-14 dc-embarassed with dissolve
    play voice3 girl36_scared_oof noloop
    dc "Still, I didn't need to bring it up."
    scene sm1cs-dc006-21 mc-talking with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Trust me, it's A-okay. I mean, I can't say that I'm surprised, you know? With you being a cop and all."
    scene sm1cs-dc006-18 dc-leaning-in with dissolve
    play voice3 girl36_arrogant_yeah2 noloop
    dc "Yeah..."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "How'd you find out?"
    play sound sfx_heels_steps2 fadein 1.5 loop
    dc "I-"
    stop sound fadeout 1.0
    scene sm1cs-dc006-15 cs-approaching-them with dissolve
    play voice4 girl37_disappointed_ehh noloop
    cs "I'm sorry the coffee is taking longer than normal, we had a bit of a morning rush. But I promise it will be done soon!"
    play voice2 mc_yes_okay3 noloop
    mc "Thank you!"
    play sound sfx_heels_steps2
    scene sm1cs-dc006-16 dc-confessing with dissolve
    stop sound fadeout 1.5
    play voice3 girl36_disappointed_aah noloop
    dc "I, erm... may have ran a teensy little background check on you."
    scene sm1cs-dc006-17 mc-surprised with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Really? Anything interesting pop up?"
    scene sm1cs-dc006-18 dc-leaning-in with dissolve
    play voice3 girl36_no_nope noloop
    dc "No... I mean, the Fetish Locator stuff, but that's it. I asked around the station about it, but no one would really tell me anything."
    play sound sfx_cloth_rustling2
    scene sm1cs-dc006-19 mc-smiling with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Huh. That's kind of a surprise. It was a big deal thing that happened, I figured they'd love to talk about it."
    scene sm1cs-dc006-20 dc-nervous with dissolve
    play voice3 girl36_arrogant_yeah3 noloop
    dc "Yeah, surprisingly everyone is pretty tight lipped about it."
    dc "I would be lying if I didn't say I was a little interested in what happened. If the cops won't talk about it... it must be juicy."
    scene sm1cs-dc006-21 mc-talking with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "I'll make you a deal. If you tell me what's been bothering you, I'll tell you something about Fetish Locator."
    mct "Uh oh... what the hell did I do now?"
    scene sm1cs-dc006-22 dc-confessing with dissolve
    play voice3 girl36_angry_breath noloop
    dc "I... uhm... I don't know, [mcname]."
    play voice2 mc_arrogant_pff1 noloop
    mc "Come on, Debbie. It can't be that bad."
    scene sm1cs-dc006-23 dc-about-to-talk with dissolve
    play voice3 girl36_thinking_hmm noloop
    dc "I've heard that one before."
    scene sm1cs-dc006-19 mc-smiling with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Seriously, it can't be any worse than trying to keep it a secret from me. Right?"
    scene sm1cs-dc006-20 dc-nervous with dissolve
    play voice3 girl36_happy_relief2 noloop
    dc "You're right, [mcname]. I... I can't keep hiding it from you."
    dc "Okay, where to begin... I, uhm-"
    play sound sfx_heels_steps2
    play sound2 sfx_plates_moving1 volume 0.6 noloop
    scene sm1cs-dc006-24 cs-interuptting-them with dissolve
    play voice4 girl37_hey_happy2 noloop
    cs "Sorry about that wait! Here you go, one white chocolate mocha, and one red eye. Enjoy!"
    scene sm1cs-dc006-25 mc-thinking with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "Wow, what terrible timing."
    scene sm1cs-dc006-26 dc-nervous with dissolve
    play voice3 girl36_happy_mmm noloop
    dc "Uhm... so, have you ever had a white chocolate mocha?"
    play voice2 mc_no_nope2 noloop
    mc "Nope, can't say that I have. I'm actually pretty sure I've never had a mocha."
    dc "They're pretty good. It's espresso and milk and some chocolate mix. I mean, your's is a white chocolate mix, and..."
    play sound sfx_cloth_rustling1
    scene sm1cs-dc006-27 dc-talking with dissolve
    play voice3 girl36_happy_laugh1 noloop
    dc "Sorry, I kind of ramble when I get nervous."
    scene sm1cs-dc006-35 mc-confused with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "It's okay, Debbie. You can tell me what's been bugging you."
    scene sm1cs-dc006-36 dc-nervous with dissolve
    play voice3 girl36_no_nonono noloop
    dc "No, no. Try the mocha first, while it's still warm. The Starducks' coffee is best right away, and then it kind of gets meh if it gets too cold."
    play sound sfx_cloth_rustling2
    scene sm1cs-dc006-28 mc-holding-the-cup with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Sure, I can do that."
    mc "Bottoms up!"
    play sound sfx_drink_slurp2
    scene sm1cs-dc006-29 mc-drinking with dissolve
    pause
    scene sm1cs-dc006-30 dc-speaking with dissolve
    play voice3 girl36_arrogant_huh2 noloop
    dc "So? What do you think of your first mocha?"
    play sound sfx_plate_place1
    scene sm1cs-dc006-33 mc-talking with dissolve
    play voice2 d3s7_mcemm noloop volume 1.7
    mc "I..."
    mc "I didn't know coffee could be so sweet."
    scene sm1cs-dc006-31 dc-giggling with dissolve
    play voice3 girl36_happy_laugh2 noloop
    dc "Well it's not the coffee that's sweet! It's all that added sugar."
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, you're right. You said that there's {i}ex{/i}presso in this too?"
    scene sm1cs-dc006-32 dc-giggling with dissolve
    play voice3 girl36_no_questioning noloop
    dc "No. But there is {i}es{/i}presso in it."
    scene sm1cs-dc006-35 mc-confused with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, what did I say?"
    scene sm1cs-dc006-34 dc-speaking with dissolve
    play voice3 girl36_arrogant_huh3 noloop
    dc "Ex-presso. But there's no x in it."
    play voice2 mc_surprised_oh3 noloop
    mc "Oh, oops!"
    dc "No worries, it's a pretty common mistake."
    play sound sfx_drink_slurp2
    scene sm1cs-dc006-29 mc-drinking with dissolve
    pause
    play sound sfx_plate_place1
    scene sm1cs-dc006-33 mc-talking with dissolve
    play voice2 mc_happy_a1 noloop
    mc "But, it tastes pretty good!"
    play voice3 girl36_happy_yay noloop
    dc "Good, I'm glad you like it."
    mc "But, you were about to say something."
    scene sm1cs-dc006-34 dc-speaking with dissolve
    play voice3 girl36_disgust_neh noloop
    dc "I... I was, yes."
    dc "So, uhm... I don't even know how to say it. Okay, so back in my hometown, I, erm, had this problem."
    scene sm1cs-dc006-35 mc-confused with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Okay?"
    scene sm1cs-dc006-36 dc-nervous with dissolve
    play voice3 girl36_disappointed_oof noloop
    dc "I didn't ever really feel like I fit in. Well, kind of. I guess... I just never really got to feel like me."
    play voice2 mc_yes_yeah1 noloop
    mc "Okay, yeah I can kind of understand that."
    scene sm1cs-dc006-34 dc-speaking with dissolve
    play voice3 girl36_disappointed_geh noloop
    dc "So, as I started getting older, I thought that maybe I could fix it."
    play voice2 mc_surprised_what1 noloop
    mc "Fix what?"
    dc "Me, so I would feel more like me."
    scene sm1cs-dc006-35 mc-confused with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Is that why you moved here?"
    play voice3 girl36_no_angry2 noloop
    dc "No, I-"
    play sound sfx_phone_ringtone2_debbie loop
    scene sm1cs-dc006-37 dc-pulling-phone-out with dissolve
    "{i}Ring, ring!{/i}"
    play voice3 girl36_angry_doh3 noloop
    dc "Hang on one second."
    scene sm1cs-dc006-38 dc-hang-on with dissolve
    play voice3 girl36_disgust_ohh noloop
    dc "Oh no, it's the station. I'm sorry, [mcname], but I have to take this."
    play voice2 d9s3_no noloop volume 2.5
    mc "No worries, Officer. The job comes first, I get it."
    play sound sfx_phone_hungup1
    scene sm1cs-dc006-39 dc-talking with dissolve
    play voice3 girl36_yes_angry noloop
    dc "Officer Callahan."
    dc "..."
    scene sm1cs-dc006-40 dc-worried with dissolve
    play voice3 girl36_happy_relief1 noloop
    dc "I'm sorry, it's my break, and-"
    dc "..."
    play voice3 girl36_surprised_what2 noloop
    play sound sfx_cloth_rustling1
    scene sm1cs-dc006-41 dc-shocked with hpunch
    dc "What! When!?"
    dc "..."
    play voice3 girl36_pain_aff noloop
    with hpunch
    dc "I'll be right there!"
    play sound sfx_phone_hungup2 volume 0.4
    scene sm1cs-dc006-42 dc-telling-him with dissolve
    play voice3 girl36_angry_doh2 noloop
    dc "I'm so sorry, [mcname], but I have to go! The creep is at the park!"
    scene sm1cs-dc006-35 mc-confused with dissolve
    play voice2 mc_surprised_uh3 noloop
    if player.get_choice("sm1cs_dc002_backup"):
        mc "Do you need backup, partner?"
    else:
        mc "Do you need backup?"
    scene sm1cs-dc006-43 dc-telling-him with dissolve
    play voice3 girl36_no_angry1 noloop
    dc "No, you stay here. I'm already going to get yelled at enough for being on break, I definitely don't need them finding out I've had a civilian helping me on the case."
    dc "No offense, [mcname]."
    play voice2 mc_yes_okay1 noloop
    mc "It's okay, I understand."
    scene sm1cs-dc006-42 dc-telling-him with dissolve
    play voice3 girl36_hey_greeting1 noloop
    dc "Rain check?"
    play voice2 mc_yes_yes7 noloop
    mc "Definitely."
    dc "Cool."
    play sound sfx_stone_run1 loop
    scene sm1cs-dc006-44 dc-going with dissolve
    pause
    play sound sfx_double_door1
    scene sm1cs-dc006-45 mc-thinking with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Man... what bad luck for both of us, huh."
    scene sm1cs-dc006-46 mc-noticing with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "Oh shit, Debbie!"
    scene sm1cs-dc006-47 mc-looking-back with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "Shit, she probably needs her phone."
    play sound sfx_cloth_rustling1
    play sound2 sfx_heels_steps2
    scene sm1cs-dc006-48 mc-grabs-her-phone with dissolve
    mct "Well, at least I know where she's heading."
    scene sm1cs-dc006-49 mc-walking-away with dissolve
    pause
    play sound2 sfx_door_openclosed2 noloop
    stop sound4 fadeout 2.0
    jump sm1cs_dc006_at_park
label sm1cs_dc006_at_park:
    stop music2 fadeout 3.0
    queue sound4 sfx_parknight_crickets fadein 2.0 volume 0.5
    play sound sfx_heels_steps2 loop fadein 1.0
    scene sm1cs-dc006-50 mc-thinking-away with Fade(0.5, 0.5, 0.5)
    play music music_still_waters fadein 3.0 volume 0.6
    play voice2 mc_thinking_hmm5 noloop
    mct "Where, oh where, could Officer Callahan be?"
    scene sm1cs-dc006-51 mc-noticing-her with dissolve
    pause
    scene sm1cs-dc006-52 mc-hey with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Debbie!"
    play sound sfx_cloth_rustling1
    play voice3 girl36_angry_argh4 noloop
    scene sm1cs-dc006-53 dc-talking with hpunch
    dc "[mcname]! I told you to stay at the coffee shop."
    play sound sfx_cloth_rustling2
    scene sm1cs-dc006-54 mc-talking with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "I know, but you forgot something."
    mc "I figured the coffee wasn't a big deal, but you might want your phone."
    play sound sfx_hair_scratch1
    scene sm1cs-dc006-55 dc-ugh with dissolve
    play voice3 girl36_surprised_ohmy2 noloop
    dc "Oh my God..."
    scene sm1cs-dc006-56 dc-sad with dissolve
    play voice3 girl36_pain_ergh noloop
    dc "Thanks, [mcname]. If I had gotten another call from the station and I didn't pick it up... I'm already in enough trouble."
    scene sm1cs-dc006-57 mc-smiling with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Did you manage to get the creep?"
    scene sm1cs-dc006-58 dc-surprised with dissolve
    play voice3 girl36_no_nah2 noloop
    dc "No, by the time I got back here, he was gone."
    scene sm1cs-dc006-59 mc-curious with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Don't worry, I know you'll catch him."
    scene sm1cs-dc006-60 dc-telling-him with dissolve
    play voice3 girl36_arrogant_yeah1 noloop
    dc "Yeah... Sorry our coffee keeps getting interrupted."
    play voice2 mc_hey_hey3 noloop
    mc "Hey, it's all a part of the gig, right? Nothing you can do about it."
    dc "Yeah..."
    scene sm1cs-dc006-57 mc-smiling with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Besides, it's kind of like our coffee date just moved outside!"
    play voice3 girl36_surprised_huh3 noloop
    dc "D-date?"
    mc "Yeah, or coffee hang out, or whatever."
    mct "Man, what did I do now? She's got the look again..."
    scene sm1cs-dc006-58 dc-surprised with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Debbie, what's up?"
    play voice3 girl36_angry_ugh2 noloop
    dc "I really need to tell you this... thing."
    mc "Okay, well I'm here now, and you can tell me."
    scene sm1cs-dc006-60 dc-telling-him with dissolve
    play voice3 girl36_thinking_eem noloop
    dc "Okay, uhm..."
    dc "So, before I moved here..."
    dc "I... Well, I used to be different. I... uhm..."
    dc "I didn't feel like I was... me, yet."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 0.5, "music2" )
    $ renpy.music.set_volume(0.0, 0.0, "music3" )
    play sound music_horror_moment1_short
    play sound2 sfx_footsteps_grass2 fadein 2.0
    scene sm1cs-dc006-61 dc-creep-walking-through with dissolve
    $ renpy.music.play(audio.music_midnightcreep1_calm, "music2" , True, None, True, 3.0)
    $ renpy.music.play(audio.music_midnightcreep1_active, "music3", True, None, True, 3.0)
    dc "So, I-"
    play voice2 d2s12_emmm noloop volume 1.5
    mc "Debbie?"
    play voice3 girl36_angry_breath noloop
    dc "[mcname], I-"
    scene sm1cs-dc006-62 mc-looking-at-creep with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "Is that the creep over there?"
    scene sm1cs-dc006-63 dc-turning-around with dissolve
    pause
    scene sm1cs-dc006-64 dc-looking-at-each-other with dissolve
    pause
    play voice3 girl36_hey_scandalized noloop
    $ renpy.music.set_volume(1.0, 0.5, "music2" )
    $ renpy.music.set_volume(1.0, 2.0, "music3" )
    play sound sfx_horror_violin1
    scene sm1cs-dc006-65 dc-freeze with hpunch
    dc "Creep! Freeze!"
    play voice4 creep_scared_oinkoink noloop
    play sound sfx_stone_run1 loop volume 2.0
    play sound2 sfx_grass_run1
    play sound3 sfx_heels_run2
    scene sm1cs-dc006-66 dc-running with hpunch
    "Creep" "Oink, oink, bacon!"
    play voice2 mc_hey_hey1 noloop
    mc "Wait, Debbie!"
    play voice3 girl36_angry_argh3 noloop
    scene sm1cs-dc006-67 mc-dc-running with hpunch
    dc "I will get you, you sonuvabitch!"
    play voice4 creep_no_nah1 noloop
    "Creep" "You'll never take me alive!"
    scene sm1cs-dc006-68 mc-thinking with dissolve
    play voice2 d7s4_mcbreathing noloop
    mct "Gah - this guy is fast!"
    play voice3 girl36_pain_aff noloop
    stop voice2 fadeout 1.0
    play sound2 sfx_socks_dancing1
    scene sm1cs-dc006-69 dc-almost-there with hpunch
    pause
    play voice3 girl36_arrogant_ha noloop
    play sound sfx_cloth_tear1
    scene sm1cs-dc006-70 dc-grabbing-his-coat with hpunch
    dc "Gotcha'!"
    play voice4 creep_no_nah2 noloop
    "Creep" "Not quite!"
    play voice4 creep_happy_laugh1 noloop
    play sound sfx_cloth_planket3
    play sound3 sfx_heels_run1 noloop
    stop sound3 fadeout 1.0
    stop sound2 fadeout 2.0
    scene sm1cs-dc006-71 dc-holding-his-coat with hpunch
    "Creep" "Until next time! Hahahaha!"
    play voice3 girl36_pain_ah2 noloop
    $ renpy.music.set_volume(1.0, 3.5, "music2" )
    $ renpy.music.set_volume(0.0, 5.0, "music3" )
    play sound sfx_skirt_off2
    scene sm1cs-dc006-72 dc-pissed with vpunch
    dc "Gah! You bastard! I will get you!!"
    scene sm1cs-dc006-73 mc-catching-up with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Shit... Did he... get... away?"
    scene sm1cs-dc006-74 dc-upset with dissolve
    play voice3 girl36_angry_errr noloop
    dc "Yeah, the bastard literally slipped through my fingers!"
    play voice2 mc_thinking_hmm9 noloop
    mc "But... at least... you've gotten... something?"
    stop music2 fadeout 15.0
    stop music3 fadeout 15.0
    scene sm1cs-dc006-75 dc-upset with dissolve
    $ renpy.music.set_volume(0.7, 3.0, "music" )
    play music music_still_waters fadein 15.0
    play voice3 girl36_angry_ugh1 noloop
    dc "It's not enough. Dammit!"
    menu:
        "Reassure her"(hint="sm1cs_dc006_m01_h01"):
            call sm1cs_dc006_m01_c01 from _call_sm1cs_dc006_m01_c01
            play sound sfx_cloth_rustling4
            scene sm1cs-dc006-78 mc-holding-her-shoulder with dissolve
            play voice2 mc_thinking_mmm4 noloop
            mc "You'll get him Debbie, I know it."
            scene sm1cs-dc006-79 dc-looking with dissolve
            play voice3 girl36_yes_yeah noloop
            dc "Thanks, [mcname]..."
        "Crack a joke"(hint="sm1cs_dc006_m01_h02"):
            scene sm1cs-dc006-76 mc-cheering-her-up with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "He wouldn't be a slippery bastard if he wasn't... slippery."
            play voice3 girl36_yes_yeah noloop
            dc "Yeah..."
            play sound sfx_cloth_rustling4
    scene sm1cs-dc006-78 mc-holding-her-shoulder with dissolve
    pause
    scene sm1cs-dc006-79 dc-looking with dissolve
    play voice3 girl36_angry_breath noloop
    dc "[mcname]... I..."
    scene sm1cs-dc006-80 dc-stuttering with dissolve
    play voice3 girl36_scared_huh7 noloop
    dc "I have a dick!"
    scene sm1cs-dc006-82 mc-confused with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Wha..."
    scene sm1cs-dc006-81 dc-confessing with dissolve
    play voice3 girl36_disappointed_geh noloop
    dc "I've been trying to tell you all morning. I... transitioned back in my hometown because I never felt like {i}me{/i}. Now I do."
    play sound sfx_cloth_rustling5
    scene sm1cs-dc006-83 dc-facepalm with dissolve
    play voice3 girl36_angry_rrr noloop
    dc "But, I've talked to a lot of guys who... can't handle that."
    play sound sfx_phone_ringtone2_debbie loop
    scene sm1cs-dc006-84 dc-phone-ringing with dissolve
    pause
    play voice3 girl36_angry_doh1 noloop
    dc "This is, uhm... the station. I need to take this."
    dc "I... I'll understand if you don't want to talk to me anymore. You wouldn't be the first."
    scene sm1cs-dc006-85 dc-talking with dissolve
    play voice3 girl36_happy_relief2 noloop
    dc "I'll... it was nice getting to know you, [mcname]."
    scene sm1cs-dc006-86 dc-turning-away with dissolve
    menu:
        "Stop Debbie"(hint="sm1cs_dc006_m02_h01"):
            call sm1cs_dc006_m02_c01 from _call_sm1cs_dc006_m02_c01
            stop sound fadeout 1.0
            scene sm1cs-dc006-87 mc-wait with dissolve
            play voice2 d1s2_mchey noloop volume 1.4
            mc "Wait, Debbie!"
            mc "I {i}will{/i} see you around. Hopefully I can catch you on a day where things are less crazy, and we can have a {i}real{/i} coffee date."
            scene sm1cs-dc006-88 dc-smiling with dissolve
            play voice3 girl36_happy_yeah noloop
            dc "I would like that. I would like that a lot."
        "Show no interest in Debbie"(hint="sm1cs_dc006_m02_h02"):
            $ player.set_choice("sm1cs_dc006_offramp")
            $ player.set_choice("sm1ms_dc006_selected_offramp")
            play sound2 sfx_heels_steps1
            play voice2 mc_angry_huh2 noloop
            mct "Woah... that's a lot to take in..."
            play sound sfx_phone_hungup1
            stop sound2 fadeout 1.0
            scene sm1cs-dc006-89 dc-walking with dissolve
            play voice3 girl36_angry_cough noloop
            dc "Officer Callahan...{w} I know. I got here just as he was making his escape...{w}I know, sir..."
    stop music fadeout 3.0
    stop sound4 fadeout 3.0
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "music3" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(DC_STORY, 3, 0, 5)
    return
label sm1cs_dc006_m01_c01:
    $ player.set_choice("sm1cs_dc006_reassure_dc")
    $ CharacterController.get_character("dc").add_point()
    return
label sm1cs_dc006_m02_c01:
    $ player.set_choice("sm1cs_dc006_date_dc")
    return