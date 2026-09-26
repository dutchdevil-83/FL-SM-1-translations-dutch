image sm1cs_my003-glambot-1 = Movie(play = "images/Character-Scenes/MY/s003/anim/sm1cs-my003-a09-2x-RIFE4.26-50fps.webm", start_image = "sm1cs-my003-a09 my-standing-gym-clothes-glambot-00_i", image = "sm1cs-my003-a09 my-standing-gym-clothes-glambot-89_i", loop = False)
label sm1cs_my003:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1cs-my003-01 mc-sy-walking-towards-kitchen with dissolve
    play music music_relaxed_thoughts
    pause
    scene sm1cs-my003-02 mc-be-nice-knowing-where-bring-my with dissolve
    play voice2 mc_thinking_hmm1 noloop
    if persistent.is_special:
        mc "Well, it would just be nice to know what I'm bringing Mom to."
    else:
        mc "It would just be nice to know what I'm bringing Melony to."
    scene sm1cs-my003-03 sy-you-prolly-chicken-mc-nuh-huh with dissolve
    play voice3 stacy_yeahno noloop
    sy "But, you probably would have chickened out."
    play voice2 mc_no_uhuh1 noloop
    mc "Nuh uh."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-my003-04 sy-yeah-huh with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "Yeah huh."
    scene sm1cs-my003-05 knock-on-door with dissolve
    call knock from _call_knock_7
    scene sm1cs-my003-06 mc-sy-looking-door-sy-how-that-be-mc-got-it with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "Now who the hell could that be?"
    play voice2 mc_thinking_hmm2 noloop
    mc "I got it."
    play sound sfx_heels_steps2 loop
    scene sm1cs-my003-07 mc-goes-towards-door with dissolve
    pause
    play sound sfx_door_open1
    scene sm1cs-my003-08 mc-opens-door with dissolve
    pause
    scene sm1cs-my003-a09 my-standing-gym-clothes-glambot-00_i with dissolve
    pause 0.01
    play sound sfx_camera_fly1 volume 2.0
    scene sm1cs_my003-glambot-1
    pause
    scene sm1cs-my003-10 mc-oh-hey-sy-her-ears-must-burn with dissolve
    play voice2 mc_surprised_oh3 noloop
    if persistent.is_special:
        mc "Oh, hey Mom!"
    else:
        mc "Oh, hey Melony!"
    play voice4 stacy_hmm noloop
    sy "{size=*0.6}Her ears must have been burning.{/size}"
    play sound sfx_door_closed1
    play sound2 sfx_heels_steps2
    scene sm1cs-my003-11 my-enters-he-mc-stacy with dissolve
    play voice3 girl34_hey_hi1 noloop
    my "Hi, [mcname]! Stacy!"
    stop sound2 fadeout 1.0
    scene sm1cs-my003-12 mc-look-like-going-run-my-trying-climbing-gym with dissolve
    play voice2 d1s5_mchappy noloop volume 1.4
    mc "You look like you were out for a run or something."
    play voice3 girl34_thinking_hmm7 noloop
    my "I'm actually on my way to try out this bouldering gym."
    scene sm1cs-my003-13 sy-asking-you-climb with dissolve
    play voice4 stacy_huh2 noloop
    sy "You climb?"
    scene sm1cs-my003-14 my-so-shocking-have-hobbies-sy-no-guess-not-know-climbing with dissolve
    play voice3 girl34_yes_questioning2 noloop
    if persistent.is_special:
        my "Is it so shocking that your Mom has hobbies?"
    else:
        my "Is it so shocking that I have hobbies?"
    play voice4 stacy_no_sad1 noloop
    sy "No, I guess... I just didn't think that one of your hobbies was bouldering."
    scene sm1cs-my003-15 my-well-had-find-something-do with dissolve
    play voice3 girl34_thinking_hmm2 noloop
    my "Well, while you and [mcname] have been busy with your lives, I've had to find something to do."
    play sound sfx_cloth_rustling3
    scene sm1cs-my003-16 my-turns-back-mc-besides-points-either-join-mc-go-gym-dont with dissolve
    play voice3 girl34_thinking_emm5 noloop
    my "But, that's besides the point. I found out there's a bouldering gym here in Crowning, and I was wondering if either of you wanted to join me?"
    play voice2 mc_thinking_emm1 noloop
    mc "To go to the gym? I don't-"
    scene sm1cs-my003-17 sy-have-million-errands-mc-just-saying-want-do-something with dissolve
    play voice4 stacy_no_nope1 noloop
    sy "I have a million errands to run today, but [mcname] was just saying that he wanted to do go out and do something!"
    scene sm1cs-my003-18 mc-irritated-stacyy with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Stacy-"
    scene sm1cs-my003-19 my-really-that-wonderful-mc-was-going-help-stacy with dissolve
    play voice3 girl34_surprised_huh1 noloop
    my "Really, [mcname]? Because it would be wonderful if you would join me!"
    play voice2 d2s9_confused noloop volume 1.4
    mc "I was going to help Stacy out with errands-"
    scene sm1cs-my003-20 sy-oh-got-it-you-go-climbing with dissolve
    play voice4 stacy_disappointed_oh7 noloop
    sy "Oh, I got it! You go bouldering!"
    scene sm1cs-my003-21 my-excited-amazing-mc-go-put-gym-clothes with dissolve
    play voice3 girl34_happy_yeah2 noloop
    my "Amazing! [mcname], go put on some gym clothes and let's go!"
    scene sm1cs-my003-22 mc-defeated-yeah-give-sec with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. Give me a second..."
    play sound sfx_heels_steps2 loop
    scene sm1cs-my003-23 mc-walks-towards-stairs-mct-damnit-stacy-last-thing-go-gym with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "Damnit Stacy... the last thing I want to do is go to the gym."
    scene sm1cs-my003-24 mct-least-another-excuse-hang-out-which-prolly-why-sy-voluntered with dissolve
    play voice2 d14s16_smell noloop
    if persistent.is_special:
        mct "But at least it's another excuse to hang out with Mom..."
    else:
        mct "But at least it's another excuse to hang out with Melony..."
    mct "Which is probably why Stacy volunteered me to go..."
    stop sound fadeout 1.0
    jump sm1cs_my003_at_gym
