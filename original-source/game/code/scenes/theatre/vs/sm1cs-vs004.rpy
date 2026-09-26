image sm1cs_vs004-a74-glambot = Movie(play = "images/FS_T/VS/s004/anim/sm1cs-vs004-a74-2x-50fps.webm", start_image = "sm1cs-vs004-a74 vs-kiss-glambot-00_i", image = "sm1cs-vs004-a74 vs-kiss-glambot-80_i", loop = False)
label sm1cs_vs004:
    $ renpy.music.set_volume(0.8, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound4 sfx_parkday_birds fadein 1.5 volume 0.7
    play music music_nowhere_tobe
    play sound sfx_heels_steps1 loop
    scene sm1cs-vs004-00 a_better_understanding with Fade(0.5, 0.5, 0.5)
    play voice3 girl33_hey_involved noloop
    vs "Hey, hot stuff."
    stop sound fadeout 1.0
    scene sm1cs-vs004-01 a_better_understanding_mc_talk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "That's my line."
    scene sm1cs-vs004-02 a_better_understanding_vs_talk with dissolve
    play voice3 girl33_happy_laugh1 noloop
    vs "Haha."
    scene sm1cs-vs004-03 a_better_understanding_vs_talk_serious with dissolve
    play voice3 girl33_disappointed_off noloop
    vs "Thanks for taking the time to meet up."
    scene sm1cs-vs004-04 a_better_understanding_mc_talk with dissolve
    play voice2 d9s3_no noloop volume 1.7
    mc "No worries."
    menu:
        "Check in on Blitz Alert"(hint="sm1cs_vs004_m01_h01"):
            call sm1cs_vs004_m01_c01 from _call_sm1cs_vs004_m01_c01
            scene sm1cs-vs004-05 a_better_understanding_mc_talk_mischevious with dissolve
            play voice2 d1s2_hmm noloop volume 1.7
            mc "Should I be expecting the Blitz Alert to go off while we're here?"
            mc "I figured you might want to do some outdoor stuff."
            scene sm1cs-vs004-06 a_better_understanding_vs_talk with dissolve
            play voice3 girl33_happy_laugh2 noloop
            vs "Haha. That would be really kinky."
            vs "I've always wanted to do outdoor doggy-style at the dog park."
            scene sm1cs-vs004-07 a_better_understanding_vs_talk_coy with dissolve
            play voice3 girl33_disappointed_oh noloop
            vs "But I think you're safe. The alarm shouldn't go off today."
            play sound sfx_cloth_rustling2
            scene sm1cs-vs004-08 a_better_understanding_vs_talk_lick_lips with dissolve
            play voice3 girl33_happy_mmm noloop
            vs "Or maybe it will. *giggle*"
            scene sm1cs-vs004-09 a_better_understanding_vs_talk with dissolve
            play voice3 girl33_no_uhuh noloop
            vs "I'm not telling."
            scene sm1cs-vs004-10 a_better_understanding_mc_talk with dissolve
            play voice2 d9s2_yeah noloop volume 1.7
            mc "Fair enough."
        "Focus on Kellie"(hint="sm1cs_vs004_m01_h02"):
            pass
    scene sm1cs-vs004-11 a_better_understanding_vs_talk with dissolve
    play voice3 girl33_thinking_eem2 noloop
    vs "Shall we?"
    scene sm1cs-vs004-12 a_better_understanding_mc_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-vs004-13 a_better_understanding_mc_talk_walk with dissolve
    play voice2 mc_thinking_hm noloop
    mc "So what did you want to talk about?"
    scene sm1cs-vs004-14 a_better_understanding_vs_talk_walk with dissolve
    play voice3 girl33_disappointed_aah noloop
    vs "It's Kellie."
    scene sm1cs-vs004-15 a_better_understanding_vs_talk_walk with dissolve
    play voice3 girl33_disappointed_mmf3 noloop
    vs "I can't make heads or tails about what is up with her."
    vs "And normally, I can get people to tell me the reason why they are angry with me pretty easily."
    scene sm1cs-vs004-16 a_better_understanding_vs_talk_walk_fingers with dissolve
    play voice3 girl33_thinking_hmm3 noloop
    vs "If I was late. {w}If my lipstick is too shiny.{w} If my boobs are being too distracting during a test."
    scene sm1cs-vs004-17 a_better_understanding_mc_talk with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "But this time..."
    scene sm1cs-vs004-18 a_better_understanding_vs_talk_exasperated with dissolve
    play voice3 girl33_yes_serious noloop
    vs "This time I can't get anything from her. Kellie won't say what I did to piss her off."
    scene sm1cs-vs004-19 a_better_understanding_vs_talk_thinking with dissolve
    play voice3 girl33_surprised_huh1 noloop
    vs "Wait. Maybe it is because I mentioned that I saw you naked when we saw her naked."
    vs "That could be it. She thinks that we are in a relationship, and she is jealous because she likes you."
    menu:
        "Aren't we in a relationship?"(hint="sm1cs_vs004_m02_h01"):
            call sm1cs_vs004_m02_c01 from _call_sm1cs_vs004_m02_c01
            scene sm1cs-vs004-20 a_better_understanding_mc_talk_switch with dissolve
            play voice2 mc_surprised_uh1 noloop
            mc "Aren't we kind of in a relationship, Veronica?"
            scene sm1cs-vs004-21 a_better_understanding_vs_talk_confused with dissolve
            play voice3 girl33_surprised_huh4 noloop
            vs "Huh? In a..."
            scene sm1cs-vs004-22 a_better_understanding_vs_talk_hair with dissolve
            play voice3 girl33_surprised_why2 noloop
            vs "Why do you say that?"
            scene sm1cs-vs004-23 a_better_understanding_mc_talk with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "I mean, I guess it's just more of a \"friends with benefits\" thing."
            scene sm1cs-vs004-24 a_better_understanding_vs_talk_bubbly with dissolve
            play voice3 girl33_happy_yeah noloop
            vs "Yeah. I mean."
            vs "I do like you. And we have fun together."
            scene sm1cs-vs004-25 a_better_understanding_vs_talk_serious with dissolve
            play voice3 girl33_disappointed_eeh noloop
            vs "But I can't do something serious, [mcname]."
            vs "Not if I'm going to become a big movie star."
            scene sm1cs-vs004-26 a_better_understanding_vs_talk_excited with dissolve
            play voice3 girl33_happy_laugh3 noloop
            vs "I'd have to end up breaking your heart when I moved to Hollywood."
            scene sm1cs-vs004-27 a_better_understanding_mc_talk_chuckles with dissolve
            play voice2 d4s4_mclaugh noloop volume 1.7
            mc "*chuckles* You've given this some thought."
            scene sm1cs-vs004-28 a_better_understanding_vs_talk_smile with dissolve
            play voice3 girl33_yes_yeah noloop
            vs "Well, yeah. Duh-doy."
            stop sound fadeout 1.0
            stop sound2 fadeout 1.0
            scene sm1cs-vs004-29 a_better_understanding_vs_talk_close with dissolve
            play voice3 girl33_happy_relief noloop
            vs "That doesn't mean that I want anything to change, though."
            vs "There is something so exciting about the Blitz Alerts. I wish I was doing them the whole year with you."
            jump sm1cs_vs004_second_choice
        "I don't think that is it"(hint="sm1cs_vs004_m02_h02"):
            stop sound fadeout 1.0
            stop sound2 fadeout 1.0
            scene sm1cs-vs004-33 a_better_understanding_mc_talk_unsure with dissolve
            play voice2 mc_no_no10 noloop
            mc "I don't think that is it."
            play sound sfx_throw_something1
            scene sm1cs-vs004-34 a_better_understanding_vs_talk with dissolve
            play voice3 girl33_surprised_why2 noloop
            vs "Why not?"
            scene sm1cs-vs004-35 a_better_understanding_mc_talk_explaining with dissolve
            play voice2 mc_thinking_mmm4 noloop
            mc "I mean, I think Kellie tolerates me. I'm not sure she likes me."
            mc "And I don't think she's like in love with me or anything like that."
            jump sm1cs_vs004_after_choice
label sm1cs_vs004_second_choice:
    scene sm1cs-vs004-30 a_better_understanding_mc_talk with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Heh. I appreciate that, Veronica."
    menu:
        "Hope for something more"(hint="sm1cs_vs004_m03_h01"):
            call sm1cs_vs004_m03_c01 from _call_sm1cs_vs004_m03_c01
            play voice2 d1s1_mmm noloop volume 1.7
            mct "But I can't ignore the feeling that I want something more with her."
            mct "Some day..."
        "It's good that we cleared that up"(hint="sm1cs_vs004_m03_h02"):
            play voice2 mc_happy_a1 noloop
            mc "Glad we cleared the air about that."
            scene sm1cs-vs004-31 a_better_understanding_vs_talk with dissolve
            play voice3 girl33_yes_happy noloop
            vs "Yeah. Me too."
    scene sm1cs-vs004-32 a_better_understanding_mc_talk_remembers with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "Either way, I don't think Kellie is all worked up about you and me doing naked twister."
    jump sm1cs_vs004_after_choice
label sm1cs_vs004_after_choice:
    mc "In fact, I'm pretty sure Kellie is acting this way because she is jealous of you, Veronica."
    scene sm1cs-vs004-36 a_better_understanding_vs_talk_surprised with dissolve
    play voice3 girl33_surprised_what noloop
    vs "What? Jealous of me?"
    vs "That doesn't make sense. She's probably the most talented member of the cast."
    vs "Taisia does good, but there is no way she's in Kellie's league."
    scene sm1cs-vs004-37 a_better_understanding_mc_talk with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Well, I don't think Kellie shares your opinion."
    mc "She told me that pretty much since you joined the theater, all the lead roles have been going to you."
    play sound sfx_cloth_rustling3
    scene sm1cs-vs004-38 a_better_understanding_mc_talk with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "Kellie is starting to worry that Denise will never give her a lead role because of you."
    scene sm1cs-vs004-39 a_better_understanding_vs_talk_worried with dissolve
    play voice3 girl33_pain_aah2 noloop
    vs "Oh no. That's terrible.{w} I hadn't really thought of it or kept track..."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-vs004-40 a_better_understanding_vs_talk_go_sit with dissolve
    vs "..."
    play sound sfx_cloth_rustling4
    stop sound2 fadeout 1.0
    scene sm1cs-vs004-41 a_better_understanding_vs_talk with dissolve
    play voice3 girl33_disappointed_geh noloop
    vs "I must be pretty self-centered not to notice that she's right."
    vs "I have gotten all the female lead roles since I came here."
    vs "No wonder she doesn't like me."
    vs "[mcname]. You have to help me."
    scene sm1cs-vs004-42 a_better_understanding_mc_talk with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Huh?"
    scene sm1cs-vs004-43 a_better_understanding_vs_talk_worried with dissolve
    play voice3 girl33_angry_argh2 noloop
    vs "I can't stand knowing someone is out there who doesn't like me."
    vs "If I'm going to be a successful star, I need to learn how to be loved by all, or I'll never be in a major blockbuster."
    menu:
        "That sounds like a major headache"(hint="sm1cs_vs004_m04_h01"):
            call sm1cs_vs004_m04_c01 from _call_sm1cs_vs004_m04_c01
            scene sm1cs-vs004-44 a_better_understanding_mc_talk_lose with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "That sounds like a major headache, Veronica."
            mc "You can't expect everyone to like you. Especially if you're a movie star."
            scene sm1cs-vs004-45 a_better_understanding_vs_talk_lose_disappointed with dissolve
            play voice3 girl33_angry_cough noloop
            vs "Well, when you become a movie star, you can do things how you want, [mcname]."
            vs "But I'm going to work super hard and do amazing work so that all my fans adore me."
            vs "And I'm going to start with getting Kellie to like me!"
            scene sm1cs-vs004-46 a_better_understanding_mc_talk_lose_amused with dissolve
            play voice2 mc_yes_okay2 noloop
            mc "If you say so."
        "It's good that you want to fix things with Kellie"(hint="sm1cs_vs004_m04_h02"):
            scene sm1cs-vs004-47 a_better_understanding_mc_talk_good_smile with dissolve
            play voice2 mc_yes_yeah2 noloop
            mc "It's good that you want to fix things up with Kellie."
            mc "Not that you really did anything wrong, or directly attacked her."
            scene sm1cs-vs004-48 a_better_understanding_vs_talk_good with dissolve
            play voice3 girl33_yes_unsure noloop
            vs "I know, but... at least now, I can try to help her out."
            vs "Or something."
    scene sm1cs-vs004-49 a_better_understanding_vs_talk_lookforadvice with dissolve
    play voice3 girl33_thinking_eem1 noloop
    vs "Do you have any ideas on how I should fix things up between us?"
    scene sm1cs-vs004-50 a_better_understanding_mc_talk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I'm not sure. Did she ever invite you to go to the mall or to go see a movie?"
    mc "You could invite her to do something she likes."
    play sound sfx_skirt_off2
    scene sm1cs-vs004-51 a_better_understanding_vs_talk_offbench with dissolve
    play voice3 girl33_disappointed_mmf1 noloop
    vs "*nervous noises*"
    vs "But that's just it. I don't really know what she likes. And it's not like she's going to tell me now."
    vs "Oh, I'm such a terrible person."
    play sound sfx_cloth_rustling2
    scene sm1cs-vs004-52 a_better_understanding_mc_talk_offbench with dissolve
    play voice2 d2s9_mchey noloop volume 1.4
    mc "I could ask her."
    scene sm1cs-vs004-53 a_better_understanding_vs_talk with dissolve
    play voice3 girl33_surprised_huh3 noloop
    vs "Yeah?"
    scene sm1cs-vs004-54 a_better_understanding_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, if she is avoiding you, it might be the best shot."
    mc "I can let her know that you want to hang out."
    scene sm1cs-vs004-55 a_better_understanding_mc_talk_vs_closer with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Mmmmmm."
    mc "How about this?"
    mc "I convince her that Denise wants you and her to work together to create a new acting workshop for the theater."
    scene sm1cs-vs004-56 a_better_understanding_mc_talk_vs_closer with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "If she thinks it's from Denise, she'll agree to it for sure. And it will get you two in the same room."
    mc "And maybe you can describe your style to her and who knows..."
    mc "Maybe she tries some of your tips and tricks and is better prepared for the next audition."
    play sound sfx_throw_something1
    scene sm1cs-vs004-57 a_better_understanding_vs_talk with dissolve
    play voice3 girl33_happy_nice noloop
    vs "That's a great idea."
    vs "But how are you going to get Denise to ask Kellie and I to do a workshop."
    scene sm1cs-vs004-58 a_better_understanding_mc_talk with dissolve
    play voice2 mc_no_no6 noloop
    mc "No uh..."
    mc "Denise isn't actually going to ask you two to work together. But I'm going to convince Kellie that she is."
    scene sm1cs-vs004-59 a_better_understanding_vs_talk with dissolve
    play voice3 girl33_surprised_oh noloop
    vs "Oooooh."
    vs "So you have an idea of how to get Denise to help us out."
    scene sm1cs-vs004-60 a_better_understanding_mc_talk with dissolve
    play voice2 mc_no_no5 noloop
    mc "No, it's-"
    mc "Nevermind. Just... leave it to me."
    scene sm1cs-vs004-61 a_better_understanding_vs_talk_excited with dissolve
    play voice3 girl33_happy_great noloop
    vs "Great. And if this plan doesn't work..."
    vs "I can always just sabotage myself before the audition so that Denise would have to be crazy to pick me."
    scene sm1cs-vs004-62 a_better_understanding_mc_talk_smile with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Let's save that in your pocket. Kellie will probably get more embarrassed if she sees you tanking an audition on purpose."
    scene sm1cs-vs004-63 a_better_understanding_vs_talk_thinking with dissolve
    play voice3 girl33_surprised_wow noloop
    vs "Good thinking, [mcname]. You really are sharp."
    play sound sfx_cloth_rustling1
    scene sm1cs-vs004-64 a_better_understanding_vs_talk_clap with dissolve
    play voice3 girl33_arrogant_hm noloop
    vs "Okay. We've got a plan."
    scene sm1cs-vs004-65 a_better_understanding_vs_talk_hero pose with dissolve
    play voice3 girl33_arrogant_yeah noloop
    vs "Look out Kellie. We're going to be best friends in no time."
    scene sm1cs-vs004-66 a_better_understanding_mc_talk_grinning with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Try not to get too excited. It might not work out."
    scene sm1cs-vs004-67 a_better_understanding_vs_talk_bubbly with dissolve
    play voice3 girl33_no_nah noloop
    vs "I can't help it. Life is always better when you're excited and perky."
    vs "And perky things are the best things."
    vs "Perky music, perky boobs, perky butts. Free perks."
    play voice3 girl33_happy_wooh noloop
    play sound sfx_epic_jump1
    scene sm1cs-vs004-68 a_better_understanding_vs_talk_jump with dissolve
    pause
    play sound sfx_leg_kick8
    scene sm1cs-vs004-69 a_better_understanding_vs_talk_hug with dissolve
    play voice3 girl3_sex_closedmoan1 noloop
    vs "*whispers* Perky things in guy's pants. Wouldn't you agree?"
    play sound sfx_cloth_rustling5
    scene sm1cs-vs004-70 a_better_understanding_mc_talk_hug with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "I suppose you're right about that."
    scene sm1cs-vs004-a74 vs-kiss-glambot-00_i with dissolve
    pause
    scene sm1cs_vs004-a74-glambot
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", mc_kiss2] noloop
    pause
    vs "Mwhaah."
    scene sm1cs-vs004-72 a_better_understanding_vs_talk_look with dissolve
    play voice3 girl33_disappointed_mmf3 noloop
    vs "You're a great guy, [mcname]."
    vs "I really wish the Blitz Alert turned on right now."
    play sound sfx_cloth_rustling4
    scene sm1cs-vs004-73 a_better_understanding_mc_talk_hardlook with dissolve
    pause
    play sound sfx_cloth_rustling1
    scene sm1cs-vs004-74 a_better_understanding_vs_talk_grin_notice with dissolve
    play voice3 girl33_arrogant_laugh noloop
    vs "Woah tiger. Someone is ready to pounce."
    scene sm1cs-vs004-75 a_better_understanding_vs_talk_giggle with dissolve
    play voice3 girl33_happy_laugh5 noloop
    vs "*giggles* I try not to tease, but I will say this."
    vs "When my phone does go off, I'll figure out something really special for us to do."
    scene sm1cs-vs004-76 a_better_understanding_mc_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Looking forward to it, Veronica."
    scene sm1cs-vs004-77 a_better_understanding_vs_talk_rembering with dissolve
    play voice3 girl33_thinking_hmm2 noloop
    vs "Mmhmm. I should get going. My math teacher says if I fail my next exam, I will have to take the class over for some reason."
    vs "I keep telling him when I get successful, I'll just hire an accountant to handle my money."
    scene sm1cs-vs004-78 a_better_understanding_vs_talk_wave with dissolve
    play voice3 girl33_hey_bye1 noloop
    vs "Later, [mcname]."
    scene sm1cs-vs004-79 a_better_understanding_mc_talk_bye with dissolve
    play voice2 mc_hey_bye1 noloop
    mc "Bye Veronica."
    play sound sfx_heels_steps2 loop
    scene sm1cs-vs004-80 a_better_understanding_mc_thought_walkaway with dissolve
    play voice2 d14s16_smell noloop
    mct "Alright. Now, just to figure out how to sell this to Kellie."
    stop sound fadeout 2.0
    stop music fadeout 3.0
    stop sound4 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2")
    jump sm1cs_vs004_end
label sm1cs_vs004_end:
    $ StoryController.end_scene(VS_STORY, 1, 0, 2)
    return
label sm1cs_vs004_m01_c01:
    $ player.set_choice("sm1cs_vs004_check_blitz_alert")
    return
label sm1cs_vs004_m02_c01:
    $ player.set_choice("sm1cs_vs004_vs_relationship")
    return
label sm1cs_vs004_m03_c01:
    $ player.set_choice("sm1cs_vs004_hope_for_more")
    return
label sm1cs_vs004_m04_c01:
    $ player.set_choice("sm1cs_vs004_major_headache")
    $ CharacterController.get_character("vs").deduct_point(2)
    return