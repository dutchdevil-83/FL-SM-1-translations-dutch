label sm1cs_tl004:
    $ sm1cs_tl004_pool_score = 0
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.0, 0.0, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.set_volume(0.8, 0.0, "music3" )
    $ renpy.music.set_volume(0.0, 0.0, "music4" )
    $ renpy.music.play(audio.music_bbq_n_roll_1, "music" , True, None, True, 1.5)
    $ renpy.music.play(audio.music_bbq_n_roll_2, "music2" , True, None, True, 1.5)
    $ renpy.music.play(audio.music_bbq_n_roll_1_radio, "music3", True, None, True, 1.5)
    $ renpy.music.play(audio.music_bbq_n_roll_2_radio, "music4", True, None, True, 1.5)
    play sound sfx_double_door1
    play sound2 sfx_heels_steps1
    play sound4 sfx_cafe_crowd volume 1.5
    scene sm1cs-tl004-01-mc-tl with dissolve
    queue sound sfx_heels_steps2 loop
    pause
    scene sm1cs-tl004-02-tl-order with dissolve
    pause
    scene sm1cs-tl004-03-barmaid-thumbs-up with dissolve
    pause
    play sound sfx_bed_slide2
    stop sound2 fadeout 1.0
    scene sm1cs-tl004-04-mc-tl-sits with dissolve
    pause
    $ renpy.music.set_volume(0.6, 10.0, "music3" )
    scene sm1cs-tl004-05-mc-talk-tl with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "So... come here often, then?"
    scene sm1cs-tl004-06-tl-talk-mc with dissolve
    play voice3 girl24_surprised_huh3 noloop
    tl "Huh?"
    scene sm1cs-tl004-07-mc-talk-tl with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "I don't know. You just seem to know the bartender."
    scene sm1cs-tl004-08-tl-talk-mc with dissolve
    play voice3 girl24_disappointed_oh noloop
    tl "Oh, I thought you were trying to say I have a drinking problem."
    scene sm1cs-tl004-09-mc-talk-tl with dissolve
    play voice2 mc_surprised_why2 noloop
    mc "Why would I be saying that?"
    scene sm1cs-tl004-10-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_hah noloop
    tl "I don't know. But you wouldn't be the first."
    play sound sfx_heels_steps1
    scene sm1cs-tl004-11-mc-talk-tl with dissolve
    play voice2 d2s12_emmm noloop volume 1.5
    mc "I-"
    play sound2 sfx_plate_place1 noloop
    stop sound fadeout 5.0
    scene sm1cs-tl004-12-beer with dissolve
    play voice3 girl24_hey_simple noloop
    tl "Thanks."
    scene sm1cs-tl004-14-mc-talk-tl with dissolve
    play voice2 d2s9_confused noloop volume 1.8
    mc "Do... do you have a problem with drinking, Taisia?"
    scene sm1cs-tl004-25-tl-talk-mc with dissolve
    play voice3 girl24_surprised_what2 noloop
    tl "What...{w} hahahahaha! Don't make me laugh, [mcname]."
    scene sm1cs-tl004-26-mc-talk-tl with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "What have I gotten into?"
    scene sm1cs-tl004-27-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_kgh1 noloop
    tl "What, did someone piss in your beer?"
    play voice2 mc_surprised_what6 noloop
    scene sm1cs-tl004-28-mc-talk-tl with dissolve
    mc "I- wait, what?"
    scene sm1cs-tl004-29-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_yeah1 noloop
    tl "You seem to be extra out of it today."
    scene sm1cs-tl004-32-mc-talk-tl with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "I don't know what you mean."
    scene sm1cs-tl004-33-tl-talk-mc with dissolve
    play voice3 girl24_disgust_ooh1 noloop
    tl "'What', 'how', 'why'. I feel like you've said it 90 times."
    scene sm1cs-tl004-36-mc-talk-tl with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "I've said it three times since we started talking today."
    scene sm1cs-tl004-37-mc-inner-talk with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "And thought it to myself once... but she doesn't know that."
    scene sm1cs-tl004-33-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_yeah3 noloop
    tl "Whatever."
    scene sm1cs-tl004-22-mc-talk-tl with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Sorry, I just wasn't expecting you to say you have a problem drinking and then watch you sip on a beer."
    scene sm1cs-tl004-25-tl-talk-mc with dissolve
    play voice3 girl24_angry_err2 noloop
    tl "I do not have a problem drinking."
    play voice2 mc_arrogant_heh1 noloop volume 1.4
    mc "But, you said-"
    play sound sfx_skirt_off2
    scene sm1cs-tl004-27-tl-talk-mc with hpunch
    play voice3 girl24_angry_argh2 noloop
    tl "What, you want the sob story? You want some poor \"oh, look at fucking Taisia, messy, sloppy, Taisia\" story?"
    play voice2 mc_no_no10 noloop
    mc "No, I-"
    tl "Good, because you're not going to get one."
    play sound sfx_drinking_passionately
    scene sm1cs-tl004-30-mc-inner-talk with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Jesus... maybe coming out for drinks with Taisia was a mistake..."
    stop sound fadeout 1.0
    play sound2 sfx_cup_place1 noloop volume 1.7
    scene sm1cs-tl004-31-tl-talk-mc with dissolve
    play voice3 girl24_disappointed_eeh2 noloop
    tl "Look... I didn't mean to be so... grouchy about it."
    scene sm1cs-tl004-32-mc-talk-tl with dissolve
    play voice2 mc_no_nah2 noloop
    mc "It's fine..."
    scene sm1cs-tl004-33-tl-talk-mc with dissolve
    play voice3 girl24_no_simple1 noloop
    tl "No, I-"
    scene sm1cs-tl004-34-tl-talk-mc with dissolve
    play voice3 girl24_thinking_emm1 noloop
    tl "It's just a sore spot for me, 'kay? I used to be... more reckless."
    tl "And back then, there were some people around me who weren't... great."
    tl "And they said I had a drinking problem all the time. Told lots of people I did too. Started some crazy rumors about me."
    tl "Some of them were maybe a little true, but they were always way exaggerated."
    scene sm1cs-tl004-35-tl-talk-mc with dissolve
    play voice3 girl24_thinking_hmm1 noloop
    tl "It got me in trouble a few times. So... I don't like talking about it."
    play voice2 mc_happy_thatsgood noloop
    scene sm1cs-tl004-36-mc-talk-tl with dissolve
    stop voice2 fadeout 0.2
    mc "That... that makes sense."
    scene sm1cs-tl004-37-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Why the hell didn't she start with that? Now I feel like an asshole!"
    scene sm1cs-tl004-38-mc-talk-tl with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    mc "I'm sorry for bringing it up, Taisia."
    scene sm1cs-tl004-39-tl-talk-mc with dissolve
    play voice3 girl24_no_nah noloop
    tl "It's whatever.{w} You got any quarters?"
    scene sm1cs-tl004-40-mc-talk-tl with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "Quarters, what?"
    scene sm1cs-tl004-41-tl-talk-mc with dissolve
    play voice3 girl24_yes_yeah noloop
    tl "Yeah. They got a pool table here and I want to play pool."
    scene sm1cs-tl004-42-mc-talk-tl with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Uhm..."
    mc "Yeah, I've got a couple?"
    play sound sfx_bed_slide3
    scene sm1cs-tl004-43-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_huh1 noloop
    tl "Good."
    play sound sfx_heels_steps1 loop
    scene sm1cs-tl004-44-mc-inner-talk with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Man... Taisia is nuts. What if I don't want to play pool? "
    scene sm1cs-tl004-45-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Not like I have any say in the matter..."
    stop sound fadeout 1.5
    $ renpy.music.set_volume(0.8, 4.0, "music3" )
    scene sm1cs-tl004-46-pool-table with fade
    pause
    play sound sfx_sword_equiped1
    scene sm1cs-tl004-47-tl-talk-mc with dissolve
    play voice3 girl24_surprised_huh2 noloop
    tl "Want to make it interesting?"
    scene sm1cs-tl004-48-mc-talk-tl with dissolve
    play voice2 mc_surprised_how2 noloop
    mc "How interesting?"
    play sound sfx_cloth_wiping1
    scene sm1cs-tl004-49-tl-talk-mc with dissolve
    play voice3 girl24_happy_laugh1 noloop
    tl "Loser buys the next round."
    scene sm1cs-tl004-50-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "You're on."
    stop sound fadeout 1.0
    scene sm1cs-tl004-51-tl-talk-mc with dissolve
    play voice3 girl24_hey_greeting noloop
    tl "You'll have to go easy on me, it's been a long time since I've played pool."
    scene sm1cs-tl004-52-mc-talk-tl with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Hmmm..."
    scene sm1cs-tl004-53-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_huh2 noloop
    tl "What?"
    menu:
        "Call her bluff"(hint="sm1cs_tl004_m01_h01"):
            call sm1cs_tl004_m01_c01 from _call_sm1cs_tl004_m01_c01
            scene sm1cs-tl004-54-mc-talk-tl with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "For some reason, I don't believe you."
            scene sm1cs-tl004-55-tl-talk-mc with dissolve
            play voice3 girl24_surprised_oh1 noloop
            tl "You calling me a liar?"
            scene sm1cs-tl004-56-mc-talk-tl with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "Well I ain't calling you a truther."
        "Go along with it"(hint="sm1cs_tl004_m01_h01"):
            scene sm1cs-tl004-56-mc-talk-tl with dissolve
            play voice2 mc_yes_okay3 noloop
            mc "All right, I'll go easy on you."
            scene sm1cs-tl004-57-tl-talk-mc with dissolve
            play voice3 girl24_thinking_hmm3 noloop
            tl "Sweet."
    scene sm1cs-tl004-59-tl-talk-mc with dissolve
    play voice3 girl24_thinking_ah noloop
    tl "So, we have a bet?"
    scene sm1cs-tl004-58-mc-talk-tl with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure, we have a bet."
    play voice3 girl24_yes_ugu noloop
    tl "Cool. You can break."
    mc "Sounds good to me."
    scene sm1cs-tl004-60-mc-talk-tl with dissolve
    pause
    $ renpy.music.set_volume(0.0, 5.0, "music" )
    $ renpy.music.set_volume(0.0, 5.0, "music2" )
    $ renpy.music.set_volume(0.4, 5.0, "music3" )
    $ renpy.music.set_volume(0.4, 5.0, "music4" )
    scene sm1cs-tl004-62-pool-table with fade
    pause
    play sound sfx_billiards_hit1
    scene sm1cs-tl004-61-pool-table with dissolve
    pause
    play sound sfx_billiards_hit2
    scene sm1cs-tl004-63-pool-table with dissolve
    pause
    play sound sfx_billiards_hit3
    scene sm1cs-tl004-64-pool-table with dissolve
    pause
    scene sm1cs-tl004-65-mc-inner-talk with dissolve
    play voice2 mc_angry_errr7 noloop
    mct "Shit, she's going to win..."
    play sound sfx_billiards_hit4
    play sound2 sfx_billiards_goal1 noloop
    scene sm1cs-tl004-66-ball with hpunch
    pause
    scene sm1cs-tl004-67-tl-talk-mc with dissolve
    play voice3 girl24_happy_laugh2 noloop
    tl "Huh, I guess I wasn't as rusty as I thought I was."
    scene sm1cs-tl004-68-mc-talk-tl with dissolve
    play voice2 mc_yes_aga1 noloop volume 1.6
    mc "Uh huh. Apparently not."
    scene sm1cs-tl004-69-tl-talk-mc with dissolve
    play voice3 girl24_hey_angry noloop
    tl "Hey, don't hate the player."
    tl "You down for another game?"
    scene sm1cs-tl004-70-mc-talk-tl with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "What, after you kicked my ass?"
    scene sm1cs-tl004-71-tl-talk-mc with dissolve
    play voice3 girl24_no_happy noloop
    tl "Come on, you put up a good fight! I'd bet we're pretty evenly matched."
    scene sm1cs-tl004-72-mc-talk-tl with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Sure... and I'm guessing you'll want to bet on this one too, right? Another round of drinks."
    scene sm1cs-tl004-73-tl-talk-mc with dissolve
    play voice3 girl24_no_nope noloop
    tl "Nope."
    play sound sfx_cloth_rustling2
    scene sm1cs-tl004-74-tl-talk-mc with dissolve
    play voice3 girl24_sex_closedmoan1 noloop
    tl "I think we should make it even more interesting."
    scene sm1cs-tl004-75-mc-inner-talk with dissolve
    play voice2 mc_angry_off noloop
    mct "Uh oh."
    scene sm1cs-tl004-76-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_hm2 noloop
    tl "If I win, you'll give me 40 bucks."
    scene sm1cs-tl004-77-mc-talk-tl with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "Woah, 40 bucks is a jump up from the next round of drinks."
    scene sm1cs-tl004-78-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_yeah2 noloop
    tl "Gotta' keep it interesting, [mcname]. Can't do the same thing over, and over."
    scene sm1cs-tl004-79-mc-talk-tl with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "And what would I get if I win?"
    scene sm1cs-tl004-80-tl-talk-mc with dissolve
    play voice3 girl24_thinking_emm2 noloop
    tl "I'll give you a kiss."
    scene sm1cs-tl004-81-mc-look-tl with dissolve
    mc "..."
    play sound sfx_cloth_wiping1
    scene sm1cs-tl004-82-tl-look-mc with dissolve
    tl "..."
    mc "..."
    stop sound fadeout 1.0
    scene sm1cs-tl004-83-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_hah noloop
    tl "What?"
    scene sm1cs-tl004-84-mc-talk-tl with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Let me get this straight. If you win, I owe you 40 bucks. But if I win, all I get is a kiss?"
    scene sm1cs-tl004-85-tl-talk-mc with dissolve
    play voice3 girl24_happy_yeah2 noloop
    tl "Yeah. That's a pretty sweet deal honestly."
    scene sm1cs-tl004-87-mc-talk-tl with dissolve
    play voice2 d1s5b_emmm noloop volume 1.8
    mc "But... we've already fucked. How is a kiss an upgrade from that?"
    scene sm1cs-tl004-86-tl-talk-mc with dissolve
    play voice3 girl24_sex_closedmoan3 noloop
    tl "Because it'll be a deep, passionate kiss. Something you'd get, from like, a girlfriend or something."
    scene sm1cs-tl004-87-mc-talk-tl with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "I don't see how I'm winning in this deal."
    scene sm1cs-tl004-88-tl-talk-mc with dissolve
    play voice3 girl24_angry_argh1 noloop
    tl "Well that's the deal. Take it, or leave it."
    scene sm1cs-tl004-89-mc-talk-tl with dissolve
    menu:
        "Agree"(hint="sm1cs_tl004_m02_h01"):
            call sm1cs_tl004_m02_c01 from _call_sm1cs_tl004_m02_c01
            play voice2 mc_angry_errr2 noloop
            mc "Fine, you've got a deal."
            scene sm1cs-tl004-90-tl-talk-mc with dissolve
            play voice3 girl24_happy_yay2 noloop
            tl "Good."
        "Haggle over the betting price"(hint="sm1cs_tl004_m02_h02"):
            call sm1cs_tl004_m02_c02 from _call_sm1cs_tl004_m02_c02
            play voice2 mc_thinking_hmm5 noloop
            mc "20 bucks."
            scene sm1cs-tl004-90-tl-talk-mc with dissolve
            play voice3 girl24_angry_mmm noloop
            tl "Ugh, fine. But next time, it's going to be 40."
            play voice2 mc_yes_yeah5 noloop
            mc "Fine."
    jump sm1cs_tl004_pool01
