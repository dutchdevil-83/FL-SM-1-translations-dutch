image sm1cs_kv005-glambot-a75-1 = Movie(play = "images/Character-Scenes/kv/s005/anim/sm1cs-kv005-a75-3x-60fps.webm", start_image = "sm1cs-kv005-a75 kanya-glambot-000", image = "sm1cs-kv005-a75 kanya-glambot-120", loop = False)
label sm1cs_kv005i:
    scene sm1cs-kv005-01-kv-studio with dissolve
    pause
    if player.has_played_scene("sm1cs_kv005"):
        scene sm1cs-kv005-02-kv-talk-mc with dissolve
        play voice3 kanya_hey_simple2 noloop
        kv "Hey, [mcname]! Ready to keep practicing?"
        scene sm1cs-kv005-03-mc-talk-kv with dissolve
        play voice2 d9s2_yeah noloop volume 1.7
        mc "Yeah! Let's do it!"
    else:
        scene sm1cs-kv005-02-kv-talk-mc with dissolve
        play voice3 kanya_hey_simple2 noloop
        kv "Oh hey, [mcname]."
        scene sm1cs-kv005-03-mc-talk-kv with dissolve
        play voice2 mc_hey_hey8 noloop
        mc "What's up, Kanya!"
        scene sm1cs-kv005-04-kv-talk-mc with dissolve
        play voice3 kanya_happy_relief2 noloop
        kv "I was actually hoping you'd stop by, I actually had something I wanted to run by you."
        scene sm1cs-kv005-05-mc-talk-kv with dissolve
        play voice2 mc_yes_yeah7 noloop
        mc "Oh yeah?"
        scene sm1cs-kv005-08-kv-talk-mc with dissolve
        play voice3 kanya_yes_yep2 noloop
        kv "Yep! I want you to do another photo shoot."
        scene sm1cs-kv005-09-mc-talk-kv with dissolve
        play voice2 mc_surprised_oh1 noloop
        mc "Oh? With who?"
        play voice3 kanya_happy_laugh1 noloop
        kv "Me!"
    jump sm1cs_kv005
label sm1cs_kv005:
    if not player.has_played_scene("sm1cs_kv005_start"):
        jump sm1cs_kv005_start
    else:
        jump sm1cs_kv005_continue
