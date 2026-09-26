label sm1cs_ns008:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.6, 1.0, "music" )
    play sound4 sfx_office_ambience1 fadein 2.0
    play sound sfx_heels_steps2 loop
    scene sm1cs-ns008-01 mc-ns-am-think-notice-nari with dissolve
    play music music_pixel_funk fadein 2.5
    play voice2 mc_thinking_hmm5 noloop
    mct "Alright, things are quiet. Perfect time to say hello to Nari."
    mct "It's strange; I kind of imagined she'd come to talk to me about our date night. She's usually so excitable."
    stop sound fadeout 1.0
    scene sm1cs-ns008-02 mc-ns-talk-greet-nari with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey Nari."
    scene sm1cs-ns008-03 mc-ns-am-nari-look-tired with dissolve
    play sound sfx_mouse_clicks1 volume 0.8
    play voice3 nari_disappointed_mff noloop
    ns "..."
    scene sm1cs-ns008-04 mc-ns-reach-out-hand with dissolve
    pause
    scene sm1cs-ns008-05 mc-ns-think-dont-bother with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Probably should just leave her be for now. Looks like she's really focused on her assignment."
    play sound sfx_chair_slide1
    scene sm1cs-ns008-06 mc-ns-think-sit with dissolve
    mct "I wonder what's going on with her?"
    scene sm1cs-ns008-07 mc-ns-am-ag-think-concerned-nari-eyes-closed with dissolve
    mct "She still hasn't talked to me about why she had to rush off so quickly that night we were together..."
    play sound sfx_heels_steps1
    scene sm1cs-ns008-08 mc-ns-am-ag-am-cw-claire-enters-main-area with dissolve
    stop sound fadeout 2.0
    pause
    scene sm1cs-ns008-09 cw-talk-announce-meeting with dissolve
    play voice4 girl29_hey_angry noloop
    cw "Look alive, C.U.M Division. I need Peter, Eugene, Anna, April, Jayden, Nari, and [mcname]."
    scene sm1cs-ns008-10 cw-talk-five-minutes-hold-up-hand with dissolve
    play voice4 girl29_thinking_hm noloop
    cw "Conference room in five minutes."
    play sound sfx_heels_steps1
    scene sm1cs-ns008-11 mc-ns-am-ag-am-cw-claire-leaves with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mct "Great. Another meeting. Nari loves meetings."
    stop sound fadeout 1.0
    scene sm1cs-ns008-12 mc-think-happy with dissolve
    mct "Maybe this will get her out of her funk."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-ns008-13 ns-am-ag-leaving-for-meeting with dissolve
    pause
    play sound3 sfx_chair_slide1 noloop
    scene sm1cs-ns008-14 ns-mc-think-get-out-of-chair with dissolve
    pause
    stop sound2 fadeout 3.0
    scene sm1cs-ns008-15 ns-mc-talk-wake-up-nari with dissolve
    play sound sfx_cloth_rustling2
    play voice2 mc_znames_nari3 noloop
    mc "Nari. Claire needs us in the conference room."
    scene sm1cs-ns008-16 ns-mc-talk-groggy with dissolve
    play voice3 nari_disappointed_eh noloop
    ns "Huh?"
    play sound sfx_chair_slide1
    scene sm1cs-ns008-17 ns-mc-talk-happy with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Oh, [mcname]."
    ns "Hi there."
    scene sm1cs-ns008-18 ns-mc-talk-response with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Hello, cutie."
    mc "Claire needs us in the conference room."
    play sound sfx_mouse_clicks1
    scene sm1cs-ns008-19 ns-mc-talk-random-fact with dissolve
    stop sound fadeout 3.0
    play voice3 nari_yes_sad noloop
    ns "Right, right. Conference room."
    ns "Did you know that the word \"conference\" comes from the Medieval Latin word conferentia, which means \"contribution, discussion\"?"
    scene sm1cs-ns008-20 ns-mc-confused-reaction with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I did not know that."
    mc "Are you feeling alright, Nari? Do you want to talk about it?"
    play sound sfx_heels_steps1 loop
    scene sm1cs-ns008-21 ns-mc-talk-walk-concern with dissolve
    play voice3 nari_yes_yeah noloop
    ns "Everything is fine. Better than fine."
    ns "Don't tell anyone, but I kind of have a boyfriend now."
    play sound2 sfx_heels_steps2
    scene sm1cs-ns008-22 ns-mc-whisper with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Oh really?"
    scene sm1cs-ns008-23 ns-mc-walk-think with dissolve
    play voice3 nari_yes_questioning noloop
    ns "Yes. He's fun and supportive. And he's really kinky too. And we work together."
    play voice2 d3s11b_mcheh noloop volume 1.6
    mct "Alright, good to see her back to her usual self."
    scene sm1cs-ns008-24 ns-mc-cw-ag-am-enter-meeting-room with dissolve
    pause
    stop sound4 fadeout 4.0
    stop sound2 fadeout 1.0
    play sound sfx_door_openclosed1
    scene sm1cs-ns008-25 ns-mc-cw-ag-am-wide-shot-sit-at-meeting with dissolve
    pause
    scene sm1cs-ns008-26 cw-talk-focus-claire with dissolve
    play voice4 girl29_disappointed_ehh noloop
    cw "We have a new problem for our Channel Six Website Project."
    if player.has_played_scene("sm1fs_i005"):
        scene sm1cs-ns008-27 cw-am-false-talk-am-focus with dissolve
        play voice5 girl22_arrogant_he noloop
        am "What now? We're already trying to hook the damn virus."
        scene sm1cs-ns008-28 cw-am-false-talk-claire-focus with dissolve
        play voice4 girl29_no_questioning noloop
        cw "Thankfully, this isn't about the virus, but I hope one of you will have a solution to that soon."
    else:
        scene sm1cs-ns008-27 cw-am-false-talk-am-focus with dissolve
        play voice5 girl22_arrogant_he noloop
        am "Well, it can't be me. The coding is going smoothly as can be."
        if player.has_played_scene("sm1cs_am005"):
            scene sm1cs-ns008-30 am-else-talk-april-glance-at-mc with dissolve
            play voice5 girl22_thinking_hmm1 noloop
            am "And despite his handicap, [mcname] has been helping out a lot."
            scene sm1cs-ns008-31 cw-else-talk-claire-reaction with dissolve
            play voice4 girl29_thinking_oh noloop
            cw "Really."
            cw "That's what I like to hear, [mcname]."
            scene sm1cs-ns008-32 mc-ns-else-talk-mc-nervous with dissolve
            play voice2 mc_yes_yes2 noloop
            mc "Right. I won't let you down, Claire."
            scene sm1cs-ns008-28 cw-am-false-talk-claire-focus with dissolve
            play voice4 girl29_no_questioning noloop
            cw "But no, the code isn't the problem we need to go over."
    scene sm1cs-ns008-34 cw-talk-mad-trolls with dissolve
    play voice4 girl29_arrogant_ha noloop
    cw "The problem is a troll that always messes with Channel Six's old website. The one that we are replacing."
    scene sm1cs-ns008-35 cw-talk-laugh-eugene with dissolve
    play voice5 boy5_happy_laugh6 noloop
    en "Haha. They think they have a troll? Only I have seen real trolls."
    play sound sfx_cloth_rustling2
    scene sm1cs-ns008-36 cw-talk-laugh-alt-story with dissolve
    play voice5 boy5_arrogant_heh1 noloop
    en "Back in the old country trolls make a mess of everything."
    en "One year, my father did not sell a whole turnip because a villainous troll told people that my father's turnips would make them sterile!"
    scene sm1cs-ns008-37 cw-talk-sad-story with dissolve
    play voice5 boy5_disappointed_mmf3 noloop
    en "He was nearly ruined..."
    scene sm1cs-ns008-38 cw-talk-annoyed with dissolve
    play voice4 girl29_angry_breath noloop
    cw "Well, this prankster is fixing to be just as bad as the uh... one who ruined your father's business, Eugene."
    play sound sfx_cloth_rustling3
    scene sm1cs-ns008-39 cw-talk-focused with dissolve
    play voice4 girl29_thinking_mmm1 noloop
    cw "They've been a thorn in the side of Channel Six for years, and apparently, they've learned that we're working on a new website."
    cw "Angela called me today and warned me that the troll has now targeted the new website."
    scene sm1cs-ns008-40 cw-talk-triangle-hand with dissolve
    play voice5 boy7_no_nonono noloop
    pm "This cannot stand."
    pm "We have to strike first. We don't need some imbecile screwing up our new project."
    scene sm1cs-ns008-41 cw-ag-talk-not-sure with dissolve
    play voice6 girl27_arrogant_huh2 noloop
    ag "Well, some of these online disruptors have been agents of change recently. Maybe this person is just trying to call attention to mistakes made by the news studio."
    play sound sfx_hair_scratch1
    scene sm1cs-ns008-42 cw-talk-annoyed-hold-head with dissolve
    play voice4 girl29_happy_relief noloop
    cw "I didn't bring you all in to discuss the merits of online trolls."
    play sound sfx_cloth_rustling5
    scene sm1cs-ns008-43 cw-am-talk-notices-april with dissolve
    pause
    scene sm1cs-ns008-44 cw-am-talk-notices-april-alt with dissolve
    play voice4 girl29_yes_serious noloop
    cw "*sighs* Yes, April? Do you also have an opinion about trolls?"
    scene sm1cs-ns008-46 am-talk-grin with dissolve
    play voice5 girl22_no_uhuh1 noloop
    am "No. The only troll you guys should be worried about is the one who works here."
    scene sm1cs-ns008-47 ag-talk-angry-snap-back with dissolve
    play voice6 girl27_surprised_what noloop
    ag "What?"
    scene sm1cs-ns008-48 am-talk-angry-back-and-forth with dissolve
    play voice5 girl22_happy_laugh3 noloop
    am "I am the one who trolls, Anna."
    scene sm1cs-ns008-45 cw-am-ag-talk-troll-in-office with dissolve
    play voice6 girl27_yes_aga3 noloop
    ag "You certainly have the traits of one. Socially inept. Shut-in. Serial complainer."
    scene sm1cs-ns008-46 am-talk-grin with dissolve
    play voice5 girl22_surprised_oh noloop
    am "And you have the traits of a-"
    play voice4 girl29_angry_argh2 noloop
    play sound sfx_bed_slide2
    scene sm1cs-ns008-49 cw-talk-angry-shut-up with vpunch
    cw "Everyone put a lid on it."
    scene sm1cs-ns008-50 cw-am-ag-reaction-shut-up with dissolve
    pause
    scene sm1cs-ns008-51 cw-talk-calm-down with dissolve
    play voice4 girl29_disappointed_mff noloop
    cw "*sighs* Thank you."
    cw "It doesn't matter what this person's agenda is. Angela wants new protective measures put in place."
    scene sm1cs-ns008-52 cw-am-talk-april-chime-in with dissolve
    play voice5 girl22_thinking_eeh noloop
    am "I could create a program that doxxes the asshat once he posts on the new website."
    play voice4 girl29_no_simple noloop
    cw "No. No more doxxing."
    play sound sfx_cloth_rustling1
    scene sm1cs-ns008-53 mc-ns-raise-hand with dissolve
    pause
    scene sm1cs-ns008-54 cw-talk-point-to-nari with dissolve
    play voice4 girl29_yes_questioning noloop
    cw "Ms. Song, what do you have for me?"
    scene sm1cs-ns008-55 ns-mc-talk-shy-change-mind with dissolve
    play voice3 nari_thinking_emm noloop
    ns "Ummm. It's probably a bad idea."
    scene sm1cs-ns008-56 cw-talk-ask-eugene with dissolve
    play voice4 girl29_yes_aga1 noloop
    cw "Alright. What about other solutions? Eugene?"
    cw "Eugene? Anything?"
    play voice5 boy5_pain_sobs1 noloop
    scene sm1cs-ns008-57 cw-talk-reply-still-sad with dissolve
    en "No. I am sorry, Claire. I am still thinking of my poor papa."
    scene sm1cs-ns008-58 cw-talk-rolls-eye with dissolve
    play voice4 girl29_yes_yeah noloop
    cw "Take your time..."
    scene sm1cs-ns008-59 mc-ns-talk-encourage-nari with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "*whispers* Come on. Tell Claire your idea."
    scene sm1cs-ns008-60 mc-ns-talk-response-scared with dissolve
    play voice3 nari_no_sad noloop
    ns "*whispers* I can't. What if she gets mad? What if she hates it?"
    play sound sfx_cloth_rustling2
    scene sm1cs-ns008-61 mc-ns-talk-hold-hand-encourage with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "*whispers* It's one of your ideas. I'm sure it's amazing."
    mc "*whispers* You got this, Nari. I know you do."
    scene sm1cs-ns008-62 mc-ns-smile-confident with dissolve
    play voice3 stacy_smell noloop
    pause
    play sound sfx_skirt_off1
    scene sm1cs-ns008-63 mc-ns-stand-talk with dissolve
    play voice3 nari_hey_high noloop
    ns "Claire. I mean... Ms. Watts.{w} I have a plan."
    scene sm1cs-ns008-64 cw-talk-acknowledge-nari with dissolve
    play voice4 girl29_yes_aga2 noloop
    cw "Well, let's hear it."
    scene sm1cs-ns008-65 ns-mc-talk-address-room with dissolve
    play voice3 nari_disappointed_mff noloop
    ns "I can create a program that will act as a monitor for the new website."
    ns "I'm sure Ms. Porillo can provide us with some of the troublemaker's previous posts."
    scene sm1cs-ns008-68 ns-mc-cw-am-talk-wide-shot with dissolve
    ns "I'll take those old posts and teach the program what to look for so we can make sure this user is not a problem for our new website."
    scene sm1cs-ns008-67 ns-mc-talk-unsure with dissolve
    play voice3 nari_disappointed_huh noloop
    ns "I can even add some tracking software so once a problem user is detected, we can locate their IP address."
    ns "If the company wants to take legal action."
    scene sm1cs-ns008-66 am-cw-talk-like-idea with dissolve
    play voice5 girl22_happy_yeah noloop
    am "Search and destroy. I like that."
    scene sm1cs-ns008-69 cw-talk-end-of-meeting with dissolve
    play voice4 girl29_thinking_mmm2 noloop
    cw "I'm finding myself a fan as well. How long would it take you, Ms. Song?"
    scene sm1cs-ns008-65 ns-mc-talk-address-room with dissolve
    play voice3 nari_disappointed_eeh noloop
    ns "Probably about a week. I...{w} I would have to stay here late most days, if that is alright with you, Ms. Watts."
    scene sm1cs-ns008-54 cw-talk-point-to-nari with dissolve
    play voice4 girl29_yes_yep noloop
    cw "Sure, that would help make sure you can still spend time on the video servers."
    play voice3 nari_yes_confident noloop
    ns "Yes. That's exactly what I was thinking."
    play voice4 girl29_happy_phew noloop
    cw "Alright, plan approved. Thank you, Nari, if you can put that program in action, the client will be very happy with us."
    scene sm1cs-ns008-67 ns-mc-talk-unsure with dissolve
    play voice3 nari_happy_relief noloop
    ns "Uh... happy to help."
    scene sm1cs-ns008-64 cw-talk-acknowledge-nari with dissolve
    play voice4 girl29_yes_aga3 noloop
    cw "Alright everyone, let's get back to it."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    play sound3 sfx_door_open2 noloop
    play sound4 sfx_office_ambience1 fadein 2.0
    $ renpy.music.set_volume(0.3, 0.0, "sound4" )
    scene sm1cs-ns008-70 ns-mc-talk-leaving-meeting with dissolve
    pause
    play sound sfx_cloth_rustling3
    stop sound2 fadeout 1.0
    scene sm1cs-ns008-71 ns-mc-talk-grab hand with dissolve
    play voice2 mc_happy_yay3 noloop
    mc "Way to go, Nari. I knew it would work out."
    scene sm1cs-ns008-72 ns-mc-talk-blush with dissolve
    play voice3 nari_happy_phew noloop
    ns "Thank you, [mcname]. But my heart is still pounding a mile a minute."
    ns "Look you can feel it."
    play voice2 mc_thinking_hmm9 noloop
    mc "Maybe I can feel it later."
    play voice3 nari_happy_laugh1 noloop
    ns "Oh... *giggles* I like that idea."
    $ renpy.music.set_volume(1.0, 3.0, "sound4" )
    play sound sfx_door_closed2
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene sm1cs-ns008-73 ns-mc-talk-walk-together with dissolve
    play voice3 nari_disappointed_oh noloop
    ns "But it's going to have to wait. I mean, I'd love to hang out with you tonight, but I should get started on the program."
    play voice2 mc_yes_yes1 noloop
    mc "Totally."
    scene sm1cs-ns008-74 ns-mc-talk-cute-walk with dissolve
    play voice3 nari_thinking_hmm3 noloop
    ns "And you're okay, waiting a little bit until our next date?"
    play voice2 mc_yes_aga2 noloop volume 1.4
    mc "Of course, I know how important this job is to you."
    scene sm1cs-ns008-75 ns-mc-talk-yawn-excuse-me with dissolve
    play voice3 nari_disappointed_mff noloop
    ns "Yes. Very... *yawns* very important."
    play voice2 mc_thinking_hmm1 noloop
    mc "Hmmm."
    ns "Excuse me, [mcname]."
    stop sound3 fadeout 1.0
    stop sound2 fadeout 1.0
    play sound sfx_keyboard_typing2
    scene sm1cs-ns008-76 ns-mc-sit-back-at-desks with dissolve
    pause
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    stop sound4 fadeout 2.0
    stop music fadeout 3.0
    stop sound fadeout 1.0
    $ StoryController.end_scene(NS_STORY, 2, 0, 1)
    return