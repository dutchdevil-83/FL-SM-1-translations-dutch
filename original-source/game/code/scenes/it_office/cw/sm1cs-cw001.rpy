label sm1cs_cw001:
    $ renpy.music.set_volume(0.8, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.5, "sound4" )
    play sound4 sfx_office_ambience1 fadein 2.0 volume 0.6
    play sound sfx_heels_steps2 loop
    scene cs-cw001-01-mc-cw with dissolve
    play music music_binary_work
    pause
    stop sound fadeout 1.0
    scene cs-cw001-02-mc-talk-cw with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hi Ms. Watts. I've got some time for that meeting if you're free."
    scene cs-cw001-03-cw-talk-mc with dissolve
    play voice3 girl29_yes_aga2 noloop
    cw "Of course."
    play sound sfx_chair_slide1
    scene cs-cw001-04-cw-talk-mc with dissolve
    play sound2 sfx_heels_steps1
    play voice3 girl29_thinking_hmm3 noloop
    cw "Let's go to the conference room. Better for this."
    scene cs-cw001-05-mc-inner-talk with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "What does she mean by 'this'?"
    play sound sfx_heels_steps2 loop
    scene cs-cw001-06-mc-cw with dissolve
    pause
    play sound sfx_door_openclosed1
    stop sound2 fadeout 1.0
    scene cs-cw001-07-mc-cw with dissolve
    pause
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene cs-cw001-08-cw-talk-mc with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "I appreciate you finding room in your schedule so quickly, [mcname]."
    cw "I thought I might have to hunt you down and drag you into this."
    menu:
        "Be bold"(hint="sm1cs_cw001_m01_h01"):
            call sm1cs_cw001_m01_c01 from _call_sm1cs_cw001_m01_c01
            scene cs-cw001-09-c1-mc-talk-cw with dissolve
            play voice2 d4s4_mclaugh noloop volume 1.5
            mc "Haha. Next time I'll be sure to make you work for it, Ms. Watts."
            scene cs-cw001-10-c1-cw-talk-mc with dissolve
            play voice3 girl29_thinking_oh noloop
            cw "Oh, will you now?"
        "Be submissive"(hint="sm1cs_cw001_m01_h02"):
            call sm1cs_cw001_m01_c02 from _call_sm1cs_cw001_m01_c02
            scene cs-cw001-11-c2-mc-talk-cw with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "I'm sorry if you were waiting on me, Ms. Watts."
            mc "I'm trying really hard to keep up with Nari and April on my work."
            scene cs-cw001-12-c2-cw-talk-mc with dissolve
            play voice3 girl29_thinking_oh noloop
            cw "Don't worry about it. And I'm glad to hear you've been keeping your nose to the grindstone."
        "Be a dork"(hint="sm1cs_cw001_m01_h03"):
            call sm1cs_cw001_m01_c03 from _call_sm1cs_cw001_m01_c03
            scene cs-cw001-13-c3-mc-talk-cw with dissolve
            play voice2 mc_yes_yeah7 noloop
            mc "You like hunting? Sounds like your D and D class would be a Ranger."
            scene cs-cw001-14-c3-cw-talk-mc with dissolve
            play voice3 girl29_surprised_what noloop
            cw "A what?"
            scene cs-cw001-15-c3-mc-talk-cw with dissolve
            play voice2 d2s12_emmm noloop
            mc "I uh.. never mind."
    scene cs-cw001-16-mc-talk-cw with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "How can I help you?"
    scene cs-cw001-17-cw-talk-mc with dissolve
    play voice3 girl29_thinking_hmm5 noloop
    cw "I appreciate that this may be an uncomfortable topic to discuss with your superior, but I have noticed a developing situation."
    cw "And this particular situation requires my input as the C.U.M Division Manager."
label sm1cs_cw001_am_convo:
    if not player.has_played_scene("sm1cs_am005"):
        jump sm1cs_cw001_ns_convo
    play sound sfx_cloth_rustling1
    scene cs-cw001-18-cw-talk-mc with dissolve
    play voice3 girl29_pain_cough1 noloop
    cw "*clears throat* I've noticed that you and April seemed to have quite a heated conversation at work recently."
    cw "You need to know that Orbix takes harassment between its employees very seriously."
    scene cs-cw001-19-mc-talk-cw with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait. Now I can-"
    scene cs-cw001-20-cw-talk-mc with dissolve
    play voice3 girl29_angry_hm noloop
    cw "I'm not finished. Naturally, this is a high-functioning workplace, and our duties demand a lot from us."
    scene cs-cw001-21-cw-talk-mc with dissolve
    play voice3 girl29_disgust_meh noloop
    cw "I understand how these things can happen."
    cw "But if April is harassing you, then you need to tell me."
    scene cs-cw001-22-mc-talk-cw with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene cs-cw001-23-cw-talk-mc with dissolve
    play voice3 girl29_thinking_mmm2 noloop
    cw "I'm a sharp observer, [mcname], especially when it comes to new employees."
    cw "Trust me, you can let it all out, [mcname]. Please, you're safe here with me."
    jump sm1cs_cw001_menu_am
