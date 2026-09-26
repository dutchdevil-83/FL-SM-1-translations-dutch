image sm1cs-cw002-a31-glambot = Movie(play = "images/FS_IT/CW/s002/anim/sm1cs-cw002-a31-2x-50fps.webm", start_image = "sm1cs-cw002-a31 boyfriend-glambot-000_i", image = "sm1cs-cw002-a31 boyfriend-glambot-120_i", loop = False)
label sm1cs_cw002_2:
    $ renpy.music.set_volume(0.0, 0.0, "music" )
    $ renpy.music.set_volume(1.0, 0.5, "music2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound sfx_door_open7
    play sound4 sfx_cafe_crowd fadein 3.0
    play sound2 sfx_heels_steps2 fadein 1.0
    scene sm1cs-cw002-27 mc-walk-into-restaurant_c1 with dissolve
    $ renpy.music.play(audio.music_waterfall_ending, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_waterfall_ending_radio, "music2", True, None, True, 0.0)
    play voice2 mc_angry_errr7 noloop
    mct "Damn. That rideshare took way too long."
    mct "Claire is going to kill me for being late."
    scene sm1cs-cw002-28 cw-notices-mc_c1 with dissolve
    pause
    scene sm1cs-cw002-29 mc-hi-ms-watts-so-sorry-chw-this-tardy-boyfriend_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Hi Ms. Watts. I'm so sorry I'm-"
    stop sound2 fadeout 1.0
    scene sm1cs-cw002-30 mc-looking-confused_c1 with dissolve
    play voice4 boy7_arrogant_hmm1 noloop
    "Man" "So this must be the tardy boyfriend."
    play voice2 mc_thinking_mmm4 noloop
    mct "What?"
    play sound sfx_bed_slide3
    scene sm1cs-cw002-31 mc-ask-boyfriend-cw-smiling-yes-he-is_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "Boyfriend?"
    scene sm1cs-cw002-a31 boyfriend-glambot-000_i with dissolve
    pause 0.1
    play sound sfx_camera_fly1 volume 2.0
    scene sm1cs-cw002-a31-glambot
    pause 2.6
    play voice3 girl29_yes_aga1 noloop
    cw "Yes he is. But he is {i}very{/i} late."
    stop sound fadeout 1.0
    scene sm1cs-cw002-32 mct-what-hell-going-on_c1 with dissolve
    pause
    play voice3 girl29_thinking_mmm1 noloop
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-cw002-33 cw-kiss-near-lips-faking-_c1 with dissolve
    play sound mc_kiss2
    play voice2 mc_angry_hm2 noloop
    mct "What the hell is going on?"
    pause
    scene sm1cs-cw002-35 cw-whispers-cannot-believe-shouldve-asked-eugene_c1 with dissolve
    play voice3 girl29_angry_kgh noloop
    cw "*whispers* I cannot believe you."
    cw "*whispers* I knew I should have asked Eugene."
    scene sm1cs-cw002-35 mc-absoleutly-lost_c1 with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "*whispers* Eugene? Claire. I'm totally lost."
    scene sm1cs-cw002-36 cw-wouldve-explained-if-on-time-mc-whispers-boyfriend_c1 with dissolve
    play voice3 girl29_thinking_hmm2 noloop
    cw "*whispers* Those are my parents, and you're pretending to be my {b}boyfriend{/b}."
    cw "*whispers* And I could have explained the plan to you if you were on time."
    play voice2 mc_angry_huh2 noloop
    mc "*whispers* Boyfriend?"
    scene sm1cs-cw002-37 fw-dont-look-cute-chw-certainly-air-young-love_c1 with dissolve
    play voice4 girl9_surprised_oh noloop
    fw "Ah don't they look cute, Charles?"
    play voice5 boy7_yes_happy noloop
    chw "Certainly has the air of young love. Remember us at that age?"
    scene sm1cs-cw002-38 fw-giggling-you-dog-chw-all-adults_c1 with dissolve
    play voice4 girl9_happy_laugh1 noloop
    fw "Charles. You dog."
    play voice5 boy7_disappointed_hmm noloop
    chw "What? They're both adults."
    scene sm1cs-cw002-39 mct-okay-this-no-joke-cw-wants-acts-like-boyfriend_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "Okay. This isn't a joke..."
    mct "Claire wants me to act as her boyfriend in front of her parents!"
    play sound sfx_rope_stretch volume 0.5
    scene sm1cs-cw002-40 mct-thinks-while-cw-holding-his-had_c1 with dissolve
    pause
    play voice2 d14s16_smell noloop
    mct "Then again, this must be important to Claire."
    mct "She is my boss. Or my boss's boss. I should help."
    scene sm1cs-cw002-41 cw-eyes-begging-mc-play-along_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "My god. Look at her eyes. She's worried. This is why she was acting so strange last time."
    scene sm1cs-cw002-42 mc-raise-hand-hello-sorry-late-introduces-himself_c1 with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Hello. Sorry, I'm so late."
    mc "I'm [mcname] Young. I'm your daughter's boyfriend..."
    play sound sfx_cloth_rustling4
    play sound2 sfx_bed_slide2 noloop volume 0.6
    scene sm1cs-cw002-43 fw-hugs-mc-so-lovely-meet-you-mc-yeah-same_c1 with dissolve
    play voice4 girl9_sex_closedmoan4 noloop
    fw "It's so lovely to meet you."
    scene sm1cs-cw002-44 fw-still-hugging-mc-pls-call-farah-mc-farah-it-is_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Great... to meet you too, Mrs. Watts."
    play sound sfx_cloth_rustling1
    scene sm1cs-cw002-46 mc-checking-fw-thinks-cw-takes-after-her-still-fox_c1 with dissolve
    play voice4 girl9_arrogant_ha3 noloop
    fw "So proper. Please, call me, Farah. Makes me feel young again."
    play voice2 mc_yes_sure1 noloop
    mc "Farah it is."
    mct "Man. Claire definitely takes after her mother."
    mct "She's definitely still a bit of a fox."
    scene sm1cs-cw002-47 chw-hard-look-nerve-first-dating-daughter-now-hugging-wife_c1 with dissolve
    play voice5 boy7_arrogant_ha2 noloop
    chw "The nerve. First dating my daughter. Now hugging my wife and I don't even know you."
    play sound sfx_bed_slide3
    scene sm1cs-cw002-48 chw-goes-shake-relaxes-dating-chaotic-as-market-nice-meet-you_c1 with dissolve
    play voice5 boy7_angry_argh2 noloop
    chw "But I know these days dating is chaotic as the stock market."
    chw "Charles Watts. Good to meet you, [mcname]."
    play sound sfx_hands_clap2
    scene sm1cs-cw002-49 mc-chw-shake-hands_c1 with dissolve
    pause
    scene sm1cs-cw002-50 chw-pulls-mc-close-hip-new-shit-threatens-him_c1 with dissolve
    play voice5 boy7_hey_sexy noloop
    chw "*whispers* I'm hip with the new age shit."
    scene sm1cs-cw002-51 chw-got-it-mc-got-it_c1 with dissolve
    play voice5 boy7_disappointed_groan noloop
    chw "*whispers* But you break my daughter's heart, and I'll break what you hold most dear."
    chw "*whispers* Got it?"
    play voice2 d9s2_mcyes2 noloop volume 2.4
    mc "*whispers* Yes sir."
    scene sm1cs-cw002-52 chw-relaxed-again_c1 with dissolve
    play voice5 boy7_yes_aga1 noloop
    chw "I think we're going to get along fine, young man."
    play sound sfx_bed_slide2
    scene sm1cs-cw002-53 chw-calls-waiter-order-drinks_c1 with dissolve
    play voice5 boy7_hey_simple noloop
    chw "Come on. Let's get some food and drinks. I'm starving."
    play sound sfx_plates_moving1
    scene sm1cs-cw002-54 group-seated-get-drinks-by-waiter_c1 with dissolve
    pause
    play sound2 sfx_celebration_ding1 noloop
    scene sm1cs-cw002-55 chw-orders-waiter-keep-coming-waiter-yes-sirt_c1 with dissolve
    play voice5 boy7_yes_yep noloop
    chw "Keep bringing them until one of us passes out. *chuckles*"
    play voice6 boy10_yes_simple noloop
    "Waiter" "Right away, Mr. Watts."
    scene sm1cs-cw002-56 chw-looking-mc-ask-about-him-cw-daddy_c1 with dissolve
    play voice5 boy7_thinking_emm2 noloop
    chw "[mcname], tell us about yourself. I need to know if I approve or need to chase you out to the hills."
    play voice3 girl29_disgust_meh noloop
    cw "Daddy."
    scene sm1cs-cw002-57 chw-kidding-right-mc_c1 with dissolve
    play voice5 boy7_happy_laugh2 noloop
    chw "He knows I'm kidding."
    chw "Don't you?"
    scene sm1cs-cw002-58 mc-ofc-mr-watts-chw-start-talking_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Of course, Mr. Watts."
    play voice5 boy7_happy_laugh1 noloop
    chw "*chuckles* So get talking sonny."
    scene sm1cs-cw002-59 mc-sure-sure-cw-told-lot-fw-no-you-mystery_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Well, *coughs* I'm sure Claire has told you a lot."
    play voice4 girl9_no_angry noloop
    fw "Not really. You're a man of mystery to us."
    scene sm1cs-cw002-60 mc-glances-at-cw-she-avoids-look_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    pause
    scene sm1cs-cw002-61 mc-back-at-chw-explains-work-orbix_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    if player.completion_log_compare_date_for_item("sm1fs_i003", 21):
        mc "Well, I've been working at Orbix for a few weeks now."
    if player.completion_log_compare_date_for_item("sm1fs_i003", 14):
        mc "I'm still fairly new to Orbix. I think I've been there about two weeks."
    else:
        mc "Well, I pretty much just started at Orbix. But it's been a lot of fun."
    play voice5 boy7_surprised_huh1 noloop
    chw "You're working for my daughter?"
    scene sm1cs-cw002-62 chw-working-with-daughter-cw-not-really-under-her_c1 with dissolve
    play voice3 girl29_no_simple noloop
    cw "Not really, Daddy. [mcname] is under my purview, but we don't work hand in hand."
    play voice5 boy7_arrogant_hmm3 noloop
    chw "Good to hear."
    scene sm1cs-cw002-63 fw-smiling-good-work-charles-chw-oh-know-hard-work-too_c1 with dissolve
    play voice4 girl9_hey_simple noloop
    fw "It's good work, Charles."
    scene sm1cs-cw002-64 chw-always-knew-pride-joy-sharp-fills-heart-with-pride_c1 with dissolve
    play voice5 boy7_thinking_oh noloop
    chw "Oh I know. And it's hard work too."
    chw "I always knew my pride and joy was sharp. And now she's working for one of the most tech-no-logical companies in the city."
    chw "Fills this old heart with pride, it does."
    play voice4 girl9_yes_aga noloop
    fw "Mmhmm."
    scene sm1cs-cw002-65 cw-smiles-painted-smile_c1 with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "Oh no. If Claire has to keep smiling like that, her face might freeze like that."
    mct "I should tap in a bit more."
    scene sm1cs-cw002-66 mc-tells-cw-amazing-boss_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 2.2
    mc "Claire is a great boss. We're doing a big project right now, and it's all going very smooth thanks to her."
    play sound sfx_skirt_off2
    scene sm1cs-cw002-67 chw-outfuckinstanding-fw-enough-work-talk_c1 with dissolve
    play voice5 boy7_disgust_ooh noloop
    chw "Out-fucking-standing."
    play voice4 girl9_happy_mmm1 noloop
    fw "Enough work talk. So you two really just met at work and decided to go out together?"
    scene sm1cs-cw002-68 cw-mc-silently-look-each-other_c1 with dissolve
    pause
    scene sm1cs-cw002-69 mc-cw-both-yes_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    play voice3 girl29_yes_yep noloop
    "Both" "Yup."
    cw "I met him during the onboarding. Once I laid eyes on him, I knew I'd have ask him out."
    play voice5 boy7_surprised_ehh1 noloop
    chw "Wait. You asked him out?"
    scene sm1cs-cw002-70 cw-met-during-onboarding-wanted-ask-him-out-chw-wait-you-asked-out_c1 with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "I mean, I was hoping he'd ask me out. Even though I'm his boss and he works for me."
    play sound sfx_drink_slurp2
    scene sm1cs-cw002-71 cw-lying-ties-hide-with-cocktail-mean-hoping-he-ask-out_c1 with dissolve
    pause
    scene sm1cs-cw002-72 fw-oh-mc-bold-man-mc-yep-that-me_c1 with dissolve
    play voice4 girl9_disappointed_oof noloop
    fw "Oh [mcname]. Such a bold young man."
    play voice2 mc_yes_yeah4 noloop
    mc "Yup. That's me."
    scene sm1cs-cw002-73 fw-talking-makes-feel-good-was-scared-meet-scoundrel-sex-app_c1 with dissolve
    play voice4 girl9_happy_mmm2 noloop
    fw "Well it just makes me feel so good that you two found yourselves as you did."
    fw "I was so frightened that you might meet some scoundrel on that sex app you were using."
    play voice3 girl29_scared_ah4 noloop
    play sound sfx_throw_something1
    scene sm1cs-cw002-74 cw-shocked-mom-not-sex-app_c1 with hpunch
    cw "Mom! It wasn't a sex app."
    play sound3 sfx_comic_crickets1 noloop volume 0.3
    scene sm1cs-cw002-75 everyone-akward-silence_c1 with dissolve
    pause
    scene sm1cs-cw002-76 cw-repeats-wasnt-sex-app-just-dating-app_c1 with dissolve
    play voice3 girl29_angry_breath noloop
    cw "It wasn't a sex app."
    cw "It was just another dating app."
    scene sm1cs-cw002-77 fw-dont-believe-cw-dont-try-pull-wool-heard-from-mincie-diggler_c1 with dissolve
    play sound sfx_ice_cubes1
    play voice4 girl9_no_nah noloop
    fw "Don't try to pull the wool over my eyes, Claire."
    fw "I heard from Mincie Diggler that it was an illicit app for illicit hookups."
    fw "And I couldn't bear knowing my daughter was using it."
    scene sm1cs-cw002-78 fw-not-bear-daugther-using-it-chw-outrages-name-fw-yes_c1 with dissolve
    play voice5 boy7_arrogant_yeah noloop
    chw "And it had that outrageous name too, didn't it, hon?"
    play voice4 girl9_yes_confident noloop
    fw "Yes."
    play sound sfx_hands_clap3 volume 0.5
    scene sm1cs-cw002-79 cw-facepalm-told-daddy-fw-was-worried_c1 with dissolve
    play voice3 girl29_angry_dough noloop
    cw "You told daddy?"
    play voice4 girl9_thinking_hmm1 noloop
    fw "Well, I was worried about you, darling."
    scene sm1cs-cw002-80 chw-tries-remember-name-fw-no-not-it_c1 with dissolve
    play voice5 boy7_thinking_emm1 noloop
    chw "Bang Finder? Lewd Mapper?"
    play voice4 girl9_no_simple noloop
    fw "No, it wasn't that?"
    scene sm1cs-cw002-81 mc-is-it-fl-fw-that-one_c1 with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait, was it Fetish Locator?"
    scene sm1cs-cw002-82 fw-distraught-what-name-this-others-disguise_c1 with dissolve
    play voice4 girl9_yes_yeah2 noloop
    fw "That's the one."
    fw "Fetish Locator? I mean, really? What kind of name is that?"
    fw "At least the others disguise it a bit."
    scene sm1cs-cw002-83 mct-have-say-didnt-see-it_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.7
    mct "Wow, so Claire was one of the people at Orbix using the Fetish Locator app."
    scene sm1cs-cw002-84 mc-looking-cw-mct-she-ppl-orbix-using-app_c1 with dissolve
    mct "I have to say, I didn't see it."
    scene sm1cs-cw002-85 chw-narrows-eyes-how-you-know-app_c1 with dissolve
    play voice5 boy7_surprised_huh2 noloop
    chw "And just how do you know the name of that godless app?"
    play sound sfx_drink_gulp
    scene sm1cs-cw002-86 mc-drinking with dissolve
    pause
    scene sm1cs-cw002-87 mc-nervously-talking with dissolve
    play voice2 d1s5_mchappy noloop volume 1.8
    mc "I heard it on the news."
    scene sm1cs-cw002-88 chw-being-wary with dissolve
    play voice5 boy7_arrogant_ha1 noloop
    chw "I bet."
    scene sm1cs-cw002-89 fw-calming-them-down with dissolve
    play voice4 girl9_hey_happy2 noloop
    fw "It doesn't matter none. It's all in the past now."
    scene sm1cs-cw002-90 fw-looking-at-mc with dissolve
    play voice4 girl9_yes_unsure noloop
    fw "Ain't that right?"
    scene sm1cs-cw002-91 cw-pretending with dissolve
    play voice3 girl29_yes_happy noloop
    cw "It sure is, Momma."
    scene sm1cs-cw002-92 fw-giggling with dissolve
    play voice4 girl9_happy_laugh3 noloop
    fw "*giggles*"
    play sound "<from 1>audio/sfx/cloth/sfx_cloth_suitcase_ride1.ogg"
    scene sm1cs-cw002-93 waiter-bringing-in-food with dissolve
    pause
    stop sound fadeout 3.0
    play sound2 sfx_fork_eating1 noloop fadein 1.5
    jump sm1cs_cw002_2_after_lunch
label sm1cs_cw002_2_after_lunch:
    scene black
    show screen scene_transistion(_("After a tense lunch"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    stop sound2 fadeout 2.0
    scene sm1cs-cw002-94 fw-praising
    with Fade(0.5, 0.5, 0.5)
    play voice4 girl9_sex_closedmoan3 noloop
    fw "That was delicious."
    scene sm1cs-cw002-95 fw-happy with dissolve
    play voice4 girl9_happy_phew noloop
    fw "I'm so glad to meet you, [mcname]. I hope we'll be seeing more of you in the future."
    scene sm1cs-cw002-96 mc-replying with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah. Right back at you, Farah."
    scene sm1cs-cw002-97 chw-talking with dissolve
    play voice5 boy7_angry_hmm noloop
    chw "You might be a bit young, but if you can handle our darling, we're okay with you still dating her."
    scene sm1cs-cw002-98 cw-talking with dissolve
    play voice3 girl29_yes_yeah noloop
    cw "And I think that's my cue to say we should get going."
    scene sm1cs-cw002-99 fw-talking with dissolve
    play voice4 girl9_happy_laugh2 noloop
    fw "You know what your father means."
    fw "And it's good that you've found someone who can keep up with you, Claire."
    fw "No one here is getting any younger."
    scene sm1cs-cw002-100 cw-stressed with dissolve
    play voice3 girl29_yes_arrogant noloop
    cw "Yes. Thanks for the reminder."
    play sound sfx_paper_slide1 volume 1.6
    scene sm1cs-cw002-101 waiter-bill-time with dissolve
    cw "Thank you."
    mct "Claire looks very happy to pay the check and get out of here."
    play sound sfx_book_closed1
    scene sm1cs-cw002-102 chw-grabbing-the-check with dissolve
    play voice5 boy7_arrogant_he noloop
    chw "Heh, I don't think so, miss."
    play sound sfx_paper_slide1
    scene sm1cs-cw002-103 chw-teasing with dissolve
    play voice5 boy7_thinking_hmm1 noloop
    chw "Course, we should have your boyfriend cover this."
    scene sm1cs-cw002-104 ch-talking with dissolve
    play voice3 girl29_happy_laugh1 noloop
    cw "Good thing you already put your card down, Daddy."
    scene sm1cs-cw002-105 chw-grinning with dissolve
    play voice5 boy7_happy_laugh4 noloop
    chw "Yup. Good thing."
    play sound sfx_bed_slide2
    scene sm1cs-cw002-106 ch-holding-mc with dissolve
    play voice3 girl29_yes_aga2 noloop
    cw "Well I'm going to make sure [mcname] finds a rideshare. He needs to get back to work."
    scene sm1cs-cw002-107 fw-curious with dissolve
    play voice4 girl9_disappointed_geh noloop
    fw "So soon?"
    scene sm1cs-cw002-108 cw-excusing with dissolve
    play voice3 girl29_yes_yep noloop
    cw "Yup. Busy projects and all that."
    scene sm1cs-cw002-109 cw-pleasure with dissolve
    play voice4 girl9_thinking_hmm4 noloop
    fw "It was a pleasure to meet you, [mcname]."
    scene sm1cs-cw002-110 mc-pleasure with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Pleasure meeting you, Farah."
    stop sound4 fadeout 2.0
    play sound3 sfx_distanttraffic_city fadein 3.0
    $ renpy.music.set_volume(0.6, 2.0, "music" )
    $ renpy.music.set_volume(0.0, 4.5, "music2" )
    play sound sfx_door_openclosed1
    scene sm1cs-cw002-111 cw-talking with fade
    play voice3 girl29_angry_argh1 noloop
    cw "Fuck me. I swear I need a drink, and I already had two in there."
    scene sm1cs-cw002-112 cw-complaining with dissolve
    play voice3 girl29_angry_hmf noloop
    cw "Why couldn't you be on time? Then I could have better prepared you."
    menu:
        "It was fine."(hint="sm1cs_am002_2_m01_h01"):
            scene sm1cs-cw002-113 mc-its-ok with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "It was fine, Claire. I think your parents totally bought it."
            mc "Heck, they seem like they liked me."
            scene sm1cs-cw002-114 cw-arguing with dissolve
            play voice3 girl29_no_uhuh noloop
            cw "That's not the point, [mcname]."
        "Sorry, Claire."(hint="sm1cs_am002_2_m01_h02"):
            call sm1cs_am002_2_m01_c02 from _call_sm1cs_am002_2_m01_c02
            scene sm1cs-cw002-115 mc-sorry with dissolve
            play voice2 mc_disappointed_ehh5 noloop
            mc "Sorry Claire. It was just bad timing."
    scene sm1cs-cw002-116 mc-standing-up-for-himself with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "It probably would have been easier if you told me ahead of time what the plan was."
    scene sm1cs-cw002-117 cw-are-you-crazy with dissolve
    play voice3 girl29_thinking_oh noloop
    cw "Oh yes. I'm supposed to tell a man I barely know that he needs to stand in as my 'boyfriend'."
    scene sm1cs-cw002-118 mc-youre-right with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "You're right."
    scene sm1cs-cw002-119 mc-should-have-told-me with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "It probably wouldn't have hurt if you just asked me."
    mc "Instead of pretending like it was some Orbix work meeting."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw002-120 cw-shh with dissolve
    cw "..."
    scene sm1cs-cw002-121 cw-soft with dissolve
    play voice3 girl29_happy_relief noloop
    cw "You're right, [mcname]."
    cw "At the very least, it was certainly a less boring conversation than I usually have with them."
    play sound sfx_cloth_rustling4
    scene sm1cs-cw002-122 cw-work-mode with dissolve
    play voice3 girl29_pain_cough1 noloop
    cw "*ahem* Mr. Young... Please accept my apologies."
    cw "*sighs* I love my parents. But when they get involved, it can drive me crazy."
    cw "And it's been a while since I was in a relationship. So they worry."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw002-123 mc-talking with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Everyone's parents are like that."
    scene sm1cs-cw002-124 cw-talking with dissolve
    play voice3 girl29_arrogant_pff noloop
    cw "One time my mother tried to unlock my Ember profile so she could 'improve' it."
    scene sm1cs-cw002-125 mc-agreeing with dissolve
    play voice2 mc_scared_oh2 noloop
    mc "Yeah that's bad."
    scene sm1cs-cw002-126 cw-vulnerable with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "Thank you. For your help today, Mr. Young."
    menu:
        "Anything for my 'girlfriend'"(hint="sm1cs_am002_2_m02_h01"):
            call sm1cs_am002_2_m02_c01 from _call_sm1cs_am002_2_m02_c01
            scene sm1cs-cw002-127 mc-grinning with dissolve
            play voice2 d9s2_mcyes noloop volume 2.5
            mc "Anything for my girlfriend."
            scene sm1cs-cw002-128 cw-goodbye with dissolve
            play voice3 girl29_disappointed_mff noloop
            cw "Goodbye, Mr. Young."
            play sound sfx_heels_steps1 loop
            scene sm1cs-cw002-129 mc-thinking with dissolve
            play voice2 mc_arrogant_hm2 noloop
            mct "Hmmm. Maybe I shouldn't have pushed my luck."
        "Don't mention it, Ms. Watts."(hint="sm1cs_am002_2_m02_h02"):
            call sm1cs_am002_2_m02_c02 from _call_sm1cs_am002_2_m02_c02
            scene sm1cs-cw002-130 mc-smiling with dissolve
            play voice2 mc_no_nah2 noloop
            mc "Don't mention it, Ms. Watts."
            scene sm1cs-cw002-131 cw-smiling-back with dissolve
            play voice3 girl29_thinking_hmm4 noloop
            cw "Well. Until next time, Mr. Young."
            play sound sfx_heels_steps1 loop
            scene sm1cs-cw002-132 cw-walking-away with dissolve
            pause
    stop sound fadeout 2.5
    scene sm1cs-cw002-133 mc-thinking with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Well that was definitely one of the strangest lunches I've had."
    mct "Never really been interrogated by a girl's parents with whiskey before."
    scene sm1cs-cw002-134 mc-remembering with dissolve
    play voice2 mc_surprised_huh4 noloop
    mct "And holy shit. Now I know for sure that Claire used Fetish Locator."
    mct "I should talk to Stacy about this when I get the chance."
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    stop music fadeout 3.0
    stop sound3 fadeout 2.0
    stop music2 fadeout 3.0
    jump sm1cs_cw002_2_end
label sm1cs_cw002_2_end:
    $ StoryController.end_scene(CW_STORY, 3, 0, 1)
    return
label sm1cs_am002_2_m01_c02:
    $ player.set_choice("sm1cs_am002_2_apologize")
    return
label sm1cs_am002_2_m02_c01:
    $ CharacterController.get_character("cw").deduct_point(1)
    return
label sm1cs_am002_2_m02_c02:
    $ player.set_choice("sm1cs_am002_2_be_professional")
    $ CharacterController.get_character("cw").add_point(2)
    return