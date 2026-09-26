label sm1cs_am001:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1cs-am001-00 first_time_with_april_am_talk with dissolve
    play music music_chiptuned_evil
    play voice3 girl22_hey_simple noloop
    am "Hey. Don't forget, we need to stay late tonight."
    scene sm1cs-am001-01 first_time_with_april_mc_talk with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What for?"
    scene sm1cs-am001-02 first_time_with_april_am_talk_annoyed with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "Anna assigned you to help me with all the code for the client's news website."
    am "Or did you already forget?"
    scene sm1cs-am001-03 first_time_with_april_mc_talk_shake with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh right. No, didn't forget. Just been busy with my other duties."
    scene sm1cs-am001-04 first_time_with_april_am_talk with dissolve
    play voice3 girl22_yes_aga1 noloop
    am "Well tonight we're going hard in the paint and going to knock out the foundation."
    menu:
        "Cool, do we get overtime?"(hint="sm1cs_am001_m01_h01"):
            call sm1cs_am001_m01_c01 from _call_sm1cs_am001_m01_c01
            scene sm1cs-am001-05 first_time_with_april_mc_talk_menu_excited with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "Cool. We get paid extra, right?"
            scene sm1cs-am001-06 first_time_with_april_mc_talk_menu_am_stare with dissolve
            play voice3 stacy_smell noloop
            pause
            scene sm1cs-am001-07 first_time_with_april_mc_talk_menu_am_stare with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "Right?"
            scene sm1cs-am001-08 first_time_with_april_am_talk with dissolve
            play voice3 girl22_yes_yeah1 noloop
            am "Oh yeah. The company will pay you more for doing your job."
            am "Genius."
        "You should have asked me if I can stay"(hint="sm1cs_am001_m01_h02"):
            call sm1cs_am001_m01_c02 from _call_sm1cs_am001_m01_c02
            scene sm1cs-am001-09 first_time_with_april_mc_talk_annoyed with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "Shouldn't you have asked me if I can stay later?"
            scene sm1cs-am001-10 first_time_with_april_am_talk_menu with dissolve
            play voice3 girl22_yes_aga5 noloop
            am "I thought about it."
            scene sm1cs-am001-11 first_time_with_april_mc_talk_menu with dissolve
            play voice2 mc_yes_yeah8 noloop
            mc "And?"
            scene sm1cs-am001-12 first_time_with_april_am_talk_menu_sigh with dissolve
            play voice3 girl22_disappointed_geh noloop
            am "And I deduced that this way would be easier for me."
        "Where do we begin?"(hint="sm1cs_am001_m01_h03"):
            call sm1cs_am001_m01_c03 from _call_sm1cs_am001_m01_c03
            scene sm1cs-am001-05 first_time_with_april_mc_talk_menu_excited with dissolve
            play voice2 mc_yes_okay2 noloop
            mc "Where do we begin?"
    play sound sfx_heels_steps1 loop
    scene sm1cs-am001-13 first_time_with_april_am_desk with dissolve
    pause
    play sound sfx_chair_slide1
    scene sm1cs-am001-14 first_time_with_april_am_talk_sitting with dissolve
    play voice3 girl22_thinking_hmm2 noloop
    am "I emailed you the files. Make sure you download everything."
    play sound sfx_mouse_clicks1
    scene sm1cs-am001-15 first_time_with_april_mc_talk_look_computer with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay, I downloaded everything. There is a task list too."
    scene sm1cs-am001-16 first_time_with_april_am_talk with dissolve
    play voice3 girl22_yes_yep4 noloop
    am "Read it."
    stop sound fadeout 1.0
    scene sm1cs-am001-17 first_time_with_april_mc_talk with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Then what?"
    play sound sfx_cloth_rustling2
    scene sm1cs-am001-18 first_time_with_april_am_talk_phone_ring with dissolve
    play voice3 girl22_disappointed_ehh1 noloop
    am "Nothing. Anna wants to go over things in detail in ten minutes."
    am "So hurry up and read, and don't bother me until she tries to validate her worth here."
    scene sm1cs-am001-19 first_time_with_april_mc_strange_look with dissolve
    pause
    scene sm1cs-am001-20 first_time_with_april_mc_thought with dissolve
    play voice2 mc_thinking_mmm3 noloop volume 1.5
    mct "One day she's going to lighten up. She has to."
    scene sm1cs-am001-21 first_time_with_april_ag_talk_walks_over with dissolve
    play voice4 girl27_hey_greeting noloop
    ag "Hey [mcname]. How are you doing?"
    scene sm1cs-am001-22 first_time_with_april_mc_talk with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "I'm doing alright."
    play sound sfx_cloth_rustling4
    scene sm1cs-am001-23 first_time_with_april_ag_talk_leans_screen with dissolve
    play voice4 girl27_happy_great2 noloop
    ag "Great. Thanks for staying late for this. Join me in the meeting room please. Just want to make sure we have our marching-"
    ag "Uh... In order. Hehe."
    scene sm1cs-am001-24 first_time_with_april_mc_talk with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    $ renpy.music.set_volume(0.1, 1.5, "sound2" )
    scene sm1cs-am001-25 first_time_with_april_ag_talk with fade
    play voice4 girl27_angry_cough2 noloop
    ag "Thanks again, everyone. I know no one likes working late, but a few nights like these will let us relax later on in the project."
    scene sm1cs-am001-26 first_time_with_april_pm_talk with dissolve
    play voice5 boy9_disappointed_geh1 noloop
    pm "Let's just make sure this doesn't mess up our other projects, Anna."
    scene sm1cs-am001-27 first_time_with_april_ag_talk with dissolve
    play voice4 girl27_no_nonono4 noloop
    ag "It's going to be fine, Pete. Have I ever let you down before?"
    scene sm1cs-am001-28 first_time_with_april_pm_talk with dissolve
    play voice5 boy9_thinking_hmm4 noloop
    pm "Hmmm."
    scene sm1cs-am001-29 first_time_with_april_am_talk_ag_frown with dissolve
    play voice3 girl22_arrogant_ha noloop
    am "Come on, Pete, if Anna wants to pull her weight finally, we shouldn't stop her."
    scene sm1cs-am001-30 first_time_with_april_ag_talk_back with dissolve
    play voice4 girl27_arrogant_aha noloop
    ag "Since April was gracious enough to take the lead on fixing up all the code."
    scene sm1cs-am001-31 first_time_with_april_am_talk with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "Under extreme duress."
    scene sm1cs-am001-32 first_time_with_april_ag_talk with dissolve
    play voice4 girl27_arrogant_huh2 noloop
    ag "Or just extremely poor decision making."
    scene sm1cs-am001-33 first_time_with_april_ag_talk_fuming with dissolve
    play voice4 girl27_thinking_hmm3 noloop
    ag "The C.U.M. Division has around three weeks to tackle an entire news studio worth of code."
    ag "That will include work like finding and fixing any bugs and deficiencies that their original software contains."
    scene sm1cs-am001-34 first_time_with_april_ag_talk_supportive with dissolve
    play voice4 girl27_thinking_oh3 noloop
    ag "And of course, our task is more than just moving the code into the new framework."
    ag "If we see areas we can improve and streamline, we should jump on those too."
    ag "We show off our initiative here, and we're going to be the best division in Orbix."
    scene sm1cs-am001-35 first_time_with_april_ag_talk_supportive with dissolve
    play voice4 girl27_yes_yeah6 noloop
    ag "Whatever happened to bring us here, we're not going to let down Claire."
    ag "Right, April?"
    scene sm1cs-am001-36 first_time_with_april_am_talk_sarcastic with dissolve
    play voice3 girl22_happy_yeah noloop
    am "Put me in coach!"
    play sound sfx_phone_tapping1 volume 2.0
    scene sm1cs-am001-37 first_time_with_april_ag_talk_look_tablet with dissolve
    play voice4 girl27_disgust_mff noloop
    ag "So their system is definitely in need of some work."
    stop sound fadeout 1.0
    scene sm1cs-am001-38 first_time_with_april_am_talk_talk_back with dissolve
    play voice3 girl22_surprised_huh1 noloop
    am "\"Some\" work? This is a lot. And what are we going to do about all the old articles and pictures that are in these archives?"
    scene sm1cs-am001-39 first_time_with_april_ag_talk with dissolve
    play voice4 girl27_yes_aga2 noloop
    ag "I'm prepared for that. Here is how tonight will go-"
    play sound sfx_phone_buzz
    scene sm1cs-am001-40 first_time_with_april_mc_thought_phone with dissolve
    play voice2 d1s1_mmm noloop volume 1.4
    mct "Someone sent me a text"
    scene sm1cs-am001-41 first_time_with_april_ag_talk with dissolve
    play voice4 girl27_arrogant_hm5 noloop
    ag "So Megan, I want you to setup our usual make a ticket framework. Once April sets up the foundation we'll plug it right in."
    scene sm1cs-am001-42 first_time_with_april_mj_talk with dissolve
    play voice5 girl26_yes_aga noloop
    mj "Check."
    play sound sfx_message_in1
    scene sm1cs-am001-43 first_time_with_april_mc_phone_picture with dissolve
    sy "Where are you? Stacy horny, [mcname]."
    sy "LOL. JK. Text me when you can."
    scene sm1cs-am001-44 first_time_with_april_mc_phone_picture_thought with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "Hmmm."
    scene sm1cs-am001-45 first_time_with_april_ag_talk_phone_picture with dissolve
    play voice4 girl27_hey_angry noloop
    ag "[mcname]?"
    scene sm1cs-am001-46 first_time_with_april_ag_talk_mc_thoughtphone with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "I could totally jack off to pics of her in the bathroom."
    play voice4 girl27_hey_expressive noloop
    ag "[mcname]?"
    scene sm1cs-am001-47 first_time_with_april_am_talk_mc_startled with dissolve
    play voice3 girl22_arrogant_hm noloop
    am "Earth to nimrod?"
    scene sm1cs-am001-48 first_time_with_april_mc_talk with dissolve
    play voice2 mc_angry_huh1 noloop
    mc "Huh?"
    scene sm1cs-am001-49 first_time_with_april_ag_talk with hpunch
    play voice4 girl27_angry_cough1 noloop
    ag "Ahem."
    play voice2 mc_pain_mff1 noloop
    mct "Oh fuck me."
    play voice4 girl27_angry_cough1 noloop
    ag "You got all that, [mcname]?"
    scene sm1cs-am001-50 first_time_with_april_mc_talk_thought with dissolve
    play voice2 d1s5b_emmm noloop volume 2.0
    mct "Shit. What was she talking about. Something... uh something about data."
    mc "Yeah. Totally. That data won't know what hit it after I'm done with it."
    scene sm1cs-am001-51 first_time_with_april_ag_talk with dissolve
    play voice4 girl27_happy_relief3 noloop
    ag "Okay..."
    scene sm1cs-am001-52 first_time_with_april_ag_talk_april with dissolve
    play voice4 girl27_hey_sexy noloop
    ag "Okay, April. You're up. I need your honest assessment."
    ag "How many coding tasks can you handle before the end of the night?"
    scene sm1cs-am001-53 first_time_with_april_am_talk_mc_relaxes with dissolve
    play voice3 girl22_arrogant_pff noloop
    am "I said I got it, Anna. Move on."
    scene sm1cs-am001-54 first_time_with_april_ag_talk with dissolve
    play voice4 girl27_happy_great3 noloop
    ag "Great. So we're all on the same page."
    scene sm1cs-am001-55 first_time_with_april_am_talk with dissolve
    play voice3 girl22_arrogant_he noloop
    am "Heh. Just don't forget your work too, Anna."
    scene sm1cs-am001-56 first_time_with_april_ag_talk with dissolve
    play voice4 girl27_happy_laugh6 noloop
    ag "Well if I did, I could always just assign it to you, April."
    scene sm1cs-am001-57 first_time_with_april_am_talk with dissolve
    play voice3 girl22_happy_mmm noloop
    am "Bingo. The best way to show you're a good boss is to be lazy and pass off your work to skilled people."
    scene sm1cs-am001-58 first_time_with_april_ag_talk with dissolve
    play voice4 girl27_no_nah2 noloop
    ag "It's called delegation. Now, since there is nothing else, let's get to work.."
    $ renpy.music.set_volume(1.0, 3.0, "sound2" )
    play sound sfx_door_open3
    scene sm1cs-am001-59 first_time_with_april_mc_thought_walk out with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mct "Seriously, what's the deal with the two of them?"
    play sound sfx_cloth_rustling2
    scene sm1cs-am001-60 first_time_with_april_am_mc_thought_sit with dissolve
    mct "I don't think I'm going to get any answers about it tonight. Best to just focus on my work."
    play sound sfx_mouse_clicks1
    scene sm1cs-am001-61 first_time_with_april_am_mc_thought_worried with dissolve
    play voice2 mc_pain_mff2 noloop volume 1.2
    mct "Crap. What is my work? I can't ask Anna. I definitely can't ask April. Data. data something."
    scene sm1cs-am001-62 first_time_with_april_am_mc_thought_worried with dissolve
    mct "Data Structures. That was it."
    stop sound fadeout 1.0
    scene sm1cs-am001-63 first_time_with_april_am_mc_talk with dissolve
    play voice2 d3s7_mcemm noloop
    mct "Right?"
    scene sm1cs-am001-64 first_time_with_april_am_talk with dissolve
    play voice3 girl22_yes_yeah4 noloop
    am "Yeah?"
    scene sm1cs-am001-65 first_time_with_april_mc_talk with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "When we're done, you're going to see just how awesome I am with data."
    play sound sfx_mouse_clicks1
    scene sm1cs-am001-66 first_time_with_april_am_talk_look_back with dissolve
    play voice3 girl22_yes_aga4 noloop
    am "Yeah, whatever."
    scene sm1cs-am001-67 first_time_with_april_mc_look_proud with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mct "Okay. Was good to double check."
    stop sound fadeout 1.0
    jump sm1cs_am001_after_coding