label sm1cs_my003_at_gym:
    stop music fadeout 2.0
    play sound5 sfx_bouldering_ambience fadein 1.5
    scene sm1cs-my003-25 mc-my-inside-boulder-gym with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(0.6, 2.5, "music" )
    queue music music_bouldering_goesbold
    play voice2 mc_angry_huh2 noloop
    mct "Oh man... this is going to be a workout..."
    scene sm1cs-my003-27 my-ask-you-excited-mc with dissolve
    play voice3 girl34_hey_happy noloop
    my "Are you excited, [mcname]!?"
    scene sm1cs-my003-28 mc-yeah-sure with dissolve
    play voice2 d2s12_emmm noloop
    mc "Erm... sure am."
    scene sm1cs-my003-29 my-have-ever-tried-climbing-mc-rock-climbing-no with dissolve
    play voice3 girl34_arrogant_huh3 noloop
    my "Have you ever tried bouldering before?"
    play voice2 mc_no_nah2 noloop
    mc "Like rock climbing? No. This will be a first for me."
    scene sm1cs-my003-30 my-not-tough-first-need-stretching with dissolve
    play voice3 girl34_thinking_hmm6 noloop
    my "It's not as tough as you think it is! I promise."
    play sound sfx_carpet_footsteps1 loop
    scene sm1cs-my003-31 mc-stretching-my-uh-huh_c1 with dissolve
    play voice3 girl34_arrogant_ha1 noloop
    my "But first, we need to do some stretching!"
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Stretching?"
    stop sound fadeout 1.0
    scene sm1cs-my003-32 my-important-stretch-mc-trust-you_c1 with dissolve
    play voice3 girl34_yes_aga6 noloop
    my "Uh huh!"
    my "It's important to stretch. You'll regret it if you don't, [mcname]."
    play voice2 mc_yes_ugu1 noloop
    mc "I trust you."
    scene sm1cs-my003-33 mc-stands-next-my-my-alright-just-try-dont-push-yourself_c1 with dissolve
    play voice3 girl34_happy_relief1 noloop
    my "All right, just try and do what I do, to the best of your abilities."
    my "But don't push yourself. You can absolutely overstretch yourself."
    scene sm1cs-my003-34 mc-looking-my-okay_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    if persistent.is_special:
        mc "Okay, Mom."
    else:
        mc "Okay, Melony."
    play sound sfx_cloth_rustling5
    scene sm1cs-my003-35 mc-copies-pose_c1 with dissolve
    pause
    scene sm1cs-my003-36 my-move-next-pose_c1 with dissolve
    play voice3 girl34_thinking_hmm4 noloop
    my "All right, so for our first pose..."
    play sound sfx_cloth_rustling5 volume 1.6
    scene sm1cs-my003-37 my-does-next-pose_c1 with dissolve
    pause
    scene sm1cs-my003-38 my-starting-easy-one-mct-shit-not-that-flexible_c1 with dissolve
    play voice3 girl34_happy_mmm1 noloop
    my "Starting off with an easy one, loosen up those lower back muscles."
    mct "Shit... I don't think I'm that flexible..."
    scene sm1cs-my003-39 mct-cant-let-my-think-not-keep-up_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    if persistent.is_special:
        mct "But I can't let Mom think I can't keep up..."
    else:
        mct "But I can't let Melony think I can't keep up..."
    scene sm1cs-my003-40 mct-tries-best-mct-oh-shit-my-how-does-feel_c1 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Oh shiiiiit... I'm stretching muscles I don't think are supposed to be streeeeeetched."
    scene sm1cs-my003-41 mc-good-so-good-my-hehe_c1 with dissolve
    play voice3 girl34_arrogant_hm2 noloop
    my "How's that feel, [mcname]?"
    play voice2 mc_pain_rrrr noloop
    mc "G-good. So, so g-gooood. Yeah."
    scene sm1cs-my003-42 mc-if-say-so-my-heheeh-think-time-next-pose_c1 with dissolve
    play voice3 girl34_happy_laugh1 noloop
    my "Hehe - trust me, it's good for you."
    play voice2 mc_disappointed_ah2 noloop
    mc "I-if you say so."
    mct "Is stretching how she keeps her boobs looking so good?"
    my "Hehehehe. Well, I think it's time for the next pose."
    scene sm1cs-my003-43 mct-jesus-there-more_c1 with dissolve
    play voice2 mc_scared_huuuh1 noloop
    mct "Jesus, there's more?"
    play sound sfx_cloth_rustling2
    scene sm1cs-my003-44 my-gets-next-pose-mct-how-in-hell-my_c1 with dissolve
    play voice2 mc_pain_mff3 noloop
    mct "How in the hell..."
    scene sm1cs-my003-45 my-come-on-not-that-hard-mc-you-say-so_c1 with dissolve
    play voice3 girl34_yes_aga2 noloop
    my "Come on, [mcname], you got this! I promise, it's not as hard as it looks."
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "If you say so..."
    scene sm1cs-my003-46 mct-holy-shit-my-how-you-doing-mc_c1 with dissolve
    play voice2 mc_pain_ffff noloop
    mct "Holy shhhhhhhhhit... owowowowowowow."
    play voice3 girl34_disappointed_huh noloop
    my "How you doing, [mcname]?"
    mc "O-oh, I'm s-so, so... mmmm. Mmmhmmm. Stretched."
    scene sm1cs-my003-47 mc-so-stretched-my-hehee-really-need-stretching-more_c1 with dissolve
    play voice3 girl34_happy_laugh11 noloop
    my "Hehehehehehe. You really need to start stretching more!"
    scene sm1cs-my003-48 my-especially-new-profession-mct-got-point-about-that_c1 with dissolve
    play voice3 girl34_thinking_hmm5 noloop
    my "Especially with your new chosen profession."
    if persistent.is_special:
        mc "You might have a point, Mom."
    else:
        mc "You might have a point, Melony."
    play sound sfx_skirt_off2
    scene sm1cs-my003-49 my-stands-up-mct-rule-senventeen-my-alright-this-one-tougher_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Rule 18 of running your own porn studio. Limber up."
    play voice3 girl34_yes_yeah6 noloop
    my "All right, now this one is a little bit tougher, but I have faith in you."
    scene sm1cs-my003-50 mc-aight-lets-see_c1 with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "All right, let's see what..."
    play sound sfx_cloth_rustling1
    scene sm1cs-my003-51 my-gets-new-pose-mct-oh-fuck-me_c1 with dissolve
    play voice2 mc_pain_mff5 noloop
    mct "Oh fuck me..."
    scene sm1cs-my003-52 my-alright-give-try-mct-this-not-going-well_c1 with dissolve
    play voice3 girl34_hey_simple4 noloop
    my "All right! Give it a try!"
    play voice2 mc_thinking_mmm3 noloop
    mc "I don't think this will end well."
    my "Come on. You won't know until you try."
    play sound sfx_cloth_rustling2
    scene sm1cs-my003-53 mc-tries-almost-gets-position_c1 with dissolve
    pause
    play sound sfx_fall_mud1
    scene sm1cs-my003-54 mc-shakes-mct-oh-oh_c1 with dissolve
    play voice2 mc_pain_ou1 noloop
    mct "Uh oh-"
    play voice2 mc_pain_auh3 noloop
    play voice3 girl34_scared_ah7 noloop
    play sound sfx_fall_down1 volume 1.4
    scene sm1cs-my003-55 mc-falls-on-ground_c1 with vpunch
    my "[mcname]!"
    play sound sfx_cloth_rustling3
    scene sm1cs-my003-56 my-crawls-top-mc-my-you-okay_c1 with dissolve
    play voice3 girl34_surprised_huh4 noloop
    my "Are you okay?"
    scene sm1cs-my003-57 mct-my-what-boobs-have_c1 with dissolve
    play voice2 mc_angry_errr8 noloop
    if persistent.is_special:
        mct "My god, what boobs you have, Mom..."
    else:
        mct "My God... Melony's tits are in my face..."
    scene sm1cs-my003-58 mc-erm-totally-good-my-that-one-pretty-advanced-pose_c1 with dissolve
    play voice2 d1s5b_emmm noloop
    mc "Erm- yeah, totally good. I just lost my balance."
    play voice3 girl34_disappointed_mmf2 noloop
    my "That one was a pretty advanced pose, I shouldn't have done it with you."
    play sound sfx_cloth_rustling2
    scene sm1cs-my003-59 mc-my-stand-up-mc-seriously-fine-my-how-about-finish-my-stretching_c1 with dissolve
    play voice2 mc_no_uhuh2 noloop
    if persistent.is_special:
        mc "It's alright Mom. I'm okay. "
    else:
        mc "*chuckles* I'll live."
    play voice3 girl34_thinking_hmm3 noloop
    my "Well, how about you just help me finish my stretching, 'kay?"
    scene sm1cs-my003-60 mc-yeah-totally-fine_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, that's totally fine."
    play sound sfx_cloth_rustling4
    scene sm1cs-my003-61 my-gets-position-mct-honestly-no-stretching-mct-something-gonna-tear_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "I honestly don't think I could do any more stretching."
    mct "I feel like if I try anything else, something is going to tear."
    scene sm1cs-my003-62 my-little-help-mct-oh-my_c1 with dissolve
    play voice3 girl34_hey_simple2 noloop
    my "[mcname], can I get your help?"
    mct "Oh my..."
    scene sm1cs-my003-63 mc-totally-what-need-help-my-inner-thigh_c1 with dissolve
    play voice2 mc_yes_yes8 noloop
    mc "Erm, totally. What do you need help with?"
    play voice3 girl34_thinking_emm4 noloop
    my "My inner thigh muscle is really tight. While I'm stretching, can you just help rub it out?"
    scene sm1cs-my003-64 mc-rub-erm-yes-can_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Rub - erm - yeah, I can."
    scene sm1cs-my003-65 mc-gets-position-mct-come-on-mc-just-melony-be-cool_c1 with dissolve
    play voice2 d14s16_smell noloop
    if persistent.is_special:
        mct "Come on, [mcname]... this is your Mom. Be cool. Be {u}cool.{/u}"
    else:
        mct "Come on, [mcname]... it's just Melony. Be cool. Be {u}cool.{/u}"
    play sound sfx_cloth_wiping1 loop volume 2.0
    scene sm1cs-my003-66 mc-massage-my-mmm-yes-mc-that-spot_c1 with dissolve
    play voice3 girl34_happy_mmm3 noloop
    my "Mmmmmmm, yesssss."
    play voice2 mc_yes_yeah8 noloop
    mc "That the spot?"
    scene sm1cs-my003-67 my-yes-that-it-just-that-my-oh-yes-keep-going_c1 with dissolve
    play voisex3 girl13_sex_openmoans1 volume 0.6
    play sound sfx_handjob_cream1 loop
    my "Yes, yes, that's itttt. Juuuuust like that..."
    my "Oh yes, keep going... mmmmm..."
    scene sm1cs-my003-68 mct-god-sounds-so-hot-nope-cant-think-like-that_c1 with dissolve
    play voice2 mc_angry_errr3 noloop
    mct "God, she sounds so fucking hot right now-"
    mct "Nope, can't think like that. Last thing I need is a boner at a bouldering gym."
    scene sm1cs-my003-69 my-mmm-okay-time-next-stretch_c1 with dissolve
    my "Mmmm... okay, that's good. Time for the next position."
    play sound sfx_cloth_rustling1
    scene sm1cs-my003-70 my-gets-nes-position-my-press-hands-on-lower-back_c1 with dissolve
    play voisex3 girl34_thinking_hmm1 noloop
    my "Now, just press your hands into my lower back. It will help me push my limits."
    play sound sfx_drink_gulp volume 0.6
    scene sm1cs-my003-71 mc-gulp-mhm-can-do-that_c1 with dissolve
    play voice2 d9s2_ugu noloop
    mc "*Gulp* Mmhm-mm. I can do that."
    play sound sfx_cloth_rustling2
    scene sm1cs-my003-72 mc-akward-press-how-that-my-have-get-closer_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "How's that?"
    play voice3 girl34_no_happy3 noloop
    my "You have to get closer, silly. I really need you to give it to me."
    scene sm1cs-my003-73 mct-oh-god_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Oh my sweet fluffy lord."
    play sound sfx_cloth_wiping1 loop volume 2.0
    scene sm1cs-my003-74 mc-gets-position-that-better-my-oooh-good_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "That better?"
    play voisex3 girl13_sex_openmoans1 volume 0.7
    my "That is perfect, [mcname]. You're going great."
    scene sm1cs-my003-75 mct-does-have-idea-how-sounds_c1 with dissolve
    play voisex2 mc_sex_openmoans2
    mct "Does she have any idea of what this sounds like? Jesus."
    scene sm1cs-my003-76 my-moaning-face-harder-mc-harder-please-mct-jesus_c1 with dissolve
    my "Harder, [mcname]... harder, please!"
    mct "Jesus H. - oh she sounds so-"
    scene sm1cs-my003-77 mct-fuck-pupies-bitcoin-cows-mct-phew-that-close_c1 with dissolve
    mct "Fuck, fuck, fuck - erm, puppies, bitcoin, stock market, uhhhh cows?"
    mct "Phew. That was close..."
    stop voisex2 fadeout 1.0
    stop sound fadeout 1.0
    scene sm1cs-my003-78 my-that-was-good-just-one-more_c1 with dissolve
    play voisex3 girl34_happy_mmm1 noloop
    my "Mmmm, that was good. Just one more."
    play sound sfx_cloth_rustling3
    scene sm1cs-my003-79 my-gets-back-this-one-need-bracing-mc-what-pose_c1 with dissolve
    play voice3 girl34_thinking_emm3 noloop
    my "So for this one, I just need your help bracing me. I can get into the pose, I just can't hold it very long."
    play voice2 mc_thinking_hm noloop
    mc "What po-"
    play sound sfx_cloth_planket2
    scene sm1cs-my003-80 my-gets-new-position-oh-jesus-my-hurry-mc-grab-me_c1 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Cool. New pose."
    play voice3 girl34_scared_oof noloop
    my "Come on tiger. I'm waiting."
    play sound sfx_cloth_wiping1 loop volume 2.0
    scene sm1cs-my003-81 mc-gets-position-mct-oh-my-does-melony-have-idea_c1 with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "Holy cow."
    if persistent.is_special:
        mct "Is Mom intending to be so..."
    else:
        mct "Is Melony intending to be so..."
    scene sm1cs-my003-82 mct-no-she-doesnt-my-oh-yes_c1 with dissolve
    play voisex3 girl13_sex_openmoans1
    play voisex2 mc_sex_openmoans2
    mct "Sexy?"
    scene sm1cs-my003-83 my-moaning-oh-so-close-just-longer-right-there_c1 with dissolve
    my "Oh, right there. Just hold on a little longer."
    my "Yes...{w}just like thaaaat..."
    scene sm1cs-my003-84 mct-fuck-deff-have-boner-mct-there-no-way_c1 with dissolve
    mct "Fuck... fuck, fuck, fuck... I definitely have a boner, and it is rubbing right up against her crotch."
    mct "There's no way-"
    stop voisex2 fadeout 1.0
    scene sm1cs-my003-85 my-oh-yes-oh-yes-my-put-me-down_c1 with dissolve
    play voisex3 girl13_sex_orgasm2 noloop
    my "Oh yessss..."
    my "Put me down."
    play sound sfx_cloth_rustling1
    scene sm1cs-my003-86 my-lying-down-oh-my-incredible-mc-erm-yeah_c1 with dissolve
    play voice3 girl34_surprised_ohmy1 noloop
    my "Oh my... that was incredible. You make an excellent partner, [mcname]."
    play voice2 d2s9_confused noloop
    mc "Happy to help."
    scene sm1cs-my003-87 my-sits-up-my-now-dont-sound-excited-mc-he-excited-see-how-much-stetching-helps_c1 with dissolve
    play voice3 girl34_thinking_eeh1 noloop
    my "Now that I'm all good and stretched out to, shall we get to the main event?"
    play voice2 mc_yes_yes2 noloop
    mc "The main event?"
    my "*giggles* The bouldering, silly."
    mc "Oh right..."
    scene sm1cs-my003-88 my-mc-standing-my-not-that-excited-mc-excited-how-much-stretching-helps_c1 with dissolve
    play voice3 girl34_happy_laugh3 noloop
    my "Now, don't sound too excited, [mcname]."
    play voice2 d3s7_mcemm noloop
    mc "I'm just excited to see how much stretching has helped me out."
    scene sm1cs-my003-89 my-notice-right-away_c1 with dissolve
    play voice3 girl34_disappointed_oh2 noloop
    my "Oh, you'll notice it right away."
    scene sm1cs-my003-90 my-mc-standing-front-boulders_c1 with dissolve
    pause
    scene sm1cs-my003-91 my-okay-now-all-stretched-tackle-first-wall-go-first-watch-path_c1 with dissolve
    play voice3 girl34_yes_aga3 noloop
    my "Put your game face on. It's time to tackle our first wall!"
    my "I'll go up first, and you can watch my path."
    scene sm1cs-my003-92 mc-asking-path-my-mhm-route-she-takes_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Path?"
    play voice3 girl34_yes_ugu2 noloop
    my "Mmmhmmm! The route I take. And if I get stuck, you can help guide me to the top."
    play sound sfx_carpet_footsteps1 loop
    scene sm1cs-my003-93 mc-sounds-good-my-walking-towards-wall-here-we-go_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay, that sounds good to me!"
    play voice3 girl34_happy_relief4 noloop
    my "Here we go!"
    play sound sfx_skirt_off2
    scene sm1cs-my003-94 my-starts-climbing-one-things-all-power-in-hips_c1 with dissolve
    play voice3 girl34_thinking_emm1 noloop
    my "So one of the things I've learned about climbing, is that all of the power is in your hips!"
    my "Most people think it's in your fingers, but if you try it that way, you'll get tired super fast."
    my "So remember, legs!"
    scene sm1cs-my003-95 my-so-remember-legs-mc-that-explains-big-ass_c1 with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mct "That explains why her ass is so big..."
    play sound sfx_cloth_rustling3 volume 2.5
    scene sm1cs-my003-96 my-keeps-climbing-also-try-keep-three-point-contact-mc-okay-three-point_c1 with dissolve
    play voice3 girl34_thinking_eeh2 noloop
    my "You also want to try and keep three points of contact on the wall. That's how you keep most of the stress of your body."
    play voice2 mc_yes_okay3 noloop
    mc "Okay, three points of contact."
    play sound sfx_throw_something1
    scene sm1cs-my003-97 my-ooph-mc-you-okay_c1 with dissolve
    play voice3 girl34_pain_ergh noloop
    my "Ooooph!"
    play voice2 mc_surprised_huh7 noloop
    mc "You okay?"
    scene sm1cs-my003-98 my-yeah-been-while-hmm_c1 with dissolve
    play voice3 girl34_yes_yeah2 noloop
    my "Yeah, it's just been awhile since I've been able to get to the gym. Working some muscles that are a little frozen up."
    my "Hmmmmm..."
    scene sm1cs-my003-99 mc-what-up-my-not-sure-next-hold_c1 with dissolve
    play voice2 mc_hey_hey6 noloop
    mc "What's up?"
    play voice3 girl34_disappointed_eeh3 noloop
    my "I'm just not sure what my next hold is. Do you have any suggestions from down there?"
    scene sm1cs-my003-100 mct-man-no-idea-what-doing-focus-waiting-for-choice_c1 with dissolve
    play voice2 mc_angry_huh1 noloop
    mct "Man, I have no idea what I'm doing..."
    mct "But I didn't realize her butt would-"
    scene sm1cs-my003-101 mc-choice-menu-screen_c1 with dissolve
    play voice2 mc_angry_errr1 noloop
    mct "Focus, [mcname]! She's hanging there waiting for you to make a choice!"
    menu:
        "Try for the hold on your left!":
            $ player.set_choice("sm1cs_my003_hold_left")
            scene sm1cs-my003-102 choice-left-mc-that-left-one-my-okay_c1 with dissolve
            play voice2 mc_hey_hey7 noloop
            mc "Try to reach the handhold on your left!"
            play voice3 girl34_yes_aga4 noloop
            my "Okay!"
            play sound sfx_skirt_off1 volume 1.7
            scene sm1cs-my003-103 my-reaching-almooost_c1 with dissolve
            play voice3 girl34_angry_breath2 noloop
            my "Almoooost..."
            scene sm1cs-my003-104 my-damnit-cant-reach_c1 with dissolve
            play voice3 girl34_angry_argh4 noloop
            my "Damnit!"
            my "I can't reach it!"
            scene sm1cs-my003-105 my-back-previous-hold-there-another-good-hold-mc-can-tri-right-my-okay_c1 with dissolve
            play voice3 girl34_thinking_emm2 noloop
            my "Is there another good hold for me?"
            play voice2 mc_yes_yeah7 noloop
            mc "You can try the one on your right?"
            my "Okay!"
        "It looks like the right one is within reach!":
            scene sm1cs-my003-106 choice-right-one-my-okay_c1 with dissolve
            play voice2 mc_hey_hey7 noloop
            mc "The one on your right looks within reach!"
            play voice3 girl34_yes_aga4 noloop
            my "Okay!"
    jump sm1cs_my003_continue
