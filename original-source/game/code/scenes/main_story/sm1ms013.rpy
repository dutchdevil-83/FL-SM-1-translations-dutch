image sm1ms013-a42-glm = Movie(play = "images/ms/s013/anim/sm1ms013-a42-2x-60fps.webm", start_image = "sm1ms013-a42 melony-walk-glambot-040", image = "sm1ms013-a42 melony-walk-glambot-220", loop = False)
label sm1ms013:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound sfx_heels_run2
    scene sm1ms013-11 sy_run_bed with dissolve
    play music slow_love
    pause
    queue sound sfx_heels_run2 loop
    scene sm1ms013-12 sy_talk_mcstand with dissolve
    play voice3 stacy_hey noloop
    if persistent.is_special:
        sy "Oh hey! That reminds me. You should call Mom!"
        scene sm1ms013-13 mc_talk_mcstand with dissolve
        play voice2 mc_surprised_uh1 noloop
        mc "You getting the redhead wig reminds you of Mom?"
    else:
        sy "Oh hey! That reminds me. You should call Melony!"
        scene sm1ms013-13 mc_talk_mcstand with dissolve
        play voice2 mc_surprised_uh1 noloop
        mc "You getting the redhead wig reminds you of Melony?"
    scene sm1ms013-14 sy_talk with dissolve
    play voice3 stacy_no_simple1 noloop
    sy "No! But she tried calling me like 18 times today, but I was busy. One of us should probably call her at some point."
    stop sound fadeout 2.0
    scene sm1ms013-15 mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, I can do that."
    play sound [sfx_cloth_rustling5, sfx_cloth_rustling3]
    scene sm1ms013-16 sy_talk_look_mattress with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "It was kind of weird she tried calling me so many times in a row."
    scene sm1ms013-17 mc_talk_look with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Well, why didn't you answer the phone?"
    scene sm1ms013-18 sy_talk_hornysmirk with dissolve
    play voice3 stacy_happy_laugh1 noloop
    sy "I might have been watching our maid video... Apparently it ended up online."
    scene sm1ms013-19 mc_talk_nervous with dissolve
    play voice2 d2s12_emmm noloop
    mc "Isn't that... not good?"
    play sound sfx_cloth_rustling4
    scene sm1ms013-20 sy_talk with dissolve
    play voice3 stacy_no_nah3 noloop
    sy "It's totally fine! The client must have posted it. They said only good things, must have wanted to share it with everyone!"
    scene sm1ms013-21 mc_talk with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "I guess..."
    play sound sfx_skirt_off2
    scene sm1ms013-22 sy_talk_stand_wig with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "Besides, it'll be some good publicity for the studio!"
    sy "Found it!"
    play sound sfx_heels_steps2 loop
    scene sm1ms013-23 sy_talk_walkback with dissolve
    play voice3 stacy_thinking_emm4 noloop
    if persistent.is_special:
        sy "Promise me you'll call Mom?"
    else:
        sy "Promise me you'll call Melony?"
    scene sm1ms013-24 mc_talk_walkback with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I promise."
    stop sound fadeout 1.0
    scene sm1ms013-25 mc_talk_standfront with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I'll do it right after we fuck."
    scene sm1ms013-26 sy_talk_grin with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Mmmm... sounds good to me. I've kind of been wanting you to fuck my ass lately."
    scene sm1ms013-27 mc_talk with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Oh yeah?"
    scene sm1ms013-28 sy_talk_grin with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "Mmhmmmm... just some deep, hard, pound-"
    scene sm1ms013-29 sy_talk_lookdoor with dissolve
    play sound sfx_knock_wood2
    "*knock knock*"
    play voice3 stacy_surprised_huh1 noloop
    sy "Who the hell could that be?"
    scene sm1ms013-30 mc_talk_lookdoor with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I don't know. Were you expecting anyone?"
    scene sm1ms013-31 sy_talk_lookdoor with dissolve
    play voice3 stacy_no_nope1 noloop
    sy "Nope."
    scene sm1ms013-32 sy_talk_lookmc with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "It's probably not important. I'd rather have your cock buried in my ass, pounding-"
    play sound sfx_knock_wood2
    "*knock knock*"
    scene sm1ms013-33 sy_talkrritated with dissolve
    play voice3 stacy_angry_breath1 noloop
    sy "Goddamnit."
    scene sm1ms013-34 mc_talk_lookdoor with dissolve
    play voice2 d2s9_mchey noloop
    mc "I'll get it."
    scene sm1ms013-35 sy_talk with dissolve
    play voice3 stacy_happy_yay1 noloop
    sy "Cool, and then I can get the wig on, and you can use your magnificent cock to make me scream your name!"
    scene sm1ms013-36 mc_talk with dissolve
    play voice2 mc_angry_errr6 noloop
    mc "That sounds fucking awesome."
    scene sm1ms013-37 sy_talk_walkdoor_smiling with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "I never thought I'd enjoy wearing a wig so much!"
    stop music fadeout 6.0
    play sound sfx_door_open1
    scene sm1ms013-38 mc_opendoor with dissolve
    pause
    scene sm1ms013-38 mc_surprised with dissolve
    play voice2 d3s7_mcemm noloop volume 1.5
    pause
    scene sm1ms013-39 sy_talk with dissolve
    play voice3 stacy_thinking_emm3 noloop
    sy "Who is it?"
    $ renpy.music.set_volume(1.0, 2.0, "music" )
    scene sm1ms013-40 mc_talk with dissolve
    play music music_the_darker_side
    play voice2 mc_angry_huh2 noloop
    if persistent.is_special:
        mc "Uhm... hey, Mom."
    else:
        mc "Uhhh... hey, Melony."
    scene sm1ms013-40 mc_talk_glambot with dissolve
    pause
    play sound3 sfx_heels_steps1 loop
    play sound2 sfx_door_closed1 noloop
    scene sm1ms013-41 sy_talk_my_walkin with dissolve
    play voice3 stacy_surprised_huh2 noloop
    if persistent.is_special:
        sy "Mom!?"
    else:
        sy "Melony!?"
    sy "What are you doing here!?"
    scene sm1ms013-a42 melony-walk-glambot-040 with dissolve
    pause 0.1
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1ms013-a42-glm
    pause 4.0
    play voice4 girl34_surprised_what3 noloop
    if persistent.is_special:
        my "What, a mother can't check up on her children?"
    else:
        my "What, I can't check in on you two?"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1ms013-43 mc_talk with dissolve
    play voice2 mc_no_no6 noloop
    mc "No, that's not it! It's just, uh... a bit of a surprise is all."
    scene sm1ms013-44 my_talk with dissolve
    play voice4 girl34_thinking_emm1 noloop
    my "Well I haven't heard from either of you in forever, and it seems like Stacy's phone is broken. So I thought I'd make the trip."
    my "Hell, I haven't even seen where you two live! I had to figure it out from the one time Stacy asked me to mail her something from home!"
    scene sm1ms013-45 my_talk_arms_up with dissolve
    play voice4 girl34_happy_laugh1 noloop
    my "I'm sorry, I don't mean to harp on you."
    if persistent.is_special:
        my "Come here and give your mother a hug!"
    else:
        my "Come here and give me a hug!"
    $ renpy.music.set_volume(0.8, 10.0, "music" )
    play sound sfx_cloth_rustling4
    scene sm1ms013-46 mc_thought_hug with dissolve
    play voice2 d1s1_mmm noloop volume 2.0
    mct "Well... I didn't expect this to happen today..."
    play sound sfx_heels_steps1 loop
    scene sm1ms013-47 my_talk_looksy with dissolve
    play voice4 girl34_hey_happy noloop
    my "And my dear, sweet Stacy."
    stop sound fadeout 1.0
    scene sm1ms013-48 my_talk_standinfront with dissolve
    play voice4 girl34_happy_relief1 noloop
    my "It is so good to see you two! I miss you both so much."
    play sound sfx_cloth_rustling3
    scene sm1ms013-49 sy_talk_hug with dissolve
    play voice3 stacy_happy_relief1 noloop
    if persistent.is_special:
        sy "Yeah, erm, it's soooo good to see you too, Mom!"
    else:
        sy "Yeah, uhhh, it's great to see you too, Melony!"
    scene sm1ms013-50 my_talk_hug with dissolve
    play voice4 girl34_happy_laugh2 noloop
    my "You really need to start answering my calls!"
    scene sm1ms013-51 sy_talk_hug with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "I, erm, totally will! Is that why you stopped by?"
    play sound sfx_cloth_rustling2
    scene sm1ms013-52 my_talk_stepback with dissolve
    play voice4 girl34_no_questioning2 noloop
    my "Not exactly... I actually need to talk to [mcname] about something."
    scene sm1ms013-53 mc_talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh?"
    scene sm1ms013-54 sy_talk_special with dissolve
    play voice3 stacy_pain_huh1 noloop
    if persistent.is_special:
        sy "Everything okay, Mom?"
    else:
        sy "Everything okay, Melony?"
    scene sm1ms013-55 my_talk with dissolve
    play voice4 girl34_thinking_eeh1 noloop
    my "Can you give us a moment, Stacy?"
    scene sm1ms013-56 mc_talk_concerned with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Is everything okay?"
    scene sm1ms013-57 sy_talk_concerned with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Should we be worried about something?"
    scene sm1ms013-58 my_talk with dissolve
    play voice4 girl34_happy_relief2 noloop
    my "Please, Stacy-"
    scene sm1ms013-59 mc_talk with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "If there's something we need to talk about, Stacy can be here. We talk about everything."
    scene sm1ms013-60 my_talk with dissolve
    play voice4 girl34_angry_breath1 noloop
    my "{size=*0.6}I hope not...{/size}"
    scene sm1ms013-61 mc_talk with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Huh?"
    scene sm1ms013-62 my_talk with dissolve
    play voice4 girl34_no_nonono3 noloop
    my "It's nothing... [mcname], Stacy-"
    scene sm1ms013-63 mc_talk with dissolve
    play voice2 d1s5b_emmm noloop volume 1.4
    mc "Why, uhm, don't we sit in the kitchen and talk?"
    scene sm1ms013-64 my_talk_mc_thought with dissolve
    play voice4 girl34_disappointed_eem1 noloop
    my "That would be good... this might be a conversation to have sitting down."
    mct "I don't like the sound of that..."
    play sound sfx_heels_steps1 loop
    scene sm1ms013-65 my_talk_goingtable with dissolve
    play voice4 girl34_disappointed_huh noloop
    my "Are you coming, Stacy?"
    scene sm1ms013-66 sy_talk with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Yep! Just one second!"
    play sound sfx_bed_slide2
    scene sm1ms013-67 my_talk_sit with dissolve
    play voice4 girl34_disappointed_mmf4 noloop
    my "[mcname]..."
    scene sm1ms013-68 mc_talk_sit with dissolve
    play voice2 d9s2_mcyes2 noloop volume 2.7
    if persistent.is_special:
        mc "Yes, Mom?"
    else:
        mc "Yes, Melony?"
    scene sm1ms013-69 my_talk_sylook with dissolve
    play voice4 girl34_angry_ahem4 noloop
    my "Is there something you want to tell me?"
    scene sm1ms013-70 mc_talk with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Uhm..."
    scene sm1ms013-71 my_talk with dissolve
    play voice4 girl34_arrogant_huh2 noloop
    my "No new changes? Nothing at all?"
    scene sm1ms013-72 mc_talk_serious with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I, uh..."
    scene sm1ms013-73 my_talk_mc_winces with dissolve
    play voice4 girl34_angry_argh2 noloop
    my "Maybe something about dropping out of college?"
    my "Did you honestly think I wasn't going to find out about that?!"
    scene sm1ms013-74 mc_talk with dissolve
    play voice2 mc_disappointed_off2 noloop
    mct "I was really hoping she wouldn't..."
    scene sm1ms013-75 my_talk with dissolve
    play voice4 girl34_angry_errr noloop
    if persistent.is_special:
        my "I got a letter in the mail last week about it. And I am... disappointed, to say the least."
        play voice2 mc_thinking_mmm3 noloop
        mc "Mom..."
    else:
        my "Your parents got a letter in the mail last week about it. And we are... disappointed, to say the least."
        play voice2 mc_thinking_mmm3 noloop
        mc "Melony..."
    scene sm1ms013-76 my_talk_lean with dissolve
    play voice4 girl34_no_nouh4 noloop
    my "I don't want to hear it."
    my "But, can you at least tell me {i}why{/i} you dropped out?"
    scene sm1ms013-77 mc_talk_thought_look_sy with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Shit... how do I tell her about everything that's happened? This is {u}not{/u} a conversation I want to have..."
    mc "Erm... I..."
    $ renpy.music.set_volume(0.0, 1.0, "music" )
    play sound sfx_comic_rewind
    scene sm1ms013-78 my_talk with dissolve
    $ renpy.music.set_pause(True, channel="music")
    play voice4 girl34_surprised_huh5 noloop volume 1.3
    my "Is it because you're making porn now?"
    scene sm1ms013-79 mc_talk_nervous with dissolve
    play voice2 mc_surprised_what8 noloop
    mc "Uhm... what?"
    $ renpy.music.set_pause(False, channel="music")
    $ renpy.music.set_volume(0.0, 0.0, "music" )
    scene sm1ms013-80 sy_talk with dissolve
    $ renpy.music.set_volume(0.8, 3.5, "music" )
    play voice3 stacy_scared_ah1 noloop
    sy "That's... that's crazy! [mcname]!"
    scene sm1ms013-81 my_talk_turnlooksy with dissolve
    play voice4 girl34_disappointed_oh2 noloop
    my "Oh, stop it."
    my "Did you know about this?"
    scene sm1ms013-82 sy_talk with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "Uhhhh..."
    scene sm1ms013-83 my_talk with dissolve
    play voice4 girl34_angry_nergh noloop
    my "Oh, who am I kidding. You two are as thick as thieves."
    scene sm1ms013-84 mc_talk with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    if persistent.is_special:
        mc "I'm not sure what to say, Mom..."
    else:
        mc "I'm not sure what to say, Melony..."
    mc "I never thought in a million years you would find out about this..."
    scene sm1ms013-85 my_talk_serious with dissolve
    play voice4 girl34_angry_argh1 noloop
    my "I received an email with a strange attachment... I didn't know what it was right away, but..."
    my "I saw the video with you and that redhead, whoever she is. I know you're making porn now."
    scene sm1ms013-86 mc_talk with dissolve
    play voice2 mc_thinking_wait1 noloop
    mc "Wait - you... you saw it?"
    scene sm1ms013-87 my_talk_embarassed with dissolve
    play voice4 girl34_disgust_ergh1 noloop
    my "I... did, unfortunately. But my personal time is not what we're talking about here. We're talking about why you dropped out of college."
    my "And whomever that redhead is."
    scene sm1ms013-90 my_talk with dissolve
    play voice4 girl34_surprised_huh7 noloop
    my "Do you know this redheaded gal, Stacy?"
    scene sm1ms013-89 sy_talk with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "Uhhhhhmmmmmm... nope."
    scene sm1ms013-88 my_talk_looksy with dissolve
    pause
    scene sm1ms013-91 my_talk_lookmc with dissolve
    play voice4 girl34_yes_yeah3 noloop
    my "Well, whoever she is, she... well, she's now immortalized on the internet making a pornographic film with you, [mcname]."
    my "So is that it? Did you decide to drop out of school because you're making porn?"
    scene sm1ms013-92 mc_talk with dissolve
    play voice2 mc_no_no9 noloop
    mc "That's not... entirely why."
    scene sm1ms013-93 my_talk with dissolve
    play voice4 girl34_thinking_hmm7 noloop
    my "Then does it have something to do with Fetish Locator?"
    scene sm1ms013-94 mc_talk_shock with dissolve
    play voice2 mc_surprised_what4 noloop
    mc "What did you just say?"
    scene sm1ms013-95 my_talk_shock with dissolve
    play voice4 girl34_angry_ahem1 noloop
    my "Fetish Locator. Is that why you dropped out of college?"
    play sound sfx_heels_steps2
    scene sm1ms013-96 mc_talk with dissolve
    stop sound fadeout 5.0
    play voice2 mc_angry_huh1 noloop
    mc "I... uh... how do you know about Fetish Locator?"
    scene sm1ms013-97 my_talk_serious with dissolve
    play voice4 girl34_hey_angry5 noloop
    my "Because I know how to use the internet, [mcname]. After I saw your video, I spent some time checking in on you and I found the stories about your school, and..."
    my "I can put two and two together."
    scene sm1ms013-98 mc_talk_syhiding with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "I... I'm not sure what to say."
    scene sm1ms013-99 my_talk_soften with dissolve
    play voice4 girl34_happy_relief3 noloop
    my "I'm not upset about... the porn, or Fetish Locator. I understand, I was young once too."
    mct "Wait, what did she just say?"
    my "But that doesn't mean you should abandon your studies!"
    play sound sfx_heels_steps2 loop
    scene sm1ms013-100 mc_talk_leanin_sysit with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Wait... you're not mad about Fetish Locator? Or about the porn?"
    stop sound fadeout 2.0
    scene sm1ms013-101 my_talk with dissolve
    play voice4 girl34_no_angry6 noloop
    my "No. I mean, is it awkward? Absolutely."
    play sound sfx_bed_slide3 volume 0.5
    scene sm1ms013-102 my_talk_leanback with dissolve
    play voice4 girl34_disappointed_eeh2 noloop
    if persistent.is_special:
        my "I did not expect to hear and see my son's... proclivities on the internet, but things happen."
    else:
        my "I didn't expect to learn so much about... your private life on the internet."
    my "I thought the worst thing I'd learn about you was in that box under your bed."
    scene sm1ms013-103 mc_talk_surprised with dissolve
    play voice2 mc_thinking_wait2 noloop
    mc "Wait... you knew about my special box!?"
    scene sm1ms013-104 my_talk with dissolve
    play voice4 girl34_arrogant_yeah noloop
    my "Did you think your room magically cleaned itself, [mcname]?"
    scene sm1ms013-105 sy_talk with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "She's got a good point there, [mcname]."
    scene sm1ms013-106 my_talk with dissolve
    play voice4 girl34_disgust_ooh2 noloop
    my "I won't even get started about what I found in your room, missy."
    scene sm1ms013-107 sy_talk_embarassed with dissolve
    play voice4 girl34_thinking_emm5 noloop
    my "But, we're off track. I did not want to come here and talk about your... personal moments."
    my "I came to try and get you to go back to school, [mcname]."
    scene sm1ms013-108 mc_talk with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    mc "I..."
    play sound sfx_cloth_rustling2
    scene sm1ms013-109 my_talk_reachout with dissolve
    play voice4 girl34_hey_simple2 noloop
    my "I know that maybe I'm asking a lot. It sounds like everything that happened at school was... tough on you."
    my "But can you at least think about it? For me?"
    scene sm1ms013-110 mc_talk_smile with dissolve
    play voice2 d9s2_yeah noloop volume 1.8
    if persistent.is_special:
        mc "Yeah, I can do that, Mom."
    else:
        mc "Yeah, I can do that, Melony."
    scene sm1ms013-111 my_talk_smile with dissolve
    play voice4 girl34_arrogant_aga noloop
    my "That's all I ask."
    my "And now that we have that uncomfortableness out of the way."
    play sound sfx_bed_slide2 volume 0.6
    scene sm1ms013-112 my_talk_stand with dissolve
    play voice4 girl34_surprised_wow3 noloop
    my "This is where you live! Why don't you give me the tour?"
    play sound sfx_cloth_rustling3
    scene sm1ms013-113 mc_talk_stand with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course! Let's see..."
    scene sm1ms013-114 mc_talk_standkitchentable with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "So, this is our kitchen and dining room."
    scene sm1ms013-115 mc_talk_stand_couch with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Our living room."
    scene sm1ms013-116 mc_talk_stand_bathroom with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Bathroom, and right next to it is the bedroom!"
    scene sm1ms013-117 my_talk_stand_bathroom with dissolve
    play voice4 girl34_thinking_emm2 noloop
    my "And what about the upstairs?"
    scene sm1ms013-118 mc_talk_sheepish with dissolve
    play voice2 d2s9_confused noloop
    mc "Uhm... well, we don't have stairs that go up there, so we haven't really looked it over yet."
    scene sm1ms013-119 my_talk with dissolve
    play voice4 girl34_thinking_hmm2 noloop
    my "I see..."
    scene sm1ms013-120 mc_talk with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Erm, what do you think?"
    scene sm1ms013-121 my_talk_lookaround with dissolve
    play voice4 girl34_thinking_eeh2 noloop
    my "I think... it could definitely use some work. I don't think I'm crazy about the condition your apartment is in."
    my "Hopefully your apartment is nicer, Stacy!"
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1ms013-122 sy_talk_walkmattress with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Oh, uhhhh, yeah! It totally is! It's just, uhm-"
    scene sm1ms013-123 mc_talk_walkmattress with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Getting fumigated!"
    scene sm1ms013-124 my_talk_walkmattress with dissolve
    play voice4 girl34_surprised_ah1 noloop
    my "Wait, really?"
    play sound3 sfx_leg_kick8 noloop volume 0.5
    scene sm1ms013-125 sy_talk_walkmattress with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Yep, unfortunately, uhm, one of my downstairs neighbors had a weird bug problem..."
    sy "So, [mcname] is letting me stay here!"
    scene sm1ms013-126 my_talk_walkmattress with dissolve
    play voice4 girl34_arrogant_huh1 noloop
    my "How kind of him!"
    scene sm1ms013-127 mc_talk_walkmattress with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yep - so kind!"
    stop sound fadeout 1.5
    stop sound2 fadeout 1.0
    scene sm1ms013-128 my_talk_nexttobed with dissolve
    play voice4 girl34_happy_laugh3 noloop
    my "Well, at least I know there isn't a secret stash of adult movies underneath this bed!"
    my "But maybe I should check, just for old time's sake."
    scene sm1ms013-129 sy_talk_nervous with dissolve
    play voice3 stacy_no_nonono2 noloop
    sy "You don't need to do that! [mcname] has totally cleaned up his act."
    play voice4 girl34_yes_aga8 noloop
    my "Mmmhmmmm."
    play sound2 sfx_heels_steps1
    scene sm1ms013-131 my_talk_walktomiddle with dissolve
    play voice4 girl34_happy_nice1 noloop
    my "At least your bathroom looks nice!"
    scene sm1ms013-132 mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah! That was a pleasant surprise."
    scene sm1ms013-133 my_talk_middleroom with dissolve
    play voice4 girl34_disappointed_eem2 noloop
    my "But so much of this place needs so much work... you especially need to get some stairs in here. And maybe a bed frame so you're not sleeping on the floor anymore."
    stop sound2 fadeout 1.0
    scene sm1ms013-134 mc_talk with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Those are all good things to do, for sure..."
    play sound sfx_hands_clap1
    scene sm1ms013-135 my_talk with dissolve
    play voice4 girl34_happy_yeah2 noloop
    my "Then it's decided!"
    scene sm1ms013-136 mc_sy_lookconfused with dissolve
    pause
    scene sm1ms013-137 mc_sy_talk with dissolve
    play voice3 stacy_surprised_huh3 noloop
    if persistent.is_special:
        sy "What's decided, Mom?"
    else:
        sy "What's decided?"
    scene sm1ms013-138 my_talk with dissolve
    play voice4 girl34_happy_relief5 noloop
    my "I'll stay around town and help you fix the place up!"
    scene sm1ms013-139 mc_talk_surprised with dissolve
    play voice2 mc_arrogant_huh2 noloop
    if persistent.is_special:
        mc "You don't need to do that, Mom!"
    else:
        mc "You don't need to do that, Melony!"
    scene sm1ms013-140 my_talk with dissolve
    play voice4 girl34_arrogant_pff noloop
    my "Oh, pish posh. It's no bother, really."
    my "I've been looking for a... new project lately, anywho. Something to keep me busy."
    scene sm1ms013-141 my_talk_lookaround with dissolve
    play voice4 girl34_disappointed_eeh3 noloop
    my "After you two left, life got quiet... I find myself needing something to do."
    my "I'm staying just down the street as well! So I can come by every day and help out. Plus, it gives me a chance to spend some time with you two."
    play sound2 sfx_heels_steps1
    scene sm1ms013-142 my_talk_walksinfront with dissolve
    play voice4 girl34_arrogant_ha3 noloop
    my "Maybe convince someone here to go back to college!"
    scene sm1ms013-143 mc_talk with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Uhm, yeah."
    stop sound2 fadeout 1.0
    scene sm1ms013-144 my_talk with dissolve
    play voice4 girl34_disappointed_ehh2 noloop
    my "But, I should go and check into my hotel. Plus, you two have lots to talk about I imagine."
    scene sm1ms013-145 my_talk_armsout with dissolve
    play voice4 girl34_thinking_hmm4 noloop
    if persistent.is_special:
        my "Give your mother a hug, and I'll see you tomorrow, okay?"
        play sound sfx_cloth_rustling4
        scene sm1ms013-146 my_talk_hug with dissolve
        play voice4 girl34_happy_mmm1 noloop
        my "I love you, [mcname]."
        scene sm1ms013-147 mc_talk_hug with dissolve
        play voice2 mc_yes_ugu1 noloop
        mc "I love you too, Mom."
        play sound sfx_cloth_rustling3
        scene sm1ms013-148 my_talk_hug with dissolve
        play voice4 girl34_hey_laughing noloop
        my "And I love you too, Stacy."
        scene sm1ms013-149 sy_talk_hug with dissolve
        play voice3 stacy_laugh4 noloop
        sy "Love ya, Mom."
    else:
        my "Give me a hug, and I'll see you tomorrow, okay?"
        play sound sfx_cloth_rustling4
        scene sm1ms013-146 my_talk_hug with dissolve
        play voice4 girl34_happy_mmm1 noloop
        my "I'm so happy to see you again, [mcname]."
        scene sm1ms013-147 mc_talk_hug with dissolve
        play voice2 mc_yes_ugu1 noloop
        mc "You too, Melony."
        play sound sfx_cloth_rustling3
        scene sm1ms013-148 my_talk_hug with dissolve
        play voice4 girl34_hey_laughing noloop
        my "And you too, Stacy."
        scene sm1ms013-149 sy_talk_hug with dissolve
        play voice3 stacy_laugh4 noloop
        sy "Yeah, it's great seeing you, Melony."
    play sound2 sfx_heels_steps1
    scene sm1ms013-150 my_talk with dissolve
    play voice4 girl34_hey_bye3 noloop
    my "All right, I'll see you both tomorrow morning! Bye!"
    scene sm1ms013-151 mc_talk_wave with dissolve
    play voice2 mc_hey_bye1 noloop
    mc "Bye!"
    scene sm1ms013-152 mc_talk_lookeachother with dissolve
    play voice2 mc_angry_errr5 noloop
    mc "Shit."
    scene sm1ms013-153 sy_talk with dissolve
    play voice3 stacy_disappointed_oh1 noloop
    sy "You can say that again."
    play sound2 sfx_door_closed2 noloop
    scene sm1ms013-154 mc_talk with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "...{w} Shit."
    if persistent.is_special:
        mc "It is going to be way harder to run a porn studio with Mom around."
    else:
        mc "It is going to be way harder to run a porn studio with Melony around."
    scene sm1ms013-155 sy_talk_lookaround with dissolve
    play voice3 stacy_disappointed_ehh4 noloop
    sy "It definitely is..."
    sy "But, she's really only sticking around because the studio is such a mess, right?"
    scene sm1ms013-156 mc_talk_lookaround with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Uh huh."
    scene sm1ms013-157 sy_talk with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "And we already needed to fix it up for the next video, right?"
    scene sm1ms013-158 mc_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, we did."
    scene sm1ms013-159 sy_talk_smile with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "So, we just have her help us out with the studio, and when we're all done she'll head back home and we can celebrate by butt fucking!"
    scene sm1ms013-160 mc_talk_smile with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I like the sound of that."
    scene sm1ms013-161 sy_talk_horny with dissolve
    play voice3 stacy_happy_yay2 noloop
    sy "Yay! Me too!"
    sy "I also like the sound of putting that wig on and going to pound town right now."
    scene sm1ms013-162 mc_talk with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "I wish we could Stacy, but it sounds like I need to start figuring out how to renovate the studio."
    scene sm1ms013-163 sy_talk_disappointed with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "Fiiiiiiiiiiiine."
    play sound sfx_heels_steps2 loop
    scene sm1ms013-164 mc_talk_walkdoor with dissolve
    play voice2 mc_angry_off noloop
    mc "And maybe we should start locking the front door."
    if persistent.is_special:
        mc "You remember how Mom was, never remembering to knock."
    else:
        mc "You know how Melony is, she always forgets to knock."
    stop sound fadeout 1.0
    scene sm1ms013-161 sy_talk_horny with dissolve
    play voice3 stacy_happy_laugh4 noloop
    sy "I think that makes it more fun!"
    scene sm1ms013-160 mc_talk_smile with dissolve
    play voice2 mc_scared_oh1 noloop
    mc "You're insane."
    scene sm1ms013-159 sy_talk_smile with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "But you love it!"
    scene sm1ms013-158 mc_talk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "For better or worse."
    play sound sfx_heels_steps2 loop
    scene sm1ms013-165 mc_talk_walkdoor with dissolve
    pause
    play sound sfx_door_open1
    scene sm1ms013-166 mc_talk_outdoor with dissolve
    pause
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(MS, 2, 0, 6)
    return