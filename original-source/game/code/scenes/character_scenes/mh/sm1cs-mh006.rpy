image sm1cs_mh006-glambot-1 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a47-3x-60fps.webm", start_image = "sm1cs-mh006-a47 mc-mh-walk2-glambot-000", image = "sm1cs-mh006-a47 mc-mh-walk2-glambot-120", loop = False)
image sm1cs_mh006-a52-1 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a52-1-2x-50fps.webm", start_image = "sm1cs-mh006-a52-1 mc-mh-anim-01")
image sm1cs_mh006-a52-1-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a52-1-2x-60fps.webm", start_image = "sm1cs-mh006-a52-1 mc-mh-anim-01")
image sm1cs_mh006-a52-2 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a52-2-2x-50fps.webm", start_image = "sm1cs-mh006-a52-2 mc-mh-anim-01")
image sm1cs_mh006-a52-2-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a52-2-2x-60fps.webm", start_image = "sm1cs-mh006-a52-2 mc-mh-anim-01")
image sm1cs_mh006-a52-3 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a52-3-2x-50fps.webm", start_image = "sm1cs-mh006-a52-3 mc-mh-anim-01")
image sm1cs_mh006-a52-3-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a52-3-2x-60fps.webm", start_image = "sm1cs-mh006-a52-3 mc-mh-anim-01")
image sm1cs_mh006-a56-1 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a56-1-2x-50fps.webm", start_image = "sm1cs-mh006-a56-1 mc-mh-anim-01")
image sm1cs_mh006-a56-1-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a56-1-2x-60fps.webm", start_image = "sm1cs-mh006-a56-1 mc-mh-anim-01")
image sm1cs_mh006-a56-2 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a56-2-2x-50fps.webm", start_image = "sm1cs-mh006-a56-2 mc-mh-anim-01")
image sm1cs_mh006-a56-2-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a56-2-2x-60fps.webm", start_image = "sm1cs-mh006-a56-2 mc-mh-anim-01")
image sm1cs_mh006-a56-3 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a56-3-2x-50fps.webm", start_image = "sm1cs-mh006-a56-3 mc-mh-anim-01")
image sm1cs_mh006-a56-3-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a56-3-2x-60fps.webm", start_image = "sm1cs-mh006-a56-3 mc-mh-anim-01")
image sm1cs_mh006-a56-4 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a56-4-2x-50fps.webm", start_image = "sm1cs-mh006-a56-4 mc-mh-anim-01")
image sm1cs_mh006-a56-4-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a56-4-2x-60fps.webm", start_image = "sm1cs-mh006-a56-4 mc-mh-anim-01")
image sm1cs_mh006-a58-1 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a58-1-2x-50fps.webm", start_image = "sm1cs-mh006-a58-1 mc-mh-anim-01")
image sm1cs_mh006-a58-1-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a58-1-2x-60fps.webm", start_image = "sm1cs-mh006-a58-1 mc-mh-anim-01")
image sm1cs_mh006-a58-2 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a58-2-2x-50fps.webm", start_image = "sm1cs-mh006-a58-2 mc-mh-anim-01")
image sm1cs_mh006-a58-2-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a58-2-2x-60fps.webm", start_image = "sm1cs-mh006-a58-2 mc-mh-anim-01")
image sm1cs_mh006-a58-3 = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a58-3-2x-50fps.webm", start_image = "sm1cs-mh006-a58-3 mc-mh-anim-01")
image sm1cs_mh006-a58-3-f = Movie(play = "images/Character-Scenes/mh/s006/anim/sm1cs-mh006-a58-3-2x-60fps.webm", start_image = "sm1cs-mh006-a58-3 mc-mh-anim-01")
label sm1cs_mh006:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 1.5, "sound3" )
    $ renpy.music.set_volume(0.8, 1.5, "music" )
    play music music_restaraunt_serenade fadein 2.0
    play sound3 sfx_cafe_crowd fadein 2.5 volume 0.6
    scene sm1cs-mh006-01 mc-mh-wine1_c1 with Fade(0.5, 0.5, 0.5)
    play voice2 mc_thinking_hmm2 noloop
    mc "How's work?"
    scene sm1cs-mh006-01 mc-mh-wine1_c2 with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "Same old, same old. Not much changes. Client needs a lawyer for a contract, or work dispute, I show up. I do the job, collect my retainer, head home to watch whatever's on the news."
    scene sm1cs-mh006-02 mc-mh-wine2_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "That sounds... Exhilirating."
    scene sm1cs-mh006-02 mc-mh-wine2_c2 with dissolve
    play voice3 lissa_haha2 noloop
    mh "Oh, it very much is. I've been thinking of picking up a new extreme sport."
    play sound sfx_drink_loop1 loop
    scene sm1cs-mh006-03 mc-mh-wine3_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Oh yeah? What extreme sport would that be?"
    stop sound fadeout 1.0
    scene sm1cs-mh006-03 mc-mh-wine3_c2 with dissolve
    play voice3 lissa_thinking2 noloop volume 1.8
    mh "Reading. I've always meant to give Emerson and Descartes some more face time, I figure now is as good a time as any."
    mh "What about you? How are things at the studio?"
    scene sm1cs-mh006-04 mc-mh-wine4_c1 with dissolve
    play sound sfx_drink_loop1 loop fadein 1.5
    play voice2 mc_yes_aga1 noloop
    mc "Kind of the same. Just a whole lot of work that I need to do."
    play voice3 lissa_thinking1 noloop
    mh "Hmmmm."
    mc "What?"
    scene sm1cs-mh006-04 mc-mh-wine4_c2 with dissolve
    play voice3 dahlia_no_simple noloop
    mh "Nothing, it's just good to see you being productive."
    scene sm1cs-mh006-05 mc-mh-wine5_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I don't know if I would call it 'productive'."
    stop sound fadeout 1.0
    scene sm1cs-mh006-05 mc-mh-wine5_c2 with dissolve
    play voice3 lissa_hey noloop
    mh "Rome wasn't built in a day."
    play voice2 mc_surprised_huh7 noloop
    mc "Huh?"
    mh "How long do you think it took me to build my legal practice?"
    play sound sfx_cup_slide1
    scene sm1cs-mh006-06 mc-mh-wine6_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I don't know. You're really good at your job. So like, 3 months?"
    scene sm1cs-mh006-06 mc-mh-wine6_c2 with dissolve
    play voice3 lissa_laugh noloop
    mh "You're incouragable. No, it took me years to get my clients. Between consistency, trust, meshing with each other - it wasn't an overnight matter."
    play voice2 mc_arrogant_huh3 noloop
    mc "Huh..."
    mh "But if you keep your nose to the grindstone, it will start to come together."
    scene sm1cs-mh006-09 mc-mh-look_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "I know you're right. I just want it to come together now."
    scene sm1cs-mh006-09 mc-mh-look_c2 with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "Don't we all?"
    mh "How are things with Stacy?"
    scene sm1cs-mh006-13 mc-mh-back_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Good! At least I think so."
    if player.is_storyline_item_finished(MS, "sm1ms007"):
        mc "We actually just went on a date! It went... Mostly well minus the little bit of shop talk we had to do..."
    else:
        mc "I do need to remember to take her out, but between our schedules it never feels like there's free time."
    scene sm1cs-mh006-13 mc-mh-back_c2 with dissolve
    play voice3 lissa_laugh2 noloop
    mh "Responsibilities."
    play voice2 mc_yes_yes1 noloop
    mc "Exactly."
    mh "Well... I'm glad you two are doing well."
    scene sm1cs-mh006-14 mc-mh-look_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I am... Pleasantly surprised to hear you say that, Lyssa."
    play voice3 dahlia_thinking_hmm4 noloop
    mh "Why?"
    mc "Well, from our first talk... I didn't think you were a big fan of Stacy's."
    scene sm1cs-mh006-14 mc-mh-look_c2 with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "I have... Really, no feelings about Stacy."
    play sound sfx_cloth_rustling2
    scene sm1cs-mh006-15 mc-mh-lean_c1 with dissolve
    play voice2 mc_happy_thatsgood noloop
    mc "That's... Well, different than what I was thinking."
    scene sm1cs-mh006-15 mc-mh-lean_c2 with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "Truthfully, the limited interactions I've had with Stacy, I have enjoyed her company."
    if persistent.is_special:
        mh "And I know she's your sister, and that she's important to you."
    else:
        mh "And I know you two are dating, and she's important to you."
    mh "I wouldn't actually mind spending more time with her. I think... When we started seeing each other, I was just nervous you wouldn't find time for me."
    play sound sfx_cloth_rustling1 volume 0.5
    scene sm1cs-mh006-07 mc-mh-hand1_c2 with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "But, I think I was wrong."
    scene sm1cs-mh006-07 mc-mh-hand1_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course I'll make time for you, Lyssa. Always."
    mc "And you know..."
    menu:
        "Offer to hang out - you, Lyssa, Stacy"(hint="sm1cs_mh006_m01_h01") if player.get_choice("sm1cs_mh003_thruple"):
            call sm1cs_mh006_m01_c01 from _call_sm1cs_mh006_m01_c01
            play voice2 mc_thinking_hmm4 noloop
            mc "We can all spend some time together. Learn a little bit more about each other."
            scene sm1cs-mh006-08 mc-mh-hand2_c2 with dissolve
            play voice3 dahlia_yes_ugu noloop
            mh "I would like that."
            mc "I think I would, too."
            jump sm1cs_mh006_after_choice
        "I don't need to talk about Stacy when we're together"(hint="sm1cs_mh006_m01_h02"):
            scene sm1cs-mh006-08 mc-mh-hand2_c1 with dissolve
            play voice2 mc_thinking_hmm4 noloop
            mc "When I'm here, it can be just you and me."
            scene sm1cs-mh006-08 mc-mh-hand2_c2 with dissolve
            play voice3 dahlia_no_nah noloop
            mh "You don't need to do that, [mcname]."
            play voice2 mc_thinking_mmm5 noloop
            mc "If it will make you more comfortable-"
            mh "What would make me more comfortable is knowing that we are both totally open and honest with each other."
            jump sm1cs_mh006_after_choice