label sm1cs_kv005_start:
    scene sm1cs-kv005-04-kv-talk-mc with dissolve
    play voice3 kanya_thinking_eeh1 noloop
    kv "Is that cool with you?"
    scene sm1cs-kv005-05-mc-talk-kv with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "You want me to... take photos of you?"
    scene sm1cs-kv005-06-kv-talk-mc with dissolve
    play voice3 kanya_yes_yeah2 noloop
    kv "Yeah. Me."
    play voice2 mc_happy_thatsgood noloop
    scene sm1cs-kv005-07-mc-talk-kv with dissolve
    stop voice2 fadeout 0.45
    mc "That's... Not what I was expecting."
    scene sm1cs-kv005-08-kv-talk-mc with dissolve
    play voice3 kanya_surprised_huh2 noloop
    kv "What, am I not good enough to be in front of the camera, [mcname]?!"
    scene sm1cs-kv005-09-mc-talk-kv with dissolve
    play voice2 d1s5b_emmm noloop volume 1.7
    mc "No! Wait - I mean, yes! I, uhm, I meant-"
    scene sm1cs-kv005-10-kv-talk-mc with dissolve
    play voice3 kanya_happy_laugh2 noloop
    kv "Just fucking with you. I know I'm hot."
    scene sm1cs-kv005-11-mc-talk-kv with dissolve
    play voice2 mc_happy_oof2 noloop
    mc "God, I almost had a heart attack."
    mc "I was just trying to say that I was expecting there to be a model, and you with me behind the camera."
    scene sm1cs-kv005-12-kv-talk-mc with dissolve
    play voice3 kanya_yes_aga4 noloop
    kv "I know, but I figured we'd mix it up a bit."
    kv "Besides, this will be a real solid test of your skills, [mcname]."
    kv "And you don't have to worry too much about me not mentoring you. Even in front of the camera I can still tell you what to do."
    play sound sfx_cloth_rustling2
    scene sm1cs-kv005-13-mc-talk-kv with dissolve
    play sound2 sfx_heels_steps2
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "I'm not surprised by that.{w} Where are you going?"
    scene sm1cs-kv005-14-kv-talk-mc with dissolve
    play voice3 kanya_disappointed_oh noloop
    kv "To change!"
    $ renpy.music.set_volume(0.6, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 4.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 4.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 4.0, "freeroam_sound2" )
    play music "<silence 3.0>" noloop
    stop sound2 fadeout 1.0
    scene sm1cs-kv005-15-mc-inner-talk with dissolve
    queue music music_synthpop_sunset fadein 1.5
    play voice2 d1s1_mmm noloop volume 1.5
    mct "Fuck... Am I ready for this? I don't think I'm ready for this..."
    scene sm1cs-kv005-16-mc-inner-talk with dissolve
    mct "But... I don't think Kanya is going to give me a choice..."
    play sound sfx_barefoot_steps1
    scene sm1cs-kv005-17-mc-inner-talk with dissolve
    play voice2 d14s16_smell noloop
    mct "Here we go..."
    scene sm1cs-kv005-18-mc-talk-kv with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh shit."
    scene sm1cs-kv005-19-kv-talk-mc with dissolve
    play voice3 kanya_yes_yeah5 noloop
    kv "Yeah?"
    stop sound fadeout 1.0
    scene sm1cs-kv005-20-mc-talk-kv with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, I was expecting you to be more... Naked."
    scene sm1cs-kv005-21-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_huh noloop
    kv "Yeah, you dirty perv? Every woman in your life just ready to throw her panties at you?"
    play voice2 d2s9_confused noloop volume 1.8
    mc "Well, uhm..."
    kv "Don't worry, stud. We'll get there. But, not every photoshoot is in latex or the nude! So I thought we'd start there."
    scene sm1cs-kv005-22-mc-talk-kv with dissolve
    play voice2 mc_yes_okay3 noloop volume 1.7
    mc "Fair enough."
    scene sm1cs-kv005-23-kv-talk-mc with dissolve
    play voice3 kanya_happy_laugh3 noloop
    kv "Enough chit chat! Let's get to the shoot!"
    scene sm1cs-kv005-24-mc-talk-kv with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.8
    mc "All right... Here goes nothing."
    play voice3 kanya_thinking_hmm1 noloop
    kv "Don't you mean everything?"
    mc "Maybe..."
    scene sm1cs-kv005-25-mc-shot with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-26-mc-shot with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-27-mc-shot with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-28-kv-talk-mc with dissolve
    play voice3 kanya_thinking_eeh3 noloop
    kv "You know, a little bit of conversation is good while doing a photo shoot."
    scene sm1cs-kv005-29-mc-talk-kv with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "But I'm concentrating."
    scene sm1cs-kv005-31-kv-talk-mc with dissolve
    play voice3 kanya_yes_yeah3 noloop
    kv "Yeah, but do you like someone just staring at you and not saying anything?"
    play sound sfx_photocamera_zoom1
    scene sm1cs-kv005-30-mc-talk-kv with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "...{w}You've got a point there. Fine."
    mc "Uhm, so... How did you get into photography?"
    scene sm1cs-kv005-31-kv-talk-mc with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    play voice3 kanya_disappointed_ohh noloop
    kv "Oh boy, starting out with a doozy! Well..."
    kv "A few years ago I was hanging out with a friend, and she had this clunky old camera.{w} We started goofing around with it, and just snapping random photos of each other."
    scene sm1cs-kv005-33-kv-talk-mc with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    play voice3 kanya_thinking_hmm3 noloop
    kv "The longer we did it though, the more and more I started taking all the pictures. I started to realize that I really, really liked taking photos."
    kv "My friend wasn't using the camera, so I borrowed it and started taking more and more photos. I swear, I didn't sleep for a week.{w} I just ran around snapping shots of everything and anything."
    scene sm1cs-kv005-32-kv-talk-mc with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    play voice3 kanya_arrogant_ha noloop
    kv "I showed a photo teacher what I was doing, and they said I showed promise. They gave me a few pointers, and from there I just started to grow more and more as a photographer."
    kv "All right, I think that's enough of the fully clothed stuff. You ready to move onto something new?"
    $ player.completion_log_add_item_date("sm1cs_kv005_start")
    if player.get_topic(TOPIC_PHOTOGRAPHY) > 7:
        scene sm1cs-kv005-35-mc-talk-kv with dissolve
        play voice2 mc_yes_yeah4 noloop
        mc "Yeah, I think so. Not sure what else we'd want in this outfit."
        scene sm1cs-kv005-36-kv-talk-mc with dissolve
        play voice3 kanya_yes_long noloop
        kv "Exactly what my instincts were saying. Let me go change real quick."
        play sound sfx_barefoot_steps1
        scene sm1cs-kv005-37-kv-walk with dissolve
        pause
        jump sm1cs_kv005_part_2
    else:
        scene sm1cs-kv005-35-mc-talk-kv with dissolve
        play voice2 mc_disappointed_ah2 noloop
        mc "Uhhhh..."
        scene sm1cs-kv005-34-kv-talk-mc with dissolve
        play voice3 kanya_angry_hm noloop
        kv "Running out of ideas?"
        scene sm1cs-kv005-35-mc-talk-kv with dissolve
        play voice2 mc_yes_yeah9 noloop
        mc "Maybe."
        play sound sfx_barefoot_steps1
        scene sm1cs-kv005-36-kv-talk-mc with dissolve
        play voice3 kanya_sex_closedmoan5 noloop
        kv "Hang on, let me go change. This shirt is too tight for me to think straight."
        scene sm1cs-kv005-37-kv-walk with dissolve
        pause
        stop sound fadeout 1.0
        stop music fadeout 3.0
        $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
        $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
        $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
        $ player.add_topic(TOPIC_PHOTOGRAPHY, 2)
        jump sm1cs_kv005_come_back_later
