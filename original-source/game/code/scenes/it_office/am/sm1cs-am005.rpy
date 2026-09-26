image sm1cs-am005-a25-glambot = Movie(play = "images/FS_IT/AM/s005/anim/sm1cs-am005-a25-3x-60fps.webm", start_image = "sm1cs-am005-a25 am-am-softens-up-tries-speak-glambot-000", image = "sm1cs-am005-a25 am-am-softens-up-tries-speak-glambot-199", loop = False)
label sm1cs_am005:
    $ renpy.music.set_volume(0.8, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.5, "sound4" )
    play sound4 sfx_office_ambience1 fadein 2.0
    scene sm1cs-am005-01 mc-work-as-usual_c1 with dissolve
    play music music_digital_lover
    pause
    scene sm1cs-am005-02 mct-am-hasnt-talked-since-watched-band-play_c1 with dissolve
    play voice2 d1s5_mcthinks noloop
    if player.get_choice("sm1cs_am004_no_sex"):
        mct "April hasn't really talked to me since that night I watched her band play."
        scene sm1cs-am005-03 mct-look-down-same-night-not-fuck-her-that-night_c1 with dissolve
        mct "Same night I said I didn't want to fuck her."
        scene sm1cs-am005-04 mct-keeps-thinking-looks-at-ap_c1 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mct "But that night... I mean. It was just chaotic. I never imagined those words would have come out of April's mouth."
        mct "And I didn't want to lie to her."
    else:
        mct "April hasn't really talked to me since we fooled around the night I watched her band play."
        scene sm1cs-am005-05 mct-turned-on-almost-frenzied_c1 with dissolve
        mct "She was like a different person. Almost frenzied."
        scene sm1cs-am005-06 mct-frowning-mct-something-switched_c1 with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mct "Then something switched, and she kicked me out of the car. I thought we were going all the way for sure."
    play sound sfx_bed_slide2 volume 0.6
    scene sm1cs-am005-07 mc-stands-up-resolved_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "This can't go on. I need to at least get us back on some kind of page. We can't work like this."
    scene sm1cs-am005-08 mc-hey-am-am-dont-even-think-about-it_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Hey April."
    play voice3 girl22_angry_argh3 noloop
    am "Don't even think about it."
    scene sm1cs-am005-09 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Push it."(hint="sm1cs_am005_m01_h01"):
            call sm1cs_am005_m01_c01 from _call_sm1cs_am005_m01_c01
            play sound sfx_hair_scratch1
            scene sm1cs-am005-10 choice-push-it-mc-listen-am-bite-me_c1 with dissolve
            play voice2 d2s12_emmm noloop volume 1.4
            mc "Listen April, we should really-"
            play voice3 girl22_angry_geh noloop
            am "Bite me."
            scene sm1cs-am005-11 mct-okay-not-right-time_c1 with dissolve
            play voice2 mc_thinking_mmm3 noloop
            mct "Okay. This is not the right time."
        "Don't push it."(hint="sm1cs_am005_m01_h02"):
            scene sm1cs-am005-12 choice-not-push-mc-walks-away with dissolve
            play voice2 mc_thinking_mmm3 noloop
            mct "Okay. Message received, April."
    jump sm1cs_am005_hours_later
