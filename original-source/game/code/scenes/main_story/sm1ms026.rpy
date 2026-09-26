image sm1ms026-a24-glm = Movie(play = "images/ms/s026/anim/sm1ms026-a24-2x-60fps.webm", start_image = "sm1ms026-a24 sy-uh-huh-all-ass-mc-pretty-good-costar-glambot-00", image = "sm1ms026-a24 sy-uh-huh-all-ass-mc-pretty-good-costar-glambot-78_i", loop = False)
label sm1ms026:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music music_mewpeowpeow fadein 1.0 volume 0.75
    if not player.get_choice("sm1ms026_second_movie"):
        scene sm1ms026-01 mc-sy-walk-towards-couch_c1 with dissolve
        play sound sfx_heels_steps1 loop
        play sound2 sfx_barefoot_steps1
        pause
        scene sm1ms026-02 sy-okay-so-been-thinking-mc-oh-yeah_c1 with dissolve
        play voice3 stacy_yes_okay1 noloop
        sy "Okay, so I've been thinking a lot about this-"
        play voice2 mc_yes_yeah8 noloop
        mc "Oh yeah?"
        play sound sfx_sand_jump1 volume 2.0
        play sound2 sfx_epic_jump1 volume 2.0 noloop
        scene sm1ms026-03 sy-shut-up-im-on-roll_c1 with dissolve
        play voice3 stacy_angry noloop
        sy "Shut up, [mcname], because I'm on a roll."
        scene sm1ms026-04 sy-jumps-couch-first-need-idea-mc-thought-had-idea_c1 with dissolve
        play voice3 stacy_happy_wooh1 noloop
        sy "So, before we can really get into the preproduction for the films, we need to have an idea."
        play voice2 mc_surprised_uh1 noloop
        mc "I thought we already had an idea?"
        play sound sfx_cloth_planket3
        scene sm1ms026-05 sy-mean-yeah-have-general-theme_c1 with dissolve
        play voice3 stacy_thinking_emm1 noloop
        sy "I mean, yeah, we have like a general theme, sure, but before we get too into it, I think we need to figure out the elephant in the room."
        play sound sfx_cloth_rustling4
        scene sm1ms026-06 mc-hey-thought-slimming-sy-hahaha-comedian_c1 with dissolve
        play voice2 mc_hey_hey3 noloop
        mc "Hey! I thought I was slimming down nicely, thank you!"
        play voice3 stacy_arrogant_laugh1 noloop
        sy "Ha, ha, Mr. Comedian - no, I'm talking about the {i}other{/i} elephant in the room."
        scene sm1ms026-07 sy-serious-mc-which-is-sy-who-gonna-cast_c1 with dissolve
        play voice2 mc_thinking_hmm2 noloop
        mc "Which is?"
        play voice3 stacy_thinking_hmm4 noloop
        sy "Who are we going to cast in our movies."
        play sound sfx_cloth_rustling3
        scene sm1ms026-08 mc-ah-sy-since-talent-scout-figures-should-talk-together_c1 with dissolve
        play voice2 d1s5b_ehhh noloop
        mc "Ahhh."
        play voice3 stacy_yes_ugu1 noloop
        sy "And since you're our \"talent scout\", I figured we should talk about this together."
        mc "Right, right."
        scene sm1ms026-09 sy-should-also-figure-kinky-mc-got-point-there_c1 with dissolve
        play voice3 stacy_thinking_oh1 noloop
        sy "We should also maybe figure out if we want to do anything kinky in the movies. Because everyone has their own kinks they like."
        play voice2 mc_yes_yes2 noloop
        mc "You've got a good point there..."
        scene sm1ms026-10 sy-so-which-movie-want-figure-first_c1 with dissolve
        play voice3 stacy_surprised_huh1 noloop
        sy "So, which movie do you want to figure out first?"
    jump sm1ms026_movie
