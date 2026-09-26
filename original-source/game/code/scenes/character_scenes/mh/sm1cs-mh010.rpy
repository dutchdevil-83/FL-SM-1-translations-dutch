label sm1cs_mh010:
    $ renpy.music.set_volume(0.8, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play sound sfx_door_open2
    scene sm1cs_mh010-00 mh_talk_neutral with dissolve
    play music music_midnight_blow
    play voice3 lissa_hey noloop
    mh "Oh, [mcname], what a pleasant surprise!"
    scene sm1cs_mh010-01 mc_talk with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Hey, Lyssa."
    scene sm1cs_mh010-02 mh_talk with dissolve
    play voice3 lissa_aga noloop
    mh "Please, come on in!"
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs_mh010-03 mc_talk_walkin with dissolve
    play voice3 lissa_thinking1 noloop
    mh "Sorry, I just got home."
    mh "And my feet are killing me."
    play voice2 mc_thinking_hmm1 noloop
    mc "Long day?"
    scene sm1cs_mh010-04 mh_talk_walk with dissolve
    play voice3 lissa_shyoh noloop
    mh "Oh... you have no idea..."
    play sound sfx_cloth_rustling4
    stop sound2 fadeout 1.0
    scene sm1cs_mh010-05 mh_talk_shoes with dissolve
    pause
    play sound2 sfx_shoes_off1 noloop
    scene sm1cs_mh010-06 mc_talk with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Want to talk about it?"
    scene sm1cs_mh010-07 mh_talk_kick with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "Mmmmm..."
    scene sm1cs_mh010-08 mh_talk_relax with dissolve
    play voice3 dahlia_no_simple noloop
    mh "Not really.{w} How was your day?"
    scene sm1cs_mh010-09 mc_talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh it was fine. Little bit of this, little bit of that..."
    play sound sfx_cloth_rustling3
    scene sm1cs_mh010-10 mh_talk_feet with dissolve
    play voice2 mc_happy_a1 noloop
    mc "But, I brought you a little something."
    scene sm1cs_mh010-11 mh_talk with dissolve
    play voice3 lissa_haha noloop
    mh "Is it ice cream? God, I could go for a little bit of ice cream."
    scene sm1cs_mh010-12 mc_talk with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Not exactly..."
    play sound sfx_cloth_rustling1
    scene sm1cs_mh010-13 mh_talk_mcusb with dissolve
    play voice3 lissa_thinking2 noloop volume 1.6
    mh "What have you got there?"
    scene sm1cs_mh010-14 mc_talk with dissolve
    play voice2 mc_thinking_hm noloop
    mc "This is our video from the other day."
    scene sm1cs_mh010-15 mh_talk with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oooo, you don't say."
    scene sm1cs_mh010-16 mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yep!"
    play sound sfx_cloth_rustling5
    scene sm1cs_mh010-17 mc_talk_pass with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "And as promised, that's the only copy of the footage, and video."
    scene sm1cs_mh010-18 mh_talk with dissolve
    play voice3 dahlia_thinking_hmm3 noloop volume 1.3
    mh "Hmmmm..."
    mh "You really gave me the only copy?"
    scene sm1cs_mh010-19 mc_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course, Lyssa. Not everyone wants to be on camera, and it would be super fucked-up of me to secretly keep a copy."
    play sound sfx_cloth_rustling4
    scene sm1cs_mh010-20 mc_talk_grabfeet with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I mean, that didn't stop Stacy from asking to see it six different times."
    scene sm1cs_mh010-21 mh_talk with dissolve
    play voice3 lissa_laugh noloop
    mh "Hehehehe - what'd you tell her?"
    scene sm1cs_mh010-22 mc_talk with dissolve
    if player.get_choice("sm1cs_mh008_convince_mh"):
        play voice2 mc_yes_yeah3 noloop
        mc "That I would ask you if she could see it."
        scene sm1cs_mh010-23 mh_talk with dissolve
        play voice3 lissa_mmm2 noloop
        mh "Mmmmm. I like that...{w} Maybe one day. When she's a good girl."
        scene sm1cs_mh010-24 mc_talk with dissolve
        play voice2 mc_happy_laugh2 noloop
        mc "Hahahaha - I will let her know that."
    else:
        play voice2 mc_no_nah2 noloop
        mc "Much to her annoyance, I told her no."
        scene sm1cs_mh010-25 mh_talk_massage with dissolve
        play voice3 dahlia_surprised_oh noloop
        mh "Oh really?"
        scene sm1cs_mh010-26 mc_talk_massage with dissolve
        play voice2 mc_disappointed_ehh2 noloop
        mc "Yeah, not looking forward to the cold shoulder I'm going home to."
        scene sm1cs_mh010-27 mh_talk_massage with dissolve
        play voice3 dahlia_happy_laugh2 noloop
        mh "Hahahahahaha."
    play sound2 sfx_cloth_wiping1
    scene sm1cs_mh010-29 mh_talk with dissolve
    play voice3 lissa_moan4 noloop
    mh "Oh God, [mcname], what are you doing?"
    scene sm1cs_mh010-28 mc_talk_smile with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Well, you said you had a long day and your feet were killing you."
    play voice2 mc_yes_yes1 noloop
    mc "Seemed like the only logical thing to do."
    scene sm1cs_mh010-32 mc_talk_rub_headback with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "God, that feels good..."
    scene sm1cs_mh010-33 mh_talk_rub_headback with dissolve
    play voice3 dahlia_happy_relief noloop
    mh "Mmmmmm..."
    mh "You're a good man, [mcname]."
    scene sm1cs_mh010-30 mc_talk with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "I do my best, Lyssa. That's what you deserve."
    scene sm1cs_mh010-31 mh_talk with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "I..."
    mh "I'm too tired for you to be this sweet, [mcname]."
    stop sound2 fadeout 1.0
    scene sm1cs_mh010-34 mc_talk_rub_headback_smile with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "Well, all right! I'll just go back to my sensual foot rubbing then."
    scene sm1cs_mh010-35 mh_talk_smile_closeup with dissolve
    play voice3 lissa_moan1 noloop
    mh "Yes, please..."
    play sound2 sfx_handjob_cream1
    scene sm1cs_mh010-26 mc_talk_massage with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "You know, I'm kind of like-"
    scene sm1cs_mh010-27 mh_talk_massage with dissolve
    play voice3 dahlia_no_serious noloop
    mh "Please, don't ruin this with a terrible joke, [mcname]."
    scene sm1cs_mh010-28 mc_talk_smile with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "All right, all right..."
    scene sm1cs_mh010-32 mc_talk_rub_headback with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "Lyssa and I have... we've really gotten closer."
    mct "After everything... it's really nothing short of amazing how we've bounced back."
    scene sm1cs_mh010-33 mh_talk_rub_headback with dissolve
    play voice3 lissa_moan3 noloop
    mct "She is really incredible... I mean... really, really incredible."
    mct "I still can't believe how lucky I got..."
    scene sm1cs_mh010-36 mh_talk with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "You know, I've been thinking about something."
    play voice2 mc_arrogant_hm1 noloop
    mc "Oh yeah? What's that."
    play sound2 sfx_cloth_rustling3 noloop
    scene sm1cs_mh010-37 mh_talk_situp with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "Mmmm... as much as I don't want the massage to stop..."
    mh "This deserves a face to face conversation."
    play voice2 mc_pain_mff1 noloop
    mct "Uh oh."
    scene sm1cs_mh010-38 mh_talk_look_laugh with dissolve
    play voice3 dahlia_happy_laugh1 noloop
    mh "Hahahaha - you don't have to worry, [mcname], it's nothing bad."
    scene sm1cs_mh010-39 mc_talk with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What, is it that obvious?"
    scene sm1cs_mh010-40 mh_talk with dissolve
    play voice3 dahlia_yes_yeah1 noloop
    mh "Oh yes, yes it is."
    play voice3 dahlia_happy_hmm1 noloop
    mh "If anything, this will probably make your day."
    scene sm1cs_mh010-41 mc_talk with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Oh yeah?"
    play sound sfx_cloth_rustling4
    scene sm1cs_mh010-42 mh_talk_knees with dissolve
    play voice3 lissa_aga noloop
    mh "Mmhmmm...{w} I've been thinking a lot about the video we made..."
    scene sm1cs_mh010-45 mc_talk_surprised with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Really?"
    scene sm1cs_mh010-46 mh_talk_mmm with dissolve
    play voice3 lissa_mmm3 noloop
    mh "Mmmhmmm..."
    scene sm1cs_mh010-47 mc_talk with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "What about it?"
    scene sm1cs_mh010-48 mh_talk_seductive with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "Well... I've been thinking... it was pretty hot."
    scene sm1cs_mh010-49 mc_talk with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "I mean, I think every time we have sex is pretty hot."
    scene sm1cs_mh010-50 mh_talk with dissolve
    play voice3 lissa_yes noloop
    mh "Yes, you're right, but..."
    play sound sfx_cloth_rustling2
    scene sm1cs_mh010-51 mh_talk_finger with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "Recording it kind of made it hotter."
    scene sm1cs_mh010-52 mc_talk with dissolve
    play voice2 mc_surprised_what3 noloop
    mc "Really?"
    scene sm1cs_mh010-53 mh_talk_finger with dissolve
    play voice3 dahlia_yes_yeah4 noloop
    mh "Yes. I've... I've thought about it more than once while I've been home, alone... {w}Me being that young nursing student, wild and carefree."
    scene sm1cs_mh010-54 mc_talk with dissolve
    play voice2 mc_surprised_wow1 noloop
    mct "Wow... this is insane. She was so adamantly against this before..."
    mc "Uhm... okay?"
    scene sm1cs_mh010-55 mh_talk with dissolve
    play voice3 dahlia_yes_questioning noloop
    mh "What is it, [mcname]?"
    scene sm1cs_mh010-56 mc_talk with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I'm just... kind of surprised is all."
    mc "When we talked about the porn studio, and everything else, you just seemed so opposed to it."
    mc "So...{w} What changed, Lyssa?"
    play sound sfx_cloth_rustling1
    scene sm1cs_mh010-57 mh_talk_sitback with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "I...{w} I got to feel free for a moment, do something just for {i}me{/i}."
    mh "That was...{w} that was the appeal of Fetish Locator to me."
    mh "Every day, I am expected to be some version of myself."
    scene sm1cs_mh010-58 mh_talk_look_floor with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "I need to be the best lawyer, I need to present as a woman, I need to keep everything together."
    mh "There are so many people who want to see me fail. Because I'm good at my job, because I... I'm a woman."
    mh "And every day, I need to keep up that facade."
    scene sm1cs_mh010-59 mh_talk_sadsmile with dissolve
    play voice3 lissa_moan5 noloop
    mh "But, making that video with you [mcname]... I got to be that wild, carefree person that I so desperately want to be."
    mh "And it was fun, and it was with someone I care deeply for, that I might even-"
    scene sm1cs_mh010-60 mh_talk_covermouth with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "Oh.{w} I promised myself that the feelings I have would be shared with you, but this isn't that moment."
    mct "Was Lyssa about to-"
    play sound sfx_cloth_rustling2
    scene sm1cs_mh010-61 mh_talk_handleg with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "But I trust you, [mcname]. I trust you so much."
    mh "Since we reconnected, you promised me maximum effort."
    mh "And I've gotten it."
    scene sm1cs_mh010-62 mh_talk_closer with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "The video woke something up in me, something that first stirred during Fetish Locator.{w} Something I've been looking to find again."
    mh "And it's something I want to explore with you. I want to see where it goes, where it takes us."
    mh "So, if you'll have me, I'd love to make some more movies with you."
    scene sm1cs_mh010-63 mc_talk_smile with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "Lyssa, I don't know what to say..."
    scene sm1cs_mh010-64 mh_talk with dissolve
    play voice3 dahlia_no_simple noloop
    mh "Then don't say anything."
    play sound sfx_skirt_off2
    scene sm1cs_mh010-65 mh_talk_standup with dissolve
    play voice3 dahlia_happy_phew noloop
    mh "I'm exhausted, why don't we just cuddle up tonight, and you sleep on everything I just told you."
    menu:
        "Spend the night at Lyssa's":
            $ player.set_choice("sm1cs_mh010_spend_night")
            scene sm1cs_mh010-66 mc_talk_takesout with dissolve
            play voice2 mc_yes_okay2 noloop
            mc "That sounds good to me."
            scene sm1cs_mh010-67 mh_talk with dissolve
            play voice3 dahlia_happy_hmm1 noloop
            mh "I was hoping you'd say that."
            play sound sfx_cloth_rustling4
            scene sm1cs_mh010-68 mc_talk_armsaround with dissolve
            play voice2 mc_happy_a1 noloop
            mc "Has anyone told you that you're amazing?"
            scene sm1cs_mh010-69 mh_talk with dissolve
            play voice3 lissa_laugh noloop
            mh "Once or twice, but a girl likes to hear it every once in awhile."
            scene sm1cs_mh010-70 mc_talk with dissolve
            play voice2 mc_disappointed_ah2 noloop
            mc "You're amazing, Lyssa."
            play sound sfx_cloth_rustling3
            scene sm1cs_mh010-71 mh_talk_smile with dissolve
            pause
            scene sm1cs_mh010-72 mh_talk_kiss with dissolve
            play voice3 lissa_mmm2 noloop
            play voice2 mc_thinking_mmm2 noloop
            play sound dahlia_kiss_french1
            pause
            scene sm1cs_mh010-73 mh_talk_kiss with dissolve
            queue sound mc_kiss1
            pause
            play sound sfx_heels_steps1 loop
            play sound2 sfx_heels_steps2
            scene sm1cs_mh010-74 mh_talk_walktobed with dissolve
            play voice3 lissa_haha2 noloop
            mh "Now, troublemaker, let's crawl into bed."
            scene sm1cs_mh010-75 mc_talk_walktobed with dissolve
            play voice2 mc_arrogant_huh1 noloop
            mc "You don't have to tell me twice!"
            scene sm1cs_mh010-76 mc_talk_walktobed with fade
            pause
            play sound sfx_cloth_rustling4
            play sound2 sfx_skirt_off1 noloop
            scene sm1cs_mh010-77 mh_talk_cuddlinglightsoff with dissolve
            play voice3 lissa_moan2 noloop
            mh "Mmmmm..."
            mh "It is nice sharing a bed with you, [mcname]."
            scene sm1cs_mh010-78 mc_talk_cuddlinglightsoff with dissolve
            play voice2 mc_yes_yes2 noloop
            mc "I feel the same way."
            play sound sfx_skirt_off1
            scene sm1cs_mh010-79 mh_talk_cuddlinglightsoff with dissolve
            play voice3 dahlia_yes_yeah2 noloop
            mh "As you should. Good night, lover boy."
            scene sm1cs_mh010-80 mc_talk_cuddlinglightsoff with dissolve
            play voice2 mc_yes_aga2 noloop
            mc "Good night, Lyssa."
            scene sm1cs_mh010-81 mc_talk_eyesclosed with dissolve
            pause
            jump sm1cs_mh010_spend_the_night_exit
        "Leave Lyssa's house":
            scene sm1cs_mh010-82 mc_talk_menu_thingstodo_sad with dissolve
            play voice2 mc_disappointed_ah2 noloop
            mc "God, I would love to, Lyssa, but I still have things I need to do tonight."
            scene sm1cs_mh010-83 mh_talk_menu_thingstodo_sad with dissolve
            play voice3 dahlia_disappointed_ehh1 noloop
            mh "Shame."
            play sound sfx_cloth_rustling2
            scene sm1cs_mh010-84 mc_talk_menu_thingstodo_stand with dissolve
            play voice2 mc_thinking_mmm6 noloop
            mc "But I will definitely be taking you up on that offer."
            play voice3 dahlia_yes_questioning noloop
            mh "Promise?"
            play voice2 mc_yes_yes5 noloop
            mc "I swear on my life, I will."
            mh "Good."
            play sound sfx_heels_steps1 loop
            play sound2 sfx_heels_steps2
            scene sm1cs_mh010-87 mh_talk_menu_thingstodo with dissolve
            play voice3 lissa_haha2 noloop
            mh "Well then you better skedaddle, before I start using my feminine wiles to convince you to stay."
            scene sm1cs_mh010-86 mc_talk_menu_thingstodo_smirk with dissolve
            play voice2 mc_arrogant_heh2 noloop volume 1.5
            mc "Maybe I can sit here just a little longer, see what wiles you've got up your sleeve."
            stop sound fadeout 1.0
            stop sound2 fadeout 1.0
            scene sm1cs_mh010-89 mh_talk_menu_thingstodo with dissolve
            play voice3 lissa_laugh2 noloop
            mh "Hehehe, go you rapscallion. You know where to find me."
            scene sm1cs_mh010-88 mc_talk_menu_thingstodo with dissolve
            play voice2 mc_hey_bye2 noloop
            mc "Good night, Lyssa."
            play sound sfx_heels_steps1 loop
            scene sm1cs_mh010-90 mc_talk_menu_thingstodo_walkout with dissolve
            play voice3 dahlia_yes_yeah2 noloop
            mh "Good night, [mcname]."
            play sound sfx_door_openclosed1
            jump sm1cs_mh010_exit
label sm1cs_mh010_spend_the_night_exit:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    if vn_mode:
        $ StoryController.end_scene(MH_STORY)
        return
    $ gt.add((6 + (24 - gt.curr_hour)), 0, 0)
    $ player.sleep_common_function()
    $ player.progress_storyline(MH_STORY)
    return
label sm1cs_mh010_exit:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(MH_STORY, 2, 0, 2)
    return