image sm1cs-vs002-a28-glambot = Movie(play = "images/FS_T/VS/s002/anim/sm1cs-vs002-a28-3x-60fps.webm", start_image = "sm1cs-vs002-a28 mc-vs-point-glambot-000", image = "sm1cs-vs002-a28 mc-vs-point-glambot-120", loop = False)
label sm1cs_vs002:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound sfx_heels_steps2 loop
    scene sm1cs-vs002-01 mc-vs-entry_c2 with dissolve
    play music music_circo_lento
    play voice3 girl33_hey_serious noloop
    vs "Hiya, [mcname]."
    scene sm1cs-vs002-01 mc-vs-entry_c1 with dissolve
    play voice2 d1s1_mmm noloop
    mct "Here she comes. Is she finally going to dig into me about seeing her masturbating in the shower?"
    stop sound fadeout 1.0
    scene sm1cs-vs002-02 mc-vs-talk_c2 with dissolve
    play voice3 girl33_thinking_hmm1 noloop
    vs "What's shaking?"
    scene sm1cs-vs002-03 mc-vs-talk2_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Not much."
    scene sm1cs-vs002-03 mc-vs-talk2_c2 with dissolve
    play voice3 girl33_thinking_eem1 noloop
    vs "You look a lilttle nervous."
    scene sm1cs-vs002-03 mc-vs-talk2_c1 with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Hah, well that's probably because the last time I saw you, you were in your birthday suit."
    scene sm1cs-vs002-03 mc-vs-talk2_c2 with dissolve
    play voice3 girl33_happy_laugh1 noloop
    vs "*giggles* Ooooh. Sounds like someone enjoyed their glimpse."
    mct "I hope a glimpse is not all I'll get."
    scene sm1cs-vs002-02 mc-vs-talk_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "You're very comfortable in own skin, aren't you?"
    scene sm1cs-vs002-03 mc-vs-talk2_c2 with dissolve
    play voice3 girl33_yes_happy noloop
    vs "Oh yeah. I think it's an after-effected of cheerleading."
    vs "I'm glad you're here. You're a healthy distraction from another boring theater session."
    scene sm1cs-vs002-02 mc-vs-talk_c1 with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    mc "Strange to think that working in a theater could ever be boring."
    scene sm1cs-vs002-02 mc-vs-talk_c2 with dissolve
    play voice3 girl33_disappointed_eeh noloop
    vs "Well, it totally is. I mean, it can be. And it is today."
    vs "Earlier, Denise took Kellie's advice that we needed to practice our breathing exercises, and we spent an hour just sitting on the floor breathing."
    play sound sfx_cloth_rustling1
    scene sm1cs-vs002-04 mc-vs-talk3_c2 with dissolve
    play voice3 girl33_disappointed_geh noloop
    vs "In and out, in and out. For an hour. I didn't even get sweaty, it was so lame."
    vs "I thought my brain might jump out of my skull, summersault off my tits and run off."
    scene sm1cs-vs002-04 mc-vs-talk3_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "That would have been a tough act to follow."
    scene sm1cs-vs002-05 mc-vs-talk4_c2 with dissolve
    play voice3 girl33_happy_laugh1 noloop
    vs "Hehehe. Yeah, but I pushed through it. My cheerleading coach always said, 'Just keep bouncing, and everything will work out.'"
    play voice2 mc_yes_aga1 noloop
    mc "Uh-huh."
    scene sm1cs-vs002-06 mc-vs-talk5_c2 with dissolve
    play voice3 girl33_disappointed_oh noloop
    if player.has_played_scene("sm1fs_t005"):
        vs "I guess I'm still not one hundred percent into Denise's new show."
        scene sm1cs-vs002-06-1 mc-vs-talk5-1_c1 with dissolve
        play voice2 mc_yes_yeah2 noloop
        mc "I can see that. Still, it's going to bring the theater some money, so the next show will probably be way cooler."
        scene sm1cs-vs002-06-1 mc-vs-talk5-1_c2 with dissolve
        play voice3 girl33_disappointed_mmf2 noloop
        vs "That's months from now. I don't know if I can wait that long."
        scene sm1cs-vs002-07 mc-vs-talk6_c1 with dissolve
        play voice2 d1s2_hmm noloop volume 1.4
        mc "Why all the rush, Veronica?"
    else:
        vs "I probably wouldn't feel so bored if Denise just told me what the next show is. I'm pretty sure she's figured it out but she won't tell us yet."
        vs "The suspense is killing me."
        scene sm1cs-vs002-06-1 mc-vs-talk5-1_c1 with dissolve
        play voice2 d1s2_hmm noloop volume 1.4
        mc "Denise is the director, I'm sure she'll reveal it soon. Why all the rush, Veronica?"
    scene sm1cs-vs002-07 mc-vs-talk6_c2 with dissolve
    play voice3 girl33_hey_scared noloop
    vs "Come on, [mcname]. I've been working at this theater for a couple of months now, and I haven't had my big break."
    vs "A few more months like this, and I'll be tired and wrinkled, and the only roles I'll get will be kooky grandmother or the stern female judge."
    vs "I can't let that happen. I'm getting sick of being just another pretty face. I want to be a star! Like Rina Jubilee or Ivana Hoft!"
    menu:
        "Rina worked hard for a while."(hint="sm1cs_vs002_m01_h01"):
            call sm1cs_vs002_m01_c01 from _call_sm1cs_vs002_m01_c01
            jump sm1cs_vs002_rina_worked_hard
        "Ivana has more talents than just acting."(hint="sm1cs_vs002_m01_h02"):
            jump sm1cs_vs002_ivana_talents
