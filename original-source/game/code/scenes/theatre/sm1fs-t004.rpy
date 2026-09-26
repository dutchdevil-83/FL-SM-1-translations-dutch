image sm1fs_t004-a07-glam = Movie(play = "images/FS_T/s004/anim/sm1fs-t004-a07-3x-60fps.webm", start_image = "sm1fs-t004-a07 glambot-000", image = "sm1fs-t004-a07 glambot-120", loop = False)
image sm1fs_t004-a116-1-f = Movie(play = "images/FS_T/s004/anim/sm1fs-t004-a116-1-2x-50fps.webm", start_image = "sm1fs-t004-a116-1 tl-masturbation-anim-01")
image sm1fs_t004-a116-1 = Movie(play = "images/FS_T/s004/anim/sm1fs-t004-a116-1-3x-60fps.webm", start_image = "sm1fs-t004-a116-1 tl-masturbation-anim-01")
image sm1fs_t004-a116-2-f = Movie(play = "images/FS_T/s004/anim/sm1fs-t004-a116-2-2x-50fps.webm", start_image = "sm1fs-t004-a116-2 tl-masturbation-anim-01")
image sm1fs_t004-a116-2 = Movie(play = "images/FS_T/s004/anim/sm1fs-t004-a116-2-3x-60fps.webm", start_image = "sm1fs-t004-a116-2 tl-masturbation-anim-01")
image sm1fs_t004-a116-3-f = Movie(play = "images/FS_T/s004/anim/sm1fs-t004-a116-3-2x-50fps.webm", start_image = "sm1fs-t004-a116-3 tl-masturbation-anim-01")
image sm1fs_t004-a116-3 = Movie(play = "images/FS_T/s004/anim/sm1fs-t004-a116-3-3x-60fps.webm", start_image = "sm1fs-t004-a116-3 tl-masturbation-anim-01")
image sm1fs_t004-a116-4-f = Movie(play = "images/FS_T/s004/anim/sm1fs-t004-a116-4-2x-50fps.webm", start_image = "sm1fs-t004-a116-4 tl-masturbation-anim-01")
image sm1fs_t004-a116-4 = Movie(play = "images/FS_T/s004/anim/sm1fs-t004-a116-4-3x-60fps.webm", start_image = "sm1fs-t004-a116-4 tl-masturbation-anim-01")
label sm1fs_t004:
    $ sm1fs_t004_km_trust_fall = False
    $ sm1fs_t004_tl_trust_fall = False
    $ sm1fs_t004_vs_trust_fall = False
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    scene sm1fs-t004-a07 glambot-000 with fade
    play music music_theatrical_life1
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1fs_t004-a07-glam
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1fs_t004-08-dvh-talk with dissolve
    play voice3 girl34_hey_angry1 noloop
    dvh "Goedendag, everyone."
    scene sm1fs_t004-09-tl-talk with dissolve
    play voice4 girl24_surprised_huh2 noloop
    tl "What's going on?"
    scene sm1fs_t004-10-dvh-talk with dissolve
    play voice3 girl34_thinking_hmm2 noloop
    dvh "Today we are doing something different. We have been doing the same show now for two months."
    scene sm1fs_t004-11-dvh-talk with dissolve
    play voice3 girl34_thinking_emm1 noloop
    dvh "I suspect that many of us could do this show while sleeping, at this point."
    dvh "Which does not make good actors. Today, we are going to be doing a workshop, to keep your instincts honed."
    scene sm1fs_t004-12-tl-talk with dissolve
    play voice4 girl24_angry_argh2 noloop
    tl "Uggggggggghhhhhh."
    scene sm1fs_t004-13-dvh-talk-tl with dissolve
    play voice3 girl34_no_nouh4 noloop
    dvh "I will hear no back talk. Believe me when I say that this is important."
    scene sm1fs_t004-14-km-talk-dvh with dissolve
    play voice5 girl31_surprised_uh1 noloop
    km "Then what is he doing here? He's just a stagehand."
    scene sm1fs_t004-15-mc-inner-talk with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "Jesus. Sounds like someone is in a bad mood today."
    scene sm1fs_t004-16-dvh-talk-km with dissolve
    play voice3 girl34_disappointed_eeh2 noloop
    dvh "He has demonstrated interest in the craft. I want him to witness the amount of work it takes to be an actor."
    dvh "And, he is in need of more training with Bruce. Today is as much of a workshop for us, as it is for the crew."
    scene sm1fs_t004-17-vs-talk-dvh with dissolve
    play voice5 girl33_disappointed_eeh noloop
    vs "So what are we going to be doing in the workshop?"
    scene sm1fs_t004-18-dvh-talk with dissolve
    play voice3 girl34_disappointed_huh noloop
    dvh "First, we will be doing some group improvisation. I will be giving you each an emotion to try and elicit from the audience, who will be me."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-19-dvh-talk with dissolve
    play voice3 girl34_angry_ahem4 noloop
    dvh "But first, I want you each to stretch. Before we begin to use our skills, our bodies must be ready."
    dvh "Chop, chop!"
    play sound2 sfx_heels_steps1
    scene sm1fs_t004-20-people-stretch with dissolve
    play sound3 sfx_socks_dancing1 volume 0.5
    play sound4 sfx_museum_ambience
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1fs_t004-21-tl-talk with dissolve
    play voice4 girl24_angry_err1 noloop
    tl "God, I {i}haaaaaaaaate{/i} these workshops."
    scene sm1fs_t004-22-mc-talk-tl with dissolve
    play voice2 mc_surprised_why3 noloop
    mc "Why?"
    scene sm1fs_t004-23-tl-talk-mc with dissolve
    play voice4 girl24_disappointed_eeh1 noloop
    tl "They're fucking boring as hell. We do some stupid scene studies, and then we do some stupid trust building activity."
    scene sm1fs_t004-24-mc-talk-tl with dissolve
    play voice2 mc_happy_a1 noloop
    mc "That doesn't sound that bad."
    scene sm1fs_t004-25-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_pff noloop
    tl "Pfft. Whatever."
    scene sm1fs_t004-26-mc-talk-tl with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What would you rather be doing?"
    scene sm1fs_t004-27-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_hah noloop
    tl "Literally anything. Even fucking you would be better than this."
    scene sm1fs_t004-28-mc-talk-tl with dissolve
    play voice2 mc_pain_auch1 noloop
    mc "Well, ouch."
    scene sm1fs_t004-25-tl-talk-mc with dissolve
    play voice4 girl24_no_nah noloop
    tl "I'm kidding. Fucking you is pretty all right."
    scene sm1fs_t004-26-mc-talk-tl with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "I'd hope so."
    scene sm1fs_t004-27-tl-talk-mc with dissolve
    play voice4 girl24_disappointed_neh noloop
    tl "But, I'd rather be practicing some monster makeup, or something. But Denise doesn't like horror at all. So, instead I have to sit and try to entertain myself during this stupid shit..."
    scene sm1fs_t004-28-mc-talk-tl with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Well, I don't think it's that stupid."
    play sound sfx_cloth_rustling1
    scene sm1fs_t004-29-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_yeah1 noloop
    tl "Yeah, yeah... well I better start stretching before Denise comes over here and yells at me."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-30-tl-stretch with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1fs_t004-31-vs-talk-dvh with dissolve
    play voice5 girl33_hey_serious noloop
    vs "Come on, Denise! I bet you're working on a new show right now!"
    scene sm1fs_t004-32-dvh-talk-vs with dissolve
    play voice3 girl34_arrogant_aga noloop
    dvh "I may. I may not. But, that is all you will hear from me."
    scene sm1fs_t004-33-vs-talk-dvh with dissolve
    play voice4 girl33_disappointed_aah noloop
    vs "Pleeeaaaaaaase!"
    scene sm1fs_t004-34-dvh-talk-vs with dissolve
    play voice3 girl34_no_uhuh noloop
    dvh "Begging does not suit you, Veronica."
    scene sm1fs_t004-35-vs-talk-dvh with dissolve
    play voice5 girl33_surprised_huh1 noloop
    vs "How about just a hint! Just a small little hint about what you're working on?"
    scene sm1fs_t004-36-km-talk-vs with dissolve
    play voice6 girl31_hey_angry noloop
    km "You heard her, Veronica. Knock it off and start stretching."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-37-vs-talk-km with dissolve
    play voice5 girl33_yes_yep noloop
    vs "You're right, Kellie. I'll find out soon enough, I bet!"
    stop sound fadeout 1.0
    scene sm1fs_t004-38-dvh-talk-mc with dissolve
    play voice3 girl34_yes_yeah3 noloop
    dvh "Ya?"
    scene sm1fs_t004-39-mc-talk-dvh with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I was wondering if I could do the workshop too."
    scene sm1fs_t004-40-dvh-talk-mc with dissolve
    play voice3 girl34_no_angry8 noloop
    dvh "You are not an actor. You are a stagehand."
    scene sm1fs_t004-41-mc-talk-dvh with dissolve
    play voice2 mc_thinking_hm noloop
    mc "But I want to be an actor."
    if player.has_played_scene("sm1cs_dvh001"):
        mc "And you told me I have to show some initiative."
    scene sm1fs_t004-42-dvh-talk-mc with dissolve
    play voice3 girl34_arrogant_laugh1 noloop
    dvh "Fine, you can participate."
    scene sm1fs_t004-43-mc-talk-dvh with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Yaaay!"
    scene sm1fs_t004-44-dvh-talk-mc with dissolve
    play voice3 girl34_arrogant_huh1 noloop
    dvh "{i}But,{/i} only after you have finished your work with Bruce. Your role as a stagehand will not be overtaken by your desire to act. Understand?"
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-45-mc-talk-dvh with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Yes, of course! Thank you, Denise!"
    scene sm1fs_t004-46-vs-talk-mc with dissolve
    play voice5 girl33_surprised_huh3 noloop
    vs "Did I hear Denise say that you could join us for the workshop?"
    scene sm1fs_t004-47-mc-talk-vs with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "You did! At least, after I'm done working with Bruce!"
    scene sm1fs_t004-48-vs-talk-mc with dissolve
    play voice5 girl33_happy_yay noloop
    vs "Oh that's awesome! Yay! You better work quickly, then!"
    scene sm1fs_t004-49-mc-talk-vs with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh believe me, I'm going to!"
    stop sound fadeout 1.0
    stop sound4 fadeout 2.0
    stop sound3 fadeout 2.0
    jump sm1fs_t004_backstage
