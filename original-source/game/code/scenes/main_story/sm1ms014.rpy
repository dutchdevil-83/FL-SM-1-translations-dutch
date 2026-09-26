label sm1ms014:
    $ renpy.music.set_volume(0.5, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    scene sm1ms014-01 sy-excited with dissolve
    play music music_business_b
    play voice3 stacy_happy_wooh1 noloop
    sy "This is pretty exciting!"
    scene sm1ms014-02 mc-talking with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Right? I can't believe we're doing this."
    scene sm1ms014-03 mc-sy-talking with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Which part? The porn studio? Or the renovating?"
    play voice2 mc_arrogant_heh1 noloop
    mc "Both?"
    scene sm1ms014-04 mc-sy-knock-knock with dissolve
    call knock from _call_knock_2
    scene sm1ms014-05 sy-curious with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "Who is it?"
    scene sm1ms014-06 mc-assuming with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Should be some of the stuff we need to start working!"
    sy "Oh, awesome!"
    play sound sfx_door_open1
    scene sm1ms014-07 mc-hey with dissolve
    play voice2 mc_thinking_oh1 noloop
    if persistent.is_special:
        mc "Oh, hey Mom."
        scene sm1ms014-08 sy-ouu with dissolve
        play voice3 stacy_surprised_huh3 noloop
        sy "Wait, it's Mom?"
        scene sm1ms014-09 my-itzme with dissolve
        play voice4 girl34_yes_yeap4 noloop
        my "Yep, it's just your dear, old mother."
    else:
        mc "Oh, hey Melony."
        scene sm1ms014-08 sy-ouu with dissolve
        play voice3 stacy_surprised_huh3 noloop
        sy "Wait, it's Melony?"
        scene sm1ms014-09 my-itzme with dissolve
        play voice4 girl34_yes_yeap4 noloop
        my "Yep, it's just me."
    play sound sfx_heels_steps1 loop
    scene sm1ms014-10 my-asking with dissolve
    play voice4 girl34_thinking_hmm4 noloop
    my "Were you expecting someone else?"
    play sound2 sfx_door_closed1 noloop
    scene sm1ms014-11 mc-talking with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Actually, yeah. We're having some of the stuff dropped off to start working on the studio."
    stop sound fadeout 1.0
    scene sm1ms014-12 my-talking with dissolve
    play voice4 girl34_surprised_oh3 noloop
    my "Oh that's wonderful news! I am so happy to hear that you were taking me seriously!"
    my "Come here!"
    play sound sfx_cloth_rustling3
    scene sm1ms014-14 mc-my-hugging with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Uhm, yeah... I mean, it was something we needed to do."
    mc "But you definitely helped convince us."
    scene sm1ms014-13 mc-my-hugging with dissolve
    play voice4 girl34_happy_great1 noloop
    my "Good... hopefully you'll take some of my other thoughts seriously too."
    scene sm1ms014-15 mc-talking with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "Like going back to school?"
    if persistent.is_special:
        mc "Mom..."
        scene sm1ms014-16 sy-talking with dissolve
        play voice3 stacy_scared_oof1 noloop
        sy "How, uhm, rude of me! Mom, would you like anything?"
    else:
        mc "Melony..."
        scene sm1ms014-16 sy-talking with dissolve
        play voice3 stacy_scared_oof1 noloop
        sy "How, erm, inconsiderate of me! Melony, would you like a glass of water or anything?"
    scene sm1ms014-17 my-talking with dissolve
    play voice4 girl34_yes_happy1 noloop
    my "Actually, a glass of water sounds lovely!"
    scene sm1ms014-18 mc-thinking with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Thank God for Stacy."
    play sound sfx_heels_steps1 loop
    scene sm1ms014-19 mc-thinking with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Because I have no idea what it's going to take to convince her that I'm doing the right thing."
    mct "What am I going to do? Because she won't listen to anything other than me going back to school..."
    stop sound fadeout 1.0
    scene sm1ms014-20 sy-yoo with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "Uhm, hello? Earth to [mcname]!"
    scene sm1ms014-21 sy-asking with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "Would you like a glass of water, too?"
    scene sm1ms014-22 mc-nope with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh, uhhh - I'm good."
    play voice3 stacy_yes_ugu1 noloop
    sy "Suit yourself."
    scene sm1ms014-23 my-asking with dissolve
    play voice4 girl34_arrogant_huh3 noloop
    my "Whatcha' thinking about over there?"
    scene sm1ms014-24 mc-answering with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Uhm... just... the renovation stuff. It's going to be a lot of work."
    play voice4 girl34_yes_neutral3 noloop
    my "Yes it is."
    scene sm1ms014-25 sy-talking with dissolve
    play voice3 stacy_no_nah3 noloop
    sy "Come on, this is going to be a piece of cake! Just like when we built that Faraday cage at my old apartment!"
    scene sm1ms014-26 my-surprised with dissolve
    play voice4 girl34_surprised_what1 noloop
    my "You built... what?"
    scene sm1ms014-27 sy-talking with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "A Faraday cage! It's a-"
    scene sm1ms014-28 my-interrupting with dissolve
    play voice4 girl34_angry_ahem4 noloop
    my "I know what a Faraday cage is, Stacy. I'm more concerned about why you thought you needed to build one."
    scene sm1ms014-29 my-overreacting with dissolve
    play voice4 girl34_surprised_huh1 noloop
    if persistent.is_special:
        my "Did my kids turn into weird, doomsday preppers? Have I failed as a mother?"
    else:
        my "Have you two turned into weird, doomsday preppers? Should I be concerned?"
    scene sm1ms014-30 mc-talking with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, it was because of the, uhm...{w} Fetish Locator stuff."
    scene sm1ms014-31 my-talking with dissolve
    play voice4 girl34_disappointed_eeh2 noloop
    my "Ahh... that whole experience sounded... harrowing, to say the least."
    my "But there were very few details about it on the web."
    scene sm1ms014-32 mc-talking with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Thanks to Hana. I didn't... really want people to know I was involved."
    play sound sfx_drink_loop1 volume 3.0 loop
    scene sm1ms014-33 my-talking with dissolve
    play voice4 girl34_yes_questioning1 noloop
    my "I can understand that. No one wants all of their dirty laundry aired out for everyone to see."
    my "It's like the first time one of my nudes was shown."
    play sound sfx_biologic_water_spit1
    scene sm1ms014-34 sy-spitting-water with dissolve
    play voice3 stacy_pain_cough3 noloop
    pause
    scene sm1ms014-35 mc-surprised with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "One of your... whats?"
    scene sm1ms014-36 sy-shocked with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "You have nudes!? And someone leaked them!?!"
    scene sm1ms014-37 my-casually-answering with dissolve
    play voice4 girl34_no_neutral1 noloop
    my "No, it was nothing like that. One of the nude drawings that was done of me."
    scene sm1ms014-38 my-smirking with dissolve
    play voice4 girl34_happy_relief4 noloop
    my "Right after college I was doing some work with this artist. She had the most wonderful way of drawing me."
    my "She had an exhibit. I went to the opening of her show and... it was quite an experience to know that everyone was looking at me, naked as the day I was born."
    my "But, she never drew my face, so no one knew."
    scene sm1ms014-39 my-talking with dissolve
    play voice4 girl34_disappointed_eem1 noloop
    my "But, it was also uncomfortable to know that everyone could see me. Every detail, every flaw..."
    my "So I can understand that it's... difficult right now."
    scene sm1ms014-40 mc-sad with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    if persistent.is_special:
        mc "Thanks, Mom."
        scene sm1ms014-41 sy-in-disbelief with dissolve
        play voice3 stacy_disappointed_oh7 noloop
        sy "I can't believe that someone has nudes of my Mom..."
    else:
        mc "Thanks, Melony."
        scene sm1ms014-41 sy-in-disbelief with dissolve
        play voice3 stacy_disappointed_oh7 noloop
        sy "I can't believe there are nudes of you... somewhere out there, in the world..."
    scene sm1ms014-42 my-oh-please with dissolve
    play voice4 girl34_disappointed_oh2 noloop
    my "Oh please, Stacy. I bet there's some boy out there who has a bunch of nudes of you."
    my "Or girl, whomever you might find yourself attracted to."
    my "I just hope it's not like [mcname] though, just posted on the internet for anyone to see."
    scene sm1ms014-43 mc-sy-exchanging-looks with dissolve
    play voice3 stacy_no_questioning2 noloop
    sy "Uhm, yeah... no internet nudies of me..."
    scene sm1ms014-05 sy-curious with dissolve
    call knock from _call_knock_3
    play voice3 stacy_surprised_oh1 noloop
    sy "That must be the people with the stuff or something! I'll get it!"
    play sound sfx_heels_run2 loop
    scene sm1ms014-44 sy-hurrying-towards-the-door with dissolve
    pause
    stop sound fadeout 2.0
    scene sm1ms014-45 my-talking with dissolve
    play sound2 sfx_door_open1 noloop volume 0.5
    play voice4 mc_arrogant_tsktsk noloop
    my "Aye yea yea..."
    play voice2 mc_arrogant_huh1 noloop
    mc "What?"
    play voice4 girl34_arrogant_ha2 noloop
    if persistent.is_special:
        my "Your sister can't keep a secret to save her life."
    else:
        my "Stacy can't keep a secret to save her life."
    play sound sfx_heels_steps1 loop
    scene sm1ms014-46 my-walking with dissolve
    play voice4 girl34_yes_aga3 noloop
    my "Come on, let's get this renovation started though!"
    scene sm1ms014-47 mc-thinking with dissolve
    play voice2 mc_angry_errr7 noloop
    mct "Oh man... we might be in trouble. How long can Stacy keep it a secret that she was the redhead in the video-"
    stop sound fadeout 1.0
    scene sm1ms014-48 sy-calling with dissolve
    play voice3 stacy_hey_angry1 noloop
    sy "[mcname]!"
    scene sm1ms014-49 mc-coming with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "I'm coming, I'm coming!"
    scene sm1ms014-50 sy-talking with dissolve
    play voice5 boy9_thinking_emm4 noloop
    "Delivery Guy" "Where do you want this stuff?"
    play voice3 stacy_arrogant_huh4 noloop
    sy "Just - wherever!"
    "Delivery Guy" "Okaaaay..."
    call sm1ms014_charge_money from _call_sm1ms014_charge_money
    play sound sfx_metal_fence1 volume 1.5
    scene sm1ms014-51 sy-talking with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "Come on! Let's get all of this stuff inside."
    scene sm1ms014-52 my-talking with dissolve
    play voice4 girl34_happy_laugh3 noloop
    my "The fun had to start eventually, right?"
    $ renpy.music.set_volume(1.0, 1.5, "music" )
    scene sm1ms014-53 mc-my-sy-getting-stuff-in-montage with dissolve
    pause(1.5)
    scene sm1ms014-54 mc-my-sy-getting-stuff-in-montage with dissolve
    pause(1.5)
    scene sm1ms014-55 mc-my-sy-getting-stuff-in-montage with dissolve
    pause(1.5)
    scene sm1ms014-56 mc-my-sy-getting-stuff-in-montage with dissolve
    pause(1.5)
    scene sm1ms014-57 mc-my-sy-getting-stuff-in-montage with dissolve
    pause(1.5)
    scene sm1ms014-58 mc-my-sy-getting-stuff-in-montage with dissolve
    pause(1.5)
    scene sm1ms014-59 mc-my-sy-getting-stuff-in-montage with dissolve
    pause(1.5)
    scene sm1ms014-60 mc-my-sy-getting-stuff-in-montage with dissolve
    pause(1.5)
    scene sm1ms014-61 mc-my-sy-getting-stuff-in-montage with dissolve
    pause(1.5)
    jump sm1ms014_after_montage
label sm1ms014_after_montage:
    $ renpy.music.set_volume(0.5, 2.5, "music" )
    scene sm1ms014-62 mc-talking with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow. We've made some good progress!"
    scene sm1ms014-63 sy-unhappy with dissolve
    play voice3 stacy_disappointed_ehh2 noloop
    sy "Yeah..."
    scene sm1ms014-64 mc-confused with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "What?"
    scene sm1ms014-65 sy-whinning with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "I just thought we'd be done by now."
    scene sm1ms014-66 mc-too-big with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "The studio is really big, Stacy-"
    scene sm1ms014-67 mc-sy-talking with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah, but we finished the Faraday cage in a day!"
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, but your old apartment was way smaller than this one."
    scene sm1ms014-68 my-asking with dissolve
    play voice4 girl34_thinking_emm1 noloop
    my "You never said why you had to build a Faraday cage for Fetish Locator."
    scene sm1ms014-69 mc-uncomfortable with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Oh, uhm..."
    mc "We found out that the app could listen to our conversations whenever it wanted... Stacy came up with the idea to make the cage so we could have some privacy."
    scene sm1ms014-70 my-shocked with dissolve
    play voice4 girl34_disappointed_oh3 noloop
    my "Wow... I didn't realize it was that bad."
    my "I can see why you wouldn't want to stay at your college after that."
    scene sm1ms014-71 mc-trying-to-calm-her with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    if persistent.is_special:
        mc "Mom..."
    else:
        mc "Melony..."
    scene sm1ms014-72 my-irritated with dissolve
    play voice4 girl34_angry_breath1 noloop
    my "[mcname]. I have tried being patient with you, but I am at my wit's end."
    my "I'm happy that you have this place, and that you're... occupied."
    scene sm1ms014-73 my-irritated with dissolve
    play voice4 girl34_hey_angry2 noloop
    my "But you can't throw your future away for this!"
    my "Have you even thought about your future? What about after you get too old to be in porno movies? Or - or if it doesn't pay well enough to afford this place?"
    scene sm1ms014-74 mc-explaining with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "I have, a bit. I am working other jobs right now that help pay the bills."
    scene sm1ms014-75 my-surprised with dissolve
    play voice4 girl34_disappointed_oh1 noloop
    my "Oh..."
    scene sm1ms014-76 mc-explaining with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "But I also haven't thought too much about it - not because I'm not worried, but because I don't want to plan for failure."
    if persistent.is_special:
        mc "I'm giving this my all, Mom. I really want to make something out of this."
    else:
        mc "I'm really giving this my all, Melony. I want to make something of this."
    scene sm1ms014-77 my-curious with dissolve
    play voice4 girl34_yes_ugu1 noloop
    my "Mmhmmm. Well, if you are, then I can ask you how you plan to make these videos."
    play sound sfx_cloth_rustling2
    scene sm1ms014-78 mc-telling-her with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Well, I've hired a camera woman-"
    scene sm1ms014-79 mc-my-talking with dissolve
    play voice4 girl34_surprised_huh7 noloop
    my "You're hiring crew for this?"
    play voice2 mc_yes_yeah4 noloop
    mc "Uhm, yep. St-t - I don't know enough about camera stuff to do it myself, so I found someone who did."
    scene sm1ms014-80 mc-thinking with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Shit - almost slipped up and told her that Stacy is involved!"
    scene sm1ms014-81 my-asking with dissolve
    play voice4 girl34_disappointed_oof2 noloop
    my "Oh. So you got someone from the internet or something?"
    play sound sfx_heels_steps2 loop
    scene sm1ms014-82 mc-walking-towards-couch with dissolve
    play voice2 mc_no_no5 noloop
    mc "Actually, she's a professional photographer in Crowning who's always wanted to do video content."
    play sound2 sfx_heels_steps1
    scene sm1ms014-83 my-curious with dissolve
    play voice4 girl34_surprised_ah1 noloop
    my "Is she the redhead in your video?"
    scene sm1ms014-84 mc-disagreeing with dissolve
    play voice2 mc_no_no10 noloop
    mc "Uhm - no."
    scene sm1ms014-85 my-walking-towards-couch with dissolve
    play voice4 girl34_arrogant_hm1 noloop
    my "Where did you even find her?"
    play sound sfx_cloth_rustling4
    stop sound2 fadeout 2.0
    scene sm1ms014-86 mc-making-it-up with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Erm... she's someone I work - or used to work with."
    queue sound2 sfx_cloth_rustling5 noloop
    scene sm1ms014-87 my-sitting with dissolve
    play voice4 girl34_arrogant_ha3 noloop
    my "Is that where you're finding your... video stars?"
    scene sm1ms014-88 my-mc-talking with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Sometimes. If they're interested in doing adult content, yeah."
    play voice4 girl34_thinking_hmm7 noloop
    my "What are you even doing for work right now?"
    scene sm1ms014-89 mc-explaining with dissolve
    play voice2 mc_arrogant_heh2 noloop
    if player.has_played_scene("sm1fs_i003") and player.has_played_scene("sm1fs_t003"):
        mc "Well one of my jobs is in an IT office, as a coder. And my other job is at a theater, working backstage."
    elif player.has_played_scene("sm1fs_i003"):
        mc "Well I work at an IT office, as a coder."
    elif player.has_played_scene("sm1fs_t003"):
        mc "Well I work at a theater, working backstage."
    mc "I also deliver bratwursts sometimes."
    scene sm1ms014-90 my-surprised with dissolve
    play voice4 girl34_surprised_ohmy2 noloop
    my "I didn't realize you were doing so much."
    scene sm1ms014-91 mc-talking with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Starting a business costs a lot of money."
    scene sm1ms014-92 my-serious with dissolve
    play voice4 girl34_thinking_emm2 noloop
    my "Well where are you filming? Location scouting must be difficult."
    play voice2 d3s7_mcemm noloop
    mc "It is... erm..."
    scene sm1ms014-93 mc-my-talking with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Honestly, it's part of the reason we're doing the renovations. We're hoping to be able to use the studio more for filming."
    play voice4 girl34_disappointed_eeh4 noloop
    my "Oh... I guess you use what you have at your disposal."
    my "What about assets? When this is all said and done, do you actually own anything?"
    play sound sfx_hair_scratch1
    scene sm1ms014-94 mc-talking with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "I do - all of the videos are my property. We had a lawyer draw up contracts between all of our stars and contractors."
    mc "Plus, that covers pay, testing, and anything else we might need covered in a legal contract."
    scene sm1ms014-95 my-impressed with dissolve
    play voice4 girl34_disappointed_oof1 noloop
    my "Oh..."
    scene sm1ms014-96 mc-surprised with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What?"
    scene sm1ms014-97 my-happy with dissolve
    play voice4 girl34_disappointed_eem2 noloop
    my "I just didn't think that this... new business was so well thought out."
    my "In all the time I've known you, you've never thought anything out this far."
    play sound sfx_cloth_rustling2
    scene sm1ms014-98 my-mc-having-a-moment with dissolve
    play voice4 girl34_happy_relief1 noloop
    if persistent.is_special:
        my "I'm proud of you, son."
        scene sm1ms014-99 mc-thanking-her with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Thanks, Mom."
    else:
        my "I'm proud of you, [mcname]."
        scene sm1ms014-99 mc-thanking-her with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Thanks, Melony."
    scene sm1ms014-100 my-talking with dissolve
    play voice4 girl34_arrogant_hm3 noloop
    my "I'm still not crazy about you not being in school, but..."
    play sound sfx_cloth_rustling3
    scene sm1ms014-101 my-talking with dissolve
    play voice4 girl34_disappointed_huh noloop
    my "At the very least, this doesn't sound like a half baked idea."
    my "Just, promise me you'll at least keep school in the back of your mind as an alternative."
    scene sm1ms014-102 mc-talking with dissolve
    play voice2 mc_yes_sure1 noloop
    if persistent.is_special:
        mc "I will, Mom."
    else:
        mc "I will, Melony."
    scene sm1ms014-103 my-asking-to-leave with dissolve
    play voice4 girl34_arrogant_ugu2 noloop
    my "All right, well I'm going to take off."
    my "I'll be by tomorrow, and I can help you and Stacy out around the studio."
    play sound sfx_cloth_rustling1
    play voice2 mc_happy_thatsgood noloop
    scene sm1ms014-104 mc-standing with dissolve
    mc "That sounds good!"
    play sound sfx_heels_steps1
    scene sm1ms014-105 my-leaving with dissolve
    stop sound fadeout 2.0
    play sound2 sfx_door_open1 noloop
    play voice4 girl34_hey_bye8 noloop
    if persistent.is_special:
        my "I'll see you tomorrow, Stacy! And keep your brother out of trouble."
        scene sm1ms014-106 sy-bye with dissolve
        play voice3 stacy_yes_yap3 noloop
        sy "I will, Mom!"
        scene sm1ms014-107 my-bye with dissolve
        play voice4 girl34_happy_relief3 noloop
        my "I love you, son."
        scene sm1ms014-108 mc-bye with dissolve
        play voice2 d9s2_ugu noloop volume 1.5
        mc "Love you too, Mom."
    else:
        my "I'll see you tomorrow, Stacy! And keep [mcname] out of trouble."
        scene sm1ms014-106 sy-bye with dissolve
        play voice3 stacy_yes_yap3 noloop
        sy "I will, Melony!"
        scene sm1ms014-107 my-bye with dissolve
        play voice4 girl34_happy_relief3 noloop
        my "Be good, [mcname]."
        scene sm1ms014-108 mc-bye with dissolve
        play voice2 d9s2_ugu noloop volume 1.5
        mc "I will."
    scene sm1ms014-107 my-bye with dissolve
    play voice4 girl34_hey_bye9 noloop
    my "Bye!"
    play sound sfx_door_closed1
    scene sm1ms014-109 mc-thinking with dissolve
    play voice2 mc_happy_oof3 noloop
    mct "Phew... that was a lot."
    scene sm1ms014-110 sy-talking with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "That could have been... worse?"
    scene sm1ms014-111 mc-talking with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah. It definitely could have."
    scene sm1ms014-112 mc-sy-talking with dissolve
    play voice3 stacy_hey_happy1 noloop
    sy "At least she sounds like she's warming up to the idea."
    play voice2 mc_yes_yes8 noloop
    mc "That she is. Which is good."
    scene sm1ms014-113 mc-talking with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "God, I am tired."
    scene sm1ms014-114 sy-talking with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Me too."
    scene sm1ms014-115 mc-proud with dissolve
    pause
    scene sm1ms014-116 sy-talking with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "We've made some good progress though."
    play voice3 stacy_angryhuh noloop
    sy "There's still so much to do though..."
    scene sm1ms014-117 mc-sy-talking with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "We should get those stairs installed though so we don't have to do some goofy climbing to get up there."
    play voice2 mc_yes_aga1 noloop
    mc "I'll see if I can get some good stairs delivered. We can install those next time we can carve out some time for the renovation."
    play sound sfx_cloth_rustling4
    scene sm1ms014-118 mc-sy-hugging with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "Yay!"
    sy "This is so exciting!"
    scene sm1ms014-119 mc-sy-hugging with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I think so too!"
    sy "..."
    scene sm1ms014-120 sy-lets-celeb with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Celebration sex?"
    scene sm1ms014-121 mc-nope with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I wish, Stacy, but I am exhausted."
    play voice3 stacy_pain_mmm2 noloop
    sy "Fiiiiiiine."
    scene sm1ms014-122 sy-going with dissolve
    queue voice3 stacy_angry noloop
    sy "In that case, I'm going to shower. I worked up quite the sweat today!"
    play sound sfx_door_openclosed1
    scene sm1ms014-123 mc-thinking with dissolve
    play voice2 d1s1_mmm noloop volume 2.5
    mct "Man... we're really doing this."
    mct "By the time this is over we're going to have like a real studio."
    scene sm1ms014-124 mc-thinking with dissolve
    mct "We're doing this... we're really doing this."
    mct "But, there's more that needs doing."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    call sm1ms014_start_renovation from _call_sm1ms014_start_renovation
    $ StoryController.end_scene(MS, 8, 0, 10)
    return
label sm1ms014_start_renovation:
    $ player.set_choice("sm1ms_renovation_started")
    $ CharacterController.get_character("sy").remove_schedule("sy_MS003_perma")
    $ LocationController.get_location(STUDIO, DEFAULT_SUBLOCATION, SD_BATHROOM).remove_override_interaction_option("io-SD_Peek_On_Stacy")
    return
label sm1ms014_charge_money:
    $ player.spend_money(300, _("Renovation equipment"), _("You spent $300 on renovation equipment"))
    return