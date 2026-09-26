label sm1mv02s01:
    $ renpy.music.set_volume(0.55, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    play music music_noir_journey
    scene sm1mv02s01b-01-mc-enter with dissolve
    play voice3 stacy_pain_mmm1 noloop
    pause
    scene sm1mv02s01b-02-mc-talk-sy with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Hey, Stacy. Ready to get into preproduction for the sci fi movie?"
    scene sm1mv02s01b-03-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_ehh1 noloop
    sy "Yes! But, we'll need coffee for this."
    scene sm1mv02s01b-02-mc-talk-sy with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I agree."
    play sound2 sfx_sport_run1 volume 2.0
    play sound sfx_throw_something1
    scene sm1mv02s01i-01-sy-mc-walk-kitchen with dissolve
    pause
    play sound2 sfx_coffee_machine noloop
    scene sm1mv02s01i-04-sy-talk-mc with dissolve
    play voice3 stacy_thinking_emm1 noloop
    sy "All right, have we got anyone officially cast yet?"
    stop sound2 fadeout 2.0
    play sound sfx_coffee_pouring volume 2.0
    scene sm1mv02s01i-05-mc-talk-sy with dissolve
    play voice2 mc_no_nope2 noloop
    mc "Erm... nope. Not yet."
    play voice3 stacy_thinking_hmm2 noloop
    sy "Well, that's a big thing to get taken care of."
    play sound2 sfx_heels_steps2
    stop sound fadeout 1.0
    scene sm1mv02s01i-06-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_huh3 noloop
    sy "I guess we'll probably need a script for them, huh."
    play sound sfx_cup_slide1 volume 2.0
    stop sound2 fadeout 1.0
    scene sm1mv02s01i-08-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, that would be good. They'll probably want to know what they're going to star in."
    play sound sfx_bed_slide2
    scene sm1mv02s01i-09-sy-talk-mc with dissolve
    play voice3 stacy_yes_yap3 noloop
    sy "Then let's get to work!"
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1mv02s01i-10-mc-sy-work with fade
    play sound sfx_keyboard_typing2
    pause
    scene sm1mv02s01i-11-mc-sy-work with fade
    play sound sfx_bed_slide3 volume 0.5
    pause
    scene sm1mv02s01i-12-mc-sy-work with fade
    play sound sfx_throw_something1
    pause
    scene sm1mv02s01i-13-mc-sy-work with fade
    play sound sfx_keyboard_typing2
    pause
    scene sm1mv02s01i-14-mc-sy-work with fade
    play sound sfx_skirt_off2
    pause
    $ renpy.music.set_volume(0.55, 2.5, "music" )
    scene sm1mv02s01i-16-sy-talk-mc with fade
    play sound sfx_keyboard_enter1
    play sound2 sfx_drink_slurp2 noloop
    play voice3 stacy_thinking_emm3 noloop
    sy "Aaaaaaaaand there we go! One complete pornographic science fiction movie script!"
    scene sm1mv02s01i-17-mc-talk-sy with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "God, that was a mouthful."
    scene sm1mv02s01i-18-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_ha1 noloop
    sy "About as much of a mouthful as your dick!"
    scene sm1mv02s01i-19-mc-look with dissolve
    pause
    scene sm1mv02s01i-20-sy-talk-mc with dissolve
    play voice3 stacy_mmm1 noloop
    sy "I thought that one was pretty good."
    play sound sfx_cup_place1 volume 1.6
    scene sm1mv02s01i-21-mc-talk-sy with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Of course you did."
    scene sm1mv02s01i-22-mc-talk with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mc "\"Star Voyage VI: Babe-lyon 9\"."
    scene sm1mv02s01i-23-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "Now that is a mouthful."
    scene sm1mv02s01i-24-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah, yeah. I like the name though."
    scene sm1mv02s01i-25-sy-talk-mc with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "...{size=*0.7}It is a pretty good name...{/size}"
    scene sm1mv02s01i-26-mc-talk-sy with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What was that?"
    scene sm1mv02s01i-27-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "What?"
    play sound sfx_hair_scratch1
    scene sm1mv02s01i-28-mc-smirks with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "Losersayswhat?"
    scene sm1mv02s01i-29-sy-talk-mc with dissolve
    play voice3 stacy_surprised_ah2 noloop
    sy "What?"
    scene sm1mv02s01i-30-mc-talk-sy with dissolve
    play voice2 mc_happy_hah2 noloop
    pause
    play sound sfx_bed_slide2
    scene sm1mv02s01i-31-sy-talk-mc with dissolve
    play voice3 stacy_angryhuh noloop
    sy "Oh my God, [mcname]. Seriously?"
    play sound2 sfx_heels_steps2
    scene sm1mv02s01i-32-mc-talk-sy with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "Gotcha'."
    scene sm1mv02s01i-33-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_ehh2 noloop
    if persistent.is_special:
        sy "Sometimes I forget that you're my {i}older{/i} brother."
    else:
        sy "Sometimes I forget that you're older than me."
    stop sound2 fadeout 1.0
    scene sm1mv02s01i-34-mc-talk-sy with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Okay, so we've got the script-"
    play sound sfx_bed_slide3
    scene sm1mv02s01i-35-sy-talk-mc with dissolve
    play voice3 stacy_hey_attention1 noloop
    sy "-and we have our potential actresses picked out-"
    scene sm1mv02s01i-36-mc-talk-sy with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "So now we just need a place to film."
    mc "I hadn't even thought about that yet... where the hell are we going to get a spaceship?"
    play sound sfx_heels_steps2 loop
    scene sm1mv02s01i-37-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Oh, if only someone had been thinking how to solve that problem..."
    scene sm1mv02s01i-38-mc-talk-sy with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "You have an idea?"
    scene sm1mv02s01i-39-sy-talk-mc with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "Come on, follow me!"
    play voice2 mc_surprised_uh2 noloop
    mc "To where?"
    sy "You'll see."
    scene sm1mv02s01i-40-mc-talk-sy with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Is this when you decide to ritual sacrifice me to some pagan god?"
    scene sm1mv02s01i-41-sy-talk-mc with dissolve
    play voice3 stacy_angry noloop
    sy "You are ridiculous, [mcname]."
    play sound2 sfx_heels_steps1
    scene sm1mv02s01i-42-mc-sy-dojo with Fade(0.5, 0.5, 0.5)
    pause
    scene sm1mv02s01i-43-kv-talk-sy-mc with dissolve
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    play voice4 kanya_hey_attention noloop
    kv "Hey, Stacy! [mcname]!"
    scene sm1mv02s01i-44-mc-talk-sy with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "What are we doing at the Photo Dojo, Stacy?"
    scene sm1mv02s01i-45-sy-talk-mc with dissolve
    play voice3 stacy_thinking_well1 noloop
    sy "You'll see."
    play sound sfx_heels_steps2 loop
    scene sm1mv02s01i-46-kv-talk with dissolve
    play voice4 kanya_thinking_eeh5 noloop
    kv "Okay, I'm going to let you know right now, that I haven't been over here in forever."
    kv "So I apologize for the dust."
    scene sm1mv02s01i-47-sy-talk-kv with dissolve
    play voice3 stacy_no_nah2 noloop
    sy "It's all good!"
    scene sm1mv02s01i-48-mc-talk with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Been over to where?"
    play sound2 sfx_heels_steps1
    scene sm1mv02s01i-49-sy-talk-mc with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "You'll see."
    scene sm1mv02s01i-50-kv-talk with dissolve
    play voice4 kanya_yes_yeah3 noloop
    kv "All right, open sesame!"
    play sound sfx_door_openclosed1
    stop sound2 fadeout 1.0
    scene sm1mv02s01i-51-warehouse with dissolve
    pause
    scene sm1mv02s01i-52-warehouse with dissolve
    pause
    scene sm1mv02s01i-53-mc-talk with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay?...{w} What am I looking at?"
    scene sm1mv02s01i-54-kv-talk-mc with dissolve
    play voice4 kanya_surprised_oh noloop
    kv "Oh shit, the lights. Hang on."
    play sound sfx_light_turn2
    play sound2 sfx_light_podium_2 noloop
    scene sm1mv02s01i-55-lights with hpunch
    pause
    scene sm1mv02s01i-56-mc-talk with dissolve
    play voice2 mc_scared_huuuh1 noloop
    mc "Oh holy shit!"
    scene sm1mv02s01i-57-sy-talk-mc with dissolve
    play voice3 stacy_happy_yay2 noloop
    sy "I present to you, a stage!"
    scene sm1mv02s01i-58-mc-talk-kv with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "There's not a stage in here?"
    scene sm1mv02s01i-59-sy-talk-mc with dissolve
    play voice3 stacy_no_simple1 noloop
    sy "No, but that's what they call the places the film movies. Shorthand for \"sound stage\"."
    scene sm1mv02s01i-60-kv-talk-mc with dissolve
    play voice4 kanya_arrogant_ha noloop
    kv "But to be clear, this is {i}not{/i} a sound stage."
    scene sm1mv02s01i-61-mc-talk-kv with dissolve
    play voice2 mc_surprised_why3 noloop
    mc "Why not?"
    scene sm1mv02s01i-62-kv-talk-mc with dissolve
    play voice4 kanya_thinking_eeh1 noloop
    kv "It's not soundproof. So you can hear all the planes, trains, and automobiles that zip by."
    kv "But there's not a lot of them."
    scene sm1mv02s01i-63-sy-talk-kv with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh, that's good to know!"
    sy "Here we can build a huge set of the spaceship! And a small set for when they go down to the planet."
    scene sm1mv02s01i-64-sy-talk with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "The CGI we would have to do if we were building most of the ship for most of the movie would be insane. And time costly."
    sy "But if we build the ship instead, we just have to do the outside! Which is easy peasy."
    sy "Especially if we put up some chroma green screens outside the windows."
    play sound sfx_heels_steps2 loop
    scene sm1mv02s01i-65-mc-talk-sy with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "Wow, you've really been thinking about this, haven't you."
    stop sound fadeout 1.0
    scene sm1mv02s01i-66-sy-talk-mc with dissolve
    play voice3 stacy_yes_yap1 noloop
    sy "Yep!"
    sy "So anytime we do a movie that's primarily one location, we can always come over here and build it! And Kanya has offered quite the deal for letting us rent this place."
    scene sm1mv02s01i-67-kv-talk-sy with dissolve
    play voice4 kanya_thinking_hmm1 noloop
    kv "I figure if I want to film the movie, I should probably help make it happen."
    scene sm1mv02s01i-68-mc-talk-kv with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "And we appreciate that."
    scene sm1mv02s01i-69-kv-talk-mc with dissolve
    play voice4 kanya_yes_yeah2 noloop
    kv "Plus, I'm not really using the space too much."
    scene sm1mv02s01i-70-sy-talk-mc with dissolve
    play voice3 stacy_huh2 noloop
    sy "So, what do you think?"
    scene sm1mv02s01i-71-mc-talk-sy with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "I think..."
    scene sm1mv02s01i-72-sy-talk-mc with dissolve
    play voice3 stacy_surprised_huh5 noloop
    if persistent.is_special:
        sy "You think you have the best, most wonderful, incredible, magnificent sister in this whole galaxy?"
    else:
        sy "You think you have the best, most wonderful, incredible, magnificent girlfriend in this whole galaxy?"
    scene sm1mv02s01i-73-mc-talk-sy with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "You forgot \"humble\", too."
    scene sm1mv02s01i-74-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_huh5 noloop
    sy "Nobody has time for humility anymore, [mcname]."
    play sound sfx_heels_steps2 loop
    scene sm1mv02s01i-75-mc-talk-sy with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "I think it's perfect, Stacy."
    stop sound fadeout 1.0
    scene sm1mv02s01i-76-sy-talk with dissolve
    play voice3 stacy_happy_yay3 noloop
    sy "Yay!"
    sy "Now it's time to start the build! And you, sir, need to go get our actresses locked in!"
    scene sm1mv02s01i-77-mc-talk-sy with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I will, I will. Are you going to order everything we need for the set?"
    scene sm1mv02s01i-78-sy-talk-mc with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "I-{w} wait, what the hell are we going to build?"
    play voice2 mc_thinking_hm noloop
    mc "Why don't we head back into the studio and we can plan something out?"
    play sound sfx_heels_steps2 loop
    scene sm1mv02s01i-79-kv-talk with dissolve
    play voice4 kanya_yes_yep1 noloop
    kv "I'll get the coffee ready."
    scene sm1mv02s01i-80-sy-talk-kv with dissolve
    play voice3 stacy_happy_wooh1 noloop
    sy "Woooo! Party at Kanya's!"
    stop sound fadeout 1.0
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1mv02s01i-81-kv-mc-sy with fade
    play sound sfx_pen_writing1
    pause
    scene sm1mv02s01i-82-kv-mc-sy with fade
    pause
    scene sm1mv02s01i-83-kv-mc-sy with fade
    play sound sfx_cloth_shuffle1 volume 0.5
    pause
    scene sm1mv02s01i-84-kv-mc-sy with fade
    play sound sfx_photocamera_flash2
    pause
    scene sm1mv02s01i-85-kv-mc-sy with fade
    play sound sfx_photocamera_flash2
    pause
    $ renpy.music.set_volume(0.55, 2.5, "music" )
    scene sm1mv02s01i-86-kv-mc-sy with fade
    play sound sfx_videocamera_finish
    pause
    scene sm1mv02s01i-87-sy-talk with dissolve
    play voice3 stacy_arrogant_huh2 noloop
    sy "That's the final design of the ship?"
    scene sm1mv02s01i-88-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, I think so. It will give us enough space for everything, make it feel open and not so claustrophobic."
    scene sm1mv02s01i-89-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_mmm2 noloop
    sy "A little... on the nose, don't you think?"
    play voice2 mc_no_nah2 noloop
    mc "Nah, it'll be great!"
    play sound sfx_bed_slide2 volume 0.7
    scene sm1mv02s01i-90-sy-talk-mc with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "If you say so."
    sy "All right, well I'll start getting everything we need."
    sy "And you sir, need to go and find us our talent!"
    scene sm1mv02s01i-91-mc-talk-sy with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Don't worry, I'm on it."
    scene sm1mv02s01i-92-sy-talk with dissolve
    play voice3 stacy_arrogant_hmm2 noloop
    sy "Kanya and I have a few logistical things to iron out. You get out there, and let's start making this movie!"
    play sound sfx_throw_something1
    scene sm1mv02s01i-93-mc-talk-sy with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Aye, aye, captain!"
    jump sm1mv02s01_exit_to_map
label sm1mv02s01_exit_to_map:
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ scifi_movie = SciFiMovieController()
    $ StoryController.end_scene(MOVIE_SCIFI, 8, 0, 4, PHOTO_DOJO, LPD_SUB_INSIDE, LPD_OVERVIEW)
    return