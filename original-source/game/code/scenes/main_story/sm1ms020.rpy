label sm1ms020:
    scene black
    show screen scene_transistion(_("A half hour later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 0.0, "music2" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music light_casual_guitar fadein 1.5
    scene sm1ms020-01 mc-sy-my-entry1_c1
    with Fade(0.5, 0.5, 0.5)
    play voice2 d1s5_mchappy noloop volume 1.7
    mct "Man, we did a really good job with the renovation."
    mct "It's really starting to look like a real porn studio in here."
    play sound sfx_cloth_rustling1
    scene sm1ms020-01-1 mc-sy-my-entry1_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "I can't wait to start filming in here."
    mct "There's so much room for activities!"
    play sound sfx_knock_wood1
    scene sm1ms020-02 mc-sy-my-entry2_c1 with dissolve
    play voice2 mc_angry_huh1 noloop
    if persistent.is_special:
        mct "Oh, Mom must be done with her call."
    else:
        mct "Oh, Melony must be done with her call."
    play sound sfx_door_creak4
    scene sm1ms020-02 mc-sy-my-entry2_c2 with dissolve
    play voice4 girl34_hey_hi1 noloop
    mc "All done?"
    my "Yep!"
    play voice2 d1s2_hmm noloop volume 1.7
    play sound sfx_heels_steps2 loop
    scene sm1ms020-02 mc-sy-my-entry2_c3 with dissolve
    sy "How was your phone call?"
    my "It was good! The client is just a little anxious 24/7. Just needed some gentle reassuring."
    scene sm1ms020-03 mc-sy-my-entry3_c2 with dissolve
    play voice3 girl34_surprised_ohmy2 noloop
    my "My, my - are you two going out?"
    scene sm1ms020-03 mc-sy-my-entry3_c1 with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "We are!"
    stop sound fadeout 1.0
    scene sm1ms020-04 mc-sy-my-talk_c1 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "We're going out to celebrate the studio being renovated!"
    scene sm1ms020-04 mc-sy-my-talk_c2 with dissolve
    play voice4 girl34_surprised_oh4 noloop
    my "Oh that sounds like a ton of fun!"
    my "Would you two mind if an old gal like me crashed your celebration?"
    scene sm1ms020-05 mc-sy-my-talk2_c1 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Are you kidding me? You're not old!"
    sy "And of course you're welcome to join us!"
    scene sm1ms020-06 mc-sy-my-talk3_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    if persistent.is_special:
        mc "You're always invited to spend time with us, Mom."
    else:
        mc "You're always invited to spend time with us, Melony."
    mc "And you did so much to help around the studio, it would only be right if you were there with us. "
    play sound sfx_heels_steps2 loop
    scene sm1ms020-06 mc-sy-my-talk3_c2 with dissolve
    play voice4 girl34_happy_yay2 noloop
    my "Yay! So where are we going?"
    scene sm1ms020-06 mc-sy-my-talk3_c3 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "You'll see."
    play sound sfx_door_open1
    scene sm1ms020-07 mc-sy-my-walk_c2 with dissolve
    play voice4 girl34_arrogant_laugh1 noloop
    my "Aye yi yi..."
    scene sm1ms020-07 mc-sy-my-walk_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    if persistent.is_special:
        mc "Hey, she's your daughter!"
        play voice4 girl34_yes_neutral7 noloop
        my "And your sister."
    else:
        mc "You know how Stacy is."
        play voice4 girl34_yes_neutral7 noloop
        my "Yes, yes I do."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1ms020-08 mc-sy-my-walk2_c1 with dissolve
    play voice4 girl34_yes_ugu1 noloop
    my "Come along, [mcname]. Let's catch up to her."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop music fadeout 3.0
    play sound sfx_double_door1
    play music2 music_whiskey_rock_radio volume 0.8 fadein 2.0
    play sound4 sfx_crowd_fightclub_ambient2 fadein 3.0 volume 0.8
    scene sm1ms020-09 mc-sy-my-entry_c2 with Fade(0.5, 0.5, 0.5)
    queue sound sfx_heels_steps1 loop
    queue sound2 sfx_heels_steps2
    play voice3 stacy_happy_wooh1 noloop
    sy "Tadaaaaa!"
    play voice2 d1s1_mmm noloop
    if LocationController.get_map_location(GR_BAR).get_location().get_discovered_status():
        mct "I should've assumed this was the bar Stacy was talking about when she said she wanted to go to a dive."
    else:
        mct "Wow, when Stacy said dive... I didn't think it would be this much of a dive."
    scene sm1ms020-10 mc-sy-my-entry2_c2 with dissolve
    play voice4 girl34_surprised_oh1 noloop
    my "Oh! You brought us to Guns and Rosette's!"
    scene sm1ms020-11 mc-sy-my-talk_c1 with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "You... you've been here before?"
    scene sm1ms020-11 mc-sy-my-talk_c2 with dissolve
    play voice4 girl34_yes_aga1 noloop
    my "A long, long time ago this was my drinking spot!"
    scene sm1ms020-13 mc-sy-my-walk_c1 with dissolve
    play voice3 stacy_surprised_huh3 noloop
    sy "What!"
    scene sm1ms020-13 mc-sy-my-walk_c2 with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "You used to live in Crowning?"
    play voice4 girl34_yes_happy2 noloop
    my "You know I had a life before you two, right?"
    play sound sfx_bed_slide2
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(0.3, 10.5, "sound4" )
    scene sm1ms020-14 mc-sy-my-sit_c2 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "Apparently. We've learned a lot about you since we started the renovation. You have nudes, you used to live in Crowning..."
    play voice4 girl34_arrogant_yeah noloop
    my "Well you two never asked me about me before!"
    scene sm1ms020-15 mc-sy-my-ask_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Well... why did you used to live in Crowning?"
    scene sm1ms020-15 mc-sy-my-ask_c2 with dissolve
    play voice4 girl34_disappointed_mmf1 noloop
    my "This is where I did my art residency."
    scene sm1ms020-16 mc-sy-my-ask2_c3 with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "You did an art residency?"
    scene sm1ms020-17 mc-sy-my-talk_c1 with dissolve
    play voice4 girl34_yes_ugu2 noloop
    my "Mmhmmmm. I started meeting artists here, and then gallery owners..."
    my "This is where my career got jump started."
    play sound sfx_heels_steps1
    scene sm1ms020-17 mc-sy-my-talk_c3 with dissolve
    play voice5 girl26_hey_confused noloop
    "Bartender" "What can I get you?"
    stop sound fadeout 1.0
    scene sm1ms020-18 mc-sy-my-talk2_c2 with dissolve
    play voice4 girl34_thinking_emm1 noloop
    my "I'll have a glass of your house red, and-"
    scene sm1ms020-18 mc-sy-my-talk2_c1 with dissolve
    play voice3 stacy_disappointed_oh5 noloop
    sy "Oooo! That sounds delicious, make that two!"
    scene sm1ms020-18 mc-sy-my-talk2_c4 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "And I'll have a beer."
    play sound sfx_bottle_pouring1 volume 1.6
    scene sm1ms020-19 mc-sy-my-talk3_c3 with dissolve
    play voice5 girl26_yes_ugu noloop
    "Bartender" "Coming right up."
    scene sm1ms020-19 mc-sy-my-talk3_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "So, you started being a gallery...?"
    scene sm1ms020-19 mc-sy-my-talk3_c2 with dissolve
    play voice4 girl34_yes_yeap2 noloop
    my "An art gallery manager."
    scene sm1ms020-20 mc-sy-my-talk4_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "What do you do as an art gallery manager?"
    scene sm1ms020-20 mc-sy-my-talk4_c2 with dissolve
    play voice4 girl34_thinking_hmm6 noloop
    my "I manage connections between investors and the gallery, talent scout for new artist's to showcase..."
    my "It's all truly boring stuff, you don't want to hear about that."
    scene sm1ms020-21 mc-sy-my-talk5_c1 with dissolve
    play voice2 mc_no_no6 noloop
    if persistent.is_special:
        mc "No, no, Mom. I do! I've started to realize, there's a lot I don't know about you."
    else:
        mc "No, no, Melony. I do! I've started to realize, there's a lot I don't know about you."
    scene sm1ms020-21 mc-sy-my-talk5_c2 with dissolve
    play voice4 girl34_happy_relief2 noloop
    my "You know, [mcname]... I came here to chastise you about going back to school."
    my "Before you moved here... to put it mildly, you were a little shit."
    play voice3 stacy_scared_ah1 noloop
    scene sm1ms020-21 mc-sy-my-talk5_c3 with hpunch
    if persistent.is_special:
        sy "Mom!"
    else:
        sy "Melony!"
    scene sm1ms020-17 mc-sy-my-talk_c1 with dissolve
    play voice4 girl34_angry_ahem1 noloop
    my "Don't you start missy. You've got all his bad habits, and more."
    play sound sfx_cloth_rustling1
    scene sm1ms020-22 mc-sy-my-talk6_c2 with dissolve
    play voice4 girl34_disappointed_eeh2 noloop
    my "But, and this applies to both of you..."
    scene sm1ms020-23 mc-sy-my-close_c2 with dissolve
    play voice4 girl34_happy_relief1 noloop
    my "You've shown me what a fine, young man you've turned into [mcname]."
    my "You're dedicated, {i}passionate{/i}, caring..."
    scene sm1ms020-22 mc-sy-my-talk6_c3 with dissolve
    play voice4 girl34_happy_mmm1 noloop
    if persistent.is_special:
        my "And you've taken great care of your sister."
    else:
        my "And you've taken great care of Stacy."
    play voice3 stacy_yes_simple1 noloop
    sy "He really has."
    $ renpy.music.set_volume(0.6, 5.0, "music2" )
    queue music2 music_shadow_whiskey_rock_radio
    scene sm1ms020-22 mc-sy-my-talk6_c2 with dissolve
    play voice4 girl34_thinking_emm5 noloop
    my "Even in the middle of... everything you've gone through, you're still a good man."
    my "A man I am proud to know, a man I want to get to know better..."
    my "But, if you'll excuse me - I need to visit the ladies room."
    play sound sfx_cloth_planket2
    play sound2 sfx_heels_steps1
    scene sm1ms020-24 mc-sy-my-walk_c1 with dissolve
    pause
    stop sound2 fadeout 1.0
    scene sm1ms020-24 mc-sy-my-walk_c2 with dissolve
    play voice3 stacy_surprised_ohmy1 noloop
    sy "Oh my God! [mcname], you dog!"
    scene sm1ms020-25 mc-sy-my-look_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "W-what?"
    scene sm1ms020-25 mc-sy-my-look_c2 with dissolve
    play voice3 stacy_arrogant_huh5 noloop
    if persistent.is_special:
        sy "You're flirting with Mom!"
    else:
        sy "You're flirting with Melony!"
    scene sm1ms020-26 mc-sy-my-look2_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "No I'm not!"
    scene sm1ms020-26 mc-sy-my-look2_c2 with dissolve
    play voice3 stacy_angry noloop
    sy "Bull shit!"
    scene sm1ms020-27 mc-sy-my-close_c1 with dissolve
    play voice2 mc_no_no4 noloop
    mc "I'm not! I swear!"
    scene sm1ms020-27 mc-sy-my-close_c2 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, you should."
    play sound sfx_cloth_rustling3
    scene sm1ms020-28 mc-sy-my-close2_c1 with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "I-wait..."
    mc "What? What are you saying?"
    scene sm1ms020-28 mc-sy-my-close2_c2 with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "You know what I'm saying."
    if persistent.is_special:
        sy "You should totally hit on Mom. She was hitting on you."
    else:
        sy "You should totally hit on Melony. She was hitting on you."
    scene sm1ms020-29 mc-sy-my-look_c1 with dissolve
    play voice2 mc_no_uhuhno noloop
    mc "Nuh uh, she was not."
    scene sm1ms020-29 mc-sy-my-look_c2 with dissolve
    play voice3 stacy_disgust_ehh2 noloop
    sy "Was too. You're dense, [mcname]. Trust me, she was."
    if persistent.is_special:
        sy "This is why you need your sister. Best. Wingman. Ever."
    else:
        sy "This is why you need me. I'm the best damn wingman ever."
    scene sm1ms020-27 mc-sy-my-close_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I don't know, Stacy..."
    scene sm1ms020-27 mc-sy-my-close_c2 with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "Come on, you know she's hot."
    scene sm1ms020-25 mc-sy-my-look_c1 with dissolve
    play voice2 mc_znames_stacy3 noloop
    mc "Stacy-!"
    scene sm1ms020-29 mc-sy-my-look_c2 with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    if persistent.is_special:
        sy "Come on! Mom is fucking {i}foxy!{/i} And she has a banging bod."
    else:
        sy "Come on! Melony is fucking {i}sexy!{/i} And she has a banging bod."
    sy "I'd fuck her if I could."
    play sound sfx_cloth_rustling1
    scene sm1ms020-30 mc-sy-my-stand_c2 with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "And you totally can."
    scene sm1ms020-31 mc-sy-my-talk_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Come on, Stacy..."
    scene sm1ms020-31 mc-sy-my-talk_c2 with dissolve
    play voice3 stacy_yeahno noloop
    sy "I'm just saying. Hell, it might help us out if she plans to stay around."
    scene sm1ms020-32 mc-sy-my-talk2_c2 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "Because a good dicking down can do a lot for someone."
    play voice2 d1s1_mmm noloop
    mct "She makes a good point..."
    if persistent.is_special:
        mct "Mom is cool with everything right now, but... who knows how long that'll last."
    else:
        mct "Melony is cool with everything right now, but... who knows how long that'll last."
    mct "And a good dicking down would definitely help keep her calm."
    mct "But..."
    if persistent.is_special:
        mct "She is my mom..."
    else:
        mct "She is Melony..."
    menu:
        "Try and see where things go"(hint="sm1ms020_m01_h01"):
            call sm1ms020_m01_c01 from _call_sm1ms020_m01_c01
            scene sm1ms020-32 mc-sy-my-talk2_c1 with dissolve
            play voice2 mc_thinking_hmm7 noloop
            mc "Well, we can see if she was really flirting with me or not."
            play voice3 stacy_yes noloop
            sy "Yes! Hell yes."
            if persistent.is_special:
                sy "This is so hot... [mcname] hitting on our mom."
            else:
                sy "This is so hot... [mcname] hitting on our oldest, family friend."
            play sound sfx_heels_steps1 loop
            scene sm1ms020-33 mc-sy-my-walk_c1 with dissolve
            play voice3 stacy_happy_laugh1 noloop
            sy "Well you'll get a chance to test my theory! Here she comes."
            play voice2 mc_arrogant_heh2 noloop
            mct "All right, game face, [mcname]."
            if persistent.is_special:
                mct "Time to find out if my Mom was actually hitting on me... or if I'm about to make our next family get together really awkward."
            else:
                mct "Time to find out if Melony was actually hitting on me... or if I'm about to make our next get together really awkward."
            play sound "<from 0 to 1>audio/sfx/appliances/sfx_plates_moving1.ogg"
            jump sm1ms020_flirting
        "Leave it alone"(hint="sm1ms020_m01_h02"):
            scene sm1ms020-32 mc-sy-my-talk2_c1 with dissolve
            play voice2 mc_arrogant_nah1 noloop
            mc "I don't know, Stacy..."
            scene sm1ms020-32 mc-sy-my-talk2_c2 with dissolve
            play voice3 stacy_hey_angry1 noloop
            sy "Come on, you got this!"
            play voice2 mc_disappointed_ah1 noloop
            mc "It's not that, I just..."
            play sound sfx_heels_steps1 loop
            scene sm1ms020-33 mc-sy-my-walk_c1 with dissolve
            play voice2 mc_no_noway noloop
            if persistent.is_special:
                mc "I just don't think it's a good idea for me to hit on Mom."
            else:
                mc "I just don't think it's a good idea for me to hit on Melony."
            play voice3 stacy_yes_fine3 noloop
            sy "Fine.{w} Party pooper."
            stop sound fadeout 1.5
            scene sm1ms020-35 mc-sy-my-look_c1 with dissolve
            play voice4 girl34_surprised_ah1 noloop
            my "Did I miss anything?"
            play voice2 mc_no_nope2 noloop
            mc "Nope! Just some chit chatting."
            play sound "<from 0 to 1>audio/sfx/appliances/sfx_plates_moving1.ogg"
            scene sm1ms020-35 mc-sy-my-look_c2 with dissolve
            pause
            jump sm1ms020_cheers
label sm1ms020_flirting:
    scene sm1ms020-35 mc-sy-my-look_c2 with dissolve
    pause
    play sound sfx_plate_place1
    scene sm1ms020-36 mc-sy-my-look2_c1 with dissolve
    play voice4 girl34_yes_aga4 noloop
    pause
    scene sm1ms020-37 mc-sy-my-talk_c1 with dissolve
    play voice4 girl34_thinking_emm2 noloop
    my "And what are you two chit chatting about?"
    scene sm1ms020-37 mc-sy-my-talk_c2 with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh nooooooothing!"
    scene sm1ms020-38 mc-sy-my-talk2_c1 with dissolve
    play voice4 girl34_yes_yeah5 noloop
    my "Is that so? No little juicy tidbits or gossip?"
    play voice3 stacy_thinking_emm4 noloop
    sy "Weeellllll, there was one thing. Right, [mcname]?"
    play voice2 mc_yes_yeah8 noloop
    mc "There was?"
    play sound sfx_cloth_rustling2
    scene sm1ms020-38 mc-sy-my-talk2_c2 with dissolve
    play voice3 stacy_yes_ugu1 noloop volume 1.4
    sy "Uh huh! I think we can tell her, don't you, [mcname]?"
    scene sm1ms020-39 mc-sy-my-talk3_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "Uhm... yeah, I, uhh, think so?"
    mct "What the hell is she talking about?"
    scene sm1ms020-39 mc-sy-my-talk3_c2 with dissolve
    play voice3 stacy_thinking_hmm2 noloop
    sy "So, now that you know what [mcname] does for work, and you're kind of okay with it..."
    play voice4 girl34_angry_hmf noloop
    my "Is this going somewhere, Stacy?"
    sy "It is! [mcname] thought it would be a great idea to do a swimsuit competition with some of the gals that work with us!"
    scene sm1ms020-39 mc-sy-my-talk3_c1 with dissolve
    play voice4 girl34_surprised_huh1 noloop
    my "Is that so?"
    scene sm1ms020-39 mc-sy-my-talk3_c2 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "It is!"
    play sound sfx_cup_slide1
    scene sm1ms020-57 mc-sy-my-stand_c1 with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "But now it's my turn to visit the ladies room."
    play sound sfx_heels_steps2
    scene sm1ms020-58 mc-sy-my-walk_c2 with dissolve
    play voice4 girl34_arrogant_ha5 noloop
    my "So a swimsuit competition, huh?"
    scene sm1ms020-59 mc-sy-my-look_c1 with dissolve
    play sound2 sfx_hair_scratch1 noloop
    play voice2 d2s12_emmm noloop volume 1.4
    mc "Erm, yep. It, uhhh, can be a great competition and lead to some great promotional shots?"
    scene sm1ms020-59 mc-sy-my-look_c2 with dissolve
    play voice4 girl34_yes_aga3 noloop
    my "Uh huh."
    play sound sfx_cloth_rustling2
    scene sm1ms020-60 mc-sy-my-look2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "What! We do one thing, and it helps to have promotional shots that show off the models!"
    scene sm1ms020-60 mc-sy-my-look2_c2 with dissolve
    play voice4 girl34_yes_yeah2 noloop
    my "Yeah, yeah.{w} It's a smart idea though."
    scene sm1ms020-61 mc-sy-my-ask_c1 with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Really? You think so?"
    scene sm1ms020-61 mc-sy-my-ask_c2 with dissolve
    play voice4 girl34_yes_yeah8 noloop
    my "Yeah, it's a good way to make some advertisements, plus it's good for morale."
    my "Who doesn't like looking good in a swimsuit?"
    play sound sfx_cloth_rustling3
    scene sm1ms020-62 mc-sy-my-look_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Yeah, I didn't even think about that."
    scene sm1ms020-62 mc-sy-my-look_c2 with dissolve
    play voice4 girl34_happy_relief3 noloop
    my "God... I can't even remember the last time I put on a swimsuit. It had to be... ages ago."
    my "I bet I couldn't even fit into any of my old swimsuits anymore..."
    scene sm1ms020-63 mc-sy-my-look2_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Oh, Stacy. You clever girl.{w} Now I see what you were doing."
    play voice2 mc_no_uhuh1 noloop
    if persistent.is_special:
        mc "I doubt that, Mom! You look great!"
    else:
        mc "I doubt that, Melony! You look great!"
    scene sm1ms020-63 mc-sy-my-look2_c2 with dissolve
    play voice4 girl34_disappointed_oh2 noloop
    my "You're just saying that because you have to."
    scene sm1ms020-64 mc-sy-my-look3_c1 with dissolve
    play voice2 mc_no_no7 noloop
    mc "I swear, I'm not. You look amazing! I bet you'd look great in whatever swimsuit you have at home."
    scene sm1ms020-64 mc-sy-my-look3_c2 with dissolve
    play voice4 girl34_yes_yeah6 noloop
    my "Yeah, yeah-"
    scene sm1ms020-64 mc-sy-my-look3_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "I swear, on my honor as a gentleman, that I'm not lying to you."
    scene sm1ms020-65 mc-sy-my-ask_c2 with dissolve
    play voice4 girl34_disappointed_oh1 noloop
    my "Oh? On your honor as a gentleman. Very serious oath you're swearing there, [mcname]."
    scene sm1ms020-65 mc-sy-my-ask_c1 with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "It's because I'm serious!"
    scene sm1ms020-66 mc-sy-my-look_c2 with dissolve
    play voice4 girl34_thinking_emm4 noloop
    my "Well, how do I know it means anything? I don't know anything about your honor as a gentleman."
    scene sm1ms020-66 mc-sy-my-look_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well I'll just have to show you then!"
    play sound sfx_heels_steps2 loop fadein 5.0
    scene sm1ms020-67 mc-sy-my-ask_c2 with dissolve
    play voice4 girl34_arrogant_huh3 noloop
    my "Your honor as a gentleman?"
    scene sm1ms020-67 mc-sy-my-ask_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Exactly! If that's what it takes to prove to you I'm not lying, that's what I'll have to do!"
    play voice4 girl34_arrogant_hm2 noloop
    my "Well, I look forward to whatever you have planned to show me how much of a gentleman you are."
    mct "Well... I might be a little dense, but..."
    if persistent.is_special:
        mct "I'm pretty sure I just agreed to take my Mom on a date."
    else:
        mct "I'm pretty sure I just agreed to take Melony on a date."
    stop sound fadeout 1.0
    scene sm1ms020-68 mc-sy-my-ask2_c1 with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Now it's my turn to ask - what'd I miss?"
    scene sm1ms020-68 mc-sy-my-ask2_c2 with dissolve
    play voice4 girl34_thinking_eeh1 noloop
    if persistent.is_special:
        my "Oh, just your brother swearing on his honor as a gentleman."
    else:
        my "Oh, just [mcname] swearing on his honor as a gentleman."
    play sound sfx_cloth_planket2
    scene sm1ms020-69 mc-sy-my-talk_c1 with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "What! You have honor! And you're a gentleman!"
    play voice2 mc_yes_sure1 noloop
    mc "Of course! I have plenty of gentlemanly honor!"
    play sound sfx_hands_clap3
    scene sm1ms020-69 mc-sy-my-talk_c2 with dissolve
    play voice4 girl34_angry_ahem2 noloop
    if persistent.is_special:
        my "Quit picking on your brother!"
    else:
        my "Quit picking on [mcname]!"
    play voice3 stacy_pain_au3 noloop
    sy "Sooorrrrrrrrryyyy, I can't help it."
    my "Oh, you two, I swear."
    jump sm1ms020_cheers
label sm1ms020_cheers:
    play sound sfx_plate_place1
    scene sm1ms020-38 mc-sy-my-talk2_c1 with dissolve
    play voice4 girl34_hey_simple4 noloop
    my "But, now that we have these drinks, we should do a toast!"
    scene sm1ms020-38 mc-sy-my-talk2_c2 with dissolve
    play voice3 stacy_happy_yay2 noloop
    sy "I love toasts! What should we toast to?"
    play voice4 girl34_thinking_hmm7 noloop
    my "Well, we all should pick something. What about you, Stacy? What do you want to toast to?"
    play voice3 stacy_happy_relief1 noloop
    sy "A toast to this damn renovation being over, and going back to no more manual labor!"
    scene sm1ms020-39 mc-sy-my-talk3_c1 with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "I can toast to that!"
    scene sm1ms020-40 mc-sy-my-look_c2 with dissolve
    play voice4 girl34_arrogant_ha4 noloop
    my "And what about you, [mcname]?"
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Hmmm..."
    menu:
        "To the future!"(hint="sm1ms020_m02_h01"):
            call sm1ms020_m02_c01 from _call_sm1ms020_m02_c01
            scene sm1ms020-40 mc-sy-my-look_c1 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "To a profitable and wonderful future for the studio!"
        "To the two of you!"(hint="sm1ms020_m02_h02"):
            call sm1ms020_m02_c02 from _call_sm1ms020_m02_c02
            scene sm1ms020-40 mc-sy-my-look_c1 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "To the wonderful women in my life! I don't know what I would have done without the two of you."
        "To no more manual labor!"(hint="sm1ms020_m02_h03"):
            call sm1ms020_m02_c03 from _call_sm1ms020_m02_c03
            scene sm1ms020-40 mc-sy-my-look_c1 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "The same thing as Stacy! Grateful that the renovation is over, and that it went well."
    if persistent.is_special:
        mc "And what about you, Mom?"
    else:
        mc "And what about you, Melony?"
    scene sm1ms020-40 mc-sy-my-look_c2 with dissolve
    play voice4 girl34_happy_relief4 noloop
    my "To having you two back in my life."
    my "I am... so, so grateful that I came to see you, [mcname]. And that I got to help you with the renovation."
    my "And you, Stacy. Quite the duo."
    if persistent.is_special:
        my "So a toast, to my two wonderful kids."
    else:
        my "So a toast, to you two wonderful humans."
    play sound sfx_wineglass_ding1
    play sound2 sfx_drink_horse1
    play sound3 sfx_drink_loop1 volume 2.5
    scene sm1ms020-41 mc-sy-my-drink_c1 with dissolve
    pause
    stop sound2 fadeout 2.0
    stop sound3 fadeout 5.0
    scene sm1ms020-41 mc-sy-my-drink_c2 with dissolve
    play voice4 girl34_yes_ugu2 noloop
    my "And with that, this old lady needs to get home!"
    stop sound3 fadeout 1.0
    scene sm1ms020-42 mc-sy-my-talk_c1 with dissolve
    play voice3 stacy_disappointed_oh3 noloop
    sy "What! No, stay out with us!"
    play sound sfx_cup_place1 volume 2.0
    scene sm1ms020-42 mc-sy-my-talk_c2 with dissolve
    play voice4 girl34_no_nonono1 noloop
    my "No, no. It is way past my bedtime."
    my "You two kids shut the bar down for me, okay?"
    scene sm1ms020-43 mc-sy-my-talk2_c1 with dissolve
    play voice3 stacy_disappointed_mmm2 noloop
    sy "Okaaaayyyy..."
    play sound sfx_heels_steps1 loop
    scene sm1ms020-44 mc-sy-my-walk_c1 with dissolve
    play voice2 mc_hey_bye2 noloop
    if persistent.is_special:
        mc "Good night, Mom!"
    else:
        mc "Good night, Melony!"
    scene sm1ms020-44 mc-sy-my-walk_c2 with dissolve
    play voice4 girl34_hey_bye9 noloop
    my "Good night, [mcname]."
    stop sound fadeout 2.0
    if player.get_choice("sm1ms020_flirt_my"):
        scene sm1ms020-45 mc-sy-my-talk_c1 with dissolve
        play voice3 stacy_arrogant_huh1 noloop
        sy "How'd it go?"
        scene sm1ms020-45 mc-sy-my-talk_c2 with dissolve
        play voice2 mc_thinking_oh1 noloop
        mc "I think... I asked her out on a date."
        scene sm1ms020-46 mc-sy-my-talk2_c1 with dissolve
        play voice3 stacy_angryhuh noloop
        sy "What! Ballsy move, [mcname]."
        scene sm1ms020-46 mc-sy-my-talk2_c2 with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah, but it worked out. She agreed."
        play voice3 stacy_pain_cough1 noloop
        scene sm1ms020-48 mc-sy-my-talk4_c1 with vpunch
        sy "What!? WHAT!?!"
        scene sm1ms020-47 mc-sy-my-talk3_c2 with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "Yeah, so now I just need to figure out what I'm going to do on this date."
        scene sm1ms020-47 mc-sy-my-talk3_c1 with dissolve
        play voice3 stacy_surprised_wow1 noloop
        if persistent.is_special:
            sy "You got this. If you can wine and dine me, you can win over Mom."
        else:
            sy "You got this. If you can wine and dine me, you can win over Melony."
        scene sm1ms020-48 mc-sy-my-talk4_c2 with dissolve
        play voice2 mc_yes_ugu1 noloop
        mc "I hope so."
    scene sm1ms020-49 mc-sy-my-talk5_c1 with dissolve
    play voice3 stacy_happy_phew1 noloop
    sy "But, here's to us! And to finally being able to start filming again!"
    scene sm1ms020-49 mc-sy-my-talk5_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, thank God for that!"
    play sound sfx_wineglass_ding1
    scene sm1ms020-50 mc-sy-my-talk6_c1 with dissolve
    pause
    play sound sfx_drink_loop1 loop volume 2.5
    play sound2 [sfx_drink_gulp, "<silence 1.0>", sfx_drink_gulp] noloop
    scene sm1ms020-51 mc-sy-my-drink_c1 with dissolve
    pause
    play sound2 sfx_cloth_rustling2 noloop
    scene sm1ms020-52 mc-sy-my-down_c1 with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "You know, filming isn't the only thing we can start doing again?"
    scene sm1ms020-52 mc-sy-my-down_c2 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Hehehe."
    mc "What else can we do again?"
    play sound sfx_cup_slide1
    scene sm1ms020-52-1 mc-sy-my-look_c1 with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "Hahaha."
    sy "I was thinking that it is past time we try out our new bed."
    scene sm1ms020-52-1 mc-sy-my-look_c2 with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "Mmmm. Not a bad idea."
    play sound sfx_cup_place1
    scene sm1ms020-52-2 mc-sy-my-ask_c1 with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "Alright, let's get the check and then get out of here."
    play sound sfx_cloth_rustling4
    scene sm1ms020-52-3 mc-sy-my-close_c2 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    pause
    stop music2 fadeout 3.0
    call sm1_unlock_gr_bar from _call_sm1_unlock_gr_bar_2
    call sm1ms020_unlock_new_bed from _call_sm1ms020_unlock_new_bed
    call sm1ms020_renovation_changes from _call_sm1ms020_renovation_changes
    stop music fadeout 3.0
    stop sound4 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.5, "sound4" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1ms020_exit_to_free_roam
label sm1ms020_exit_to_free_roam:
    $ StoryController.end_scene(MS, 0, 0, 0, STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_BED)
    return
label sm1ms020_unlock_new_bed:
    $ ObjectController.get_object(RENOVATED_BED).unlock()
    $ ObjectController.get_object(RENOVATED_BED).add_override_interaction_option("io-Sleep-with-time-skip")
    $ ObjectController.get_object(BED).lock()
    return
label sm1ms020_renovation_changes:
    $ player.create_storyline(MY_STORY)
    $ CharacterController.get_character("sy").add_schedule("default_sy2")
    $ CharacterController.get_character("my").add_schedule("default_my2")
    $ CharacterController.get_character("sy").remove_schedule("default_sy")
    $ CharacterController.get_character("sy").remove_schedule("sy_MS005_perma")
    $ LocationController.get_location(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM).add_override_interaction_option("io-SD_Peek_On_Stacy")
    return
label sm1ms020_m01_c01:
    $ player.set_choice("sm1ms020_flirt_my")
    return
label sm1ms020_m02_c01:
    $ player.set_choice("sm1ms020_future")
    return
label sm1ms020_m02_c02:
    $ player.set_choice("sm1ms020_my_and_sy")
    return
label sm1ms020_m02_c03:
    $ player.set_choice("sm1ms020_manual_labour")
    return