label sm1cs_tl004_pool01:
    $ renpy.music.set_volume(0.4, 8.0, "music" )
    $ renpy.music.set_volume(0.4, 8.0, "music2" )
    $ renpy.music.set_volume(0.0, 10.0, "music3" )
    $ renpy.music.set_volume(0.0, 10.0, "music4" )
    $ renpy.music.set_volume(0.0, 15.0, "sound4" )
    play sound sfx_heels_steps1
    scene sm1cs-tl004-91-tl-talk-mc with dissolve
    play voice3 girl24_thinking_hmm6 noloop
    tl "All right, rack 'em up."
    play sound sfx_billiards_triangle
    scene sm1cs-tl004-92-pool-table with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-tl004-93-mc-talk-tl with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Ladies first."
    scene sm1cs-tl004-94-tl with dissolve
    pause
    play sound sfx_billiards_splash
    scene sm1cs-tl004-95-pool-table with hpunch
    pause
    scene sm1cs-tl004-96-tl-talk-mc with dissolve
    play voice3 girl24_yes_yap noloop
    tl "All you."
    scene sm1cs-tl004-97-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop volume 1.6
    mct "Okay... solids or stripes?"
    scene sm1cs-tl004-98-pool-table with dissolve
    menu:
        "Solids"(hint="sm1cs_tl004_m03_h01"):
            call sm1cs_tl004_m03_c01 from _call_sm1cs_tl004_m03_c01
            $ sm1cs_tl004_pool_score += 1
            scene sm1cs-tl004-99-mc-inner-talk with dissolve
            play voice2 d1s5_mcthinks noloop volume 1.7
            mct "Looks like the solids broke better."
            play sound sfx_billiards_hit2
            play sound2 sfx_skeeball_goal2 noloop
            scene sm1cs-tl004-100-ball-in with hpunch
            pause
            scene sm1cs-tl004-101-mc-inner-talk with dissolve
            play voice2 mc_happy_yes1 noloop
            mct "Yes! Got one in!"
            scene sm1cs-tl004-102-tl-talk-mc with dissolve
            play voice3 girl24_arrogant_kgh2 noloop
            tl "Lucky shot."
        "Stripes"(hint="sm1cs_tl004_m03_h02"):
            scene sm1cs-tl004-103-c2-mc-inner-talk with dissolve
            play voice2 d1s5_mcthinks noloop volume 1.7
            mct "I've always had good luck with stripes."
            play sound sfx_billiards_hit4
            scene sm1cs-tl004-104-c2-ball with dissolve
            pause
            scene sm1cs-tl004-105-c2-mc-inner-talk with dissolve
            play voice2 mc_angry_errr6 noloop
            mct "Damn... didn't go in."
    scene sm1cs-tl004-106-tl with dissolve
    pause
    play sound sfx_billiards_hit3
    scene sm1cs-tl004-107-tl-talk with dissolve
    play voice3 girl24_angry_err1 noloop
    tl "Shit..."
    scene sm1cs-tl004-108-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mct "Okay... do I go for the easy shot, or should I try to go for the ball near the middle pocket."
    menu:
        "Easy shot"(hint="sm1cs_tl004_m04_h01"):
            scene sm1cs-tl004-109-mc-inner-talk with dissolve
            play voice2 d14s16_smell noloop
            mct "Easy shot seems best."
            play sound sfx_billiards_hit2
            scene sm1cs-tl004-110-mc-inner-talk with dissolve
            play voice2 mc_pain_mff5 noloop
            mct "Shit! I didn't hit it hard enough!"
            scene sm1cs-tl004-111-tl-talk-mc with dissolve
            play voice3 girl24_happy_laugh3 noloop
            tl "Haha!"
            scene sm1cs-tl004-114-tl with dissolve
            pause
            play sound sfx_billiards_hit4
        "Middle pocket"(hint="sm1cs_tl004_m04_h02"):
            $ sm1cs_tl004_pool_score += 1
            call sm1cs_tl004_m04_c02 from _call_sm1cs_tl004_m04_c02
            scene sm1cs-tl004-109-mc-inner-talk with dissolve
            play voice2 d14s16_smell noloop
            pause
            play sound sfx_billiards_hit1
            play sound2 sfx_billiards_goal1 noloop
            scene sm1cs-tl004-112-c2-mc-inner-talk with dissolve
            play voice2 mc_thinking_hmm8 noloop
            mct "Yes! Another one down!"
            scene sm1cs-tl004-113-c2-tl-talk-mc with dissolve
            play voice3 girl24_arrogant_pff noloop
            tl "Shit."
    scene sm1cs-tl004-115-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Okay. I've got to go for the one at either the corner pocket, or bounce it off the back and get the other middle pocket ball in..."
    menu:
        "Corner pocket"(hint="sm1cs_tl004_m05_h01"):
            call sm1cs_tl004_m05_c01 from _call_sm1cs_tl004_m05_c01
            $ sm1cs_tl004_pool_score += 1
            scene sm1cs-tl004-116-mc with dissolve
            pause
            play sound sfx_billiards_hit5
            scene sm1cs-tl004-117-mc-talk with dissolve
            play voice2 mc_happy_wooh3 noloop
            mc "Hell yeah!"
            scene sm1cs-tl004-118-tl-talk-mc with dissolve
            play voice3 girl24_arrogant_hm1 noloop
            tl "Don't get cocky kid."
            scene sm1cs-tl004-121-mc-inner-talk with dissolve
        "Middle pocket"(hint="sm1cs_tl004_m05_h02"):
            play sound sfx_billiards_miss1
            scene sm1cs-tl004-119-c2-mc-talk with dissolve
            play voice2 mc_angry_daugh1 noloop
            mc "Shit."
            scene sm1cs-tl004-120-c2-tl-talk with dissolve
            play voice3 girl24_happy_laugh4 noloop
            tl "Haha!"
            scene sm1cs-tl004-121-mc-inner-talk with fade
    play voice2 mc_thinking_mmm1 noloop
    mct "All right... time to go for the 8 ball. There's not really a good option for where I should hit it."
    if sm1cs_tl004_pool_score == 3:
        call sm1cs_tl004_won_pool_game from _call_sm1cs_tl004_won_pool_game
        scene sm1cs-tl004-122-mc-inner-talk with dissolve
        play voice2 mc_thinking_hmm6 noloop
        mct "But, I think I should go for the corner pocket."
        play sound sfx_billiards_hit5
        play sound2 sfx_skeeball_goal2 noloop
        scene sm1cs-tl004-123-ball with hpunch
        pause
        scene sm1cs-tl004-124-mc-talk-tl with dissolve
        play voice2 mc_happy_oof2 noloop
        mc "Yes!"
        scene sm1cs-tl004-125-tl-talk-mc with dissolve
        play voice3 girl24_angry_argh3 noloop
        tl "Fuck."
        jump sm1cs_tl004_pool_kiss
    else:
        scene sm1cs-tl004-126-c2-mc-talk-tl with dissolve
        play voice2 mc_thinking_hmm6 noloop
        mc "I've had some good luck with the middle pocket."
        play sound sfx_billiards_hit2
        scene sm1cs-tl004-127-c2-ball-miss with dissolve
        pause
        play voice2 mc_pain_argh1 noloop
        scene sm1cs-tl004-128-c2-mc-talk with vpunch
        mc "Shit!"
        scene sm1cs-tl004-129-c2-tl-talk-mc with dissolve
        play voice3 girl24_surprised_oh3 noloop
        tl "Oh, that's it!"
        scene sm1cs-tl004-130-c2-tl with dissolve
        pause
        play sound sfx_billiards_hit5
        play sound2 sfx_skeeball_goal2 noloop
        scene sm1cs-tl004-131-c2-ball-in with hpunch
        pause
        scene sm1cs-tl004-132-c2-tl-talk with dissolve
        play voice3 girl24_happy_yeah1 noloop
        tl "Hell yeah."
        jump sm1cs_tl004_pool_lose
