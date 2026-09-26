label sm1mv01s07:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1mv01s07-01 mc-sy-going-up_c1 with dissolve
    play music zigzag_reggae
    pause
    scene sm1mv01s07-02 mc-sy-talking_c1 with dissolve
    play voice3 stacy_happy_phew1 noloop
    sy "I figured out how we are going to fix the problem."
    play voice2 mc_yes_aga2 noloop
    mc "Great."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1mv01s07-03 mc-asking_c1 with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "And the problem is what exactly?"
    scene sm1mv01s07-03 mc-asking_c2 with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "*sighs* Come on, get your head in the game."
    play voice2 mc_hey_hey3 noloop
    mc "My head is in the game. But it's a crazy game, and there are also like twenty tabs open on my laptop too."
    play sound sfx_chair_slide1
    play sound2 sfx_gadgets_laptop_opened noloop
    scene sm1mv01s07-04 mc-focused_c1 with dissolve
    play voice3 stacy_thinking_emm4 noloop
    sy "The problem is how to film the next two scenes and finish the pirate movie."
    sy "We can't film them here.{w} We need real sand for the location."
    scene sm1mv01s07-05 sm-looking-at-the-studio_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "And I don't think the warehouse is rated to have a ton of sand dumped in it."
    play sound sfx_cloth_rustling4
    scene sm1mv01s07-06 mc-thinking_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "We've skirted the rules before."
    scene sm1mv01s07-06 mc-thinking_c2 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "Do you want sand mites?"
    scene sm1mv01s07-07 mc-asking_c1 with dissolve
    sy "Because that's how you get sand mites!"
    scene sm1mv01s07-07 mc-asking_c2 with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay, so what is the plan then?"
    play sound sfx_keyboard_enter1
    scene sm1mv01s07-08 mc-let-me-see_c1 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "This."
    play voice2 mc_arrogant_hm1 noloop
    mc "Let me see."
    scene sm1mv01s07-09 sy-looking-at-screen_c1 with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Hmmm. 472 Fryblau Street, one bedroom, two beds."
    mc "Looks cozy."
    scene sm1mv01s07-09 sy-looking-at-screen_c2 with dissolve
    play voice3 stacy_no_nah3 noloop
    sy "I'm not eyeing it for comfort. {w} It's the location that made me fall in love."
    play sound sfx_keyboard_enter1
    scene sm1mv01s07-10 sy-grinning_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "The place is walking distance from the Palace Beach."
    play sound sfx_keyboard_typing2 volume 1.5
    scene sm1mv01s07-10 sy-grinning_c2 with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "The good news is that the water is cold right now. Which means..."
    scene sm1mv01s07-10 sy-grinning_c3 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "If we're lucky, we could find a quiet stretch of beach to film at."
    scene sm1mv01s07-11 sy-mc-talking_c2 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What's the bad news?"
    scene sm1mv01s07-11 sy-mc-talking_c1 with dissolve
    play voice3 stacy_no_uhuh3 noloop
    sy "No bad news."
    sy "Only great news."
    play sound sfx_keyboard_enter1
    scene sm1mv01s07-12 sy-mc-talking_c1 with dissolve
    play voice3 stacy_happy_relief1 noloop
    sy "The Carcio Cave. The perfect spot for our buried treasure scene."
    scene sm1mv01s07-12 sy-mc-talking_c2 with dissolve
    play voice2 mc_surprised_ohmy noloop
    mc "I'm speechless."
    play voice3 stacy_arrogant_ha1 noloop
    sy "Am I good, or am I good?"
    mc "You're the absolute best!"
    play sound sfx_chair_slide1
    scene sm1mv01s07-13 sy-being-cute_c1 with dissolve
    play voice3 stacy_yes_ugu1 noloop
    sy "Mmhm. Mmhmm. Mmmm.{w} I try."
    scene sm1mv01s07-13 sy-being-cute_c2 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "And you deliver."
    play sound sfx_skirt_off2
    scene sm1mv01s07-14 mc-thinking_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "But if we're doing this, we'll have to leave the city for a bit."
    mc "Probably like two days or so."
    scene sm1mv01s07-14 mc-thinking_c2 with dissolve
    play voice3 stacy_yes_yeah1 noloop
    sy "Yeah."
    sy "A little mini vacation."
    scene sm1mv01s07-15 mc-sy-talking_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "That actually sounds kind of perfect."
    mc "The last scene was a doozy."
    scene sm1mv01s07-15 mc-sy-talking_c2 with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Yup. So what better way to put it in the past and have a little fun in the sun."
    sy "Then we'll film the last two scenes."
    play sound sfx_cloth_rustling1
    play sound2 sfx_phone_tapping1 volume 2.0
    scene sm1mv01s07-16 mc-texting_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Sounds great."
    mc "Guess we just need to text Kanya and Taisia and let them know the plan."
    stop sound2
    play sound sfx_throw_something1
    scene sm1mv01s07-16 mc-texting_c2 with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "Great.{w} Road trip!"
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(MOVIE_PIRATES, 1, 0, 2)
    return