label sm1fs_t004_backstage:
    stop music fadeout 3.0
    scene sm1fs_t004-50-theater-backstage with Fade(0.5, 0.5, 0.5)
    queue sound4 sfx_clock_ticks_loop1 volume 0.4
    $ renpy.music.set_volume(1.0, 5.0, "music" )
    queue music thinking_music_6
    pause
    scene sm1fs_t004-51-sb-talk-mc with dissolve
    play voice3 boy5_angry_ehh1 noloop
    sb "Hey, kid."
    scene sm1fs_t004-52-mc-talk-sb with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Hey, Bruce! Looks like I'm working with you today. So what's first!"
    scene sm1fs_t004-53-sb-talk-mc with dissolve
    play voice3 boy5_surprised_oh1 noloop
    sb "My, my. You sound very gung ho today."
    scene sm1fs_t004-54-mc-talk-sb with dissolve
    play voice2 d2s12_emmm noloop
    mc "Well, I'm, uhhhh, just excited to be a stagehand!"
    scene sm1fs_t004-56-sb-talk-mc with dissolve
    play voice3 boy5_yes_ugu1 noloop
    sb "And it has nothing to do at all with little miss thing out there being excited for you to join her in the workshop."
    scene sm1fs_t004-55-mc-talk-sb with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Oh, well, uhmmmm..."
    mc "I'm surprised you heard that."
    scene sm1fs_t004-58-sb-talk-mc with dissolve
    play voice3 boy5_happy_laugh1 noloop
    sb "It's a theater. Great acoustics in here."
    scene sm1fs_t004-57-mc-talk-sb with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Oh... that makes sense."
    mc "What are you looking at?"
    scene sm1fs_t004-59-sb-talk-mc with dissolve
    play voice3 boy5_thinking_hmm2 noloop
    sb "Wonderin' if I need to add more lights up there."
    sb "You know how to tie any knots?"
    scene sm1fs_t004-60-mc-talk-sb with dissolve
    play voice2 mc_no_no10 noloop
    mc "I can't say that I do..."
    scene sm1fs_t004-59-sb-talk-mc with dissolve
    play voice3 boy5_hey_attention noloop
    sb "You should learn. It's a useful skill. You never know what you're going to use them for."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-62-mc-talk-sb with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh..."
    play voice3 boy5_yes_ugu2 noloop
    sb "Well come on, I think I got something for you to do."
    stop sound4 fadeout 2.0
    play sound sfx_double_door1
    scene sm1fs_t004-63-theater-storage with dissolve
    play sound3 sfx_lockerroom_ambience volume 1.4 fadein 3.0
    pause
    play sound sfx_bed_slide2
    scene sm1fs_t004-64-mc-talk-sb with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "So..."
    scene sm1fs_t004-65-sb-talk-mc with dissolve
    play voice3 boy5_arrogant_heh1 noloop
    sb "So, we need to organize the prop storage area."
    scene sm1fs_t004-66-mc-talk-sb with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "And that's..."
    scene sm1fs_t004-67-sb-talk-mc with dissolve
    play voice3 boy5_yes_yeah noloop
    sb "Everything in here. It's a bit of a mess, but with a new show coming, we need to be able to find stuff."
    scene sm1fs_t004-68-mc-inner-talk with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "Shit, this is going to suck..."
    scene sm1fs_t004-69-sb-talk-mc with dissolve
    play voice3 boy5_arrogant_yeah1 noloop
    sb "Yeah, this is going to suck."
    scene sm1fs_t004-70-mc-inner-talk with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Can he read my mind!?"
    scene sm1fs_t004-71-sb-talk-mc with dissolve
    play voice3 boy5_thinking_oh1 noloop
    sb "And if you're wondering if I can read your mind, I can't. This is just a shitty job."
    play sound sfx_hair_scratch1
    scene sm1fs_t004-72-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mct "Oh..."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-73-sb-talk-mc with dissolve
    play voice3 boy5_hey_bye2 noloop
    sb "Good luck kid. If you need me, I'll be talking with Denise."
    stop sound fadeout 1.0
    scene sm1fs_t004-74-mc-inner-talk with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "God... where do I even start?"
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-75-mc-inner-talk with dissolve
    mct "This is going to suck..."
    scene sm1fs_t004-76-theater-storage with dissolve
    play sound sfx_metal_fence2
    pause
    jump sm1fs_t004_one_hour_later
