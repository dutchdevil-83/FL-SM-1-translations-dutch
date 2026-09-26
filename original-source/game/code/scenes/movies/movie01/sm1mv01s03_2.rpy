image sm1mv01s03_2-a59-glambot = Movie(play = "images/MV/mv01/s03_2/anim/sm1mv01s03_2-a59-2x-50fps.webm", start_image = "sm1mv01s03_2-a59 tl-oh-wasnt-asking-permission-glambot-_0_00_i", image = "sm1mv01s03_2-a59 tl-oh-wasnt-asking-permission-glambot-_0_78_i", loop = False)
image sm1mv01s03_2-a19-glambot = Movie(play = "images/MV/mv01/s03_2/anim/sm1mv01s03_2-a19-2x-50fps.webm", start_image = "sm1mv01s03_2-a19 tl-turns-towards-mc-thanks-grabbing-clothes-glambot-00_i", image = "sm1mv01s03_2-a19 tl-turns-towards-mc-thanks-grabbing-clothes-glambot-89_i", loop = False)
label sm1mv01s03_2:
    if vn_mode:
        $ renpy.music.set_volume(0.6, 0.5, "music" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
        play music music_freeroam_gunsnrosette2
    else:
        $ renpy.music.set_volume(1.0, 0.5, "music" )
        $ renpy.music.set_volume(0.6, 3.0, "freeroam_music1" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play sound4 sfx_crowd_fightclub_ambient2 fadein 1.5
    scene sm1mv01s03_2-01 mc-sees-tl-drinking-clowns_c1 with dissolve
    pause
    play sound sfx_double_door1
    play sound2 sfx_heels_steps2
    scene sm1mv01s03_2-01-02 mc-there-you-are-tl-mmm_c1 with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "There you are."
    stop sound2 fadeout 1.0
    scene sm1mv01s03_2-01-03 tl-sees-mc-oh-hey-mc_c1 with dissolve
    play voice3 girl24_thinking_hmm1 noloop
    tl "Mmm?"
    tl "Oh. Hey, [mcname]."
    scene sm1mv01s03_2-01-04 mc-silent-looking-mad_c1 with dissolve
    pause
    scene sm1mv01s03_2-01-05 mc-eyes-clowns-they-neutral-mc-ask-everything-good-tl_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Everything good, Taisia?"
    scene sm1mv01s03_2-01-06 tl-oh-yeah-just-taking-breather_c1 with dissolve
    play voice3 girl24_arrogant_yeah1 noloop
    tl "Oh yeah."
    tl "Just taking a breather after work."
    scene sm1mv01s03_2-01-07 tl-three-birthdays-jg-celelbrating-death_c1 with dissolve
    play voice3 girl24_disappointed_eeh1 noloop
    tl "We had three mega birthday parties with some real little shits to handle."
    scene sm1mv01s03_2-01-08 jg-klusty-clown-tl-right-this-juggsy_c1 with dissolve
    play voice4 girl32_disappointed_ehh2 noloop
    jg "And we're celebrating the death of our beloved comrade in big shoes."
    jg "Klusty the Clown."
    play voice3 girl24_disappointed_oh noloop
    tl "Oh right. [mcname], this is Juggsy."
    scene sm1mv01s03_2-01-09 tl-introduces-bentley-this-bentley-clown-palls_c1 with dissolve
    play voice3 girl24_thinking_hmm3 noloop
    tl "And this is Bently."
    tl "Pals of mine in the carnival clown posse."
    scene sm1mv01s03_2-01-10 mc-choice-menu-screen_c1 with dissolve
    menu:
        "How did Klusty die?":
            play voice2 mc_thinking_mmm5 noloop
            mc "Did Klusty die during a performance?"
            scene sm1mv01s03_2-01-11 choice-how-klusty-dies-mc-ask-how-tl-explains-tricycle-extravaganza_c1 with dissolve
            play voice3 girl24_yes_simple2 noloop
            tl "Yes, he tried to do the tricycle extravaganza."
            scene sm1mv01s03_2-01-12 be-close-pulling-it-jg-then-chocked-on-tricycle_c1 with dissolve
            play voice5 boy7_disappointed_mff noloop
            be "He got close to pulling it off. {w}But then he choked on the tricycle."
            scene sm1mv01s03_2-01-13 clowns-keep-moment-silence_c1 with dissolve
            pause
            play sound sfx_hair_scratch1
            scene sm1mv01s03_2-01-14 mc-silent-moment_c1 with dissolve
            play voice2 mc_thinking_mmm4 noloop
            pause
            play sound2 sfx_heels_steps2
            scene sm1mv01s03_2-01-15 mc-goes-towards-bar-get-drink_c1 with dissolve
            pause
            play sound2 sfx_throw_something1 noloop
            scene sm1mv01s03_2-01-16 mc-back-with-drink-to-klusty-tl-yeah-klusty_c1 with fade
            play voice2 d2s9_confused noloop
            mc "To Klusty the clown then."
            play voice3 girl24_happy_yeah3 noloop
            tl "Yeah. To Klusty!"
            scene sm1mv01s03_2-01-17 juggsy-joins-klusty_c1 with dissolve
            play voice4 girl32_yes_yep noloop
            jg "To Klusty!"
            scene sm1mv01s03_2-01-18 be-still-hear-ghost-ring-ring_c1 with dissolve
            play voice5 boy7_disappointed_groan noloop
            be "Legend has it sometimes you can hear his ghost at the carnival."
            be "Ring ring. Ring ring."
            scene sm1mv01s03_2-01-19 mc-okay-cheers_c1 with dissolve
            play voice2 mc_angry_huh2 noloop
            mc "Okay..."
            mc "Cheers."
            play sound sfx_drink_loop1 volume 3.0
            play sound2 sfx_drink_gulp noloop
            scene sm1mv01s03_2-01-20 gang-takes-drink_c1 with dissolve
            pause
            stop sound fadeout 1.0
        "I was a little worried":
            $ player.set_choice("sm1mv01s03_2_worried")
            $ CharacterController.get_character("tl").add_point(1)
            scene sm1mv01s03_2-01-21 choice-waslittle-worried-mc-cool-cool-glad-alright_c1 with dissolve
            play voice2 mc_yes_aga2 noloop
            mc "Cool cool. Just glad you're doing okay."
            scene sm1mv01s03_2-01-22 tl-ofc-she-is-softie-not-many-ppl-mess-three-clowns_c1 with dissolve
            play voice2 girl24_arrogant_kgh1 noloop
            tl "Of course I am, you big softie."
            tl "Not many people out there like to mess with a clown, let alone three."
            scene sm1mv01s03_2-01-23 jg-cracks-knuckle-not-unless-knuckle-sandwich_c1 with dissolve
            play voice4 girl32_yes_yep noloop
            jg "Not unless they want a knuckle sandwich and fries."
            scene sm1mv01s03_2-01-24 be-mmm-knuckle-sandwich-do-serve-food_c1 with dissolve
            play voice5 boy7_disappointed_groan noloop noloop
            be "Mmm. Knuckle sandwich."
            be "Do they serve food here?"
    scene sm1mv01s03_2-01-25 tl-look-mc-whats-up-dont-think-here-sad-clowns_c1 with dissolve
    play voice3 girl24_hey_simple noloop
    tl "So what's up, [mcname]?"
    tl "I don't think you came here looking for sad clowns."
    scene sm1mv01s03_2-01-26 jg-not-sad-clowns-we-getting-close-drunk-clowns_c1 with dissolve
    play voice4 girl32_no_nah noloop
    jg "We're not sad clowns."
    jg "We are getting close to becoming drunk clowns."
    scene sm1mv01s03_2-01-27 be-worked-drunk-clown-was-fun-could-never-work-second-floor_c1 with dissolve
    play voice5 boy7_thinking_hmm3 noloop
    be "I worked with a drunk clown once."
    be "He was fun, but we could never work a job on the second floor."
    scene sm1mv01s03_2-01-28 mc-why-not-be-he-hated-upstairs_c1 with dissolve
    play voice2 mc_surprised_why3 noloop
    mc "Why not?"
    scene sm1mv01s03_2-01-29 mc-why-hate-stairs-be-he-afraid-twelve-steps_c1 with dissolve
    play voice5 boy7_thinking_oh noloop
    be "He hated going up stairs."
    play voice2 mc_arrogant_hm1 noloop
    mc "Why did he hate stairs?"
    scene sm1mv01s03_2-01-30 tl-god-bentley-jg-why-drunk-clown-go-cemetery_c1 with dissolve
    play voice5 boy7_happy_laugh1 noloop
    be "He was afraid of the twelve steps."
    play voice3 girl24_surprised_ohmy1 noloop
    tl "*groans* Oh my god, Bentley."
    scene sm1mv01s03_2-01-31 mc-why-tl-dont-get-them-started_c1 with dissolve
    play voice4 girl32_surprised_huh noloop
    jg "Why did the drunk clown go to the cemetery?"
    play voice2 mc_surprised_why1 noloop
    mc "Why?"
    play voice3 girl24_no_confident noloop
    tl "No! Don't get them started!"
    scene sm1mv01s03_2-01-32 jg-punchline-she-looking-spirits-clowns-laughing-hooting_c1 with dissolve
    play voice4 girl32_hey_happy noloop
    jg "She was looking for spirits."
    scene sm1mv01s03_2-01-33 tl-you-two-worst-everything-wrong-clowns_c1 with dissolve
    play voice4 girl32_happy_woohoo noloop
    play voice5 boy7_happy_laugh4 noloop
    "Juggsy and Bently" "Laughing and hooting."
    play voice3 girl24_disgust_boeagh1 noloop
    tl "You two are the worst."
    tl "You're everything wrong with modern clowns."
    scene sm1mv01s03_2-01-34 be-ahaha-see-smiling-taisia-tl-dont-smile_c1 with dissolve
    play voice5 boy7_happy_relief noloop
    be "Ahooo-hah. Hah. I see you smiling, Taisia."
    play voice3 girl24_no_uhuh noloop
    tl "I don't smile."
    scene sm1mv01s03_2-01-35 mc-remember-why-looking-you-uuuhm_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Right. Taisia, I remembered the reason I was looking for you."
    scene sm1mv01s03_2-01-36 tl-what-mc-kind-private_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Ummmm."
    play voice3 girl24_thinking_hmm5 noloop
    tl "What?"
    mc "Well, it's kind of private."
    scene sm1mv01s03_2-01-37 tl-thanks-jg-be-trusted-pals-saved-each-other-lives_c1 with dissolve
    play voice3 girl24_no_nah noloop
    tl "Thanks, but you can say whatever you want."
    tl "Juggsy and Bentley are my trusted associates."
    tl "We've all saved each others' lives from rogue carnies and crazy rubes."
    scene sm1mv01s03_2-01-38 jg-noone-takes-seriously-when-talk_c1 with dissolve
    play voice4 girl32_disappointed_hm noloop
    jg "No one takes us seriously when we talk anyhow."
    scene sm1mv01s03_2-01-39 be-sad-yeah-that-happened-made-hostage-negotiator-difficult_c1 with dissolve
    play voice5 boy7_disappointed_aah noloop
    be "Yeah... And that happened even before I put on the red nose."
    be "It made being a hostage negotiator extremely difficult."
    mc "..."
    scene sm1mv01s03_2-01-40 mc-well-here-say-ready-table-read-tl-you-serious_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Well I came here to say that we are ready to do the first table read for the movie script."
    scene sm1mv01s03_2-01-41 mc-deadly-tl-about-damn-time_c1 with dissolve
    play voice3 girl24_surprised_huh1 noloop
    tl "You serious?"
    play voice2 mc_yes_yes3 noloop
    mc "Deadly."
    tl "It's about damn time."
    scene sm1mv01s03_2-01-42 tl-you-guys-settle-tab-be-ofc_c1 with dissolve
    play voice3 girl24_surprised_eeh2 noloop
    tl "You guys can settle my tab?"
    play voice5 boy7_yes_yep noloop
    be "Of course."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1mv01s03_2-01-43 mc-tl-leaving-jg-be-behind-saying-jokes-for-bye_c1 with dissolve
    play voice4 girl32_hey_bye2 noloop
    jg "Have fun, Taisia."
    jg "Honk the nose. Twirl the tie."
    play voice5 boy7_yes_aga1 noloop
    be "Break every mirror you can see."
    stop sound2 fadeout 1.0
    scene sm1mv01s03_2-01-44 tl-blows-kisses-love-you-guys_c1 with dissolve
    play voice3 girl24_sex_closedmoan2 noloop
    play sound mc_kiss1
    tl "Love you guys."
    scene sm1mv01s03_2-01-45 mc-interesting-friends-tl-should-meet-smoking-lion-leave-bar_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Interesting friends."
    play voice3 girl24_happy_laugh1 noloop
    tl "You should meet the smoking lion..."
    stop sound4 fadeout 1.5
    if vn_mode:
        stop music fadeout 3.0
    else:
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    play sound sfx_door_closed1
    scene sm1mv01s03_2-02 mc-tl-enter-sutdio_c1 with fade
    play sound2 sfx_heels_steps2
    play sound3 sfx_heels_steps1
    queue music music_gentle_spa
    pause
    scene sm1mv01s03_2-03 sy-kv-kitchen-hey-taisia-tl-hey-sy_c1 with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "Hey, Taisia. Glad you found her, [mcname]."
    play voice4 girl24_hey_greeting noloop
    tl "Hey, Stacy."
    scene sm1mv01s03_2-04 kv-nods-taisia-tl-good-see-gang-together_c1 with dissolve
    play voice5 kanya_hey_simple2 noloop
    kv "Taisia."
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1mv01s03_2-06 tl-good-luck-hate-sometimes_c1 with dissolve
    play voice4 girl24_happy_yeah1 noloop
    tl "Nice, we've got the full crew here."
    tl "How's it going, Kanya?"
    scene sm1mv01s03_2-05 tl-how-going-kanya-kv-good-finding-lens_c1 with dissolve
    play voice5 kanya_happy_relief3 noloop
    kv "Good. Ready to find the best lenses to capture your essence."
    scene sm1mv01s03_2-06 tl-good-luck-hate-sometimes_c1 with dissolve
    play voice4 girl24_arrogant_hah noloop
    tl "Good luck. My essence cannot be captured or restrained."
    tl "I hate it sometimes..."
    scene sm1mv01s03_2-07 kv-giggling_c1 with dissolve
    play voice5 kanya_happy_laugh2 noloop
    kv "*giggling*"
    scene sm1mv01s03_2-08 tl-looks-mc-tl-hear-got-show-sy-oh-yeah_c1 with dissolve
    play voice4 girl24_thinking_huh1 noloop
    tl "[mcname] tells me that we've got a show to get ready for."
    play voice3 stacy_yes_yeah2 noloop
    sy "Oh yeah."
    scene sm1mv01s03_2-09 tl-gotta-wash-up-hot-shower_c1 with dissolve
    play voice4 girl24_yes_aga noloop
    tl "I just gotta wash up."
    tl "A hot shower will get my head back in the game."
    play voice3 stacy_yes_ugu1 noloop
    sy "Sure."
    scene sm1mv01s03_2-11 tl-be-dear-grab-clothes-mc-yeah-sure_c1 with dissolve
    play voice4 girl24_thinking_hmm6 noloop
    tl "Be a dear and go grab some clothes for me, roomie."
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah sure."
    play sound2 sfx_heels_steps2
    play sound3 sfx_heels_steps1
    scene sm1mv01s03_2-12 mc-goes-upstairs-tl-bathroom_c1 with dissolve
    pause
    play sound3 sfx_door_closed1 noloop
    scene sm1mv01s03_2-13 mc-in-tl-room-holding-clothes-what-now-butler_c1 with dissolve
    play sound2 sfx_cloth_rustling1 noloop
    play voice2 mc_angry_hm1 noloop
    mc "What am I, a butler now?"
    play sound sfx_knock_wood2
    $ renpy.music.set_volume(0.3, 0.0, "sound4" )
    play sound4 sfx_shower_ambience1
    scene sm1mv01s03_2-14 mc-front-bathroom-door-shower-sounds-knocking_c1 with dissolve
    "*shower water running*"
    play voice2 mc_hey_hey5 noloop
    mc "Got your clothes ready, Taisia."
    scene sm1mv01s03_2-15 mc-got-clothes-tl-come-in_c1 with dissolve
    play voice4 girl24_yes_happy_muffled noloop
    tl "Come in, [mcname]."
    play sound sfx_door_open1
    $ renpy.music.set_volume(0.7, 5.0, "sound4" )
    scene sm1mv01s03_2-16 mc-enters-wow-here-go_c1 with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Woah."
    mc "Here you go."
    play sound sfx_door_closed2
    play sound2 sfx_shower_off1 noloop
    stop sound4 fadeout 0.5
    scene sm1mv01s03_2-17 tl-mischevious-tl-grow-up-fucked-every-hole_c1 with dissolve
    queue sound4 sfx_cloth_wiping1
    play voice4 girl24_arrogant_pff noloop
    tl "Grow up, [mcname]."
    tl "You've fucked every hole on my body."
    scene sm1mv01s03_2-18 mc-shrugs-old-habits_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Old habits I guess."
    scene sm1mv01s03_2-a19 tl-turns-towards-mc-thanks-grabbing-clothes-glambot-00_i with dissolve
    pause 0.01
    play sound sfx_camera_fly1 volume 2.0
    scene sm1mv01s03_2-a19-glambot
    play voice4 girl24_thinking_emm2 noloop
    tl "Thanks for grabbing my clothes."
    play sound sfx_barefoot_steps1 volume 2.0
    scene sm1mv01s03_2-20 tl-enters-shower_c1 with dissolve
    pause
    play sound sfx_shower_off1
    $ renpy.music.set_volume(1.0, 0.0, "sound4" )
    play sound4 sfx_shower_ambience1
    scene sm1mv01s03_2-21 tl-under-shower_c1 with dissolve
    pause
    scene sm1mv01s03_2-22 tl-put-clothes-down-mmm_c1 with dissolve
    play voice4 girl24_yes_ugu noloop
    tl "You can put the clothes down."
    scene sm1mv01s03_2-23 tl-thanks-mc-for-what_c1 with dissolve
    play voice4 girl24_happy_mmm noloop
    tl "Mmmmm..."
    scene sm1mv01s03_2-24 tl-washes-body-even-after-chose-me_c1 with dissolve
    pause
    scene sm1mv01s03_2-25 tl-washes-boobs-sure-girls-less-baggage_c1 with dissolve
    play voice4 girl24_sex_closedmoan5 noloop
    tl "Thanks."
    scene sm1mv01s03_2-26 mc-choice-menu-screen_c1 with dissolve
    play voice2 mc_surprised_what7 noloop
    mc "For what?"
    play voice4 girl24_thinking_hmm2 noloop
    tl "Even after you chose me, a part of me figured that eventually, you'd sit me down and say something had changed..."
    tl "I'm sure there are girls with less baggage you could hire to be in your movies."
    scene sm1mv01s03_2-27 choice-mc-chose-you-mc-want-about-let-down-when-started-said-have-work_c1 with dissolve
    menu:
        "I chose you for the role":
            $ CharacterController.get_character("tl").add_point(2)
            $ player.set_choice("sm1mv01s03_2_chose_tl")
            play voice2 mc_no_no5 noloop
            mc "I wasn't about to let you down, Taisia."
            mc "When we started this thing, I said I'd have some work for you."
            scene sm1mv01s03_2-28 tl-turned-away-like-said-thanks-wont-let-down-either_c1 with dissolve
            play voice4 girl24_arrogant_huh1 noloop
            tl "Like I said. 'Thanks'."
            tl "I won't let you down either, [mcname]."
        "I don't like the sound of that":
            $ CharacterController.get_character("tl").deduct_point(2)
            scene sm1mv01s03_2-29 choice-no-like-sound-mc-what-saying-not-up-this_c1 with dissolve
            play voice2 mc_surprised_what1 noloop
            mc "What? Are you saying that you're not up to this?"
            scene sm1mv01s03_2-30 tl-neutral-never-said-that_c1 with dissolve
            play voice4 girl24_no_simple1 noloop
            tl "Hell no!"
            scene sm1mv01s03_2-31 tl-turns-away-let-girl-take-shower_c1 with dissolve
            play voice4 girl24_arrogant_hm4 noloop
            tl "I never said that.{w} I'm just glad you stuck with me for the role."
            play voice2 mc_yes_ugu1 noloop
            mc "Mmhmm."
    tl "Now... Can you let a girl shower in peace or what?"
    scene sm1mv01s03_2-32 mc-grinning_c1 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    pause
    play sound sfx_door_open1
    $ renpy.music.set_volume(0.3, 1.0, "sound4" )
    scene sm1mv01s03_2-33 mc-walks-out-just-dont-take-long_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Just don't take too long."
    $ renpy.music.set_volume(1.0, 1.0, "sound4" )
    scene sm1mv01s03_2-34 tl-keeps-showering-yup-work-be-done_c1 with dissolve
    play voice4 girl24_yes_yap noloop
    tl "Yup."
    tl "Work to be done, heh."
    stop sound4 fadeout 1.5
    scene sm1mv01s03_2-35 gang-sitting-couch-ready-read_c1 with Fade(0.3, 0.3, 0.3)
    play voice3 stacy_thinking_hmm1 noloop
    sy "So that is most of the setup out of the way."
    scene sm1mv01s03_2-36 sy-so-that-about-setup-everyone-good_c1 with dissolve
    play voice3 stacy_huh2 noloop
    sy "Everyone good?"
    scene sm1mv01s03_2-37 mc-tl-kv-all-yep_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yup."
    play voice4 girl24_yes_simple1 noloop
    tl "On track."
    play voice5 kanya_yes_yep1 noloop
    kv "Good to go."
    scene sm1mv01s03_2-38 sy-gestures-mc-okay-take-it-away_c1 with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    if persistent.is_special:
        sy "Now I'll turn it over to big bro."
    else:
        sy "Now I'll turn it over to [mcname]."
    scene sm1mv01s03_2-39 mc-right-focus-on-these-fetishes_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Right."
    mc "So for this film, we're going to focus on these fetishes."
    play sound sfx_paper_slide1
    scene sm1mv01s03_2-40 got-choking-maso-extreme_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "We've got choking, masochism, extreme..."
    scene sm1mv01s03_2-41 tl-smiling-at-him-mc-continues-cum-swallowing_c1 with dissolve
    play voice4 girl24_sex_closedmoan1 noloop
    pause
    scene sm1mv01s03_2-42 group-shot-mc-finish-threesome-tl-hot_c1 with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "... cum swallowing since we can't do sword swallowing."
    mc "And we'll round it out with some threesome action that includes girl girl."
    play voice4 girl24_disappointed_ohh2 noloop
    tl "Hot."
    scene sm1mv01s03_2-43 sy-not-forget-bondage-mc-check-script_c1 with dissolve
    play voice3 stacy_hey_happy1 noloop
    sy "Don't forget bondage in the 'Recruitment' scene."
    mc "..."
    scene sm1mv01s03_2-44 right-yeah-tying-taisia_c1 with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Oh right."
    mc "Yeah, we'll be tying Taisia up when she works to recruit Captain Dickhart."
    scene sm1mv01s03_2-45 kv-kinky-tl-nods_c1 with dissolve
    play voice5 kanya_happy_laugh3 noloop
    kv "Kinky."
    play voice2 mc_thinking_hmm1 noloop
    mc "We all good on those. None opposed?"
    scene sm1mv01s03_2-44 right-yeah-tying-taisia_c1 with dissolve
    play voice4 girl24_surprised_huh2 noloop
    tl "Do I get paid extra for getting tied up?"
    play voice2 mc_no_nope1 noloop
    mc "Nope. Next time, check the small print on your agreement."
    play voice4 girl24_happy_laugh5 noloop
    tl "*laughing*"
    tl "You rotten scallywag."
    scene sm1mv01s03_2-45 kv-kinky-tl-nods_c1 with dissolve
    play voice5 kanya_angry_hm noloop
    kv "There you go, use the anger."
    scene sm1mv01s03_2-47 tl-get-paid-extra-mc-no-next-time-read-print_c1 with dissolve
    play voice4 girl24_arrogant_yeah2 noloop
    tl "That's my secret, cap."
    scene sm1mv01s03_2-50 sy-gets-back-turn-page-four_c1 with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "Alright, now turn to page four and we can start the readthrough."
    play sound sfx_barefoot_steps1 loop
    scene sm1mv01s03_2-51 tl-goes-towards-kitchen-hup-sy-huh_c1 with dissolve
    play voice4 girl24_arrogant_kgh2 noloop
    tl "Hup."
    play voice3 stacy_surprised_huh1 noloop
    sy "Huh?"
    scene sm1mv01s03_2-52 tl-need-beer-mc-taisia-come-on_c1 with dissolve
    play voice4 girl24_thinking_emm1 noloop
    tl "Anyone need a beer?"
    play voice2 mc_disappointed_off1 noloop
    mc "Taisa, come on."
    scene sm1mv01s03_2-53 kv-looking-script-drink-acting-great-combo_c1 with dissolve
    play voice5 kanya_disgust_meh noloop
    kv "Drinking and acting. Great combination."
    play sound sfx_fridge_closed1
    scene sm1mv01s03_2-54 tl-we-not-acting-just-reading_c1 with dissolve
    play voice4 girl24_disappointed_ohh1 noloop
    tl "Oh come on."
    tl "We're not acting, we're just reading and talking."
    scene sm1mv01s03_2-55 sy-silently-looking-mc_c1 with dissolve
    sy "..."
    scene sm1mv01s03_2-56 kv-glancing-mc_c1 with dissolve
    pause
    scene sm1mv01s03_2-57 mc-thinking-choice-menu-screen_c1 with dissolve
    mc "..."
    menu:
        "Maybe we should leave the drinks till after, Taisia":
            $ CharacterController.get_character("kv").add_point(2)
            $ CharacterController.get_character("tl").deduct_point(2)
            scene sm1mv01s03_2-58 choice-maybe-drinks-later-mcmaybe-drinks-later_c1 with dissolve
            play voice2 mc_hey_hey2 noloop
            mc "Maybe we should leave the drinks till after, Taisia."
            scene sm1mv01s03_2-a59 tl-oh-wasnt-asking-permission-glambot-_0_00_i with dissolve
            pause 0.01
            play sound sfx_camera_fly1 volume 2.0
            scene sm1mv01s03_2-a59-glambot
            play voice4 girl24_disappointed_oh noloop
            tl "Oh."
            tl "I wasn't really asking for permission."
            play sound sfx_beer_open1
            scene sm1mv01s03_2-60 tl-snaps-bottle-snapping-sound_c1 with dissolve
            "Snnnnnp"
            play sound sfx_cloth_rustling4
            scene sm1mv01s03_2-61 tl-sits-down-aight-now-ready_c1 with dissolve
            play voice4 girl24_happy_phew1 noloop
            tl "Alright, now I'm ready."
        "Alright. I'll take one too":
            $ CharacterController.get_character("tl").add_point(2)
            $ CharacterController.get_character("kv").deduct_point(2)
            $ player.set_choice("sm1mv01s03_2_tl_beer")
            play voice2 mc_yes_yeah7 noloop
            mc "Yeah, I could use a beer."
            scene sm1mv01s03_2-63 sy-kv-both-glance-mc_c1 with dissolve
            pause
            scene sm1mv01s03_2-64 sy-yeah-one-me-too-tl-okay_c1 with dissolve
            play voice3 stacy_yes_yeah1 noloop
            sy "Yeah. One for me too."
            play voice4 girl24_yes_calm noloop
            play sound sfx_beer_open1
            tl "Alright."
            play sound sfx_barefoot_steps1
            scene sm1mv01s03_2-65 kv-frowns-tl-coming-with-beers_c1 with dissolve
            pause
            play sound sfx_cloth_rustling4
            scene sm1mv01s03_2-66 tl-sits-down-kv-pulls-up-phone_c1 with dissolve
            pause
            scene sm1mv01s03_2-67 tl-teases-kv-what-blue-gloomy-kv-hair-turqoise_c1 with dissolve
            play voice4 girl24_thinking_ah noloop
            tl "Ah. Guess who has blue hair, and is a gloomy girl."
            scene sm1mv01s03_2-68 tl-right-both-counts-kanya_c1 with dissolve
            play voice5 kanya_arrogant_ha noloop
            kv "My hair is turquoise."
            play voice4 girl24_yes_aga noloop
            tl "Right on both counts, Kanya."
    if player.get_choice("sm1mv01s03_2_tl_beer"):
        scene sm1mv01s03_2-69 mc-taking-sip-beer_c1 with dissolve
        play sound sfx_drink_gulp
        pause
        scene sm1mv01s03_2-70 sy-also-takes-sip_c1 with dissolve
        play sound sfx_drink_gulp
        pause
    else:
        scene sm1mv01s03_2-71 mc-looking-tl-amused_c1 with dissolve
        pause
        scene sm1mv01s03_2-72 sy-gives-look-hmmm_c1 with dissolve
        play voice3 stacy_hmm noloop
        sy "Hmmm."
    scene sm1mv01s03_2-73 sy-starts-reading-script-lets-go-movie-by-act-one_c1 with dissolve
    play voice3 stacy_thinking_emm4 noloop
    if persistent.is_special:
        sy "Let's go. Curse of the Pirate Queen, by [mcname] and Stacy Young."
    else:
        sy "Let's go. Curse of the Pirate Queen, by [mcname] Young and Stacy Brawn."
    sy "Act one. Scene one.{w} Interior, Captain Dickhart's cabin."
    scene sm1mv01s03_2-74 sy-again-again-mc-bummed-again_c1 with fade
    play voice3 stacy_angryhuh noloop
    sy "Again. Say it again."
    play voice2 mc_surprised_uh3 noloop
    mc "Again?"
    scene sm1mv01s03_2-75 sy-just-know-can-do-better-mc-says-line_c1 with dissolve
    play voice3 stacy_disappointed_ehh2 noloop
    sy "I just... I know you can do it better, [mcname]."
    play voice2 d14s16_smell noloop
    mc "Alright. *deep breath*"
    play voice2 mc_arrogant_huh2 noloop
    mc "Kill me and you'll never make it off this ship."
    scene sm1mv01s03_2-76 sy-looks-at-tl-she-reads-lines_c1 with dissolve
    pause
    scene sm1mv01s03_2-77 tl-killing-you-not-what-want-tl-want-pirate-queen_c1 with dissolve
    play sound sfx_paper_slide1
    pause
    scene sm1mv01s03_2-78 tl-least-steal-traesure-mc-cap-roy_c1 with dissolve
    play voice4 girl24_no_simple2 noloop
    tl "Killing you is not what I want."
    tl "I want the Pirate Queen."
    tl "Or to at least steal the treasure right out from under her."
    play voice2 mc_hey_hey3 noloop
    mc "Captain Roy of the {i}Succession{/i} and twenty hands died looking for that treasure."
    scene sm1mv01s03_2-79 tl-good-thing-not-plan-die-mc-long-exchanging-plans_c1 with dissolve
    play voice4 girl24_arrogant_huh2 noloop
    tl "Then it's a good thing I don't plan to die, Captain Dickhart."
    scene sm1mv01s03_2-80 mc-perhaps-there-one-can-make-together-tl-listening_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Hmph. So long as we're... exchanging plans."
    mc "Perhaps there is one we can make... together."
    play voice4 girl24_thinking_hmm4 noloop
    tl "I'm listening."
    play sound sfx_throw_something1
    scene sm1mv01s03_2-81 kv-sy-clapping-kv-not-bad-sy-nice_c1 with dissolve
    play voice3 stacy_happy_wooh1 noloop
    play voice5 kanya_happy_yeah noloop
    sy "And scene."
    "Stacy and Kanya" "Cheering."
    kv "Not bad."
    sy "Nice."
    if player.get_choice("sm1mv01s03_2_tl_beer"):
        play sound sfx_glass_bottle_bonk
        scene sm1mv01s03_2-82 tl-see-beer-makes-better_c1 with dissolve
        play voice4 girl24_arrogant_hm3 noloop
        tl "See. Beer makes everything better."
        scene sm1mv01s03_2-83 kv-rolls-eyes_c1 with dissolve
        play voice5 kanya_disappointed_hm noloop
        pause
        play sound sfx_bottle_clink1
        scene sm1mv01s03_2-84 tl-mc-cheers-with-beers_c1 with dissolve
        pause
        play sound [sfx_drink_gulp, sfx_drink_gulp]
        scene sm1mv01s03_2-85 tl-mc-sipping-beer_c1 with dissolve
        pause
        scene sm1mv01s03_2-86 mc-done-sipping-aaaah_c1 with dissolve
        play voice2 d1s5b_ehhh noloop volume 1.6
        mc "Ahhh."
    else:
        scene sm1mv01s03_2-87 tl-raises-beer-nice-work-captain-mc-nods-just-followed-lead_c1 with dissolve
        play voice4 girl24_hey_sexy noloop
        tl "Nice work, Captain."
        play voice2 mc_yes_yes7 noloop
        mc "I just followed your lead, Captain."
        scene sm1mv01s03_2-88 tl-grinning-silently_c1 with dissolve
        play voice4 girl24_arrogant_hm3 noloop
        pause
    play sound sfx_throw_something1
    scene sm1mv01s03_2-89 mc-asking-next-scene-tl-aye-aye-captain_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Next scene?"
    play voice4 girl24_yes_happy noloop
    tl "Aye aye, Captain Dickhard."
    scene sm1mv01s03_2-90 mc-corrects-tl-dickhart-tl-haha_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Dickhart."
    play voice4 girl24_happy_laugh2 noloop
    tl "Haha."
    jump sm1mv01s03_2_later_on
label sm1mv01s03_2_later_on:
    scene black
    show screen scene_transistion(_("Later on"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene sm1mv01s03_2-91 later-mc-reading-scene-rather-die-give-in-aye-so-would-crew_c1
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_angry_errr2 noloop
    mc "I'd rather die than give in to you."
    mc "Aye, so would my whole crew."
    scene sm1mv01s03_2-92 tl-would-not-mc-what_c1 with dissolve
    play voice4 girl24_no_nonono1 noloop
    tl "I would not."
    play voice2 mc_surprised_what3 noloop
    mc "What?"
    play sound sfx_paper_rustl3
    scene sm1mv01s03_2-93 tl-just-saying-with-him_c1 with dissolve
    play voice4 girl24_arrogant_hm2 noloop
    tl "I'm just saying, I'm not really..."
    tl "{i}With{/i} him."
    scene sm1mv01s03_2-94 sy-haha-friends-like-this-good-see-finally-turned-woman_c1 with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "Haha. With friends like these, eh Dickhart?"
    sy "It's good to see you finally be turned aside by a woman."
    scene sm1mv01s03_2-95 sy-must-be-new-you_c1 with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "Must be {i}new{/i} for you."
    scene sm1mv01s03_2-96 sy-turns-towards-tl-now-mean-join-me-tl-oh-no_c1 with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "Now, you mean to join {i}my{/i} crew then, Miss Searose?"
    play voice4 girl24_no_long noloop
    tl "Oh no, I'd rather sleep with First Mate Bob."
    play sound sfx_paper_rustl2
    play sound2 sfx_throw_something1 noloop
    scene sm1mv01s03_2-97 sy-frowns-he-too-good-take-away_c1 with dissolve
    play voice3 stacy_angry_aah1 noloop
    sy "He's too good for a blackheart like you, wench!"
    sy "Take them away!"
    scene sm1mv01s03_2-98 kv-reading-captain-lyra-dragged-off-and-scene_c1 with dissolve
    play voice5 kanya_yes_yeah1 noloop
    kv "Captain Dickhart and Scarlet Searose are dragged off to be imprisoned."
    kv "And that's the scene."
    scene sm1mv01s03_2-99 mc-relieved-phew-kv-nice-work-everyone_c1 with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "Phew."
    play voice5 kanya_happy_relief2 noloop
    kv "Nice work, everyone."
    scene sm1mv01s03_2-100 mc-yeah-not-bad_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. Not bad."
    scene sm1mv01s03_2-101 tl-checking-script-decent-script-even-got-chuckle-me_c1 with dissolve
    play voice4 girl24_arrogant_yeah3 noloop
    tl "Yeah. Decent script."
    play sound sfx_paper_rustl1
    scene sm1mv01s03_2-102 tl-horny-looking-mc-excited-what-do-sets-mc-heh_c1 with dissolve
    play voice4 girl24_arrogant_hah noloop
    tl "Even got a couple chuckles out of me."
    tl "Excited to see what we can do with those sets too."
    scene sm1mv01s03_2-103 mc-good-think-enough-getting-late_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Heh."
    mc "Good. I think that's it for today. It's getting late."
    if player.has_played_scene("sm1mv01s02"):
        scene sm1mv01s03_2-104 kv-not-quite-done-sy-huh_c1 with dissolve
        play voice5 kanya_hey_arrogant noloop
        kv "We're not {b}quite{/b} done, [mcname]."
        play voice3 stacy_arrogant_huh2 noloop
        sy "Huh?"
        scene sm1mv01s03_2-105 kv-point-tl-we-still-need-see-star-costume-mc-oh-shit-forgot_c1 with dissolve
        play voice5 kanya_thinking_eeh5 noloop
        kv "We still need to see how our star looks in her costume."
        play voice2 mc_surprised_oh2 noloop
        mc "Oh shit. Good thinking."
        play sound sfx_barefoot_run1
        scene sm1mv01s03_2-106 sy-running-away-will-get-it_c1 with dissolve
        play voice3 stacy_yes_fine3 noloop
        sy "I'll go get it."
        stop sound fadeout 1.0
        call sm1mv01s03_2_tl_costume from _call_sm1mv01s03_2_tl_costume_1
    else:
        play sound sfx_paper_rustl3
        scene sm1mv01s03_2-100 mc-yeah-not-bad_c1 with dissolve
        play voice2 mc_thinking_hmm4 noloop
        mc "Now that we've got the script done, we need to get Taisia's costume."
        mc "And all the other ones, now that I think of it."
        scene sm1mv01s03_2-104 kv-not-quite-done-sy-huh_c1 with dissolve
        play voice3 stacy_yes_yap3 noloop
        sy "Yup. We should make that our top priority."
        play voice5 kanya_yes_yeah2 noloop
        kv "Agreed."
    jump sm1mv01s03_2_end
label sm1mv01s03_2_end:
    stop sound fadeout 2.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    if player.has_played_scene("sm1mv01s02"):
        $ StoryController.end_scene_without_storyline("sm1mv01s03_2", 6, 0, 4, STUDIO, DEFAULT_SUBLOCATION, SD_UPSTAIRS_2)
    else:
        $ StoryController.end_scene_without_storyline("sm1mv01s03_2", 4, 0, 3, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1mv01s03_2_tl_costume:
    $ player.set_choice("sm1mv01s03_2_tl_costume")
    play sound sfx_photocamera_zoom2
    scene sm1mv01s03_2-107 later-kv-clicking-tl-on-backdrop_c1 with Fade(0.5, 0.5, 0.5)
    play voice5 kanya_happy_yay noloop
    kv "Very nice."
    scene sm1mv01s03_2-108 click-tl-picture_c1 with dissolve
    play voice4 girl24_arrogant_hm1 noloop
    tl "Shit looks classy as hell."
    play sound sfx_photocamera_flash2
    "Click"
    scene sm1mv01s03_2-109 tl-frowns-wish-had-swords-feel-goofy-no-cutlass_c1 with dissolve
    play voice4 girl24_disappointed_neh noloop
    tl "I wish you guys already had swords."
    tl "I feel goofy without a cutlass."
    play sound sfx_photocamera_flash2 loop
    scene sm1mv01s03_2-110 mc-gives-shower-brush-use-this-tl-for-real_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Here you go. We used these to pretend."
    play sound sfx_cloth_rustling2
    scene sm1mv01s03_2-111 tl-not-greatly-impressed-thanks_c1 with dissolve
    play voice4 girl24_disappointed_oof noloop
    tl "Really?"
    tl "Thanks."
    scene sm1mv01s03_2-112 mc-derping-got-it_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "You got it."
    scene sm1mv01s03_2-113 kv-looking-camera-one-for-road_c1 with dissolve
    play voice5 kanya_thinking_hmm4 noloop
    kv "Okay, and one more for the road."
    scene sm1mv01s03_2-114 camera-click-tl-does-next-pose_c1 with dissolve
    play sound sfx_photocamera_flash2
    "Click"
    scene sm1mv01s03_2-115 kv-looking-photos-gotit-great-will-check-photoshopping_c1 with dissolve
    play sound sfx_remote_button1
    play voice5 kanya_yes_yep2 noloop
    kv "Got it."
    kv "Great. I'll check it for any photoshopping that we need."
    scene sm1mv01s03_2-116 tl-mc-surprised-photoshopping_c1 with dissolve
    play voice4 girl24_surprised_huh3 noloop
    tl "Photoshoppping?"
    scene sm1mv01s03_2-117 kv-replying-say-any-tweaking-stacy-said-could-do-little-sewing_c1 with dissolve
    play voice5 kanya_yes_yeah3 noloop
    kv "I said any tweaking."
    kv "Stacy said she could do a little sewing on your outfit if we needed it."
    scene sm1mv01s03_2-118 mc-riiight_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Right."
    scene sm1mv01s03_2-119 kw-yawns_c1 with dissolve
    play voice5 kanya_sex_closedmoan3 noloop
    pause
    play sound sfx_cloth_rustling1
    scene sm1mv01s03_2-120 kv-checks-phone-really-late-gotta-get-going_c1 with dissolve
    play voice5 kanya_disappointed_oof noloop
    kv "It {b}really{/b} is late."
    kv "I gotta get going."
    scene sm1mv01s03_2-121 kv-prepares-leave-text-once-schedule-mc-you-first-list_c1 with dissolve
    play voice5 kanya_hey_simple1 noloop
    kv "Text me once we have a scheduled figured out."
    play voice2 mc_yes_okay3 noloop
    mc "You're the first on my list."
    play sound sfx_cloth_rustling4
    scene sm1mv01s03_2-122 mc-kv-hug-kv-great_c1 with dissolve
    play voice5 kanya_happy_relief3 noloop
    kv "Great."
    play sound sfx_heels_steps2 loop
    scene sm1mv01s03_2-123 kv-leaves-waves-nice-work-film-will-rule_c1 with dissolve
    play voice5 kanya_yes_aga1 noloop
    kv "Nice work, everyone. This film is going to rule."
    scene sm1mv01s03_2-124 tl-sy-say-goodbye-kv_c1 with dissolve
    play voice4 girl24_hey_bye1 noloop
    tl "Later Kanya."
    play voice3 stacy_hey_byebye noloop
    sy "Bye."
    play sound2 sfx_heels_steps1
    play sound3 sfx_door_closed1 noloop
    scene sm1mv01s03_2-125 sy-goes-towards-computer-mc-tl-follow_c1 with dissolve
    pause
    play sound sfx_chair_slide1
    play sound2 sfx_keyboard_typing2
    scene sm1mv01s03_2-126 sy-sitting-laptop-another-things-checklist-mc-what-next_c1 with dissolve
    play voice3 stacy_yes_fine4 noloop
    sy "And another few things are off the checklist."
    play voice2 mc_thinking_hm noloop
    mc "What's next?"
    play sound2 sfx_cloth_rustling1 noloop
    scene sm1mv01s03_2-127 sy-we-build-ship-mc-every-boy-dream_c1 with dissolve
    play voice3 stacy_thinking_oh1 noloop
    sy "We get to build a pirate ship in our home."
    play voice2 mc_surprised_ohmy noloop
    mc "My god, it's every boy's dream."
    scene sm1mv01s03_2-128 tl-butts-in-girls-like-pirates-too-orlando-bloom-hot_c1 with dissolve
    play voice4 girl24_hey_angry noloop
    tl "Girls can like pirates too, [mcname]."
    tl "Orlando Bloom still looks fucking hot."
    scene sm1mv01s03_2-129 sy-lusty-nod-mc-not-happy_c1 with dissolve
    play voice3 stacy_moan4 noloop
    pause
    scene sm1mv01s03_2-130 mc-focuses-so-next-up-sets_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "So next up is the sets."
    play sound sfx_throw_something1
    play sound2 sfx_heels_steps1
    scene sm1mv01s03_2-131 tl-yeah-let-know-when-start-got-little-experience_c1 with dissolve
    play voice4 girl24_yes_yeah noloop
    tl "Yeah, let me know when you want to start on that."
    tl "I've got a little experience fixing things up."
    play sound2 sfx_bed_fall1 noloop
    scene sm1mv01s03_2-132 mc-where-get-decent-looking-swords-tl-hmmm_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    mc "Yeah, and then we gotta figure out where to find some decent-looking pirate swords."
    play voice4 girl24_thinking_hmm1 noloop
    tl "Hmmm."
    scene sm1mv01s03_2-133 sy-stetches-cant-wait-see-what-come-up-also-have-finish-writing_c1 with dissolve
    play voice3 stacy_disappointed_moan1 noloop
    sy "I can't wait to see what we come up with for the set."
    sy "But we also have to finish the writing one day."
    scene sm1mv01s03_2-134 mc-ofc-add-list-hope-writers-block-gone_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Course. Just add it to the list."
    mc "Hopefully this writer's block fades quickly."
    scene sm1mv01s03_2-135 tl-shrugging-maybe-all-need-night-sleep-got-faith_c1 with dissolve
    play voice4 girl24_thinking_hmm2 noloop
    tl "Maybe all you need is a good night's sleep, and it will come to you."
    tl "I got faith, [mcname]."
    scene sm1mv01s03_2-136 mc-thanks-tl_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thanks, Taisia."
    play sound sfx_heels_steps1 loop
    scene sm1mv01s03_2-137 tl-heads-towards-her-room_c1 with dissolve
    play voice4 girl24_hey_bye2 noloop
    tl "Catch you later."
    play sound sfx_door_closed4
    scene sm1mv01s03_2-138 mc-sy-hear-door-closing_c1 with dissolve
    "*door closing*"
    play sound sfx_cloth_rustling3
    scene sm1mv01s03_2-139 mc-checking-stacy-mc-something-wrong_c1 with dissolve
    mc "..."
    play voice2 mc_thinking_hmm5 noloop
    mc "Something wrong?"
    scene sm1mv01s03_2-140 sy-really-want-get-movie-right-did-some-research_c1 with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "I just really want to get this movie done right."
    sy "I did some research, people online say that all pirate movies are kind of cursed."
    play sound sfx_barefoot_steps1
    scene sm1mv01s03_2-141 mc-surprised-what-come-on_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What? Come on."
    play sound sfx_cloth_rustling4
    scene sm1mv01s03_2-142 mc-serious-it-true-one-bankrupted-studio_c1 with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "It's true. One ended up being so bloated and disastrously run that by the end, it bankrupted a whole studio."
    scene sm1mv01s03_2-143 well-this-big-studio-operation-small_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Well that was a big ass studio."
    mc "Our operation is tight and small."
    mc "Heh heh."
    scene sm1mv01s03_2-145 even-after-filming-need-thinking-promote_c1 with dissolve
    play voice3 stacy_yeahno noloop
    sy "Good point. But man, this is a lot of work. I mean, we're barely through the writing."
    play sound sfx_cloth_rustling5
    scene sm1mv01s03_2-146 mc-sure-going-be-fine-at-least-adventure_c1 with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "And even after we do all the filming and editing, we have to think about how we are going to promote and market this monster."
    scene sm1mv01s03_2-147 mc-one-hundred-percent_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I'm sure it's going to work out fine."
    play voice3 stacy_yes_yeah2 noloop
    sy "At the very least, it's going to be an adventure."
    play sound sfx_cloth_planket2
    scene sm1mv01s03_2-148 mc-think-going-bed_c1 with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "One hundred percent."
    mc "I think I'm going to get ready for bed."
    scene sm1mv01s03_2-149 sy-smiles-see-you-there_c1 with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "See you there."
    play sound sfx_heels_steps2 loop
    scene sm1mv01s03_2-150 mc-goes-bed-end-scene_c1 with dissolve
    pause
    stop sound fadeout 2.0
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    return