image sm1fs-i003-glambot-1 = Movie(play = "images/FS_IT/s003/anim/sm1fs-i003-a59-2x-30fps.webm", start_image = "sm1fs-i003-a59 glambot-anim-00000", image = "sm1fs-i003-a59 glambot-anim-00099", loop = False)
screen sm1fs_i003_presentation():
    style_prefix "sm1fs_i003_presentation"

    text _("End of onboarding presentation") xsize 810 xalign 0.68 yalign 0.5 size 100 color "#000000" text_align 0.5
    text _("Page 247/247") xalign 0.845 yalign 0.2 size 35 color "#000000"
label sm1fs_i003:
    play voice3 stacy_disappointed_snoring fadein 2.0 volume 0.5
    play voice2 mc_disappointed_snoring1 fadein 1.0
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.2, 0.0, "sound2" )
    play sound2 sfx_parkday_birds
    scene sm1fs-i003-01-01 mc-sy-sleep-naked-studio_c1 with dissolve
    pause
    play voice2 d7s6_awake noloop volume 2.0
    stop voice3 fadeout 2.5
    $ renpy.music.set_volume(1.0, 0.0, "sound4" )
    play sound4 sfx_phone_ringtone1
    scene sm1fs-i003-01-02 mc-wakes-phone-ringing_c1 with hpunch
    pause
    play sound sfx_cloth_planket2
    scene sm1fs-i003-01-03 mc-looks-phone-sy-shut-up-takes-blanket_c1 with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "Shuuddddup."
    stop sound4
    play sound sfx_phone_hungup1
    scene sm1fs-i003-01-04 mc-answers-phone_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hello, this is [mcname]."
    $ renpy.music.set_volume(0.0, 0.8, "sound2" )
    $ renpy.music.set_volume(0.7, 0.0, "sound3" )
    play sound3 sfx_office_ambience1
    scene sm1fs-i003-01-05 cw-talking-in-office_c1 with dissolve
    play voice4 girl29_hey_provocative noloop
    cw "Hello Mr. Young. I'm not waking you up, am I?"
    $ renpy.music.set_volume(0.2, 0.8, "sound2" )
    $ renpy.music.set_volume(0.0, 0.8, "sound3" )
    scene sm1fs-i003-01-06 mc-lies-doing-morning-workout_c1 with dissolve
    play voice2 d1s5b_emmm noloop
    mc "Uhh, no. Just, uhm, doing a morning work out?"
    $ renpy.music.set_volume(0.0, 0.8, "sound2" )
    $ renpy.music.set_volume(0.7, 0.8, "sound3" )
    scene sm1fs-i003-01-07 cw-tells-mc-he-hired_c1 with dissolve
    play voice3 girl29_yes_aga1 noloop
    cw "Sure. I'm calling to offer you the job if you're still interested."
    $ renpy.music.set_volume(0.2, 0.8, "sound2" )
    $ renpy.music.set_volume(0.0, 0.8, "sound3" )
    scene sm1fs-i003-01-08 mc-jumps-from-bed-awesome-when-start-cw-tells-thirty-mins_c1 with dissolve
    play voice2 mc_scared_huh1 noloop
    mc "Absolutely! Awesome, thank you! When do I start?"
    $ renpy.music.set_volume(0.0, 0.8, "sound2" )
    $ renpy.music.set_volume(0.7, 0.8, "sound3" )
    scene sm1fs-i003-01-05 cw-talking-in-office_c1 with dissolve
    $ renpy.music.set_volume(0.65, 0.0, "music2" )
    play music2 music_sirens_transition1 noloop
    play voice3 girl29_angry_hm noloop
    cw "In 30 minutes. You and our other new hire are to be here to start your onboarding process. Don't be late."
    $ renpy.music.set_volume(0.2, 0.8, "sound2" )
    $ renpy.music.set_volume(0.0, 0.8, "sound3" )
    scene sm1fs-i003-01-09 mc-will-be-there-calls-cw-she-hung-up_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Absolutely, I'll be there Ms. Watts!"
    play sound sfx_phone_hungup1
    "..."
    play voice2 d2s9_confused noloop volume 1.7
    mc "Ms. Watts?"
    scene sm1fs-i003-01-10 mc-looks-phone-sy-agnry-behind-him_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh. I guess she hung up."
    mc "...{w} ..."
    stop sound2 fadeout 2.0
    $ renpy.music.set_volume(1.0, 1.0, "music2" )
    play sound sfx_camera_fly1 volume 2.0
    scene black with Fade(.25, 0, .75, color="#fff")
    pause
    play voice2 mc_pain_argh1 noloop
    $ renpy.music.set_volume(1.0, 1.5, "sound3" )
    $ renpy.music.set_volume(0.7, 1.0, "music2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound sfx_double_door1 volume 1.5
    play sound2 sfx_sport_run1 volume 3.0
    scene sm1fs-i003-02 mc-runs-inside-office-ns-next-to-entrance_c1 with Fade(.25, 0, .75, color="#fff")
    pause
    play voice2 mc_pain_cough1 noloop
    stop sound2
    $ renpy.music.set_volume(0.5, 3.0, "music2" )
    scene sm1fs-i003-03 mc-clocks-himself-ns-observe-out-of-shape_c1 with hpunch
    queue voice2 mc_breathing_heavy noloop
    mc "... 29 minutes... Hell... Yeah..."
    play voice4 nari_arrogant_heh noloop
    ns "You seem to be out of shape."
    scene sm1fs-i003-04 mc-ask-what-ns-explains-reasoning_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "... What?"
    play voice4 nari_thinking_hmm3 noloop
    ns "If you ran from the front of the building to here, it's not that far. Not far enough for you to be out of breath."
    scene sm1fs-i003-05 mc-havent-hit-gym-lately-ns-reason-why-out-shape_c1 with dissolve
    play voice2 mc_angry_huh2 noloop volume 1.5
    mc "... So... You know... I've been... Kind of busy... I haven't really... Been able to get to the gym..."
    scene sm1fs-i003-06 mc-guess-she-right-ns-should-use-threadmill_c1 with dissolve
    play voice4 nari_thinking_oh noloop
    ns "That would be a good reason to be out of shape."
    mc "... I guess?"
    scene sm1fs-i003-07 mc-doesnt-get-it-ns-explaining-mct-who-wierd-chick_c1 with dissolve
    play voice4 nari_hey_calm noloop
    ns "You should start with the treadmill."
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    ns "If you go back to the gym, I'd recommend a treadmill."
    mct "What is up with this lady?"
    stop music2 fadeout 3.0
    play sound sfx_heels_steps2
    scene sm1fs-i003-08 cw-goes-welcome-mc_c1 with dissolve
    $ renpy.music.set_volume(0.7, 0.0, "music" )
    play music music_sucksexful
    pause
    stop sound fadeout 1.0
    scene sm1fs-i003-11 cw-checks-mc-compliments-new-outfit_c1 with dissolve
    play voice3 girl29_thinking_oh noloop
    cw "I see you two have already met. Mr. [mcname] Young, Ms. Nari Song."
    play sound sfx_cloth_rustling2
    scene sm1fs-i003-09 cw-introduces-mc-ns-introduces-herself-in-korean_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "It's nice to meet you Nari."
    play voice4 nari_surprised_ehh noloop
    ns "{font=fonts/arial-unicode.ttf}새로운 잘생긴 동료를 만나서 반가워요!{/font}"
    scene sm1fs-i003-10 mc-doesnt-understand-korean-ns-excuses-herself-introduces-english_c1 with dissolve
    play voice2 d3s7_mcemm noloop
    mc "Uhm..."
    play voice4 nari_disappointed_oh noloop
    ns "Oh, sorry. It's nice to meet you too!"
    scene sm1fs-i003-11 cw-checks-mc-compliments-new-outfit_c1 with dissolve
    play voice3 girl29_thinking_hmm5 noloop
    cw "Mr. Young, I hope you are ready to work."
    cw "Now let's get started, follow me."
    play sound sfx_heels_steps2 loop
    scene sm1fs-i003-12 cw-leads-mc-ns-through-office_c1 with dissolve
    pause
    scene sm1fs-i003-13 cw-leads-ns-mc-ag-desk_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1fs-i003-14 cw-introduces-ag_c1 with dissolve
    play voice3 girl29_yes_aga2 noloop
    cw "I know you both have already met Ms. Anna Goodwin."
    play voice5 girl27_hey_interested noloop
    ag "It's good to see you both! I am absolutely thrilled that you both got hired."
    scene sm1fs-i003-15 mc-ns-both-great-seeing-ag-ns-calls-her-sirname_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I am too!"
    play voice4 nari_happy_yeah noloop
    ns "Yes! Thank you Ms. Goodwin for hiring us!"
    scene sm1fs-i003-16 ag-no-need-sirname-ns-keeps-calling-her-sirname_c1 with dissolve
    play voice5 girl27_happy_relief2 noloop
    ag "Please, Anna is fine."
    play voice4 nari_yes_aga2 noloop
    ns "Okay, Ms. Goodwin. I'm excited to be working with you."
    scene sm1fs-i003-17 cw-explains-ag-role-grimaces-anything-they-might-need_c1 with dissolve
    play voice3 girl29_thinking_hmm4 noloop
    cw "Anna is your team lead, and I'm the project lead. If you need something, you speak with her first. If it's important, it comes to me."
    cw "She'll also be in charge of most of your day-to-day operations and your daily work reviews."
    scene sm1fs-i003-16 ag-no-need-sirname-ns-keeps-calling-her-sirname_c1 with dissolve
    play voice5 girl27_yes_yap2 noloop
    ag "I'm here for anything you two might need."
    scene sm1fs-i003-18 cw-introduced-en-he-huffs-from-his-place_c1 with dissolve
    play voice3 girl29_thinking_hmm3 noloop
    cw "Over there is Mr. Eugene Nowakowski. He handles most of our behind the scenes. Our division couldn't run without him."
    play voice5 boy5_disappointed_mmf2 noloop volume 0.7
    en "Hmmph."
    scene sm1fs-i003-19 cw-no-worries-en-warms-up-nc-ask-cw-explain_c1 with dissolve
    play voice3 girl29_arrogant_he noloop
    cw "Don't worry, he warms up over time."
    play voice4 nari_surprised_huh2 noloop
    ns "What do you mean?"
    cw "He can be, let's say, difficult when you first meet him."
    scene sm1fs-i003-20 cw-introduces-am-she-wants-say-something-new-hires_c1 with dissolve
    play voice3 girl27_angry_cough1 noloop
    cw "Over there is the last member of your team."
    cw "April. Say something to the new hires."
    scene sm1fs-i003-21 am-will-wait-two-weeks-see-they-stay_c1 with dissolve
    play voice5 girl22_disappointed_geh noloop
    am "I'll say something to them after they've been around longer than two weeks."
    scene sm1fs-i003-22 ag-yells-am-flips-off-cw-ask-another-hr-trip_c1 with dissolve
    play voice5 girl3_disappointed_ehh2 noloop
    am "And as long as they're better than Aubergine Anna."
    play voice4 girl27_angry_argh4 noloop
    ag "April!"
    scene sm1fs-i003-20 cw-introduces-am-she-wants-say-something-new-hires_c1 with dissolve
    play voice3 girl29_arrogant_huh noloop
    cw "Do you need another trip to HR, Ms. Mercer?"
    play voice5 girl3_no_nah1 noloop
    am "No boss."
    cw "Don't do it again."
    scene sm1fs-i003-24 circus-over-cw-want-lead-mc-ns-meeting-room-ag-scorns-am-background_c1 with dissolve
    play voice3 girl29_happy_relief noloop
    cw "Now that the circus is over, let's get to the onboarding. Shall we?"
    play voice4 girl27_angry_err4 noloop
    ag "{size=23}You're the worst.{/size}"
    $ renpy.music.set_volume(0.2, 2.0, "sound3" )
    $ renpy.music.set_volume(0.5, 3.0, "music" )
    scene sm1fs-i003-25 cw-mc-ns-ml-meeting-room-cw-invites-them-sit-down_c1 with fade
    play voice3 girl29_yes_aga3 noloop
    cw "Please, take a seat."
    play sound sfx_cloth_rustling5
    scene sm1fs-i003-26 ppl-sit-table-cw-introduces-ml_c1 with dissolve
    play voice3 girl29_thinking_mmm1 noloop
    cw "First I'd like to introduce you to Mrs. Maureen Lindt. She's the head of the Human Resources department."
    scene sm1fs-i003-28 ml-horified-cw-frustrated-explains-cum-meaning_c1 with dissolve
    play voice5 girl9_hey_angry noloop
    ml "Pleasure to meet you both! Welcome to C.U.M.!"
    scene sm1fs-i003-27 ns-cum-not-place-ml-not-sure-what-means_c1 with dissolve
    play voice4 nari_surprised_huh1 noloop
    ns "Excuse me, I didn't think cum was a place."
    play voice5 girl9_angry_mmm noloop
    ml "I'm not sure what you mean?"
    ns "My understanding of the word is that it is primarily a derogatory word for a man's semen."
    scene sm1fs-i003-29 cw-leans-forward-expects-no-vulgarities-ns-apologizes_c1 with dissolve
    play voice3 girl27_angry_cough2 noloop
    cw "Ms. Song. C.U.M. is an acronym for Cloud User Management. While here, you may hear this name used from time to time."
    cw "But I expect while you work here, you will not speak vulgarities like that on company time."
    scene sm1fs-i003-38 ns-mc-look-presentation_c1 with dissolve
    play voice4 nari_happy_relief noloop
    ns "I'm sorry Ms. Watts. I didn't realize I was being derogatory myself."
    scene sm1fs-i003-30 ml-advice-against-use-or-meet-her-ns-likes-her-doesnt-mind_c1 with dissolve
    play voice5 girl9_angry_errr1 noloop
    ml "I'd also advise against it. Unless you want to see me more often."
    scene sm1fs-i003-32 ml-brief-behaviour-wont-tolerate-harassment_c1 with dissolve
    play voice4 nari_disappointed_huh noloop
    ns "You seem fine Mrs. Lindt. I wouldn't mind spending time with you."
    scene sm1fs-i003-33 ml-finishes-hr-brief_c1 with dissolve
    play voice5 girl9_arrogant_ha3 noloop
    ml "Why thank you Ms. Song. We should get back to the onboarding process though."
    play voice3 girl29_yes_yeah noloop
    cw "Agreed. Maureen, why don't we start with your spiel?"
    scene sm1fs-i003-34 ml-relationships-with-superiors-ask-any-questions_c1 with dissolve
    play voice5 girl9_arrogant_yeah noloop
    ml "Sure, I'll be brief. Please refrain from inappropriate comments or jokes in the office."
    ml "Sexual and verbal harassment will not be tolerated."
    scene sm1fs-i003-35 mc-ns-share-look_c1 with dissolve
    play voice5 girl9_thinking_hmm1 noloop
    ml "Lastly, if you end up in a relationship with a coworker, that's generally okay."
    ml "Unless it affects your work. Then you'll have to come and see me."
    ml "If you somehow find yourself in a relationship with your superior, you'll need to report that to me immediately."
    scene sm1fs-i003-34 ml-relationships-with-superiors-ask-any-questions_c1 with dissolve
    play voice5 girl9_thinking_hm noloop
    ml "Any questions?"
    play sound sfx_cloth_rustling2
    scene sm1fs-i003-36 cw-thanks-ml-will-start-presentation_c1 with dissolve
    play voice3 girl29_thinking_mmm2 noloop
    cw "Thank you Maureen. You both are welcome to talk to her anytime you need. Now I'll have you turn your attention to the projector..."
    $ renpy.music.set_volume(1.0, 1.5, "music" )
    scene black
    show screen scene_transistion(_("Three Hours Later..."))
    with Fade(0.3, 0.5, 0.3)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 1.5, "music" )
    scene sm1fs-i003-39 three-hours-later-mc-bored_c1
    play voice2 mc_angry_huh2 noloop
    with Fade(0.3, 0.5, 0.3)
    pause
    scene sm1fs-i003-37 cw-starts-presentation_c1
    show screen sm1fs_i003_presentation
    with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "That concludes the onboarding concerning work expectations, code of conduct, office attire, etc. Have you got any questions?"
    hide screen sm1fs_i003_presentation
    scene sm1fs-i003-38 ns-mc-look-presentation_c1
    with dissolve
    play voice4 nari_yes_emotional noloop
    ns "I do!"
    scene sm1fs-i003-40 cw-concludes-presentation-any-questions-ns-start-asking_c1 with dissolve
    play voice4 nari_thinking_emm noloop
    ns "You mentioned that the employee handbook-"
    play sound sfx_phone_buzz
    scene sm1fs-i003-41 cw-pulls-phone-gestures-wait-has-to-take_c1 with dissolve
    play voice3 girl29_surprised_oh noloop
    cw "Hang on, I need to take this."
    $ renpy.music.set_volume(0.7, 1.0, "sound3" )
    play sound sfx_door_open5
    scene sm1fs-i003-42 cw-takes-call-outside-meeting-rrom_c1 with dissolve
    play voice3 girl29_hey_happy noloop
    cw "Angela! Good afternoon."
    $ renpy.music.set_volume(0.4, 2.0, "music" )
    scene sm1fs-i003-43 mc-ns-sit-in-akward-silence_c1 with dissolve
    pause
    scene sm1fs-i003-45 mc-turns-ns-pretty-borin-ns-thought-was-great_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "That was a little boring, wasn't it?"
    scene sm1fs-i003-46 mc-not-sure-ns-explains-positives-of-rules_c1 with dissolve
    play voice4 nari_no_expressive noloop
    ns "Not at all! I thought it was great!"
    play voice2 mc_thinking_oh1 noloop
    mc "Oh..."
    ns "Rules create structures for us to thrive in. They are, at their very center, the building blocks for any progress to be made."
    scene sm1fs-i003-47 mc-guess-so-leans-back-rules-must-be-broken_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "I guess, yeah."
    mc "But rules are also meant to be broken!"
    scene sm1fs-i003-48 ns-insist-rules-good-thing-mc-agrue-fun_c1 with dissolve
    play voice4 nari_no_angry noloop
    ns "No! They shouldn't be! What's the purpose of having something if it is going to be broken?"
    play voice2 mc_happy_yay2 noloop
    mc "That's where all the fun is! Outside the rules."
    scene sm1fs-i003-49 ns-turns-mc-not-right-mct-he-upset-her_c1 with dissolve
    play voice4 nari_no_uhuh noloop
    ns "I don't think that's right."
    mct "I think I might have upset her."
    scene sm1fs-i003-50 cw-walks-back-in-meeting-room_c1 with dissolve
    play voice2 d1s5b_ehhh noloop
    mct "This is going to be rough if things go on like this."
    $ renpy.music.set_volume(0.2, 1.0, "sound3" )
    play sound sfx_door_closed6
    scene sm1fs-i003-51 cw-talk-ns-mc-lost-in-thoughts_c1 with dissolve
    mct "Fuck, I have no idea what I'm going to do about working with Nari."
    scene sm1fs-i003-52 cw-turns-mc-ask-paying-attention-he-yeah-she-doesn-want-daydream_c1 with dissolve
    play voice3 girl29_surprised_huh2 noloop
    cw "[mcname], are you paying attention?"
    scene sm1fs-i003-53 mc-insist-no-daydreaming-cw-wants-them-situated-follow-her_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Uhh, yes I am. Sorry I got a little distracted thinking about... All the rules."
    scene sm1fs-i003-52 cw-turns-mc-ask-paying-attention-he-yeah-she-doesn-want-daydream_c1 with dissolve
    play voice3 girl29_no_uhuh noloop
    cw "Uh huh. Please don't daydream about your coworkers."
    play voice2 mc_surprised_what3 noloop
    mc "I wasn't-"
    cw "Let's get you both situated at your desks, follow me."
    $ renpy.music.set_volume(0.8, 2.0, "sound3" )
    $ renpy.music.set_volume(0.7, 2.0, "music" )
    play sound sfx_door_open5
    scene sm1fs-i003-54 cw-leads-mc-ns-towards-seats_c1 with dissolve
    pause
    scene sm1fs-i003-55 cw-arives-their-desk-wants-clean-ns-starts-reciting-code_c1 with dissolve
    $ renpy.music.set_volume(0.5, 2.0, "music" )
    play voice3 girl29_yes_aga2 noloop
    cw "These are your work stations! Please keep them neat while you work here. We do have-"
    play voice4 nari_thinking_oh noloop
    ns "Under Chapter 4 \"Workplace Etiquette\", section 7, paragraph 4. \"Your workstation is not only yours, but a reflection of the company\"."
    scene sm1fs-i003-56 ns-goes-her-own-world-gang-listens_c1 with dissolve
    play voice4 nari_thinking_hmm1 noloop
    ns "At any time there may be a higher up, or client on the floor. It is important that we, as a company, maintain an appearance of professionalism."
    ns "If your team lead, or anyone above them finds your workplace to be slovenly or disheveled, you may be issued a written warning."
    ns "If it continues, you'll be sent to speak with someone in the Human Resources department."
    scene sm1fs-i003-57 cw-impressed-ns-correct-word-for-word_c1 with dissolve
    play voice3 girl29_yes_happy noloop
    cw "That is correct, word for word."
    scene sm1fs-i003-58 cw-turns-mc-perfect-partner-tells-ag-all-yours_c1 with dissolve
    play voice3 girl29_angry_hm noloop
    cw "If you have any questions, just ask Ms. Song. I think she's the perfect person to sit next to you."
    cw "They're all yours. I have some matters to attend to with the new client."
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound sfx_camera_fly1 volume 1.7
    play sound2 ["<silence 2.5>", sfx_camera_fly1] noloop volume 1.7
    scene sm1fs-i003-glambot-1 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1fs-i003-59-01 cw-walks-away-wide-shot_c1 with dissolve
    pause
    scene sm1fs-i003-60 ag-hopes-onboarding-not-too-painful-mc-was-but-still-here_c1 with dissolve
    play voice3 girl27_happy_nice1 noloop
    ag "Wonderful. Hope the onboarding hasn't been too painful!"
    play voice2 mc_arrogant_hm3 noloop
    mc "It was... I haven't left yet though!"
    scene sm1fs-i003-61 ns-not-bored-learned-so-much-about-cum-ag-good_c1 with dissolve
    play voice4 nari_happy_phew noloop
    ns "I thought it was wonderful. I've already learned so much about C.U.M., and I can't wait for more!"
    play voice3 girl27_happy_relief1 noloop
    ag "That's the spirit."
    scene sm1fs-i003-62 ag-shows-mc-ns-desks-get-comfortable-will-be-back_c1 with dissolve
    play voice3 girl27_yes_ugu2 noloop
    ag "You two get comfortable at your desks. I'm actually just about to run out and grab some lunch."
    ag "When I get back, we'll go over your work a bit more before the end of the day."
    scene sm1fs-i003-63 ns-wonderful-mc-will-be-here_c1 with dissolve
    play voice4 nari_yes_aga1 noloop
    ns "That sounds wonderful!"
    play voice2 mc_yes_okay1 noloop
    mc "We'll be here then."
    play sound sfx_chair_slide1
    scene sm1fs-i003-64 ag-walks-away-mc-sits-chair-likes-it_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "At least the chairs are comfy."
    scene sm1fs-i003-65 mc-ask-ns-what-up-to-she-want-work_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "What are you up to?"
    play voice4 nari_thinking_hm noloop
    ns "I'm at work, so I should work."
    scene sm1fs-i003-67 mct-thinks-have-break-ice-ask-ns-tell-about-herself_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What are you going to work on? We haven't been given anything to do."
    play sound sfx_keyboard_typing1
    scene sm1fs-i003-66 ns-opens-stuff-pc-mc-ask-what-work-on-nothing-yet-ns-agrees_c1 with dissolve
    play voice4 nari_disappointed_eeh noloop
    ns "I guess you're right."
    mct "God, I have to do something to break the ice. I won't be able to stand just sitting here with this awkwardness."
    scene sm1fs-i003-68 nc-excuse-not-understand-mc-sits-desk-explains-question_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "So, uh, Nari. Tell me about yourself?"
    play voice4 nari_arrogant_huh noloop
    ns "Excuse me?"
    mc "I figure if we're going to be working next to each other, we might as well learn a little something about each other."
    scene sm1fs-i003-69 ns-tells-her-name-every-thing-mc-whoah_c1 with dissolve
    play voice3 nari_arrogant_hm noloop
    ns "Okay. My name is Nari Song. I'm 5'2\". I'm South Korean. My measurements are-"
    scene sm1fs-i003-70 ns-yes-mc-mc-tells-no-need-measurements_c1 with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Woah, Nari!"
    play voice3 nari_yes_questioning noloop
    ns "Yes?"
    mc "I meant tell me where you're from, why you got a job here, stuff like that. I don't need to know your measurements."
    scene sm1fs-i003-71 ns-thought-mc-wanted-know-her-mc-not-that-literally_c1 with dissolve
    play voice4 nari_disappointed_oh noloop
    ns "Oh, I thought you wanted to know about me."
    play voice2 mc_yes_yes3 noloop
    mc "I do. Just not so much in the literal sense."
    scene sm1fs-i003-72 ns-akward-face-from-korea-did-well-school-dad-paid-education_c1 with dissolve
    play voice4 nari_thinking_mff noloop
    ns "Well I'm from South Korea. I did really well in school, especially with technology systems."
    ns "My dad paid for me to get a good education, which I did. I studied hard and graduated near the top of my class."
    ns "After school was completed, I worked at a major tech company in South Korea for a bit. I met a nice woman there, who was the daughter of the CEO."
    scene sm1fs-i003-73 ns-relaxed-was-encouraged-recommended-come-here-got-housing_c1 with dissolve
    play voice4 nari_thinking_hmm2 noloop
    ns "She encouraged me to try and find something outside of South Korea. To experience the world a bit more."
    ns "She recommended that I come to Crowning and find a job."
    ns "I applied at a few places, and Orbix was the first to respond, and even offered to house me while I was applying and starting."
    scene sm1fs-i003-74 mc-engaged-thats-great-ns-feels-lucky-has-work-hard_c1 with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow, that's great Nari."
    scene sm1fs-i003-72 ns-akward-face-from-korea-did-well-school-dad-paid-education_c1 with dissolve
    play voice4 nari_happy_relief noloop
    ns "I feel very lucky to have this opportunity. I need to work hard to ensure I do a good job and can make my father proud."
    scene sm1fs-i003-75 mc-tells-ns-father-should-be-proud-ns-tells-he-doesnt-fully-approve_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "He should be proud."
    play voice4 nari_happy_mmm noloop
    ns "He was. I... Had a prestigious job which I quit to move here. He doesn't fully approve of what I'm doing."
    mc "Well he should be. You took a risk but it looks like it's paying off."
    scene sm1fs-i003-76 mc-taken-back-ns-smiles_c1 with dissolve
    play voice4 nari_happy_laugh3 noloop
    ns "I hope it will."
    play voice2 mc_yes_yeah1 noloop
    mc "I {i}know{/i} it will."
    scene sm1fs-i003-77 ag-comes-back-ask-ready-work-ns-mc-both-ready_c1 with dissolve
    play voice3 girl27_hey_active noloop
    ag "Hey you two, are you ready to get started?"
    play voice4 nari_happy_yeah noloop
    ns "Yes!"
    play voice2 mc_yes_yes1 noloop
    mc "Ready as I'll ever be."
    play sound sfx_chair_slide1
    scene sm1fs-i003-78 ag-sits-chair-sent-work-over_c1 with dissolve
    play voice3 girl27_happy_great2 noloop
    ag "Great! I just sent you over your first work assignments."
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1fs-i003-79 mc-starts-working-nonogram_c1 with dissolve
    pause
    jump sm1fs_i003_setup_nonogram
