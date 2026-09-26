image sm1cs-cw004-a167-1 = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a167-1-2x-50fps.webm", start_image = "sm1cs-cw004-a167-1 cw-hj-anim-01")
image sm1cs-cw004-a167-1-f = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a167-1-2x-60fps.webm", start_image = "sm1cs-cw004-a167-1 cw-hj-anim-01")
image sm1cs-cw004-a167-2 = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a167-2-2x-50fps.webm", start_image = "sm1cs-cw004-a167-2 cw-hj-anim-01")
image sm1cs-cw004-a167-2-f = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a167-2-2x-60fps.webm", start_image = "sm1cs-cw004-a167-2 cw-hj-anim-01")
image sm1cs-cw004-a167-3 = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a167-3-2x-50fps.webm", start_image = "sm1cs-cw004-a167-3 cw-hj-anim-01")
image sm1cs-cw004-a167-3-f = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a167-3-2x-60fps.webm", start_image = "sm1cs-cw004-a167-3 cw-hj-anim-01")
image sm1cs-cw004-a167-4 = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a167-4-2x-50fps.webm", start_image = "sm1cs-cw004-a167-4 cw-hj-anim-01")
image sm1cs-cw004-a167-4-f = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a167-4-2x-60fps.webm", start_image = "sm1cs-cw004-a167-4 cw-hj-anim-01")
image sm1cs-cw004-a187-1 = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a187-1-2x-50fps.webm", start_image = "sm1cs-cw004-a187-1 cw-bj-anim-01")
image sm1cs-cw004-a187-1-f = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a187-1-2x-60fps.webm", start_image = "sm1cs-cw004-a187-1 cw-bj-anim-01")
image sm1cs-cw004-a187-2 = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a187-2-2x-50fps.webm", start_image = "sm1cs-cw004-a187-2 cw-bj-anim-01")
image sm1cs-cw004-a187-2-f = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a187-2-2x-60fps.webm", start_image = "sm1cs-cw004-a187-2 cw-bj-anim-01")
image sm1cs-cw004-a187-3 = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a187-3-2x-50fps.webm", start_image = "sm1cs-cw004-a187-3 cw-bj-anim-01")
image sm1cs-cw004-a187-3-f = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a187-3-2x-60fps.webm", start_image = "sm1cs-cw004-a187-3 cw-bj-anim-01")
image sm1cs-cw004-a187-4 = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a187-4-2x-50fps.webm", start_image = "sm1cs-cw004-a187-4 cw-bj-anim-01")
image sm1cs-cw004-a187-4-f = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a187-4-2x-60fps.webm", start_image = "sm1cs-cw004-a187-4 cw-bj-anim-01")
image sm1cs-cw004-a95-glambot = Movie(play = "images/FS_IT/CW/s004/anim/sm1cs-cw004-a95-2x-50fps.webm", start_image = "sm1cs-cw004-a95 cw-smiles-looks-away-glambot-000_i", image = "sm1cs-cw004-a95 cw-smiles-looks-away-glambot-119_i", loop = False)
label sm1cs_cw004:
    $ renpy.music.set_volume(0.7, 3.0, "freeroam_music1" )
    play sound sfx_heels_steps2 loop
    scene sm1cs-cw004-01 mc-walks-up-to-cw-office-kitchen_c1 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-cw004-01-02 mc-waves-hi-claire_c1 with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Hi Claire."
    scene sm1cs-cw004-01-03 cw-hello-mc-please-call-ms-watts-unless-instructed_c1 with dissolve
    play voice3 girl29_hey_provocative noloop
    cw "Hello, Mr. [mcname]."
    cw "Please continue to call me Ms. Watts unless otherwise instructed."
    play sound sfx_hair_scratch1
    scene sm1cs-cw004-01-04 mct-dont-understand-why-she-still-so-formal-mc-right-how-can-help-ms-watts_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "I don't understand why she still acts so formal after the lunch with her parents."
    mc "Right. How can I help you, Ms. Watts?"
    scene sm1cs-cw004-01-05 cw-talking-cw-get-right-chase-thought-showing-up-buy-time-parents_c1 with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "I'll get it right to the chase."
    cw "I thought that you showing up during that lunch would buy me a few months of quiet from my folks."
    scene sm1cs-cw004-01-06 cw-instead-they-latched-idea-sighs-swear-sometimes_c1 with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "But instead, they've latched onto the idea of us being together."
    cw "*sighs* I swear... I feel like they get their kicks thinking of me in some house, cooking, and nursing their grandchild."
    scene sm1cs-cw004-01-07 cw-nothing-else-explain-mc-dont-really-understand_c1 with dissolve
    play voice3 girl29_disgust_meh noloop
    cw "Nothing else would explain how much they like to meddle."
    play voice2 mc_thinking_mmm5 noloop
    mc "I don't really understand, but if there is something I can do to help, I'm here for you."
    scene sm1cs-cw004-01-08 cw-silent-there-is-actually_c1 with dissolve
    cw "..."
    play voice3 girl29_yes_yep noloop
    cw "There is, actually."
    play sound sfx_cloth_rustling1
    scene sm1cs-cw004-01-09 cw-folks-invited-on-corellia-yacht-they-rent-weekends_c1 with dissolve
    play voice3 girl29_thinking_mmm1 noloop
    cw "My folks asked me to invite you out for a weekend trip on the {i}Corellia{/i}. We will leave Saturday morning and come back Monday morning."
    cw "The {i}Corellia{/i} is a yacht they rent for weekend trips."
    scene sm1cs-cw004-01-10 mc-whoah-they-loaded-they-do-fine-not-your-concern_c1 with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Woah. They must be loaded."
    scene sm1cs-cw004-01-11 cw-only-concern-show-up-weekend-mc-so-another-favor-you-need_c1 with dissolve
    play voice3 girl29_yes_aga1 noloop
    cw "They do fine. But that isn't your concern."
    cw "Your only concern is showing up for the weekend and helping me to keep up this ill-fated charade."
    play voice2 mc_thinking_hmm2 noloop
    mc "So this is another favor you need."
    scene sm1cs-cw004-01-12 cw-silent-mc-calls-claire_c1 with dissolve
    cw "..."
    play voice2 d2s9_confused noloop volume 1.6
    mc "Claire?"
    scene sm1cs-cw004-01-13 mct-worries-did-push-far_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Did I push too far?"
    scene sm1cs-cw004-01-14 cw-you-right-need-help-again-obvs-can-pay_c1 with dissolve
    play voice3 girl29_yes_serious noloop
    cw "You're right. I need your help again."
    cw "Obviously, I can't pay you for your time without violating a huge number of HR and ethical lines..."
    scene sm1cs-cw004-01-15 cw-call-decency-cw-if-dont-show-up-say-broke-up_c1 with dissolve
    play voice3 girl29_thinking_mmm2 noloop
    cw "But I can call on your basic decency."
    cw "If you don't show up, I'm probably going to have to say that we broke up."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw004-01-16 cw-not-ready-face-judgement-cw-still-not-recovered-last-breakup-talk_c1 with dissolve
    play voice3 girl29_disappointed_mff noloop
    cw "And I am not ready to face their judgemental looks."
    cw "I still haven't recovered from their last \"breakup pep talk\"."
    play sound sfx_fridge_open1
    scene sm1cs-cw004-01-17 cw-nonetheless-cant-find-heart-help-understand_c1 with dissolve
    play voice3 girl29_thinking_hmm2 noloop
    cw "Nonetheless, if you absolutely can't find it within your heart to assist someone in need..."
    cw "I will understand."
    play sound sfx_fridge_closed1 volume 0.6
    scene sm1cs-cw004-01-18 mc-choice-menu-screen_c1 with dissolve
    menu:
        "I will help you Claire"(hint="sm1cs_cw004_m01_h01"):
            call sm1cs_cw004_m01_c01 from _call_sm1cs_cw004_m01_c01
            jump sm1cs_cw004_onramp
        "I don't think so Claire"(hint="sm1cs_cw004_m01_h02"):
            play sound sfx_cloth_rustling2
            scene sm1cs-cw004-01-20 choice-refuse-mc-mc-sorry-would-be-much-wish-things-different_c1 with dissolve
            play voice2 mc_disappointed_ah2 noloop
            mc "I'm sorry. I think that would be way too much for me, Claire."
            mc "I wish things were different."
            scene sm1cs-cw004-01-21 cw-sad-understanding-ofcourse-leave-now_c1 with dissolve
            play voice3 girl29_disappointed_oh noloop
            cw "Of course. I understand, [mcname]."
            cw "*quietly* You can leave now."
            jump sm1cs_cw004_reject_cw