label sm1cs_am005_hours_later:
    $ renpy.music.set_volume(0.0, 2.0, "sound4" )
    scene black
    show screen scene_transistion("Hours later")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 2.0, "sound4" )
    scene sm1cs-am005-13 hours-later-mc-still-works
    with Fade(0.5, 0.5, 0.5)
    play voice2 d7s6_moan2 noloop volume 1.5
    pause
    play sound sfx_keyboard_typing1 volume 1.5
    scene sm1cs-am005-14 mct-finally-last-ticket-day with dissolve
    queue voice2 d1s1_mmm noloop
    mct "Finally. That's the last ticket for my shit."
    play sound sfx_heels_steps1
    scene sm1cs-am005-15 am-leaves-on-phone-mc-hmm with dissolve
    mc "Hmmm."
    play sound sfx_phone_buzz
    scene sm1cs-am005-16 mc-phones-beeps-msg-am with dissolve
    pause
    play sound sfx_message_in1 volume 1.5
    scene sm1cs-am005-17 mc-reads-msg-meet-cw-desk with dissolve
    am "Meet me near Claire's desk."
    play voice2 mc_angry_huh2 noloop
    mct "Why do I feel like she's going to ninja-jump my ass or something?"
    play sound sfx_heels_steps2 loop
    scene sm1cs-am005-18 mc-goes-towards-cw-desk with dissolve
    pause
    $ renpy.music.set_volume(0.8, 2.5, "sound4" )
    scene sm1cs-am005-19 mc-arrives-cw-desk-am-there-now-talk with dissolve
    play voice3 girl22_yes_aga11 noloop
    am "Now I can talk. So talk."
    stop sound fadeout 1.0
    scene sm1cs-am005-20 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Act evasive"(hint="sm1cs_am005_m02_h01"):
            call sm1cs_am005_m02_c01 from _call_sm1cs_am005_m02_c01
            scene sm1cs-am005-21 choice-act-evasive-mc-maybe-not-talk-am-that-lie with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "Maybe I don't want to talk anymore."
            play voice3 girl22_no_nope4 noloop
            am "That's a lie."
            scene sm1cs-am005-22 am-softens-up-lets-reset-mc-will-try with dissolve
            play voice3 girl22_disappointed_ehh2 noloop
            am "I mean. Let's just reset. Can we do that, [mcname]."
            play voice2 mc_yes_okay2 noloop
            mc "I'll try."
        "Push back"(hint="sm1cs_am005_m02_h02"):
            scene sm1cs-am005-23 choice-push-back-mc-been-blown-all-day-am-yes-want-talk with dissolve
            play voice2 mc_surprised_uh3 noloop
            mc "You've been blowing me off all day, and now you want to talk?"
            play voice3 girl22_disappointed_ehh2 noloop
            am "I... yes. I want to talk."
            scene sm1cs-am005-24 am-you-right-ask-start-fresh-mc-okay with dissolve
            play voice3 girl22_disappointed_geh noloop
            am "But you're right, I could have handled things a lot better."
            am "So... can we just open up a new doc, [mcname]? Start fresh?"
            play voice2 mc_yes_okay2 noloop
            mc "Okay."
    scene sm1cs-am005-a25-glambot with Dissolve(0.15)
    pause
    play voice3 girl22_thinking_hmm2 noloop
    am "I..."
    am "..."
    scene sm1cs-am005-26 mc-waiting-something-am-no-dummy with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Are you waiting for something?"
    play voice3 girl22_no_angry noloop
    am "No, you dummy."
    scene sm1cs-am005-27 mc-next-choice-menu-screen with dissolve
    menu:
        "Put an end to things with April"(hint="sm1cs_am005_m03_h01"):
            call sm1cs_am005_m03_c01 from _call_sm1cs_am005_m03_c01
            play sound sfx_heels_steps2 loop
            scene sm1cs-am005-28 choice-end-am-quest-mc-walks-away-done-this-am-whatever with dissolve
            play voice2 mc_arrogant_nah1 noloop
            mc "Alright, I'm done with this."
            play voice3 girl22_arrogant_hm noloop
            am "Yeah, well... Whatever."
            stop sound fadeout 1.0
            jump sm1cs_am005_end
        "Be patient"(hint="sm1cs_am005_m03_h02"):
            pass
    scene sm1cs-am005-29 mc-not-syaing-thinking-should-be-patient-am-why-struggling with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mct "I should be a little patient with her. She's obviously got something on her mind."
    mct "What is it? And why is she struggling so much?"
    scene sm1cs-am005-30 mct-realizing-am-like-him with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Wait. Was there more going on when we were in her car?"
    mct "Does April have-"
    play sound sfx_chair_slide1
    scene sm1cs-am005-31 am-finally-speaks-difficult-say-mc-okay with dissolve
    play voice3 girl22_disappointed_mmf noloop
    am "I know what I want to say, but it's difficult to say it."
    play voice2 d9s2_ugu noloop volume 1.6
    mc "Okay."
    scene sm1cs-am005-32 am-looks-away-sorry-what-happened-car-mc-which-part with dissolve
    play voice3 girl22_surprised_eh1 noloop
    am "I'm sorry for what happened in my car."
    play voice2 mc_arrogant_hm1 noloop
    mc "What part?"
    scene sm1cs-am005-33 am-sarcastic-trunk-what-think-idiot with dissolve
    play voice3 girl22_arrogant_hm noloop
    am "The {i}trunk{/i}."
    scene sm1cs-am005-33 am-sarcastic-trunk-what-think-idiot with hpunch
    am "What do you think, idiot? All of it."
    if player.get_choice("sm1cs_am004_no_sex"):
        jump sm1cs_am005_no_sex_1
    else:
        jump sm1cs_am005_sex_1