label sm1cs_cw001_menu_am:
    menu:
        "You must be joking"(hint="sm1cs_cw001_m02_h01"):
            call sm1cs_cw001_m02_c01 from _call_sm1cs_cw001_m02_c01
            scene cs-cw001-24-c1-mc-talk-cw with dissolve
            play voice2 mc_surprised_uh3 noloop
            mc "You have to be joking around, right?"
            scene cs-cw001-25-c1-cw-talk-mc with dissolve
            play voice3 girl29_arrogant_huh noloop
            cw "Do I look like I'm joking?"
            cw "I need to know if the situation merits the involvement of HR, [mcname]."
            scene cs-cw001-26-c1-cw-talk-mc with dissolve
            play voice3 girl29_disappointed_mff noloop
            cw "It's very important that any liabilities for Orbix are covered. If an issue isn't properly reported, that can lead to damage for the company."
            cw "And dismissals."
            scene cs-cw001-27-c1-mc-talk-cw with dissolve
            play voice2 mc_yes_okay2 noloop
            mc "I can tell you with one-hundred percent honesty that there is nothing to report."
            mc "HR doesn't need to protect me from April because April didn't harass me or anything."
            scene cs-cw001-28-c1-mc-inner-talk with dissolve
            play voice2 mc_thinking_mmm6 noloop
            mct "Well, that's not entirely true, but better not to talk about that."
            scene cs-cw001-27-c1-mc-talk-cw with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.7
            mc "The truth is... April and I are actually going on a date together. That's what our last conversation was about."
            jump sm1cs_cw001_continue_am
        "Tell her the truth"(hint="sm1cs_cw001_m02_h02"):
            call sm1cs_cw001_m02_c02 from _call_sm1cs_cw001_m02_c02
            scene cs-cw001-29-c2-mc-talk-cw with dissolve
            play voice2 d1s5b_ehhh noloop volume 1.7
            mc "The simple fact of the matter is that April and I are... kind of dating."
            mc "Well, not dating. We're going to try going out on a date and seeing where that takes us."
            jump sm1cs_cw001_continue_am
        "Question Claire"(hint="sm1cs_cw001_m02_h03") if not player.get_choice("sm1cs_cw001_question_cw"):
            call sm1cs_cw001_m02_c03 from _call_sm1cs_cw001_m02_c03
            scene cs-cw001-30-c3-mc-talk-cw with dissolve
            play voice2 mc_thinking_wait3 noloop
            mc "Wait, what makes you think that April is harassing me?"
            scene cs-cw001-31-c3-cw-talk-mc with dissolve
            play voice3 girl29_surprised_ehh noloop
            cw "I keep a close watch over the people in my division."
            scene cs-cw001-32-c3-cw-talk-mc with dissolve
            play voice3 girl29_thinking_hmm4 noloop
            cw "Recently I noticed the two of you having a very animated conversation that didn't seem to pertain to work at all."
            cw "I've known April a while now. She rarely has a problem figuring out how to push other people's buttons."
            scene cs-cw001-33-c3-mc-talk-cw with dissolve
            play voice2 mc_thinking_hmm1 noloop
            mc "So you were watching us."
            scene cs-cw001-34-c3-cw-talk-mc with dissolve
            play voice3 girl29_yes_serious noloop
            cw "A good manager knows everything that's going on under her purview."
            scene cs-cw001-35-c3-mc-inner-talk with dissolve
            play voice2 d1s1_mmm noloop volume 1.5
            mct "Sounds like I should be a little more careful going forward. If Claire realizes I'm here for more than just a job, that could mean trouble for me."
            jump sm1cs_cw001_menu_am
