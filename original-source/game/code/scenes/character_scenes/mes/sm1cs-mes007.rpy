image sm1cs-mes007-a63-glam = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a63-3x-60fps.webm", start_image = "sm1cs-mes007-a63 mes-kneeling-on-bed-glambot-00", image = "sm1cs-mes007-a63 mes-kneeling-on-bed-glambot-90", loop = False)
image sm1cs-mes007-a77-1 = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a77-1-2x-50fps.webm", start_image = "sm1cs-mes007-a77-1 mc-mes-rev-cgirl-anim-01")
image sm1cs-mes007-a77-1-f = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a77-1-2x-60fps.webm", start_image = "sm1cs-mes007-a77-1 mc-mes-rev-cgirl-anim-01")
image sm1cs-mes007-a77-2 = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a77-2-2x-50fps.webm", start_image = "sm1cs-mes007-a77-2 mc-mes-rev-cgirl-anim-01")
image sm1cs-mes007-a77-2-f = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a77-2-2x-60fps.webm", start_image = "sm1cs-mes007-a77-2 mc-mes-rev-cgirl-anim-01")
image sm1cs-mes007-a77-3 = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a77-3-2x-50fps.webm", start_image = "sm1cs-mes007-a77-3 mc-mes-rev-cgirl-anim-01")
image sm1cs-mes007-a77-3-f = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a77-3-2x-60fps.webm", start_image = "sm1cs-mes007-a77-3 mc-mes-rev-cgirl-anim-01")
image sm1cs-mes007-a77-4 = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a77-4-2x-50fps.webm", start_image = "sm1cs-mes007-a77-4 mc-mes-rev-cgirl-anim-01")
image sm1cs-mes007-a77-4-f = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a77-4-2x-60fps.webm", start_image = "sm1cs-mes007-a77-4 mc-mes-rev-cgirl-anim-01")
image sm1cs-mes007-a78-1 = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a78-1-2x-50fps.webm", start_image = "sm1cs-mes007-a78-1 mc-mes-sideways-anim-01")
image sm1cs-mes007-a78-1-f = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a78-1-2x-60fps.webm", start_image = "sm1cs-mes007-a78-1 mc-mes-sideways-anim-01")
image sm1cs-mes007-a78-2 = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a78-2-2x-50fps.webm", start_image = "sm1cs-mes007-a78-2 mc-mes-sideways-anim-01")
image sm1cs-mes007-a78-2-f = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a78-2-2x-60fps.webm", start_image = "sm1cs-mes007-a78-2 mc-mes-sideways-anim-01")
image sm1cs-mes007-a78-3 = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a78-3-2x-50fps.webm", start_image = "sm1cs-mes007-a78-3 mc-mes-sideways-anim-01")
image sm1cs-mes007-a78-3-f = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a78-3-2x-60fps.webm", start_image = "sm1cs-mes007-a78-3 mc-mes-sideways-anim-01")
image sm1cs-mes007-a78-4 = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a78-4-2x-50fps.webm", start_image = "sm1cs-mes007-a78-4 mc-mes-sideways-anim-01")
image sm1cs-mes007-a78-4-f = Movie(play = "images/Character-Scenes/MES/s007/anim/sm1cs-mes007-a78-4-2x-60fps.webm", start_image = "sm1cs-mes007-a78-4 mc-mes-sideways-anim-01")
label sm1cs_mes007:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    scene sm1cs-mes007-01 mc-mes-entering_c2 with dissolve
    play music music_high_fly
    play voice3 min_happy_relief noloop
    mes "Moving day. Ready to put those long legs to good use."
    scene sm1cs-mes007-01 mc-mes-entering_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yes."
    scene sm1cs-mes007-02 mes-smiling_c1 with dissolve
    pause
    scene sm1cs-mes007-03 mc-mes-talking_c1 with dissolve
    play voice3 min_arrogant_heh2 noloop
    mes "I really appreciate this, [mcname]."
    scene sm1cs-mes007-03 mc-mes-talking_c2 with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "You're my tenant. Happy to help."
    play sound sfx_cloth_rustling2
    scene sm1cs-mes007-04 mc-mes-flirting_c1 with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "Just your tenant?"
    scene sm1cs-mes007-04 mc-mes-flirting_c2 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Haha. You're never just anything, Min."
    mc "You're spectacular."
    scene sm1cs-mes007-04 mc-mes-flirting_c3 with dissolve
    play voice3 min_happy_laugh3 noloop
    mes "Haha. Trying to butter me up?"
    play voice2 mc_thinking_hmm2 noloop
    mc "Always."
    mes "Save it for after loverboy. We have a lot of work to do."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps1
    scene sm1cs-mes007-05 mc-mes-walking-away_c1 with dissolve
    pause
    play sound sfx_door_open1
    play sound2 sfx_bus_startmove noloop
    $ renpy.music.set_volume(1.0, 3.5, "music" )
    scene black
    show screen scene_transistion(_("Over at Min's house"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    stop sound2 fadeout 2.0
    play sound4 sfx_parkday_birds fadein 1.5
    scene sm1cs-mes007-06 mc-mes-montage-at-her-place_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-mes007-07 mc-mes-montage-at-her-place_c1 with dissolve
    pause
    scene sm1cs-mes007-08 mc-mes-montage-at-her-place_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.6, 2.5, "music" )
    scene sm1cs-mes007-09 mc-mes-boxing-up_c1 with fade
    play voice2 mc_arrogant_heh1 noloop
    mc "That it?"
    scene sm1cs-mes007-09 mc-mes-boxing-up_c2 with dissolve
    play voice3 min_yes_ugu noloop
    mes "Mmhmm."
    mes "Now we just load these into the truck."
    scene sm1cs-mes007-09 mc-mes-boxing-up_c3 with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "You have a lot of stuff."
    play voice3 min_thinking_oh noloop
    mes "Most of it is just going into storage."
    mc "Cool."
    stop sound4 fadeout 1.0
    play sound3 sfx_car_startmove noloop
    scene sm1cs-mes007-10 mc-mes-taking-up-box_c1 with Fade(0.5, 0.5, 0.5)
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    play voice2 mc_pain_auh5 noloop
    pause
    scene sm1cs-mes007-10 mc-mes-taking-up-box_c2 with dissolve
    play voice3 min_hey_greeting noloop
    mes "Careful with those."
    play voice2 mc_yes_yeah7 noloop
    mc "Of course, I am always careful."
    play voice2 mc_pain_argh1 noloop
    play voice4 stacy_scared_ah4 noloop
    play sound sfx_leg_kick2
    play sound2 sfx_box_slide noloop
    play sound3 sfx_phone_fall1 noloop
    play sound4 sfx_epic_jump1 noloop
    scene sm1cs-mes007-11 mc-mes-sy-bumping-into-her_c1 with hpunch
    sy "Bah."
    play sound sfx_fall_down1
    play sound2 sfx_leg_kick1 noloop
    scene sm1cs-mes007-12 mc-mes-sy-on-ground-sorry_c1 with vpunch
    play voice4 stacy_hey_angry1 noloop volume 1.4
    sy "Hey. I'm walking here!"
    scene sm1cs-mes007-12 mc-mes-sy-on-ground-sorry_c2 with dissolve
    play voice2 mc_pain_mff1 noloop volume 1.4
    mc "Shit. Sorry Stacy."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes007-13 mc-mes-sy-talking_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Got a little distracted."
    scene sm1cs-mes007-13 mc-mes-sy-talking_c2 with dissolve
    play voice4 stacy_yes_yeah1 noloop
    sy "It's okay."
    sy "Let me know if I can help with anything."
    scene sm1cs-mes007-13 mc-mes-sy-talking_c3 with dissolve
    play voice3 min_no_nah noloop
    mes "Thanks Stacy. But [mcname] and I have it handled."
    play voice4 stacy_happy_relief1 noloop
    sy "Cool, then I'll give you two some space."
    play sound sfx_heels_steps1
    play sound2 sfx_armored_footsteps1
    scene sm1cs-mes007-14 mc-mes-talking_c1 with dissolve
    play voice2 mc_angry_errr6 noloop
    mc "*grunting*"
    scene sm1cs-mes007-14 mc-mes-talking_c2 with dissolve
    play voice3 min_happy_mmm noloop
    mes "So glad to have a big strong man to help me out."
    scene sm1cs-mes007-15 mc-mes-talking_c1 with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah. I don't want you getting squished."
    scene sm1cs-mes007-15 mc-mes-talking_c2 with dissolve
    play voice3 min_no_uhuh noloop
    mes "I'm small but not {i}that{/i} small."
    scene sm1cs-mes007-16 mc-mes-opening-door_c1 with dissolve
    play voice3 min_hey_angry1 noloop
    mes "And you lugging the big stuff save me the trouble of building an elaborate pulley and winch system that might damage the studio."
    play sound sfx_door_open5
    stop sound2 fadeout 1.0
    scene sm1cs-mes007-16 mc-mes-opening-door_c2 with dissolve
    play voice2 d2s12_emmm noloop volume 1.6
    mc "Also a plus."
    play voice3 min_old_laugh noloop
    mes "Heh."
    scene sm1cs-mes007-17 mc-mes-in-her-room_c1 with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "Home sweet home."
    scene sm1cs-mes007-17 mc-mes-in-her-room_c2 with dissolve
    play voice3 min_yes_yeah2 noloop
    mes "It will be."
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1cs-mes007-18 mc-mes-montage-taking-boxes-in_c1 with fade
    pause
    scene sm1cs-mes007-19 mc-mes-montage-taking-boxes-in_c1 with fade
    pause
    scene sm1cs-mes007-20 mc-mes-montage-taking-boxes-in_c1 with fade
    pause
    scene sm1cs-mes007-21 mc-mes-montage-taking-boxes-in_c1 with fade
    pause
    scene sm1cs-mes007-22 mc-mes-montage-taking-boxes-in_c1 with fade
    pause
    $ renpy.music.set_volume(0.6, 2.5, "music" )
    scene sm1cs-mes007-23 mc-mes-talking_c1 with fade
    play voice2 mc_yes_okay2 noloop volume 1.6
    mc "Alright, we're on the home stretch now."
    scene sm1cs-mes007-23 mc-mes-talking_c2 with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "Tut tut tut."
    mes "You get to clock out now, [mcname]."
    scene sm1cs-mes007-24 mc-mes-talking_c1 with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "Huh?"
    scene sm1cs-mes007-24 mc-mes-talking_c2 with dissolve
    play voice3 min_yes_aga noloop
    mes "This is my room, so I need to get it all set up myself."
    scene sm1cs-mes007-25 mc-mes-talking_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "You're kicking me out."
    scene sm1cs-mes007-25 mc-mes-talking_c2 with dissolve
    play voice3 min_thinking_oh noloop
    mes "Temporarily."
    menu:
        "What if I demand to stay":
            $ player.set_choice("sm1cs_mes007_demand_to_stay")
            play sound sfx_cloth_rustling2 volume 2.0
            scene sm1cs-mes007-26 mc-mes-demand-to-stay_c1 with dissolve
            play voice2 mc_angry_hm1 noloop
            mc "And what if I demand to stay?"
            scene sm1cs-mes007-26 mc-mes-demand-to-stay_c2 with dissolve
            play voice3 min_thinking_hmm2 noloop
            mes "Then I will 'politely' decline your entry."
            scene sm1cs-mes007-26 mc-mes-demand-to-stay_c3 with dissolve
            play voice3 min_disappointed_ehh2 noloop
            mes "And remind you that under Crowning City Statute 616, a paying tenant does not have to surrender access to anyone."
            mes "Landowner included."
            mes "Without thirty days written notice. So you can fill out form 1088-12a, and start a month of waiting."
            play sound sfx_cloth_rustling3
            scene sm1cs-mes007-27 mc-mes-lawyered_c1 with dissolve
            play voice3 min_surprised_ehh2 noloop
            mes "Or just wait until I am ready to show you my new room."
            mes "Sounds fair, doesn't it?"
            play sound sfx_hands_clap2
            scene sm1cs-mes007-27 mc-mes-lawyered_c2 with dissolve
            play voice2 mc_yes_yes4 noloop
            mc "Yes. Maybe this will teach me to play business hardball with you."
            scene sm1cs-mes007-27 mc-mes-lawyered_c3 with dissolve
            play voice3 min_thinking_mhh noloop
            mes "I hope not. I like beating you on the field."
            play sound sfx_leg_kick5
            play voice2 mc_angry_errr2 noloop
            scene sm1cs-mes007-28 mc-mes-pulling-her-in_c1 with dissolve
            play voice3 min_thinking_hmm1 noloop
            mes "Makes me imagine I will receive a... {i}punishing{/i} offer later."
            mes "In the future."
            scene sm1cs-mes007-28 mc-mes-pulling-her-in_c2 with dissolve
            play voice2 mc_happy_hah2 noloop
            mc "Haha."
            mc "Count on it."
        "As you wish":
            scene sm1cs-mes007-29 mc-mes-as-you-wish_c1 with dissolve
            play voice2 mc_disappointed_ehh3 noloop
            mc "As you wish."
            scene sm1cs-mes007-29 mc-mes-as-you-wish_c2 with dissolve
            play voice3 min_yes_yeah1 noloop
            mes "Thank you, farmboy."
    play sound sfx_heels_steps2 loop
    scene sm1cs-mes007-30 mc-mes-walking-out_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-mes007-31 mc-mes-are-you-sure_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "You're really serious?"
    mc "You don't want me to help unpacking?"
    scene sm1cs-mes007-31 mc-mes-are-you-sure_c2 with dissolve
    play voice3 min_yes_yeah2 noloop
    mes "I'm all good."
    scene sm1cs-mes007-32 mc-mes-all-set_c1 with dissolve
    play voice3 min_thinking_emm noloop
    mes "I just."
    mes "I have to do this my way, [mcname]."
    scene sm1cs-mes007-32 mc-mes-all-set_c2 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure but, I can just do what you ask."
    scene sm1cs-mes007-32 mc-mes-all-set_c3 with dissolve
    play voice3 min_no_nope noloop
    mes "That won't be necessary."
    mes "I just want our lines of demarcation to be clear."
    mes "This is your home, but this is going to be my home within you home."
    menu:
        "Lines of demar-what?":
            scene sm1cs-mes007-33 mc-mes-talking_c1 with dissolve
            play voice2 mc_surprised_uh2 noloop
            mc "Lines of defenestration?"
            mc "You're going to throw me out a window?!"
            scene sm1cs-mes007-33 mc-mes-talking_c2 with dissolve
            play voice3 min_surprised_what noloop
            mes "What?"
            scene sm1cs-mes007-34 mes-giggling_c1 with dissolve
            play voice3 min_disappointed_off noloop
            mes "No. I'm not throwing you anywhere."
            mes "Well, except out of my room."
            mes "I just want to make sure we have clear boundaries between us."
            scene sm1cs-mes007-35 mes-mc-being-cute_c1 with dissolve
            play voice3 min_hey_simple noloop
            mes "We're already together, [mcname]."
            mes "But I still need some things that are really my own."
            scene sm1cs-mes007-35 mes-mc-being-cute_c2 with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "Alright. I can get behind that."
        "I'm excited to see what you come up with":
            $ player.set_choice("sm1cs_mes007_excited_to_see")
            scene sm1cs-mes007-36 mes-mc-understanding_c1 with dissolve
            play voice2 mc_yes_yeah2 noloop
            mc "Cool cool."
            mc "Well I'm excited to see what you come with, Min."
            mc "I know its going to be great."
            scene sm1cs-mes007-37 mes-smiling_c1 with dissolve
            pause
            play sound sfx_cloth_rustling4
            scene sm1cs-mes007-38 mc-mes-hugging_c1 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            pause
            scene sm1cs-mes007-38 mc-mes-hugging_c2 with dissolve
            play voice3 min_happy_relief noloop
            mes "You're the best, [mcname]."
            scene sm1cs-mes007-39 mc-mes-kissing_c1 with dissolve
            play voice3 min_thinking_mhh noloop
            play sound dahlia_kiss_french1
            play voice2 mc_thinking_mmm1 noloop
            mes "Mmm."
            scene sm1cs-mes007-40 mc-happy_c1 with dissolve
            play voice2 mc_thinking_hmm4 noloop
            mc "Well I have the best girlfriend to motivate me."
            scene sm1cs-mes007-41 mc-mes-talking_c1 with dissolve
            play voice3 min_surprised_huh1 noloop
            mes "Don't you mean girlfriends?"
            scene sm1cs-mes007-41 mc-mes-talking_c2 with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "Haha. I try not to bring up how much of a harem I have when I'm with you."
            play sound sfx_cloth_rustling2
            scene sm1cs-mes007-42 mc-mes-horny_c1 with dissolve
            play voice3 min_arrogant_hm noloop
            mes "Ah. I don't mind it, [mcname]."
            mes "I know I'll always get my share of you."
            mes "And being one of your free-use sex dolls...."
            mes "Well if I didn't have better control, I might have jumped you already."
            scene sm1cs-mes007-42 mc-mes-horny_c2 with dissolve
            play voice2 mc_happy_hah1 noloop
            mc "Curse your good control."
            scene sm1cs-mes007-43 mc-mes-bye_c1 with dissolve
            play voice3 min_happy_laugh4 noloop
            mes "Hahaha."
            mes "Bye now, [mcname]. I'll come get you when it's done."
            scene sm1cs-mes007-43 mc-mes-bye_c2 with dissolve
            play voice2 mc_yes_yes7 noloop
            mc "Perfect."
    jump sm1cs_mes007_continue
label sm1cs_mes007_continue:
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene black
    show screen scene_transistion(_("Three hours later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_paper_rustl1 volume 1.5
    $ renpy.music.set_volume(0.6, 2.5, "music" )
    scene sm1cs-mes007-44 mc-reading_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-mes007-45 mc-mes-showtime_c1 with dissolve
    play voice3 min_happy_yay noloop
    mes "It's ready."
    scene sm1cs-mes007-45 mc-mes-showtime_c2 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What is ready?"
    scene sm1cs-mes007-46 mc-mes-talking_c1 with dissolve
    play voice3 min_happy_mmm noloop volume 1.5
    mes "My room."
    scene sm1cs-mes007-46 mc-mes-talking_c2 with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Oh yeah. Let's check it out."
    play sound sfx_door_openclosed1
    scene sm1cs-mes007-47 mc-mes-impressed_c1 with fade
    play voice2 mc_surprised_wow2 noloop
    mc "You outdid yourself."
    scene sm1cs-mes007-47 mc-mes-impressed_c2 with dissolve
    pause
    play sound sfx_heels_steps1
    scene sm1cs-mes007-48 mc-mes-showing-him-her-collection_c1 with dissolve
    play voice3 min_happy_yeah noloop
    mes "Thanks. As you can see, this is the naughty area."
    scene sm1cs-mes007-48 mc-mes-showing-him-her-collection_c2 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I do. Nice to see the old playmount."
    scene sm1cs-mes007-49 mc-mes-showing-him-her-collection_c1 with dissolve
    play voice3 min_yes_ugu noloop
    mes "I'm sure we'll have some more fun with it."
    stop sound fadeout 1.0
    scene sm1cs-mes007-50 mc-mes-showing-him-her-collection_c1 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "Here is where I do most of my schoolwork."
    scene sm1cs-mes007-50 mc-mes-showing-him-her-collection_c2 with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "Good girl, keeping studies in mind."
    play voice3 min_happy_laugh2 noloop
    mes "Haha."
    play sound sfx_heels_steps1
    scene sm1cs-mes007-51 mc-mes-crossing_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-mes007-52 mc-mes-at-her-dresser_c1 with dissolve
    pause
    play sound sfx_door_slide2 volume 2.5
    scene sm1cs-mes007-53 mc-mes-opening-the-drawer_c1 with dissolve
    play voice3 min_disappointed_mph noloop
    mes "And here is where I keep all the hot stuff."
    scene sm1cs-mes007-54 mc-mes-warning_c1 with dissolve
    play voice3 min_angry_cough noloop
    mes "You are not allowed to steal any of my panties, [mcname]."
    mes "But I will allow you to borrow one for your collection."
    scene sm1cs-mes007-54 mc-mes-warning_c2 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Hmmm."
    menu:
        "Red":
            $ player.set_choice("sm1cs_mes007_panty_choice", "red")
            play sound sfx_skirt_off1 volume 1.6
            scene sm1cs-mes007-55 mc-mes-picking-red_c2 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "I love some red hot panties."
            scene sm1cs-mes007-55 mc-mes-picking-red_c1 with dissolve
            pause
        "Black":
            $ player.set_choice("sm1cs_mes007_panty_choice", "black")
            play sound sfx_skirt_off1 volume 1.6
            scene sm1cs-mes007-56 mc-mes-picking-black_c2 with dissolve
            play voice2 mc_thinking_hmm5 noloop
            mc "Always bet on black."
            scene sm1cs-mes007-56 mc-mes-picking-black_c1 with dissolve
            pause
        "Pink":
            $ player.set_choice("sm1cs_mes007_panty_choice", "pink")
            play sound sfx_skirt_off1 volume 1.6
            scene sm1cs-mes007-57 mc-mes-picking-pink_c2 with dissolve
            play voice2 mc_thinking_hmm4 noloop
            mc "You're always pretty in pink."
            scene sm1cs-mes007-57 mc-mes-picking-pink_c1 with dissolve
            pause
        "I don't need one":
            $ player.set_choice("sm1cs_mes007_panty_choice", None)
            scene sm1cs-mes007-58 mc-mes-picking-none_c2 with dissolve
            play voice2 mc_happy_a1 noloop
            mc "I appreciate, Min. But my favoite thing about panties is when I pull them off you."
            scene sm1cs-mes007-58 mc-mes-picking-none_c1 with dissolve
            play voice3 min_yes_ugu noloop
            mes "Mmhmmm."
    play sound sfx_door_slide6
    play sound2 sfx_heels_steps1
    scene sm1cs-mes007-59 mc-mes-going-to-bed_c1 with dissolve
    pause
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-mes007-60 mc-mes-talking_c1 with dissolve
    play voice3 min_pain_ah noloop
    mes "And of course, this is where the magic happens."
    mes "Or... where it {i}will{/i} happen."
    scene sm1cs-mes007-60 mc-mes-talking_c2 with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Huh. I don't think I ever saw your own room in your old home."
    mc "Apart from today."
    play sound sfx_cloth_rustling2
    scene sm1cs-mes007-61 mc-mes-standing_c1 with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "Mmhmm."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes007-62 mc-mes-taking-her-clothes-off_c1 with dissolve
    pause
    play sound2 sfx_cloth_rustling3 noloop
    scene sm1cs-mes007-a63 mes-kneeling-on-bed-glambot-00 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    scene sm1cs-mes007-a63-glam
    pause
    play voice3 min_thinking_hmm2 noloop
    mes "Curious."
    mes "*soft humming*"
    scene sm1cs-mes007-64 mc-mes-kneeling-in-undies_c1 with dissolve
    pause
    play sound sfx_cloth_rustling3
    scene sm1cs-mes007-65 mc-mes-inviting-him_c1 with dissolve
    pause
    scene sm1cs-mes007-66 mc-mes-closer_c1 with dissolve
    play voice3 min_happy_phew noloop
    mes "We're going to change that today."
    scene sm1cs-mes007-66 mc-mes-closer_c2 with dissolve
    pause
    play sound sfx_cloth_planket3
    scene sm1cs-mes007-67 mc-mes-on-top-of-her_c1 with dissolve
    play voice2 mc_angry_errr7 noloop
    pause
    play sound2 sfx_cloth_rustling3 noloop volume 1.6
    scene sm1cs-mes007-68 mc-mes-on-top-of-her_c1 with dissolve
    pause
    play sound sfx_cloth_rustling4 volume 2.0
    scene sm1cs-mes007-69 mc-mes-holding-her-face_c1 with dissolve
    pause
    play voice2 d14s16_smell noloop
    scene sm1cs-mes007-69 mc-mes-holding-her-face_c2 with dissolve
    pause
    play voice2 mc_angry_errr5 noloop
    scene sm1cs-mes007-70 mc-mes-taking-her-bra-off_c1 with dissolve
    play sound dahlia_kiss_french1
    play voice3 min_old_mff noloop
    mes "Mmuaaah..."
    scene sm1cs-mes007-70 mc-mes-taking-her-bra-off_c2 with dissolve
    queue sound mc_kiss1
    pause
    play sound sfx_underpants_off1 volume 3.0
    scene sm1cs-mes007-71 mc-mes-undies-on-floor_c1 with dissolve
    pause
    play sound sfx_handjob_cream1 loop volume 2.0
    scene sm1cs-mes007-72 mc-mes-getting-on-top_c1 with dissolve
    play voice3 min_happy_mmm noloop
    mes "Now it's your turn, big boy."
    mes "You don't mind if I get on top do you?"
    scene sm1cs-mes007-72 mc-mes-getting-on-top_c2 with dissolve
    menu:
        "Like I have a choice?":
            play voice2 d4s4_mclaugh noloop volume 1.5
            mc "Haha. Like a have a choice."
            mc "Your room, your rules."
            scene sm1cs-mes007-72 mc-mes-getting-on-top_c3 with dissolve
            play voice3 min_yes_simple noloop
            mes "Smart man."
        "Knock yourself out":
            $ player.set_choice("sm1cs_mes007_knock_yourself_out")
            scene sm1cs-mes007-73 mc-mes-knock-yourself-out_c1 with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "Knock yourself out. Just don't be surprised to feel a sudden presure pushing against your pussy."
            scene sm1cs-mes007-73 mc-mes-knock-yourself-out_c2 with dissolve
            play voice3 min_yes_simple noloop
            mes "I'm counting on it."
    play sound sfx_cloth_rustling1
    scene sm1cs-mes007-74 mc-mes-rubbing-her-pvss_c1 with dissolve
    play voice3 min_old_moan1 noloop volume 1.4
    mes "Ooouha... I'm so wet."
    mes "Get ready to say hello to my kitty."
    scene sm1cs-mes007-74 mc-mes-rubbing-her-pvss_c2 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Your will is my command."
    scene sm1cs-mes007-74 mc-mes-rubbing-her-pvss_c3 with dissolve
    pause
    scene sm1cs-mes007-75 mc-mes-lifting-her-butt_c1 with dissolve
    pause
    play sound sfx_fisting_fist2
    scene sm1cs-mes007-76 mc-mes-inside-her_c1 with dissolve
    play voisex3 min_angry_breath noloop
    mes "Muaaah..."
    scene sm1cs-mes007-76 mc-mes-inside-her_c2 with dissolve
    play voisex2 mc_scared_oh4 noloop
    mc "You're so wet."
    scene sm1cs-mes007-76 mc-mes-inside-her_c3 with dissolve
    play voisex3 min_thinking_hmm1 noloop
    mes "I've been feeling horny the whole day, [mcname]."
    mes "Now I finally have what I want!"
    scene sm1cs-mes007-a77-1 mc-mes-rev-cgirl-anim-01 with dissolve
    pause
    scene sm1cs-mes007-a77-1
    play voisex3 min_old_longmoan1
    play voisex2 mc_sex_openmoans1
    play sound sfx_vagina_penetration1_fast loop
    mes "Yes!"
    mes "So thick and strong."
    mes "I can't wait to christen this bed with you."
    pause
    scene sm1cs-mes007-a77-2 with dissolve
    mc "Yes, baby."
    mc "You're the best, Min."
    mes "Tch. Go easy, [mcname]. I get enough praise from my parents."
    pause
    scene sm1cs-mes007-a77-3 with dissolve
    mes "I want you... to hammer my cunt."
    mes "And talk dirty to me."
    pause
    scene sm1cs-mes007-a77-4 with dissolve
    mc "Haha. You like that don't you?"
    pause
    scene sm1cs-mes007-a77-1-f with dissolve
    mc "Being pounded like my personal fuckdoll."
    pause
    scene sm1cs-mes007-a77-2-f with dissolve
    mes "Yes, I do. I'm a dirty slut."
    pause
    scene sm1cs-mes007-a77-3-f with dissolve
    mes "I'm brilliant and hardworking."
    mes "But at the end of the day, solving complicated business math is nothing."
    pause
    scene sm1cs-mes007-a77-4-f with dissolve
    mes "Compared to being worked over by my stallion."
    pause
    stop voisex2 fadeout 1.0
    stop voisex3 fadeout 1.0
    play sound sfx_cloth_planket3
    scene sm1cs-mes007-a78-1 mc-mes-sideways-anim-01 with dissolve
    pause
    scene sm1cs-mes007-a78-1
    play voisex2 mc_sex_closedmoans1
    play voisex3 min_old_moans2
    play sound sfx_vagina_penetration1_fast loop
    mc "Time for your stallion to take control."
    mes "Yes. Oh f-fuck."
    mct "With her leg up like this, she feels even tighter than before."
    pause
    scene sm1cs-mes007-a78-2 with dissolve
    mes "Give it to me."
    mes "Imprint the shape of yoru cock against my womb."
    pause
    scene sm1cs-mes007-a78-3 with dissolve
    mc "That's so fucking hot!"
    pause
    scene sm1cs-mes007-a78-4 with dissolve
    mes "*moaning* I'm all yours, [mcname]."
    pause
    scene sm1cs-mes007-a78-1-f with dissolve
    mes "Wreck my naughty fucking hole!"
    pause
    scene sm1cs-mes007-a78-2-f with dissolve
    mes "I'm going to milk you dry until you get ready to explode!"
    pause
    scene sm1cs-mes007-a78-3-f with dissolve
    pause
    scene sm1cs-mes007-a78-4-f with dissolve
    pause
    play voisex3 min_old_screams2 noloop
    play voisex2 mc_sex_openmoans2
    scene sm1cs-mes007-79 mc-mes-squirting_c1 with hpunch
    mes "Fuahh-haah... Cumming. Cummihaa-hahuaah!"
    play voisex3 min_old_orgasm1 noloop
    play sound2 sfx_squirt1 noloop
    play sound3 sfx_piss_cum1 noloop
    scene sm1cs-mes007-79 mc-mes-squirting_c2 with hpunch
    mes "*moaning*"
    play sound sfx_spitcum1
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-mes007-80 mc-mes-out_c1 with dissolve
    play voisex3 min_old_breathing noloop
    mes "Buaah-huah..."
    play voisex3 min_old_longmoan2
    play voisex2 d7s4_mcbreathing
    play sound2 sfx_fisting_fist1 noloop
    play sound sfx_vagina_penetration1_fast loop
    scene sm1cs-mes007-81 mc-mes-back-in_c1 with hpunch
    mes "Oh!"
    scene sm1cs-mes007-a78-4-f with dissolve
    mes "On you're grinding me down!"
    mes "Fuck me. Fuck me, [mcname]!"
    mes "Use me to fucking cum!"
    mct "Oh shit."
    menu:
        "Cum inside":
            $ player.set_choice("sm1cs_mes007_cum_inside")
            play voisex2 mc_sex_orgasm4 noloop
            play voisex3 min_old_orgasm1 noloop
            play sound mc_cum_sound1 volume 2.0
            scene sm1cs-mes007-85 mc-mes-creampie_c1 with hpunch
            mes "Yessss-huaaah!"
            play voisex3 min_old_orgasm3 noloop
            play sound mc_cum_sound1 volume 2.0
            play voisex2 mc_angry_errr4 noloop
            with hpunch
            mc "*grunting*"
            play sound sfx_spitcum1
            scene sm1cs-mes007-85 mc-mes-creampie_c2 with dissolve
            play voisex3 min_angry_breath noloop
            mes "You always make me so fucking full."
            mes "Thank fuck my birth control is strong."
            scene sm1cs-mes007-86 mc-mes-lying-down_c2 with dissolve
            play voisex2 mc_arrogant_heh2 noloop
            mc "Heh."
        "Cum down her throat":
            $ player.set_choice("sm1cs_mes007_cum_throat")
            scene sm1cs-mes007-87 mc-mes-ordering-her_c1 with dissolve
            mc "Lie on your back."
            mes "Yes sir."
            scene sm1cs-mes007-88 mc-mes-ordering-her_c1 with dissolve
            pause
            play sound sfx_cloth_rustling4
            scene sm1cs-mes007-89 mc-mes-shoving-it-down-her-throat_c1 with dissolve
            play voisex2 mc_sex_openmoans3
            play voisex3 min_old_moans2
            play sound mc_sex_sucking_fast2 loop
            mes "Oooouh..."
            scene sm1cs-mes007-89 mc-mes-shoving-it-down-her-throat_c2 with dissolve
            mes "Mfffhaaafff..."
            mc "Nrraah..."
            scene sm1cs-mes007-90 mc-mes-shoving-it-down-her-throat_c1 with dissolve
            pause
            scene sm1cs-mes007-91 mc-mes-shoving-it-down-her-throat_c2 with dissolve
            pause
            play voisex3 min_sex_mfff2 noloop
            play voisex2 mc_sex_orgasm4 noloop
            play sound mc_cum_sound1 volume 2.0
            scene sm1cs-mes007-92 mc-mes-tearing-down_c1 with hpunch
            mes "Fffummmtth!"
            play voisex3 min_sex_mfff3 noloop
            play sound mc_cum_sound1 volume 2.0
            scene sm1cs-mes007-92 mc-mes-tearing-down_c2 with hpunch
            pause
            play sound sfx_cloth_planket3
            scene sm1cs-mes007-93 mc-mes-taking-off_c1 with dissolve
            play voisex3 min_angry_breath noloop
            play voisex2 mc_happy_oof3 noloop
            pause
            scene sm1cs-mes007-93 mc-mes-taking-off_c2 with dissolve
            play voisex3 min_old_moan1 noloop
            pause
            play sound sfx_drink_gulp
            scene sm1cs-mes007-94 mc-mes-swallowing_c1 with dissolve
            mes "Gulp."
            scene sm1cs-mes007-95 mc-mes-talking_c1 with dissolve
            play voisex3 min_arrogant_heh1 noloop
            mes "Thanks for the treat, handsome."
            scene sm1cs-mes007-95 mc-mes-talking_c2 with dissolve
            play voisex2 mc_yes_aga1 noloop
            mc "You're welcome."
        "Cum on her face and boobs":
            $ player.set_choice("sm1cs_mes007_cum_face")
            play sound sfx_handjob_cream1 volume 2.0 loop
            play sound2 sfx_skirt_off2 noloop
            scene sm1cs-mes007-96 mc-mes-jacking-off_c1 with dissolve
            play voisex2 mc_sex_openmoans3
            play voisex3 min_old_moans
            mc "On your knees."
            play voisex2 mc_sex_orgasm4 noloop
            play sound mc_cum_sound1 volume 2.0
            scene sm1cs-mes007-97 mc-mes-cumming_c1 with hpunch
            mc "Hurraaah..."
            mes "*humming*"
            play sound mc_cum_sound1 volume 2.0
            scene sm1cs-mes007-97 mc-mes-cumming_c2 with hpunch
            mes "Ahuaah..."
            play sound mc_cum_sound1 volume 2.0
            scene sm1cs-mes007-98 mc-mes-cumming-all-over_c1 with hpunch
            mes "Ooohuah..."
            scene sm1cs-mes007-98 mc-mes-cumming-all-over_c2 with dissolve
            play voisex3 min_old_mff noloop
            pause
            scene sm1cs-mes007-98 mc-mes-cumming-all-over_c3 with dissolve
            pause
            scene sm1cs-mes007-99 mc-mes-talking_c2 with dissolve
            play voisex3 min_disappointed_mph noloop
            mes "Mrmmm."
            mes "You must have been a little backed up, hehe."
            scene sm1cs-mes007-99 mc-mes-talking_c1 with dissolve
            play voisex2 mc_yes_yes4 noloop
            mc "Working hard for that money."
            play sound sfx_cloth_wiping1 volume 2.5
            scene sm1cs-mes007-100 mc-mes-wiping_c1 with dissolve
            pause
    play sound sfx_cloth_rustling2
    scene sm1cs-mes007-101 mc-mes-lying-down_c1 with fade
    play voice3 min_surprised_ehh1 noloop
    mes "Emmm."
    mes "Nothing quite like a good reward fuck after moving in with my boyfriend."
    scene sm1cs-mes007-102 mc-mes-cmere_c1 with dissolve
    play voice3 min_arrogant_heh2 noloop
    mes "Come here, you big lug."
    play sound sfx_cloth_rustling4 volume 1.4
    scene sm1cs-mes007-103 mc-mes-cuddling_c1 with dissolve
    play voice3 min_happy_mmm noloop
    mes "Mmmm."
    mes "Here is to the next chapter in my life. And the next chapter in our relationship, [mcname]."
    scene sm1cs-mes007-103 mc-mes-cuddling_c2 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "It's going to be amazing."
    scene sm1cs-mes007-104 mc-mes-talking_c1 with dissolve
    play voice3 min_thinking_hmm2 noloop
    mes "I like your spunky atttitude."
    mes "And your spunk."
    play sound sfx_cloth_planket2
    scene sm1cs-mes007-105 mc-mes-laughing_c1 with dissolve
    play voice2 mc_happy_laugh2 noloop
    play voice3 min_happy_laugh2 noloop
    "[mcname] and Min" "*chuckling*"
    scene sm1cs-mes007-106 mc-mes-just-lying_c1 with dissolve
    pause
    scene black
    show screen scene_transistion(_("A few minutes later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_cloth_rustling3 volume 1.6
    scene sm1cs-mes007-107 mc-mes-telling-him_c1
    with Fade(0.5, 0.5, 0.5)
    play voice3 min_hey_simple noloop
    mes "I should take a shower."
    scene sm1cs-mes007-108 mc-mes-kiss-on-the-cheek_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    play sound mc_kiss3
    pause
    scene sm1cs-mes007-109 mc-mes-talking_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "I'll leave you to it."
    mc "Going to check things out around the studio."
    scene sm1cs-mes007-109 mc-mes-talking_c2 with dissolve
    play voice3 min_yes_yeah1 noloop
    mes "Until next time."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ LocationController.get_location(STUDIO, SD_SUB_MIN, SD_MIN).discover()
    $ LocationController.get_location(STUDIO, SD_SUB_MIN, SD_MIN).unlock()
    $ CharacterController.get_character("mes").add_schedule("default_mes2")
    $ StoryController.end_scene(MES_STORY, 10, 0, 7, STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_1)
    return