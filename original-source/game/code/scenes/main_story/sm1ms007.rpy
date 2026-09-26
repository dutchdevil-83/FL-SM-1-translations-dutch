label sm1ms007:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 1.5, "sound3" )
    $ renpy.music.set_volume(1.0, 1.5, "sound2" )
    $ renpy.music.set_volume(0.8, 1.5, "music" )
    play sound3 sfx_cafe_crowd fadein 2.5 volume 0.6
    play music music_boring_restaraunt1 fadein 3.0
    play sound sfx_heels_steps1 volume 0.7 loop fadein 1.0
    play sound2 sfx_heels_steps2 fadein 1.0
    scene sm1ms007-01 mc-sy-waiter-entry1_c1 with dissolve
    pause
    scene sm1ms007-01 mc-sy-waiter-entry1_c2 with dissolve
    play voice4 boy5_happy_mmm2 noloop
    pause
    play sound sfx_bed_slide2 volume 0.7
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1ms007-02 mc-sy-waiter-ask_c2 with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "Isn't this the life?"
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh?"
    sy "We're doing something we love, and it gives us the freedom just to run out and have lunch whenever we want."
    scene sm1ms007-02 mc-sy-waiter-ask_c1 with dissolve
    play voice2 d4s4_mclaugh noloop volume 1.6
    mc "*chuckles* You're right. A lot of other people don't have it so easy."
    scene sm1ms007-03 mc-sy-waiter-talk1_c2 with dissolve
    play voice3 stacy_hey noloop
    if persistent.is_special:
        sy "We don't have it easy either, bro."
        sy "We've been working our butts off since we started this.."
    else:
        sy "We don't have it easy either, [mcname]."
        sy "As your best friend, I can say that we have both been working our butts off since we started this."
    menu:
        "Agree with Stacy"(hint="sm1ms007_m01_h01"):
            call sm1ms007_m01_c01 from _call_sm1ms007_m01_c01
            scene sm1ms007-03 mc-sy-waiter-talk1_c1 with dissolve
            play voice2 mc_yes_yes3 noloop volume 1.4
            mc "You're right. And all that hard work deserves a nice lunch."
            scene sm1ms007-05 mc-sy-waiter-talk3_c2 with dissolve
            play voice3 stacy_yes_simple1 noloop
            sy "Yes, it does!"
        "Disagree with Stacy"(hint="sm1ms007_m01_h02"):
            scene sm1ms007-03 mc-sy-waiter-talk1_c1 with dissolve
            play voice2 mc_no_nah2 noloop
            mc "We've been blessed, Stacy. You have to see that."
            mc "I've talked to some people in the city, and they would kill to be in our shoes."
            scene sm1ms007-04 mc-sy-waiter-talk2_c2 with dissolve
            play voice3 stacy_angryhuh noloop
            sy "No one better even look at my shoes."
            play voice2 mc_surprised_what6 noloop
            scene sm1ms007-05 mc-sy-waiter-talk3_c1 with dissolve
            mc "What?"
            scene sm1ms007-05 mc-sy-waiter-talk3_c2 with dissolve
            play voice3 stacy_arrogant_ha1 noloop
            if persistent.is_special:
                sy "Just yanking your chain, bro."
            else:
                sy "Just yanking your chain, [mcname]."
            sy "I'm just saying that it's not like we've had an easy time getting the studio going."
            sy "And we still have a long and hard road to go."
            scene sm1ms007-06 mc-sy-waiter-talk4_c1 with dissolve
            play voice2 d3s7_mcemm noloop volume 1.6
            pause
            play voice3 stacy_arrogant_huh1 noloop
            sy "What's with you?"
            play voice2 mc_happy_laugh2 noloop
            mc "You said long and hard. Heheh."
            scene sm1ms007-02 mc-sy-waiter-ask_c2 with dissolve
            play voice3 stacy_disappointed_oh1 noloop
            sy "You are so lame."
            sy "Oh, I almost forgot."
    jump sm1ms007_after_choice
