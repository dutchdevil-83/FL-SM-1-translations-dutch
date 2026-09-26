label sm1cs_cw003:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_morning_news volume 0.8
    scene sm1cs-cw003-01 mc-excited with dissolve
    play voice2 mc_happy_laugh1 noloop
    mc "You'll never guess what I found out about Claire!"
    scene sm1cs-cw003-02 sy-huh with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "What?"
    scene sm1cs-cw003-03 sy-thinking with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "Wait, which one is Claire again?"
    scene sm1cs-cw003-04 mc-saying with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "My boss."
    scene sm1cs-cw003-05 mc-saying with dissolve
    play voice2 mc_angry_off noloop
    mc "I mean, my boss' boss."
    scene sm1cs-cw003-06 sy-asking with dissolve
    play voice3 stacy_thinking_oh1 noloop
    sy "Right. So what did you find out."
    scene sm1cs-cw003-07 mc-explaining with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "So first she pretends like we're going to this business meeting."
    mc "But it turns out her parents were there."
    scene sm1cs-cw003-08 mc-explaining with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "I'm about to turn around and leave, but then she comes up close."
    mc "Tells me to act like I'm her boyfriend."
    scene sm1cs-cw003-09 sy-shocked with dissolve
    play voice3 stacy_surprised_huh4 noloop
    sy "Wait. This woman had you pretend to be her boyfriend?"
    sy "You were her beard?"
    scene sm1cs-cw003-10 mc-confused with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Beard?"
    scene sm1cs-cw003-11 sy-explaining with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah. It's a cover. Sometimes people use it if they're not \"out\" yet."
    scene sm1cs-cw003-12 mc-talking with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Alright. Interesting."
    mc "So anyhow, there I am, doing my best to pretend like Claire and I are in a relationship."
    mc "Her mom is so relieved, saying she's glad Claire won't have to use that \"kinky\" app anymore."
    scene sm1cs-cw003-13 sy-surprised with dissolve
    play voice3 stacy_surprised_ah1 noloop
    sy "No way."
    scene sm1cs-cw003-14 mc-talking with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Yes way. Claire was using Fetish Locator!"
    scene sm1cs-cw003-15 sy-impressed with dissolve
    play voice3 stacy_surprised_wow1 noloop
    sy "I'm surprised they talked about that with you there."
    sy "You must have really impressed her parents."
    sy "Nice work, [mcname]."
    play sound sfx_chair_slide1
    scene sm1cs-cw003-16 sy-back-to-work with dissolve
    play sound2 sfx_keyboard_enter1 noloop
    pause
    scene sm1cs-cw003-17 mc-talking with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait? That's it?"
    scene sm1cs-cw003-18 sy-huh with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Huh?"
    scene sm1cs-cw003-19 mc-explaining with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "You don't think that we should check the data you kept to figure out what she was into?"
    mc "And see if she might be a potential actress for the studio?"
    scene sm1cs-cw003-20 sy-asking with dissolve
    play voice3 stacy_yes_fine4 noloop
    sy "I mean, sure that is a good point. But do you really want to go digging?"
    sy "I thought we weren't supposed to use the data like that."
    scene sm1cs-cw003-21 mc-saying with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Normally I would agree."
    scene sm1cs-cw003-22 mc-closing-eyes with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "But she \"used\" me first. All things equal, I think it's only fair I get to know a little more about Claire."
    mc "Besides, since I'm her boyfriend, this is just like me getting the information early."
    scene sm1cs-cw003-23 sy-taunting with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "Fake boyfriend."
    scene sm1cs-cw003-24 mc-talking with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Details details."
    scene sm1cs-cw003-25 sy-fine with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Alright, if you're in, I'm in."
    play sound sfx_cloth_rustling3
    scene sm1cs-cw003-26 sy-pulling-it-out with dissolve
    pause
    scene sm1cs-cw003-27 sy-smiling with dissolve
    pause
    scene sm1cs-cw003-28 mc-asking with dissolve
    play voice2 d2s12_emmm noloop volume 1.7
    mc "What is that?"
    scene sm1cs-cw003-29 sy-stating with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "The data."
    sy "Not going to leave it around for AmRose to steal again."
    scene sm1cs-cw003-30 mc-astonished with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "But... in your panties?"
    scene sm1cs-cw003-31 sy-you-want-or-not with dissolve
    play voice3 stacy_hey noloop
    sy "My panties are always kept clean."
    sy "Now, are you going to question my methods, or do you want to check out Claire's naughty list?"
    scene sm1cs-cw003-32 mc-check with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Check the naughty list."
    scene sm1cs-cw003-33 sy-hooking-the-pendrive with dissolve
    pause
    play sound sfx_gadgets_laptop_opened
    scene sm1cs-cw003-34 mc-standing-behind-him with dissolve
    pause
    jump sm1cs_cw003_continue
