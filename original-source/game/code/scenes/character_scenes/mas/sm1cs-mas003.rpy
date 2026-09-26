image sm1cs_mas003-glambot-1 = Movie(play = "images/Character-Scenes/mas/s003/anim/sm1cs-mas003-a164-2x-50fps.webm", start_image = "sm1cs-mas003-a164 mas-topless-girls-cheer-00000", image = "sm1cs-mas003-a164 mas-topless-girls-cheer-00089", loop = False)
label sm1cs_mas003:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    play sound sfx_heels_steps2 loop
    scene sm1cs-mas003-01 mc-waves-mas_c1 with dissolve
    play music music_bedroom_groove
    play voice2 mc_hey_hey5 noloop
    mc "Hey Maya."
    play sound2 sfx_cloth_rustling1 noloop
    scene sm1cs-mas003-02 mc-hey-maaya-mas-mhm_c1 with dissolve
    play voice3 girl26_yes_aga noloop
    ms "Mmhmm."
    stop sound fadeout 2.0
    scene sm1cs-mas003-03 nr-soups-on-kids_c1 with dissolve
    play voice4 boy7_hey_simple noloop
    nr "Soup's on kids!"
    scene sm1cs-mas003-04 mc-what-mas-explains-mc-oh_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    play voice3 girl28_arrogant_hah1 noloop
    ms "That means he got an order."
    mc "Oh."
    scene sm1cs-mas003-05 nr-smile-there-are-orders-then-super-orders-this-super_c1 with dissolve
    play voice4 boy7_yes_aga1 noloop
    nr "There are orders, and then there are super orders."
    nr "This is a super order."
    play sound sfx_alarm1
    scene sm1cs-mas003-06 nr-looks-back-beep-its-got-friends_c1 with dissolve
    stop sound fadeout 2.0
    "*Electronic beeping*"
    play voice4 boy7_disappointed_aah noloop
    nr "And it's got friends."
    scene sm1cs-mas003-07 mas-great-hope-stretched-you-wearing-out-bike-today_c1 with dissolve
    play voice3 girl28_disappointed_eeh2 noloop
    ms "Great. Hope you stretched, [mcname]."
    ms "You'll be wearing out the bike today."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1cs-mas003-08 nr-going-twitch-him-mas-excuse-me_c1 with dissolve
    play voice4 boy7_arrogant_hmm3 noloop
    nr "You're going with him, Maya."
    play voice3 girl28_surprised_eeh noloop
    ms "Excuse me?"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mas003-09 super-order-getting-bigger-nr-looks-like-three-deliveries_c1 with dissolve
    play voice4 boy7_thinking_emm2 noloop
    nr "The super order is getting bigger."
    nr "Looks like three deliveries. So I want my best delivery people on it."
    scene sm1cs-mas003-10 mc-we-only-two-drivers-mas-what-shut-up_c1 with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Aren't we your only delivery people?"
    play voice3 girl28_arrogant_pff1 noloop
    ms "What? Shut up."
    scene sm1cs-mas003-12 mas-looks-nr-mas-nelson-cant-ride-mc-bike-one-seater_c1 with dissolve
    play voice3 girl28_hey_active noloop
    ms "Nelson. I can't ride on the bike with [mcname]."
    ms "It's a one-seater."
    scene sm1cs-mas003-13 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Flirt"(hint="sm1cs_mas003_m01_h01"):
            call sm1cs_mas003_m01_c01 from _call_sm1cs_mas003_m01_c01
            scene sm1cs-mas003-14 choice-flirt-mc-can-always-sit-in-lap_c1 with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "You can always ride on my lap, Maya."
            scene sm1cs-mas003-15 mas-rather-eat-garbage-mc-cheesh_c1 with dissolve
            play voice3 girl28_disgust_oeagh1 noloop
            ms "I'd rather eat last week's brauts from the garbage."
            play voice2 mc_angry_oof noloop
            mc "Sheesh."
        "Say nothing"(hint="sm1cs_mas003_m01_h01"):
            pass
    if player.get_choice("sm1cs_mas003_flirt_1"):
        play sound sfx_keys_jingle1
        scene sm1cs-mas003-16 nr-dont-eat-garbage-mas-wasnt-going-to_c1 with dissolve
        stop sound fadeout 2.0
        play voice4 boy7_disgust_boeagh noloop
        nr "Don't eat garbage, Maya."
        play voice3 girl28_no_nah2 noloop
        ms "I wasn't going to."
    scene sm1cs-mas003-17 nr-never-said-sharing-bike_c1 with dissolve
    play voice4 boy7_arrogant_ha2 noloop
    nr "I never said you two had to share a bike."
    play sound sfx_throw_something1
    play sound2 sfx_metal_chain1 noloop
    scene sm1cs-mas003-18 nr-tosses-keys-taking-car-mct-didnt-know-he-has-car_c1 with dissolve
    play voice4 boy7_yes_yep noloop
    nr "You're taking the car."
    play voice2 mc_angry_huh2 noloop
    mct "I didn't even know we had a car."
    play sound sfx_leg_kick8
    play sound2 sfx_chains_swings1 noloop
    scene sm1cs-mas003-19 mas-catches-keys-yoink-mc-hey_c1 with dissolve
    stop sound2 fadeout 1.5
    play voice3 girl28_arrogant_hah3 noloop
    ms "Yoink."
    play voice2 mc_hey_hey8 noloop
    mc "Hey."
    scene sm1cs-mas003-20 mas-you-carry-i-drive-choice-menu_c1 with dissolve
    play voice3 girl28_yes_yeah2 noloop
    ms "You carry. I drive."
    menu:
        "Joke"(hint="sm1cs_mas003_m02_h01"):
            call sm1cs_mas003_m02_c01 from _call_sm1cs_mas003_m02_c01
            scene sm1cs-mas003-21 choice-joke-mc-good-do-cars-have-two-pedals_c1 with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "Good because I honestly can't recall the last time I drove."
            mc "Do cars still have two pedals?"
            scene sm1cs-mas003-22 nr-grinning_c1 with dissolve
            play voice4 boy7_arrogant_he noloop
            pause
        "Flirt"(hint="sm1cs_mas003_m02_h02"):
            call sm1cs_mas003_m02_c02 from _call_sm1cs_mas003_m02_c02
            scene sm1cs-mas003-23 choice-flirt-mc-whatever-say-gorgeous-mas-say-that-again_c1 with dissolve
            play voice2 mc_yes_yes7 noloop
            mc "Whatever you say, gorgeous."
            play voice3 girl28_angry_argh2 noloop
            ms "Say that again, and I'll run over your foot."
            scene sm1cs-mas003-24 mc-cools-jets-got-it_c1 with dissolve
            play voice2 mc_scared_oh3 noloop
            mc "Got it."
        "Complain"(hint="sm1cs_mas003_m02_h03"):
            call sm1cs_mas003_m02_c03 from _call_sm1cs_mas003_m02_c03
            scene sm1cs-mas003-25 choice-complain-mc-division-one-sided_c1 with dissolve
            play voice2 mc_disappointed_ehh5 noloop
            mc "This division of labor feels one-sided."
            play voice3 girl28_arrogant_hah2 noloop
            ms "What are you, my economics teacher?"
    play sound sfx_heels_steps2 loop
    scene sm1cs-mas003-26 mas-nears-door-hurry-up-mc-could-help-carry_c1 with dissolve
    play voice3 girl28_arrogant_huh1 noloop
    ms "Hurry up. We've got tips to make."
    play voice2 d2s12_emmm noloop
    mc "You could help me carry them."
    play sound sfx_door_open1
    scene sm1cs-mas003-27 mas-at-door-has-get-car-ready-sometimes-takes-minute-warm-up_c1 with dissolve
    play voice3 girl28_no_nah3 noloop
    ms "I need to get the car ready."
    ms "Sometimes it takes a minute to warm up."
    play sound sfx_door_creak4
    play sound4 sfx_distanttraffic_city fadein 1.0
    scene sm1cs-mas003-28 nr-never-does-that-me-mas-guess-lucky_c1 with dissolve
    play voice4 boy7_no_nah noloop
    nr "Never does that with me."
    play voice3 girl26_thinking_hmm4 noloop
    ms "Hmm. Guess I'm just lucky."
    play sound sfx_heels_steps2 loop
    scene sm1cs-mas003-29 mc-walking-out-carying-bags-food-mct-ouah-my-arrms_c1 with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "Ouhaaah."
    mct "My arms..."
    play sound sfx_car_door_open1
    scene sm1cs-mas003-30 mc-straining-yeah-no-problem_c1 with dissolve
    play voice3 boy7_angry_cough noloop
    nr "Don't let me down, [mcname]."
    $ renpy.music.set_pan(0.7, 0.0, "music" )
    play voice2 mc_yes_yeah5 noloop
    mc "*straining* Yeah... no problem."
    play sound sfx_paper_bag_2
    play sound2 sfx_paper_bag_1
    scene sm1cs-mas003-31 mc-puts-food-back-seat_c1 with dissolve
    $ renpy.music.set_pan(0.0, 0.5, "music" )
    pause
    play sound sfx_car_enter1
    play sound2 sfx_car_door_closed1 noloop
    stop sound4 fadeout 2.0
    scene sm1cs-mas003-32 mc-sits-passenger-mas-everything-secure-mc-yes_c1 with dissolve
    play voice3 girl28_arrogant_hmm1 noloop
    ms "Everything secure?"
    play voice2 mc_yes_yes1 noloop
    mc "Yes."
    scene sm1cs-mas003-33 mas-talking-something-mess-up-coming-out-your-tip_c1 with dissolve
    play voice3 girl28_arrogant_hah4 noloop
    ms "Good. Because if something gets messed up, it's coming out of your tip."
    play sound sfx_supercar_skid1
    play sound2 sfx_supercar_drive1 fadein 1.5
    play sound3 sfx_car_startmove2 noloop
    scene sm1cs-mas003-34 mas-floors-pedal_c1 with hpunch
    play voice2 mc_scared_huh1 noloop
    pause
    play sound4 sfx_supercar_passby1 noloop
    scene sm1cs-mas003-35 mc-mas-car-flies-towards-first-delivery_c1 with dissolve
    pause
    scene sm1cs-mas003-36 mc-woah-you-crazy-mas-we-on-clock_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Woah! Are you crazy?"
    play voice3 girl28_arrogant_hm noloop
    ms "We're on the clock, remember."
    play sound sfx_car_skid1
    stop sound2 fadeout 1.0
    play sound3 sfx_car_approach1 noloop
    scene sm1cs-mas003-37 mc-mas-arrive-first-location_c1 with hpunch
    play voice2 mc_surprised_huh3 noloop
    pause
    scene sm1cs-mas003-38 mc-freaked-out-buh_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Buh."
    scene sm1cs-mas003-39 mas-we-here_c1 with dissolve
    play voice3 girl28_yes_yap3 noloop
    ms "We're here."
    play sound sfx_cloth_rustling1
    scene sm1cs-mas003-40 mas-looks-receipt-grab-order-three-bags_c1 with dissolve
    play voice3 girl28_disappointed_mmm2 noloop
    ms "Grab the order. Should all be in three bags."
    play sound sfx_car_door_open1
    play sound2 sfx_paper_bag_1 noloop
    play sound4 sfx_distanttraffic_city2 fadein 1.0
    scene sm1cs-mas003-41 mc-gets-back-seat-mas-next-car_c1 with dissolve
    pause
    scene sm1cs-mas003-42 mc-what-looking-for-mas-reads-order_c1 with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "What am I looking for?"
    play voice3 girl26_thinking_ehh2 noloop
    ms "Three number ones. One number one with extra cheese. Two Hot Hause Combos, one hold the relish. Five fries and four drinks."
    play sound2 sfx_paper_bag_2 noloop
    play sound sfx_car_door_closed1
    scene sm1cs-mas003-43 mc-holding-bags-looking-building_c1 with dissolve
    pause
    if player.get_choice("sm1cs_mas003_flirt_1") or player.get_choice("sm1cs_mas003_flirt_2"):
        scene sm1cs-mas003-44 mas-shout-wooh-go-get-hot-buns-mc-what-doing_c1 with dissolve
        play voice3 girl28_happy_nice2 noloop
        ms "Wooh. Looking good, hotbuns!"
        play voice2 mc_surprised_what3 noloop
        mc "What are you doing?"
        scene sm1cs-mas003-45 mas-smiles-oh-not-flirty-when-working-mas-good-know_c1 with dissolve
        play voice3 girl28_surprised_oh noloop
        ms "Oh, you don't like people being flirty with you when you're working?"
        ms "Good to know."
    play sound sfx_heels_steps2 loop
    scene sm1cs-mas003-46 mc-walks-towards-delivery_c1 with dissolve
    pause
    jump sm1cs_mas003_second_delivery