label sm1cs_tl004_pool_lose:
    scene sm1cs-tl004-133-tl-talk-mc with dissolve
    play voice3 girl24_angry_cough2 noloop
    tl "Pay up, [mcname]."
    if player.money >= player.get_choice("sm1cs_tl004_pool_bet"):
        call sm1cs_tl004_pay_bet from _call_sm1cs_tl004_pay_bet
        scene sm1cs-tl004-134-mc-talk-tl with dissolve
        play voice2 mc_yes_yeah6 noloop
        mc "Yeah, yeah. Here you go."
        scene sm1cs-tl004-135-tl-talk-mc with dissolve
        play voice3 girl24_happy_laugh5 noloop
        tl "Good game, [mcname]."
        jump sm1cs_tl004_pool_kiss
    else:
        scene sm1cs-tl004-136-c2-mc-talk-tl with dissolve
        play voice2 mc_angry_oof noloop
        mc "I don't have the cash right now... will you take an IOU?"
        play sound sfx_cloth_rustling4
        scene sm1cs-tl004-137-c2-tl-talk-mc with dissolve
        play voice3 girl24_angry_argh5 noloop
        tl "Ugh...{w} Fine. But, I will be collecting what you owe me."
        jump sm1cs_tl004_after_game
label sm1cs_tl004_pool_kiss:
    call sm1cs_tl004_got_kiss from _call_sm1cs_tl004_got_kiss
    scene sm1cs-tl004-138-tl-look-mc with dissolve
    pause
    play sound sfx_cloth_rustling3
    scene sm1cs-tl004-139-tl-mc with dissolve
    pause
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-tl004-140-tl-kiss-mc with dissolve
    play voice3 girl24_sex_closedmoan5 noloop
    play voice2 mc_thinking_mmm2 noloop
    play sound dahlia_kiss_french1
    pause
    if player.get_choice("sm1cs_tl004_won_pool_game"):
        scene sm1cs-tl004-141-mc-talk-tl with dissolve
        play voice2 mc_surprised_uh2 noloop
        mc "What the hell was that for?"
        scene sm1cs-tl004-142-tl-talk-mc with dissolve
        play voice3 girl24_disappointed_hmf noloop
        tl "Just... felt right. I don't know."
    else:
        scene sm1cs-tl004-143-c2-mc-talk-tl with dissolve
        play voice2 mc_thinking_mmm7 noloop
        mc "Mmmm... okay, that was some pretty good winnings."
        scene sm1cs-tl004-144-c2-tl-talk-mc with dissolve
        play voice3 girl24_no_uhuh noloop
        tl "You won't be so lucky next time."
    jump sm1cs_tl004_after_game
