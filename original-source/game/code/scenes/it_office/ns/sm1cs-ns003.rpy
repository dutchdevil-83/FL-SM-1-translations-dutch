label sm1cs_ns003:
    $ renpy.music.set_volume(0.45, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1cs-ns003-00 office_mc_talk_stretching_out with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "Phew."
    scene sm1cs-ns003-01 office_mc_thought_look_ns with dissolve
    mct "Nari has been usually quiet today"
    scene sm1cs-ns003-02 office_mc_stand with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Everything good, Nari?"
    scene sm1cs-ns003-03 office_ns_talk_panic with dissolve
    play music music_silly_sunshine
    play voice3 nari_yes_emotional noloop
    ns "Yes."
    scene sm1cs-ns003-04 office_ns_talk_calm with dissolve
    play voice3 nari_disappointed_eh noloop
    ns "I mean \"yes\". I... uh."
    scene sm1cs-ns003-05 office_mc_talk_calm with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Just relax. It's just me."
    scene sm1cs-ns003-06 office_ns_talk_shame with dissolve
    play voice3 nari_disappointed_eeh noloop
    ns "I know. I... I've been meaning to talk to you about something."
    scene sm1cs-ns003-07 office_ns_talk_awkward with dissolve
    play voice3 nari_happy_mmm noloop
    ns "You've been so nice to me."
    ns "I fear I've been acting awkward since- Well, since that time in the bathroom."
    scene sm1cs-ns003-08 office_mc_talk_awkward with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, you've been fine."
    scene sm1cs-ns003-09 office_mc_thinking_ns_deep breadth with dissolve
    play voice2 d1s1_mmm noloop
    mct "She can be so damn cute when she's embarrassed. Still shy, but there is something else there."
    mct "Like she's playing a game with me. Only she knows the moves"
    scene sm1cs-ns003-10 office_mc_thinking_ns_relieved with dissolve
    play voice3 nari_happy_relief noloop
    ns "You have no idea how glad that makes me feel. Thank you, [mcname]."
    ns "When I got back to my desk, it felt like every minute, I wanted to shrivel up and hide. It would get worse when Anna or Clare got close to me."
    scene sm1cs-ns003-11 office_mc_talk_ns_tilt with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "I think you're being hard on yourself. If I didn't know, I wouldn't have had a clue. You handled it like a pro."
    scene sm1cs-ns003-12 office_ns_talk_ns_tilt with dissolve
    play voice3 nari_thinking_mff noloop
    ns "I know you are just saying that, but I still appreciate it."
    scene sm1cs-ns003-13 office_ns_talk_ns_pull_on_finger with dissolve
    ns "*whisper* Sometimes it can feel so hard to remain disciplined. I don't know if it's stress from work or if it's just my way."
    scene sm1cs-ns003-14 office_ns_talk_ns_look_mc with dissolve
    play voice3 nari_surprised_ehh noloop
    ns "Do you think I'm too perverted?"
    scene sm1cs-ns003-15 office_mc_talk_neutral with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Remember we weren't going to talk about that kind of stuff at work, Nari."
    scene sm1cs-ns003-16 office_ns_talk_brightening_up with dissolve
    play voice3 nari_happy_yeah noloop
    ns "Right! But we can talk about it somewhere else. Come on, [mcname]."
    scene sm1cs-ns003-17 office_mc_talk_grab_arm with dissolve
    play voice2 d1s2_hmm noloop volume 1.8
    mc "Where are you taking me?"
    scene sm1cs-ns003-18 office_ns_talk_finger_lips with dissolve
    play voice3 nari_disappointed_oh noloop
    ns "It's' a secret. But... well not a total secret. I wanted to get you something for your help."
    scene sm1cs-ns003-19 office_mc_talk_finger_lips with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "You don't need to get me anything, Nari."
    play sound sfx_chair_slide1 volume 1.6
    scene sm1cs-ns003-20 office_mc_thought_ns_pulling with dissolve
    mct "Shit did I leave my computer on?"
    scene sm1cs-ns003-21 office_mc_talk_ns_pulling with dissolve
    play voice2 d2s12_emmm noloop
    mc "We have to go right now?"
    scene sm1cs-ns003-22 office_ns_talk_ns_pulling with dissolve
    play voice3 nari_yes_confident noloop
    ns "Yes."
    scene sm1cs-ns003-23 office_mc_talk_ns_pulling with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Where are you taking me?"
    ns "You'll see."
    stop sound2 fadeout 2.0
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound3 sfx_parkday_birds fadein 2.0
    scene sm1cs-ns003-24 outside_mc_thoughtce_cream with Fade(0.5, 0.5, 0.5)
    mct "It turns out that her sneaky plan was to buy me a perfect ice cream to relax after a long day of work."
    if player.get_choice("NS002-took-panty"):
        scene sm1cs-ns003-25 outside_ns_talkce_cream with dissolve
        ns "By the way, when I went back to find my panties in the bathroom, they were missing."
        mct "Uh oh."
        ns "You wouldn't happen to know anything about that, would you?"
        scene sm1cs-ns003-26 outside_mc_talkce_cream with dissolve
        mc "Oh. Uh... I bet the janitor just found em and put them in the trash."
        scene sm1cs-ns003-29 outside_ns_talk_looking_menu_no_more with dissolve
        ns "*giggles* Yes. I'm sure that's what happened."
    else:
        scene sm1cs-ns003-25 outside_ns_talkce_cream with dissolve
    play voice3 nari_surprised_huh2 noloop
    ns "You never answered my question, [mcname]."
    scene sm1cs-ns003-26 outside_mc_talkce_cream with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What question would that be?"
    scene sm1cs-ns003-27 outside_ns_talkce_cream_embarassed with dissolve
    play voice3 nari_arrogant_huh noloop
    ns "Do you think I'm just a big pervert?"
    scene sm1cs-ns003-28 outside_mc_talk_looking_menu_no_more with dissolve
    menu:
        "No more than me"(hint="sm1cs_ns003_m01_h01"):
            play voice2 mc_happy_yay2 noloop
            mc "If you are a pervert, then so am I."
            scene sm1cs-ns003-29 outside_ns_talk_looking_menu_no_more with dissolve
            play voice3 nari_happy_laugh1 noloop
            ns "Really? You seem so normal."
            scene sm1cs-ns003-30 outside_mc_talk_shrug_menu_no_more with dissolve
            play voice2 mc_angry_hm1 noloop
            mc "What is normal these days? The world is a crazy place. Sometimes-"
            scene sm1cs-ns003-31 outside_mc_talk_grin_menu_no_more with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "-staying sane means you gotta let the naughty thoughts out of the cage."
            scene sm1cs-ns003-32 outside_ns_talk_giggle_menu_no_more with dissolve
            play voice3 nari_happy_laugh2 noloop
            ns "*Giggles* Yes. I know exactly what you mean. But I still probably am a bigger deviant than you."
            scene sm1cs-ns003-33 outside_mc_talk_cocky_menu_no_more with dissolve
            play voice2 d1s5_mchappy noloop volume 1.7
            mc "I don't know. I've seen a lot and done a lot."
            scene sm1cs-ns003-34 outside_ns_talk_relaxed_menu_no_more with dissolve
            play voice3 nari_arrogant_hm noloop
            ns "Hehe. Sounds like a challenge."
            scene sm1cs-ns003-35 outside_mc_talk_relaxed_menu_no_more with dissolve
            play voice2 mc_no_nope2 noloop
            mc "Not at all."
        "We all need to blow off steam now and again"(hint="sm1cs_ns003_m01_h02"):
            call sm1cs_ns003_m01_c02 from _call_sm1cs_ns003_m01_c02
            scene sm1cs-ns003-34 outside_ns_talk_relaxed_menu_no_more with dissolve
            play voice3 nari_happy_laugh1 noloop
            ns "Yes, but normal people can do it without ruining one of their favorite pairs of panties."
            ns "It was silk, and I only have one left."
            scene sm1cs-ns003-32 outside_ns_talk_giggle_menu_no_more with dissolve
            play voice3 nari_thinking_emm noloop
            ns "I mean... It's fine. I'll get better at it. I mean-"
    scene sm1cs-ns003-36 outside_walking_mc_thought with fade
    mct "She can be so shy, and yet so casual about talking about sexy stuff"
    mct "That's hot, but there has to be more to her."
    scene sm1cs-ns003-37 outside_walking_mc_talk with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.8
    mc "Tell me more about yourself, Nari. I should know about all women who like to give me sweets."
    scene sm1cs-ns003-38 outside_walking_ns_talk_smiling with dissolve
    play voice3 nari_thinking_hmm2 noloop
    ns "Well, you know I'm from South Korea. I'm twenty-one."
    scene sm1cs-ns003-39 outside_walking_mc_talk_probe with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "That's the basic stuff. I'm talking about deeper things."
    scene sm1cs-ns003-40 outside_walking_ns_talk_brightens_up with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Oh, like if I like regular anal or anal beads?"
    scene sm1cs-ns003-41 outside_walking_mc_talk_facepalm with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Too deep."
    scene sm1cs-ns003-42 outside_walking_ns_talk_confused with dissolve
    play voice3 nari_arrogant_heh noloop
    ns "I thought we could talk about stuff like that here, [mcname]."
    scene sm1cs-ns003-43 outside_walking_mc_talk_neutral with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I guess you're right. It's not like anyone is listening to us like back at the office."
    mc "But I was thinking more, what do you like to do for fun that isn't sex?"
    scene sm1cs-ns003-44 outside_walking_ns_thinking with dissolve
    play voice3 nari_thinking_hmm1 noloop
    ns "..."
    scene sm1cs-ns003-45 outside_walking_mc_thinking with dissolve
    ns "Hmmm..."
    play voice2 mc_angry_huh2 noloop
    mct "I never imagined it would take this long"
    scene sm1cs-ns003-46 outside_walking_ns_talk_again with dissolve
    play voice3 nari_thinking_hm noloop
    ns "Well, when I'm not at work, I usually just read a few pages from one of my books, or I look up new finance reports."
    ns "Oh! And I watch about ten videos a night about new technologies."
    scene sm1cs-ns003-47 outside_walking_topuc_tech_mc_talk_shocked with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Ten videos a night?"
    scene sm1cs-ns003-48 outside_walking_topic_tech_ns_talk_hesitant with dissolve
    play voice3 nari_yes_questioning noloop
    ns "Is that a lot?"
    scene sm1cs-ns003-49 outside_walking_topic_tech_mc_talk_unsure with dissolve
    play voice2 d2s9_confused noloop volume 1.8
    mc "That's just a lot of technology."
    call sm1cs_ns003_add_topic_technology from _call_sm1cs_ns003_add_topic_technology
    scene sm1cs-ns003-50 outside_walking_topic_tech_mc_talk_awkward with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "I can't even watch more than like twenty minutes of porn at a time, and I love porn.."
    scene sm1cs-ns003-51 outside_walking_topic_tech_mc_talk_look with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Alright, it's your turn."
    scene sm1cs-ns003-52 outside_walking_topic_tech_ns_talk_smile with dissolve
    play voice3 nari_yes_confident noloop
    ns "Yes."
    scene sm1cs-ns003-53 outside_walking_topic_tech_mc_talk_look with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Uh. Nari?"
    scene sm1cs-ns003-54 outside_walking_topic_tech_ns_talk_look with dissolve
    play voice3 nari_yes_yeah noloop
    ns "Yes?"
    scene sm1cs-ns003-55 outside_walking_topic_tech_mc_talk_smile with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I meant like it's your turn to ask me something if you like."
    scene sm1cs-ns003-56 outside_walking_topic_tech_ns_talk_confused with dissolve
    play voice3 nari_disappointed_oh noloop
    ns "Oh! Of course. Yes. Ask you something. Question."
    ns "Personal questions."
    scene sm1cs-ns003-57 outside_walking_topic_tech_mc_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "But not too deep."
    scene sm1cs-ns003-58 outside_walking_topic_tech_ns_talk with dissolve
    play voice3 nari_thinking_hmm3 noloop
    ns "Not too deep."
    ns "So, are you liking uh... do you like working at Orbix?"
    scene sm1cs-ns003-59 outside_walking_topic_tech_mc_talk_neutral with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "It's a job. Good company, though."
    scene sm1cs-ns003-60 outside_walking_topic_tech_ns_talk_neutral with dissolve
    play voice3 nari_yes_yep noloop
    ns "Yes. That's why I've been so excited to be there. There are only a few companies in the state that have so much growth potential."
    ns "Their financial estimates for the next twenty quarters are incredible, even if I think they're inflated by one point three percent."
    scene sm1cs-ns003-61 outside_walking_topic_tech_mc_blank_stare with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure. Totally. And also meant like, good \"company\" as in the people working there."
    scene sm1cs-ns003-62 outside_walking_topic_tech_ns_not_gettingt with dissolve
    play voice3 nari_yes_aga1 noloop
    ns "Mmhmm. And we've both been good workers there. I think your coding has been improving every day since we first talked."
    scene sm1cs-ns003-63 outside_walking_topic_tech_mc_talk_unsure with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "I don't know about that. I'm still no master like you or April."
    scene sm1cs-ns003-64 outside_walking_topic_tech_ns_talk_passion with dissolve
    play voice3 nari_happy_laugh3 noloop
    ns "Oh, definitely not. But you never give up when you run into a problem. That is admirable."
    ns "It's so easy just to accept defeat or run away when you face a big problem."
    ns "Like in the bathroom. Before you came in, it just looked like a no-win scenario. I wanted to break down, to text Claire that I was quitting because I felt like a..."
    scene sm1cs-ns003-65 outside_walking_topic_tech_ns_talk_defeated with dissolve
    play voice3 nari_thinking_mff noloop
    ns "Well, like a failure who didn't deserve to walk the halls of Orbix."
    scene sm1cs-ns003-66 outside_walking_topic_tech_mc_talk_defeated with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I'm glad you didn't text her. And you didn't fail or do anything wrong, Nari."
    mc "I mean, I don't know if masturbation at work is forbidden in the manual or something."
    scene sm1cs-ns003-67 outside_walking_topic_tech_ns_talk with dissolve
    play voice3 nari_disappointed_mff noloop
    ns "It is."
    scene sm1cs-ns003-68 outside_walking_topic_tech_mc_talk_shrug with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Well, to hell with the manual. We work so hard, sometimes we need a little me-time to cool off."
    scene sm1cs-ns003-69 outside_have_snack with fade
    pause
    play sound sfx_paper_bag_1
    scene sm1cs-ns003-70 outside_have_snack_ns_talk_question with dissolve
    stop sound fadeout 4.0
    play voice3 nari_disappointed_eeh noloop
    ns "Uh... [mcname]... Have you ever \"cooled off\" in the office before?"
    scene sm1cs-ns003-71 outside_have_snack_mc_talk_question with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Haha. I don't think I'm brave enough for that."
    scene sm1cs-ns003-72 outside_have_snack_ns_talk_question with dissolve
    play voice3 nari_thinking_emm noloop
    ns "Mhmm. But... what about one day?"
    mct "Is she asking me if I think I'll jack off in the office one day?"
    menu:
        "Maybe"(hint="sm1cs_ns003_m02_h01"):
            call sm1cs_ns003_m02_c01 from _call_sm1cs_ns003_m02_c01
            scene sm1cs-ns003-73 outside_have_snack_menu_mc_talk_grinning with dissolve
            play voice2 d9s2_yeah noloop volume 2.5
            mc "Maybe. I do like getting freaky-deaky from time to time."
            scene sm1cs-ns003-74 outside_have_snack_menu_ns_talk_excited with dissolve
            play voice3 nari_happy_laugh4 noloop
            ns "Hahaha. So maybe I'll come to your rescue next time."
            play voice2 mc_yes_aga1 noloop
            mc "Maybe."
        "I don't think so"(hint="sm1cs_ns003_m02_h02"):
            scene sm1cs-ns003-75 outside_have_snack_menu_mc_talk_concerned with dissolve
            play voice2 mc_arrogant_hm3 noloop
            mc "I think it might be too risky in the office."
            mc "My heart was racing just being around you after-"
            scene sm1cs-ns003-76 outside_have_snack_menu_ns_talk_kinky with dissolve
            play voice3 nari_surprised_huh1 noloop
            ns "After I came so hard, I squirted all over my panties?"
            scene sm1cs-ns003-73 outside_have_snack_menu_mc_talk_grinning with dissolve
            play voice2 d9s2_yeah noloop volume 2.5
            mc "Yup. That's the one."
            scene sm1cs-ns003-74 outside_have_snack_menu_ns_talk_excited with dissolve
            play voice3 nari_happy_laugh4 noloop
            ns "*giggles*"
    scene sm1cs-ns003-77 outside_have_snack_ns_bite_closed_eyes with dissolve
    play voice3 nari_sex_closedmoan3 noloop
    ns "Yummm."
    scene sm1cs-ns003-78 outside_have_snack_mc_talk_notice with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Nari, you have a little something."
    scene sm1cs-ns003-79 outside_have_snack_ns_talk_brushes with dissolve
    play voice3 nari_happy_mmm noloop
    ns "Better?"
    play sound sfx_paper_rustl3
    scene sm1cs-ns003-80 outside_have_snack_mc_talk_napkin with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.4
    mc "Haha. What am I going to do with you?"
    scene sm1cs-ns003-81 outside_have_snack_ns_talk_napkin_clean with dissolve
    play voice3 nari_disappointed_huh noloop
    ns "I... I don't know."
    play sound sfx_paper_slide1 volume 1.6
    scene sm1cs-ns003-82 outside_have_snack_ns_look_at_each_other with dissolve
    pause
    scene sm1cs-ns003-83 outside_have_snack_ns_talk_look_away with dissolve
    play voice3 nari_angry_cough noloop
    ns "*clears throat* I really like it here. The park."
    scene sm1cs-ns003-84 outside_have_snack_ns_look_away with dissolve
    pause
    play sound sfx_cloth_rustling1 volume 1.6
    scene sm1cs-ns003-85 outside_walk_again_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. It sure beats being cooped up in the office. It would be great just working out here on a laptop."
    scene sm1cs-ns003-86 outside_walk_again_ns_talk with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Oh, they couldn't do that. Orbix needs constant security to ensure Trojans and other malware can't penetrate their cybersecurity."
    ns "There isn't a Wi-Fi system available that could keep things as secure out here as compared to a site like the office."
    scene sm1cs-ns003-87 outside_walk_again_mc_talk with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Totally."
    mct "Maybe one day I'll know what half of that means."
    scene sm1cs-ns003-88 outside_walk_again_ns_talk_near_bathroom with dissolve
    play voice3 nari_sex_closedmoan1 noloop
    ns "I need to go inside."
    menu:
        "Tease her"(hint="sm1cs_ns003_m03_h01"):
            call sm1cs_ns003_m03_c01 from _call_sm1cs_ns003_m03_c01
            scene sm1cs-ns003-89 outside_menu_mc_talk_tease with dissolve
            play voice2 mc_happy_hah1 noloop
            mc "You really can't hold off from jilling for more than an hour?"
            scene sm1cs-ns003-90 outside_menu_ns_talk_shocked with dissolve
            play voice3 nari_surprised_what noloop
            ns "Jilling? What. I didn't even bring a toy. I-"
            scene sm1cs-ns003-91 outside_menu_ns_look_moment with dissolve
            pause
            scene sm1cs-ns003-92 outside_menu_mc_look_moment_chuckle with dissolve
            play voice2 d4s4_mclaugh noloop volume 1.8
            mc "*Chuckles*"
            scene sm1cs-ns003-93 outside_menu_ns_talk_frown with dissolve
            play voice3 nari_no_uhuh noloop
            ns "That wasn't funny."
            scene sm1cs-ns003-94 outside_menu_mc_talk with dissolve
            play voice2 mc_scared_oh3 noloop
            mc "Oh come on, it was a little funny."
        "Say nothing"(hint="sm1cs_ns003_m03_h02"):
            pass
    scene sm1cs-ns003-95 outside_ns_goesnside with dissolve
    pause
    play sound sfx_door_openclosed1
    scene sm1cs-ns003-96 outside_mc_buzzzz with dissolve
    pause
    call buzz from _call_buzz_2
    scene sm1cs-ns003-97 outside_mc_look_phone with dissolve
    play sound sfx_message_in1 volume 1.6
    pause
    scene sm1cs-ns003-98 outside_mc_look_phone_confused with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Did she ruin her panties again?"
    play sound sfx_door_open1
    scene sm1cs-ns003-99 inside_mc_talk with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Nari?"
    scene sm1cs-ns003-100 inside_ns_talk with dissolve
    play voice3 nari_yes_aga2 noloop
    ns "In here."
    play sound sfx_door_creak4 volume 1.4
    scene sm1cs-ns003-101 inside_ns_opening_door with dissolve
    play voice3 nari_surprised_wow noloop
    ns "I can't believe it."
    scene sm1cs-ns003-103 inside_ns_talk_excited with dissolve
    play voice3 nari_surprised_ohmy noloop
    ns "I found my first gloryhole. Right here in a park bathroom."
    scene sm1cs-ns003-102 inside_ns_talk_pointing with dissolve
    pause
    menu:
        "Excited"(hint="sm1cs_ns003_m04_h01"):
            call sm1cs_ns003_m04_c01 from _call_sm1cs_ns003_m04_c01
            scene sm1cs-ns003-104 inside_menu_mc_talk_excited with dissolve
            play voice2 mc_surprised_wow2 noloop
            mc "Awesome Nari. I didn't expect to find one here."
        "Bored"(hint="sm1cs_ns003_m04_h02"):
            call sm1cs_ns003_m04_c02 from _call_sm1cs_ns003_m04_c02
            scene sm1cs-ns003-105 inside_menu_mc_talk_bored with dissolve
            play voice2 mc_arrogant_heh2 noloop
            mc "Hah. That's cool, but it's just a gloryhole. I've seen way kinkier shit around the city."
            scene sm1cs-ns003-106 inside_menu_ns_talk_bored with dissolve
            play voice3 nari_yes_sad noloop
            ns "Yes, but I haven't."
        "Confused"(hint="sm1cs_ns003_m04_h03"):
            call sm1cs_ns003_m04_c03 from _call_sm1cs_ns003_m04_c03
            scene sm1cs-ns003-107 inside_menu_mc_talk_confused with dissolve
            play voice2 mc_disappointed_ehh3 noloop
            mc "And why is this exciting?"
            scene sm1cs-ns003-108 inside_menu_ns_talk_confused with dissolve
            play voice3 nari_hey_unsure noloop
            ns "I've never seen one in the wild before, [mcname]. I never found one back home."
            ns "Well, I was never brave enough to even go looking back home."
            scene sm1cs-ns003-109 inside_menu_mc_talk_confused with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "Right. I mean it's kind of cool, in a kinky way."
            scene sm1cs-ns003-110 inside_menu_ns_talk_confused_breathe_deep with dissolve
            play voice3 nari_happy_phew noloop
            ns "*deep breath* Yeah..."
    scene sm1cs-ns003-111 inside_ns_talk_look_close with dissolve
    play voice3 nari_thinking_hmm1 noloop
    ns "It's amazing. One of the first tools for anonymous sex."
    scene sm1cs-ns003-112 inside_ns_talk_horny with dissolve
    play voice3 nari_angry_breathing noloop
    ns "*deep breathing* So... someone would just... stick their thing in there..."
    scene sm1cs-ns003-113 inside_ns_talk_stand_look_mc with dissolve
    play voice3 nari_surprised_ah noloop
    ns "Would yours... fit in there?"
    scene sm1cs-ns003-114 inside_mc_talk_horny with dissolve
    play voice2 d3s7_mcemm noloop volume 1.2
    mc "You want me to see?"
    scene sm1cs-ns003-115 inside_ns_talk_bite_lip with dissolve
    play voice3 nari_sex_closedmoan2 noloop
    ns "Only if you want to. I mean I definitely want to see it. Not like, I need to see yours."
    scene sm1cs-ns003-116 inside_ns_talk_flustered with dissolve
    play voice3 nari_arrogant_fff noloop
    ns "I just mean. Without a dick inside, it's just another hole."
    scene sm1cs-ns003-117 inside_mc_talk_flustered with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "You really do get kinky around bathrooms."
    scene sm1cs-ns003-118 inside_ns_talk_thirsty with dissolve
    play voice3 nari_yes_questioning noloop
    ns "Yes... doing things here... it really gets me excited. I don't know if it's because I like watersports, or if I like watersports because I like doing stuff in bathrooms."
    scene sm1cs-ns003-119 inside_mc_thought_cool with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "Man. Nari is so kinky, and she's into watersports."
    call sm1cs_ns003_discover_watersports from _call_sm1cs_ns003_discover_watersports
    mct "I'll have to let Stacy know she was right. Nari could be a great recruit for the studio"
    scene sm1cs-ns003-120 inside_mc_talk_look_hole with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "I guess I should go over to the other side."
    scene sm1cs-ns003-121 inside_ns_talk_look_hole with dissolve
    play voice3 nari_happy_yeah noloop
    ns "Yes! I mean... yeah. Totally. Whatever."
    scene sm1cs-ns003-122 inside_mc_grinning with dissolve
    play voice2 d3s11b_mcheh noloop
    pause
    play sound sfx_door_closed7
    scene sm1cs-ns003-123 outside_mc_walking with dissolve
    pause
    play sound sfx_door_openclosed1
    scene sm1cs-ns003-124 inside_mc_thought with dissolve
    pause
    play sound sfx_jeans_on1 volume 2.0
    scene sm1cs-ns003-125 inside_mc_talk with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Alright. Let's do this."
    scene sm1cs-ns003-126 inside_ns_talk with dissolve
    play voice3 nari_yes_yep noloop
    ns "Okay."
    scene sm1cs-ns003-127 inside_mc_thoughtn_hole with dissolve
    play voice2 mc_disgust_pfe1 noloop
    mct "This is either my best idea or my worst idea yet"
    scene sm1cs-ns003-128 inside_ns_talk_see_cock with dissolve
    play voice3 nari_scared_ho noloop
    ns "Oh wow. It's really big. I've seen a lot in porn. But this one..."
    scene sm1cs-ns003-129 inside_ns_talk_enamored with dissolve
    play voice3 nari_happy_relief noloop
    ns "I can feel your warmth, [mcname]. It looks so tasty."
    scene sm1cs-ns003-130 inside_mc_talk_smirk with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Just be careful, Nari. This thing has a mind of its own sometimes.."
    scene sm1cs-ns003-131 inside_ns_talk_grinning with dissolve
    play voice3 nari_no_unsure noloop
    ns "I'm not shy."
    play sound sfx_spitcum1
    scene sm1cs-ns003-132 inside_ns_suck_finger with dissolve
    play voice3 nari_sex_closedmoan6 noloop
    ns "Mrmmm."
    queue sound sfx_cloth_rustling1
    scene sm1cs-ns003-133 inside_mc_thought_touch with dissolve
    pause
    play voice2 d1s5_orgasm noloop
    mct "No, you are definitely not shy, Nari. Wow"
    scene sm1cs-ns003-134 inside_mc_ns_horny with dissolve
    play voice2 d1s5_orgasm2 noloop
    mct "She certainly has a perfectly gentle touch. Soft but not so light that you can't feel it"
    scene sm1cs-ns003-135 inside_ns_talk_horny with dissolve
    play voice3 nari_surprised_ehh noloop
    ns "I think I want to. I mean... can I put my-"
    scene sm1cs-ns003-135-1 inside_ed__talk_opens door with dissolve
    play voice4 girl24_arrogant_huh2 noloop
    ed "That was such a good-"
    play sound sfx_locker_open1 volume 2.0
    scene sm1cs-ns003-136 inside_ed__talk_opens door with hpunch
    play voice4 girl24_scared_oof noloop
    ed "Oh my god."
    scene sm1cs-ns003-137 inside_ns_talk_pulls_away with dissolve
    play voice3 nari_hey_asking noloop
    ns "Oh. Hello."
    scene sm1cs-ns003-138 inside_ed_talk_panics with dissolve
    play voice4 girl24_scared_oh1 noloop
    ed "Oh fuck. Sorry sorry sorry. I didn't mean to-"
    play sound sfx_door_closed2
    scene sm1cs-ns003-139 inside_ed_leaves with dissolve
    play voice4 girl24_disappointed_hmf noloop
    pause
    scene sm1cs-ns003-140 inside_mc_talk_panics with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "Nari?"
    scene sm1cs-ns003-141 inside_ns_talk_focus with dissolve
    play voice3 nari_disappointed_eh noloop
    ns "I'm here. We uh... we should probably go."
    play sound sfx_jeans_on1
    scene sm1cs-ns003-142 outside_mc_talk with fade
    play voice2 mc_thinking_hmm4 noloop
    mc "Alright, just act cool."
    scene sm1cs-ns003-143 outside_ns_talk with dissolve
    play voice3 nari_disgust_ergh noloop
    ns "I did not anticipate someone just walking in on me."
    scene sm1cs-ns003-144 outside_walk_mc_talk with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. I hope she's not some Karen and she's going to report us to a park ranger."
    scene sm1cs-ns003-145 outside_walk_ns_talk with dissolve
    play voice3 nari_no_nah noloop
    ns "I don't think this park has rangers. Still, one way or the other, that was... very exciting."
    scene sm1cs-ns003-146 outside_walk_mc_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah."
    scene sm1cs-ns003-147 outside_walk_mc_thought_ns_conflicted with dissolve
    mct "For a second there, I thought Nari was going to start sucking me off through the gloryhole"
    scene sm1cs-ns003-148 outside_walk_ns_talk_check_phone with dissolve
    play voice3 nari_thinking_hmm3 noloop
    ns "It's getting late. I should get home."
    scene sm1cs-ns003-149 outside_walk_mc_talk_neutral with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, me too."
    scene sm1cs-ns003-150 outside_walk_ns_talk_pose with dissolve
    play voice3 nari_happy_phew noloop
    ns "You... I mean I. I had a really good time with you, [mcname]."
    scene sm1cs-ns003-151 outside_walk_mc_talk_pose with dissolve
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "Me too, Nari."
    scene sm1cs-ns003-152 outside_walk_ns_talk_wave with dissolve
    play voice3 nari_yes_aga1 noloop
    ns "I guess I'll see you at work next time. Bye!"
    scene sm1cs-ns003-153 outside_walk_mc_talk_ns_walks_away with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Later."
    scene sm1cs-ns003-154 outside_walk_mc_thought_shrug with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Well, that was quite a ride. I almost thought she might want to hang out"
    mct "Maybe next time"
    stop music fadeout 3.0
    stop sound3 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(NS_STORY, 2, 0, 3, PARK, DEFAULT_SUBLOCATION, LPA_ENTRANCE)
    return
label sm1cs_ns003_m01_c02:
    $ player.set_choice("sm1cs_ns003_blow_off_steam")
    return
label sm1cs_ns003_m02_c01:
    $ player.set_choice("sm1cs_ns003_maybe_jerk_off")
    return
label sm1cs_ns003_m03_c01:
    $ player.set_choice("sm1cs_ns003_tease_her")
    return
label sm1cs_ns003_m04_c01:
    $ player.set_choice("sm1cs_ns003_gloryhole_excited")
    $ CharacterController.get_character("ns").add_point()
    return
label sm1cs_ns003_m04_c02:
    $ player.set_choice("sm1cs_ns003_gloryhole_bored")
    $ CharacterController.get_character("ns").deduct_point()
    return
label sm1cs_ns003_m04_c03:
    $ player.set_choice("sm1cs_ns003_gloryhole_confused")
    return
label sm1cs_ns003_discover_watersports:
    $ CharacterController.get_character("ns").discover_trait(WATERSPORTS)
    return
label sm1cs_ns003_add_topic_technology:
    $ CharacterController.get_character("ns").discover_topic(TOPIC_TECHNOLOGY)
    return
label sm1cs_ns003_unlocks:
    call sm1cs_ns003_m01_c02 from _call_sm1cs_ns003_m01_c02_1
    call sm1cs_ns003_m02_c01 from _call_sm1cs_ns003_m02_c01_1
    call sm1cs_ns003_m03_c01 from _call_sm1cs_ns003_m03_c01_1
    call sm1cs_ns003_m04_c01 from _call_sm1cs_ns003_m04_c01_1
    call sm1cs_ns003_add_topic_technology from _call_sm1cs_ns003_add_topic_technology_1
    call sm1cs_ns003_discover_watersports from _call_sm1cs_ns003_discover_watersports_1
    if config_storyline_mode is True:
        $ execute_storyline_config(NS_STORY)
    return