label sm1cs_mas003_second_delivery:
    play sound sfx_door_openclosed1
    scene black
    show screen scene_transistion("One delivery down")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_heels_steps2 loop
    scene sm1cs-mas003-47 mc-walking-out-holding-cash_c1
    with Fade(0.5, 0.5, 0.5)
    play sound2 sfx_paper_rustl1 noloop
    pause
    scene sm1cs-mas003-48 mas-sitting-on-car-hey_c1 with dissolve
    play voice3 girl28_hey_angry noloop
    ms "Hey."
    play sound sfx_throw_something1
    play sound2 sfx_metal_chain1 noloop
    scene sm1cs-mas003-49 mas-tosses-keys-you-drive-mc-huh_c1 with dissolve
    play voice3 girl28_arrogant_hmm3 noloop
    ms "You drive."
    play voice2 mc_surprised_huh7 noloop
    mc "Huh?"
    play sound sfx_leg_kick8
    play sound2 sfx_chains_swings1 noloop
    scene sm1cs-mas003-50 mas-next-door-too-angry-drive-mct-something-he-said_c1 with dissolve
    stop sound2 fadeout 1.0
    play voice3 girl26_angry_argh3 noloop
    ms "I'm too angry to drive."
    play voice2 d1s1_mmm noloop
    mct "Was it something I said?"
    play sound sfx_car_door_closed1
    play sound2 sfx_car_enter1 noloop
    scene sm1cs-mas003-51 mas-mc-in-car_c1 with dissolve
    pause
    play sound sfx_car_startmove
    play sound2 sfx_supercar_drive1 fadein 2.0
    scene sm1cs-mas003-52 mc-takes-off-car_c1 with dissolve
    pause
    scene sm1cs-mas003-53 mc-mas-driving-next-part-town_c1 with dissolve
    pause
    stop sound2 fadeout 4.0
    play sound3 sfx_car_inside_ride1 fadein 2.0
    stop sound4 fadeout 2.0
    scene sm1cs-mas003-54 mas-notices-mc-looking-her_c1 with dissolve
    pause
    scene sm1cs-mas003-55 mc-snaps-head-forward_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Uh oh."
    scene sm1cs-mas003-56 mas-zoom-tiny-smile_c1 with dissolve
    pause
    scene sm1cs-mas003-57 mas-talking-mc-not-gonna-bite-head-off_c1 with dissolve
    play voice3 girl28_happy_laugh1 noloop
    ms "*chuckles* I'm not going to bite your head off or anything."
    scene sm1cs-mas003-58 mc-you-sure-mas-pretty-sure_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "You sure?"
    play voice3 girl28_yes_confident noloop
    ms "Pretty sure."
    scene sm1cs-mas003-59 mas-bummed-today-rejected-all-applications-thankful-this-one-sent-letter_c1 with dissolve
    play voice3 girl26_disappointed_mmh2 noloop
    ms "Today, I got the last rejection from all of the places I applied to."
    ms "I guess I should be thankful this one actually sent a rejection letter."
    scene sm1cs-mas003-60 mas-bunch-sent-nothing-website-mc-that-sucks-maya_c1 with dissolve
    play voice3 girl26_arrogant_mff noloop
    ms "A bunch sent nothing. I'm just assuming I didn't get it because the job is off of the website."
    play voice2 mc_disappointed_ah2 noloop
    mc "That sucks, Maya."
    play sound sfx_cloth_rustling1
    scene sm1cs-mas003-61 mas-holding-up-hands-mas-didnt-get-job-mc-okay-they-moron_c1 with dissolve
    play voice3 girl28_angry_dough1 noloop
    ms "I couldn't even land the job where I run around in a protective suit and get chased and tackled by police dogs in training."
    play voice2 mc_yes_okay2 noloop
    mc "Okay well, whoever made that decision is a moron."
    mc "You would be perfect to help train police dogs."
    scene sm1cs-mas003-62 mc-grin-perfect-train-police-dogs-mas-shut-up_c1 with dissolve
    play voice3 girl28_happy_laugh2 noloop
    ms "Shut up."
    scene sm1cs-mas003-63 mc-can-imagine-mas-run-not-get-anywhere_c1 with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "I can just imagine you trying to run, and not getting anywhere."
    scene sm1cs-mas003-64 mas-jokingly-shut-up-not-funny-mc-be-pro-being-slobbered-on_c1 with dissolve
    play voice3 girl28_happy_laugh3 noloop
    ms "*giggles* Shut it. It's not funny."
    play voice2 mc_happy_laugh2 noloop
    mc "You'd be a pro at being slobbered on."
    scene sm1cs-mas003-65 mc-focus-ppl-say-never-seen-that-before-could-be-slobber-atractor_c1 with dissolve
    queue voice2 d1s5_mchappy noloop volume 1.7
    mc "People would say, \"I've never seen someone like that before\"."
    mc "\"She could be the Slobber Attractor.\""
    scene sm1cs-mas003-66 mas-giggles-mc_c1 with dissolve
    play voice3 girl28_happy_laugh4 noloop
    ms "*giggles*"
    scene sm1cs-mas003-67 mc-turns-towards-mas-dogs-eat-up-mas-laughs_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Those dogs would just eat you up."
    play voice3 girl28_happy_laugh5 noloop
    ms "*laughs*"
    scene sm1cs-mas003-68 mas-you-suck-dork-mc-ywa-but-better-day-now_c1 with dissolve
    play voice3 girl26_happy_relief2 noloop
    ms "You're such a dork."
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, but you're having a better day now."
    play sound sfx_car_window1
    play sound4 sfx_supercar_drive1 fadein 1.5 volume 0.5
    scene sm1cs-mas003-69 mas-nope-still-rain-clouds_c1 with dissolve
    play voice3 girl28_no_nope1 noloop
    ms "Nope. Still just rain clouds and cold winds."
    scene sm1cs-mas003-70 mc-can-admit-on-one-think-less-cool-mas-think-im-cool_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "You can admit it. No one will think you're less cool if you have fun like a human being."
    play voice3 girl28_disappointed_eeh1 noloop
    ms "You think I'm cool?"
    scene sm1cs-mas003-71 choice-menu-screen_c1 with dissolve
    menu:
        "Play it cool"(hint="sm1cs_mas003_m03_h01"):
            call sm1cs_mas003_m03_c01 from _call_sm1cs_mas003_m03_c01
            scene sm1cs-mas003-72 choice-play-cool-mc-being-slick-dont-think-said-that-mas-okay-mr-suave_c1 with dissolve
            play voice2 mc_surprised_oh1 noloop
            mc "Oh. I don't think I said that."
            scene sm1cs-mas003-73 mas-pushing-back-totally-said-that_c1 with dissolve
            play voice3 girl28_arrogant_hmm2 noloop
            ms "Okay, Mr. Suave."
            ms "You totally said that."
            scene sm1cs-mas003-74 mc-grinning-yeah-did-so-im-right-world-no-shity-with-me_c1 with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "Yeah, I did. So, I'm right, right?"
            mc "The world's not so shitty with [mcname] by your side."
            scene sm1cs-mas003-75 mas-accepts-maybe-right_c1 with dissolve
            play voice3 girl28_yes_yap4 noloop
            ms "Maybe."
        "Agree with her"(hint="sm1cs_mas003_m03_h02"):
            scene sm1cs-mas003-76 choice-agree-mc-yeah-mas-mmm_c1 with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "Yeah."
            play voice3 girl28_disappointed_mmm1 noloop
            ms "Mmm."
            scene sm1cs-mas003-77 mc-adding-mc-just-regular-cool-got-room-special-cool_c1 with dissolve
            play voice2 mc_arrogant_hm1 noloop
            mc "Just regular cool, though."
            mc "I think you've got some room for super cool."
            scene sm1cs-mas003-78 mas-sarcastic-what-shame_c1 with dissolve
            play voice3 girl26_disappointed_oof noloop
            ms "What a shame."
    scene sm1cs-mas003-79 mas-sigh-just-waiting-things-get-easier-life-feels-like-pedal_c1 with dissolve
    play voice3 girl28_happy_relief2 noloop
    ms "*sighs*"
    ms "I'm just waiting for things to get a little easier."
    ms "My life feels like the pedal hit the metal at the end of high school, and it hasn't fucking stopped."
    scene sm1cs-mas003-80 mc-agreeing-with-her-mc-lots-stuff-last-years-mas-you-right_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "There has been a lot of stuff on these last couple of years."
    scene sm1cs-mas003-80 mc-agreeing-with-her-mc-lots-stuff-last-years-mas-you-right_c1 with dissolve
    play voice3 girl28_disappointed_oh noloop
    ms "God. I wasn't even thinking about that stuff, but you're right."
    scene sm1cs-mas003-81 mas-self-loathing-now-feel-selfish-mopey-maya-mc-its-alright_c1 with dissolve
    play voice3 girl28_disappointed_off noloop
    ms "Now I feel selfish. No one likes mopey Maya."
    play voice2 mc_no_nah2 noloop
    mc "It's alright."
    scene sm1cs-mas003-82 mc-trying-bolster-spirits-mc-going-figure-out-cant-imagine-being-wursthaus-rest-days_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "You're going to figure something out, Maya."
    mc "I can't imagine you'll be at the Wurst Delivery for the rest of your days."
    scene sm1cs-mas003-83 mas-kinda-depressed-what-if-am-need-another-job-one-better-paying_c1 with dissolve
    play voice3 girl26_thinking_ehh2 noloop
    ms "What if I am? My student loans aren't going to just disappear."
    ms "I need another job or just one that is better paying."
    play sound sfx_car_approach1
    stop sound4 fadeout 2.0
    stop sound3 fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mas003-84 mas-waves-hands-mas-this-life-mas-nights-stuck-car-delivering-sausages_c1 with dissolve
    queue sound4 sfx_distanttraffic_city2 fadein 1.5
    play voice3 girl26_thinking_huh noloop
    ms "Or this is my life."
    ms "Nights stuck in a car delivering sausages with some dude."
    scene sm1cs-mas003-85 mas-realize-offend-mc-i-mean_c1 with dissolve
    play voice3 girl28_happy_mmm1 noloop
    ms "I mean..."
    scene sm1cs-mas003-86 mc-think-we-here-mas-so-we-are_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I think we're here."
    play voice3 girl28_yes_yap1 noloop
    ms "So we are."
    play sound sfx_car_door_open1
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene sm1cs-mas003-87 mc-mas-make-second-delivery_c1 with dissolve
    pause
    play sound sfx_door_openclosed1
    stop sound2 fadeout 2.0
    stop sound3 fadeout 2.0
    jump sm1cs_mas003_third_delivery
