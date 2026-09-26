image sm1cs_kv-renovation-glambot-1 = Movie(play = "images/Character-Scenes/kv/s-renovation/anim/sm1cs-kv-r-a50-2x-50fps.webm", start_image = "sm1cs-kv-r-a50 kv-crouch-glambot-000_i", image = "sm1cs-kv-r-a50 kv-crouch-glambot-179_i", loop = False)
label sm1cs_kv_renovation:
    play sound sfx_heels_steps2 loop
    scene sm1cs-kv-r-02-mc-talk-kv with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey, Kanya."
    scene sm1cs-kv-r-03-kv-talk-mc with dissolve
    play voice3 kanya_hey_simple2 noloop
    kv "Sup, [mcname]?"
    stop sound fadeout 1.0
    scene sm1cs-kv-r-04-mc-talk-kv with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Not much. Just wanted a break and found myself coming here."
    scene sm1cs-kv-r-05-kv-talk-mc with dissolve
    play voice3 kanya_disappointed_oh noloop
    kv "Nice. I could use the company."
    kv "No appointments or photoshoots today and no walk-ins."
    scene sm1cs-kv-r-06-mc-talk-kv with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "So why are you here then?"
    scene sm1cs-kv-r-07-kv-talk-mc with dissolve
    play voice3 kanya_thinking_eeh1 noloop
    kv "There is always something to do for a photographer, [mcname]."
    kv "I already spend some time checking all my equipment, cleaning lenses, checking settings."
    kv "You know, the nitty-gritty."
    play sound sfx_cloth_rustling3
    scene sm1cs-kv-r-08-mc-talk-kv with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Nice."
    scene sm1cs-kv-r-09-mc-talk-kv with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "By the way, Stacy and I finally started working on fixing up the studio."
    scene sm1cs-kv-r-10-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_huh noloop
    kv "Cool. A little fast isn't it?"
    scene sm1cs-kv-r-11-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_laugh noloop
    kv "I mean we've only filmed one scene so far."
    scene sm1cs-kv-r-12-mc-talk-kv with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah, we had some extra {i}motivation{/i} to start earlier than planned."
    scene sm1cs-kv-r-13-kv-talk-mc with dissolve
    play voice3 kanya_surprised_oh noloop
    kv "Oh yeah? Someone putting the screws to you, hehe?"
    scene sm1cs-kv-r-14-mc-talk-kv with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "You could say that."
    if persistent.is_special:
        scene sm1cs-kv-r-15-mc-talk-kv with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "Melony, my mom showed up."
        scene sm1cs-kv-r-16-kv-talk-mc with dissolve
        play voice3 kanya_surprised_eeh2 noloop
        kv "Oh no."
        scene sm1cs-kv-r-17-mc-talk-kv with dissolve
        play voice2 mc_yes_yes6 noloop
        mc "Oh yes. Someone sent her a link to the first video."
    else:
        scene sm1cs-kv-r-17-mc-talk-kv with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "Melony, a close family friend, showed up. I've known her most of my life, and she's always liked to look out for me."
        mc "But she was really worked up. Someone sent her a link to the first video."
    mc "Melony hasn't realized it's Stacy and me on the tape, but she has realized I bailed on college to start making porn."
    play sound sfx_hair_scratch1
    scene sm1cs-kv-r-18-kv-talk-mc with dissolve
    play voice3 kanya_disappointed_oof noloop
    kv "Holy shit."
    scene sm1cs-kv-r-19-mc-talk-kv with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, you could say she's not a fan of my choice."
    mc "So the renovation is partly being done to make the studio into something more liveable so she stops freaking out about it."
    mc "But it's been an adjustment, having her around."
    scene sm1cs-kv-r-20-kv-talk-mc with dissolve
    play voice3 kanya_happy_relief2 noloop
    kv "Yeesh. Well, at least it's for a good cause."
    scene sm1cs-kv-r-21-mc-talk-kv with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Yup. That's what I've been trying to focus on, too."
    mc "Every improvement will help us out for the next film."
    scene sm1cs-kv-r-22-kv-talk-mc with dissolve
    play voice3 kanya_yes_yep1 noloop
    kv "Totally."
    kv "Do you need any help? I'm kind of bored here and wouldn't mind helping out the team."
    play sound sfx_hair_scratch1
    scene sm1cs-kv-r-23-mc-talk-kv with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Really? Sure. {w}We can use all the help we can get."
    scene sm1cs-kv-r-24-mc-talk-kv with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Thanks, Kanya."
    scene sm1cs-kv-r-25-kv-talk-mc with dissolve
    play voice3 kanya_yes_aga4 noloop
    kv "You got it."
    jump sm1cs_kv_renovation_at_studio