label sm1cs_my003_continue:
    play sound sfx_cloth_rustling2
    scene sm1cs-my003-107 my-reaches-right-hold-mmm_c1 with dissolve
    play voice3 girl34_angry_errr noloop
    my "Mmmmmm!"
    play sound sfx_leg_kick8
    scene sm1cs-my003-108 my-grabs-got-it-mc-hell-yeah_c1 with dissolve
    play voice3 girl34_happy_yes noloop
    my "I got it!"
    play voice2 mc_happy_yes1 noloop
    mc "Hell yeah!"
    scene sm1cs-my003-109 my-phew-big-leap-have-path-routed-can-follow_c1 with dissolve
    play voice3 girl34_happy_phew1 noloop
    my "Phew! That was a big reach!"
    my "Okay, I think I have a path routed! You want to follow behind me?"
    scene sm1cs-my003-110 my-almost-top-will-help-mct-here-goes-nothing_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Uhm, sure!"
    play voice3 girl34_happy_nice4 noloop
    my "I'm almost to the top! Get started and I'll help you from the top!"
    mct "Well... here goes nothing."
    play sound sfx_leg_kick7
    scene sm1cs-my003-111 mc-climbing-mct-not-bad-not-too-hard_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Okay, not too bad..."
    mct "Definitely not too hard yet..."
    play sound sfx_cloth_rustling3 volume 1.6
    scene sm1cs-my003-112 mc-climbing-deff-feeling-in-fingers-mct-more-push-legs_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mct "Can definitely feel it in my fingers, I have to remember the legs thing..."
    mct "More pushing with my legs."
    scene sm1cs-my003-113 my-okay-on-top-how-doing-mc-so-good-so-far_c1 with dissolve
    play voice3 girl34_happy_woohoo2 noloop
    my "Okay! I'm at the top! How're you doing, [mcname]?"
    play voice2 mc_yes_yeah4 noloop
    mc "So far, so good!"
    play sound sfx_leg_kick8
    scene sm1cs-my003-114 my-hard-part-coming-up-mc-dont-remind_c1 with dissolve
    play voice3 girl34_yes_yeap4 noloop
    my "Okay, the hard part is coming up!"
    play voice2 mc_angry_off noloop
    mc "Don't remind me..."
    scene sm1cs-my003-115 mc-tough-hold-this-hold-right-my-okay-this-big-stretch-mc-okay_c1 with dissolve
    mct "Okay, so it's the hold on the right... right?"
    play voice3 girl34_yes_aga1 noloop
    my "Okay! This is the big stretch! You're really going to have to reach the hold on the right."
    play voice2 mc_yes_okay2 noloop
    mc "Okay!"
    play sound sfx_epic_jump1
    scene sm1cs-my003-116 mc-reaching-mct-shit-no-kidding-really-stretch_c1 with dissolve
    play voice2 mc_angry_errr7 noloop
    mct "Almost... got it!"
    play sound sfx_leg_kick7
    scene sm1cs-my003-117 mc-reaches-hold-got-it-my-good-job_c1 with dissolve
    play voice2 mc_happy_wooh3 noloop
    mc "I got it!"
    scene sm1cs-my003-118 my-almost-there_c1 with dissolve
    play voice3 girl34_happy_nice3 noloop
    my "Good job, [mcname]! You're almost there!"
    play sound sfx_cloth_rustling5 volume 1.7
    scene sm1cs-my003-119 mc-getting-top-my-happy-yay-did-it_c1 with dissolve
    play voice3 girl34_happy_yay2 noloop
    my "Yay! You did it!"
    scene sm1cs-my003-120 mc-bent-over-yep-phew-workout-my-dont-feel-good_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    if persistent.is_special:
        mc "Yep... You were right, Mom. It's a helluva workout."
    else:
        mc "Yep... You were right, Melony. It's a helluva workout."
    play voice3 girl34_yes_questioning7 noloop
    my "That it is! But don't you feel good about it?"
    scene sm1cs-my003-121 mc-standing-smiling-mc-mostly-surprised-my-ready-next-climb_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I'm... mostly surprised I made it. But yeah... Feels good."
    play voice3 girl34_arrogant_huh1 noloop
    my "Ready for the next climb?"
    scene sm1cs-my003-122 mc-uhhhhm-mct-was-hoping-just-one_c1 with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "Uhm..."
    mct "I was really hoping for just the one..."
    scene sm1cs-my003-123 mct-cant-dissapoint-mc-sure-lets-climb-walls_c1 with dissolve
    if persistent.is_special:
        mct "But I can't disappoint Mom."
    else:
        mct "But I can't disappoint Melony."
    play voice2 mc_yes_sure1 noloop
    mc "Sure! Let's go bouldering!"
    scene sm1cs-my003-124 my-excited-happy-yay-okay-bottom-mct-oh-boy_c1 with dissolve
    play voice3 girl34_happy_yay3 noloop
    my "Yay! Okay! Back to the bottom!"
    mct "Oh boy..."
    $ renpy.music.set_volume(1.0, 2.0, "music" )
    scene sm1cs-my003-125 climbing-montage-one-my-one_c1 with dissolve
    pause
    scene sm1cs-my003-126 climbing-montage-two-mc-one_c1 with dissolve
    pause
    scene sm1cs-my003-127 climbing-montage-three-my-two_c1 with dissolve
    pause
    scene sm1cs-my003-128 climbing-montage-four-mc-two_c1 with dissolve
    pause
    scene sm1cs-my003-129 climbing-montage-five-my-three_c1 with dissolve
    pause
    scene sm1cs-my003-130 climbing-montage-six-mc-three_c1 with dissolve
    pause
    scene sm1cs-my003-131 mc-my-sit-down-after-climbing-taking-break_c1 with dissolve
    pause
    $ renpy.music.set_volume(0.5, 2.5, "music" )
    scene sm1cs-my003-132 my-wow-mc-impressed-mc-oh_c1 with dissolve
    play voice3 girl34_surprised_wow1 noloop
    my "Wow, [mcname]! I'm impressed!"
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    scene sm1cs-my003-133 my-yeah-great-shape-mc-thanks-melony_c1 with dissolve
    play voice3 girl34_yes_yeah8 noloop
    my "Yeah! You're in great shape! This much climbing is a real workout. And you've been keeping up!"
    play voice2 mc_happy_a1 noloop
    if persistent.is_special:
        mc "Thanks, Mom."
    else:
        mc "Thanks, Melony."
    scene sm1cs-my003-134 my-ready-real-challenge-mc-uhm-real-challenge_c1 with dissolve
    play voice3 girl34_angry_ahem3 noloop
    my "But are you ready for the real challenge?"
    play voice2 d2s12_emmm noloop
    mc "What's the real challenge?"
    play sound sfx_throw_something1
    scene sm1cs-my003-135 my-race-to-top_c1 with dissolve
    play voice3 girl34_arrogant_ha2 noloop
    my "A race to the top, of course."
    scene sm1cs-my003-136 mc-feels-like-advantage-my-calling-old_c1 with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "I feel like you have an unfair advantage, with your experience and whatnot."
    play voice3 girl34_surprised_huh2 noloop
    my "Are you calling me old, [mcname]?"
    play sound sfx_cloth_rustling3
    scene sm1cs-my003-137 mc-what-no-no-my-relax-just-teasing-you_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What! No! No! I'm, uhm, just saying that you've got more {i}climbing{/i} experience!"
    play voice3 girl34_happy_laugh4 noloop
    my "I'm just teasing you, [mcname]."
    scene sm1cs-my003-138 mc-relaxes-my-what-say-race-top-mc-you-on_c1 with dissolve
    play voice3 girl34_thinking_hmm6 noloop
    my "So, what do you say? Race to the top?"
    play voice2 mc_yes_yes7 noloop
    mc "All right, you're on."
    scene sm1cs-my003-139 my-hooray_c1 with dissolve
    play voice3 girl34_happy_woohoo1 noloop
    my "Hooray!"
    scene sm1cs-my003-140 mc-my-looking-wall-my-you-ready-mc-can-say-no_c1 with dissolve
    play voice3 girl34_disappointed_mmf3 noloop
    my "All right, you ready?"
    play voice2 mc_surprised_uh2 noloop
    mc "Can I say no?"
    scene sm1cs-my003-141 my-looks-mc-nope_c1 with dissolve
    play voice3 girl34_no_nope4 noloop
    my "Nope!"
    play sound sfx_cloth_rustling1
    scene sm1cs-my003-142 my-ready-get-set_c1 with dissolve
    play voice3 girl34_angry_ahem1 noloop
    my "On your mark...{w} get set..."
    play sound sfx_socks_dancing1
    scene sm1cs-my003-143 my-stars-running-go-mc-hey_c1 with dissolve
    play voice3 girl34_happy_wooh2 noloop
    my "Go!"
    play voice2 mc_hey_hey1 noloop
    mc "Hey!"
    play sound2 sfx_carpet_run1 noloop
    scene sm1cs-my003-144 my-wall-mc-after-mc-that-cheating-my-all-fair_c1 with dissolve
    play voice2 mc_angry_errr4 noloop
    mc "That's cheating!"
    play voice3 girl34_happy_laugh9 noloop
    my "All is fair in love and war, [mcname]!"
    play sound sfx_leg_kick8
    scene sm1cs-my003-145 mc-oh-will-show-you-mct-shit-she-fast_c1 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Oh, I'll show you!"
    mct "Shit, she's fast... I don't think I'll be able to catch up to her."
    scene sm1cs-my003-146 my-top-mc-come-on-mc-grrr_c1 with dissolve
    play voice3 girl34_arrogant_huh2 noloop
    my "Come one, [mcname]! You'll have to try harder than that!"
    play voice2 mc_angry_errr2 noloop
    mc "Grrr."
    play sound sfx_cloth_rustling2
    scene sm1cs-my003-147 my-reaches-next-hold-let-me-show-how-do-it_c1 with dissolve
    play voice3 girl34_happy_laugh10 noloop
    if persistent.is_special:
        my "Let your Mom show you-"
    else:
        my "Let me show you-"
    play sound sfx_fall_mud1
    scene sm1cs-my003-148 my-slips-oh-shit_c1 with dissolve
    play voice3 girl34_scared_ah6 noloop
    my "Ohh shiiitttt!"
    play sound sfx_epic_jump1 volume 2.0
    scene sm1cs-my003-149 my-falling-shiiiit_c1 with dissolve
    play voice2 mc_scared_huh3 noloop
    mc "Oh shi-!"
    play sound sfx_leg_kick5
    scene sm1cs-my003-150 mc-grabs-her-my-wait-mc-uh-oh_c1 with dissolve
    play voice3 girl34_scared_ah1 noloop
    my "Wait, [mcname]-"
    play voice2 mc_pain_ou1 noloop
    mc "Uh oh."
    play sound sfx_fall_mud1
    play sound2 sfx_epic_jump1 noloop
    scene sm1cs-my003-151 mc-my-both-fall_c1 with dissolve
    play voice2 mc_pain_argh1 noloop
    mc "Shit!"
    play voice2 mc_pain_cough1 noloop
    play voice3 girl34_pain_ah3 noloop
    play sound sfx_fall_down1
    play sound2 sfx_leg_kick2 noloop
    scene sm1cs-my003-152 mc-falls-my-top-of-him-both-oooow_c1 with vpunch
    mc "OOUUUUPPPHHHH!"
    my "Owww!"
    scene sm1cs-my003-153 mct-that-no-fun-my-you-okay_c1 with dissolve
    play voice2 mc_pain_ffff noloop
    mct "Fuck... that wasn't fun..."
    play voice3 girl34_surprised_huh6 noloop
    my "Are you okay?"
    scene sm1cs-my003-154 mc-yeah-totally-fine_c1 with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah... totally fine..."
    scene sm1cs-my003-155 my-tits-closeup-mct-least-tits-broke-fall-big-beautiful-tits_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    if persistent.is_special:
        mct "At least Mom's tits broke the fall a little bit..."
    else:
        mct "At least Melony's tits broke the fall a little bit..."
    mct "Her big, wonderful-"
    play sound sfx_cloth_rustling3
    scene sm1cs-my003-156 my-calls-mc-my-you-fine-maybe-concussion_c1 with dissolve
    play voice3 girl34_hey_simple3 noloop
    my "[mcname]?"
    my "Are you sure you're okay? Maybe you have a concussion."
    scene sm1cs-my003-157 mc-no-fine-my-maybe-hospital_c1 with dissolve
    play voice2 mc_no_no1 noloop
    mc "No, I'm fine. I promise."
    play voice3 girl34_disappointed_eeh1 noloop
    my "Are you sure? Maybe we should get you to the hospital."
    play sound sfx_cloth_rustling4
    scene sm1cs-my003-158 mc-no-serious-no-hospital-visit-needed_c1 with dissolve
    play voice2 mc_no_no8 noloop
    if persistent.is_special:
        mc "Seriously, Mom, no hospital visit needed. Just... a little sore, that's all."
    else:
        mc "Seriously, Melony, no hospital visit needed. Just... a little sore, that's all."
    scene sm1cs-my003-159 my-sure-concussions-serious-mc-pinky-swear-okay_c1 with dissolve
    play voice3 girl34_disappointed_eem2 noloop
    my "Are you sure? Concussions are serious-"
    play voice2 mc_disappointed_ehh1 noloop
    mc "I pinky promise that I am totally okay."
    scene sm1cs-my003-160 my-maybe-no-more-today-mc-that-totally-okay_c1 with dissolve
    play voice3 girl34_happy_relief2 noloop
    my "If you say so. But maybe no more climbing for today."
    play voice2 mc_yes_yes3 noloop
    mc "Now that, I am totally okay with!"
    play sound sfx_carpet_footsteps1 loop
    scene sm1cs-my003-161 my-mc-walking-towards-exit-my-gotta-back-hotel-mc-need-too_c1 with dissolve
    play voice3 girl34_happy_laugh2 noloop
    my "Hehehehehe!"
    my "I have to get back to the hotel, I definitely need a shower."
    play voice2 mc_yes_aga2 noloop
    mc "I do too."
    stop sound fadeout 1.0
    scene sm1cs-my003-162 my-this-lot-fun-mc-of-course_c1 with dissolve
    play voice3 girl34_thinking_hmm1 noloop
    my "This was a lot of fun, thank you for coming with me today."
    play voice2 mc_yes_yeah2 noloop
    if persistent.is_special:
        mc "Of course, Mom! I'm happy I was able to spend some more time with you."
    else:
        mc "Of course, Melony! I'm happy I was able to spend some more time with you."
    scene sm1cs-my003-163 my-look-forward-whatever-got-next_c1 with dissolve
    play voice3 girl34_thinking_hmm7 noloop
    my "Me too, [mcname]."
    scene sm1cs-my003-164 my-starts-walking-away-fact-stacy-inv-competition-thing-mc-what-thing_c1 with dissolve
    play voice3 girl34_surprised_oh4 noloop
    my "In fact, Stacy invited me over sometime soon for your little competition thing."
    play voice2 mc_surprised_huh6 noloop
    mc "Competition thing?"
    scene sm1cs-my003-165 my-yeah-talked-at-bar-mct-what-hell-talked-about_c1 with dissolve
    play voice3 girl34_yes_yeah5 noloop
    my "Yeah, we talked about it at the bar."
    mct "The bar? What the hell did we talk about again..."
    scene sm1cs-my003-166 my-see-later-mc-bye_c1 with dissolve
    play voice3 girl34_hey_seeya noloop
    my "I'll see you later, [mcname]!"
    play voice2 mc_hey_bye1 noloop
    mc "Bye!"
    play sound sfx_carpet_footsteps1 loop
    scene sm1cs-my003-167 my-walk-out_c1 with dissolve
    pause
    stop sound fadeout 2.0
    scene sm1cs-my003-168 mct-what-hell-sy-planning-never-get-rest_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "What the hell is Stacy planning now?"
    mct "I swear, while she's in my life, I will never get any rest..."
    scene sm1cs-my003-169 mc-walks-out-end-scene_c1 with dissolve
    pause
    stop sound5 fadeout 1.0
    jump sm1cs_my003_end_scene
label sm1cs_my003_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(MY_STORY, 4, 0, 7)
    return