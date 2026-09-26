label sm1cs_ns010:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.7, 3.0, "music2" )
    play music2 [music_starducks1_radio, music_starducks1_radio, music_starducks2_reverbed, music_starducks2_reverbed]
    play sound sfx_door_open2
    play sound2 sfx_heels_steps2 fadein 1.0
    scene sm1cs-ns010-01 mc-sy-entry1_c1 with dissolve
    queue sound sfx_heels_steps1 loop
    pause
    play sound3 sfx_door_closed2 noloop
    scene sm1cs-ns010-02 mc-sy-entry2_c2 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "I'll grab a table. You grab us some drinks."
    play voice2 mc_yes_yeah2 noloop
    mc "Right."
    scene sm1cs-ns010-03 mc-sy-walk1_c2 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Triple shot expresso right?"
    scene sm1cs-ns010-03 mc-sy-walk1_c1 with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Bingo."
    stop sound2 fadeout 3.0
    stop sound fadeout 1.0
    if LocationController.get_map_location(STARDUCKS).get_location().get_discovered_status() is False:
        call sm1cs_cs001 from _call_sm1cs_cs001_3
    else:
        scene sm1cs-ns010-06 mc-sy-talk_c1 with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "One vento light roast and one dark roast, please."
        scene sm1cs-ns010-06 mc-sy-talk_c2 with dissolve
        play voice3 girl37_yes_yep noloop
        cs "Sure."
        play sound sfx_paper_slide1
        scene sm1cs-ns010-07 mc-sy-cash_c2 with dissolve
        pause
        play sound sfx_coffee_machine
        scene sm1cs-ns010-08 mc-sy-coffee_c1 with dissolve
        pause
        play sound2 sfx_coffee_pouring noloop volume 2.5
        stop sound fadeout 3.0
        scene sm1cs-ns010-08 mc-sy-coffee_c2 with dissolve
        pause
        play sound sfx_cloth_rustling1
        scene sm1cs-ns010-09 mc-sy-coffee2_c1 with dissolve
        play voice2 mc_yes_aga1 noloop
        mc "Thanks."
        scene sm1cs-ns010-09 mc-sy-coffee2_c2 with dissolve
        play voice3 girl37_thinking_hmm1 noloop
        cs "{i}Glad{/i} to serve."
    play sound sfx_heels_steps2 loop
    scene sm1cs-ns010-10 mc-sy-walk_c1 with dissolve
    pause
    scene sm1cs-ns010-10 mc-sy-walk_c2 with dissolve
    pause
    play sound sfx_cloth_rustling4
    scene sm1cs-ns010-11 mc-sy-sniffs_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "Mmmm. Smells perfect."
    play sound sfx_paper_rustl3 volume 0.6
    scene sm1cs-ns010-12 mc-sy-look_c1 with dissolve
    play voice3 stacy_thinking_oh2 noloop
    if player.has_played_scene("sm1ms015"):
        sy "Oh there she is."
    else:
        sy "Oh, is that her?"
    play sound2 sfx_heels_steps1
    scene sm1cs-ns010-12 mc-sy-look_c2 with dissolve
    pause
    if player.has_played_scene("sm1ms015"):
        stop sound2 fadeout 1.0
        scene sm1cs-ns010-13 mc-sy-look2_c1 with dissolve
        play voice2 mc_arrogant_heh1 noloop
        mc "Perfect. Right on time as usual."
        play voice3 stacy_disappointed_oh1 noloop
        sy "You weren't kidding. Super cute."
        mc "Oh yeah."
    else:
        play voice2 mc_yes_yes2 noloop
        mc "Yes. That's Nari."
    stop sound2 fadeout 1.0
    scene sm1cs-ns010-13 mc-sy-look2_c2 with dissolve
    play voice4 nari_happy_laugh1 noloop
    pause
    play sound sfx_drink_slurp2
    scene sm1cs-ns010-14 mc-sy-look3_c1 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "What did you tell her in the message?"
    play voice2 mc_thinking_mmm4 noloop
    mc "Just that I know someone who might be able to help her out with her home situation."
    scene sm1cs-ns010-14 mc-sy-look3_c2 with dissolve
    pause
    scene sm1cs-ns010-15 mc-sy-look4_c1 with dissolve
    play voice2 mc_hey_hey9 noloop
    if player.has_played_scene("sm1ms015"):
        mc "Remember. We're not trying to recruit her today."
    else:
        mc "Remember. This is just a meet and invite. Not a meet and recruit."
    scene sm1cs-ns010-15 mc-sy-look4_c2 with dissolve
    play voice3 stacy_yes_fine1 noloop
    sy "Of course. Unless it comes up organically."
    play sound sfx_cloth_rustling1
    scene sm1cs-ns010-15 mc-sy-look4_c3 with dissolve
    pause
    scene sm1cs-ns010-16 mc-sy-talk_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "How would {i}that{/i} come up organically?"
    mc "No. Not even if the topic of us running a porn studio comes up organically."
    mc "You just steer the bus away from that road."
    scene sm1cs-ns010-16 mc-sy-talk_c2 with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "Okay okay."
    play sound sfx_heels_steps1
    scene sm1cs-ns010-17 mc-sy-talk2_c3 with dissolve
    stop sound fadeout 2.0
    play voice4 nari_hey_asking noloop
    if player.has_played_scene("sm1ms015"):
        ns "Hello, [mcname]. Stacy."
    else:
        ns "Hello, [mcname]."
        play sound sfx_bed_slide2 volume 0.5
        scene sm1cs-ns010-18 mc-sy-talk3_c1 with dissolve
        play voice2 mc_hey_hey10 noloop
        mc "Hey, Nari. How are you doing?"
        scene sm1cs-ns010-18 mc-sy-talk3_c2 with dissolve
        play voice4 nari_yes_aga2 noloop
        ns "Good. Very good."
        ns "Super."
        scene sm1cs-ns010-18 mc-sy-talk3_c1 with dissolve
        play voice2 mc_arrogant_heh3 noloop
        mc "Great."
        if persistent.is_special:
            mc "This is my sister, Stacy."
            scene sm1cs-ns010-19 mc-sy-talk4_c1 with dissolve
            play voice3 stacy_hey_happy2 noloop
            sy "Nice to meet you."
            scene sm1cs-ns010-19 mc-sy-talk4_c2 with dissolve
            play voice4 nari_yes_questioning noloop
            ns "Yes. Sister. Stacy."
            ns "I'm Nari. Nari Song."
            scene sm1cs-ns010-20 mc-sy-talk5_c2 with dissolve
            play voice4 nari_disappointed_mff noloop
            ns "So nice to meet you."
            play sound sfx_cloth_rustling4
            scene sm1cs-ns010-21 mc-sy-talk6_c1 with dissolve
            play voice3 stacy_yes_yeah2 noloop
            sy "Yeah. Uh... good to be met."
        else:
            mc "And this is my good friend, Stacy."
            scene sm1cs-ns010-19 mc-sy-talk4_c1 with dissolve
            play voice3 stacy_hey_happy2 noloop
            sy "Hi there. Nice to meet you."
            scene sm1cs-ns010-19 mc-sy-talk4_c2 with dissolve
            play voice4 nari_yes_yep noloop
            ns "Thank you. My name is Nari Song."
            play sound sfx_cloth_rustling4
            scene sm1cs-ns010-21 mc-sy-talk6_c1 with dissolve
            play voice3 stacy_yes_yeah2 noloop
            sy "Of course. [mcname] has told me lots about you."
            scene sm1cs-ns010-20 mc-sy-talk5_c2 with dissolve
            play voice4 nari_disappointed_mff noloop
            ns "Mmhmm."
    scene sm1cs-ns010-21 mc-sy-talk6_c2 with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Uh Nari, would you like to sit?"
    play voice4 nari_yes_confident noloop
    ns "Yes."
    scene sm1cs-ns010-22 mc-sy-talk7_c2 with dissolve
    play voice4 nari_thinking_oh noloop
    ns "Oh."
    scene sm1cs-ns010-24-2 mc-sy-talk2_c1 with dissolve
    play voice3 stacy_laugh4 noloop
    sy "You can relax, Nari. I don't bite."
    play sound sfx_cloth_rustling5
    scene sm1cs-ns010-24-2 mc-sy-talk2_c2 with dissolve
    play voice4 nari_happy_laugh3 noloop
    ns "*chuckles softly* That's good."
    scene sm1cs-ns010-23 mc-sy-sit_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "So like I mentioned, I know someone who might have a place for you."
    scene sm1cs-ns010-23 mc-sy-sit_c2 with dissolve
    play voice4 nari_yes_yeah noloop
    ns "Yes."
    scene sm1cs-ns010-24 mc-sy-point_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.8
    mc "Uh. Well, it's actually Stacy and I. We're renting a warehouse not far from here."
    mc "Nice, very uh... spacious. And we have space for you, if you're still looking for a place to live."
    scene sm1cs-ns010-24 mc-sy-point_c2 with dissolve
    play voice4 nari_surprised_huh1 noloop
    ns "[mcname], you told {i}her{/i} that I'm... having some trouble?"
    scene sm1cs-ns010-26 mc-sy-look2_c1 with dissolve
    play voice2 d3s7_mcemm noloop volume 1.7
    mc "Uhhh."
    scene sm1cs-ns010-25 mc-sy-look_c2 with dissolve
    play voice4 nari_hey_high noloop
    ns "That was... my private business."
    play voice2 mc_angry_errr5 noloop
    mct "Shit. She's right."
    scene sm1cs-ns010-24-6 mc-sy-talk6_c1 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Well I... I'm sorry, Nari. You're right. I should have asked you first about sharing that information."
    play voice3 stacy_hmm noloop volume 1.4
    sy "[mcname] meant well, Nari."
    sy "He likes you and he just wants to help."
    scene sm1cs-ns010-24-4 mc-sy-talk4_c2 with dissolve
    pause
    play voice4 nari_happy_relief noloop
    ns "*sighs* That is kind but... well back home, this is just not something we talk about so..."
    ns "Honestly."
    scene sm1cs-ns010-24-1 mc-sy-talk_c2 with dissolve
    play voice4 nari_thinking_hmm3 noloop
    ns "But, I am not back home."
    ns "Could you please tell me more about this place you're offering."
    ns "I should really stop risking the loss of my job. At least, not anymore than I already have."
    ns "And it's been nearly impossible to look for a place while I try to keep up my performance at work."
    scene sm1cs-ns010-37 mc-sy-look_c1 with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.5
    mc "Well then, let me go over what the place would be like."
    mc "You'd have your own bedroom, we all share a kitchen and everyone pulls their weight when it's time to clean up."
    play sound sfx_cloth_rustling1 volume 0.6
    scene sm1cs-ns010-37 mc-sy-look_c2 with dissolve
    play voice4 nari_happy_phew noloop
    ns "That should not be a problem. I have never purchased any weights."
    ns "I just prefer to go for a run or a good climb to stay fit."
    scene sm1cs-ns010-38 mc-sy-ask_c1 with dissolve
    play voice2 mc_happy_a1 noloop volume 1.4
    mc "Perfect."
    scene sm1cs-ns010-38 mc-sy-ask_c2 with dissolve
    play voice4 nari_disappointed_huh noloop
    ns "Well it sounds like a nice step up from sleeping on the Orbix office couch."
    ns "But I'm guessing you wanted to ask me some questions before inviting me over."
    scene sm1cs-ns010-36 mc-sy-ask_c2 with dissolve
    play voice4 nari_thinking_hmm1 noloop
    ns "What would you like to know, Miss Stacy?"
    scene sm1cs-ns010-37 mc-sy-look_c1 with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "Just Stacy is fine. Uh... let me think."
    sy "Hmmm."
    scene sm1cs-ns010-36 mc-sy-ask_c1 with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Oh I know. [mcname] tells me that you're really smart at computers and stocks."
    sy "Is there anything I should invest in?"
    play sound sfx_drink_slurp3
    scene sm1cs-ns010-24-3 mc-sy-talk3_c2 with dissolve
    ns "*sips*"
    scene sm1cs-ns010-24-4 mc-sy-talk4_c2 with dissolve
    play voice4 nari_arrogant_hm noloop
    ns "I imagine that you are a first time investor."
    scene sm1cs-ns010-24-5 mc-sy-talk5_c1 with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "Haha. Yes. What gave it away?"
    scene sm1cs-ns010-24-5 mc-sy-talk5_c2 with dissolve
    play voice4 nari_disappointed_eh  noloop
    ns "Experienced investors like to talk about what they're into now. At least, that's been my experience with Americans."
    ns "Many enjoy bragging that they're in futures, or that they've found an emergent pharmaceutical company that will make them a billionaire."
    scene sm1cs-ns010-24-1 mc-sy-talk_c2 with dissolve
    play voice4 nari_thinking_hm noloop
    ns "Given that this would be your first time, I'd recommend a six month CD. Good return. Safe and stable."
    play voice3 stacy_no_angry1 noloop
    play sound sfx_door_slam2
    scene sm1cs-ns010-24-1 mc-sy-talk_c1 with vpunch
    sy "Safe and stable doesn't sound nearly adventurous enough to me."
    scene sm1cs-ns010-24-6 mc-sy-talk6_c2 with dissolve
    play voice4 nari_happy_mmm noloop
    ns "Mmm. You're right, it wouldn't be adventurous."
    ns "But maybe since we'll be sharing a roof, I can come back to you with something more suited to your style."
    ns "Once I get to know you better."
    scene sm1cs-ns010-25 mc-sy-look_c1 with dissolve
    play voice3 stacy_yes_fine3 noloop
    sy "Okay, that was a regular question. Now for something a little harder."
    play voice4 nari_arrogant_yeah noloop
    ns "I'm ready."
    play sound sfx_drink_slurp2 volume 0.6
    scene sm1cs-ns010-30 mc-sy-coffee_c1 with dissolve
    play voice3 stacy_huh2 noloop
    sy "Are you okay seeing naked people from time to time?"
    scene sm1cs-ns010-29 mc-sy-talk3_c2 with dissolve
    play voice4 nari_surprised_what noloop
    ns "What?"
    scene sm1cs-ns010-54 mc-sy-look_c1 with dissolve
    play voice2 mc_angry_hm2 noloop volume 1.3
    mc "*whispers* What are you doing?"
    scene sm1cs-ns010-54 mc-sy-look_c2 with dissolve
    play voice3 amrose_old_psst2 noloop
    sy "*whispers* Relax, I just want to see if she scares easily."
    play sound sfx_hair_scratch1
    scene sm1cs-ns010-56 mc-sy-talk2_c2 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Ahem. It's just, I'm kind of free-spirited and sometimes I like to prance around in my birthday suit."
    sy "So I figured I should check and make sure you're cool with that before you come live with us."
    scene sm1cs-ns010-44 mc-sy-talk5_c2 with dissolve
    play voice4 nari_yes_emotional noloop
    ns "It's a strange question, but as they say."
    ns "Your house, your rules."
    scene sm1cs-ns010-32 mc-sy-talk_c1 with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "Great. It probably won't happen. Much."
    scene sm1cs-ns010-32 mc-sy-talk_c2 with dissolve
    play voice4 nari_happy_laugh6 noloop
    ns "*giggles* Well, just in case [mcname] hasn't told you."
    ns "I'm not a super shy person."
    play sound sfx_drink_loop1
    scene sm1cs-ns010-33 mc-sy-talk2_c1 with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Oooohah."
    scene sm1cs-ns010-33 mc-sy-talk2_c2 with dissolve
    play voice4 nari_thinking_hmm2 noloop
    ns "And the only problems you might have from me is sometimes I like to take long showers."
    ns "But beyond that, I've never had any complaints."
    ns "Of course, my only other roommates were family, hehe."
    stop sound fadeout 1.0
    scene sm1cs-ns010-34 mc-sy-talk3_c1 with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "*giggles*"
    play sound sfx_bed_slide2
    scene sm1cs-ns010-45 mc-sy-stand_c1 with dissolve
    play voice3 stacy_hey_happy1 noloop
    sy "Well I am sold, Nari. I think we have a deal."
    scene sm1cs-ns010-45 mc-sy-stand_c2 with dissolve
    play voice4 nari_disappointed_woof noloop
    ns "Oh."
    play sound sfx_bed_slide3 volume 0.5
    scene sm1cs-ns010-46 mc-sy-stand2_c2 with dissolve
    play voice4 nari_disappointed_eeh noloop
    ns "So that means I can come live with you two? That won't be... too much of a burden?"
    scene sm1cs-ns010-46 mc-sy-stand2_c1 with dissolve
    play voice3 stacy_no_sad1 noloop
    sy "No way. Like you said, it will give you time to pick my brain."
    sy "And maybe [mcname] and I can pick yours back."
    play sound sfx_hands_clap2
    scene sm1cs-ns010-47 mc-sy-handshake_c1 with dissolve
    pause
    play sound sfx_cloth_rustling4
    scene sm1cs-ns010-48 mc-sy-sit_c2 with dissolve
    play voice4 nari_happy_yay noloop
    ns "I guess we'll just have to see."
    scene sm1cs-ns010-49 mc-sy-sit2_c2 with dissolve
    play voice4 nari_happy_relief noloop
    ns "But I am grateful to both of you for even the consideration."
    ns "Having a new place to live would help me out a lot, both for work and..."
    ns "Other issues."
    play sound sfx_drink_loop1 volume 2.0
    scene sm1cs-ns010-51 mc-sy-talk_c2 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    if player.get_choice("sm1ms_renovation_completed"):
        sy "Now it will take a little bit of time to get your room ready. We just finished renovating the place, but I'd like to get your room nice and tidy before you move in."
        scene sm1cs-ns010-52 mc-sy-talk2_c1 with dissolve
        play voice4 nari_yes_aga2 noloop
        ns "Thank you. I'm sure I can manage until then."
    elif player.get_choice("sm1ms_renovation_started"):
        sy "Now it will take a little bit of time to get your room ready. We started renovating the place, but there is still a lot of work to do."
        scene sm1cs-ns010-52 mc-sy-talk2_c1 with dissolve
        play voice4 nari_yes_aga2 noloop
        ns "Thank you. I'm sure I can manage until then."
        ns "I'd also love to help you guys fix up the place."
        scene sm1cs-ns010-52 mc-sy-talk2_c2 with dissolve
        play voice2 mc_happy_yay2 noloop
        mc "Sounds great, Nari."
    else:
        sy "It will take us a bit of time to get the place fixed up. But as soon as it is, [mcname] will tell you at work and we can get you moved in."
        scene sm1cs-ns010-52 mc-sy-talk2_c1 with dissolve
        play voice4 nari_yes_aga2 noloop
        ns "Thank you. I'm sure I can manage until then."
        ns "I'd also love to help you guys fix up the place."
        scene sm1cs-ns010-52 mc-sy-talk2_c2 with dissolve
        play voice2 mc_happy_yay2 noloop
        mc "Sounds great, Nari."
    scene sm1cs-ns010-53 mc-sy-talk3_c1 with dissolve
    play voice4 nari_thinking_hmm3 noloop
    ns "And it will give me time to come up with a proper gift to thank you two for your hospitality."
    ns "Don't worry, it will be beyond the rent that I pay you."
    play sound sfx_hair_scratch1
    scene sm1cs-ns010-56 mc-sy-talk2_c2 with dissolve
    play voice2 mc_no_nah1 noloop
    mc "You don't have to worry about a gift, or rent, Nari. We're happy to help you out as long as you need."
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah. Besides, making the rent on the place is [mcname]'s job."
    scene sm1cs-ns010-55 mc-sy-talk_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Lucky me."
    scene sm1cs-ns010-55 mc-sy-talk_c3 with dissolve
    play voice4 nari_no_angry noloop
    ns "No, that is unacceptable."
    ns "I cannot accept such a gift and give nothing back in return. I don't know what the right gift will be, but I am confident I will find something worthy of what you two are giving me."
    scene sm1cs-ns010-56 mc-sy-talk2_c2 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Uh, sure."
    play voice3 stacy_thinking_hm1 noloop
    sy "Whatever you want to give us will be great. But there is no rush."
    scene sm1cs-ns010-57 mc-sy-look_c1 with dissolve
    play voice4 nari_yes_sad noloop
    ns "Of course."
    play sound sfx_bed_slide2
    scene sm1cs-ns010-58 mc-sy-stand_c1 with dissolve
    play voice4 nari_happy_laugh1 noloop
    ns "Well, I've taken up enough of your time with my troubles. I should get back to work."
    scene sm1cs-ns010-59 mc-sy-stand2_c1 with dissolve
    play voice3 nari_sex_closedmoan1 noloop
    ns "I will always be grateful for this."
    play sound sfx_heels_steps1 loop
    scene sm1cs-ns010-60 mc-sy-look_c1 with dissolve
    pause
    play sound sfx_door_openclosed2
    scene sm1cs-ns010-61 mc-sy-talk_c2 with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "Well she is cute, kind and definitely a little weird."
    sy "But I like weird."
    scene sm1cs-ns010-61 mc-sy-talk_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. Me too."
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    stop music2 fadeout 3.0
    $ StoryController.end_scene(NS_STORY, 3, 0, 2, STARDUCKS, DEFAULT_SUBLOCATION, LSC_ENTRANCE)
    return