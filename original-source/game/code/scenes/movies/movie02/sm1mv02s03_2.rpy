image sm1mv02s03-a107-glam = Movie(play = "images/MV/mv02/s03/anim/sm1mv02s03-a107-3x-60fps.webm", start_image = "sm1mv02s03-a107 building-set-kv-mc-glambot-00", image = "sm1mv02s03-a107 building-set-kv-mc-glambot-90",  loop = False)
label sm1mv02s03_2:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play sound sfx_door_openclosed1
    play sound2 sfx_heels_steps2
    scene sm1mv02s03-97 building_the_set_mc_talk_studio with dissolve
    play music take_the_ride_calm
    play voice2 d1s5_mcthinks noloop volume 1.6
    mct "All right, another day, another wall! Or paint! Or whatever it is I need to do!"
    mct "And hopefully no ranting about gods or fury or whatever."
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1mv02s03-98 building_the_set_mc_talk_studio_paint with fade
    play sound2 sfx_brush_painting3
    play sound sfx_paint_smearing5 volume 0.7
    pause
    play sound2 sfx_box_slide noloop
    scene sm1mv02s03-99 building_the_set_montage_wire with fade
    play sound sfx_bed_slide3
    pause
    play sound2 sfx_hammer_loop1
    stop sound fadeout 1.0
    scene sm1mv02s03-100 building_the_set_montage_hammer with fade
    pause
    stop sound2 fadeout 1.0
    scene sm1mv02s03-101 building_the_set_montage_chair with fade
    play sound sfx_chair_slide1
    play sound3 sfx_cloth_suitcase_ride1 noloop
    pause
    stop sound3 fadeout 1.5
    play sound2 sfx_brush_painting2
    play sound sfx_paint_smearing4 volume 0.7
    scene sm1mv02s03-102 building_the_set_montage_paint with fade
    pause
    $ renpy.music.set_volume(0.7, 2.5, "music" )
    stop sound2 fadeout 1.5
    stop sound fadeout 2.0
    scene sm1mv02s03-103 building_the_set_montage_stand_back with fade
    pause
    play voice2 d1s5_orgasm2 noloop
    mct "Damn..."
    scene sm1mv02s03-104 building_the_set_mc_thought_overshoulder with dissolve
    mct "That looks super good."
    play sound sfx_door_closed4
    play sound2 sfx_heels_steps2
    scene sm1mv02s03-105 building_the_set_kv_talk with dissolve
    play voice4 kanya_hey_arrogant noloop
    kv "Yo, yo."
    kv "How's it looking?"
    scene sm1mv02s03-106 building_the_set_mc_talk with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Come check it out for yourself."
    stop sound2 fadeout 1.0
    scene sm1mv02s03-a107 building-set-kv-mc-glambot-00 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 1.4>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1mv02s03-a107-glam
    pause
    play voice4 kanya_surprised_ohmy noloop
    kv "Holy shit..."
    stop sound2 fadeout 1.0
    scene sm1mv02s03-108 building_the_set_mc_talk with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Good holy shit, or bad holy shit?"
    scene sm1mv02s03-109 building_the_set_kv_talk with dissolve
    play voice4 kanya_happy_relief2 noloop
    if player.has_played_scene("sm1cs_tl003"):
        kv "If we didn't still have work to do, I would give you a reward fuck right here and now."
        scene sm1mv02s03-110 building_the_set_mc_talk with dissolve
        play voice2 mc_yes_yes7 noloop
        mc "I mean... we can always postpone working. For a little bit."
    else:
        kv "It looks... fucking incredible, [mcname]."
    scene sm1mv02s03-111 building_the_set_kv_talk_turn with dissolve
    play voice4 kanya_sex_closedmoan1 noloop
    kv "Seriously, [mcname]. You did an amazing job. This looks fucking awesome."
    scene sm1mv02s03-112 building_the_set_mc_talk with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Phew. I'm glad."
    scene sm1mv02s03-113 building_the_set_kv_talk_smile with dissolve
    play voice4 kanya_hey_simple2 noloop
    kv "What?"
    scene sm1mv02s03-114 building_the_set_mc_talk with dissolve
    play voice2 mc_disappointed_ah2 noloop
    if player.has_played_scene("sm1cs_kv005_start"):
        mc "I've come a long way from trying to build sets out of cardboard."
        scene sm1mv02s03-115 building_the_set_kv_talk with dissolve
        play voice4 kanya_arrogant_huh noloop
        kv "Huh?"
        scene sm1mv02s03-116 building_the_set_mc_talk with dissolve
        play voice2 mc_thinking_mmm5 noloop
        mc "Just... something Stacy and I tried once."
    else:
        mc "I just... never thought I'd be building a spaceship in a photo studio for my job."
        scene sm1mv02s03-115 building_the_set_kv_talk with dissolve
        play voice4 kanya_arrogant_huh noloop
        kv "It's pretty cool, right?"
        scene sm1mv02s03-116 building_the_set_mc_talk with dissolve
        play voice2 mc_yes_yes2 noloop
        mc "Best job I ever had."
    play sound sfx_cloth_rustling2
    scene sm1mv02s03-117 building_the_set_kv_talk_drink with dissolve
    play voice4 kanya_yes_yep1 noloop
    kv "You rehydrate a bit. I'll start bringing over the rest of the things we need to set up."
    play sound sfx_cloth_rustling1 volume 1.6
    scene sm1mv02s03-118 building_the_set_mc_talk_water_kv_walk with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Sounds good to me."
    play sound2 sfx_heels_steps2
    scene sm1mv02s03-119 building_the_set_kv_walkout with dissolve
    pause
    play sound2 sfx_door_closed6 noloop
    play sound sfx_drinking_passionately
    scene sm1mv02s03-120 building_the_set_mc_talk_sip with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1mv02s03-121 building_the_set_mc_thought with dissolve
    play voice2 d1s1_mmm noloop volume 1.7
    mct "Man... this looks really good."
    mct "Stacy is going to freak out when she sees it."
    scene sm1mv02s03-122 building_the_set_mc_thought_smile with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "This movie is going to look really good. I hope... I hope people like it."
    mct "We're putting a lot of time and work into this..."
    play sound sfx_drink_loop1 volume 2.5 loop
    scene sm1mv02s03-123 building_the_set_mc_thought_sip with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mct "What am I saying?"
    mct "This is going to go great. I've got faith in us."
    mct "No more negative self talk! Time to... manifest? Yeah, manifest!"
    play sound sfx_door_closed10
    play sound2 sfx_heels_steps2
    scene sm1mv02s03-124 building_the_set_kv_talk with dissolve
    play voice4 kanya_thinking_hmm4 noloop
    kv "All right, [mcname]."
    stop sound2 fadeout 1.0
    scene sm1mv02s03-125 building_the_set_kv_talk_mcturn with dissolve
    play voice4 kanya_happy_woohoo noloop
    kv "Let's get to work!"
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1mv02s03-127 building_the_set_montage_greenscreen with fade
    play sound sfx_metal_fence1 volume 1.4
    pause
    scene sm1mv02s03-128 building_the_set_montage_screen with fade
    play sound2 sfx_metal_fence2 noloop volume 2.0
    pause
    scene sm1mv02s03-129 building_the_set_montage_light with fade
    play sound sfx_wrench_long1
    pause
    stop sound fadeout 1.5
    scene sm1mv02s03-130 building_the_set_montage_picture with fade
    play sound2 sfx_photocamera_flash2 noloop
    pause
    scene sm1mv02s03-131 building_the_set_montage_point with fade
    play sound2 sfx_photocamera_flash2 noloop
    pause
    play sound sfx_light_turn2 volume 1.5
    play sound2 sfx_light_on1 volume 2.5 noloop
    scene sm1mv02s03-132 building_the_set_montage_light with fade
    pause
    $ renpy.music.set_volume(0.7, 2.5, "music" )
    scene sm1mv02s03-133 building_the_set_mc_talk_look set with fade
    play voice2 mc_happy_oof2 noloop
    mc "Damn."
    scene sm1mv02s03-134 building_the_set_kv_talk with dissolve
    play voice4 kanya_hey_simple1 noloop
    kv "You can say that again."
    scene sm1mv02s03-135 building_the_set_mc_talk with dissolve
    mc "..."
    play voice2 mc_happy_oof1 noloop
    mc "Damn."
    scene sm1mv02s03-136 building_the_set_kv_talk with dissolve
    play voice4 kanya_happy_laugh1 noloop
    kv "Hehehehe. Yeah, that was a lot of work."
    scene sm1mv02s03-137 building_the_set_mc_talk with dissolve
    play voice2 mc_happy_a1 noloop
    mc "But it looks really good."
    scene sm1mv02s03-138 building_the_set_kv_talk with dissolve
    play voice4 kanya_yes_yep2 noloop
    kv "Yeah, it does. This movie is going to look fucking great."
    kv "You killed it, [mcname]. Seriously."
    scene sm1mv02s03-139 building_the_set_mc_talk with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Hey, the lighting really brought the set to life!"
    scene sm1mv02s03-140 building_the_set_kv_talk_shrug with dissolve
    play voice4 kanya_yes_long noloop
    kv "But, if you point a bunch of lights at a pile of shit, it just looks like a well lit pile of shit."
    kv "Which is to say, that every part of the movie is important. Including art."
    scene sm1mv02s03-141 building_the_set_mc_talk_smiling with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Thanks, Kanya."
    scene sm1mv02s03-142 building_the_set_kv_talk with dissolve
    play voice4 kanya_no_happy noloop
    kv "No, thank you."
    scene sm1mv02s03-143 building_the_set_kv_talk_lookset with dissolve
    play voice4 kanya_sex_closedmoan5 noloop
    kv "Because this is going to look fucking sick. I am {i}definitely{/i} going to be putting it on my website."
    scene sm1mv02s03-144 building_the_set_mc_talk with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Good! As you should."
    play sound sfx_cloth_rustling3 volume 1.6
    scene sm1mv02s03-145 building_the_set_mc_talk_stretch with dissolve
    play voice2 mc_angry_errr5 noloop
    mc "But I am fucking beat, I'm going to head out."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps2
    scene sm1mv02s03-146 building_the_set_kv_talk with dissolve
    play voice4 kanya_hey_simple2 noloop
    kv "Same. This really tuckered me out. Definitely sleeping in tomorrow."
    scene sm1mv02s03-147 building_the_set_mc_talk_walkout with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "If only I could. Too many things to try and get done."
    scene sm1mv02s03-148 building_the_set_kv_talk_walkout with dissolve
    play voice4 kanya_yes_yeah1 noloop
    kv "Yeah. You are a busy man, [mcname]."
    scene sm1mv02s03-149 building_the_set_mc_talk with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "Well, I try to be."
    scene sm1mv02s03-150 building_the_set_kv_talk_door with dissolve
    play voice4 kanya_arrogant_pff noloop
    kv "Try? Really, [mcname]. You have like a kajillion jobs {i}and{/i} you're helping run a porn studio."
    kv "I don't think you're trying to be busy anymore. You just are."
    play sound sfx_door_open5
    stop sound2 fadeout 1.0
    scene sm1mv02s03-151 building_the_set_mc_talk_door with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "You've got a good point there."
    scene sm1mv02s03-152 building_the_set_mc_talk_lookback with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "Hopefully it all pays off."
    play sound sfx_door_closed1
    scene sm1mv02s03-153 building_the_set_doorclosed with dissolve
    pause
    play sound sfx_door_openclosed1
    play sound2 sfx_heels_steps2
    scene sm1mv02s03-154 building_the_set__mcthought_walkin_studio with Fade(0.5, 0.5, 0.5)
    play voice2 mc_angry_hm2 noloop
    mct "God... manual labor is exhausting. Damn..."
    stop sound2 fadeout 1.0
    scene sm1mv02s03-155 building_the_set_sy_talk_stairs with dissolve
    play voice3 stacy_surprised_huh4 noloop
    sy "Is it done!?"
    scene sm1mv02s03-156 building_the_set_mc_talk with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Yep."
    scene sm1mv02s03-157 building_the_set_sy_talk with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "Eeeeep!"
    play sound sfx_heels_run2 loop
    scene sm1mv02s03-158 building_the_set_mc_talk_stairs with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Woah, calm down Stacy. Last thing I need is for you to trip and smash your face."
    scene sm1mv02s03-159 building_the_set_sy_talk with dissolve
    play voice3 stacy_no_angry2 noloop
    sy "I'm too excited to calm down!"
    stop sound fadeout 1.0
    scene sm1mv02s03-160 building_the_set_sy_talk_halfway with dissolve
    play voice3 stacy_surprised_huh3 noloop
    sy "How does it look?"
    scene sm1mv02s03-161 building_the_set_mc_talk with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Really, really good, honestly."
    scene sm1mv02s03-162 building_the_set_sy_talk with dissolve
    play voice3 stacy_yay noloop
    sy "Eeeeeeeeeep!"
    play voice2 mc_pain_ou1 noloop
    play sound sfx_leg_kick7
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1mv02s03-163 building_the_set_mc_talk_hug with hpunch
    mc "Woah, Stacy! You're going to make us both fall down."
    scene sm1mv02s03-164 building_the_set_sy_talk_hug with dissolve
    play voice3 stacy_happy_laugh4 noloop
    sy "Sorry!"
    scene sm1mv02s03-165 building_the_set_sy_talk_letgo with dissolve
    play voice3 stacy_happy_phew2 noloop
    sy "I'm just super happy to hear that."
    scene sm1mv02s03-166 building_the_set_mc_talk_letgo with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Believe me, I'm happy to tell you."
    mc "But, I am also fucking exhausted, so I'm going to go to sleep."
    scene sm1mv02s03-167 building_the_set_sy_talk with dissolve
    play voice3 stacy_disappointed_oh4 noloop
    sy "Awwwwww-"
    play sound sfx_heels_steps2 loop
    scene sm1mv02s03-168 building_the_set_mc_talk_walkinguptostairs with dissolve
    play voice2 d7s6_moan1 noloop
    mc "I spent the whole day doing manual labor, Stacy."
    play sound2 sfx_heels_steps1
    scene sm1mv02s03-169 building_the_set_sy_talk with dissolve
    play voice3 stacy_pain_mmm2 noloop
    sy "I knooooow. But I want to go see the set!"
    scene sm1mv02s03-170 building_the_set_mc_talk_walkinguptostairs with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "You'll see it, and soon."
    scene sm1mv02s03-171 building_the_set_sy_talk_by_bed with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "You know patience is not one of my strong suits, [mcname]."
    scene sm1mv02s03-172 building_the_set_mc_talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, I am well aware."
    play sound sfx_bed_fall1 volume 2.0
    stop sound2 fadeout 1.0
    scene sm1mv02s03-173 building_the_set_mc_talk_collapse with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "But there is nothing you could do to drag me out of this bed."
    scene sm1mv02s03-174 building_the_set_sy_talk with dissolve
    play voice3 stacy_arrogant_hmm3 noloop
    sy "Sounds like a challen-"
    scene sm1mv02s03-175 building_the_set_mc_talk with dissolve
    play voice2 mc_no_no5 noloop
    mc "It's not a challenge, I'm just really tired."
    scene sm1mv02s03-176 building_the_set_sy_talk_hips with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Promise you'll show it to me soon?"
    scene sm1mv02s03-177 building_the_set_mc_talk with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Promise."
    scene sm1mv02s03-178 building_the_set_sy_talk_smile with dissolve
    play voice3 stacy_happy_phew1 noloop
    sy "Good! Now, I have some more things I have to do."
    scene sm1mv02s03-179 building_the_set_sy_talk_mcpuppy with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "What? What's that look for?"
    play sound sfx_cloth_rustling2
    scene sm1mv02s03-190 building_the_set_mc_talk with dissolve
    play voice2 mc_thinking_mmm3 noloop volume 1.6
    mc "After a long day at work, you don't want to crawl into bed and cuddle?"
    scene sm1mv02s03-191 building_the_set_sy_talk_thinking with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well... when you put it that way..."
    play sound sfx_cloth_rustling4 volume 1.5
    scene sm1mv02s03-192 building_the_set_sy_talk_crawlbed with dissolve
    play voice3 stacy_laugh4 noloop
    sy "How could I refuse your logic?"
    scene sm1mv02s03-193 building_the_set_mc_talk with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "My logic is undeniable."
    play sound sfx_cloth_rustling3
    scene sm1mv02s03-194 building_the_set_sy_talk_cuddlesmile with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "It's definitely {i}something{/i}."
    scene sm1mv02s03-195 building_the_set_mc_talk_cuddlesmile with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, I don't need sass right before bed."
    scene sm1mv02s03-196 building_the_set_sy_talk with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "Then don't say crazy things like \"my logic is undeniable\"."
    scene sm1mv02s03-197 building_the_set_mc_talk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Fair."
    scene sm1mv02s03-198 building_the_set_sy_talk with dissolve
    play voice3 stacy_disappointed_moan3 noloop
    sy "Good night, [mcname]."
    scene sm1mv02s03-199 building_the_set_mc_talk_eyesclosed with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Night, Stacy."
    scene sm1mv02s03-200 building_the_set_sy_closedeyes with dissolve
    pause
    scene black with dissolve
    pause
    jump sm1mv02s03_02_nextday
label sm1mv02s03_02_nextday:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    if vn_mode:
        $ StoryController.end_scene(MOVIE_SCIFI)
        return
    $ gt.add((7 + (24 - gt.curr_hour)), 0, 0)
    $ player.sleep_common_function()
    $ player.progress_storyline(MOVIE_SCIFI)
    return