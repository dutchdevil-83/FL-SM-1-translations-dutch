image sm1cs_km003-a133-glm = Movie(play = "images/FS_T/KM/s002/anim/sm1cs-km002-a133-4x-60fps.webm", start_image = "sm1cs-km002-a133 vs-glambot-000", image = "sm1cs-km002-a133 vs-glambot-119", loop = False)
image sm1cs_km003-a126-1 = Movie(play = "images/FS_T/KM/s002/anim/sm1-km002-a126-1-2x-50fps.webm", start_image = "sm1-km002-a126-1 mc-km-vs-masturbate-anim-01")
image sm1cs_km003-a126-1-f = Movie(play = "images/FS_T/KM/s002/anim/sm1-km002-a126-1-2x-60fps.webm", start_image = "sm1-km002-a126-1 mc-km-vs-masturbate-anim-01")
image sm1cs_km003-a126-2 = Movie(play = "images/FS_T/KM/s002/anim/sm1-km002-a126-2-2x-50fps.webm", start_image = "sm1-km002-a126-2 mc-km-vs-masturbate-anim-01")
image sm1cs_km003-a126-2-f = Movie(play = "images/FS_T/KM/s002/anim/sm1-km002-a126-2-2x-60fps.webm", start_image = "sm1-km002-a126-2 mc-km-vs-masturbate-anim-01")
image sm1cs_km003-a126-3 = Movie(play = "images/FS_T/KM/s002/anim/sm1-km002-a126-3-2x-50fps.webm", start_image = "sm1-km002-a126-3 mc-km-vs-masturbate-anim-01")
image sm1cs_km003-a126-3-f = Movie(play = "images/FS_T/KM/s002/anim/sm1-km002-a126-3-2x-60fps.webm", start_image = "sm1-km002-a126-3 mc-km-vs-masturbate-anim-01")
image sm1cs_km003-a126-4 = Movie(play = "images/FS_T/KM/s002/anim/sm1-km002-a126-4-2x-50fps.webm", start_image = "sm1-km002-a126-4 mc-km-vs-masturbate-anim-01")
image sm1cs_km003-a126-4-f = Movie(play = "images/FS_T/KM/s002/anim/sm1-km002-a126-4-2x-60fps.webm", start_image = "sm1-km002-a126-4 mc-km-vs-masturbate-anim-01")
label sm1cs_km003:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound sfx_heels_steps2 loop
    scene sm1cs-km002-101-theater-km with Fade(0.5, 0.5, 0.5)
    play music music_swagger_strategy
    pause
    scene sm1cs-km002-102-mc-talks-km with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, Kellie. I finished reading up on my chapters."
    mc "Did you know that some people consider Theater an art form?"
    stop sound fadeout 1.0
    scene sm1cs-km002-103-mc-talks-km with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "The more you know, am I right?"
    play sound sfx_cloth_rustling3
    scene sm1cs-km002-104-km-grabs-mc with dissolve
    play voice3 girl31_thinking_hmm1 noloop
    km "That's great, very good. A+, [mcname]. Our next lesson begins right now."
    scene sm1cs-km002-105-mc-talks-km with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "What are we doing?"
    scene sm1cs-km002-106-km-talks-mc with dissolve
    play voice3 girl31_thinking_emm3 noloop
    km "I need your help. Don't ask questions."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-km002-108-km-talks-mc with dissolve
    pause
    scene sm1cs-km002-109-theater-backroom with fade
    pause
    scene sm1cs-km002-110-mc-talks-tl with dissolve
    play voice2 mc_hey_hey1 noloop
    mc "Hey Taisia. Little help?"
    scene sm1cs-km002-111-tl-talks-mc with dissolve
    play voice4 girl24_no_nah noloop
    tl "I'm sure you'll survive. Or not."
    scene sm1cs-km002-112-mc-talks-tl with dissolve
    play voice2 mc_angry_errr6 noloop
    mc "Come on."
    scene sm1cs-km002-113-km-talks-mc with dissolve
    play voice3 girl31_disappointed_ehh1 noloop
    km "Come on, this is part of your training, so stop being a wuss."
    stop sound fadeout 1.5
    stop sound2 fadeout 1.5
    if not player.get_choice("sm1cs_km002_km_cool"):
        scene sm1cs-km002-115-mc-talks-km with dissolve
        play voice2 mc_surprised_uh3 noloop
        mc "A wuss? Really. Real good teaching technique, coming from a girl who was ready to give me a concussion."
        scene sm1cs-km002-116-km-talks-mc with dissolve
        play voice3 girl31_disappointed_mff1 noloop
        km "[mcname], I said I was sorry. We don't have time for this."
        scene sm1cs-km002-117-mc-talks-km with dissolve
        play voice2 mc_angry_off noloop
        mc "Oh yeah, you're two out of five-star apology. Very sincere."
        mc "This doesn't feel like training, so why should I do anything you want?"
        scene sm1cs-km002-118-km-talks-mc with dissolve
        play voice3 girl31_arrogant_hm1 noloop
        km "Because I'm asking for your help."
        scene sm1cs-km002-119-mc-talks-km with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "I'm going to regret this."
    $ renpy.music.set_volume(0.2, 1.0, "sound4" )
    scene sm1cs-km002-120-theater-shower with fade
    play sound4 sfx_shower_ambience1 fadein 3.0
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    pause
    stop sound fadeout 1.0
    scene sm1cs-km002-121-km-talks-mc with dissolve
    play voice3 stacy_shhh noloop
    km "Shhhh."
    scene sm1cs-km002-122-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop
    mct "Oh man. What is she getting me into?"
    $ renpy.music.set_volume(0.5, 3.0, "sound4" )
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-km002-123-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "Someone is taking a shower."
    scene sm1cs-km002-124-mc-inner-talk with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "I need to get out of here."
    $ renpy.music.set_volume(1.0, 3.0, "sound4" )
    scene sm1cs-km002-125-mc-inner-talk with dissolve
    pause
    play voice2 mc_pain_ou1 noloop
    play voisex4 girl26_sex_openmoans3
    play sound sfx_vagina_penetration1_fast loop
    stop sound2 fadeout 1.0
    scene sm1cs-km002-126-mc-km-pop-out with hpunch
    mct "Oh shit."
    play voisex4 girl26_sex_closedmoans2
    scene sm1cs_km003-a126-1 with dissolve
    pause
    play voice2 mc_surprised_huh8 noloop
    mc "What are we doing here?"
    scene sm1cs_km003-a126-2 with dissolve
    pause
    scene sm1cs_km003-a126-3 with dissolve
    pause
    scene sm1cs_km003-a126-4 with dissolve
    pause
    scene sm1cs_km003-a126-1-f with dissolve
    pause
    scene sm1cs_km003-a126-2-f with dissolve
    pause
    scene sm1cs_km003-a126-3-f with dissolve
    pause
    scene sm1cs_km003-a126-4-f with dissolve
    pause
    play sound sfx_squirt1
    play sound2 sfx_piss_loop1 noloop
    play voisex4 girl26_sex_orgasming1 noloop
    scene sm1cs-km002-130-vs-squirt with hpunch
    vs "Ahuuaaa-fuffyaah... Yes..."
    scene sm1cs-km002-131-mc-inner-talk with dissolve
    play voice2 mc_surprised_wow4 noloop
    mct "Woah."
    stop sound2 fadeout 1.0
    scene sm1cs-km002-132-vs-talks with dissolve
    play voisex4 girl26_sex_scream7 noloop
    pause
    play voisex4 girl33_surprised_oh noloop
    vs "Oh hey."
    play sound [sfx_camera_fly1, sfx_camera_fly1] volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs_km003-a133-glm with Dissolve(0.15)
    pause
    play voice4 girl33_surprised_huh1 noloop
    vs "Sorry, you two, am I making too much noise?"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-km002-134-vs-talks with dissolve
    play voice4 girl33_arrogant_huh1 noloop
    vs "Or is this a VidVok thing? That's so cool."
    scene sm1cs-km002-135-vs-ass with dissolve
    play voice4 girl33_disappointed_mmf1 noloop
    vs "My one rule is no face shots."
    scene sm1cs-km002-136-vs-talks with dissolve
    play voice4 girl33_happy_laugh1 noloop
    vs "Gotta keep anonymous, after all. *giggles*"
    scene sm1cs-km002-137-vs-talks with dissolve
    play voice4 girl33_hey_scared noloop
    vs "Wait, why doesn't anyone have their phone out."
    scene sm1cs-km002-138-km-talks-vs with dissolve
    play voice3 girl31_surprised_huh3 noloop
    km "That's it. We've seen you naked and you're just... giving us rules on how to take pictures of you?"
    scene sm1cs-km002-139-vs-talks-km with dissolve
    play voice4 girl33_yes_yeah noloop
    vs "Yeah.{w} Why?"
    scene sm1cs-km002-140-km-talks-vs with dissolve
    play voice3 girl31_arrogant_geh noloop
    km "Aren't you shocked and embarrassed?"
    scene sm1cs-km002-141-vs-talks-km with dissolve
    play voice4 girl33_no_fun noloop
    vs "No. Why?{w} We're in the theater."
    scene sm1cs-km002-142-mc-inner-talk with hpunch
    play voice3 girl31_angry_ergh5 noloop
    km "*aggravated growl*"
    play voice2 mc_arrogant_huh1 noloop
    mct "Looks like lessons are canceled for today."
    scene sm1cs-km002-143-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "What is up with Kellie?"
    mct "Why did she want to embarrass Veronica?"
    scene sm1cs-km002-144-mc-talks-vs with dissolve
    play voice2 mc_scared_oh2 noloop
    mc "Oh fuck. Sorry, Veronica. I didn't mean to peep. It was... I know this will sound like bullshit."
    play sound sfx_heels_steps2
    scene sm1cs-km002-145-mc-talks-vs with dissolve
    play voice2 d2s12_emmm noloop
    mc "But it was all her idea."
    play voice2 mc_pain_ou3 noloop
    play sound sfx_leg_kick6
    scene sm1cs-km002-146-mc-talks with hpunch
    mc "Nrugh. Ouch."
    scene sm1cs-km002-147-vs-giggles with dissolve
    play voice4 girl33_happy_laugh4 noloop
    vs "*giggles*"
    scene sm1cs-km002-148-vs-talks-mc with dissolve
    play voice4 girl33_happy_mmm noloop
    vs "Now that you saw mine, you have to show me yours next time."
    scene sm1cs-km002-149-vs-talks-mc with dissolve
    play voice4 girl33_thinking_hmm1 noloop
    vs "I better get dried off now."
    scene sm1cs-km002-150-vs-talks with dissolve
    play voice4 girl33_arrogant_hm noloop
    vs "Don't want to make a scene."
    play sound sfx_barefoot_steps1 loop
    scene sm1cs-km002-151-vs with dissolve
    pause
    scene sm1cs-km002-152-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "I'm starting to really like some of these theater girls."
    stop sound fadeout 1.0
    stop sound4 fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    jump sm1cs_km003_end
label sm1cs_km003_end:
    $ StoryController.end_scene(KM_STORY, 1, 30, 3)
    return