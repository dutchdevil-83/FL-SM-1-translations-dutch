image sm1cs_bg003-glambot-1 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a57-2x-50fps.webm", start_image = "sm1cs-bg003-a57 mc-woah-glambot-00_i", image = "sm1cs-bg003-a57 mc-woah-glambot-80_i", loop = False)
image sm1cs_bg003-a165-1 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a165-1-2x-50fps.webm", start_image = "sm1cs-bg003-a165-1 mc-bg-hj-anim-01")
image sm1cs_bg003-a165-1-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a165-1-2x-60fps.webm", start_image = "sm1cs-bg003-a165-1 mc-bg-hj-anim-01")
image sm1cs_bg003-a165-2 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a165-2-2x-50fps.webm", start_image = "sm1cs-bg003-a165-2 mc-bg-hj-anim-01")
image sm1cs_bg003-a165-2-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a165-2-2x-60fps.webm", start_image = "sm1cs-bg003-a165-2 mc-bg-hj-anim-01")
image sm1cs_bg003-a165-3 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a165-3-2x-50fps.webm", start_image = "sm1cs-bg003-a165-3 mc-bg-hj-anim-01")
image sm1cs_bg003-a165-3-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a165-3-2x-60fps.webm", start_image = "sm1cs-bg003-a165-3 mc-bg-hj-anim-01")
image sm1cs_bg003-a165-4 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a165-4-2x-50fps.webm", start_image = "sm1cs-bg003-a165-4 mc-bg-hj-anim-01")
image sm1cs_bg003-a165-4-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a165-4-2x-60fps.webm", start_image = "sm1cs-bg003-a165-4 mc-bg-hj-anim-01")
image sm1cs_bg003-a191-1 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a191-1-2x-50fps.webm", start_image = "sm1cs-bg003-a191-1 mc-bg-titjob-anim-01")
image sm1cs_bg003-a191-1-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a191-1-2x-60fps.webm", start_image = "sm1cs-bg003-a191-1 mc-bg-titjob-anim-01")
image sm1cs_bg003-a191-2 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a191-2-2x-50fps.webm", start_image = "sm1cs-bg003-a191-2 mc-bg-titjob-anim-01")
image sm1cs_bg003-a191-2-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a191-2-2x-60fps.webm", start_image = "sm1cs-bg003-a191-2 mc-bg-titjob-anim-01")
image sm1cs_bg003-a191-3 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a191-3-2x-50fps.webm", start_image = "sm1cs-bg003-a191-3 mc-bg-titjob-anim-01")
image sm1cs_bg003-a191-3-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a191-3-2x-60fps.webm", start_image = "sm1cs-bg003-a191-3 mc-bg-titjob-anim-01")
image sm1cs_bg003-a204-1 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a204-1-2x-50fps.webm", start_image = "sm1cs-bg003-a204-1 mc-bg-bj-anim-01")
image sm1cs_bg003-a204-1-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a204-1-2x-60fps.webm", start_image = "sm1cs-bg003-a204-1 mc-bg-bj-anim-01")
image sm1cs_bg003-a204-2 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a204-2-2x-50fps.webm", start_image = "sm1cs-bg003-a204-2 mc-bg-bj-anim-01")
image sm1cs_bg003-a204-2-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a204-2-2x-60fps.webm", start_image = "sm1cs-bg003-a204-2 mc-bg-bj-anim-01")
image sm1cs_bg003-a204-3 = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a204-3-2x-50fps.webm", start_image = "sm1cs-bg003-a204-3 mc-bg-bj-anim-01")
image sm1cs_bg003-a204-3-f = Movie(play = "images/Character-Scenes/BG/s003/anim/sm1cs-bg003-a204-3-2x-60fps.webm", start_image = "sm1cs-bg003-a204-3 mc-bg-bj-anim-01")
label sm1cs_bg003:
    $ bg_mcname = None
    play sound sfx_heels_steps2 loop
    scene sm1cs-bg003-01 kv-asking with dissolve
    play voice4 kanya_yes_yeah5 noloop
    kv "Yeah? What?"
    scene sm1cs-bg003-02 bg-asking with dissolve
    play voice3 girl26_thinking_ehh2 noloop
    bg "You haven't shown [mcname] the photos yet?"
    scene sm1cs-bg003-03 kv-talking with dissolve
    play voice4 kanya_no_uhuh4 noloop
    kv "I, like, just finished them."
    scene sm1cs-bg003-04 bg-talking with dissolve
    play voice3 girl26_hey_greeting noloop
    bg "Come on! We have to show him!"
    scene sm1cs-bg003-05 kv-talking with dissolve
    play voice4 kanya_yes_aga4 noloop
    kv "All right, don't get your panties in a twist, Amore."
    scene sm1cs-bg003-06 bg-defending-herself with dissolve
    play voice3 girl26_happy_laugh1 noloop
    bg "What! I'm just excited!"
    stop sound fadeout 1.5
    scene sm1cs-bg003-07 bg-mc-talking with dissolve
    play voice3 girl26_disappointed_oh noloop
    bg "I think they turned out so good."
    scene sm1cs-bg003-08 bg-mc-talking with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "I can tell."
    scene sm1cs-bg003-09 mc-excited with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "And there's nothing wrong with that! I have to say I'm pretty excited to see them."
    scene sm1cs-bg003-10 bg-smirking with dissolve
    play voice3 girl26_arrogant_hah noloop
    bg "Oh yeah?"
    scene sm1cs-bg003-11 mc-excited with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah! Are you kidding me? I bet they look super hot."
    play sound sfx_phone_tapping1 volume 2.0 loop
    scene sm1cs-bg003-12 kv-see-for-yourself with dissolve
    play voice4 kanya_arrogant_ha noloop
    kv "Well, you can see for yourself."
    stop sound fadeout 1.0
    scene sm1cs-bg003-13 mc-woah with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Wow..."
    scene sm1cs-bg003-14 bg-proud with dissolve
    play voice3 girl26_arrogant_yeah noloop
    bg "Right!?"
    play sound sfx_remote_button1
    scene sm1cs-bg003-15 mc-looking-at-pictures with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "Those are..."
    play sound sfx_remote_button1
    scene sm1cs-bg003-16 mc-looking-at-pictures with dissolve
    play voice2 mc_angry_errr8 noloop
    mc "Holy shit."
    play sound sfx_remote_button1
    scene sm1cs-bg003-17 mc-looking-at-pictures with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Those are {i}super{/i} hot."
    play voice3 girl26_yes_yep noloop
    bg "And that's not even my favorite one!"
    play voice4 kanya_yes_aga3 noloop
    kv "Mine neither."
    play sound sfx_remote_button1
    scene sm1cs-bg003-18 mc-looking-at-pictures with dissolve
    play voice2 mc_angry_errr6 noloop
    mc "Goddamn..."
    play sound sfx_remote_button1
    scene sm1cs-bg003-19 mc-looking-at-pictures with dissolve
    play voice3 girl26_yes_aga noloop
    bg "Uh huh. We nailed this shoot."
    play sound sfx_remote_button1
    scene sm1cs-bg003-20 mc-looking-at-pictures with dissolve
    play voice4 kanya_thinking_hmm1 noloop
    kv "You both really did. But..."
    play sound sfx_remote_button1
    scene sm1cs-bg003-21 mc-looking-at-pictures with dissolve
    play voice4 kanya_disappointed_oof noloop
    kv "This one is probably my favorite."
    play voice3 girl26_happy_yeah noloop
    bg "Same."
    play sound sfx_remote_button1
    scene sm1cs-bg003-22 mc-looking-at-pictures with dissolve
    pause
    play sound sfx_remote_button1
    scene sm1cs-bg003-23 mc-looking-at-pictures with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Kanya... these are incredible."
    play sound sfx_cloth_rustling2
    scene sm1cs-bg003-24 kv-talking with dissolve
    play voice4 kanya_happy_laugh1 noloop
    kv "I know."
    scene sm1cs-bg003-25 mc-praising with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Seriously... you did an incredible job."
    scene sm1cs-bg003-26 kv-nah-its-you-guys with dissolve
    play voice4 kanya_hey_long noloop
    kv "Hey, a photographer can only achieve greatness if her models are great. And you two showed some real chemistry."
    scene sm1cs-bg003-27 mc-really with dissolve
    play voice2 d1s2_hmm noloop
    mc "You think so?"
    scene sm1cs-bg003-28 kv-talking with dissolve
    play voice4 kanya_no_nah2 noloop
    kv "I don't need to \"think\". I have evidence."
    scene sm1cs-bg003-29 bg-agreeing with dissolve
    play voice3 girl26_yes_yeah noloop
    bg "Yeah..."
    scene sm1cs-bg003-30 kv-cmon with dissolve
    play voice4 kanya_arrogant_huh noloop
    kv "Come on, out with it."
    scene sm1cs-bg003-31 mc-huh with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Out with what?"
    scene sm1cs-bg003-32 kv-mc-talking with dissolve
    play voice4 kanya_thinking_eeh1 noloop
    kv "Our little resident freak has something she wants to ask you."
    play sound sfx_cloth_rustling3
    scene sm1cs-bg003-33 mc-bg-talking with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Oh yeah?"
    scene sm1cs-bg003-34 mc-bg-talking with dissolve
    play voice3 girl26_thinking_hmm2 noloop
    bg "Uhm..."
    bg "I was wondering if you wanted to do another shoot..."
    scene sm1cs-bg003-35 mc-astonished with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Really?"
    scene sm1cs-bg003-36 bg-i-want-more with dissolve
    play voice3 girl26_yes_simple noloop
    bg "The last one was... it was incredible."
    bg "I've never felt so... hot. And I want to do it again."
    scene sm1cs-bg003-37 mc-agreeing with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay! Yeah, I'd love to!"
    scene sm1cs-bg003-38 bg-excited with dissolve
    play voice3 girl26_happy_yay noloop
    bg "Awesome!"
    play sound sfx_heels_steps1
    scene sm1cs-bg003-39 kv-talking with dissolve
    stop sound fadeout 3.0
    play voice4 kanya_yes_yep1 noloop
    kv "Let me grab my camera and we can get going!"
    kv "But you and Amore need to change, [mcname]."
    scene sm1cs-bg003-40 mc-huh with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Huh?"
    scene sm1cs-bg003-41 kv-talking with dissolve
    play voice4 kanya_thinking_hmm4 noloop
    kv "You've got an outfit to put on."
    scene sm1cs-bg003-42 mc-really with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Oh. Really?"
    play sound sfx_heels_steps2 loop
    scene sm1cs-bg003-43 kv-talking-while-walking with dissolve
    play voice4 kanya_yes_yeah3 noloop
    kv "Yeah, Mr. Model! Time to strut your stuff!"
    stop sound fadeout 3.0
    scene sm1cs-bg003-44 mc-thinking with dissolve
    play voice2 mc_thinking_hm noloop
    mct "I wonder what these two have in store for me..."
    mct "Only one way to find out."
    $ renpy.music.set_volume(0.65, 0.0, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play sound sfx_heels_steps2 fadein 1.0 loop
    scene sm1cs-bg003-46 mc-entry with Fade(0.5, 0.5, 0.5)
    play music music_sexymassive_b
    pause
    scene sm1cs-bg003-47 kv-oh-la-la with dissolve
    play voice4 kanya_surprised_ohmy noloop
    kv "Owww, owwwww! Look at you!"
    scene sm1cs-bg003-48 mc-thanks with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Thanks, Kanya."
    scene sm1cs-bg003-49 kv-asking with dissolve
    play voice4 kanya_arrogant_laugh noloop
    kv "How's it fit?"
    stop sound fadeout 1.0
    scene sm1cs-bg003-50 mc-kv-talking with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "Shockingly well, actually."
    play voice4 kanya_yes_yep2 noloop
    kv "I had to guess your measurements a bit."
    scene sm1cs-bg003-51 mc-looking-around with dissolve
    pause
    scene sm1cs-bg003-52 kv-curious with dissolve
    play voice4 kanya_thinking_eeh5 noloop
    kv "What?"
    scene sm1cs-bg003-53 mc-talking with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I'm just looking for Amore. If this is my outfit, I wonder what she's going to be wearing."
    scene sm1cs-bg003-54 kv-talking with dissolve
    play voice4 kanya_disappointed_oh noloop
    kv "Oh, I think you're going to {i}love{/i} it."
    scene sm1cs-bg003-55 kv-you-will-love-it with dissolve
    play voice4 kanya_happy_relief2 noloop
    kv "And it doesn't look like you'll have to wait long to find out!"
    play sound sfx_barefoot_steps1 loop
    scene sm1cs-bg003-56 kv-you-will-love-it with dissolve
    pause
    jump sm1cs_bg003_bg_appears
label sm1cs_bg003_bg_appears:
    scene sm1cs-bg003-a57 mc-woah-glambot-00_i with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh..."
    play sound sfx_camera_fly1 volume 2.0
    scene sm1cs_bg003-glambot-1
    pause
    play voice4 kanya_yes_ugu1 noloop
    kv "I told you, you'd like it."
    stop sound fadeout 1.0
    scene sm1cs-bg003-58 mc-wow with dissolve
    play voice2 mc_happy_wow1 noloop
    mc "Wow, Amore..."
    scene sm1cs-bg003-59 bg-nervous with dissolve
    play voice3 girl26_happy_mmf noloop
    bg "I just wanted to... spice things up."
    scene sm1cs-bg003-60 mc-liking-it with dissolve
    play voice2 d9s2_ugu noloop volume 1.6
    mc "I like it."
    scene sm1cs-bg003-61 bg-blushing with dissolve
    play voice3 girl26_disappointed_huh noloop
    bg "Yeah?"
    scene sm1cs-bg003-62 mc-talking with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah. You look fucking great!"
    scene sm1cs-bg003-63 bg-complimenting with dissolve
    play voice3 girl26_happy_relief2 noloop
    bg "Thanks. You clean up nicely too."
    scene sm1cs-bg003-64 mc-talking with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Oh yeah? Should I wear suits more often?"
    scene sm1cs-bg003-65 mc-posing with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "An international man of intrigue."
    scene sm1cs-bg003-66 bg-laughing with dissolve
    play voice3 girl26_happy_laugh2 noloop
    bg "Hehehehehe."
    scene sm1cs-bg003-67 kv-alr-lets-start with dissolve
    play voice4 kanya_hey_arrogant noloop
    kv "All right, knock it off. We have a photoshoot to do!"
    kv "So first, [mcname] take a seat, and Amore lay across his lap."
    scene sm1cs-bg003-70 bg-agreeing with dissolve
    play voice3 girl26_yes_yep noloop
    bg "Okay!"
    play sound sfx_cloth_rustling4
    scene sm1cs-bg003-71 kv-directing with dissolve
    play voice4 kanya_thinking_hmm3 noloop
    kv "Now [mcname]... put one hand on her ass, and one around her throat."
    play sound sfx_hands_clap3
    scene sm1cs-bg003-72 mc-like-this with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Like this?"
    scene sm1cs-bg003-73 kv-directing with dissolve
    play voice4 kanya_yes_yeah1 noloop
    kv "Yeah... just like that. And Amore, arch your back...{w} a little more...{w} Perfect."
    play sound sfx_photocamera_zoom2
    scene sm1cs-bg003-74 kv-clicking with dissolve
    pause
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-75 mc-bg-first-photo with dissolve
    pause
    scene sm1cs-bg003-76 kv-complimenting with dissolve
    play voice4 kanya_sex_closedmoan1 noloop
    kv "Fuck yes..."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-77 mc-asking with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "It looking good?"
    play sound sfx_photocamera_zoom4
    scene sm1cs-bg003-76 kv-complimenting with dissolve
    play voice4 kanya_happy_yeah noloop
    kv "If by good you mean \"incredibly hot\", then yes. It looks {i}fucking great!{/i}"
    scene sm1cs-bg003-78 mc-great with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Awesome!"
    scene sm1cs-bg003-79 kv-directing with dissolve
    play voice4 kanya_disappointed_hm noloop
    kv "Now, Amore... get on your knees, looking up at [mcname]. [mcname], stand up."
    play sound sfx_cloth_rustling3
    scene sm1cs-bg003-80 bg-asking with dissolve
    play voice3 girl26_thinking_hmm1 noloop
    bg "This a good position?"
    play sound sfx_photocamera_zoom3
    scene sm1cs-bg003-81 kv-directing with dissolve
    play voice4 kanya_yes_long noloop
    kv "That's perfect. And [mcname], take one finger, and put it under her chin. Make her look up at you."
    scene sm1cs-bg003-82 kv-great with dissolve
    play voice4 kanya_hey_simple1 noloop
    kv "Hold that! Hold that! Perfect!"
    scene sm1cs-bg003-83 mc-bg-second-photo with dissolve
    pause
    scene sm1cs-bg003-84 kv-great with dissolve
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    play voice4 kanya_sex_closedmoan2 noloop
    kv "Fuuuuuuck!"
    scene sm1cs-bg003-85 mc-asking with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "That good?"
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-86 kv-yep with dissolve
    play voice4 kanya_happy_relief1 noloop
    kv "You have no idea!"
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-87 bg-enjoying with dissolve
    play voice3 girl26_sex_closedmoan1 noloop
    bg "Mmmmmmm."
    scene sm1cs-bg003-88 mc-huh with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Huh?"
    scene sm1cs-bg003-89 bg-enjoying with dissolve
    play voice3 girl26_surprised_ehh2 noloop
    bg "Uh-nothing. Just... enjoying the shoot is all."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-90 mc-good with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Good!"
    scene sm1cs-bg003-91 kv-clicking-pictures with dissolve
    play voice4 kanya_thinking_eeh3 noloop
    kv "Aaaaaaand, great. On to the next pose..."
    scene sm1cs-bg003-92 kv-directing with dissolve
    play voice4 kanya_yes_yeah2 noloop
    kv "Okay, [mcname], you can sit back down... and Amore, stay on your knees but spin to face me."
    kv "Yeah, just like that. Now, [mcname], I want you to take one hand and wrap it around her throat, and with your other hand I want you to grab one of her tits."
    play sound sfx_cloth_rustling4
    scene sm1cs-bg003-93 mc-bg-third-picture with dissolve
    play voice4 kanya_disappointed_oof noloop
    kv "Ooooo, fuck that looks hot. Now, Amore... I don't exist. You're here just for [mcname]. You're his."
    play sound sfx_photocamera_zoom2
    scene sm1cs-bg003-94 kv-talking with dissolve
    play voice4 kanya_yes_simple noloop
    kv "You exist to serve him, you're his plaything, his toy, his highest fantasy, sexual slave... Make me believe it..."
    kv "Yeah, that's the look!"
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-95 mc-huh with dissolve
    play voice4 kanya_sex_closedmoan5 noloop
    kv "God, I'm going to be using these later..."
    play voice2 mc_arrogant_huh3 noloop
    mc "Huh?"
    scene sm1cs-bg003-96 kv-explaining with dissolve
    play voice4 kanya_pain_sobs3 noloop
    kv "This is preem jilling material. I'm going to have to rub one out so hard to this... you both look so hot."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-97 mc-okay with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh. Well, good!"
    play voice4 kanya_sex_closedmoan4 noloop
    kv "And how are you doing, Amore?"
    play voice3 girl26_sex_closedmoan2 noloop
    bg "I-I'm good!"
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    play sound sfx_cloth_rustling2
    scene sm1cs-bg003-98 kv-asking with dissolve
    play voice4 kanya_angry_hm noloop
    kv "Are you?"
    scene sm1cs-bg003-99 bg-replying with dissolve
    play voice3 girl26_yes_active noloop
    bg "Yeah! I'm really, really good..."
    scene sm1cs-bg003-100 kv-are-you-sure with dissolve
    play voice4 kanya_yes_aga4 noloop
    kv "Uh huuuuuuuh."
    scene sm1cs-bg003-101 kv-okay-relax with dissolve
    play voice4 kanya_happy_relief3 noloop
    kv "Okay, you two can relax for a second."
    play sound sfx_cloth_rustling1
    scene sm1cs-bg003-102 bg-asking with dissolve
    play voice3 girl26_surprised_ehh1 noloop
    bg "Can we see a sneak peek of what we've shot so far?"
    scene sm1cs-bg003-103 kv-smirking with dissolve
    play voice4 kanya_no_nonono2 noloop
    kv "No, ma'am. Because we still have more shooting to do!"
    scene sm1cs-bg003-104 mc-asking with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Oh yeah? What's next?"
    scene sm1cs-bg003-105 kv-idea with dissolve
    play voice4 kanya_thinking_hmm2 noloop
    kv "Well..."
    kv "I did have one small idea..."
    jump sm1cs_bg003_whipping
label sm1cs_bg003_whipping:
    play sound sfx_metal_chain1
    play sound2 sfx_skirt_off2 noloop
    scene sm1cs-bg003-106 kv-how-about-these with dissolve
    play voice4 kanya_happy_laugh2 noloop
    kv "How do you two feel about using props?"
    scene sm1cs-bg003-107 mc-not-what-i-saw-coming with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Oh, that's not exactly what I thought was coming next."
    scene sm1cs-bg003-108 kv-asking with dissolve
    play voice4 kanya_disappointed_eeh noloop
    kv "You're trying to tell me that during a dom sub photoshoot, you didn't expect to see any impact toys?"
    scene sm1cs-bg003-109 mc-explaining with dissolve
    play voice2 d2s12_emmm noloop
    mc "I mean... I just wasn't sure if Amore was going to be comfortable with it."
    play sound sfx_cloth_shuffle1
    scene sm1cs-bg003-110 kv-smirking with dissolve
    stop sound fadeout 1.0
    play voice4 kanya_happy_laugh3 noloop
    kv "Oh, this was {i}her{/i} idea."
    scene sm1cs-bg003-111 mc-bg-talking with dissolve
    play voice2 mc_angry_really noloop
    mc "Really?"
    play voice3 girl26_happy_yeah noloop
    bg "Yeah... unless you're not into it! We can totally do something else."
    scene sm1cs-bg003-112 mc-bg-talking with dissolve
    play voice2 mc_no_nono1 noloop
    mc "No, no! I'm totally down. I just wanted to make sure you were comfortable with it."
    scene sm1cs-bg003-113 mc-bg-talking with dissolve
    play voice3 girl26_yes_aga noloop
    bg "Uh huh. I'm excited for it even."
    scene sm1cs-bg003-114 mc-bg-talking with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Well, who am I to deny a sexy creature such as yourself?"
    scene sm1cs-bg003-115 kv-giving-it with dissolve
    play voice4 kanya_thinking_hmm3 noloop
    kv "Here you go, [mcname]!"
    play sound sfx_cloth_rustling5
    scene sm1cs-bg003-116 mc-thanks with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Thanks."
    play sound sfx_photocamera_zoom1
    scene sm1cs-bg003-117 kv-directing with dissolve
    play voice4 kanya_yes_active noloop
    kv "So now... [mcname] sit back down, and hold the riding crop by your leg. Think \"powerful\"."
    kv "And Amore... kneel in front of him. Yeah, nailed it."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-118 mc-bg-fourth-picture with dissolve
    play voice4 kanya_sex_closedmoan3 noloop
    kv "Oh yeah... this was a good idea."
    scene sm1cs-bg003-119 kv-talking with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "It looking good?"
    play voice4 kanya_surprised_oh noloop
    kv "Oh, it definitely is. And I don't think I'm the only one excited about it."
    scene sm1cs-bg003-120 mc-asking with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "What do you mean?"
    scene sm1cs-bg003-121 kv-answering with dissolve
    play voice4 kanya_thinking_eeh2 noloop
    kv "I don't know, maybe you should ask Amore."
    scene sm1cs-bg003-122 mc-wdym with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Amore?"
    scene sm1cs-bg003-124 bg-close-up with dissolve
    play voice3 girl26_sex_closedmoan5 noloop
    bg "Hmmm?"
    scene sm1cs-bg003-125 mc-bg-talking with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.5
    mc "You okay?"
    scene sm1cs-bg003-126 bg-talking with dissolve
    play voice3 girl26_surprised_oh noloop
    bg "Oh, uhm - yeah!"
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-127 mc-bg-talking with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "You're staring at the riding crop?"
    scene sm1cs-bg003-129 bg-answering with dissolve
    play voice3 girl26_surprised_huh2 noloop
    bg "Am I?"
    scene sm1cs-bg003-128 mc-asking with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Uh huh."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-130 kv-next with dissolve
    play voice3 girl26_sex_closedmoan4 noloop
    bg "Well..."
    play voice4 kanya_hey_simple2 noloop
    kv "Next position!"
    play sound sfx_cloth_rustling3
    scene sm1cs-bg003-131 kv-directing with dissolve
    play voice4 kanya_yes_yep3 noloop
    kv "Okay, [mcname], stand up... Good."
    scene sm1cs-bg003-132 kv-serious with dissolve
    play voice4 kanya_disappointed_oh noloop
    kv "Amore, kneeling in front of him... Yep. [mcname], lay the riding crop against her chest... yeah..."
    play sound sfx_cloth_rustling2
    scene sm1cs-bg003-133 bg-huh with dissolve
    play voice4 kanya_thinking_hmm2 noloop
    kv "All right, now this next part is really important.{w} Amore, I want you to suck on his finger."
    play voice3 girl26_surprised_huh1 noloop
    bg "Huh?"
    scene sm1cs-bg003-134 kv-asking with dissolve
    play voice4 kanya_sex_closedmoan2 noloop
    kv "I want you to suck his finger with all the love and adoration you would suck his cock with."
    scene sm1cs-bg003-135 kv-bg-talking with dissolve
    play voice3 girl26_surprised_ah noloop
    bg "Kanya!"
    play voice4 kanya_hey_attention noloop
    kv "Trust me. It's going to look good."
    bg "Okay..."
    play sound2 sfx_photocamera_zoom2 noloop
    scene sm1cs-bg003-136 kv-clicking with dissolve
    play voisex3 girl22_sex_sucking1
    play voice4 kanya_happy_yeah noloop
    kv "Oh yeah, that's it!"
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-137 mc-bg-fifth-picture with dissolve
    play voice4 kanya_sex_closedmoan1 noloop
    kv "Fuck... that's hot, Amore. That might be the hottest photo we've ever taken."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-138 mc-asking with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "That good?"
    scene sm1cs-bg003-139 kv-excited with dissolve
    play voice4 kanya_thinking_eeh5 noloop
    kv "This is \"front page of the portfolio\" good, [mcname]."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-140 mc-thinking with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "Is... Amore swirling her tongue around my finger?"
    scene sm1cs-bg003-141 kv-talking with dissolve
    play voice4 kanya_disappointed_ohh noloop
    kv "Oh, and the photo isn't even the best part."
    play sound3 sfx_cloth_rustling1 noloop
    scene sm1cs-bg003-142 mc-asking with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.6
    mc "And what is the best part?"
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    scene sm1cs-bg003-143 kv-pointing with dissolve
    play voice4 kanya_thinking_eeh1 noloop
    kv "I think someone is {i}really{/i} enjoying this."
    scene sm1cs-bg003-144 bg-close-up with dissolve
    pause
    scene sm1cs-bg003-145 mc-thinking with dissolve
    play voisex2 mc_sex_openmoans1
    mct "Oh, she's definitely doing the tongue thing on purpose then."
    stop voisex2 fadeout 1.0
    stop voisex3 fadeout 1.0
    scene sm1cs-bg003-146 kv-teasing with dissolve
    play voice4 kanya_angry_hm noloop
    kv "Taking the \"suck his dick\" part literally, Amore, eh?"
    play sound sfx_cloth_rustling2
    scene sm1cs-bg003-147 bg-explaining with dissolve
    play voice3 girl26_disappointed_mmh2 noloop
    bg "I... I got a little lost in the moment."
    scene sm1cs-bg003-148 kv-ofc with dissolve
    play voice4 kanya_yes_yeah1 noloop
    kv "We noticed."
    scene sm1cs-bg003-149 kv-so-what-now with dissolve
    play voice4 kanya_arrogant_laugh noloop
    kv "Well, are you going to instigate this, or do I have to?"
    scene sm1cs-bg003-150 bg-embarrassed with dissolve
    play voice3 girl26_disappointed_eeh noloop
    bg "I don't know what you're talking about..."
    scene sm1cs-bg003-151 kv-we-know with dissolve
    play voice4 kanya_yes_long noloop
    kv "Yes you do, you little freak. I can see how wet you are from here!"
    play voice3 girl26_angry_cough noloop
    scene sm1cs-bg003-152 bg-more-embarrassed with hpunch
    bg "Kanya!"
    scene sm1cs-bg003-153 kv-smirking with dissolve
    play voice4 kanya_disappointed_neh noloop
    kv "I guess I will then.{w} [mcname], pull out your cock and lay down. Head towards me."
    play sound sfx_cloth_rustling3
    scene sm1cs-bg003-154 mc-telling with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "All right, Kanya."
    mc "As long as your comfortable with this."
    scene sm1cs-bg003-155 bg-explaining with dissolve
    play voice3 girl26_arrogant_yeah noloop
    bg "I am!"
    bg "I just... this is all new, so I don't know where to start."
    scene sm1cs-bg003-157 kv-directing with dissolve
    play voice4 kanya_hey_simple1 noloop
    kv "And that's why I'm here! [mcname], pants off. Chop, chop."
    play sound sfx_jeans_on1
    scene sm1cs-bg003-158 kv-directing with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "All right, all right! Sheesh."
    play voice4 kanya_yes_yep1 noloop
    kv "Good... Now, Amore - get between his legs."
    scene sm1cs-bg003-159 bg-hesitating with dissolve
    play voice4 kanya_yes_aga1 noloop
    kv "Good girl... now I want you to grab his cock."
    play voice3 girl26_arrogant_mff noloop
    bg "Uhm..."
    scene sm1cs-bg003-160 kv-grab-it-now with dissolve
    play voice4 kanya_angry_cough noloop
    kv "Come on. I know you've wanted to since you walked out here. Grab it."
    scene sm1cs-bg003-161 bg-okay with dissolve
    play voice3 girl26_yes_serious noloop
    bg "Yes, ma'am."
    play sound sfx_cloth_rustling2
    scene sm1cs-bg003-162 bg-grabbing with dissolve
    play voice4 kanya_thinking_hmm4 noloop
    kv "Mmmm, good. Now, stroke it. Jerk him off for me."
    scene sm1cs-bg003-163 kv-keep-it-up with dissolve
    play voice3 girl26_yes_simple noloop
    bg "Yes, Kanya."
    scene sm1cs-bg003-a165-1 mc-bg-hj-anim-01 with dissolve
    pause
    scene sm1cs_bg003-a165-1
    play sound2 sfx_handjob_cream1 volume 2.0
    play voisex3 girl26_sex_openmoans1
    play voisex2 mc_sex_openmoans2
    play voice4 kanya_sex_closedmoan1 noloop
    kv "Mmmmm, that's a good, {i}good{/i} girl."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    pause
    scene sm1cs_bg003-a165-2 with dissolve
    play voice4 kanya_happy_relief2 noloop
    kv "How does his cock feel in your hand?"
    bg "Warm... stiff... wonderful..."
    pause
    scene sm1cs_bg003-a165-3 with dissolve
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    kv "And how does it feel, giving [mcname] pleasure?"
    bg "Amazing..."
    pause
    scene sm1cs_bg003-a165-4 with dissolve
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    kv "And what about you, [mcname]? Is she doing a good job?"
    mc "Oh yeah."
    pause
    scene sm1cs_bg003-a165-1-f with dissolve
    play voice4 kanya_arrogant_yeah noloop
    kv "Well don't tell me, tell {i}her{/i}."
    mc "Amore..."
    bg "Yes, Master?"
    mct "Oh man, she's really getting into this."
    pause
    scene sm1cs_bg003-a165-2-f with dissolve
    mc "Amore... you stroke my cock like a good, little slut."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    bg "That makes me happy, Master."
    pause
    scene sm1cs_bg003-a165-3-f with dissolve
    mc "Do you see how hard I am?"
    bg "I do, Master."
    mc "You did this to me."
    pause
    scene sm1cs_bg003-a165-4-f with dissolve
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    bg "I'm sorry I have caused you discomfort, Master."
    mc "It is your duty to help me cum. Understood?"
    bg "I do, Master."
    pause
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    stop sound2 fadeout 1.0
    stop voisex2 fadeout 1.0
    stop voisex3 fadeout 1.0
    scene sm1cs-bg003-166 kv-standing with dissolve
    play voice4 kanya_yes_yep2 noloop
    kv "That's everything I can snap of that pose."
    scene sm1cs-bg003-167 bg-oops with dissolve
    play voice3 girl26_scared_oh1 noloop
    bg "Oh - I totally spaced we were still doing a shoot..."
    scene sm1cs-bg003-168 bg-realising with dissolve
    play voice3 girl26_surprised_ohmy noloop
    bg "Oh my God, I just realized I started calling you Master!"
    scene sm1cs-bg003-169 mc-chill with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "It's all right, Amore."
    scene sm1cs-bg003-170 mc-bg-talking with dissolve
    play voice3 girl26_no_long noloop
    bg "No it isn't! I need to let you know, or get your consent, or-"
    scene sm1cs-bg003-171 mc-smiling with dissolve
    play voice2 mc_hey_hey6 noloop
    mc "Hey, hey, hey - calm down! It's not like you chaotically slipped a finger in my ass or anything."
    mc "Besides, now that we've realized it, we can fix it."
    scene sm1cs-bg003-172 bg-asking with dissolve
    play voice3 girl26_thinking_ehh1 noloop
    bg "You're right... [mcname], is it alright if I call you Master?"
    menu:
        "That's all right. I like being called Master"(hint="sm1cs_bg003_m01_h01"):
            $ bg_mcname = _("Master")
            scene sm1cs-bg003-173 mc-smiling-universal with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "Yeah, I like being called Master."
            scene sm1cs-bg003-174 bg-smiling with dissolve
            play voice3 girl26_happy_yay noloop
            bg "That makes me happy, [bg_mcname!t]."
        "Actually, what if you called me Sir?"(hint="sm1cs_bg003_m01_h02"):
            $ bg_mcname = _("Sir")
            scene sm1cs-bg003-173 mc-smiling-universal with dissolve
            play voice2 d2s9_confused noloop volume 1.6
            mc "How about... Sir, instead?"
            scene sm1cs-bg003-175 bg-small-smiling with dissolve
            play voice3 girl26_yes_unsure noloop
            bg "Yes, [bg_mcname!t]."
        "I'd actually prefer it if you used my name"(hint="sm1cs_bg003_m01_h03"):
            $ bg_mcname = mcname
            scene sm1cs-bg003-173 mc-smiling-universal with dissolve
            play voice2 d2s9_confused noloop
            mc "If it's okay with you, I'd rather you just used my name."
            scene sm1cs-bg003-176 bg-nodding with dissolve
            play voice3 girl26_yes_ugu noloop
            bg "Of course, [bg_mcname!t]. You're in charge."
        "How about instead, you call me..."(hint="sm1cs_bg003_m01_h04"):
            $ bg_mcname = renpy.input(_("Please enter your BDSM nickname")).strip().title()
            if not bg_mcname:
                $ bg_mcname = __("Master")
            scene sm1cs-bg003-173 mc-smiling-universal with dissolve
            play voice2 d2s9_confused noloop
            mc "Would that work for you?"
            scene sm1cs-bg003-174 bg-smiling with dissolve
            play voice3 girl26_yes_unsure noloop
            bg "Yes, [bg_mcname!t]."
    scene sm1cs-bg003-177 kv-consent with dissolve
    play voice4 kanya_arrogant_ha noloop
    kv "Consent, kids. We love to see it."
    play sound sfx_cloth_rustling3
    scene sm1cs-bg003-178 mc-asking with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "So what are you thinking next?"
    scene sm1cs-bg003-179 kv-all-on-you with dissolve
    play voice4 kanya_disappointed_ohh noloop
    kv "Oh, this is no longer my show. It depends on what you two want to do next."
    scene sm1cs-bg003-180 mc-asking with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Well, what do you think, Amore? What are you comfortable with?"
    scene sm1cs-bg003-181 bg-answering with dissolve
    play voice3 girl26_surprised_ehh1 noloop
    bg "I...{w} I don't think I'm ready to have sex with you yet. But... anything and everything else is on the table."
    scene sm1cs-bg003-182 mc-are-you-sure with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Everything?"
    scene sm1cs-bg003-183 bg-yeah with dissolve
    play voice3 girl26_yes_aga noloop
    bg "Uh huh."
    jump sm1cs_bg003_continue
label sm1cs_bg003_continue:
    scene sm1cs-bg003-184 mc-smirking with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "Well, I haven't been able to take my eyes off your tits since you walked in..."
    scene sm1cs-bg003-185 mc-commanding with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "So why don't you take them, and wrap them around my cock, you little whore?"
    scene sm1cs-bg003-186 bg-agreeing with dissolve
    play voice3 girl26_yes_active noloop
    bg "Yes, [bg_mcname!t]."
    scene sm1cs-bg003-187 mc-asking with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Don't forget to lube them up for me, either."
    scene sm1cs-bg003-188 bg-agreeing with dissolve
    play voice3 girl26_yes_yeah noloop
    bg "Yes, [bg_mcname!t]."
    play sound sfx_biologic_spit1
    scene sm1cs-bg003-189 bg-lubricating with dissolve
    pause
    scene sm1cs-bg003-190 mc-thinking with dissolve
    play voice2 mc_angry_errr8 noloop
    mct "Holy shit... I didn't think that Amore would just be this willing right away. Goddamn..."
    scene sm1cs-bg003-a191-1 mc-bg-titjob-anim-01 with dissolve
    pause
    scene sm1cs_bg003-a191-1
    play sound2 sfx_handjob_cream1 volume 2.0
    play voisex3 girl26_sex_openmoans1
    play voisex2 mc_sex_openmoans2
    play sound3 sfx_paint_smearing5 noloop
    scene sm1cs-bg003-191 mc-bg-titjob with dissolve
    bg "How is that, [bg_mcname!t]?"
    mc "Mmmm, your tits are just as soft as they looked."
    bg "That's good to hear, [bg_mcname!t]."
    pause
    scene sm1cs_bg003-a191-2 with dissolve
    bg "Are my tits wet enough for you, [bg_mcname!t]?"
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    mc "Uh huh, they are."
    mc "Perfect tits, for a perfect little slut."
    pause
    scene sm1cs_bg003-a191-3 with dissolve
    bg "Mmmmmm..."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    mc "Are you enjoying this, slut?"
    bg "Yes, [bg_mcname!t]."
    pause
    scene sm1cs_bg003-a191-1-f with dissolve
    mc "Do you like being my personal little fuck toy?"
    bg "I do, [bg_mcname!t]."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    mc "Good. Because I have plans for all the things I want to do to you."
    bg "Mmmmmmmmm!"
    pause
    scene sm1cs_bg003-a191-2-f with dissolve
    mc "Are you ready to please me, however I ask?"
    bg "Yes, [bg_mcname!t]."
    pause
    scene sm1cs_bg003-a191-3-f with dissolve
    mc "That's good."
    mc "That's a good girl."
    bg "Mmmmmmmmmmmmmmm..."
    pause
    stop sound2 fadeout 1.0
    stop voisex2 fadeout 1.0
    stop voisex3 fadeout 1.0
    scene sm1cs-bg003-192 mc-sitting with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "Good. Then bring me that riding crop."
    scene sm1cs-bg003-193 bg-yeah with dissolve
    play voice3 girl26_yes_yep noloop
    bg "Yes, [bg_mcname!t]."
    play sound sfx_skirt_off2
    scene sm1cs-bg003-194 bg-grabbing with dissolve
    pause
    scene sm1cs-bg003-195 mc-commanding with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "Crawl to me."
    play sound sfx_barefoot_run1
    scene sm1cs-bg003-196 bg-crawling with dissolve
    pause
    scene sm1cs-bg003-197 mc-good-girl with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Good girl."
    play sound sfx_skirt_off3 volume 1.5
    scene sm1cs-bg003-198 mc-commanding with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Now, I want you to suck my dick."
    scene sm1cs-bg003-199 bg-yeah with dissolve
    play voice3 girl26_yes_simple noloop
    bg "Yes, [bg_mcname!t]."
    scene sm1cs-bg003-200 bg-suckingh with dissolve
    pause
    play voisex2 mc_angry_errr4 noloop
    play voisex3 girl26_sex_scream10 noloop
    play sound sfx_whip_slap6
    scene sm1cs-bg003-201 bg-ouch with hpunch
    bg "Ow!"
    scene sm1cs-bg003-202 bg-close-up with dissolve
    play voisex2 mc_angry_hm1 noloop
    mc "Well? What are you waiting for?"
    scene sm1cs-bg003-203 mc-get-to-it with dissolve
    play voisex3 girl26_sexpressions_fuck noloop
    bg "I... I'm sorry, [bg_mcname!t]."
    play voisex2 mc_thinking_hmm1 noloop
    mc "Good."
    scene sm1cs-bg003-a204-1 mc-bg-bj-anim-01 with dissolve
    pause
    scene sm1cs_bg003-a204-1
    play voisex2 mc_sex_openmoans2
    play voisex3 girl26_sex_sucking1
    mc "That's it... suck my dick with love and adoration..."
    mc "And that thing with your tongue, mmmmm..."
    pause
    scene sm1cs_bg003-a204-2 with dissolve
    mc "Do you enjoy sucking my cock?"
    bg "Mmmmphhhmmmmm."
    bg "Nnnpppphhh!"
    pause
    scene sm1cs_bg003-a204-3 with dissolve
    mc "Weren't you taught not to speak with your mouth full?"
    bg "..."
    mc "Good girl. You do know your manners after all."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    pause
    scene sm1cs_bg003-a204-1-f with dissolve
    mc "But, you are the perfect little slut, who gives perfect head!"
    mc "Whomever taught you all this needs to be thanked, God!"
    pause
    scene sm1cs_bg003-a204-2-f with dissolve
    mc "If you keep this up... I'm..."
    play sound sfx_photocamera_flash2
    "*CAMERA STROBE SOUND EFFECT*"
    mc "Oh shit, yeah, keep doing that my little whore!"
    pause
    scene sm1cs_bg003-a204-3-f with dissolve
    mc "Oh shi- I'm getting close."
    mc "When I cum, you better swallow every drop. Otherwise, you will be punished."
    mc "Is that -nnngggpphh- understood?"
    bg "Mmmmmmmm."
    mc "Good girl - gah, I'm close!"
    mc "Are you- are you ready for your reward for being my little slut?"
    mc "Because here it cuuuuuums!"
    pause
    play voisex2 [mc_sex_orgasm1, mc_sex_orgasm5] noloop
    play voisex3 girl26_sex_closedmoan5 noloop
    play sound mc_cum_sound1
    scene sm1cs-bg003-205 mc-climax with vpunch
    mc "Oh yeah, swallow every drop! Fuuuuuuuck!"
    scene sm1cs-bg003-206 mc-asking with dissolve
    play voisex2 mc_angry_oof noloop
    mc "Did you do it? Did you get every last little bit of my cum?"
    play sound sfx_spitcum1
    scene sm1cs-bg003-207 bg-showing with dissolve
    play voisex3 girl26_angry_breath noloop
    bg "Yes, [bg_mcname!t]."
    scene sm1cs-bg003-208 mc-talking with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Good. You were a good little slut for me. Even though I wish you had spilled some of my cum on the floor."
    mc "I had some great ideas for punishments."
    scene sm1cs-bg003-209 bg-talking with dissolve
    play voice3 girl26_hey_sad noloop
    bg "You can still punish me if you want, [bg_mcname!t]. I am yours to do with as you wish."
    scene sm1cs-bg003-210 mc-surprised with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Wow..."
    scene sm1cs-bg003-211 bg-uh-oh with dissolve
    play voice3 girl26_surprised_ah noloop
    bg "Oh my God... that was too much."
    bg "I, uhm, need to wash off."
    play sound sfx_cloth_rustling2
    scene sm1cs-bg003-212 bg-talking with dissolve
    play voice3 girl26_surprised_ehh2 noloop
    bg "This was a great shoot, Kanya! I'm looking forward to the photos!"
    play sound sfx_barefoot_run1 volume 1.6
    scene sm1cs-bg003-213 bg-going with dissolve
    stop sound fadeout 4.0
    pause
    scene sm1cs-bg003-214 mc-thinking with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "What the hell was that?"
    scene sm1cs-bg003-215 bg-dw with dissolve
    play voice3 kanya_no_nah1 noloop
    kv "Don't worry about it, [mcname]. Give her some time."
    scene sm1cs-bg003-216 mc-telling-her with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Uh huh..."
    mc "It was just very... hot and cold."
    scene sm1cs-bg003-217 kv-talking with dissolve
    play voice3 kanya_yes_yeah2 noloop
    kv "That doesn't surprise me."
    scene sm1cs-bg003-218 mc-talking with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Oh yeah? You got some insider information you'd like to share?"
    scene sm1cs-bg003-219 kv-shrugging with dissolve
    play voice3 kanya_thinking_eeh1 noloop
    kv "It's not like it's that much of a secret. Amore has wanted a relationship like this for a long time."
    kv "This has been her fantasy for forever. And now she gets to play it out."
    kv "But, it's also new, so she doesn't exactly know what she's doing. And she's not even sure she's entirely ready for it."
    kv "But now that she's started... it's all going to come out."
    scene sm1cs-bg003-220 kv-pointing with dissolve
    play voice3 kanya_happy_laugh2 noloop
    kv "But go put some pants on. I'm trying to get home."
    scene sm1cs-bg003-221 mc-talking with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Oh yeah, I totally forgot that I'm not wearing pants."
    play voice3 kanya_yes_yep2 noloop
    kv "You seem to be the only one who has."
    scene sm1cs-bg003-222 mc-smirking with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I'll get my clothes back on and get out of your hair! Text me when the photos are edited."
    scene sm1cs-bg003-223 kv-okay with dissolve
    play voice3 kanya_yes_yeah3 noloop
    kv "Sounds good!"
    play sound sfx_barefoot_steps1
    scene sm1cs-bg003-224 mc-going with dissolve
    pause
    stop sound fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 6.0, "music" )
    jump sm1cs_bg003_exit_to_map
label sm1cs_bg003_exit_to_map:
    $ StoryController.end_scene(BG_STORY, 3, 0, 5)
    return