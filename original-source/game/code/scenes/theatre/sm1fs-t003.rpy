image sm1fs_t003-glambot-1 = Movie(play = "images/FS_T/s003/anim/sm1fs_t003-a03-anim.webm", start_image = "sm1fs_t003-a03 mc-tl-vs-dv-km-talk1-glambot-03-000", image = "sm1fs_t003-a03 mc-tl-vs-dv-km-talk1-glambot-03-179", loop = False)
label sm1fs_t003:
    $ renpy.music.set_volume(0.5, 0.5, "music" )
    $ renpy.music.set_volume(0.35, 0.0, "music2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music2 music_theater_fallenfriends fadein 2.0
    play sound sfx_double_door1
    scene sm1fs_t003-01 mc-tl-vs-dv-km-entry1_c1 with fade
    play voice2 mc_thinking_hm noloop
    mct "Definitely looks like I found the right place."
    scene sm1fs_t003-01 mc-tl-vs-dv-km-entry1_c2 with dissolve
    pause
    $ renpy.music.set_volume(0.8, 1.0, "music2" )
    scene sm1fs_t003-03 mc-tl-vs-dv-km-talk1_c3 with dissolve
    play voice4 girl31_hey_angry noloop
    km "Did you see those texts?"
    scene sm1fs_t003-03 mc-tl-vs-dv-km-talk1_c4 with dissolve
    play voice5 girl33_yes_serious noloop
    vs "Oh yes, I saw them all. Sent romantic novellas that should have never been published."
    scene sm1fs_t003-04 mc-tl-vs-dv-km-talk2_c3 with dissolve
    play voice4 girl31_disappointed_ehh3 noloop
    km "Doesn't matter, he hit send."
    scene sm1fs_t003-04 mc-tl-vs-dv-km-talk2_c4 with dissolve
    play voice5 girl33_disappointed_oh noloop
    vs "True, but even the send button regrets that."
    scene sm1fs_t003-05 mc-tl-vs-dv-km-talk3_c3 with dissolve
    play voice4 girl31_surprised_uh1 noloop
    km "Don't you want to know who's writing love poems about you, though?"
    $ renpy.music.set_volume(0.35, 1.0, "music2" )
    play sound sfx_carpet_footsteps2 loop
    scene sm1fs_t003-02 mc-tl-vs-dv-km-entry2_c1 with dissolve
    pause
    scene sm1fs_t003-02 mc-tl-vs-dv-km-entry2_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1fs_t003-a03 mc-tl-vs-dv-km-talk1-glambot-03-000 with dissolve
    play voice3 girl24_surprised_wow1 noloop
    tl "*Quietly* Fuck me. You actually came."
    play sound sfx_camera_fly1 volume 2.0
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1fs_t003-glambot-1
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1fs_t003-03 mc-tl-vs-dv-km-talk1_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "I mean, yeah. You said-"
    scene sm1fs_t003-04 mc-tl-vs-dv-km-talk2_c2 with dissolve
    play voice3 stacy_shhh noloop
    tl "*Quietly* Shhh, keep your voice down."
    scene sm1fs_t003-04 mc-tl-vs-dv-km-talk2_c1 with dissolve
    play voice2 d2s9_confused noloop
    mc "*Quietly* Sorry. You said they were looking for someone, and Stacy would not shut up about getting some practice."
    mc "*Quietly* So here I am."
    scene sm1fs_t003-05 mc-tl-vs-dv-km-talk3_c2 with dissolve
    play voice3 girl24_arrogant_huh1 noloop
    tl "*Quietly* Huh, well that's actually kind of tight. You seem all right, and we could definitely use some good dick around here."
    scene sm1fs_t003-05 mc-tl-vs-dv-km-talk3_c1 with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "Whaaaaa-"
    scene sm1fs_t003-05 mc-tl-vs-dv-km-talk3_c2 with dissolve
    play voice3 girl24_arrogant_pff noloop
    tl "*Quietly* Shh, otherwise you're going to piss Denise off."
    play voice2 d1s2_hmm noloop
    mc "*Quietly* Shit, sorry... Who's Denise?"
    scene sm1fs_t003-06 mc-tl-vs-dv-km-point1_c2 with dissolve
    play voice3 girl24_thinking_emm1 noloop
    tl "*Quietly* That's her. She's the director, and she's not been in a great mood lately."
    scene sm1fs_t003-06 mc-tl-vs-dv-km-point1_c3 with dissolve
    pause
    scene sm1fs_t003-06 mc-tl-vs-dv-km-point1_c1 with dissolve
    play voice2 mc_surprised_why1 noloop
    mc "*Quietly* Why?"
    play voice3 girl24_happy_laugh1 noloop
    tl "*Quietly* I have my theories, but if you ask her it's because we're doing modern Shakespeare."
    scene sm1fs_t003-07 mc-tl-vs-dv-km-node_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "*Quietly* Huh? Isn't Shakespeare like hundreds of years old."
    scene sm1fs_t003-07 mc-tl-vs-dv-km-node_c2 with dissolve
    play voice3 girl24_arrogant_yeah1 noloop
    tl "*Quietly* Yeah, but it's chic to take old Shakespeare and make it contemporary. You know, modern English, modern situations, that kind of shit. And it's fucking awful. Just listen."
    $ renpy.music.set_volume(0.8, 1.0, "music2" )
    scene sm1fs_t003-07 mc-tl-vs-dv-km-node_c3 with dissolve
    play voice4 girl31_arrogant_hm2 noloop
    km "You're going to want his dick the second I say who it is."
    scene sm1fs_t003-07 mc-tl-vs-dv-km-node_c4 with dissolve
    play voice5 girl33_disappointed_aah noloop
    vs "Just tell me! Is he hot? Or kind of fugly? Oooo, does he have a beard!"
    scene sm1fs_t003-05 mc-tl-vs-dv-km-talk3_c3 with dissolve
    play voice4 girl31_no_nah noloop
    km "It's not really a beard, more like some scruff."
    scene sm1fs_t003-08 mc-tl-vs-dv-km-talk_c4 with dissolve
    play voice5 girl33_disappointed_geh noloop
    vs "He'll grow some more, probs. Unless you don't tell me whose chin it is!"
    scene sm1fs_t003-08 mc-tl-vs-dv-km-talk_c3 with dissolve
    play voice4 girl31_thinking_emm3 noloop
    km "It's... Fuck I forgot his name."
    stop music2 fadeout 1.0
    play sound sfx_music_shutdown2
    play music "<silence 3.0>"
    $ renpy.music.set_volume(0.2, 0.0, "music" )
    scene sm1fs_t003-08 mc-tl-vs-dv-km-talk_c5 with dissolve
    $ renpy.music.set_volume(0.5, 10.0, "music" )
    queue music music_1784_lofi
    play voice6 girl34_angry_argh4 noloop
    dvh "That is enough for now. Everyone... Take a break. Stretch, walk it off. Make sure Kellie gets the line."
    scene sm1fs_t003-09 mc-tl-vs-dv-km-walk1_c2 with dissolve
    play voice3 girl24_happy_yeah3 noloop
    tl "Now's our moment to introduce you to Denise."
    scene sm1fs_t003-09 mc-tl-vs-dv-km-walk1_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, but you don't need to drag me."
    play voice3 girl24_arrogant_hm2 noloop
    tl "Whatever."
    scene sm1fs_t003-09 mc-tl-vs-dv-km-walk1_c3 with dissolve
    play voice6 girl34_angry_breath1 noloop
    dvh "*Quietly* Als ik deze toneelschrijver ooit ontmoet, beloof ik dat ik zijn tong door zijn kont naar buiten zal trekken..."
    play sound sfx_carpet_footsteps2 loop
    scene sm1fs_t003-10 mc-tl-vs-dv-km-walk2_c1 with dissolve
    play voice3 girl24_hey_greeting noloop
    tl "Hey Denise, there's someone I want to introduce to you."
    scene sm1fs_t003-10 mc-tl-vs-dv-km-walk2_c2 with dissolve
    play voice3 girl24_thinking_emm2 noloop
    tl "This is [mcname]. [mcname], meet Denise Van der Haute, the director of the group."
    scene sm1fs_t003-10 mc-tl-vs-dv-km-walk2_c3 with dissolve
    play voice6 girl34_hey_scandalized2 noloop
    dvh "Hallo. Welcome to this... masterwork of Dante."
    play voice2 mc_surprised_uh1 noloop
    mc "Oh who?"
    play voice6 girl34_no_nah2 noloop
    dvh "Never mind."
    stop sound fadeout 1.0
    scene sm1fs_t003-12 mc-tl-vs-dv-km-talk2_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "It's nice to meet you, Denise. I love your accent, too."
    scene sm1fs_t003-12 mc-tl-vs-dv-km-talk2_c3 with dissolve
    play voice6 girl34_arrogant_ha4 noloop
    dvh "It is Dutch."
    scene sm1fs_t003-13 mc-tl-vs-dv-km-talk3_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Huh. Is that what you were speaking when we came over here?"
    scene sm1fs_t003-13 mc-tl-vs-dv-km-talk3_c3 with dissolve
    play voice6 girl34_arrogant_yeah noloop
    dvh "Yah."
    play voice2 d2s12_emmm noloop
    mc "Uhm..."
    mct "Come on, [mcname], be cool!"
    scene sm1fs_t003-14 mc-tl-vs-dv-km-talk4_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "What were you saying to yourself?"
    scene sm1fs_t003-13 mc-tl-vs-dv-km-talk3_c3 with dissolve
    play voice6 girl34_disappointed_eeh2 noloop
    dvh "This is fine. Everything is fine."
    play voice2 mc_arrogant_heh2 noloop
    mc "Huh."
    scene sm1fs_t003-11 mc-tl-vs-dv-km-talk1_c3 with dissolve
    play voice6 girl34_arrogant_huh1 noloop
    dvh "Taisia, why have you brought this bumbling man to me?"
    scene sm1fs_t003-11 mc-tl-vs-dv-km-talk1_c2 with dissolve
    play voice3 girl24_disappointed_eeh1 noloop
    tl "I convinced him to try out. You know, maybe join the team."
    scene sm1fs_t003-14 mc-tl-vs-dv-km-talk4_c3 with dissolve
    play voice6 girl34_angry_argh2 noloop
    dvh "You are joking, no? This man can barely string together three words together. How will he perform for a crowd?"
    scene sm1fs_t003-11 mc-tl-vs-dv-km-talk1_c1 with dissolve
    play voice3 girl24_no_nonono1 noloop
    tl "Trust me, Denise. He's got it in him."
    play voice6 girl34_disappointed_oh2 noloop
    dvh "Trust you like I used to trust you to do your own makeup?"
    scene sm1fs_t003-15 mc-tl-vs-dv-km-talk5_c2 with dissolve
    play voice3 girl24_angry_argh4 noloop
    tl "That play needed something horrific! This bippity-boppity bullshit is awful, and we needed a monster. So I dressed like a monster."
    scene sm1fs_t003-15 mc-tl-vs-dv-km-talk5_c3 with dissolve
    play voice6 girl34_disappointed_mmf4 noloop
    dvh "*Quietly* You are not entirely wrong."
    scene sm1fs_t003-16 mc-tl-vs-dv-km-talk6_c2 with dissolve
    play voice3 girl24_arrogant_huh2 noloop
    tl "What was that?"
    scene sm1fs_t003-11 mc-tl-vs-dv-km-talk1_c3 with dissolve
    play voice6 girl34_angry_ahem1 noloop
    dvh "*Coughs* I expressly told you {i}nee{/i} when you asked. Then you did it anyway. Do you know how much trouble you brought me?"
    dvh "The theater's owners brought their grandchildren that night! The brats had nightmares for weeks!"
    scene sm1fs_t003-16 mc-tl-vs-dv-km-talk6_c3 with dissolve
    play voice6 girl34_angry_nergh noloop
    dvh "You are lucky to still be working here after that incident. I would not push my luck if I was you."
    scene sm1fs_t003-16 mc-tl-vs-dv-km-talk6_c2 with dissolve
    play voice3 girl24_yes_simple2 noloop
    tl "... Yes, Denise."
    scene sm1fs_t003-13 mc-tl-vs-dv-km-talk3_c3 with dissolve
    play voice6 girl34_thinking_emm1 noloop
    dvh "Ahem. All that aside, we do need more men to act. I will give you an audition, [mcname]."
    scene sm1fs_t003-14 mc-tl-vs-dv-km-talk4_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Wait... Really?"
    scene sm1fs_t003-17 mc-tl-vs-dv-km-talk7_c1 with dissolve
    play voice6 girl34_yes_neutral4 noloop
    dvh "Yes. It is mostly women here at the theater, and not all plays are solely women. Besides, I believe Veronica may be growing tired of kissing women."
    scene sm1fs_t003-17 mc-tl-vs-dv-km-talk7_c2 with dissolve
    play voice6 girl34_thinking_hmm7 noloop
    dvh "Or perhaps, maybe not. Either way, if you have what it takes, I'm sure I can find roles suited for you."
    dvh "Let us see what you can do."
    scene sm1fs_t003-16 mc-tl-vs-dv-km-talk6_c1 with hpunch
    play voice2 mc_thinking_wait1 noloop
    mc "Wait... Like, right now?"
    scene sm1fs_t003-13 mc-tl-vs-dv-km-talk3_c3 with dissolve
    play voice6 girl34_yes_yeah8 noloop
    dvh "Yah. We are on a break, this is the perfect moment."
    play voice2 mc_disappointed_ehh5 noloop
    mc "Okay... Uhh, what should I do?"
    scene sm1fs_t003-18 mc-tl-vs-dv-km-talk8_c2 with hpunch
    play voice6 girl34_hey_scandalized4 noloop
    dvh "Veronica!"
    scene sm1fs_t003-18 mc-tl-vs-dv-km-talk8_c3 with dissolve
    play voice5 girl33_hey_serious noloop
    vs "Yes, Ms. Van der Haute?"
    scene sm1fs_t003-19 mc-tl-vs-dv-km-talk9_c1 with dissolve
    play voice6 girl34_thinking_eeh1 noloop
    dvh "Grab one of the scripts. This is [mcname]. He's going to audition to join us. I want him to read lines with you."
    scene sm1fs_t003-19 mc-tl-vs-dv-km-talk9_c3 with dissolve
    play voice5 girl33_surprised_ohmy noloop
    vs "Of course! {w}Oh my goodness!"
    scene sm1fs_t003-19 mc-tl-vs-dv-km-talk9_c2 with dissolve
    play voice6 girl34_arrogant_huh2 noloop
    dvh "*sighs* What is it now, Veronica?"
    scene sm1fs_t003-19 mc-tl-vs-dv-km-talk9_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "That was a weird reaction."
    play voice5 girl33_thinking_eem2 noloop
    vs "Oh, uhm, nothing! What scene would you like us to do?"
    play voice6 girl34_thinking_hmm6 noloop
    dvh "There is the part, between Rosalind and Orlando in the same act and scene. Just read that."
    scene sm1fs_t003-20 mc-tl-vs-dv-km-talk10_c3 with dissolve
    play voice5 girl33_surprised_huh3 noloop
    vs "The part between Rose and Orley?"
    play sound sfx_cloth_rustling2
    scene sm1fs_t003-20 mc-tl-vs-dv-km-talk10_c2 with dissolve
    play voice6 girl34_angry_argh6 noloop
    dvh "*Sighs*"
    dvh "Yah. Between Rose and Orley."
    play sound sfx_cloth_rustling4
    scene sm1fs_t003-21 mc-tl-vs-dv-km-talk11_c2 with dissolve
    play voice6 girl34_hey_simple3 noloop
    dvh "Quickly. I do not have the whole day."
    scene sm1fs_t003-21 mc-tl-vs-dv-km-talk11_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Uhm... Okay."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t003-22 mc-tl-vs-dv-km-walk1_c1 with dissolve
    mct "Here goes nothing I guess."
    scene sm1fs_t003-22 mc-tl-vs-dv-km-walk1_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1fs_t003-23 mc-tl-vs-dv-km-stand1_c2 with dissolve
    mct "She's pretty cute. Seems friendlier than Denise at least."
    scene sm1fs_t003-24 mc-tl-vs-dv-km-stand2_c2 with dissolve
    play voice5 girl33_hey_involved noloop
    vs "Hi! I'm Veronica! I'll be your scene partner!"
    scene sm1fs_t003-24 mc-tl-vs-dv-km-stand2_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Hi Veronica. I'm [mcname]."
    scene sm1fs_t003-24 mc-tl-vs-dv-km-stand2_c2 with dissolve
    play voice5 girl33_happy_relief noloop
    vs "I know, it's so awesome to meet you!"
    play sound sfx_paper_slide1
    scene sm1fs_t003-25 mc-tl-vs-dv-km-stand3_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mct "Hmmm. There is something off about her."
    mc "Veronica, have wet met before?"
    scene sm1fs_t003-25 mc-tl-vs-dv-km-stand3_c2 with dissolve
    play voice5 girl33_no_nah noloop
    vs "Uhm, no. Not really."
    stop music fadeout 3.0
    scene sm1fs_t003-29 mc-tl-vs-dv-km-talk2_c3 with vpunch
    $ renpy.music.set_volume(0.4, 0.0, "music2" )
    play music2 music_theater_fallenfriends fadein 3.0
    play voice6 girl34_angry_ahem4 noloop
    dvh "Chop chop! I don't have all day."
    scene sm1fs_t003-29 mc-tl-vs-dv-km-talk2_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Of course, uhhh..."
    scene sm1fs_t003-29 mc-tl-vs-dv-km-talk2_c2 with dissolve
    play voice5 girl33_surprised_huh4 noloop
    vs "Nervous?"
    scene sm1fs_t003-30 mc-tl-vs-dv-km-talk3_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Uhm... A bit."
    scene sm1fs_t003-30 mc-tl-vs-dv-km-talk3_c2 with dissolve
    play voice5 girl33_happy_laugh1 noloop
    vs "Don't worry, I'll do what I can to help!"
    scene sm1fs_t003-31 mc-tl-vs-dv-km-talk4_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thank you, I appreciate that."
    scene sm1fs_t003-31 mc-tl-vs-dv-km-talk4_c2 with dissolve
    play voice5 girl33_thinking_hmm3 noloop
    vs "I always picture everyone naked, that helps me!"
    scene sm1fs_t003-33 mc-tl-vs-dv-km-stand1_c1 with dissolve
    play voice2 mc_disgust_meh4 noloop
    mct "Christ, all that'll do is give me a boner. It's just like high school all over again..."
    play sound sfx_cloth_rustling3
    scene sm1fs_t003-33 mc-tl-vs-dv-km-stand1_c3 with dissolve
    play voice6 girl34_arrogant_huh3 noloop
    dvh "Prepared?"
    scene sm1fs_t003-34 mc-tl-vs-dv-km-walk1_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "I guess so."
    $ renpy.music.set_volume(0.8, 3.0, "music2" )
    play voice6 girl34_yes_ugu1 noloop
    dvh "The curtain rises, and..."
    scene sm1fs_t003-34-02 mc-tl-vs-dv-km-walk1_c2 with dissolve
    play voice5 girl33_arrogant_huh1 noloop
    vs "Did ya' hear me?"
    play voice2 mc_yes_yeah7 noloop
    mc "Erm... Uh, yeah. What's up?"
    scene sm1fs_t003-35 mc-tl-vs-dv-km-walk2_c1 with dissolve
    play voice5 girl33_disappointed_off noloop
    vs "Do you know what time it is?"
    play voice2 mc_no_no1 noloop
    mc "I don't have a watch."
    scene sm1fs_t003-33 mc-tl-vs-dv-km-stand1_c2 with dissolve
    play voice5 girl33_disappointed_mmf1 noloop
    vs "Then there are no hotties around, because hotties got that plain Jane."
    play voice2 mc_thinking_hmm2 noloop
    mc "I've got my phone, though."
    play voice5 girl33_no_uhuh noloop
    vs "Lame. Everyone needs a watch piece. Because you know who can tell the time?"
    scene sm1fs_t003-34-02 mc-tl-vs-dv-km-walk1_c2 with dissolve
    play voice2 d3s7_mcemm noloop volume 1.5
    mc "Uhh, who tells time?"
    play voice5 girl33_thinking_hmm1 noloop
    vs "A guy with a hot fiance, a hot fiance who's going to be married in a week. Which feels like forever away."
    scene sm1fs_t003-34 mc-tl-vs-dv-km-walk1_c2 with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "But, erm, who has the time?"
    stop music2 fadeout 1.0
    play sound sfx_music_shutdown2
    play music "<silence 2.0>"
    $ renpy.music.set_volume(0.2, 0.0, "music" )
    scene sm1fs_t003-34 mc-tl-vs-dv-km-walk1_c3 with dissolve
    $ renpy.music.set_volume(0.5, 10.0, "music" )
    queue music music_1784_lofi
    play voice6 girl34_arrogant_aga noloop
    dvh "I have seen enough."
    scene sm1fs_t003-30 mc-tl-vs-dv-km-talk3_c2 with dissolve
    play voice5 girl33_surprised_wow noloop
    vs "Hey, you did great!"
    play voice2 mc_yes_ugu1 noloop
    mc "Thanks."
    scene sm1fs_t003-36 mc-tl-vs-dv-km-walk3_c3 with dissolve
    play voice6 girl34_yes_yeap4 noloop
    dvh "Hmmm. {w}I think you posess some talent, [mcname]."
    scene sm1fs_t003-34 mc-tl-vs-dv-km-walk1_c2 with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Really!?"
    scene sm1fs_t003-37 mc-tl-vs-dv-km-talk1_c3 with dissolve
    play voice6 girl34_arrogant_hm1 noloop
    dvh "{i}Some.{/i}"
    play voice2 mc_surprised_oh1 noloop
    mc "Oh..."
    play voice6 girl34_arrogant_ha3 noloop
    dvh "Not enough to take my stage though."
    scene sm1fs_t003-35 mc-tl-vs-dv-km-walk2_c1 with dissolve
    play voice5 girl33_surprised_why1 noloop
    vs "I thought he did great!"
    scene sm1fs_t003-36 mc-tl-vs-dv-km-walk3_c2 with dissolve
    play voice3 girl24_surprised_eeh2 noloop
    tl "I mean, he definitely has potential."
    scene sm1fs_t003-35 mc-tl-vs-dv-km-walk2_c3 with dissolve
    play voice6 girl34_yes_angry1 noloop
    dvh "That might be. But he is not ready to take {i}my{/i} stage."
    play sound sfx_heels_steps1
    scene sm1fs_t003-36 mc-tl-vs-dv-km-walk3_c1 with dissolve
    play voice4 girl31_arrogant_ha noloop
    km "I agree with Denise. I've seen trees give more compelling performances."
    stop sound fadeout 1.0
    play voice6 girl34_angry_ahem2 noloop
    dvh "Kellie, silence."
    play voice4 girl31_surprised_uh1 noloop
    km "But-"
    scene sm1fs_t003-36 mc-tl-vs-dv-km-walk3_c2 with dissolve
    play voice3 girl24_hey_angry noloop
    tl "Denise, I-"
    scene sm1fs_t003-34 mc-tl-vs-dv-km-walk1_c1 with dissolve
    play voice5 girl33_disappointed_eeh noloop
    vs "Come on-"
    play voice6 girl34_angry_argh5 noloop
    scene sm1fs_t003-36 mc-tl-vs-dv-km-walk3_c3 with hpunch
    dvh "{i}Silence.{/i}"
    dvh "I agree. You have potential, [mcname]. Maybe in the future you will be ready. But for now, we have a position in the backstage for another hand. This is what I can offer you."
    mct "That's not exactly what I want but... She said I could maybe act in the future? Besides, a job is a job."
    scene sm1fs_t003-37 mc-tl-vs-dv-km-talk1_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I'll take it."
    scene sm1fs_t003-37 mc-tl-vs-dv-km-talk1_c2 with dissolve
    play voice6 girl34_yes_aga8 noloop
    dvh "Good. Veronica, you show him around. Make sure to introduce him to Sam."
    scene sm1fs_t003-38 mc-tl-vs-dv-km-talk2_c3 with dissolve
    play voice5 girl33_yes_happy noloop
    vs "Of course, Denise! Anything you want. I'd love to show [mcname] around!"
    play sound sfx_carpet_footsteps2 loop
    scene sm1fs_t003-39 mc-tl-vs-dv-km-talk3_c3 with dissolve
    play voice6 girl34_thinking_hmm2 noloop
    dvh "I will be in my office if anyone is looking for me."
    stop sound fadeout 1.0
    scene sm1fs_t003-39 mc-tl-vs-dv-km-talk3_c2 with dissolve
    play voice5 girl33_happy_nice noloop
    vs "Don't worry, I thought you were great! You'll be on stage in no time!"
    scene sm1fs_t003-39 mc-tl-vs-dv-km-talk3_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.5
    mc "Thanks. Definitely not how I wanted today to go."
    play voice4 girl31_disappointed_mff1 noloop
    km "What?"
    scene sm1fs_t003-40 mc-tl-vs-dv-km-talk4_c1 with dissolve
    play voice4 girl31_arrogant_fff noloop
    km "You used to life just giving you everything you wanted, whenever you give the bare minimum effort?"
    play voice2 mc_yes_yeah8 noloop
    mc "Kind of? I mean, it's not the bare minimum effort, but-"
    scene sm1fs_t003-40 mc-tl-vs-dv-km-talk4_c3 with dissolve
    play voice4 girl31_arrogant_hm1 noloop
    km "HMPH."
    play sound sfx_heels_steps2
    scene sm1fs_t003-41 mc-tl-vs-dv-km-talk5_c1 with dissolve
    stop sound fadeout 4.0
    play voice2 mc_surprised_huh6 noloop
    mc "What'd I say?"
    scene sm1fs_t003-41 mc-tl-vs-dv-km-talk5_c2 with dissolve
    play voice5 girl33_happy_laugh2 noloop
    vs "Oh nothing, that's just Kellie. She's like that. Always upset about something."
    scene sm1fs_t003-42 mc-tl-vs-dv-km-talk6_c2 with dissolve
    play voice5 girl33_happy_yay noloop
    vs "But come on! Let me show you around."
    play sound sfx_heels_steps1 loop
    scene sm1fs_t003-43 mc-tl-vs-dv-km-walk1_c1 with dissolve
    pause
    scene sm1fs_t003-43 mc-tl-vs-dv-km-walk1_c2 with dissolve
    pause
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1.0, 1.0, "sound4" )
    play sound4 sfx_lockerroom_ambience fadein 1.5
    scene sm1fs_t003-44 mc-tl-vs-dv-km-walk2_c2 with dissolve
    play voice5 girl33_yes_aga noloop
    vs "This is backstage! Where you'll be doing all of the stagehand work."
    scene sm1fs_t003-44 mc-tl-vs-dv-km-walk2_c1 with dissolve
    play voice5 girl33_thinking_hmm2 noloop
    vs "Usually Bruce is back here somewhere... But I don't see him. I'll show you the rest of the theater while we wait!"
    vs "Pretty much every room you'll need is in the hallway! Let's see..."
    play sound sfx_cloth_rustling1
    scene sm1fs_t003-45 mc-tl-vs-dv-km-door1_c1 with dissolve
    play voice5 girl33_thinking_hmm3 noloop
    vs "This is where we store our old props and sets."
    play sound sfx_heels_steps2 loop
    stop sound4 fadeout 1.0
    scene sm1fs_t003-47 mc-tl-vs-dv-km-point_c2 with dissolve
    play voice5 girl33_yes_yeah noloop
    vs "This is where most of the actors and actresses do their makeup and get dressed in wardrobe."
    scene sm1fs_t003-47 mc-tl-vs-dv-km-point_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh? Does everyone just... Get dressed together?"
    play voice5 girl33_yes_yep noloop
    vs "Yep!"
    play voice2 d1s1_mmm noloop
    mct "Hell. Yeah."
    stop sound fadeout 1.0
    scene sm1fs_t003-48 mc-vs-room1_c2 with dissolve
    play voice5 girl33_angry_mfhmm noloop
    vs "And this is the lead actress makeup and wardrobe area!"
    scene sm1fs_t003-48 mc-vs-room1_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Who's in here?"
    scene sm1fs_t003-49 mc-vs-room2_c2 with dissolve
    play voice5 girl33_thinking_eem2 noloop
    vs "It changes depending on the production, but lately it's been mine!"
    scene sm1fs_t003-49 mc-vs-room2_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "You're the star of the show?"
    scene sm1fs_t003-48 mc-vs-room1_c2 with dissolve
    play voice5 girl33_happy_yeah noloop
    vs "Yeah! Denise thinks I've got what it takes to go the distance."
    play voice2 mc_surprised_wow3 noloop
    mc "Wow, I didn't realize the big time actress was showing me around!"
    play voice5 girl33_no_happy noloop
    vs "I'm not big time. Not like some people here!"
    vs "Seriously, it's not a problem! I'm super happy to show you around"
    scene sm1fs_t003-49 mc-vs-room2_c2 with dissolve
    play voice5 girl33_thinking_hmm1 noloop
    vs "Over there is Denise's office. And that's pretty much it!"
    scene sm1fs_t003-49 mc-vs-room2_c1 with dissolve
    play voice2 mc_no_no10 noloop
    mc "No tour of Denise's office?"
    play voice5 girl33_no_nah noloop
    vs "She's taking her \"me\" time. Best not to interrupt her."
    mc "Good to know!"
    vs "Come on, let's go see if Bruce is back!"
    play sound sfx_heels_steps2 loop
    scene sm1fs_t003-50 mc-tl-vs-dv-km-entry1_c1 with dissolve
    pause
    scene sm1fs_t003-50 mc-tl-vs-dv-km-entry1_c2 with dissolve
    play voice5 girl33_hey_serious noloop
    vs "Bruce-y!"
    play sound2 sfx_metal_fence2 noloop
    scene sm1fs_t003-50 mc-tl-vs-dv-km-entry1_c3 with dissolve
    play voice4 boy5_hey_attention noloop
    sb "Hey Veronica."
    stop sound fadeout 1.0
    scene sm1fs_t003-51 mc-tl-vs-dv-km-handshake_c2 with dissolve
    play voice5 girl33_happy_laugh3 noloop
    vs "I want to introduce you to [mcname]! Denise just hired him as a new stagehand."
    play sound sfx_hands_clap2 volume 0.6
    scene sm1fs_t003-51 mc-tl-vs-dv-km-handshake_c3 with dissolve
    play voice4 boy5_arrogant_heh1 noloop
    sb "Huh, nice to meet you. Sam Bruce."
    sb "I guess I'm your new boss."
    scene sm1fs_t003-51 mc-tl-vs-dv-km-handshake_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I guess so."
    mc "Do I have something on my face?"
    scene sm1fs_t003-52 mc-tl-vs-dv-km-talk1_c3 with dissolve
    play voice4 boy5_no_simple2 noloop
    sb "No but... There ain't no way to say this nice but you're real pretty for a stagehand."
    scene sm1fs_t003-52 mc-tl-vs-dv-km-talk1_c1 with dissolve
    play voice2 mc_surprised_what5 noloop
    mc "What???"
    scene sm1fs_t003-53 mc-tl-vs-dv-km-talk2_c2 with dissolve
    play voice4 boy5_thinking_emm2 noloop
    sb "Most stagehands look like construction workers. You look like Denise put you on the wrong side of the curtain."
    scene sm1fs_t003-53 mc-tl-vs-dv-km-talk2_c1 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, uhm... Thanks? I guess?"
    scene sm1fs_t003-54 mc-tl-vs-dv-km-talk3_c2 with dissolve
    play voice4 boy5_arrogant_heh2 noloop
    sb "Don't mention it. You ever worked in a theater before?"
    play voice2 mc_no_nope2 noloop
    mc "Nope."
    play voice4 boy5_yes_ugu2 noloop
    sb "Okay, well it ain't rocket surgery so you'll be fine. Come with me, I'll show you the ropes. Literally."
    scene sm1fs_t003-55-2 mc-tl-vs-dv-km-talk4_c2 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Sounds good! Uh, thanks for showing me around Veronica."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t003-55-2 mc-tl-vs-dv-km-talk4_c1 with dissolve
    play voice5 girl33_hey_bye1 noloop
    vs "Of course! I'm hoping to see you around some more!"
    stop sound fadeout 2.0
    scene sm1fs_t003-57 mc-tl-vs-dv-km-walk1_c2 with dissolve
    play voice4 boy5_thinking_hmm2 noloop
    sb "Okay, this is the nerve center of the show. From here, we make the magic happen."
    scene sm1fs_t003-57 mc-tl-vs-dv-km-walk1_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.5
    mc "Looks... Fancy."
    play voice4 boy5_thinking_hm noloop
    sb "Let me show you..."
    jump sm1fs_t003_ss_tutorial
