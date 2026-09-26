label sm1cs_arj001:
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1")
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1")
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2")
    $ renpy.music.set_volume(1.0, 0.5, "music2")
    scene sm1cs-arj001-10 mc-arj-walk_c1 with fade
    play sound sfx_door_open5
    play music2 music_starducks2_reverbed
    play voice2 mc_angry_hm1 noloop
    mct "Man... I hope AmRose is a little less... spicy this time. She seemed upset the last time I saw her."
    scene sm1cs-cs001-01 mc-cs-start1_c1 with dissolve
    if LocationController.get_map_location(STARDUCKS).get_location().get_discovered_status() is False:
        call sm1cs_cs001 from _call_sm1cs_cs001_2
    play voice2 d14s16_smell noloop
    $ renpy.music.set_volume(0.75, 3.0, "music2" )
    play sound sfx_heels_steps2 loop
    scene sm1cs-arj001-11 mc-arj-walk2_c1 with dissolve
    mct "Well... here goes nothing."
    play voice2 mc_hey_hey5 noloop
    mc "Hey, AmRose."
    scene sm1cs-arj001-11 mc-arj-walk2_c2 with dissolve
    play voice3 amrose_hey_whisper noloop
    arj "Hey."
    mct "All right, off to a better start..."
    play sound sfx_cloth_rustling4
    scene sm1cs-arj001-12 mc-arj-ask_c2 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "So, what's up? You... you wanted to talk about something."
    scene sm1cs-arj001-12 mc-arj-ask_c1 with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "So last time we talked, it kind of sounded like you had Stacy's flash drive."
    play voice3 amrose_thinking_hmm1 noloop
    arj "Maybe... why?"
    scene sm1cs-arj001-13 mc-arj-ask2_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.5
    mc "Do you think... I could get it back?"
    scene sm1cs-arj001-13 mc-arj-ask2_c2 with dissolve
    play voice3 amrose_no_simple1 noloop
    arj "No."
    play voice2 mc_thinking_mmm5 noloop
    mc "So you do have it."
    arj "So what if I do? {i}No one{/i} should have the zip drive."
    scene sm1cs-arj001-14 mc-arj-talk_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.6
    mc "I... you're right."
    scene sm1cs-arj001-14 mc-arj-talk_c2 with dissolve
    play voice3 amrose_surprised_uh3 noloop
    arj "W... what?"
    scene sm1cs-arj001-15 mc-arj-talk2_c1 with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "I don't think anyone should have it. Not me, not you, not Stacy."
    scene sm1cs-arj001-15 mc-arj-talk2_c2 with dissolve
    play voice3 amrose_thinking_hmm3 noloop
    arj "I... I'm surprised."
    play sound sfx_cloth_rustling1
    scene sm1cs-arj001-16 mc-arj-talk3_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Like I told you on the phone - I didn't know Stacy had really kept anything."
    mc "So it was news to me finding out that there was definitely more Fetish Locator data than I knew about."
    mc "So, if anything, thank you. Thank you for being honest with me."
    scene sm1cs-arj001-16 mc-arj-talk3_c2 with dissolve
    play voice3 amrose_disappointed_ehh1 noloop
    arj "Now, please, be honest with me [mcname].{w} Does Stacy still have my sca-"
    scene sm1cs-arj001-18 mc-arj-ask_c2 with dissolve
    play voice4 girl37_hey_simple noloop
    if not player.has_played_scene("sm1cs_cs001"):
        cs "Hi, I saw you come in, and wanted to make sure you didn't want to order or anything."
        scene sm1cs-arj001-18 mc-arj-ask_c1 with dissolve
        play voice2 mc_surprised_oh1 noloop
        mc "Oh, uhm, how about just a medium black coffee?"
        play voice4 girl37_thinking_hmm1 noloop
        cs "Sounds great."
    else:
        cs "Hey, welcome back in. You're a... medium light roast, right?"
    play voice2 mc_yes_yeah2 noloop
    mc "Yep!"
    scene sm1cs-arj001-18 mc-arj-ask_c2 with dissolve
    play voice4 girl37_disappointed_aga1 noloop
    cs "I'll bring one right out."
    scene sm1cs-arj001-19 mc-arj-walk_c2 with dissolve
    play voice3 amrose_arrogant_huh4 noloop
    arj "Just... tell me if Stacy has anything of mine from Fetish Locator."
    scene sm1cs-arj001-20 mc-arj-talk_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "I promise, she doesn't have anything. She said she wiped anything from anyone who was at college with us."
    scene sm1cs-arj001-20 mc-arj-talk_c2 with dissolve
    play voice3 amrose_disappointed_pff noloop
    arj "Hmph..."
    scene sm1cs-arj001-21 mc-arj-look_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "Come on. I... I don't know how else you want me to say it, AmRose."
    scene sm1cs-arj001-21 mc-arj-look_c2 with dissolve
    play voice3 amrose_thinking_hmm2 noloop
    arj "I want you to keep saying it until I know it's true."
    scene sm1cs-arj001-22 mc-arj-look2_c1 with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "But it {i}is{/i} the truth..."
    scene sm1cs-arj001-22 mc-arj-look2_c2 with dissolve
    play voice3 amrose_yes_yeah1 noloop
    arj "Yeah. And you told me the {b}truth{/b} when you said Stacy had deleted {i}all{/i} of the Fetish Locator data."
    play sound sfx_heels_steps1 loop
    scene sm1cs-arj001-23 mc-arj-coffee_c1 with dissolve
    play voice2 d2s12_emmm noloop
    mc "Well, I-"
    scene sm1cs-arj001-23 mc-arj-coffee_c2 with dissolve
    play voice4 girl37_thinking_hmm2 noloop
    cs "Here's that coffee for you."
    play voice2 mc_happy_yay1 noloop
    mc "Thank you! How much do I owe you?"
    play voice4 girl37_no_nah noloop
    cs "Don't worry about it, it's on the house."
    play sound2 sfx_cloth_rustling2 noloop
    stop sound fadeout 1.5
    scene sm1cs-arj001-24 mc-arj-talk_c2 with dissolve
    play voice3 amrose_arrogant_huh3 noloop
    arj "Still working your charms, I see."
    scene sm1cs-arj001-24 mc-arj-talk_c1 with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "I didn't do anything!"
    play sound sfx_bed_slide2
    scene sm1cs-arj001-25 mc-arj-talk2_c2 with dissolve
    play voice3 amrose_angry_ehh noloop
    arj "Whatever. Enjoy your new life with Stacy."
    play sound sfx_heels_steps1
    scene sm1cs-arj001-26 mc-arj-walk_c1 with dissolve
    play voice2 mc_thinking_wait2 noloop
    mc "Wait, AmRose..."
    play sound sfx_skirt_off1 volume 1.4
    scene sm1cs-arj001-26 mc-arj-walk_c2 with dissolve
    play voice3 amrose_angry_argh1 noloop
    arj "What, [mcname]. You expect me to just do whatever you want because you asked so nicely?"
    play voice2 mc_no_no6 noloop
    mc "No, I..."
    scene sm1cs-arj001-27 mc-arj-look_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I just want to say that I miss you."
    mc "I miss... well, whatever the hell we had. Before things got so... complicated."
    scene sm1cs-arj001-27 mc-arj-look_c2 with dissolve
    play voice3 amrose_happy_mmm noloop
    arj "I...{w} I do too."
    play voice2 mc_arrogant_hm3 noloop
    mc "Can we just pretend things are normal between us? For five minutes?"
    play voice3 amrose_disappointed_ehh2 noloop
    arj "Fine. For old time's sake."
    play sound sfx_cloth_rustling4
    scene sm1cs-arj001-28 mc-arj-look2_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "So... last time I saw you, you said you had two jobs over the summer?"
    scene sm1cs-arj001-28 mc-arj-look2_c2 with dissolve
    play voice3 amrose_thinking_oh1 noloop
    arj "You remember that?"
    play voice2 mc_yes_yes2 noloop
    mc "Of course I do."
    arj "Huh... well yeah, I did."
    scene sm1cs-arj001-29 mc-arj-ask_c1 with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "What were you doing?"
    scene sm1cs-arj001-29 mc-arj-ask_c2 with dissolve
    play voice3 amrose_thinking_hmm4 noloop
    arj "I..."
    arj "I went back home for the summer. I spent days working on the family farm, and nights working at a bar."
    arj "I had to save up because I knew when I came back I was going to be all on my own."
    scene sm1cs-arj001-30 mc-arj-ask2_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah... I'm sorry about how that all went, I never meant to hurt you."
    scene sm1cs-arj001-30 mc-arj-ask2_c2 with dissolve
    play voice3 amrose_no_nah noloop
    arj "It's whatever."
    scene sm1cs-arj001-32 mc-arj-look2_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "No, AmRose. It wasn't whatever. I hurt you. And I can't tell you how bad I feel about it."
    scene sm1cs-arj001-32 mc-arj-look2_c2 with dissolve
    play voice3 amrose_yes_ugu noloop
    arj "Thanks, [mcname]."
    scene sm1cs-arj001-33 mc-arj-look3_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Don't mention it."
    mc "But, now that you're back, what are you doing? You back in school?"
    scene sm1cs-arj001-33 mc-arj-look3_c2 with dissolve
    play voice3 amrose_yes_yap noloop
    arj "Something like that. I figured I was about halfway done, I might as well finish."
    play voice2 mc_happy_thatsgood noloop
    scene sm1cs-arj001-34 mc-arj-look4_c1 with dissolve
    mc "That's good!"
    scene sm1cs-arj001-34 mc-arj-look4_c2 with dissolve
    play voice3 amrose_arrogant_hmm1 noloop
    arj "What about you? Are you planning on finishing college?"
    play sound sfx_cloth_rustling3
    scene sm1cs-arj001-35 mc-arj-cup_c1 with dissolve
    play voice2 mc_disappointed_off2 noloop
    mc "I..."
    mc "I don't know."
    scene sm1cs-arj001-35 mc-arj-cup_c2 with dissolve
    play voice3 amrose_arrogant_huh1 noloop
    arj "You don't know? Are you seriously not going to finish college?"
    play sound sfx_drink_loop1 loop
    scene sm1cs-arj001-36 mc-arj-cup2_c1 with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Maybe one day... but Stacy and I are working on this thing, and I want to see that through first."
    scene sm1cs-arj001-36 mc-arj-cup2_c2 with dissolve
    play voice3 amrose_angry_ergh noloop
    arj "The porn studio thing, that's why you're not going to finish college."
    play sound sfx_cup_place1
    scene sm1cs-arj001-37 mc-arj-cup3_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, the porn studio thing."
    play voice3 amrose_disappointed_oh5 noloop
    arj "You really think that's going to work?"
    scene sm1cs-arj001-38 mc-arj-shrugs_c1 with dissolve
    play voice2 mc_yes_yes8 noloop
    mc "I hope so. We're working really hard on it, and I think that it could really be something."
    scene sm1cs-arj001-38 mc-arj-shrugs_c2 with dissolve
    play voice3 amrose_happy_phew2 noloop
    arj "Seems ridiculous to throw away your education for... that."
    play voice2 mc_yes_aga2 noloop
    mc "Maybe. But college will still be there, even if this all goes sideways on me."
    arj "Yeah."
    scene sm1cs-arj001-39 mc-arj-smirk_c1 with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Plus, if I wait a few years, maybe I can go back to school and not be 'the Fetish Locator Guy'."
    scene sm1cs-arj001-39 mc-arj-smirk_c2 with dissolve
    play voice3 amrose_happy_laugh3 noloop
    arj "I guess I didn't really think of that."
    scene sm1cs-arj001-40 mc-arj-talk_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "It will eventually go away, but for the time being, I'm just famous, I guess... or infamous, really."
    scene sm1cs-arj001-40 mc-arj-talk_c2 with dissolve
    play voice3 amrose_yes_yeah2 noloop
    arj "That you are."
    play sound sfx_cloth_rustling2
    scene sm1cs-arj001-41 mc-arj-stand_c2 with dissolve
    play voice3 amrose_yes_okay2 noloop
    arj "That's your five minutes of normalcy, [mcname]. I have to go."
    scene sm1cs-arj001-41 mc-arj-stand_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mc "This was nice, AmRose."
    play sound sfx_cloth_rustling3
    scene sm1cs-arj001-42 mc-arj-stand2_c2 with dissolve
    play voice3 amrose_thinking_hmm5 noloop
    arj "I... have to admit, I enjoyed myself a bit. Pretending, and all."
    scene sm1cs-arj001-42 mc-arj-stand2_c1 with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "We should do this again."
    play voice3 amrose_yes_yeah4 noloop
    arj "Maybe..."
    scene sm1cs-arj001-43 mc-arj-smirk_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.6
    mc "But... about the USB-"
    scene sm1cs-arj001-43 mc-arj-smirk_c2 with dissolve
    play voice3 amrose_angry_errr noloop
    arj "We almost got to end this on a high note, [mcname]."
    scene sm1cs-arj001-44 mc-arj-look_c1 with dissolve
    play voice2 mc_yes_yeah9 noloop
    mc "I know, but if I don't try, I have to go back and face the wrath of Stacy. You know what that's like."
    scene sm1cs-arj001-44 mc-arj-look_c2 with dissolve
    play voice3 amrose_disappointed_oh1 noloop
    arj "That I do..."
    arj "*sighs*"
    play sound sfx_cloth_rustling4
    scene sm1cs-arj001-45 mc-arj-look2_c1 with dissolve
    pause
    scene sm1cs-arj001-45 mc-arj-look2_c2 with dissolve
    play voice3 amrose_happy_phew2 noloop
    arj "I don't want it anyway. All this thing is going to do is bring trouble. So take it."
    play sound sfx_cloth_rustling5
    scene sm1cs-arj001-46 mc-arj-usb_c2 with dissolve
    play voice3 amrose_arrogant_hmm2 noloop
    arj "Seriously. You and Stacy should throw this thing into a fire. Or a lake. Somewhere no one can get their hands on it."
    scene sm1cs-arj001-46 mc-arj-usb_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Thank you, AmRose. I know Stacy will be glad to have it back."
    play voice3 amrose_no_uhuh noloop
    arj "I'm not doing this for her. I'm doing it for you."
    play sound sfx_heels_steps1 loop
    scene sm1cs-arj001-47 mc-arj-walk_c2 with dissolve
    play voice3 amrose_thinking_emm noloop
    arj "'Til next time."
    scene sm1cs-arj001-48 mc-arj-walk2_c1 with dissolve
    pause
    scene sm1cs-arj001-48 mc-arj-walk2_c2 with dissolve
    pause
    stop sound fadeout 1.0
    scene sm1cs-arj001-49 mc-arj-walk3_c1 with dissolve
    play sound2 sfx_heels_steps2
    play voice2 d1s2_mchey noloop
    mc "Oh hey, thanks for the free drink."
    scene sm1cs-arj001-49 mc-arj-walk3_c2 with dissolve
    play voice3 girl37_arrogant_ha noloop
    cs "Don't mention it."
    play sound2 sfx_cloth_rustling1 noloop
    scene sm1cs-arj001-50 mc-arj-talk_c2 with dissolve
    play voice3 girl37_surprised_ha noloop
    cs "Seriously, don't. Because my boss is kind of uptight about that kind of thing."
    scene sm1cs-arj001-50 mc-arj-talk_c1 with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "I won't. But I seriously appreciate it."
    play sound sfx_cloth_wiping1
    scene sm1cs-arj001-51 mc-arj-wiping_c1 with dissolve
    play voice3 girl37_happy_relief noloop
    cs "I thought you might. That looked pretty intense, whatever was happening back here."
    play voice2 mc_angry_oof noloop
    mc "It... it definitely was."
    scene sm1cs-arj001-51 mc-arj-wiping_c2 with dissolve
    play voice3 girl37_happy_mmm noloop
    cs "Was that your girlfriend or something?"
    scene sm1cs-arj001-52 mc-arj-look_c1 with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh no, she's not my girlfriend."
    scene sm1cs-arj001-52 mc-arj-look_c2 with dissolve
    play voice3 girl37_thinking_oh noloop
    cs "Oh, so your ex, then?"
    scene sm1cs-arj001-53 mc-arj-think_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Something like that."
    scene sm1cs-arj001-53 mc-arj-think_c2 with dissolve
    play voice3 girl37_arrogant_hm noloop
    cs "I was going to say, the sexual tension between you two was insane."
    scene sm1cs-arj001-54 mc-arj-shock_c1 with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Really?"
    play sound sfx_cloth_rustling2
    scene sm1cs-arj001-54 mc-arj-shock_c2 with dissolve
    play voice3 girl37_yes_yep noloop
    cs "Yep. I figured that there had to have been something between you two at some point."
    scene sm1cs-arj001-55 mc-arj-walk_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, there definitely was."
    play sound sfx_heels_steps1 loop
    scene sm1cs-arj001-55 mc-arj-walk_c2 with dissolve
    play voice3 girl37_hey_bye3 noloop
    cs "Well, thanks for coming in and giving me something to watch."
    scene sm1cs-arj001-56 mc-arj-think_c1 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Yeah, uhm, not a problem?"
    stop sound fadeout 2.0
    scene sm1cs-arj001-56 mc-arj-think_c2 with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mct "Sexual tension... I didn't realize me and AmRose still had sexual tension..."
    play sound sfx_heels_steps2 loop
    scene sm1cs-arj001-57 mc-arj-walk_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "I guess... if I had the chance, I'd still have sex with AmRose."
    stop music2 fadeout 3.0
    play sound3 sfx_distanttraffic_city2 fadein 1.5
    play voice2 mc_thinking_mmm1 noloop
    mct "I wonder if she feels the same way?"
    scene black with fade
    call sm1cs_arj001_get_arj_points from _call_sm1cs_arj001_get_arj_points
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1")
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2")
    stop sound3 fadeout 3.0
    stop sound fadeout 1.0
    jump sm1cs_arj001_exit
label sm1cs_arj001_exit:
    $ StoryController.end_scene(ARJ_STORY, 1, 0, 2, STARDUCKS, DEFAULT_SUBLOCATION, LSC_COUNTER)
    return
label sm1cs_arj001_get_arj_points:
    $ CharacterController.get_character("arj").add_point(2)
    return
label sm1cs_arj001_unlocks:
    call sm1cs_arj001_get_arj_points from _call_sm1cs_arj001_get_arj_points_1
    if config_storyline_mode is True:
        $ execute_storyline_config(ARJ_STORY)
    return