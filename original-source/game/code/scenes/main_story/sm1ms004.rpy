image sm1ms004-glambot-1 = Movie(play = "images/ms/s004/anim/sm1ms004-a17-2x-50fps.webm", start_image = "sm1ms004-a17 mc-shows-above-kitchen-arj-ask-ideas-glambot-17-00_i", image = "sm1ms004-a17 mc-shows-above-kitchen-arj-ask-ideas-glambot-17-89_i", loop = False)
image sm1ms004-glambot-2 = Movie(play = "images/ms/s004/anim/sm1ms004-a19-2x-50fps.webm", start_image = "sm1ms004-a19 mc-shows-arj-couch-area-glambot-19-000_i", image = "sm1ms004-a19 mc-shows-arj-couch-area-glambot-19-119_i", loop = False)
image sm1ms004-glambot-3 = Movie(play = "images/ms/s004/anim/sm1ms004-a42-3x-60fps.webm", start_image = "sm1ms004-a42 glambot-000", image = "sm1ms004-a42 glambot-108", loop = False)
label sm1ms004:
    play sound sfx_door_closed2
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    scene sm1ms004-01 mc-enters-studio_c1 with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Hey Stacy - I did it!"
    play music "<silence 1.4>" noloop
    scene sm1ms004-03 arj-tells-mc-sy-not-here-mc-good-see-you_c1 with dissolve
    $ renpy.music.set_volume(1.0, 1.0, "music" )
    queue music saxophone_sexy2
    play voice3 amrose_no_uhuh noloop
    arj "She's not here."
    scene sm1ms004-02 mc-sees-arj-sitting-table_c1 with dissolve
    play voice2 mc_surprised_huh3 noloop
    mc "AmRose! Great to see you!"
    mc "I wasn't expecting to see you here."
    scene sm1ms004-04 mc-not-expecting-unsure-ask-sy-let-arj-in_c1 with dissolve
    mct "Why do I feel like I walked into a lion's den?"
    play voice2 mc_thinking_mmm4 noloop
    mc "Did Stacy let you in?"
    scene sm1ms004-05 arj-let-herself-mc-tells-both-been-busy_c1 with dissolve
    play voice3 amrose_arrogant_hmm1 noloop
    arj "I let myself in...{w} Stacy invited me here, then didn't show."
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, well, she's been busy. We both have."
    scene sm1ms004-06 arj-enjoying-summer-work-mc-believes-her-she-was-ironic_c1 with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "Sure. Meanwhile I've just been enjoying my summer break."
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah? Do anything fun?"
    play voice3 amrose_no_angry1 noloop
    arj "No. I work all summer so I don't have to during the semesters."
    scene sm1ms004-07 mc-makes-sense-arj-has-two-jobs_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Oh, that makes sense. What do you do again?"
    play voice3 amrose_no_nah noloop
    arj "I have two jobs. Don't worry about it."
    mc "Heh, well, at least you don't have to worry about Fetish Locator anymore."
    scene sm1ms004-08 mc-uncomfortable-akward_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "That app distracted us both quite a bit last semester..."
    mc "Ate up a lot of our free time, I mean."
    play sound sfx_cloth_rustling1
    scene sm1ms004-09 arj-holding-drive-sass-about-data-safety_c1 with dissolve
    play voice3 amrose_disappointed_ah noloop
    arj "At least I can see you're keeping the data secure.{w} [mcname], there isn't even a lock on the door."
    play voice2 mc_hey_hey3 noloop
    mc "There's a lock. In fact, there are two of them."
    arj "Then why was I able to just walk right in here?"
    scene sm1ms004-10 mc-defensive-locks-broken_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Well, they're all broken. Stacy is probably out buying replacements now."
    play voice3 amrose_arrogant_yeah2 noloop
    arj "Yeah, and how long until they're broken?"
    play sound sfx_throw_something1
    play voice3 amrose_angry_argh1 noloop
    play sound3 ["<silence 0.3>", sfx_phone_fall1] volume 0.4 noloop
    scene sm1ms004-11 arj-throws-usb-drive_c1 with dissolve
    pause
    scene sm1ms004-12 arj-whatever-hopes-mc-deleted-everything_c1 with dissolve
    play voice3 amrose_angry_ergh noloop
    arj "Nevermind. It doesn't matter."
    arj "I just hope you deleted everything I did for that damnable app."
    play voice2 mc_no_no4 noloop
    mc "We never even copied that. Stacy even destroyed that drive from the server room."
    scene sm1ms004-13 arj-looking-drive-ask-how-know-mc-explains-username_c1 with dissolve
    play voice3 amrose_arrogant_huh3 noloop
    arj "She must have seen it, though. How else could she have known what to delete?"
    play voice2 mc_thinking_emm1 noloop
    mc "We all knew your username. It was probably that easy."
    arj "Sure, I guess."
    play sound sfx_bed_slide2 volume 0.5
    scene sm1ms004-14 arj-stands-up-chair-acting-asshole_c1 with dissolve
    play voice3 amrose_angry_ehh noloop
    arj "Anyway. Why don't you show me around your shithole so I can get out of here?"
    play voice2 mc_surprised_what3 noloop
    mc "Shithole?! My home, this is!"
    mc "Fine. Let me show you around."
    scene sm1ms004-15 mc-shows-kitchen-arj-obvs-mc-viable-for-porn_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Over here is the kitchen."
    play voice3 amrose_yes_confident2 noloop
    arj "Obviously."
    mc "It's a kitchen, but we plan to fix it up a bit to make it viable for porn shoots."
    scene sm1ms004-16 arj-kinky-mc-agrees_c1 with dissolve
    play voice3 amrose_thinking_hmm5 noloop
    arj "Kinky. Food fetish?"
    play voice2 d9s2_yeah noloop volume 2.5
    mc "Maybe."
    play sound sfx_camera_fly1 volume 2.5
    scene sm1ms004-glambot-1 with dissolve
    pause
    play voice2 mc_thinking_hmm4 noloop
    mc "Above the Kitchen there's a nice area for something. We haven't quite decided what to do with it."
    play voice3 amrose_arrogant_huh1 noloop
    arj "What are your ideas?"
    mc "Stacy wants to put my bedroom up there, so women can fuck me reverse cowgirl and look out on the whole place, but..."
    stop sound fadeout 1.0
    scene sm1ms004-17-01 mc-shows-above-kitchen-wide-shot_c1 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "That sounds dangerous. I don't think it would hold all that weight and motion."
    scene sm1ms004-18 mc-tells-sy-wants-bedroom-arj-dangerous_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. I'd go to bed every night thinking I might fall all the way down."
    scene sm1ms004-a19 mc-shows-arj-couch-area-glambot-19-000_i with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Obviously, that's where our couch and TV are. We plan to fix that up a little bit, but..."
    play sound sfx_camera_fly1 volume 1.7
    play sound3 ["<silence 1.5>", sfx_camera_fly1] noloop volume 1.7
    scene sm1ms004-glambot-2
    pause
    play voice3 amrose_thinking_hmm1 noloop
    arj "Casting couch?"
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1ms004-19-01 mc-shows-arj-couch-area-wide-shot_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Pretty much. Also we could watch TV... if we pay for cable or whatever."
    scene sm1ms004-20 mc-shows-arj-matress_c1 with dissolve
    play voice3 amrose_thinking_oh2 noloop
    arj "It looks like you have a wonderful open concept bedroom over there."
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, thanks. It's shared. We're working on it."
    scene sm1ms004-20-01 mc-shows-arj-matress-wide-shot_c1 with dissolve
    play voice3 amrose_disappointed_ehh2 noloop
    arj "I guess everyone has to start from somewhere."
    scene sm1ms004-21 mc-shows-arj-future-staircase_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "This will be the main staircase, leading up to the upstairs rooms."
    play voice3 amrose_arrogant_huh4 noloop
    arj "How many rooms are up there?"
    scene sm1ms004-21-01 mc-shows-arj-future-staircase-wide-shot_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I forgot to count.{w} More than we'll need."
    scene sm1ms004-22 mc-thinks-thats-it-arj-where-refresher_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "I guess that's pretty much everything."
    play voice3 amrose_happy_mmm noloop
    arj "I think you missed something very important. Where's the refresher?"
    scene sm1ms004-23 mc-jokes-bucket-corner-arj-shocked_c1 with dissolve
    play voice2 mc_scared_oh2 noloop
    mc "Oh, there's a bucket over there in the corner."
    play voice3 amrose_surprised_what noloop
    arj "What?!"
    scene sm1ms004-24 mc-shows-bathroom-arj-goes-use-bathroom_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "No, of course not. It's through that door over there."
    play voice3 amrose_happy_phew2 noloop
    arj "Oh, good. Do you mind if I..."
    play voice2 mc_yes_sure1 noloop
    mc "Oh, sure. Go ahead."
    scene sm1ms004-25 mc-arj-together-mc-ask-what-think-arj-thinks-building-condemned_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "So, what do you think?"
    play voice3 amrose_disappointed_oh3 noloop
    arj "I think this building should be condemned. There's serious metal fatigue in all the load-bearing members, the wiring is substandard..."
    play voice2 mc_arrogant_heh3 noloop
    mc "(deadpan) Ha, ha. That's so funny I forgot to laugh."
    scene sm1ms004-26 mc-forgot-laugh-arj-want-joking_c1 with dissolve
    play voice3 amrose_hey_active1 noloop
    arj "I wasn't kidding. You shouldn't be living here. You shouldn't be working here. This place should be demolished immediately."
    play voice2 mc_yes_aga1 noloop
    mc "Well, I guess that ends the tour."
    mct "You probably want to sugarcoat that if you tell Stacy. She's very optimistic about all this and I don't want her to lose that."
    scene sm1ms004-27 arj-arms-folded-thinks-both-crazy_c1 with dissolve
    play voice3 amrose_surprised_uh2 noloop
    arj "You're both nuts. This is all crazy, [mcname]."
    scene sm1ms004-28 mc-confident_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I know, but it seems to work for me."
    mc "If I stopped doing things just because they seem a little crazy, Fetish Locator would still be manipulating people."
    scene sm1ms004-29 arj-looks-towards-door-feels-gotta-get-going_c1 with dissolve
    play voice3 amrose_disappointed_ehh1 noloop
    arj "Well I've taken up enough of your time."
    scene sm1ms004-30 mc-arj-next-entrance-door_c1 with dissolve
    pause
    scene sm1ms004-31 mc-great-seeing-arj-sure-was_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "It was great seeing you again."
    play voice3 amrose_yes_yeah3 noloop
    arj "Yeah, right. I'm sure it was."
    scene sm1ms004-32 mc-serious-liked-seeing-arj-even-jerk_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "No, seriously. I mean, you've been a bit of a jerk, but I'm really glad to see you again."
    play voice3 amrose_surprised_huh2 noloop
    arj "I'm not-"
    scene sm1ms004-33 arj-disarmed-tells-mc-save-suave-charm_c1 with dissolve
    play voice3 amrose_disappointed_pff noloop
    arj "Look, you can save the suave charm."
    play voice2 mc_surprised_what2 noloop
    mc "What does that mean?"
    arj "Let me spell it out for you. You and Stacy were the best thing that ever happened to me. You were the love of my life. Stacy was the sister I never had."
    scene sm1ms004-34 arj-looks-mc-sad-betrayed-mc-insist-all-did-keep-data_c1 with dissolve
    play voice3 amrose_disappointed_oh5 noloop
    arj "Then you both betrayed me. You did something unthinkable."
    play voice2 mc_thinking_mmm3 noloop
    mc "All we did is keep some of the data."
    scene sm1ms004-35 arj-tells-mc-betrayed-her-mc-thought-in-love-lc_c1 with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "All you did was betray me. Do you have any idea what that's like?"
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, I do.{w} I thought I was in love with Lydia, but she-"
    scene sm1ms004-36 arj-angry-mc-jerked-her-around_c1 with dissolve
    play voice3 amrose_yes_confident1 noloop
    arj "Exactly! Even then you were jerking me around as second or third best!"
    arj "And then you both just tossed me aside."
    scene sm1ms004-37 mc-insist-her-choice-avoiding-them_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "We didn't. It was your choice to avoid us."
    play voice3 amrose_yes_ugu noloop
    arj "And then you disappear without a trace. You were both supposed to be at the apartment this summer, but instead you came here!"
    scene sm1ms004-38 mc-reminds-arj-never-called-things-not-for-phone_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "We still had the same phone numbers. We didn't try to-"
    play voice3 amrose_angry_breath1 noloop
    arj "Whatever.{w} There are some things that just can't be done over the phone."
    scene sm1ms004-39 mc-dirty-look-arj-not-what-she-meant_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "You mean like that time when I was on the phone with Lydia and you-"
    play voice3 amrose_angry_ergh noloop
    arj "(sigh) You know that isn't what I meant."
    scene sm1ms004-40 arj-less-angry-still-not-fucking-mc-today_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I know, but it was effective. You aren't as angry as you were a minute ago."
    play voice3 amrose_happy_laugh1 noloop
    arj "Yeah, well.{w}.. I'm still not fucking you today."
    play voice2 mc_yes_yeah8 noloop
    mc "Just today?"
    scene sm1ms004-41 arj-mc-smile-each-other_c1 with dissolve
    play voice3 amrose_angry_errr noloop
    arj "You're tenacious, I'll give you that..."
    play voice2 d2s9_confused noloop volume 2.2
    mc "Either way, it is good to see you. I hope I can see you again soon."
    arj "Well, now I know where you live."
    play sound sfx_camera_fly1 volume 1.7
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound3 ["<silence 2.5>", sfx_camera_fly1] noloop volume 1.7
    scene sm1ms004-glambot-3 with dissolve
    pause
    play voice2 d2s9_mchey noloop
    mc "Don't be a stranger. Our door is always open to you."
    play voice3 amrose_happy_laugh2 noloop
    arj "*chuckle* Your door is open to everyone.{w} Seriously, get that lock fixed."
    play voice2 mc_yes_sure1 noloop
    mc "I will."
    $ renpy.music.set_volume(0.0, 0.0, "freeroam_music1" )
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1ms004-43 arj-about-leave-both-dont-want-leave_c1 with dissolve
    play voice3 amrose_happy_mmm noloop
    arj "Well. See ya'."
    play voice2 mc_arrogant_hm1 noloop
    mc "See you soon?"
    arj "We'll see."
    play sound sfx_door_openclosed1
    scene sm1ms004-44 mc-thinking-after-arj-leaves_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "That was interesting.{w} I feel good - like AmRose is coming back around to liking us."
    mct "Maybe this isn't completely fucked afterall."
    scene sm1ms004-45 usb-missing-scene-end_c1 with dissolve
    mct "Still, I can't help feeling like I missed something really important."
    call sm1ms004_get_arj_points from _call_sm1ms004_get_arj_points
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ StoryController.end_scene(MS)
    return
label sm1ms004_get_arj_points:
    $ CharacterController.get_character("arj").add_point()
    $ player.set_choice("sm1ms004_got_arj_points")
    return
label sm1ms004_unlocks:
    call sm1ms004_get_arj_points from _call_sm1ms004_get_arj_points_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MS)
    return