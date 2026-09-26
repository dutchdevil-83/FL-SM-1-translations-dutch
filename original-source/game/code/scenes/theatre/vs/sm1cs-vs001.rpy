image sm1cs-vs-glambot-1 = Movie(play = "images/FS_T/VS/s001/anim/sm1cs-vs001-a14-2x-50fps.webm", start_image = "sm1cs-vs001-a14 mc-vs-talk5-glambot-14-000_i", image = "sm1cs-vs001-a14 mc-vs-talk5-glambot-14-179_i", loop = False)
label sm1cs_vs001:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play sound sfx_heels_steps2 loop
    scene sm1cs-vs001-01 mc-vs-entry1_c1 with dissolve
    play music music_lizards_casual
    pause
    scene sm1cs-vs001-01 mc-vs-entry1_c2 with dissolve
    pause
    play sound2 sfx_cloth_rustling3 noloop
    scene sm1cs-vs001-02 mc-vs-entry2_c1 with dissolve
    pause
    scene sm1cs-vs001-02 mc-vs-entry2_c2 with dissolve
    pause
    play sound sfx_cloth_rustling2
    scene sm1cs-vs001-03 mc-vs-bend1_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey there-"
    scene sm1cs-vs001-04 mc-vs-bend2_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mct "Woah. That is some flexibility."
    scene sm1cs-vs001-03 mc-vs-bend1_c2 with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Hey there, Veronica."
    play sound sfx_cloth_rustling4
    scene sm1cs-vs001-04 mc-vs-bend2_c2 with dissolve
    play voice3 girl33_hey_serious noloop
    vs "Hey, [mcname]. What's new?"
    scene sm1cs-vs001-05 mc-vs-stand1_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Not much, still just getting used to navigating this place."
    scene sm1cs-vs001-05 mc-vs-stand1_c2 with dissolve
    play voice3 girl33_happy_laugh1 noloop
    vs "Haha. I'm sure you'll get the hang of it. Just don't take too long."
    vs "You want to impress Denise, right?"
    scene sm1cs-vs001-06 mc-vs-bend1_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Denise. Yeah, she's the director, right?"
    scene sm1cs-vs001-06 mc-vs-bend1_c2 with dissolve
    play voice3 girl33_happy_laugh2 noloop
    vs "*giggles*"
    vs "Nrrrh... Yeah. She's the one who gave you a chance, silly."
    play sound sfx_cloth_rustling5
    scene sm1cs-vs001-07 mc-vs-bend2_c1 with dissolve
    play voice3 girl33_arrogant_huh2 noloop
    vs "Are my stretches too distracting?"
    play voice2 mc_no_no10 noloop
    mc "Huh? No, I mean, not at all. I didn't realize the show going on right now was so physical."
    scene sm1cs-vs001-07 mc-vs-bend2_c2 with dissolve
    play voice3 girl33_thinking_eem1 noloop
    vs "This one isn't, but I always try to keep up with my stretches during downtime."
    vs "Plus I'm going out dancing tonight. Gotta keep things limber."
    play sound sfx_cloth_rustling3
    scene sm1cs-vs001-08 mc-vs-bend3_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah limber. Very important."
    play sound sfx_cloth_rustling2
    scene sm1cs-vs001-08 mc-vs-bend3_c2 with dissolve
    pause
    scene sm1cs-vs001-09 mc-vs-bend4_c1 with dissolve
    mct "Why is she looking at me like that?"
    play voice2 mc_surprised_what1 noloop
    mc "What's up?"
    play sound sfx_cloth_rustling1
    scene sm1cs-vs001-09 mc-vs-bend4_c2 with dissolve
    pause
    scene sm1cs-vs001-09 mc-vs-bend4_c3 with dissolve
    play voice3 girl33_disappointed_eeh noloop
    vs "Well, I was trying to keep it a secret, but I suppose I should tell you."
    play sound sfx_cloth_rustling2
    scene sm1cs-vs001-10 mc-vs-talk1_c2 with dissolve
    play voice3 girl33_happy_laugh3 noloop
    vs "I know who you are."
    scene sm1cs-vs001-10 mc-vs-talk1_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.4
    mc "Uh, I hope so. We talked quite a bit after I screwed up my audition."
    scene sm1cs-vs001-11 mc-vs-talk2_c2 with dissolve
    play voice3 girl33_arrogant_yeah noloop
    vs "Yeah, but that's not what I'm talking about.{w} I'm talking about how you are the guy who brought down Fetish Locator."
    vs "At least I'm pretty sure you are. Right?"
    scene sm1cs-vs001-11 mc-vs-talk2_c1 with dissolve
    mct "Hopefully, no one is paying attention to us."
    play voice2 mc_yes_yes2 noloop
    mc "I am."
    scene sm1cs-vs001-12 mc-vs-talk3_c2 with dissolve
    play voice3 girl33_surprised_ohmy noloop
    vs "I knew it!"
    scene sm1cs-vs001-12 mc-vs-talk3_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Easy. It's not like I'm hiding that part of my life, but you never know how some people will react to information like that."
    scene sm1cs-vs001-a14 mc-vs-talk5-glambot-14-000_i with dissolve
    play voice3 girl33_thinking_hmm1 noloop
    vs "I didn't think about that. That's so true."
    play sound [sfx_camera_fly1] volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0 noloop
    play sound3 ["<silence 3.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs-vs-glambot-1
    pause
    stop sound2 fadeout 1.0
    play sound sfx_cloth_rustling1
    scene sm1cs-vs001-15 mc-vs-walk1_c2 with dissolve
    queue sound sfx_heels_steps2 loop
    play voice3 girl33_arrogant_laugh noloop
    vs "Come on, I know the perfect spot backstage."
    scene sm1cs-vs001-15 mc-vs-walk1_c1 with dissolve
    pause
    play sound sfx_double_door1
    scene sm1cs-vs001-16 mc-vs-entry1_c1 with fade
    pause
    scene sm1cs-vs001-16 mc-vs-entry1_c2 with dissolve
    play voice3 girl33_thinking_hmm3 noloop
    vs "This more comfortable?"
    menu:
        "Flirt"(hint="sm1cs_vs001_m01_h01"):
            call sm1cs_vs001_m01_c01 from _call_sm1cs_vs001_m01_c01
            scene sm1cs-vs001-17 mc-vs-wink_c1 with dissolve
            play voice2 mc_thinking_hmm6 noloop
            mc "It's great."
            mc "I imagine a smart girl like you could use this place for all sorts of mischief."
            scene sm1cs-vs001-17 mc-vs-wink_c2 with dissolve
            play voice3 girl33_happy_laugh6 noloop
            vs "Hehehe. If these walls could talk."
            vs "But I still want to learn more about your story, [mcname]."
        "Worried"(hint="sm1cs_vs001_m01_h02"):
            scene sm1cs-vs001-17 mc-vs-wink_c1 with dissolve
            play voice2 mc_thinking_mmm5 noloop
            mc "Um... why did you bring me over here?"
            scene sm1cs-vs001-17 mc-vs-wink_c2 with dissolve
            play voice3 girl33_disappointed_oh noloop
            vs "I thought it would be better with some privacy. It felt like you were worried other people might hear us."
            scene sm1cs-vs001-19 mc-vs-talk2_c1 with dissolve
            play voice2 mc_yes_aga1 noloop
            mc "Smart. But I'm still worried that {i}you{/i} already know about my past."
            scene sm1cs-vs001-19 mc-vs-talk2_c2 with dissolve
            play voice3 girl33_surprised_what noloop
            vs "What? You don't have to worry about that with me, [mcname]."
            vs "But I can't resist digging into some hot gossip."
    play sound sfx_cloth_rustling1
    scene sm1cs-vs001-18 mc-vs-talk1_c2 with dissolve
    play voice3 girl33_surprised_huh1 noloop
    vs "So is it true? Lydia twisted you around her finger and then shattered your heart into like a million pieces."
    scene sm1cs-vs001-18 mc-vs-talk1_c1 with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "Twisted me around her finger? Listen, Veronica, this isn't really the-"
    scene sm1cs-vs001-20 mc-vs-talk3_c2 with dissolve
    play voice3 girl33_disappointed_aah noloop
    vs "It's okay. This is a totally safe place, [mcname]. You don't have to say anything."
    scene sm1cs-vs001-20 mc-vs-talk3_c1 with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What? I don't... how did you figure out it was me anyhow?"
    scene sm1cs-vs001-21 mc-vs-talk4_c2 with dissolve
    play voice3 girl33_happy_relief noloop
    vs "Well, I didn't know for sure until you said it was you."
    vs "But I got suspicious when we first met because I recognized you from campus."
    scene sm1cs-vs001-21 mc-vs-talk4_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "You were a student at the college?"
    scene sm1cs-vs001-19 mc-vs-talk2_c2 with dissolve
    play voice3 girl33_yes_yep noloop
    vs "Still am. Aren't you still taking classes?"
    scene sm1cs-vs001-22 mc-vs-talk5_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Nah. I uh... I found something else to put my focus on."
    scene sm1cs-vs001-21 mc-vs-talk4_c2 with dissolve
    play voice3 girl33_disappointed_off noloop
    vs "Oh. Is it because of Lydia?"
    scene sm1cs-vs001-23 mc-vs-talk6_c1 with dissolve
    play voice2 mc_surprised_why1 noloop
    mc "Why do you say that?"
    scene sm1cs-vs001-23 mc-vs-talk6_c2 with dissolve
    play voice3 girl33_disappointed_mmf1 noloop
    vs "Well, I can just imagine how that felt..."
    vs "The woman who was the apple of your eye turned out to be a snake whispering poison in your ears."
    vs "You are so{w} lucky."
    menu:
        "You don't know what you're talking about"(hint="sm1cs_vs001_m02_h01"):
            scene sm1cs-vs001-24 mc-vs-talk7_c1 with dissolve
            play voice2 mc_no_no5 noloop
            mc "Veronica, just stop. You don't know what you're talking about."
            scene sm1cs-vs001-24 mc-vs-talk7_c2 with dissolve
            play voice3 girl33_disappointed_geh noloop
            vs "Oh. I'm... I'm sorry, [mcname]."
            vs "Hearing about the story, it got me so excited."
            vs "I mean what else has ever happened in this town that even comes close to the Fetish Locator Story."
            vs "But it was-"
            scene sm1cs-vs001-25 mc-vs-talk8_c1 with dissolve
            play voice2 mc_yes_yeah5 noloop
            mc "-my life"
            scene sm1cs-vs001-25 mc-vs-talk8_c2 with dissolve
            play voice3 girl33_disappointed_mmf3 noloop
            vs "Big yikes."
            scene sm1cs-vs001-26 mc-vs-talk9_c1 with dissolve
            play voice2 mc_happy_yay2 noloop
            mc "Don't worry about it, Veronica. It's strange, but it's almost nice to talk to someone about it."
            mc "But maybe we can talk more about it when we've gotten to know each other better."
            scene sm1cs-vs001-24 mc-vs-talk7_c2 with dissolve
            play voice3 girl33_yes_happy noloop
            vs "Oh, of course. Absolutely. Thanks for being cool about it. Sometimes I just get carried away."
            scene sm1cs-vs001-24 mc-vs-talk7_c1 with dissolve
            play voice2 mc_arrogant_heh3 noloop
            mc "I can see why you're the lead. No one else has your passion."
            scene sm1cs-vs001-21 mc-vs-talk4_c2 with dissolve
            play voice3 girl33_happy_laugh5 noloop
            vs "Hehe. Picked up on that, did you?"
            vs "Well, if there is something I'll never apologize for, it is my energy."
            vs "I love putting it to good use in a show."
            vs "Every play lets you become someone new, go somewhere exotic, learn something about ourselves that we never expected."
            vs "You'll understand once you're on stage with us."
        "I'm so lucky?"(hint="sm1cs_vs001_m02_h02"):
            call sm1cs_vs001_m02_c02 from _call_sm1cs_vs001_m02_c02
            scene sm1cs-vs001-24 mc-vs-talk7_c1 with dissolve
            play voice2 mc_surprised_uh1 noloop
            mc "I'm so... lucky?"
            scene sm1cs-vs001-24 mc-vs-talk7_c2 with dissolve
            play voice3 girl33_yes_happy noloop
            vs "Totally! You've experienced the pain of actual, {b}real{/b}, betrayal. So few actors have experienced the kind of situations they take on."
            vs "Your life could have turned into a real-world tragedy, and now you will carry that weight with you forever."
            scene sm1cs-vs001-25 mc-vs-talk8_c1 with dissolve
            play voice2 mc_yes_yeah5 noloop
            mc "Guess I've been stress-eating more than before."
            scene sm1cs-vs001-25 mc-vs-talk8_c2 with dissolve
            play voice3 girl33_happy_laugh5 noloop
            vs "Hehehe. No silly. It's not real weight. You look fine."
            vs "Tall and sturdy and a little handsome."
            vs "No, what I mean is that this weight is inside of you."
            scene sm1cs-vs001-26-2 mc-vs-talk10_c2 with dissolve
            play voice3 girl33_disappointed_mmf3 noloop
            vs "And one day when you're on that stage, it's going to come out of you like lightning from a bottle."
            vs "I just know you'll blow the tops off everyone in the audience."
            vs "The theater has power, [mcname]. And once you're on stage, I think you're going to show people something special."
    play sound sfx_cloth_rustling2
    scene sm1cs-vs001-27 mc-vs-dance1_c2 with dissolve
    play voice3 girl33_thinking_hmm2 noloop
    vs "That's still your plan, right? You don't want to stay a stagehand forever, right?"
    scene sm1cs-vs001-27 mc-vs-dance1_c1 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Getting on stage is definitely one of my goals."
    scene sm1cs-vs001-36 mc-vs-story9_c2 with dissolve
    play voice3 girl33_happy_great noloop
    vs "Great. Then I'm your girl. If you ever need some pointers or want someone to give you notes on your next interview piece, give me a ring."
    vs "Give me your phone."
    play sound sfx_cloth_rustling3
    scene sm1cs-vs001-37 mc-vs-story10_c2 with dissolve
    pause
    play sound sfx_phone_tapping1 volume 1.6 loop
    scene sm1cs-vs001-37-1 mc-vs-story11-1_c2 with dissolve
    play voice3 girl33_yes_aga noloop
    vs "I put myself in as Bubblegum so it's easy to find me."
    scene sm1cs-vs001-37-1 mc-vs-story11-1_c1 with dissolve
    play voice3 girl33_thinking_eem2 noloop
    vs "And if you ever need to talk about Lydia or whatever... feel free."
    play sound sfx_cloth_rustling2
    scene sm1cs-vs001-38 mc-vs-story11_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure. Maybe one day."
    scene sm1cs-vs001-38 mc-vs-story11_c2 with dissolve
    play voice3 girl33_yes_simple noloop
    vs "Great. Well, I should probably get back to practicing with Kellie."
    play sound sfx_heels_steps2 loop
    scene sm1cs-vs001-39 mc-vs-story12_c2 with dissolve
    play voice3 girl33_hey_bye1 noloop
    vs "See you next time, [mcname]."
    stop sound fadeout 1.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2")
    $ StoryController.end_scene(VS_STORY, 2, 0, 1, THEATER, LTH_SUB_BACKSTAGE, LTH_BACKSTAGE_CENTER)
    return
label sm1cs_vs001_m01_c01:
    $ player.set_choice("sm1cs_vs001_flirt")
    return
label sm1cs_vs001_m02_c02:
    $ player.set_choice("sm1cs_vs001_so_lucky")
    $ CharacterController.get_character("vs").add_point()
    return
label sm1cs_vs001_unlocks:
    call sm1cs_vs001_m01_c01 from _call_sm1cs_vs001_m01_c01_1
    call sm1cs_vs001_m02_c02 from _call_sm1cs_vs001_m02_c02_1
    if config_storyline_mode is True:
        $ execute_storyline_config(VS_STORY)
    return