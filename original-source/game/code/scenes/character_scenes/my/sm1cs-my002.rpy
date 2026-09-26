label sm1cs_my002:
    $ sm1cs_my002_date_points = 0
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music bass_sexy3_piano
    play sound sfx_heels_steps1 loop
    scene sm1cs_my002-00 thiss_art_sy_talkcoffee with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "So, fancy restaurant, with fancy food, and..."
    stop sound fadeout 1.0
    play sound sfx_hair_scratch1
    scene sm1cs_my002-01 thiss_art_mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, we got some oysters-"
    scene sm1cs_my002-02 thiss_art_sy_talk_headache with dissolve
    play voice3 stacy_surprised_huh4 noloop
    sy "You got oysters?"
    scene sm1cs_my002-03 thiss_art_mc_talk with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah? What's wrong with that?"
    scene sm1cs_my002-04 thiss_art_sy_talk with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "That's such a horny dude thing to do."
    sy "You might as well have just pulled your dick out and slapped it on the table, [mcname]."
    scene sm1cs_my002-05 thiss_art_mc_talk with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I mean..."
    play sound sfx_heels_steps1
    scene sm1cs_my002-06 thiss_art_sy_talk_sitting with dissolve
    play voice3 stacy_no2 noloop
    sy "That won't actually work, don't do that."
    play sound sfx_bed_slide2
    scene sm1cs_my002-07 thiss_art_sy_talk_sitting with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    if persistent.is_special:
        sy "Mom probably saw right through that."
    else:
        sy "Melony probably saw right through that."
    scene sm1cs_my002-08 thiss_art_mc_talk with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well she wants to spend more time together, so even if she did, she didn't care."
    scene sm1cs_my002-09 thiss_art_sy_talk with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "See? I told you she had a thing for you."
    scene sm1cs_my002-10 thiss_art_mc_talk with dissolve
    play voice2 mc_no_no2 noloop
    mc "I don't think that's the case, Stacy. I think she's just happy to be able to spend some time with me - with us, ya know?"
    scene sm1cs_my002-11 thiss_art_sy_talk with dissolve
    play voice3 stacy_yes_fine4 noloop
    sy "Whatever you want to tell yourself."
    sy "So, when's your next date?"
    scene sm1cs_my002-12 thiss_art_mc_talk with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I don't know. Haven't set one up yet."
    scene sm1cs_my002-13 thiss_art_sy_talk with dissolve
    play voice3 stacy_mmm1 noloop
    sy "Okaaaaay. Well, where are you going to go for your next date?"
    scene sm1cs_my002-14 thiss_art_mc_talk with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "Beats me... maybe another restaurant?"
    scene sm1cs_my002-15 thiss_art_sy_talk_flabbergasted with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "Seriously? Another restaurant? Come on, [mcname]. You can do better than that."
    play sound sfx_cloth_rustling2
    scene sm1cs_my002-16 thiss_art_mc_talk with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "What? Sitting and getting to know people is how you form deep and meaningful relationships with them!"
    scene sm1cs_my002-17 thiss_art_sy_talk with dissolve
    play voice3 stacy_yeahno noloop
    sy "Yeah, but you need to do something with some action."
    scene sm1cs_my002-18 thiss_art_mc_talk_rolleyes with dissolve
    play voice2 mc_angry_errr5 noloop
    pause
    scene sm1cs_my002-19 thiss_art_mc_talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Well, what do you suggest, then."
    play sound sfx_cloth_rustling3
    scene sm1cs_my002-20 thiss_art_sy_talk_thinking with dissolve
    pause
    scene sm1cs_my002-21 thiss_art_sy_talk_aha with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "OH! I remembered seeing something, uhm..."
    sy "Let's see, let's see...{w} there it is!"
    scene sm1cs_my002-22 thiss_art_sy_talk_phone with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "There's a gallery here in Crowning that just opened with some really great art. Why don't you bring her there?"
    play sound sfx_cloth_rustling1
    scene sm1cs_my002-23 thiss_art_mc_talk with dissolve
    play voice2 mc_thinking_hm noloop
    if persistent.is_special:
        mc "Mom does always talk about how much she likes art."
    else:
        mc "Melony does really like art..."
    mc "Plus, I can show her that I can talk about art too."
    play sound sfx_cloth_rustling2
    scene sm1cs_my002-24 thiss_art_sy_talk with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "You can talk about art?"
    scene sm1cs_my002-25 thiss_art_mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    if player.has_played_scene("sm1cs_kv002"):
        mc "Yeah, I learned all that shit for Kanya."
    elif player.has_played_scene("sm1fs_t004"):
        mc "I've done all that theater training, I can probably make something up from that?"
    else:
        mc "Yeah, how hard can it be?"
    mc "Besides, if I start talking about color contrast and subtlety, I'll sound like I know what I'm talking about."
    scene sm1cs_my002-26 thiss_art_sy_talk_skeptical with dissolve
    play voice3 stacy_happy_laugh1 noloop
    if persistent.is_special:
        sy "Well, text Mom and see if she's free."
    else:
        sy "Well, text Melony and see if she's free."
    play voice2 d9s2_ugu noloop volume 2.0
    mc "Maybe I will!"
    sy "This can not end well."
    scene sm1cs_my002-27 thiss_art_mc_talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Just you wait... I'm going to... go... and do the art thing... so well."
    play sound sfx_phone_tapping1 loop volume 3.0
    scene sm1cs_my002-28 thiss_art_sy_talk_mctext with dissolve
    mc "..."
    scene sm1cs_my002-29 thiss_art_mc_talk_mctext with dissolve
    play sound sfx_message_in1
    mc "..."
    scene sm1cs_my002-30 thiss_art_mc_talk_loookmc with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "And she texted me back! She's free right now."
    scene sm1cs_my002-31 thiss_art_sy_talk with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, go get her tiger."
    play sound sfx_bed_slide3 volume 0.5
    scene sm1cs_my002-32 thiss_art_mc_talk_getup with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "I will!"
    play sound2 sfx_heels_steps2
    scene sm1cs_my002-33 thiss_art_mc_talk_walk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    if persistent.is_special:
        mct "Did my sister just goad me into going on a date with our mom?"
    else:
        mct "Did Stacy just goad me into going on a date with Melony?"
    scene sm1cs_my002-34 thiss_art_mc_talk_door with dissolve
    mct "I think she did... God, I hope I don't mess this up..."
    stop music fadeout 3.0
    play sound2 sfx_door_openclosed1 noloop
    jump sm1cs_my002_art_gallery
