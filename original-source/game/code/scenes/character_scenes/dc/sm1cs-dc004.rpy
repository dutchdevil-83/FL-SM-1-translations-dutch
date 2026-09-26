label sm1cs_dc004:
    $ renpy.music.set_volume(0.6, 3.0, "freeroam_music1" )
    scene sm1sc-dc004-01 mc-dc-park1_c2 with fade
    play voice3 girl36_yes_yeah noloop
    dc "Yeah, I'm just busy... walking my beat and all."
    scene sm1sc-dc004-02 mc-dc-park2_c1 with dissolve
    play voice2 d1s5_mchappy noloop
    mc "There's still that pervert running around, right?"
    scene sm1sc-dc004-02 mc-dc-park2_c2 with dissolve
    play voice3 girl36_yes_yep noloop
    dc "Yep. He's still running around out here, bare dicked and crazy."
    scene sm1sc-dc004-03 mc-dc-park3_c1 with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Never heard a cop say 'bare-dicked' before!"
    scene sm1sc-dc004-03 mc-dc-park3_c2 with dissolve
    play voice3 girl36_disappointed_geh noloop
    dc "Shit... I shouldn't talk like that while I'm working."
    scene sm1sc-dc004-03 mc-dc-park3_c1 with dissolve
    play voice2 mc_no_nono1 noloop
    mc "No, no. It's fine! I think it's fun."
    play voice3 girl36_thinking_hmm noloop
    dc "Yeah..."
    play voice2 mc_surprised_oh1 noloop
    mc "But I wanted to ask you something. The other day, at coffe, you kind of ran off in a hurry. Is something wrong? Did I say something wrong?"
    play sound sfx_sport_run1 loop
    scene sm1sc-dc004-03 mc-dc-park3_c2 with dissolve
    play voice3 girl36_no_happy noloop
    dc "No, I-"
    scene sm1sc-dc004-04 mc-dc-park4_c1 with dissolve
    pause
    scene sm1sc-dc004-04 mc-dc-park4_c2 with dissolve
    play voice3 girl36_disappointed_aah noloop
    dc "I can't really talk right now... uhm, come back... later? Or something, I don't know."
    scene sm1sc-dc004-05 mc-dc-park5_c1 with dissolve
    pause
    stop sound fadeout 3.0
    scene sm1sc-dc004-05 mc-dc-park5_c2 with dissolve
    play voice3 girl36_disappointed_oh noloop
    dc "Because she is, uhm, running too fast. And I need to give her a ticket."
    play sound sfx_heels_run2 loop
    scene sm1sc-dc004-06 mc-dc-park6_c1 with dissolve
    play voice3 girl36_hey_happy noloop
    dc "Ma'am! Excuse me, ma'am!"
    scene sm1sc-dc004-06 mc-dc-park6_c2 with dissolve
    pause
    stop sound fadeout 4.0
    scene sm1sc-dc004-07 mc-dc-park7_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "That was still... weird. I hope she's okay."
    play sound2 sfx_heels_steps2
    scene sm1sc-dc004-07 mc-dc-park7_c2 with dissolve
    mct "I guess all I can do is try and talk to her later..."
    stop sound2 fadeout 1.0
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    jump sm1cs_dc004_end
label sm1cs_dc004_end:
    $ StoryController.end_scene(DC_STORY, 0, 15, 0, PARK, DEFAULT_SUBLOCATION, LPA_CENTER)
    return