label sm1cs_kv005_part_2:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    stop music fadeout 3.0
    queue sound sfx_barefoot_steps1
    scene sm1cs-kv005-38-kv-lingerie with Fade(0.5, 0.5, 0.5)
    queue music music_synthpop_arcade fadein 1.5
    pause
    scene sm1cs-kv005-39-mc-talk-kv with dissolve
    play voice2 mc_surprised_ohmy noloop
    mc "Holy..."
    scene sm1cs-kv005-40-kv-talk-mc with dissolve
    play voice3 kanya_happy_laugh4 noloop
    kv "I figured you'd like this one."
    scene sm1cs-kv005-41-mc-talk-kv with dissolve
    play voice2 mc_yes_yes6 noloop
    mc "Oh, {i}I love it.{/i}"
    stop sound fadeout 1.0
    scene sm1cs-kv005-42-kv-talk-mc with dissolve
    play voice3 kanya_disappointed_oof noloop
    kv "Good. It's got a little more lace than I'm used to, but I figured I'd try out something different, see how it went."
    scene sm1cs-kv005-43-mc-talk-kv with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "I think this is the only thing you should wear from now on."
    scene sm1cs-kv005-44-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_yeah noloop
    kv "Oh yeah? Not a fan of the leather anymore, [mcname]?"
    scene sm1cs-kv005-45-mc-talk-kv with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "I didn't say that. You just look super hot in that lingerie."
    scene sm1cs-kv005-46-kv-talk-mc with dissolve
    play voice3 kanya_happy_relief3 noloop
    kv "Well, thank you, [mcname]."
    kv "We can go on all day about how good I look, but we have photos to take."
    scene sm1cs-kv005-47-mc-talk-kv with dissolve
    play voice2 mc_surprised_oh2 noloop
    mc "Oh yeah, uhm..."
    scene sm1cs-kv005-48-kv-talk-mc with dissolve
    play voice3 kanya_thinking_hmm2 noloop
    kv "Want a pro tip for working with models in lingerie, or in the nude?"
    scene sm1cs-kv005-43-mc-talk-kv with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, that would be awesome."
    scene sm1cs-kv005-42-kv-talk-mc with dissolve
    play voice3 kanya_thinking_eeh5 noloop
    kv "Pretend they're not naked."
    scene sm1cs-kv005-45-mc-talk-kv with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "...What?"
    scene sm1cs-kv005-46-kv-talk-mc with dissolve
    play voice3 kanya_thinking_eeh2 noloop
    kv "Most of the times you've seen lingerie, or naked women, you've been about to sleep with them, right?"
    scene sm1cs-kv005-47-mc-talk-kv with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "I mean... yeah."
    scene sm1cs-kv005-48-kv-talk-mc with dissolve
    play voice3 kanya_yes_yep1 noloop
    kv "But, here you need to at least photograph them first."
    scene sm1cs-kv005-44-kv-talk-mc with dissolve
    play voice3 kanya_sex_closedmoan1 noloop
    kv "My trick, when I'm behind the camera, is to think 'what kind of photos do I think look sexy as hell'. Then I try to do that."
    kv "So while we're shooting, maybe think something like 'if I was going to ask for a sexy photo of a chick, what would I want it to look like?'"
    scene sm1cs-kv005-59-mc-talk-kv with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "Huh... That's a good trick! Okay-"
    scene sm1cs-kv005-49-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mct "Let's see... What kind of sexy photo would I want of Kanya..."
    play sound sfx_photocamera_zoom2
    scene sm1cs-kv005-50-mc-talk-kv with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "So, uhm... How did you get started with the BDSM model photography?"
    scene sm1cs-kv005-44-kv-talk-mc with dissolve
    play voice3 kanya_happy_relief1 noloop
    kv "Well, I started doing model photos with whoever I could. Friends, random baristas, people on the street."
    kv "I ended up meeting this chick who was super hot that was really excited about getting in front of the camera."
    scene sm1cs-kv005-51-kv-talk-mc with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    kv "When she showed up for the shoot, she had all of these latex outfits. I thought they were awesome, so the whole shoot turned into a light BDSM modeling thing."
    kv "She showed her friends some of the photos. They wanted to do their own shoot, so she connected us."
    scene sm1cs-kv005-52-kv-talk-mc with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    play voice3 kanya_happy_laugh1 noloop
    kv "Next thing you know, every model coming through the door wanted to do a BDSM shoot."
    kv "After like the fifth person, I started asking for them to pay for their shoots. Everyone agreed in a heartbeat."
    scene sm1cs-kv005-53-kv-talk-mc with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    play voice3 kanya_thinking_hmm1 noloop
    kv "And next thing you know, I've got enough to rent a real studio."
    kv "Bought more cameras, some lights, got a good website. Just stumbled into a whole career of being a BDSM model photographer."
    play sound sfx_photocamera_zoom3
    scene sm1cs-kv005-54-mc-talk-kv with dissolve
    play voice2 d1s2_hmm noloop volume 1.7
    mc "Where'd you shoot before you rented the studio here?"
    scene sm1cs-kv005-55-kv-talk-mc with dissolve
    play voice3 kanya_disappointed_oh noloop
    kv "Literally anywhere I could. I got kicked out of Theomalt Park once for doing a shoot there!"
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-56-kv-talk-mc with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "God, I can't even imagine the look on that cop's face."
    play voice3 kanya_arrogant_laugh noloop
    kv "Oh, it was {i}priceless{/i}."
    scene sm1cs-kv005-55-01-kv-talk-mc with dissolve
    kv "You ever heard of Robert Capa?"
    play sound sfx_photocamera_zoom4
    scene sm1cs-kv005-55-02-mc-talk-kv with dissolve
    play voice2 mc_no_no10 noloop
    mc "Uhhh... No."
    scene sm1cs-kv005-55-03-kv-talk-mc with dissolve
    play voice3 kanya_thinking_hmm3 noloop
    kv "'If your pictures aren't good enough, you're not close enough.'"
    scene sm1cs-kv005-55-04-mc-talk-kv with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, that's a pretty good tip."
    scene sm1cs-kv005-55-01-kv-talk-mc with dissolve
    kv "Uh huh. Next lesson is to vary your shots a bit. Come and take some close ups, get some cowboys, mediums, whatever. Full body shots are great, but variety is the spice of life."
    scene sm1cs-kv005-57-mc-talk-kv with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "What the hell is a cowboy?"
    scene sm1cs-kv005-58-kv-talk-mc with dissolve
    play voice3 kanya_disappointed_hm noloop
    kv "Shot from the knees up."
    scene sm1cs-kv005-59-mc-talk-kv with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh...{w} Okay, time to mix it up a bit then."
    scene sm1cs-kv005-60-mc-kv with dissolve
    pause
    play sound sfx_photocamera_zoom2
    scene sm1cs-kv005-61-kv-talk-mc with dissolve
    play voice3 kanya_yes_yeah4 noloop
    kv "See? A little bit of variety is a good thing."
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-62-mc-talk-kv with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "You're not wrong..."
    scene sm1cs-kv005-63-mc-inner-talk with dissolve
    play voice2 mc_angry_errr6 noloop
    mct "God... Kanya has some great tits..."
    scene sm1cs-kv005-64-kv-talk-mc with dissolve
    play voice3 kanya_hey_arrogant noloop
    kv "You just going to stare at them? Or are you going to take a picture?"
    play sound sfx_photocamera_zoom1
    scene sm1cs-kv005-65-mc-talk-kv with dissolve
    play voice2 mc_pain_ou1 noloop
    mc "Oh, I, uh..."
    scene sm1cs-kv005-66-kv-talk-mc with dissolve
    play voice3 kanya_disappointed_eeh noloop
    kv "[mcname], I put this on and walked out in front of the camera. I {i}know{/i} my tits look good. I want them to be photographed."
    play voice2 mc_yes_yeah6 noloop
    mc "Yeah, didn't even think of that."
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-67-kv-talk-mc with dissolve
    play voice3 kanya_hey_long noloop
    kv "Remember, I walked out in a sexy outfit. I want you to make me {i}look sexy{/i} in it."
    kv "And we can even embellish a little bit. Give me that slightly bigger cup size I've always wanted."
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-65-mc-talk-kv with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Are you kidding me, Kanya? Your tits are already great!"
    play voice3 kanya_happy_yeah noloop
    kv "Good! That's exactly what a model wants to hear."
    play sound sfx_photocamera_zoom2
    scene sm1cs-kv005-68-mc-talk-kv with dissolve
    play voice2 mc_surprised_huh6 noloop
    mc "Huh?"
    scene sm1cs-kv005-51-kv-talk-mc with dissolve
    play voice3 kanya_thinking_eeh4 noloop
    kv "Every model has some insecurity. Some flaw, something they'd want to change."
    kv "You, as the photographer, need to reassure them that even with their flaws, they're hot enough to be in front of the camera."
    scene sm1cs-kv005-69-kv-talk-mc with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    play voice2 mc_surprised_wow3 noloop
    mc "Wow. I'm glad that's one lesson I already had figured out."
    play voice3 kanya_thinking_hmm4 noloop
    kv "How are you feeling about these shots?"
    play sound sfx_remote_button1 volume 1.6
    scene sm1cs-kv005-70-mc-talk-kv with dissolve
    play voice2 mc_happy_a1 noloop volume 1.7
    mc "Good! I definitely think we've got some good stuff."
    play voice3 kanya_happy_laugh3 noloop
    kv "Great, in that case, you ready to move on?"
    $ player.completion_log_add_item_date("sm1cs_kv005_part_2")
    if player.get_topic(TOPIC_PHOTOGRAPHY) > 9:
        mc "Yeah!"
        scene sm1cs-kv005-72-kv-talk-mc with dissolve
        play voice3 kanya_yes_aga1 noloop
        kv "Great! I have one more outfit for you."
        play sound sfx_barefoot_steps1
        scene sm1cs-kv005-73-mc-inner-talk with dissolve
        pause
        jump sm1cs_kv005_part_3
    else:
        mc "Uhm... I'm trying to think of what else we could do..."
        scene sm1cs-kv005-72-kv-talk-mc with dissolve
        play voice3 kanya_thinking_hmm2 noloop
        kv "Hang on, let me go get some clothes on. It's a bit nippy in here."
        play sound sfx_barefoot_steps1
        scene sm1cs-kv005-73-mc-inner-talk with dissolve
        pause
        stop sound fadeout 2.0
        stop music fadeout 3.0
        $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
        $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
        $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
        $ player.add_topic(TOPIC_PHOTOGRAPHY, 2)
        jump sm1cs_kv005_come_back_later
