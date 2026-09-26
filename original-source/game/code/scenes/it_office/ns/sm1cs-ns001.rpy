image sm1cs_ns001-glambot-1 = Movie(play = "images/FS_IT/NS/s001/anim/sm1cs-ns001-a11-2x-50fps.webm", start_image = "sm1cs-ns001-a11 ns-talk-ag-glambot-11-000_i", image = "sm1cs-ns001-a11 ns-talk-ag-glambot-11-119_i", loop = False)
label sm1cs_ns001:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1cs-ns001-01-mc-office with dissolve
    play sound sfx_mouse_clicks1
    pause
    play music music_chilled_fun
    stop sound fadeout 1.0
    scene sm1cs-ns001-02-ns-talk-mc with dissolve
    play voice3 nari_hey_high noloop
    ns "I'm hungry."
    scene sm1cs-ns001-03-mc-talk-ns with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Uh yeah. You should fix that issue."
    scene sm1cs-ns001-04-ns-talk-mc with dissolve
    play voice3 nari_yes_emotional noloop
    ns "Yes. That is why I'm coming to you. I think I can ask Anna, but there is no clear definition in the employee handbook if I can bother a superior about something like this."
    play sound sfx_chair_slide1
    scene sm1cs-ns001-05-mc-talk-ns with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I'm sure she won't mind."
    scene sm1cs-ns001-06-mc-talk-ag with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey Anna. Nari and I were looking for some food. Is there anything close around here?"
    scene sm1cs-ns001-07-ag-talk-mc with dissolve
    play voice4 girl27_yes_yeah6 noloop
    ag "Of course. The office has it's own cafeteria."
    scene sm1cs-ns001-08-ag-talk-mc with dissolve
    play voice4 girl27_thinking_hmm3 noloop
    ag "Just take that hallway and watch for the signs. You can't miss it."
    scene sm1cs-ns001-09-mc-talk-ag with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Thanks. Care to join us, Anna?"
    scene sm1cs-ns001-10-ag-talk-mc with dissolve
    play voice4 girl27_thinking_emm noloop
    ag "Thank you, but maybe next time. Claire wants me to make sure the materials are prepared for our new client pitch. You two have a good time."
    play sound ["<silence 1.0>", sfx_camera_fly1] volume 2.0
    scene sm1cs_ns001-glambot-1 with dissolve
    pause
    play voice3 nari_thinking_oh noloop
    ns "Oh. Yes. Thank you very much, Anna."
    stop sound fadeout 1.0
    stop sound2 fadeout 2.0
    jump sm1cs_ns001_cafeteria