label sm1cs_am005_sex_1:
    scene sm1cs-am005-34 am-let-bad-impulse-mc-so-not-about-me with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "I let my bad impulses take over. My brain wasn't thinking straight."
    play voice2 mc_happy_a1 noloop
    mc "Ah. So it wasn't about me. It was just about who was close."
    scene sm1cs-am005-35 am-silence-mc-get-it with dissolve
    am "..."
    play voice2 mc_yes_yeah4 noloop
    mc "I get it."
    scene sm1cs-am005-36 am-locked-hands-mc-talks with dissolve
    play voice3 girl22_disappointed_ehh1 noloop
    pause
    scene sm1cs-am005-37 mc-rubs-neck-say-no-more-gotta-say-was-fun_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Say no more."
    mc "But I gotta say, it was fun."
    scene sm1cs-am005-38 mc-accepts-defeat-maybe-next-life-not-what-mean_c1 with dissolve
    mc "Maybe in the next life."
    play voice3 girl22_no_uhuh1 noloop
    am "That's not what I mean."
    scene sm1cs-am005-39 mct-what-hell-turns-what-mean_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mct "What the hell does that mean?"
    mc "What the hell-"
    scene sm1cs-am005-40 mc-relaxes-care-explain_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Care to explain that, April? As you often say, I'm not as sharp as you."
    scene sm1cs-am005-41 am-when-saw-with-anna-something-bent_c1 with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "When I saw you with Anna, I..."
    am "I don't know, something bent in a direction it's not meant to bend."
    scene sm1cs-am005-42 am-clenches-fists-went-stupid-primal-side_c1 with dissolve
    play voice3 girl22_angry_breathing noloop
    am "And I just, I don't know, I went stupid mode. Basic mode."
    am "But super basic, like primal, animal side. Not the most logical part of me, naturally."
    scene sm1cs-am005-43 mct-pretty-sexy-side-asks-why-pump-breaks_c1 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mct "But a pretty sexy side."
    mc "So why did you pump the brakes?"
    scene sm1cs-am005-44 am-because-tries-speak-mc-signs_c1 with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "Because I..."
    am "..."
    scene sm1cs-am005-45 mc-whatever-text-when-figured-out_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Text me if you ever figure it out. I got other-"
    play sound sfx_cloth_rustling1
    scene sm1cs-am005-46 mc-turns-walk-away-am-grabs-hand-no_c1 with hpunch
    play voice3 girl22_no_simple noloop
    am "No."
    mct "She just grabbed my hand to stop me from leaving."
    scene sm1cs-am005-47 mc-angry-am-sorry_c1 with dissolve
    mc "..."
    play voice3 girl22_disappointed_oh noloop
    am "Sorry. I."
    play sound sfx_heels_steps1 loop
    scene sm1cs-am005-48 cw-approach-am-notices-her-follow-her_c1 with dissolve
    pause
    play voice3 girl22_thinking_eeh noloop
    am "Follow me."
    play sound2 sfx_heels_steps2
    scene sm1cs-am005-49 mc-am-pass-cw-walking-away_c1 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-am005-50 cw-looks-them-smiling_c1 with dissolve
    play voice4 girl29_thinking_hmm5 noloop
    pause
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-am005-51 am-walk-talk-mc-through-office_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.2, 2.5, "sound4" )
    scene sm1cs-am005-52 mc-looking-am-talking-back_c1 with dissolve
    play voice3 girl22_sex_closedmoan3 noloop
    am "*whispers* I didn't want it to be like {i}that{/i}."
    play voice2 mc_surprised_what7 noloop
    mc "What?"
    am "I didn't want our first time to be like that."
    scene sm1cs-am005-53 mc-wait-how-long-am-shh-not-here_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "You didn't want our first time to be like that?"
    mc "Well what was it supposed to be like."
    play sound sfx_door_open2 volume 1.5
    stop sound2 fadeout 1.0
    scene sm1cs-am005-54 mc-am-walk-into-small-office_c1 with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, how long have you been thinking of us do-"
    play voice3 stacy_shhh noloop
    am "Shuuuussssssh. Not here."
    play sound sfx_door_closed2
    scene sm1cs-am005-55 am-mc-in-office-am-dont-know-after-inv-see-band_c1 with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "How long have you been thinking... about this?"
    play voice3 girl22_surprised_eh2 noloop
    am "I don't know. Maybe after I invited you to see my band."
    am "I don't write my thoughts down in a diary or anything. I'm not that girl."
    play sound sfx_skirt_off2
    scene sm1cs-am005-56 mc-comfort-am_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "April, calm down. It's alright. Listen..."
    jump sm1cs_am005_reply_2
