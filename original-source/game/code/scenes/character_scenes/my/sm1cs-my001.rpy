image sm1cs_my001-glambot-1 = Movie(play = "images/Character-Scenes/MY/s001/anim/sm1cs-my001-a87-2x-50fps.webm", start_image = "sm1cs-my001-a87 mc-what-fav-thing-my-that-tough-glambot-000_i", image = "sm1cs-my001-a87 mc-what-fav-thing-my-that-tough-glambot-198_i", loop = False)
label sm1cs_my001:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 0.5, "music2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.play(audio.music_toomuchwork_relax, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_toomuchwork_relax_radio, "music2", True, None, True, 0.0)
    scene sm1cs-my001-01 mc-standing-front-mirror-checking-clothes_c1 with dissolve
    play sound sfx_cloth_rustling1
    pause
    play sound sfx_heels_steps2 loop
    scene sm1cs-my001-02 sy-approach-mc-what-do-think-sy-oo-lala_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "So, what do ya' think?"
    play voice3 stacy_surprised_oh1 noloop
    sy "Oooo la la! Someone is getting all fancy."
    stop sound fadeout 1.0
    scene sm1cs-my001-03 mc-uhu-has-hot-date-sy-yeah-who_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Uh huh. I got myself a hot date tonight."
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh yeah? With who?"
    scene sm1cs-my001-04 mc-tells-date-with-melony_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    if persistent.is_special:
        mc "Mom."
    else:
        mc "Melony."
    scene sm1cs-my001-05 sy-surprised-real-date-mc-taking-her-dinner_c1 with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "Like, a real bona fide date?"
    play voice2 mc_thinking_hmm2 noloop
    mc "Well, I'm taking her to dinner to thank her for her help with the renovation."
    play sound sfx_metal_fence2
    scene sm1cs-my001-06 sy-oh-mc-what_c1 with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Oooooooh."
    play voice2 mc_arrogant_huh1 noloop
    mc "What?"
    scene sm1cs-my001-07 sy-she-not-know-date-mc-but-thanking-her_c1 with dissolve
    play voice3 stacy_no_nah2 noloop
    sy "She doesn't {i}know{/i} it's a date."
    play voice2 mc_hey_hey8 noloop
    mc "But I'm taking her out!"
    scene sm1cs-my001-08 sy-yeah-explains-situation-sarcastic_c1 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    if persistent.is_special:
        sy "Yeah, her son is taking her to dinner for being a good mom. That's all she thinks it is."
    else:
        sy "Yeah, her friend's kid is taking her out to dinner to say thanks for painting the wall. That's all she thinks it is."
    scene sm1cs-my001-09 mc-well-put-this-way_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well, when you put it that way..."
    play sound sfx_heels_steps2 loop
    scene sm1cs-my001-10 sy-smirks-walks-away-just-have-use-charm-mc-wtf-mc-charm_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "You'll just have to use the ol' [mcname] charm on her to show her it's a {i}date{/i} date."
    play voice2 mc_surprised_what1 noloop
    mc "What the hell is the \"[mcname] charm\"?"
    play sound2 sfx_heels_steps1
    scene sm1cs-my001-11 sy-no-idea-be-yourself-mc-thanks_c1 with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "No clue. But it seems to work with pretty much everyone, so just be you tonight and everything will work out."
    play voice2 d1s5b_ehhh noloop volume 2.0
    if persistent.is_special:
        mc "Thanks for the pep talk, sis."
    else:
        mc "Thanks for the pep talk, Stacy."
    play voice3 stacy_angry noloop
    play sound sfx_leg_kick5
    stop sound2 fadeout 1.0
    scene sm1cs-my001-12 sy-punch-mc-chest-that-swhat-here-for_c1 with hpunch
    sy "That's what I'm here for!"
    scene sm1cs-my001-13 sy-puts-hands-pants-cant-believe-actually-asked-her-out_c1 with dissolve
    play voice3 stacy_angry_argh3 noloop
    sy "I just can't believe you actually asked her out."
    play sound sfx_skirt_off2
    scene sm1cs-my001-14 mc-surprsied-this-your-idea-sy-yeah-didnt-think-you-do-it_c1 with dissolve
    play voice2 mc_surprised_why4 noloop
    mc "Why!? This was your idea!"
    scene sm1cs-my001-15 mc-why-not-sy-dont-know-support-fact_c1 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Yeah, but I didn't think you'd do it."
    play sound sfx_hair_scratch1 volume 1.5
    scene sm1cs-my001-16 mc-silent-why-naked_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Why not?"
    play sound sfx_cloth_rustling2
    scene sm1cs-my001-17 sy-going-shower-mc-ask-couldnt-get-bathroom_c1 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "I don't know. But I support the fact that you're going for it!"
    play voice2 mc_thinking_mmm6 noloop
    mc "Well... I have to keep you guessing!"
    mc "..."
    mc "Why are you naked?"
    play sound sfx_barefoot_steps1 loop
    scene sm1cs-my001-18 sy-didnt-want-get-panties-wet-mc-huh-wet_c1 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "I'm going to take a shower."
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh... and why didn't you just wait to get into the bathroom?"
    scene sm1cs-my001-19 sy-explains-because-got-horny_c1 with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "I didn't want to get my panties wet."
    play voice2 mc_surprised_uh1 noloop
    mc "Wet... but... huh?"
    play sound sfx_throw_something1
    scene sm1cs-my001-20 sy-goes-bathroom-enjoy-date_c1 with dissolve
    play voice3 stacy_pain_mmm2 noloop
    if persistent.is_special:
        sy "The thought of you fucking Mom really turned me on. So I'm going to rub one out picturing that."
    else:
        sy "The thought of you fucking Melony really turned me on. So I'm going to rub one out picturing that."
    sy "Enjoy your date!"
    scene sm1cs-my001-21 mc-looking-below-ofc-she-just-tease_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Of course. She just has to tease me when I'm already nervous about my not date, date tonight."
    play sound sfx_heels_steps2 loop
    scene sm1cs-my001-22 mc-walks-downstairs_c1 with dissolve
    play voice2 mc_angry_errr3 noloop
    mct "And now I have to go to the restaurant with half of an erection..."
    scene sm1cs-my001-23 mc-leaving-studio_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.0, 3.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    play sound2 sfx_door_openclosed1 noloop
    play sound4 sfx_cafe_crowd fadein 2.0
    scene sm1cs-my001-24 mc-arrives-restaurant-thinking-five-min-early_c1 with Fade(0.5, 1.0, 0.5)
    play voice2 d1s5_mcthinks noloop volume 1.6
    mct "All right, 5 minutes early. I should have beat her here..."
    stop sound fadeout 1.0
    scene sm1cs-my001-25 waiter-asks-mc-hello-table-one-mc-two-actually_c1 with dissolve
    play voice4 boy9_hey_easy noloop
    "Waiter" "Good evening, sir. Table for one?"
    play voice2 mc_thinking_hm noloop
    mc "Two, actually. My date will be joining me shortly."
    scene sm1cs-my001-26 waiter-ofc-this-way-sire_c1 with dissolve
    play voice4 boy9_yes_aga1 noloop
    "Waiter" "Of course, sir. Right this way, then."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_bed_slide2 noloop
    scene sm1cs-my001-27 waiter-leads-mc-table-here-you-are-mc-thank-you_c1 with dissolve
    play voice4 boy9_yes_yep2 noloop
    "Waiter" "And here you are, sir."
    play sound sfx_cloth_rustling4
    scene sm1cs-my001-28 waiter-ofc-will-bring-menus_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thank you."
    play voice4 boy9_thinking_emm3 noloop
    "Waiter" "Of course. I will bring you some menus."
    play sound sfx_heels_steps2 loop
    scene sm1cs-my001-29 waiter-leaves-mct-okay-need-be-usual-cahrming-self_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.6
    mct "Okay... I just need to be my usual, charming self... no need to overthink, or stress. Just do the date, [mcname]..."
    stop sound fadeout 2.5
    scene sm1cs-my001-30 mct-not-like-dating-mom-or-something_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    if persistent.is_special:
        mct "It's not like you're trying to seduce your Mom or anything..."
    else:
        mct "It's not like you're trying to seduce one of your parent's friends or anything..."
    scene sm1cs-my001-31 mc-sees-my-walking-in-oh-shit_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Oh shit..."
    play sound sfx_heels_steps1 loop
    scene sm1cs-my001-32 my-enters-stage-sexy-as-fuck_c1 with dissolve
    play voice2 d1s5_orgasm noloop volume 1.4
    if persistent.is_special:
        mct "Goddamn, Mom is hot..."
    else:
        mct "Goddamn, Melony is hot..."
    scene sm1cs-my001-33 my-hey-mc-mc-hey_c1 with dissolve
    play voice3 girl34_hey_simple4 noloop
    my "[mcname]!"
    play voice2 mc_hey_hey10 noloop
    mc "Hey!"
    play sound sfx_bed_slide2
    play sound2 sfx_cloth_rustling3 noloop
    scene sm1cs-my001-34 my-wow-quite-spot-mc-responds-based-taboo_c1 with dissolve
    play voice3 girl34_surprised_wow2 noloop
    my "Wow, you've picked quite the spot for dinner."
    play voice2 mc_thinking_mmm2 noloop
    if persistent.is_special:
        mc "What can I say? I got my taste of restaurants from my mother."
    else:
        mc "What can I say? I got my taste of restaurants from a woman with a great palette."
    scene sm1cs-my001-35 my-little-tongued-devil_c1 with dissolve
    play voice3 girl34_disappointed_oh2 noloop
    my "Oh, you little silver tongued devil."
    scene sm1cs-my001-36 mc-oh-allow-me_c1 with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Oh, allow me."
    play sound sfx_bed_slide3 volume 0.7
    scene sm1cs-my001-37 mc-pulls-chair-my-sits-m-really-wnet-exra-mile-mc-want-show-much-appriciate_c1 with dissolve
    play voice3 girl34_arrogant_huh1 noloop
    my "My, my. Really going the extra mile tonight, aren't we?"
    play voice2 d2s9_confused noloop volume 1.6
    mc "Well, I just, uhm, really want to show you how much I appreciate you."
    play sound sfx_heels_steps2
    scene sm1cs-my001-38 my-well-tank-you-treated-non-business-dinner_c1 with dissolve
    play voice3 girl34_happy_relief4 noloop
    my "Well, thank you, [mcname]. It's been a long time since anyone has treated me to any sort of dinner."
    my "Well, at least treated me to a non-business dinner."
    play sound sfx_cloth_rustling4
    scene sm1cs-my001-39 mc-hard-believe-look-you_c1 with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "That's hard to believe. I mean, look at you!"
    scene sm1cs-my001-40 my-what-looking-at-mc-look-absoleutly-stunning_c1 with dissolve
    play voice3 girl34_disappointed_oh1 noloop
    my "Oh? And what am I looking at?"
    play voice2 mc_disappointed_ah2 noloop
    if persistent.is_special:
        mc "Well, you look absolutely stunning tonight, Mom."
    else:
        mc "Well, you look absolutely stunning tonight, Melony."
    scene sm1cs-my001-41 my-laying-thing-hun-mc-i-erm_c1 with dissolve
    play voice3 girl34_disappointed_eeh2 noloop
    my "Laying it on a little thick tonight, honey?"
    play voice2 d1s5b_emmm noloop
    mc "I, erm-"
    play sound2 sfx_heels_steps2 noloop
    scene sm1cs-my001-42 waiter-your-menus_c1 with dissolve
    play sound sfx_paper_rustl3
    play voice4 boy9_hey_simple2 noloop
    "Waiter" "Your menus."
    play voice2 mc_angry_huh2 noloop
    mct "Oh, thank God."
    scene sm1cs-my001-43 my-glass-red-wine-mc-same_c1 with dissolve
    play voice4 boy9_arrogant_huh2 noloop
    "Waiter" "Can I start you off with anything to drink?"
    play voice3 girl34_disappointed_mmf3 noloop
    my "Mmmmm, I'll take a glass of the hosue red."
    play voice2 d9s2_yeah noloop volume 1.76
    mc "And I'll do the same."
    scene sm1cs-my001-44 waiter-good-choice_c1 with dissolve
    play voice4 boy9_happy_great4 noloop
    "Waiter" "Excellent choice. I'll have those right out for you."
    $ renpy.music.set_volume(0.2, 15.5, "music" )
    $ renpy.music.set_volume(0.5, 15.0, "music2" )
    play sound sfx_cloth_rustling2
    scene sm1cs-my001-45 my-looks-mc-wine-drinker-now-mc-got-that-from-you_c1 with dissolve
    play voice3 girl34_arrogant_ha3 noloop
    my "A wine drinker now?"
    play voice2 mc_yes_yeah7 noloop
    if persistent.is_special:
        mc "Well... I also got that from you?"
    else:
        mc "Well... I got that from watching you?"
    scene sm1cs-my001-46 my-compliment-after-compliment-mct-uh-oh_c1 with dissolve
    play voice3 girl34_disappointed_eem4 noloop
    my "Compliment after compliment... if I didn't know any better, I'd say this was a date."
    mct "Uh oh."
    scene sm1cs-my001-47 my-leans-back-or-did-something-naughty-mc-no-no-no-trouble_c1 with dissolve
    play voice3 girl34_disappointed_oof1 noloop
    my "Or that you did something naughty and you're in trouble now."
    scene sm1cs-my001-48 my-good-even-lifestyle-mc-what-youmean_c1 with dissolve
    play voice2 d9s2_mmno noloop volume 2.3
    mc "No, no. Definitely not in trouble."
    play voice3 girl34_thinking_hmm7 noloop
    my "Good. Even though your new lifestyle will probably invite whole heaps of trouble."
    mc "What do you mean?"
    scene sm1cs-my001-49 my-leans-forward-used-have-friend-empire-began-unravel_c1 with dissolve
    play voice3 girl34_thinking_eeh1 noloop
    my "I used to have this... friend. Now, he wasn't exactly working in the adult entertainment industry, but close. Lots of nude models in his studio, lots of partying..."
    my "But this little empire of industry he had started to build began to unravel. Problems with his love life, half baked ideas for making money..."
    scene sm1cs-my001-50 my-models-personal-lives-whole-thing-failed_c1 with dissolve
    play voice3 girl34_disappointed_oof2 noloop
    my "The models own personal lives becoming intwined with his work and the studio..."
    my "The whole thing failed before it really even got a chance to be successful. That chaos just seems to be a part of the industry."
    scene sm1cs-my001-51 mc-serious-things-diff-my-god-hope-so_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "But I think w- I'm doing something different. There's a real plan, and professionals involved, and I think I'm going to be successful with the porn studio."
    scene sm1cs-my001-50 my-models-personal-lives-whole-thing-failed_c1 with dissolve
    play voice3 girl34_disappointed_mmf4 noloop
    my "{size=*0.6}God, I hope so...{/size}"
    scene sm1cs-my001-52 mc-man-not-sure-how-longer-convince_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "Man, I don't know how much longer I can go trying to convince her that the studio is going to work..."
    play sound2 sfx_heels_steps2 noloop
    play sound sfx_cup_slide1 volume 2.0
    scene sm1cs-my001-53 waiter-brings-wine-ask-like-apetizers-straight-course-my-havent-even-looked-menu_c1 with dissolve
    play voice4 boy9_yes_aga2 noloop
    "Waiter" "Your wine. Would you like to begin tonight with any appetizers? Or straight to the main course."
    play voice3 girl34_disappointed_oh3 noloop
    my "Oh, you'll have to forgive me. I haven't even had a chance to look at the menu."
    scene sm1cs-my001-54 mc-ask-have-oyster-waiter-indeed-do_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Do you happen to have oysters?"
    play voice4 boy9_yes_happy3 noloop
    "Waiter" "We do indeed, sir."
    scene sm1cs-my001-55 mc-then-two-linguini-pastas-after-waiter-both-wonderful-choices_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "How about an order of those to start. And then we'll each have an order of the pasta linguini."
    play voice4 boy9_happy_nice1 noloop
    "Waiter" "Both wonderful choices, sit."
    play sound2 sfx_heels_steps2 noloop
    scene sm1cs-my001-56 waiter-goes-away_c1 with dissolve
    stop sound2 fadeout 4.0
    pause
    scene sm1cs-my001-57 my-wow-cant-believe-remember-mct-damn-picked-at-random-luck_c1 with dissolve
    play voice3 girl34_surprised_wow4 noloop
    my "Wow, I can't believe you remembered my favorite Italian dish, [mcname]."
    mct "Damn, I only picked that because the reviews said it was their best dish. What luck is that!"
    scene sm1cs-my001-58 mc-tries-play-it-cool-uh-huh_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Uh huh!"
    scene sm1cs-my001-59 my-suspicious-didnt-remember-right-mc-uhm_c1 with dissolve
    play voice3 girl34_thinking_emm1 noloop
    my "You didn't know that was my favorite pasta dish, did you?"
    play voice2 d2s12_emmm noloop
    mc "Uhm..."
    scene sm1cs-my001-60 my-smiles-only-you-luck-into-something-like-that_c1 with dissolve
    play voice3 girl34_happy_laugh2 noloop
    my "Hahaha! Only you could luck into something like that."
    play sound sfx_cloth_rustling1
    scene sm1cs-my001-61 mc-so-like-time-crowning-my-good_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "So, how are you enjoying your time in Crowning?"
    scene sm1cs-my001-62 my-reaching-glass-extended-leave-office-mc-oh-really_c1 with dissolve
    play voice3 girl34_yes_yeah8 noloop
    my "It's good! It's been fun to go and see some of my old haunts."
    play sound sfx_drink_loop1 volume 2.0
    scene sm1cs-my001-63 my-takes-sip-wine_c1 with dissolve
    pause
    play sound sfx_cup_place1 volume 1.5
    scene sm1cs-my001-64 my-love-this-place-but-be-nice-out-of-hotel_c1 with dissolve
    play voice3 girl34_thinking_hmm6 noloop
    my "In fact, I just extended my out of office for a while longer. I'm not quite yet ready to leave Crowning yet."
    scene sm1cs-my001-65 mc-something-wrong-my-no-no_c1 with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Oh really?"
    play voice3 girl34_yes_ugu2 noloop
    my "Mmmhmmm. There's just something about this place... I love it here."
    scene sm1cs-my001-66 my-erase-personality-art-corporate-garbage_c1 with dissolve
    play voice3 girl34_disappointed_eeh4 noloop
    my "But I would love to get out of that hotel."
    play voice2 mc_surprised_why3 noloop
    mc "Something wrong with it?"
    scene sm1cs-my001-67 just-rich-garbage-they-peddle-filth_c1 with dissolve
    play voice3 girl34_no_nonono3 noloop
    my "No, no. Nothing like that. I've just always found hotels... sterile. There's no life in them."
    my "The erase the personality so you can fill it with whatever you can fit into a suitcase."
    scene sm1cs-my001-66 my-erase-personality-art-corporate-garbage_c1 with dissolve
    play voice3 girl34_disappointed_ehh2 noloop
    my "The art is all some crap corporate garbage, the walls always ultra clean canvases, with fake marble and granite..."
    my "Just a bunch of rich people garbage to make you feel like it's a luxe stay, when in reality the designer is tasteless and couldn't hack it in the art world."
    my "So they peddle this filth on every unsuspecting visitor who is too jet lagged to care, or experiencing too much of the vibrant life of wherever they are to notice."
    play sound sfx_cloth_rustling2
    scene sm1cs-my001-68 my-shocked-omg-totally-ranting-mc-totally-fine_c1 with dissolve
    play voice3 girl34_pain_ou3 noloop
    my "Oh my God, I am so sorry for ranting at you [mcname]!"
    scene sm1cs-my001-70 mc-seriously-ok-actually-odd-way-nice_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    if persistent.is_special:
        mc "It's totally fine, Mom!"
    else:
        mc "It's totally fine, Melony!"
    mc "I didn't realize you had such a high opinion of hotels."
    play voice3 girl34_angry_hmf noloop
    my "God, I am usually so much better at keeping that in."
    mc "It's seriously okay. It was actually, in an odd way, kind of nice to hear?"
    play sound sfx_throw_something1
    scene sm1cs-my001-71 my-raise-eyebrow-presence-another-hotel-revolutionary-mc-laughs-haha-no_c1 with dissolve
    play voice3 girl34_surprised_oh3 noloop
    my "Oh? Am I in the presence of another hotel revolutionary? A comrade in arms willing to become saboteur against the influx of snobby hotels?"
    scene sm1cs-my001-69 mc-smiling-didnt-realize-such-opinion-hotels-my-god-usually-better_c1 with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.6
    mc "Hahahaha! No, nothing like that."
    scene sm1cs-my001-72 my-then-we-enemies-mc-no-actually-not-really-travelled-enough_c1 with dissolve
    play voice3 girl34_angry_ahem1 noloop
    my "Then we are enemies!"
    scene sm1cs-my001-70 mc-seriously-ok-actually-odd-way-nice_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "No, I've actually not really travelled enough to have developed such an intense belief about hotel rooms."
    scene sm1cs-my001-73 my-sad-mc-what-said-my-shouldve-brought-you-more-business-trips_c1 with dissolve
    play voice3 girl34_disappointed_mmf1 noloop
    pause
    play voice2 mc_surprised_wow1 noloop
    mc "Woah, what'd I say?"
    play voice3 girl34_disappointed_eem3 noloop
    my "I should've brought you with me on more of my business trips. You deserved to experience more pockets of the world."
    play sound sfx_cloth_rustling3
    scene sm1cs-my001-74 mc-like-childhood-reaches-my-hand-seriously-very-happy_c1 with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Hey, I liked the way I grew up!"
    mc "Seriously, I am very happy with how things were back then. You don't need to do this to yourself."
    scene sm1cs-my001-75 my-small-smile-thank-you-mc-ofcourse_c1 with dissolve
    play voice3 girl34_happy_relief2 noloop
    my "Thank you, [mcname]."
    play voice2 mc_yes_sure1 noloop
    if persistent.is_special:
        mc "Of course, Mom."
    else:
        mc "Of course, Melony."
    play sound sfx_heels_steps2
    scene sm1cs-my001-76 waiter-brings-oysters_c1 with dissolve
    play voice4 boy9_thinking_hmm1 noloop
    "Waiter" "Sir, ma'am, your oysters."
    play sound sfx_plate_place1
    scene sm1cs-my001-77 waiter-here-oysters-pasta-soon_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Thank you!"
    play voice4 boy9_yes_aga3 noloop
    "Waiter" "And your linguini is soon to follow. Enjoy."
    play sound2 sfx_heels_steps2
    scene sm1cs-my001-78 waiter-walks-away-my-cant-remember-last-time-mc-me-neither_c1 with dissolve
    play voice3 girl34_happy_mmm1 noloop
    my "Mmmm... I can't even remember the last time I had oysters."
    play voice2 mc_yes_yeah1 noloop
    mc "Neither can I."
    stop sound2 fadeout 2.5
    play sound sfx_cloth_rustling1
    scene sm1cs-my001-79 my-picks-up-oyster-you-know-they-afrodisiac_c1 with dissolve
    play voice3 girl34_arrogant_laugh1 noloop
    my "You know, they say that oysters are an aphrodisiac."
    scene sm1cs-my001-81 mc-nervous-huh_c1 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Uh oh. I thought I was being subtle!"
    scene sm1cs-my001-80 mct-huh-thought-subtle-my-this-why-dont-believe-havent-had-recently_c1 with dissolve
    play voice3 girl34_arrogant_yeah noloop
    my "Which is why I don't believe for a second that you haven't had oysters recently."
    play voice2 mc_surprised_uh2 noloop
    mc "Huh?"
    scene sm1cs-my001-82 my-smirks-we-both-adults-dont-open-adult-entertainment-withouth-game_c1 with dissolve
    play voice3 girl34_disappointed_oh2 noloop
    my "Oh, we're both adults here, [mcname]. And maybe it's the wine talking a bit..."
    scene sm1cs-my001-83 my-judging-what-read-fl-wooed-more-than-fair-share-mc-well-uh_c1 with dissolve
    play voice3 girl34_thinking_hmm4 noloop
    my "But you don't open an adult entertainment studio without knowing how to woo a woman or two."
    scene sm1cs-my001-84 my-its-okay-we-all-have-wild-times-mc-what-yours_c1 with dissolve
    play voice3 girl34_happy_relief6 noloop
    my "And judging from what I read about Fetish Locator, you have wooed more than your fair share of women."
    play voice2 mc_arrogant_huh3 noloop
    mc "Well, uh..."
    my "It's okay, [mcname]. We all have our wild times. Sure, they all look a little different, but they're all wild."
    mc "Then what was your wild time?"
    scene sm1cs-my001-85 my-explains-europe-time-mc-wow-didnt-know_c1 with dissolve
    play voice3 girl34_thinking_emm2 noloop
    my "When I finished my residency in Crowning, I bought a one way ticket to Europe and spent 6 months roaming and seeing all of the breathtaking art I could find."
    play voice2 mc_surprised_wow4 noloop
    mc "Wow, I didn't know that."
    if persistent.is_special:
        my "There's a lot you don't know about your mother, [mcname]."
    else:
        my "There's a lot you don't know about me, [mcname]."
    mc "Well, what was your favorite thing you saw on that trip?"
    play sound sfx_cloth_rustling5
    scene sm1cs-my001-a87 mc-what-fav-thing-my-that-tough-glambot-000_i with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    play sound3 ["<silence 4.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs_my001-glambot-1
    pause
    play voice3 girl34_thinking_hmm3 noloop
    my "Mmmmm. That's tough..."
    my "But... the one I think back to the most was in Rome."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-my001-88 my-thinks-most-of-rome-everyone-who-do-art-must-go-rome_c1 with dissolve
    play voice3 girl34_arrogant_ha5 noloop
    my "Everyone who does art, has to go to Rome once. There's just so much history there..."
    scene sm1cs-my001-89 my-story-staying-hostel-find-treasure-trove_c1 with dissolve
    play voice3 girl34_thinking_emm4 noloop
    my "I was staying in this hostel, and the gal in the bed next to me came back one day, eyes shining like she had just found a treasure trove."
    my "And she had."
    scene sm1cs-my001-90 mc-leans-real-gold-my-better-caravaggio_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Like, real gold?"
    play voice3 girl34_no_uhuh noloop
    my "Better. She had found a hidden Caravaggio."
    scene sm1cs-my001-91 mc-car-what-my-explains_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "A car of what?"
    play voice3 girl34_arrogant_hm2 noloop
    my "Caravaggio was a famous painter. His works are in all of the big museums. But, before he did portraits, he painted churches."
    scene sm1cs-my001-92 my-excited-found-hidden-church-gave-her-address_c1 with dissolve
    play voice3 girl34_disappointed_huh noloop
    my "And she had found one of those churches, hidden away from the tourists and the madness."
    my "She gave me an address-"
    scene sm1cs-my001-93 mc-ask-to-church-my-nope-beginning-hunt_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "To the church?"
    play sound sfx_cloth_rustling3
    scene sm1cs-my001-94 my-explains-told-where-start-find-church-spent-next-days-rushing-though-rome_c1 with dissolve
    play voice3 girl34_no_nope4 noloop
    my "Nope. To the beginning of the hunt."
    play voice2 mc_thinking_hmm3 noloop
    mc "What do you mean?"
    scene sm1cs-my001-95 my-at-sunset-stumbled-nondescript-chapel-when-when-stepped-inside_c1 with dissolve
    play voice3 girl34_thinking_emm5 noloop
    my "She was told where to start to find the church, but she told me that the only way I could see it, is if I found it myself."
    my "I spent the next day, tearing through Rome, trying to find this church."
    my "And at sunset, exhausted, I stumbled into this completely nondescript chapel. A place you wouldn't look twice at."
    my "And when I stepped inside..."
    scene sm1cs-my001-96 mc-engulfed-story-you-saw-it_c1 with dissolve
    play voice2 mc_surprised_huh1 noloop
    mc "You saw it?"
    scene sm1cs-my001-97 my-too-dark-see-anything-no-light-nothing-someone-asked-five-euros_c1 with dissolve
    play voice3 girl34_no_neutral1 noloop
    my "It was too dark to see anything. There were no lights, nothing."
    my "I stumbled around, until a kind person told me that it would be 5 euros. I nervously held out my hand, and felt them take the money."
    scene sm1cs-my001-98 my-remembering-day-lights-came-on-thirty-seconds-all-she-got_c1 with dissolve
    play voice3 girl34_happy_mmm2 noloop
    my "And then the lights came on. The walls, the ceiling... they were covered in these masterpieces. I can't even begin to describe how beautiful they were."
    my "And then the lights shut off. 30 seconds is all I got."
    my "I stumbled into the hostel that night, sore, exhausted, but more alive than I had ever felt."
    play sound sfx_cloth_rustling2
    scene sm1cs-my001-99 my-stumbled-into-hostel-sore-numb-mc-wow_c1 with dissolve
    play voice2 mc_happy_wow1 noloop
    mc "Wow..."
    scene sm1cs-my001-100 my-embrassed-another-reason-apologize-mc-no-dont_c1 with dissolve
    play voice3 girl34_happy_relief1 noloop
    my "It seems I have another reason to apologize tonight. I didn't mean to get so lost in an old memory."
    play voice2 mc_no_no3 noloop
    mc "No! Don't apologize. That was beautiful."
    play sound sfx_heels_steps2
    scene sm1cs-my001-101 waiter-brings-pasta_c1 with dissolve
    play voice4 boy9_arrogant_ha4 noloop
    "Waiter" "And your main course for the evening, the pasta linguini. Please enjoy."
    play sound sfx_cup_slide1
    play sound2 sfx_cup_place1 noloop
    scene sm1cs-my001-102 waiter-drops-pasta-table_c1 with dissolve
    pause
    scene sm1cs-my001-103 mc-my-look-pasta-my-wow-looks-incredible-mc-only-best_c1 with dissolve
    play voice3 girl34_surprised_ohmy1 noloop
    my "Wow, [mcname], this looks incredible."
    play voice2 mc_yes_yes2 noloop
    if persistent.is_special:
        mc "Only the best for you, Mom."
    else:
        mc "Only the best for you, Melony."
    scene sm1cs-my001-104 my-thanks-before-continue-lets-eat_c1 with dissolve
    play voice3 girl34_happy_laugh1 noloop
    my "Thank you, sweetheart."
    my "But, before you ask me any other questions, let's eat. Lord knows what will happen if I keep rambling on."
    play sound sfx_fork_eating1 loop
    scene sm1cs-my001-105 mc-enjoying-rambling-though_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "I'm enjoying the rambling though."
    scene sm1cs-my001-106 my-happy-hear-not-boring-mc-you-never-could_c1 with dissolve
    play voice3 girl34_happy_great2 noloop
    my "Well, I'm happy to hear I'm not boring you."
    play voice2 mc_no_uhuh1 noloop
    mc "You never could."
    scene sm1cs-my001-107 my-starts-eating-fade-black_c1 with dissolve
    pause
    stop sound fadeout 2.0
    scene sm1cs-my001-109 my-that-incredible-mc-yeah-abosleutly-delicious_c1 with fade
    play voice3 girl34_happy_mmm3 noloop
    my "Mmmmmm, that was wonderful."
    scene sm1cs-my001-108 mc-my-after-dinner-holding-glasses_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, absolutely delicious!"
    play sound sfx_heels_steps2
    scene sm1cs-my001-110 waiter-comes-sir-you-date-interested-desert-mc-oh-she_c1 with dissolve
    play voice4 boy9_hey_easy noloop
    "Waiter" "Sir, would you and your date be interested in a dessert this evening?"
    play voice2 mc_pain_ou1 noloop
    mc "Oh, she's-"
    scene sm1cs-my001-111 my-quite-full-just-check-waiter-ofc-maam_c1 with dissolve
    play voice3 girl34_no_nah3 noloop
    my "I'm quite full actually. I believe just the check is all we need."
    play voice4 boy9_yes_simple3 noloop
    "Waiter" "Of course, ma'am."
    scene sm1cs-my001-112 mc-sorry-told-earlier-waiting-date-my-its-alright_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I'm sorry, I said earlier I was waiting for my date. I didn't mean to make it weird or anything."
    scene sm1cs-my001-113 my-leans-forwards-long-time-since-been-date-wonderful-evening_c1 with dissolve
    play voice3 girl34_yes_aga5 noloop
    my "It's all right, [mcname]."
    scene sm1cs-my001-114 mc-good-wanted-make-sure-pleasant-evening_c1 with dissolve
    play voice3 girl34_happy_relief3 noloop
    my "It's been a long time since anyone has taken me on a date. I'm fine with leaning into it a bit."
    my "This has truly been a wonderful evening."
    play voice2 mc_happy_a1 noloop
    mc "Good. I wanted to make sure you had a pleasant evening."
    play sound sfx_heels_steps2
    play sound2 sfx_paper_rustl1 noloop
    scene sm1cs-my001-115 waiter-bring-back-check_c1 with dissolve
    stop sound fadeout 1.0
    pause
    play sound sfx_paper_slide1
    scene sm1cs-my001-116 mc-snags-check-dont-pay-your-thank-you-dinner_c1 with dissolve
    play voice2 mc_no_uhuh3 noloop
    mc "Nuh uh. You don't get to pay for your \"thank you\" dinner."
    play sound sfx_paper_rustl2
    scene sm1cs-my001-117 mc-puts-cash-inside-check_c1 with dissolve
    pause
    play sound sfx_paper_rustl3
    scene sm1cs-my001-118 mc-hands-check-back-waiter-hope-both-had-excelent-dinner_c1 with dissolve
    play voice4 boy9_hey_bye1 noloop
    "Waiter" "I hope you both had an excellent evening, and we hope to see you again soon."
    scene sm1cs-my001-119 my-dont-have-be-ridicilous-mc-what-let-pay-dinner_c1 with dissolve
    play voice3 girl34_surprised_oh5 noloop
    my "[mcname], you don't need to be so ridiculous."
    play voice2 mc_surprised_uh3 noloop
    mc "What, and let you pay for the dinner I asked you to?"
    scene sm1cs-my001-120 my-yes-place-expensive-saving-money-for-studio_c1 with dissolve
    play voice3 girl34_yes_happy1 noloop
    my "Yes! Because this place is expensive, and you should be saving your money for the studio."
    scene sm1cs-my001-121 mc-no-prize-too-high-you-my-still-save-money_c1 with dissolve
    play voice2 mc_no_no2 noloop
    if persistent.is_special:
        mc "There's no price too high for you, Mom."
    else:
        mc "There's no price too high for you, Melony."
    scene sm1cs-my001-122 mc-you-never-my-sweet-talker_c1 with dissolve
    play voice3 girl34_angry_ahem3 noloop
    my "Still. Save your money!"
    play voice2 mc_no_nah1 noloop
    mc "When it comes to you? Never."
    play sound sfx_cloth_rustling3
    scene sm1cs-my001-123 my-stands-up_c1 with dissolve
    play voice3 girl34_disappointed_oof1 noloop
    my "Oh you sweet talker."
    call sm1cs_my001_deduct_money from _call_sm1cs_my001_deduct_money
    play sound sfx_bed_slide2
    scene sm1cs-my001-124 mc-stands-up-mc-would-like-walk-you-hotel-my-no-be-alright_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Would you like me to walk you back to your hotel?"
    play voice3 girl34_no_nah2 noloop
    my "No, I'll be alright. The hotel is pretty close to here."
    scene sm1cs-my001-125 my-offers-hand-thanks-for-special-evening_c1 with dissolve
    play voice3 girl34_happy_phew1 noloop
    my "Thank you for a special evening, [mcname]."
    play sound sfx_cloth_rustling4
    scene sm1cs-my001-126 mc-my-hug-mc-ofc-mom-melony-we-do-this-again_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    if persistent.is_special:
        mc "Of course, Mom."
    else:
        mc "Of course, Melony."
    mc "We'll have to do it again soon."
    scene sm1cs-my001-127 my-promise-mc-promise_c1 with dissolve
    play voice3 girl34_yes_questioning8 noloop
    my "Promise?"
    play voice2 mc_yes_yes3 noloop
    mc "Promise."
    scene sm1cs-my001-128 my-this-means-lot-mct-hugging-takes-long_c1 with dissolve
    play voice3 girl34_happy_relief2 noloop
    my "This really means the world to me. You have no idea."
    mct "Man, this hug is going on for a while."
    scene sm1cs-my001-129 mct-while-while-not-friend-hug_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Like, a while a while... not like a friendly hug, but..."
    play sound sfx_cloth_rustling2
    scene sm1cs-my001-130 my-lets-go-mc-well-know-how-get-hold-see-soon-hope_c1 with dissolve
    play voice3 girl34_disappointed_eem1 noloop
    my "Well, you know how to get a hold of me."
    my "I'll see you soon, I hope."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, you will!"
    play sound sfx_heels_steps1
    scene sm1cs-my001-131 my-leaves-restaurant-end-scene_c1 with dissolve
    pause
    play voice2 mc_thinking_hmm9 noloop
    mct "Well, I think that went well... Like, really well."
    mc "Well enough that she wants to do it again. Which is a good sign!"
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop sound fadeout 2.0
    stop sound4 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    jump sm1cs_my001_exit_to_free_roam
label sm1cs_my001_exit_to_free_roam:
    $ StoryController.end_scene(MY_STORY, 5, 0, 3)
    return
label sm1cs_my001_deduct_money:
    $ player.spend_money(200, _("Date with Melony"), _("You paid $200 as restaurant bill"))
    return