label sm1cs_cw001_continue_am:
    scene cs-cw001-36-cw-talk-mc with dissolve
    play voice3 girl29_happy_laugh3 noloop
    cw "Really? And April is aware of this planned 'date'?"
    scene cs-cw001-37-mc-talk-cw with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Oh yeah. She kind of... initiated it, in her own... 'special way' of course."
    scene cs-cw001-38-cw-talk-mc with dissolve
    play voice3 girl29_thinking_mmm1 noloop
    cw "I see. That's definitely not what I expected to hear."
    cw "But it's certainly better if April was harassing you."
    scene cs-cw001-39-cw-talk-mc with dissolve
    play voice3 girl29_arrogant_he noloop
    cw "I assume that this is just starting and it's not exclusive or anything."
    scene cs-cw001-40-mc-talk-cw with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. Uh, I mean, we didn't discuss anything like that."
    scene cs-cw001-41-cw-talk-mc with dissolve
    play voice3 girl29_disappointed_oh noloop
    cw "Oh. How very modern of you both."
    jump sm1cs_cw001_ns_convo
label sm1cs_cw001_ns_convo:
    if player.has_played_scene("sm1cs_ns004"):
        jump sm1cs_cw001_end_convo
    scene cs-cw001-42-cw-talk-mc with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "It's not in my nature to pry, but recently, I was visiting the bathroom and I heard things."
    cw "Sounds that should not be heard in an office bathroom."
    scene cs-cw001-43-cw-talk-mc with dissolve
    play voice3 girl29_arrogant_ha noloop
    cw "Now I'm not going to accuse you, or Ms. Song of anything. We've all been young and..."
    cw "Excitable."
    scene cs-cw001-47-c2-cw-talk-mc with dissolve
    play voice3 girl29_thinking_hmm2 noloop
    cw "But this is a place of business, and certain acts have no place on the premises."
    menu:
        "Promise to not do anything else at the office"(hint="sm1cs_cw001_m03_h01"):
            call sm1cs_cw001_m03_c01 from _call_sm1cs_cw001_m03_c01
            scene cs-cw001-44-c1-mc-talk-cw with dissolve
            play voice2 mc_yes_sure1 noloop
            mc "Of course. That makes sense."
            mc "I promise to never do anything... like {i}that{/i}, in the office, again."
            scene cs-cw001-45-c1-cw-talk-mc with dissolve
            play voice3 girl29_yes_aga1 noloop
            cw "Good. And I'm sure you'll convey that to Ms. Song as well."
            scene cs-cw001-46-c2-mc-talk-cw with dissolve
            play voice2 mc_yes_yeah2 noloop
            mc "Of course."
            jump sm1cs_cw001_ns_convo_continue
        "Deny deny deny"(hint="sm1cs_cw001_m03_h02"):
            call sm1cs_cw001_m03_c02 from _call_sm1cs_cw001_m03_c02
            scene cs-cw001-49-c2-mc-talk-cw with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "Ms. Watts, I'm going to be honest with you."
            mc "I have absolutely no idea what you're talking about."
            scene cs-cw001-48-c2-cw-talk-mc with dissolve
            play voice3 girl29_angry_argh1 noloop
            cw "Of course not."
            cw "But if it's all the same to you, I'd just remind you that no one should be having sex on Orbix premises."
            scene cs-cw001-50-c2-cw-talk-mc with dissolve
            play voice3 girl29_angry_hmf noloop
            cw "This is a place of business, and any... repeated situations could lead to disciplinary actions."
            cw "Or worse."
            scene cs-cw001-48-c2-cw-talk-mc with dissolve
            play voice3 girl29_arrogant_yeah noloop
            cw "You'll be sure to keep an eye out for such troublemakers. Right [mcname]?"
            scene cs-cw001-52-mc-talk-cw with dissolve
            play voice2 d1s5b_emmm noloop volume 1.7
            mc "C-can."
            mc "Can do, Ms. Watts."
            scene cs-cw001-53-cw-talk-mc with dissolve
            play voice3 girl29_happy_laugh5 noloop
            cw "Excellent. I knew I could count on you."
            jump sm1cs_cw001_end_convo
label sm1cs_cw001_ns_convo_continue:
    scene cs-cw001-51-cw-talk-mc with dissolve
    play voice3 girl29_happy_relief noloop
    cw "I trust that the two of you will make sure to bring your relationship to Maureen at HR, once it becomes something 'official'."
    cw "I'm all for young love, but all of us need to make sure that Orbix is covered in case of... whatever situations might arise."
    scene cs-cw001-52-mc-talk-cw with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Totally. Yeah, I'm sure we'll bring it to HR if things continue the way they're going."
    scene cs-cw001-53-cw-talk-mc with dissolve
    play voice3 girl29_yes_aga3 noloop
    cw "Excellent."
    jump sm1cs_cw001_end_convo