label sm1cs_mas003_third_delivery:
    scene black
    show screen scene_transistion("Second delivery complete")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene sm1cs-mas003-88 mc-mas-go-out-building-both-wierded-out_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-mas003-89 mc-that-was-mas-holy-shit_c1 with vpunch
    play voice2 d1s5b_emmm noloop
    mc "That guy was..."
    play voice3 girl26_disgust_argh noloop
    ms "Holy shit."
    scene sm1cs-mas003-90 mc-wierd-mas-no-you-wierd-this-guy_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Weird."
    play voice3 girl28_no_questioning noloop
    ms "No, you're {i}weird{/i}. That guy was just..."
    scene sm1cs-mas003-91 mas-wasnt-pervert-mc-wasnt-creep_c1 with dissolve
    play voice3 girl26_surprised_ehh2 noloop
    ms "I mean, he wasn't a pervert."
    play voice2 mc_yes_aga1 noloop
    mc "And wasn't a creep."
    play sound sfx_cloth_rustling4
    scene sm1cs-mas003-92 mas-no-jackass-mc-no-was-something_c1 with dissolve
    play voice3 girl28_yes_yeah1 noloop
    ms "Not a jackass..."
    play voice2 mc_no_no6 noloop
    mc "No. But he was something."
    scene sm1cs-mas003-93 mas-totally_c1 with dissolve
    play voice3 girl26_yes_yep noloop
    ms "Totally."
    scene sm1cs-mas003-94 mas-mc-looking-each-other_c1 with dissolve
    pause
    play sound sfx_cloth_rustling3
    scene sm1cs-mas003-95 mc-mas-laugh-together_c1 with dissolve
    play voice2 mc_happy_laugh4 noloop
    play voice3 girl28_happy_laugh6 noloop
    "[mcname] and Maya" "*laughing*"
    scene sm1cs-mas003-96 more-motivation-stop-working-wurst-mas-you-said-it_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Just more motivation for you to stop working at Wurst Delivery."
    play voice3 girl28_happy_relief1 noloop
    ms "Amen to that."
    play sound sfx_car_door_open1
    play sound2 sfx_car_enter1 noloop
    scene sm1cs-mas003-97 mc-mas-get-back-car_c1 with dissolve
    pause
    scene sm1cs-mas003-98 mas-looking-back-bags-one-more-order-than-done_c1 with dissolve
    play voice3 girl26_happy_relief1 noloop
    ms "One more order."
    ms "Then we're done."
    play sound sfx_car_door_closed1
    stop sound4 fadeout 2.0
    scene sm1cs-mas003-99 least-not-boring-mas-silent_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mc "At least it hasn't been boring."
    ms "..."
    scene sm1cs-mas003-100 mas-ask-what-do-when-not-delivering-wieners-mas-you-in-college-right_c1 with dissolve
    play voice3 girl28_hey_sexy noloop
    ms "What do you do when you're not delivering wieners, [mcname]?"
    ms "You're in college, right?"
    scene sm1cs-mas003-101 mc-no-anymore-finished-sophomore-year-mas-and_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "No. Not anymore. I finished my sophomore year."
    play voice3 girl26_thinking_hmm3 noloop
    ms "And?"
    scene sm1cs-mas003-102 mc-now-thinking-going-diff-direction-mas-smart_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "And now I'm thinking of going in a different direction."
    play voice3 girl28_happy_mmm3 noloop
    ms "Smart."
    scene sm1cs-mas003-103 mas-or-dumb-mas-at-least-have-fewer-loans-me_c1 with dissolve
    play voice3 girl28_arrogant_huh2 noloop
    ms "Or dumb. What do I know?"
    ms "At least you'll have fewer student loans than me."
    play voice3 girl28_arrogant_heh noloop
    ms "So, how are you surviving in the city? You must need money, or you wouldn't be doing this."
    scene sm1cs-mas003-104 mas-how-surviving-city-mc-have-main-job_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. I have a main job. It's what I'm focusing all my energy on."
    play sound sfx_car_startmove
    play sound2 sfx_supercar_drive1 fadein 2.0
    scene sm1cs-mas003-105 car-drives-off-mas-talking-mysterious-job-mas-what-is-it_c1 with dissolve
    play voice3 girl26_disappointed_oh noloop
    ms "Oh a 'main' job. So mysterious."
    ms "What is it?"
    scene sm1cs-mas003-106 mc-uh-mct-dont-think-is-time-like-maya-not-friendship-level-yet_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "Uh."
    mct "I don't think this is the time to tell her I'm trying to become a porn actor and producer."
    mct "I like Maya, but I'm not sure we're on the \"I do porn\" level of our friendship yet."
    scene sm1cs-mas003-107 mas-hey-earth-mc-sorry_c1 with dissolve
    play voice3 girl28_hey_active noloop
    ms "Hey. Earth to [mcname]?"
    play voice2 mc_disappointed_off2 noloop
    mc "Sorry."
    scene sm1cs-mas003-108 mas-just-tell-what-main-job-is-mc-trying-get-into-movies_c1 with dissolve
    play voice3 girl28_arrogant_huh1 noloop
    ms "Just tell me what this main job is."
    play voice2 mc_disappointed_ah1 noloop
    mc "Uh... a friend and I are trying to get into making... movies."
    scene sm1cs-mas003-109 mas-laughs-at-mc_c1 with dissolve
    play voice3 girl28_happy_laugh5 noloop
    ms "Hahaha."
    scene sm1cs-mas003-116 mc-what_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What?"
    scene sm1cs-mas003-117 mas-talking-way-said-it-acted-so-awkward-mc-like-what_c1 with dissolve
    play voice3 girl28_happy_laugh1 noloop
    ms "The way you said that, haha."
    ms "You acted so awkward. It sounds like you're trying to cover up something."
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Like what?"
    scene sm1cs-mas003-118 mas-like-making-porn-movies-mc-blush-what-what-made-mind-go-there_c1 with dissolve
    play voice3 girl28_arrogant_hmm3 noloop
    ms "Like you're making porn movies."
    play voice2 mc_arrogant_heh3 noloop
    mc "Haha. What? What made your mind go there."
    scene sm1cs-mas003-119 mas-dont-know-mc-huh-mas-mmm_c1 with dissolve
    play voice3 girl26_disappointed_mmh1 noloop
    ms "I don't know. Just the first thought that came to mind."
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh..."
    ms "Mmm."
    scene sm1cs-mas003-120 mc-mas-continue-driving-silence_c1 with dissolve
    pause
    play sound sfx_car_approach1
    stop sound2 fadeout 3.0
    play sound4 sfx_distanttraffic_city2 fadein 2.0
    scene sm1cs-mas003-121 mc-mas-pull-up-front-house_c1 with dissolve
    pause
    play sound3 sfx_car_door_open1 noloop
    stop sound fadeout 2.0
    scene sm1cs-mas003-122 mas-thank-god-next-destination-nevermind_c1 with dissolve
    play voice3 girl28_happy_phew1 noloop
    ms "Oh, thank god we're at the last dropoff."
    ms "Nevermind."
    play sound sfx_paper_bag_1
    scene sm1cs-mas003-123 mct-that-getting-strange-hopefully-make-last-delivery_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Alright, this is starting to feel strange."
    mct "Hopefully, we can just make this last delivery and then be done."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1cs-mas003-124 mas-walks-towards-sorority-mc-follows_c1 with dissolve
    pause
    play sound3 sfx_door_openclosed2 noloop
    play sound sfx_carpet_footsteps1 loop
    play sound2 sfx_carpet_footsteps2
    stop sound4 fadeout 2.0
    scene sm1cs-mas003-125 mas-mc-walking-sorority-corridor-hope-this-one-is-quick_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "I hope this one is quick. No weird customers and no awkwardness."
    $ renpy.music.set_volume(0.0, 3.5, "music" )
    $ renpy.music.set_volume(1.0, 0.5, "music2" )
    play music2 music_party_11 fadein 2.0 volume 0.84
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    scene sm1cs-mas003-127 sorrority-girls-open-door_c1 with dissolve
    pause
    scene sm1cs-mas003-126 mc-jaw-drops-sees-girls_c1 with dissolve
    play voice2 d3s7_mcemm noloop
    pause
    scene sm1cs-mas003-128 ka-yay-food-here-lg-coming-in-style_c1 with dissolve
    play voice4 girl30_happy_yeah3 noloop
    ka "Yay. Food is here!"
    scene sm1cs-mas003-129 os-omg-lauren-keep-in-pants_c1 with dissolve
    play voice5 girl35_angry_hmm1 noloop
    lg "And it's coming in style. *growls*"
    play voice6 girl34_surprised_ohmy1 noloop
    ols "Oh my god, Lauren. Keep it in your pants."
    play sound sfx_glass_bottle_bonk
    scene sm1cs-mas003-130 lg-what-would-be-rude-kg-omg-she-drunk_c1 with dissolve
    play voice5 girl35_surprised_what5 noloop
    lg "What? It would be rude not to let the Johnny know he's handsome."
    play voice4 girl30_surprised_ohmy1 noloop volume 0.7
    ka "Oh my god, she's so drunk."
    scene sm1cs-mas003-131 lg-usually-say-something-lewd-oh-my-ethics_c1 with dissolve
    play voice5 girl35_yes_aga6 noloop
    lg "She is, usually, she'd be the one saying something lewd."
    lg "Oh my. It was me ethic's time."
    scene sm1cs-mas003-132 os-drunk-lauren-best_c1 with dissolve
    play voice6 girl34_happy_laugh1 noloop
    ols "Drunk Lauren is the best."
    scene sm1cs-mas003-133 mas-yeah-need-payment-ka-oh-didnt-see-there_c1 with dissolve
    play voice3 girl28_yes_yeah4 noloop
    ms "Yeah, so we need the payment."
    play voice4 girl30_surprised_oh2 noloop
    ka "Oh hey. Sorry didn't see you there."
    scene sm1cs-mas003-134 ka-which-mistake-you-cute_c1 with dissolve
    play voice4 girl30_thinking_mmm1 noloop
    ka "Which is a mistake.{w} You're kind of cute."
    scene sm1cs-mas003-135 mas-surprsed-what_c1 with dissolve
    play voice3 girl28_surprised_what noloop
    ms "What?"
    scene sm1cs-mas003-136 lg-disagree-i-say-keen-eyes-kennedy-os-oh-my-god_c1 with dissolve
    play voice5 girl35_thinking_oh1 noloop
    lg "I say. Keen eyes, Kennedy."
    play voice6 girl34_surprised_ohmy2 noloop
    ols "Oh my god. How do the two of you go on deliveries together and not just snack on each other?"
    scene sm1cs-mas003-137 mc-mas-confused-mc-what-mas-normally-no-deliveries-together_c1 with dissolve
    play voice2 mc_surprised_what5 noloop
    mc "What?"
    play voice3 girl28_surprised_eeh noloop
    ms "Normally we don't go on deliveries together."
    scene sm1cs-mas003-138 ka-teases-mas-but-want-to-mas-what-gross_c1 with dissolve
    play voice4 girl30_arrogant_huh1 noloop
    ka "But you've been wanting to."
    play voice3 girl28_surprised_huh noloop
    ms "What? Gross."
    scene sm1cs-mas003-139 os-read-through-mas-she-totally-glad-they-are-lg-can-order-food_c1 with dissolve
    play voice6 girl34_happy_yeah2 noloop
    ols "She is totally glad they are. Oh my god."
    play voice5 girl35_thinking_eem3 noloop
    lg "Can we order food? I'm really hungry."
    scene sm1cs-mas003-140 mc-holding-bags-you-already-did-lg-smashing-good-time_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Uh yeah. You already did."
    play voice5 girl35_happy_great3 noloop
    lg "Smashing good time."
    play sound sfx_cloth_rustling4
    play sound2 sfx_paper_bag_2 noloop
    scene sm1cs-mas003-141 lg-touches-mc-hand-in-porn-would-smash-you-os-keeps-outdoing-herself_c1 with dissolve
    play voice5 girl35_disappointed_mff2 noloop
    lg "You know... if this was a porno, I'd be smashing him already."
    play voice6 girl34_happy_laugh4 noloop
    ols "She keeps outdoing herself."
    scene sm1cs-mas003-142 lg-drunk-who-dear-os-you-lg-splendid_c1 with dissolve
    play voice5 girl35_disappointed_oh2 noloop
    lg "Oh dear. Who?"
    play voice6 girl34_arrogant_laugh2 noloop
    with hpunch
    ols "You!"
    lg "Splendid."
    scene sm1cs-mas003-143 ka-gives-mas-money-sorry-my-friend-never-drank-exposed-real-men_c1 with dissolve
    play voice4 girl30_hey_quiet noloop
    ka "I'm sorry for my friend. I think she was super sheltered growing up and never drank."
    ka "Or got exposed to real men."
    play sound sfx_cloth_rustling3
    scene sm1cs-mas003-144 mc-grinning-happy-help_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Happy to help."
    scene sm1cs-mas003-145 os-need-more-help-first-pi-phi-party_c1 with dissolve
    play voice6 girl34_hey_simple2 noloop
    ols "We need more help. This is the first party for the Pi Phi house."
    play voice3 girl28_arrogant_huh2 noloop
    ms "Did you say pie pie?"
    scene sm1cs-mas003-146 ka-no-get-it-right-lg-wow-steady-on_c1 with dissolve
    play voice4 girl30_angry_err3 noloop
    ka "No, the Pi Phi house. For Pi Beta Phi. Get it right."
    play voice5 girl35_surprised_wow1 noloop
    lg "Wow. Steady on."
    play sound sfx_cloth_rustling2
    scene sm1cs-mas003-147 os-easy-tiger-ka-sorry-just-love-house-love-bitches_c1 with dissolve
    play voice6 girl34_yes_yeah1 noloop
    ols "Yeah, easy tiger."
    play voice4 girl30_disappointed_eeh2 noloop
    ka "I'm sorry. I just... I love my house. And I love these two bitches."
    scene sm1cs-mas003-148 ka-they-best-lg-aaaw_c1 with dissolve
    play voice3 nari_pain_sniff1 noloop
    ka "*sniff* There the best."
    play voice5 girl35_thinking_oh4 noloop
    lg "Ahhh."
    scene sm1cs-mas003-149 os-about-cry-dont-start-cry-will-start-crying_c1 with dissolve
    play voice6 girl34_pain_sobs4 noloop
    ols "*sniff* Don't you start crying because then I'll start crying."
    scene sm1cs-mas003-150 ka-focuses-mc-he-cute-lg-oh-yes_c1 with dissolve
    play voice4 girl30_arrogant_heh noloop
    ka "He's kind of cute."
    play voice5 girl35_yes_happy3 noloop
    lg "Oh yes. The sausage delivery boy is a sausage man."
    scene sm1cs-mas003-151 lg-show-sausage-os-lauren_c1 with dissolve
    play voice5 girl35_happy_mmm3 noloop
    lg "Show us your sausage, sailor."
    play voice6 girl34_disgust_ohh noloop
    ols "Lauren."
    scene sm1cs-mas003-152 ka-yeah-want-see-both-before-decision-mc-nah-here-just-bring-food_c1 with dissolve
    play voice4 girl30_yes_yeah5 noloop
    ka "Yeah. I want to see both. Then I'll make my final decision."
    play voice2 mc_no_nah1 noloop
    mc "Nah... no thanks. I'm just here to bring food."
    play sound sfx_leg_kick8
    scene sm1cs-mas003-153 lg-drool-no-fun-you-are-no-fun_c1 with dissolve
    play voice5 girl35_disappointed_aah noloop
    lg "Droll. No fun."
    lg "You are no fun."
    scene sm1cs-mas003-154 os-looks-mas-what-bout-you-mas-surprised-me_c1 with dissolve
    play voice6 girl34_arrogant_huh2 noloop
    ols "What about you?"
    play voice3 girl28_disappointed_eeh1 noloop
    ms "Me?"
    play sound sfx_cloth_rustling3
    scene sm1cs-mas003-155 ka-lg-close-mas-lg-yeah-flash-us-ka-oh-yeah-do-it_c1 with dissolve
    play voice5 girl35_happy_yeah3 noloop
    lg "Yeah. Flash us your kibble and biscuits."
    play voice4 girl30_yes_yeah2 noloop
    ka "Oh yeah. Do it."
    scene sm1cs-mas003-156 mas-not-flashing-guys-lg-wait-wait_c1 with dissolve
    play voice3 girl28_no_nonono1 noloop
    ms "I'm not flashing you guys."
    play voice5 girl35_hey_angry1 noloop
    lg "Wait, wait."
    play sound sfx_paper_rustl1
    scene sm1cs-mas003-157 lg-holds-money-three-hundos-already-seen-sorority-boobs_c1 with dissolve
    play voice5 girl35_yes_yep3 noloop
    lg "Here. One, two, three hundred dollars."
    lg "I've already seen Olivia and Kennedy's girls."
    play voice6 girl34_no_angry7 noloop
    scene sm1cs-mas003-158 os-no-havent-ka-giggle-naughty-tart_c1 with vpunch
    ols "No you haven't."
    play voice4 girl30_happy_laugh2 noloop
    ka "Lauren, you're such a horny tart."
    scene sm1cs-mas003-159 lg-come-on-party-mas-looking-money-mct-no-way-maya-goes_c1 with dissolve
    play voice5 girl35_hey_attention2 noloop
    lg "Come on, it's a party. I must have my unchained entertainment."
    mct "No way, Maya goes for this."
    play sound sfx_cloth_rustling1
    scene sm1cs-mas003-160 mas-pulls-half-way-shirt-mct-wait-what-mas-make-five-hundred_c1 with dissolve
    play voice2 mc_scared_huh1 noloop
    mct "Wait, what is she doing?"
    play voice3 girl28_arrogant_hah1 noloop
    ms "Make if five hundred."
    scene sm1cs-mas003-161 lg-sold-girls-giggle_c1 with dissolve
    play voice5 girl35_happy_yay2 noloop
    lg "Sold!"
    play voice4 girl30_scared_oh1 noloop
    ka "Lauren, you did not."
    play voice6 girl34_happy_laugh5 noloop
    ols "She's off her bobby."
    scene sm1cs-mas003-162 lg-hush-not-how-say-it_c1 with dissolve
    play voice5 stacy_shhh noloop
    lg "Hush. And that's not at all how you say that."
    play sound sfx_skirt_off2
    scene sm1cs-mas003-a164 mas-topless-girls-cheer-00000 with dissolve
    play voice6 girl34_happy_woohoo1 noloop
    play voice5 girl35_happy_woohoo6 noloop
    play voice4 girl30_happy_surprised noloop
    "Kennedy, Lauren and Olivia" "*cheer widly*"
    play sound sfx_camera_fly1 volume 2.0
    scene sm1cs_mas003-glambot-1
    pause
    stop sound fadeout 1.0
    scene sm1cs-mas003-165 lg-examines-mas-boobs-exquisite_c1 with dissolve
    play voice5 girl35_disgust_oof2 noloop
    lg "Exquisite."
    scene sm1cs-mas003-166 ka-not-bad-os-damn-girl-belong-on-cover_c1 with dissolve
    play voice4 girl30_surprised_wow noloop
    ka "Not bad."
    play voice6 girl34_happy_relief5 noloop
    ols "Damn girl. You belong on a magazine or something."
    scene sm1cs-mas003-167 mas-catches-mc-watching_c1 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1cs-mas003-168 mas-puts-shirt-back-on-show-over-ladies_c1 with dissolve
    play voice3 girl28_yes_yap3 noloop
    ms "Show's over ladies."
    play sound sfx_paper_rustl3
    scene sm1cs-mas003-169 mas-takes-money-lg-again-again_c1 with dissolve
    play voice3 girl28_disappointed_mmm1 noloop
    ms "Thank you."
    play voice5 girl35_yes_yeah3 noloop
    lg "Again again."
    play sound sfx_carpet_footsteps1 loop
    play sound2 sfx_paper_bag_2 noloop
    scene sm1cs-mas003-170 mas-leaves-girls-go-for-food_c1 with dissolve
    play voice5 girl35_disappointed_hiccup noloop
    lg "Cracking. The food is here."
    play sound3 sfx_carpet_run1
    scene sm1cs-mas003-171 mc-hurry-after-mas-leave-building_c1 with dissolve
    pause
    stop sound fadeout 2.0
    stop sound3 fadeout 2.0
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(0.7, 3.5, "music" )
    jump sm1cs_mas003_after_delivery
