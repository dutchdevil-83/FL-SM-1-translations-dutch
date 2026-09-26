image sm1ms018-a04-glm = Movie(play = "images/ms/s018/anim/sm1ms018-a04-3x-60fps.webm", start_image = "sm1ms018-a04 theater-glambot-000", image = "sm1ms018-a04 theater-glambot-120", loop = False)
label sm1ms018:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music music_another_theater_day fadein 2.0
    scene sm1ms018-01-tl-act with dissolve
    play voice4 girl24_arrogant_hm1 noloop
    pause
    scene sm1ms018-02-km-vs-act with dissolve
    play voice5 girl31_arrogant_nrgh noloop
    pause
    scene sm1ms018-03-dvh with dissolve
    play voice6 girl34_arrogant_laugh2 noloop
    pause
    play sound sfx_double_door1
    scene sm1ms018-a04 theater-glambot-000 with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1ms018-a04-glm
    pause
    play voice3 stacy_surprised_wow1 noloop
    sy "Woah, this place is really cool."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms018-06-mc-talk with dissolve
    play voice4 girl34_surprised_oh4 noloop
    my "Ooooh. They look like they're in the middle of a practice."
    scene sm1ms018-07-sy-talk-mc with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "You know it's high time I came to see a show here."
    sy "See if your acting skills have improved."
    if True:
        scene sm1ms018-08-c1-mc-talk-sy with dissolve
        play voice2 mc_no_nah2 noloop
        mc "I'm not in the show."
        mc "Not yet anyhow."
        scene sm1ms018-09-c1-sy-talk-mc with dissolve
        play voice3 stacy_hey_happy2 noloop
        sy "But it's only a matter of time, right."
    if False:
        scene sm1ms018-11-c2-mc-talk-sy with dissolve
        play voice2 d3s11b_mcheh noloop volume 1.7
        mc "Haha. I'm sure you'll get the chance soon."
        mc "Right now, we're still waiting to hear what kind of show Denise wants to run."
    if False:
        scene sm1ms018-12-c3-mc-talk-sy with dissolve
        play voice2 d3s11b_mcheh noloop volume 1.7
        mc "Haha. It should be."
        mc "Denise has figured out what she wants to do for the next show."
        scene sm1ms018-13-c3-mc-talk with dissolve
        play voice2 mc_thinking_hmm3 noloop
        mc "It's a little strange but it should be fun."
    scene sm1ms018-14-my-talk-mc with dissolve
    play voice4 girl34_thinking_hmm5 noloop
    my "It would be delightful to see you up on the stage, [mcname]."
    scene sm1ms018-15-mc-talk-my with dissolve
    play voice2 mc_happy_a1 noloop
    if persistent.is_special:
        mc "Thanks Mom."
    else:
        mc "Thanks Melony."
    play sound sfx_heels_steps2 loop
    scene sm1ms018-16-mc-talk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Come on, let's go meet the ensemble."
    stop sound fadeout 1.0
    scene sm1ms018-17-tl-talk with dissolve
    play voice5 girl24_happy_laugh3 noloop
    tl "*chuckles* Gah, those flirty lines are the worst."
    tl "I totally butchered it."
    scene sm1ms018-18-dvh-talk-mc with dissolve
    play voice6 girl34_no_angry8 noloop
    dvh "No arguments here."
    play sound2 sfx_heels_steps1 fadein 8.0
    play sound sfx_heels_steps2 fadein 8.0 loop
    scene sm1ms018-19-tl-talk-dvh with dissolve
    play voice5 girl24_happy_laugh4 noloop
    tl "Haha."
    tl "So serious, Denise."
    scene sm1ms018-20-dvh-talk-tl with dissolve
    play voice6 girl34_arrogant_yeah noloop
    dvh "Someone has to be, Taisia. It's the only way we'll get this crew any notoriety."
    scene sm1ms018-21-dvh-talk-tl with dissolve
    play voice6 girl34_arrogant_hm1 noloop
    dvh "It would be spectacular to have the house full once."
    scene sm1ms018-22-tl-talk-dvh with dissolve
    play voice5 girl24_surprised_eeh2 noloop
    tl "We get paid more when that happens, right?"
    scene sm1ms018-23-dvh-talk-tl with dissolve
    play voice6 girl34_angry_breath1 noloop
    dvh "*sighs*"
    scene sm1ms018-24-vs-talk with dissolve
    play voice7 girl33_hey_involved noloop
    vs "Hey, it's [mcname]."
    scene sm1ms018-25-mc-talk with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hi everyone."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms018-26-tl-talk-mc-sy with dissolve
    play voice5 girl24_surprised_oh1 noloop
    if persistent.is_special:
        tl "[mcname] and sister Stacy."
    else:
        tl "[mcname] and his best pal, Stacy."
    play sound sfx_cloth_rustling2
    scene sm1ms018-27-tl-talk with dissolve
    play voice5 girl24_arrogant_huh2 noloop
    tl "You I don't know."
    scene sm1ms018-28-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah2 noloop
    if persistent.is_special:
        mc "Uh right. This is Melony, my mom."
        scene sm1ms018-29-tl-talk-my-sy with dissolve
        play voice5 girl24_thinking_ah noloop
        tl "Ah, I can see where Stacy gets her good looks."
        scene sm1ms018-30-my-talk-tl with dissolve
        play voice4 girl34_surprised_oh5 noloop
        my "Oh my. Thank you. Miss..."
    else:
        mc "Right. This is Melony, a friend of the family."
    scene sm1ms018-31-mc-talk-my with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "This is Taisia, she introduced me to the theater."
    scene sm1ms018-32-mc-talk-vs with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Veronica."
    scene sm1ms018-33-vs-talk with dissolve
    play voice6 girl33_hey_serious noloop
    vs "Hi!"
    scene sm1ms018-34-mc-talk-km with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Kellie."
    scene sm1ms018-35-km-talk with dissolve
    play voice5 girl31_hey_excited noloop
    km "Hey."
    scene sm1ms018-36-mc-talk-dvh with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "And finally, our director, Denise."
    scene sm1ms018-37-dvh-talk-mc with dissolve
    play voice6 girl34_arrogant_hm3 noloop
    dvh "Hmph."
    dvh "And why exactly did you bring them here?"
    scene sm1ms018-38-mc-talk-dvh with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, just wanted to show them a bit of where I work."
    scene sm1ms018-39-dvh-talk-mc with dissolve
    play voice6 girl34_arrogant_ha3 noloop
    dvh "*sighs* I see..."
    dvh "Well, as you can tell, we're in the middle of a bit of practice and this is not a great time for a tour."
    scene sm1ms018-40-mc-talk-dvh with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Oh right. I should have checked."
    scene sm1ms018-41-tl-talk with dissolve
    play voice5 girl24_no_nah noloop
    tl "She's just in a bad mood."
    scene sm1ms018-42-tl-talk-mc with dissolve
    play voice5 girl24_yes_aga noloop
    tl "Come on, I'll give you the quick tour."
    scene sm1ms018-43-dvh-talk with dissolve
    play voice6 girl34_angry_nergh noloop
    dvh "I need a cigarette."
    scene sm1ms018-44-dvh-talk with dissolve
    play voice6 girl34_angry_ahem1 noloop
    dvh "Take five everyone."
    scene sm1ms018-45-vs-talk-dvh with dissolve
    play voice7 girl33_happy_wooh noloop
    vs "Wooh. Then I'm going on the tour."
    jump sm1ms018_backstage