label sm1ms026_movie:
    scene sm1ms026-11 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Pirates" if not player.get_choice("sm1ms026_pirates"):
            $ player.set_choice("sm1ms026_pirates")
            if player.get_choice("sm1ms026_second_movie"):
                $ player.set_choice("second_movie", "pirates_movie")
            else:
                $ player.set_choice("first_movie", "pirates_movie")
            scene sm1ms026-12 choice-pirates-mc-look-mc-lets-start-pirates_c1 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "Let's start with pirates."
            jump sm1ms026_pirates
label sm1ms026_pirates:
    scene sm1ms026-14 sy-excited-hell-yeah-so-pirates-mc-yeah-all-sounds-great_c1 with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "Hell yeah. So - pirates - hot chicks, sword fights, booty, booty, booty!"
    play voice2 mc_happy_yes1 noloop
    mc "Yeah! That all sounds great!"
    scene sm1ms026-15 sy-well-first-question-how-kinky_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, I guess the first question is, how kinky do we want to be?"
    scene sm1ms026-16 mc-already-lots-action-sy-agreed_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Well, there's already a lot of action in the movie... so maybe we don't have to get too crazy with it?"
    play voice3 stacy_yes_yap1 noloop
    sy "Agreed."
    scene sm1ms026-17 mc-what-about-choking-sy-oh-yeah_c1 with dissolve
    play voice2 d1s2_hmm noloop
    mc "What about some choking stuff?"
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh yeah?"
    scene sm1ms026-18 mc-mean-pirates-intro-ropes-shit_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "I mean... the pirates were into ropes and shit. I feel like they might like a little choke and stroke."
    scene sm1ms026-19 sy-covering-mouth-mc-what-sy-that-so-dark_c1 with dissolve
    play voice3 stacy_pain_huh1 noloop
    play voice2 mc_surprised_uh2 noloop
    mc "What?"
    play voice3 stacy_disappointed_mmm1 noloop
    sy "That is {i}so{/i} dark, [mcname]."
    scene sm1ms026-20 mc-is-it-shit-wait_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Is it?{w} Oh wait- shit!"
    scene sm1ms026-21 sy-devilish-smirk-love-it-sy-alright-choking_c1 with dissolve
    play voice3 stacy_suckmoan3 noloop
    sy "But I love it."
    sy "All right. Choking. Now we just need a star!"
    scene sm1ms026-22 yeah-who-cast-pirater-theme_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah... who to cast in a pirate themed porno..."
    play sound sfx_hair_scratch1
    scene sm1ms026-23 sy-playing-braid-know-think-be-pretty-hot-pirate-mc-oh-yeah_c1 with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "You know... I think I would look pretty hot as a pirate villain."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh yeah?"
    play sound sfx_camera_fly1 volume 2.0
    scene sm1ms026-a24 sy-uh-huh-all-ass-mc-pretty-good-costar-glambot-00 with dissolve
    pause 0.01
    scene sm1ms026-a24-glm
    play voice3 stacy_angryhuh noloop
    sy "Uh huh. All ass, swinging a sword... you know, being a baddie."
    play voice2 mc_thinking_mmm4 noloop
    mc "And you are a pretty good costar..."
    play sound [sfx_hands_clap4, sfx_hands_clap2] volume 0.75
    scene sm1ms026-25 excited-does-mean-pirate-villain-mc-didnt-say-get-part_c1 with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "Does that mean I can be the pirate villain! Yay! Yayayayayayay!"
    play voice2 mc_no_uhuh1 noloop
    mc "Now hang on, I didn't say you could get the part."
    scene sm1ms026-26 sy-what-you-kidding-mc-yes_c1 with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "What! Are you kidding me!?"
    play voice2 mc_yes_yeah1 noloop
    mc "...{w}Yes."
    play sound sfx_cloth_rustling3
    scene sm1ms026-27 mc-ofc-can-be-pirate-villain_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Of course you can be the pirate villain, Stacy."
    play sound sfx_skirt_off2
    scene sm1ms026-28 sy-playful-slap-jerk-mc-come-on-had-to_c1 with dissolve
    play voice3 stacy_angry_argh3 noloop
    sy "Jerk!"
    play voice2 mc_hey_hey6 noloop
    mc "Come on, I had to."
    scene sm1ms026-29 sy-not-that-funny_c1 with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "Big ol meanie!"
    play sound sfx_cloth_rustling4
    scene sm1ms026-30 mc-smiling-we-have-villain-cast-now-lead-sy-picture-badass_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, so we have our villain cast, now we just need a lead actress..."
    play voice3 stacy_yes_yap2 noloop
    sy "Yeah. I'm picturing... a total bad ass."
    mc "Same. And tall... you know, someone striking on camera."
    scene sm1ms026-31 mc-same-tall-sy-what-if-pale_c1 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "What if she was pale?"
    play voice2 mc_surprised_huh7 noloop
    mc "Huh?"
    scene sm1ms026-32 mc-confused-huh-sy-knowo-tall-pale-tattoos_c1 with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "You know, tall, pale, bad ass. Oooo! With tattoos!"
    play sound sfx_cloth_rustling2
    scene sm1ms026-33 mc-tattoes-piraty-sy-exactly_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, I mean, tattoos are pirate-y?"
    play voice3 stacy_yes_yap3 noloop
    sy "Exactly!"
    scene sm1ms026-34 sy-you-know-someone-like-that-mc-sound-like-tl_c1 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "Do you know anyone like that?"
    if player.has_played_scene("sm1cs_tl003"):
        play voice2 mc_thinking_hmm5 noloop
        mc "You know... that sounds exactly like Taisia."
        scene sm1ms026-35 sy-excited-totally-does-and-badass-_c1 with dissolve
        play voice3 stacy_surprised_oh1 noloop
        sy "You're right, it totally does."
        sy "And she's a bad ass."
        scene sm1ms026-36 mc-so-taisia-sy-this-she-perfect_c1 with dissolve
        play voice2 mc_thinking_hmm4 noloop
        mc "So... Taisia?"
        play voice3 stacy_yes_yeah1 noloop
        sy "I think she's perfect!"
        if player.has_played_scene("sm1cs_tl007"):
            scene sm1ms026-37 mc-excited-now-she-lives-here-easier-sy-that-does-talk-her_c1 with dissolve
            play voice2 mc_yes_yeah7 noloop
            mc "Yeah, and now she lives with us, which makes it sooo much easier."
            play voice3 stacy_thinking_hmm2 noloop
            sy "That it does! So you'll talk to her?"
            mc "Absolutely."
        else:
            scene sm1ms026-38 mc-thinking-dont-know-super-pumped-sy-what-think-talent-scout_c1 with dissolve
            play voice2 mc_thinking_hmm3 noloop
            mc "I don't know... I know she's super pumped to film, but if she is the star, we'd be relying on her a lot."
            play voice3 stacy_thinking_hmm2 noloop
            sy "Well, you get to make the final call, Mr. Talent Scout."
            mc "I think I need to get to know her a little better before I can sign off on bringing her on as our star."
            scene sm1ms026-39 mc-think-know-better-tl-sy-this-your-are-your-call_c1 with dissolve
            play voice3 stacy_hey_happy2 noloop
            sy "Hey, this is your area of expertise. What you say goes!"
    else:
        scene sm1ms026-40 mc-hard-thinking-looking-sy-mc-mean-feel-like-seen-sy-sounds-like-need-scout-talent_c1 with dissolve
        play voice2 mc_thinking_hmm5 noloop
        mc "I mean... I feel like I've seen someone around who would fit the bill... but I can't say for sure."
        play voice3 stacy_thinking_hmm2 noloop
        sy "Sounds like you need to get out there and do some talent scouting!"
        if not player.get_choice("sm1ms026_scifi"):
            scene sm1ms026-41 sy-smiling-mc-choice-menu-screen_c1 with dissolve
            menu:
                "Talk about Sci Fi film":
                    $ player.set_choice("sm1ms026_scifi")
                    scene sm1ms026-42 choice-scifi-mc-lets-talk-scifi-sy-deff-should_c1 with dissolve
                    play voice2 mc_thinking_hmm3 noloop
                    mc "Should we talk about our sci fi film?"
                    play voice3 stacy_hey_happy2 noloop
                    sy "We definitely should!"
                    jump sm1ms026_scifi
                "That's enough planning for now":
                    pass
    jump sm1ms026_end
