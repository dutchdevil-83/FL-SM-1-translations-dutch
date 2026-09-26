label sm1cs_mas001:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 0.5, "sound4" )
    play sound4 sfx_closetraffic_city
    play sound sfx_heels_steps2 loop
    scene sm1cs-mas001-01 mc-mas-entry_c1 with dissolve
    play music music_urban_funk1
    play voice2 d1s5_mcthinks noloop volume 1.5
    mct "Another day, another dollar."
    scene sm1cs-mas001-02 mc-mas-entry2_c1 with dissolve
    mct "Should probably get to it... these wursts won't deliver themselves!"
    scene sm1cs-mas001-02 mc-mas-entry2_c2 with dissolve
    pause
    play voice2 mc_pain_ou1 noloop
    play voice3 girl28_scared_ah4 noloop
    play sound sfx_leg_kick6
    play sound2 sfx_books_fallen1 noloop
    scene sm1cs-mas001-03 mc-mas-col_c1 with hpunch
    mc "Oh shit!"
    scene sm1cs-mas001-03 mc-mas-col_c2 with hpunch
    play voice3 girl28_angry_argh3 noloop
    ms "Ouch! Watch where you're going, jacka-"
    scene sm1cs-mas001-04 mc-mas-pick1_c2 with dissolve
    play voice3 girl28_surprised_oh noloop
    ms "Oh, uhm, hi, [mcname]."
    scene sm1cs-mas001-04 mc-mas-pick1_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Shit, I am so sorry, Maya."
    scene sm1cs-mas001-05 mc-mas-pick2_c2 with dissolve
    play voice3 girl26_no_nonono noloop
    ms "No, no, it's fine. I should have, uhm, been watching where I was going."
    scene sm1cs-mas001-05 mc-mas-pick2_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Let me help you with that."
    scene sm1cs-mas001-06 mc-mas-pick3_c2 with dissolve
    play voice3 girl28_no_scared noloop
    ms "No, it's fine. I got it!"
    scene sm1cs-mas001-06 mc-mas-pick3_c1 with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "It's the least I could do after running into you."
    scene sm1cs-mas001-07 mc-mas-pick4_c2 with dissolve
    play voice3 girl28_disappointed_eeh1 noloop
    ms "I don't want to be a pain, [mcname]. I got it."
    scene sm1cs-mas001-07 mc-mas-pick4_c1 with dissolve
    play voice2 d2s9_mchey noloop volume 1.2
    mc "Seriously, it's not a problem."
    play sound sfx_paper_rustl1 volume 1.7
    scene sm1cs-mas001-08 mc-mas-pick8_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "What have you got here, anyway?"
    scene sm1cs-mas001-08 mc-mas-pick8_c2 with dissolve
    play voice3 girl28_disappointed_oh noloop
    ms "Oh, it's nothing-"
    scene sm1cs-mas001-09 mc-mas-pick9_c1 with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Are these job applications?"
    scene sm1cs-mas001-09 mc-mas-pick9_c2 with dissolve
    play voice3 girl28_surprised_eeh noloop
    ms "I... Maybe."
    scene sm1cs-mas001-10 mc-mas-talk1_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Well, they definitely look like job applications."
    scene sm1cs-mas001-10 mc-mas-talk1_c2 with dissolve
    play voice3 girl28_disappointed_geh noloop
    ms "Look, Nelson is great, and I like this job but... I have bills and shit, you know?"
    play voice2 mc_yes_yeah4 noloop
    mc "I get it, Maya."
    ms "Please don't tell him."
    scene sm1cs-mas001-11 mc-mas-talk2_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Don't worry, my lips are sealed. I won't mention this at all."
    mc "Heck, I'll even forget it happened! I'll pretend like I've never met you, I know nothing about jobs, and that I'm brand new here."
    play voice2 mc_hey_hey5 noloop
    mc "Hi, my name's [mcname], it's a pleasure to meet you!"
    scene sm1cs-mas001-11 mc-mas-talk2_c2 with dissolve
    play voice3 girl28_happy_laugh1 noloop
    ms "Thank you, [mcname]. I needed that."
    scene sm1cs-mas001-12 mc-mas-talk3_c1 with dissolve
    menu:
        "Anything for a pretty gal"(hint="sm1cs_mas001_m01_h01"):
            call sm1cs_mas001_m01_c01 from _call_sm1cs_mas001_m01_c01
            scene sm1cs-mas001-12 mc-mas-talk3_c2 with dissolve
            play voice3 girl28_happy_mmm1 noloop
            ms "Thank you."
        "Just happy to help"(hint="sm1cs_mas001_m01_h02"):
            scene sm1cs-mas001-12 mc-mas-talk3_c2 with dissolve
            play voice3 girl28_happy_mmm1 noloop
            ms "Thank you, [mcname]."
    ms "You know, as far as coworkers go, you're not too bad."
    scene sm1cs-mas001-13 mc-mas-talk4_c1 with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "God, I'd hate to imagine a bad one."
    play sound sfx_paper_rustl2
    scene sm1cs-mas001-13 mc-mas-talk4_c2 with dissolve
    play voice3 girl28_yes_yeah2 noloop
    ms "Lizard people."
    scene sm1cs-mas001-14 mc-mas-talk5_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What?"
    scene sm1cs-mas001-14 mc-mas-talk5_c2 with dissolve
    play voice3 girl28_arrogant_hah3 noloop
    ms "The last guy who worked here. It's literally all he would talk about. And how the Earth was flat."
    ms "Every delivery was late, and it was always the lizard people's fault."
    scene sm1cs-mas001-15 mc-mas-talk6_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "That sounds terrible!"
    scene sm1cs-mas001-15 mc-mas-talk6_c2 with dissolve
    play voice3 girl28_arrogant_pff1 noloop
    ms "You have no idea."
    scene sm1cs-mas001-16 mc-mas-talk7_c2 with dissolve
    play voice3 girl28_hey_bye3 noloop
    ms "I'll see you around, [mcname]."
    scene sm1cs-mas001-16 mc-mas-talk7_c1 with dissolve
    play voice2 mc_hey_bye2 noloop
    mc "Yeah, see ya, Maya."
    play sound sfx_heels_steps2 loop
    scene sm1cs-mas001-17 mc-mas-go_c1 with dissolve
    pause
    stop sound fadeout 1.0
    stop music fadeout 3.0
    stop sound4 fadeout 2.0
    jump sm1cs_mas001_end
label sm1cs_mas001_end:
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(MAS_STORY, 1, 0, 1, WURST_DELIVERY, DEFAULT_SUBLOCATION, WD_ENTRANCE)
    return
label sm1cs_mas001_m01_c01:
    $ player.set_choice("sm1cs_mas001_do_anything")
    $ CharacterController.get_character("ms").add_point()
    return