label sm1fs_i003_setup_nonogram:
    $ nono_row_hints = []
    $ nono_col_hints = []
    $ nono_match_col = []
    $ nono_match_row = []
    $ nono_hints_max = 0
    $ grid_padding = 5
    $ nonogram_background = "sm1fs-i003-monitor-render"
    $ nonogram_end_jump = "sm1fs_i003_nonogram_result"
    $ random.seed()
    $ random_nonogram = renpy.random.choice(nonogram_puzzle_list_4x4)
    $ base64_string = random_nonogram[0]
    $ grid_cols = random_nonogram[1]
    $ grid_rows = random_nonogram[2]
    $ grid_size = grid_rows * grid_cols
    $ Nonogram.generate_hints(base64_string, grid_rows, grid_cols)
    $ nono_buttons_list = []
    $ Nonogram.generate_buttons()
    jump nonogram_game
label sm1fs_i003_nonogram_result:
    if nonogram_puzzle_solved is True:
        jump sm1fs_i003_success
    else:
        jump sm1fs_i003_fail
label sm1fs_i003_success:
    scene sm1fs-i003-80 ag-comes-over-mc-check-progress_c1 with dissolve
    pause
    scene sm1fs-i003-81 success-ag-checks-mc-work_c1 with dissolve
    play voice3 girl27_surprised_wow2 noloop
    ag "That looks good [mcname]!"
    play voice2 mc_happy_yay2 noloop
    mc "Thank you!"
    scene sm1fs-i003-82 mc-smiles-ag-she-happy_c1 with dissolve
    play voice3 girl27_thinking_hmm3 noloop
    ag "I knew you'd be a good fit here."
    jump sm1fs_i003_end