label sm1cs_am001_after_coding:
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    scene black
    show screen scene_transistion("Two hours of mind-numbing codeing later...")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(0.5, 3.0, "sound2" )
    scene sm1cs-am001-68 first_time_with_april_mc_talk_walks_up
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_hey_hey5 noloop
    mc "Hey April."
    scene sm1cs-am001-69 first_time_with_april_mc_talk_am_annoyed with dissolve
    play voice2 mc_happy_yay3 noloop
    mc "Alright. I finished my work, can you check it out?"
    scene sm1cs-am001-70 first_time_with_april_am_talk with dissolve
    play voice3 girl22_surprised_huh2 noloop
    am "Is something wrong with it?"
    menu:
        "I want to make sure it's correct"(hint="sm1cs_am001_m02_h01"):
            scene sm1cs-am001-71 first_time_with_april_mc_talk_menu with dissolve
            play voice2 mc_no_no2 noloop
            mc "I don't think so. But I figured that since I've got a pro nearby, you could make sure everything is in place."
            scene sm1cs-am001-72 first_time_with_april_am_talk with dissolve
            play voice3 girl22_yes_simple noloop
            am "Right. Because that's my {i}actual{/i} job here."
        "No, I just thought you could use a break."(hint="sm1cs_am001_m02_h02"):
            call sm1cs_am001_m02_c02 from _call_sm1cs_am001_m02_c02
            scene sm1cs-am001-73 first_time_with_april_mc_talk_menu_annoyed with dissolve
            play voice2 mc_no_no3 noloop
            mc "No. I mean we've been at it two hours. Two hours of working in silence."
            scene sm1cs-am001-74 first_time_with_april_mc_talk_menu_shrug with dissolve
            play voice2 d1s5_mchappy noloop volume 1.6
            mc "I figured you could use a break."
            scene sm1cs-am001-75 first_time_with_april_am_talk_menu_more annoyed with dissolve
            play voice3 girl22_angry_heergh noloop
            am "Yay. A break to check your homework. I'm such a lucky gal."
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1cs-am001-76 first_time_with_april_am_opens_tab with dissolve
    pause
    scene sm1cs-am001-77 first_time_with_april_mc_talk_nervous with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "... uh... is there a problem?"
    play voice3 girl22_angry_argh3 noloop
    stop sound fadeout 0.5
    scene sm1cs-am001-78 first_time_with_april_am_talk with hpunch
    am "Motherfucker!"
    scene sm1cs-am001-79 first_time_with_april_mc_talk_shocked with dissolve
    play voice2 mc_surprised_what8 noloop
    mc "What?"
    play sound sfx_chair_slide1
    scene sm1cs-am001-80 first_time_with_april_am_talk_swing with dissolve
    play voice3 girl22_angry_argh2 noloop
    am "Yes, there is a problem. Some Business 101 dropout just fucked my night."
    am "You did the data structuring."
    scene sm1cs-am001-81 first_time_with_april_mc_talk_swing with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Yes."
    play sound sfx_hands_clap1
    scene sm1cs-am001-82 first_time_with_april_am_talk_deep_breathe with dissolve
    play voice3 girl22_angry_breathing noloop volume 1.3
    am "{i}You{/i}... were supposed to handle the convertor tools for the old data!"
    menu:
        "Simple mistake"(hint="sm1cs_am001_m03_h01"):
            scene sm1cs-am001-83 first_time_with_april_mc_talk_menu_sorry with dissolve
            play voice2 mc_thinking_oh1 noloop
            mc "Oh. Really. I must have gotten em mixed up. Sorry. I'm sure that kind of things happens all the time."
            scene sm1cs-am001-84 first_time_with_april_am_talk_menu_sorry with dissolve
            play voice3 girl22_angry_argh1 noloop
            am "You dense motherfucker. This is Orbix, one of the premier tech companies in the country. {w}Not the state,{w} not the city."
            scene sm1cs-am001-85 first_time_with_april_am_talk_menu_speak_slowly with dissolve
            play voice3 girl22_disappointed_geh noloop
            am "The country. We don't make simple mistakes here. But we do pay for them."
        "Oh shit"(hint="sm1cs_am001_m03_h02"):
            call sm1cs_am001_m03_c02 from _call_sm1cs_am001_m03_c02
            scene sm1cs-am001-86 first_time_with_april_mc_talk_menu_oh_shit with dissolve
            play voice2 mc_pain_rrrr noloop
            mc "Oh shit. I'm really sorry, April. I'll get to work on that immediately."
            scene sm1cs-am001-87 first_time_with_april_am_talk_menu_having fun with dissolve
            play voice3 girl22_arrogant_yeah noloop
            am "Maybe if you weren't looking at nip slip pics on your phone like some jerk-faced pervert, you wouldn't need me to pull your head out of your ass."
    play sound sfx_drink_slurp1
    scene sm1cs-am001-88 first_time_with_april_mc_talk_am _sip_typing with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Okay. How do we fix this?"
    scene sm1cs-am001-89 first_time_with_april_am_talk with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "You want to fix this?"
    scene sm1cs-am001-90 first_time_with_april_mc_talk with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yes."
    scene sm1cs-am001-91 first_time_with_april_am_talk_turn with dissolve
    play voice3 girl22_thinking_oh noloop
    am "Maybe go play in traffic. That might do it."
    scene sm1cs-am001-92 first_time_with_april_mc_talk with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Hey, come on. That's not cool."
    scene sm1cs-am001-93 first_time_with_april_am_talk_screen with dissolve
    play voice3 girl22_yes_yeah3 noloop
    am "You're right. You'd probably screw that up too."
    scene sm1cs-am001-94 first_time_with_april_mc_talk_sigh with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "*sighs*"
    scene sm1cs-am001-95 first_time_with_april_mc_talk_turn back with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "So what happens now?"
    scene sm1cs-am001-96 first_time_with_april_am_talk with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "I fix your fuckup. You're lucky I'm nearly done with my own workload."
    am "Just go back to your desk, before Anna figures out the problem."
    scene sm1cs-am001-97 first_time_with_april_mc_talk with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "You're... you're not going to tell her?"
    scene sm1cs-am001-98 first_time_with_april_am_talk_look with dissolve
    play voice3 girl22_angry_cough noloop
    am "Did I stutter?"
    scene sm1cs-am001-99 first_time_with_april_mc_talk with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Right. Desk, going."
    play sound sfx_mouse_clicks1
    scene sm1cs-am001-100 first_time_with_april_mc_thought_sit_down with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Okay, now I just have to... pretend I'm working."
    mct "Still, the bigger problem is that April might lord this fuckup over me whenever she likes."
    mct "And I don't like that feeling at all."
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.0, 1.0, "sound2" )
    jump sm1cs_am001_later