label sm1cs_mas003_after_delivery:
    play sound sfx_supercar_drive1 fadein 2.0 loop
    scene sm1cs-mas003-172 mc-mas-driving-silence_c1 with Fade(0.5, 0.5, 0.5)
    pause
    play sound2 sfx_car_inside_ride1 fadein 2.0
    $ renpy.music.set_volume(1.0, 2.0, "sound2" )
    $ renpy.music.set_volume(0.0, 2.0, "sound" )
    scene sm1cs-mas003-173 mc-silent-mct-maybe-say-something-_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "Maybe I'll wait for her to say something."
    scene sm1cs-mas003-174 mas-silent-speaks-not-mad_c1 with dissolve
    ms "..."
    play voice3 girl28_disappointed_eeh2 noloop
    ms "I'm not mad."
    scene sm1cs-mas003-176 mc-didnt-think-were-mas-good_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I didn't think you were."
    play voice3 girl26_thinking_ehh1 noloop
    ms "Good."
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    $ renpy.music.set_volume(1.0, 1.0, "sound" )
    scene sm1cs-mas003-177 mc-great-nothing-more-say-then_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Great."
    mc "Nothing more to say then."
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    stop sound fadeout 3.5
    scene sm1cs-mas003-178 mas-fine-by-me-chew-lips-but_c1 with dissolve
    play voice3 girl28_yes_simple noloop
    ms "Fine by me."
    ms "But..."
    scene sm1cs-mas003-179 mas-since-work-together-uneven-you-know_c1 with dissolve
    play voice3 girl26_disappointed_mmh1 noloop
    ms "Since we work together, I feel like things are a little- uneven..."
    ms "You know?"
    scene sm1cs-mas003-180 mc-totally-what-that-means_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Totally."
    mc "What does that mean?"
    scene sm1cs-mas003-181 mas-since-saw-mine-one-day-see-yours_c1 with dissolve
    play voice3 girl28_happy_mmm2 noloop
    ms "Well, since you saw mine, if we want to equal things out..."
    ms "One day, I'll have to see yours."
    play voice2 mc_yes_sure1 noloop
    mc "Sure. Makes sense."
    play sound sfx_cloth_rustling1
    scene sm1cs-mas003-182 mas-not-that-want-see-it-mc-ofc-not_c1 with dissolve
    play voice3 girl28_surprised_oh noloop
    ms "It's not something I {i}want{/i} to see."
    play voice2 mc_no_no2 noloop
    mc "No, of course not."
    scene sm1cs-mas003-183 not-looks-bad-or-good-mc-not-point_c1 with dissolve
    play voice3 girl28_disappointed_geh noloop
    ms "Not that I think it looks bad."
    ms "Or good!"
    play voice2 mc_yes_ugu1 noloop
    mc "Not the point."
    scene sm1cs-mas003-184 mas-professional-mas-point-make-things-equal-mc-oh-always-comfortable_c1 with dissolve
    play voice3 girl28_no_nope4 noloop
    ms "Exactly. The {i}point{/i} is just to make things equal. If you're comfortable with that."
    play voice2 mc_scared_oh4 noloop
    mc "Oh, I'm always comfortable."
    scene sm1cs-mas003-185 mas-turn-intense-tell-nelson-be-in-trouble_c1 with dissolve
    play voice3 girl28_happy_great2 noloop
    ms "Good."
    play voice2 mc_yes_yeah2 noloop
    mc "Great."
    play sound sfx_car_approach1 volume 2.0
    stop sound2 fadeout 2.0
    stop sound3 fadeout 2.0
    play sound4 sfx_distanttraffic_city2 fadein 2.0
    scene sm1cs-mas003-185 mc-mas-stop-front-wurst_c1 with dissolve
    pause
    scene sm1cs-mas003-186 choice-saw-nothing-mc-didnt-see-anything_c1 with dissolve
    play voice3 girl28_arrogant_hmm1 noloop
    ms "Last word. If you say anything to Nelson, you're going to be in huge trouble, [mcname]."
    menu:
        "I saw nothing"(hint="sm1cs_mas003_m04_h01"):
            play voice2 mc_no_uhuh1 noloop
            mc "I saw nothing."
            scene sm1cs-mas003-187 mas-not-believing-him-they-speak-more_c1 with dissolve
            play voice3 girl28_arrogant_hah4 noloop
            ms "Oh yeah. You should work on your lies."
            play voice2 mc_disappointed_ehh5 noloop
            mc "I thought you didn't want to talk about it."
            ms "I don't."
        "Ask for your cut"(hint="sm1cs_mas003_m04_h02"):
            play voice2 mc_thinking_hmm6 noloop
            mc "So... what's my cut for keeping this a secret between us."
            scene sm1cs-mas003-188 choice-ask-extra-mc-how-much-keep-secret-mas-earned-that_c1 with dissolve
            play voice3 girl28_hey_angry noloop
            ms "Hey, I {i}earned{/i} every single dollar of that tip."
            scene sm1cs-mas003-189 mas-think-half-goes-me-mc-why-that_c1 with dissolve
            play voice3 girl28_arrogant_hah3 noloop
            ms "And I think 'your' half still goes to me."
            play voice2 mc_surprised_why3 noloop
            mc "Why's that?"
            scene sm1cs-mas003-190 mas-sexy-think-show-tits-free-mc-fair-point_c1 with dissolve
            play voice3 girl28_arrogant_yeah1 noloop
            ms "Do you think I'd just show you my tits for free, [mcname]?"
            play voice2 mc_thinking_mmm3 noloop
            mc "Fair point."
            play sound sfx_paper_rustl1
            scene sm1cs-mas003-191 mas-handing-money-yanking-chain_c1 with dissolve
            play voice3 girl28_arrogant_hmm2 noloop
            ms "I'm just yanking your chain, [mcname]."
            call sm1cs_mas003_m04_c02 from _call_sm1cs_mas003_m04_c02
    play sound sfx_car_door_closed1
    play sound2 sfx_heels_steps2
    scene sm1cs-mas003-192 mas-quickly-darts-towards-wurst-place_c1 with dissolve
    play voice3 girl28_hey_bye3 noloop
    ms "*rapidly* Okay. Bye. Goodnight."
    play sound sfx_car_door_open1
    stop sound2 fadeout 3.0
    scene sm1cs-mas003-193 mc-watches-after-mas-wondering-end-scene_c1 with dissolve
    pause
    stop sound4 fadeout 2.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "sound2" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1cs_mas003_end