label sm1cs_tl004_after_game:
    $ renpy.music.set_volume(1.0, 6.0, "sound4" )
    $ renpy.music.set_volume(0.0, 12.0, "music" )
    $ renpy.music.set_volume(0.0, 12.0, "music2" )
    $ renpy.music.set_volume(0.5, 10.0, "music3" )
    $ renpy.music.set_volume(0.5, 10.0, "music4" )
    scene sm1cs-tl004-145-tl-talk-mc with dissolve
    play voice3 girl24_thinking_huh1 noloop
    tl "So, how's the movie doing?"
    scene sm1cs-tl004-146-mc-inner-talk with dissolve
    play voice2 mc_angry_huh1 noloop
    mct "Man, she is just all over the map with things tonight."
    scene sm1cs-tl004-147-mc-talk-tl with dissolve
    play voice2 d9s2_yeah noloop volume 2.4
    mc "It's doing all right."
    scene sm1cs-tl004-148-tl-talk-mc with dissolve
    play voice3 girl24_surprised_eeh2 noloop
    tl "So you'll be able to pay me soon?"
    scene sm1cs-tl004-149-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, we should have something for you."
    scene sm1cs-tl004-150-tl-talk-mc with dissolve
    play voice3 girl24_yes_aga noloop
    tl "When are we going to make our next movie?"
    play voice2 d1s5b_ehhh noloop volume 1.8
    mc "Uhhh, I haven't planned anything."
    scene sm1cs-tl004-149-mc-talk-tl with dissolve
    play voice2 mc_thinking_mmm5 noloop
    if not player.get_choice("sm1ms_renovation_completed"):
        mc "I think we need to upgrade the studio before we can really use it for anything else..."
    else:
        mc "I've been more concerned about getting the first video sold."
    scene sm1cs-tl004-150-tl-talk-mc with dissolve
    play voice3 girl24_thinking_hmm4 noloop volume 1.6
    tl "Well, we should make another one soon. I think selling more videos would mean more cash."
    scene sm1cs-tl004-151-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mct "Taisia is really harping on cash... I wonder if something is up."
    scene sm1cs-tl004-152-tl-talk-mc with dissolve
    play voice3 girl24_surprised_eeh1 noloop
    tl "So why don't you put those two heads of yours together and come up with something sexy for us to do."
    scene sm1cs-tl004-153-mc-talk-tl with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Two heads?"
    scene sm1cs-tl004-154-tl-talk-mc with dissolve
    play voice3 girl24_happy_yeah3 noloop
    tl "Yeah, the one on your shoulders, and the one in your pants."
    tl "But, I have to jet. I'll see you around, [mcname]."
    scene sm1cs-tl004-155-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, see you, Taisia."
    play sound sfx_cloth_rustling1
    scene sm1cs-tl004-156-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mct "Hmmm... I should really see what's up with Taisia needing cash {i}so{/i} badly. Most of our conversations are about money."
    mct "I hope everything is all right..."
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    stop music4 fadeout 3.0
    stop sound4 fadeout 2.0
    $ renpy.music.set_volume(1.0, 6.0, "sound4" )
    $ renpy.music.set_volume(1.0, 12.0, "music" )
    $ renpy.music.set_volume(1.0, 12.0, "music2" )
    $ renpy.music.set_volume(1.0, 10.0, "music3" )
    $ renpy.music.set_volume(1.0, 10.0, "music4" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    call sm1_unlock_gr_bar from _call_sm1_unlock_gr_bar_3
    jump sm1cs_tl004_exit_to_map
label sm1cs_tl004_exit_to_map:
    $ StoryController.end_scene(TL_STORY, 3, 0, 4, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1_unlock_gr_bar:
    if LocationController.get_map_location(GR_BAR).get_location().get_discovered_status() is False:
        $ player.discover_map_location(GR_BAR)
        $ CharacterController.get_character("mes").add_schedule("start_mes")
        $ StoryController.activate_story_line(MES_STORY)
        $ StoryController.activate_story_line(RD_STORY)
    return
label sm1cs_tl004_m01_c01:
    $ player.set_choice("sm1cs_tl004_call_bluff")
    return
label sm1cs_tl004_m02_c01:
    $ player.set_choice("sm1cs_tl004_pool_bet", 40)
    return
label sm1cs_tl004_m02_c02:
    $ player.set_choice("sm1cs_tl004_haggle_price")
    $ player.set_choice("sm1cs_tl004_pool_bet", 20)
    return
label sm1cs_tl004_m03_c01:
    $ player.set_choice("sm1cs_tl004_solids")
    return
label sm1cs_tl004_m04_c02:
    $ player.set_choice("sm1cs_tl004_middle_pocket")
    return
label sm1cs_tl004_m05_c01:
    $ player.set_choice("sm1cs_tl004_corner_pocket")
    return
label sm1cs_tl004_won_pool_game:
    $ player.set_choice("sm1cs_tl004_won_pool_game")
    return
label sm1cs_tl004_pay_bet:
    $ player.set_choice("sm1cs_tl004_pay_bet")
    $ player.spend_money(player.get_choice("sm1cs_tl004_pool_bet"), _("Pool bet with Taisia"), _("You lost ${} to Taisia in a pool game.").format(player.get_choice("sm1cs_tl004_pool_bet")))
    return
label sm1cs_tl004_got_kiss:
    $ player.set_choice("sm1cs_tl004_got_kiss")
    return