label sm1cs_kv_renovation_at_studio:
    $ renpy.music.set_volume(0.4, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music [music_elbaile_intro, music_elbaile]
    play sound sfx_door_openclosed1
    scene sm1cs-kv-r-28-renovation with Fade(0.5, 0.5, 0.5)
    pause
    play sound sfx_heels_steps2
    scene sm1cs-kv-r-29-renovation with dissolve
    queue music music_elbaile
    play voice3 kanya_surprised_wowohmy noloop
    kv "Oh wow. This place is a mess, haha."
    stop sound fadeout 1.0
    scene sm1cs-kv-r-30-kv-talk with dissolve
    play voice3 kanya_surprised_eeh2 noloop
    kv "You weren't kidding."
    scene sm1cs-kv-r-32-mc-talk-kv with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. I'm very interested in getting this job done asap."
    scene sm1cs-kv-r-33-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_laugh noloop
    kv "Sure."
    scene sm1cs-kv-r-34-kv-talk with dissolve
    play voice3 kanya_thinking_hmm4 noloop
    kv "Where are we starting?"
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1cs-kv-r-35-renovation-montage with fade
    play sound sfx_box_slide
    pause
    scene sm1cs-kv-r-36-renovation-montage with fade
    queue sound sfx_metal_fence1
    pause
    scene sm1cs-kv-r-37-renovation-montage with fade
    pause
    scene sm1cs-kv-r-38-renovation-montage with fade
    play sound sfx_bed_slide2 volume 0.7
    pause
    scene sm1cs-kv-r-39-renovation-montage with fade
    pause
    scene sm1cs-kv-r-40-renovation-montage with dissolve
    pause
    scene sm1cs-kv-r-41-renovation-montage with dissolve
    pause
    scene sm1cs-kv-r-42-renovation-montage with fade
    pause
    scene sm1cs-kv-r-43-renovation-montage with dissolve
    pause
    $ renpy.music.set_volume(0.4, 2.5, "music" )
    scene sm1cs-kv-r-44-kv-talk with fade
    play sound sfx_rope_stretch volume 0.6
    play voice3 kanya_arrogant_hm noloop
    kv "*groans* Woouah. I suddenly realized why I didn't take a job that wears out my hands."
    scene sm1cs-kv-r-45-mc-talk-kv with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Your normal job keeps your hands pretty busy."
    scene sm1cs-kv-r-46-kv-talk-mc with dissolve
    play voice3 kanya_happy_laugh1 noloop
    kv "Haha. Yeah, but after that, I'm only thinking about some hands on my shoulders."
    scene sm1cs-kv-r-47-kv-stretch with dissolve
    play voice3 kanya_happy_relief1 noloop
    kv "*sighs*"
    scene sm1cs-kv-r-48-mc-talk-kv with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "I'm sure we can work something out."
    scene sm1cs-kv-r-49-kv-talk-mc with dissolve
    play voice3 kanya_happy_laugh2 noloop
    kv "Haha. Dial it down, bud. I had an idea while we were working."
    play sound sfx_cloth_rustling2
    scene sm1cs-kv-r-a50 kv-crouch-glambot-000_i with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs_kv-renovation-glambot-1
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-kv-r-51-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_yeah noloop
    kv "We need some behind-the-scenes pics."
    scene sm1cs-kv-r-52-mc-talk-kv with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Huh?"
    play sound sfx_skirt_off2
    scene sm1cs-kv-r-53-kv-talk-mc with dissolve
    play voice3 kanya_hey_long noloop
    kv "Think about it. In probably a week or so, this whole place will look different."
    kv "We have to capture the essence of how it used to look before the studio's metamorphosis."
    scene sm1cs-kv-r-54-mc-talk-kv with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "So... you want to take pictures of the place."
    scene sm1cs-kv-r-55-kv-talk-mc with dissolve
    play voice3 kanya_no_uhuh2 noloop
    kv "Correction. I want to take pictures while {i}you{/i} work."
    kv "It will give me a break and then later on, we can build a before and after album."
    kv "I bet Stacy would love it."
    scene sm1cs-kv-r-56-mc-talk-kv with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Hey, if you're too tired, you can just chill."
    scene sm1cs-kv-r-57-kv-talk-mc with dissolve
    play voice3 kanya_no_happy noloop
    kv "I'm not. I must record, for posterity."
    play sound sfx_hair_scratch1
    scene sm1cs-kv-r-58-mc-talk-kv with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Haha. Knock yourself out."
    $ renpy.music.set_volume(1.0, 2.5, "music" )
    scene sm1cs-kv-r-59-kv-mc-ren-mon with fade
    play sound sfx_metal_fence2
    pause
    scene sm1cs-kv-r-60-kv-mc-ren-mon with fade
    play sound sfx_photocamera_flash2
    pause
    scene sm1cs-kv-r-61-kv-mc-ren-mon with dissolve
    play sound sfx_photocamera_zoom2
    pause
    scene sm1cs-kv-r-62-kv-mc-ren-mon with dissolve
    play sound sfx_photocamera_flash2
    pause
    scene sm1cs-kv-r-63-kv-mc-ren-mon with fade
    play sound sfx_photocamera_flash2
    pause
    scene sm1cs-kv-r-64-kv-mc-ren-mon with dissolve
    play sound sfx_photocamera_flash2
    pause
    scene sm1cs-kv-r-65-kv-mc-ren-mon with dissolve
    play sound sfx_photocamera_flash2
    pause
    $ renpy.music.set_volume(0.4, 2.5, "music" )
    play sound sfx_bed_slide2
    scene sm1cs-kv-r-65-mc-talk-kv with fade
    play voice2 mc_happy_oof3 noloop
    mc "Phew. Alright, break time."
    play sound sfx_fridge_closed1
    scene sm1cs-kv-r-66-kv-talk-mc with dissolve
    play sound2 sfx_heels_steps2
    play voice3 kanya_happy_laugh3 noloop
    kv "Glad you still have power to your fridge."
    scene sm1cs-kv-r-67-mc-talk-kv with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "You're a lifesaver."
    play sound2 sfx_beer_open1 noloop
    scene sm1cs-kv-r-68-mc-kv-beer with dissolve
    play sound sfx_drinking_passionately
    pause
    stop sound fadeout 1.0
    scene sm1cs-kv-r-69-kv-talk-mc with dissolve
    play voice3 kanya_thinking_eeh5 noloop
    kv "Everything is going to change once the studio is done, isn't it?"
    scene sm1cs-kv-r-70-mc-talk-kv with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Probably in some ways. But at the core it will still just be you me and Stacy trying to make this work."
    scene sm1cs-kv-r-71-kv-talk-mc with dissolve
    play voice3 kanya_happy_relief3 noloop
    kv "I like the sound of that. After the first film, I've started feeling a bit excited on the off-hours, thinking of what comes next."
    scene sm1cs-kv-r-72-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_huh noloop
    kv "And you're sure Melony won't convince you to hit pause on the studio?"
    scene sm1cs-kv-r-73-mc-talk-kv with dissolve
    play voice2 mc_no_no5 noloop
    mc "Not a chance. I haven't felt this pumped up about anything since Fetish Locator."
    mc "Melony showing up definitely surprised me, but after everything I've gone through to get here, nothing is going to stop me from continuing this."
    scene sm1cs-kv-r-74-kv-talk-mc with dissolve
    play voice3 kanya_happy_relief2 noloop
    kv "Amen to that, [mcname]."
    scene sm1cs-kv-r-75-mc-kv-beer with dissolve
    play sound sfx_drink_gulp
    pause
    play sound sfx_bed_slide3 volume 0.6
    scene sm1cs-kv-r-76-kv-talk-mc with dissolve
    play voice3 kanya_hey_simple1 noloop
    kv "I should get going. But make sure to call me when you figure out what comes next, [mcname]."
    scene sm1cs-kv-r-77-mc-talk-kv with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "You're at the top of my list, Kanya."
    scene sm1cs-kv-r-78-kv-kiss with dissolve
    play sound mc_kiss3
    kv "Mwah."
    play sound sfx_heels_steps2 loop
    scene sm1cs-kv-r-79-kv-talk-mc with dissolve
    play voice3 kanya_yes_yeah1 noloop
    kv "Until next time."
    stop sound fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    stop music fadeout 3.0
    jump sm1cs_kv_renovation_end
label sm1cs_kv_renovation_end:
    $ renovation_controller.set_progress(renovation_controller.get_renovation_scenes_progress())
    $ renovation_controller.set_daily_limit()
    $ StoryController.end_scene_without_storyline("sm1cs_kv_renovation", 2, 0, 4, STUDIO, DEFAULT_SUBLOCATION, SD_OVERVIEW)
    return