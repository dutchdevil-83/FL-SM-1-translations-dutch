image sm1cs_mh003-glambot-1 = Movie(play = "images/Character-Scenes/mh/s003/anim/sm1cs-mh003-a19-2x-50fps.webm", start_image = "sm1cs-mh003-a19 sy-seductively-sitting-table-hi-mh-hey-doing-well-glambot-19-000_i", image = "sm1cs-mh003-a19 sy-seductively-sitting-table-hi-mh-hey-doing-well-glambot-19-149_i", loop = False)
label sm1cs_mh003:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    scene sm1cs-mh003-01 mc-looking-his-phone-speak-of-devil_c1 with dissolve
    play music music_vibing_chilling
    play voice2 d1s5b_ehhh noloop
    mc "Speak of the devil..."
    play voice3 stacy_surprised_huh3 noloop
    sy "Is that Lyssa!?"
    scene sm1cs-mh003-02 mc-it-is-sy-happy-tell-i-say-hi_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "It is-"
    play voice3 stacy_hey noloop
    sy "Tell her I say hi!"
    scene sm1cs-mh003-03 mc-just-text-sy-still-tell-her_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "It's just a text, Stacy."
    play voice3 stacy_yes_yap1 noloop
    sy "Still, tell her I said hi."
    play sound sfx_message_in1
    scene sm1cs-mh003-04 mc-ok-mh-has-paperwork-sy-tell-come-over_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Okaaaay. Anyway, Lyssa said that she got some of the paperwork stuff sorted out for us."
    play voice3 stacy_happy_yay2 noloop
    sy "Awesome! Tell her to come on over!"
    scene sm1cs-mh003-05 mc-mh-busy-bzzz_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Stacy, Lyssa is a busy lawyer. I doubt-"
    call buzz from _call_buzz_3
    scene sm1cs-mh003-06 mc-looks-text-mh-has-time-come-by_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well... I guess Lyssa has some free time and she offered to come by and show us what she's got."
    scene sm1cs-mh003-07 sy-excited-what-waiting-for-mc-texting-right-now_c1 with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "What are you waiting for! Tell her to come over!"
    play voice2 mc_surprised_wow2 noloop
    mc "All right, all right! Jees, I'm texting her right now."
    scene sm1cs-mh003-08 sy-checks-her-clothes_c1 with dissolve
    play voice3 stacy_surprised_oh1 noloop
    pause
    play sound sfx_heels_run2 loop
    scene sm1cs-mh003-09 sy-runs-towards-bed-mc-what-sy-put-sexy-clothes_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "What's wrong, Stacy?"
    play voice3 stacy_thinking_hm1 noloop
    sy "I need to put on my sexy clothes!"
    scene sm1cs-mh003-10 mc-you-what-sy-want-impress-mh_c1 with dissolve
    play voice2 mc_surprised_what6 noloop
    mc "Your what?"
    play voice3 stacy_arrogant_ha1 noloop
    sy "I can't wear {i}this{/i} in front of Lyssa! I want to impress her! It's hard to be sexy in your lounging clothes!"
    stop sound fadeout 2.0
    scene sm1cs-mh003-11 mc-smiles-get-that-fade-out_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "I get that."
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    scene sm1cs-mh003-12 fade-in-later-mc-goes-for-door_c1 with Fade(0.5, 0.5, 0.5)
    play sound2 sfx_doorbell_lyssa noloop
    play sound sfx_heels_steps1 loop
    pause
    scene sm1cs-mh003-13 mc-goes-open-door-tells-sy-mh-here_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Stacy, Lyssa is here!"
    play sound sfx_door_open1
    scene sm1cs-mh003-14 mc-opens-door-hey-mh-hey-too_c1 with dissolve
    play voice2 mc_hey_hello noloop
    mc "Hey, Lyssa."
    play voice4 lissa_hey noloop
    mh "Hey, [mcname]."
    scene sm1cs-mh003-15 mc-good-see-you-mh-you-too_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's good to see you."
    play voice4 lissa_ugu noloop
    mh "And you."
    scene sm1cs-mh003-16 mh-invite-mc-ofc-come-in_c1 with dissolve
    play voice4 lissa_thinking2 noloop volume 1.4
    mh "Are you going to invite me in?"
    play voice2 mc_surprised_oh3 noloop
    mc "Oh, of course. Yes, please come in."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh003-17 mc-gestures-inside-mh-jokes-lawyers-invited-mc-thought-vampires_c1 with dissolve
    play voice4 lissa_laugh2 noloop
    mh "Haven't you heard, lawyers need to be invited to come in."
    play voice2 mc_arrogant_heh1 noloop
    mc "I thought that was vampires?"
    scene sm1cs-mh003-18 mh-whats-diff-both-smile_c1 with dissolve
    play voice4 dahlia_thinking_hmm1 noloop
    mh "What's the difference?"
    play sound sfx_door_closed2
    scene sm1cs-mh003-a19 sy-seductively-sitting-table-hi-mh-hey-doing-well-glambot-19-000_i with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs_mh003-glambot-1
    pause
    play voice3 stacy_hey_attention1 noloop
    sy "Hey, how you doin'?"
    play voice4 lissa_aga noloop
    mh "Hey, Stacy. I'm doing well, and you?"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mh003-20 sy-good-as-well_c1 with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh, uh, I'm good."
    sy "I want to say thanks for helping us out with this, by the way."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh003-21 mh-ofc-had-fun-figuring-out_c1 with dissolve
    play voice4 lissa_yes noloop
    mh "Of course! I would be lying if I didn't say that I had some fun figuring this out for you."
    play sound sfx_bed_slide2 volume 0.6
    scene sm1cs-mh003-22 mh-sits-table-begin-sounds-good-mc_c1 with dissolve
    play voice4 lissa_thinking1 noloop
    mh "Shall we hop right in?"
    play voice2 mc_yes_yeah2 noloop
    mc "Sounds good to me!"
    play sound sfx_paper_rustl1
    scene sm1cs-mh003-23 mh-begins-reading-what-they-need-sy-sounds-easy_c1 with dissolve
    play voice4 lissa_ugu2 noloop
    mh "Great, so looking first into what you'll need for actors and actresses..."
    mh "First, you'll need an image release form. A consent and age confirmation form, with a copy of an ID."
    scene sm1cs-mh003-24 mh-explains-certified-std-test-results_c1 with dissolve
    play voice3 stacy_yes_fine4 noloop
    sy "That seems easy enough."
    play voice4 dahlia_disappointed_hmm1 noloop
    mh "You'll also need certified STD test results confirming everyone is clean."
    mh "You'll need clear contracts as to what the actor or actress will be doing on screen, as well as a contract agreeing to the performance in general."
    play sound sfx_hair_scratch1
    scene sm1cs-mh003-25 sy-mc-overwhelmed-wow-more-than-expected_c1 with dissolve
    play voice3 stacy_upset1 noloop
    sy "Wow..."
    play voice2 mc_arrogant_huh3 noloop
    mc "That's more than I was expecting."
    scene sm1cs-mh003-26 mh-smiles-all-forms-boiler-plate-everything-need-fill-blanks_c1 with dissolve
    play voice4 lissa_ha noloop
    mh "But, all of those forms are pretty boiler plate. I've got them all right here for you, and I can always bring more copies for you if you need."
    mh "Everything that you need to do here is \"fill in the blanks\". Names, ages, performance deals, so on."
    play sound sfx_paper_slide1
    scene sm1cs-mh003-27 sy-wow-ty-mh-mc-holy-shit-thanks-mh_c1 with dissolve
    play voice3 stacy_thinking_oh1 noloop
    sy "Wow... Thank you Lyssa! That's awesome!"
    play voice4 dahlia_yes_ugu noloop
    mh "Of course. I also included a facility in there that is willing to do volume testing and certification."
    play voice2 mc_surprised_wow3 noloop
    mc "Holy shit, Lyssa. Thank you!"
    scene sm1cs-mh003-28 mh-first-many-surprised-ask-film-here_c1 with dissolve
    play voice4 lissa_oh2 noloop
    mh "Oh, that is only the first of many surprises. I'm guessing that this is where you plan to film?"
    play voice2 mc_yes_yes1 noloop
    mc "Yep! This is the studio! Or... Will be. Still need to do a few more things to get it fully up and running."
    scene sm1cs-mh003-29 mh-ask-zoned-mc-what_c1 with dissolve
    play voice4 dahlia_thinking_hmm2 noloop
    mh "Are you zoned for mixed use?"
    play voice2 mc_surprised_what5 noloop
    mc "For... What?"
    scene sm1cs-mh003-30 mh-points-bed-this-where-live-mc-confirms_c1 with dissolve
    play voice4 dahlia_thinking_mmm1 noloop
    mh "This is where you and Stacy live, yes?"
    play voice2 mc_yes_ugu1 noloop
    mc "Yep."
    play sound sfx_cloth_rustling2
    scene sm1cs-mh003-31 live-where-work-need-zone-sy-never-thought-about-it_c1 with dissolve
    play voice4 lissa_moan1 noloop
    mh "If you want to live where you work, you need to make sure that you're zoned for it - i.e. mixed use."
    play voice3 stacy_arrogant_huh3 noloop
    sy "Huh. I never even thought about that."
    scene sm1cs-mh003-32 mc-shit-mh-pays-have-lawyer-friend_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Holy shit, Lyssa."
    play voice4 lissa_haha noloop
    mh "It pays to have a lawyer as a friend."
    scene sm1cs-mh003-33 mc-tries-talk-money-she-puts-hand-up-they-friends-least-she-can-do_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Uhh, it does. But, Lyssa, we don't-"
    play voice4 lissa_lno noloop
    mh "Please, you two are... Friends. It's the least I could do."
    scene sm1cs-mh003-34 mc-way-more-mh-fun-little-side-project_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "That's way, way more than the least you could do! It's honestly the most you could do!"
    play voice4 lissa_haha2 noloop
    mh "If I'm totally honest, this was a fun little side project for me."
    scene sm1cs-mh003-35 mc-appreciate-huge-help-sy-owe-big-time-enough-business-talk-stay-hang_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "We appreciate, seriously. This is a huge help."
    play voice3 stacy_yes_yeah2 noloop
    sy "Yeah! Thank you, Lyssa. We owe you. Big time. Now enough business talk! Stay, hang out for a bit."
    scene sm1cs-mh003-36 mh-sure-sy-awesome-want-coffee_c1 with dissolve
    play voice4 dahlia_thinking_mmm2 noloop
    mh "Sure, I've got a little bit of time before my next appointment."
    play voice3 stacy_happy_yay3 noloop
    sy "Awesome! Do you want a coffee or something?"
    scene sm1cs-mh003-37 mh-no-thanks-sy-whats-new-any-new-hotties-fondling-cock_c1 with dissolve
    play voice4 dahlia_no_simple noloop
    mh "No thank you, Stacy. I appreciate the offer though."
    play voice3 stacy_thinking_well1 noloop
    sy "Well, then what's new with you? Got any new hotties fondling that cock of yours."
    scene sm1cs-mh003-38 mh-surprised-loss-for-words_c1 with dissolve
    play voice4 lissa_moan8 noloop
    pause
    scene sm1cs-mh003-39 mc-scolds-sy-mh-all-cool-mc_c1 with dissolve
    play voice2 mc_pain_argh1 noloop
    mc "Stacy! What the hell!"
    play voice4 dahlia_disappointed_hmm2 noloop
    mh "It's fine, [mcname]. She's not the first person to be so... Blunt about my romantic life."
    scene sm1cs-mh003-40 mh-none-sy-business-sy-that-shame-super-hot_c1 with dissolve
    play voice4 dahlia_disappointed_ehh2 noloop
    mh "It may be none of your business, Stacy. But, no - I'm not seeing anyone right now."
    play voice3 stacy_angry noloop
    sy "That's a shame. You are super hot, and you deserve to have someone hot to bang."
    scene sm1cs-mh003-41 mh-thanks-compliment-sy-what-about-mc_c1 with dissolve
    play voice4 lissa_yes noloop
    mh "Thank you for the compliment. It's just not everyone's cup of tea."
    play voice3 stacy_arrogant_huh4 noloop
    sy "What about [mcname]? I thought you two had a thing going on."
    scene sm1cs-mh003-42 mc-choice-menu-screen_c1 with dissolve
    menu:
        "We did, but..."(hint="sm1cs_mh003_m01_h01"):
            call sm1cs_mh003_m01_c01 from _call_sm1cs_mh003_m01_c01
            call sm1cs_mh003_progress_storyline_choice from _call_sm1cs_mh003_progress_storyline_choice
            jump sm1cs_mh003_romance
        "I think you're mistaken"(hint="sm1cs_mh003_m01_h02"):
            jump sm1cs_mh003_no_romance