label sm1cs_vs002_rina_worked_hard:
    mc "Rina worked hard for a while."
    play voice3 girl33_surprised_oh noloop
    vs "Oh yes. I've loved her for years. Sounds like someone has been reading up on their movie stars."
    scene sm1cs-vs002-08 mc-vs-ask_c1 with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "I have. But you get my point, right?"
    scene sm1cs-vs002-08 mc-vs-ask_c2 with dissolve
    play voice3 girl33_surprised_huh3 noloop
    vs "Huh?"
    scene sm1cs-vs002-06-1 mc-vs-talk5-1_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "I'm just saying, maybe you might have to work for the theater a little longer than you expected."
    mc "Before you get your big break."
    scene sm1cs-vs002-02 mc-vs-talk_c2 with dissolve
    play voice3 girl33_disappointed_mmf1 noloop
    vs "Darn. Do you think that will affect my plans to run for office later?"
    play voice2 mc_thinking_mmm4 noloop
    mc "Ummm. Why don't you just focus on your acting career first."
    vs "Yes. One thing at a time."
    jump sm1cs_vs002_after_choice
label sm1cs_vs002_ivana_talents:
    scene sm1cs-vs002-08 mc-vs-ask_c1 with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I hate to say it, Veronica, but Ivana's path might not be the general path."
    mc "Lucas Georgeberg found her randomly in that little coffee shop, and she made a big splash with {i}War in our Stars{/i}, but she didn't just sit on money from those movies."
    mc "She worked with a band and won a bunch of awards as a musician and kept doing movies, too."
    scene sm1cs-vs002-08 mc-vs-ask_c2 with dissolve
    play voice3 girl33_surprised_oh noloop
    vs "You learned all that from {u}Stars Weekly{/u}?"
    scene sm1cs-vs002-09 mc-vs-look_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "Not really, I actually knew her from {i}Citizen Alien{/i}. It's a favorite of mine."
    mc "My point is even after she starred in a big hit, Ivana didn't stand on her laurels after making it big."
    scene sm1cs-vs002-09 mc-vs-look_c2 with dissolve
    play voice3 girl33_happy_phew noloop
    vs "That's good. I'd hate to think she would stand on a bunch of fans named Laurel. That sounds so mean."
    play voice2 mc_yes_yes2 noloop
    mc "Yes and-"
    scene sm1cs-vs002-10 mc-vs-look2_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "I guess my point is, have you ever gone to places to try to get discovered?"
    scene sm1cs-vs002-10 mc-vs-look2_c2 with dissolve
    play voice3 girl33_surprised_huh3 noloop
    vs "I'm already working here at the theater, [mcname]. Isn't that enough?"
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, but... maybe there are other spots in Crowning that might help you get uh... discovered faster."
    menu:
        "Reach for the stars, Veronica"(hint="sm1cs_vs002_m02_h01"):
            call sm1cs_vs002_m02_c01 from _call_sm1cs_vs002_m02_c01
            scene sm1cs-vs002-11 mc-vs-look3_c1 with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "I believe in you, Veronica."
        "Dreams can be distracting"(hint="sm1cs_vs002_m02_h02"):
            scene sm1cs-vs002-11 mc-vs-look3_c1 with dissolve
            play voice2 mc_thinking_hmm2 noloop
            mc "Be careful about focusing too much on dreams, Veronica."
            mc "You might miss stuff right in front of you."
    jump sm1cs_vs002_after_choice
