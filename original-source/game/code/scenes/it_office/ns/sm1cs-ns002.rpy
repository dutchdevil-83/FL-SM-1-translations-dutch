image sm1cs_ns002-glambot-1 = Movie(play = "images/FS_IT/NS/s002/anim/sm1cs-ns002-a00-3x-60fps.webm", start_image = "sm1cs-ns002-a00 glambot-00-000", image = "sm1cs-ns002-a00 glambot-00-119", loop = False)
label sm1cs_ns002:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1cs-ns002-a00 glambot-00-000 with dissolve
    pause
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound sfx_camera_fly1 volume 2.0
    play sound3 ["<silence 2.5>", sfx_camera_fly1] noloop volume 2.0
    scene sm1cs_ns002-glambot-1
    pause
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-ns002-01 with dissolve
    pause
    play music music_action_fun
    play sound sfx_kick_leg1
    scene sm1cs-ns002-02 am_talk_appear_suddenly with vpunch
    play voice3 girl22_hey_loud noloop
    am "Hey."
    scene sm1cs-ns002-03 mc_talk_freakout with dissolve
    play voice2 mc_scared_huh1 noloop volume 1.5
    mc "Gah!"
    scene sm1cs-ns002-04 mc_talk_calm with dissolve
    play voice2 mc_scared_oh3 noloop
    mc "Jeez. Were you a vampire in your former life?"
    scene sm1cs-ns002-05 am_talk_deadpan with dissolve
    play voice3 girl22_yes_simple noloop
    am "Yes."
    am "Have you seen Nari?"
    scene sm1cs-ns002-06 mc_talk_thinking with dissolve
    play voice2 mc_no_no2 noloop
    mc "Uh, no. I've been kinda focused on my work."
    scene sm1cs-ns002-07 am_talk_amused with dissolve
    play voice3 girl22_arrogant_he noloop
    am "Heh. Sure you are. If you see her, can you tell her I'm looking for her?"
    scene sm1cs-ns002-08 mc_talk_grin with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Trying to drink her blood?"
    scene sm1cs-ns002-09 mc_talk_am_stonefaced with dissolve
    mc "You know, because you're a vampire?"
    scene sm1cs-ns002-10 am_talk_am_sigh with dissolve
    play voice3 girl22_no_uhuh1 noloop
    am "She wrote a piece of code, and I need to figure out how she did it. It's impressive. Way better than anything you've done so far."
    scene sm1cs-ns002-11 mc_talk_am_sigh with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Do you always insult people after asking them for help?"
    play sound sfx_cloth_rustling1 volume 1.5
    scene sm1cs-ns002-12 am_talk_punkt with dissolve
    play voice3 girl22_disappointed_geh noloop
    am "Whatever."
    scene sm1cs-ns002-13 mc_talk_thought_am_turnaround with dissolve
    mct "She might have an attitude, but I really don't need to make any enemies at work."
    scene sm1cs-ns002-14 mc_talk_thought_calling_over with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "April, if I see her, I'll let you know."
    play sound sfx_keyboard_typing2 volume 2.0
    scene sm1cs-ns002-15 am_sits with dissolve
    pause
    scene sm1cs-ns002-16 mc_thought_buzz with dissolve
    call buzz from _call_buzz_1
    queue sound sfx_message_in1
    mct "Got a text."
    scene sm1cs-ns002-17 mc_thought_look_phone with dissolve
    queue sound sfx_message_in1
    play voice2 mc_thinking_mmm4 noloop
    mct "Lot of texts."
    scene sm1cs-ns002-18 mc_thought_look_phone_tap with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Okay that sounds bad. What's with the X's?"
    mct "They're from Nari."
    scene sm1cs-ns002-19 mc_thought_look_phone_more_messages with dissolve
    play sound sfx_message_in1
    ns "Emergency XXX."
    play sound sfx_message_in1
    ns "Please [mcname]! Come to the bathroom. Don't tell Anna."
    play sound sfx_message_in1
    ns "Please hurry."
    play sound sfx_chair_slide1 volume 1.6
    scene sm1cs-ns002-20 mc_thought_walk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mct "Shit. Sounds serious."
    scene sm1cs-ns002-21 am_look_mc_talk_walk with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Oh hey! Uh, what's up? Just taking a little bathroom break. Nothing to worry about over here!"
    scene sm1cs-ns002-22 am_talk_look_screen with dissolve
    play voice3 girl22_yes_aga1 noloop
    am "Do I look worried?"
    scene sm1cs-ns002-23 mc_moving_on_frustrated with dissolve
    pause
    scene sm1cs-ns002-23-1 mc_moving_on_frustrated with dissolve
    pause
    stop sound2 fadeout 1.0
    play sound sfx_door_openclosed1
    scene sm1cs-ns002-24 mc_talkn_bathroom with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Nari?"
    scene sm1cs-ns002-25 ns_talkn_bathroom with dissolve
    play voice3 nari_yes_sad noloop
    ns "In here."
    scene sm1cs-ns002-26 bathroom_mc_look_door with dissolve
    pause
    play sound sfx_locker_open1 volume 2.0
    scene sm1cs-ns002-27 bathroom_mc_look_door_crack with dissolve
    pause
    scene sm1cs-ns002-28 bathroom_ns_talk_door_crack with dissolve
    play voice3 nari_scared_huh noloop
    ns "Are you alone?"
    scene sm1cs-ns002-29 bathroom_mc_talk_door_crack with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Yes Nari. It's just me."
    scene sm1cs-ns002-30 bathroom_ns_talk_mc_walksn with dissolve
    play voice3 nari_pain_aaa3 noloop
    ns "Quick. Lock the door behind you."
    play sound sfx_locker_open1 volume 2.0
    scene sm1cs-ns002-31 bathroom_ns_talk_mc_talk_ns_holding with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What's up with that-"
    scene sm1cs-ns002-32 bathroom_ns_talk_look_down with dissolve
    play voice3 nari_disgust_brrgh noloop
    ns "I didn't know who else to call."
    scene sm1cs-ns002-33 bathroom_mc_talk_thought with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "It's all good, Nari. What happened?"
    mct "Of course I didn't think when I offered to help I'd end up in a situation like this."
    scene sm1cs-ns002-34 bathroom_nc_talk_panicked with dissolve
    play voice3 nari_pain_sobs1 noloop
    ns "I can't say it. Oh my god. I'm totally getting fired."
    mct "She sounds completely terrified."
    scene sm1cs-ns002-35 bathroom_mc_talk_hands with dissolve
    play voice2 mc_no_no5 noloop
    mc "Nari, it's cool."
    menu:
        "I don't need to know."(hint="sm1cs_ns002_m01_h01"):
            scene sm1cs-ns002-36 bathroom_mc_talk_menu_neutral with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "Whatever is going on, you'll tell me if you want to."
        "You can tell me what happened"(hint="sm1cs_ns002_m01_h02"):
            call sm1cs_ns002_m01_c02 from _call_sm1cs_ns002_m01_c02
            scene sm1cs-ns002-36 bathroom_mc_talk_menu_neutral with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "You can tell me. I can keep a secret."
            scene sm1cs-ns002-37 bathroom_ns_talk_menu_nervous with dissolve
            play voice3 nari_pain_aaa2 noloop
            ns "I think it would be best to take this one to my death."
            scene sm1cs-ns002-38 bathroom_mc_talk_menu_nervous with dissolve
            play voice2 mc_no_nah2 noloop
            mc "Come on. Whatever deep dark thing it is, I bet I can beat you."
            scene sm1cs-ns002-39 bathroom_mc_talk_menu_chuckling with dissolve
            play voice2 mc_arrogant_heh3 noloop volume 1.4
            mc "My life got pretty crazy last year."
            scene sm1cs-ns002-40 bathroom_ns_talk_menu_nervous with dissolve
            play voice3 nari_surprised_ehh noloop
            ns "Okay. I was masturbating, and then I came so hard that I lost control and squirted all over my panties."
            scene sm1cs-ns002-41 bathroom_ns_talk_menu_mc_speechless_thought with dissolve
            play voice3 nari_sex_closedmoan2 noloop
            ns "Now they're wet. Maybe ruined. I don't know. But I can't leave this place. Which means eventually someone will find out and then I'll be fired for sure."
    scene sm1cs-ns002-42 bathroom_mc_talk_confident with dissolve
    play voice2 mc_happy_a1 noloop volume 1.4
    mc "Let's just take a beat. I'll get you through this. we've all... had urges in strange places."
    mc "First thing, maybe I should, I don't know, maybe you can get up and clean up at the sink?"
    scene sm1cs-ns002-43 bathroom_ns_talk_frozen with dissolve
    play voice3 nari_happy_relief noloop
    ns "I don't think I can move. If I move, the floor might fall out beneath me."
    scene sm1cs-ns002-44 bathroom_mc_talk_frozen with dissolve
    play voice2 mc_yes_okay2 noloop volume 1.7
    mc "Cool, cool. No moving. No need for you to, uh, move."
    scene sm1cs-ns002-45 bathroom_mc_talk_spotd with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh hey, looks like you dropped your keycard."
    play sound sfx_cloth_rustling2 volume 1.6
    scene sm1cs-ns002-46 bathroom_ns_talk_mc_reaching with dissolve
    play voice3 nari_surprised_ohmy noloop
    ns "I didn't even realize it came off. This is terrible."
    scene sm1cs-ns002-47 bathroom_mc_talk_mc_reaching with dissolve
    play voice2 mc_pain_rrrr noloop
    mc "*grunting*"
    mct "Damnit."
    scene sm1cs-ns002-48 bathroom_ns_talk_mc_reaching_close_tears with dissolve
    play voice3 nari_pain_sobs3 noloop
    ns "I just can't believe it."
    ns "All my hard work, everything I went through to get here, but I couldn't control myself."
    scene sm1cs-ns002-49 bathroom_mc_talk_mc_reaching_close_tears with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "It's going to be fine."
    scene sm1cs-ns002-49-1 bathroom_mc_talk_mc_reaching_close_tears with dissolve
    pause
    mct "Come on, man. Focus!"
    scene sm1cs-ns002-50 bathroom_ns_talk_mc_reaching_desperate with dissolve
    play voice3 nari_hey_unsure noloop
    ns "[mcname], this is serious. Right? I mean if word gets out that I masturbated at work, I'll get fired for sure right?"
    play sound sfx_skirt_off2
    scene sm1cs-ns002-51 bathroom_mc_talk_mc_getd with dissolve
    play voice2 d2s12_emmm noloop
    mc "It's going to be all right, Nari. You just got to calm down."
    mc "And we both just have to pray super hard that no one else comes along."
    scene sm1cs-ns002-52 bathroom_ns_talk_mc_getd with dissolve
    play voice3 nari_surprised_huh2 noloop
    ns "Why \"both\"? You weren't doing something wrong."
    play sound sfx_cloth_rustling1 volume 1.5
    scene sm1cs-ns002-53 bathroom_mc_talk_mc_getd with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, but this could be a bad look for me for... so many reasons."
    scene sm1cs-ns002-54 bathroom_ns_talk_freakout with dissolve
    play voice3 nari_scared_ho noloop
    ns "Oh no! Now I'm going to get you fired, too."
    play sound sfx_cloth_rustling3 volume 1.5
    scene sm1cs-ns002-55 bathroom_mc_talk_hand_shoulder with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "No one is getting fired, Nari."
    scene sm1cs-ns002-56 bathroom_ns_talk_hand_shoulder with dissolve
    play voice3 nari_thinking_emm noloop
    ns "How do you know, [mcname]?"
    scene sm1cs-ns002-57 bathroom_mc_thought_look with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Shit. I didn't realize just how close I'd be this close to Nari's bare pussy."
    scene sm1cs-ns002-58 bathroom_mc_talk_look_up with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "Nari. Say it with me. \"This is going to be fine.\""
    scene sm1cs-ns002-59 bathroom_ns_talk_look_up with dissolve
    play voice3 nari_surprised_ah noloop
    ns "But what if it's not?"
    scene sm1cs-ns002-60 bathroom_mc_talk_look_up with dissolve
    play voice2 mc_no_no4 noloop
    mc "Come on. Just say it. \"This is going to be fine.\""
    scene sm1cs-ns002-61 bathroom_ns_talk_deep_breadth with dissolve
    pause
    scene sm1cs-ns002-62 bathroom_ns_talk_look_mc with dissolve
    play voice3 nari_happy_phew noloop
    ns "This is going to be fine."
    scene sm1cs-ns002-63 bathroom_mc_talk_look_mc with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Good, good. One more time. This is going to be fine."
    scene sm1cs-ns002-64 bathroom_ns_talk_relaxed with dissolve
    play voice3 nari_happy_mmm noloop
    ns "This is going to be fine."
    scene sm1cs-ns002-65 bathroom_mc_talk_relaxed with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Phew. Okay, got your ID card. What's next?"
    scene sm1cs-ns002-66 bathroom_mc_talk_smelling_air with dissolve
    play voice2 d14s16_smell noloop
    mc "*sniffs* Uh, first I- Hmm. Let's get you cleaned up."
    play sound sfx_locker_open1 volume 1.5
    scene sm1cs-ns002-67 bathroom_ns_talk_mc_stepping_out with dissolve
    play voice3 nari_yes_emotional noloop
    ns "Yes. Sorry. I can uh... I can squirt a lot."
    scene sm1cs-ns002-68 bathroom_mc_talk_mc_stepping_out with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "I didn't notice. It's no problem."
    play sound sfx_toilet_paper_rip1 volume 2.0
    scene sm1cs-ns002-69 bathroom_mc_grabbing towel with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-ns002-70 bathroom_mc_talk_return with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "I gotcha covered."
    scene sm1cs-ns002-71 bathroom_ns_talk_grabbing with dissolve
    play voice3 nari_thinking_mff noloop
    ns "Thank you..."
    play sound sfx_cloth_wiping1 volume 2.0
    scene sm1cs-ns002-72 bathroom_mc_thought_turn_around with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Nothing to see here."
    scene sm1cs-ns002-73 bathroom_mc_thought_turn_around_smell with dissolve
    mct "Damn. I can still smell her panties from here."
    stop sound fadeout 1.0
    scene sm1cs-ns002-74 bathroom_ns_talk_standing with dissolve
    play voice3 nari_disappointed_eh noloop
    ns "I'm so sorry about pulling you into this, [mcname]."
    scene sm1cs-ns002-75 bathroom_mc_talk_standing with dissolve
    play voice2 d1s2_mchey noloop volume 1.6
    mc "All good. What are friends for?"
    scene sm1cs-ns002-76 bathroom_ns_talk_nods with dissolve
    play voice3 nari_happy_relief noloop
    ns "I feel much better already. Thank you so much, [mcname]."
    scene sm1cs-ns002-77 bathroom_mc_talk_friendly with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "Don't mention it."
    mc "There. Everything is back to normal. You with your badge, looking cute as a peach."
    scene sm1cs-ns002-78 bathroom_ns_talkd_on with dissolve
    play voice3 nari_disappointed_huh noloop
    ns "Cute as a peach?"
    play sound sfx_hair_scratch1 volume 1.5
    scene sm1cs-ns002-79 bathroom_mc_talk_rub_back with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Oh it's uh, just an expression. Like uh, life's a peach."
    scene sm1cs-ns002-80 bathroom_ns_talk_smile with dissolve
    play voice3 nari_yes_aga2 noloop
    ns "Of course."
    play sound sfx_cloth_rustling4 volume 1.6
    scene sm1cs-ns002-81 bathroom_ns_hug with dissolve
    play voice3 nari_sex_closedmoan4 noloop
    pause
    scene sm1cs-ns002-82 bathroom_mc_thought_hug_sniff with dissolve
    play voice2 d14s16_smell noloop
    mc "*Sniffs*"
    mct "Raise up the flag, Captain!"
    scene sm1cs-ns002-83 bathroom_mc_talk_hug_sniff with dissolve
    play voice2 d1s5b_emmm noloop
    mc "Nari. Panties. Red alert."
    play sound sfx_cloth_planket2
    scene sm1cs-ns002-84 bathroom_ns_talk_pull_back with dissolve
    play voice3 nari_surprised_oh noloop
    ns "Oh!"
    ns "I swear I'm not trying to pull anything. Not that I don't think you're worthy of seduction."
    scene sm1cs-ns002-85 bathroom_ns_talk_hold with dissolve
    play voice3 nari_surprised_ehh noloop
    ns "Not that I'm trying to seduce you. If I were trying to seduce you, I'd do something much better and much less embarrassing than this."
    scene sm1cs-ns002-86 bathroom_mc_talk_hands_up with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Nari, Nari. It's okay. I'm happy you think I'm worthy of seduction."
    scene sm1cs-ns002-87 bathroom_ns_talk_exasperated with dissolve
    play voice3 nari_disappointed_mff noloop
    ns "I... I really need to get out of this stall."
    scene sm1cs-ns002-88 bathroom_ns_look_down with dissolve
    pause
    scene sm1cs-ns002-89 bathroom_ns_look_up with dissolve
    pause
    scene sm1cs-ns002-90 bathroom_mc_talk_confused with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Nari?"
    play sound sfx_comic_boner1
    scene sm1cs-ns002-91 bathroom_mc_look_down with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Ah."
    scene sm1cs-ns002-92 bathroom_mc_talk_mc_cover_up_ns_look_up with dissolve
    play voice2 d2s9_confused noloop
    mc "So we should probably leave and, uh, get out of here without anyone noticing."
    scene sm1cs-ns002-93 bathroom_mc_talk_mc_cover_up_ns_look_up with dissolve
    mc "Uh... You should probably go out first, Nari. I need to hang here for a bit."
    scene sm1cs-ns002-94 bathroom_nc_talk_concerned with dissolve
    play voice3 nari_disgust_ergh noloop
    ns "[mcname]... I'm still very nervous. I can walk out there and sit down, and then I'll have to finish without any panties on."
    scene sm1cs-ns002-95 bathroom_mc_talk with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "You've never done that before?"
    scene sm1cs-ns002-96 bathroom_ns_talk_kinky_smile with dissolve
    play voice3 nari_happy_laugh1 noloop
    ns "Well, I have thought about it, but I always planned to do it near the end of the day."
    scene sm1cs-ns002-97 bathroom_mc_talk_kinky_smile with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Well, here is your chance. Unless you have a better idea."
    scene sm1cs-ns002-98 bathroom_ns_talk_kinky_smile with dissolve
    play voice3 nari_no_unsure noloop
    ns "No. I've already been absent long enough. I can't let Anna think I'm slacking off."
    scene sm1cs-ns002-99 bathroom_mc_talk_kinky_smile with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, especially since you were jacking off."
    scene sm1cs-ns002-100 bathroom_ns_talk_blush with dissolve
    play voice3 nari_angry_fff noloop
    ns "[mcname]!"
    scene sm1cs-ns002-101 bathroom_mc_talk_blush with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "I'm sorry. I couldn't help it."
    scene sm1cs-ns002-102 bathroom_ns_talk_panicked_mc_back with dissolve
    play voice3 nari_angry_breathing noloop
    ns "Oh my god. This is it. It's not going to work."
    scene sm1cs-ns002-103 bathroom_mc_talk_panicked_mc_back with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "Listen, it's not all that bad. Later, we're totally going to laugh at this."
    scene sm1cs-ns002-104 bathroom_ns_talk_look_away with dissolve
    play voice3 nari_no_expressive noloop
    ns "No we won't. But I'm sure you'll laugh about it with others."
    scene sm1cs-ns002-105 bathroom_mc_talk_look_away with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I'm not going to tell anyone about this, Nari."
    scene sm1cs-ns002-106 bathroom_ns_talk_look_mc with dissolve
    play voice3 nari_pain_sobs1 noloop
    ns "*sniffs* Really?"
    scene sm1cs-ns002-107 bathroom_mc_talk_cross_heart with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Cross my heart and hope to die. It will forever be just a fun work secret between the two of us."
    scene sm1cs-ns002-108 bathroom_ns_talk_cross_heart with dissolve
    play voice3 nari_arrogant_heh noloop
    ns "You really think I can handle spending the rest of my day with... without panties?"
    scene sm1cs-ns002-109 bathroom_mc_talk_cross_heart with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "I know you can. Remember, you told me how important this job is. If you just keep your cool, everything is going to be fine."
    scene sm1cs-ns002-110 bathroom_ns_talk_nods with dissolve
    play voice3 nari_happy_phew noloop
    ns "Okay. Maybe... maybe it will all work out. Thank you, [mcname]."
    scene sm1cs-ns002-111 bathroom_mc_talk_thumbs_up with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "No problem. Like I said, one day, we'll laugh about this."
    scene sm1cs-ns002-112 bathroom_ns_talk_look_panties with dissolve
    play voice3 nari_thinking_hmm3 noloop
    ns "What do I do about these?"
    scene sm1cs-ns002-113 bathroom_mc_thinking with dissolve
    pause
    scene sm1cs-ns002-114 bathroom_mc_talk_point with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Stow them here. The cleaner they use in this place is so strong, it should cover up the scent."
    play sound sfx_bed_slide3 volume 0.5
    scene sm1cs-ns002-115 bathroom_ns_talk_puts_between with dissolve
    play voice3 nari_yes_confident noloop
    ns "And then what?"
    scene sm1cs-ns002-116 bathroom_mc_talk_puts_between with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Get a plastic bag from the breakroom when you're about to leave for the day. Then you can-"
    play sound sfx_toilet_flush1
    scene sm1cs-ns002-117 bathroom_ns_talk_puts_between with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Bag them up and hide them in my purse. No one can smell them through the bag."
    scene sm1cs-ns002-118 bathroom_mc_talk_puts_between_bingo with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Bingo."
    scene sm1cs-ns002-119 bathroom_ns_talk_finishes with dissolve
    play voice3 nari_disgust_oogh noloop
    ns "Oh god, I hope this works."
    play sound sfx_locker_open1 volume 1.5
    scene sm1cs-ns002-120 bathroom_mc_talk_finishes with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Me too."
    scene sm1cs-ns002-121 bathroom_mc_next_door with dissolve
    pause
    scene sm1cs-ns002-122 bathroom_mc_next_door_listening with dissolve
    play voice2 mc_angry_huh1 noloop
    mct "No one is close. I hope"
    scene sm1cs-ns002-123 bathroom_mc_talk_thought_next_door_look_ns_walk_awkward with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Coast is clear."
    scene sm1cs-ns002-124 bathroom_mc_thought_next_door_look_ns_walk_awkward with dissolve
    play voice3 nari_sex_closedmoan6 noloop
    ns "..."
    mct "She looks like she has as stick up her ass."
    scene sm1cs-ns002-125 bathroom_mc_talk_next_door_look_ns_walk_awkward with dissolve
    play voice2 d1s5_mcthinks noloop volume 2.0
    mc "*whispers* Pssst. Nari. Act casual."
    scene sm1cs-ns002-126 bathroom_ns_talk_next_door_terrified with dissolve
    play voice3 nari_thinking_hmm2 noloop
    ns "*whispers* I've never acted so casual that I didn't wear panties at my job."
    play sound sfx_door_openclosed1
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1cs-ns002-127 bathroom_mc_talk_office with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Remember, just take it one step at a time. You're just coming back from the bathroom. Everything is good."
    scene sm1cs-ns002-128 bathroom_ns_talk_office with dissolve
    play voice3 nari_yes_sad noloop
    ns "Yes. One step at a time."
    scene sm1cs-ns002-129 bathroom_office_awkward_walk with dissolve
    pause
    scene sm1cs-ns002-130 bathroom_office_madet_mc_thought with dissolve
    play voice2 d1s1_mmm noloop
    mct "We made it."
    scene sm1cs-ns002-131 bathroom_office_madet_april_talk with dissolve
    play voice4 girl22_arrogant_hm noloop
    am "*sniffs* You guys smell something?"
    scene sm1cs-ns002-132 bathroom_office_madet_mc_talk with dissolve
    play voice2 mc_no_nope2 noloop
    mc "Nope."
    play sound sfx_skirt_off2
    play sound3 sfx_chair_slide1 noloop volume 1.6
    scene sm1cs-ns002-133 bathroom_office_ns_working with dissolve
    pause
    stop music fadeout 3.0
    stop sound2 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(NS_STORY, 0, 30, 3)
    return
label sm1cs_ns002_m01_c02:
    $ player.set_choice("sm1cs_ns002_tell_me")
    return
label sm1cs_ns002_unlocks:
    call sm1cs_ns002_m01_c02 from _call_sm1cs_ns002_m01_c02_1
    if config_storyline_mode is True:
        $ execute_storyline_config(NS_STORY)
    return