label sm1ms018_backstage:
    play sound sfx_double_door1
    scene sm1ms018-46-theater-backstage with fade
    pause
    scene sm1ms018-47-tl-talk with dissolve
    play voice5 girl24_thinking_huh1 noloop
    tl "This is the backstage area, where the real magic happens."
    scene sm1ms018-48-tl-talk with dissolve
    play voice5 girl24_thinking_emm2 noloop
    if True:
        tl "This is [mcname]'s domain. He works here with Bruce, our stage director."
    else:
        tl "This was where we kept [mcname] when he first started out."
        tl "He would work with Bruce, our stage director."
        scene sm1ms018-49-tl-talk with dissolve
        play voice5 girl24_happy_yeah1 noloop
        tl "But now he's doing lines with the rest of us."
        scene sm1ms018-50-sy-talk-tl with dissolve
        play voice3 stacy_thinking_oh2 noloop
        sy "So his acting has improved."
        scene sm1ms018-51-tl-talk-sy with dissolve
        play voice5 girl24_yes_yap noloop
        tl "Yup."
    scene sm1ms018-52-vs-talk with dissolve
    play voice6 girl33_happy_relief noloop
    vs "I want to show them our dressing rooms next."
    scene sm1ms018-53-tl-talk-vs with dissolve
    play voice5 girl24_yes_ugu noloop
    tl "Knock yourself out."
    play sound sfx_heels_steps2
    scene sm1ms018-54-vs-talk with dissolve
    play voice6 girl33_happy_nice noloop
    vs "Follow me."
    play sound2 sfx_heels_steps1
    scene sm1ms018-55-vs-talk-my-sy with dissolve
    play voice6 girl33_arrogant_huh2 noloop
    vs "And this is the path we take when we're all done with hair and makeup."
    vs "It's like our VIP access."
    stop sound fadeout 7.0
    stop sound2 fadeout 7.0
    scene sm1ms018-56-tl-talk-mc with dissolve
    play voice5 girl24_surprised_huh3 noloop
    if persistent.is_special:
        tl "Hey, so how much does your mom like..."
    else:
        tl "Hey, so... how much does Melony like..."
    tl "How much does she know about the stuff you've been doing?"
    scene sm1ms018-58-mc-talk-tl with dissolve
    play voice2 mc_angry_off noloop
    mc "More than I wish."
    mc "Someone sent her a video that Stacy and I made."
    scene sm1ms018-59-mc-talk-tl with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "She hasn't realized that it was Stacy and I, but she knows I want to make a career making porn."
    play sound sfx_cloth_rustling1
    scene sm1ms018-60-tl-talk-mc with dissolve
    play voice5 girl24_happy_laugh5 noloop
    tl "Hahaha."
    scene sm1ms018-61-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Glad I could entertain."
    scene sm1ms018-62-tl-talk-mc with dissolve
    play voice5 girl24_disappointed_ohh1 noloop
    tl "I'm sorry. I know it's bad but that really is fucking hilarious."
    tl "If I ever told my parents anything like {i}that{/i}, it would probably be when they couldn't really hear me."
    scene sm1ms018-63-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah that might have been the better approach for me."
    scene sm1ms018-64-vs-talk with dissolve
    play voice6 girl33_yes_aga noloop
    vs "And this is my dressing room."
    scene sm1ms018-65-vs-talk with dissolve
    play voice6 girl33_surprised_oh noloop
    vs "Oh yeah, it's also used by Taisia and [mcname]. I almost forgot."
    play sound sfx_door_openclosed2 volume 1.5
    scene sm1ms018-66-dressing-room with fade
    pause
    scene sm1ms018-67-vs-talk with dissolve
    play voice6 girl33_happy_yay noloop
    vs "Ta-dah!"
    vs "It's not much, but it could be better."
    scene sm1ms018-68-vs-talk with dissolve
    play voice6 girl33_arrogant_huh1 noloop
    vs "One day soon I'll probably have my own private dressing room."
    play sound sfx_cloth_rustling3
    scene sm1ms018-69-vs-talk with dissolve
    play voice6 girl33_disappointed_oh noloop
    vs "It will probably suck not having any friends to hang out with before I do a scene."
    scene sm1ms018-70-vs-talk with dissolve
    play voice6 girl33_happy_laugh1 noloop
    vs "But I'll also be a movie star, and that's what I've always dreamed about."
    scene sm1ms018-71-my-talk-vs with dissolve
    play voice4 girl34_yes_aga1 noloop
    my "Uh-huh. Well I hope you have a lot of success, Veronica."
    scene sm1ms018-72-vs-talk-my with dissolve
    play voice6 girl33_happy_yeah noloop
    vs "Thank you so much, Melony. You're super nice."
    play sound sfx_phone_buzz
    scene sm1ms018-73-vs-phone with dissolve
    play voice6 girl33_thinking_hmm1 noloop
    vs "Hmmm."
    scene sm1ms018-74-vs-talk-tl with dissolve
    play voice6 girl33_disappointed_off noloop
    vs "Oooh. Looks like Denise wants us to run the scene again."
    scene sm1ms018-75-vs-talk-tl with dissolve
    play voice6 girl33_arrogant_hm noloop
    vs "Come on, Taisia."
    scene sm1ms018-77-tl-talk-vs with dissolve
    play voice5 girl24_disappointed_neh noloop
    tl "I'm so excited."
    tl "Later. Was nice to meet you, Melony."
    play voice4 girl34_yes_ugu1 noloop
    my "You too."
    play sound sfx_door_openclosed2 volume 1.6
    scene sm1ms018-78-mc-talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "So yeah, that's pretty much the tour, apart from Denise's office, but we'll skip that."
    scene sm1ms018-79-mc-talk-my with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What do you think?"
    if player.has_played_scene("sm1ms015"):
        scene sm1ms018-80-my-talk-mc with dissolve
        play voice4 girl34_thinking_emm5 noloop
        my "Well this place is certainly no Orbix."
        scene sm1ms018-81-my-talk-mc with dissolve
        play voice4 girl34_disappointed_ehh1 noloop
        my "I wish that you found another place with a bit more structure, but then, a little structure goes a long way."
        scene sm1ms018-82-my-talk-mc with dissolve
        play voice4 girl34_thinking_hmm6 noloop
        my "The most important thing I can ask is that the job pays well and you enjoy it."
        my "Is that the case?"
        scene sm1ms018-83-mc-talk-my with dissolve
        play voice2 mc_yes_yes3 noloop
        mc "Oh yes."
        mc "Being here at the theater is so different than just about anything else I've done."
        scene sm1ms018-84-mc-talk-my with dissolve
        play voice2 mc_thinking_mmm4 noloop
        mc "I'm really enjoying myself."
        scene sm1ms018-85-mc-talk-my with dissolve
        play voice2 d1s5b_ehhh noloop volume 1.6
        if True:
            mc "The money is probably the area that needs the most improvement."
            mc "But I think once I'm actually an actor, all of that will change."
            scene sm1ms018-86-my-talk-mc with dissolve
            play voice4 girl34_yes_aga4 noloop
            my "Glad to hear it."
        else:
            mc "The money could be a little better, but once the new show starts, I think things will improve."
            scene sm1ms018-86-my-talk-mc with dissolve
            play voice4 girl34_yes_aga4 noloop
            my "Glad to hear it."
    else:
        scene sm1ms018-80-my-talk-mc with dissolve
        play voice4 girl34_thinking_emm5 noloop
        my "It's all a bit much for me, but everyone seems very animated."
        scene sm1ms018-81-my-talk-mc with dissolve
        play voice4 girl34_disappointed_ehh1 noloop
        my "When I was in high school, theater kids always kind of gave off an arrogant vibe."
        my "A little like that Denise..."
        scene sm1ms018-82-my-talk-mc with dissolve
        play voice4 girl34_thinking_hmm6 noloop
        my "But if you're enjoying your time here, then who am I to say anything."
    scene sm1ms018-87-my-talk with dissolve
    play voice4 girl34_angry_ahem2 noloop
    my "*ahem* And I did notice that many of these actresses are quite easy on the eyes."
    scene sm1ms018-88-my-talk-mc with dissolve
    play voice4 girl34_arrogant_ha4 noloop
    my "I'll wager that you have a mind to ask one or two to join your..."
    my "{i}Other{/i} work down the line."
    scene sm1ms018-89-mc-talk-my with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "The thought had crossed my mind. But it's not like it's the first thing I bring up."
    mc "I only talk to people about working with us if we feel that it's something up their alley."
    play sound sfx_cloth_rustling2
    scene sm1ms018-90-my-talk-mc with dissolve
    play voice4 girl34_arrogant_ugu2 noloop
    my "Well that's good to know."
    my "I will say you should probably stay clear of Veronica."
    scene sm1ms018-91-mc-talk-my with dissolve
    play voice2 mc_surprised_why3 noloop
    mc "Why do you say that?"
    scene sm1ms018-92-my-talk-mc with dissolve
    play voice4 girl34_disappointed_eeh4 noloop
    my "You heard her, she definitely has higher aspirations than working here."
    my "She seems super focused on becoming a movie star, and I doubt she has a kinky side."
    if player.has_played_scene("sm1cs_vs002"):
        scene sm1ms018-93-mc-inner-talk with dissolve
        play voice2 mc_arrogant_heh3 noloop
        if persistent.is_special:
            mct "Haha. You might be wrong about that, Mom."
        else:
            mct "Haha. You might be wrong about that, Melony."
    else:
        scene sm1ms018-94-mc-talk-my with dissolve
        play voice2 mc_yes_yeah6 noloop
        mc "Yeah, you're probably right."
    scene sm1ms018-95-my-talk-mc with dissolve
    play voice4 girl34_thinking_eeh1 noloop
    my "Well, I think I've taken enough of your time today, [mcname]."
    my "But I appreciate you showing me the theater."
    scene sm1ms018-96-my-talk with dissolve
    play voice4 girl34_disappointed_oh2 noloop
    my "And I look forward to the time Stacy and I can come see you on stage."
    scene sm1ms018-97-sy-talk with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Me too."
    play sound sfx_heels_steps2 loop
    scene sm1ms018-98-mc-talk with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Great."
    play sound sfx_door_open3
    scene sm1ms018-99-mc-talk-my-sy with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "I'll walk us out."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ player.completion_log_add_item_date("sm1ms018")
    $ StoryController.end_scene(MS, 2, 0, 2, THEATER, LTH_SUB_CORRIDOR, LTH_SECOND_CORRIDOR)
    return