label sm1cs_cw001_end_convo:
    play sound sfx_phone_buzz
    scene cs-cw001-54-cw-phone with dissolve
    pause
    scene cs-cw001-55-cw-talk with dissolve
    play voice3 girl29_thinking_hmm1 noloop
    cw "Hmmm."
    scene cs-cw001-56-cw-talk-mc with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "I apologize for going 'nosy boss' on you about this, [mcname]. Definitely not my favorite part of the job."
    menu:
        "What is your favorite part?"(hint="sm1cs_cw001_m04_h01"):
            scene cs-cw001-57-c1-mc-talk-cw with dissolve
            play voice2 d1s5_mchappy noloop volume 1.5
            mc "So what is your favorite part of the job, Claire?"
            scene cs-cw001-58-c1-cw-talk-mc with dissolve
            play voice3 girl29_thinking_hmm4 noloop
            cw "Mmm. Perhaps I'll tell you once we know each other a little better."
        "I get the feeling there was trouble in the past"(hint="sm1cs_cw001_m04_h02"):
            call sm1cs_cw001_m04_c02 from _call_sm1cs_cw001_m04_c02
            scene cs-cw001-59-c2-mc-talk-cw with dissolve
            play voice2 d1s2_hmm noloop volume 1.8
            mc "Did Orbix had some trouble with inter-office relationships in the past."
            scene cs-cw001-60-c2-cw-talk-mc with dissolve
            play voice3 girl29_yes_yep noloop
            cw "Very perceptive, [mcname]."
            scene cs-cw001-61-c2-mc-talk-cw with dissolve
            play voice2 mc_surprised_uh1 noloop
            mc "Did {i}you{/i} get in big trouble when people found out?"
            scene cs-cw001-62-c2-cw-talk-mc with dissolve
            play voice3 girl29_arrogant_ha noloop
            cw "Hah. You think that I was involved in some kind of scandal?"
            cw "Shame on you, [mcname]."
            scene cs-cw001-63-c2-mc-talk-cw with dissolve
            play voice2 mc_thinking_mmm3 noloop
            mc "Sorry, Ms. Watts."
            scene cs-cw001-60-c2-cw-talk-mc with dissolve
            play voice3 girl29_no_nah noloop
            cw "It's fine, but to think you imagined I would get into some trouble at work..."
            cw "You should be careful with such stray thoughts."
            play sound sfx_cloth_rustling2
            scene cs-cw001-61-c2-mc-talk-cw with dissolve
            play voice2 mc_yes_okay1 noloop
            mc "Of course."
            scene cs-cw001-64-c2-mc-inner-talk with dissolve
            play voice2 d1s5_mcthinks noloop
            mct "The way she is talking isn't really matching how she's looking at me."
            mct "I think she liked me thinking she was doing something in the office."
    scene cs-cw001-65-cw-talk-mc with dissolve
    play voice3 girl29_arrogant_hm noloop
    cw "Ahem. I'm very glad we had a chance to chat, [mcname]."
    if player.get_choice("sm1cs_cw001_deny"):
        scene cs-cw001-66-c1-cw-talk-mc with dissolve
        play voice3 girl29_thinking_hmm5 noloop
        cw "And you're sure there is nothing else you want to get off your chest?"
        scene cs-cw001-67-c1-mc-talk-cw with dissolve
        play voice2 mc_no_nope1 noloop
        mc "Nope. Can't think of anything."
    else:
        scene cs-cw001-68-c2-cw-talk-mc with dissolve
        play voice3 girl29_thinking_hmm5 noloop
        cw "And I'm double glad I didn't go with my first thought."
        scene cs-cw001-69-c2-mc-talk-cw with dissolve
        play voice2 mc_surprised_huh7 noloop
        mc "What was that?"
        scene cs-cw001-70-c2-cw-talk-mc with dissolve
        play voice3 girl29_disappointed_oh noloop
        cw "Oh just reporting the situation straight to Maureen at HR."
        cw "Who knows what would have happened then."
        scene cs-cw001-71-c2-mc-talk-cw with dissolve
        play voice2 mc_yes_yeah1 noloop
        mc "Yeah. Well, I appreciate you asking me."
        mc "And I'll brush up on my HR handbook. Probably a good move."
        scene cs-cw001-68-c2-cw-talk-mc with dissolve
        play voice3 girl29_no_simple noloop
        cw "You don't need to do that, [mcname]."
    scene cs-cw001-72-cw-talk-mc with dissolve
    play voice3 girl29_thinking_mmm1 noloop
    cw "If you're ever curious about something, you can come and have a little chat with me."
    cw "I can make sure you stay on the straight and narrow path."
    scene cs-cw001-73-mc-talk-cw with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "That sounds nice, Claire. But I don't want to be a nuisance."
    scene cs-cw001-74-cw-talk-mc with dissolve
    play voice3 girl29_no_uhuh noloop
    cw "Ms. Watts."
    play sound sfx_heels_steps1 loop
    scene cs-cw001-75-mc-talk-cw with dissolve
    play voice2 d3s7_mcemm noloop volume 1.4
    mc "*nervously* Right, sorry. Ms. Watts."
    scene cs-cw001-76-cw-talk-mc with dissolve
    play voice3 girl29_yes_yeah noloop
    cw "It won't be any trouble to me, [mcname]. Over the years working here, I've gotten very skilled at managing my work and play balance."
    cw "With my advice, you'll do the same in no time."
    $ renpy.music.set_volume(1.0, 3.0, "sound4" )
    stop sound fadeout 1.0
    menu:
        "Agree with Claire"(hint="sm1cs_cw001_m05_h01"):
            call sm1cs_cw001_m05_c01 from _call_sm1cs_cw001_m05_c01
            scene cs-cw001-77-c1-mc-talk-cw with dissolve
            play voice2 mc_yes_yes1 noloop
            mc "Of course. I'll take any help I can get, Ms. Watts."
            scene cs-cw001-78-c1-cw-talk-mc with dissolve
            play voice3 girl29_thinking_hmm3 noloop
            cw "I knew you'd see it my way."
            play sound sfx_heels_steps1
            scene cs-cw001-79-c1-cw with dissolve
            pause
        "Disagree with Claire"(hint="sm1cs_cw001_m05_h02"):
            call sm1cs_cw001_m05_c02 from _call_sm1cs_cw001_m05_c02
            scene cs-cw001-80-c2-mc-talk-cw with dissolve
            play voice2 mc_arrogant_hm1 noloop
            mc "I think about it, but I'm usually pretty good at standing out of trouble."
            scene cs-cw001-81-c2-cw-talk-mc with dissolve
            play voice3 girl29_disappointed_eh noloop
            cw "Did you really think I'd believe that?"
            scene cs-cw001-82-c2-cw-talk-mc with dissolve
            play voice3 girl29_hey_bye2 noloop
            cw "That will be all, Mr. Young."
            cw "You can go."
            scene cs-cw001-83-c2-mc-talk-cw with dissolve
            play voice2 mc_yes_sure1 noloop
            mc "Sure."
            play sound sfx_heels_steps2
            scene cs-cw001-84-c2-cw with dissolve
            pause
    jump sm1cs_cw001_end