label sm1cs_cw004_onramp:
    if player.get_choice("sm1cs-cw004-offramp"):
        $ player.progress_storyline(CW_STORY, -1)
        $ player.set_choice("sm1cs-cw004-offramp", False)
    scene sm1cs-cw004-01-19 choice-will-help-mc-will-help-cw-smiling_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    mc "I will help you Claire."
    mc "As long as you think this is a good idea."
    scene sm1cs-cw004-01-22 mc-as-long-think-good-idea-cw-thankss-mc-mean_c1 with dissolve
    play voice3 girl29_happy_relief noloop
    cw "Thank you, [mcname]. I mean..."
    scene sm1cs-cw004-01-23 cw-back-normal-ahem-mr-young-cw-sure-will-be-fine-go-over-details_c1 with dissolve
    play voice3 girl29_pain_cough1 noloop
    cw "*ahem* Mr. Young."
    cw "And I'm sure it will be fine. We're both capable."
    play sound sfx_cloth_rustling2 loop
    scene sm1cs-cw004-01-24 cw-leaves-will-explain-tomorrow-for-love-god-no-late_c1 with dissolve
    play voice3 girl29_thinking_hm noloop
    cw "I will text you instructions tomorrow morning."
    cw "And for the love of god, don't be late."
    stop sound fadeout 1.0
    jump sm1cs_cw004_docks