label sm1fs_t004_one_hour_later:
    scene black
    show screen scene_transistion(_("One hour later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene sm1fs_t004-77-mc-inner-talk
    with Fade(0.5, 0.5, 0.5)
    play sound sfx_heels_steps2 fadein 4.0 loop
    play voice2 mc_angry_hm2 noloop
    mct "Shit... this is exhausting..."
    stop sound fadeout 2.0
    scene sm1fs_t004-78-sb-talk-mc with dissolve
    play voice3 boy5_surprised_wow1 noloop
    sb "Wow, you did a lot of work in here, [mcname]."
    scene sm1fs_t004-79-mc-inner-talk with dissolve
    play voice2 mc_angry_errr7 noloop
    mct "What's he talking about!? It looks exactly the same!"
    scene sm1fs_t004-80-mc-talk-sb with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I'm glad you think so."
    scene sm1fs_t004-81-sb-talk-mc with dissolve
    play voice3 boy5_yes_simple1 noloop
    sb "I do."
    scene sm1fs_t004-82-mc-talk-sb with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "What else do you want me to do?"
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-83-sb-talk-mc with dissolve
    play voice3 boy5_thinking_hmm1 noloop
    sb "Just finish up in here and then you can go and join the actresses on stage."
    scene sm1fs_t004-84-mc-talk-sb with dissolve
    play voice2 mc_happy_yay3 noloop
    mc "Thanks Bruce!"
    scene sm1fs_t004-85-sb-talk-mc with dissolve
    play voice3 boy5_no_nah noloop
    sb "Don't mention it."
    scene sm1fs_t004-86-sb-leave with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1fs_t004-87-mc-inner-talk with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    mct "Uhhhhh, what else is there to do?"
    play sound sfx_double_door1 volume 0.5
    scene sm1fs_t004-88-door-noise with dissolve
    pause
    scene sm1fs_t004-89-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Did someone just walk in?"
    mct "..."
    play sound sfx_cloth_rustling2
    scene sm1fs_t004-90-mc-inner-talk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "Must just be imagining things."
    scene sm1fs_t004-91-tl-talk with dissolve
    play voisex3 girl24_sex_orgasm1 noloop volume 0.3
    tl "{size=*0.3}Oh fuuuuuuuck...{/size}"
    scene sm1fs_t004-92-mc-inner-talk with dissolve
    play voice2 mc_angry_huh1 noloop
    mct "What the hell was that?"
    scene sm1fs_t004-93-mc-inner-talk with dissolve
    mct "Was the Taisia? It kind of sounded like Taisia..."
    menu:
        "Check the storage area"(hint="sm1fs_t004_m01_h01"):
            call sm1fs_t004_m01_c01 from _call_sm1fs_t004_m01_c01
            jump sm1fs_t004_tl_masturbating
        "Just finish up"(hint="sm1fs_t004_m01_h02"):
            play sound sfx_cloth_rustling1
            scene sm1fs_t004-94-mc-inner-talk with dissolve
            play voice2 mc_no_uhuh1 noloop
            mct "Nah... I must just be imagining things."
            mct "I think... that's good enough. Time to get to the workshop!"
            play sound sfx_heels_steps2 loop
            stop music fadeout 3.0
            scene sm1fs_t004-95-mc-leave with dissolve
            pause
            stop sound fadeout 1.0
            jump sm1fs_t004_workshop
label sm1fs_t004_tl_masturbating:
    play sound sfx_cloth_rustling3
    scene sm1fs_t004-96-mc-looking-around with dissolve
    pause
    $ renpy.music.set_volume(0.8, 5.0, "music" )
    stop music fadeout 3.0
    scene sm1fs_t004-97-tl-talk with dissolve
    queue music music_backstage_fun
    play voisex3 girl24_sex_orgasm3 noloop volume 0.4
    tl "{size=*0.6}Yesssssssss...{/size}"
    scene sm1fs_t004-98-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop volume 1.6
    mct "Oh, that is definitely Taisia, but where-"
    scene sm1fs_t004-99-mc-inner-talk with dissolve
    play voice2 mc_pain_ou1 noloop
    mct "Oh shit!"
    scene sm1fs-t004-a116-1 tl-masturbation-anim-01 with dissolve
    pause
    play voisex3 girl24_sex_openmoans2
    play sound sfx_sex_fingering_slow1 loop volume 0.6
    scene sm1fs_t004-a116-1 with dissolve
    tl "{size=*0.8}Fuck, yesssss, oh that's sooo gooooood!{/size}"
    pause
    tl "{size=*0.8}Gooood, I'm so cloooooooseeeee.{/size}"
    scene sm1fs_t004-104-mc-inner-talk with dissolve
    play voice2 mc_pain_rrrr noloop
    mct "Holy shit, Taisia is really masturbating in the props storage!"
    mct "It's kind of super hot..."
    scene sm1fs_t004-a116-2 with dissolve
    play voisex3 girl24_sex_orgasm2
    tl "{size=*0.8}Mmmmmmm, yesss, oooooooo!{/size}"
    play voice2 mc_thinking_mmm2 noloop
    mct "And she has no idea I'm watching her... damn..."
    pause
    stop sound fadeout 1.0
    scene sm1fs_t004-107-tl-talk-mc with dissolve
    play voisex3 girl24_sex_closedmoan1 noloop
    tl "Mmmmm... [mcname], is that you over there?"
    scene sm1fs_t004-108-mc-inner-talk with dissolve
    play voice2 mc_angry_errr8 noloop
    mct "Fuck, my cover is blown."
    play sound2 sfx_heels_steps2 volume 1.5 noloop
    scene sm1fs_t004-109-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yep, it's me..."
    scene sm1fs_t004-110-tl-talk-mc with dissolve
    play voisex3 girl24_sex_openmoans1
    play sound sfx_sex_fingering_slow1 loop volume 0.6
    tl "Cool, I thought it was - ooooo!"
    scene sm1fs_t004-111-mc-talk-tl with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "And you're... still masturbating?"
    scene sm1fs_t004-a116-4 with dissolve
    play voisex3 girl24_sex_openmoans4
    tl "Fuuuuucccck yes, I'm too close to stop! Plus, having an audience makes this hoooootter."
    pause
    scene sm1fs_t004-a116-3 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh, well if you're cool with it-"
    pause
    scene sm1fs_t004-a116-1-f with dissolve
    play voisex3 girl24_sex_orgasm2
    tl "Oh God!"
    tl "Shut up and go back to watching me! Oh fuck - I'm so clooooose! Fuck, fuck, fuck!"
    pause
    scene sm1fs_t004-a116-2-f with dissolve
    tl "Mmmmmnnnnng - fuuuuuuuck!"
    play voice2 d3s11b_mcheh noloop
    mct "Well if all I have to do to get a free show is stay quiet..."
    tl "Shiiiiit - I'm going to cum sooo hard with a little perv watching meeee!"
    pause
    scene sm1fs_t004-a116-3-f with dissolve
    play voice2 d1s5_mcthinks noloop
    mct "Wait a second... Am I the little perv?"
    pause
    scene sm1fs_t004-a116-4-f with dissolve
    tl "Fuhhh - fuuuuhhh - fuuuucccccckkk!"
    pause
    tl "I'm-I'm-I'm-!"
    play voisex3 girl24_sex_orgasm4 noloop
    play sound sfx_squirt1
    scene sm1fs_t004-120-tl-cum with vpunch
    tl "Cuuuuummmmiiiinnnnnggggg!"
    scene sm1fs_t004-121-mc-tl with dissolve
    pause
    scene sm1fs_t004-122-mc-tl with fade
    pause
    scene sm1fs_t004-123-mc-talk-tl with dissolve
    play voice2 d2s9_confused noloop
    mc "So... rubbing one out in the storage?"
    scene sm1fs_t004-124-tl-talk-mc with dissolve
    play voice3 girl24_yes_yeah noloop volume 0.8
    tl "Yeah. No one ever comes back here."
    play sound sfx_heels_steps1 loop
    scene sm1fs_t004-125-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_hah noloop
    tl "Plus, these workshops are boring as fuck. At the very least I can get an orgasm out of it."
    scene sm1fs_t004-126-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Damn. Taisia is such a freak."
    scene sm1fs_t004-127-mc-inner-talk with dissolve
    play voice2 d14s16_smell noloop
    mct "But, I should probably get back to the workshop."
    stop music fadeout 3.0
    stop sound fadeout 2.0
    jump sm1fs_t004_workshop
label sm1fs_t004_workshop:
    stop sound3 fadeout 3.0
    play sound4 sfx_museum_ambience fadein 1.5
    $ renpy.music.set_volume(0.8, 3.5, "music" )
    scene sm1fs_t004-128-theater with Fade(0.5, 0.5, 0.5)
    queue sound sfx_heels_steps2 loop
    queue music music_theatrical_life1
    pause
    scene sm1fs_t004-129-dvh-talk with dissolve
    play voice3 girl34_arrogant_hm2 noloop
    dvh "That is the improvisation part of the workshop. You have all done well."
    scene sm1fs_t004-130-dvh-talk-mc with dissolve
    play voice3 girl34_hey_simple1 noloop
    dvh "Good. Mr. Bruce told me of your hard work, and I am happy that you can join us."
    stop sound fadeout 1.0
    scene sm1fs_t004-131-mc-talk-dvh with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Oh, uhm, thanks Denise."
    scene sm1fs_t004-132-dvh-talk-mc with dissolve
    play voice3 girl34_yes_aga2 noloop
    dvh "Of course."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-133-dvh-talk-mc with dissolve
    play voice3 girl34_thinking_hmm7 noloop
    dvh "Now, to our trust building exercise."
    dvh "We are going to do trust falls. If we are to operate as a theater team, we need to trust each other wholly."
    stop sound fadeout 1.0
    scene sm1fs_t004-134-theater with dissolve
    play voice3 girl34_thinking_eeh1 noloop
    dvh "Veronica, Kelly. Please walk into the center of the circle."
    scene sm1fs_t004-135-dvh-talk-km with dissolve
    play voice3 girl34_disappointed_mmf4 noloop
    dvh "Kellie. I want you to turn and fall into Veronica's arms."
    scene sm1fs_t004-136-km-talk-dvh with dissolve
    play voice6 girl31_surprised_what1 noloop
    km "What!"
    scene sm1fs_t004-137-dvh-talk-km with dissolve
    play voice3 girl34_yes_angry1 noloop
    dvh "You will begin this trust fall exercise."
    scene sm1fs_t004-138-km-talk-dvh with dissolve
    play voice6 girl31_no_angry noloop
    km "Absolutely not!"
    scene sm1fs_t004-139-dvh-talk-km with dissolve
    play voice3 girl34_surprised_ah1 noloop
    dvh "Do you not trust Veronica?"
    scene sm1fs_t004-140-km-talk-dvh with dissolve
    play voice6 girl31_angry_ergh1 noloop
    km "No! Not at all!"
    scene sm1fs_t004-141-vs-talk-km with dissolve
    play voice5 girl33_surprised_why2 noloop
    vs "Why?"
    scene sm1fs_t004-142-km-talk-vs with dissolve
    play voice6 girl31_surprised_ah2 noloop
    km "Because-because-"
    scene sm1fs_t004-143-dvh-talk with dissolve
    play voice3 girl34_arrogant_ha4 noloop
    dvh "You must learn to trust her. To trust your troupe."
    scene sm1fs_t004-144-dvh-talk-mc with dissolve
    play voice3 girl34_thinking_hmm5 noloop
    dvh "I will show you.{w} [mcname], come here."
    play sound sfx_heels_steps2 loop
    scene sm1fs_t004-145-mc-talk-dvh with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay?"
    stop sound fadeout 1.0
    scene sm1fs_t004-146-dvh-talk-mc with dissolve
    play voice3 girl34_arrogant_yeah noloop
    dvh "You will catch me now, understood?"
    scene sm1fs_t004-147-mc-talk-dvh with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh, uhm-"
    scene sm1fs_t004-148-mc-inner-talk with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Oh-!"
    play sound sfx_epic_kick2
    scene sm1fs_t004-149-dvh-falls with dissolve
    pause
    play sound sfx_epic_jump1
    scene sm1fs_t004-150-mc-inner-talk with dissolve
    play voice2 mc_scared_huuuh1 noloop
    mct "-shit!"
    play sound sfx_leg_kick7
    play voice2 mc_angry_hm2 noloop
    scene sm1fs_t004-151-mc-dvh with vpunch
    pause
    scene sm1fs_t004-152-dvh-talk-mc with dissolve
    play voice3 girl34_happy_phew1 noloop
    dvh "Very good, [mcname]."
    play sound sfx_cloth_rustling2
    scene sm1fs_t004-153-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop volume 1.6
    mct "I can't believe I caught her."
    scene sm1fs_t004-154-dvh-talk with dissolve
    play voice3 girl34_yes_yeah8 noloop
    dvh "See? We must trust all in this troupe. And if I can trust a man who has yet to prove himself to us, I believe you can all trust each other."
    scene sm1fs_t004-155-mc-inner-talk with dissolve
    play voice2 mc_pain_auh1 noloop
    mct "Ouch."
    scene sm1fs_t004-156-dvh-talk with dissolve
    play voice3 girl34_hey_angry7 noloop
    dvh "Now, each of you will take turns trusting one another with a fall. We shall not move on until each one of you has fallen for another."
    scene sm1fs_t004-157-mc-inner-talk with dissolve
    play voice2 mc_pain_ffff noloop
    mct "Fuck... I didn't expect to have to do trust falls with everyone. I guess... where do I get started?"
    jump sm1fs_t004_trust_fall_menu
label sm1fs_t004_trust_fall_menu:
    if sm1fs_t004_tl_trust_fall is True or sm1fs_t004_km_trust_fall is True or sm1fs_t004_vs_trust_fall is True:
        scene sm1fs_t004-157-mc-inner-talk with dissolve
        pause
    menu:
        "Taisia"(hint="sm1fs_t004_m02_h01") if sm1fs_t004_tl_trust_fall is False:
            $ sm1fs_t004_tl_trust_fall = True
            jump sm1fs_t004_tl_trust_fall
        "Kelly"(hint="sm1fs_t004_m02_h02") if sm1fs_t004_km_trust_fall is False:
            $ sm1fs_t004_km_trust_fall = True
            jump sm1fs_t004_km_trust_fall
        "Veronica"(hint="sm1fs_t004_m02_h03") if sm1fs_t004_vs_trust_fall is False:
            $ sm1fs_t004_vs_trust_fall = True
            jump sm1fs_t004_vs_trust_fall
        "That's everyone"(hint="sm1fs_t004_m02_h04") if sm1fs_t004_tl_trust_fall is True and sm1fs_t004_km_trust_fall is True and sm1fs_t004_vs_trust_fall is True:
            jump sm1fs_t004_workshop_end
label sm1fs_t004_tl_trust_fall:
    scene sm1fs_t004-158-c1-mc-tl with dissolve
    pause
    scene sm1fs_t004-159-c1-mc-talk-tl with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "So-"
    scene sm1fs_t004-160-c1-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_yeah3 noloop
    tl "Come on, let's get this over with."
    scene sm1fs_t004-161-c1-mc-talk-tl with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait!"
    play sound sfx_epic_jump1
    scene sm1fs_t004-162-c1-tl-fall with dissolve
    pause
    play voice2 mc_pain_mff4 noloop
    play sound sfx_leg_kick7
    scene sm1fs_t004-163-c1-mc-catch-tl with vpunch
    pause
    scene sm1fs_t004-164-c1-mc-talk-tl with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "What were you thinking!"
    scene sm1fs_t004-165-c1-tl-talk-mc with dissolve
    play voice4 girl24_disappointed_ohh1 noloop
    tl "That you'd either catch me, or I'd smack into the ground and I could leave early."
    play sound sfx_cloth_rustling1
    scene sm1fs_t004-166-c1-mc-talk-tl with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Jesus, Taisia."
    scene sm1fs_t004-167-c1-tl-talk-mc with dissolve
    play voice4 girl24_disappointed_eeh2 noloop
    tl "What! I'm boooooored!"
    scene sm1fs_t004-168-c1-mc-talk-tl with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Why is this so boring to you?"
    scene sm1fs_t004-169-c1-tl-talk-mc with dissolve
    play voice4 girl24_hey_angry noloop
    tl "I've said it before - it's not creature stuff. Or monster stuff. It's just... 'actress' stuff."
    scene sm1fs_t004-170-c1-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "And why is actress stuff so boring."
    scene sm1fs_t004-171-c1-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_hm1 noloop
    tl "It just is. I'd rather be a clown, or wendigo, or... or... literally anything else."
    scene sm1fs_t004-172-c1-mc-talk-tl with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "Why are you so obsessed with monsters?"
    scene sm1fs_t004-173-c1-tl-talk-mc with dissolve
    play voice4 girl24_thinking_huh1 noloop
    tl "Because they're unique. Different. Misunderstood."
    scene sm1fs_t004-174-c1-mc-talk-tl with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Huh."
    scene sm1fs_t004-175-c1-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_huh2 noloop
    tl "What?"
    scene sm1fs_t004-176-c1-mc-talk-tl with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I don't know... I thought you were going to say something like 'because they scare the shit out of people'. That was... I don't know, deep?"
    scene sm1fs_t004-177-c1-tl-talk-mc with dissolve
    play voice4 girl24_angry_err2 noloop
    tl "Shut up and let me catch you before you say something else stupid."
    scene sm1fs_t004-178-c1-mc-inner-talk with dissolve
    play voice2 mc_yes_ugu1 noloop
    mct "Yeah... I'm the one being stupid."
    scene sm1fs_t004-179-c1-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_huh1 noloop
    tl "You ready?"
    scene sm1fs_t004-180-c1-mc-talk-tl with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "You promise to catch me?"
    scene sm1fs_t004-181-c1-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_kgh1 noloop
    tl "You going to say something else stupid?"
    scene sm1fs_t004-182-c1-mc-talk-tl with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "Uhhhh..."
    scene sm1fs_t004-183-c1-tl-talk-mc with dissolve
    play voice4 girl24_disappointed_hmf noloop volume 1.5
    tl "Just fall already, you big baby."
    scene sm1fs_t004-184-c1-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "Here goes nothing..."
    play sound sfx_epic_jump1
    scene sm1fs_t004-185-c1-mc-inner-talk with dissolve
    mct "God I hope she catches me."
    play sound sfx_leg_kick8
    scene sm1fs_t004-186-c1-tl-catch-mc with vpunch
    pause
    scene sm1fs_t004-187-c1-mc-talk-tl with dissolve
    play voice2 mc_happy_wooh2 noloop
    mc "Woooo... I thought you were going to drop me."
    scene sm1fs_t004-188-c1-tl-talk-mc with dissolve
    play voice4 girl24_yes_aga noloop
    tl "I thought about it."
    scene sm1fs_t004-189-c1-mc-talk-tl with dissolve
    play voice2 mc_surprised_what4 noloop
    mc "What!?"
    play sound sfx_fall_down1
    scene sm1fs_t004-190-c1-tl-drop-mc with dissolve
    play voice4 girl24_angry_argh3 noloop
    tl "I told you not to say anything stupid."
    scene sm1fs_t004-191-c1-mc-talk-tl with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "That wasn't stupid!"
    play sound sfx_cloth_rustling5
    scene sm1fs_t004-192-c1-tl-talk-mc with dissolve
    play voice4 girl24_yes_angry noloop
    tl "Yes it was."
    if player.has_played_scene("sm1cs_tl003"):
        tl "We're business partners now. I wouldn't want my costar getting fucked up. Because that would fuck with my money."
    else:
        tl "I'm trying to convince you to hire me. Why would I let you get hurt?"
    play sound sfx_hands_clap2
    scene sm1fs_t004-193-c1-mc-talk-tl with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Good point."
    scene sm1fs_t004-194-c1-mc-talk-tl with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Thanks."
    scene sm1fs_t004-195-c1-tl-talk-mc with dissolve
    play voice4 girl24_happy_mmm noloop
    tl "You learn to trust me yet?"
    scene sm1fs_t004-196-c1-mc-talk-tl with dissolve
    play voice2 mc_yes_yes8 noloop
    mc "I guess so."
    scene sm1fs_t004-197-c1-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_hm4 noloop
    tl "Learn to stop saying stupid shit?"
    scene sm1fs_t004-198-c1-mc-talk-tl with dissolve
    play voice2 mc_no_no6 noloop
    mc "That one... not so much."
    scene sm1fs_t004-199-c1-tl-talk-mc with dissolve
    play voice4 girl24_arrogant_pff noloop
    tl "Whatever. At least we're closer to being done."
    jump sm1fs_t004_trust_fall_menu
label sm1fs_t004_km_trust_fall:
    scene sm1fs_t004-200-c2-mc-km with dissolve
    pause
    scene sm1fs_t004-201-c2-mc-talk-km with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Hey, Kellie."
    scene sm1fs_t004-202-c2-km-talk-mc with dissolve
    play voice3 girl31_arrogant_huh1 noloop
    km "What do you want?"
    scene sm1fs_t004-203-c2-mc-talk-km with dissolve
    play voice2 d2s12_emmm noloop volume 1.5
    mc "Uhm, just trying to do the trust falls-"
    scene sm1fs_t004-204-c2-km-talk-mc with dissolve
    play voice3 girl31_no_nah noloop
    km "I'm not doing a trust fall with you."
    scene sm1fs_t004-205-c2-mc-talk-km with dissolve
    play voice2 mc_surprised_why2 noloop
    mc "Why?"
    scene sm1fs_t004-206-c2-km-talk-mc with dissolve
    play voice3 girl31_arrogant_ha noloop
    km "Because."
    scene sm1fs_t004-207-c2-mc-talk-km with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Becaaaaaause...?"
    scene sm1fs_t004-206-c2-km-talk-mc with dissolve
    play voice3 girl31_arrogant_geh noloop
    km "I don't owe you an explanation."
    scene sm1fs_t004-205-c2-mc-talk-km with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Well... we have to do this..."
    scene sm1fs_t004-208-c2-mc-talk-km with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "What if... I go first?"
    scene sm1fs_t004-209-c2-km-talk-mc with dissolve
    play voice3 girl31_surprised_uh2 noloop
    km "What?"
    scene sm1fs_t004-210-c2-mc-talk-km with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I'll go first."
    scene sm1fs_t004-211-c2-mc-inner-talk with dissolve
    play voice2 d14s16_smell noloop
    mct "I feel like this might be a bad idea..."
    scene sm1fs_t004-212-c2-km-talk-mc with dissolve
    play voice3 girl31_no_uhuh noloop
    km "I won't catch you."
    play sound sfx_epic_jump1
    scene sm1fs_t004-213-c2-mc-talk-km with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "Well... I'm falling!"
    play voice3 girl31_angry_ergh1 noloop
    play sound sfx_leg_kick8
    scene sm1fs_t004-214-c2-km-catch-mc with vpunch
    pause
    scene sm1fs_t004-215-c2-mc-talk-km with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "God, I was really hoping you'd catch me."
    scene sm1fs_t004-216-c2-km-talk-mc with dissolve
    play voice3 girl31_angry_dagh noloop
    km "You're an asshole."
    scene sm1fs_t004-217-c2-mc-talk-km with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Well, we need to do this... right?"
    play sound sfx_cloth_rustling1
    scene sm1fs_t004-218-c2-km-talk-mc with dissolve
    play voice3 girl31_arrogant_fff noloop
    km "Whatever."
    km "Just because you did it, doesn't mean I will."
    scene sm1fs_t004-220-c2-mc-talk-km with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "But-"
    scene sm1fs_t004-219-c2-km-talk-mc with dissolve
    play voice3 girl31_angry_ergh7 noloop
    km "You won't change my mind, so scram."
    scene sm1fs_t004-220-c2-mc-talk-km with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "Fine..."
    jump sm1fs_t004_trust_fall_menu
label sm1fs_t004_vs_trust_fall:
    scene sm1fs_t004-221-c3-mc-vs with dissolve
    pause
    scene sm1fs_t004-222-c3-vs-talk-mc with dissolve
    play voice3 girl33_hey_involved noloop
    vs "Hey, [mcname]!"
    scene sm1fs_t004-223-c3-mc-talk-vs with dissolve
    play voice2 mc_hey_hey6 noloop
    mc "Hey, Veronica."
    scene sm1fs_t004-224-c3-vs-talk-mc with dissolve
    play voice3 girl33_arrogant_huh1 noloop
    vs "Are you ready to do a trust fall?"
    scene sm1fs_t004-225-c3-mc-talk-vs with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Uhm, sure?"
    scene sm1fs_t004-226-c3-vs-talk-mc with dissolve
    play voice3 girl33_thinking_hmm1 noloop
    vs "Ready?"
    scene sm1fs_t004-227-c3-mc-talk-vs with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yep?"
    scene sm1fs_t004-228-c3-vs-fall with dissolve
    play sound sfx_epic_jump1
    pause
    scene sm1fs_t004-229-c3-mc-catch-vs with vpunch
    play sound sfx_leg_kick7
    pause
    scene sm1fs_t004-230-c3-vs-talk-mc with dissolve
    play voice3 girl33_happy_relief noloop
    vs "My hero."
    scene sm1fs_t004-231-c3-mc-talk-vs with dissolve
    play voice2 mc_no_nah1 noloop
    mc "I just caught you, nothing special."
    scene sm1fs_t004-232-c3-vs-talk-mc with dissolve
    play voice3 girl33_thinking_eem1 noloop
    vs "Still, I think the man who managed to stop Lydia is definitely a hero."
    scene sm1fs_t004-233-c3-mc-talk-vs with dissolve
    mc "Veronica-"
    scene sm1fs_t004-234-c3-vs-talk-mc with dissolve
    play voice3 girl33_disappointed_mmf1 noloop
    vs "I know, I know..."
    scene sm1fs_t004-235-c3-vs-talk-mc with dissolve
    vs "But... I don't know... I just think it's so... cool."
    scene sm1fs_t004-236-c3-mc-talk-vs with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Cool, Veronica-"
    scene sm1fs_t004-237-c3-vs-talk-mc with dissolve
    play voice3 girl33_hey_scared noloop
    vs "Look, there was something special about Fetish Locator, and... I just want to know more. I'm sorry I'm weird about it."
    menu:
        "Forgive and forget"(hint="sm1fs_t004_m03_h01"):
            call sm1fs_t004_m03_c01 from _call_sm1fs_t004_m03_c01
            scene sm1fs_t004-238-c3-mc-talk-vs with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "Look, maybe I do need to talk about it more... normalize it, or whatever."
            scene sm1fs_t004-239-c3-mc-talk-vs with dissolve
            mc "And it was kind of a big deal thing... I'm just being a little... I don't know. It's just a lot."
            scene sm1fs_t004-240-c3-vs-talk-vs with dissolve
            play voice3 girl33_yes_aga noloop
            vs "I promise to try and be more chill about it."
            scene sm1fs_t004-238-c3-mc-talk-vs with dissolve
            play voice2 mc_happy_a1 noloop
            mc "Thanks, Veronica."
        "Just move on"(hint="sm1fs_t004_m03_h02"):
            scene sm1fs_t004-242-c3-mc-talk-vs with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "Look, I'm just not ready to talk about it."
            scene sm1fs_t004-241-c3-vs-talk-mc with dissolve
            play voice3 girl33_disappointed_oh noloop
            scene sm1fs_t004-238-c3-mc-talk-vs with dissolve
            vs "Okay... I'm sorry, [mcname]."
            play voice2 mc_happy_a1 noloop
            mc "Just... don't worry about it."
    scene sm1fs_t004-223-c3-mc-talk-vs with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "But, no matter what - I'm glad you trust me."
    scene sm1fs_t004-222-c3-vs-talk-mc with dissolve
    play voice3 girl33_happy_yeah noloop
    vs "Of course! Because... you're my-"
    scene sm1fs_t004-240-c3-vs-talk-vs with dissolve
    play voice3 girl33_thinking_eem2 noloop
    vs "Uhm, my stagehand."
    vs "I should probably get ready for my next trust fall."
    scene sm1fs_t004-242-c3-mc-talk-vs with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Me too."
    jump sm1fs_t004_trust_fall_menu
label sm1fs_t004_workshop_end:
    scene sm1fs_t004-243-dvh-talk with dissolve
    play voice3 girl34_yes_ugu2 noloop
    dvh "Now that we have all had time to do a trust fall together - Kellie, Veronica. Would you please step into the circle."
    scene sm1fs_t004-244-km-talk-dvh with dissolve
    play voice4 girl31_no_angry noloop
    km "No."
    scene sm1fs_t004-245-dvh-talk-km with dissolve
    play voice3 girl34_arrogant_huh3 noloop
    dvh "Why not, Kellie?"
    scene sm1fs_t004-246-km-talk-dvh with dissolve
    km "I won't do a trust fall with Veronica."
    scene sm1fs_t004-247-dvh-talk-km with dissolve
    play voice3 girl34_angry_ahem3 noloop
    dvh "And why do you refuse such an easy exercise."
    scene sm1fs_t004-249-km-talk-vs with dissolve
    play voice4 girl31_angry_kghh1 noloop
    km "Because I don't trust her."
    scene sm1fs_t004-245-dvh-talk-km with dissolve
    play voice3 girl34_arrogant_ha3 noloop
    dvh "What has Veronica done to you, Kellie?"
    scene sm1fs_t004-248-vs-talk-km with dissolve
    play voice5 girl33_surprised_oh noloop
    vs "Whatever it is, I'm sorry!"
    scene sm1fs_t004-249-km-talk-vs with dissolve
    play voice4 girl31_angry_cough4 noloop
    km "Shut up, I don't care!"
    scene sm1fs_t004-250-vs-talk-km with dissolve
    play voice5 girl33_disappointed_mmf2 noloop
    vs "Sorry..."
    scene sm1fs_t004-251-dvh-talk with dissolve
    play voice3 girl34_angry_breath1 noloop
    dvh "I do not have time for this squabble. You two must work it out if we are ever to move forward as a troupe."
    play voice3 girl34_thinking_hmm6 noloop
    dvh "But for now, I must leave. I am to speak with some sponsors about our newest show."
    scene sm1fs_t004-252-tl-talk-dvh with dissolve
    play voice4 girl24_thinking_hmm3 noloop
    tl "Does that mean the workshop is over?"
    scene sm1fs_t004-253-dvh-talk-tl with dissolve
    play voice3 girl34_yes_yeah2 noloop
    dvh "Yeah."
    scene sm1fs_t004-254-tl-talk with dissolve
    play voice4 girl24_arrogant_hm2 noloop
    tl "Fucking finally."
    scene sm1fs_t004-255-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Man. I wonder what their problem is..."
    mct "Maybe I should talk to Kellie about it... or Veronica."
    stop music fadeout 3.0
    stop sound3 fadeout 1.0
    stop sound4 fadeout 2.0
    jump sm1fs_t004_end
label sm1fs_t004_end:
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(THEATER_STORY_LINE, 3, 0, 3, THEATER, LTH_SUB_STAGE, LTH_STAGE_ENTRANCE)
    return
label sm1fs_t004_m01_c01:
    $ player.set_choice("sm1fs_t004_check_storage")
    return
label sm1fs_t004_m03_c01:
    $ player.set_choice("sm1fs_t004_forgive_forget")
    $ CharacterController.get_character("vs").add_point()
    return