label sm1cs_mh006_after_choice:
    play sound sfx_cloth_rustling2
    scene sm1cs-mh006-09 mc-mh-look_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "You know... There's something that's been bothering me a little bit..."
    play voice3 dahlia_thinking_hmm3 noloop
    mh "What's that?"
    mc "The other night, after the arcade. I thought we were having a nice moment, but then you kind of shut down..."
    scene sm1cs-mh006-09 mc-mh-look_c2 with dissolve
    play voice3 lissa_shyoh noloop
    mh "Yes, I've been meaning to apologize for that..."
    scene sm1cs-mh006-10 mc-mh-look2_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Can you tell me what happened?"
    scene sm1cs-mh006-10 mc-mh-look2_c2 with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "I... I wanted to hold out a little longer..."
    play voice2 d1s5_mcthinks noloop volume 1.4
    mc "What do you mean?"
    mh "When we first started seeing each other again, I... I told myself I would hold out until at least the third date. I wouldn't even think the word sex until you had wined and dined me enough."
    mh "But the other night..."
    scene sm1cs-mh006-14 mc-mh-look_c2 with dissolve
    play voice3 lissa_moan3 noloop
    mh "I don't know what it is about you, [mcname], but there is an intoxicating aura that surrounds you. Whenever I get close to you, I..."
    mh "God, I sound like a horny teenager."
    scene sm1cs-mh006-14 mc-mh-look_c1 with dissolve
    play voice2 mc_no_no6 noloop
    mc "No! No, not at all. Please, go on."
    mct "For the love of God, go on!"
    play sound sfx_cloth_rustling2 volume 0.5
    scene sm1cs-mh006-10 mc-mh-look2_c2 with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "The other night I caved to my... Baser instincts. I was... Not ashamed, or guilty, but... Not proud of it. I broke that promise to myself."
    play sound sfx_cloth_rustling4 volume 0.7
    scene sm1cs-mh006-11 mc-mh-hand1_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I am sorry for being so... Enticing, I guess?"
    scene sm1cs-mh006-11 mc-mh-hand1_c2 with dissolve
    play voice3 lissa_yes noloop
    mh "You should be sorry. The amount of trouble and turmoil you cause is truly astonishing."
    play voice2 mc_scared_oh2 noloop
    mc "Oh, I know."
    mh "Oh, [mcname]..."
    scene sm1cs-mh006-12 mc-mh-hand2_c1 with dissolve
    play voice2 mc_yes_yes8 noloop
    mc "Yes, Lyssa?"
    scene sm1cs-mh006-12 mc-mh-hand2_c2 with dissolve
    play voice3 lissa_moan1 noloop
    mh "I love being around you."
    scene sm1cs-mh006-13 mc-mh-back_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "And I love being around you."
    mc "So... You can think about sex again, huh?"
    scene sm1cs-mh006-13 mc-mh-back_c2 with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh? Someone's keeping track, huh."
    play voice2 mc_yes_yes7 noloop
    mc "Maaaaaaybe."
    mh "I see where your mind is."
    scene sm1cs-mh006-14 mc-mh-look_c1 with dissolve
    play voice2 mc_hey_hey8 noloop
    mc "Hey! I'm only thinking about it because you brought it up!"
    scene sm1cs-mh006-14 mc-mh-look_c2 with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "Are you trying to tell me that the guy running a porn studio only thinks about sex when it's brought up in conversation?"
    mc "..."
    scene sm1cs-mh006-15 mc-mh-lean_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, technically, I was thinking about it before, but I'm only {i}talking{/i} about it because you brought it up!"
    scene sm1cs-mh006-15 mc-mh-lean_c2 with dissolve
    play voice3 dahlia_arrogant_hm noloop
    mh "Mmmhmmmm. I'll believe that when pigs fly."
    scene sm1cs-mh006-16 mc-mh-lean2_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "Or when a shark bites a lawyer."
    scene sm1cs-mh006-16 mc-mh-lean2_c2 with dissolve
    play voice3 dahlia_surprised_what noloop
    mh "What? What do you mean 'when a shark bites a lawyer'?"
    scene sm1cs-mh006-17 mc-mh-ask_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. Because sharks don't bite lawyers. Professional courtesy."
    play sound sfx_hair_scratch1
    scene sm1cs-mh006-26-2 mc-mh-talk10_c1 with dissolve
    play voice3 lissa_haha noloop
    mh "That was okay. Off your game tonight."
    scene sm1cs-mh006-26-3 mc-mh-near_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "I'll take a pity chuckle."
    scene sm1cs-mh006-26-3 mc-mh-near_c2 with dissolve
    play voice3 dahlia_angry_oh noloop
    mh "You know, you are absolutely ridiculous."
    scene sm1cs-mh006-17 mc-mh-ask_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 2.0
    mc "Yeah, it's all a part of my charm!"
    play voice3 lissa_ugu2 noloop
    mh "Sure it is."
    mc "So... Third date... What are the chances?"
    scene sm1cs-mh006-16 mc-mh-lean2_c2 with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "We'll see, if you play it cool. Then, maybe."
    scene sm1cs-mh006-15 mc-mh-lean_c1 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Good enough for me!"
    scene sm1cs-mh006-26-2 mc-mh-talk10_c1 with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "It looks like our food is on it's way."
    scene sm1cs-mh006-27 mc-mh-wait_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Great, because I am starving!"
    scene sm1cs-mh006-27 mc-mh-wait_c2 with dissolve
    play voice3 dahlia_arrogant_heh noloop
    mh "Thinking about sex making you hungry?"
    scene sm1cs-mh006-27 mc-mh-wait_c1 with dissolve
    play voice2 mc_no_nope1 noloop
    mc "Nope.{w} Trying to resist the gravitational pull of your beauty has really worked up my appetite."
    play voice3 dahlia_happy_hmm2 noloop
    mh "You smooth talker."
    mc "I know."
    $ renpy.music.set_volume(0.6, 1.5, "music" )
    $ renpy.music.set_volume(1.0, 1.5, "sound2" )
    stop sound3 fadeout 1.5
    scene black
    show screen scene_transistion(_("After dinner"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound2 sfx_parknight_crickets fadein 2.0
    scene sm1cs-mh006-28 mc-mh-talk_c2
    with Fade(0.5, 0.5, 0.5)
    play voice3 dahlia_arrogant_huh noloop
    mh "... Well you know the real difference between a lawyer and a vampire, right, [mcname]?"
    scene sm1cs-mh006-28 mc-mh-talk_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Uhhh, nope."
    scene sm1cs-mh006-28 mc-mh-talk_c2 with dissolve
    play voice3 dahlia_arrogant_ha noloop
    mh "Law school."
    scene sm1cs-mh006-29 mc-mh-talk2_c1 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "That one was pretty good!"
    scene sm1cs-mh006-29 mc-mh-talk2_c2 with dissolve
    play voice3 lissa_laugh noloop
    mh "I don't know, I really liked your cement joke."
    scene sm1cs-mh006-29 mc-mh-talk2_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "That one is an absolute classic."
    mc "So..."
    play voice3 lissa_thinking1 noloop
    mh "So..."
    mc "I had a great time tonight, Lyssa."
    scene sm1cs-mh006-28 mc-mh-talk_c2 with dissolve
    play voice3 dahlia_yes_yeah4 noloop
    mh "I had a great time as well, [mcname]."
    scene sm1cs-mh006-28 mc-mh-talk_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "We should... Do it again, sometime, maybe?"
    play voice3 lissa_ugu noloop
    mh "I think that would be amenable to me."
    mc "Good. Good..."
    scene sm1cs-mh006-30 mc-mh-talk3_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "Wel, uhm... I guess-"
    scene sm1cs-mh006-30 mc-mh-talk3_c2 with dissolve
    play voice3 lissa_thinking2 noloop volume 1.8
    mh "You want to come in for tea, or something?"
    scene sm1cs-mh006-31 mc-mh-talk4_c1 with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Yes! Yeah, uhm, absolutely."
    mct "I don't know about tea, but I'm definitely down for something!"
    scene sm1cs-mh006-31 mc-mh-talk4_c2 with dissolve
    play voice3 mc_arrogant_tsktsk noloop
    mh "Tsk tsk, [mcname]. You're losing your cool."
    play voice2 mc_yes_yes2 noloop
    mc "You're right, I'm sorry."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh006-32 mc-mh-walk1_c1 with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "'Yeah, tea sounds cool. Or whatever.'"
    scene sm1cs-mh006-32 mc-mh-walk1_c2 with dissolve
    play voice3 dahlia_arrogant_pff noloop
    mh "Come on, before I change my mind, you weirdo."
    stop sound2 fadeout 3.0
    play sound3 sfx_door_closed2 noloop
    scene sm1cs-mh006-35 mc-mh-walk_c1 with dissolve
    play voice2 mc_angry_errr8 noloop
    mct "Hell yeah!!!"
    scene sm1cs-mh006-35 mc-mh-walk_c2 with dissolve
    pause
    scene sm1cs-mh006-36 mc-mh-walk2_c1 with dissolve
    pause
    play sound sfx_stove_turn_on1
    scene sm1cs-mh006-36 mc-mh-walk2_c2 with dissolve
    queue sound sfx_airhockey_hum volume 0.3 loop
    play voice2 mc_disappointed_off2 noloop
    mct "Oh... She meant actual tea..."
    scene sm1cs-mh006-37 mc-mh-ask1_c2 with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    mh "Disappointed?"
    scene sm1cs-mh006-37 mc-mh-ask1_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "Uh, huh? What?"
    scene sm1cs-mh006-37 mc-mh-ask1_c2 with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    mh "The look on your face. You look disappointed."
    scene sm1cs-mh006-38 mc-mh-ask2_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "What! Nahhhhh. I'm... Like, totally cool."
    scene sm1cs-mh006-38 mc-mh-ask2_c2 with dissolve
    play voice3 lissa_aga noloop
    mh "Sure, Casanova. What kind of tea do you want?"
    play voice2 d3s7_mcemm noloop
    mc "Uhm..."
    scene sm1cs-mh006-39 mc-mh-talk1_c1 with dissolve
    play voice2 d1s5_orgasm noloop
    mct "Shit! The only tea I can think of is a video game teabag and that is {u}very different.{/u}"
    mc "I'll have some... Jasper tea?"
    scene sm1cs-mh006-39 mc-mh-talk1_c2 with dissolve
    play voice3 dahlia_happy_laugh3 noloop
    mh "Did you mean jasmine?"
    scene sm1cs-mh006-40 mc-mh-talk2_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah! Jasmine, that's it."
    scene sm1cs-mh006-40 mc-mh-talk2_c2 with dissolve
    play voice3 dahlia_angry_oof noloop
    mh "Sometimes you are the smoothest man I've ever met. Other times, I'd swear you learned how to talk on the internet."
    scene sm1cs-mh006-41 mc-mh-walk1_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "If she only knew..."
    scene sm1cs-mh006-41 mc-mh-walk1_c2 with dissolve
    play voice3 lissa_hey noloop
    mh "I will be right back, just need to use the ladies room."
    play voice2 mc_yes_okay1 noloop
    mc "Okay! I will be right here, waiting for the tea to be ready."
    play sound2 sfx_heels_steps1
    scene sm1cs-mh006-42 mc-mh-walk2_c2 with dissolve
    pause
    stop sound2 fadeout 2.0
    scene sm1cs-mh006-42 mc-mh-walk2_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mct "I don't think I've ever used a teapot before..."
    mct "In fact, I don't think anyone has ever really made me tea..."
    play sound3 sfx_tea_kettle_whistle1 fadein 1.5
    mct "Is that weird?"
    stop music fadeout 6.0
    stop sound fadeout 3.0
    scene sm1cs-mh006-43 mc-mh-tea_c1 with dissolve
    play sound2 sfx_button_electro_click1 noloop
    play voice2 mc_scared_huh1 noloop
    mct "Oh shit! What did I do!?"
    scene sm1cs-mh006-43 mc-mh-tea_c2 with dissolve
    pause
    play sound sfx_tea_kettle_off1 fadein 1.0
    scene sm1cs-mh006-43 mc-mh-tea_c4 with dissolve
    stop sound3 fadeout 2.5
    play sound2 sfx_stove_turn_on1 noloop
    play voice2 mc_arrogant_hm1 noloop
    mct "Did I break it? Uhhh, I don't know what to do. Uhm, I guess I'll just turn off the stove?"
    scene sm1cs-mh006-44 mc-mh-stand_c1 with dissolve
    pause
    scene sm1cs-mh006-44 mc-mh-stand_c2 with dissolve
    play voice3 lissa_mmm1 noloop
    mh "Looks like our tea is ready."
    $ renpy.music.set_volume(0.8, 1.5, "music" )
    scene sm1cs-mh006-45 mc-mh-ask_c1 with dissolve
    play music music_latenight_whisp
    play voice2 mc_scared_huuuh3 noloop
    mc "..."
    play voice3 dahlia_thinking_hmm2 noloop
    mh "You okay?"
    play voice2 mc_yes_yes6 noloop volume 0.7
    mc "Yep. You look so damn good I was stunned silent."
    scene sm1cs-mh006-45 mc-mh-ask_c2 with dissolve
    play voice3 lissa_haha2 noloop
    mh "Well, since the tea is ready, I think it's time for the 'something else'."
    play sound sfx_barefoot_steps1 loop
    play sound2 sfx_heels_steps2 fadein 1.0
    scene sm1cs-mh006-47 mc-mh-walk2_c1 with dissolve
    pause
    scene sm1cs-mh006-a47 mc-mh-walk2-glambot-000 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 1.7>", sfx_camera_fly1] noloop volume 2.0
    scene sm1cs_mh006-glambot-1
    pause
    jump sm1cs_mh006_sex
label sm1cs_mh006_sex:
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mh006-49 mc-mh-ask_c2 with fade
    play voice3 dahlia_arrogant_heh noloop
    mh "You know, keeping your clothes on might make this harder than it needs to be."
    scene sm1cs-mh006-49 mc-mh-ask_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "You've got a good point."
    play sound sfx_skirt_off2 volume 1.8
    play sound2 sfx_cloth_tear1 noloop volume 0.5
    scene sm1cs-mh006-50 mc-mh-talk_c2 with dissolve
    play voice3 lissa_mmm2 noloop
    mh "Mmmmmmm..."
    play voice2 mc_surprised_uh1 noloop
    mc "Yeah?"
    mh "I missed this view a lot... I may have spent a few nights picturing this moment..."
    scene sm1cs-mh006-50 mc-mh-talk_c1 with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah? Well, in your fantasy, what's next?"
    play sound sfx_cloth_rustling2
    scene sm1cs-mh006-51 mc-mh-knee_c1 with dissolve
    play voice3 lissa_moan2 noloop
    mh "This."
    scene sm1cs-mh006-51 mc-mh-knee_c2 with dissolve
    play voice3 lissa_moan3 noloop
    mh "I have missed the taste of your dick, [mcname]."
    mh "And judging by how hard you are, it's missed being in my mouth."
    scene sm1cs-mh006-51 mc-mh-knee_c1 with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "More than you know."
    play voice3 dahlia_thinking_mmm2 noloop
    mh "Should we let them get reacquainted then?"
    play voice2 d9s2_mcyes noloop volume 2.5
    mc "God, yes."
    scene sm1cs-mh006-a52-1 mc-mh-anim-01 with dissolve
    pause
    scene sm1cs_mh006-a52-1
    play sound mc_sex_sucking_slow2 loop volume 0.6
    play voisex2 mc_sex_openmoans2
    play voisex3 lissa_sucking_deep
    mc "Fuck, Lyssa... You weren't lying when you said you missed my dick."
    mc "I've missed your blowjobs, so much... You know exactly what I want."
    pause
    scene sm1cs_mh006-a52-2 with dissolve
    mc "Oh shit, that's {i}fucking amazing!{/i}"
    mh "Gllllllck, glck, glck, gllllllllllcccccck!"
    pause
    scene sm1cs_mh006-a52-3 with dissolve
    mc "If I could, I wouldn't ever let you stop... This is just so wonderful..."
    mc "Your lips wrapped around me, your head bobbing down on my cock, your tongue - God, your tongue!"
    pause
    play sound mc_sex_sucking_fast2 loop volume 0.6
    scene sm1cs_mh006-a52-1-f with dissolve
    play voisex2 mc_sex_openmoans3
    mh "Glck, glck, glck!"
    mc "If you're not careful-"
    pause
    scene sm1cs_mh006-a52-2-f with dissolve
    mc "-Jesus, I want to cum down your throat. Holllly guacamollllley!"
    mc "Yeah, just like that - fuh - just like that!"
    pause
    scene sm1cs_mh006-a52-3-f with dissolve
    mh "Glck, glck, glck, glck."
    mc "I'm so close, Lyssa. Gah, I'm close!"
    stop voisex2 fadeout 1.0
    stop sound fadeout 1.0
    scene sm1cs-mh006-53 mc-mh-undress1_c2 with dissolve
    play voisex3 lissa_moan5 noloop
    mh "I can't wait any longer, [mcname]."
    mh "Please, will you fuck me?"
    scene sm1cs-mh006-53 mc-mh-undress1_c1 with dissolve
    play voisex2 mc_happy_hah2 noloop
    mc "I would be an idiot to say no."
    play sound sfx_cloth_dress_off3
    scene sm1cs-mh006-54 mc-mh-undress2_c2 with dissolve
    play voisex3 dahlia_thinking_hmm3 noloop
    mh "I've been waiting for this... I... I've missed this, so much... Missed you..."
    scene sm1cs-mh006-54 mc-mh-undress2_c1 with dissolve
    play voisex2 d1s5_mchappy noloop volume 1.6
    mc "Sounds like I need to make up for lost time."
    play sound sfx_cloth_rustling4
    scene sm1cs-mh006-55 mc-mh-knee_c2 with dissolve
    play voisex3 lissa_ugu3 noloop
    mh "Please."
    scene sm1cs-mh006-a56-1 mc-mh-anim-01 with dissolve
    pause
    scene sm1cs_mh006-a56-1
    play voisex2 d7s4_mcbreathing
    play voisex3 dahlia_sex_openmoans2 volume 0.8
    play sound sfx_vagina_penetration1_fast loop volume 0.6
    mh "Oh my - [mcname]!"
    mc "Are you okay?"
    pause
    scene sm1cs_mh006-a56-2 with dissolve
    mh "I'm more than okay! Fnnnnng - I'm in {i}heaven{/i}!"
    pause
    scene sm1cs_mh006-a56-3 with dissolve
    mh "I forgot how incredible this felt - how perfect your dick feels inside me."
    mh "Your cock fills me up, and stretches me - Mmmmmmmm! It's nothing short of {i}perfect!{/i}"
    pause
    scene sm1cs_mh006-a56-4 with dissolve
    mc "And you're so incredibly tight. Jesus, I don't think I could pull my dick out if I tried!"
    mh "{i}Don't you dare, [mcname].{/i}"
    pause
    scene sm1cs_mh006-a56-1-f with dissolve
    mc "I wouldn't dream of it."
    mh "Good, because - ohh, ohhhh, yessss - I need you to cum in meee."
    pause
    scene sm1cs_mh006-a56-2-f with dissolve
    mh "I need to feel you fill me up, your warm, sticky cum coating my insides."
    mc "Goddamn, Lyssa..."
    mh "I've been thinking about this... A lot. And I just need to remember what it feels like."
    pause
    scene sm1cs_mh006-a56-3-f with dissolve
    mc "I think I can fulfill your fantasy."
    mh "Good. Because you've already filled me today."
    pause
    scene sm1cs_mh006-a56-4-f with dissolve
    mc "Mmmmnnngnnnngggg, I'm getting close!"
    mh "Flip me over, I want to see you cum!"
    pause
    stop voisex2 fadeout 1.0
    play sound sfx_cloth_rustling3
    scene sm1cs-mh006-57 mc-mh-move_c2 with dissolve
    play voisex3 dahlia_sex_closedmoan2 noloop
    mh "What are you-"
    play sound sfx_fisting_fist1 volume 0.6
    scene sm1cs-mh006-58 mc-mh-animation3_c2 with dissolve
    play voisex3 lissa_moan8 noloop
    mh "Oh my God!!!"
    play voisex2 mc_yes_yeah8 noloop
    mc "Yeah?"
    play voisex3 dahlia_sex_closedmoan1 noloop
    mh "Fuhhh - that felt -"
    scene sm1cs-mh006-58 mc-mh-animation3_c1 with dissolve
    play voisex2 mc_thinking_hmm8 noloop
    mc "Almost as good as this?"
    scene sm1cs-mh006-a58-1 mc-mh-anim-01 with dissolve
    pause
    scene sm1cs_mh006-a58-1
    play sound sfx_vagina_penetration1_fast loop volume 0.6
    play voisex2 d7s4_mcbreathing
    play voisex3 dahlia_sex_openmoans1
    mh "Oh my {i}GOD!{/i}"
    mh "Don't stop, [mcname], please don't stop!"
    scene sm1cs_mh006-a58-2 with dissolve
    mh "You're going to make me cum - holy shit, you're going to make me cum!"
    mc "I can feel myself getting close..."
    scene sm1cs_mh006-a58-3 with dissolve
    mh "I want to cum together, {i}I need us to cum together!{/i}"
    pause
    scene sm1cs_mh006-a58-1-f with dissolve
    mh "Your dick is getting so much deeper now, holy - mmmmmmmm!"
    pause
    mc "Lyssa, fuuuuuuuuhhhhg, Lyssa!"
    mh "Yes, [mcname], yes!"
    scene sm1cs_mh006-a58-2-f with dissolve
    mc "Gaaaahh, I'm going to - fuuuuuck!"
    mh "Yes! Yes, yes, yes!"
    mh "God yes, fill me up! Shoot your cum deep inside my ass! Yes, yes, yes!"
    pause
    scene sm1cs_mh006-a58-3-f with dissolve
    mc "Fuck, Lyssa, I'm cummmmmming!"
    mh "Yes! {i}Yes! YES! I'M CUMMING!{/i}"
    play voisex2 mc_sex_orgasm5 noloop
    play voisex3 lissa_moan8 noloop
    play sound mc_cum_sound1
    scene sm1cs-mh006-59 mc-mh-cum_c1 with hpunch
    mh "Ohhhh fuuUUUCK!"
    play voisex3 lissa_moan10 noloop
    queue voisex2 d1s5_orgasm2 noloop
    play sound2 mc_cum_sound1 noloop
    scene sm1cs-mh006-59 mc-mh-cum_c2 with hpunch
    pause
    $ renpy.music.set_volume(0.4, 5.0, "music" )
    play sound sfx_cloth_rustling4
    scene sm1cs-mh006-60 mc-mh-down_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Everything you had imagined?"
    scene sm1cs-mh006-60 mc-mh-down_c2 with dissolve
    play voice3 lissa_lno noloop
    mh "No. It was better than I could have ever dreamed."
    play voice2 mc_happy_a1 noloop
    mc "Good. That's what we aim to do here."
    scene sm1cs-mh006-61 mc-mh-ask_c2 with dissolve
    play voice3 dahlia_arrogant_huh noloop
    mh "We?"
    scene sm1cs-mh006-61-2 mc-mh-ask2_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, me and you."
    mc "We aim to have the best sex possible."
    scene sm1cs-mh006-61-2 mc-mh-ask2_c2 with dissolve
    play voice3 lissa_laugh2 noloop
    mh "Well I think we exceeded those expectations tonight."
    scene sm1cs-mh006-62 mc-mh-look_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I think so, too."
    scene sm1cs-mh006-62 mc-mh-look_c2 with dissolve
    play voice3 lissa_moan1 noloop
    mh "Hell, I think you might have fucked me into a coma... I can't move an inch."
    play voice2 mc_yes_ugu1 noloop
    mc "Neither can I."
    play sound sfx_cloth_rustling2
    scene sm1cs-mh006-62-2 mc-mh-look_c1 with dissolve
    play voice2 d7s6_moan2 noloop
    mc "But I should get up, otherwise, I'll fall asleep here."
    play voice3 lissa_aga noloop
    mh "That's fine."
    mc "Really? What happened to taking it slow?"
    scene sm1cs-mh006-62-2 mc-mh-look_c2 with dissolve
    play voice3 lissa_haha noloop
    mh "It's not like you're leaving a toothbrush in the bathroom. Besides, I don't have the energy to kick you out."
    scene sm1cs-mh006-63 mc-mh-snuggle_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Well, how can I say no to spending the night with a beautiful woman?"
    mc "Should I get you a towel or something?"
    play voice3 dahlia_happy_hmm2 noloop
    mh "Hmmm? Why?"
    mc "Well, you made a mess of yourself."
    scene sm1cs-mh006-63 mc-mh-snuggle_c2 with dissolve
    play voice3 lissa_oh2 noloop
    mh "It's fine, I'll deal with it in the morning."
    play voice2 mc_thinking_mmm4 noloop
    mc "Sounds good to me."
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    scene sm1cs-mh006-64 mc-mh-snuggle2_c1 with dissolve
    play voice2 d7s6_snoring fadein 3.0
    play voice3 girl27_disappointed_snoring fadein 5.0
    pause
    scene sm1cs-mh006-64 mc-mh-snuggle2_c2 with dissolve
    pause
    scene sm1cs-mh006-64 mc-mh-snuggle2_c3 with dissolve
    pause
    stop voice3 fadeout 2.0
    $ renpy.music.set_volume(0.2, 3.0, "music" )
    scene sm1cs-mh006-65 mc-morning1_c2 with fade
    pause
    play voice2 d7s6_moan1 noloop
    scene sm1cs-mh006-66 mc-morning2_c1 with dissolve
    mc "Mmmmmm, morning, Lyssa."
    play sound sfx_cloth_rustling5
    scene sm1cs-mh006-67 mc-morning3_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Lyssa?"
    scene sm1cs-mh006-67 mc-morning3_c2 with dissolve
    pause
    play sound sfx_paper_slide1
    scene sm1cs-mh006-68 mc-morning4_c1 with dissolve
    play voice3 lissa_hey_reverbed1 noloop
    mct "\"[mcname], got an early morning call from a client, had to run to the office. I loved our date last night, hope to do it again soon. x o, Lyssa.\""
    scene sm1cs-mh006-68 mc-morning4_c2 with dissolve
    play voice2 mc_thinking_hm noloop
    mct "I hope we get to do that again real soon, too.{w} But I should probably get a start on the day."
    scene sm1cs-mh006-69 mc-morning5_c2 with dissolve
    pause
    play sound sfx_jeans_on1
    scene sm1cs-mh006-70 mc-end_c1 with dissolve
    call sm1cs_mh006_get_point from _call_sm1cs_mh006_get_point
    pause
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    jump sm1cs_mh006_exit
label sm1cs_mh006_exit:
    if vn_mode:
        $ StoryController.end_scene(MH_STORY)
        return
    $ gt.update(23, 0, 0)
    $ player.progress_storyline(MH_STORY, 1)
    $ player.sleep()
    return
label sm1cs_mh006_m01_c01:
    $ player.set_choice("sm1cs_mh006_thruple")
    return
label sm1cs_mh006_get_point:
    $ CharacterController.get_character("mh").add_point(2)
    $ player.set_choice("sm1cs_mh006_got_point")
    return
label sm1cs_mh006_unlocks:
    call sm1cs_mh006_get_point from _call_sm1cs_mh006_get_point_1
    call sm1cs_mh006_m01_c01 from _call_sm1cs_mh006_m01_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(MH_STORY)
    return