label sm1cs_cw001_end:
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    stop sound fadeout 1.0
    stop music fadeout 3.0
    stop sound4 fadeout 2.0
    $ StoryController.end_scene(CW_STORY, 1, 30, 2)
    return
label sm1cs_cw001_m01_c01:
    $ player.set_choice("sm1cs_cw001_be_bold")
    $ CharacterController.get_character("cw").add_point()
    return
label sm1cs_cw001_m01_c02:
    $ player.set_choice("sm1cs_cw001_be_submissive")
    $ CharacterController.get_character("cw").add_point()
    return
label sm1cs_cw001_m01_c03:
    $ player.set_choice("sm1cs_cw001_be_dork")
    $ CharacterController.get_character("cw").deduct_point()
    return
label sm1cs_cw001_m02_c01:
    $ player.set_choice("sm1cs_cw001_cw_joking")
    $ CharacterController.get_character("cw").deduct_point()
    return
label sm1cs_cw001_m02_c02:
    $ player.set_choice("sm1cs_cw001_tell_truth")
    return
label sm1cs_cw001_m02_c03:
    $ player.set_choice("sm1cs_cw001_question_cw")
    return
label sm1cs_cw001_m03_c01:
    $ player.set_choice("sm1cs_cw001_promise")
    return
label sm1cs_cw001_m03_c02:
    $ player.set_choice("sm1cs_cw001_deny")
    return
label sm1cs_cw001_m04_c02:
    $ player.set_choice("sm1cs_cw001_cw_past_trouble")
    return
label sm1cs_cw001_m05_c01:
    $ player.set_choice("sm1cs_cw001_agree_with_cw")
    $ CharacterController.get_character("cw").add_point()
    return
label sm1cs_cw001_m05_c02:
    $ player.set_choice("sm1cs_cw001_disagree_with_cw")
    $ CharacterController.get_character("cw").deduct_point()
    return