label sm1cs_tl001:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    scene sm1cs-tl001-01-sy-studio with Fade(0.5, 0.5, 0.5)
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_keyboard_typing2 volume 1.5 noloop
    pause
    play sound sfx_door_open1
    scene sm1cs-tl001-02-mc-tl-studio with dissolve
    play music music_convo_lofi
    pause
    scene sm1cs-tl001-03-sy-talk-mc with dissolve
    play voice4 stacy_hey_happy1 noloop
    sy "Welcome home, [mcname]!"
    play sound sfx_heels_steps1
    play sound2 sfx_door_closed2 noloop
    scene sm1cs-tl001-04-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Thanks, Stacy."
    play sound sfx_cloth_rustling2
    scene sm1cs-tl001-05-sy-talk-tl with dissolve
    play voice4 stacy_thinking_oh1 noloop
    sy "Good to see you too, Taisia. He already tell you the good news?"
    scene sm1cs-tl001-06-tl-yalk-sy with dissolve
    play voice3 girl24_yes_aga noloop
    tl "He did. He said we had to come here to talk about the next porno."
    scene sm1cs-tl001-07-tl-yalk-mc with dissolve
    play voice3 girl24_surprised_huh3 noloop
    tl "So when are we filming the next sex scene?"
    scene sm1cs-tl001-08-mc-talk-tl with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "We're not entirely sure yet, but we're hoping soon!"
    scene sm1cs-tl001-09-tl-look-mc with dissolve
    play voice3 girl24_arrogant_hm1 noloop
    tl "..."
    scene sm1cs-tl001-10-mc-talk-tl with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What?"
    scene sm1cs-tl001-07-tl-yalk-mc with dissolve
    play voice3 girl24_angry_argh1 noloop
    tl "I thought you were going to say \"tomorrow\" or \"this weekend\"."
    if False:
        scene sm1cs-tl001-10-mc-talk-tl with dissolve
        play voice2 d1s5_mchappy noloop volume 1.6
        mc "We've got a lot of moving parts and aren't exactly liquid-"
        play voice3 girl24_angry_cough2 noloop
        tl "English, please."
        play sound sfx_keyboard_typing1
        scene sm1cs-tl001-13-sy-talk-tl with dissolve
        play voice4 stacy_thinking_emm2 noloop
        sy "We don't have the money right now to finance another film."
        stop sound fadeout 1.0
        scene sm1cs-tl001-14-sy-talk-tl with dissolve
        play voice4 stacy_hey_attention1 noloop
        sy "We're working on getting it figured out, but it's going to take a little bit of time before we're ready to go again."
        sy "But all I do right now is try to get things sorted so that we can keep filming."
    else:
        scene sm1cs-tl001-11-mc-talk-tl with dissolve
        play voice2 d1s5_mchappy noloop volume 1.6
        mc "Well we're still building things up around here, and-"
        scene sm1cs-tl001-12-tl-talk-mc with dissolve
        play voice3 girl24_angry_cough2 noloop
        tl "So when the hell do you think you're going to be ready to start?"
        play voice2 mc_disappointed_ehh5 noloop
        mc "Uhh..."
        play sound sfx_keyboard_typing1
        scene sm1cs-tl001-13-sy-talk-tl with dissolve
        play voice4 stacy_thinking_emm2 noloop
        sy "We're really not sure, Taisia. First we needed to get a star - like you - and now we need to get all of the other stuff figured out to make the studio kosher."
        stop sound fadeout 1.0
        scene sm1cs-tl001-14-sy-talk-tl with dissolve
        play voice4 stacy_hey_attention1 noloop
        sy "Sorry, there's a lot that goes into opening a studio! There's paperwork, and gear, and testing, and props, and sets, and..."
        sy "It's literally all I do these days."
    scene sm1cs-tl001-15-tl-talk-sy with hpunch
    play voice3 girl24_arrogant_huh2 noloop
    tl "So how long is it going to take you to figure it out?"
    scene sm1cs-tl001-16-sy-talk-tl with dissolve
    play sound sfx_keyboard_typing2
    play voice4 stacy_no_nah1 noloop
    sy "I honestly have no idea right now."
    stop sound fadeout 1.0
    scene sm1cs-tl001-17-tl-talk-mc with dissolve
    play voice3 girl24_angry_argh5 noloop
    tl "What was this, some weird con to try and fuck me?"
    scene sm1cs-tl001-18-tl-talk with dissolve
    play voice3 girl24_arrogant_hm3 noloop
    tl "I mean, people have tried weirder so I get it, but-"
    scene sm1cs-tl001-19-mc-talk-tl with dissolve
    play voice2 mc_no_no7 noloop
    mc "No, no! I promise we're legit. It just takes some time, you know?"
    scene sm1cs-tl001-20-tl-talk-mc with dissolve
    play voice3 girl24_no_uhuh noloop
    tl "I don't have the luxury of time."
    scene sm1cs-tl001-21-mc-talk-tl with dissolve
    play voice2 mc_surprised_what7 noloop
    mc "What do you mean?"
    play sound sfx_heels_steps1 loop
    scene sm1cs-tl001-22-tl-talk-mc with dissolve
    play voice3 girl24_disappointed_eeh1 noloop
    tl "Forget it.{w} If you two don't have work for me, I'm going to have to try and find something else."
    play sound sfx_skirt_off2
    scene sm1cs-tl001-23-mc-talk-tl with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Woah, hang on a sec!"
    scene sm1cs-tl001-24-mc-talk-tl with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Taisia, what's going on?"
    scene sm1cs-tl001-25-tl-talk-mc with dissolve
    play voice3 girl24_disappointed_neh noloop
    tl "I don't want to get into it."
    scene sm1cs-tl001-26-mc-talk-tl with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "You know, we might work together, but you can also talk to us about stuff."
    mc "So what's going on?"
    scene sm1cs-tl001-27-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_hm4 noloop
    tl "I don't want to talk about it."
    scene sm1cs-tl001-28-mc-talk-tl with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, su-"
    scene sm1cs-tl001-29-tl-talk-mc with dissolve
    play voice3 girl24_no_nonono1 noloop
    tl "I {i}seriously{/i} don't want to talk about it."
    scene sm1cs-tl001-30-mc-talk-tl with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Okay, I won't press. But you gotta give me something here."
    scene sm1cs-tl001-31-tl-talk-mc with dissolve
    play voice3 girl24_angry_err2 noloop
    tl "Fine."
    scene sm1cs-tl001-32-tl-talk-mc with dissolve
    play voice3 girl24_hey_angry noloop
    tl "Look, long story short, I just need some consistent extra income. I do a lot of side work, but I need something that pays better and is a sure thing."
    scene sm1cs-tl001-33-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Okay?"
    scene sm1cs-tl001-34-tl-talk-mc with dissolve
    play voice3 girl24_happy_mmm noloop
    tl "A dude just offered me a gig, and I think it'll be good. Not as fun as riding you, but a pretty close second honestly."
    scene sm1cs-tl001-35-mc-talk-tl with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Why can't you do both?"
    scene sm1cs-tl001-36-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_yeah3 noloop
    tl "The other one would take up most of my free time. It would be awesome but... Just not something I want to do right now."
    tl "But I've just got a big expense I {i}need{/i} to make. I was hoping your thing would cover that, but if it's going to be a while before you start making movies on the regular, I have to move on."
    tl "No hard feelings or anything, just bad timing."
    scene sm1cs-tl001-37-mc-talk-tl with dissolve
    play voice2 mc_thinking_wait3 noloop
    mc "Just wait. {w}What if{w} we figure something out and make a movie?"
    scene sm1cs-tl001-38-tl-talk-mc with dissolve
    play voice3 girl24_surprised_huh4 noloop
    tl "Didn't you literally just say you didn't know when you could be making your next thing?"
    scene sm1cs-tl001-40-mc-talk-tl with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "I did, but I also didn't know you needed to make something so soon."
    scene sm1cs-tl001-41-tl-talk-mc with dissolve
    play voice3 girl24_arrogant_yeah2 noloop
    tl "Yeah."
    scene sm1cs-tl001-42-mc-talk-tl with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Look, I'm going to be honest with you. I think you'd make a great pornstar and I don't want to lose you to some other job."
    scene sm1cs-tl001-43-tl-talk-mc with dissolve
    play voice3 girl24_disappointed_ohh1 noloop
    tl "Even though my \"performance\" could use some work?"
    scene sm1cs-tl001-37-mc-talk-tl with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "I mean, so could mine. How will we ever get better if you quit before we even start."
    scene sm1cs-tl001-39-tl-talk-mc with dissolve
    play voice3 girl24_thinking_emm2 noloop
    tl "Still doesn't change the fact that I need to be working ASAP."
    scene sm1cs-tl001-40-mc-talk-tl with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Then we can start working, ASAP."
    play voice3 girl24_surprised_what1 noloop
    tl "Really?"
    scene sm1cs-tl001-45-sy-talk-mc with dissolve
    play voice4 stacy_hey noloop
    sy "Hang on a sec, [mcname]-"
    scene sm1cs-tl001-46-mc-talk-tl with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes, really. Stacy and I can start working on putting a small little film together for us to get working on. It won't be a big, blockbuster production, but you need to start somewhere, right?"
    scene sm1cs-tl001-47-tl-talk-mc with dissolve
    play voice3 girl24_happy_yeah1 noloop
    tl "Right. So when do you think you'd be ready to film that?"
    scene sm1cs-tl001-48-mc-talk-tl with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "I mean, we need a little time to get everything put together, but really soon."
    scene sm1cs-tl001-49-tl-talk-mc with dissolve
    play voice3 girl24_surprised_huh2 noloop
    tl "Do you mean that?"
    scene sm1cs-tl001-48-mc-talk-tl with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course! I don't want to lose you, and making a movie could be just the thing for the studio right now."
    scene sm1cs-tl001-50-tl-talk-mc-sy with dissolve
    play voice3 girl24_happy_laugh1 noloop
    tl "Okay, I guess I can linger for a little bit."
    tl "But you can't keep me on the hook too long."
    scene sm1cs-tl001-33-mc-talk-tl with dissolve
    play voice2 mc_no_nono1 noloop
    mc "I promise we won't. Me and Stacy are going to talk about it right now, and start figuring it out."
    mc "Right, Stacy?"
    scene sm1cs-tl001-51-sy-talk-mc with dissolve
    play voice4 stacy_yes_yeah1 noloop
    sy "Sure."
    scene sm1cs-tl001-48-mc-talk-tl with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "See? I have literally the best person on the planet who's going to help me figure it out. We'll be filming in no time."
    scene sm1cs-tl001-49-tl-talk-mc with dissolve
    play voice3 girl24_yes_ugu noloop
    tl "Cool."
    tl "Call me whenever you get a plan together, yeah?"
    scene sm1cs-tl001-50-tl-talk-mc-sy with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "I promise you I will!"
    play voice3 girl24_yes_yap noloop
    tl "Good. I'm excited for it."
    play sound sfx_heels_steps1 loop
    tl "Catch you two on the flipside."
    play sound sfx_door_closed7
    scene sm1cs-tl001-51-sy-talk-mc with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "*groans* [mcname]."
    scene sm1cs-tl001-52-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "I know, I know."
    scene sm1cs-tl001-53-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "Why the hell did you tell her we were going to make a movie soon? We have, like, no money right now."
    scene sm1cs-tl001-54-mc-talk-sy with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    if True:
        mc "What was I supposed to do? Lose one of our first actresses to some regular, boring job?"
    else:
        mc "What was I supposed to do? Lose some grade-A hottie with a body to some boring desk job?"
    scene sm1cs-tl001-55-sy-talk-mc with dissolve
    play voice3 stacy_no_angry1 noloop
    sy "No, but you shouldn't make empty promises like that."
    play sound sfx_cloth_rustling4
    scene sm1cs-tl001-56-mc-talk-sy with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Come on, I think doing something with her will be good for us. You know, make something like a portfolio piece with her."
    scene sm1cs-tl001-57-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "I don't know [mcname]..."
    scene sm1cs-tl001-58-mc-talk-sy with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "What don't you know? I mean, think about it. We have a willing actress, who is down to do whatever, and is chomping at the bit to do whatever. I think we should use it!"
    scene sm1cs-tl001-59-sy-talk-mc with dissolve
    play voice3 stacy_yes_okay1 noloop
    if True:
        sy "Okay, sure. But you're the one who's going to have to pay her. Because the studio is making no money right now."
    else:
        sy "Okay, sure. But you're the one who's going to have to pay her. Because the studio can't afford to pay her right now."
    scene sm1cs-tl001-60-mc-talk-sy with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Fine, if that's what I have to do to keep Taisia around, that's what I have to do."
    scene sm1cs-tl001-61-sy-talk-mc with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "So Mr. Pornstar, what the hell is this movie going to be about?"
    scene sm1cs-tl001-62-mc-talk-sy with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "I honestly have no clue."
    play sound sfx_heels_steps2
    scene sm1cs-tl001-63-sy-talk-mc with dissolve
    play voice3 stacy_laugh4 noloop
    sy "Well you have to figure that out if you plan to keep Taisia around."
    sy "You did just promise her her own little movie."
    scene sm1cs-tl001-64-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah6 noloop
    mc "Yeah... I don't know."
    mc "I know nothing about her. Like what would she be interested in filming, what kind of movie she would want to make..."
    stop sound fadeout 1.0
    scene sm1cs-tl001-65-sy-talk-mc with dissolve
    play voice3 stacy_huh2 noloop
    sy "You better figure out something. Taisia doesn't seem to be the type to forgive easily."
    play sound sfx_cloth_rustling1
    scene sm1cs-tl001-66-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah, yeah. I get it. I'll make sure to talk to you about this in the future."
    scene sm1cs-tl001-67-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    if persistent.is_special:
        sy "Just remember, sister knows best."
    else:
        sy "Good, I'm glad you are starting to realize that I know what I'm talking about."
    scene sm1cs-tl001-68-mc-talk-sy with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I've always known that, Stacy."
    scene sm1cs-tl001-67-sy-talk-mc with dissolve
    play voice3 stacy_angry noloop
    sy "Well maybe you'll finally start to listen to me then!"
    play sound sfx_heels_steps2 loop
    scene sm1cs-tl001-66-mc-talk-sy with dissolve
    play voice2 d2s9_confused noloop
    mc "Will you help me figure this out?"
    scene sm1cs-tl001-69-sy-talk-mc with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Of course I will."
    play voice2 mc_happy_oof1 noloop
    mc "Thanks, Stacy. I owe you."
    sy "I'll put it on the tab."
    scene sm1cs-tl001-70-mc-talk-sy with dissolve
    play sound sfx_keyboard_typing2
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "What would I do without you?"
    stop sound fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(TL_STORY, 2, 0, 1, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return