label sm1cs_am005_no_sex_1:
    scene sm1cs-am005-57 am-frustrated-let-impulse-brain-wasnt-thinking_c1 with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "I put you in a shit situation, and when you said 'no', I acted like a child."
    am "That's not me. Or... at least I thought I was better than that."
    scene sm1cs-am005-59 mc-gotta-say-was-fun-maybe-next-life_c1 with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "I misread things. I thought you liked me, and I started seeing something between us."
    am "It's really Anna's fault. When I saw her talking to you."
    play sound sfx_heels_steps1 loop
    scene sm1cs-am005-48 cw-approach-am-notices-her-follow-her_c1 with dissolve
    pause
    play voice3 girl22_thinking_eeh noloop
    am "Follow me."
    play sound2 sfx_heels_steps2
    scene sm1cs-am005-49 mc-am-pass-cw-walking-away_c1 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-am005-50 cw-looks-them-smiling_c1 with dissolve
    play voice4 girl29_thinking_hmm5 noloop
    pause
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-am005-51 am-walk-talk-mc-through-office_c1 with dissolve
    pause
    scene sm1cs-am005-52 mc-looking-am-talking-back_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.2, 2.0, "sound4" )
    play sound sfx_door_open2 volume 1.5
    stop sound2 fadeout 1.0
    scene sm1cs-am005-54 mc-am-walk-into-small-office_c1 with dissolve
    pause
    play sound sfx_door_closed2
    scene sm1cs-am005-55 am-mc-in-office-am-dont-know-after-inv-see-band_c1 with dissolve
    am "..."
    play sound sfx_skirt_off2
    scene sm1cs-am005-60 am-cant-look-mc-he-gather-talking-seeing-with-am_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "You were talking about seeing me with Anna."
    scene sm1cs-am005-61 am-sometimes-see-red-so-dragged-myself_c1 with dissolve
    play voice3 girl22_yes_yeah1 noloop
    am "Sometimes I see her, and I just see red, you know?"
    am "So I dragged you to the car and I made an ass out of myself."
    scene sm1cs-am005-62 am-lips-closeup-moment-really-thought-say-yes-mc-choice-menu-screen_c1 with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    am "At that moment, I really thought you'd say 'yes'."
    menu:
        "I thought it was a game"(hint="sm1cs_am005_m04_h01"):
            call sm1cs_am005_m04_c01 from _call_sm1cs_am005_m04_c01
            scene sm1cs-am005-63 choice-thought-was-game-mc-figured-didnt-seem-serious_c1 with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "I figured you were just trying to trick me."
            mc "It didn't feel serious."
            scene sm1cs-am005-64 mc-touches-chest-way-acting_c1 with dissolve
            play voice2 mc_disappointed_ehh2 noloop
            mc "I mean the way you act toward me, I never have more than a faint guess what you're thinking."
            scene sm1cs-am005-65 am-asking-question-mc-dont-know_c1 with dissolve
            play voice3 girl22_thinking_oh noloop
            am "So... if things were different, you would have said 'yes'?"
            play voice3 mc_arrogant_hm3 noloop
            mc "I don't know."
            jump sm1cs_am005_reply_2
        "What do you want from me?"(hint="sm1cs_am005_m04_h02"):
            call sm1cs_am005_m04_c02 from _call_sm1cs_am005_m04_c02
            mc "What do you want from me?"
            scene sm1cs-am005-66 choice-what-want-am-lying-dont-know-mc-sounds-like-lie_c1 with dissolve
            play voice3 girl22_sex_closedmoan6 noloop
            am "I don't know."
            play voice3 mc_arrogant_hm3 noloop
            mc "Sounds like a lie to me."
            jump sm1cs_am005_reply_1
        "You look so cute when you're flustered"(hint="sm1cs_am005_m04_h03"):
            call sm1cs_am005_m04_c03 from _call_sm1cs_am005_m04_c03
            mc "You look so cute when you're flustered."
            scene sm1cs-am005-73 choice-look-cute-am-angry-am-trying-be-serious-mc-me-too_c1 with dissolve
            play voice3 girl22_hey_scared noloop
            am "I'm trying to be serious here."
            play voice2 mc_yes_yeah7 noloop
            mc "Me too. I seriously think you look cute when you get mad."
            scene sm1cs-am005-74 am-clench-fist-mc-angry-kitty-am-kick-ass_c1 with dissolve
            play voice2 mc_happy_hah2 noloop
            mc "Like an angry little kitty."
            play voice3 girl22_angry_argh2 noloop
            am "I will kick your ass."
            scene sm1cs-am005-75 mc-leans-closer-tells-am-not-what-want-do-him_c1 with dissolve
            play voice2 mc_no_uhuh1 noloop
            mc "Nuh-uh. I can see it. That's not what you want to do to me, is it?"
            jump sm1cs_am005_reply_1