label sm1fs_i003_fail:
    scene sm1fs-i003-80 ag-comes-over-mc-check-progress_c1 with dissolve
    pause
    scene sm1fs-i003-83 quit-one-ag-checks-work-missed-something-mc-nervous-shit_c1 with dissolve
    play voice3 girl27_disappointed_oh3 noloop
    ag "[mcname], you missed a few things here."
    play voice2 mc_angry_daugh1 noloop
    mc "Shit."
    scene sm1fs-i003-84 mc-meant-crap-ag-okay-still-learning_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "I mean, shoot."
    play voice3 girl27_no_nah1 noloop
    ag "It's okay, you're learning though! Why don't you try this?"
    scene sm1fs-i003-85 ag-ask-mc-try-again-he-sure_c1 with dissolve
    play voice3 girl27_thinking_hmm5 noloop
    ag "Want to try again?"
    play voice2 mc_happy_yes1 noloop
    mc "Absolutely!"
    jump sm1fs_i003_setup_nonogram_2
label sm1fs_i003_setup_nonogram_2:
    $ mt = SMGameTime("01 Jan Mon 00 00 00")
    $ nono_row_hints = []
    $ nono_col_hints = []
    $ nono_match_col = []
    $ nono_match_row = []
    $ nono_hints_max = 0
    $ grid_padding = 5
    $ nonogram_end_jump = "sm1fs_i003_nonogram_result_2"
    $ nonogram_background = "sm1fs-i003-monitor-render"
    $ random.seed()
    $ random_nonogram = renpy.random.choice(nonogram_puzzle_list_4x4)
    $ base64_string = random_nonogram[0]
    $ grid_cols = random_nonogram[1]
    $ grid_rows = random_nonogram[2]
    $ grid_size = grid_rows * grid_cols
    $ Nonogram.generate_hints(base64_string, grid_rows, grid_cols)
    $ nono_buttons_list = []
    $ Nonogram.generate_buttons()
    jump nonogram_game
