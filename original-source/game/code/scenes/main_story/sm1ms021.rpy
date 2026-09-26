label sm1ms021:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music past_sadness
    scene sm1ms021-00 the_next_concept with dissolve
    play voice2 d1s5b_ehhh noloop
    mc "Still incredible thinking that this place used to be that old rundown space."
    scene sm1ms021-01 the_next_concept_sy_talk with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "I know, right? Feels like just yesterday we were just sleeping on a musty old mattress on the floor."
    sy "Now we have an upstairs bedroom."
    scene sm1ms021-02 the_next_concept_mc_talk_question with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, but it's still not a room room."
    scene sm1ms021-03 the_next_concept_mc_talk_switch with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "You sure you're cool rawdogging it?"
    mc "Could make for awkward situations with guests."
    if player.has_played_scene("sm1cs_ns010"):
        mc "And I don't know what Nari will think if she comes to live here."
        scene sm1ms021-04 the_next_concept_sy_talk with dissolve
        play voice3 stacy_hey_happy2 noloop
        sy "Hey, our house, our rules."
        scene sm1ms021-05 the_next_concept_mc_talk with dissolve
        play voice2 mc_yes_okay1 noloop
        mc "Good point."
    play sound sfx_heels_steps2 loop
    scene sm1ms021-06 the_next_concept_sy_stairs with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1ms021-07 the_next_concept_sy_talk_stairs with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "Come on, hot stuff. The view from upstairs is way better."
    play sound sfx_heels_steps1 loop
    scene sm1ms021-08 the_next_concept_mc_talk_stairs with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Haha."
    stop sound fadeout 1.0
    play sound2 sfx_metal_fence2 noloop
    scene sm1ms021-09 the_next_concept_mc_talk_lookdown with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "It was a lot of hard work and sweat, but it's finally over."
    play sound sfx_cloth_rustling1
    scene sm1ms021-10 the_next_concept_mc_talk_look_fingers with dissolve
    play voice2 mc_angry_errr6 noloop
    mc "I never knew how painful it is to wang your own finger with a hammer until we did this."
    scene sm1ms021-11 the_next_concept_sy_talk_grin with dissolve
    play voice3 stacy_hey noloop
    sy "Hey remember. No pain, no gain."
    scene sm1ms021-12 the_next_concept_mc_talk_chuckles with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Just remember that when I try to finger you with a swollen index finger."
    scene sm1ms021-13 the_next_concept_sy_talk_horny with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "I guess you can always finger me with something else."
    sy "I know something else that is meant to get swollen."
    play sound sfx_cloth_rustling3
    scene sm1ms021-14 the_next_concept_sy_talk_horny_chest with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "And it gets swollen a lot when I'm around."
    scene sm1ms021-15 the_next_concept_mc_talk_smile with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Nice."
    scene sm1ms021-16 the_next_concept_mc_talk_playdumb with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "You're talking about me, dick, right?"
    play sound sfx_hair_scratch1
    scene sm1ms021-17 the_next_concept_sy_talk_touchface with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "Oh my god. You did not just ask that."
    play sound sfx_heels_steps2 loop
    scene sm1ms021-18 the_next_concept_sy_talk_walkaway with dissolve
    play voice3 stacy_happy_laugh4 noloop
    sy "*laughing*"
    stop sound fadeout 1.0
    scene sm1ms021-19 the_next_concept_sy_lookout with dissolve
    pause
    play voice3 stacy_smell noloop
    scene sm1ms021-20 the_next_concept_sy_smile with dissolve
    pause
    scene sm1ms021-21 the_next_concept_sy_talk_turnbackmc with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "I'm feeling good, you know?"
    scene sm1ms021-22 the_next_concept_mc_talk with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Yeah."
    scene sm1ms021-23 the_next_concept_sy_talk_relieved with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "This space... it’s not just a studio anymore. It’s starting to feel like our dream is finally taking shape."
    sy "It's crazy thinking not too long ago we were just recording ourselves having some fun at my apartment."
    sy "And now we've got our first adult film under our belts."
    scene sm1ms021-24 the_next_concept_sy_talk_lovingly with dissolve
    play voice3 stacy_hmm noloop volume 1.4
    sy "You really stepped up, [mcname]."
    play sound sfx_cloth_rustling4
    scene sm1ms021-25 the_next_concept_sy_talk_hug with dissolve
    play voice3 stacy_moan4 noloop
    sy "Mmm."
    scene sm1ms021-26 the_next_concept_mc_talk_hug with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "We did this together, Stacy. Couldn't have done it without you."
    scene sm1ms021-27 the_next_concept_sy_talk_hug with dissolve
    play voice3 stacy_yes_yap2 noloop
    sy "Same here. I mean, you’re the one who kept me sane through all of this."
    play sound sfx_cloth_rustling5
    scene sm1ms021-28 the_next_concept_sy_talk_hug_finished with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    if persistent.is_special:
        sy "And with mom around, it's been just a little bit more hectic."
    else:
        sy "And with Melony around, it's just been a little bit more hectic."
    scene sm1ms021-29 the_next_concept_mc_talk_smiling with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "We always knew that it wasn't going to be easy."
    if persistent.is_special:
        mc "Mom being so... 'close' is just an extra hoop to jump through."
    else:
        mc "Melony being so... 'close' is just an extra hoop to jump through."
    scene sm1ms021-30 the_next_concept_sy_talk_smiling with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Yup."
    play sound sfx_cloth_rustling1
    scene sm1ms021-31 the_next_concept_sy_talk_phone with dissolve
    play sound2 sfx_message_in1 noloop
    play voice3 stacy_thinking_hmm4 noloop
    sy "Mmm."
    scene sm1ms021-32 the_next_concept_sy_talk_fist with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "Score."
    sy "More good news! {w}The client who commissioned the first film is ready to start another one."
    scene sm1ms021-33 the_next_concept_mc_talk_thinking with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "So soon? Man, it must be nice to have money."
    scene sm1ms021-34 the_next_concept_sy_talk with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, soon it will be our money."
    scene sm1ms021-35 the_next_concept_sy_talk_gesturefollow with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Come on, I'll load up the email on the computer."
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1ms021-36 the_next_concept_sy_talk_computer with fade
    play voice3 stacy_thinking_hmm2 noloop
    sy "Here is some of what they wrote."
    sy "'Loved your work. The scene was exactly what I was looking for.'"
    sy "'Great work by both of your actors and your camera work. I really enjoyed watching the film.'"
    scene sm1ms021-37 the_next_concept_mc_talk_smiling with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Customer feedback. Why does it taste so sweet?"
    scene sm1ms021-38 the_next_concept_sy_talk_horny with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "I know, right?"
    play sound sfx_keyboard_enter1
    scene sm1ms021-39 the_next_concept_sy_talk_scrolling with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Whoever it is, sounds like they totally jerked off to our film."
    sy "Ooouha. That's so hot."
    sy "And it keeps getting better!"
    scene sm1ms021-40 the_next_concept_mc_talk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "'This is embarrassing, but if I can't talk to you about it, who can I?'"
    mc "'I have always been a fan of buttstuff. Not just anal sex, but that is where we can start.'"
    mc "Start?"
    scene sm1ms021-41 the_next_concept_sy_talk with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "Sweet. Maybe they're planning to do another one after this one."
    scene sm1ms021-42 the_next_concept_mc_talk_cool with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Haha. Relax. Let's just focus on the meal in front of us."
    play sound sfx_keyboard_typing2
    scene sm1ms021-43 the_next_concept_sy_talk with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "Right, right."
    scene sm1ms021-44 the_next_concept_mc_talk_reading_closer with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "'So for this new scene, I would like to have it focus on anal sex.'"
    mc "'You can use toys and fingering or whatever, but one thing I want to make sure is in there is a big cock pounding a tight ass.'"
    mc "'And please use the red wig again.'"
    scene sm1ms021-45 the_next_concept_sy_talk_smiling with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "Good thing we've got the tight ass and big cock covered."
    scene sm1ms021-46 the_next_concept_mc_talk with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Now we just need lube."
    scene sm1ms021-47 the_next_concept_sy_talk with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "Mmhmm."
    play sound sfx_keyboard_typing1
    scene sm1ms021-48 the_next_concept_mc_talk_armscrossed with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Well, I am glad they want to hire us again."
    mc "They gave us instructions but still left us plenty of room to work with."
    scene sm1ms021-49 the_next_concept_sy_talk with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "Yeah, they're a great client. Seems like they really like redheads, too."
    scene sm1ms021-50 the_next_concept_mc_talk_grinning with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "They're not the only one."
    scene sm1ms021-51 the_next_concept_sy_talk with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "Haha."
    scene sm1ms021-52 the_next_concept_sy_talk_frown with dissolve
    play voice3 stacy_disappointed_ehh2 noloop
    sy "Shame we don't really know who they are."
    sy "When we're rich and famous, it would be great to meet them."
    scene sm1ms021-53 the_next_concept_sy_talk_normal with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "We could throw a big party here. Our first client deserves the best."
    scene sm1ms021-54 the_next_concept_mc_talk with dissolve
    play voice2 mc_thinking_hm noloop
    mc "A little mystery makes it fun. Besides, it's not like everyone talks about porn and the adult film industry as easily as we do."
    scene sm1ms021-55 the_next_concept_sy_talk_hardwork with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah, I guess so."
    sy "I guess so long as the check clears, I’m not complaining."
    sy "And now that we’ve got the extra power and space in the studio, this film is going to be even better than the first one."
    play sound sfx_cloth_rustling2
    scene sm1ms021-57 the_next_concept_mc_talk_chinlookup with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "She’s got a point. This is the kind of project that could put us on the map if we nail it."
    play sound sfx_hands_clap3
    scene sm1ms021-56 the_next_concept_mc_talk_clap with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Alright, let’s start brainstorming then."
    scene sm1ms021-59 the_next_concept_mc_talk with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "I wonder if we can hang a chain line from the ceiling."
    scene sm1ms021-58 the_next_concept_sy_talk_handup with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "Hold on there, Spielberg. We can’t just jump in without a solid plan and, more importantly, without money."
    scene sm1ms021-61 the_next_concept_mc_talk_faking with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Right. The eternal obstacle. How much are we talking for this one?"
    scene sm1ms021-60 the_next_concept_sy_talk with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "I did the math. Hiring Kanya for her time, ordering some special toys, and then with the odds and ends as usual..."
    sy "We're looking at around $200."
    scene sm1ms021-61 the_next_concept_mc_talk_faking with dissolve
    play voice2 mc_pain_auh1 noloop volume 1.2
    mc "Yeouch! Straight to the wallet!"
    scene sm1ms021-62 the_next_concept_sy_talk_giggles with dissolve
    play voice3 stacy_laugh4 noloop
    sy "*giggles*"
    sy "Come on, you know it's worth it to make another impression on this client."
    sy "Plus, I'm sure we'll start making back some of the costs on the first film down the line."
    scene sm1ms021-63 the_next_concept_mc_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, that would be nice."
    scene sm1ms021-64 the_next_concept_mc_talk_begrudge with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "But in the meantime, it sounds like I'm going to spend some more time doing my other jobs."
    play sound sfx_cloth_rustling3
    scene sm1ms021-65 the_next_concept_sy_talk_toucharm with dissolve
    play voice3 stacy_arrogant_hmm2 noloop
    sy "Winner winner, chicken dinner."
    sy "It's all going to be worth it, [mcname]."
    scene sm1ms021-66 the_next_concept_mc_talk with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I know, but now that we've started doing the porn, everything else doesn't quite have the same luster."
    scene sm1ms021-67 the_next_concept_sy_talk with dissolve
    play voice3 stacy_no_nah4 noloop
    sy "I doubt that. You always bring a certain shine to everything you do."
    scene sm1ms021-68 the_next_concept_mc_talk with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "Haha. I guess you're right about that."
    play sound sfx_chair_slide1
    scene sm1ms021-69 the_next_concept_sy_stroke_chin with dissolve
    pause
    scene sm1ms021-70 the_next_concept_sy_kiss with dissolve
    play voice3 stacy_suckmoan1 noloop
    play voice2 mc_thinking_mmm2 noloop
    play sound dahlia_kiss_french1
    sy "Mmmm."
    scene sm1ms021-71 the_next_concept_sy_kiss with dissolve
    play sound mc_kiss2
    pause
    play sound sfx_cloth_rustling1
    scene sm1ms021-72 the_next_concept_mc_talk_pumped with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Alright, let’s map this out. First, we secure the funding. Then, we finalize the concept for the scene."
    mc "Then we'll be set."
    scene sm1ms021-73 the_next_concept_sy_talk with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Almost. I think I'll need some help with the post-production."
    scene sm1ms021-74 the_next_concept_mc_talk_confused with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "There is post-production now?"
    mc "What a time to be alive."
    scene sm1ms021-75 the_next_concept_sy_talk_laugh with dissolve
    play voice3 stacy_laugh noloop
    sy "Haha. There was post-production the first time, but I did it on my own."
    sy "This time, you're tagging in, buster."
    play sound sfx_hair_scratch1 volume 1.4
    scene sm1ms021-76 the_next_concept_mc_talk_doh with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Doh!"
    scene sm1ms021-77 the_next_concept_mc_talk_readytowork with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Still, the first thing we need is money."
    mc "Right?"
    scene sm1ms021-78 the_next_concept_sy_talk with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "Right."
    scene sm1ms021-79 the_next_concept_mc_talk with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Then it's money I'll get. And when I'm through, S&M will have its second film ready to fire people up across the whole city."
    play sound sfx_cloth_planket2
    scene sm1ms021-80 the_next_concept_mc_talk_pose with dissolve
    play voice2 mc_happy_wooh3 noloop
    mc "Let’s do this. For the studio and for the dream."
    scene sm1ms021-81 the_next_concept_sy_talk_joining with dissolve
    play voice3 stacy_happy_wooh1 noloop
    sy "For the dream! Hehehe!"
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1ms021_end_scene
label sm1ms021_end_scene:
    $ StoryController.end_scene(MS, 1, 0, 0)
    return