label sm1cs_cw004_docks:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.set_volume(0.0, 2.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 2.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 2.0, "freeroam_sound2" )
    scene black
    show screen scene_transistion(_("Saturday Morning"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound4 sfx_seawaves_ambience1 fadein 1.5
    play sound3 sfx_sea_guls_1 noloop
    play sound sfx_heels_steps1 loop fadein 3.5
    play sound2 sfx_heels_steps2 fadein 3.5
    scene sm1cs-cw004-02 mc-cw-walking-towards-docks_c1 with Fade(0.5, 0.5, 0.5)
    $ renpy.music.play(audio.music_miami_reggae2, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_miami_reggae2_drums, "music2", True, None, True, 0.0)
    pause
    scene sm1cs-cw004-03 cw-cant-believe-happening-terrible-idea_c1 with dissolve
    play voice3 girl29_surprised_ehh noloop
    cw "I can't believe this is happening."
    cw "This is a terrible idea."
    scene sm1cs-cw004-04 mc-choice-menu-screen_c1 with dissolve
    menu:
        "It was yours"(hint="sm1cs_cw004_m02_h01"):
            scene sm1cs-cw004-05 choice-your-idea-mc-was-your-bad-idea-had-bad-feeling_c1 with dissolve
            play voice2 mc_yes_yeah5 noloop
            mc "It was yours. I had a bad feeling from the start."
            scene sm1cs-cw004-06 cw-know-but-have-press-on_c1 with dissolve
            play voice3 girl29_yes_aga2 noloop
            cw "I know. But... we're just going to have to press on."
        "It's going to be okay, Claire"(hint="sm1cs_cw004_m02_h02"):
            call sm1cs_cw004_m02_c02 from _call_sm1cs_cw004_m02_c02
            scene sm1cs-cw004-07 choice-gonna-be-okay-mc-all-okay-got-through-lunch_c1 with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "It's all going to be okay, Claire."
            mc "We got through lunch."
            scene sm1cs-cw004-08 mc-we-get-through-this_c1 with dissolve
            play voice2 mc_thinking_hmm9 noloop
            mc "We'll get through this."
            scene sm1cs-cw004-09 cw-looking-at-mc-pouty-silent_c1 with dissolve
            pause
            scene sm1cs-cw004-10 mc-cw-walk-in-silent_c1 with dissolve
            pause
            scene sm1cs-cw004-11 cw-looks-mc-very-good-point-here-we-go_c1 with dissolve
            play voice3 girl29_arrogant_he noloop
            cw "That's a very good point, [mcname]."
            cw "Here we go."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-cw004-12 cw-looks-mc-oh-almost-forgot-cw-tried-but-insisted-cabin-together_c1 with dissolve
    play voice3 girl29_thinking_oh noloop
    cw "Oh, I almost forgot."
    cw "I tried and tried, but they insisted that we share a cabin together."
    scene sm1cs-cw004-13 cw-sure-noticed-if-one-us-sleeping-on-couch_c1 with dissolve
    play voice3 girl29_thinking_hmm4 noloop
    cw "And I'm sure they would notice if..."
    cw "Ahem. If one of us was just sleeping on a couch on the deck."
    scene sm1cs-cw004-14 mc-all-good-so-long-you-share-pillows_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "It's all good. I can survive sleeping on the floor."
    mc "So long as you share some pillows."
    scene sm1cs-cw004-15 cw-amused-kind-offer-both-adults-only-sleeping_c1 with dissolve
    play voice3 girl29_yes_aga3 noloop
    cw "It's kind of you to offer."
    cw "But we are both adults, and I trust that I don't need to say that we will just be sleeping while we are aboard the boat."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw004-16 mc-of-course_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course."
    play sound sfx_ship_horn1
    scene sm1cs-cw004-17 mc-cw-look-towards-yacht_c1 with dissolve
    pause
    scene sm1cs-cw004-18 fw-chw-waving-from-yacht_c1 with dissolve
    pause
    scene sm1cs-cw004-19 fw-hey-two-chw-great-see-you-two_c1 with dissolve
    play voice4 girl9_hey_happy2 noloop
    fw "Hello, you two!"
    play voice5 boy7_hey_simple noloop
    chw "Great to see you, sweetheart."
    play sound3 sfx_ship_inside1 fadein 3.0
    queue sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-cw004-20 cw-smiling-greeting-getting-on-board-hi-daddy_c1 with dissolve
    play voice3 girl29_hey_happy noloop
    cw "Hi Daddy."
    play sound2 sfx_bag_fall1 noloop
    scene sm1cs-cw004-21 cw-mc-on-board-cw-goes-hug-father_c1 with dissolve
    pause
    play sound sfx_cloth_rustling4
    scene sm1cs-cw004-22 cw-hugs-dad-mmm_c1 with dissolve
    play voice3 girl29_thinking_hmm2 noloop
    cw "Mmm."
    play sound sfx_cloth_rustling3
    scene sm1cs-cw004-23 cw-hugs-fw-cw-not-think-see-soon-fw-we-couldnt-wait_c1 with dissolve
    play voice3 girl29_happy_laugh5 noloop
    cw "I didn't think I'd see you again so soon."
    play voice4 girl9_surprised_oh noloop
    fw "Oh we couldn't wait. Once we heard the {i}Corellia{/i} was available, we knew we had to get you two out for a trip."
    scene sm1cs-cw004-24 cw-nervous-smile-so-great-available_c1 with dissolve
    play voice3 girl29_happy_yeah noloop
    cw "*nervous* So great it was available..."
    play sound sfx_throw_something1
    scene sm1cs-cw004-25 chw-hold-there-moment-mct-uh-oh_c1 with dissolve
    play voice5 boy7_hey_serious noloop
    chw "Hold on there a moment, [mcname]."
    mct "Uh oh."
    scene sm1cs-cw004-26 chw-trying-pull-fast-me-mc-no-dont-think-so_c1 with dissolve
    play voice5 boy7_surprised_huh2 noloop
    chw "Are you trying to pull a fast one on me, son?"
    play voice2 mc_no_no2 noloop
    mc "No. I don't think so."
    scene sm1cs-cw004-27 chw-ask-permission-mc-oh-yeah-uh_c1 with dissolve
    play voice5 boy7_disappointed_hmm noloop
    chw "Then you'll be asking permission to come aboard my vessel?"
    scene sm1cs-cw004-28 mc-can-come-board-chw-permission-granted_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh yeah. Uh."
    mc "Can I come aboard, sir?"
    play voice5 boy7_yes_happy noloop
    chw "Permission granted. Welcome aboard the {i}Corellia{/i}."
    scene sm1cs-cw004-29 mc-thanks_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thanks."
    play sound sfx_heels_steps2 loop
    scene sm1cs-cw004-30 mc-goes-nice-boat-chw-favourite-toy_c1 with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "It's a great yacht."
    play voice5 boy7_yes_low noloop
    chw "Yes. She is one of our favorite treat-yourself toys."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw004-31 chw-when-retire-mc-had-money-do-same_c1 with dissolve
    play voice5 boy7_thinking_hmm2 noloop
    chw "When we retire, we might buy one all on our own."
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "If I had the money, I'd do the same."
    scene sm1cs-cw004-32 fw-ofc-wanted-first-grandkids-chw-as-agreed-gorgeous_c1 with dissolve
    play voice4 girl9_thinking_emm noloop
    fw "Of course, if we were to become grandparents, the personal yacht would have to wait a little."
    play voice5 boy7_happy_mmm noloop
    chw "As agreed, gorgeous."
    scene sm1cs-cw004-33 mc-know-not-what-say-cw-nervous-mc-cough_c1 with dissolve
    cw "..."
    play voice2 mc_pain_cough2 noloop
    mc "*cough*"
    scene sm1cs-cw004-34 chw-ask-mc-want-drink_c1 with dissolve
    play voice5 boy7_hey_short noloop
    chw "Want a drink there, [mcname]?"
    play voice2 mc_happy_yes1 noloop
    scene sm1cs-cw004-35 mc-good-good-mean-yes_c1 with hpunch
    mc "Good god, yes."
    mc "Ahem. I mean. Yes, I'd love one."
    scene sm1cs-cw004-36 chw-laughs-haha_c1 with dissolve
    play voice5 boy7_happy_laugh1 noloop
    chw "Hahaha."
    play sound sfx_heels_steps2 loop
    scene sm1cs-cw004-37 chw-goes-away-for-beers_c1 with dissolve
    pause
    stop sound fadeout 2.0
    scene sm1cs-cw004-38 cw-will-go-get-dressed_c1 with dissolve
    play voice3 girl29_thinking_mmm2 noloop
    cw "I'm going to get dressed."
    scene sm1cs-cw004-39 cw-leans-mc-no-carry-away-dad-smell-weakness_c1 with dissolve
    play voice3 amrose_old_psst2 noloop
    cw "*whispers* Don't get carried away."
    cw "My father manages people. If he smells weakness, he'll latch his teeth into your neck and shake you like a hound dog until you squeal."
    scene sm1cs-cw004-40 cw-dont-let-figure-not-really-together-mc-right-got-this_c1 with dissolve
    cw "Whatever happens, do whatever they ask, but don't let them figure out we're not really together."
    play voice2 mc_yes_ugu1 noloop
    mc "Right. I got this."
    play voice3 girl29_angry_breath noloop
    cw "*sighs*"
    scene sm1cs-cw004-41 cw-fakes-smile-for-parents_c1 with dissolve
    pause
    play sound2 sfx_cloth_rustling3 noloop
    scene sm1cs-cw004-42 cw-kiss-mc_c1 with dissolve
    play voice2 mc_angry_errr5 noloop
    play voice3 girl29_pain_mmh noloop
    play sound dahlia_kiss_french1
    cw "Mmmm!"
    scene sm1cs-cw004-43 cw-smiles-mc-see-soon-handsome_c1 with dissolve
    play voice3 girl29_surprised_ah noloop
    cw "See you soon, handsome."
    play sound sfx_heels_steps1 loop
    scene sm1cs-cw004-44 cw-walks-away-towards-rooms_c1 with dissolve
    pause
    scene sm1cs-cw004-45 fw-looks-mc-go-start-lunch_c1 with dissolve
    play voice4 girl9_yes_aga noloop
    fw "I'll start taking care of lunch."
    play sound2 sfx_heels_steps2
    scene sm1cs-cw004-46 fw-exits-scene-chw-returns-beer_c1 with dissolve
    pause
    play sound sfx_beer_open1
    stop sound2 fadeout 1.0
    scene sm1cs-cw004-47 chw-hands-mc-beer-looks-like-just-two-partner_c1 with dissolve
    play voice5 boy7_happy_laugh2 noloop
    chw "Looks like it's just you and me for a bit, partner."
    scene sm1cs-cw004-49 chw-raises-beer-cheers-to-great-women_c1 with dissolve
    play voice5 boy7_happy_yeah noloop
    chw "Cheers, to the great women in our life."
    play voice2 mc_happy_yay1 noloop
    mc "Cheers."
    play sound [sfx_drink_gulp, sfx_drink_gulp]
    play sound2 sfx_drink_loop1 volume 3.0
    scene sm1cs-cw004-50 mc-chw-drink-beer_c1 with dissolve
    pause
    stop sound2 fadeout 1.0
    jump sm1cs_cw004_later
label sm1cs_cw004_later:
    $ renpy.music.set_volume(0.0, 1.0, "sound3" )
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene black
    show screen scene_transistion(_("Two drinks later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 1.5, "sound3" )
    $ renpy.music.set_volume(1.0, 1.5, "sound4" )
    scene sm1cs-cw004-51 hours-later-open-see-mc-leaning-deck-mct-man-that-great-view_c1
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_thinking_hm noloop
    mct "Man, that is a great view."
    scene sm1cs-cw004-52 mc-takes-sip-beer-mct-maybe-wrong-business-investment-manager-working_c1 with dissolve
    play sound sfx_drink_gulp
    mct "Maybe I'm in the wrong business."
    mct "Being an investment manager seems to be working great for Charles."
    scene sm1cs-cw004-53 mct-not-many-porn-people-with-yachts_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "I don't know many people in charge of porn companies with yachts."
    play sound sfx_heels_steps2
    scene sm1cs-cw004-54 mc-looks-around-mct-where-everyone-claire-dad-went-get-something_c1 with dissolve
    mct "Where is everyone?"
    mct "Claire's dad brought me my second beer, and then he said he had to get something."
    scene sm1cs-cw004-55 mc-dread-mct-what-if-rich-twisted-people-kill-for-virgin-blood_c1 with dissolve
    play voice2 mc_surprised_huh3 noloop
    mct "What if this is one of those twisted rich people murder rituals my friend Seth warned me about in high school?"
    mct "They're going to kill me for my virgin blood and sacrifice me to an alien god so that their investments pay out this year."
    play sound sfx_heels_steps2 loop
    scene sm1cs-cw004-56 mct-wait-minute-not-virgin_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mct "Wait a minute.{w} I'm not a virgin."
    play sound sfx_cloth_rustling4
    scene sm1cs-cw004-57 mc-looks-beer-mct-six-percent-abv_c1 with dissolve
    mct "Six percent ABV. No wonder I'm wigging out a little."
    scene sm1cs-cw004-58 mct-no-one-trying-kill-me_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "No one on this boat is trying to kill me."
    play sound2 sfx_heels_steps2
    scene sm1cs-cw004-59 mc-takes-another-drink-chw-comes-background-shotgun_c1 with dissolve
    play sound sfx_drink_gulp
    pause
    play sound sfx_glass_bottle_bonk
    scene sm1cs-cw004-60 mct-unless-maybe-claire-virgin-have-save-homicidal-parents_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "Unless... maybe Claire is the virgin bride for the ritual."
    mct "I'd have to save her from her homicidal parents."
    scene sm1cs-cw004-61 mc-smiling-mct-and-then-reward-me_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.67
    mct "And then she'd want to reward me."
    scene sm1cs-cw004-62 mc-imagines-cw-on-bed-naked_c1 with dissolve
    play voice2 mc_angry_errr8 noloop
    mct "My boss's boss is a virgin. And I could be her first."
    scene sm1cs-cw004-63 mc-horny-mct-man-that-wouldbe_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Oh man, that would be-"
    play sound2 sfx_shotgun_cocking1 noloop
    scene sm1cs-cw004-64 mc-hears-gun-cocking-freaks-out-oh-shit-fuck_c1 with dissolve
    play voice2 mc_surprised_huh4 noloop
    "*gun cocking*"
    play voice2 mc_angry_fuck1 noloop
    mc "Oh shit. Fuck."
    scene sm1cs-cw004-65 mc-looks-chw-hah-mr-watts_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Hah! Mr. Watts!"
    scene sm1cs-cw004-66 chw-looking-menacing-its-time-come-with-me_c1 with dissolve
    play voice5 boy7_disappointed_groan noloop
    chw "It's time. Come with me, [mcname]."
    scene sm1cs-cw004-67 mc-gulping-expression_c1 with dissolve
    play voice2 sfx_drink_gulp noloop
    pause
    $ renpy.music.set_volume(1.0, 6.0, "music2" )
    $ renpy.music.set_volume(0.0, 10.0, "music" )
    play sound sfx_heels_steps2
    scene sm1cs-cw004-68 mc-now-confused-different-location_c1 with fade
    stop sound fadeout 2.0
    pause
    scene sm1cs-cw004-69 chw-aims-shotgun_c1 with dissolve
    play voice5 boy7_disappointed_mff noloop
    chw "Pull!"
    play sound sfx_shotgun_skeet1
    "*launching noise*"
    play sound sfx_shotgun_shot1
    scene sm1cs-cw004-70 chw-fires-shotgun_c1 with dissolve
    "POW!"
    play sound sfx_shotgun_aimbreak1
    play sound2 sfx_water_splash2 noloop
    scene sm1cs-cw004-71 skeet-disc-explodes-in-sky_c1 with dissolve
    "KOW!"
    scene sm1cs-cw004-72 mc-drinking-beer-nervous-lookingchw-mct-so-dead_c1 with dissolve
    play sound sfx_drink_gulp
    play voice2 mc_pain_mff2 noloop
    mct "I am so dead."
    play sound sfx_shotgun_cocking2
    play sound2 sfx_shotgun_bulletfall1 noloop
    scene sm1cs-cw004-73 chw-laughing-that-sure-something-you-looked-like-pissing_c1 with dissolve
    play voice5 boy7_happy_laugh3 noloop
    chw "*laughing* That sure was something."
    chw "You looked like you were going to piss your pants when you saw me holding this beauty."
    scene sm1cs-cw004-74 mc-yeah-really-got-me-mr-watts-chw-charles-pls_c1 with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Yeah. You really got me, Mr. Watts."
    play voice5 boy7_happy_laugh5 noloop
    chw "Haha. Charles please, [mcname]."
    scene sm1cs-cw004-75 chw-imagine-cw-forgot-mention-mc-guess-slipped-her-mind_c1 with dissolve
    play voice5 boy7_thinking_hmm1 noloop
    chw "I imagine Claire forgot to mention I love skeet shooting when we do these trips."
    play voice2 mc_yes_yes2 noloop
    mc "I guess it slipped her mind."
    play voice5 boy7_happy_laugh6 noloop
    chw "*chuckling* My Claire? Never. Smart as a tack, and twice as sharp."
    scene sm1cs-cw004-76 chw-or-just-wanted-didnt-chief-either-way-sharp-mind_c1 with dissolve
    chw "I'm sure she wanted to see that look on your face. Heh heh."
    chw "Or just wanted to be sure you didn't chicken out."
    chw "Either way, sharp mind, right?"
    scene sm1cs-cw004-77 mc-agrees-mhm_c1 with dissolve
    play voice2 d9s2_ugu noloop volume 2.2
    mc "Mmhmmm."
    play sound sfx_shotgun_reload1
    scene sm1cs-cw004-78 chw-reloads-shotgun_c1 with dissolve
    "Click"
    play sound sfx_shotgun_cocking2
    scene sm1cs-cw004-79 chw-hands-mc-shotgun-your-turn_c1 with dissolve
    play voice5 boy7_yes_yep noloop
    chw "Your shot."
    scene sm1cs-cw004-80 mc-choice-menu-screen_c1 with dissolve
    menu:
        "I don't want to waste your ammo"(hint="sm1cs_cw004_m03_h01"):
            scene sm1cs-cw004-81 choice-not-waste-ammo-mc-dont-want-waste-ammo-charles_c1 with dissolve
            play voice2 mc_no_nah1 noloop
            mc "I don't want to waste your ammo, Charles."
            play sound sfx_cloth_rustling2
            scene sm1cs-cw004-82 chw-do-fine-kid-besides-loads-more_c1 with dissolve
            play voice5 boy7_hey_sexy noloop
            chw "You'll do fine kid."
            chw "Besides, I got loads more where that came from."
        "Sure lets do it"(hint="sm1cs_cw004_m03_h02"):
            call sm1cs_cw004_m03_c02 from _call_sm1cs_cw004_m03_c02
            scene sm1cs-cw004-83 choice-mc-sure-mc-sure-should-be-fun_c1 with dissolve
            play voice2 mc_yes_yeah2 noloop
            mc "Sure, let's do it."
            mc "Should be fun."
            play sound sfx_cloth_rustling2
            scene sm1cs-cw004-84 chw-thats-spirit_c1 with dissolve
            play voice5 boy7_arrogant_hmm2 noloop
            chw "That's the spirit."
    scene sm1cs-cw004-85 chw-just-say-pull-make-sure-you-ready_c1 with dissolve
    play voice5 boy7_yes_aga3 noloop
    chw "Just say \"pull\" when you're ready."
    chw "Make sure you are ready, cause they're fast buggers."
    play sound sfx_shotgun_cocking1
    scene sm1cs-cw004-86 mc-aims-pull-disk-flies-out_c1 with dissolve
    pause
    play sound2 sfx_shotgun_skeet1 noloop
    play voice2 mc_yes_yeah1 noloop
    mc "Pull."
    play sound sfx_shotgun_shot2
    queue sound2 sfx_water_splash2 noloop
    scene sm1cs-cw004-87 mc-shoots-misses-disk_c1 with vpunch
    pause
    scene sm1cs-cw004-88 mc-damn-chw-almost-got-it_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Damn."
    play voice3 boy7_disgust_ooh noloop
    chw "Almost got it."
    scene sm1cs-cw004-89 mc-how-can-tell-chw-good-sense-years-shooting_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "How can you tell?"
    play voice5 boy7_arrogant_hmm1 noloop
    chw "I got a good sense after years of shooting."
    scene sm1cs-cw004-90 chw-lets-go-again_c1 with dissolve
    play voice5 boy7_disappointed_aah noloop
    chw "Let's go again."
    play sound sfx_barefoot_steps1 loop
    scene sm1cs-cw004-91 girls-approach-mc-chw-behind_c1 with dissolve
    pause
    scene sm1cs-cw004-92 fw-haha-look-boys-things-never-change_c1 with dissolve
    play voice4 girl9_happy_laugh1 noloop
    fw "Haha. Look at our boys and their guns."
    fw "Some things never change."
    scene sm1cs-cw004-93 cw-how-he-chw-just-about-go-second-shot_c1 with dissolve
    play voice3 girl29_arrogant_huh noloop
    cw "How is he, daddy?"
    play voice5 boy7_thinking_oh noloop
    chw "Just about to go for his second shot."
    stop sound fadeout 1.0
    scene sm1cs-cw004-94 mc-eyes-cw-look-great_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "You look great."
    scene sm1cs-cw004-a95 cw-smiles-looks-away-glambot-000_i with dissolve
    pause
    play sound ["<silence 0.5>", sfx_camera_fly1] volume 2.0
    scene sm1cs-cw004-a95-glambot
    pause
    play voice3 girl29_happy_laugh1 noloop
    cw "*giggles* Little old me?"
    play voice2 d9s2_mcyes noloop volume 2.8
    mc "Yes."
    play sound sfx_barefoot_steps1 loop
    scene sm1cs-cw004-97 cw-approach-mc-thanks-hun_c1 with dissolve
    play voice5 girl29_thinking_hmm3 noloop
    cw "Thanks, honey."
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-cw004-98 cw-kisses-mc-lips_c1 with dissolve
    play sound mc_kiss2
    pause
    scene sm1cs-cw004-99 cw-whispers-everything-alright-mc-yeah-easier-before-know-dad-likes-guns_c1 with dissolve
    play voice3 girl29_arrogant_pff noloop
    cw "*whispers* Is everything alright?"
    play voice2 mc_yes_yeah4 noloop
    mc "*whispers* Yeah. Was easier before I knew your dad likes guns."
    scene sm1cs-cw004-100 cw-sorry-stay-strong-mc-thanks-claire_c1 with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "*whispers* Sorry. Just... stay strong. You got this."
    play voice2 mc_yes_yeah9 noloop
    mc "*whispers* Thanks, Claire."
    scene sm1cs-cw004-101 cw-turns-head-notices-fw-watching-her_c1 with dissolve
    pause
    scene sm1cs-cw004-102 cw-kisses-mc-deeper-mmm_c1 with dissolve
    play voice3 girl29_thinking_hmm2 noloop
    play sound dahlia_kiss_french1
    cw "Mmmm."
    scene sm1cs-cw004-103 fw-hehe-look-two-blushing-tells-story-first-time-father_c1 with dissolve
    play voice4 girl9_happy_laugh2 noloop
    fw "Hehe. Look at you two. Blushing."
    fw "The first time your father and I were in just swimsuits, we couldn't keep our hands from one another."
    scene sm1cs-cw004-104 fw-looks-chw-explains-first-time-only-swimsuits_c1 with dissolve
    play voice4 girl9_happy_laugh3 noloop
    fw "We found pieces of my two-piece scattered across the deck. *giggles*."
    play sound sfx_shotgun_bulletfall2
    play sound2 sfx_shotgun_reload1 noloop
    scene sm1cs-cw004-105 mc-gulp-cw-have-lil-more-self-control_c1 with dissolve
    "KLANK."
    play voice2 sfx_drink_gulp noloop
    mc "*gulp*"
    play voice3 girl29_yes_yeah noloop
    cw "I guess we have a little more self-control then you two did."
    scene sm1cs-cw004-106 mc-chw-self-control-very-important-second-shot-mc_c1 with dissolve
    play voice5 boy7_yes_aga1 noloop
    chw "Mmhmm. Self-control {b}is{/b} very important."
    chw "Your second shot, [mcname]."
    play sound sfx_shotgun_cocking1
    scene sm1cs-cw004-107 mc-aims-again-pull_c1 with dissolve
    play voice2 mc_yes_okay3 noloop volume 1.6
    mc "Pull."
    play sound2 sfx_shotgun_skeet1 noloop
    "FWAP."
    play sound sfx_shotgun_shot3
    scene sm1cs-cw004-108 mc-tracks-fires-cw-fw-chw-excited_c1 with hpunch
    "BANG!!!"
    play sound sfx_shotgun_aimbreak1
    play sound2 sfx_water_splash2 noloop
    scene sm1cs-cw004-109 mc-shooting-skeet-down-exploding_c1 with dissolve
    "POW."
    scene sm1cs-cw004-110 guys-cheer-mc-fw-nice-shot-cw-well-done-mr_c1 with dissolve
    play voice4 girl9_happy_woohoo noloop
    fw "Nice shot."
    play voice3 girl29_surprised_ohmy noloop
    cw "Well done, Mister Yo-"
    scene sm1cs-cw004-111 cw-mean-great-shot-mc_c1 with dissolve
    play voice3 girl29_pain_cough1 noloop
    cw "I mean."
    cw "{b}You{/b} are such a great shot, [mcname]."
    scene sm1cs-cw004-112 fw-notices-slip-up-cw-nervous_c1 with dissolve
    cw "..."
    scene sm1cs-cw004-113 fw-well-if-two-done-lunch-ready_c1 with dissolve
    play voice4 girl9_happy_mmm1 noloop
    fw "Well if you two are done with your toys, lunch is ready."
    stop sound4 fadeout 2.0
    stop sound3 fadeout 2.0
    jump sm1cs_cw004_first_evening
label sm1cs_cw004_first_evening:
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    scene black
    show screen scene_transistion(_("Later that evening"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.7, 3.0, "music" )
    play sound4 sfx_shower_ambience1 fadein 1.0
    play sound3 sfx_cloth_wiping1 volume 2.0
    scene sm1cs-cw004-114 mc-taking-shower_c1
    with Fade(0.5, 0.5, 0.5)
    play music love_gospel_intro
    play voice2 d1s5_orgasm noloop
    mct "What a day..."
    mct "So glad to have a little time on my own."
    scene sm1cs-cw004-115 mct-learn-say-no-claire-cant-imagine-what-happen-when-break-up_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "I should really start to learn how to say no to Claire."
    mct "I can't imagine what will happen when we \"break up\"."
    play sound sfx_shower_off1
    stop sound4 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-cw004-116 mct-nervous-dad-would-shoot-over-breakup-right_c1 with dissolve
    queue sound4 sfx_ship_inside2 fadein 2.0
    play voice2 mc_angry_huh1 noloop
    mct "Her dad wouldn't shoot me over that..."
    mct "Would he?"
    play sound2 sfx_barefoot_steps1
    play sound sfx_skirt_off2
    scene sm1cs-cw004-117 mc-wrapping-towel-around-mct-alright-not-let-guard-down_c1 with dissolve
    mct "Alright, just got to focus, and make sure not to let my guard down."
    play voice2 mc_scared_huh1 noloop
    queue music love_gospel
    stop sound2 fadeout 1.0
    scene sm1cs-cw004-118 surprised-sees-fw_c1 with hpunch
    mc "Oh, Mrs. Watts."
    play sound sfx_cloth_rustling4
    scene sm1cs-cw004-119 fw-sitting-bed-swimsuit-mc-oh-mrs-watts-fw-farrah-pls_c1 with dissolve
    play voice4 girl9_hey_happy1 noloop
    fw "Farrah please, [mcname]."
    scene sm1cs-cw004-120 fw-no-need-be-so-formal_c1 with dissolve
    play voice4 girl9_thinking_hmm2 noloop
    fw "No need to be so formal..."
    play sound sfx_cloth_rustling5
    scene sm1cs-cw004-121 fw-thirsty-look-daughter-lucky-mc-yes-she-is_c1 with dissolve
    play voice4 girl9_happy_mmm2 noloop
    fw "My daughter is so lucky to have such a handsome, young boyfriend."
    scene sm1cs-cw004-122 mc-also-lucky-mct-cw-his-boss-why-thinking_c1 with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Uh, yes she is."
    mc "And I feel very lucky to be with her."
    mct "Claire is my boss' boss."
    mct "Why am I thinking about that?"
    scene sm1cs-cw004-123 mct-oh-yeah-boss-boss-mom-standing-close-me_c1 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Oh yeah, because this is my boss' boss' mother."
    mct "Standing this close to me.{w} Wearing that.{w} Looking like that."
    play voice2 mc_pain_mff3 noloop
    scene sm1cs-cw004-124 mct-so-fucked-fw-you-nervous_c1 with hpunch
    mct "I'm so fucked."
    play voice4 girl9_thinking_hmm4 noloop
    fw "You seem nervous."
    scene sm1cs-cw004-125 mc-no-just-little-husband-loves-guns_c1 with dissolve
    play voice2 mc_no_nono1 noloop
    mc "No no. Just a little."
    mc "Your husband really enjoys his guns."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw004-126 fw-dont-want-talk-husband-not-thrill-anymore_c1 with dissolve
    play voice4 girl9_no_uhuh noloop
    fw "I don't want to talk about my husband."
    fw "He doesn't thrill me anymore."
    scene sm1cs-cw004-127 fw-still-love-charles-attention-not-land-even-after-puppies_c1 with dissolve
    play voice4 girl9_disappointed_eeh noloop
    fw "I mean, I still love Charles. But his attention doesn't land on me as often as it used to."
    fw "This... even after I got these puppies."
    scene sm1cs-cw004-128 fw-would-not-do-that-what-mct-kind-man-leaves_c1 with dissolve
    play voice4 girl9_sex_closedmoan2 noloop
    fw "You would not do that to me, would you, [mcname]?"
    play voice2 mc_thinking_mmm6 noloop
    mc "What kind of man leaves his woman unattended?"
    scene sm1cs-cw004-129 fw-untouched-mct-conundrum_c1 with dissolve
    play voice4 girl9_sex_closedmoan3 noloop
    fw "Untouched..."
    play voice2 mc_disappointed_ehh3 noloop
    mc "It's a conundrum."
    scene sm1cs-cw004-130 fw-you-touch-them_c1 with dissolve
    play voice4 girl9_disappointed_mmm noloop
    fw "You can feel them...{w} If you'd like."
    scene sm1cs-cw004-131 mc-choice-menu-screen_c1 with dissolve
    menu:
        "Touch her boobs"(hint="sm1cs_cw004_m04_h01"):
            call sm1cs_cw004_m04_c01 from _call_sm1cs_cw004_m04_c01
            play sound sfx_cloth_rustling2
            scene sm1cs-cw004-132 choice-touch-boobs-mc-reaches-mean-if-you-want_c1 with dissolve
            play voice2 mc_thinking_mmm7 noloop
            mc "I mean... if you want it."
        "Resist!"(hint="sm1cs_cw004_m04_h02"):
            scene sm1cs-cw004-133 choice-resist-mc-whispers-dont-think-good-idea_c1 with dissolve
            play voice2 mc_no_no5 noloop
            mc "*whispers* I don't think that's a good idea."
    play sound sfx_door_closed1
    scene sm1cs-cw004-134 cw-walks-in-on-mc-fw_c1 with hpunch
    pause
    scene sm1cs-cw004-135 cw-i-silent-surprised_c1 with dissolve
    play voice3 girl29_pain_ah noloop
    cw "I-"
    scene sm1cs-cw004-136 cw-you-gotta-kidding_c1 with dissolve
    play voice3 girl29_angry_argh1 noloop
    cw "You have got to be kidding me!"
    play voice2 mc_surprised_huh2 noloop
    if player.get_choice("sm1cs_cw004_touch_boobs"):
        scene sm1cs-cw004-138 mc-hand-about-grab-boob_c1 with dissolve
    else:
        scene sm1cs-cw004-137 mc-surprised-fw-looks-back-at-cw_c1 with dissolve
    pause
    scene sm1cs-cw004-139 mc-snaps-mct-oh-shit_c1 with dissolve
    play voice2 mc_pain_mff4 noloop
    mct "Oh shit! Did Claire notice I was about to touch her mom?!"
    scene sm1cs-cw004-140 fw-oh-honey-cw-cant-believe-sticking-boobs-young-man_c1 with dissolve
    play voice4 girl9_disappointed_oh noloop
    fw "Oh honey... I was just checking in on [mcname]."
    play voice3 girl29_angry_argh2 noloop
    play sound sfx_throw_something1
    scene sm1cs-cw004-141 cw-and-with-my-boyfriend-means-really_c1 with hpunch
    cw "I cannot believe you were sticking your boobs out to a man half your age."
    cw "And... You know... {w}He is my boyfriend on top of that!"
    cw "I mean, really?"
    scene sm1cs-cw004-142 fw-found-mc-alone-keep-company-cw-nuh-huh_c1 with dissolve
    play voice4 girl9_angry_mmm noloop
    fw "Mmm. Well, when I found him here alone, I figured you wanted me to keep him entertained."
    scene sm1cs-cw004-143 cw-come-out-lets-go-out-fw-so-forceful_c1 with dissolve
    play voice3 girl29_no_uhuh noloop
    cw "Nuh-uh!"
    cw "Come out. Out of here. Let's go."
    play sound sfx_barefoot_steps1 loop volume 1.5
    scene sm1cs-cw004-144 cw-pushes-fw-out-of-room-fw-merely-want-second-opinion-cw-talk-later_c1 with dissolve
    play voice4 girl9_disappointed_oof noloop
    fw "So forceful."
    fw "I merely wanted to get a second opinion on something."
    play voice3 girl29_yes_aga1 noloop
    cw "We will talk about this later."
    play sound sfx_door_openclosed1
    scene sm1cs-cw004-145 cw-closes-door-after-fw-turns-mc-what-have-say-mc-was-totally-innocent_c1 with dissolve
    play voice3 girl29_angry_dough noloop
    cw "And what do {i}you{/i} have to say for yourself?"
    play voice2 d2s12_emmm noloop volume 1.6
    mc "It was totally innocent. And nothing happened."
    play sound sfx_barefoot_steps1
    scene sm1cs-cw004-146 cw-walks-towards-mc-half-how-could-situation-mc-not-here-if-you-not-pull-me_c1 with dissolve
    play voice3 girl29_angry_oof noloop
    cw "But how could you let yourself be in a situation like that?"
    play voice2 mc_hey_hey1 noloop
    mc "I wouldn't be here if you didn't pull me into this."
    stop sound fadeout 1.0
    scene sm1cs-cw004-147 cw-yest-enjoyed-self_c1 with dissolve
    play voice3 girl29_angry_hmf noloop
    cw "And yet, you seemed to be enjoying yourself."
    scene sm1cs-cw004-148 cw-point-erection-doesnt-look-minded-much-mc-that-just_c1 with dissolve
    cw "Doesn't look like you minded that too much."
    play voice2 mc_angry_off noloop
    mc "I mean, that's just."
    play sound sfx_cloth_rustling1
    scene sm1cs-cw004-149 mc-hides-erection-hands-silent-cw-bettter-be-me-mean-outfit_c1 with dissolve
    mc "Totally unrelated physical reaction."
    play voice3 girl29_angry_hm noloop
    cw "Whatever {i}that{/i} is... It had better be because of {b}me{/b}."
    cw "*short breath* I mean...{w} because of {i}my{/i} outfit."
    scene sm1cs-cw004-150 mc-that-feel-trap-cw-not-trap-well_c1 with dissolve
    play voice2 d3s7_mcemm noloop volume 1.7
    mc "I feel like that's a trap."
    play voice3 girl29_no_active noloop
    cw "I'm not trying to trap you.{w} But..."
    scene sm1cs-cw004-151 cw-looks-back-maybe-mom-trying-one-sure-happy-couple_c1 with dissolve
    play voice3 girl29_arrogant_yeah noloop
    cw "*whispers* Maybe my mom is trying to get both of us..."
    cw "*whispers* Making sure we are a {i}happy{/i} couple..."
    scene sm1cs-cw004-152 cw-looks-back-mc-hmm_c1 with dissolve
    play voice3 girl29_thinking_hmm5 noloop
    cw "Hmmm."
    play sound sfx_cloth_wiping1 loop volume 2.5
    scene sm1cs-cw004-153 cw-puts-hands-towel-mc-claire-cw-fine-just-trust-me_c1 with dissolve
    play voice2 d1s5b_emmm noloop volume 1.6
    mc "Claire?"
    play voice3 girl29_thinking_hmm1 noloop
    cw "It's fine. Just...{w} trust me."
    scene sm1cs-cw004-154 mc-slow-breath-uh-okay_c1 with dissolve
    play voisex2 mc_sex_openmoans1
    mc "*slow breath* Uh... okay."
    scene sm1cs-cw004-155 cw-whispers-just-show-mom-see-through-lies_c1 with dissolve
    play voice3 girl29_angry_breath noloop
    cw "*whispers* This is just for show, [mcname]."
    cw "*whispers* I didn't hear her leave.{w} Or... I'm not sure I did."
    cw "*whispers* So just play along."
    scene sm1cs-cw004-156 mc-ask-lies-cw-sure-ask-later-take-care-you_c1 with dissolve
    mc "*whispers* Sure... makes sense."
    scene sm1cs-cw004-157 cw-if-say-word-anyone-fired-mc-you-sure_c1 with dissolve
    play voice3 girl29_angry_ehh noloop
    cw "*whispers* If you ever breathe a word of this to anyone...{w} being fired will be the least of your worries."
    mc "*whispers* Are you sure?"
    stop voisex2 fadeout 1.0
    stop sound fadeout 1.0
    scene sm1cs-cw004-158 cw-just-drop-towel_c1 with dissolve
    play voice3 girl24_angry_breath noloop
    cw "*short breaths* Just drop the towel."
    play sound sfx_skirt_off2
    scene sm1cs-cw004-159 mc-takes-towel-off_c1 with dissolve
    pause
    play sound sfx_cloth_planket2 volume 1.6
    scene sm1cs-cw004-160 cw-surprised-looking-dick-well-cant-blame-mom_c1 with dissolve
    play voice3 girl24_sex_closedmoan5 noloop
    cw "*whispers* I... Well, obviously, you can't really blame my mom for her momentary lust."
    scene sm1cs-cw004-161 cw-but-make-sure-not-be-cornered-mct-she-cornering-me-now_c1 with dissolve
    play voice3 girl29_hey_angry noloop
    cw "But you are going to make sure that you don't allow yourself to be cornered like a rabbit for the rest of the trip."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw004-162 mct-best-keep-myself-mc-yes_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mct "She says that but isn't she kind of cornering me right now?"
    mct "Probably best to keep that to myself."
    scene sm1cs-cw004-163 cw-good-answer_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes..."
    play voice3 girl29_yes_aga2 noloop
    cw "Good answer."
    play sound sfx_cloth_rustling1
    scene sm1cs-cw004-164 cw-mmm-mc-impressed_c1 with dissolve
    play voisex3 girl24_sex_closedmoan4 noloop
    cw "Mmmm."
    play voice2 mc_thinking_hmm3 noloop
    mc "Impressed?"
    scene sm1cs-cw004-165 cw-only-with-stupidity_c1 with dissolve
    play voice3 girl29_disappointed_mff noloop
    cw "*whispers* Only with your stupidity. *very quiet moan*"
    play voisex3 girl24_sex_openmoans3
    play sound sfx_handjob_cream1 loop volume 2.0
    scene sm1cs-cw004-166 cw-loud-so-big-cant-wait-make-cum_c1 with dissolve
    cw "*loudly* Oh, it's so big."
    cw "*loudly* I can't wait to make you cum."
    scene sm1cs-cw004-a167-1 with dissolve
    play voisex2 mc_sex_openmoans1
    cw "*softer* I can't believe I'm doing this."
    mc "*whispers* Me neither."
    pause
    scene sm1cs-cw004-a167-2 with dissolve
    cw "*whispers* I insist that you release quickly, [mcname]."
    mc "*grunting*"
    pause
    scene sm1cs-cw004-a167-3 with dissolve
    cw "What did I just say?"
    mc "I'm sorry. It just feels really good."
    mc "*whispers* And... hu-gahh... I think your parents already assume we have sex."
    cw "..."
    pause
    scene sm1cs-cw004-a167-4 with dissolve
    cw "*whispers* Be that as it may. Your only job right now is to forget everything else and cum."
    cw "*whispers* I don't want to sleep and think about your..."
    pause
    scene sm1cs-cw004-a167-1-f with dissolve
    cw "*whispers* Weakness."
    mc "*whispers* Well, I think it looks pretty strong."
    pause
    scene sm1cs-cw004-a167-2-f with dissolve
    cw "Hmmph."
    cw "*whispers*Stop resisting."
    pause
    scene sm1cs-cw004-a167-3-f with dissolve
    mc "*strained* I'm not."
    cw "*angry* [mcname]."
    pause
    scene sm1cs-cw004-a167-4-f with dissolve
    mc "*whispers* I swear, I'm not putting on a show, Claire."
    cw "*growling* That's Ms. Watts right now..."
    scene sm1cs-cw004-173 cw-growling-what-problem_c1 with dissolve
    play voisex3 girl29_angry_hmf noloop
    cw "*low growling* What is the problem?"
    play sound sfx_rope_stretch
    scene sm1cs-cw004-174 cw-pulls-mc-huh-cw-why-not-cumming_c1 with dissolve
    play voisex2 mc_arrogant_huh2 noloop
    mc "Huh?"
    play voice3 girl29_angry_argh1 noloop
    scene sm1cs-cw004-174 cw-pulls-mc-huh-cw-why-not-cumming_c1 with hpunch
    cw "*whispers* Why.{w} Aren't.{w} You.{w} Cumming?"
    play sound sfx_hair_scratch1
    scene sm1cs-cw004-175 cw-this-supposed-quick-fix-precise-system_c1 with dissolve
    play voice3 girl29_disgust_ergh noloop
    cw "*whispers* This was supposed to be quick and dirty."
    cw "*whispers* A precise system fix."
    scene sm1cs-cw004-176 mc-guess-stress-very-little-romance-air_c1 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "*whispers* I mean... I guess it's just the stress... you know{w} the situation."
    mc "*whispers* There is very little romance in the air."
    scene sm1cs-cw004-177 cw-annoyed-silent-what-suggest_c1 with dissolve
    cw "*whispers*..."
    play voice3 girl29_angry_kgh noloop
    cw "*whispers* You had better have a suggestion."
    scene sm1cs-cw004-178 mc-uh-maybe_c1 with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "Uh..."
    mc "Maybe..."
    scene sm1cs-cw004-179 mct-this-going-blow-in-face-so-sexy-might-go-for-it_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mct "This is going to blow up in my face, but I gotta do it."
    mct "She's so sexy, and she's already jacking me off."
    mct "She might go for it."
    scene sm1cs-cw004-180 cw-looking-hell-no-silencemaybe-could-use-mouth-mc-ms-watts_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Maybe you could use your mouth?{w} I'm sure that will help me cum..."
    mc "*whispers* Ms. Watts..."
    scene sm1cs-cw004-181 cw-looking-hell-no-silence_c1 with dissolve
    pause
    scene sm1cs-cw004-182 cw-better-cum-quick-mc-yes-ms-watts_c1 with dissolve
    play voice3 girl29_disgust_meh noloop
    cw "*whispers* You had better cum quickly."
    play voice2 d9s2_mcyes2 noloop volume 3.0
    mc "*whispers* Yes, Ms. Watts."
    scene sm1cs-cw004-183 cw-gets-lil-horny-get-on-bed_c1 with dissolve
    play voice3 girl29_thinking_hm noloop
    cw "Get... Get on the bed."
    play sound sfx_cloth_planket3
    scene sm1cs-cw004-184 fade-next-position_c1 with dissolve
    pause
    scene sm1cs-cw004-185 cw-licks-mc-dick_c1 with dissolve
    play voisex3 girl24_sex_sucking1
    pause
    scene sm1cs-cw004-186 cw-takes-mc-dick-in-mouth_c1 with dissolve
    play voisex3 girl24_sex_sucking2
    cw "*soft panting*"
    scene sm1cs-cw004-a187-1 cw-bj-anim-01 with dissolve
    pause
    scene sm1cs-cw004-a187-1
    play voisex2 mc_sex_openmoans2
    mc "*soft grunting*"
    mct "No way. Claire is doing it."
    pause
    scene sm1cs-cw004-a187-2 with dissolve
    mct "She's sucking my cock. And we haven't even kissed."
    mct "Well, I guess we have technically kissed, but it was always for show."
    mct "This isn't for show."
    pause
    scene sm1cs-cw004-a187-3 with dissolve
    mct "It's just the two of us. Alone in this cabin."
    mct "She's fucking milking my balls dry."
    pause
    scene sm1cs-cw004-a187-4 with dissolve
    mct "It feels so fucking good."
    mct "Way better than her handjob."
    pause
    play voisex3 lissa_sucking_deep
    scene sm1cs-cw004-a187-1-f with dissolve
    pause
    scene sm1cs-cw004-a187-2-f with dissolve
    pause
    scene sm1cs-cw004-a187-3-f with dissolve
    pause
    scene sm1cs-cw004-a187-4-f with dissolve
    pause
    scene sm1cs-cw004-192 cw-takes-cock-out-mouth-grins_c1 with dissolve
    play voisex3 girl29_disgust_boeagh2 noloop
    cw "Puwah."
    play voisex2 mc_pain_argh1 noloop
    play sound mc_cum_sound1 volume 2.0
    scene sm1cs-cw004-193 mc-cant-hold-cums-big_c1 with vpunch
    mc "*grunts*"
    play voisex2 mc_sex_orgasm5 noloop
    play sound mc_cum_sound1 volume 2.0
    scene sm1cs-cw004-194 mc-grunts-cums-on-himself_c1 with hpunch
    mc "Grauah..."
    scene sm1cs-cw004-195 cw-licks-lips-hornily_c1 with dissolve
    play voisex3 girl24_sex_closedmoan1 noloop
    pause
    $ renpy.music.set_volume(0.4, 6.0, "music" )
    scene sm1cs-cw004-196 cw-back-business-go-inside-clean-pervert-mc-what_c1 with dissolve
    play voice3 girl29_hey_provocative noloop
    cw "*whispers* Go in the bathroom and get cleaned up.{w} You pervert."
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene sm1cs-cw004-197 cw-did-stutter-mc-no-maam_c1 with dissolve
    play voice3 girl29_surprised_huh1 noloop
    cw "Did I stutter?"
    play voice2 mc_no_no10 noloop
    mc "No ma'am?"
    scene sm1cs-cw004-198 cw-good-clean-get-blanket-mc-why-said-share-bed_c1 with dissolve
    play voice3 girl29_yes_yeah noloop
    cw "Good. So be a good boy and clean up. Then, take a pillow and a blanket from the closet."
    play voice2 mc_surprised_why2 noloop
    mc "Why? You said we would just sleep on the same bed."
    scene sm1cs-cw004-199 cw-changed-mind-going-sleep-ground-mc-what-he-do_c1 with dissolve
    play voice3 girl29_no_nonono noloop
    cw "I've changed my mind.{w} You're going to sleep on the floor like a bad little boy and think about what you've done."
    play voice2 mc_surprised_huh7 noloop
    mc "What did I do?"
    scene sm1cs-cw004-200 cw-quiet-need-beauty-sleep_c1 with dissolve
    play voice3 girl29_arrogant_ha noloop
    cw "Go wash up now, this isn't up for discussion."
    play sound2 sfx_barefoot_steps1
    play sound sfx_cloth_rustling4
    scene sm1cs-cw004-201 mc-goes-towards-bathroom_c1 with dissolve
    pause
    play sound2 sfx_shower_ambience1 volume 0.6
    scene sm1cs-cw004-202 washing-sounds-mc-takes-another-shower_c1 with dissolve
    "*washing sounds*"
    stop sound2 fadeout 1.0
    play sound sfx_shower_off1
    play sound3 sfx_barefoot_steps1
    scene sm1cs-cw004-204 mc-could-be-worse-father-couldve-walked-in_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mct "Could be worse. Her father could have walked in."
    play sound3 sfx_cloth_rustling4 noloop
    scene sm1cs-cw004-205 mc-lies-down-mct-sleep-now-then-just-one-more-day_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "Sleep now. Then it's just one more day of this strange journey."
    scene sm1cs-cw004-206 mct-still-blowjob-helped-push-hill_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Still, that blowjob definitely helped push me over the hill."
    scene sm1cs-cw004-207 mc-closes-eyes-going-have-problem-falls-asleep_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "I'm going to have no problem falling to-"
    scene sm1cs-cw004-208 camera-pull-cw-sleep-mask-on_c1 with dissolve
    play voice2 mc_disappointed_snoring1 noloop
    pause
    scene sm1cs-cw004-209 cw-hmmm-falls-asleep_c1 with dissolve
    play voice3 girl24_sex_closedmoan2 noloop
    cw "Hmm."
    stop voice2 fadeout 1.0
    jump sm1cs_cw004_end_scene
label sm1cs_cw004_reject_cw:
    stop music fadeout 3.0
    stop sound4 fadeout 2.0
    stop sound3 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ player.set_choice("sm1cs-cw004-offramp")
    $ player.set_choice("cw004-selected-offramp")
    $ StoryController.end_scene_in_time(CW_STORY, 23, 59, 0)
    return
label sm1cs_cw004_end_scene:
    stop music fadeout 3.0
    stop sound4 fadeout 2.0
    stop sound3 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    if vn_mode:
        $ player.progress_storyline(CW_STORY, 2)
    $ StoryController.end_scene(CW_STORY)
    return
label sm1cs_cw004_m01_c01:
    $ player.set_choice("sm1cs_cw004_help_cw")
    $ CharacterController.get_character("cw").add_point(2)
    return
label sm1cs_cw004_m02_c02:
    $ player.set_choice("sm1cs_cw004_reassure_cw")
    $ CharacterController.get_character("cw").add_point(2)
    return
label sm1cs_cw004_m03_c02:
    $ player.set_choice("sm1cs_cw004_be_confident")
    return
label sm1cs_cw004_m04_c01:
    $ player.set_choice("sm1cs_cw004_touch_boobs")
    return