label sm1fs_t003_ss_tutorial:
    $ ss_rehearsal_mode = True
    $ ss_buttons_count = 12
    $ ss_pattern_length = 9
    $ ss_animtion_timer = 1.5
    $ ss_buttons_set = "theater1"
    $ simon_says_end_jump = "sm1fs_t003_ss_tutorial_end"
    jump simon_says_start
label sm1fs_t003_ss_tutorial_end:
    scene sm1fs_t003-60 mc-tl-vs-dv-km-talk2_c2 with dissolve
    play voice4 boy5_happy_phew1 noloop
    sb "And that's it!"
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh. That wasn't so bad."
    sb "Now, the important thing is to remember the rehearsals."
    scene sm1fs_t003-60 mc-tl-vs-dv-km-talk2_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Rehearsals."
    play voice4 boy5_yes_yep noloop
    sb "Yep. Throughout the week we hold rehearsals for the show on Saturday. Show up, practice what you need to do, and come Saturday you just need to show up and do it for the show."
    mc "Oh, that makes sense."
    scene sm1fs_t003-60 mc-tl-vs-dv-km-talk2_c2 with dissolve
    play voice4 boy5_thinking_hmm7 noloop
    sb "We'll even pay you for rehearsals, but the big payday comes Saturday nights."
    play voice2 mc_happy_a1 noloop
    mc "Cool. So show up, rehearse, then Saturday night showtime?"
    play voice4 boy5_yes_simple1 noloop
    sb "You got it?"
    scene sm1fs_t003-60 mc-tl-vs-dv-km-talk2_c1 with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Cool, I can do that."
    play voice4 boy5_happy_relief1 noloop
    sb "Great. Well I've done my 12 today, so I'm heading out. I'll see ya' around kid."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t003-61 mc-tl-vs-dv-km-end1_c1 with dissolve
    play voice2 mc_hey_bye2 noloop
    mc "Sounds good, I'll see ya', Sam!"
    stop sound fadeout 3.5
    scene sm1fs_t003-61 mc-tl-vs-dv-km-end1_c2 with dissolve
    pause
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    call sm1fs_t003_location_unlocked from _call_sm1fs_t003_location_unlocked
    call sm1fs_t003_job_unlocked from _call_sm1fs_t003_job_unlocked
    call sm1fs_t003_activate_storylines from _call_sm1fs_t003_activate_storylines
    $ StoryController.end_scene(THEATER_STORY_LINE, 3, 0, 6, THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER)
    return
