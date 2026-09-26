image sm1ms019-a106-glm = Movie(play = "images/ms/s019/anim/sm1ms019-a106-4x-60fps.webm", start_image = "sm1ms019-a106 studio-flythrough-glambot-000", image = "sm1ms019-a106 studio-flythrough-glambot-348", loop = False)
label sm1ms019:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music take_the_ride_calm
    play sound sfx_box_slide
    scene sm1ms019-00 montage with dissolve
    pause
    scene sm1ms019-01 montage with fade
    play sound sfx_light_turn2
    pause
    play sound sfx_cloth_planket3
    scene sm1ms019-02 montage with fade
    pause
    scene sm1ms019-02-2 montage with fade
    play sound sfx_bed_slide3
    play sound2 sfx_book_closed1 noloop
    pause
    scene sm1ms019-02-3 montage with fade
    play sound2 sfx_box_placed1 noloop
    pause
    $ renpy.music.set_volume(0.5, 3.0, "music" )
    play sound sfx_door_closed1
    play sound2 sfx_heels_steps1
    scene sm1ms019-03 my_walksn_talk with dissolve
    play voice4 girl34_hey_simple2 noloop
    my "Hello?"
    queue sound sfx_heels_steps2 loop
    scene sm1ms019-04 sy_talk with dissolve
    play voice3 stacy_hey_attention1 noloop
    if persistent.is_special:
        sy "Hey, Mom!"
    else:
        sy "Hey, Melony!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms019-05 my_talk with dissolve
    play voice4 girl34_hey_hi4 noloop
    my "Hey, you two!"
    scene sm1ms019-06 my_talk_look with dissolve
    play voice4 girl34_thinking_hmm7 noloop
    my "The studio is really coming along!"
    scene sm1ms019-07 mc_talk with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Yeah! I think we're just putting the finishing touches on the studio now!"
    scene sm1ms019-08 my_talk with dissolve
    play voice4 girl34_happy_nice2 noloop
    my "Perfect! Then let me do the same with the painting!"
    play sound sfx_heels_steps1 loop
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    scene sm1ms019-09 my_walk_painitng with dissolve
    pause
    stop sound fadeout 2.0
    scene sm1ms019-10 mc_sy_working_studio with fade
    play sound sfx_bed_slide4
    pause
    stop sound fadeout 1.0
    scene sm1ms019-11 my_painting with fade
    play sound2 sfx_brush_painting3 volume 1.5 noloop
    pause
    stop sound2 fadeout 2.5
    scene sm1ms019-12 mc_sy_working_studio with fade
    play sound sfx_cloth_rustling4 volume 2.7
    pause
    $ renpy.music.set_volume(0.5, 3.0, "music" )
    scene sm1ms019-13 sy_talk_looking around with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "[mcname]...{w} are we...?"
    scene sm1ms019-14 mc_talk with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I think so. I think that's it."
    scene sm1ms019-15 sy_talk with dissolve
    play voice3 stacy_surprised_ohmy1 noloop
    sy "Oh my God!"
    play sound sfx_cloth_planket2 volume 1.6
    scene sm1ms019-16 sy_talk_hug with dissolve
    play voice3 stacy_happy_wooh1 noloop
    sy "We did it!"
    scene sm1ms019-17 mc_talk_hug with dissolve
    play voice2 mc_happy_yay3 noloop
    mc "We did! We renovated the studio!"
    scene sm1ms019-18 mc_talk_lookfelse with dissolve
    play voice2 mc_thinking_hmm1 noloop
    if persistent.is_special:
        mc "Let's go see how Mom's painting is coming along."
    else:
        mc "Let's go see how Melony's painting is coming along."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1ms019-19 mc_sywalk with dissolve
    pause
    scene sm1ms019-20 mc_sywalk with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms019-21 sy_talk with dissolve
    play voice3 stacy_surprised_wow1 noloop
    sy "Oh, wow..."
    scene sm1ms019-22 mc_talk with dissolve
    play voice2 mc_scared_huuuh1 noloop
    if persistent.is_special:
        mc "This is incredible, Mom!"
    else:
        mc "This is incredible, Melony!"
    scene sm1ms019-23 my_talk with dissolve
    play voice4 girl34_disappointed_mmf1 noloop
    my "Mmmm..."
    scene sm1ms019-24 mc_talk with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "What?"
    scene sm1ms019-25 my_talk with dissolve
    play voice4 girl34_no_nah2 noloop
    my "I don't think it's my best work."
    scene sm1ms019-26 sy_talk with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "Are you freaking kidding me! This is incredible!"
    scene sm1ms019-27 sy_talk_painting_shot with dissolve
    play voice3 stacy_hey_happy2 noloop
    sy "It looks {i}just{/i} like me!"
    scene sm1ms019-28 mc_talk with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "It really does. I mean, I don't know why you put the diamond in there, though..."
    scene sm1ms019-29 sy_talk_nervous with dissolve
    play voice3 stacy_surprised_oh1 noloop
    sy "Well, because weeee-"
    scene sm1ms019-30 sy_talk_relaxes with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Weeeellllllllll - you are building the studio on the ashes of Fetish Locator. I don't know, it felt important."
    sy "It's important to know where you came from, and never forget that."
    sy "Because if you don't know where you've been you'll never know where you're going."
    scene sm1ms019-31 mc_talk_my_shocked with dissolve
    play voice2 mc_surprised_wow4 noloop
    mc "Wow, Stacy..."
    scene sm1ms019-32 sy_talk with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "What?"
    scene sm1ms019-33 my_talk with dissolve
    play voice4 girl34_happy_laugh1 noloop
    my "That's just... surprisingly insightful, Stacy."
    scene sm1ms019-34 sy_talk with dissolve
    play voice3 stacy_hey noloop
    sy "Hey! I have my moments!"
    scene sm1ms019-35 my_talk_smiling with dissolve
    play voice4 girl34_yes_yeah8 noloop
    my "I know, Stacy."
    my "That's why I agreed to paint the picture of you."
    scene sm1ms019-36 my_talk_look_painting with dissolve
    play voice4 girl34_disappointed_eeh2 noloop
    my "Because, even though you both get into a shocking amount of trouble..."
    scene sm1ms019-37 my_talk_smiling_close with dissolve
    play voice4 girl34_happy_relief3 noloop
    my "When you two are together, you manage to keep each other... well, you manage to help each other out of trouble."
    scene sm1ms019-38 my_talk_turn_studio with dissolve
    play voice4 girl34_arrogant_ha1 noloop
    my "But enough of my sentimentality! I've been so preoccupied with the painting, I've missed how everything else has gone!"
    my "Give me the tour!"
    scene sm1ms019-39 mc_talk with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Uhm, yeah! Let's see - so you've seen the painting..."
    scene sm1ms019-40 my_talk with dissolve
    play voice4 girl34_arrogant_laugh1 noloop
    my "Very cute, [mcname]."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1ms019-41 mc_talk_look_around with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Uhm... first we have this new makeup area!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms019-42 mc_talk_gesture_makeup with dissolve
    play voice2 mc_happy_a1 noloop
    mc "So when I have actresses come in to work, they have a place to get ready!"
    scene sm1ms019-43 my_talk with dissolve
    play voice4 girl34_yes_aga6 noloop
    my "Smart, you'll need that. It's always better to expect models to come in half ready and need to hurry to finish putting themselves together."
    scene sm1ms019-44 sy_talk with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    if persistent.is_special:
        sy "Mom! Seems like you know some things about the porn industry."
    else:
        sy "Melony! Seems like you know some things about the porn industry."
    scene sm1ms019-45 my_talk with dissolve
    play voice4 girl34_yes_happy1 noloop
    my "Models are models. Whether in the adult industry, or the art world."
    my "No matter where you are, they're pretty much the same."
    scene sm1ms019-46 my_talk_look_kitchen with dissolve
    play voice4 girl34_thinking_mmm noloop
    my "It looks like the kitchen is about the same?"
    scene sm1ms019-47 mc_talk with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, I wasn't sure what to do with the kitchen."
    scene sm1ms019-48 my_talk with dissolve
    play voice4 girl34_no_neutral6 noloop
    my "No, that's fine. I love your kitchen as it is."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1ms019-49 my_talk_walk_tv with dissolve
    play voice4 girl34_surprised_oh3 noloop
    my "I see you finally got a TV!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms019-50 sy_talk with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah! I couldn't handle just staring at the walls anymore."
    scene sm1ms019-51 my_talk with dissolve
    play voice4 girl34_arrogant_huh1 noloop
    my "And you could afford this?"
    scene sm1ms019-52 mc_talk with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well, Stacy said we were buying this so we-erm, I could watch our playbacks for editing notes."
    scene sm1ms019-53 my_talk with dissolve
    play voice4 girl34_disappointed_oh2 noloop
    my "Ahhh..."
    play sound2 sfx_heels_steps1
    scene sm1ms019-54 my_talk_walk with dissolve
    play voice4 girl34_arrogant_ha5 noloop
    my "And the fact that it's a large TV that you can watch whenever you want is a perk?"
    scene sm1ms019-55 sy_talk with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "It's incredible how easy it is to make an excuse for a tax write off."
    play sound sfx_heels_steps2 loop
    scene sm1ms019-56 my_talk_towards stairs with dissolve
    play voice4 girl34_arrogant_hm2 noloop
    my "Oh, it can be anything you want if you try hard enough."
    my "It must be nice to finally be able to get upstairs!"
    play voice2 mc_yes_yes7 noloop
    mc "It is. We have so much more space now! So much room for activities!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms019-58 my_talk_look_photoarea with dissolve
    play voice4 girl34_happy_great1 noloop
    my "I see that your bed is finally off the floor!"
    scene sm1ms019-59 mc_talk with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "It is!"
    scene sm1ms019-60 my_talk with dissolve
    play voice4 girl34_disappointed_oof2 noloop
    my "It might be hard to sleep on a photo backdrop though."
    scene sm1ms019-61 sy_talk with dissolve
    play voice3 stacy_yes_yeah2 noloop
    sy "We moved it up to the second floor!"
    scene sm1ms019-62 sy_talk_arms_outturn with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "The whole first floor is for business, and the second floor is for pleasure!"
    scene sm1ms019-63 my_talk_arch_brow with dissolve
    play voice4 girl34_disappointed_eem1 noloop
    my "Pleasure?"
    scene sm1ms019-64 mc_talk with dissolve
    play voice2 d2s12_emmm noloop volume 1.6
    mc "She's, erm, being dramatic. It's mostly just for sleeping and living and whatnot."
    scene sm1ms019-65 my_talk with dissolve
    play voice4 girl34_yes_aga3 noloop
    my "Uh huh. And all of these posters of sex toys on the wall are just for the ambiance, right?"
    scene sm1ms019-66 mc_talk with dissolve
    play voice2 d1s5b_emmm noloop volume 1.7
    mc "Erm..."
    play sound2 sfx_heels_steps1
    scene sm1ms019-67 my_talk_walk_stairs with dissolve
    play voice4 girl34_arrogant_ha4 noloop
    my "That's what I thought."
    my "But I am excited to see what the upstairs looks like!"
    scene sm1ms019-68 mc_talk with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Me too, it's been a mystery to me what was up there this whole time!"
    stop sound2 fadeout 1.0
    scene sm1ms019-69 my_talk_bed with dissolve
    play voice4 girl34_surprised_wow1 noloop
    my "Oh wow, is this your bed, [mcname]?"
    scene sm1ms019-70 mc_talk with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Yeah!"
    scene sm1ms019-71 my_talk with dissolve
    play voice4 girl34_happy_relief1 noloop
    my "I don't believe it..."
    play sound sfx_cloth_rustling1
    scene sm1ms019-72 my_talk_lookunderbed with dissolve
    play voice4 girl34_surprised_ohmy1 noloop
    my "You have an actual bed frame!"
    scene sm1ms019-73 mc_talk with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, I figured I can't have people over and see my mattress on the floor."
    scene sm1ms019-74 my_talk with dissolve
    play voice4 girl34_surprised_huh5 noloop
    my "But why on the stairs landing?"
    play sound sfx_metal_fence1
    scene sm1ms019-75 sy_talk_armsout with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "So [mcname] can look over his kingdom!"
    sy "Because everything the light touches, is a part of his kingdoooooom!"
    scene sm1ms019-76 my_talk with dissolve
    play voice4 girl34_thinking_hmm4 noloop
    my "Hmmmm... that's one way to look at it."
    scene sm1ms019-77 mc_talk with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I mean, I do pay rent here."
    scene sm1ms019-78 sy_talk with dissolve
    play voice3 stacy_angry noloop
    sy "Sometimes?"
    scene sm1ms019-79 my_sylook with dissolve
    pause
    scene sm1ms019-80 mc_talk with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    if persistent.is_special:
        mc "She's joking, Mom. I, erm, always pay my rent!"
    else:
        mc "She's joking, Melony. I, uhm, always pay my rent!"
    scene sm1ms019-81 my_talk with dissolve
    play voice4 girl34_disappointed_mmf4 noloop
    my "I hope so..."
    play sound sfx_heels_steps1 loop
    scene sm1ms019-82 my_talk_walk with dissolve
    play voice4 girl34_disappointed_oof1 noloop
    my "I see the decorating trend continued with the posters."
    play sound2 sfx_heels_steps2
    scene sm1ms019-83 mc_talk with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Yeah, it's all about, uhm, the aesthetic."
    scene sm1ms019-84 my_talk_keep_walking with dissolve
    play voice4 girl34_thinking_hmm6 noloop
    my "There's definitely an aesthetic..."
    scene sm1ms019-85 mc_talk_keep_walking with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Yeah, and then we have a little spot to do some editing, and there are some empty rooms that we... I guess just have. I might try and see if anyone wants to live here."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms019-86 my_talk_doors with dissolve
    play voice4 girl34_surprised_ah2 noloop
    my "You're going to rent out rooms in your porn studio? I feel like that might get dicey, [mcname]."
    scene sm1ms019-87 mc_talk_doors with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "Well, we wouldn't let just anyone move in. I'd probably only really ask if any of the actresses, if they were interested."
    scene sm1ms019-88 my_talk with dissolve
    play voice4 girl34_disgust_ooh2 noloop
    my "Oh, that can only end in tears."
    scene sm1ms019-89 mc_talk with dissolve
    play voice2 mc_surprised_why3 noloop
    mc "Why?"
    scene sm1ms019-90 my_talk with dissolve
    play voice4 girl34_angry_hmf noloop
    my "Living with adult movie stars? The amount of trouble you'll get into, [mcname]."
    scene sm1ms019-91 mc_talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Maybe. But I know a few of them are already in tight spots with where they're currently living."
    mc "And here at least they'll have their own room, and a good landlord-"
    scene sm1ms019-92 sy_talk with dissolve
    play voice3 stacy_angryhuh noloop
    sy "I think you'll only ever be a decent landlord."
    scene sm1ms019-93 mc_talk with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Ha. Ha. Very funny, Stacy."
    scene sm1ms019-94 mc_talk_serious with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "But in all seriousness, some of them just need a better place to live. And there are a lot of rooms here that are just sitting empty."
    scene sm1ms019-95 my_talk with dissolve
    play voice4 girl34_happy_mmm1 noloop
    my "Hm..."
    scene sm1ms019-96 mc_talk with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What?"
    scene sm1ms019-97 my_talk with dissolve
    play voice4 girl34_thinking_emm3 noloop
    my "When you lay it out like that, it sounds like you're doing it for at least a somewhat good reason."
    scene sm1ms019-98 mc_talk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Well, I'm doing what I can at least."
    play sound sfx_metal_fence2
    scene sm1ms019-99 my_talk_railing with dissolve
    play voice4 girl34_happy_relief4 noloop
    if persistent.is_special:
        my "My son... running a porn studio."
        scene sm1ms019-100 mc_talk with dissolve
        play voice2 mc_disappointed_ah1 noloop
        mc "Mom..."
    else:
        my "I still can't believe you're opening a porn studio, [mcname]."
        scene sm1ms019-100 mc_talk with dissolve
        play voice2 mc_disappointed_ah1 noloop
        mc "Melony..."
    scene sm1ms019-101 my_talk_lean with dissolve
    play voice4 girl34_thinking_emm1 noloop
    my "I do still wish you were going back to college."
    scene sm1ms019-102 mc_talk with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "M-"
    scene sm1ms019-103 my_talk with dissolve
    play voice4 girl34_angry_dough noloop
    my "Let me finish."
    my "I do wish college was on the table, but you seem happy. And you are passionate about it."
    my "And I love you, and I want to see you succeed."
    my "The studio looks great, you finally have a bedframe... I'm proud of how hard you're working on this."
    scene sm1ms019-104 mc_talk with dissolve
    play voice2 mc_surprised_wow2 noloop
    if persistent.is_special:
        mc "Wow... Thanks, Mom."
    else:
        mc "Wow... Thanks, Melony."
    play sound sfx_cloth_rustling2
    scene sm1ms019-105 my_talk with dissolve
    play voice4 girl34_yes_ugu1 noloop
    my "Of course, [mcname]."
    play sound3 sfx_camera_fly2 noloop volume 1.6
    play sound4 ["<silence 17.0>", sfx_camera_fly1] noloop volume 2.0
    play sound2 ["<silence 19.5>", sfx_camera_fly1] noloop volume 2.0
    scene sm1ms019-a106 studio-flythrough-glambot-000 with dissolve
    pause
    scene sm1ms019-a106-glm
    pause
    play voice4 girl34_happy_laugh3 noloop
    my "I'll also say, this place has become the perfect little party pad! I think you'll have some great wrap parties here."
    my "And I would know."
    play voice2 mc_angry_huh2 noloop
    mct "Wait... is she saying what I think she's saying?"
    if persistent.is_special:
        mct "I didn't realize Mom had such a crazy life... before us."
    else:
        mct "I didn't realize Melony has had such a crazy life..."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    stop sound3 fadeout 1.0
    stop sound4 fadeout 1.0
    scene sm1ms019-107 my_talk_walk_stair with dissolve
    play voice4 girl34_happy_relief5 noloop
    my "Thank you for the tour! I do have to get going though."
    scene sm1ms019-108 sy_talk with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "What, have you got a hot date or something?"
    scene sm1ms019-109 my_talk_walk_stair with dissolve
    play voice4 girl34_arrogant_pff noloop
    my "Don't be ridiculous, Stacy. I may not be at home, but I do still have work to do. I'm scheduled for a phone call in a half hour, and I need to be in my hotel room for that."
    play sound3 sfx_metal_fence1 noloop
    scene sm1ms019-110 sy_talk with dissolve
    play voice3 stacy_disappointed_oh3 noloop
    sy "I imagine you'll have to get back soon... galleries don't run themselves."
    scene sm1ms019-111 my_talk with dissolve
    play voice4 girl34_no_nah3 noloop
    my "I plan to be around for a bit longer. Just in case [mcname] changes his mind about college."
    my "And I haven't had a chance to see your place yet!"
    scene sm1ms019-112 sy_talk with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Oh, the, uhm... recarpeting of the lobby is taking longer than expected."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1ms019-113 my_talk_stop with dissolve
    play voice4 girl34_arrogant_huh3 noloop
    my "I thought it was a fumigation?"
    scene sm1ms019-114 sy_talk with dissolve
    play voice3 stacy_yes_simple1 noloop
    sy "Uhm, it is! And after they finished that, they decided that the carpet was, uhm the problem."
    scene sm1ms019-115 my_talk with dissolve
    play voice4 girl34_arrogant_aga noloop
    my "Uh huh..."
    scene sm1ms019-116 mc_talk_allbydoor with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "How is work going, being so far away?"
    scene sm1ms019-117 my_talk_smirk with dissolve
    play voice4 girl34_disappointed_oh1 noloop
    my "Oh, you can train a monkey how to do my job."
    my "But let's just say I have a few assets that keep the artists stupefied, which keeps them from making too many ridiculous demands of the gallery."
    scene sm1ms019-118 sy_talk_special with dissolve
    play voice3 stacy_surprised_ah1 noloop
    if persistent.is_special:
        sy "Mom!"
    else:
        sy "Melony!"
    scene sm1ms019-119 my_talk with dissolve
    play voice3 girl34_angry_ahem2 noloop
    my "Oh, I don't want to hear it from you, missy."
    my "But I actually need to step out and take a call real quick from a... persistent client."
    scene sm1ms019-120 my_talk_walkingout with dissolve
    play voice3 girl34_hey_bye7 noloop
    my "I'll be right back!"
    scene sm1ms019-121 mc_talk_walkingout with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "See you in a sec!"
    play sound sfx_door_openclosed1
    scene sm1ms019-122 mc_talk_hangout with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Wow... I can't believe we're really done with the renovation."
    scene sm1ms019-123 sy_talk with dissolve
    play voice3 stacy_happy_phew1 noloop
    sy "Neither can I."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1ms019-124 mc_talk_walk_couch with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "I think it's time for us to just kick back and relax in our new studio!"
    play sound sfx_cloth_rustling5
    scene sm1ms019-125 sy_talk_mc_couch with dissolve
    play voice3 stacy_happy_hmm1 noloop
    if persistent.is_special:
        sy "Man... Mom was feeling a little spicy today."
    else:
        sy "Man... Melony was feeling a little spicy today."
    stop sound2 fadeout 1.0
    scene sm1ms019-126 mc_talk with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "What makes you say that?"
    play sound sfx_cloth_rustling2
    scene sm1ms019-127 sy_talk_leancouch_mclooktv with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Did you hear her talking about her ass?"
    scene sm1ms019-128 mc_talk with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What!?"
    scene sm1ms019-129 sy_talk with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "What did you think she meant by \"her assets\"?"
    scene sm1ms019-130 mc_talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "I mean, maybe she was talking about... her charming personality?"
    scene sm1ms019-131 sy_talk with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "And then there was her comments about models and wrap parties-"
    scene sm1ms019-132 mc_talk with dissolve
    play voice2 d9s2_yeah noloop volume 1.8
    if persistent.is_special:
        mc "Mom has been in the art world for like, ever. She's probably met her fair share of models and been to her fair share of wrap parties."
    else:
        mc "Melony has been in the art world for like, ever. She's probably met her fair share of models and been to her fair share of wrap parties."
    play sound sfx_cloth_rustling1
    scene sm1ms019-133 sy_talk_lean with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "Well, then there was her sticking out her ass every chance she got."
    scene sm1ms019-134 mc_talk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Or she was just bending over like a normal person."
    scene sm1ms019-135 sy_talk with dissolve
    play voice3 stacy_no_uhuh4 noloop
    sy "With an ass like that, there's no just \"bending over like a normal person\", [mcname]."
    scene sm1ms019-136 mc_talk with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I think you're imagining things, Stacy."
    scene sm1ms019-137 sy_talk_closer with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "Maybe... but, maybe not."
    if persistent.is_special:
        sy "A woman has needs, [mcname]. And Mom is a woman."
    else:
        sy "A woman has needs, [mcname]. And Melony is a woman."
    scene sm1ms019-138 mc_talk with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah, and?"
    scene sm1ms019-139 sy_talk with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "When was the last time there was a guy around?"
    scene sm1ms019-140 mc_talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "I mean..."
    scene sm1ms019-141 sy_talk with dissolve
    play voice3 stacy_arrogant_hmm2 noloop
    sy "Never. Never is the answer."
    play sound sfx_cloth_rustling4
    scene sm1ms019-142 sy_talk_grab with dissolve
    play voice3 stacy_moan4 noloop
    sy "And you know... maybe she just wants some male attention."
    sy "Maybe... from you."
    scene sm1ms019-143 mc_talk with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What, you're nuts, Stacy."
    mc "Like, you have said some crazy things before, but this one might just be the most insane thing to ever come out of your mouth."
    scene sm1ms019-144 sy_talk with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "I'm just saying! I'm picking up a vibe from her."
    scene sm1ms019-145 mc_talk with dissolve
    play voice2 mc_no_nah2 noloop
    mc "I think it might be your own horny vibe, Stacy."
    scene sm1ms019-142 sy_talk_grab with dissolve
    play voice3 stacy_no_uhuh3 noloop
    sy "Nuh uh. It's palpable, [mcname]."
    sy "Just something to think about."
    play sound sfx_cloth_rustling3
    scene sm1ms019-146 sy_talk_stand with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "All I know is we have to do something about her. Because I have my own needs that need taken care of."
    sy "And while she's around, it's hard to take care of those needs."
    sy "Just think about it, I need to go get ready."
    scene sm1ms019-147 mc_talk with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Ready for what?"
    play sound sfx_heels_steps2 loop
    scene sm1ms019-148 sy_talk_walkstairs with dissolve
    play voice3 stacy_arrogant_huh5 noloop
    sy "We're going out tonight to celebrate!"
    mc "Wait, I thought we were going to relax-"
    sy "Nuh uh! We need to celebrate! And you need to celebrate too!"
    scene sm1ms019-149 mc_thought with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "Ugh... I just wanted to kick back and relax tonight."
    mct "But, Stacy gets what Stacy wants..."
    mct "And it'll be good to go out. Get out of the house for a bit."
    mct "There's no way... Stacy is just imagining things."
    if persistent.is_special:
        mct "Mom wouldn't... couldn't think about me like that."
    else:
        mct "Melony wouldn't... couldn't think about me like that."
    mct "Right?..."
    mct "Maybe..."
    mct "But when has Stacy been wrong?"
    play sound sfx_tv_off2
    play sound2 sfx_tv_film2 fadein 1.5
    scene sm1ms019-150 mc_thought_remote with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Nah, she's just being crazy and horny. There's no way..."
    mct "There's just no way..."
    stop sound2 fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2")
    if vn_mode:
        $ renovation_controller.set_progress(100)
    jump sm1ms019_exit_to_studio
label sm1ms019_exit_to_studio:
    $ StoryController.end_scene(MS, 5, 0, 2)
    return