label sm1cs_kv005_part_3:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    stop music fadeout 3.0
    stop sound fadeout 1.0
    scene sm1cs-kv005-16-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mct "All right, let's see if I can make some photo magic!"
    scene sm1cs-kv005-a75 kanya-glambot-000 with Fade(0.5, 0.5, 0.5)
    queue music music_synthpop_funkydunk
    pause
    play sound sfx_camera_fly1 volume 2.0
    play sound2 ["<silence 2.0>", sfx_camera_fly1] volume 2.0
    scene sm1cs_kv005-glambot-a75-1
    pause
    play voice3 kanya_happy_wooh noloop
    kv "Tada - the last outfit of our practice session!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-kv005-75-mc-inner-talk with dissolve
    play voice2 mc_angry_errr7 noloop
    mct "Oh fuck... How am I supposed to concentrate when she's totally naked!?"
    scene sm1cs-kv005-75-01-kv-talk-mc with dissolve
    play voice3 kanya_surprised_eeh2 noloop
    kv "What's the matter, [mcname], cat got your tongue?"
    scene sm1cs-kv005-75-02-mc-talk-kv with dissolve
    play voice2 d2s12_emmm noloop volume 1.5
    mc "Uhm... well, no... but... You know."
    scene sm1cs-kv005-75-03-kv-talk-mc with dissolve
    kv "Come on, you've already seen me naked. This is nothing new."
    scene sm1cs-kv005-75-04-mc-talk-kv with dissolve
    mc "Yeah, but you're still hot."
    play sound sfx_barefoot_steps1
    scene sm1cs-kv005-76-kv-talk-mc with dissolve
    play voice3 kanya_disappointed_oof noloop
    kv "Oh, you flatterer you. Come on, we have photos to take!"
    scene sm1cs-kv005-77-mc-talk-kv with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "Yes, we do."
    play sound sfx_photocamera_zoom1
    scene sm1cs-kv005-78-mc-inner-talk with dissolve
    play voice2 mc_angry_errr4 noloop
    mct "I have no idea how I'm going to do this with a boner... But here we go."
    scene sm1cs-kv005-79-mc-kv with dissolve
    pause
    scene sm1cs-kv005-80-kv-talk-mc with dissolve
    play voice3 kanya_happy_relief2 noloop
    kv "There we go! Something a little different from everything else!"
    play sound sfx_photocamera_flash2
    "*CLICK*"
    kv "You're a quick learner, [mcname]."
    play sound sfx_photocamera_zoom4
    scene sm1cs-kv005-81-mc-talk-kv with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mc "Well, I've got a great teacher."
    scene sm1cs-kv005-82-kv-talk-mc with dissolve
    play voice3 kanya_happy_laugh2 noloop
    kv "Do you think flirting with me during the shoot will make me go easy on you?"
    scene sm1cs-kv005-83-mc-talk-kv with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "...Maybe."
    scene sm1cs-kv005-84-kv-talk-mc with dissolve
    play sound sfx_photocamera_flash2
    "*CLICK*"
    play voice3 kanya_no_nah2 noloop
    kv "I think you may have to try a little harder than that."
    play voice2 mc_yes_yeah5 noloop
    mc "If you say so, Professor Vu."
    scene sm1cs-kv005-84-01-kv-talk-mc with dissolve
    play voice3 kanya_surprised_ohmy noloop
    kv "Ooooo, I like that. You might have to call me that more from now on."
    kv "Wait! I just had an idea, I want you to stand up straight, and look down at me with the camera."
    scene sm1cs-kv005-84-02-mc-talk-kv with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Kind of like a top down?"
    scene sm1cs-kv005-84-03-kv-talk-mc with dissolve
    play voice3 kanya_yes_yep3 noloop
    kv "Yep! But more point of view."
    kv "I bet this looks super hot, doesn't it."
    play sound sfx_photocamera_flash2
    scene sm1cs-kv005-84-05-kv-talk-mc with dissolve
    "*CLICK*"
    scene sm1cs-kv005-84-04-mc-talk-kv with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Does that answer your question?"
    play sound sfx_cloth_rustling4 volume 2.0
    scene sm1cs-kv005-85-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_laugh noloop
    kv "I bet it looks kind of like I'm about to suck your dick, huh."
    scene sm1cs-kv005-86-mc-talk-kv with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Yep. It definitely does."
    scene sm1cs-kv005-87-kv-talk-mc with dissolve
    play voice3 kanya_angry_breathing noloop
    kv "And it's so close to my face... I can see you just bursting at the seams."
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-88-mc-inner-talk with dissolve
    play voice2 d1s5_orgasm noloop
    mct "Jesus..."
    scene sm1cs-kv005-89-kv-talk-mc with dissolve
    play voice3 kanya_sex_closedmoan2 noloop
    kv "I bet you're picturing it right now. Your hard cock on my lips..."
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-90-kv-talk-mc with dissolve
    play voice3 kanya_angry_errr1 noloop
    kv "Your dick, disappearing down my throat. My wet tongue gliding under your shaft as you thrust your cock in and out of my mouth..."
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-91-kv-talk-mc with dissolve
    play voice3 kanya_surprised_eeh1 noloop
    kv "You know, you're not the only one that gets turned on during a shoot. Just look at how much my pussy is begging for you to fuck it."
    kv "Wet and warm and {i}tight{/i}... Waiting for you to fuck me, [mcname]."
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-92-kv-talk-mc with dissolve
    play voice3 kanya_thinking_hmm1 noloop
    kv "Mmmmm, make sure to get some photos of my {i}good side{/i}."
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-93-kv-talk-mc with dissolve
    play voice3 kanya_hey_attention noloop
    kv "Tell me, [mcname], what's going through your head right now?"
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-94-mc-talk-kv with dissolve
    play voice2 mc_angry_errr2 noloop
    mc "I have no idea why I'm still taking photos when I should be fucking you."
    scene sm1cs-kv005-95-kv-talk-mc with dissolve
    play voice3 kanya_happy_laugh4 noloop
    kv "Because, I'm teaching you how to be a {i}professional{/i}. And professionals wait until at least after the shoot for their treat."
    play sound sfx_photocamera_flash2
    "*CLICK*"
    scene sm1cs-kv005-96-mc-inner-talk with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "Christ, I might just cum from taking these photos!"
    scene sm1cs-kv005-97-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_huh noloop
    kv "How do those look?"
    play sound sfx_remote_button1 volume 2.0
    scene sm1cs-kv005-98-mc-talk-kv with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "Uhm... I'd say pretty good!"
    play sound sfx_cloth_rustling1
    scene sm1cs-kv005-99-kv-talk-mc with dissolve
    play voice3 kanya_angry_hm noloop
    kv "Let me see."
    scene sm1cs-kv005-100-mc-talk-kv with dissolve
    pause
    scene sm1cs-kv005-101-kv-talk-mc with dissolve
    play voice3 kanya_surprised_wowohmy noloop
    kv "Wow, [mcname], these look great!"
    scene sm1cs-kv005-102-mc-talk-kv with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "You think so?"
    scene sm1cs-kv005-103-kv-talk-mc with dissolve
    play voice3 kanya_yes_yeah2 noloop
    kv "Yeah. You've shown a lot of improvement since our first shoot. I'm impressed, seriously."
    scene sm1cs-kv005-104-mc-talk-kv with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Like I said, I've got a great teacher."
    scene sm1cs-kv005-104-01-kv-talk-mc with dissolve
    kv "That, and a little bit of talent."
    kv "A little bit more work, and I might have to be worried!"
    scene sm1cs-kv005-104-02-mc-talk-kv with dissolve
    play voice2 mc_happy_hah2 noloop
    mc "Yeah? Afraid I might start poaching your clients?"
    scene sm1cs-kv005-104-03-kv-talk-mc with dissolve
    play voice3 kanya_arrogant_pff noloop
    kv "Please. They all love me too much. But you might be able to scoop up all the new models."
    kv "But, speaking of clients, I have one coming in so I have to kick you out."
    scene sm1cs-kv005-104-04-mc-talk-kv with dissolve
    play voice2 mc_surprised_what8 noloop
    mc "All that teasing, and you're kicking me out!"
    scene sm1cs-kv005-105-kv-talk-mc with dissolve
    play voice3 kanya_no_happy noloop
    kv "Don't worry stud, there will be plenty more fucking in our future."
    kv "I have to throw some clothes on and get ready, you know how to get out!"
    play voice2 mc_yes_yeah3 noloop
    mc "Yeah, I do..."
    play sound sfx_barefoot_steps1
    scene sm1cs-kv005-106-kv-talk-mc with dissolve
    play voice3 kanya_yes_yep2 noloop
    kv "I'll see you soon, [mcname]!"
    scene sm1cs-kv005-107-mc-talk-kv with dissolve
    play voice2 mc_hey_bye1 noloop
    $ player.add_topic(TOPIC_PHOTOGRAPHY, 2)
    mc "See ya' soon, Kanya!"
    stop sound fadeout 1.0
    stop music fadeout 3.0
    jump sm1cs_kv005_fullexit