label sm1cs_am001_later:
    scene black
    show screen scene_transistion("Another hour later")
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    $ renpy.music.set_volume(1.0, 3.0, "sound2" )
    stop sound2 fadeout 6.0
    play sound sfx_classroom_ambience
    scene sm1cs-am001-101 first_time_with_april_ag_talk_walkout_pm_mj_leave
    with Fade(0.5, 0.5, 0.5)
    stop sound fadeout 6.0
    play voice4 girl27_hey_bye6 noloop
    ag "Good night guys. Keep up the good work."
    scene sm1cs-am001-102 first_time_with_april_mc_talk_walkout_pm_mj_leave with dissolve
    play voice2 mc_hey_bye2 noloop
    mc "*nervously* You too, Anna. I mean. Have a good night."
    scene sm1cs-am001-103 first_time_with_april_am_talk_ag_gone with dissolve
    play voice3 girl22_happy_laugh1 noloop
    am "Smooth."
    scene sm1cs-am001-104 first_time_with_april_mc_thought with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "At least now I can relax and not pretend for an hour straight."
    scene sm1cs-am001-105 first_time_with_april_mc_thought_focus_am with dissolve
    mct "April told me she would handle it, but it doesn't feel right, leaving all the work to her."
    mct "There has to be something I can do."
    play sound sfx_cloth_rustling1
    scene sm1cs-am001-106 first_time_with_april_mc_pullout_phone with dissolve
    play voice2 mc_thinking_hmm8 noloop
    pause
    play sound sfx_phone_call1
    scene sm1cs-am001-107 first_time_with_april_mc_talk with dissolve
    play voice2 mc_hey_hey6 noloop
    mc "Hey it's me."
    scene sm1cs-am001-108 first_time_with_april_mc_stand with dissolve
    pause
    scene sm1cs-am001-109 first_time_with_april_am_talk_finished with fade
    play voice3 girl22_angry_argh3 noloop
    am "Fuck yeah!"
    play sound sfx_chair_slide1
    scene sm1cs-am001-110 first_time_with_april_am_talk_stretch with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "Mrraah."
    scene sm1cs-am001-111 first_time_with_april_am_talk_look with dissolve
    play voice3 girl22_surprised_eh2 noloop
    am "Huh? Now where did the idiot go?"
    play sound sfx_heels_steps2 loop
    scene sm1cs-am001-112 first_time_with_april_mc_talk_bag with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey."
    scene sm1cs-am001-113 first_time_with_april_am_talk with dissolve
    play voice3 girl22_hey_scared noloop
    am "Hey. What's this?"
    play sound sfx_paper_bag_2
    scene sm1cs-am001-114 first_time_with_april_mc_talk_pullout with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Well you wouldn't let me help one way, so I figured out another way."
    scene sm1cs-am001-115 first_time_with_april_am_talk with dissolve
    play voice3 girl22_surprised_eh1 noloop
    am "You don't know what I like."
    scene sm1cs-am001-116 first_time_with_april_mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yup. Which is why I ordered everything on the Wurst Delivery Menu."
    scene sm1cs-am001-117 first_time_with_april_am_speechless with dissolve
    play voice3 girl22_sex_closedmoan1 noloop
    pause
    scene sm1cs-am001-118 first_time_with_april_mc_talk_grin with dissolve
    play voice2 mc_happy_a1 noloop
    mc "How's the progress?"
    play sound sfx_cloth_rustling3
    scene sm1cs-am001-119 first_time_with_april_am_cheesdog with dissolve
    pause
    scene sm1cs-am001-120 first_time_with_april_am__talk_cheesdog with dissolve
    play voice3 girl22_yes_aga11 noloop
    am "It's done."
    scene sm1cs-am001-121 first_time_with_april_am_eating with dissolve
    play voice3 girl22_sex_closedmoan3 noloop
    pause
    scene sm1cs-am001-122 first_time_with_april_am_eating with dissolve
    play voice3 girl22_sex_closedmoan4 noloop
    pause
    play sound sfx_bite_strawberry1
    scene sm1cs-am001-123 first_time_with_april_am_talk with dissolve
    play voice3 girl22_arrogant_he noloop
    am "You got one thing right tonight."
    scene sm1cs-am001-124 first_time_with_april_mc_talk with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Yup. And I... I should have said this earlier, but thanks for not telling Anna about my screwup."
    scene sm1cs-am001-125 first_time_with_april_am_talk_fries with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "I was too busy to fink on you. Maybe next time."
    am "But don't count on me covering for you in the future, [mcname]"
    scene sm1cs-am001-126 first_time_with_april_mc_talk with dissolve
    play voice2 mc_no_no5 noloop
    mc "I won't."
    scene sm1cs-am001-127 first_time_with_april_am_talk with dissolve
    play voice3 girl22_hey_attention noloop
    am "I'm dead serious. We have a job to do. Sometimes it's long hours, and that sucks."
    scene sm1cs-am001-128 first_time_with_april_am_talk_otherbite with dissolve
    play voice3 girl22_thinking_hmm1 noloop
    am "But if you're here, and especially if you're working with me, I need your A game."
    am "Got it?"
    scene sm1cs-am001-129 first_time_with_april_mc_talk_reply with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Loud and clear, April."
    play voice2 mc_eating_mmm noloop
    scene sm1cs-am001-130 first_time_with_april_montage_cleanup with dissolve
    pause
    play sound sfx_paper_bag_1
    scene sm1cs-am001-131 first_time_with_april_montage_cleanup with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-am001-132 first_time_with_april_am_talk_phone with dissolve
    play voice3 girl22_arrogant_hm noloop
    am "I just texted Anna the good news. Had to rub it in her face that we did it all in one night."
    scene sm1cs-am001-133 first_time_with_april_mc_thinking with dissolve
    pause
    scene sm1cs-am001-134 first_time_with_april_mc_talk with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "I'm sure she loved that."
    scene sm1cs-am001-135 first_time_with_april_am_talk with dissolve
    play voice3 girl22_arrogant_pff noloop
    am "Psssh. She won't read it. This late, she'll either be nose-down in a book or playing some strat game."
    play sound sfx_heels_steps2 loop
    scene sm1cs-am001-136 first_time_with_april_am_talk_lead with dissolve
    play voice3 girl22_happy_laugh3 noloop
    am "Night loser."
    scene sm1cs-am001-137 first_time_with_april_mc_talk with dissolve
    play voice2 mc_hey_bye1 noloop
    mc "Night April."
    stop sound fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene_in_time(AM_STORY, 22, 0, 4)
    return
label sm1cs_am001_m01_c01:
    $ player.set_choice("sm1cs_am001_get_overtime")
    $ CharacterController.get_character("am").deduct_point()
    return
label sm1cs_am001_m01_c02:
    $ player.set_choice("sm1cs_am001_i_can_stay")
    return
label sm1cs_am001_m01_c03:
    $ player.set_choice("sm1cs_am001_where_begin")
    $ CharacterController.get_character("am").add_point()
    return
label sm1cs_am001_m02_c02:
    $ player.set_choice("sm1cs_am001_use_break")
    return
label sm1cs_am001_m03_c02:
    $ player.set_choice("sm1cs_am001_oh_shit")
    $ CharacterController.get_character("am").add_point()
    return
label sm1cs_am001_unlocks:
    call sm1cs_am001_m01_c01 from _call_sm1cs_am001_m01_c01_1
    call sm1cs_am001_m02_c02 from _call_sm1cs_am001_m02_c02_1
    call sm1cs_am001_m03_c02 from _call_sm1cs_am001_m03_c02_1
    if config_storyline_mode is True:
        $ execute_storyline_config(AM_STORY)
    return