label sm1cs_am005_reply_1:
    scene sm1cs-am005-67 am-shutup-want-truth-dum-stupid-truth_c1 with dissolve
    play voice3 girl22_angry_dagh noloop
    am "Shut up. Okay, you want the truth?"
    am "The dumb stupid, no filters, just the bare thing?"
    scene sm1cs-am005-68 mc-yeah-am-want-ask-question_c1 with dissolve
    play voice2 mc_yes_yes8 noloop
    mc "Uh. Yes?"
    play voice3 girl22_disappointed_geh noloop
    am "I want to ask you a question, and I want a no bull-shit answer."
    scene sm1cs-am005-70 am-look-vulenarable-ask-do-like-me_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Ask away."
    play voice3 girl22_surprised_eh2 noloop
    am "Even with me being a bitch to you, for some totally warranted reasons, and a few... unwarranted ones."
    am "..."
    am "Do you like me?"
    scene sm1cs-am005-71 mct-didnt-see-coming-what-question-this_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Okay I didn't see that coming."
    scene sm1cs-am005-72 am-binary-question-mc-sighs_c1 with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "What kind of question is that?"
    play voice3 girl22_disappointed_mmf noloop
    am "The kind that has a simple binary answer, [mcname]."
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "*sighs* Listen April. I'm going to tell you something that I haven't really talked to many people about."
    jump sm1cs_am005_reply_2
