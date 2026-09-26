label sm1cs_cs001:
    $ from_scene_arj001 = False
    if player.get_storyline(ARJ_STORY) == 3:
        $ from_scene_arj001 = True
    play sound sfx_heels_steps2 loop
    play voice2 d1s1_mmm noloop volume 1.7
    mct "Wow, it looks so different in here now."
    mct "It looks nothing like Nora's place anymore..."
    stop sound fadeout 1.0
    scene sm1cs-cs001-02 mc-cs-start2_c1 with dissolve
    play voice4 girl31_angry_cough1 noloop
    cs "Ahem."
    play voice2 mc_thinking_mmm6 noloop
    mct "I actually can't believe that this is her old coffee shop. They painted, and-"
    play voice4 girl31_angry_cough2 noloop
    $ renpy.music.set_volume(0.0, 2.0, "music" )
    $ renpy.music.set_volume(0.6, 2.0, "music2" )
    scene sm1cs-cs001-02 mc-cs-start2_c2 with hpunch
    cs "{i}Ahem.{/i}"
    scene sm1cs-cs001-03 mc-cs-talk1_c1 with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Oh, sorry!"
    scene sm1cs-cs001-03 mc-cs-talk1_c2 with dissolve
    play voice4 girl37_hey_simple noloop
    cs "Welcome to Starducks, can I take your order?"
    scene sm1cs-cs001-04 mc-cs-talk2_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, I'll have a..."
    mc "Sorry, I'm just having a moment of nostalgia. Give me a second."
    scene sm1cs-cs001-04 mc-cs-talk2_c2 with dissolve
    play voice4 girl37_surprised_what noloop
    cs "Nostalgia? For what, Starducks? There's like a million of them."
    scene sm1cs-cs001-05 mc-cs-talk3_c1 with dissolve
    play voice2 d9s3_no noloop volume 1.7
    mc "No, I used to come to this coffee shop before it was a Starducks."
    scene sm1cs-cs001-05 mc-cs-talk3_c2 with dissolve
    play voice4 girl37_surprised_oh noloop
    cs "Oh yeah, some woman used to own this spot, right? It was... Nara's or something like that."
    scene sm1cs-cs001-06 mc-cs-talk4_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Nora's - yeah."
    mc "I made some good memories here..."
    scene sm1cs-cs001-06 mc-cs-talk4_c2 with dissolve
    play voice4 girl37_yes_yeah noloop
    cs "Oh yeah? Like what?"
    scene sm1cs-cs001-07 mc-cs-talk5_c1 with dissolve
    play voice2 d2s12_emmm noloop volume 1.4
    mc "Uhm, you know... Studying and... Stuff."
    scene sm1cs-cs001-07 mc-cs-talk5_c2 with dissolve
    play voice4 girl37_disappointed_aga1 noloop
    cs "Okay?... Well, are you going to order something or not?"
    scene sm1cs-cs001-08 mc-cs-talk6_c1 with dissolve
    if from_scene_arj001:
        mc "You know... now that I think about it, my friend is waiting for me back there..."
        scene sm1cs-cs001-06 mc-cs-talk4_c2 with dissolve
        play voice4 girl37_disappointed_aga2 noloop
        cs "Really now..."
        play voice2 mc_yes_yeah1 noloop
        scene sm1cs-cs001-03 mc-cs-talk1_c1 with dissolve
        mc "Yeah, I'll check with them first..."
    else:
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah, yeah. I'll have a dark roast cofee and a..."
        mc "I guess just a medium coffee."
        scene sm1cs-cs001-08 mc-cs-talk6_c2 with dissolve
        play voice4 girl37_thinking_hmm2 noloop
        cs "For the second one do you want light or dark roast?"
        scene sm1cs-cs001-08 mc-cs-talk6_c1 with dissolve
        play voice2 mc_disappointed_ehh5 noloop
        mc "Uhhh... Which one do you like?"
        play voice4 girl37_thinking_hmm1 noloop
        cs "Most people-"
        play voice2 mc_no_nono1 noloop volume 1.3
        mc "No, no. What one do {i}you{/i} like?"
        scene sm1cs-cs001-08 mc-cs-talk6_c2 with dissolve
        play voice4 girl37_thinking_emm noloop
        cs "...Me?"
        play voice2 mc_yes_yeah7 noloop
        mc "Yeah. You work here, you know what's good and what isn't."
        play voice4 girl37_arrogant_laugh noloop
        cs "Honestly, they both kind of suck. They purposefully burn the beans here, it's nasty."
        cs "But I think the light roast is better."
        scene sm1cs-cs001-09 mc-cs-talk7_c1 with dissolve
        play voice2 mc_disappointed_ah1 noloop
        mc "Cool, then I'll have that."
        play sound sfx_coffee_machine
        queue sound sfx_coffee_pouring volume 2.5
        scene sm1cs-cs001-09 mc-cs-talk7_c2 with dissolve
        play voice4 girl37_yes_yep noloop
        cs "Great, one vento light roast and one dark roast coming up."
        scene sm1cs-cs001-09 mc-cs-talk7_c1 with dissolve
        play voice2 mc_happy_a1 noloop
        mc "Thank you!"
        play voice4 girl37_disappointed_aga2 noloop
        cs "Uh huh."
    call sm1cs_cs001_discover_starducks from _call_sm1cs_cs001_discover_starducks
    return
label sm1cs_cs001_discover_starducks:
    $ player.discover_map_location(STARDUCKS)
    return