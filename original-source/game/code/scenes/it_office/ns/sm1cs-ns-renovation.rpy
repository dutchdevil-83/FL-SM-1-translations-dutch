label sm1cs_ns_renovation:
    $ renpy.music.set_volume(0.8, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 0.0, "music2" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    play sound sfx_chair_slide1 volume 1.6
    play sound2 sfx_mouse_clicks1 noloop
    scene sm1cs-ns renovation-01 mc-ns-talking with dissolve
    $ renpy.music.play(audio.music_cute_code_renovation_nodrums, "music" , True, None, True, 0.0)
    $ renpy.music.play(audio.music_cute_code_renovation_onlydrums, "music2", True, None, True, 0.0)
    play voice2 mc_hey_hey5 noloop
    mc "Hey Nari. I've got great news."
    scene sm1cs-ns renovation-02 ns-excited with dissolve
    play voice3 nari_thinking_oh noloop
    ns "Oh?"
    scene sm1cs-ns renovation-03 mc-ns-talking with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Stacy and I have started fixing up our home."
    mc "Probably in a little bit of time, you can come to move into our new place."
    play voice3 nari_happy_yay noloop
    ns "That is great news, [mcname]."
    scene sm1cs-ns renovation-04 ns-hmm with dissolve
    play voice3 nari_hey_asking noloop
    ns "You must let me do something to help out."
    ns "Why don't I come over after work and give a hand."
    scene sm1cs-ns renovation-05 mc-talking with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "I think you mean 'lend a hand.'"
    scene sm1cs-ns renovation-06 ns-happy with dissolve
    play voice3 nari_yes_emotional noloop
    ns "Of course. I'll lend you anything of mine to help."
    ns "So, should I come with you after work?"
    scene sm1cs-ns renovation-08 mc-smiling with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure. Sounds good to me."
    scene sm1cs-ns renovation-09 ns-smiling with dissolve
    play voice3 nari_happy_yeah noloop
    ns "Thank you so much, [mcname]."
    scene sm1cs-ns renovation-12 mc-talking with dissolve
    play voice2 mc_no_nono1 noloop
    mc "You don't need to thank me."
    mc "It will kind of be 'your' place soon, too, after all."
    scene sm1cs-ns renovation-10 ns-excited with dissolve
    play voice3 nari_happy_laugh1 noloop
    ns "I can't wait."
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 1.5, "music" )
    scene black
    show screen scene_transistion(_("After work"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen scene_transistion
    play sound sfx_door_openclosed1
    $ renpy.music.set_volume(0.7, 2.5, "music" )
    scene sm1cs-ns renovation-13 ns-impressed
    with Fade(0.5, 0.5, 0.5)
    play voice3 nari_surprised_wow noloop
    ns "Woah. This place is huge."
    scene sm1cs-ns renovation-14 ns-talking with dissolve
    play voice3 nari_surprised_huh2 noloop
    ns "You really want me to live here? You don't have plans for all this space?"
    scene sm1cs-ns renovation-15 mc-talking with dissolve
    play voice2 mc_happy_a1 noloop
    mc "It's going to be fine, Nari. Stacy and I will be fine with you joining us."
    scene sm1cs-ns renovation-16 mc-thinking with dissolve
    play voice2 mc_thinking_hm noloop
    mct "Maybe when the studio really takes off, people can stay here to relax when they're working with us."
    scene sm1cs-ns renovation-17 ns-talking with dissolve
    play voice3 nari_surprised_ohmy noloop
    ns "It's just incredible. I've never heard of someone living in a space like this."
    scene sm1cs-ns renovation-18 mc-grinning with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "We have a friend who is a real estate genius."
    play sound sfx_cloth_rustling2
    scene sm1cs-ns renovation-19 ns-embarassed with dissolve
    play voice3 nari_disappointed_mff noloop
    ns "I suddenly feel like I'm going to be nothing more than a burden to you."
    scene sm1cs-ns renovation-20 mc-reassuring with dissolve
    play voice2 mc_no_no2 noloop
    mc "There is nothing to worry about, Nari."
    mc "And you're not a burden. I care about you and I want you to have a nice place to sleep that is not a couch at work."
    scene sm1cs-ns renovation-21 ns-happy with dissolve
    play voice3 nari_happy_phew noloop
    ns "You... you are so kind to me, [mcname]."
    scene sm1cs-ns renovation-22 ns-happy-close-up with dissolve
    play voice3 nari_disappointed_eeh noloop
    ns "You mean a great deal to me as well."
    play sound sfx_hands_clap3
    scene sm1cs-ns renovation-23 ns-lets-start with dissolve
    play voice3 nari_disappointed_huh noloop
    ns "Now. Where should we begin?"
    $ renpy.music.set_volume(1.4, 2.0, "music" )
    $ renpy.music.set_volume(1.4, 2.0, "music2" )
    scene sm1cs-ns renovation-24 mc-ns-montage-working with dissolve
    pause
    scene sm1cs-ns renovation-25 mc-ns-montage-working with dissolve
    pause
    scene sm1cs-ns renovation-26 mc-ns-montage-working with dissolve
    pause
    scene sm1cs-ns renovation-27 mc-ns-montage-working with dissolve
    pause
    scene sm1cs-ns renovation-28 mc-ns-montage-working with dissolve
    pause
    scene sm1cs-ns renovation-29 mc-ns-montage-working with dissolve
    pause
    $ renpy.music.set_volume(0.65, 3.0, "music" )
    $ renpy.music.set_volume(0.65, 3.0, "music2" )
    scene sm1cs-ns renovation-30 mc-in-bathroom with fade
    play voice3 nari_happy_mmm noloop
    ns "Mmm."
    play sound sfx_door_creak2
    scene sm1cs-ns renovation-31 mc-entry with dissolve
    pause
    scene sm1cs-ns renovation-32 ns-asking with dissolve
    play voice3 nari_disappointed_oh noloop
    ns "Oooh. This is the main bathroom?"
    scene sm1cs-ns renovation-33 mc-answering with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Yes, it is."
    scene sm1cs-ns renovation-34 ns-being-naughty with dissolve
    play voice3 nari_arrogant_huh noloop
    ns "Do you think that when I move in, we can celebrate with some..."
    ns "{i}Special{/i} fun in here?"
    scene sm1cs-ns renovation-35 mc-smiling-back with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "I'm sure we can find some time to have some fun, Nari."
    scene sm1cs-ns renovation-36 ns-good with dissolve
    play voice3 nari_thinking_hmm1 noloop
    ns "Good."
    play sound sfx_cloth_rustling3
    scene sm1cs-ns renovation-37 ns-getting-close with dissolve
    pause
    scene sm1cs-ns renovation-38 ns-getting-close-and-talking with dissolve
    play voice3 nari_sex_closedmoan1 noloop
    ns "You know how much I like to get sticky with you."
    scene sm1cs-ns renovation-39 mc-talking with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Oh yeah."
    scene sm1cs-ns renovation-40 mc-being-boring with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "But for now, we have to focus."
    scene sm1cs-ns renovation-41 ns-annoyed-in-korean with dissolve
    play voice3 nari_angry_cough noloop
    ns "Yeol-bat-ne."
    scene sm1cs-ns renovation-42 mc-lol with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Hah. What does that mean?"
    scene sm1cs-ns renovation-43 ns-explaining with dissolve
    play voice3 nari_arrogant_hm noloop
    ns "It means \"I'm so irritated\"."
    play sound sfx_cloth_rustling5
    scene sm1cs-ns renovation-44 ns-sexy with dissolve
    play voice3 nari_sex_closedmoan5 noloop
    ns "But in this case, I should probably have said..."
    ns "I'm so horny."
    scene sm1cs-ns renovation-45 ns-smiling with dissolve
    play voice3 nari_disappointed_woof noloop
    ns "But I don't want to tease you."
    scene sm1cs-ns renovation-46 ns-giggling with dissolve
    play voice3 nari_happy_laugh3 noloop
    ns "*giggles*"
    play sound sfx_heels_steps1
    scene sm1cs-ns renovation-47 mc-thinking with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "I might be in trouble when I have both Nari and Stacy living with me."
    stop sound fadeout 2.0
    scene sm1cs-ns renovation-48 mc-talking with fade
    play voice2 mc_yes_okay2 noloop
    mc "Looks like we put a good dent in everything."
    scene sm1cs-ns renovation-49 ns-asking with dissolve
    play voice3 nari_surprised_huh1 noloop
    ns "Where will I be sleeping when I move in?"
    scene sm1cs-ns renovation-50 mc-pointing-up with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "You'll be living upstairs, Nari."
    scene sm1cs-ns renovation-51 ns-excited with dissolve
    play voice3 nari_pain_aaa3 noloop
    ns "I'm so excited."
    scene sm1cs-ns renovation-52 ns-subdue with dissolve
    play voice3 nari_surprised_ehh noloop
    ns "I hope it is okay that my room will be pretty naked."
    ns "I didn't bring much when I moved here."
    scene sm1cs-ns renovation-53 mc-talking with dissolve
    play voice2 mc_no_noway noloop
    mc "We can't have that."
    mc "When the renovation is over, we should get you some basic stuff that is all yours."
    scene sm1cs-ns renovation-54 ns-talking with dissolve
    play voice3 nari_yes_aga2 noloop
    ns "I think I'd like that, [mcname]."
    ns "Tonight I'll skip checking my crypto and look up some styles."
    scene sm1cs-ns renovation-55 ns-closing-in with dissolve
    play voice3 nari_thinking_emm noloop
    ns "Thank you again for all of your help."
    ns "I'm very glad I could contribute in my own small way."
    scene sm1cs-ns renovation-56 mc-offering-his-hand with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "You can give me a hand anytime, Nari."
    play sound sfx_cloth_rustling4 volume 1.5
    scene sm1cs-ns renovation-57 ns-mc-joining-hands with dissolve
    pause
    scene sm1cs-ns renovation-58 ns-calling-him with dissolve
    play voice3 nari_happy_relief noloop
    ns "[mcname]..."
    play sound2 sfx_hair_scratch1 noloop
    scene sm1cs-ns renovation-59 mc-ns-kissing with dissolve
    play voice2 mc_thinking_mmm1 noloop
    play voice3 nari_sex_closedmoan4 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-ns renovation-60 ns-talking with dissolve
    play voice3 nari_happy_laugh6 noloop
    ns "I can't wait to move in, [mcname]."
    scene sm1cs-ns renovation-61 mc-talking with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Likewise."
    play sound sfx_heels_steps2 loop volume 1.5 loop
    scene sm1cs-ns renovation-62 ns-heading-out with dissolve
    play voice3 nari_yes_aga1 noloop
    ns "I'm off to find out some sheets I like."
    scene sm1cs-ns renovation-63 ns-waving with dissolve
    play voice3 nari_hey_high noloop
    ns "I'll see you at work."
    scene sm1cs-ns renovation-64 mc-cya with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Looking forward to it."
    scene sm1cs-ns renovation-65 ns-leaving with dissolve
    pause
    play sound sfx_door_closed3
    stop music2 fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    stop music fadeout 3.0
    jump sm1cs_ns_renovation_end
label sm1cs_ns_renovation_end:
    $ renovation_controller.set_progress(renovation_controller.get_renovation_scenes_progress())
    $ renovation_controller.set_daily_limit()
    $ StoryController.end_scene_without_storyline("sm1cs_ns_renovation", 2, 0, 4, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return