label sm1cs_am005_reply_2:
    scene sm1cs-am005-76 mc-sighs-rushed-relationship-fcking-blew-up-face_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I rushed into a relationship with someone recently."
    mc "*softly* And it fucking blew up in my face."
    if player.get_choice("sm1cs_am004_no_sex"):
        scene sm1cs-am005-86 am-empathetic-mc-sucks-no-excuses_c1 with dissolve
        play voice3 girl22_sex_closedmoan4 noloop
        am "That sucks, [mcname]."
        am "But that doesn't excuse what I did. It wasn't fair."
        scene sm1cs-am005-87 am-looks-away-guess-not-complete-asshat-sorry-how-acted_c1 with dissolve
        play voice3 girl22_disappointed_ehh2 noloop
        am "So I guess I should just say that you're not a complete asshat."
        am "And I like you, and I'm sorry for how I acted."
        scene sm1cs-am005-88 su-surprised-wait-you-like-me_c1 with dissolve
        play voice2 mc_thinking_wait3 noloop volume 0.8
        mc "Wait. You like me, even with all my flaws?"
        play voice3 girl22_yes_questioning noloop
        am "I can like parts of you and dislike other parts of you."
        scene sm1cs-am005-89 am-can-parts-dislike-others-not-completely-useless_c1 with dissolve
        play voice3 girl22_arrogant_he noloop
        am "You're still pretty stupid for thinking you could just start working at an IT job without any training."
        am "But... you're not completely useless and I could probably stomach spending time with you."
        am "Outside of work. Maybe. If that's something you'd be into."
        jump sm1cs_am005_no_sex_2
    else:
        scene sm1cs-am005-77 mc-understanting-totally-gets-it_c1 with dissolve
        play voice2 mc_disappointed_ehh3 noloop
        mc "So I totally get... wanting to start things off on the right foot."
        mc "Even when it doesn't seem like you're starting anything."
        play sound sfx_cloth_rustling2
        scene sm1cs-am005-78 mc-what-now-am-thought-he-will-know_c1 with dissolve
        play voice2 mc_arrogant_hm2 noloop
        mc "So. Now what?"
        play voice3 girl22_surprised_huh2 noloop
        am "I thought you would know."
        scene sm1cs-am005-79 mc-we-try-date-something-am-yeah-something_c1 with dissolve
        play voice2 d1s5_mchappy noloop volume 1.7
        mc "I guess we can try a date. Or something."
        play voice3 girl22_yes_yeah4 noloop
        am "Yeah. Or something."
        scene sm1cs-am005-80 am-starts-walking-away-set-something-up-growls_c1 with dissolve
        play voice3 girl22_disappointed_ehh1 noloop
        am "You set something up.{w} Or I will.{w} No, you should.{w} You have more experience.{w} Or maybe I should."
        am "*frustrated growl* I don't know but-"
        play sound sfx_heels_steps1 loop
        scene sm1cs-am005-81 am-stands-shoulder-mc-like-they-both-like-each-other_c1 with dissolve
        am "I like that...{w} we both {i}like{/i} each other."
        play sound2 sfx_door_open2 noloop
        scene sm1cs-am005-82 am-leaves-mc-thinks-behind-her_c1 with dissolve
        play voice2 mc_thinking_hmm6 noloop
        mct "Okay, that went in a very different direction than I thought it would go."
        mct "But... I guess I should call it progress. I mean I definitely want to pick up where we left off last time."
        scene sm1cs-am005-83 mc-sighs-more-thinking_c1 with dissolve
        play voice2 d14s16_smell noloop volume 0.8
        mct "Then again, that's not exactly what April wants."
        mct "Hmmmm. Maybe. Nope, that's not it either."
        play sound2 sfx_heels_steps2
        scene sm1cs-am005-85 mc-follow-am-out-door_c1 with dissolve
        mct "Serves me right for starting to like such a confounding woman..."
        jump sm1cs_am005_end