label sm1fs_i003_nonogram_result_2:
    if nonogram_puzzle_solved is True:
        jump sm1fs_i003_success
    else:
        jump sm1fs_i003_quit
label sm1fs_i003_quit:
    scene sm1fs-i003-86 quit-two-ag-checks-mc-work-again_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I'm just struggling a bit today."
    play voice3 girl27_yes_aga noloop
    ag "That's okay, there's always tomorrow. Right?"
    mc "Right!"
    jump sm1fs_i003_end
label sm1fs_i003_end:
    scene sm1fs-i003-87 end-ag-checks-ns-work-did-great-ns-thanks-ag-reminds-call-her-anna_c1 with dissolve
    play voice3 girl27_surprised_wow1 noloop
    ag "Wow, that looks great Nari!"
    play voice4 nari_happy_laugh6 noloop
    ns "Thank you Ms. Goodwin."
    play voice3 girl27_thinking_hmm noloop
    ag "Please Nari, you can call me Anna."
    scene sm1fs-i003-88 ns-has-revelation-about-anna-name_c1 with dissolve
    play voice4 nari_surprised_ehh noloop
    ns "Oh, that's what you meant earlier."
    play voice3 girl27_surprised_huh2 noloop
    ag "Huh?"
    ns "Earlier you called me Anna. I'm realizing that you meant you wanted me to call you Anna."
    scene sm1fs-i003-89 ns-thought-her-name-anna-ag-says-she-prefers-anna-ns-agrees_c1 with dissolve
    play voice3 girl27_surprised_oh2 noloop
    ag "Oh, well. Yeah. I'd prefer it if you called me Anna."
    play voice4 nari_yes_yep noloop
    ns "I can do that Ms. Good- Anna."
    scene sm1fs-i003-90 ag-smiles-wraps-first-day-ns-feeling-great-mc-positive-day_c1 with dissolve
    play voice3 girl27_happy_great1 noloop
    ag "Great. That wraps up your first day! How are you both feeling?"
    play voice4 nari_happy_yay noloop
    ns "I'm feeling great, I'm happy to have officially started."
    scene sm1fs-i003-91 ag-shows-door-thats-all-today_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "I feel like I have some more to learn, but today was a mostly good day."
    play voice3 girl27_yes_yap3 noloop
    ag "Then that's all! You can take off for the rest of the day."
    scene sm1fs-i003-92 mc-ns-leave-it-office_c1 with dissolve
    pause
    stop music fadeout 3.0
    stop sound3 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    call sm1fs_i003_job_unlocked from _call_sm1fs_i003_job_unlocked
    call sm1fs_i003_quest_line_unlock from _call_sm1fs_i003_quest_line_unlock
    call sm1fs_i003_unlock_it_location from _call_sm1fs_i003_unlock_it_location
    call sm1fs_i003_unlock_it_location_storylines from _call_sm1fs_i003_unlock_it_location_storylines
    $ StoryController.end_scene(IT_STORY_LINE, 8 if gt.curr_timeslot == TIMESLOT_4 else 10, 0, 4, IT_OFFICE, IT_SUB_ENTRANCE, IT_ENTRANCE)
    return
