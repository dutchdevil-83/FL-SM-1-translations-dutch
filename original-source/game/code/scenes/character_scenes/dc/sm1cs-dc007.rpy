image sm1cs_dc007-glambot-1 = Movie(play = "images/Character-Scenes/DC/s007/anim/sm1cs-dc007-a31-2x-50fps.webm", start_image = "sm1cs-dc007-a31 dc-thanks-waiting-mc-no-problem-glambot-000_i", image = "sm1cs-dc007-a31 dc-thanks-waiting-mc-no-problem-glambot-219_i", loop = False)
label sm1cs_dc007:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound4 sfx_parknight_crickets fadein 2.0 volume 0.7
    play sound sfx_heels_steps2 loop fadein 1.5
    scene sm1cs-dc007-01 mc-walking-alone-park-at-night_c1 with dissolve
    pause
    scene sm1cs-dc007-02 mct-wonder-how-debbie-patrol_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mct "I wonder how Debbie's patrol is going right now."
    scene sm1cs-dc007-03 mct-chuckles-himself_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Maybe I'll bump into her again... hopefully not literally."
    $ renpy.music.set_pan(0.7, 0.0, "voice3" )
    play voice3 girl36_hey_scandalized noloop
    $ renpy.music.set_volume(1.0, 0.0, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.play(audio.music_travelling_inyourmind, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_travelling_inyourmind_radio, "music2", True, None, True, 0.0)
    play sound sfx_stone_run1 loop
    play sound2 sfx_heels_run2
    scene sm1cs-dc007-05 creep-runs-towards-mc-looking-back-dc-shouts-stop_c1 with hpunch
    dc "Stop! Police!"
    $ renpy.music.set_pan(0.0, 0.0, "voice3" )
    scene sm1cs-dc007-04 mc-surprised-by-noise_c1 with dissolve
    play voice2 d3s7_mcemm noloop
    mct "Wait... is that guy even looking where he's going?"
    play voice2 mc_pain_ou3 noloop
    play sound sfx_leg_kick1
    play sound3 sfx_epic_jump1 noloop
    scene sm1cs-dc007-06 creep-bumps-mc_c1 with hpunch
    mc "Ow!"
    play voice4 boy9_angry_argh6 noloop
    play sound sfx_fall_down1 volume 2.0
    play sound3 sfx_kick_leg1 noloop
    scene sm1cs-dc007-07 creep-mc-ground-mc-ow-creep-get-off-me_c1 with vpunch
    "Suspect" "Get off me!"
    scene sm1cs-dc007-08 mc-angry-you-one-ran-into-me_c1 with dissolve
    play voice2 mc_pain_argh1 noloop
    mc "You're the one that ran into me!"
    mc "Ouch!"
    play voice3 girl36_angry_argh4 noloop
    scene sm1cs-dc007-09 db-catches-up-to-creep-still-top-mc_c1 with hpunch
    dc "Stay down!"
    play voice4 boy9_surprised_ah4 noloop
    play voice2 mc_surprised_huh8 noloop
    play voice3 girl36_angry_argh1 noloop
    play sound sfx_epic_jump1
    play sound2 sfx_sand_jump1 noloop
    scene sm1cs-dc007-10 db-jumps-top-of-creep_c1 with hpunch
    pause
    play voice2 mc_pain_ou6 noloop
    play sound sfx_fall_down1
    play sound2 sfx_leg_kick2 noloop
    scene sm1cs-dc007-11 db-falls-top-creep-top-mc_c1 with vpunch
    pause
    play voice4 boy9_angry_breathing1 noloop volume 1.7
    scene sm1cs-dc007-12 mc-ouch-dc-stay-down_c1 with dissolve
    play voice3 girl36_arrogant_huh2 noloop
    dc "Gotcha'!"
    play sound sfx_cloth_shuffle1
    scene sm1cs-dc007-14 creep-struggles-bit_c1 with dissolve
    pause
    play sound2 sfx_metal_chain1 noloop
    play sound3 sfx_sextoy_uncuff1 noloop
    scene sm1cs-dc007-15 dc-takes-out-handcuffs_c1 with dissolve
    pause
    play sound sfx_sextoy_cuff1
    scene sm1cs-dc007-16 dc-cuffs-creep-gotya-creep-damn-you-pig_c1 with dissolve
    play voice4 boy9_angry_argh7 noloop
    "Suspect" "Damn you, pig!"
    scene sm1cs-dc007-17 mc-hey-she-damn-good-cop_c1 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Hey! She's not a pig! She actually looks damn good!"
    play sound sfx_cloth_planket2
    scene sm1cs-dc007-18 dc-thanks-mc-ofc-debbie_c1 with dissolve
    play voice3 girl36_thinking_oh noloop
    dc "Thanks, [mcname]."
    play voice2 mc_yes_sure1 noloop
    mc "Of course, Debbie."
    play sound sfx_sextoy_uncuff1 volume 0.5
    scene sm1cs-dc007-19 dc-serious-under-arrest-creep_c1 with dissolve
    play voice3 girl36_angry_cough noloop
    dc "As for {b}you{/b}.{w} You're under arrest."
    scene sm1cs-dc007-20 dc-looks-mc-you-okay-mc-think-so-ask-just-help_c1 with dissolve
    play voice3 girl36_thinking_eem noloop
    dc "Are you okay?"
    scene sm1cs-dc007-22 mc-can-have-badge-no-but-grateful-help_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "I think so. Did I... just help?"
    scene sm1cs-dc007-21 dc-sure-did-this-point-should-give-badge_c1 with dissolve
    play voice3 girl36_yes_happy1 noloop
    dc "You sure did. That was perfect timing."
    scene sm1cs-dc007-23 dc-smiles-even-help-not-conventional-mc-yeah-no-mentioned_c1 with dissolve
    play voice3 girl36_happy_laugh1 noloop
    dc "At this point, I should be giving you a badge for how much you've helped me out."
    scene sm1cs-dc007-24 mct-helping-human-speed-bump_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Can you just give badges out?"
    scene sm1cs-dc007-20 dc-looks-mc-you-okay-mc-think-so-ask-just-help_c1 with dissolve
    play voice3 girl36_no_calm1 noloop
    dc "No, [mcname]. But I am grateful to have the help."
    dc "Even if it's, erm, unconventional help."
    scene sm1cs-dc007-22 mc-can-have-badge-no-but-grateful-help_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, don't mention it."
    scene sm1cs-dc007-24 mct-helping-human-speed-bump_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Helping by being a human speed bump... At least we caught this guy."
    scene sm1cs-dc007-25 dc-offer-mc-hand-mc-happy-be-service-dc-seriously-that-amazing_c1 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Well, happy to be of service."
    play voice3 girl36_happy_yeah noloop
    dc "Seriously, that was amazing."
    mct "Amazing? I think I just redefined accidental heroics."
    play sound sfx_hands_clap2
    scene sm1cs-dc007-26 mc-gets-up-mct-just-redefines-accidental-heroics_c1 with dissolve
    play voice3 girl36_thinking_hmm noloop
    dc "I've got to file this guy's paperwork. Can you wait a bit?"
    play voice2 d9s2_yeah noloop volume 1.8
    mc "Yeah, not a problem. I can hang out for a bit!"
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-dc007-28 dc-leads-creep-away_c1 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-dc007-29 mc-wait-dc-finish-creep_c1 with Fade(0.5, 0.5, 0.5)
    pause
    play sound sfx_heels_steps1 loop
    scene sm1cs-dc007-30 dc-reaturns-mc-after-processing_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-dc007-a31 dc-thanks-waiting-mc-no-problem-glambot-000_i with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    play sound3 ["<silence 5.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs_dc007-glambot-1
    pause
    play voice3 girl36_hey_happy noloop
    dc "Thanks for waiting."
    play voice2 mc_yes_yeah4 noloop
    mc "No problem. Figured you might need some backup for your next dramatic chase."
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    play sound sfx_cloth_rustling3
    scene sm1cs-dc007-32 dc-chuckles-lets-hope-break-mc-would-like-coffee_c1 with dissolve
    play voice3 girl36_happy_laugh3 noloop
    dc "Let's hope I get a break. That was enough excitement for one night."
    scene sm1cs-dc007-33 dc-should-be-her-treat-helping-her_c1 with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "Well, if you get the break, would you like a coffee? My treat."
    play voice3 girl36_no_angry1 noloop
    dc "It should be my treat! The big crime stopping vigilante literally tripping up bad guys."
    scene sm1cs-dc007-34 mc-smiles-when-tell-story-be-different-dc-oh-how-tell-it_c1 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "When I tell the story, it's going to be a little different."
    play voice3 girl36_disappointed_oh noloop
    dc "Oh? How are you going to tell it?"
    play sound sfx_throw_something1 volume 1.6
    scene sm1cs-dc007-35 mc-involve-karate-chops-pretty-cop_c1 with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "Well, it's going to involve a lot more karate chops, and talking about this pretty cop who helped me out!"
    scene sm1cs-dc007-36 dc-blushes-love-hear-final-version_c1 with dissolve
    play voice3 girl36_disappointed_aah noloop
    dc "Well when you have the final version ready, I'd love to hear it."
    play sound sfx_cloth_rustling1
    scene sm1cs-dc007-37 mc-gets-up-so-coffee-dc-lovely_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "So, coffee?"
    play voice3 girl36_yes_happy2 noloop
    dc "That sounds lovely, [mcname]."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-dc007-38 mc-dc-leave-park-towards-cafe_c1 with dissolve
    pause
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    $ renpy.music.set_volume(0.0, 5.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    stop sound4 fadeout 2.0
    scene sm1cs-dc007-39 mc-dc-sitting-cafe_c1 with Fade(0.5, 0.5, 0.5)
    queue sound4 sfx_cafe_crowd fadein 1.5
    play voice2 d1s5_mcthinks noloop
    mc "So, Officer Callahan, was that your creeper in the park?"
    scene sm1cs-dc007-40 mc-so-this-creep-dc-unfortunately-not_c1 with dissolve
    play voice3 girl36_no_nah1 noloop
    dc "Unfortunately not. That was a pickpocket who had just robbed some grandma down the street."
    scene sm1cs-dc007-41 mc-wow-good-thing-there-call-manbat_c1 with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow, well good thing I showed up when I did! You can call me, Manbat!"
    play sound sfx_cloth_rustling2
    scene sm1cs-dc007-42 mc-covers-eyes-where-drugs-going_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Where were the other drugs going!?"
    scene sm1cs-dc007-43 dc-laugh-you-something-else-mc-take-that-compliment_c1 with dissolve
    play voice3 girl36_happy_laugh4 noloop
    dc "You're something else, you know that?"
    play voice2 mc_yes_aga2 noloop
    mc "I'll take that as a compliment."
    scene sm1cs-dc007-44 dc-thanks-making-laugh-but-mc-but-what_c1 with dissolve
    play voice3 girl36_disappointed_eeh noloop
    dc "Thanks for making me laugh, [mcname], but..."
    play voice2 d1s2_hmm noloop volume 1.8
    mc "But, what?"
    scene sm1cs-dc007-45 dc-what-makes-her-so-important_c1 with dissolve
    play voice3 girl36_surprised_eeh noloop
    dc "What makes me so important?"
    play voice2 mc_happy_yay2 noloop
    mc "I think you're great, and I like spending time with you."
    scene sm1cs-dc007-46 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Plus, you're pretty hot"(hint="sm1cs_dc007_m01_h01"):
            scene sm1cs-dc007-47 choice-pretty-hot-mc-tells-pretty-hot-dc-smiles-thanks-mc_c1 with dissolve
            play voice2 mc_thinking_hmm6 noloop
            mc "And you're pretty hot, Debbie."
            scene sm1cs-dc007-48 choice-pretty-cute-mc-tells-cute-dc-blushes_c1 with dissolve
            play voice3 girl36_happy_relief2 noloop
            dc "Thanks, [mcname]."
        "Plus, I think you're pretty cute"(hint="sm1cs_dc007_m01_h02"):
            call sm1cs_dc007_m01_c02 from _call_sm1cs_dc007_m01_c02
            scene sm1cs-dc007-47 choice-pretty-hot-mc-tells-pretty-hot-dc-smiles-thanks-mc_c1 with dissolve
            play voice2 mc_thinking_mmm6 noloop
            mc "And I think you're pretty cute, Debbie."
            scene sm1cs-dc007-48 choice-pretty-cute-mc-tells-cute-dc-blushes_c1 with dissolve
            play voice3 girl36_happy_relief2 noloop
            dc "Thank you, [mcname]."
    jump sm1cs_dc007_continue
label sm1cs_dc007_continue:
    scene sm1cs-dc007-49 mc-leans-how-else-get-detective-badge_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "And, how else am I supposed to get that detective badge, other than impressing you?"
    scene sm1cs-dc007-50 dc-might-take-while-mc-oh-dedicated-cause_c1 with dissolve
    play voice3 girl36_arrogant_huh3 noloop
    dc "It might take a while before that happens."
    play voice2 mc_scared_oh4 noloop
    mc "Oh, but I'm dedicated to the cause."
    scene sm1cs-dc007-51 dc-well-now-curious-mc-saving-world-accident-at-time_c1 with dissolve
    play voice3 girl36_arrogant_hmf noloop
    dc "Well you kow, I'm curious... what do you do for work that gives you so much free time to trip up my suspects?"
    scene sm1cs-dc007-52 dc-seriously-mc-okay-working-film-studio_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Oh, you know, saving the world, one accidental hero moment at a time."
    play voice3 girl36_arrogant_he noloop
    dc "Seriously."
    scene sm1cs-dc007-53 mct-technically-true-we-do-film-stuff_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Okay.{w} Erm, I'm working on starting a film studio with a friend of mine."
    mct "Which isn't technically untrue... we do film stuff.{w} Just naked stuff."
    scene sm1cs-dc007-54 dc-surprise-film-studio-really_c1 with dissolve
    play voice3 girl36_surprised_what2 noloop
    dc "A film studio? Really?"
    play sound sfx_cloth_rustling3
    scene sm1cs-dc007-55 mc-yep-getting-started_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    if True:
        mc "Yep. Right now, it's a lot of groundwork and planning. But we're getting there."
    else:
        mc "Yep. We've just kind of started, but we have a lot more still to do."
    play sound sfx_hair_scratch1
    if not player.get_choice("sm1ms_renovation_started"):
        scene sm1cs-dc007-56 renovation-ongoing-mc-actually-just-started-renovating-studio-dc-sounds-hard-work_c1 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "Our studio is a little rough around the edges, but we plan to renovate it. Hopefully soon."
        play voice3 girl36_surprised_aah noloop
        dc "What kind of work does the place need?"
        scene sm1cs-dc007-57 mc-yes-but-exciting-dc-need-extra-hand_c1 with dissolve
        play voice2 d1s5b_ehhh noloop volume 1.7
        mc "Everything, honestly. Fixing the space up, setting up equipment, making it look professional."
        play voice3 girl36_arrogant_hm noloop
        dc "Sounds ambitious."
        play sound sfx_drink_loop1 loop
        scene sm1cs-dc007-58 mc-might-take-up-offer_c1 with dissolve
        play voice2 mc_yes_yes3 noloop
        mc "It is, but it'll be worth it."
        stop sound fadeout 1.0
        scene sm1cs-dc007-60 mc-everything-fixing-space-up-dc-sounds-ambitious_c1 with dissolve
        play voice3 girl36_surprised_huh2 noloop
        dc "Well, if you need advice or someone to bounce ideas off, let me know."
        play voice2 mc_yes_okay3 noloop
        mc "I might just take you up on that."
    elif player.get_choice("sm1ms_renovation_started") and not player.get_choice("sm1ms_renovation_completed"):
        scene sm1cs-dc007-56 renovation-ongoing-mc-actually-just-started-renovating-studio-dc-sounds-hard-work_c1 with dissolve
        play voice2 mc_thinking_emm1 noloop
        mc "We actually just started working on renovating the studio. It's been... a process."
        play voice3 girl36_surprised_aah noloop
        dc "Sounds like hard work."
        scene sm1cs-dc007-57 mc-yes-but-exciting-dc-need-extra-hand_c1 with dissolve
        play voice2 mc_yes_yes3 noloop
        mc "It is, but it's exciting. Every step gets us closer to making something great."
        play voice3 girl36_surprised_huh2 noloop
        dc "Need an extra hand? I'm not bad with tools, you know."
        scene sm1cs-dc007-58 mc-might-take-up-offer_c1 with dissolve
        play voice2 mc_yes_okay3 noloop
        mc "Really? I might take you up on that."
        scene sm1cs-dc007-60 mc-everything-fixing-space-up-dc-sounds-ambitious_c1 with dissolve
    play voice3 girl36_hey_angry1 noloop
    dc "I wouldn't have guessed that you were a filmmaker."
    scene sm1cs-dc007-59 mc-studio-rough-aroundedges-plan-renovate-it-dc-what-kind-work-place-needs_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "What can I say? I am an enigma."
    scene sm1cs-dc007-63 that-you-are-what-movies-mct-cant-really-tell-porn_c1 with dissolve
    play voice3 girl36_yes_aga noloop
    dc "That you are... What kind of movies do you make?"
    play sound sfx_cloth_rustling2
    scene sm1cs-dc007-65 mc-leans-lots-of-non-pro-people_c1 with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "I really can't tell her that it's porn..."
    scene sm1cs-dc007-64 mc-erm-character-pieces-dc-where-getting-actors_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Erm... they're, uh, character driven pieces?"
    scene sm1cs-dc007-66 dc-thoughtful-really-mc-yeah_c1 with dissolve
    play voice3 girl36_happy_relief1 noloop
    dc "Oh? And where are you getting your actors and actresses? From the theater?"
    scene sm1cs-dc007-68 dc-presence-mc-explains-commanding-sharp_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Some of them, but we work with a lot of \"non-professional\" actors. You know, regular people like you!"
    scene sm1cs-dc007-67 dc-ppl-like-me-mc-you-be-great_c1 with dissolve
    play voice3 girl36_surprised_huh1 noloop
    dc "Really?"
    play voice2 mc_yes_yes2 noloop
    mc "Yeah, we're trying to discover new talent all the time."
    scene sm1cs-dc007-69 dc-think-so-mc-know-so_c1 with dissolve
    play voice3 girl36_arrogant_laugh noloop
    dc "People like me...{w} I've never thought about being on camera."
    play voice2 mc_thinking_hmm3 noloop
    mc "You'd be great at it! You've got presence."
    play sound sfx_cup_place1
    scene sm1cs-dc007-70 dc-big-producer-where-can-watch-movies_c1 with dissolve
    play voice3 girl36_surprised_what1 noloop
    dc "Presence? What's that supposed to mean?"
    play voice2 mc_thinking_hmm4 noloop
    mc "You're commanding, sharp, and let's be honest, you'd make an amazing action hero."
    scene sm1cs-dc007-72 mc-not-that-mysterious-basic-stuff-dc-sounds-mysterious_c1 with dissolve
    play voice3 girl36_surprised_huh3 noloop
    dc "You think so?"
    scene sm1cs-dc007-73 mc-laughs-mct-way-too-much-fun-mc-promise-show-something-soon_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "I {i}know{/i} so!"
    scene sm1cs-dc007-74 dc-good-otherwise-threaten-handcuffs_c1 with dissolve
    play voice3 girl36_angry_ugh2 noloop
    dc "Well, Mr. Big-Time-Movie-Director, where can I watch your movies?"
    play sound sfx_cloth_rustling2
    scene sm1cs-dc007-71 mc-no-where-yet-portfolio-pieces-dc-sounds-mysterious_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Uhm... nowhere really, yet. We've mostly shot portfolio scenes. Stuff to try and help us get more... funding?"
    scene sm1cs-dc007-75 mc-oh-no-plan-detaining-dc-if-have-to-will_c1 with dissolve
    play voice3 girl36_arrogant_huh1 noloop
    dc "Portfolio scenes, huh? Sounds mysterious."
    play voice2 mc_no_nah2 noloop
    mc "It's not that mysterious. Just some basic stuff to build a catalog."
    dc "Uh-huh. Still pretty mysterious sounding."
    scene sm1cs-dc007-77 dc-eyes-linger-mc-soft-look_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.7
    mct "She's having way too much fun with this."
    mc "I promise to show you something soon."
    scene sm1cs-dc007-76 mc-promise-perfect-thing-show-dc-alright-fine-mc-appriciate-it_c1 with dissolve
    play voice3 girl36_yes_yep noloop
    dc "Good! Otherwise I was going to threaten to put you in handcuffs until you told me."
    scene sm1cs-dc007-80 mc-fake-shock-didnt-exactly-volunteer-dc-but-was-impressive_c1 with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "Oh, do you plan on detaining me, Officer Callahan?"
    scene sm1cs-dc007-78 flirty-banter-dc-you-triple-threat-mc-is-that-so_c1 with dissolve
    play voice3 girl36_arrogant_fff noloop
    dc "If I have to, I will!"
    scene sm1cs-dc007-81 mc-smirk-so-you-impressed-dc-dont-push-it-mc-too-late_c1 with dissolve
    play voice2 mc_hey_hey8 noloop
    mc "I promise, I'll find the perfect thing to show you soon."
    play voice3 girl36_angry_ugh1 noloop
    dc "Alright, fine. I'll take your word for it. For now."
    mc "Appreciate that, Officer Callahan."
    scene sm1cs-dc007-82 dc-smirks-ok-maybe-little_c1 with dissolve
    play voice3 girl36_angry_hmm noloop
    dc "You know, you're a real triple threat, [mcname]."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, is that so?"
    dc "Mmmhmmmm, rogue vigilante, movie director, and cute to boot."
    scene sm1cs-dc007-80 mc-fake-shock-didnt-exactly-volunteer-dc-but-was-impressive_c1 with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.6
    mc "I don't know about \"rogue vigilante\", what about \"hot action hero\"?"
    play voice3 girl36_disgust_mneagh noloop
    dc "Mmmmm, maybe when you're move isn't \"Human Roadblock\"."
    mc "Hey, I didn't exactly volunteer for that part of tonight!"
    dc "You didn't, but it was pretty impressive."
    mc "So you're saying you were impressed?"
    scene sm1cs-dc007-79 dc-mhm-rogue-vigilante-movie-director-cute-mc-not-sure-rogue-vigilante_c1 with dissolve
    play voice3 girl36_hey_angry2 noloop
    dc "Don't push it."
    play voice2 mc_no_uhuh1 noloop
    mc "Too late."
    dc "Okay, maybe a little."
    play sound sfx_alarm1 volume 0.5
    scene sm1cs-dc007-83 dc-checks-phone-break-over-mc-walk-her-out_c1 with dissolve
    play voice3 girl36_angry_doh3 noloop
    dc "Shoot, looks like my break is over."
    play voice2 mc_disappointed_ehh2 noloop
    mc "Well, let me walk you out."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-dc007-84 mc-dc-head-out-for-exit_c1 with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-dc007-85 dc-stop-before-exit-nervous-hey-wait-second_c1 with dissolve
    play voice3 girl36_hey_greeting2 noloop
    dc "Hey, uh... wait a second."
    play voice3 girl36_disappointed_moan noloop
    play voice2 mc_thinking_mmm2 noloop
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-dc007-86 dc-kiss-mc-quick-firm_c1 with dissolve
    play sound mc_kiss2
    pause
    mct "Whoa. Didn't see that coming."
    scene sm1cs-dc007-87 dc-pull-uhm-mct-debbie-full-of-surprised_c1 with dissolve
    play voice3 girl36_happy_mmm noloop
    dc "Umm..."
    mct "Debbie is really full of surprises."
    scene sm1cs-dc007-88 dc-should-say-something-mc-that-was-great_c1 with dissolve
    play voice3 girl36_surprised_eeh noloop
    dc "You should say something now, before I think I made a big mistake."
    play sound sfx_cloth_rustling3
    scene sm1cs-dc007-89 mc-pretty-good-deduction-dc-thanks-seriously-way-better-chasing-criminals_c1 with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "That was great! Just, a bit unexpected. Didn't think you'd make the first move."
    scene sm1cs-dc007-90 dc-smiles-mc-promise-next-time-talk-going-real-date-dc-okay_c1 with dissolve
    play voice3 girl36_happy_laugh2 noloop
    dc "You've bought me coffee how many times now? I think you might have made the first move."
    play voice2 mc_yes_yes1 noloop
    mc "That's a pretty good deduction, Officer Callahan."
    dc "Thanks. But seriously, I'm way better at chasing down criminals than... whatever this is."
    play sound sfx_door_open1
    scene sm1cs-dc007-91 mc-opens-door-dc-if-need-help-studio-lemme-know-mc-might-take-up-on-that_c1 with dissolve
    play sound2 sfx_heels_steps1
    play voice2 mc_yes_okay2 noloop
    mc "That's okay. We can figure it out together."
    mc "And I promise you, the next time we talk, we're going to go on a {i}real{/i} date."
    play voice3 girl36_yes_yeah noloop
    dc "Okay. But only if there's no tackling involved."
    mc "Deal."
    if player.get_choice("sm1ms_renovation_started") and not player.get_choice("sm1ms_renovation_completed"):
        stop sound2 fadeout 1.0
        scene sm1cs-dc007-90 dc-smiles-mc-promise-next-time-talk-going-real-date-dc-okay_c1 with dissolve
        play voice3 girl36_thinking_oh noloop
        dc "And if you need help at the studio, let me know."
        play voice2 mc_yes_yes7 noloop
        mc "I might just take you up on that."
    play sound2 sfx_heels_steps1
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(0.0, 5.0, "music2" )
    scene sm1cs-dc007-92 dc-mc-leave-cafe-end-scene_c1 with dissolve
    pause
    stop sound2 fadeout 2.0
    stop sound4 fadeout 2.0
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1cs_dc007_end
label sm1cs_dc007_end:
    $ StoryController.end_scene(DC_STORY, 3, 0, 3)
    return
label sm1cs_dc007_m01_c02:
    $ player.set_choice("sm1cs_dc007_dc_cute")
    $ CharacterController.get_character("dc").add_point()
    return