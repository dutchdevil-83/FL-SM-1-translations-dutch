label sm1ms015:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound4 sfx_office_ambience1 fadein 2.0
    play sound sfx_heels_steps1 fadein 1.0 loop
    play sound2 sfx_heels_steps2 fadein 1.0
    scene sm1-ms015-01 mc-sy-my-walk-into-office_c1 with dissolve
    play music acid_jazz
    pause
    scene sm1-ms015-02 dont-know-good-idea-place-seem-busy_c1 with dissolve
    play voice4 girl34_thinking_emm1 noloop
    my "I don't know if this is a good idea, [mcname]."
    my "This place looks very busy."
    scene sm1-ms015-03 mc-can-be-fine-wanted-bring-see-effort-mc-put_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 2.4
    mc "It can be, but it will be fine."
    mc "I just wanted to bring you by to see some of the efforts I'm putting into the studio."
    play voice4 girl34_yes_ugu1 noloop
    my "Mmhmm."
    scene sm1-ms015-04 sy-whoah-so-cool-like-silicon-valley_c1 with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Woah. You work in a place like this."
    sy "So cool. It's like a Silicon Valley set."
    scene sm1-ms015-05 sy-not-call-attention_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Stacy, don't call attention to us."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1-ms015-06 mc-my-sy-stop-look-around_c1 with dissolve
    pause
    scene sm1-ms015-07 my-impressed-sy-what-orbix-does_c1 with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "What does Orbix do again?"
    play voice2 mc_thinking_hm noloop
    mc "Their main focus is developing IT solutions and infastructure."
    scene sm1-ms015-08 mc-they-do-specialized-work-also_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "But they do a lot of specialized work, too. Right now, we're working on building a new website system for one of the local news companies."
    play voice3 girl34_thinking_hmm2 noloop
    my "Mmmm."
    scene sm1-ms015-09 my-thinking-mmm-mc-what-up_c1 with dissolve
    play voice2 mc_surprised_uh2 noloop
    if persistent.is_special:
        mc "Everything okay, mom?"
    else:
        mc "Everything okay, Melony?"
    play voice4 girl34_thinking_emm5 noloop
    my "Everything is fine. I... I think I assumed that you'd have some of your college friends make it look like a work place."
    scene sm1-ms015-10 my-all-fine-no-way-this-fake-workplace_c1 with dissolve
    play voice4 girl34_happy_laugh1 noloop
    my "But there is no way this is a fake workplace."
    play sound sfx_heels_steps1 loop
    scene sm1-ms015-11 cw-approached-group_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1-ms015-12 cw-swoops-should-hope-not-orbix-most-industious-city_c1 with dissolve
    play voice5 girl29_yes_aga1 noloop
    cw "I should hope not."
    cw "Orbix is one of the most industrious businesses in the city."
    scene sm1-ms015-13 cw-so-please-passed-test_c1 with dissolve
    play voice5 girl29_arrogant_ha noloop
    cw "I'm {i}so{/i} glad we passed your test, miss."
    scene sm1-ms015-14 my-sorry-sometimes-mc-exaggerates_c1 with dissolve
    play voice4 girl34_surprised_ohmy1 noloop
    my "Oh my. I'm sorry."
    if persistent.is_special:
        my "It's just that sometimes my son has been known to exaggerate."
        scene sm1-ms015-15 cw-see-who-person_c1 with dissolve
        play voice5 girl29_thinking_oh noloop
        cw "I see."
        cw "And who is your son exactly?"
    else:
        my "[mcname] has pulled a fib now and then, so I wanted to make sure he was telling the truth."
        scene sm1-ms015-15 cw-see-who-person_c1 with dissolve
        play voice5 girl29_thinking_oh noloop
        cw "Oh, so [mcname] has a flair for deception. How curious."
    cw "But I guess I should be asking something else while I'm here."
    cw "Who are you? Are you a client?"
    scene sm1-ms015-16 my-introduces-herself_c1 with dissolve
    play voice4 girl34_surprised_oh4 noloop
    if persistent.is_special:
        my "Oh, please excuse me. My name is Melony Young."
        my "I'm [mcname]'s mother."
        scene sm1-ms015-17 my-introduces-sy-heya_c1 with dissolve
        play voice4 girl34_disappointed_eem3 noloop
        my "And this is my daughter, Stacy."
        play voice3 stacy_hey_attention1 noloop
        sy "Heya."
    else:
        my "Oh, please excuse me. My name is Melony Chase."
        my "I'm a close family friend of [mcname]."
        scene sm1-ms015-17 my-introduces-sy-heya_c1 with dissolve
        play voice3 stacy_hey_attention1 noloop
        sy "And I'm [mcname]'s best friend, Stacy Brown."
    scene sm1-ms015-18 cw-surprised-oh-nice-both-you_c1 with dissolve
    play voice5 girl29_disappointed_oh noloop
    cw "Oh... Nice to meet you both."
    scene sm1-ms015-19 sy-wanted-see-workplace-sorry-protective_c1 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "We just wanted to see what his workplace was like."
    sy "Sorry, we can get a little protective."
    scene sm1-ms015-20 cw-forgive-hastiness-my-should-we-leave_c1 with dissolve
    play voice5 girl29_thinking_hmm4 noloop
    cw "Well, please forgive my hastiness. I didn't expect strangers to be wandering in."
    play voice4 girl34_disappointed_eh noloop
    my "Should we leave?"
    scene sm1-ms015-21 cw-hmm-mc-will-be-just-minute_c1 with dissolve
    play voice5 girl29_thinking_hmm3 noloop
    cw "Hmmm."
    play voice2 mc_hey_hey2 noloop
    mc "They'll just be a few minutes, Claire. We won't bother anyone."
    scene sm1-ms015-22 cw-this-highly-irregular-mc-please_c1 with dissolve
    play voice5 girl29_no_uhuh noloop
    cw "This is highly irregular, [mcname]."
    play voice2 mc_arrogant_nah1 noloop
    mc "Please..."
    scene sm1-ms015-23 mc-tells-my-worried-been-shuts-up-umm_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    if persistent.is_special:
        mc "My mom is just a little worried that I've been..."
    else:
        mc "Melony has just been a little worried that I've been..."
    mc "Ummm."
    play sound sfx_cloth_rustling1
    scene sm1-ms015-24 cw-curious-you-been-what_c1 with dissolve
    play voice5 girl29_surprised_huh2 noloop
    cw "That you've been what?"
    scene sm1-ms015-25 my-steps-in-decided-put-college-hold-other-opportunities_c1 with dissolve
    play voice4 girl34_angry_breath1 noloop
    my "That he's decided to put his college degree on hold and pursue..."
    my "Ahem. That he's been looking at {i}other{/i} opportunities to make his way in life."
    scene sm1-ms015-26 cw-well-doing-adequate-job-her-hope-continues-learn_c1 with dissolve
    play voice5 girl29_thinking_hmm1 noloop
    cw "Hmmm. Well, I can say he's been more than adequate at his job here so far."
    cw "It's my hope he continues to learn from the more skilled programmers and becomes a real asset."
    play sound sfx_phone_buzz
    scene sm1-ms015-27 cw-gets-text-on-phone_c1 with dissolve
    pause
    scene sm1-ms015-28 cw-give-ten-minutes-then-need-business-back-usual_c1 with dissolve
    play voice5 girl29_arrogant_he noloop
    if persistent.is_special:
        cw "I'll give you ten minutes, Mrs. Young."
    else:
        cw "I'll give you ten minutes, Mrs. Chase."
    cw "Then I'm afraid we need to be back to business as usual."
    scene sm1-ms015-29 my-thanks-claire-miss-nvm_c1 with dissolve
    play voice4 girl34_yes_happy3 noloop
    my "Of course. Thank you, Claire."
    play voice5 girl29_arrogant_hm noloop
    cw "It's Miss."
    play sound sfx_heels_steps1 loop
    scene sm1-ms015-30 cw-walks-away-towards-workplace_c1 with dissolve
    play voice5 girl29_disgust_meh noloop
    cw "Nevermind."
    play voice2 mc_happy_a1 noloop
    mc "Thank you, Miss Watts."
    stop sound fadeout 3.0
    scene sm1-ms015-31 sy-seems-fun-my-very-serious-like-her_c1 with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "She seems like a lot of fun."
    play voice4 girl34_yes_ugu2 noloop
    my "Very serious woman. I like her."
    scene sm1-ms015-32 mc-she-boss-boss-will-show-desk_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, I mean, she is my boss' boss, so she likes to run a tight ship."
    mc "I'll show you my desk, and then we'll get out of here."
    play sound sfx_heels_steps1 fadein 1.0 loop
    play sound2 sfx_heels_steps2 fadein 1.0
    scene sm1-ms015-33 mc-fam-approach-work-desk_c1 with dissolve
    pause
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    scene sm1-ms015-34 ag-dont-listen-am-not-know-good-music_c1 with dissolve
    play voice5 girl27_no_uhuh3 noloop
    ag "Don't listen to her, Nari."
    ag "April doesn't know what good music is."
    scene sm1-ms015-35 am-which-one-in-band_c1 with dissolve
    play voice6 girl22_surprised_what noloop
    am "Which of the three of us is in a band and has actual musical talent?"
    scene sm1-ms015-36 ns-maybe-april-right-am-notices-mc_c1 with dissolve
    play voice7 nari_yes_yep noloop
    ns "I have to admit, she makes a good point, Anna."
    scene sm1-ms015-37 ag-can-have-talent-not-taste-am-maybe-talk-your-taste_c1 with dissolve
    play voice5 girl27_arrogant_huh2 noloop
    ag "You can have musical talent and still have no real taste when it comes to music."
    play voice6 girl22_thinking_oh noloop
    am "Maybe we should talk about your {i}tastes{/i}. Anna."
    scene sm1-ms015-38 ag-blushes-looks-away-dont-know-what-say_c1 with dissolve
    play voice5 girl27_arrogant_pfhah noloop
    pause
    scene sm1-ms015-39 ag-notices-mc-agknowledges-him_c1 with dissolve
    play voice5 girl27_hey_interested noloop
    ag "[mcname]!"
    scene sm1-ms015-40 ns-hello-mc-am-who-backup_c1 with dissolve
    play voice7 nari_hey_high noloop
    ns "Hello [mcname]."
    play voice6 girl22_surprised_huh1 noloop
    am "Who's your backup?"
    scene sm1-ms015-41 mc-introduces-my-sy_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    if persistent.is_special:
        mc "This is my mother, Melony."
        mc "And my sister, Stacy."
    else:
        mc "This is Stacy, my best friend."
        mc "And this is Melony Chase, a friend of my family."
    scene sm1-ms015-42 mc-wanted-show-where-work_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "I wanted to show them around my work."
    scene sm1-ms015-43 mc-this-boss-anna-she-smiles-correct-mc_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "This is Anna Goodwin, my boss."
    play voice5 girl27_yes_aga3 noloop
    ag "Hello, I'm actually [mcname]'s team lead. In charge of his day-to-day."
    scene sm1-ms015-44 mc-right-my-nice-meet-you-sy-hello-anna_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Oh right. My mistake."
    play voice4 girl34_hey_hi1 noloop
    my "Nice to meet you."
    play voice3 stacy_hey_happy2 noloop
    sy "Hello, Anna."
    scene sm1-ms015-45 mc-introduces-am-top-coder-nari_c1 with dissolve
    play voice5 girl27_thinking_emm3 noloop
    ag "That's April Mercer, our top coder."
    ag "And this is Nari Song."
    if player.has_played_scene("sm1cs_ns010"):
        scene sm1-ms015-46 ns-nice-see-again-stacy-same-fine_c1 with dissolve
        play voice7 nari_thinking_oh noloop
        ns "Nice to see you again, Stacy."
        play voice3 stacy_yes_yap3 noloop
        sy "Likewise, Nari. How are you doing?"
        ns "Fine."
    elif persistent.is_special:
        scene sm1-ms015-47 ns-not-know-mc-sister-great-meet-sy-likewise_c1 with dissolve
        play voice7 nari_thinking_oh noloop
        ns "I didn't realize that [mcname] had a sister."
        ns "It's great to meet you, Stacy."
        play voice3 stacy_yes_yap3 noloop
        sy "Likewise, Nari."
    play sound sfx_chair_slide1
    scene sm1-ms015-48 ns-stands-up-delighted-meet-melony-not-mention-her-before_c1 with dissolve
    play voice7 nari_hey_unsure noloop
    ns "And I'm delighted to meet you too, Miss Melony."
    if persistent.is_special:
        ns "[mcname] did not mention he had such a beautiful mother before."
        scene sm1-ms015-49 sy-giggles-my-thanks-ns_c1 with dissolve
        play voice3 stacy_laugh4 noloop
        sy "*giggles*"
        play voice4 girl34_happy_relief4 noloop
        my "Thank you, Nari."
    scene sm1-ms015-50 sy-looks-at-am_c1 with dissolve
    pause
    play sound sfx_heels_steps2
    scene sm1-ms015-51 sy-step-forward-offers-hand-great-meet-april-she-also-programmer_c1 with dissolve
    stop sound fadeout 3.0
    play voice3 stacy_hey noloop
    sy "It's great to meet you, April."
    sy "You know, I'm a bit of a programmer myself."
    scene sm1-ms015-52 am-thinking-what-make-sy_c1 with dissolve
    play voice6 girl22_arrogant_hm noloop
    pause
    if player.has_played_scene("sm1cs_am006"):
        play sound sfx_hands_clap3
        scene sm1-ms015-53 am-shakes-sy-hand-cool_c1 with dissolve
        play voice6 girl22_yes_aga6 noloop
        am "Cool."
    else:
        play sound sfx_cloth_rustling2
        scene sm1-ms015-54 am-not-shaking-hand-good-for-you_c1 with dissolve
        play voice6 girl22_yes_yep4 noloop
        am "Good for you."
    scene sm1-ms015-55 am-need-make-calls_c1 with dissolve
    play voice6 girl22_thinking_eeh noloop
    am "I need to go make some calls."
    play sound sfx_heels_steps1 loop
    scene sm1-ms015-56 am-leaves-area_c1 with dissolve
    pause
    stop sound fadeout 2.0
    scene sm1-ms015-57 sy-shit-did-do-something-ag-nah-just-april-being-april_c1 with dissolve
    play voice3 stacy_disappointed_oh3 noloop
    sy "Shit did I do something wrong?"
    play voice5 girl27_no_nah2 noloop
    ag "Nah, that's just April. She's always like that around new people."
    scene sm1-ms015-58 ns-ask-my-what-brings-here-my-well_c1 with dissolve
    play voice7 nari_disappointed_huh noloop
    ns "Can I ask what brought you in today?"
    play voice4 girl34_thinking_hmm7 noloop
    my "Well..."
    scene sm1-ms015-59 my-looking-ag-ns-explains_c1 with dissolve
    play voice4 girl34_arrogant_ha5 noloop
    my "[mcname] mentioned he was working at Orbix and I just wanted to see what it was like."
    my "I'm a little worried that he's stopped going to college."
    scene sm1-ms015-60 my-looks-mc-admits-very-proud_c1 with dissolve
    play voice4 girl34_thinking_emm3 noloop
    my "But I have to admit."
    my "I'm very proud of him, working at a place like Orbix."
    scene sm1-ms015-61 ns-happy-proud-mc-been-great-worker_c1 with dissolve
    play voice7 nari_happy_yeah noloop
    ns "Oh yeah. It's a great place to work and [mcname] has been a great worker."
    scene sm1-ms015-62 ag-tells-nari-mc-started-same-day-my-really-so-work-buddies_c1 with dissolve
    play voice5 girl27_happy_relief2 noloop
    ag "Nari and [mcname] actually started working on the same day."
    play voice4 girl34_happy_nice1 noloop
    my "Really? That's very nice. So you're work buddies."
    scene sm1-ms015-63 ns-yes-already-helipng-mc_c1 with dissolve
    play voice7 nari_yes_emotional noloop
    ns "Yes. I've been doing my best to teach [mcname] a little bit of what I know to help him do even better than he already was."
    if player.has_played_scene("sm1cs_ns007"):
        scene sm1-ms015-64 ns-acting-cute-leanred-lot-mc-ag-really_c1 with dissolve
        play voice7 nari_thinking_emm noloop
        ns "And I've learned a lot from [mcname] too."
        play voice5 girl27_surprised_huh2 noloop
        ag "Really? I'm a little surprised to hear that."
        scene sm1-ms015-65 ns-realizes-should-not-say-that_c1 with dissolve
        pause
        scene sm1-ms015-66 ag-ask-what-mc-teaching-ns_c1 with dissolve
        play voice5 girl27_arrogant_huh1 noloop
        ag "What has [mcname] been teaching you?"
        scene sm1-ms015-67 ns-english-then-corrects-way-english-code_c1 with dissolve
        play voice7 nari_disappointed_mff noloop
        ns "Ummm. English."
        ns "I mean, the way the English code."
        scene sm1-ms015-68 ns-digging-hole-deeper-means-way-americans-code_c1 with dissolve
        play voice7 nari_angry_cough noloop
        ns "I mean, the special way that Americans code."
        play voice5 girl27_thinking_emm5 noloop
        ag "Nari are you feeling well?"
        scene sm1-ms015-69 ns-excuse-need-bathroom_c1 with dissolve
        play voice7 nari_surprised_ehh noloop
        ns "I have to use the restroom. Excuse me."
        play sound sfx_heels_run2
        scene sm1-ms015-70 ns-leaves-are-go-bathroom-ag-chuckles_c1 with dissolve
        play voice5 girl27_happy_laugh6 noloop
        ag "*chuckles* Haha. I hope she never changes."
    else:
        scene sm1-ms015-69 ns-excuse-need-bathroom_c1 with dissolve
        play voice7 nari_thinking_emm noloop
        ns "Excuse me, I need to use the restroom."
        play sound sfx_heels_run2
        scene sm1-ms015-70 ns-leaves-are-go-bathroom-ag-chuckles_c1 with dissolve
        play voice5 girl27_happy_laugh6 noloop
        ag "**chuckles*"
    scene sm1-ms015-71 ag-nice-meeting-sy-my-but-have-much-work_c1 with dissolve
    play voice5 girl27_thinking_hmm4 noloop
    ag "Well, it was a pleasure to meet you, Melony, Stacy."
    ag "But we do have a lot of work to handle today, so we should get back to it."
    scene sm1-ms015-72 ag-that-includes-mc-she-chuckles_c1 with dissolve
    play voice5 girl27_happy_laugh4 noloop
    ag "That includes you too, [mcname]."
    ag "*chuckles*"
    play sound sfx_heels_steps1 loop
    scene sm1-ms015-73 ag-starts-walking-towards-workstation_c1 with dissolve
    pause
    play sound2 sfx_heels_steps2
    scene sm1-ms015-74 mc-leads-sy-my-towards-exit_c1 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1-ms015-75 mct-stands-next-door-what-think_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "So what do you think?"
    if not player.has_played_scene("sm1ms018"):
        scene sm1-ms015-76 my-very-nice-only-pays-so-much_c1 with dissolve
        play voice4 girl34_yes_aga4 noloop
        my "It's a very nice place, [mcname]."
        my "But a nice job like this only pays so much."
        scene sm1-ms015-77 my-convincing-mc-wants-him-just-think_c1 with dissolve
        play voice4 girl34_thinking_hmm6 noloop
        my "You were going to college to get a business degree."
        my "I mean just think.{w} If you got your degree, you could have been running a place like this in a few years."
        scene sm1-ms015-78 mc-diplomatic-explaining_c1 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "Well, there is no guarantee that I could have become some twenty-some CEO."
        mc "On the other hand, I am a twenty-something co-owner for the studio."
        scene sm1-ms015-79 sy-looking-my-got-you-there-mom_c1 with dissolve
        play voice3 stacy_arrogant_ha2 noloop
        if persistent.is_special:
            sy "Haha. He's got you there, mom."
        else:
            sy "Haha. He's got you there, Melony."
        play sound sfx_hair_scratch1
        scene sm1-ms015-80 my-not-happy-supposed-orbix-good-job_c1 with dissolve
        play voice4 girl34_arrogant_hm1 noloop
        my "Hmmm. Well, I suppose that, at the very least, Orbix is a good job for you."
        my "It gives you something to fall back on when things don't work out."
        scene sm1-ms015-81 mc-convice-my-things-work-out_c1 with dissolve
        play voice2 mc_hey_hey5 noloop
        mc "Things will work out."
        play voice4 girl34_yes_aga8 noloop
        my "I want them to. But that's not always how life works out."
        mc "Mmmhmm."
    else:
        scene sm1-ms015-82 my-likes-place-more-than-theater-more-structure_c1 with dissolve
        play voice4 girl34_thinking_eeh1 noloop
        my "I think I like this place a bit more than the theater."
        my "More structure for you."
        scene sm1-ms015-83 my-frowns-must-ask-worth-studio_c1 with dissolve
        play voice4 girl34_arrogant_hm1 noloop
        my "But you have to ask yourself if working all of these jobs is worth it for the studio, [mcname]."
        my "There are only so many hours in the day."
        scene sm1-ms015-84 mc-understanding-but-pumped_c1 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "I hear you."
        mc "But I'm working hard to make my dream a reality."
        mc "So a little hard work now is going to pay off later."
        play sound sfx_hair_scratch1
        scene sm1-ms015-85 my-well-spirit-infectious_c1 with dissolve
        play voice4 girl34_yes_aga4 noloop
        my "Well, your can-do spirit is certainly infectious."
        my "And I guess if the studio doesn't work out, you could try to work here full time."
        play voice2 mc_yes_yeah2 noloop
        mc "Yeah maybe..."
    scene sm1-ms015-86 mc-well-lets-back-studio-sy-yes_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Well, let's head back to the studio."
    play voice3 stacy_yes_yap1 noloop
    sy "Yup."
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    stop music fadeout 3.0
    stop sound4 fadeout 2.0
    $ player.completion_log_add_item_date("sm1ms015")
    $ StoryController.end_scene(MS, 2, 0, 2, IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW)
    return