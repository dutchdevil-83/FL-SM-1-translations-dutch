image sm1cs_mh002-glambot-1 = Movie(play = "images/Character-Scenes/mh/s002/anim/sm1cs-mh002-01-a04-2x-50fps.webm", start_image = "sm1cs-mh002-01-a04 sy-looks-away-mc-explains-her-worries-glambot-000_i", image = "sm1cs-mh002-01-a04 sy-looks-away-mc-explains-her-worries-glambot-119_i", loop = False)
image sm1cs_mh002-glambot-2 = Movie(play = "images/Character-Scenes/mh/s002/anim/sm1cs-mh002-a28-2x-50fps.webm", start_image = "sm1cs-mh002-a28 mh-thinking-will-need-few-days-lists-details-she-will-need-galmbot-000_i", image = "sm1cs-mh002-a28 mh-thinking-will-need-few-days-lists-details-she-will-need-galmbot-119_i", loop = False)
image sm1cs_mh002-glambot-3 = Movie(play = "images/Character-Scenes/mh/s002/anim/sm1cs-mh002-a01-04-2x-50fps.webm", start_image = "sm1cs-mh002-a01-04 sy-looks-away-mc-explains-her-worries-glambot-01-04-000_i", image = "sm1cs-mh002-a01-04 sy-looks-away-mc-explains-her-worries-glambot-01-04-119_i", loop = False)
label sm1cs_mh002:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.5, "sound2" )
    scene black
    show screen scene_transistion("Twenty minutes later")
    with Fade(0.5, 0.5, 0.5)
    pause
    play sound2 sfx_subwaycar fadein 1.5
    hide screen scene_transistion
    scene sm1cs-mh002-01-01 mc-ask-call-ahead-sy-oops_c1
    with Fade(0.5, 0.5, 0.5)
    play music monotonous_perverticus fadein 3.0
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Should we have called ahead?"
    scene sm1cs-mh002-01-02 mc-calls-himself-liver-sy-laughs_c1 with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "Probably. But it will be fun. Lyssa is always happy to see me?"
    scene sm1cs-mh002-01-01 mc-ask-call-ahead-sy-oops_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "What am I, chopped liver?"
    play voice3 stacy_laugh4 noloop
    sy "Hahaha."
    scene sm1cs-mh002-01-03 sy-little-concerned-mc-asking-about-what_c1 with dissolve
    queue voice3 stacy_thinking_hmm4 noloop
    sy "I am a little concerned."
    play voice2 mc_thinking_hmm1 noloop
    mc "About what?"
    play sound ["<silence 1.0>", sfx_camera_fly1] volume 2.8
    scene sm1cs_mh002-glambot-3 with dissolve
    pause
    play voice3 stacy_upset1 noloop volume 1.4
    sy "Well, what if all the legal mumbo-jumbo is too much."
    sy "Our dream of starting up a studio might be dead before it begins."
    stop sound fadeout 1.0
    scene sm1cs-mh002-01-06 mc-puts-hand-sy-shoulder_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "It can't be complicated. There are like a bajillion porn studios out there."
    mc "I'm sure we can figure it out."
    play sound mc_kiss1
    scene sm1cs-mh002-01-07 mc-kisses-sy-forehea_c1 with dissolve
    pause
    scene sm1cs-mh002-01-08 sy-thanks-mc-depending-taboo_c1 with dissolve
    play voice3 stacy_happy_relief1 noloop
    if persistent.is_special is True:
        sy "Thanks big bro."
    else:
        sy "You always know just what to say."
    play sound sfx_metro_closed1
    stop sound2 fadeout 2.0
    play sound3 "<from 8.0>audio/ambient/sfx_subwaystation.ogg" fadein 1.0 noloop
    scene sm1cs-mh002-01-09 mc-notices-their-stop-next-fade-black_c1 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "This is our stop."
    stop sound3 fadeout 1.0
    scene sm1cs-mh002-02 sy-mc-enter-mh-office_c1 with Fade(0.5, 0.5, 0.5)
    play sound sfx_door_closed1
    pause
    scene sm1cs-mh002-01-a04 sy-looks-away-mc-explains-her-worries-glambot-000_i with dissolve
    pause
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 1.6>", sfx_camera_fly1] noloop volume 2.0
    scene sm1cs_mh002-glambot-1
    pause
    play voice4 lissa_thinking2 noloop
    mh "Well, look what the cat dragged in."
    play voice2 mc_hey_hey5 noloop
    mc "Hey Lyssa."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mh002-05 sy-hi-mh-come-on-in_c1 with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "Hi Lyssa!"
    scene sm1cs-mh002-04 mh-look-what-cat-dragged-mc-hi-mh_c1 with dissolve
    play voice4 lissa_laugh2 noloop
    mh "Well come on in."
    scene sm1cs-mh002-06 sy-concerned-not-sure-what-happening_c1 with dissolve
    pause
    scene sm1cs-mh002-07 sy-asking-what-mc-did-her_c1 with dissolve
    play voice3 stacy_angry noloop
    sy "What's up with her? What did you do?"
    play voice2 mc_surprised_what1 noloop
    mc "What? I didn't do anything. At least, I don't think so."
    scene sm1cs-mh002-08 mh-asking-if-apologize-mc-ask-what-for_c1 with dissolve
    play voice4 lissa_cmonbaby noloop
    mh "So, are you finally going to apologize?"
    scene sm1cs-mh002-10 mc-sy-surprised-mc-whahuh_c1 with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Apologize for what?"
    scene sm1cs-mh002-09 mh-explains-not-including-her_c1 with dissolve
    play voice4 lissa_oh2 noloop
    mh "For not letting me join you to take down the villain behind Fetish Locator?"
    scene sm1cs-mh002-10 mc-sy-surprised-mc-whahuh_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "Whahuh?"
    scene sm1cs-mh002-11 sy-explains-werent-trying-exclude-mh_c1 with dissolve
    play voice3 stacy_no_nonono2 noloop
    sy "We weren't trying to exclude you or anything, Lyssa."
    sy "The plan kind of came together real fast and before we knew it, [mcname] stumbled his way into solving the riddle."
    scene sm1cs-mh002-12 sy-sorry-not-calling_c1 with dissolve
    play voice3 stacy_disappointed_oh2 noloop
    sy "But... we are sorry that we didn't call you to help us take down that bitch."
    scene sm1cs-mh002-13 mh-ty-sy-was-just-pulling-leg_c1 with dissolve
    play voice4 lissa_mmm1 noloop
    mh "Thank you, Stacy."
    scene sm1cs-mh002-14 mh-tells-gang-was-able-figure-lydia_c1 with dissolve
    queue voice4 lissa_haha noloop
    mh "I was just pulling your leg. From what I heard of, things picked up pace near the end of the semester."
    mh "It sounds like once you guys picked up steam, you were able to pierce the vale of mystery quite quickly to figure out what Lydia was doing."
    scene sm1cs-mh002-15 mc-rubs-neck-yeah-mct-thinks-what-if_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. I did have some pretty good motivation to put an end to things as quickly as possible."
    mct "Who knows what Lydia would have cooked up for me after the cockcage."
    scene sm1cs-mh002-16 mh-smiles-hopes-if-involved-will-call-loves-good-story_c1 with dissolve
    play voice4 lissa_thinking1 noloop
    mh "Hmmm. Well, I hope if you get involved in something like that again, you'll give me a call."
    mh "I love a good story of people rising to the occasion."
    scene sm1cs-mh002-17 sy-totally-will-jokes-mc-likes-rising-ocasion_c1 with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "We totally will. I'm sure there will be plenty of capers ahead."
    sy "And we know that [mcname] always likes 'rising', no matter the occasion."
    scene sm1cs-mh002-18 mc-shoots-look-sy-mh-laughs-off-camera_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Stacy..."
    scene sm1cs-mh002-19 mh-points-chair-sit-down-talk_c1 with dissolve
    play voice4 lissa_laugh noloop
    mh "Hahaha."
    mh "Alright. Why don't you two sit down and explain what you're here for."
    play sound sfx_cloth_rustling2
    scene sm1cs-mh002-20 mc-sy-sitting-chairs-mh-sitting-desk-front-of-them_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.4
    mc "So that's the long and short of it. Stacy and I are building our own porn studio."
    scene sm1cs-mh002-22 sy-explain-why-they-started-porn-studio_c1 with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "We learned so much from our experiences with Fetish Locator, including just how many sex-positive people there are in the city."
    sy "So we figured, why not build something amazing with our knowledge and expertise."
    scene sm1cs-mh002-23 mh-very-bold-on-brand-mc-thanks_c1 with dissolve
    play voice4 lissa_moan1 noloop
    mh "Well it is very on-brand for you two. Very bold."
    scene sm1cs-mh002-21 mc-so-that_s-long-and-short-building-porn-studio_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thanks."
    scene sm1cs-mh002-24 mh-guessing-some-kind-hiccup-mc-need-figure-out-legals_c1 with dissolve
    play voice4 lissa_shyoh noloop
    mh "But I'm guessing you ran into some kind of legal hiccup."
    scene sm1cs-mh002-21 mc-so-that_s-long-and-short-building-porn-studio_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "We're close to having our first cast member join the studio, and we need to figure out everything involved so that everyone is safe from a legal standpoint."
    scene sm1cs-mh002-25 sy-thought-she-knows-mh-smiles-appriciate_c1 with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "So naturally, we thought you might know something about the nitty-gritty."
    scene sm1cs-mh002-24 mh-guessing-some-kind-hiccup-mc-need-figure-out-legals_c1 with dissolve
    play voice4 lissa_moan3 noloop
    mh "Well Stacy, I appreciate your faith in my expert knowledge of the law, but the specific arena of employment contracts for adult film actors was not something that interested me while I studied."
    scene sm1cs-mh002-26 sy-very-worried-oh-no-mh-amazing-lawyer-will-help_c1 with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Oh no."
    scene sm1cs-mh002-27 mh-ofcourse-they-helped-her-now-she-help-them-mc-thanks-mh_c1 with dissolve
    play voice4 lissa_haha2 noloop
    mh "But what kind of amazing lawyer would I be if I couldn't find out the basics of what you two need to get things started?"
    scene sm1cs-mh002-22 sy-explain-why-they-started-porn-studio_c1 with dissolve
    play voice3 stacy_surprised_huh3 noloop
    sy "You mean it?"
    scene sm1cs-mh002-23 mh-very-bold-on-brand-mc-thanks_c1 with dissolve
    play voice4 lissa_yes noloop
    mh "Of course. You came to me for help, and I'm not in the habit of letting my friends down."
    scene sm1cs-mh002-30 mc-have-figure-way-pay-her-budget-tight-right-now_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Thanks, Lyssa."
    scene sm1cs-mh002-a28 mh-thinking-will-need-few-days-lists-details-she-will-need-galmbot-119_i with dissolve
    play voice4 lissa_thinking2 noloop volume 1.4
    mh "Now it might take me a few days to get the basics worked out, so I'll need the basic information for the candidate sent to me as soon as possible."
    mh "Legal name, date of birth, a copy of a government-issued license. There is probably more."
    scene sm1cs-mh002-a28 mh-thinking-will-need-few-days-lists-details-she-will-need-galmbot-000_i with dissolve
    pause 0.1
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 1.6>", sfx_camera_fly1] noloop volume 2.0
    scene sm1cs_mh002-glambot-2
    pause
    play sound sfx_cloth_rustling1
    stop sound2 fadeout 1.0
    scene sm1cs-mh002-29 sy-mc-stand-from-chairs-sy-ofcourse-mh-mh-not-sure-more-help-today-will-deliver_c1 with dissolve
    play voice3 stacy_yes_fine3 noloop
    sy "Of course. I can email you over everything we have and get anything missing sent over."
    play voice4 lissa_ugu noloop
    mh "Excellent. Well, I coudln't be much help today, but I am sure I can deliver in the next couple of days."
    scene sm1cs-mh002-30 mc-have-figure-way-pay-her-budget-tight-right-now_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Right. And uh... we'll have to figure out how to pay you for your time."
    mc "Things are a bit tight right now."
    play sound sfx_cloth_rustling2
    scene sm1cs-mh002-31 mh-waves-off-nonsense-will-owe-her-mc-thinks-mh-diamond_c1 with dissolve
    play voice4 lissa_lno noloop
    mh "Nonsense. It shouldn't be too difficult for me. Let's just say that you both owe me one."
    play voice2 mc_scared_oh1 noloop
    mc "You're a diamond, Lyssa."
    mh "I like helping people. That's all."
    scene sm1cs-mh002-32 mh-likes-helping-people-sy-puzzled-asking_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "So is that one favor from both of us? Or one favor from each of us."
    scene sm1cs-mh002-33 mh-leans-sy-seductively-will-find-out-for-now-bye_c1 with dissolve
    play voice4 lissa_laugh2 noloop
    mh "I supposed you'll find out when I come up with something, Stacy."
    mh "For now though, I will have to bid you two adieu. I have a client coming in. But I'll be in touch."
    scene sm1cs-mh002-34 mc-sy-wave-mh-leave-office-end-scene_c1 with dissolve
    play voice3 stacy_hey_byebye noloop
    sy "Bye Lyssa. Thanks again."
    play voice4 lissa_ugu2 noloop
    mh "Ciao."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene_in_time(MH_STORY, 18, 0, 2)
    return