label sm1ms007_after_choice:
    scene sm1ms007-09 mc-sy-waiter-talk7_c2 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "All our hard work is starting to pay off, [mcname]."
    scene sm1ms007-09 mc-sy-waiter-talk7_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "What do you mean?"
    scene sm1ms007-05 mc-sy-waiter-talk3_c2 with dissolve
    play voice3 stacy_yay noloop
    sy "This morning, we got our first job request. We're in business, [mcname]!"
    scene sm1ms007-05 mc-sy-waiter-talk3_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "That's awesome. What are the details."
    scene sm1ms007-08 mc-sy-waiter-talk6_c1 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "It's pretty straightforward, just some good guy-on-girl banging."
    sy "The client is open to things getting a little rough, but no like master-pet situation."
    sy "Oh, and they specifically requested some spanking, which should be very easy for us to do."
    scene sm1ms007-08 mc-sy-waiter-talk6_c2 with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Us? You don't want me to ask one of the candidates to do it?"
    scene sm1ms007-09 mc-sy-waiter-talk7_c2 with dissolve
    play voice3 stacy_no_nah4 noloop
    sy "No way."
    sy "This is our first job, [mcname]! Our maiden voyage. Our first step into a larger world."
    sy "I want to put our best foot forward, so I'll be your co-star for this one."
    play sound sfx_cloth_rustling2
    scene sm1ms007-10 mc-sy-waiter-talk8_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Well, that sounds perfect to me. Not like we haven't gotten a little kinky in front of a camera lens."
    scene sm1ms007-10 mc-sy-waiter-talk8_c2 with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Exactly."
    sy "There is one extra detail. The client is super into redhead porn and they want the girl in the scene to be a redhead."
    scene sm1ms007-11 mc-sy-waiter-talk9_c1 with dissolve
    play voice2 mc_yes_okay1 noloop volume 1.4
    mc "Okay, so we'll need some kind of red wig for you to wear."
    mc "I guess I can check out the shop. They have a lot of stuff there, so maybe we'll get lucky."
    scene sm1ms007-10 mc-sy-waiter-talk8_c2 with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "That's okay, [mcname]. I actually already found a decent-looking one online. It will just cost us $50."
    play voice2 mc_thinking_hmm3 noloop
    mc "Nice. Is there anything else we need?"
    scene sm1ms007-12 mc-sy-waiter-talk10_c2 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Yes, we probably should get some money together."
    sy "This will be Kanya's first time as our camera girl, and we don't want to just offer a smile and some dick for her services."
    play voice2 mc_yes_yeah2 noloop
    mc "Totally agree, although I'm always up for a trade like that."
    play voice3 stacy_happy_laugh4 noloop
    sy "Haha. I bet you are."
    scene sm1ms007-12 mc-sy-waiter-talk10_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "So how much money are we talking?"
    scene sm1ms007-13 mc-sy-waiter-face1_c2 with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "I figure $100 should cover us. If she needs a little more, we'll figure it out when we reach that point."
    play voice2 mc_yes_okay3 noloop
    mc "Got it."
    scene sm1ms007-11 mc-sy-waiter-talk9_c1 with dissolve
    play voice2 mc_happy_yay2 noloop volume 1.3
    mc "This is really great, Stacy. Our first gig. I can't believe it."
    scene sm1ms007-12 mc-sy-waiter-talk10_c2 with dissolve
    play voice3 stacy_happy_wooh1 noloop
    sy "We gotta celebrate."
    play voice2 mc_happy_hah2 noloop
    mc "Way ahead of you."
    play sound sfx_heels_steps2 volume 0.7 loop
    scene sm1ms007-24 mc-sy-waiter-signal_c1 with dissolve
    play voice2 mc_hey_hey8 noloop
    mc "A bottle of your most expensive wine, my good man."
    play voice4 boy5_thinking_hmm7 noloop
    "Waiter" "The deux loups fantaisie cabernet sauvignon is five hundred dollars a bottle."
    play sound sfx_hair_scratch1
    scene sm1ms007-25 mc-sy-waiter-talk_c1 with dissolve
    play voice2 d2s12_emmm noloop volume 1.4
    mc "..."
    mc "One bottle of your twenty dollar-ist bottle of wine, please."
    play voice4 boy5_yes_ugu1 noloop volume 1.4
    "Waiter" "Of course, sir."
    play sound sfx_heels_steps2 volume 0.7
    scene sm1ms007-25 mc-sy-waiter-talk_c2 with dissolve
    stop sound fadeout 5.0
    play voice3 stacy_happy_laugh3 noloop
    sy "Hahaha. That was rich. Next, you're going to ask if the bread is free."
    scene sm1ms007-27 mc-sy-waiter-talk3_c1 with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah, yeah. Just figure out what you want to order, gorgeous."
    scene sm1ms007-06 mc-sy-waiter-talk4_c2 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    pause
    scene sm1ms007-28 mc-sy-drink_c1 with fade
    play voice2 mc_thinking_mmm6 noloop volume 1.2
    mc "To our wonderful studio. May it never crash and burn."
    scene sm1ms007-28 mc-sy-drink_c2 with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "And even if it does, let it be a hell of a ride, bro."
    play sound sfx_wineglass_ding1
    scene sm1ms007-29 mc-sy-drink2_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Hear hear."
    play sound sfx_drink_loop1 loop volume 2.3
    scene sm1ms007-30 mc-sy-drink3_c2 with dissolve
    pause
    scene sm1ms007-30 mc-sy-drink3_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1ms007-31 mc-sy-drink4_c2 with dissolve
    play voice3 stacy_hey_happy1 noloop
    sy "You're really doing good, [mcname]."
    scene sm1ms007-31 mc-sy-drink4_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "We're both doing good."
    scene sm1ms007-32 mc-sy-bashful_c1 with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Sure, but you're putting in some extra miles for our dream."
    sy "Getting all the website and video editing stuff prepared is a lot to handle sure, but you've been keeping your nose to the grindstone."
    sy "{b}You{/b} are the one really making this all work so smoothly."
    scene sm1ms007-33 mc-sy-look_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Stacy, you're ruining my plan."
    scene sm1ms007-33 mc-sy-look_c2 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Your plan?"
    scene sm1ms007-34 mc-sy-look2_c1 with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Yes. I wanted to take you out for a special lunch date to show you how much I appreciate all the work {b}you've{/b} been doing for the studio."
    scene sm1ms007-34 mc-sy-look2_c2 with dissolve
    play voice3 stacy_disappointed_oh6 noloop
    sy "Really?"
    play voice2 mc_thinking_mmm3 noloop
    mc "It feels like I've been so busy talking to the girls at my jobs that I don't get to be there and show you just how important you are to me."
    play sound sfx_cloth_rustling2
    scene sm1ms007-35 mc-sy-hand1_c1 with dissolve
    play voice2 mc_happy_a1 noloop volume 1.4
    mc "And your help at the studio is invaluable."
    scene sm1ms007-35 mc-sy-hand1_c2 with dissolve
    play voice3 stacy_disappointed_oh3 noloop
    sy "Come here."
    scene sm1ms007-37 mc-sy-kiss_c1 with dissolve
    pause
    play voice2 mc_pain_auh3 noloop
    play sound sfx_rope_stretch
    scene sm1ms007-38 mc-sy-ear_c2 with hpunch
    mc "Yeouch!"
    play voice3 stacy_angry noloop
    sy "That's for making me think I did something bad, you dork."
    scene sm1ms007-38 mc-sy-ear_c1 with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    mc "Sorry. Sorry."
    play sound sfx_cloth_rustling3
    scene sm1ms007-39 mc-sy-sorry_c2 with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    if persistent.is_special:
        sy "And this is for being the best brother a girl could ask for."
    else:
        sy "And this is for being the best friend a girl like me could ask for."
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1ms007-40 mc-sy-kiss_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    play voice3 stacy_suckmoan3 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1ms007-40 mc-sy-kiss_c2 with dissolve
    play voice3 stacy_suckmoan2 noloop
    play sound mc_kiss2
    sy "Mmmm."
    scene sm1ms007-41 mc-sy-back_c2 with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "Almost better than a morning spanking.{w} Almost."
    scene sm1ms007-41 mc-sy-back_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Never change, Stacy. You're perfect."
    play sound sfx_heels_steps2 fadein 1.5 loop
    scene sm1ms007-42 mc-sy-waiter-walk_c2 with dissolve
    play voice3 stacy_yes_yap2 noloop
    sy "I know."
    sy "And if the waiter weren't coming round with our food, I'd show you just how much I appreciate {b}you{/b}, [mcname]."
    play voice2 mc_angry_errr8 noloop
    mct "Stupid cock-blocking waiter."
    stop sound fadeout 1.0
    scene sm1ms007-43 mc-sy-waiter-food_c1 with fade
    play voice2 mc_eating_mmm noloop
    pause
    play sound sfx_cloth_wiping1 volume 1.6
    scene sm1ms007-43 mc-sy-waiter-food_c2 with dissolve
    pause
    stop sound fadeout 1.5
    scene sm1ms007-44 mc-sy-waiter-bill_c1 with dissolve
    play voice2 d2s9_mchey noloop
    pause
    scene sm1ms007-44 mc-sy-waiter-bill_c2 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "So, what's the damage?"
    play sound sfx_paper_slide1
    scene sm1ms007-45 mc-sy-waiter-bill2_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "Let's just say I'm very glad that we're splitting the bill for this."
    scene sm1ms007-45 mc-sy-waiter-bill2_c2 with dissolve
    play voice3 stacy_uhuh noloop
    sy "I don't think so, buster. First and foremost, {b}this{/b} was a date with your beautiful girlfriend."
    sy "We only talked a little bit about work, so it's your treat."
    scene sm1ms007-46 mc-sy-waiter-bill3_c1 with dissolve
    play voice2 mc_disgust_meh4 noloop
    mc "You've got me there."
    scene sm1ms007-46 mc-sy-waiter-bill3_c2 with dissolve
    play voice3 stacy_laugh4 noloop
    pause
    play sound sfx_bed_slide3 volume 0.5
    scene sm1ms007-47 mc-sy-waiter-stand_c2 with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "This was very nice, [mcname]."
    sy "I'm the luckiest girlfriend in the world."
    play sound2 sfx_cloth_rustling5 noloop
    scene sm1ms007-48 mc-sy-waiter-kiss_c1 with dissolve
    play voice3 stacy_suckmoan1 noloop
    play sound mc_kiss1
    play voice2 mc_thinking_mmm2 noloop
    sy "Mmwaaah."
    scene sm1ms007-48 mc-sy-waiter-kiss_c2 with dissolve
    play sound mc_kiss3
    pause
    if vn_mode:
        stop sound3 fadeout 2.0
        stop music fadeout 3.0
        $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
        $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
        $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
        jump sm1ms007_end
    scene sm1ms007-49 mc-sy-waiter-talk_c2 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "So, you coming back home? Or heading out into the city?"
    menu:
        "I'll come home with you"(hint="sm1ms007_m02_h01"):
            call sm1ms007_m02_c01 from _call_sm1ms007_m02_c01
            scene sm1ms007-49 mc-sy-waiter-talk_c1 with dissolve
            play voice2 d9s2_yeah noloop volume 2.5
            mc "I'll come home with you."
            mc "I feel like chilling a bit after that meal."
            scene sm1ms007-49 mc-sy-waiter-talk_c2 with dissolve
            play voice3 stacy_yes_fine4 noloop
            sy "Perfect."
        "I'm going to check out the city"(hint="sm1ms007_m02_h02"):
            scene sm1ms007-49 mc-sy-waiter-talk_c1 with dissolve
            play voice2 d9s2_yeah noloop volume 2.5
            mc "I'm going to check out the city. I need to earn some extra money."
            scene sm1ms007-49 mc-sy-waiter-talk_c2 with dissolve
            play voice3 stacy_yes_fine3 noloop
            sy "Great. See you at home, handsome."
            play sound sfx_heels_steps1 loop
            scene sm1ms007-50 mc-sy-waiter-end_c1 with dissolve
            pause
            scene sm1ms007-50 mc-sy-waiter-end_c2 with dissolve
            pause
            stop sound fadeout 1.0
    stop sound3 fadeout 2.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1ms007_end
label sm1ms007_end:
    call sm1ms007_activate_storyline from _call_sm1ms007_activate_storyline
    python:
        if player.get_choice("sm1ms007_go_home"):
            StoryController.end_scene(MS, 3, 0, 2, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
        else:
            StoryController.end_scene(MS, 3, 0, 2, PARK, DEFAULT_SUBLOCATION, LPA_CENTER)

    return
label sm1ms007_activate_storyline:
    if player.get_storyline(ARJ_STORY) is False:
        $ StoryController.activate_story_line(ARJ_STORY)
    return
label sm1ms007_m01_c01:
    $ player.set_choice("sm1ms007_agree_with_sy")
    return
label sm1ms007_m02_c01:
    $ player.set_choice("sm1ms007_go_home")
    return
label sm1ms007_unlocks:
    call sm1ms007_m01_c01 from _call_sm1ms007_m01_c01_1
    call sm1ms007_m02_c01 from _call_sm1ms007_m02_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MS)
    return