label sm1fs_i003_quest_line_unlock:
    $ StoryController.activate_story_line(MS, True)
    return
label sm1fs_i003_unlock_it_location:
    $ LocationController.unlock_position(IT_OFFICE, DEFAULT_SUBLOCATION, IT_OPENVIEW)
    return
label sm1fs_i003_unlock_it_location_storylines:
    $ StoryController.activate_story_line(NS_STORY, True)
    $ StoryController.activate_story_line(AG_STORY, True)
    return
label sm1fs_i003_job_unlocked:
    $ player.set_choice("IT_JOB_UNLOCKED", True)
    $ number_of_jobs = player.get_choice("NUMBER_OF_JOBS_UNLOCKED") + 1
    $ player.set_choice("NUMBER_OF_JOBS_UNLOCKED", number_of_jobs)
    return
label sm1fs_i003_unlocks:
    call sm1fs_i003_job_unlocked from _call_sm1fs_i003_job_unlocked_1
    call sm1fs_i003_unlock_it_location from _call_sm1fs_i003_unlock_it_location_1
    call sm1fs_i003_unlock_it_location_storylines from _call_sm1fs_i003_unlock_it_location_storylines_1
    if config_storyline_mode is True:
        $ execute_storyline_config(IT_STORY_LINE)
    return