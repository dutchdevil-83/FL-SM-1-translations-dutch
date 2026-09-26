label sm1fs_i004:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1fs-i004-00 new_client_stretch with dissolve
    pause
    scene sm1fs-i004-01 new_client_cw_talk with dissolve
    play voice3 girl29_hey_angry noloop
    cw "[mcname], meeting in the conference room in five."
    scene sm1fs-i004-02 new_client_mc_talk with dissolve
    play voice2 mc_thinking_mmm5 noloop volume 1.4
    mc "Everything okay?"
    scene sm1fs-i004-03 new_client_cw_talk with dissolve
    play voice3 girl29_yes_yeah noloop
    cw "Yeah, just got a client meeting. Nothing fancy."
    play sound sfx_chair_slide1 volume 1.5
    scene sm1fs-i004-04 new_client_mc_talk_stand with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Is there anything I should know?"
    scene sm1fs-i004-05 new_client_cw_talk_confused_recognition with dissolve
    play voice3 girl29_no_questioning noloop
    cw "Know?"
    cw "This is your first client meeting, isn't it?"
    play music "<silence 1.5>"
    scene sm1fs-i004-06 new_client_mc_talk_recognition with dissolve
    queue music music_brain_power
    play voice2 mc_happy_yay2 noloop
    mc "Yep, popping my client meeting cherry!"
    scene sm1fs-i004-07 new_client_cw_talk_recognition with dissolve
    play voice3 girl29_disappointed_ehh noloop
    cw "[mcname]... That kind of remark walks dangerously close to an HR complaint."
    scene sm1fs-i004-08 new_client_mc_talk_recognition with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "... Sorry Claire."
    scene sm1fs-i004-09 new_client_cw_talk_walk with dissolve
    play voice3 girl29_yes_aga1 noloop
    cw "Just don't make any comments like that-"
    scene sm1fs-i004-10 new_client_cw_talk_stop with dissolve
    play voice3 girl29_surprised_ehh noloop
    cw "In fact, maybe for your first meeting you should just listen."
    scene sm1fs-i004-11 new_client_ag_talk_walks with dissolve
    play voice4 girl27_hey_sexy noloop
    ag "You don't need to stress, [mcname]. These things are easy."
    scene sm1fs-i004-12 new_client_mc_talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Are they?"
    play sound sfx_cloth_rustling2
    scene sm1fs-i004-13 new_client_ag_talk_hand_back with dissolve
    play voice4 girl27_happy_yeah4 noloop
    ag "Yeah! All we're doing is showing face and making the client feel like she's heard."
    scene sm1fs-i004-14 new_client_mc_talk_hand_back with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Seems easy enough."
    scene sm1fs-i004-15 new_client_ag_talk_hand_back with dissolve
    play voice4 girl27_yes_confident noloop
    ag "It is. Just follow my lead and you'll do fine."
    play sound sfx_heels_steps1
    scene sm1fs-i004-16 new_client_anna_walks with dissolve
    pause
    scene sm1fs-i004-17 new_client_mc_walks with dissolve
    pause
    play sound sfx_door_open5
    scene sm1fs-i004-18 new_client_conference_mc_enter with dissolve
    pause
    $ renpy.music.set_volume(0.2, 1.0, "sound2" )
    play sound sfx_door_open3 volume 2.0
    scene sm1fs-i004-19 new_client_conference_ag_talk with dissolve
    play voice4 girl27_surprised_huh2 noloop
    ag "Where's Claire? Isn't she-"
    scene sm1fs-i004-20 new_client_conference_am_talk with dissolve
    play voice5 girl22_arrogant_he noloop
    am "Don't get your panties in a twist. She just went to grab the client."
    scene sm1fs-i004-21 new_client_conference_ag_talk with dissolve
    play voice4 girl27_angry_cough1 noloop
    ag "I don't need the attitude, April."
    scene sm1fs-i004-22 new_client_conference_am_talk with dissolve
    play voice5 girl22_thinking_eeh noloop
    am "Sorry, {i}Aubergine Annie{/i}."
    scene sm1fs-i004-23 new_client_conference_ag_talk with dissolve
    play voice4 girl27_angry_kgh noloop
    ag "April! I will get you written up again!"
    scene sm1fs-i004-24 new_client_conference_am_talk_towards with dissolve
    play voice5 girl3_disgust_oof noloop
    am "Oooo, I'm so scared. Big scary HR is going to sit me down and make me do another mandatory training."
    scene sm1fs-i004-25 new_client_conference_ag_talk_mad with dissolve
    play voice4 girl27_angry_argh4 noloop
    ag "At least I have more going for me than some terrible band and HR meetings."
    scene sm1fs-i004-26 new_client_conference_am_talk with dissolve
    play voice5 girl22_thinking_oh noloop
    am "Oh, I've seen how much you've got going for you."
    scene sm1fs-i004-27 new_client_conference_ag_talk_madder with dissolve
    play voice4 girl27_angry_err2 noloop
    ag "Your hair screams Daddy issues."
    scene sm1fs-i004-28 new_client_conference_am_talk with dissolve
    play voice5 girl22_yes_yeah3 noloop
    am "And your code just screams issues."
    scene sm1fs-i004-29 new_client_conference_ag_talk_fist with dissolve
    play voice4 girl27_angry_err5 noloop
    ag "It's better than your ramshackle, self taught, hack job code!"
    scene sm1fs-i004-24 new_client_conference_am_talk_towards with dissolve
    play voice5 girl22_arrogant_yeah noloop
    am "Remind me, how many errors were in your last job?"
    scene sm1fs-i004-25 new_client_conference_ag_talk_mad with dissolve
    play voice4 girl27_arrogant_aha noloop
    am "And how many were in mine?"
    scene sm1fs-i004-30 new_client_conference_ns_talk_look_mc with dissolve
    play voice3 nari_surprised_huh2 noloop
    ns "Is this a typical office relationship, with normal banter?"
    scene sm1fs-i004-31 new_client_conference_mc_talk with dissolve
    play voice2 d2s12_emmm noloop
    mc "Uh, nope."
    scene sm1fs-i004-32 new_client_conference_ns_talk with dissolve
    play voice3 nari_arrogant_heh noloop
    ns "Are you sure?"
    scene sm1fs-i004-33 new_client_conference_ag_talk with dissolve
    play voice4 girl27_disappointed_ehh1 noloop
    ag "Nari-"
    scene sm1fs-i004-34 new_client_conference_ns_talk with dissolve
    play voice3 nari_yes_questioning noloop
    ns "Yes, Aubergine Annie?"
    scene sm1fs-i004-35 new_client_conference_ag_talk with hpunch
    play voice4 girl27_angry_tagh noloop volume 1.6
    ag "Don't call me that!"
    scene sm1fs-i004-36 new_client_conference_ns_talk_surprised with dissolve
    play voice3 nari_pain_aaa1 noloop
    ns "I am sorry Ms. Goodwin! I thought it was an affectionate office nickname."
    scene sm1fs-i004-37 new_client_conference_ag_talk with dissolve
    play voice4 girl27_angry_argh2 noloop
    ag "It is not affectionate! It's because April is a-"
    play sound sfx_door_open1
    $ renpy.music.set_volume(0.8, 1.0, "sound2" )
    scene sm1fs-i004-38 new_client_conference_ag_talk_claire_enters with hpunch
    play voice4 girl27_surprised_ah noloop
    ag "Oh, Claire. April was-"
    scene sm1fs-i004-38-1 new_client_conference_cw_talk_ag_sad with dissolve
    play voice3 girl29_disappointed_mff noloop
    cw "I don't want to hear it, Anna. We're here for an important meeting."
    $ renpy.music.set_volume(0.2, 1.0, "sound2" )
    play sound sfx_door_open3 volume 2.0
    scene sm1fs-i004-39 new_client_conference_cw_talks with dissolve
    play voice3 girl29_hey_happy noloop
    cw "Team, I'd like you to meet our newest client, Angela Taylor Portillo."
    scene sm1fs-i004-40 new_client_conference_atp_talks with dissolve
    play voice4 girl23_hey_greeting noloop
    atp "Hello, it's a pleasure to meet you."
    scene sm1fs-i004-41 new_client_conference_atp_talks_sits with dissolve
    play voice4 girl23_thinking_hmm3 noloop
    atp "I'm looking forward to working with you all."
    play sound sfx_cloth_rustling4
    scene sm1fs-i004-42 new_client_conference_cw_talks_atp_sits with dissolve
    play voice3 girl29_yes_aga2 noloop
    cw "We are looking forward to working with you, and your network. We have a brief presentation about our plan for your new website."
    scene sm1fs-i004-44 new_client_conference_cw_talks_screen with dissolve
    play sound sfx_light_turn2 volume 2.0
    play voice3 girl29_thinking_mmm2 noloop
    cw "We've had our teams here at Orbix do a market analysis. They came up with some solutions for a new website."
    scene sm1fs-i004-45 new_client_conference_cw_talks_angela with dissolve
    play voice3 girl29_thinking_hmm5 noloop
    cw "I won't bore you with the details; an expansion of your servers to host more video content, updating your mobile site, and a 'face lift' for your desktop presence."
    scene sm1fs-i004-46 new_client_conference_atp_talks with dissolve
    play voice4 girl23_yes_yeeeah2 noloop
    atp "Good. How long will all of this take?"
    scene sm1fs-i004-47 new_client_conference_cw_talks with dissolve
    play voice3 girl29_thinking_oh noloop
    cw "We're looking at... Minimum, three months. Without any delays, but we'll most likely be looking at six months."
    scene sm1fs-i004-48 new_client_conference_atp_talks with dissolve
    play voice4 girl23_no_angry noloop
    atp "That's not acceptable."
    scene sm1fs-i004-49 new_client_conference_am_talks with dissolve
    play voice5 girl22_arrogant_hm noloop
    am "I could do this all in my sleep. It will take me only three weeks if the existing code isn't a mess. Four if some idiots got a hold of it."
    scene sm1fs-i004-50 new_client_conference_cw_talks with dissolve
    play voice3 girl29_angry_hmf noloop
    cw "April-"
    scene sm1fs-i004-51 new_client_conference_atp_talks with dissolve
    play voice4 girl23_yes_happy noloop
    atp "That is a much better timetable for me."
    cw "..."
    play sound sfx_cloth_rustling1 volume 1.5
    scene sm1fs-i004-52 new_client_conference_atp_talks_stands_up with dissolve
    play voice4 girl23_happy_relief noloop
    atp "I have worked tirelessly to keep the network on the cutting edge, the forefront of media technology."
    scene sm1fs-i004-53 new_client_conference_atp_talks_look with dissolve
    play voice4 girl23_happy_phew noloop
    atp "I'm very glad I went with Orbix. You all look full of determination. Hopefully enough to keep me on the leading edge."
    scene sm1fs-i004-55 new_client_conference_atp_talks_look_mc_smiles with dissolve
    play voice4 girl23_thinking_hmm1 noloop
    atp "Naturally I want to stay out of your way, but I definitely want to stop by and get progress reports from time to time."
    atp "We should work closely together so there are no screwups."
    scene sm1fs-i004-56 new_client_conference_cw_talks_angela_door with dissolve
    play voice3 girl29_yes_happy noloop
    cw "Of course. We're excited to be in bussiness with you, Angela. As soon as we have a progress update, I'll get in touch."
    scene sm1fs-i004-57 new_client_conference_atp_talks_angela_door with dissolve
    play voice4 girl23_yes_yeah noloop
    atp "Excellent."
    scene sm1fs-i004-58 new_client_conference_cw_talks with dissolve
    play voice3 girl29_thinking_hmm3 noloop
    cw "Let me show you out."
    scene sm1fs-i004-59 new_client_conference_atp_talks with dissolve
    play voice4 girl23_no_uhuh2 noloop
    atp "No need, I know the way. Your time is better spent on the project anyhow."
    scene sm1fs-i004-60 new_client_conference_cw_talks_smiles with dissolve
    play voice3 girl29_yes_serious noloop
    cw "Of course."
    play sound sfx_door_open3 volume 2.0
    $ renpy.music.set_volume(0.8, 1.0, "sound2" )
    scene sm1fs-i004-61 new_client_conference_angela_smiles_walks_out with dissolve
    pause
    scene sm1fs-i004-62 new_client_conference_claire_fake_smile with dissolve
    pause
    play sound sfx_door_closed1
    $ renpy.music.set_volume(0.2, 1.0, "sound2" )
    scene sm1fs-i004-63 new_client_conference_claire_talk_annoyed with dissolve
    play voice3 girl29_angry_argh1 noloop
    cw "April. {w}That was not okay."
    scene sm1fs-i004-64 new_client_conference_am_talk with dissolve
    play voice4 girl22_disappointed_geh noloop
    am "Claire, seriously? We could-"
    scene sm1fs-i004-66 new_client_conference_ag_talk_glares with dissolve
    play voice3 girl29_angry_ehh noloop
    cw "Anna, you need to get your team in check."
    play voice5 girl27_surprised_what2 noloop
    ag "What? I can't control April."
    scene sm1fs-i004-67 new_client_conference_cw_talk_glares with dissolve
    play voice3 girl29_arrogant_yeah noloop
    cw "You had better learn how to. One day an outburst like that will cause you to lose your job."
    scene sm1fs-i004-68 new_client_conference_ag_talk_disbelief with dissolve
    play voice5 girl27_surprised_eh noloop
    ag "I... Just..."
    scene sm1fs-i004-69 new_client_conference_cw_talk_disbelief with dissolve
    play voice3 girl29_angry_argh2 noloop
    cw "And because of her outburst, your whole team is going to suffer. Learning how to manage your own team is the earmark of a good manager."
    cw "In fact, it's literally in the name."
    scene sm1fs-i004-70 new_client_conference_anna_look_down_april_rolleyes with dissolve
    play voice4 girl22_angry_heergh noloop
    pause
    scene sm1fs-i004-71 new_client_conference_cw_talks with dissolve
    play voice3 girl29_thinking_hmm4 noloop
    cw "Assignments. Nari, you're on the new video servers. Full set up. You can talk with Anna later about getting the hardware requirements."
    scene sm1fs-i004-72 new_client_conference_ns_talks with dissolve
    play voice4 nari_yes_yep noloop
    ns "I can do that, Ms. Watts."
    scene sm1fs-i004-67 new_client_conference_cw_talk_glares with dissolve
    play voice3 girl29_arrogant_he noloop
    cw "Great, Anna you're in charge of the UI for mobile and desktop."
    scene sm1fs-i004-68 new_client_conference_ag_talk_disbelief with dissolve
    play voice5 girl27_yes_yeah6 noloop
    ag "Of course, Claire. I'll get right on it."
    scene sm1fs-i004-73 new_client_conference_cw_talk with dissolve
    play voice3 girl29_angry_hm noloop
    cw "April, you're in charge of all the code."
    scene sm1fs-i004-74 new_client_conference_ag_talk with hpunch
    play voice4 girl22_no_high noloop
    am "No, come on-"
    play sound sfx_kick_leg1
    scene sm1fs-i004-75 new_client_conference_cw_talk_hands_table with dissolve
    play voice3 girl29_yes_arrogant noloop
    cw "And [mcname] will be helping you."
    scene sm1fs-i004-76 new_client_conference_ag_talk_jaw with dissolve
    play voice4 girl22_scared_huh noloop
    am "And you're sticking me with the new guy!? What the hell, Claire!"
    am "He'll just slow me down!"
    scene sm1fs-i004-77 new_client_conference_cw_talk_jaw with dissolve
    play voice3 girl29_angry_kgh noloop
    cw "We need all hands on deck now. We've got a much smaller window to complete the job."
    cw "Everyone is going to need to pull their weight."
    play sound sfx_bed_slide2
    scene sm1fs-i004-78 new_client_conference_am_talk_stands with dissolve
    play voice4 girl22_angry_argh3 noloop
    am "This is such bull-"
    scene sm1fs-i004-80 new_client_conference_cw_talk_straightens with dissolve
    play voice3 girl29_happy_laugh2 noloop
    cw "April, one more outburst and I'm rescinding your PTO."
    scene sm1fs-i004-79 new_client_conference_am_talk_straightens with dissolve
    play voice4 girl22_scared_eh noloop
    am "You can't do that!"
    scene sm1fs-i004-83 new_client_conference_cw_talk with dissolve
    play voice3 girl29_arrogant_ha noloop
    cw "I absolutely can, as your boss."
    scene sm1fs-i004-84 new_client_conference_am_talk with dissolve
    play voice4 girl22_angry_dagh noloop
    am "Come on, Claire!"
    play sound sfx_heels_steps1
    scene sm1fs-i004-85 new_client_conference_cw_talk_walks with dissolve
    play voice3 girl29_yes_questioning noloop
    cw "And you've got four weeks to finish."
    scene sm1fs-i004-86 new_client_conference_am_talk_walks with dissolve
    play voice4 girl22_disappointed_ah noloop
    am "But if a bunch of dumb code-monkeys messed around with it-"
    play sound sfx_door_open3 volume 2.0
    $ renpy.music.set_volume(0.8, 1.0, "sound2" )
    scene sm1fs-i004-89 new_client_conference_cw_talk_sits with dissolve
    play voice3 girl29_arrogant_hm noloop
    cw "That's why you've got four weeks instead of three. Guess you'll just have to do it while you're awake."
    play sound sfx_door_closed1
    $ renpy.music.set_volume(0.2, 1.0, "sound2" )
    scene sm1fs-i004-90 new_client_conference_am_talk_claire_leaves with dissolve
    play voice4 girl22_disappointed_oof noloop
    am "Uggggh!"
    scene sm1fs-i004-91 new_client_conference_ag_talk_smiles with dissolve
    play voice3 girl27_happy_laugh2 noloop
    ag "Seems like your mouth has finally started getting you into the trouble you deserve."
    scene sm1fs-i004-92 new_client_conference_am_talk_smiles with dissolve
    play voice4 girl22_angry_argh2 noloop
    am "Shut up, Aubergine. I don't need your sass right now."
    scene sm1fs-i004-93 new_client_conference_ag_talk_angry with dissolve
    play voice3 girl27_arrogant_huh2 noloop
    ag "Just don't screw this up. Or I will make your life... Difficult."
    scene sm1fs-i004-94 new_client_conference_am_talk_angry with dissolve
    play voice4 girl22_yes_aga10 noloop
    am "Don't tell me. This is the part where I'm supposed to shut up."
    am "Tch. And I'm not going to screw up. Your Friday night plans with your kitchen are safe."
    play sound sfx_bed_slide3 volume 0.7
    scene sm1fs-i004-95 new_client_conference_ns_talk_anna_storms_out with dissolve
    play voice3 nari_surprised_huh1 noloop
    ns "Um. Is this how most client meetings go?"
    play sound sfx_door_openclosed2
    scene sm1fs-i004-96 new_client_conference_am_talk_anna_storms_out with dissolve
    play voice4 girl22_no_nope4 noloop
    am "Nope."
    scene sm1fs-i004-97 new_client_conference_ns_talk with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Oh..."
    play sound sfx_bed_slide2
    scene sm1fs-i004-98 new_client_conference_ns_talk_stands with dissolve
    play voice3 nari_thinking_hmm3 noloop
    ns "I should probably start working on my portion of the project."
    scene sm1fs-i004-99 new_client_conference_ns_talk_look mc with dissolve
    play voice3 nari_hey_asking noloop
    ns "Good luck."
    scene sm1fs-i004-100 new_client_conference_ns_walks_out with dissolve
    pause
    play sound sfx_door_openclosed2
    play sound3 sfx_kick_leg1 noloop
    scene sm1fs-i004-101 new_client_conference_am_head_table with dissolve
    pause
    scene sm1fs-i004-102 new_client_conference_mc_talk_head_table with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Sorry you're stuck with me."
    play sound sfx_cloth_rustling2
    scene sm1fs-i004-103 new_client_conference_am_talk_wave_hand with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "It's not your fault."
    scene sm1fs-i004-104 new_client_conference_am_talk_raises_head with dissolve
    play voice3 girl22_arrogant_pff noloop
    am "It's me and my stupid mouth's fault."
    scene sm1fs-i004-105 new_client_conference_mc_sad with dissolve
    pause
    scene sm1fs-i004-106 new_client_conference_am_realizes with dissolve
    play voice3 girl22_disappointed_ehh1 noloop
    am "Ahem. Listen I..."
    am "You are... You're"
    scene sm1fs-i004-107 new_client_conference_mc_realizes with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I get it, I'm not... Super great at this yet."
    scene sm1fs-i004-108 new_client_conference_am_realizes with dissolve
    play voice3 girl22_no_simple noloop
    am "At least you're honest. Don't sweat. I've got more than enough skill for the both of us."
    scene sm1fs-i004-109 new_client_conference_am_moves with dissolve
    play voice3 girl22_happy_relief noloop
    am "And if you pay attention you may learn a thing or two, 'kay?"
    scene sm1fs-i004-110 new_client_conference_mc_talk_look with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Does that mean... You're going to work with me?"
    scene sm1fs-i004-111 new_client_conference_am_talk_look with dissolve
    play voice3 girl22_yes_simple noloop
    am "Yes... That means you can work for me."
    scene sm1fs-i004-112 new_client_conference_mc_talk_confused with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "For?"
    scene sm1fs-i004-113 new_client_conference_am_talk_confused with dissolve
    play voice3 girl22_yes_yeah1 noloop
    am "Yeah, keep up. I'm the talent, you're just going to copy my genius code, and we're going to crush this."
    play sound ["<silence 0.3>", sfx_hands_clap3]
    scene sm1fs-i004-114 new_client_conference_am_talk_plotting with dissolve
    play voice3 girl22_happy_laugh1 noloop
    am "We're going to crush the deadline. Just watch."
    play sound sfx_bed_slide3
    scene sm1fs-i004-115 new_client_conference_am_talk_standing with dissolve
    play voice3 girl22_hey_simple noloop
    am "Now come on, let's get to work."
    scene sm1fs-i004-116 new_client_conference_am_talk_walking_door with dissolve
    play voice3 girl22_arrogant_he noloop
    am "And you better like punk rock music."
    scene sm1fs-i004-117 new_client_conference_mc_talk_menu with dissolve
    menu:
        "I do, I love Kikini Bill."(hint="sm1fs_i004_m01_h01"):
            call sm1fs_i004_m01_c01 from _call_sm1fs_i004_m01_c01
            play voice2 mc_yes_yeah4 noloop
            mc "Yeah, I love punk! Especially Kikini Bill and MobileBrat."
            scene sm1fs-i004-118 new_client_conference_am_talk_menu with dissolve
            play voice3 girl22_surprised_huh1 noloop
            am "You know Kikini Bill and MobileBrat?"
            scene sm1fs-i004-119 new_client_conference_mc_talk_menu with dissolve
            play voice2 mc_no_uhuh1 noloop
            mc "Uh huh, that's my jam."
        "Uh, yep! Totally."(hint="sm1fs_i004_m01_h02"):
            call sm1fs_i004_m01_c02 from _call_sm1fs_i004_m01_c02
            play voice2 mc_yes_yeah4 noloop
            mc "Yeah, I love to jam out to some good ol' punk rock."
        "I don't mind some... Punk rock."(hint="sm1fs_i004_m01_h03"):
            call sm1fs_i004_m01_c03 from _call_sm1fs_i004_m01_c03
            play voice2 d2s9_confused noloop volume 1.7
            mc "I, uhm, sure do!"
        "I'd rather listen to classic rock!"(hint="sm1fs_i004_m01_h04"):
            call sm1fs_i004_m01_c04 from _call_sm1fs_i004_m01_c04
            play voice2 mc_yes_aga1 noloop
            mc "I mean, it's not as good as classic rock, but it's... Fine."
    scene sm1fs-i004-120 new_client_conference_mam_talk with dissolve
    play voice3 girl22_happy_mmm noloop
    am "I can work with that. Now, come on. Let's get to work."
    play sound sfx_door_open3 volume 2.0
    $ renpy.music.set_volume(1.0, 1.0, "sound2" )
    scene sm1fs-i004-121 new_client_conference_am_leaves with dissolve
    pause
    play sound sfx_door_closed2
    scene sm1fs-i004-122 new_client_conference_mc_leaves with dissolve
    pause
    stop music fadeout 3.0
    stop sound2 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.activate_story_line(AM_STORY)
    $ StoryController.end_scene(IT_STORY_LINE, 3, 0, 2)
    return
label sm1fs_i004_m01_c01:
    $ player.set_choice("sm1fs_i004_love_kb")
    $ CharacterController.get_character("am").add_point(2)
    return
label sm1fs_i004_m01_c02:
    $ player.set_choice("sm1fs_i004_totally_kb")
    $ CharacterController.get_character("am").add_point()
    return
label sm1fs_i004_m01_c03:
    $ player.set_choice("sm1fs_i004_dont_mind_kb")
    return
label sm1fs_i004_m01_c04:
    $ player.set_choice("sm1fs_i004_no_kb")
    return
label sm1fs_i004_unlocks:
    call sm1fs_i004_m01_c01 from _call_sm1fs_i004_m01_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(IT_STORY_LINE)
    return