label sm1cs_mas003_end:
    $ StoryController.end_scene_in_time(MAS_STORY, 0, 30, 5)
    return
label sm1cs_mas003_m01_c01:
    $ player.set_choice("sm1cs_mas003_flirt_1")
    $ CharacterController.get_character("ms").add_point()
    return
label sm1cs_mas003_m02_c01:
    $ player.set_choice("sm1cs_mas003_joke")
    return
label sm1cs_mas003_m02_c02:
    $ player.set_choice("sm1cs_mas003_flirt_2")
    $ CharacterController.get_character("ms").add_point()
    return
label sm1cs_mas003_m02_c03:
    $ player.set_choice("sm1cs_mas003_complain")
    $ CharacterController.get_character("ms").deduct_point()
    return
label sm1cs_mas003_m03_c01:
    $ player.set_choice("sm1cs_mas003_play_it_cool")
    $ CharacterController.get_character("ms").add_point()
    return
label sm1cs_mas003_m04_c02:
    $ sm1cs_mas003_tip_cut = 50
    $ player.set_choice("sm1cs_mas003_ask_for_your_cut")
    $ player.add_money(sm1cs_mas003_tip_cut, _("Wurst delivery tip"), _("You got a ${} as your cut of the tip.").format(sm1cs_mas003_tip_cut))
    return