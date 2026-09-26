image sm1cs_dc-renovation-glambot-1 = Movie(play = "images/Character-Scenes/DC/s-renovation/anim/sm1cs-dc-renovation-a20-2x-50fps.webm", start_image = "sm1cs-dc-renovation-a20 dc-talking-glambot-00000", image = "sm1cs-dc-renovation-a20 dc-talking-glambot-00089", loop = False)
label sm1cs_dc_renovation:
    $ renpy.music.set_volume(0.5, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_golden_day fadein 1.5
    play sound sfx_cleaning_floor2
    scene sm1cs-dc-renovation-16 mc-busy with Fade(0.5, 0.5, 0.5)
    stop sound fadeout 2.0
    pause
    play sound sfx_knock_wood2
    "*Knock, knock*"
    scene sm1cs-dc-renovation-17 mc-thinking with dissolve
    play voice2 mc_thinking_hm noloop
    mct "That must be Debbie!"
    play sound sfx_heels_steps2 loop
    scene sm1cs-dc-renovation-18 mc-walking with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Coming!"
    play sound sfx_door_open1
    scene sm1cs-dc-renovation-19 mc-surprised with dissolve
    play voice2 d3s7_mcemm noloop
    mc "Debbie?"
    scene sm1cs-dc-renovation-a20 dc-talking-glambot-00000 with dissolve
    pause 0.1
    play sound sfx_camera_fly1 volume 2.0
    scene sm1cs_dc-renovation-glambot-1
    pause
    play voice3 girl36_yes_questioning noloop
    dc "Yes?"
    dc "What, is something wrong?"
    stop sound fadeout 1.0
    scene sm1cs-dc-renovation-21 mc-stuttering with dissolve
    play voice2 mc_no_no10 noloop
    if player.has_played_scene("sm1cs_dc007"):
        mc "Uhm, no! I'm just realizing I've never seen you out of uniform before."
    else:
        mc "Uhm, no! I just forget what you look like without your cop hat."
    play sound sfx_heels_steps2
    play sound2 sfx_heels_steps1
    play sound3 sfx_door_closed1 noloop
    scene sm1cs-dc-renovation-22 dc-walking with dissolve
    play voice3 girl36_arrogant_huh1 noloop
    dc "What, did you think the only outfit I had was my work uniform?"
    scene sm1cs-dc-renovation-23 mc-stuttering with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I mean..."
    scene sm1cs-dc-renovation-24 dc-talking with dissolve
    play voice3 girl36_angry_ugh2 noloop
    dc "Oh stop it, you!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-dc-renovation-25 dc-impressed with dissolve
    play voice3 girl36_surprised_oh noloop
    dc "Wow, this is a great place you've got here, [mcname]."
    scene sm1cs-dc-renovation-26 mc-talking with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thanks, I have a killer real estate agent who found it for me!"
    scene sm1cs-dc-renovation-27 dc-talking with dissolve
    play voice3 girl36_thinking_hmm noloop
    dc "I'll have to get their number if I ever decide to move. The guy who rented me my apartment was..."
    scene sm1cs-dc-renovation-28 dc-talking with dissolve
    play voice3 girl36_disappointed_eeh noloop
    dc "Well, let's just say that if I had any other option for a place to live, I would've taken it."
    dc "But enough about my troubles! I'm here to help you!"
    dc "So what still needs to be done?"
    scene sm1cs-dc-renovation-29 mc-talking with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Let's see... I think some of the uhm... 2 by 4s in the walls need reinforcing. I know we're going to hang lots of photos."
    mc "And there's been this weird problem with the lights I can't fix today."
    scene sm1cs-dc-renovation-30 dc-lets-get-started with dissolve
    play voice3 girl36_thinking_oh noloop
    dc "Well why don't I get a hammer and I can start with the walls?"
    scene sm1cs-dc-renovation-31 mc-great with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "That sounds great!"
    play sound sfx_cloth_rustling3
    scene sm1cs-dc-renovation-32 mc-finding-hammer with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.7
    mc "Let's see..."
    play sound sfx_skirt_off2
    scene sm1cs-dc-renovation-33 mc-giving-her-hammer with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Here you go!"
    scene sm1cs-dc-renovation-34 dc-taking-it-and-thanking with dissolve
    play voice3 girl36_yes_aga noloop
    dc "Thanks, [mcname]!"
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    play sound sfx_hammer_loop1 volume 0.6
    scene sm1cs-dc-renovation-35 mc-dc-montage-working with fade
    pause
    play sound sfx_wrench_long1 volume 0.7
    scene sm1cs-dc-renovation-36 mc-dc-montage-working with dissolve
    pause
    play sound sfx_box_slide volume 0.7
    scene sm1cs-dc-renovation-37 mc-dc-montage-working with dissolve
    pause
    play sound sfx_hammer_loop1 volume 0.5
    scene sm1cs-dc-renovation-38 mc-dc-montage-working with dissolve
    pause
    play sound sfx_bed_slide3
    scene sm1cs-dc-renovation-39 mc-dc-montage-working with dissolve
    pause
    scene sm1cs-dc-renovation-40 mc-dc-montage-working with dissolve
    play sound sfx_handwork_flowerbreak1
    pause
    play sound sfx_hammer_loop1 volume 0.5
    scene sm1cs-dc-renovation-41 mc-dc-montage-working with dissolve
    pause
    $ renpy.music.set_volume(0.65, 3.0, "music" )
    stop sound fadeout 1.0
    scene sm1cs-dc-renovation-42 dc-talking with fade
    play voice3 girl36_surprised_wow noloop
    dc "Wow, you weren't kidding about how much work this place needed!"
    scene sm1cs-dc-renovation-43 mc-ye with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah..."
    scene sm1cs-dc-renovation-44 dc-hows-that-coming with dissolve
    play voice3 girl36_arrogant_huh3 noloop
    dc "How's this coming along?"
    scene sm1cs-dc-renovation-45 mc-not-great with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "I don't know."
    scene sm1cs-dc-renovation-46 mc-frustrated with dissolve
    play voice2 mc_angry_errr7 noloop
    mc "I've tried everything I could think of... I still can't get the lights to turn on."
    scene sm1cs-dc-renovation-47 dc-asking with dissolve
    play voice3 girl36_thinking_eem noloop
    dc "You sure there's a bulb screwed into the socket?"
    play sound sfx_cloth_rustling2
    scene sm1cs-dc-renovation-48 mc-informing with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah. New bulbs, new wires, new everything. I don't know what I'm doing wrong."
    scene sm1cs-dc-renovation-49 dc-mind-if-i-look with dissolve
    play voice3 girl36_surprised_huh1 noloop
    dc "Do you mind if I take a look?"
    scene sm1cs-dc-renovation-50 mc-sure with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Please."
    play sound sfx_cloth_rustling3
    scene sm1cs-dc-renovation-51 dc-hmm with dissolve
    play voice3 girl36_happy_mmm noloop
    dc "Hmmm."
    scene sm1cs-dc-renovation-52 mc-asking with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "Do you see something?"
    scene sm1cs-dc-renovation-53 dc-asking with dissolve
    play voice3 girl36_arrogant_hmf noloop
    dc "Maybe...{w} have you got a screwdriver?"
    scene sm1cs-dc-renovation-54 mc-somwhere-around with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Somewhere around here, yeah."
    play sound [sfx_armor_equiped1, sfx_armor_equiped2]
    scene sm1cs-dc-renovation-55 mc-looking-for-screwdriver with dissolve
    pause
    play sound sfx_sword_equiped1
    scene sm1cs-dc-renovation-56 mc-giving-her-screwdriver with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Here you go!"
    play sound sfx_cloth_rustling5
    scene sm1cs-dc-renovation-57 dc-holding-it with dissolve
    pause
    play sound sfx_cloth_rustling1
    scene sm1cs-dc-renovation-58 dc-holding-it with dissolve
    pause
    play sound sfx_gambling_knobs1
    scene sm1cs-dc-renovation-59 dc-shoving-it-inside-the-switch with dissolve
    play voice3 girl36_disappointed_aah noloop
    dc "I'll just give that a little jiggle... and tighten that... and..."
    play sound sfx_light_turn2 volume 2.0
    scene sm1cs-dc-renovation-60 dc-getting-up with dissolve
    pause
    scene sm1cs-dc-renovation-61 mc-shocked with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "Oh my God! You did it! How!?"
    scene sm1cs-dc-renovation-62 dc-explaining with dissolve
    play voice3 girl36_disappointed_oof noloop
    dc "Oh, it was a silly problem."
    play sound sfx_cloth_rustling3
    scene sm1cs-dc-renovation-63 dc-explaining with dissolve
    play voice3 girl36_arrogant_yeah2 noloop
    dc "The way this switch is wired has a ground wire that was all tangled up."
    dc "And one of your connections was loose. You had it like 90 percent of the way there."
    scene sm1cs-dc-renovation-64 mc-really with dissolve
    play voice2 mc_angry_really noloop
    mc "Really? That was it?"
    play sound sfx_cloth_rustling2
    scene sm1cs-dc-renovation-65 dc-explaining with dissolve
    play voice3 girl36_yes_yep noloop
    dc "Yep, that was it. I think you just spent too long staring into that little hole."
    dc "Tunnel vision gets even the-"
    play sound sfx_hair_scratch1
    scene sm1cs-dc-renovation-66 dc-realising with dissolve
    play voice3 girl36_surprised_ohmy2 noloop
    dc "Oh my God..."
    scene sm1cs-dc-renovation-67 mc-huh with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What? Are you okay?"
    scene sm1cs-dc-renovation-68 dc-stuttering with dissolve
    play voice3 girl36_disappointed_moan noloop
    dc "I, erm..."
    play voice2 mc_hey_hey6 noloop
    mc "Debbie, you can tell me."
    dc "I just heard what I said and... it sounds like such an innuendo."
    scene sm1cs-dc-renovation-69 mc-comforting with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "That wasn't what I was thinking, but now that you've said it..."
    mc "I think I get tunnel vision every time I stare into a little hole!"
    scene sm1cs-dc-renovation-72 dc-smiling with dissolve
    play voice3 girl36_arrogant_laugh noloop
    dc "Ha, ha. Very funny, [mcname]."
    scene sm1cs-dc-renovation-73 mc-smiling with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.4
    pause
    scene sm1cs-dc-renovation-74 mc-realising with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Oh shit! I haven't offered you water or anything! You must have world up a thirst."
    scene sm1cs-dc-renovation-75 dc-talking with dissolve
    play voice3 girl36_yes_happy2 noloop
    dc "Water actually sounds really nice right now."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-dc-renovation-76 dc-impressed with dissolve
    play voice3 girl36_disappointed_oh noloop
    dc "Man... your apartment is so big!"
    scene sm1cs-dc-renovation-77 mc-talking with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well, part of that is also because we plan to film here."
    scene sm1cs-dc-renovation-78 dc-talking with dissolve
    play voice3 girl36_arrogant_yeah3 noloop
    dc "I remember you saying that. I just thought it might be, I don't know... smaller. And that there wouldn't be so many bedrooms."
    play sound sfx_bottle_pouring1
    stop sound2 fadeout 1.0
    scene sm1cs-dc-renovation-79 mc-getting-water with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Yep! I figure if I can live at where I work, I can save some money on rent."
    scene sm1cs-dc-renovation-80 dc-sure with dissolve
    play voice3 girl36_arrogant_he noloop
    dc "That's pretty smart."
    scene sm1cs-dc-renovation-81 mc-passing-the-water with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "You have to do whatever you have to do to make it as a small business!"
    play sound sfx_cloth_rustling1
    scene sm1cs-dc-renovation-82 dc-taking-the-water with dissolve
    play voice3 girl36_happy_yay noloop
    dc "Very true!"
    play sound sfx_drinking_passionately
    scene sm1cs-dc-renovation-83 dc-drinking with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-dc-renovation-84 dc-thanks with dissolve
    play voice3 girl36_happy_phew2 noloop
    dc "Oh, that really hit the spot. Thank you, [mcname]."
    scene sm1cs-dc-renovation-85 mc-np with dissolve
    play voice2 d9s2_ugu noloop
    mc "Of course!"
    play sound sfx_cloth_rustling2
    scene sm1cs-dc-renovation-86 mc-asking with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "So I'm curious... when did you get so good at doing this kind of work?"
    scene sm1cs-dc-renovation-87 dc-objecting with dissolve
    play voice3 girl36_surprised_why2 noloop
    dc "Why? Do I not look like someone who would be handy?"
    scene sm1cs-dc-renovation-88 mc-talking with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, I just thought you were a cop and not a carpenter."
    scene sm1cs-dc-renovation-89 dc-laughing with dissolve
    play voice3 girl36_happy_laugh1 noloop
    dc "Fair! Well..."
    play sound sfx_drink_loop1 volume 2.0
    scene sm1cs-dc-renovation-90 dc-drinking with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-dc-renovation-91 dc-talking with dissolve
    play voice3 girl36_thinking_hmm noloop
    dc "When I lived out on the coast, the town I was in was super small."
    dc "If something broke, it would take forever to get someone to come out and fix it."
    dc "So I started learning how to fix things around the house, because they needed fixing."
    scene sm1cs-dc-renovation-92 dc-smiling with dissolve
    play voice3 girl36_disgust_oof noloop
    dc "I'll never forget... the first thing that I had to fix was a busted water pipe!"
    scene sm1cs-dc-renovation-93 mc-shocked with dissolve
    play voice2 mc_surprised_what8 noloop
    mc "What!"
    scene sm1cs-dc-renovation-94 dc-talking with dissolve
    play voice3 girl36_yes_happy1 noloop
    dc "Yep. It was my shower line... I had just got home from a patrol on the beach, I was covered in sand and sweat."
    scene sm1cs-dc-renovation-95 dc-smiling with dissolve
    play voice3 girl36_disgust_mneagh noloop
    dc "I walked in the door, went to the bathroom, and there was an inch of water on the ground!"
    dc "I tried calling the plumber, but he said it was going to be 3 days before he could get to me."
    dc "And I needed a shower as soon as possible. I had sand in all of the worst places."
    play sound sfx_drink_loop1 volume 2.0
    scene sm1cs-dc-renovation-96 dc-drinking with dissolve
    pause
    play sound sfx_cup_place1 volume 2.5
    scene sm1cs-dc-renovation-97 dc-telling-him with dissolve
    play voice3 girl36_angry_breath noloop
    dc "So I started looking things up on the internet, grabbed some tools I had around the house, and started trying to fix it myself."
    dc "It may have taken 6 hours, but I did it!"
    scene sm1cs-dc-renovation-98 mc-astonished with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Wow..."
    scene sm1cs-dc-renovation-99 dc-talking with dissolve
    play voice3 girl36_happy_yeah noloop
    dc "But since then, I've tried to fix things around my place instead of calling someone."
    scene sm1cs-dc-renovation-100 mc-impressed with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "That's pretty awesome, Debbie."
    scene sm1cs-dc-renovation-101 dc-talking with dissolve
    play voice3 girl36_surprised_oh noloop
    dc "Oh, it's nothing. I mean - look at you!"
    scene sm1cs-dc-renovation-102 dc-looking-around with dissolve
    play voice3 girl36_happy_relief1 noloop
    dc "You're renovating a whole studio! What I've done is nothing compared to that!"
    scene sm1cs-dc-renovation-103 mc-talking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, I don't know about all that."
    mc "We've been here for a few hours, and you got so much done, {i}and{/i} you solved my problem to!"
    play sound sfx_cloth_rustling1
    scene sm1cs-dc-renovation-104 dc-blushing with dissolve
    play voice3 girl36_no_nah1 noloop
    dc "Oh, it was nothing!"
    scene sm1cs-dc-renovation-105 dc-asking-to-leave with dissolve
    play voice3 girl36_arrogant_huh2 noloop
    dc "But, speaking of showers, I think I'm going to head home and take one. I'm starting to get a little sticky."
    scene sm1cs-dc-renovation-106 mc-makes-sense with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Oh yeah! That makes sense."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1cs-dc-renovation-107 mc-dc-walking with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Seriously, Debbie. You were such a help today. Thank you!"
    scene sm1cs-dc-renovation-108 dc-np with dissolve
    play voice3 girl36_no_happy noloop
    dc "Oh, don't mention it, [mcname]. Seriously, I was just happy to help."
    scene sm1cs-dc-renovation-109 mc-dc-np-talking with dissolve
    play voice3 girl36_happy_phew1 noloop
    dc "Besides, you've helped me catch one criminal, and helped me pursue another."
    dc "I owe you one."
    scene sm1cs-dc-renovation-110 mc-smiling with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Consider us even!"
    scene sm1cs-dc-renovation-111 dc-talking with dissolve
    play voice3 girl36_no_calm1 noloop
    dc "Oh, I don't think we're even."
    dc "But I think the scales are a little more balanced now."
    play voice2 mc_thinking_mmm7 noloop
    mc "Well, Officer Callahan, we'll have to find a way to make us even!"
    dc "Mmmmm, I guess we will!"
    play sound sfx_door_open1
    stop sound2 fadeout 1.0
    scene sm1cs-dc-renovation-112 dc-going with dissolve
    play voice3 girl36_yes_aga noloop
    dc "You think on that, and let me know when you come up with something!"
    scene sm1cs-dc-renovation-113 mc-bye with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I will. Enjoy the rest of your night, Debbie!"
    scene sm1cs-dc-renovation-114 dc-bye with dissolve
    play voice3 girl36_hey_bye5 noloop
    dc "And you, yours, [mcname]!"
    play sound sfx_door_closed1
    play sound2 sfx_heels_steps2
    scene sm1cs-dc-renovation-115 mc-walking-back with dissolve
    pause
    stop sound2 fadeout 1.0
    jump sm1cs_dc_renovation_exit_to_studio
label sm1cs_dc_renovation_exit_to_studio:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ renovation_controller.set_progress(renovation_controller.get_renovation_scenes_progress())
    $ renovation_controller.set_daily_limit()
    $ StoryController.end_scene_without_storyline("sm1cs_dc_renovation", 4, 0, 6, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return