label sm1cs_am005_no_sex_2:
    scene sm1cs-am005-90 am-well-speak-choice-menu_c1 with dissolve
    mc "..."
    play voice3 girl22_surprised_huh1 noloop
    am "Well. Say something."
    menu:
        "Tease April"(hint="sm1cs_am005_m05_h01"):
            call sm1cs_am005_m05_c01 from _call_sm1cs_am005_m05_c01
            scene sm1cs-am005-91 choice-tease-mc-leans-closer-what-part-like-most-am-grrr_c1 with dissolve
            play voice2 mc_thinking_mmm7 noloop
            mc "What part of me do you like the most?"
            play voice3 girl22_angry_heergh noloop
            am "Grrrrrr."
            scene sm1cs-am005-92 mc-confident-come-one-say-it_c1 with dissolve
            play voice2 mc_hey_hey3 noloop
            mc "Come on, you can say it."
            play voice3 girl22_angry_argh3 noloop
            play sound sfx_leg_kick5
            scene sm1cs-am005-93 am-knees-mc-in-balls_c1 with vpunch
            play voice2 mc_pain_ou6 noloop
            pause
            scene sm1cs-am005-94 mc-in-pain-groans_c1 with dissolve
            play voice2 mc_pain_argh1 noloop
            mc "*groaning* up-fuaah..."
            play sound sfx_fall_down1
            scene sm1cs-am005-95 am-leaving-office-mc-on-ground-kicked-balls_c1 with dissolve
            play voice3 girl22_angry_hmm noloop
            am "Get your mind out of the gutter. {b}This{/b} is where I work, [mcname]."
            play voice2 mc_pain_rrrr noloop
            mc "Hrrggh... understood. No fly zone."
            mct "Could have gone worse."
            jump sm1cs_am005_walkout
        "I like you too, April"(hint="sm1cs_am005_m05_h02"):
            call sm1cs_am005_m05_c02 from _call_sm1cs_am005_m05_c02
            scene sm1cs-am005-96 mc-like-too-am_c1 with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "I like you too, April."
            scene sm1cs-am005-97 am-very-happy-good-feel-better_c1 with dissolve
            play voice3 girl22_happy_relief noloop
            am "Good. Then... we're both on the same page."
            am "I feel a lot better about everything now."
            jump sm1cs_am005_thumbsup_end
        "No more games"(hint="sm1cs_am005_m05_h03"):
            call sm1cs_am005_m05_c03 from _call_sm1cs_am005_m05_c03
            scene sm1cs-am005-102 choice-no-nice-games-mc-serious-not-more-games_c1 with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "No more games, April. If we're... I don't even know."
            scene sm1cs-am005-103 am-testing-cooperative-mc-right-so-no-more-games_c1 with dissolve
            play voice3 girl22_happy_laugh1 noloop
            am "Testing out a cooperative longevity growth exercise."
            play voice2 mc_yes_yes3 noloop
            mc "Right, so if we're doing that, no more games."
            scene sm1cs-am005-104 am-doesnt-get-it-mc-dont-like-games-end-up-tossed-out-car_c1 with dissolve
            play voice3 girl22_arrogant_hm noloop
            am "I don't understand. Games are fun with people you like."
            play voice2 mc_no_nah2 noloop
            mc "I don't like games that end up with me being tossed out of a car in the middle of the night."
            scene sm1cs-am005-105 am-okay-no-more-games_c1 with dissolve
            play voice3 girl22_yes_aga4 noloop
            am "Okay, so no games like {i}that{/i}."
            jump sm1cs_am005_no_sex_3
label sm1cs_am005_no_sex_3:
    scene sm1cs-am005-106 mc-choice-menu_c1 with dissolve
    menu:
        "Sounds good"(hint="sm1cs_am005_m06_h01"):
            call sm1cs_am005_m06_c01 from _call_sm1cs_am005_m06_c01
            scene sm1cs-am005-107 choice-sounds-good-mc-am-look-each-other-good-great-good_c1 with dissolve
            play voice2 mc_yes_okay1 noloop
            mc "Sounds good."
            play voice3 girl22_yes_yep4 noloop
            am "Good."
            mc "Great."
            jump sm1cs_am005_thumbsup_end
        "No more games, period"(hint="sm1cs_am005_m06_h02"):
            scene sm1cs-am005-108 choice-no-more-games-mc-no-games-get-april-am-okay-oay_c1 with dissolve
            play voice2 mc_angry_cough1 noloop
            mc "No more games, period. You get me, April?"
            play voice3 girl22_yes_yeah3 noloop
            am "Okay okay. Easy."
            scene sm1cs-am005-109 am-promises-hand-behind-mc-good-_c1 with dissolve
            play voice3 girl22_happy_laugh3 noloop
            am "I promise. No more games. I will court you like a southern bell from the Antebellum Era."
            play voice2 mc_yes_aga1 noloop
            mc "Good. That's what I like to hear."
            scene sm1cs-am005-110 mc-akward-has-get-back-it-am-yep-no-slacking_c1 with dissolve
            play voice2 mc_thinking_hmm3 noloop
            mc "I need to get back to it."
            play voice3 girl22_yes_yep4 noloop
            am "Yup. No slacking at Orbix, Mister Young."
            play sound sfx_heels_steps2 loop
            scene sm1cs-am005-111 mc-turns-away-confused-am-hmm_c1 with dissolve
            play voice2 mc_angry_hm1 noloop
            mct "What the hell is the Antebellum Era?"
            scene sm1cs-am005-112 am-fingers-crossed-behind-ass-thinks-game-on_c1 with dissolve
            play voice3 girl22_thinking_hmm1 noloop
            am "Hmm."
            am "*thinking* Game on, [mcname]."
            jump sm1cs_am005_walkout