label sm1cs_mh003_romance:
    scene sm1cs-mh003-43 label-romance-mc-they-did-sy-how-fumble-that-one_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "We did, but, uhm..."
    play voice3 stacy_angry_argh2 noloop
    sy "How the hell did you fumble that, [mcname]!?"
    mc "Stacy-"
    scene sm1cs-mh003-44 sy-ask-seriously-how-mc-simple-answer-your_c1 with dissolve
    play voice3 stacy_hey_angry1 noloop
    sy "Seriously, [mcname], how!?"
    play voice4 lissa_thinking2 noloop
    mh "The simple answer, Stacy{w} - is you."
    scene sm1cs-mh003-45 sy-what-that-mean-mh-asked-mc-run-away-he-chose-sy_c1 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "What does that mean?"
    play voice4 lissa_thinking1 noloop
    mh "I asked [mcname] to run away with me. He decided to stay here with you."
    scene sm1cs-mh003-46 sy-wait-what-mh-simple-he-made-decision_c1 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Wait... What!?"
    play voice4 dahlia_yes_yeah2 noloop
    mh "Yep. Simple as that. He made his decision and..."
    scene sm1cs-mh003-47 mh-looks-upset_c1 with dissolve
    pause
    play sound sfx_cloth_rustling4
    scene sm1cs-mh003-48 mc-lyssa-mh-fine-come-terms-with-it_c1 with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "Lyssa..."
    play voice4 dahlia_old_argh2 noloop
    mh "It's fine. I've... I've come to terms with it."
    play sound sfx_skirt_off1
    scene sm1cs-mh003-49 sy-wait-moved-in-stopped-seeing-mh-more-blunt-but-yes_c1 with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "Wait, so since he decided to move in with me... You two stopped seeing each other?"
    play voice4 lissa_moan3 noloop
    mh "A little bit more blunt than I'd put it, but yes."
    scene sm1cs-mh003-50 sy-you-bombshell-mc-be-lucky-okay-sharing-mh-what_c1 with dissolve
    play voice3 stacy_arrogant_huh5 noloop
    sy "That's... Ridiculous.{w} You're a bombshell. [mcname] should feel lucky to know you. And I am totally okay sharing him with you."
    play voice4 dahlia_surprised_ah2 noloop
    mh "What?"
    scene sm1cs-mh003-51 sy-if-you-want-see-mc-cool-mh-uuuhm-okay_c1 with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "If you want to keep seeing [mcname], I'm totally cool with that."
    play voice4 lissa_oh2 noloop
    mh "I, uhm, okay."
    scene sm1cs-mh003-52 sy-ask-okay-mh-thinks-about-it_c1 with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "Okay?"
    play voice4 dahlia_thinking_hmm3 noloop
    mh "I'm..."
    scene sm1cs-mh003-53 mh-thinks-open-mc-pursue-mc-really_c1 with dissolve
    play voice4 lissa_shyoh noloop
    mh "I think, I would be open to you trying to pursue me."
    play voice2 mc_angry_really noloop
    mc "Really!?"
    scene sm1cs-mh003-54 mh-will-work-for-it-mc-huh_c1 with dissolve
    play voice4 dahlia_thinking_hmm2 noloop
    mh "But you're going to have to work for it."
    play voice2 mc_surprised_huh6 noloop
    mc "Huh?"
    scene sm1cs-mh003-55 last-time-relatioship-was-chaotic_c1 with dissolve
    play voice4 dahlia_disappointed_ehh3 noloop
    mh "Last time our relationship started... Chaotically. This time, I want you to put in the leg work. I want you to take me on dates, wine and dine me."
    play sound sfx_skirt_off3
    scene sm1cs-mh003-56 mh-stands-want-show-mc-means-it-mc-ofc-absolutely_c1 with dissolve
    play voice4 dahlia_disappointed_hmm1 noloop
    mh "I want you to show me that you mean it. That you {i}want{/i} a relationship with me."
    play voice2 mc_happy_yes1 noloop
    mc "Of course! Yes! Absolutely"
    scene sm1cs-mh003-57 sy-proud-look-that-being-matchmaker-mc-something-like-that_c1 with dissolve
    play voice3 stacy_laugh4 noloop
    sy "Look at that! Just out here being a matchmaker."
    play voice2 mc_arrogant_heh3 noloop
    mc "Something like that."
    scene sm1cs-mh003-58 mh-looking-forwards-first-date-mc-also_c1 with dissolve
    play voice4 dahlia_thinking_hmm1 noloop
    mh "Well, I look forward to hearing from you about our first date."
    play voice2 mc_yes_yeah4 noloop
    mc "I look forward to it too."
    jump sm1cs_mh003_business