label sm1cs_vs002_after_choice:
    scene sm1cs-vs002-11 mc-vs-look3_c2 with dissolve
    play voice3 girl33_thinking_eem1 noloop
    vs "Anyhow, I've spent enough of my day here and I could use a break and a snack."
    vs "Want to grab some ice cream and head back to my place?"
    scene sm1cs-vs002-12 mc-vs-look4_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "I thought you'd never ask."
    play sound sfx_heels_steps2 loop
    scene sm1cs-vs002-17 mc-vs-walk_c2 with dissolve
    play voice3 girl33_happy_laugh2 noloop
    vs "Don't get any ideas, [mcname]. I just want to show you some more of my magazines."
    scene sm1cs-vs002-17 mc-vs-walk_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "You had me at ice cream, Veronica."
    stop sound fadeout 1.0
    jump sm1cs_vs002_half_hour_later
label sm1cs_vs002_half_hour_later:
    scene black
    show screen scene_transistion(_("Half an hour later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene sm1cs-vs002-18 mc-vs-look_c1
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_happy_a1 noloop
    mc "Not a bad dorm room. Little smaller than my old one, but no roommate."
    scene sm1cs-vs002-19 mc-vs-walk_c2 with dissolve
    play voice3 girl33_thinking_hmm3 noloop
    vs "Hold this."
    play sound sfx_cloth_rustling1
    scene sm1cs-vs002-20 mc-vs-look_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "Uh sure."
    play sound sfx_book_closed1
    scene sm1cs-vs002-21 mc-vs-walk_c1 with dissolve
    pause
    queue sound sfx_paper_slide1
    scene sm1cs-vs002-22 mc-vs-box_c1 with dissolve
    pause
    scene sm1cs-vs002-23 mc-vs-ice_c2 with dissolve
    play voice3 girl33_yes_aga noloop
    vs "Thanks, [mcname]."
    scene sm1cs-vs002-23 mc-vs-ice_c1 with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "Don't mention it."
    play sound mc_sex_sucking_slow1 volume 0.4
    play sound sfx_paper_rustl2
    scene sm1cs-vs002-24 mc-vs-box_c2 with dissolve
    play voice3 girl33_thinking_hmm2 noloop
    vs "Mmmummm."
    vs "Sometimes I think, I wish I had a roommate."
    stop sound fadeout 1.0
    scene sm1cs-vs002-25 mc-vs-look_c2 with dissolve
    play voice3 girl33_arrogant_he noloop
    vs "Then I'm like, if they were super hot, I'd get too distracted."
    vs "And if they weren't cool, it would suck coming back home."
    scene sm1cs-vs002-26 mc-vs-look2_c1 with dissolve
    play voice3 girl33_disgust_meh noloop
    vs "And what if they were loud? Like a loud snoring person. Blegh."
    scene sm1cs-vs002-27 mc-vs-look3_c1 with dissolve
    pause
    scene sm1cs-vs002-27 mc-vs-look3_c2 with dissolve
    menu:
        "Tease"(hint="sm1cs_vs002_m03_h01"):
            call sm1cs_vs002_m03_c01 from _call_sm1cs_vs002_m03_c01
            scene sm1cs-vs002-a28 mc-vs-point-glambot-000 with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "I don't know. Something tells me you might get a little loud now and then."
            play sound sfx_camera_fly1 volume 2.0
            play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
            scene sm1cs-vs002-a28-glambot
            pause
            play voice3 girl33_happy_laugh3 noloop
            vs "Haha. I do. Live life mas, right?"
            stop sound fadeout 1.0
            stop sound2 fadeout 1.0
        "*subtly point out the dildo*"(hint="sm1cs_vs002_m03_h02"):
            scene sm1cs-vs002-a28 mc-vs-point-glambot-000 with dissolve
            play voice2 mc_angry_cough1 noloop
            mc "Ahem. Did you need a minute to clean up?"
            play sound sfx_camera_fly1 volume 2.0
            play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
            scene sm1cs-vs002-a28-glambot
            pause
            play voice3 girl33_arrogant_huh1 noloop
            vs "Huh?"
            stop sound fadeout 1.0
            stop sound2 fadeout 1.0
    scene sm1cs-vs002-29 mc-vs-ask_c2 with hpunch
    play voice3 girl33_surprised_ohmy noloop
    vs "Hahaha. Oh my god. [mcname], why didn't you say anything?"
    if player.get_choice("sm1cs_vs002_tease_vs"):
        scene sm1cs-vs002-30 mc-vs-ice_c1 with dissolve
        play voice2 mc_arrogant_heh2 noloop
        mc "I did. And I'm kind of surprised you didn't see it, given its size."
        play voice3 girl33_happy_laugh5 noloop
        vs "Hehe. Jealous?"
        mc "Nah."
    scene sm1cs-vs002-30 mc-vs-ice_c2 with dissolve
    play voice3 girl33_arrogant_hm noloop
    vs "Here. Help a lady out."
    scene sm1cs-vs002-31 mc-vs-knees_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Veronica certainly has a broad definition of what a 'lady' is."
    play sound sfx_cloth_rustling3
    scene sm1cs-vs002-31 mc-vs-knees_c2 with dissolve
    play voice3 girl33_disappointed_mmf3 noloop
    vs "Mmhmm. Mr. Slick, ogling my Secretvibe Three-Thousand."
    play sound sfx_heels_steps1
    scene sm1cs-vs002-32 mc-vs-walk_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "It was uh... hard not to notice."
    scene sm1cs-vs002-32 mc-vs-walk_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-vs002-33 mc-vs-ice_c2 with dissolve
    play voice3 girl33_yes_yep noloop
    vs "Thank you."
    play sound sfx_paper_rustl1
    scene sm1cs-vs002-34 mc-vs-magazine_c2 with dissolve
    play voice3 girl33_happy_yay noloop
    vs "Boom. Here it is."
    vs "This issue is all about Juli Silva. He talks about a bunch of lessons he learned as a struggling actor on the street."
    vs "He went from nearly homeless, to a hunk you could eat for days."
    scene sm1cs-vs002-35 mc-vs-magazine2_c1 with dissolve
    play voice2 mc_surprised_why3 noloop
    mc "And you're showing me this why?"
    scene sm1cs-vs002-35 mc-vs-magazine2_c2 with dissolve
    play voice3 girl33_thinking_eem2 noloop
    vs "I figured you could use some extra pointers on your road to success. Consider it a gift."
    scene sm1cs-vs002-35 mc-vs-magazine2_c3 with dissolve
    pause
    play sound sfx_paper_rustl3
    scene sm1cs-vs002-37 mc-vs-look_c1 with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Thanks. I'm surprised, given how you reacted earlier."
    scene sm1cs-vs002-37 mc-vs-look_c2 with dissolve
    play voice3 girl33_no_nah noloop
    vs "That one is old. If you asked me for this week's issue, I wouldn't be giving it up."
    vs "But enough about the movies."
    vs "I want to hear more about what happened with Fetish Locator, [mcname]."
    scene sm1cs-vs002-38 mc-vs-look2_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I guess I can get into it. Where should I start?"
    scene sm1cs-vs002-39 mc-vs-point_c2 with dissolve
    play voice3 girl33_angry_mfhmm noloop
    vs "Pull up a chair and start at the beginning."
    jump sm1cs_vs002_one_hour_later
label sm1cs_vs002_one_hour_later:
    scene black
    show screen scene_transistion(_("About an hour later"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    scene sm1cs-vs002-40 mc-vs-look_c1
    with Fade(0.5, 0.5, 0.5)
    play voice2 mc_yes_yeah4 noloop
    mc "And that's pretty much got you caught up to today."
    mc "Fetish Locator is gone, and I'm just trying to get on with my life."
    scene sm1cs-vs002-40 mc-vs-look_c2 with dissolve
    play voice3 girl33_surprised_wow noloop
    vs "Woah..."
    scene sm1cs-vs002-41 mc-vs-think_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.4
    mct "I almost feel like she'd be interested to hear what Stacy and I are up to, but it might be too early."
    mct "I need to know Veronica a little better before talking about my Porn Studio."
    play sound sfx_cloth_rustling4
    scene sm1cs-vs002-41 mc-vs-think_c2 with dissolve
    play voice3 girl33_disappointed_off noloop
    vs "That sucks."
    scene sm1cs-vs002-42 mc-vs-look_c1 with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "Yeah. Lydia nearly ruined my life."
    scene sm1cs-vs002-42 mc-vs-look_c2 with dissolve
    play voice3 girl33_surprised_huh4 noloop
    vs "Huh? Oh yeah. No, total bitch energy. But I was saying it sucks because I never got to enjoy the app like you guys did."
    menu:
        "Sometimes I miss it"(hint="sm1cs_vs002_m04_h01"):
            call sm1cs_vs002_m04_c01 from _call_sm1cs_vs002_m04_c01
            scene sm1cs-vs002-43 mc-vs-talk_c1 with dissolve
            play voice2 d9s2_yeah noloop volume 1.7
            mc "Yeah, some days I miss it. Especially the parties."
        "I don't miss it"(hint="sm1cs_vs002_m04_h02"):
            call sm1cs_vs002_m04_c02 from _call_sm1cs_vs002_m04_c02
            scene sm1cs-vs002-43 mc-vs-talk_c1 with dissolve
            play voice2 mc_no_no5 noloop
            mc "It was fun, but it also blinded me to a lot of problems in my life."
    scene sm1cs-vs002-44 mc-vs-ask_c2 with dissolve
    play voice3 girl33_arrogant_laugh noloop
    vs "It's probably better it's gone. If Kellie found me using it, she'd scream and yell at Denise about how I'm not taking the theater {i}seriously{/i}."
    vs "She can be a real bee eye tee sea etch, some days."
    scene sm1cs-vs002-45 mc-vs-talk_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Hmmm. Kellie might actually have been a fan of the app too."
    scene sm1cs-vs002-45 mc-vs-talk_c2 with dissolve
    play voice3 girl33_happy_laugh6 noloop
    vs "*chuckles* Shut up. You must be crazy."
    scene sm1cs-vs002-46 mc-vs-talk2_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "I knew some real uptight people who were secretly Fetish Locator users.{w} The app ended up being a great help because it was as anonymous as you wanted it to be."
    scene sm1cs-vs002-46 mc-vs-talk2_c2 with dissolve
    play voice3 girl33_happy_nice noloop
    vs "That's the word I've been trying to think of."
    vs "'Anonymous'. It even sounds sexy."
    vs "I wanted to use the app to have a bunch of anonymous fun with no one ever realizing what I was up to."
    scene sm1cs-vs002-48 mc-vs-talk_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "You wanted the freedom and the secrecy."
    play sound sfx_hair_scratch1
    scene sm1cs-vs002-48 mc-vs-talk_c2 with dissolve
    play voice3 girl33_yes_happy noloop
    vs "Totally. I mean, you know me, I'm not ashamed of my body or showing it off."
    scene sm1cs-vs002-47 mc-vs-look_c1 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "*chuckling* Yeah. You can say that again."
    play voice3 girl33_surprised_huh1 noloop
    vs "Which part?"
    mc "Never mind."
    scene sm1cs-vs002-48 mc-vs-talk_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "So that's why you were so interested in Fetish Locator."
    scene sm1cs-vs002-48 mc-vs-talk_c2 with dissolve
    play voice3 girl33_yes_yeah noloop
    vs "Yeah. It sounds like like this place from one of our shows where anything was possible."
    vs "I think it was called Camelot."
    scene sm1cs-vs002-49 mc-vs-look_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Never thought I'd hear Fetish Locator compared to Camelot."
    scene sm1cs-vs002-49 mc-vs-look_c2 with dissolve
    play voice3 girl33_happy_relief noloop
    vs "But now the app is gone, so I've just been keeping myself entertained on my own."
    vs "Sometimes I spend an evening imagining what it would have been like to use the app"
    play sound sfx_cloth_rustling1
    scene sm1cs-vs002-50 mc-vs-stand_c1 with dissolve
    play voice2 mc_hey_hey10 noloop
    mc "Maybe you don't have just to imagine it."
    scene sm1cs-vs002-50 mc-vs-stand_c2 with dissolve
    play voice3 girl33_arrogant_huh2 noloop
    vs "Hmmm?"
    scene sm1cs-vs002-51 mc-vs-stand2_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "What if we just did our own Fetish Locator thing? It will be a secret between us. I mean, we already have one, so what's another?"
    scene sm1cs-vs002-51 mc-vs-stand2_c2 with dissolve
    play voice3 girl33_angry_huh noloop
    vs "You're just messing with me. Fetish Locator is gone, remember."
    scene sm1cs-vs002-52 mc-vs-talk_c1 with dissolve
    play voice2 mc_yes_yes8 noloop
    mc "Yes, but we can do our own stuff like Fetish Locator if you're down. You just let me know what you're into, and I can make Blitz Challenges for the two of us."
    scene sm1cs-vs002-52 mc-vs-talk_c2 with dissolve
    play voice3 girl33_happy_mmm noloop
    vs "Mmm. I've heard better lines from guys trying to get into my panties."
    if player.has_played_scene("sm1cs_km003"):
        scene sm1cs-vs002-53 mc-vs-talk2_c1 with dissolve
        play voice2 mc_thinking_hm noloop
        mc "Um.{w} You know I have already seen you naked."
        scene sm1cs-vs002-53 mc-vs-talk2_c2 with dissolve
        play voice3 girl33_happy_laugh4 noloop
        vs "*giggling* Seeing me naked is not fucking me."
        scene sm1cs-vs002-54 mc-vs-talk3_c1 with dissolve
        play voice2 mc_yes_ugu1 noloop
        mc "Touche."
        mc "But Fetish Locator was always more than just seeing people naked."
        mc "I'd love to give you that experience."
    else:
        scene sm1cs-vs002-54 mc-vs-talk3_c1 with dissolve
        play voice2 mc_surprised_what1 noloop
        mc "What? No, I just thought that you wanted to try to experience what it was like."
    scene sm1cs-vs002-54 mc-vs-talk3_c2 with dissolve
    play voice3 girl33_thinking_hmm1 noloop
    vs "Hmmm."
    vs "Well, I have to admit, an exciting Fetish Locator event is way better than a typical pickup line."
    scene sm1cs-vs002-55 mc-vs-talk4_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Sounds like it's doing the trick."
    scene sm1cs-vs002-55 mc-vs-talk4_c2 with dissolve
    play voice3 girl33_yes_unsure noloop
    vs "Mmmm. I hope it has twists and turns at every step."
    play sound sfx_cloth_rustling3
    scene sm1cs-vs002-56 mc-vs-stand_c1 with dissolve
    play voice2 mc_thinking_hmm9 noloop
    mc "I love twists and turns. You should see me on the Twister board."
    scene sm1cs-vs002-56 mc-vs-stand_c2 with dissolve
    play voice3 girl33_happy_laugh2 noloop
    vs "Haha. You're really serious about this, aren't you?"
    scene sm1cs-vs002-57 mc-vs-ask_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course. I'm for Fetish Freedom everywhere."
    scene sm1cs-vs002-57 mc-vs-ask_c2 with dissolve
    play voice3 girl33_happy_great noloop
    vs "Alright. Let's do it."
    play voice2 mc_surprised_huh7 noloop
    mc "You're excited already, aren't you?"
    vs "No way. I'm just naturally bubbly. You know that."
    play sound [sfx_phone_tapping1, sfx_phone_tapping1] volume 2.5
    scene sm1cs-vs002-58 mc-vs-phone_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.4
    mc "Haha."
    mct "Okay, when should I set the alarm? It should be on one of the days we have rehearsals."
    menu:
        "Set the alarm for next Tuesday"(hint="sm1cs_vs002_m05_h01"):
            play sound sfx_phone_button1 volume 1.5
            call sm1cs_vs002_m05_c01 from _call_sm1cs_vs002_m05_c01
        "Set the alarm for next Wednesday"(hint="sm1cs_vs002_m05_h02"):
            play sound sfx_phone_button1 volume 1.5
            call sm1cs_vs002_m05_c02 from _call_sm1cs_vs002_m05_c02
        "Set the alarm for next Friday"(hint="sm1cs_vs002_m05_h03"):
            play sound sfx_phone_button1 volume 1.5
            call sm1cs_vs002_m05_c03 from _call_sm1cs_vs002_m05_c03
    play voice2 mc_yes_okay2 noloop
    mc "Okay, all set. Now when that alarm rings, we'll have to meet up real fast and complete the challenge."
    scene sm1cs-vs002-58 mc-vs-phone_c2 with dissolve
    play voice3 girl33_surprised_ohmy noloop
    vs "Oh my god this is the greatest idea ever."
    scene sm1cs-vs002-59 mc-vs-cheer_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I knew you were excited."
    scene sm1cs-vs002-59 mc-vs-cheer_c2 with dissolve
    play voice3 girl33_no_uhuh noloop
    vs "Nuh-uh. *giggles*"
    play voice2 mc_scared_huh3 noloop
    play sound sfx_alarm1 loop
    scene sm1cs-vs002-60 mc-vs-phone_c1 with vpunch
    "*loud music alarm ringing*"
    scene sm1cs-vs002-60 mc-vs-phone_c2 with dissolve
    play voice3 girl33_angry_argh2 noloop
    pause
    scene sm1cs-vs002-61 mc-vs-phone2_c1 with dissolve
    play sound sfx_phone_button1 volume 1.5
    "Beep."
    play voice3 girl33_disappointed_geh noloop
    vs "Crap. I need to study for my next class. Hopefully, your alarm isn't going off {b}too{/b} soon, haha."
    scene sm1cs-vs002-62 mc-vs-look_c1 with dissolve
    play voice2 mc_no_nope1 noloop
    mc "It's not. I'll get out of your hair and see you later."
    scene sm1cs-vs002-62 mc-vs-look_c2 with dissolve
    play voice3 girl33_yes_aga noloop
    vs "Awesome."
    vs "Thanks again, [mcname]. I think this is the start of something really fun."
    play sound sfx_cloth_rustling2
    scene sm1cs-vs002-63 mc-vs-talk_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Thanks, and thanks for the magazine."
    scene sm1cs-vs002-63 mc-vs-talk_c2 with dissolve
    play voice3 girl33_yes_yep noloop
    vs "My pleasure."
    vs "And don't worry, I'll keep all the naughty details of your past to myself. Unless you tell me to tell the other girls at the theater."
    play sound sfx_heels_steps2 loop
    scene sm1cs-vs002-64 mc-vs-walk_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Haha, yeah let's just keep it between us for now."
    mc "See you around, Veronica."
    stop sound fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2")
    jump sm1cs_vs002_end
label sm1cs_vs002_end:
    $ StoryController.end_scene(VS_STORY, 3, 30, 2, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return
label sm1cs_vs002_m01_c01:
    $ player.set_choice("sm1cs_vs002_rina_worked_hard")
    return
label sm1cs_vs002_m02_c01:
    $ player.set_choice("sm1cs_vs002_reach_the_stars")
    $ CharacterController.get_character("vs").add_point()
    return
label sm1cs_vs002_m03_c01:
    $ player.set_choice("sm1cs_vs002_tease_vs")
    $ CharacterController.get_character("vs").add_point()
    return
label sm1cs_vs002_m04_c01:
    $ player.set_choice("sm1cs_vs002_miss_fl")
    $ CharacterController.get_character("vs").add_point()
    return
label sm1cs_vs002_m05_c01:
    $ player.set_choice("sm1cs_vs002_alarm_day", TUESDAY)
    return
label sm1cs_vs002_m05_c02:
    $ player.set_choice("sm1cs_vs002_alarm_day", WEDNESDAY)
    return
label sm1cs_vs002_m05_c03:
    $ player.set_choice("sm1cs_vs002_alarm_day", FRIDAY)
    return
label sm1cs_vs002_m04_c02:
    $ CharacterController.get_character("vs").deduct_point()
    return