label sm1fs_t003_activate_storylines:
    $ StoryController.activate_story_line(DVH_STORY)
    $ StoryController.activate_story_line(KM_STORY)
    $ StoryController.activate_story_line(TL_STORY)
    $ StoryController.activate_story_line(VS_STORY)
    if player.get_choice("NUMBER_OF_JOBS_UNLOCKED") == 1:
        $ StoryController.activate_story_line(MS, True)
    return
label sm1fs_t003_job_unlocked:
    $ player.set_choice("TH_JOB_UNLOCKED", True)
    $ number_of_jobs = player.get_choice("NUMBER_OF_JOBS_UNLOCKED") + 1
    $ player.set_choice("NUMBER_OF_JOBS_UNLOCKED", number_of_jobs)
    return
label sm1fs_t003_location_unlocked:
    $ LocationController.get_location(THEATER, LTH_SUB_CORRIDOR, LTH_CORRIDOR_ENTR).unlock()
    $ LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_FRONT_STAGE).add_override_interaction_option("io-TH_Work")
    $ LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE).add_override_interaction_option("io-TH_Work")
    $ LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_FIRST_ROW).add_override_interaction_option("io-TH_Work")
    $ LocationController.get_location(THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE).add_override_interaction_option("io-TH_Rehearsal")
    $ ObjectController.get_object(TH_SIGN_REHEARSAL).unlock()
    $ ObjectController.get_object(TH_SIGN_SHOW).unlock()
    return
label sm1fs_t003_unlocks:
    call sm1fs_t003_location_unlocked from _call_sm1fs_t003_location_unlocked_1
    call sm1fs_t003_job_unlocked from _call_sm1fs_t003_job_unlocked_1
    if config_storyline_mode is True:
        $ execute_storyline_config(THEATER_STORY_LINE)
    return