label sm1ms026_scifi:
    scene sm1ms026-43 sy-leans-mc-sy-aight-hot-aliens-blasters-space-battles-mc-have-pick-kind-scifi_c1 with dissolve
    play voice3 stacy_disappointed_oh6 noloop
    sy "All right, sci fi. Hot aliens, blasters, space battles-"
    scene sm1ms026-44 sy-what-mean-mc-suerious-trekkie-or-starwars_c1 with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, we have to pick what kind of sci fi we want to do."
    play voice3 stacy_arrogant_huh2 noloop
    sy "What do you mean?"
    mc "Well, are we going to go the trekkie route? Or are we doing laser swords?"
    scene sm1ms026-45 aah-get-you-nerd-mc-what-this-big-decision_c1 with dissolve
    play voice3 stacy_disappointed_ehh4 noloop
    sy "Ahhh, I get it, you nerd."
    play voice2 mc_thinking_hmm6 noloop
    mc "What! This is a big decision!"
    play sound sfx_cloth_rustling3
    scene sm1ms026-46 sy-picturing-hot-uniforms-mc-trekkie-route_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, I'm picturing the hot uniforms, and like the big starship bridge-"
    play voice2 mc_yes_ugu1 noloop
    mc "So then the trekkie route."
    scene sm1ms026-47 sy-yeah-nerd-mc-hey-important_c1 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Yeah.{w} Nerd."
    play voice2 mc_hey_hey9 noloop
    mc "Hey! It's important!"
    scene sm1ms026-48 sy-know-know-mc-what-thinking_c1 with dissolve
    play voice3 stacy_yeahno noloop
    sy "I know, I know. Okay, so intrepid space explorers. Do you think we should make this movie a little kinkier?"
    play voice2 mc_thinking_hm noloop
    mc "What are you thinking?"
    scene sm1ms026-49 sy-shrugs-dunno-maybe-watersports-mc-yeah-works-for-me_c1 with dissolve
    play voice3 stacy_no_nah1 noloop
    sy "I don't know... maybe watersports? Watersports seems to be a thing people like."
    play voice2 mc_yes_yes3 noloop
    mc "Yeah, that works for me. We can probably come up with some crazy reasons why people need to pee. Maybe it's like an alien courting ritual?"
    scene sm1ms026-50 sy-love-idea-for-actress-smart-say-bunch-words_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "Love that idea."
    sy "For actresses... I feel like we want smart people."
    sy "You know, so they can say a bunch of science words that sound really fancy."
    jump sm1ms026_end
label sm1ms026_end:
    play sound sfx_cloth_rustling1
    scene sm1ms026-51 sy-stands-up-alright-go-out-get-stars_c1 with dissolve
    play voice3 stacy_yes_fine1 noloop
    sy "All right! Casting is kind of the big thing we need to do before we start filming. So go out and get us our lead actress!"
    play sound sfx_cloth_rustling5
    scene sm1ms026-52 mc-stands-up-youstart-everything-what-would-do-without-you_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "On it. And you'll get everything else we need figured out?"
    play voice3 stacy_yes_yap1 noloop
    sy "Bingo."
    if persistent.is_special:
        mc "What would I do without you, little sister?"
    else:
        mc "What would I do without you, Stacy?"
    play sound sfx_barefoot_steps1
    scene sm1ms026-53 sy-walk-away-god-only-knows-end-scene_c1 with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "God only knows..."
    stop sound fadeout 1.0
    jump sm1ms026_end_scene
label sm1ms026_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    if player.get_choice("sm1ms026_pirates"):
        $ StoryController.activate_story_line(MOVIE_PIRATES, True)
    $ StoryController.end_scene(MS, 1, 0, 1)
    return