label sm1cs_my002_art_gallery:
    $ renpy.music.set_volume(1.0, 3.5, "music" )
    queue music music_artgallery_piano1
    play sound sfx_heels_steps1 fadein 2.0 loop
    play sound4 sfx_museum_ambience fadein 2.0
    scene sm1cs_my002-35 thiss_art_mc_talk_art_gallery with Fade(0.5, 0.5, 0.5)
    pause
    stop sound fadeout 1.0
    scene sm1cs_my002-36 thiss_art_mc_talk_looking_around with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.5
    if persistent.is_special:
        mct "I hope I sent the right address to Mom..."
    else:
        mct "I hope I sent the right address to Melony..."
    mct "That would be a hell of a way to start this date, sending her the wrong address."
    mct "She's usually not late..."
    play sound sfx_door_openclosed2
    play sound2 sfx_heels_steps1
    scene sm1cs_my002-37 thiss_art_my_talk_mywalksin with dissolve
    play voice2 mc_disappointed_off2 noloop
    mct "Phew, okay. I did send her the right address. Thank God."
    play voice3 girl34_hey_happy noloop
    my "[mcname]! Hi, sorry I'm late."
    stop sound2 fadeout 1.0
    scene sm1cs_my002-38 thiss_art_mc_talk with dissolve
    play voice2 mc_no_no10 noloop
    if persistent.is_special:
        mc "Don't worry about it, Mom."
    else:
        mc "Don't worry about it, Melony."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs_my002-39 thiss_art_my_talk_walk with dissolve
    play voice3 girl34_surprised_wow2 noloop
    my "Wow, this place looks great, [mcname]! How'd you hear about it?"
    scene sm1cs_my002-40 thiss_art_mc_talk with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Oh, uhm, I think I saw an ad for it somewhere."
    scene sm1cs_my002-41 thiss_art_my_talk with dissolve
    play voice3 girl34_yes_aga3 noloop
    my "Uh huh. Did Stacy tell you about it?"
    scene sm1cs_my002-42 thiss_art_mc_talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "...Maybe."
    scene sm1cs_my002-43 thiss_art_my_talk with dissolve
    play voice3 girl34_arrogant_ha1 noloop
    if persistent.is_special:
        my "You always struggled to give your sister her fair due."
    else:
        my "You always struggled to give Stacy her fair due."
    scene sm1cs_my002-44 thiss_art_mc_talk with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Well, I mean..."
    scene sm1cs_my002-45 thiss_art_my_talk with dissolve
    play voice3 girl34_happy_laugh2 noloop
    my "Hahahaha! You two have grown-up a lot..."
    my "But some things never change."
    scene sm1cs_my002-46 thiss_art_mc_talk with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey now-"
    scene sm1cs_my002-47 thiss_art_my_talk_laugh with dissolve
    play voice3 girl34_happy_laugh5 noloop
    my "Hahahahaha!"
    my "I will say, I am a little surprised that you invited me to an art exhibit."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs_my002-48 thiss_art_mc_talk with dissolve
    play voice2 mc_surprised_why3 noloop
    mc "And why's that?"
    scene sm1cs_my002-49 thiss_art_my_talk with dissolve
    play voice3 girl34_thinking_hmm7 noloop
    my "You never struck me as someone interested in art."
    my "You did want to go to school for business."
    scene sm1cs_my002-50 thiss_art_mc_talk with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "And what's that supposed to mean?"
    scene sm1cs_my002-51 thiss_art_my_talk with dissolve
    play voice3 girl34_happy_laugh8 noloop
    my "Hahahaha - in my experience, guys who go to school for business aren't usually the most artistic."
    scene sm1cs_my002-52 thiss_art_mc_talk with dissolve
    play voice2 mc_no_nope2 noloop
    mc "I disagree with that, I can be very artistic!"
    scene sm1cs_my002-53 thiss_art_my_talk with dissolve
    play voice3 girl34_surprised_oh4 noloop
    my "Oh yeah? You can?"
    scene sm1cs_my002-54 thiss_art_mc_talk with dissolve
    play voice2 d9s2_yeah noloop volume 2.3
    mc "Yeah! I totally can."
    play sound sfx_cloth_rustling2
    scene sm1cs_my002-55 thiss_art_my_talk_gestyringmc_look with dissolve
    play voice3 girl34_thinking_hmm4 noloop
    my "Well, let's hear your critique than, hotshot!"
    scene sm1cs_my002-56 thiss_art_mc_talk_thought with dissolve
    play voice2 mc_pain_mff1 noloop
    mct "Oh shit, I didn't think I was going to have to start this fast! Uh oh, uh oh..."
    mc "..."
    scene sm1cs_my002-57 thiss_art_my_talk with dissolve
    play voice3 girl34_yes_yeah6 noloop
    my "So? What does the big business art man think of \"Diana and her Nymphs\"?"
    scene sm1cs_my002-58 thiss_art_mc_talk with dissolve
    play voice2 d2s12_emmm noloop
    mc "Well, erm..."
    menu:
        "The use of glaze to increase the glow around Diana is great":
            call sm1cs_my002_m01_c01 from _call_sm1cs_my002_m01_c01
            $ sm1cs_my002_date_points += 1
            scene sm1cs_my002-59 thiss_art_mc_talk with dissolve
            play voice2 mc_thinking_hmm3 noloop
            mc "The choice to use glaze on the subject adds this magnificent glow."
            mc "It really highlights her as a subject, as well as a powerful goddess."
            scene sm1cs_my002-60 thiss_art_my_talkmpressed with dissolve
            play voice3 girl34_surprised_wow3 noloop
            my "Wow, you spotted the use of glaze?"
            scene sm1cs_my002-61 thiss_art_mc_talk with dissolve
            play voice2 mc_yes_aga1 noloop
            mc "Uh huh."
            scene sm1cs_my002-62 thiss_art_my_talkmpressed with dissolve
            play voice3 girl34_happy_relief1 noloop
            my "I'm impressed."
        "I love the detail of Alpheus spying on Diana and the Nymphs":
            call sm1cs_my002_m01_c02 from _call_sm1cs_my002_m01_c02
            $ sm1cs_my002_date_points += 1
            scene sm1cs_my002-59 thiss_art_mc_talk with dissolve
            play voice2 mc_thinking_mmm2 noloop
            mc "Keeping him on the side, as a way to convey the voyeuristic nature of the viewer."
            mc "I think it's a great way to comment on viewership of the patrons and the inherently perverted nature of art."
            scene sm1cs_my002-60 thiss_art_my_talkmpressed with dissolve
            play voice3 girl34_surprised_oh1 noloop
            my "Oh, commentary on the voyeurism of viewing art?"
            scene sm1cs_my002-61 thiss_art_mc_talk with dissolve
            play voice2 mc_yes_yes2 noloop
            mc "Yep."
            scene sm1cs_my002-62 thiss_art_my_talkmpressed with dissolve
            play voice3 girl34_happy_relief1 noloop
            my "I'm impressed."
        "Oil with an autumnal palette is such a beautiful look":
            call sm1cs_my002_m01_c03 from _call_sm1cs_my002_m01_c03
            $ sm1cs_my002_date_points += 1
            scene sm1cs_my002-59 thiss_art_mc_talk with dissolve
            play voice2 mc_thinking_hmm3 noloop
            mc "The way the artist blends the colors gives a sense of warmth and beauty that's befitting the subject."
            mc "It makes her feel warm and inviting, which is befitting her as a goddess."
            scene sm1cs_my002-60 thiss_art_my_talkmpressed with dissolve
            play voice3 girl34_thinking_emm5 noloop
            my "Commenting on the color palette?"
            scene sm1cs_my002-61 thiss_art_mc_talk with dissolve
            play voice2 mc_yes_yes2 noloop
            mc "Yep."
            scene sm1cs_my002-62 thiss_art_my_talkmpressed with dissolve
            play voice3 girl34_happy_relief1 noloop
            my "I'm impressed."
        "... Who is Diana?":
            call sm1cs_my002_m01_c04 from _call_sm1cs_my002_m01_c04
            scene sm1cs_my002-59 thiss_art_mc_talk with dissolve
            play voice2 d3s11b_mcheh noloop volume 1.9
            mc "She doesn't look like a Diana... maybe she is?"
            scene sm1cs_my002-60 thiss_art_my_talkmpressed with dissolve
            play voice3 girl34_disappointed_oh2 noloop
            my "Oh, [mcname]... Diana is the Roman version of Artemis, the goddess of the hunt."
            scene sm1cs_my002-61 thiss_art_mc_talk with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "Ohhh..."
    scene sm1cs_my002-63 thiss_art_my_talk_look_painting with dissolve
    play voice3 girl34_happy_mmm1 noloop
    my "It really is a beautiful piece."
    scene sm1cs_my002-64 thiss_art_mc_talk_look_painting with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I think so too."
    scene sm1cs_my002-65 thiss_art_my_talk_look_painting with dissolve
    play voice3 girl34_disappointed_huh noloop
    my "I'm shocked that this exhibit was able to get such high quality pieces."
    my "I might have to try and speak with the manager here."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs_my002-66 thiss_art_mc_talk_look_walking with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Is there a problem?"
    scene sm1cs_my002-67 thiss_art_my_talk_look_walking with dissolve
    play voice3 girl34_no_happy2 noloop
    my "Oh no, not at all. In fact, I'm impressed by their work."
    my "I might try and steal them away from here."
    scene sm1cs_my002-68 thiss_art_mc_talk_look_walking with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oooo, a little bit of headhunting?"
    scene sm1cs_my002-69 thiss_art_my_talk_look_walking with dissolve
    play voice3 girl34_yes_yeap1 noloop
    my "Yep. Everywhere I go I'm always looking for talent."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs_my002-70 thiss_art_my_talk_look_painting with dissolve
    play voice3 girl34_disappointed_eem4 noloop
    my "And whomever is curating this exhibit has some talent."
    scene sm1cs_my002-71 thiss_art_my_talk_mc_thought with dissolve
    mct "Wait, they're both kind of naked too... is this a nude exhibit?"
    play voice3 girl34_surprised_huh5 noloop
    my "So what do you think of \"Mishief and Repose\", hotshot?"
    scene sm1cs_my002-72 thiss_art_mc_talk with dissolve
    play voice2 d2s9_confused noloop
    mc "Erm..."
    menu:
        "This feels like a neoclassical painting":
            call sm1cs_my002_m02_c01 from _call_sm1cs_my002_m02_c01
            $ sm1cs_my002_date_points += 1
            scene sm1cs_my002-73 thiss_art_mc_talk_menu with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "There are some classic hallmarks to the masters here, but the techniques are updated."
            mc "You can also see in the brushstrokes that the equipment they used was newer. More refined, you know?"
            scene sm1cs_my002-74 thiss_art_my_talk_menumpressed with dissolve
            play voice3 girl34_surprised_ohmy2 noloop
            my "Brush strokes? You've got quite an eye, [mcname]."
            scene sm1cs_my002-75 thiss_art_mc_talk_menu with dissolve
            play voice2 mc_happy_a1 noloop
            mc "Thank you."
        "The use of tempura paint here is incredible":
            call sm1cs_my002_m02_c02 from _call_sm1cs_my002_m02_c02
            scene sm1cs_my002-73 thiss_art_mc_talk_menu with dissolve
            play voice2 mc_thinking_hmm5 noloop
            mc "The color, of the, uhm, tempura paint..."
            scene sm1cs_my002-76 thiss_art_my_talk_menu_rolleyes with dissolve
            play voice3 girl34_disappointed_oh1 noloop
            my "Oh, [mcname]... this is an oil painting."
            scene sm1cs_my002-77 thiss_art_mc_talk_menu with dissolve
            play voice2 d3s7_mcemm noloop volume 1.5
            mc "...{w} Really?"
            scene sm1cs_my002-74 thiss_art_my_talk_menumpressed with dissolve
            play voice3 girl34_yes_yeap4 noloop
            my "Yep."
        "Both women looking away is a fascinating choice":
            call sm1cs_my002_m02_c03 from _call_sm1cs_my002_m02_c03
            $ sm1cs_my002_date_points += 1
            scene sm1cs_my002-76 thiss_art_my_talk_menu_rolleyes with dissolve
            play voice3 girl34_surprised_why2 noloop
            my "Why do you say that?"
            scene sm1cs_my002-73 thiss_art_mc_talk_menu with dissolve
            play voice2 d1s5_mchappy noloop volume 1.6
            mc "Well, both women are looking away from the viewer. They don't invite us in, they don't let us be the voyeur."
            mc "It's... it's like they can't be bothered with us, and instead are focused on each other. And they couldn't care about us."
            scene sm1cs_my002-74 thiss_art_my_talk_menumpressed with dissolve
            play voice3 girl34_surprised_oh5 noloop
            my "That's an incredible read, [mcname]."
        "Which one is Mischief?":
            call sm1cs_my002_m02_c04 from _call_sm1cs_my002_m02_c04
            scene sm1cs_my002-77 thiss_art_mc_talk_menu with dissolve
            play voice2 d1s5_mchappy noloop
            mc "Is it the one on the left? Or the right?"
            scene sm1cs_my002-76 thiss_art_my_talk_menu_rolleyes with dissolve
            play voice3 girl34_disappointed_ehh1 noloop
            my "It doesn't necessarily matter which is which."
            my "But it's the one with the needle."
            scene sm1cs_my002-73 thiss_art_mc_talk_menu with dissolve
            play voice2 mc_surprised_oh1 noloop
            mc "Oh... that makes sense."
    scene sm1cs_my002-78 thiss_art_my_talk_look_painting with dissolve
    play voice3 girl34_happy_nice1 noloop
    my "Really... these are excellent finds."
    scene sm1cs_my002-79 thiss_art_my_talk_look_walking with dissolve
    play voice3 girl34_thinking_emm1 noloop
    my "And, I will say, it was quite... grown-up of you to invite me to an exhibit of nudes."
    my "And to not make any jokes about the nude paintings."
    scene sm1cs_my002-80 thiss_art_mc_talk_look_walking with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Erm, yeah. That's me, a total grown-up."
    if persistent.is_special:
        mct "And I've honestly been so preoccupied by trying to impress Mom, I haven't really noticed."
    else:
        mct "And I've honestly been so preoccupied by trying to impress Melony, I haven't really noticed."
    scene sm1cs_my002-81 thiss_art_my_talk_look_smile with dissolve
    play voice3 girl34_happy_relief4 noloop
    my "I'm grateful you invited me. I love spending this time with you."
    scene sm1cs_my002-82 thiss_art_mc_talk with dissolve
    play voice2 mc_happy_yay2 noloop
    if persistent.is_special:
        mc "And I've loved spending time with you too, Mom."
    else:
        mc "And I've loved spending time with you too, Melony."
    scene sm1cs_my002-83 thiss_art_my_talk with dissolve
    play voice3 girl34_happy_relief2 noloop
    my "That makes me happy to hear, [mcname]."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs_my002-84 thiss_art_my_talk_walk with dissolve
    play voice3 girl34_disappointed_eem1 noloop
    my "Oh, well, here is the real test of your grown-up capacity."
    scene sm1cs_my002-85 thiss_art_mc_talk_walk with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Haha. I love a good test."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs_my002-86 thiss_art_my_talk_painting with dissolve
    play voice3 girl34_arrogant_hm2 noloop
    my "This painting is titled \"Danae and the Golden Shower\"."
    scene sm1cs_my002-87 thiss_art_my_talk_painting_mcthought with dissolve
    play voice2 mc_pain_mff3 noloop
    mct "Oh God..."
    play voice3 girl34_arrogant_huh2 noloop
    my "Anything to say about that, hotshot?"
    scene sm1cs_my002-88 thiss_art_mc_talk with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Erm... I have no idea why I would have anything to say about that..."
    scene sm1cs_my002-89 thiss_art_my_talk_raises_eyebrow with dissolve
    play voice3 girl34_hey_simple2 noloop
    my "Come on, [mcname], we both know what a golden shower is."
    scene sm1cs_my002-90 thiss_art_mc_talk with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Erm..."
    scene sm1cs_my002-91 thiss_art_my_talk with dissolve
    play voice3 girl34_surprised_ah1 noloop
    my "Are you going to try and convince me that you, someone who's running a porn studio, doesn't know what a golden shower is?"
    scene sm1cs_my002-92 thiss_art_mc_talk with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Uhhhh..."
    scene sm1cs_my002-93 thiss_art_my_talk_smirk with dissolve
    play voice3 girl34_yes_aga4 noloop
    my "Uh huh, [mcname]."
    my "Come on, we're both adults. We can talk about golden showers and look at nudity together."
    scene sm1cs_my002-94 thiss_art_mc_talk with dissolve
    play voice2 mc_angry_huh2 noloop
    if persistent.is_special:
        mc "Uhm... yeah, we totally can, Mom."
    else:
        mc "Uhm... yeah, we totally can, Melony."
    scene sm1cs_my002-95 thiss_art_my_talk with dissolve
    play voice3 girl34_yes_ugu2 noloop
    my "Good. Now, what do you think of the painting?"
    scene sm1cs_my002-96 thiss_art_mc_talk_menu with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, uhm..."
    menu:
        "Is this one oil?":
            call sm1cs_my002_m03_c01 from _call_sm1cs_my002_m03_c01
            play voice2 mc_thinking_hmm4 noloop
            mc "Right? This is an oil painting?"
            scene sm1cs_my002-97 thiss_art_my_talk_menu_smirk with dissolve
            play voice3 girl34_yes_neutral9 noloop
            my "Yes, [mcname], this one is an oil painting."
        "The light green fabric creates quite a focal point on Danae":
            call sm1cs_my002_m03_c02 from _call_sm1cs_my002_m03_c02
            $ sm1cs_my002_date_points += 1
            play voice2 mc_thinking_hmm9 noloop
            mc "The green cloth really draws the eye of the viewer to Danae, and it creates this... exotic, and... sensual imagery."
            scene sm1cs_my002-97 thiss_art_my_talk_menu_smirk with dissolve
            play voice3 girl34_surprised_wow4 noloop
            my "Wow, that's quite the read."
            scene sm1cs_my002-98 thiss_art_mc_talk with dissolve
            play voice2 mc_surprised_uh2 noloop
            mc "Is it... wrong?"
            play sound sfx_heels_steps1 loop
            play sound2 sfx_heels_steps2
            scene sm1cs_my002-99 thiss_art_my_talk_walkpainting with dissolve
            play voice3 girl34_no_nonono2 noloop
            my "No, no. It's spot on, in fact."
        "So... golden shower, huh":
            call sm1cs_my002_m03_c03 from _call_sm1cs_my002_m03_c03
            play voice2 mc_arrogant_heh1 noloop
            mc "Definitely... looks like a golden shower."
            scene sm1cs_my002-97 thiss_art_my_talk_menu_smirk with dissolve
            play voice3 girl34_happy_laugh3 noloop
            my "And there is the [mcname] I know."
            scene sm1cs_my002-98 thiss_art_mc_talk with dissolve
            play voice2 mc_surprised_uh3 noloop
            mc "What! I did so good... how could I resist?"
            play sound sfx_heels_steps1 loop
            play sound2 sfx_heels_steps2
            scene sm1cs_my002-99 thiss_art_my_talk_walkpainting with dissolve
        "This is a great example of chiaroscuro":
            call sm1cs_my002_m03_c04 from _call_sm1cs_my002_m03_c04
            play voice2 mc_thinking_mmm1 noloop
            mc "The contrast, and... dark background."
            scene sm1cs_my002-97 thiss_art_my_talk_menu_smirk with dissolve
            play voice3 girl34_no_nah2 noloop
            my "Just because there's a dark background doesn't make it chiaroscuro, hot shot."
            scene sm1cs_my002-98 thiss_art_mc_talk with dissolve
            play voice2 mc_disgust_meh4 noloop
            mc "Well...{w} shit."
            play sound sfx_heels_steps1 loop
            play sound2 sfx_heels_steps2
            scene sm1cs_my002-99 thiss_art_my_talk_walkpainting with dissolve
    play voice3 girl34_happy_phew2 noloop
    my "Wow... this piece really speaks to me."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs_my002-100 thiss_art_mc_talk with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah? Why's that?"
    play sound sfx_cloth_rustling3
    scene sm1cs_my002-101 thiss_art_my_talk_reach with dissolve
    play voice3 girl34_thinking_hmm2 noloop
    my "Danae is locked away, to stop Perseus from being born..."
    my "But the lust of the gods cannot be stopped. And they come for her."
    my "And she's welcoming it, yearning for it. She's waiting, nude..."
    scene sm1cs_my002-102 thiss_art_my_talk_chest with dissolve
    play voice3 girl34_happy_mmm3 noloop
    my "And she's sensual, erotic... desire is written across her face, and she's ready for this."
    my "She's ready for her shower..."
    scene sm1cs_my002-103 thiss_art_mc_talk_lookass with dissolve
    play voice2 d1s1_mmm noloop volume 1.6
    mct "God, is it just me... or is she kind of getting horny?"
    mct "And... is she making me kind of horny?"
    scene sm1cs_my002-104 thiss_art_mc_talk_lookass with dissolve
    play voice2 mc_angry_errr6 noloop
    if persistent.is_special:
        mct "God, Mom has a great ass..."
    else:
        mct "God, Melony has a great ass..."
    scene sm1cs_my002-105 thiss_art_my_talk_turn with dissolve
    play voice3 girl34_disappointed_oh3 noloop
    my "Sorry, I got a little lost there for a second. Shall we keep going?"
    scene sm1cs_my002-106 thiss_art_mc_talk with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Uhm, yeah - definitely."
    play sound sfx_heels_steps1 loop
    scene sm1cs_my002-107 thiss_art_my_talk_walk_around_mc_boner with dissolve
    mct "Jesus, she really got me turned on. I hope she doesn't notice my boner..."
    play voice3 girl34_disappointed_eem2 noloop
    my "So, [mcname], what are your thoughts about the exhibit as a whole?"
    stop sound fadeout 1.0
    scene sm1cs_my002-108 thiss_art_mc_talk with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "I, erm, think it's great!"
    if persistent.is_special:
        mc "Just looking at some nudes with my Mom."
    else:
        mc "Just looking at nudes with you."
    scene sm1cs_my002-109 thiss_art_my_talk with dissolve
    play voice3 girl34_arrogant_ha4 noloop
    my "They're just bodies, [mcname]."
    my "Fleshy bits that we've all prescribed meaning to. Sexual or otherwise."
    scene sm1cs_my002-110 thiss_art_mc_talk with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Uh... yep."
    if sm1cs_my002_date_points == 3:
        $ CharacterController.get_character("my").add_point(2)
        scene sm1cs_my002-111 thiss_art_my_talk_look with dissolve
        play voice3 girl34_surprised_wow1 noloop
        my "You know, I've been quite impressed with your art knowledge, [mcname]."
        scene sm1cs_my002-112 thiss_art_mc_talk with dissolve
        play voice2 mc_scared_oh3 noloop
        mc "Really?"
        scene sm1cs_my002-113 thiss_art_my_talk with dissolve
        play voice3 girl34_yes_happy1 noloop
        my "Yes. I guess I have to grant an exception to the \"business art\" types."
        scene sm1cs_my002-114 thiss_art_mc_talk with dissolve
        play voice2 mc_happy_hah1 noloop
        mc "Good, I would hope so!"
    elif sm1cs_my002_date_points == 2:
        $ CharacterController.get_character("my").add_point(1)
        scene sm1cs_my002-111 thiss_art_my_talk_look with dissolve
        play voice3 girl34_hey_simple3 noloop
        my "You did well with your art knowledge today, [mcname]."
        scene sm1cs_my002-112 thiss_art_mc_talk with dissolve
        play voice2 mc_scared_oh3 noloop
        mc "Really? Thank you!"
        scene sm1cs_my002-113 thiss_art_my_talk with dissolve
        play voice3 girl34_yes_yeah8 noloop
        my "Of course!"
        scene sm1cs_my002-114 thiss_art_mc_talk with dissolve
        play voice2 mc_thinking_hm noloop
    else:
        scene sm1cs_my002-113 thiss_art_my_talk with dissolve
        play voice3 girl34_disappointed_eeh4 noloop
        my "Well, you definitely did your best today, [mcname]."
        scene sm1cs_my002-114 thiss_art_mc_talk with dissolve
        play voice2 mc_thinking_hm noloop
    if persistent.is_special:
        mc "Thanks, Mom."
    else:
        mc "Thanks, Melony."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs_my002-115 thiss_art_my_talk_walk with dissolve
    play voice3 girl34_thinking_emm2 noloop
    my "Well, [mcname], this has been fun. But I do think I'm going to try and find the gallery manager."
    scene sm1cs_my002-116 thiss_art_mc_talk_walk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, yeah. That makes sense."
    scene sm1cs_my002-117 thiss_art_my_talk_walk with dissolve
    play voice3 girl34_yes_yeap2 noloop
    my "Sometimes I'm all work, my apologies."
    my "But, I promise the next date we have will be less work and more fun."
    scene sm1cs_my002-118 thiss_art_mc_talk_walk_surprised with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Date?"
    scene sm1cs_my002-119 thiss_art_my_talk_walk_smile with dissolve
    play voice3 girl34_happy_laugh1 noloop
    my "Date, hang out, whatever you want to call it."
    my "But you've been quite the gentleman, so how could I not call it a date?"
    scene sm1cs_my002-120 thiss_art_mc_talk_walk with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "I, I guess so?"
    scene sm1cs_my002-121 thiss_art_my_talk_walk with dissolve
    play voice3 girl34_yes_aga2 noloop
    my "Of course."
    my "Well, work intrudes. I'll see you later, 'kay?"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs_my002-122 thiss_art_mc_talk_walkupto with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Sounds great! I look forward to our next... date."
    scene sm1cs_my002-123 thiss_art_my_talk with dissolve
    play voice3 girl34_happy_relief3 noloop
    my "Me too."
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs_my002-124 thiss_art_my_talk_cheekkiss with dissolve
    play voice3 girl34_happy_mmm2 noloop
    play sound mc_kiss2
    pause
    scene sm1cs_my002-125 thiss_art_my_talk_chio with dissolve
    play voice3 girl34_hey_seeya noloop
    my "Ciao, [mcname]!"
    scene sm1cs_my002-126 thiss_art_mc_talk_chio with dissolve
    play voice2 mc_hey_bye1 noloop
    if persistent.is_special:
        mc "See you later, Mom!"
    else:
        mc "See you later, Melony!"
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs_my002-127 thiss_art_mc_thought_walkout with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "Well, now I know that she knows they're dates."
    mct "And she wants to do more of them... so that's a good sign."
    mct "Now I just have to figure out what comes next..."
    stop sound4 fadeout 2.5
    play sound sfx_door_openclosed1
    stop sound2 fadeout 1.0
    jump sm1cs_my002_end_scene