label sm1cs_kv005_continue:
    if player.has_played_scene("sm1cs_kv005_start") and player.get_topic(TOPIC_PHOTOGRAPHY) > 7:
        play voice2 mc_yes_yes7 noloop
        mc "I am! Did some reading and I'm good to go."
        scene sm1cs-kv005-04-kv-talk-mc with dissolve
        play voice3 kanya_happy_woohoo noloop
        kv "Great! Why don't you grab the camera and I'll go change!"
    if player.has_played_scene("sm1cs_kv005_part02") and player.get_topic(TOPIC_PHOTOGRAPHY) > 10:
        $ renpy.music.set_volume(0.8, 0.5, "music" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
        jump sm1cs_kv005_part_3
    elif player.has_played_scene("sm1cs_kv005_start") and player.get_topic(TOPIC_PHOTOGRAPHY) > 7:
        $ renpy.music.set_volume(0.8, 0.5, "music" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
        $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
        jump sm1cs_kv005_part_2
    else:
        jump sm1cs_kv005_come_back_later
label sm1cs_kv005_come_back_later:
    scene sm1cs-kv005-110-kv-talk-mc with dissolve
    play voice3 kanya_disappointed_neh noloop
    kv "Still nothing?"
    scene sm1cs-kv005-111-mc-talk-kv with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Uhhhhh..."
    play voice3 kanya_thinking_hmm4 noloop
    kv "That's okay, all part of the learning process. Why don't you go read up a little bit, and come back later?"
    mc "You sure?"
    scene sm1cs-kv005-110-kv-talk-mc with dissolve
    play voice3 kanya_yes_yeah1 noloop
    kv "Yeah. We have plenty of time."
    play sound sfx_cloth_rustling1
    scene sm1cs-kv005-112-mc-talk-kv with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "All right."
    play sound sfx_remote_button1 volume 1.5
    scene sm1cs-kv005-113-kv-talk-mc with dissolve
    play voice3 kanya_surprised_wow noloop
    kv "So far things are looking great though!"
    scene sm1cs-kv005-114-mc-talk-kv with dissolve
    play voice2 mc_angry_really noloop
    mc "Really?"
    scene sm1cs-kv005-115-kv-talk-mc with dissolve
    play voice3 kanya_yes_aga3 noloop
    kv "Really really."
    scene sm1cs-kv005-116-mc-talk-kv with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Awesome."
    mc "Don't worry, I'll be back!"
    scene sm1cs-kv005-117-kv-talk-mc with dissolve
    play voice3 kanya_yes_long noloop
    kv "I'm looking forward to it, [mcname]."
    jump sm1cs_kv005_partial_exit
label sm1cs_kv005_no_loss_exit:
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene_without_progressing(KV_STORY)
    return
label sm1cs_kv005_partial_exit:
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene_without_progressing(KV_STORY, 1, 30, 2)
    return
label sm1cs_kv005_fullexit:
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(KV_STORY, 3, 0, 3)
    return