image sm1cs_am007-a52-glambot = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a52-3x-60fps.webm", start_image = "sm1cs-am007-a52 mc-am-park-glambot-00", image = "sm1cs-am007-a52 mc-am-park-glambot-99", loop = False)
image sm1cs_am007-a115-1 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a115-1-2x-50fps.webm", start_image = "sm1cs-am007-a115-1 mc-am-lick-anim-01")
image sm1cs_am007-a115-1-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a115-1-2x-60fps.webm", start_image = "sm1cs-am007-a115-1 mc-am-lick-anim-01")
image sm1cs_am007-a115-2 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a115-2-2x-50fps.webm", start_image = "sm1cs-am007-a115-2 mc-am-lick-anim-01")
image sm1cs_am007-a115-2-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a115-2-2x-60fps.webm", start_image = "sm1cs-am007-a115-2 mc-am-lick-anim-01")
image sm1cs_am007-a115-3 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a115-3-2x-50fps.webm", start_image = "sm1cs-am007-a115-3 mc-am-lick-anim-01")
image sm1cs_am007-a115-3-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a115-3-2x-60fps.webm", start_image = "sm1cs-am007-a115-3 mc-am-lick-anim-01")
image sm1cs_am007-a130-1 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a130-1-2x-50fps.webm", start_image = "sm1cs-am007-a130-1 mc-am-titjob-anim-01")
image sm1cs_am007-a130-1-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a130-1-2x-60fps.webm", start_image = "sm1cs-am007-a130-1 mc-am-titjob-anim-01")
image sm1cs_am007-a130-2 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a130-2-2x-50fps.webm", start_image = "sm1cs-am007-a130-2 mc-am-titjob-anim-01")
image sm1cs_am007-a130-2-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a130-2-2x-60fps.webm", start_image = "sm1cs-am007-a130-2 mc-am-titjob-anim-01")
image sm1cs_am007-a130-3 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a130-3-2x-50fps.webm", start_image = "sm1cs-am007-a130-3 mc-am-titjob-anim-01")
image sm1cs_am007-a130-3-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a130-3-2x-60fps.webm", start_image = "sm1cs-am007-a130-3 mc-am-titjob-anim-01")
image sm1cs_am007-a146-1 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a146-1-2x-50fps.webm", start_image = "sm1cs-am007-a146-1 mc-am-standing-behind-anim-01")
image sm1cs_am007-a146-1-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a146-1-2x-60fps.webm", start_image = "sm1cs-am007-a146-1 mc-am-standing-behind-anim-01")
image sm1cs_am007-a146-2 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a146-2-2x-50fps.webm", start_image = "sm1cs-am007-a146-2 mc-am-standing-behind-anim-01")
image sm1cs_am007-a146-2-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a146-2-2x-60fps.webm", start_image = "sm1cs-am007-a146-2 mc-am-standing-behind-anim-01")
image sm1cs_am007-a146-3 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a146-3-2x-50fps.webm", start_image = "sm1cs-am007-a146-3 mc-am-standing-behind-anim-01")
image sm1cs_am007-a146-3-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a146-3-2x-60fps.webm", start_image = "sm1cs-am007-a146-3 mc-am-standing-behind-anim-01")
image sm1cs_am007-a146-4 = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a146-4-2x-50fps.webm", start_image = "sm1cs-am007-a146-4 mc-am-standing-behind-anim-01")
image sm1cs_am007-a146-4-f = Movie(play = "images/FS_IT/AM/s007/anim/sm1cs-am007-a146-4-2x-60fps.webm", start_image = "sm1cs-am007-a146-4 mc-am-standing-behind-anim-01")
label sm1cs_am007:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music music_averageday_it
    play sound4 sfx_office_ambience1 fadein 1.0
    scene sm1cs-am007-01 mc-am-start1_c1 with dissolve
    play voice3 girl22_hey_attention noloop
    am "Hey, [mcname]."
    am "I've been meaning to talk to you."
    play sound sfx_phone_buzz
    scene sm1cs-am007-03 mc-am-phone_c1 with dissolve
    "Buzz. Buzz."
    play voice3 girl22_arrogant_pff noloop
    am "Shit, I gotta take this."
    play sound sfx_heels_steps1
    scene sm1cs-am007-04 mc-am-walk_c2 with dissolve
    play voice2 d1s5_mcthinks noloop
    mct "I wonder what the call is about.{w} Seemed important.."
    play sound sfx_chair_slide1
    scene sm1cs-am007-05 mc-am-sit_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Shit.{w} I remember Anna asking me about this earlier."
    mct "She wanted to know if April was taking up company time with personal calls..."
    scene sm1cs-am007-05 mc-am-sit_c2 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "I hope Anna or Claire don't realize what April is doing."
    $ renpy.music.set_volume(0.0, 1.0, "sound4" )
    scene black
    show screen scene_transistion(_("Five minutes later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 2.0, "sound4" )
    scene sm1cs-am007-06 mc-am-stand_c1
    with Fade(0.5, 0.5, 0.5)
    play sound sfx_cloth_rustling3
    play voice2 d14s16_smell noloop
    mct "I wonder what is keeping April?"
    scene sm1cs-am007-07 mc-am-look_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "I didn't see her leave the office.{w} She must still be in here somewhere."
    scene sm1cs-am007-07 mc-am-look_c3 with dissolve
    pause
    scene sm1cs-am007-07 mc-am-look_c2 with dissolve
    play voice3 girl22_disappointed_geh noloop
    am "Pepper... I {b}really{/b} don't have time for this."
    am "I never said I could make it."
    play sound2 sfx_heels_steps2
    scene sm1cs-am007-08 mc-am-look2_c1 with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "You know how busy I am with work."
    scene sm1cs-am007-09 mc-am-phone_c1 with dissolve
    play voice4 sfx_phone_talk_female1 noloop volume 0.7
    ps "Listen, we get it, April."
    ps "But if we're ever going to make it big, we all have to make {b}sacrifices{/b}."
    scene sm1cs-am007-10 mc-am-phone2_c1 with dissolve
    play voice3 girl22_disappointed_oh noloop
    am "Oh, we all have to make sacrifices, Pepper?"
    stop sound2 fadeout 1.0
    scene sm1cs-am007-09 mc-am-phone_c2 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mct "April is talking to Pepper."
    mct "The drummer from her band."
    scene sm1cs-am007-10 mc-am-phone2_c1 with dissolve
    play voice3 girl22_arrogant_huh noloop
    am "What do you two sacrifice?"
    play sound sfx_throw_something1
    scene sm1cs-am007-11 mc-am-phone3_c1 with dissolve
    play voice3 girl22_angry_dagh noloop
    am "I have a job I {i}have{/i} to do to make enough money to pay rent and bills."
    am "Pepper... your parents still pay your rent."
    scene sm1cs-am007-14 mc-am-phone6_c1 with dissolve
    play voice3 girl22_arrogant_ha noloop
    am "And Mitch has been squatting with the Hastings for years."
    play voice4 sfx_phone_talk_male1 noloop volume 0.7
    mcon "And I'm very grateful to them."
    play voice2 mc_thinking_hmm1 noloop
    mct "That's Mitch. The lead guitarist and singer."
    mct "Better watch how you talk to my girl, Mitch."
    play sound sfx_cloth_rustling1
    scene sm1cs-am007-16 mc-am-phone8_c1 with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "My point is...{w} You two have nothing to do but the band."
    play voice4 sfx_phone_talk_female2 noloop volume 0.7
    ps "Okay, {i}maybe{/i} you have a point..."
    ps "We should have listened better and we should accept that sometimes you're going to miss pratice."
    scene sm1cs-am007-17 mc-am-phone9_c1 with dissolve
    play voice3 girl22_happy_relief noloop
    am "Thank you."
    play voice4 sfx_phone_talk_male2 noloop volume 0.7
    mcon "Hopefully this means you can at {i}least{/i} do the other thing for us, April."
    scene sm1cs-am007-18 mc-am-phone10_c1 with dissolve
    play voice3 girl22_no_simple noloop
    am "No. I already told you 'no'."
    am "I am not spamming Orbix's client list with an email promoting the band and our next three shows!"
    play voice4 "<from 0 to 0.5>audio/sfx/gadgets/sfx_phone_talk_female1.ogg" noloop volume 0.7
    ps "Please, April..."
    am "Do you hear yourself, Pepper?"
    play voice4 "<from 0 to 0.5>audio/sfx/gadgets/sfx_phone_talk_male2.ogg" noloop volume 0.7
    mcon "They won't care about one little email."
    scene sm1cs-am007-19 mc-am-phone11_c1 with dissolve
    play voice3 girl22_disappointed_ehh1 noloop
    am "*sighs* Mitch, you haven't had a real job in years."
    am "You don't have a pot to piss in."
    play voice4 sfx_phone_talk_male1 noloop
    mcon "So you're really going to put working for those squares above the good of the band?"
    mcon "You'd rather work for the {b}Man{/b} than help us succeed?"
    play voice4 "<from 0 to 0.4>audio/sfx/gadgets/sfx_phone_talk_female2.ogg" noloop volume 0.7
    ps "Mitch..."
    mcon "No, I want to {b}hear{/b} her say it."
    play sound sfx_hands_clap1
    scene sm1cs-am007-20 mc-am-phone12_c1 with dissolve
    play voice3 girl22_angry_breathing noloop
    am "*breathing deeply*"
    am "You guys..."
    am "I love you.{w} And you know I love Moonstone Blaze."
    am "But I'm not going to do something stupid that might threaten my job here."
    am "And you're calling at the worst possible time."
    scene sm1cs-am007-09 mc-am-phone_c1 with dissolve
    play voice3 girl22_angry_cough noloop
    if player.has_played_scene("sm1fs_i005") and not player.has_played_scene("sm1fs_i006"):
        am "Some asshole put a virus into our systems and it's slowing down progress on our big project."
        am "Everyone is worried the client might dump us."
        am "And that could screw a lot of people here."
    if player.has_played_scene("sm1fs_i006"):
        am "We have still barely recovered from repairing the damage of that virus I told you guys about."
        play voice4 "<from 0 to 0.5>audio/sfx/gadgets/sfx_phone_talk_male2.ogg" noloop volume 0.7
        mcon "What virus?"
        play voice4 sfx_phone_talk_female2 noloop
        ps "Uh... I mean come on.{w} You're a pro.{w} Virus smirus."
    else:
        am "I have a mountain of work to do around here."
    scene sm1cs-am007-12 mc-am-phone4_c1 with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "*sighs* And I can't keep spending so much time on the phone."
    am "Anna prefers to avoid me, but eventually she's going to check in on my work."
    am "And Claire keeps giving me looks."
    play voice4 "<from 0 to 0.5>audio/sfx/gadgets/sfx_phone_talk_female1.ogg" noloop volume 0.7
    ps "What kind of looks?"
    play sound sfx_cloth_rustling2
    scene sm1cs-am007-14 mc-am-phone6_c1 with dissolve
    play voice3 girl22_arrogant_he noloop
    am "The kind of looks my mom gave me every time I talked about Bill Gates and not Connie Dolls."
    play voice4 "<from 0 to 0.5>audio/sfx/gadgets/sfx_phone_talk_female2.ogg" noloop volume 0.7
    ps "Oh shit.{w} I saw one of those once."
    play voice4 sfx_phone_talk_male1 noloop
    mcon "We're getting off topic.{w} Can you at least say that you're going to be around for practice tomorrow?"
    scene sm1cs-am007-21 mc-am-phone13_c1 with dissolve
    pause
    play voice3 girl22_surprised_eh1 noloop
    am "I gotta go."
    am "The noobie needs something."
    play voice4 sfx_phone_talk_female2 noloop
    ps "Oh the stud?{w} Has he asked to strum your guitar yet?"
    play voice3 girl22_angry_argh3 noloop
    with vpunch
    am "Pepper!"
    scene sm1cs-am007-23 mc-am-look2_c1 with dissolve
    play voice4 sfx_phone_talk_female1 noloop
    ps "You know...{w} Has he pounded your kick drum?"
    play voice3 girl22_surprised_ohmy noloop
    scene sm1cs-am007-23 mc-am-look2_c1 with hpunch
    am "Oh my god.{w} I'm hanging up now!"
    stop voice4 fadeout 1.0
    play sound sfx_phone_hungup1 volume 2.0
    scene sm1cs-am007-24 mc-am-wave_c2 with dissolve
    "Beep"
    play voice2 mc_happy_yay2 noloop
    mc "There you are."
    scene sm1cs-am007-25 mc-am-look_c1 with dissolve
    play voice3 girl22_surprised_eh2 noloop
    am "Can I help you with something, [mcname]?"
    scene sm1cs-am007-25 mc-am-look_c2 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I was going to ask you the same thing."
    mc "And it doesn't seem like that phone call helped."
    scene sm1cs-am007-26 mc-am-look2_c1 with dissolve
    play voice3 girl22_yes_yeah3 noloop
    am "Congratulations. Your eyes and ears work."
    mc "..."
    play voice3 girl22_thinking_hmm2 noloop
    am "[mcname], I..."
    am "Just because we are dating, doesn't mean you have to come running to my aid anytime it looks like I'm in trouble."
    am "I work in tech.{w} Every day is a shit sandwhich for breakfast and a anxiety cocktail for lunch."
    am "And this week has been order on the double-shit sandwhich."
    if player.has_played_scene("sm1fs_i005") and not player.has_played_scene("sm1fs_i006"):
        play sound sfx_throw_something1
        scene sm1cs-am007-26-1 mc-am-talk_c1 with dissolve
        play voice3 girl22_angry_argh1 noloop
        am "I don't have to tell you what a headache the virus has been."
        am "Every time Sienna and I are close to annihilating the damn thing, it mutates and we have to start over."
        menu:
            "You'll figure it out":
                $ player.set_choice("sm1cs_am007_encourage_am")
                scene sm1cs-am007-26-1 mc-am-talk_c2 with dissolve
                play voice2 mc_hey_hey5 noloop
                mc "I am sure that you will figure it out, April."
                play voice3 girl22_yes_aga1 noloop
                am "I will.{w} Or I'll be fired."
            "Suprised it's taking you this long":
                scene sm1cs-am007-26-1 mc-am-talk_c2 with dissolve
                play voice2 mc_thinking_emm1 noloop
                mc "It's kind of strange that it has taken so long."
                scene sm1cs-am007-26-4 mc-am-talk4_c1 with dissolve
                play voice3 girl22_yes_aga1 noloop
                am "Yeah well, we can thank the absolute dick who designed it."
                am "The silver lining is that if the hacker attacked the client's website, it would be a different story."
                am "We have a chance to fight back."
                play sound sfx_cloth_rustling1
                scene sm1cs-am007-26-6 mc-am-talk6_c2 with dissolve
                play voice2 mc_surprised_wow3 noloop
                mc "That's the spirit, April."
                scene sm1cs-am007-26-6 mc-am-talk6_c1 with dissolve
                am "..."
    elif player.has_played_scene("sm1fs_i006"):
        scene sm1cs-am007-26-7 mc-am-talk7_c2 with dissolve
        play voice2 mc_hey_hey7 noloop
        mc "Hey, at least you figured out how to get that virus off the Orbix systems."
        scene sm1cs-am007-26-8 mc-am-talk8_c1 with dissolve
        play voice3 girl22_thinking_hmm1 noloop
        am "Well... that was a team effort."
        am "Even {i}you{/i} were able to help out, [mcname]."
        scene sm1cs-am007-26-8 mc-am-talk8_c2 with dissolve
        play voice2 d4s4_mclaugh noloop volume 1.6
        mc "Haha. Was that a rare compliment from you, Mercer?"
        scene sm1cs-am007-27 mc-am-look_c1 with dissolve
        play voice3 girl22_arrogant_pff noloop
        am "*playful* Shut up."
    else:
        play sound sfx_cloth_rustling3
        scene sm1cs-am007-27 mc-am-look_c1 with dissolve
        play voice3 girl22_thinking_hmm1 noloop
        am "So... I appreciate you checking in."
        am "But I can manage just fine."
    play sound sfx_phone_ringtone2_debbie
    scene sm1cs-am007-27-1 mc-am-phone_c1 with dissolve
    "Beep beep beep"
    play voice3 girl22_disappointed_ah noloop
    am "Oh shit."
    am "Really?!{w} Today of all days?"
    play sound sfx_heels_steps2 loop
    scene sm1cs-am007-28 mc-am-walk_c1 with dissolve
    play voice3 girl22_disappointed_mmf noloop
    am "I gotta...{w} go."
    stop sound fadeout 1.0
    scene sm1cs-am007-29 mc-am-stop_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mct "And there she goes again."
    scene sm1cs-am007-30 mc-am-talk_c1 with dissolve
    play voice3 girl22_hey_simple noloop
    am "Hey, how good are you at jogging?"
    play voice2 d2s9_confused noloop volume 1.6
    mc "Uh..."
    scene sm1cs-am007-30 mc-am-talk_c2 with dissolve
    menu:
        "I have heard of the general concept":
            $ player.set_choice("sm1cs_am007_joke_jogging")
            play voice2 d9s2_yeah noloop volume 1.7
            mc "I know the general premise."
            mc "People do it when they don't have a car."
        "Pretty good. I pretty much walk or jog everywhere":
            play voice2 d9s2_yeah noloop volume 1.7
            mc "Pretty good."
            play sound sfx_hands_clap3
            scene sm1cs-am007-31 mc-am-talk2_c2 with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "These puppies are my main vehicle all day. Seven days a week."
    scene sm1cs-am007-32 mc-am-talk3_c1 with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "My marathon alarm just went off."
    am "I set a random alert every two weeks."
    am "When it rings, come rain or shine, I gotta start."
    scene sm1cs-am007-33 mc-am-talk4_c2 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "You run a marathon every two weeks?"
    scene sm1cs-am007-33 mc-am-talk4_c1 with dissolve
    play voice3 girl22_yes_yeah1 noloop
    am "Have you seen how much junk food I eat?"
    am "It's a small price to pay for a sweet tooth."
    scene sm1cs-am007-32 mc-am-talk3_c2 with dissolve
    menu:
        "You're sweet":
            $ player.set_choice("sm1cs_am007_am_sweet")
            $ CharacterController.get_character("am").add_point(1)
            play sound sfx_cloth_rustling2
            scene sm1cs-am007-35 mc-am-talk6_c2 with dissolve
            play voice2 mc_thinking_hmm8 noloop
            mc "Well you are {i}sweet{/i} as sugar."
            scene sm1cs-am007-34 mc-am-talk5_c1 with dissolve
            play voice3 girl22_yes_aga11 noloop
            am "Sure..."
            am "So long as your definition of 'sweet' is the opposite of what it means in the dictionaries of every human language."
            am "Idiot."
            jump sm1cs_am007_jogging
        "I'm confused":
            $ player.set_choice("sm1cs_am007_mc_confused")
            play sound sfx_cloth_rustling2
            scene sm1cs-am007-35 mc-am-talk6_c2 with dissolve
            play voice2 d1s5_mchappy noloop volume 1.7
            mc "The word 'sweet' and you don't seem to fit together."
            scene sm1cs-am007-35 mc-am-talk6_c1 with dissolve
            play voice3 girl22_arrogant_hm noloop
            am "With that attitude, you're certainly doing great at never seeing my sweet side."
            play voice2 mc_thinking_oh1 noloop
            mc "Maybe I'm into sour candy."
            am "Hmm."
            jump sm1cs_am007_jogging
        "Maybe just don't eat so much":
            $ player.set_choice("sm1cs_am007_mock_am")
            $ CharacterController.get_character("am").deduct_point(2)
            play sound sfx_cloth_rustling2
            scene sm1cs-am007-39 mc-am-talk10_c2 with dissolve
            play voice2 mc_thinking_oh1 noloop
            mc "Maybe you shouldn't eat so much junk food, April."
            am "..."
            mc "..."
            scene sm1cs-am007-40 mc-am-look_c1 with dissolve
            play voice3 girl22_happy_mmm noloop
            am "I will give you one chance.{w} Just one..."
            am "To take back your {b}absurd{/b} statement."
            am "That you just made about your girlfriend."
            am "To her {b}face{/b}...{w} When she's having a bad day."
            jump sm1cs_am007_menu_2
label sm1cs_am007_menu_2:
    menu:
        "I am so sorry":
            scene sm1cs-am007-44 mc-am-talk_c2 with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "I'm sorry. April. I didn't mean it."
            play sound sfx_cloth_rustling1
            scene sm1cs-am007-44 mc-am-talk_c3 with dissolve
            play voice3 girl22_yes_aga10 noloop
            am "Hmmmph. Good."
        "I regret nothing":
            $ player.set_choice("sm1cs_am007_regret_nothing")
            $ CharacterController.get_character("am").deduct_point(2)
            play voice2 mc_no_uhuh1 noloop
            mc "I said what I said."
            mc "Hashtag no regrets."
            play voice3 girl22_angry_argh3 noloop
            play sound sfx_kick3
            scene sm1cs-am007-40 mc-am-look_c2 with vpunch
            am "Hiyah."
            play voice2 mc_pain_argh1 noloop
            play sound sfx_fall_down1
            scene sm1cs-am007-41 mc-am-knee_c2 with vpunch
            mc "Frrrrrrrffffhhhh...."
            queue voice2 mc_pain_cough2 noloop
            mc "*coughs*"
            mc "I deserve that."
            scene sm1cs-am007-42 mc-am-look_c1 with dissolve
            play voice3 girl22_yes_angry noloop
            am "Damn right."
            am "Hmmmph."
            scene sm1cs-am007-42 mc-am-look_c2 with dissolve
            play voice2 mc_pain_rrrr noloop
            mc "Giraaah... Going to leave a mark."
            play sound sfx_cloth_rustling3
            scene sm1cs-am007-43 mc-am-look2_c1 with dissolve
            play voice3 girl22_yes_aga10 noloop
            am "You'll live."
            scene sm1cs-am007-43 mc-am-look2_c2 with dissolve
            play voice2 mc_thinking_mmm3 noloop
            mct "Note to self.{w} Don't ever say {b}that{/b} again."
    jump sm1cs_am007_jogging
label sm1cs_am007_jogging:
    scene sm1cs-am007-45 mc-am-talk2_c1 with dissolve
    play voice3 girl22_surprised_huh2 noloop
    am "So what do you say?"
    scene sm1cs-am007-45 mc-am-talk2_c2 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "To what?"
    scene sm1cs-am007-46 mc-am-talk3_c1 with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    am "Do you want to run a marathon with me?"
    scene sm1cs-am007-46 mc-am-talk3_c2 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Uh sure. How do I sign up?"
    scene sm1cs-am007-45 mc-am-talk2_c1 with dissolve
    play voice3 girl22_no_high noloop
    am "No. I mean. It's not a real marathon."
    am "I've mapped out a route. It starts at Theomalt Park and goes throughout the city."
    am "The distance is equivalent to that of a marathon."
    scene sm1cs-am007-45 mc-am-talk2_c2 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "My girl is wicked smart."
    mc "Sure. I can do a marathon with you."
    scene sm1cs-am007-46 mc-am-talk3_c1 with dissolve
    play voice3 girl22_happy_yeah noloop
    am "Great. It will be like a date."
    am "Just the two of us."
    scene sm1cs-am007-46 mc-am-talk3_c2 with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "Even better."
    play voice3 girl22_thinking_oh noloop
    am "I need to get into my gym clothes. You should put on something else too."
    am "Unless you want to ruin your clothes."
    play sound sfx_cloth_rustling4
    scene sm1cs-am007-47 mc-am-hug_c1 with dissolve
    play voice3 girl22_sex_closedmoan2 noloop
    am "*nervously* Ummm."
    am "Kiss me goodbye?"
    am "*soft breaths*"
    scene sm1cs-am007-48 mc-am-kiss_c1 with dissolve
    play voice2 d1s1_mmm noloop
    play voice3 girl22_sex_closedmoan3 noloop
    play sound dahlia_kiss_french1
    am "Mmmmm."
    scene sm1cs-am007-48 mc-am-kiss_c2 with dissolve
    play sound mc_kiss2
    pause
    scene sm1cs-am007-49 mc-am-look_c1 with dissolve
    play voice3 girl22_happy_laugh1 noloop
    am "How do you kiss so much better than you code?"
    scene sm1cs-am007-49 mc-am-look_c2 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "One of life's mysteries I guess."
    scene sm1cs-am007-50 mc-am-talk_c1 with dissolve
    play voice3 girl22_arrogant_ha noloop
    am "Hah."
    am "Text me when you're at the park."
    scene sm1cs-am007-50-1 mc-am-walk_c2 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Count on it."
    stop sound4 fadeout 2.0
    jump sm1cs_am007_20_minutes_later
label sm1cs_am007_20_minutes_later:
    stop music fadeout 3.0
    scene black
    show screen scene_transistion(_("Twenty minutes later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene sm1cs-am007-50-2 mc-am-park1_c1
    play sound5 sfx_parkday_birds fadein 2.0
    with Fade(0.5, 0.5, 0.5)
    play sound sfx_cloth_rustling1
    queue music music_run_4_yourlife
    pause
    scene sm1cs-am007-51 mc-am-park2_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mct "She said she's coming over."
    play sound sfx_cloth_rustling2
    scene sm1cs-am007-52 mc-am-park3_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mct "Where are you, April?"
    play sound sfx_heels_steps2 loop
    if player.get_choice("sm1cs_am007_regret_nothing"):
        mct "Gah. I probably shouldn't be jogging this close to a groin injury."
        mct "Then again, it's never a good idea to even remotely imply a girl eats too much."
        mct "Of anything."
    scene sm1cs-am007-a52 mc-am-park-glambot-00
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs_am007-a52-glambot
    play voice3 girl22_hey_happy noloop
    am "Hey."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-am007-53 mc-am-look_c1 with dissolve
    play voice2 mc_hey_hello noloop
    mc "Hello-"
    mc "Hot."
    stop sound fadeout 1.0
    scene sm1cs-am007-53 mc-am-look_c2 with dissolve
    play voice3 girl22_happy_laugh3 noloop
    am "*giggles* You ready?"
    menu:
        "I need a glass of milk":
            $ player.set_choice("sm1cs_am007_glass_of_milk")
            $ CharacterController.get_character("am").add_point(1)
            scene sm1cs-am007-54 mc-am-talk_c1 with dissolve
            play voice2 mc_arrogant_hm2 noloop
            mc "Um... I don't think so."
            scene sm1cs-am007-54 mc-am-talk_c2 with dissolve
            play voice3 girl22_surprised_huh1 noloop
            am "Why not?"
            scene sm1cs-am007-55 mc-am-ask_c1 with dissolve
            play voice2 mc_angry_errr7 noloop
            mc "I have a sudden thrist for a big glass of milk."
            scene sm1cs-am007-55 mc-am-ask_c2 with dissolve
            play voice3 girl22_no_uhuh1 noloop
            am "You're here to run.{w} Not oggle my tits."
            scene sm1cs-am007-56 mc-am-look_c1 with dissolve
            play voice2 mc_happy_hah2 noloop
            mc "Can't I do both?"
            play sound sfx_hair_scratch1
            scene sm1cs-am007-56 mc-am-look_c2 with dissolve
            play voice3 girl22_arrogant_hm noloop
            am "Come on."
            jump sm1cs_am007_jogging_continue
        "I was born ready":
            $ player.set_choice("sm1cs_am007_born_ready")
            scene sm1cs-am007-57 mc-am-ask_c1 with dissolve
            play voice2 mc_surprised_oh2 noloop
            mc "Oh I was born ready."
            mc "Not to jog or anything, but I was definitely ready for a life of adventure."
            scene sm1cs-am007-57 mc-am-ask_c2 with dissolve
            play voice3 girl22_arrogant_hm noloop
            am "We'll see."
            jump sm1cs_am007_jogging_continue
        "Shouldn't you stretch first?":
            $ player.set_choice("sm1cs_am007_stretch_first")
            play sound sfx_cloth_rustling2
            scene sm1cs-am007-58 mc-am-talk_c1 with dissolve
            play voice2 mc_thinking_wait1 noloop
            mc "Wait.{w} Uh... shouldn't you stretch first?"
            mc "You don't want to pull a hammy."
            scene sm1cs-am007-58 mc-am-talk_c2 with dissolve
            play voice3 girl22_yes_yep4 noloop
            am "I already stretched earlier, [mcname]."
            mct "Doh.{w} I was hoping for a pre-run show."
            scene sm1cs-am007-59 mc-am-talk2_c1 with dissolve
            play voice2 mc_yes_okay1 noloop
            mc "Okay."
            jump sm1cs_am007_jogging_continue
        "Why don't you wear more stuff like that?":
            $ player.set_choice("sm1cs_am007_wear_hot_dress")
            $ CharacterController.get_character("am").deduct_point(2)
            play sound sfx_cloth_rustling2
            scene sm1cs-am007-58 mc-am-talk_c1 with dissolve
            play voice2 mc_thinking_hmm7 noloop
            mc "Why don't you wear stuff like that more often?"
            scene sm1cs-am007-58 mc-am-talk_c2 with dissolve
            play voice3 girl22_arrogant_hm noloop
            am "Because I'm a professional."
            am "When I'm at Orbix, I'm there to work."
            am "Not be your fap fuel."
            menu:
                "Too late":
                    $ player.set_choice("sm1cs_am007_too_late")
                    $ CharacterController.get_character("am").add_point(1)
                    scene sm1cs-am007-59 mc-am-talk2_c1 with dissolve
                    play voice2 mc_happy_hah2 noloop
                    mc "Too late!"
                    scene sm1cs-am007-59 mc-am-talk2_c2 with dissolve
                    play voice3 girl22_angry_geh noloop
                    am "You are such a dog."
                    play voice2 mc_surprised_oof1 noloop
                    mc "Woof woof."
                "Of course":
                    scene sm1cs-am007-59 mc-am-talk2_c1 with dissolve
                    play voice2 mc_yes_aga1 noloop
                    mc "Of course."
    jump sm1cs_am007_jogging_continue
label sm1cs_am007_jogging_continue:
    scene sm1cs-am007-56 mc-am-look_c2 with dissolve
    play voice3 girl22_thinking_hmm2 noloop
    am "Make sure your phone is on silent."
    am "No interruptions. Just the two of us burning a few gigabytes of calories."
    scene sm1cs-am007-57 mc-am-ask_c1 with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Let's do it."
    scene sm1cs-am007-60 mc-am-walk_c2 with dissolve
    play voice3 girl22_yes_aga6 noloop
    am "Follow me."
    play sound2 sfx_stone_run1 fadein 1.0
    play sound3 sfx_sport_run1 fadein 1.0
    scene sm1cs-am007-61 mc-am-run_c1 with dissolve
    pause
    scene sm1cs-am007-62 mc-am-run2_c1 with dissolve
    pause
    scene sm1cs-am007-63 mc-am-run3_c1 with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    stop sound5 fadeout 1.0
    scene black
    show screen scene_transistion(_("An hour later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound2 sfx_stone_run1 fadein 1.0
    play sound3 sfx_sport_run1 fadein 1.0
    play sound5 sfx_distanttraffic_city fadein 1.5
    play sound4 sfx_closetraffic_city
    scene sm1cs-am007-64 mc-am-city1_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-am007-64 mc-am-city1_c2 with dissolve
    pause
    scene sm1cs-am007-66 mc-am-city3_c1 with dissolve
    play voice3 girl22_hey_loud noloop
    am "Come on, [mcname]."
    am "We're almost halfway done."
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-am007-67 mc-am-walk_c1 with dissolve
    play voice2 d7s4_mcbreathing noloop
    mc "*panting*"
    mc "Oh god."
    mc "*wheezing* The human body was not meant to run this much."
    play sound sfx_heels_steps2
    scene sm1cs-am007-67 mc-am-walk_c2 with dissolve
    play voice3 girl22_happy_phew noloop
    am "Come on.{w} You can do it."
    play sound sfx_skirt_off1 volume 1.6
    scene sm1cs-am007-68 mc-am-talk_c1 with dissolve
    play voice2 mc_pain_ffff noloop
    mc "I can't. *wheezes*{w} I'm dead."
    mc "Just leave me where I fall."
    scene sm1cs-am007-68 mc-am-talk_c2 with dissolve
    play voice3 girl22_no_nope1 noloop
    am "Oh no you don't."
    am "I'd be a poor girlfriend if I just let you die here."
    scene sm1cs-am007-69 mc-am-talk2_c1 with dissolve
    play voice2 mc_pain_cough2 noloop
    mc "Thanks."
    scene sm1cs-am007-69 mc-am-talk2_c2 with dissolve
    play voice3 girl22_yes_yeah4 noloop
    am "The police station is not far."
    am "If I can get you there, at least I'll be doing a public service."
    scene sm1cs-am007-70 mc-am-talk3_c1 with dissolve
    play voice2 mc_happy_laugh4 noloop
    mc "*painful laughing* Your concern is so moving."
    scene sm1cs-am007-70 mc-am-talk3_c2 with dissolve
    play voice3 girl22_yes_aga4 noloop
    am "But you're not going to drop on me yet, are you?"
    scene sm1cs-am007-71 mc-am-kiss_c1 with dissolve
    play voice3 girl22_sex_closedmoan6 noloop
    play sound mc_kiss1
    am "Mwaaaah."
    scene sm1cs-am007-71 mc-am-kiss_c2 with dissolve
    play sound mc_kiss3
    pause
    scene sm1cs-am007-72 mc-am-look_c2 with dissolve
    play voice3 girl22_disgust_meeh noloop
    am "Oh my god."
    am "Do your sweat glands have sweat glands?"
    play sound sfx_paint_hand_in1 volume 0.7
    scene sm1cs-am007-73 mc-am-look2_c1 with dissolve
    play voice2 mc_happy_laugh3 noloop
    mc "Hahaha.{w} Let's move it."
    mc "Huhaaah..."
    play sound2 sfx_stone_run1 fadein 1.0
    play sound3 sfx_sport_run1 fadein 1.0
    scene sm1cs-am007-74 mc-am-run_c3 with dissolve
    play voice2 mc_happy_oof1 noloop
    mct "Just put one shaking foot in front of the other shaking foot."
    play voice3 girl22_yes_aga5 noloop
    am "I'll be right here with you."
    stop sound2 fadeout 1.5
    stop sound3 fadeout 1.5
    stop sound4 fadeout 1.5
    stop sound5 fadeout 1.5
    jump sm1cs_am007_one_hour_later
label sm1cs_am007_one_hour_later:
    scene black
    show screen scene_transistion(_("One hour of torture later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound5 sfx_parkday_birds fadein 1.5
    play sound2 sfx_stone_run1 fadein 1.0
    play sound3 sfx_sport_run1 fadein 1.0
    scene sm1cs-am007-74-2 mc-am-run_c1
    with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1cs-am007-75 mc-am-run2_c1 with dissolve
    pause
    scene sm1cs-am007-76 mc-am-run3_c1 with dissolve
    pause
    play voice2 mc_scared_oh3 noloop
    $ renpy.music.set_volume(0.35, 3.0, "music" )
    play sound sfx_sand_fallen1
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-am007-78 mc-am-down_c1 with hpunch
    mc "Oh... Sweet Fescue grass."
    mc "I've never been sexually attracted to a plant before before."
    play sound sfx_hair_scratch1
    scene sm1cs-am007-79 mc-am-look_c1 with dissolve
    play voice2 d1s5_orgasm noloop
    mc "But you feel so good beneath me."
    mc "You are my {b}new{/b} girlfriend."
    scene sm1cs-am007-79 mc-am-look_c2 with dissolve
    play voice3 girl22_happy_laugh2 noloop
    am "Haha. You ass."
    am "Good thing I'm not the jealous type."
    stop voice3 fadeout 1.5
    scene sm1cs-am007-80 mc-am-talk_c1 with fade
    play voice2 mc_scared_oh4 noloop
    mc "I still...{w} Can't believe...{w} You do this...{w} Like twice a month."
    scene sm1cs-am007-80 mc-am-talk_c2 with dissolve
    play voice3 girl22_yes_yep1 noloop
    am "It's just one of my systems."
    am "Helps me out when I'm stressing too.{w} That massive surge of endorphins is just what the doctor ordered after a long day of breaking and fixing code."
    scene sm1cs-am007-81 mc-am-talk2_c1 with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "I might need a doctor after that jog."
    scene sm1cs-am007-81 mc-am-talk2_c2 with dissolve
    play voice3 girl22_disappointed_oh noloop
    am "Oh please..."
    am "If you were going to die you would have died by now."
    play sound sfx_cloth_rustling1
    scene sm1cs-am007-85 mc-am-look_c1 with dissolve
    play voice2 mc_happy_laugh1 noloop
    mc "Hahaha."
    scene sm1cs-am007-85 mc-am-look_c2 with dissolve
    play voice2 mc_pain_ou3 noloop
    mc "Haha- *groans* Oh!"
    mc "It does not feel good to laugh."
    scene sm1cs-am007-86 mc-am-look2_c1 with dissolve
    play voice2 mc_znames_april3 noloop
    mc "April?"
    scene sm1cs-am007-86 mc-am-look2_c2 with dissolve
    play voice3 girl22_yes_questioning noloop
    am "Yes, [mcname]."
    scene sm1cs-am007-87 mc-am-look3_c1 with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Where are you?"
    scene sm1cs-am007-87 mc-am-look3_c2 with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "Mmm. I'm right here."
    scene sm1cs-am007-88 mc-am-talk_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I don't think so."
    mc "You're thinking about your band right?"
    mc "Pepper and Mitch."
    scene sm1cs-am007-89 mc-am-talk2_c2 with dissolve
    pause
    scene sm1cs-am007-86 mc-am-look2_c2 with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "I just can't believe them.{w} Pepper and Mitch have been my friends for years."
    am "But if you looked up spoiled brats in the dictionary, their pictures would be right there!"
    scene sm1cs-am007-90 mc-am-talk3_c3 with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "They know how much I love music, and they act like I'm trying to sabotage the band."
    am "I'd fucking give up my left hand to make it big as a rock star."
    scene sm1cs-am007-90 mc-am-talk3_c2 with dissolve
    play voice3 girl22_angry_breathing noloop
    am "But I'm not an idiot."
    am "The odds to become a rock star are shit."
    play sound sfx_leg_kick7
    play sound2 sfx_sand_fallen1 noloop
    scene sm1cs-am007-91 mc-am-look_c2 with dissolve
    play voice3 girl22_disappointed_geh noloop
    am "And if I left Orbix...{w} if I just abandoned {i}Anna{/i} and the rest of them..."
    am "They'd be {b}fucking{/b} lost without me."
    am "And if the band doesn't make it.{w} I would have to earn my way back into tech."
    am "I couldn't just walk back into Orbix like nothing happened."
    scene sm1cs-am007-91 mc-am-look_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mc "..."
    play voice3 girl22_surprised_huh2 noloop
    am "Well... say something, why don't you?"
    play sound sfx_hair_scratch1
    scene sm1cs-am007-94 mc-am-talk2_c2 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "You're obviously very passionate about the band."
    scene sm1cs-am007-93 mc-am-talk_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "But, as far as I can tell, coding has been part of your DNA even longer."
    menu:
        "You're between a rock and a hard place":
            $ player.set_choice("sm1cs_am007_rock_hard_place")
            $ CharacterController.get_character("am").add_point(1)
            play voice2 mc_thinking_hm noloop
            mc "You're between a rock and a hard place right now, April."
            mc "You're smart.{w} You know that sooner or later...{w} Something's gotta give."
            mc "And... Something tells me...{w} You already made the call."
            scene sm1cs-am007-94 mc-am-talk2_c2 with dissolve
            play voice3 girl22_yes_yeah1 noloop
            am "Maybe.{w} I think I needed to hear that from someone other than myself."
            am "Thank you, [mcname]."
            play sound sfx_cloth_rustling2
            scene sm1cs-am007-95 mc-am-ask_c1 with dissolve
            play voice2 mc_thinking_hmm3 noloop
            mc "So what are you going to do?"
        "I don't know what to say":
            play voice2 mc_disappointed_ehh4 noloop
            mc "I'm sorry. I can't really give you good advice about this."
            mc "It's your life, and I'd hate to say something that puts you on the wrong path."
            scene sm1cs-am007-96 mc-am-talk_c2 with dissolve
            play voice3 girl22_yes_yeah1 noloop
            am "Yeah. Forget I said anything..."
            scene sm1cs-am007-96 mc-am-talk_c1 with dissolve
            mc "..."
            play voice2 mc_thinking_hmm3 noloop
            mc "So what happens now?"
    play sound sfx_cloth_rustling3
    scene sm1cs-am007-97 mc-am-sit_c2 with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    am "..."
    am "You should go to the bathroom. {w}Splash some water in your face."
    am "You've still got some grass up your nose."
    play sound sfx_footsteps_grass1
    scene sm1cs-am007-98 mc-am-sit2_c1 with dissolve
    stop sound fadeout 2.5
    play voice2 mc_no_nah1 noloop
    mc "I'm good. I'll just shower off at home."
    scene sm1cs-am007-100 mc-am-talk_c2 with dissolve
    play voice3 girl22_hey_simple noloop
    am "It's fine. I'll come with."
    scene sm1cs-am007-101 mc-am-talk2_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Uh... I'm good. I don't need to go right now."
    scene sm1cs-am007-101 mc-am-talk2_c2 with dissolve
    play voice3 girl22_sex_closedmoan3 noloop
    am "I think you should {b}really{/b} go to the bathroom, [mcname]."
    am "And I'll come {i}with{/i} you."
    scene sm1cs-am007-102 mc-am-talk3_c1 with dissolve
    mc "..."
    menu:
        "Do you have some sixth sense?":
            $ player.set_choice("sm1cs_am007_sixth_sense")
            play voice2 mc_surprised_uh3 noloop
            mc "Do you have some sixth sense about my bladder?"
            mc "I'm telling you, I don't need to use the restroom."
            scene sm1cs-am007-102 mc-am-talk3_c2 with dissolve
            play voice3 girl22_yes_aga3 noloop
            am "Sure. But do you really know that for sure?"
            am "Cause sometimes if you go into a restroom, stuff will happen."
            scene sm1cs-am007-103 mc-am-talk4_c2 with dissolve
            play voice3 girl22_happy_mmm noloop
            am "{i}Good{/i} stuff."
            scene sm1cs-am007-103 mc-am-talk4_c1 with dissolve
            play voice2 mc_surprised_what5 noloop
            mc "..."
            mc "What?"
            play sound sfx_hair_scratch1
            scene sm1cs-am007-104 mc-am-talk5_c2 with dissolve
            play voice3 girl22_surprised_ohmy noloop
            am "Oh my god."
            am "I want you to play with me in the bathroom, [mcname]."
            scene sm1cs-am007-105 mc-am-talk6_c1 with dissolve
            play voice2 mc_thinking_oh1 noloop
            mc "Ah."
            play voice2 mc_scared_oh2 noloop
            scene sm1cs-am007-105 mc-am-talk6_c1 with hpunch
            mc "Ahhhhh..."
            mc "Why didn't you say so?"
            scene sm1cs-am007-105 mc-am-talk6_c2 with dissolve
            play voice3 girl22_angry_breathing noloop
            am "Lord help me..."
        "Oh. I get it":
            play sound sfx_cloth_rustling2
            scene sm1cs-am007-106 mc-am-talk7_c1 with dissolve
            play voice2 mc_thinking_mmm7 noloop
            mc "Ooooooh. I get it."
            mc "You want to turn that restroom..."
            mc "Into a sex room..."
            scene sm1cs-am007-106 mc-am-talk7_c2 with dissolve
            play voice3 girl22_surprised_ohmy noloop
            am "Oh my god."
            am "Forget I said anything."
            scene sm1cs-am007-107 mc-am-talk8_c1 with dissolve
            play voice2 mc_no_uhuh2 noloop
            mc "Nah-uh. No take-backs."
            scene sm1cs-am007-107 mc-am-talk8_c2 with dissolve
            play voice3 girl22_angry_hmm noloop
            am "Then hurry the fuck up before I change my mind, dummy."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-am007-110 mc-am-walk_c1 with dissolve
    pause
    stop music fadeout 4.0
    stop sound5 fadeout 2.0
    $ renpy.music.set_volume(1.0, 4.0, "music" )
    stop sound2 fadeout 1.0
    play sound sfx_door_openclosed1
    scene sm1cs-am007-111 mc-am-look_c2 with fade
    play voice3 girl22_thinking_hmm1 noloop
    am "Lock the door."
    scene sm1cs-am007-112 mc-am-look2_c1 with dissolve
    play sound sfx_door_locked1
    "Click"
    queue music music_toilette_breeze
    scene sm1cs-am007-112 mc-am-look2_c2 with dissolve
    pause
    play sound2 sfx_cloth_rustling3 noloop
    scene sm1cs-am007-113 mc-am-kiss_c1 with dissolve
    play voisex2 mc_sex_closedmoans1
    play voisex3 girl22_sex_sucking3
    play sound dahlia_kiss_french1
    mc "Mmmummm!"
    scene sm1cs-am007-113 mc-am-kiss_c2 with dissolve
    am "*moaning*"
    mct "All that fucking jogging and sweating has me right on the edge."
    scene sm1cs-am007-113-1 mc-am-kiss2_c2 with dissolve
    am "Muah..."
    am "Take off your shirt!"
    stop voisex2 fadeout 1.0
    stop voisex3 fadeout 1.0
    play sound sfx_skirt_off2
    scene sm1cs-am007-114 mc-am-look_c1 with dissolve
    pause
    play sound sfx_cloth_rustling4
    scene sm1cs-am007-a115-1 mc-am-lick-anim-01 with dissolve
    pause
    scene sm1cs_am007-a115-1
    play voisex3 girl22_sex_licking
    play voisex2 mc_sex_openmoans1
    play sound sfx_handjob_cream1 loop
    am "*hungry licking*"
    pause
    scene sm1cs_am007-a115-2 with dissolve
    mct "April's not wasting any time."
    pause
    scene sm1cs_am007-a115-3 with dissolve
    am "Lpppfff.... likkaah..."
    pause
    scene sm1cs_am007-a115-1-f with dissolve
    mc "Mmm."
    pause
    scene sm1cs_am007-a115-2-f with dissolve
    pause
    mc "This is so hot, April."
    scene sm1cs_am007-a115-3-f with dissolve
    mct "When her switch goes off, she's a real wild thang."
    pause
    stop voisex2 fadeout 1.0
    play voisex3 girl22_sex_closedmoan4 noloop
    stop sound fadeout 1.0
    scene sm1cs-am007-117 mc-am-look_c2 with dissolve
    am "Ahuaah..."
    am "You're so smelly right now."
    am "Like an animal..."
    scene sm1cs-am007-117 mc-am-look_c1 with dissolve
    play voisex2 mc_yes_yeah1 noloop
    mc "Yeah..."
    scene sm1cs-am007-117 mc-am-look_c2 with dissolve
    play voisex3 girl22_surprised_eh1 noloop
    am "Can I... lick your armpits?"
    menu:
        "So long as I can lick yours":
            $ player.set_choice("sm1cs_am007_lick_armpits_both")
            play sound sfx_cloth_rustling1
            scene sm1cs-am007-118 mc-am-lick_c1 with dissolve
            play voisex2 d9s2_mcyes noloop volume 1.6
            mc "So long as I can do the same to you."
        "I'd prefer to just lick yours":
            $ player.set_choice("sm1cs_am007_lick_armpits_am")
            play sound sfx_cloth_rustling1
            scene sm1cs-am007-124 mc-am-look_c1 with dissolve
            play voice2 mc_no_no5 noloop
            mc "I'd prefer to just lick yours, April."
            play voice3 girl22_yes_yep4 noloop
            am "Okay. That's fine."
        "I'd like to do other things to you":
            $ player.set_choice("sm1cs_am007_no_lick_armpits")
            play sound sfx_cloth_rustling1
            scene sm1cs-am007-124 mc-am-look_c1 with dissolve
            play voice2 mc_no_no5 noloop
            mc "I have other things in mind, April."
            scene sm1cs-am007-124 mc-am-look_c2 with dissolve
            play voice3 girl22_yes_yep4 noloop
            am "Okay."
    if player.get_choice("sm1cs_am007_lick_armpits_both"):
        scene sm1cs-am007-118 mc-am-lick_c2 with dissolve
        play voisex3 girl22_sex_sucking1
        play voisex2 mc_sex_openmoans1
        am "Mrmmm..."
        am "*sniffing*"
        am "Gawd..."
        play voisex2 mc_thinking_hmm1 noloop
        stop voisex3 fadeout 1.0
        scene sm1cs-am007-120 mc-am-lick3_c1 with dissolve
        mc "My turn..."
        scene sm1cs-am007-121 mc-am-lick4_c1 with dissolve
        play sound mc_sex_sucking_slow1 loop
        play voisex2 mc_sex_closedmoans1
        play voisex3 girl22_sexphrase_yes noloop
        queue voisex3 girl22_sex_openmoans1
        am "Yes..."
        am "Oh fuck."
        am "Your tongue..."
        am "That's it. I like it so much."
        scene sm1cs-am007-124 mc-am-look_c2 with dissolve
    elif player.get_choice("sm1cs_am007_lick_armpits_am"):
        scene sm1cs-am007-121 mc-am-lick4_c1 with dissolve
        play sound mc_sex_sucking_slow1 loop
        play voisex2 mc_sex_closedmoans1
        play voisex3 girl22_sex_openmoans1
        pause
        scene sm1cs-am007-124 mc-am-look_c2 with dissolve
    else:
        scene sm1cs-am007-124 mc-am-look_c2 with dissolve
        pause
    stop voisex2 fadeout 1.0
    stop sound fadeout 1.0
    play voisex3 girl22_angry_breathing noloop
    am "*heavy breathing*"
    scene sm1cs-am007-125 mc-am-kiss_c1 with dissolve
    play sound mc_sex_sucking_slow2 loop
    play voisex2 mc_sex_closedmoans1
    play voisex3 girl22_sex_openmoans1
    am "Mrraa-hffah..."
    am "Ahuaah. [mcname]."
    scene sm1cs-am007-126 mc-am-lick_c1 with dissolve
    play sound mc_sex_sucking_slow1 loop
    mc "Too much?"
    scene sm1cs-am007-126 mc-am-lick_c2 with dissolve
    am "*sighing* Just... a little..."
    am "It's starting to feel better now."
    stop voisex2 fadeout 1.0
    stop sound fadeout 1.0
    scene sm1cs-am007-127 mc-am-close_c2 with dissolve
    play voisex3 girl22_sex_closedmoan3 noloop
    am "I want to feel your cock..."
    am "Between my breasts."
    play sound2 sfx_cloth_rustling2 noloop
    scene sm1cs-am007-a130-1 mc-am-titjob-anim-01 with dissolve
    pause
    scene sm1cs_am007-a130-1
    play voisex2 mc_sex_openmoans1
    play voisex3 girl22_sex_openmoans1
    play sound sfx_handjob_cream1 loop
    am "It's getting so warm."
    am "Stroke your cock with my tits, [mcname]!"
    pause
    scene sm1cs_am007-a130-2 with dissolve
    am "I'm a bad girl. Seeing how hard I make you makes me so fucking wet!"
    mc "Your tits feel great, April."
    pause
    scene sm1cs_am007-a130-3 with dissolve
    mc "Your whole body looks perfect for this kind of thing."
    am "*happy moaning*"
    pause
    play sound sfx_biologic_spit1
    stop voisex2 fadeout 1.0
    stop voisex3 fadeout 1.0
    scene sm1cs-am007-131 mc-am-spit_c2 with dissolve
    am "Muaah..."
    scene sm1cs-am007-132 mc-am-look_c2 with dissolve
    play voisex3 girl22_yes_aga5 noloop
    am "I think I'm ready..."
    scene sm1cs-am007-133 mc-am-tip_c1 with dissolve
    play voisex2 mc_yes_yeah8 noloop
    mc "Yeah?"
    am "Mmhmm."
    scene sm1cs_am007-a130-1-f with dissolve
    play voisex3 girl22_sex_closedmoans1
    play sound mc_sex_sucking_fast2 loop
    play voisex2 mc_sex_openmoans2
    am "Glrrph..."
    pause
    scene sm1cs_am007-a130-2-f with dissolve
    am "Glrurrrp...{w} Plurrph...{w}"
    pause
    scene sm1cs_am007-a130-3-f with dissolve
    am "Gallphh..."
    pause
    stop sound fadeout 1.0
    stop voisex2 fadeout 1.0
    scene sm1cs-am007-136 mc-am-ask_c2 with dissolve
    play voisex3 girl22_happy_relief noloop
    am "Awwahhhh!"
    am "I want to feel it inside."
    scene sm1cs-am007-137 mc-am-talk_c1 with dissolve
    play voice2 mc_surprised_wow2 noloop
    mc "I didn't think you wanted our first time to be something crazy like this."
    scene sm1cs-am007-137 mc-am-talk_c2 with dissolve
    play voice3 girl22_surprised_huh1 noloop
    am "I'm not allowed to be wrong some times?"
    play voice2 mc_no_no2 noloop
    mc "Of course you are. I just didn't expect it."
    scene sm1cs-am007-138 mc-am-talk2_c1 with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "Are you going to fuck me or not?"
    mc "..."
    scene sm1cs-am007-138 mc-am-talk2_c2 with dissolve
    play voice3 girl22_arrogant_huh noloop
    am "Seriously?"
    play sound sfx_cloth_rustling1
    scene sm1cs-am007-139 mc-am-stand_c1 with dissolve
    mct "Time to activate beast mode."
    play voice2 mc_angry_errr2 noloop
    mc "Fuck you. I'm going to fuck you."
    scene sm1cs-am007-139 mc-am-stand_c2 with dissolve
    play voice3 girl22_arrogant_ha noloop
    am "You hesitated!"
    play sound sfx_cloth_rustling3
    scene sm1cs-am007-140 mc-am-touch_c1 with dissolve
    play voice2 mc_no_nope2 noloop
    mc "I was thinking of a funny story."
    scene sm1cs-am007-140 mc-am-touch_c2 with dissolve
    play voice3 girl22_yes_yeah3 noloop
    am "Oh yeah? Tell me-"
    scene sm1cs-am007-141 mc-am-kiss_c1 with dissolve
    play voice3 girl22_sex_closedmoan2 noloop
    play voice2 mc_angry_errr8 noloop
    play sound dahlia_kiss_french1
    am "Mrmmm..."
    scene sm1cs-am007-142 mc-am-look_c2 with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "Cheater."
    scene sm1cs-am007-143 mc-am-look2_c1 with dissolve
    play voice2 mc_angry_off noloop
    mc "Shut up and turn around."
    play voice3 girl22_yes_aga11 noloop
    am "Mmmmuh...."
    play sound sfx_fisting_fist2
    scene sm1cs-am007-144 mc-am-wall_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "You're a bad girl, aren't you."
    scene sm1cs-am007-144 mc-am-wall_c2 with dissolve
    play voice3 girl22_happy_laugh1 noloop
    am "I try not to be."
    scene sm1cs-am007-145 mc-am-wall2_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "You kind of suck at it."
    scene sm1cs-am007-145 mc-am-wall2_c2 with dissolve
    play voisex3 girl22_sex_openmoans1
    play sound sfx_handjob_cream1 loop
    am "*light moaning* The world made me like this."
    play voisex2 mc_thinking_hmm9 noloop
    mc "Then I have the world to thank."
    am "*moaning*"
    am "Please don't make me wait any more, [mcname]."
    scene sm1cs-am007-a146-1 mc-am-standing-behind-anim-01 with dissolve
    pause
    scene sm1cs_am007-a146-1
    play sound sfx_vagina_penetration1_fast loop
    play voisex2 mc_sex_openmoans2
    play voisex3 girl22_sex_openmoans2
    am "Oh fuck!"
    am "It's so big."
    pause
    scene sm1cs_am007-a146-2 with dissolve
    am "Fuck... Fuck me! Fuck my pussy!"
    am "I love it."
    pause
    scene sm1cs_am007-a146-3 with dissolve
    am "Give me every inch, [mcname]!"
    am "Owuaha..."
    am "Fuuhhhaaak."
    pause
    scene sm1cs_am007-a146-4 with dissolve
    am "I'm getting close."
    mc "Me too."
    pause
    scene sm1cs_am007-a146-1-f with dissolve
    am "Mrrrrm-hmmm..."
    am "Awhuaah..."
    pause
    scene sm1cs_am007-a146-2-f with dissolve
    am "I'm cumming."
    am "Ahu-huaaaah!"
    pause
    scene sm1cs_am007-a146-3-f with dissolve
    mc "April. I'm getting close."
    am "Don't stop-huaah!... *moaning*"
    pause
    scene sm1cs_am007-a146-4-f with dissolve
    am "I want it!{w} I want to feel your jizz fucking up my hole. *moans* "
    pause
    play voisex2 mc_sex_orgasm2 noloop
    play sound mc_cum_sound1
    play voisex3 girl22_sex_orgasm1 noloop
    scene sm1cs-am007-150 mc-am-cum_c2 with hpunch
    am "Phuaah... phew..."
    play sound mc_cum_sound1
    queue voisex2 mc_sex_orgasm1 noloop
    scene sm1cs-am007-150 mc-am-cum_c1 with hpunch
    pause
    stop voisex2 fadeout 1.5
    scene sm1cs-am007-151 mc-am-cum2_c1 with dissolve
    play voisex3 girl22_sex_closedmoan1 noloop
    am "Mrraaah... so much cum."
    am "You really creampied me..."
    scene sm1cs-am007-151 mc-am-cum2_c2 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah. I should have asked earlier."
    mc "I got a little crazy there at the end."
    play sound sfx_sex_fingering_fast1 loop volume 0.5
    scene sm1cs-am007-152 mc-am-cum3_c1 with dissolve
    play voice3 girl22_no_nonono1 noloop
    am "It's alright. I wanted to feel you cum inside me."
    scene sm1cs-am007-152 mc-am-cum3_c2 with dissolve
    play voice3 girl22_angry_breathing noloop
    am "In the heat of the moment, it felt wasteful to ask you to pull out."
    scene sm1cs-am007-152 mc-am-cum3_c3 with dissolve
    play voice2 d1s2_hmm noloop volume 1.4
    mc "So you enjoy a good creampie?"
    stop sound fadeout 1.0
    scene sm1cs-am007-153 mc-am-look_c2 with dissolve
    play voice3 girl22_yes_yep5 noloop
    am "I guess so."
    am "There is something so... animalistic about a man spilling his load inside a woman..."
    am "I really wanted to try it."
    scene sm1cs-am007-154 mc-am-talk_c1 with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Happy to help."
    mc "We should try to clean up a little and get our clothes back on."
    mc "Aynone standing near this building might have heard us."
    play sound sfx_tap_water1 loop
    scene sm1cs-am007-155 mc-am-talk2_c2 with dissolve
    play voice3 girl22_yes_aga4 noloop
    am "Mmhmm."
    scene sm1cs-am007-156 mc-am-dress_c1 with dissolve
    pause
    play sound2 sfx_skirt_off2 noloop
    scene sm1cs-am007-156 mc-am-dress_c2 with dissolve
    pause
    stop sound fadeout 1.0
    play sound2 sfx_door_openclosed1 noloop
    play sound4 sfx_parkday_birds fadein 1.5
    scene sm1cs-am007-159 mc-am-walk_c2 with dissolve
    queue sound sfx_heels_steps1 loop
    queue sound2 sfx_heels_steps2
    play voice3 girl22_sex_closedmoan1 noloop
    am "Thank you for that, [mcname]."
    am "I still have some shit to figure out with my band and work."
    am "But at least I got an extra {b}load{/b} of endorphins to help keep my head on straight."
    scene sm1cs-am007-160 mc-am-walk2_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah but... you know we're doing more than just hooking up, April."
    scene sm1cs-am007-160 mc-am-walk2_c2 with dissolve
    play voice3 girl22_yes_simple noloop
    am "I know. Which makes you a pretty good boyfriend."
    am "Helping to fuck his girlfriend nice and hard when she's struggling."
    am "I like...{w} I really like you, [mcname]."
    am "You understand me, and you know how to put up with my quirks."
    scene sm1cs-am007-161 mc-am-walk3_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I like you too, April."
    mc "I never imagined I'd meet someone like you when I came to Orbix."
    mc "I thought I was just going to meet people like I met at the-"
    scene sm1cs-am007-161 mc-am-walk3_c2 with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Oh shit."
    mct "This is why I should stop talking after sex."
    mct "I almost said \"at Fetish Locator parties\""
    mct "Nothing good ever comes out of pillow talk."
    scene sm1cs-am007-162 mc-am-walk4_c2 with dissolve
    play voice3 girl22_surprised_eh2 noloop
    am "People you met where?"
    scene sm1cs-am007-165 mc-am-walk7_c1 with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Oh like. People I met in computer classes during college."
    mc "You're unlike any of them. {w} One of a kind."
    scene sm1cs-am007-165 mc-am-walk7_c2 with dissolve
    play voice3 girl22_arrogant_he noloop
    am "Well, You don't need to feed my ego too much."
    am "I'm still floating on cloud nine after you filled me up."
    play voice3 girl22_happy_laugh3 noloop
    am "*giggles*"
    scene sm1cs-am007-166 mc-am-walk8_c2 with dissolve
    play voice3 girl22_thinking_eeh noloop
    am "I need to get going."
    am "I should make up some of the work I didn't do because of the call with Pepper and Mitch."
    play sound sfx_cloth_rustling2
    stop sound2 fadeout 1.0
    scene sm1cs-am007-167 mc-am-close_c1 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Good plan."
    scene sm1cs-am007-168 mc-am-kiss_c1 with dissolve
    play voice3 girl22_sex_closedmoan5 noloop
    play voice2 mc_thinking_mmm1 noloop
    play sound dahlia_kiss_french1
    am "*happy humming*"
    scene sm1cs-am007-168 mc-am-kiss_c2 with dissolve
    queue sound mc_kiss2
    pause
    play sound2 sfx_heels_steps2
    scene sm1cs-am007-169 mc-am-walk_c2 with dissolve
    play voice3 girl22_hey_attention noloop
    am "I'll talk to you later, [mcname]."
    scene sm1cs-am007-169 mc-am-walk_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Count on it."
    stop sound2 fadeout 2.5
    scene sm1cs-am007-170 mc-am-thought_c1 with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Shit."
    mct "I shouldn't have lied to April."
    scene sm1cs-am007-170-2 mc-am-thought2_c1 with dissolve
    play voice2 d14s16_smell noloop
    mct "It's a bit screwed up. I shouldn't get invovled with anyone without telling them why I came to Orbix in the first place."
    mct "But this wasn't the right time."
    scene sm1cs-am007-171 mc-am-thought3_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Yeah. That's it..."
    mct "I'll tell her in due time."
    mct "It will be fine.{w} I {b}know{/b} April will understand..."
    jump sm1cs_am007_end_scene
label sm1cs_am007_end_scene:
    stop sound4 fadeout 1.0
    stop sound5 fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(AM_STORY, 3, 0, 3)
    return