label sm1cs_mh003_no_romance:
    scene sm1cs-mh003-59 mc-thinks-sy-confused-mh-okay_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Uhhh, Stacy - I think you're a little confused."
    play voice4 dahlia_no_nah noloop
    mh "It's okay, [mcname]. You've been with your fair share of women. I'm honestly surprised you manage to keep them all straight if I'm perfectly honest."
    scene sm1cs-mh003-60 mh-no-confusion-strictly-platonic-relationship_c1 with dissolve
    play voice4 dahlia_thinking_hmm4 noloop
    mh "Stacy, so there's no confusion at all - [mcname] and I have a strictly platonic relationship. Which seems to be turning into a professional one as we speak."
    jump sm1cs_mh003_business
label sm1cs_mh003_business:
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh003-61 label-business-mh-walks-towards-door-would-encourage-both-read-docs_c1 with dissolve
    play voice4 lissa_mmm1 noloop
    mh "I would encourage you both to look through those documents. If you have any questions, please feel free to text or call me."
    mh "And I will let you know if anything changes with your zoning, and you get the actual all clear to open a business in here."
    stop sound fadeout 1.0
    scene sm1cs-mh003-62 mh-will-let-know-if-anything-changes-mc-ask-if-not_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "And what if it doesn't?"
    scene sm1cs-mh003-63 mh-will-make-happen-no-worry_c1 with dissolve
    play voice4 lissa_lno noloop
    mh "We'll make it happen, don't worry."
    scene sm1cs-mh003-64 sy-steps-forward-wanted-thank-again-mh-will-stop-by_c1 with dissolve
    play voice3 stacy_hey_happy1 noloop
    sy "I wanted to say thanks again, Lyssa! And seriously, feel free to stop by anytime."
    scene sm1cs-mh003-65 mh-gives-sinister-smile_c1 with dissolve
    play voice4 lissa_laugh2 noloop
    mh "Oh, I will. Now that you've invited me in, nothing can stop me."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh003-66 mh-leaves-apartment_c1 with dissolve
    pause
    play sound sfx_door_closed7
    scene sm1cs-mh003-67 sy-chuckles-thinks-funny-mc-two-deserve-each-other_c1 with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "What, I think she's funny."
    play voice2 mc_angry_off noloop
    mc "You two weirdos deserve each other."
    scene sm1cs-mh003-68 sy-glad-think-so_c1 with dissolve
    play voice3 stacy_happy_wooh1 noloop
    sy "I'm glad you think so!"
    if not player.get_choice("date_mh"):
        scene sm1cs-mh003-69 sy-really-good-mc-agree_c1 with dissolve
        play voice3 stacy_happy_hmm1 noloop
        sy "That was really good though. It feels like we're making some real progress on getting the studio off the ground!"
        play voice2 d9s2_yeah noloop volume 1.7
        mc "I agree. I think we're finally making some things happen."
        scene sm1cs-mh003-70 sy-me-too-get-out-find-actresses-mc-aye-aye-cap_c1 with dissolve
        play voice3 stacy_yes_fine2 noloop
        sy "Me too, now get out there and find us some more actresses!"
        play voice2 mc_yes_yes7 noloop
        mc "Aye, aye, captain!"
        jump sm1cs_mh003_exit
    else:
        jump sm1cs_mh003_stacy