label sm1cs_cw003_continue:
    scene black
    show screen scene_transistion(_("Fifteen minutes later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_keyboard_enter1
    scene sm1cs-cw003-35 sy-got-it
    with Fade(0.5, 0.5, 0.5)
    play voice3 stacy_happy_yay3 noloop
    sy "Got it. I think this is her."
    scene sm1cs-cw003-37 mc-smiling-horny with dissolve
    play voice2 mc_surprised_ohmy noloop
    mc "Oh yeah, that's definitely her."
    play sound sfx_keyboard_enter1
    scene sm1cs-cw003-39 sy-mc-watching-her-photos-montage with hpunch
    mct "But completely different than how I've seen her before before."
    pause
    play sound sfx_keyboard_enter1
    scene sm1cs-cw003-40 sy-mc-watching-her-photos-montage with dissolve
    pause
    play sound sfx_keyboard_enter1
    scene sm1cs-cw003-41 sy-mc-watching-her-photos-montage with dissolve
    pause
    play sound sfx_keyboard_enter1
    scene sm1cs-cw003-42 sy-mc-watching-her-photos-montage with dissolve
    pause
    play sound sfx_keyboard_enter1
    scene sm1cs-cw003-43 sy-mc-watching-her-photos-montage with dissolve
    pause
    scene sm1cs-cw003-44 sy-talking with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Looks like in her last post before we took FL down, she used some of her points to make a challenge."
    sy "Keep up with your hot redhead dommy and maybe she will keep you."
    menu:
        "Joke"(hint="sm1cs_cw003_m01_h01"):
            call sm1cs_cw003_m01_c01 from _call_sm1cs_cw003_m01_c01
            scene sm1cs-cw003-45 mc-grinning with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "Man, we must have been out of our minds to close down Fetish Locator."
            scene sm1cs-cw003-46 sy-laughing with dissolve
            play voice3 stacy_happy_laugh3 noloop
            sy "Apart from the whole Lydia being a supervillain in training, I agree."
        "Excited"(hint="sm1cs_cw003_m01_h02"):
            scene sm1cs-cw003-47 mc-excited with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "I gotta see this side of her."
            scene sm1cs-cw003-48 sy-talking with dissolve
            play voice3 stacy_thinking_emm3 noloop
            sy "Careful. Looks like it might involve some spanking."
            scene sm1cs-cw003-49 sy-grinning with dissolve
            play voice3 stacy_hey_happy1 noloop
            sy "If you two hook up, make sure she doesn't damage your derriere too much."
            scene sm1cs-cw003-50 mc-agreeing with dissolve
            play voice2 mc_arrogant_heh1 noloop
            mc "Agreed. Besides, I'm usually the one doing the spanking."
            scene sm1cs-cw003-51 sy-kinky with dissolve
            play voice3 stacy_yes_ugu1 noloop
            sy "Mmmhmm."
    scene sm1cs-cw003-52 sy-asking with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "So what are you going to do next?"
    scene sm1cs-cw003-53 mc-talking with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I'm not sure."
    mc "I mean it would be great if she would be down to film a scene or two with us."
    mc "I'm sure she'd end up getting a few fans."
    scene sm1cs-cw003-54 sy-sure with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "Totally."
    scene sm1cs-cw003-55 sy-unsure with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "But how are you going to do that? This is your boss."
    scene sm1cs-cw003-56 mc-correcting with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "My boss' boss."
    scene sm1cs-cw003-57 sy-smiling with dissolve
    play voice3 stacy_yes_fine3 noloop
    sy "How are you going to ask your boss' boss if she wants to film porn?"
    scene sm1cs-cw003-58 mc-thinking with dissolve
    pause
    scene sm1cs-cw003-59 mc-shrugging with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I have no freaking clue."
    scene sm1cs-cw003-60 mc-worried with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "If I go up to her and she hates the idea, it won't just be a simple 'no' answer."
    mc "It could be a lot worse."
    scene sm1cs-cw003-61 sy-yeah with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "Yeah, you could get fired."
    scene sm1cs-cw003-62 mc-orrrr with dissolve
    play voice2 mc_angry_oof noloop
    mc "Or end up on one of those lists that show up when people are looking for a home."
    scene sm1cs-cw003-63 mc-depressed with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "I guess I'll just put the idea on the shelf for now."
    mc "And look for an opening."
    scene sm1cs-cw003-64 sy-sure with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Couldn't hurt."
    scene sm1cs-cw003-65 mc-nodding with dissolve
    pause
    play sound sfx_phone_buzz
    scene sm1cs-cw003-66 mc-looking-at-his-phone with dissolve
    pause
    scene sm1cs-cw003-67 mc-surprised with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Or she could text me and tell me that she wants to meet up and talk about her parents."
    scene sm1cs-cw003-68 sy-beware with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "Haha. Lucky dog."
    sy "Just be careful, it could be a trap."
    scene sm1cs-cw003-69 mc-nah with dissolve
    play voice2 mc_no_nah1 noloop
    mc "I'm sure it's not a trap."
    play sound sfx_cloth_rustling2
    scene sm1cs-cw003-70 mc-thinking with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Then again, this is probably the best point where I can tell Claire that I don't want to get involved."
    scene sm1cs-cw003-71 mc-thinking with dissolve
    mct "At least not any more involved than I already am."
    scene sm1cs-cw003-72 mc-talking with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "I should probably text her back. Later Stacy."
    scene sm1cs-cw003-73 sy-bye with dissolve
    play voice3 stacy_hey_byebye noloop
    sy "Bye."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    jump sm1cs_cw003_end
label sm1cs_cw003_end:
    $ StoryController.end_scene(CW_STORY, 0, 30, 0)
    return
label sm1cs_cw003_m01_c01:
    $ player.set_choice("sm1cs_cw003_joke")
    return