label sm1cs_ns001_cafeteria:
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound3 sfx_cafe_crowd
    scene sm1cs-ns001-12-office-cafeteria with fade
    pause
    scene sm1cs-ns001-13-ns-talk-mc with dissolve
    play voice3 nari_happy_phew noloop
    ns "I'm glad you joined me. I was... apprehensive about leaving the office for lunch."
    scene sm1cs-ns001-14-mc-talk-ns with dissolve
    play voice2 d1s2_hmm noloop volume 2.0
    mc "Why is that?"
    play sound sfx_cloth_rustling1
    scene sm1cs-ns001-15-ns-talk-mc with dissolve
    play voice3 nari_thinking_hmm3 noloop
    ns "Anna has told me she doesn't want to see me at my desk during our breaks anymore."
    ns "I know I shouldn't continue working, but sometimes, I can't stop myself from figuring out one more problem."
    scene sm1cs-ns001-16-ns-talk-mc with dissolve
    play voice3 nari_disappointed_mff noloop
    ns "I love digging into the next problem. And when I finally unlock the solution, it's all I can do not to open up the next batch of code."
    scene sm1cs-ns001-17-ns-talk-mc with dissolve
    play voice3 nari_disappointed_eh noloop
    ns "But I don't want Anna to feel like I'm just some workaholic, or that I'm crazy, or that I don't respect her wishes."
    scene sm1cs-ns001-18-mc-talk-ns with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Ah so you're okay if I think that about you."
    scene sm1cs-ns001-19-ns-talk-mc with dissolve
    play voice3 nari_yes_questioning noloop
    ns "Yes. No. I mean. I-"
    scene sm1cs-ns001-20-mc-talk-ns with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Relax. I was just teasing you."
    scene sm1cs-ns001-21-ns-talk-mc with dissolve
    play voice3 nari_disappointed_oh noloop
    ns "Oh."
    ns "Right."
    scene sm1cs-ns001-22-ns-talk-mc with dissolve
    play voice3 nari_thinking_hm noloop
    ns "Will this work?"
    scene sm1cs-ns001-23-mc-talk-ns with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Perfect."
    play sound sfx_paper_bag_1
    scene sm1cs-ns001-24-ns-mc-sits with dissolve
    stop sound fadeout 3.0
    pause
    scene sm1cs-ns001-25-ns-talk-mc with dissolve
    play voice3 nari_disappointed_eeh noloop
    ns "No offense [mcname], but you're kind of weird. You're not like other coders I've met."
    scene sm1cs-ns001-26-mc-talk-ns with dissolve
    play voice2 d1s5_mchappy noloop volume 2.0
    mc "I get that. Probably because I wasn't super into it earlier."
    scene sm1cs-ns001-27-ns-talk-mc with dissolve
    play voice3 nari_arrogant_huh noloop
    ns "What were you into before?"
    scene sm1cs-ns001-28-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop
    mct "Don't say sex. Don't say sex."
    scene sm1cs-ns001-29-mc-talk-ns with dissolve
    play voice2 mc_thinking_hmm4 noloop volume 1.4
    mc "Just a lot of this and that. I was working on a business degree at college, and then my life got twisted upside down."
    scene sm1cs-ns001-30-ns-talk-mc with dissolve
    play voice3 nari_surprised_huh2 noloop
    ns "That must have been painful. Were you in a car crash?"
    scene sm1cs-ns001-31-mc-talk-ns with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, my life changed a lot in the last couple of months and what I thought I wanted to do just didn't hold my interest any more."
    mc "I made some mistakes, but I survived and now I'm just doing my own thing and taking it one day at a time."
    scene sm1cs-ns001-32-ns-talk-mc with dissolve
    play voice3 nari_thinking_hmm2 noloop
    ns "That sounds very adventurous."
    scene sm1cs-ns001-29-mc-talk-ns with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Maybe. It's nothing like leaving your home and starting somewhere brand new."
    menu:
        "Ask Nari about leaving home"(hint="sm1cs_ns001_m01_h01"):
            call sm1cs_ns001_m01_c01 from _call_sm1cs_ns001_m01_c01
            mc "So can I ask why you left Korea?"
            scene sm1cs-ns001-33-c1-ns-talk-mc with dissolve
            play voice3 nari_thinking_emm noloop
            ns "Since I was a little girl, my choices were not really my own. Everything was prepared and planned out for me."
            scene sm1cs-ns001-34-c1-ns-talk-mc with dissolve
            play voice3 nari_thinking_hmm1 noloop
            ns "I was happy. But it felt like a \"strange\" happy. Like a soldier who is \"happy\" to serve their country. Not the \"happy\" I saw in TV shows and movies."
            scene sm1cs-ns001-35-c1-ns-talk-mc with dissolve
            ns "I wanted more, so I committed myself to exploring what else this world has to offer."
            ns "I couldn't think of a better place to start than this melting pot. And now I'm really glad I did."
            scene sm1cs-ns001-36-c1-mc-talk-ns with dissolve
            play voice2 mc_surprised_wow3 noloop
            mc "Life is what you make it. It's really impressive that you pushed yourself to try out a new path."
            scene sm1cs-ns001-37-c1-ns-talk-mc with dissolve
            play voice3 nari_yes_sad noloop
            ns "Yes. It's funny. We have more in common than I imagined."
            jump sm1cs_ns001_menu
        "Continue"(hint="sm1cs_ns001_m01_h02"):
            jump sm1cs_ns001_continue
label sm1cs_ns001_menu:
    menu:
        "Compliment her achievement"(hint="sm1cs_ns001_m02_h01"):
            call sm1cs_ns001_m02_c01 from _call_sm1cs_ns001_m02_c01
            scene sm1cs-ns001-38-c1-c1-mc-talk-ns with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "Heh. You are the true talent here, Nari. I didn't give up anything on the scale of what you did."
            scene sm1cs-ns001-39-c1-c1-ns-talk-mc with dissolve
            play voice3 nari_no_nah noloop
            ns "You're too kind. But I prefer to think of it as just... expanding my horizons."
            ns "I just hope my family will see it the same way."
        "Be humble"(hint="sm1cs_ns001_m02_h02"):
            scene sm1cs-ns001-40-c1-c2-mc-talk-ns with dissolve
            play voice2 d2s9_confused noloop volume 1.7
            mc "Changing majors is not like changing the country you live in."
            scene sm1cs-ns001-41-c1-c2-ns-talk-mc with dissolve
            play voice3 nari_no_nah noloop
            ns "A risk is a risk, no matter the size."
            mc "Hmmm."
    jump sm1cs_ns001_continue