label sm1cs_my002_end_scene:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(MY_STORY, 2, 0, 4, STUDIO, DEFAULT_SUBLOCATION, SD_CORNER)
    return
label sm1cs_my002_m01_c01:
    $ player.set_choice("sm1cs_my002_use_of_glaze")
    return
label sm1cs_my002_m01_c02:
    $ player.set_choice("sm1cs_my002_detail_of_alpheus")
    return
label sm1cs_my002_m01_c03:
    $ player.set_choice("sm1cs_my002_autumnal_palette")
    return
label sm1cs_my002_m01_c04:
    $ player.set_choice("sm1cs_my002_who_is_diana")
    return
label sm1cs_my002_m02_c01:
    $ player.set_choice("sm1cs_my002_neoclassical_painting")
    return
label sm1cs_my002_m02_c02:
    $ player.set_choice("sm1cs_my002_use_of_tempura")
    return
label sm1cs_my002_m02_c03:
    $ player.set_choice("sm1cs_my002_fascinating_choice")
    return
label sm1cs_my002_m02_c04:
    $ player.set_choice("sm1cs_my002_who_is_mischief")
    return
label sm1cs_my002_m03_c01:
    $ player.set_choice("sm1cs_my002_is_this_oil")
    return
label sm1cs_my002_m03_c02:
    $ player.set_choice("sm1cs_my002_light_green_fabric")
    return
label sm1cs_my002_m03_c03:
    $ player.set_choice("sm1cs_my002_golden_shower")
    return
label sm1cs_my002_m03_c04:
    $ player.set_choice("sm1cs_my002_chiaroscuro")
    return