label sm1cs_mh003_stacy:
    queue voice3 stacy_thinking_emm4 noloop
    scene sm1cs-mh003-71 sy-speaking-of-mc-what_c1 with dissolve
    sy "Speaking of..."
    play voice2 mc_surprised_uh2 noloop
    mc "What?"
    scene sm1cs-mh003-72 sy-tries-find-words-mc-cat-ate-tongue_c1 with dissolve
    play voice3 stacy_upset1 noloop
    sy "I... Uhm..."
    play voice2 mc_thinking_hmm4 noloop
    mc "What, cat got your tongue? I've never known you to be tongue tied, Stacy."
    scene sm1cs-mh003-73 sy-flustered-shut-up-mc-make-me_c1 with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "Shut up!"
    play voice2 mc_arrogant_hm1 noloop
    mc "Make me."
    scene sm1cs-mh003-74 sy-irritated-will-make-him-want-ask-something-else-mc-say-it_c1 with dissolve
    play voice3 stacy_angry_argh4 noloop
    sy "I swear to God, I will - That's not the point! I wanted to say something else."
    play voice2 mc_yes_yeah7 noloop
    mc "Well come on then, say it."
    scene sm1cs-mh003-75 sy-ask-about-three-mc-confused-what-do-mean_c1 with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "How would you feel about, maybe, you, and Lyssa, and me..."
    play voice2 d1s2_hmm noloop volume 1.3
    mc "What do you mean?"
    scene sm1cs-mh003-76 sy-not-that-stupid-throuple-mc-ask-want-fuck-together-sy-sure-if-reduce-that_c1 with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "Come on. You can't be {i}that{/i} dense. Seriously. I have the hots for Lyssa, you like Lyssa, what if we had our moments of, you know, throupling."
    play voice2 mc_thinking_oh1 noloop
    mc "Are you asking me if the three of us can fuck sometimes?"
    play voice3 stacy_yes_yeah1 noloop
    sy "Sure, if you want to reduce it to that. Then, yeah."
    scene sm1cs-mh003-77 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Sure, I wouldn't be opposed to that"(hint="sm1cs_mh003_m02_h01"):
            call sm1cs_mh003_m02_c01 from _call_sm1cs_mh003_m02_c01
            scene sm1cs-mh003-78 choice-sure-mc-open-to-it-sy-excited_c1 with dissolve
            play voice2 mc_yes_sure1 noloop
            mc "I mean, I don't get the final say here, but I would be open to that."
            play voice3 stacy_yay noloop
            sy "Yay! I was hoping you'd say that."
        "I don't think I'd be cool with that"(hint="sm1cs_mh003_m02_h02"):
            scene sm1cs-mh003-79 choice-not-cool-mc-no-game-sy-disapointed_c1 with dissolve
            play voice2 mc_no_nah2 noloop
            mc "I don't think I'm game for that. And I don't think Lyssa would be crazy about that..."
            play voice3 stacy_disappointed_oh4 noloop
            sy "You got a good point there."
            scene sm1cs-mh003-80 sy-step-towards-mc-either-way-need-actresses-need-talent-mc-on-it_c1 with dissolve
            play voice3 stacy_thinking_hmm1 noloop
            sy "Either way, we need to go out and find some more actresses! We've got the paperwork, now we need the talent!"
            play voice2 mc_yes_yes7 noloop
            mc "Yes, ma'am. I'm on it."
    play sound sfx_heels_steps2 loop
    scene sm1cs-mh003-81 mc-heads-towards-exit-end-scene_c1 with dissolve
    pause
    jump sm1cs_mh003_exit