label sm1cs_am005_thumbsup_end:
    scene sm1cs-am005-98 am-nervous-uh_c1 with dissolve
    play voice3 girl22_surprised_eh2 noloop
    am "Uh."
    scene sm1cs-am005-99 am-finger-up-keep up-good-work_c1 with dissolve
    play voice3 girl22_happy_laugh3 noloop
    am "Keep up the good work."
    scene sm1cs-am005-100 am-walking-past-mc-really-thumb-up-thinks-strange-way_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "Uh. Did she just really give me a thumb's up?"
    scene sm1cs-am005-101 mct-doubt-things-ever-be-boring_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "In a strange way, even though we're getting closer, I kind of prefer April's non-work side."
    mct "I doubt things will ever be boring if I get to know her better."
    jump sm1cs_am005_walkout
label sm1cs_am005_walkout:
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    play sound3 sfx_door_closed2 noloop
    $ renpy.music.set_volume(0.7, 2.0, "sound4" )
    if player.get_choice("sm1cs_am005_tease_am"):
        scene sm1cs-am005-113 am-walk-away-mc-follows-holding-his-balls_c1 with dissolve
    else:
        scene sm1cs-am005-114 am-mc-walk-out-small-office-return-desks_c1 with dissolve
    pause
    scene sm1cs-am005-115 cw-notices-them-while-doing-some-work_c1 with dissolve
    pause
    play voice4 girl29_thinking_mmm2 noloop
    scene sm1cs-am005-116 cw-looking-at-them-hmm-end-scene_c1 with dissolve
    cw "Hmmm."
    call sm1cs_am005_failed_am from _call_sm1cs_am005_failed_am
    jump sm1cs_am005_end
label sm1cs_am005_end:
    call sm1cs_am005_unlock_cw from _call_sm1cs_am005_unlock_cw
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 5.0, "sound4" )
    stop music fadeout 3.0
    stop sound4 fadeout 2.0
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    if player.get_choice("sm1cs_am005_failed_am") is False:
        $ player.progress_storyline(AM_STORY, 2)
    $ StoryController.end_scene(AM_STORY, 1, 0, 2)
    return
label sm1cs_am005_failed_am:
    $ player.set_choice("sm1cs_am005_failed_am")
    return
label sm1cs_am005_unlock_cw:
    if player.get_storyline(CW_STORY) is False:
        $ StoryController.activate_story_line(CW_STORY)
    return
label sm1cs_am005_m01_c01:
    $ player.set_choice("sm1cs_am005_push_am")
    $ CharacterController.get_character("am").add_point()
    return
label sm1cs_am005_m02_c01:
    $ player.set_choice("sm1cs_am005_act_evasive")
    $ CharacterController.get_character("am").deduct_point()
    return
label sm1cs_am005_m03_c01:
    $ player.set_choice("sm1cs_am005_end_am_quest")
    return
label sm1cs_am005_m04_c01:
    $ player.set_choice("sm1cs_am005_it_was_game")
    return
label sm1cs_am005_m04_c02:
    $ player.set_choice("sm1cs_am005_what_do_you_want")
    return
label sm1cs_am005_m04_c03:
    $ player.set_choice("sm1cs_am005_cute_flushtered")
    return
label sm1cs_am005_m05_c01:
    $ player.set_choice("sm1cs_am005_tease_am")
    $ CharacterController.get_character("am").add_point()
    return
label sm1cs_am005_m05_c02:
    $ player.set_choice("sm1cs_am005_like_am")
    $ CharacterController.get_character("am").add_point(2)
    return
label sm1cs_am005_m05_c03:
    $ player.set_choice("sm1cs_am005_no_more_games")
    return
label sm1cs_am005_m06_c01:
    $ player.set_choice("sm1cs_am005_sounds_good")
    return