label sm1cs_ns001_continue:
    scene sm1cs-ns001-42-ns-mc with fade
    pause
    scene sm1cs-ns001-43-mc-inner-talk with dissolve
    play voice2 mc_eating_mmm noloop
    mct "That sandwich was pretty solid. I'll have to try the stew next time."
    scene sm1cs-ns001-44-mc-talk-ns with dissolve
    play voice2 d2s9_mchey noloop volume 1.5
    mc "All good? Let me take your plate."
    scene sm1cs-ns001-45-ns-talk-mc with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Oh. Thanks."
    play sound sfx_paper_rustl3 volume 1.6
    scene sm1cs-ns001-46-mc-prepare with dissolve
    pause
    scene sm1cs-ns001-47-mc-inner-talk with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mct "He shoots"
    play sound sfx_throw_something1 volume 1.5
    scene sm1cs-ns001-48-trash with dissolve
    pause
    play sound sfx_paper_trash_throw1
    scene sm1cs-ns001-49-trash-in with dissolve
    pause
    scene sm1cs-ns001-50-mc-inner-talk with dissolve
    play voice2 mc_happy_yes1 noloop
    mct "He scores!"
    scene sm1cs-ns001-51-ns-talk-mc with dissolve
    play voice3 nari_happy_relief noloop
    ns "You're really easy to talk to, [mcname]. I feel like I can talk to you about anything."
    scene sm1cs-ns001-52-ns-talk-mc with dissolve
    play voice3 nari_happy_mmm noloop
    ns "If you are ever struggling with an area of your coding, please don't hesitate to come to me."
    scene sm1cs-ns001-53-mc-talk-ns with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Great."
    scene sm1cs-ns001-54-mc-talk-ns with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "What is wrong with my coding?"
    scene sm1cs-ns001-55-ns-talk-mc with dissolve
    play voice3 nari_arrogant_heh noloop
    ns "Forgive me if I am being too forward. I noticed your coding is lacking in... several areas."
    ns "I am so sorry. It's not my job to critique you."
    scene sm1cs-ns001-56-mc-talk-ns with dissolve
    play voice2 mc_no_nono1 noloop
    mc "It's fine. I knew I wasn't a pro, but I didn't realize it was that bad."
    scene sm1cs-ns001-57-ns-talk-mc with dissolve
    play voice3 nari_yes_yep noloop
    ns "It really is. But I can help you."
    scene sm1cs-ns001-58-mc-talk-ns with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "That's a kind offer, Nari. But why would you do that?"
    scene sm1cs-ns001-59-ns-talk-mc with dissolve
    play voice3 nari_disappointed_huh noloop
    ns "You have a very rugged determination about you, [mcname]. I think that the thing holding you back is simply a lack of knowledge."
    ns "You deserve whatever assistance I can give you."
    scene sm1cs-ns001-60-mc-talk-ns with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "If it won't interfere with your work?"
    scene sm1cs-ns001-61-ns-talk-mc with dissolve
    play voice3 nari_no_uhuh noloop
    ns "It will not. So far, there hasn't been any part of our tasks that has provided me with even a hint of difficulty."
    play sound sfx_bed_slide2
    scene sm1cs-ns001-62-ns-talk-mc with dissolve
    play voice3 nari_hey_unsure noloop
    ns "Can I tell you a secret?"
    scene sm1cs-ns001-63-mc-talk-ns with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    scene sm1cs-ns001-64-ns-talk-mc with dissolve
    play voice3 nari_surprised_ehh noloop
    ns "I caught April looking over my shoulder earlier. I was so embarrassed. I thought I had done something wrong or said something wrong."
    scene sm1cs-ns001-65-ns-talk-mc with dissolve
    play voice3 nari_happy_laugh1 noloop
    ns "Later on, I realized she must have been really impressed by my work because she asked me if I wanted a Soda.."
    ns "It's by far the strangest thing she's done to me since we met. We still haven't really spoken, but it felt like a great step between us."
    scene sm1cs-ns001-66-mc-talk-ns with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Totally. She never offered to get me a soda."
    scene sm1cs-ns001-67-ns-talk-mc with dissolve
    play voice3 nari_thinking_mff noloop
    ns "There is always hope. I was just super glad because things have been a bit awkward between us."
    scene sm1cs-ns001-68-mc-talk-ns with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Oh really? I hadn't noticed. What happened?"
    scene sm1cs-ns001-69-ns-talk-mc with dissolve
    play voice3 nari_disappointed_oh noloop
    ns "Oh. I... well it was just a mistake on my part. We were talking about our interests, and I told her that I prefer anal to vaginal."
    play sound sfx_bed_slide3 volume 0.6
    scene sm1cs-ns001-70-mc-talk-ns with dissolve
    play voice2 mc_surprised_what1 noloop
    call sm1cs_ns001_dicover_trait_anal from _call_sm1cs_ns001_dicover_trait_anal
    mc "Wait. You said that?"
    scene sm1cs-ns001-71-ns-talk-mc with dissolve
    play voice3 nari_yes_confident noloop
    ns "Yes. I mean, I was just sharing something with her. It was my belief that people here are cool with sex, but April was stunned silent."
    scene sm1cs-ns001-72-mc-talk-ns with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Well, I think it's really about who you're talking to, Nari."
    mc "Or maybe you just blind-sided her and she didn't know what to say. I definitely wasn't expecting you to drop that right in the middle of the office."
    scene sm1cs-ns001-73-ns-talk-mc with dissolve
    play voice3 nari_surprised_huh1 noloop
    ns "Am I going to get in trouble? I apologized to her a bunch, but she never said she accepted any of them."
    scene sm1cs-ns001-74-mc-talk-ns with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Just take a deep breath, Nari. I wouldn't worry about it. If you didn't get in trouble already, April probably just didn't report it."
    scene sm1cs-ns001-75-ns-talk-mc with dissolve
    play voice3 nari_happy_phew noloop
    ns "Phew."
    scene sm1cs-ns001-76-ns-talk-mc with dissolve
    play voice3 nari_disappointed_eh noloop
    ns "Oh. I see your point. And I. I just wanted to say thanks. Thank you for not freaking out or reacting the same way April did."
    scene sm1cs-ns001-77-ns-talk-mc with dissolve
    play voice3 nari_sex_closedmoan1 noloop
    ns "I can't afford to lose my position there."
    ns "And the worst part is that I'm still lost. If you're making a friend, you share what you're into. Right?"
    scene sm1cs-ns001-78-mc-talk-ns with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Well, some people are uncomfortable talking about sex and uh... personal preferences in certain areas."
    scene sm1cs-ns001-79-ns-talk-mc with dissolve
    play voice3 nari_thinking_hmm3 noloop
    ns "But... you are not one of these people. Correct?"
    scene sm1cs-ns001-80-mc-talk-ns with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "You've got me there. I suppose there is no harm in talking about private things to the right person, but I wouldn't bring it up in a team meeting."
    play sound sfx_cup_slide1
    scene sm1cs-ns001-81-ns-mc with dissolve
    pause
    scene sm1cs-ns001-82-ns-talk-mc with dissolve
    play voice3 nari_hey_calm noloop
    ns "[mcname]. Can I ask you something?"
    scene sm1cs-ns001-83-mc-talk-ns with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Go for it."
    scene sm1cs-ns001-84-ns-talk-mc with dissolve
    play voice3 nari_disappointed_eeh noloop
    ns "Do you think you could help me make sure I don't make a fool of myself at the office?"
    ns "I will endeavor to only talk about naughty things if someone else talks about them."
    scene sm1cs-ns001-85-ns-talk-mc with dissolve
    play voice3 nari_disappointed_mff noloop
    ns "But... sometimes I get excited, or I might misread something again. So... what do you say?"
    scene sm1cs-ns001-86-mc-talk-ns with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure. I can watch out for you if you want. And if you have any other questions, just reach out."
    scene sm1cs-ns001-87-ns-talk-mc with dissolve
    play voice3 nari_yes_yeah noloop
    ns "You have my thanks, [mcname]. I am sure I can manage fairly well on my own, but if I could rely on you, that would mean a great deal."
    ns "Shall we go back to the office?"
    scene sm1cs-ns001-88-mc-talk-ns with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Let's."
    play sound sfx_heels_steps1
    scene sm1cs-ns001-89-ns-talk-mc with dissolve
    play voice3 nari_thinking_hmm2 noloop
    ns "Remind me to give you my number before we leave today."
    scene sm1cs-ns001-90-mc-talk-ns with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Absolutely."
    scene sm1cs-ns001-91-ns-talk-mc with dissolve
    play voice3 nari_arrogant_hm noloop
    ns "Great."
    stop sound fadeout 1.0
    stop sound3 fadeout 3.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(NS_STORY, 0, 30, 2)
    return
label sm1cs_ns001_m01_c01:
    $ player.set_choice("sm1cs_ns001_leaving_home")
    return
label sm1cs_ns001_m02_c01:
    $ player.set_choice("sm1cs_ns001_compliment")
    $ CharacterController.get_character("ns").add_point()
    return
label sm1cs_ns001_dicover_trait_anal:
    $ CharacterController.get_character("ns").discover_trait(ANAL)
    return
label sm1cs_ns001_unlocks:
    call sm1cs_ns001_m01_c01 from _call_sm1cs_ns001_m01_c01_1
    call sm1cs_ns001_m02_c01 from _call_sm1cs_ns001_m02_c01_1
    call sm1cs_ns001_dicover_trait_anal from _call_sm1cs_ns001_dicover_trait_anal_1
    if config_storyline_mode is True:
        $ execute_storyline_config(NS_STORY)
    return