label sm1cs_mh003_exit:
    stop sound fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    call sm1cs_mh003_activate_kv_story from _call_sm1cs_mh003_activate_kv_story
    call sm1cs_mh003_unlock_lyssa_house from _call_sm1cs_mh003_unlock_lyssa_house
    $ StoryController.end_scene(MH_STORY, 2, 0, 2)
    return
label sm1cs_mh003_unlock_lyssa_house:
    $ player.discover_map_location(LYSSAS_HOUSE)
    return
label sm1cs_mh003_activate_kv_story:
    $ QuestController.resolve_quest("Q-KV004")
    return
label sm1cs_mh003_m01_c01:
    $ player.set_choice("date_mh")
    return
label sm1cs_mh003_progress_storyline_choice:
    $ player.progress_storyline(MH_STORY, 1)
    return
label sm1cs_mh003_m02_c01:
    $ player.set_choice("sm1cs_mh003_thruple")
    return
label sm1cs_mh003_unlocks:
    call sm1cs_mh003_m01_c01 from _call_sm1cs_mh003_m01_c01_1
    call sm1cs_mh003_m02_c01 from _call_sm1cs_mh003_m02_c01_1
    call sm1cs_mh003_unlock_lyssa_house from _call_sm1cs_mh003_unlock_lyssa_house_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MH_STORY)
    return