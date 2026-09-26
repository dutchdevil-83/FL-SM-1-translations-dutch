image sm1mv01s04-a68-glambot = Movie(play = "images/MV/mv01/s04/anim/sm1mv01s04-a68-2x-60fps.webm", start_image = "sm1mv01s04-a68 tl-holds-cutlass-thought-guys-want-these-glambot-00", image = "sm1mv01s04-a68 tl-holds-cutlass-thought-guys-want-these-glambot-78", loop = False)
label sm1mv01s04:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    scene sm1mv01s04-01 sy-mc-looking-place-where-set-build_c1 with dissolve
    play music music_hammership_process
    play voice2 mc_thinking_hmm1 noloop
    mc "Finally time to build our sets."
    scene sm1mv01s04-02 mc-so-build-sets-sy-uh-huh-ship-cabin-deck_c1 with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "Uh huh, the ship's cabin, and the ship deck."
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "You think we should build both at the same time?"
    scene sm1mv01s04-03 mc-you-think-should-do-both-same-time-sy-no-space_c1 with dissolve
    play voice3 stacy_no_simple2 noloop
    sy "I don't think we have the space for it."
    scene sm1mv01s04-04 sy-think-build-art-flats-mc-what-hell-art-flat_c1 with dissolve
    play voice3 stacy_mmm1 noloop
    sy "But, I think we build some art flats and we can put them up and take them down when we're filming the scene."
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What the hell is an art flat?"
    scene sm1mv01s04-05 sy-fakewall-mc-oh-okay-art-flats-be-great_c1 with dissolve
    play voice3 stacy_disappointed_oh5 noloop
    sy "It's a fake wall. It's like the shit they use on theater stages when they need to build a room or something."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, okay. Yeah, art flats would be great here."
    mc "So which one do you think we should start with?"
    scene sm1mv01s04-06 mc-which-one-build-first-sy-dunno_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "I don't know."
    scene sm1mv01s04-07 door-knocks_c1 with dissolve
    call knock from _call_knock_9
    scene sm1mv01s04-08 that-why-called-expert_c1 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "That's why I called in an expert."
    play sound sfx_door_openclosed1
    scene sm1mv01s04-09 kv-sup-guys-mc-kanya-here-help-build-set_c1 with dissolve
    play voice4 kanya_hey_simple1 noloop
    kv "'Sup, guys?"
    play voice2 mc_hey_hey8 noloop
    mc "Kanya! Are you here to help us with the set building?"
    play sound sfx_heels_steps2 loop
    scene sm1mv01s04-10 kv-walk-up-kv-more-supervisory-role-make-sure-build-sets-work-easier_c1 with dissolve
    play voice4 kanya_thinking_eeh1 noloop
    kv "I'm here in a more... supervisory role."
    kv "Make sure you guys build the sets in a way that we can work easier."
    stop sound fadeout 1.0
    scene sm1mv01s04-11 kv-cant-afford-manual-labor_c1 with dissolve
    play voice4 kanya_thinking_hmm4 noloop
    kv "Besides, you couldn't afford my day rate for manual labor."
    scene sm1mv01s04-12 kv-this-spot-sy-ye-think-work_c1 with dissolve
    play voice4 kanya_arrogant_ha noloop
    kv "So, this is the spot?"
    play voice3 stacy_yes_yap1 noloop
    sy "Yep! Do you think it'll work?"
    scene sm1mv01s04-13 kv-no-worries-make-work-mc-what-set-begin_c1 with dissolve
    play voice4 kanya_yes_yeah1 noloop
    kv "Don't worry, we'll make it work."
    play voice2 mc_thinking_hmm2 noloop
    mc "Which set do you think we should build first?"
    scene sm1mv01s04-14 kv-thinking-hmm-cabin-first-start-beginning_c1 with dissolve
    play voice4 kanya_thinking_hmm1 noloop
    kv "Hmmmm... why don't we start with the cabin first, yeah? That's our first location we'll need anyway."
    kv "Might as well start at the beginning. Besides, the interior will be easier than the exterior."
    scene sm1mv01s04-15 sy-alright-mc-get-to-it_c1 with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "All right! [mcname]! Get to it!"
    scene sm1mv01s04-16 mc-arent-helping-sy-actually-production-designer_c1 with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Aren't you going to help me?"
    play sound sfx_throw_something1
    scene sm1mv01s04-17 sy-you-carpenter-get-build-mc-wait-second_c1 with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "I'm actually listed as the Production Designer on this set, which means I make decisions."
    sy "And you're listed as a carpenter, which means you build!"
    play voice2 mc_thinking_wait1 noloop
    mc "Wait a second-"
    play sound sfx_cloth_rustling1
    scene sm1mv01s04-18 sy-chop-chop-get-hammer_c1 with dissolve
    play voice3 stacy_angry noloop
    sy "So, chop, chop, [mcname]! Get your hammer and nails out and get to it!"
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    play sound sfx_heels_steps1_slow loop
    scene sm1mv01s04-19 mc-defeated-goes-get-his-hammer_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    pause
    play sound sfx_hammer_loop1
    scene sm1mv01s04-20 cabin-montage-one_c1 with fade
    pause
    play sound sfx_hammer_loop1
    scene sm1mv01s04-21 cabin-montage-two_c1 with fade
    pause
    play sound sfx_screwdriver_drill2
    scene sm1mv01s04-22 cabin-montage-three_c1 with fade
    pause
    play sound sfx_bed_slide3
    scene sm1mv01s04-23 cabin-montage-four_c1 with fade
    pause
    play sound sfx_gambling_coin1
    play sound2 sfx_locker_open1 noloop
    play sound3 sfx_door_creak2 noloop volume 2.5
    scene sm1mv01s04-24 cabin-montage-five_c1 with fade
    pause
    $ renpy.music.set_volume(0.7, 2.5, "music" )
    scene sm1mv01s04-25 cabin-montage-six_c1 with fade
    pause
    scene sm1mv01s04-26 sy-wow-really-come-together-kv-especially-desk_c1 with dissolve
    play voice3 stacy_surprised_wow1 noloop
    sy "Wow, this really came together!"
    play voice4 kanya_surprised_wow noloop
    kv "And the desk really ties it all together."
    scene sm1mv01s04-27 mc-phew-lot-work-sy-well-know-love-watch-man-work_c1 with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "Phew... that was a lot of work."
    scene sm1mv01s04-26 sy-wow-really-come-together-kv-especially-desk_c1 with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "Well, I know {i}I{/i} love watching a man at work."
    scene sm1mv01s04-28 kv-got-no-complaints-either_c1 with dissolve
    play voice4 kanya_yes_yep1 noloop
    kv "I've got no complaints about it either."
    scene sm1mv01s04-29 mc-wouldnt-mind-help-next-time-kv-eh-have-broken-toe_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I wouldn't mind a hand on the next one though."
    play voice3 kanya_surprised_eeh2 noloop
    kv "Ehhhh... I have, a, erm, broken toe?"
    scene sm1mv01s04-30 sy-pd-dont-build-mc-damnit_c1 with dissolve
    play voice3 stacy_hey noloop
    sy "And the PD doesn't do the building! That's why I hired a carpenter for the day!"
    play voice2 mc_angry_errr7 noloop
    mc "Goddamnit..."
    scene sm1mv01s04-31 sy-so-need-take-interior-down-start-making-exterior_c1 with dissolve
    play voice3 stacy_thinking_hmm2 noloop
    sy "So we need to take the interior set down and start building the ship deck set!"
    mc "..."
    play sound sfx_cloth_rustling1
    scene sm1mv01s04-32 sy-pitter-patter-mc-silent_c1 with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "Pitter patter, [mcname]!"
    kv "Let's get at her."
    scene sm1mv01s04-33 mc-damn-it-goes-back-set_c1 with dissolve
    play voice2 mc_arrogant_pff1 noloop
    mc "..."
    mc "Damnit."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1mv01s04-34 mc-working-bg-sy-so-ship-deck-think-hard-film_c1 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "So for the ship deck, do you think it'll be tough to film?"
    play voice4 kanya_no_happy noloop
    kv "I don't think so. I mean, it'll be a lot of post work to replace the studio with open sky, but it shouldn't be too bad."
    play sound sfx_cloth_rustling4
    play sound2 sfx_cloth_rustling5 noloop
    scene sm1mv01s04-35 sy-there-better-way-do-it-kv-generally-film-location_c1 with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "Is there a better way to do it?"
    scene sm1mv01s04-36 kv-hassle-location-filming-less-time-everything-look-fine-vfx_c1 with dissolve
    play voice4 kanya_disappointed_hm noloop
    kv "I'd generally recommend trying to film on location. There are pros and cons to both."
    kv "But, I find the hassle of finding a location takes less time than making the sky and everything look right in VFX."
    scene sm1mv01s04-37 sy-got-good-point-kv-make-do-what-got_c1 with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "You've got a good point there."
    play voice4 kanya_thinking_hmm3 noloop
    kv "But, we make do with what we've got, you know?"
    scene sm1mv01s04-38 sy-good-point_c1 with dissolve
    play voice3 stacy_yes_yap2 noloop
    sy "Good point."
    scene sm1mv01s04-39 mc-look-over-mc-that-reminds-still-figure-cave-too-much-sand-inside_c1 with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "That reminds me, we still need to figure out the beach and treasure cave and shit."
    mc "Because getting enough sand in here to make a beach is... is going to take a lot of work."
    scene sm1mv01s04-40 kv-also-sand-gets-everywhere-like-glitter_c1 with dissolve
    play voice4 kanya_yes_aga3 noloop
    kv "And sand gets everywhere."
    scene sm1mv01s04-43 sy-folding-arms-looking-around-know-private-beach-property-close_c1 with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "It's like you say, [mcname]. We'll figure it out."
    scene sm1mv01s04-48 sy-look-mc-back-work-have-another-set-build-mc-uugh-yeah-get-back-it_c1 with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "For now, we've still have another set to build!"
    play sound sfx_throw_something1
    scene sm1mv01s04-49 montage-deck-one_c1 with dissolve
    play voice2 mc_angry_errr8 noloop
    mc "Ugghhhhhh... yeah, I'll get back to it."
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1mv01s04-50 montage-deck-two_c1 with fade
    play sound sfx_wrench_long1
    pause
    play sound sfx_armor_equiped1
    scene sm1mv01s04-51 montage-deck-three_c1 with fade
    pause
    play sound sfx_armor_equiped2
    play sound2 sfx_metal_fence1 noloop
    scene sm1mv01s04-52 montage-deck-four_c1 with fade
    pause
    play sound sfx_screwdriver_drill5
    scene sm1mv01s04-53 montage-deck-five_c1 with fade
    pause
    play sound sfx_skirt_off2
    scene sm1mv01s04-54 montage-deck-six_c1 with fade
    pause
    $ renpy.music.set_volume(0.6, 2.5, "music" )
    scene sm1mv01s04-55 kv-sy-watching-deck-set-sy-damn-looks-great-did-great-job-on-design_c1 with dissolve
    play voice3 stacy_surprised_ah1 noloop
    sy "Damn, that looks great!"
    sy "I did a great job designing this set."
    scene sm1mv01s04-56 mc-silent-catching-his-breath_c1 with dissolve
    play voice2 mc_breathing_heavy noloop
    mc "..."
    scene sm1mv01s04-57 mc-yep-was-all-you-sy-well-helped-realize-vision_c1 with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yep, that was {b}all{/b} you."
    scene sm1mv01s04-58 mc-could-say-thanks-sy-thanks-for-doing-your-job_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, I guess you helped me realize my vision."
    scene sm1mv01s04-59 kv-alright-you-two-tension-aside-looks-great_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "You could just say thank you."
    play voice3 stacy_mmm2 noloop
    sy "Thanks{w} for doing your job, [mcname]."
    play voice4 kanya_happy_laugh3 noloop
    kv "All right you two, palpable sexual tension aside, this looks great!"
    scene sm1mv01s04-60 sy-looking-kv-enough-angles-kv-might-have-adjust-boards-bit_c1 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Have you got enough angles here to film the scene you think?"
    play voice4 kanya_thinking_eeh5 noloop
    kv "I might have to adjust my boards a bit here, but I think it shouldn't be a problem."
    scene sm1mv01s04-61 sy-excited-hell-yeah-was-really-concerned_c1 with dissolve
    play voice3 stacy_happy_yay2 noloop
    sy "Awesome! Hell yeah!"
    sy "I was really concerned about that."
    play sound sfx_door_openclosed1
    scene sm1mv01s04-62 tl-stands-door-damn-that-set_c1 with dissolve
    play voice5 girl24_surprised_ohmy2 noloop
    tl "Damn, is that the set?"
    scene sm1mv01s04-63 tl-look-fucking-great_c1 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Oh, what's up, Taisia?"
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah! This is the ship deck set. What do you think?"
    scene sm1mv01s04-64 tl-thought-try-cardboard-set-mc-figured-make-something-look-good_c1 with dissolve
    play voice5 girl24_happy_relief noloop
    tl "I thought you might try to do another cardboard set or something."
    tl "Turns out I was wrong."
    play voice2 mc_arrogant_heh1 noloop
    mc "We decided to go ham for our big budget movies, you know?"
    scene sm1mv01s04-65 tl-yeah-fuckin-great-mc-what-have-in-box_c1 with dissolve
    play voice5 girl24_happy_yeah3 noloop
    tl "Smart move."
    play voice2 d2s9_confused noloop volume 1.4
    mc "What do you have in the case, Taisia?"
    scene sm1mv01s04-66 tl-oh-shit-that-right_c1 with dissolve
    play voice5 girl24_surprised_oh1 noloop
    tl "You're about to bow down and kiss my feet, [mcname]."
    play sound sfx_box_slide
    scene sm1mv01s04-67 tl-opens-case_c1 with dissolve
    pause
    play sound2 sfx_sword_whoosh4 noloop
    scene sm1mv01s04-a68 tl-holds-cutlass-thought-guys-want-these-glambot-00 with dissolve
    pause 0.01
    play sound sfx_camera_fly1 volume 2.0
    scene sm1mv01s04-a68-glambot
    play voice5 girl24_arrogant_huh2 noloop
    tl "Thought you guys might want these."
    play voice3 stacy_scared_ah4 noloop
    play sound sfx_throw_something1
    scene sm1mv01s04-69 sy-mega-excited-these-pirate-swords-tl-ye_c1 with vpunch
    sy "ARE THOSE PIRATE SWORDS!?!"
    play voice5 girl24_arrogant_yeah1 noloop
    tl "Ye-"
    play voice3 stacy_angry_aah3 noloop
    play sound sfx_sword_whoosh1
    play sound2 sfx_throw_something1 noloop
    scene sm1mv01s04-70 sy-runs-this-fckn-awesome-tl-wow_c1 with hpunch
    sy "THIS IS FUCKING AWESOME!"
    play voice5 girl24_surprised_wow2 noloop
    tl "Wow. I thought [mcname] might act like this, wasn't expecting Stacy to get such a lady boner for a sword."
    play voice3 stacy_angry_argh5 noloop
    play sound sfx_sword_whoosh2
    scene sm1mv01s04-71 sy-gets-pose-avast-scurvy-dogs_c1 with hpunch
    sy "AVAST YE' SCURVY DOG!"
    scene sm1mv01s04-72 mc-wow-taisia-incredible-tl-snagged-from-theater_c1 with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow, Taisia. These are pretty incredible. Where'd you get them?"
    scene sm1mv01s04-73 tl-figured-probably-hiding-out-mc-oh-shit-denise-let-take-them_c1 with dissolve
    play voice5 girl24_thinking_ah noloop
    tl "Snagged them from the theater. They did this real avant garde, interpretive dance thing a few years ago about pirates."
    tl "I imagine they will be perfect for our needs."
    play voice2 mc_disappointed_off2 noloop
    mc "Oh shit. And Denise just let you take them?"
    scene sm1mv01s04-74 tl-supposed-ask-mc-think-anyone-notice_c1 with dissolve
    play voice5 girl24_surprised_eeh2 noloop
    tl "...{w} I was supposed to ask?"
    play voice2 mc_arrogant_huh1 noloop
    mc "Think anyone will notice?"
    scene sm1mv01s04-75 tl-shrugs-prolly-not-mc-we-make-sure-get-asap_c1 with dissolve
    play voice5 girl24_no_nah noloop
    tl "Probably not. And even if they do, they'll probably just assume they got lost."
    play voice2 mc_arrogant_hm1 noloop
    mc "Well, we'll make sure to get them back ASAP."
    scene sm1mv01s04-76 tl-sure-not-really-worried_c1 with dissolve
    play voice5 girl24_yes_aga noloop
    tl "Sure. I'm not really worried about it."
    scene sm1mv01s04-77 sy-these-stage-swords-they-not-sharp-doesnt-mean-wont-fkn-hurt_c1 with dissolve
    play voice3 girl24_arrogant_hm4 noloop
    tl "So you know, these are stage swords, so they're not sharp."
    tl "But that doesnt mean that it won't fucking hurt if you hit someone with it."
    play voice3 stacy_angry_aah1 noloop
    play sound sfx_sword_whoosh3
    scene sm1mv01s04-78 sy-lunges-hyah-pirate-scum_c1 with hpunch
    sy "HIYAH, YOU PIRATE SCUM!"
    mc "Still not a ninja movie."
    scene sm1mv01s04-79 tl-she-not-pay-attention-soon-right-mc-prolly-not_c1 with dissolve
    play voice5 girl24_arrogant_huh1 noloop
    tl "She's not going to pay attention to anything any time soon, is she?"
    play voice2 mc_no_uhuh1 noloop
    mc "Probably not."
    scene sm1mv01s04-80 tl-cool-go-room-mc-oh-before-go_c1 with dissolve
    play voice5 girl24_thinking_hmm1 noloop
    tl "Cool. Well, I'm gonna' head up to my room."
    play sound sfx_heels_steps1 loop
    scene sm1mv01s04-87 tl-walking-away-just-tell-when-need-mc-will-do_c1 with dissolve
    play voice2 mc_hey_bye2 noloop
    mc "Later Taisia. Thanks again for the swords."
    play voice5 girl24_yes_yap noloop
    tl "Cheers."
    stop sound fadeout 3.0
    scene sm1mv01s04-88 kv-actually-gotta-jet-have-edits-finish_c1 with dissolve
    play voice4 kanya_thinking_hmm2 noloop
    kv "I actually have to jet too. I have some edits I need to finish up."
    scene sm1mv01s04-89 kv-see-later-mc-see-you-kv-make-sure-get-call-sheet_c1 with dissolve
    play voice4 kanya_happy_relief2 noloop
    kv "See you later, [mcname]!"
    play voice2 mc_hey_bye1 noloop
    mc "See you, Kanya! We'll make sure you get a call sheet when we're going to film day one!"
    play sound sfx_heels_steps2 loop
    scene sm1mv01s04-90 kv-sounds-good-me-exits-scene_c1 with dissolve
    play voice4 kanya_yes_yeah2 noloop
    kv "Sounds good to me!"
    play voice2 mc_scared_huh4 noloop
    play voice3 stacy_angry_argh3 noloop
    play sound sfx_sword_whoosh4
    play sound2 sfx_door_openclosed2 noloop
    scene sm1mv01s04-91 mc-turns-around-sword-in-his-face_c1 with hpunch
    sy "My name is Stacy Young. You killed my father. Prepare to die."
    scene sm1mv01s04-92 sy-quotes-inigo-montoya-mc-tries-stacy_c1 with dissolve
    play voice2 d3s7_mcemm noloop
    mc "Stac-"
    play voice3 stacy_angry_aah2 noloop
    play sound sfx_epic_jump1
    play sound2 sfx_sword_whoosh1 noloop
    scene sm1mv01s04-93 sy-swings-mc-dodges-hiayah_c1 with hpunch
    sy "HIYAH!"
    play voice2 mc_hey_hey1 noloop
    if persistent.is_special:
        mc "There is no honor in killing your brother."
    else:
        mc "There is no honor in killing your boyfriend."
    play voice3 stacy_happy_laugh5 noloop
    scene sm1mv01s04-94 mc-hey-no-honor-killing-unarmed-man-sy-you-honorless-dog_c1 with hpunch
    sy "YOU ARE AN HONORLESS DOG! ARRR!"
    play voice2 mc_znames_stacy3 noloop
    play sound sfx_sword_hit_metal1
    scene sm1mv01s04-95 another-swing-mc-wow-stacy-sy-heheh-sorry-couldnt-help_c1 with hpunch
    mc "Woah, Stacy!"
    play voice3 stacy_happy_laugh3 noloop
    sy "Hehehehehe. Sorry, I couldn't help myself."
    scene sm1mv01s04-96 sy-lowers-sword-got-sets-swords-everything-needed-mc-think-so_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "Okay, so we've got the swords, and the sets... I think that's pretty much everything else that we needed before we could start filming."
    play voice2 mc_yes_yeah2 noloop
    mc "I think so too."
    scene sm1mv01s04-97 sy-excited-still-cant-believe-know-pretty-incredible_c1 with dissolve
    play voice3 stacy_surprised_ohmy1 noloop
    sy "I still can't believe this is happening! We're making a pirate movie!"
    play voice2 mc_yes_yes7 noloop
    mc "I know, it's pretty incredible."
    scene sm1mv01s04-98 sy-eeeep_c1 with dissolve
    play voice3 stacy_happy_wooh1 noloop
    sy "Eeeeeep!"
    play sound sfx_leg_kick8
    scene sm1mv01s04-99 sy-hugs-mc-serously-thanks-mc-ofc-stacy_c1 with dissolve
    play voice3 stacy_moan7 noloop
    sy "Seriously, [mcname], thank you for doing this with me."
    play voice2 mc_yes_yeah7 noloop
    mc "Of course, Stacy. And thanks for doing this with me, too."
    scene sm1mv01s04-100 sy-excited-of-course_c1 with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "Of course!"
    scene sm1mv01s04-101 sy-now-prolly-take-down-set-mc-silent_c1 with dissolve
    play voice3 stacy_hmm noloop volume 1.7
    sy "Now, we should probably take down the set. Because we do still live here and it being here is going to be a pain in the ass."
    scene sm1mv01s04-102 mc-that-why-hug-cuz-ask-more-work_c1 with dissolve
    mc "..."
    play voice2 mc_surprised_uh3 noloop
    mc "Is that why you gave me a hug, because you were going to ask me to do more work?"
    scene sm1mv01s04-103 devilish-smile_c1 with dissolve
    pause
    play sound sfx_socks_dancing1 loop
    scene sm1mv01s04-104 sy-runs-towards-stairs-till-meet-agian-mc-live-here-sy-heheheh_c1 with dissolve
    play voice3 stacy_hey_byebye noloop
    sy "Until we meet again, [mcname]!"
    play voice2 mc_thinking_wait2 noloop
    mc "Wait - you live here? What?"
    play voice3 stacy_laugh2 noloop
    sy "Hehehehehehehehehehe!"
    stop sound fadeout 2.5
    scene sm1mv01s04-105 mc-puts-god-she-really-wild-one-should-take-set-down_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "God... she really is the wild one."
    scene sm1mv01s04-106 mc-looking-set-end-scene_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "But, I should get this set taken down..."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(MOVIE_PIRATES, 8, 0, 8)
    return