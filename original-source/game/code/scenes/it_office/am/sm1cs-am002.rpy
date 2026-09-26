label sm1cs_am002:
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound3 sfx_office_ambience1 fadein 2.0
    scene sm1cs-am02-01-office-evening with dissolve
    pause
    play sound sfx_chair_slide1
    scene sm1cs-am02-02-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "What a day."
    scene sm1cs-am02-03-mc-inner-talk with dissolve
    pause
    play sound sfx_heels_steps2 loop
    scene sm1cs-am02-04-mc-walk with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mct "Time to clear the cache."
    $ renpy.music.set_volume(0.4, 2.0, "sound3" )
    play sound2 sfx_heels_steps1
    scene sm1cs-am02-05-mc-am-bump with dissolve
    pause
    play voice2 mc_pain_ou1 noloop
    play voice3 girl22_arrogant_hm noloop
    play music music_chiptuned_defeat
    stop sound2
    play sound sfx_leg_kick5
    scene sm1cs-am02-06-mc-talk-am with hpunch
    mc "Hey April - ugh."
    play sound sfx_epic_jump1
    scene sm1cs-am02-07-phone with hpunch
    pause
    play sound sfx_phone_fall1 volume 0.7
    scene sm1cs-am02-08-c1-mc-talk-am with dissolve
    play voice2 mc_disappointed_ah2 noloop
    pause
    scene sm1cs-am02-09-c1-mc-look-am with dissolve
    menu:
        "You should watch where you're going."(hint="sm1cs_am002_m01_h01"):
            scene sm1cs-am02-11-c2-mc-talk-am with dissolve
            play voice2 mc_hey_hey2 noloop
            mc "You should really watch where you're going, April."
            play sound sfx_heels_steps1 loop
            scene sm1cs-am02-12-mc-inner-talk with dissolve
        "April, you okay?"(hint="sm1cs_am002_m01_h02"):
            call sm1cs_am002_m01_c02 from _call_sm1cs_am002_m01_c02
            scene sm1cs-am02-11-c2-mc-talk-am with dissolve
            play voice2 mc_hey_hey2 noloop
            mc "April, you okay?"
            play sound sfx_heels_steps1 loop
            scene sm1cs-am02-12-mc-inner-talk with dissolve
            play voice2 mc_arrogant_hm3 noloop
            mc "Uh... earth to April."
    play voice2 mc_arrogant_hm1 noloop
    mct "What's with her? She never just sees me and moves on."
    mct "She always takes a jab at my skills."
    scene sm1cs-am02-13-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mct "Maybe I'm improving in her eyes."
    stop sound fadeout 1.0
    scene sm1cs-am02-14-ag-talk-mc with dissolve
    play voice4 girl27_arrogant_ha noloop
    ag "What did she say?"
    play voice2 mc_pain_ou3 noloop
    play sound sfx_skirt_off1
    scene sm1cs-am02-15-mc-talk-ag with hpunch
    mc "Buah!"
    scene sm1cs-am02-16-ag-talk-mc with dissolve
    play voice4 girl27_happy_laugh4 noloop
    ag "Sorry for being sneaky, [mcname]."
    scene sm1cs-am02-17-mc-talk-ag with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "Totally fine. Gave my heart a workout."
    scene sm1cs-am02-18-ag-talk-mc with dissolve
    play voice4 girl27_thinking_emm noloop
    ag "Did she say anything? Did you hear her talking on her phone?"
    scene sm1cs-am02-19-mc-talk-ag with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Uh, she actually didn't say anything. And we weren't in the bathrooms at the same time, Anna."
    scene sm1cs-am02-20-ag-talk-mc with dissolve
    play voice4 girl27_thinking_hmm8 noloop
    ag "Good... good."
    scene sm1cs-am02-21-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop
    mct "What is going on here?"
    scene sm1cs-am02-22-mc-talk-ag with dissolve
    play voice2 d2s9_mchey noloop
    mc "Is there a problem?"
    scene sm1cs-am02-23-ag-talk-mc with dissolve
    play voice4 girl27_no_unsure noloop
    ag "Oh no. Just um... I want to make sure April is not hiding in the bathroom making personal calls on company time."
    scene sm1cs-am02-24-mc-talk-ag with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okay... Maybe she was getting texts? She seemed super into her phone."
    scene sm1cs-am02-25-ag-talk-mc with dissolve
    play voice4 girl27_yes_simple noloop
    ag "Hmmm. Yes."
    ag "How is she doing on your work for the project?"
    scene sm1cs-am02-26-mc-talk-ag with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh really good. She's a natural. And after many attempts, I think I've figured out the best way to how to ask for help without her yelling at me."
    scene sm1cs-am02-27-ag-talk-mc with dissolve
    play voice4 girl27_yes_ugu1 noloop
    ag "Good. Well if she ends up slacking on the news website, be sure to let me know, [mcname]."
    scene sm1cs-am02-28-mc-talk-ag with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Totally."
    mc "I umm...{w} I actually need to {i}go{/i}, Anna."
    scene sm1cs-am02-29-am-talk-mc with dissolve
    play voice4 girl27_surprised_oh2 noloop
    am "Oh, excuse me."
    play sound sfx_heels_steps2 loop
    scene sm1cs-am02-30-mc-walk with dissolve
    pause
    $ renpy.music.set_volume(1.0, 5.0, "sound3" )
    stop sound fadeout 1.0
    scene sm1cs-am02-31-mc-inner-talk with fade
    play sound sfx_heels_steps2 loop
    play voice2 mc_happy_a1 noloop
    mct "Alright, time to open up another ticket."
    scene sm1cs-am02-32-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mct "What is she doing? Looking at dog photos?"
    scene sm1cs-am02-33-am-phone with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "That can't be for work. This must be what Anna was worried about."
    scene sm1cs-am02-34-mc-inner-talk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "But I shouldn't say anything. Or should I?"
    play sound sfx_chair_slide1 noloop
    scene sm1cs-am02-35-mc-inner-talk with dissolve
    mct "Nah. As far as I can tell, April covered for me when I screwed up on data convertor."
    play sound sfx_mouse_clicks1
    scene sm1cs-am02-36-mc-inner-talk with dissolve
    play voice2 mc_angry_hm2 noloop
    mct "I still can't really believe she didn't tell Anna or Claire."
    scene sm1cs-am02-37-mc-inner-talk with dissolve
    mct "Maybe she's just waiting for the right moment to toss me under the bus."
    play sound2 sfx_heels_steps2 fadein 1.0
    scene sm1cs-am02-38-mc-notice-ag with dissolve
    mct "Okay, now I'm just thinking crazy. She wouldn't do-"
    scene sm1cs-am02-40-mc-inner-talk with dissolve
    play voice2 mc_pain_rrrr noloop
    mct "Oh shit. April, turn around."
    scene sm1cs-am02-39-am-phone with dissolve
    pause
    stop sound2 fadeout 1.0
    scene sm1cs-am02-41-ag-talk-am with dissolve
    play voice4 girl27_hey_sexy noloop
    ag "Hey April. How's it going?"
    scene sm1cs-am02-42-am-talk-ag with dissolve
    play voice3 girl22_disappointed_ehh1 noloop
    am "Can this... Urrah..."
    scene sm1cs-am02-43-am-talk-ag with dissolve
    play voice3 girl22_hey_scared noloop
    am "Anna, can this please wait till tomorrow?"
    scene sm1cs-am02-44-mc-inner-talk with hpunch
    play voice2 mc_surprised_huh7 noloop
    mct "Did April just use the word 'please'?"
    scene sm1cs-am02-45-ag-talk-am with dissolve
    play voice4 girl27_no_short noloop
    ag "Tomorrow? No. You were supposed to have those changes to the middleware done today."
    ag "I'm trying to see where all the pieces are so I can make a progress report, but you keep disabling the remote viewer tools."
    scene sm1cs-am02-46-am-talk-ag with dissolve
    play voice3 girl22_disappointed_ehh2 noloop
    am "Ever heard of a thing called privacy, Aubergine?"
    scene sm1cs-am02-47-ag-talk-am with dissolve
    play voice4 girl27_arrogant_huh1 noloop
    ag "Will the task be done today or not?"
    scene sm1cs-am02-46-am-talk-ag with dissolve
    play voice3 girl22_disappointed_geh noloop
    pause
    scene sm1cs-am02-47-ag-talk-am with dissolve
    play voice4 girl27_arrogant_hah noloop
    ag "I'll take that as a \"no\"."
    play sound sfx_gadgets_laptop_closed
    scene sm1cs-am02-48-am-talk-ag with dissolve
    play voice3 girl22_angry_dagh noloop
    am "There, you have your answer."
    am "Look, it's like I said earlier. It will be ready tomorrow."
    scene sm1cs-am02-49-ag-talk-am with dissolve
    play voice4 girl27_disappointed_ehh1 noloop
    ag "I don't need to-"
    ag "*sighs* April, please just talk to me. This isn't like you. I mean, it's like you, but... even with all your insults and petty barbs, you never get this far behind."
    play voice3 girl22_angry_argh3 noloop
    play sound sfx_chair_slide1 volume 1.5
    scene sm1cs-am02-50-am-talk-ag with hpunch
    am "Shut it. I'm not behind."
    am "And if I was, you know exactly the reason I am."
    scene sm1cs-am02-51-mc-look-am with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "Uh oh. Here it comes."
    scene sm1cs-am02-52-am-talk-ag with dissolve
    play voice3 girl22_angry_argh2 noloop
    am "I've asked every month for those compatibility upgrades but no one gives me a straight answer."
    am "You know how fickle middleware can be. And all this squawking from you throws me off my game and sets me back even further."
    scene sm1cs-am02-53-ag-talk-am with dissolve
    play voice4 girl27_hey_active noloop
    ag "Just be calm. And I'm not squawking at you."
    ag "I'm just talking to you, and being incredibly patient with you, as a matter of fact."
    ag "You have been dodging my calls and not returning my emails the whole week."
    play voice3 girl22_angry_geh noloop
    scene sm1cs-am02-54-am-talk-ag with hpunch
    am "Why don't you suck on my queefs?"
    am "Then at least you'd be doing something useful instead of bothering me."
    scene sm1cs-am02-55-ag-talk-am with dissolve
    play voice4 girl27_surprised_oh3 noloop
    ag "April..."
    scene sm1cs-am02-56-am-talk-ag with dissolve
    play voice3 girl22_angry_breathing noloop
    am "I'm out of here. I'm going to just grab my laptop and work out of the park for a while."
    scene sm1cs-am02-57-ag-talk-am with dissolve
    play voice4 girl27_thinking_emm3 noloop
    ag "For a while?"
    scene sm1cs-am02-58-am-talk-ag with dissolve
    play voice3 girl22_disappointed_ehh3 noloop
    am "*sighs* Just... just think of it as working from home, but I'll be working from the park."
    scene sm1cs-am02-59-ag-talk-mc with dissolve
    play voice4 girl27_disappointed_ehh2 noloop
    ag "You and [mcname] are supposed to be working together on the data for the news website."
    scene sm1cs-am02-60-am-talk-ag with dissolve
    play voice3 girl22_disappointed_mmm noloop
    am "You're right."
    scene sm1cs-am02-61-am-look-mc with dissolve
    pause
    play voice2 mc_surprised_huh1 noloop
    play sound sfx_throw_something1 volume 2.0
    play sound2 sfx_leg_kick6 noloop
    scene sm1cs-am02-62-am-throw with hpunch
    pause
    play sound sfx_sodacan_clink
    scene sm1cs-am02-63-soda with dissolve
    pause
    scene sm1cs-am02-64-mc-talk with dissolve
    play voice2 mc_pain_ou4 noloop
    mc "Ow."
    play sound sfx_cloth_rustling2
    scene sm1cs-am02-65-mc-talk-am with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "What the hell, April?"
    scene sm1cs-am02-66-am-talk-mc with dissolve
    play voice3 girl22_arrogant_he noloop
    am "In case you weren't listening in already, I'm going to be working at the park."
    am "If your consciousness absolutely has to bother mine, email me."
    scene sm1cs-am02-67-mc-talk-am with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.5
    mc "Hmm."
    scene sm1cs-am02-68-ag-talk-mc with dissolve
    play voice4 girl27_disappointed_oh3 noloop
    ag "I am so sorry about that."
    menu:
        "She's a fucking menace."(hint="sm1cs_am002_m02_h01"):
            call sm1cs_am002_m02_c01 from _call_sm1cs_am002_m02_c01
            scene sm1cs-am02-69-c1-mc-talk-ag with dissolve
            play voice2 mc_angry_errr2 noloop
            mc "She's a fucking menace, Anna."
            scene sm1cs-am02-70-c1-ag-talk-mc with dissolve
            play voice4 girl27_yes_yeah4 noloop
            ag "I know, but... even if I could get her off the team, I don't think I would."
            scene sm1cs-am02-71-c1-mc-talk-ag with dissolve
            play voice2 mc_surprised_what1 noloop
            mc "Excuse me?"
            scene sm1cs-am02-72-c1-ag-talk-mc with dissolve
            play voice4 girl27_thinking_hmm5 noloop
            ag "We need her, and she knows it. I can't go to Claire and say we lost April."
            scene sm1cs-am02-73-c1-mc-talk-ag with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "*sighs*"
        "She seems stressed."(hint="sm1cs_am002_m02_h02"):
            scene sm1cs-am02-74-c2-mc-talk-ag with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "She seems super stressed about something."
            scene sm1cs-am02-75-c2-ag-talk-mc with dissolve
            play voice4 girl27_yes_simple3 noloop
            ag "Yes. I want to help her with it, but she's so stubborn."
    play sound sfx_chair_slide1
    scene sm1cs-am02-76-mc-talk-ag with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "Never imagined someone would throw a soda at me."
    scene sm1cs-am02-77-ag-talk-mc with dissolve
    play voice4 girl27_happy_laugh6 noloop
    ag "At least it wasn't full."
    scene sm1cs-am02-78-mc-talk-ag with dissolve
    play voice2 mc_scared_huuuh1 noloop
    mc "For real? April threw a full soda can at you once?"
    scene sm1cs-am02-79-ag-talk-mc with dissolve
    play voice4 girl27_no_serious noloop
    ag "Not me, thankfully. It was this asshole customer. Real class act."
    ag "Bursts into our office and starts cursing and complaining about an issue with his software."
    ag "And Orbix didn't even have anything to do with his problem. It was another company we were working with."
    ag "I tried talking to him but he wouldn't listen to me, or Claire."
    scene sm1cs-am02-80-mc-talk-ag with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What happened?"
    scene sm1cs-am02-81-ag-talk-mc with dissolve
    play voice4 girl27_happy_relief2 noloop
    ag "April happened."
    ag "She just walked in and chucked the can she'd just bought. Hit the dude right in the jaw."
    scene sm1cs-am02-82-mc-talk-ag with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Hah. So April was defending you."
    scene sm1cs-am02-83-ag-talk-mc with dissolve
    play voice4 girl27_no_happy noloop
    ag "Hahaha, never. She said it was the fastest way to get his attention and didn't think it would knock him out."
    ag "That was quite the day."
    scene sm1cs-am02-84-ag-talk-mc with dissolve
    play voice4 girl27_disappointed_eh1 noloop
    ag "I'm really hoping that she will either chill the fuck out or at least open up about what's bothering her."
    ag "But I guess for now, if you run into any problems with the website, you'll have to go down to the park on Wednesdays and Fridays."
    ag "Understood?"
    scene sm1cs-am02-85-mc-talk-ag with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Loud and clear."
    scene sm1cs-am02-84-ag-talk-mc with dissolve
    play voice4 girl27_happy_great3 noloop
    ag "Thanks [mcname]."
    stop sound2 fadeout 3.0
    stop sound3 fadeout 2.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(AM_STORY, 1, 0, 2)
    return
label sm1cs_am002_m01_c02:
    $ player.set_choice("sm1cs_am002_am_okay")
    return
label sm1cs_am002_m02_c01:
    $ player.set_choice("sm1cs_am002_am_menace")
    $ CharacterController.get_character("ag").add_point()
    return
label sm1cs_am002_unlocks:
    call sm1cs_am002_m01_c02 from _call_sm1cs_am002_m01_c02_1
    call sm1cs_am002_m02_c01 from _call_sm1cs_am002_m02_c01_1
    if config_storyline_mode is True:
        $ execute_storyline_config(AM_STORY)
    return