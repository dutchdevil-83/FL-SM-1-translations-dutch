image sm1cs_mh008-glambot-1 = Movie(play = "images/Character-Scenes/mh/s008/anim/sm1cs-mh008-a06-4x-60fps.webm", start_image = "sm1cs-mh008-a06 mh-couch-glambot-00", image = "sm1cs-mh008-a06 mh-couch-glambot-89", loop = False)
label sm1cs_mh008:
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 3.0, "freeroam_sound2" )
    scene sm1cs-mh008-01-mh-book with dissolve
    play music music_esthetic_life volume 0.8
    pause
    play sound sfx_door_closed1
    scene sm1cs-mh008-02-mc-talk with dissolve
    play voice2 mc_hey_hey5 noloop
    mc "Lyssa? You home?"
    scene sm1cs-mh008-03-mh-talk-mc with dissolve
    play voice3 dahlia_yes_yeah2 noloop
    mh "Yep! I'm in here, [mcname]."
    play sound sfx_heels_steps1
    scene sm1cs-mh008-04-mh-talk-mc with dissolve
    stop sound fadeout 1.0
    play voice3 dahlia_thinking_mmm2 noloop
    mh "One second..."
    play sound sfx_paper_rustl1
    scene sm1cs-mh008-05-mh-book with dissolve
    mh "..."
    scene sm1cs-mh008-a06 mh-couch-glambot-00 with dissolve
    pause 0.01
    play sound ["<silence 2.0>", sfx_camera_fly1]
    play sound2 sfx_camera_fly1 volume 2.0 noloop
    scene sm1cs_mh008-glambot-1
    play voice3 lissa_thinking2 noloop volume 1.4
    mh "Sorry, just needed to finish that brief."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh008-07-mc-talk-mh with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "No worries, Lyssa."
    play sound sfx_cloth_rustling4 volume 2.0
    scene sm1cs-mh008-08-mc-couch with dissolve
    pause
    scene sm1cs-mh008-09-mc-talk-mh with dissolve
    play voice2 d1s2_hmm noloop volume 1.5
    mc "Why did you want to see me?"
    scene sm1cs-mh008-10-mc-talk-mh with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "I don't know... it's been awhile since we've really spent time together. I thought we could maybe do something, go somewhere."
    scene sm1cs-mh008-11-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Of course, Lyssa! I'd love to."
    play sound sfx_cloth_rustling1
    scene sm1cs-mh008-12-mh-talk-mc with dissolve
    play voice3 lissa_haha noloop
    mh "That's what I was hoping you'd say."
    scene sm1cs-mh008-13-mc-talk-mh with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Do you have anything in mind?"
    scene sm1cs-mh008-14-mh-talk-mc with dissolve
    play voice3 dahlia_no_nope noloop
    mh "Nope. I was trusting in your spontaneity to come up with something exciting for the two of us to do."
    scene sm1cs-mh008-15-mc-talk-mh with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mc "Hmmm..."
    scene sm1cs-mh008-16-mh-talk-mc with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh, I like that look."
    scene sm1cs-mh008-17-mc-talk-mh with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "How about we go to the carnival? Play some games, do some rides?"
    play sound sfx_skirt_off2
    scene sm1cs-mh008-18-mh-talk-mc with dissolve
    play voice3 lissa_yes noloop
    mh "That sounds absolutely wonderful, [mcname]."
    mh "Let me get changed."
    play sound sfx_barefoot_steps1 loop
    scene sm1cs-mh008-19-mh-talk-mc with dissolve
    play voice3 lissa_thinking1 noloop
    mh "So what have you been up to lately?"
    play sound sfx_door_openclosed2
    scene sm1cs-mh008-21-mh-talk-mc with dissolve
    play voice2 mc_surprised_oh1 noloop
    mc "Oh not much..."
    mc "Working, getting the studio ready."
    scene sm1cs-mh008-22-mc-talk-mh with dissolve
    play voice2 mc_thinking_hm noloop
    mc "We actually just finished renovating!"
    scene sm1cs-mh008-24-mh-talk-mc with dissolve
    play voice3 lissa_what_muffled noloop
    mh "Oh? You renovated?"
    play sound sfx_heels_steps2 loop
    scene sm1cs-mh008-25-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah! We wanted to be able use the studio as, well, a studio."
    mc "So we painted, cleaned it up, you know - all the usual renovation things."
    stop sound fadeout 1.0
    scene sm1cs-mh008-24-mh-talk-mc with dissolve
    play voice3 lissa_yeah_muffled noloop
    mh "Well, I'm glad it's a mixed use space."
    scene sm1cs-mh008-23-mc-talk-mh with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "A what?"
    play sound sfx_door_openclosed1
    scene sm1cs-mh008-28-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm2 noloop
    mh "We talked about this. It's a space you can use as residential and commercial."
    mh "You'll have to show me what you've done to the place. It's been a while since I've been there."
    scene sm1cs-mh008-29-mc-talk-mh with dissolve
    play voice2 mc_yes_yes1 noloop
    mc "Absolutely!"
    play sound sfx_heels_steps1
    scene sm1cs-mh008-30-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "And how's Stacy doing?"
    stop sound fadeout 1.0
    scene sm1cs-mh008-31-mc-talk-mh with dissolve
    play voice2 mc_happy_a1 noloop
    mc "She's good-"
    scene sm1cs-mh008-32-mc-talk with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, hang on. Just got a text."
    play sound sfx_phone_buzz volume 0.6
    scene sm1cs-mh008-33-mc-talk-mh with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "Stacy's ears must be burning - she just texted me."
    scene sm1cs-mh008-36-mh-talk-mc with dissolve
    play voice3 lissa_oh noloop volume 1.6
    mh "Oh? Is everything okay?"
    scene sm1cs-mh008-37-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, she was just asking me what I was up to tonight. Seems like she wants to take the night off from working."
    scene sm1cs-mh008-38-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "Ah."
    mh "If you need to go, I understand."
    scene sm1cs-mh008-39-mc-talk-mh with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "What? No, no. Totally fine. I just told her I was spending time with you."
    scene sm1cs-mh008-40-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "Well, that does make me happy to hear."
    scene sm1cs-mh008-43-mc-talk-mh with dissolve
    play voice2 d2s9_mchey noloop
    mc "Everything okay, Lyssa?"
    scene sm1cs-mh008-41-mh-talk-mc with dissolve
    play voice3 dahlia_yes_yeah4 noloop
    mh "Yeah, it's just..."
    mh "This... situation is still a little new to me. I know we haven't been monogamous in the past, but..."
    scene sm1cs-mh008-44-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "I am still concerned from time to time that whenever Stacy calls, you'll go running."
    mh "And that I'll always be second best..."
    play sound sfx_cloth_rustling4
    scene sm1cs-mh008-45-mc-mh-hug with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Lyssa, I need you to listen very closely to me."
    mc "You are second to none. You are incredible, sexy, smart, powerful."
    scene sm1cs-mh008-46-mc-talk-mh with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "And I am ready to do anything to show you that you have a place in my life, just like Stacy, and whomever else."
    scene sm1cs-mh008-47-mh-talk-mc with dissolve
    play voice3 lissa_ugu3 noloop
    mh "You've already done a lot to show me that, [mcname]."
    mh "And I appreciate it."
    play sound sfx_cloth_rustling2
    scene sm1cs-mh008-48-mc-talk-mh with dissolve
    play voice2 mc_happy_yes1 noloop
    mc "Of course, Lyssa! You're worth it to me."
    scene sm1cs-mh008-49-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    if persistent.is_special:
        mh "I guess... I'll always be a little nervous about your sister."
    else:
        mh "I guess... I'll always be a little nervous about Stacy."
    scene sm1cs-mh008-50-mc-talk-mh with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well, I guess the best way to show you that you have nothing to worry about with Stacy is to invite her tonight!"
    scene sm1cs-mh008-51-mh-talk-mc with dissolve
    play voice3 dahlia_surprised_ah2 noloop
    mh "Wh...{w} what?"
    if player.get_choice("sm1cs_mh006_thruple"):
        scene sm1cs-mh008-61-mc-talk-mh with dissolve
        play voice2 mc_yes_yeah7 noloop
        mc "Yeah! Stacy can tag along and we can all spend some time together and see what it's like!"
        scene sm1cs-mh008-62-mh-talk-mc with dissolve
        play voice3 dahlia_thinking_hmm1 noloop
        mh "I don't know..."
        menu:
            "Try and Convince Lyssa":
                $ player.set_choice("sm1cs_mh008_convince_mh")
                scene sm1cs-mh008-52-c1-mc-talk-mh with dissolve
                play voice2 mc_thinking_hmm5 noloop
                mc "I guess... I just want to try and help you figure everything out with Stacy and I dating too."
                mc "Because... I don't know, I know you're always nervous about it."
                mc "And if I can help you get less nervous about it, then it's one less thing for you to worry about."
                scene sm1cs-mh008-53-c1-mh-talk-mc with dissolve
                play voice3 lissa_ha noloop
                mh "Always trying to make everyone's lives better, huh, [mcname]?"
                scene sm1cs-mh008-54-c1-mc-talk-mh with dissolve
                play voice2 mc_yes_yes2 noloop
                mc "Just doing what I can."
                scene sm1cs-mh008-55-c1-mh-talk-mc with dissolve
                play voice3 dahlia_disappointed_hmm2 noloop
                mh "You're right though. I do need to find a way to get more comfortable with this."
                mh "Sure, invite Stacy for a... I guess, throuple date?"
                scene sm1cs-mh008-56-c1-mc-talk-mh with dissolve
                play voice2 mc_happy_yay1 noloop
                mc "Great! I'll shoot her a text telling her to meet us there!"
                scene sm1cs-mh008-57-c1-mh-talk-mc with dissolve
                play voice3 lissa_aga noloop
                mh "That sounds great, [mcname]."
            "Don't press the issue":
                scene sm1cs-mh008-58-c2-mc-talk-mh with dissolve
                play voice2 mc_hey_hey7 noloop
                mc "Hey, if you're not comfortable with that idea, we can do it some other time."
                scene sm1cs-mh008-59-c2-mc-talk-mh with dissolve
                play voice3 dahlia_arrogant_yeah noloop
                mh "Yeah, I don't think I'm there yet, [mcname]."
                scene sm1cs-mh008-60-c2-mc-talk-mh with dissolve
                play voice2 mc_yes_okay1 noloop
                mc "Totally okay! No worries at all, Lyssa."
    else:
        scene sm1cs-mh008-61-mc-talk-mh with dissolve
        play voice2 mc_hey_hey7 noloop
        mc "Hey, if you're not comfortable with that idea, we can do it some other time."
        scene sm1cs-mh008-62-mh-talk-mc with dissolve
        play voice3 dahlia_arrogant_yeah noloop
        mh "Yeah, I don't think I'm there yet, [mcname]."
        scene sm1cs-mh008-63-mc-talk-mh with dissolve
        play voice2 mc_yes_okay1 noloop
        mc "Totally okay! No worries at all, Lyssa."
    scene sm1cs-mh008-64-mc-talk-mh with dissolve
    play voice2 mc_angry_cough1 noloop
    mc "But, without any further ado, let's get to the carnival!"
    scene sm1cs-mh008-65-mh-talk-mc with dissolve
    play voice3 lissa_laugh noloop
    mh "Hahahaha, oh, [mcname]."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh008-66-mh-walk with dissolve
    pause
    jump sm1cs_mh008_carnival
label sm1cs_mh008_carnival:
    play music2 amusement_park_music fadein 1.5
    $ renpy.music.set_volume(0.1, 2.5, "music" )
    play sound5 sfx_parknight_crickets fadein 1.5 volume 0.5
    play sound4 sfx_amusement_park_ambience fadein 2.0 volume 0.2
    scene sm1cs-mh008-67-mh-mc-carnival with Fade(0.5, 0.5, 0.5)
    play sound2 sfx_heels_steps2
    pause
    scene sm1cs-mh008-68-mh-talk with dissolve
    play voice3 lissa_mmm1 noloop
    mh "Mmmmmm..."
    scene sm1cs-mh008-69-mc-talk-mh with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "Huh?"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mh008-70-mh-talk-mc with dissolve
    play voice3 lissa_haha2 noloop
    mh "I just love that smell... popcorn, and machinery, and groups of people laughing and smiling..."
    scene sm1cs-mh008-71-mc-talk-mh with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh, really?"
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mh008-72-mh-talk-mc with dissolve
    play voice3 dahlia_yes_yeah1 noloop
    mh "Yeah... I have a lot of fond memories of circuses and carnivals."
    scene sm1cs-mh008-73-mc-talk-mh with dissolve
    play voice2 mc_surprised_wow3 noloop
    mc "That's something I didn't know about you."
    scene sm1cs-mh008-74-mh-talk-mc with dissolve
    play voice3 lissa_ugu noloop
    mh "This is one of the perks of slowing down a little bit. Learning more about each other."
    scene sm1cs-mh008-75-mc-talk-mh with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "I agree.{w} Well, why do you have so many fond memories of circuses?"
    $ renpy.music.set_volume(0.1, 15.5, "music2" )
    $ renpy.music.set_volume(1.0, 10.5, "music" )
    scene sm1cs-mh008-76-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm3 noloop
    mh "Well... my bio parents - erm, the people who actually gave birth to me, would bring me to the carnival every year."
    mh "I didn't know until I was older that it was because my bio-father had successfully defended a ride manufacturer in a pretty hairy civil suit because someone had gotten pretty badly injured."
    scene sm1cs-mh008-77-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    mh "As I kid, I just knew that we would come to the circus because we had free tickets, and..."
    mh "And I think it was one of the few times I saw my bio-father relax the hardened lawyer facade and just... be my dad."
    scene sm1cs-mh008-78-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I... I didn't know that."
    stop sound fadeout 1.5
    stop sound2 fadeout 1.5
    scene sm1cs-mh008-79-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "It's okay. I've been... guarded about it most of my life."
    scene sm1cs-mh008-80-mc-talk-mh with dissolve
    play voice2 d2s9_confused noloop
    mc "I also... didn't know that you had been adopted."
    scene sm1cs-mh008-81-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_mmm1 noloop
    mh "That's... another thing I've been pretty guarded about."
    scene sm1cs-mh008-82-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mc "Can I ask what happened?"
    scene sm1cs-mh008-83-mh-talk-mc with dissolve
    play voice3 dahlia_angry_oof noloop
    mh "Oh, it's all pretty mundane. They were coming home from some gala and were struck by a drunk driver."
    mh "I was pretty young... this all happened a long time ago."
    scene sm1cs-mh008-84-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "And then I was adopted by a lovely couple, and they took good care of me."
    mh "I had told them about my... family's trips to the carnival. So every summer, they would make sure to take me."
    scene sm1cs-mh008-85-mh-talk with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "Mmmmm..."
    scene sm1cs-mh008-86-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop
    mct "Man... there's a lot about Lyssa I don't really know."
    mct "Like... a lot a lot. Wow..."
    scene sm1cs-mh008-87-mc-inner-talk with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "I can't believe she went through all that. I always knew she was strong but..."
    mct "Damn."
    scene sm1cs-mh008-88-mh-talk-mc with dissolve
    play voice3 dahlia_angry_oh noloop
    mh "Oh, don't do that, [mcname]."
    scene sm1cs-mh008-89-mc-talk-mh with dissolve
    play voice2 mc_surprised_what7 noloop
    mc "Do what?"
    scene sm1cs-mh008-90-mh-talk-mc with dissolve
    play voice3 dahlia_arrogant_hm noloop
    mh "Start giving me pity."
    scene sm1cs-mh008-91-mc-talk-mh with dissolve
    play voice2 d9s2_mmno noloop volume 2.0
    mc "What! No, no. That's not what I was thinking."
    scene sm1cs-mh008-92-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "You sure? Because you had that look on your face everyone gets when I tell them about how I grew up."
    scene sm1cs-mh008-93-mc-talk-mh with dissolve
    play voice2 mc_no_no6 noloop
    mc "No. I was thinking about...{w} All this time together, and I'm still learning more about you."
    mc "And I'm glad I am. There's a lot of things now that make a lot more sense."
    scene sm1cs-mh008-94-mh-talk-mc with dissolve
    play voice3 lissa_haha noloop
    mh "Being an adopted orphan will make a person a bit more guarded, haha."
    scene sm1cs-mh008-95-mc-talk-mh with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "That, but it also explains why you are such a strong, fierce woman."
    scene sm1cs-mh008-96-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "Thank you, [mcname]."
    scene sm1cs-mh008-97-mc-talk-mh with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Of course, Lyssa."
    scene sm1cs-mh008-98-mc-talk-mh with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "Well, hey - no carnival trip is complete without popcorn!"
    scene sm1cs-mh008-99-mh-talk-mc with dissolve
    play voice3 dahlia_surprised_oh noloop
    mh "[mcname]-"
    play sound2 sfx_heels_steps2
    scene sm1cs-mh008-100-mc-talk-mh with dissolve
    play voice2 mc_no_uhuh3 noloop
    mc "Nuh uh, I'm not going to listen to any arguments from the defense! I am getting you some popcorn."
    stop sound2 fadeout 1.0
    scene sm1cs-mh008-101-mc-talk with dissolve
    play voice2 d9s2_yeah noloop volume 1.7
    mc "Yeah, I'll take one, uhm, large popcorn?"
    play sound2 sfx_heels_steps2
    scene sm1cs-mh008-102-mh-look-mc with dissolve
    pause
    stop sound2 fadeout 1.0
    play sound sfx_chips_crunch1
    scene sm1cs-mh008-103-mc-talk-mh with dissolve
    play voice2 mc_happy_oof1 noloop
    mc "There ain't nothing like carnival popcorn!"
    scene sm1cs-mh008-104-mh-talk-mc with dissolve
    play voice3 dahlia_disgust_yah noloop
    mh "God, you are such a goof sometimes."
    scene sm1cs-mh008-105-mc-talk-mh with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "Yeah, but you like it."
    scene sm1cs-mh008-106-mh-talk-mc with dissolve
    play voice3 dahlia_happy_laugh4 noloop
    mh "Admittedly, I do."
    mh "Because you're also quite the charmer."
    scene sm1cs-mh008-107-mc-talk-mh with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "Awe shucks, Lyssa."
    scene sm1cs-mh008-108-mh-talk with dissolve
    play voice3 dahlia_yes_ugu noloop
    mh "Uh huh."
    jump sm1cs_mh008_date
label sm1cs_mh008_date:
    if player.get_choice("sm1cs_mh008_convince_mh"):
        scene sm1cs-mh008-109-c1-mh-talk-mc with dissolve
        play voice3 dahlia_thinking_hmm2 noloop
        mh "So... you texted Stacy?"
        scene sm1cs-mh008-110-c1-mc-talk-mh with dissolve
        play voice2 mc_yes_yes6 noloop
        mc "I did. She said she had to shower and she would be on her way."
        mc "So we definitely have some time to kill before she gets here."
    else:
        scene sm1cs-mh008-111-c2-mc-talk-mh with dissolve
        play voice2 mc_thinking_hmm8 noloop
        mc "So, what would you like to do now that we have secured the best popcorn that you can get."
        scene sm1cs-mh008-112-c2-mh-talk-mc with dissolve
        play voice3 dahlia_happy_laugh6 noloop
        mh "Hahahaha!"
    scene sm1cs-mh008-113-mh-talk-mc with dissolve
    play voice3 lissa_hey noloop
    mh "How about some games?"
    scene sm1cs-mh008-114-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, that sounds great! I can try and win you a giant stuffed teddy!"
    play sound sfx_cloth_rustling1
    scene sm1cs-mh008-115-mh-talk-mc with dissolve
    play voice3 dahlia_surprised_huh2 noloop
    mh "Did you know that \"teddy bears\" are named after the 26th US President, Theodore Roosevelt?"
    scene sm1cs-mh008-116-mc-talk-mh with dissolve
    play voice2 mc_surprised_what6 noloop
    mc "What? Seriously?"
    scene sm1cs-mh008-117-mh-talk-mc with dissolve
    play voice3 dahlia_yes_yeah3 noloop
    mh "Yeah. it's a weird story, but in short - Mr. Roosevelt refused to shoot a tied up bear, and then someone made a political cartoon of it."
    mh "And then a toymaker, Morris Michtom, saw the cartoon and wanted to make a cute, stuffed bear."
    scene sm1cs-mh008-118-mh-talk-mc with dissolve
    play voice3 lissa_thinking1 noloop volume 1.7
    mh "He sold them as \"Teddy's Bears\", which is where they got the name."
    mh "And it's also why everyone started calling him Teddy Roosevelt. Because of the bear."
    scene sm1cs-mh008-119-mc-talk-mh with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Huh... that's a weird fun fact."
    scene sm1cs-mh008-120-mh-talk-mc with dissolve
    play voice3 dahlia_arrogant_heh noloop
    mh "You learn lots of weird things on the road of life."
    jump sm1ms_mh008_game
label sm1ms_mh008_game:
    $ renpy.music.set_volume(0.2, 15.5, "music2" )
    $ renpy.music.set_volume(1.0, 10.5, "music" )
    scene sm1cs-mh008-121-worker-talk-mc with dissolve
    play voice4 boy5_hey_heyo noloop
    "Carnival Worker" "Step right up! See if you have what it takes to take home one of these adorable, stuffed animals!"
    scene sm1cs-mh008-122-mc-talk-worker with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "What do I have to do to win one?"
    scene sm1cs-mh008-123-worker-talk-mc with dissolve
    play voice4 boy5_surprised_oh1 noloop
    "Carnival Worker" "It's simple! You got five shots with our air rifle, and you just need to knock down three of the targets!"
    scene sm1cs-mh008-124-mc-talk-worker with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Easy! I can do that!"
    scene sm1cs-mh008-125-worker-talk-mc with dissolve
    play voice4 boy5_happy_yeah4 noloop
    "Carnival Worker" "Yeah! Nothing to it! Show me what you got!"
    play sound sfx_shotgun_cocking2
    scene sm1cs-mh008-126-mc-inner-talk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "All right, [mcname]. Let's win Lyssa this bear!"
    scene sm1cs-mh008-127-pop-pop-pop with dissolve
    play sound sfx_tire_gunshots1
    "Bang. Bang. Bang."
    scene sm1cs-mh008-128-targets with dissolve
    pause
    scene sm1cs-mh008-129-mc-rifle with dissolve
    play voice2 d3s7_mcemm noloop
    pause
    scene sm1cs-mh008-130-worker-talk-mc with dissolve
    play voice4 boy5_thinking_eeh1 noloop
    "Carnival Worker" "Well, it seems like you missed all three shots! Would you like to try again?"
    scene sm1cs-mh008-131-mc-talk-worker with dissolve
    play voice2 mc_yes_yes5 noloop
    mc "Absolutely!"
    scene sm1cs-mh008-132-worker-talk-mc with dissolve
    play voice4 boy5_yes_ugu1 noloop
    "Carnival Worker" "All right, have at her!"
    scene sm1cs-mh008-133-pop-pop-pop with dissolve
    play sound sfx_tire_gunshots1
    "Bang. Bang. Bang."
    scene sm1cs-mh008-134-targets with dissolve
    pause
    scene sm1cs-mh008-135-mc-inner-talk with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mct "Shit..."
    scene sm1cs-mh008-136-worker-talk-mc with dissolve
    play voice4 boy5_surprised_wow2 noloop
    "Carnival Worker" "And three more misses! Wow!{w} What about you, miss? Would you like to give it a go?"
    scene sm1cs-mh008-137-mh-talk-mc with dissolve
    play voice3 dahlia_yes_yeah1 noloop
    mh "Sure. How much to play?"
    scene sm1cs-mh008-138-mc-talk-mh with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Don't worry, Lyssa. I'll pay for it."
    scene sm1cs-mh008-139-worker-talk with dissolve
    play voice4 boy5_yes_yep noloop
    "Carnival Worker" "And fire awwaaayyyy when you're ready!"
    play sound [sfx_tire_target1, sfx_tire_target2, sfx_tire_target3, sfx_tire_target4]
    scene sm1cs-mh008-140-mh-rifle with dissolve
    "Clang. Clang. Clang. Clang!"
    scene sm1cs-mh008-141-tink-tink-tink with dissolve
    pause
    scene sm1cs-mh008-142-targets with dissolve
    pause
    scene sm1cs-mh008-143-mc-shocked with dissolve
    play voice2 mc_scared_huuuh3 noloop
    pause
    scene sm1cs-mh008-144-worker-talk with dissolve
    play voice4 boy5_pain_mmm3 noloop
    "Carnival Worker" "Holy guacamole... you hit all three targets! {size=*0.5}Corporate said that it was impossible! What the hell...{/size}"
    scene sm1cs-mh008-145-mh-talk-worker with dissolve
    play voice3 dahlia_arrogant_huh noloop
    mh "I believe I am owed a teddy bear?"
    scene sm1cs-mh008-146-worker-talk-mh with dissolve
    play voice4 boy5_disappointed_oof1 noloop
    "Carnival Worker" "Oh, uhm... you most definitely are..."
    play sound sfx_cloth_planket2
    scene sm1cs-mh008-147-worker-talk-mh with dissolve
    play voice4 boy5_thinking_hmm1 noloop
    "Carnival Worker" "Here you go..."
    scene sm1cs-mh008-148-mh-talk-worker with dissolve
    play voice3 lissa_aga noloop
    mh "Thank you."
    scene sm1cs-mh008-149-mc-talk-mh with dissolve
    play voice2 mc_surprised_wow1 noloop
    mc "Wow, Lyssa... I didn't realize you were so good at shooting."
    scene sm1cs-mh008-150-mh-talk-mc with dissolve
    play voice3 lissa_ha noloop
    mh "One of the few perks of coming to the carnival once or twice a year since you were a youngster."
    scene sm1cs-mh008-151-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yeah. I also guess I need to do some target practice. Can't let you win your own stuffed animals."
    scene sm1cs-mh008-152-mh-talk-mc with dissolve
    play voice3 dahlia_hey_active1 noloop
    mh "It's okay. You tried, which is really what matters, [mcname]."
    mh "And you continue to try, try your hardest. And I see that."
    mh "And that's what I... like about you {b}most{/b}."
    scene sm1cs-mh008-153-mc-talk-mh with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Thank you, Lyssa."
    if player.get_choice("sm1cs_mh008_convince_mh"):
        play sound sfx_phone_buzz volume 0.7
        scene sm1cs-mh008-154-mc-talk-mh with dissolve
        play voice2 mc_surprised_oh3 noloop
        mc "Oh, it looks like Stacy is just about to get here. Should we head over to the entrance to meet her?"
        scene sm1cs-mh008-155-mh-talk-mc with dissolve
        play voice3 dahlia_yes_yeah2 noloop
        mh "Yeah, make everyone's life easier instead of making her look for us."
        scene sm1cs-mh008-156-mc-talk-mh with dissolve
        play voice2 mc_surprised_uh3 noloop
        mc "What, you don't want to play carnival hide-and-seek with Stacy?"
        mc "I bet we would kick her ass in some hide-and-seek!"
        scene sm1cs-mh008-157-mh-talk-mc with dissolve
        play voice3 dahlia_happy_laugh2 noloop
        mh "Come on, you goof."
        jump sm1cs_mh008_throuple_carousel
    else:
        jump sm1cs_mh008_couple_carousel
label sm1cs_mh008_couple_carousel:
    play sound sfx_popcorn_grab1
    scene sm1cs-mh008-158-carousel with dissolve
    pause
    stop music fadeout 6.0
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene sm1cs-mh008-177-c1-montage with dissolve
    queue music music_melancholy_forever
    pause
    scene sm1cs-mh008-178-c1-montage with dissolve
    pause
    scene sm1cs-mh008-179-c1-montage with dissolve
    pause
    scene sm1cs-mh008-180-c1-montage with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-mh008-181-c1-montage with dissolve
    pause
    scene sm1cs-mh008-187-c1-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm7 noloop
    mc "Well, no visit to the carnival is complete without a ferris wheel ride!"
    scene sm1cs-mh008-188-c1-mh-talk-mc with dissolve
    play voice3 dahlia_yes_simple noloop
    mh "I couldn't agree more, [mcname]."
    play sound2 sfx_heels_steps1
    play sound3 sfx_heels_steps2
    scene sm1cs-mh008-189-c1-mc-mh with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    stop music2 fadeout 2.0
    stop sound4 fadeout 3.0
    stop sound5 fadeout 3.0
    play sound3 sfx_ferris_wheel_insideambience fadein 1.0 volume 1.6
    scene sm1cs-mh008-194-ferris-wheel with dissolve
    pause
    scene sm1cs-mh008-196-mh-talk-mc with dissolve
    play voice3 lissa_laugh2 noloop
    mh "I hope you're not afraid of heights, [mcname]!"
    scene sm1cs-mh008-197-mc-talk-mh with dissolve
    play voice2 mc_no_nope1 noloop
    mc "Nope! Not afraid of them at all."
    scene sm1cs-mh008-198-c2-mh-talk-sy with dissolve
    play voice3 lissa_laugh noloop
    mh "Hehehe. Are you afraid of anything? Some of the things I've seen you do... I think of you as fearless."
    scene sm1cs-mh008-210-mc-talk with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "I... I do have one fear."
    scene sm1cs-mh008-260-mh-talk-mc with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    mh "Oh yeah? And what's that."
    scene sm1cs-mh008-261-mc-talk-mh with dissolve
    play voice2 mc_disgust_ooh2 noloop
    mc "I'm... I'm afraid of peanut butter getting stuck to the roof of my mouth."
    scene sm1cs-mh008-263-mh-talk-mc with dissolve
    play voice3 dahlia_surprised_what noloop
    mh "Excuse me... you're afraid of..."
    scene sm1cs-mh008-258-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Peanut butter getting stuck to the roof of my mouth. Yeah."
    mc "Because I'm going to be eating, like, a PB and J, and someone is going to try and talk to me."
    scene sm1cs-mh008-210-mc-talk with dissolve
    play voice2 mc_angry_oof noloop
    mc "And then I'm going to have peanut butter in my mouth, and I won't be able to talk."
    mc "Or it'll sound super weird!"
    scene sm1cs-mh008-212-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "I, uhm - uhm-"
    scene sm1cs-mh008-215-mc-talk-mh with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "What! It's a very real fear!"
    scene sm1cs-mh008-221-mh-talk with dissolve
    play voice3 dahlia_happy_laugh5 noloop
    mh "Hahahahaha!"
    scene sm1cs-mh008-213-mc-talk with dissolve
    play voice2 mc_surprised_huh8 noloop
    mc "And what, you're totally fearless, Lyssa?!?"
    scene sm1cs-mh008-214-mh-talk-mc with dissolve
    play voice3 dahlia_no_simple noloop
    mh "No, I wouldn't say that. I'm scared of some things. I used to get really bad vertigo, but I think I've finally gotten over that."
    mh "And I wouldn't say I'm scared of clowns, I just have an... aversion to them."
    scene sm1cs-mh008-216-mc-talk-mh with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "There's only one clown to be afraid of."
    scene sm1cs-mh008-217-mh-talk with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "Oh yeah? And which one is that?"
    scene sm1cs-mh008-220-mc-talk with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "Donald. MacDonald."
    scene sm1cs-mh008-228-mh-talk-mc with dissolve
    play voice3 dahlia_surprised_ah2 noloop
    mh "Like... the mascot for the fast food place?"
    scene sm1cs-mh008-251-mc-talk-mh with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "Yes. He's the most lethal clown in history."
    mc "He's killed more people than Gacy."
    scene sm1cs-mh008-252-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "You know... you've got a good point there."
    scene sm1cs-mh008-254-mc-talk with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "And he just looks creepy as hell."
    scene sm1cs-mh008-255-mh-talk-mc with dissolve
    play voice3 lissa_haha2 noloop
    mh "Hehehe - yeah, you're not wrong there either."
    scene sm1cs-mh008-256-mh-talk with dissolve
    play voice3 dahlia_surprised_wow noloop
    mh "Wow... sometimes I forget how beautiful Crowning is..."
    scene sm1cs-mh008-258-mc-talk-mh with dissolve
    play voice2 d9s2_mcyes noloop volume 2.2
    mc "Yeah, the sights are really something..."
    scene sm1cs-mh008-260-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "You're not even looking out at the city, [mcname]."
    scene sm1cs-mh008-261-mc-talk-mh with dissolve
    play voice2 mc_surprised_why1 noloop
    mc "Why would I do that?"
    scene sm1cs-mh008-262-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Because, as far as I'm concerned, the most beautiful thing I could be looking at, is you, Lyssa."
    scene sm1cs-mh008-263-mh-talk-mc with dissolve
    play voice3 lissa_oh2 noloop
    mh "Oh, you..."
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-mh008-264-mc-mh-kiss with dissolve
    play voice2 d1s5_orgasm noloop
    play voice3 lissa_mmm2 noloop
    play sound mc_kiss2
    pause
    scene sm1cs-mh008-274-mc-mh with dissolve
    pause
    scene sm1cs-mh008-276-mc-talk with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I-"
    scene sm1cs-mh008-278-mh-talk-mc with dissolve
    play voice3 lissa_thinking2 noloop volume 1.8
    mh "[mcname]?"
    scene sm1cs-mh008-280-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    scene sm1cs-mh008-282-mh-talk-mc with dissolve
    play voice3 lissa_moan1 noloop
    mh "Let's just enjoy this moment."
    scene sm1cs-mh008-284-mc-talk-mh with dissolve
    play voice2 d9s2_ugu noloop
    mc "Yeah, that sounds nice."
    jump sm1cs_mh008_couple_carousel_end
label sm1cs_mh008_couple_carousel_end:
    play sound5 sfx_amusement_park_ambience fadein 2.0 volume 0.4
    stop sound3 fadeout 2.0
    play sound4 sfx_parknight_crickets fadein 2.0 volume 0.5
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mh008-286-mc-mh with Fade(0.5, 0.5, 0.5)
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mh008-288-mh-talk-mc with dissolve
    play voice3 dahlia_happy_phew noloop
    mh "That was... truly wonderful, [mcname]."
    mh "Another wonderful carnival memory to add to the others."
    scene sm1cs-mh008-290-mc-talk with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "I couldn't think of anyone I'd rather be looking out over the city than with you, Lyssa."
    scene sm1cs-mh008-291-mh-talk with dissolve
    play voice3 dahlia_disappointed_ehh1 noloop
    mh "I'd hate to cut this short, but I do have a meeting in the morning that I have to make."
    scene sm1cs-mh008-293-mc-talk-mh with dissolve
    if gt.next_day in [SATURDAY, SUNDAY]:
        play voice2 mc_thinking_wait1 noloop
        mc "Wait, isn't it the weekend?"
        scene sm1cs-mh008-294-mh-talk-mc with dissolve
        play voice3 lissa_ugu2 noloop
        mh "When you work as a solo practitioner, you're never guaranteed weekends off."
    else:
        play voice2 mc_happy_oof3 noloop
        mc "Oh shit, it's a work night, isn't it?"
        scene sm1cs-mh008-294-mh-talk-mc with dissolve
        play voice3 lissa_ugu2 noloop
        mh "That it is."
    scene sm1cs-mh008-296-mc-talk-mh with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "In that case, I'm glad you had a great night."
    scene sm1cs-mh008-297-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "There is... one more thing you could do to make tonight phenomenal."
    scene sm1cs-mh008-298-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Oh yeah? And what's that?"
    scene sm1cs-mh008-299-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "Kiss me."
    scene sm1cs-mh008-300-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Don't mind if I do."
    play sound2 sfx_skirt_off2 noloop
    play sound3 sfx_throw_something1 noloop
    scene sm1cs-mh008-301-mc-mh-kiss with dissolve
    play voice2 mc_angry_errr8 noloop
    play voice3 lissa_mmm2 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-mh008-302-mh-talk-mc with dissolve
    play voice3 lissa_moan2 noloop
    pause
    scene sm1cs-mh008-303-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "Mmmmm... perfect, [mcname]."
    mh "That was... a hell of a kiss."
    scene sm1cs-mh008-304-mc-talk-mh with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, when you say \"memorable\" and \"kiss\", I have to give you the maximum effort kiss, right?"
    scene sm1cs-mh008-305-mh-talk-mc with dissolve
    play voice3 lissa_yes noloop
    mh "Yes, you do."
    mh "And I'm going to be holding you to that, [mcname]."
    scene sm1cs-mh008-306-mc-talk-mh with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Good."
    scene sm1cs-mh008-317-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_mmm2 noloop
    mh "All right, I do need to go though. I hope I see you soon, [mcname]."
    scene sm1cs-mh008-318-mc-talk-mh with dissolve
    play voice2 mc_hey_hey8 noloop
    mc "You will! I have to show you the new studio now that it's done!"
    scene sm1cs-mh008-319-mh-talk-mc with dissolve
    play voice3 dahlia_yes_aga noloop
    mh "Sounds like a date to me."
    scene sm1cs-mh008-325-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "Hell yeah, that was a great date."
    mct "And I'm pretty excited for her to see what the studio looks like now."
    jump sm1cs_mh008_end_scene
label sm1cs_mh008_throuple_carousel:
    play sound sfx_popcorn_grab1
    scene sm1cs-mh008-158-carousel with dissolve
    pause
    play sound sfx_heels_run2
    scene sm1cs-mh008-159-c2-sy-talk with dissolve
    play voice4 stacy_hey noloop
    sy "[mcname]! Lyssa!"
    scene sm1cs-mh008-160-c2-mc-talk-sy with dissolve
    play voice2 d1s2_mchey noloop volume 1.7
    mc "Hey, Stacy."
    scene sm1cs-mh008-161-c2-sy-talk with dissolve
    play voice4 stacy_thinking_emm1 noloop
    sy "Sorry I'm so late. I had to shower, and find some clean clothes, and - never mind, did I miss anything fun?"
    scene sm1cs-mh008-162-c2-mh-talk-sy with dissolve
    play voice3 lissa_oh2 noloop
    mh "Just [mcname] winning me a little prize."
    scene sm1cs-mh008-163-c2-sy-talk-mh with dissolve
    play voice4 stacy_surprised_huh3 noloop
    sy "What!"
    sy "It's so cute! [mcname]! Why didn't you win me one?"
    scene sm1cs-mh008-165-c2-mc-talk with dissolve
    play voice2 d2s12_emmm noloop
    mc "Well, uhhh..."
    scene sm1cs-mh008-166-c2-mh-talk-sy with dissolve
    play voice3 lissa_haha2 noloop
    mh "Well, [mcname] didn't win it, exactly. But he paid for the winning game!"
    scene sm1cs-mh008-167-c2-sy-talk-mh with dissolve
    play voice4 stacy_disappointed_oh3 noloop
    sy "Ohhhhhh."
    scene sm1cs-mh008-168-c2-sy-talk-mh with dissolve
    play voice4 stacy_thinking_emm3 noloop
    sy "Lyyssssaaaaaaaaa, will you win me a teddy bear with [mcname]'s money?"
    scene sm1cs-mh008-169-c2-mh-talk with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "Oh, well that doesn't sound like a half-bad plan. What do you think, [mcname]?"
    scene sm1cs-mh008-170-c2-mc-talk with dissolve
    play voice2 d1s5b_emmm noloop
    mc "I, uhhh - that was an expensive game, and erm-"
    scene sm1cs-mh008-171-c2-sy-talk-mc with dissolve
    play voice4 stacy_happy_laugh3 noloop
    sy "I'm kidding, [mcname]. You don't need to win me a bear."
    sy "But you do need to show me around! I don't think I've ever really been to the carnival for fun. Just for... \"work stuff\"."
    scene sm1cs-mh008-172-c2-mh-talk-sy with dissolve
    play voice3 dahlia_surprised_ah2 noloop
    mh "Really?"
    scene sm1cs-mh008-173-c2-sy-talk-mh with dissolve
    play voice4 stacy_yes_ugu1 noloop
    if persistent.is_special:
        sy "Uh huh. We never really went growing up, and I've been so busy since I got to Crowning, well... I just haven't been able to make the time."
    else:
        sy "Growing up. Our familes never really went to the carvnial."
        sy "And I've been so busy since I got to Crowning, well... I just haven't been able to make the time."
    scene sm1cs-mh008-174-c2-mh-talk-sy with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "Well, let's get you caught up."
    scene sm1cs-mh008-175-c2-sy-talk-mh with dissolve
    play voice4 stacy_happy_yay3 noloop
    sy "Thanks, Lyssa."
    scene sm1cs-mh008-176-c2-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "Well, things are definitely off to a good start!"
    stop music fadeout 6.0
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mh008-182-c2-montage with dissolve
    queue music music_melancholy_forever
    pause
    scene sm1cs-mh008-183-c2-montage with dissolve
    pause
    scene sm1cs-mh008-184-c2-montage with dissolve
    pause
    scene sm1cs-mh008-185-c2-montage with dissolve
    pause
    scene sm1cs-mh008-186-c2-montage with dissolve
    pause
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mh008-190-c2-sy-talk with dissolve
    play voice4 stacy_thinking_oh1 noloop
    sy "Ooooo, are we going to ride on the ferris wheel!?"
    scene sm1cs-mh008-191-c2-mc-talk with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mc "Well, no visit to the carnival is complete without a ferris wheel ride!"
    scene sm1cs-mh008-192-c2-mh-talk-mc with dissolve
    play voice3 dahlia_yes_aga noloop
    mh "I couldn't agree more, [mcname]."
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mh008-193-c2-mc-mh-sy with dissolve
    pause
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    stop music2 fadeout 2.0
    stop sound4 fadeout 3.0
    stop sound5 fadeout 3.0
    stop sound fadeout 1.0
    play sound3 sfx_ferris_wheel_insideambience fadein 1.0 volume 1.6
    scene sm1cs-mh008-195-c2-ferris-wheel with dissolve
    pause
    scene sm1cs-mh008-196-mh-talk-mc with dissolve
    play voice3 lissa_laugh2 noloop
    mh "I hope you're not afraid of heights, [mcname]!"
    scene sm1cs-mh008-197-mc-talk-mh with dissolve
    play voice2 mc_no_nope1 noloop
    mc "Nope! Not afraid of them at all."
    scene sm1cs-mh008-198-c2-mh-talk-sy with dissolve
    play voice3 lissa_thinking2 noloop
    mh "What about you, Stacy?"
    scene sm1cs-mh008-199-c2-sy-talk-mh with dissolve
    play voice4 stacy_surprised_oh1 noloop
    sy "Oh, I'm terrified of heights."
    scene sm1cs-mh008-200-c2-mh-talk-sy with dissolve
    play voice3 dahlia_surprised_huh1 noloop
    mh "Then... why did you want to ride the ferris wheel?"
    scene sm1cs-mh008-201-c2-mc-talk-sy with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, the whole thing with it is heights, Stacy."
    scene sm1cs-mh008-202-c2-sy-talk with dissolve
    play voice4 stacy_thinking_hmm3 noloop
    sy "You know I love challenging myself."
    sy "If I never challenged myself, I'd never grow or change."
    scene sm1cs-mh008-203-c2-sy-talk with dissolve
    play voice4 stacy_disappointed_oh1 noloop
    sy "I'd just be some stock character in the background of everyone's lives."
    sy "And I am definitely not a background character."
    scene sm1cs-mh008-204-c2-mc-talk-sy with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "You can say that again."
    scene sm1cs-mh008-205-c2-sy-talk-mc with dissolve
    play voice4 stacy_yes_yap1 noloop
    sy "But you two get it. You both also have big main character energy."
    scene sm1cs-mh008-206-c2-mh-talk-sy with dissolve
    play voice3 dahlia_thinking_hmm4 noloop
    mh "Hmmm?"
    scene sm1cs-mh008-207-c2-sy-talk-mh with dissolve
    play voice4 stacy_thinking_emm4 noloop
    sy "You know, like... erm, you're both the author of your own worlds, you know?"
    sy "You're both strong, capable people. If you want something, you go out and get it. If something needs to get done, you do it."
    sy "And neither of you are ever the second player."
    scene sm1cs-mh008-208-c2-mh-talk-sy with dissolve
    play voice3 dahlia_disappointed_hmm2 noloop
    mh "Well, sometimes..."
    scene sm1cs-mh008-209-c2-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Uhhhh, this might get awkward. I need to change the subject."
    scene sm1cs-mh008-210-mc-talk with dissolve
    play voice2 mc_disappointed_ehh3 noloop
    mc "I... I have something I'm scared of."
    scene sm1cs-mh008-211-c2-sy-talk-mc with dissolve
    play voice4 stacy_surprised_huh1 noloop
    if persistent.is_special:
        sy "Really, bro?"
    else:
        sy "Really, [mcname]?"
    scene sm1cs-mh008-212-mh-talk-mc with dissolve
    play voice3 dahlia_arrogant_yeah noloop
    mh "Oh yeah? And what's that."
    scene sm1cs-mh008-213-mc-talk with dissolve
    play voice2 mc_disgust_ooh2 noloop
    mc "I'm... I'm afraid of peanut butter getting stuck to the roof of my mouth."
    scene sm1cs-mh008-214-mh-talk-mc with dissolve
    play voice3 dahlia_surprised_what noloop
    mh "Excuse me... you're afraid of..."
    scene sm1cs-mh008-215-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Peanut butter getting stuck to the roof of my mouth. Yeah."
    mc "Because I'm going to be eating, like, a PB and J, and someone is going to try and talk to me."
    play sound sfx_cloth_rustling2
    scene sm1cs-mh008-216-mc-talk-mh with dissolve
    play voice2 mc_angry_oof noloop
    mc "And then I'm going to have peanut butter in my mouth, and I won't be able to talk."
    mc "Or it'll sound super weird and that scares me!"
    scene sm1cs-mh008-217-mh-talk with dissolve
    play voice3 dahlia_disappointed_ehh3 noloop
    mh "I, uhm - uhm-"
    scene sm1cs-mh008-218-c2-sy-talk-mc with dissolve
    play voice3 stacy_arrogant_laugh1 noloop
    sy "You're fucking with us, right?"
    scene sm1cs-mh008-219-c2-mc-talk-sy with dissolve
    play voice2 mc_no_no4 noloop
    mc "No! I'm seriously afraid of it-"
    scene sm1cs-mh008-220-mc-talk with dissolve
    play voice2 d1s5_mchappy noloop
    mc "What! It's a very real fear!"
    scene sm1cs-mh008-221-mh-talk with dissolve
    play voice3 dahlia_happy_laugh5 noloop
    mh "Hahahahaha!"
    scene sm1cs-mh008-222-c2-sy-talk with dissolve
    play voice4 stacy_happy_laugh4 noloop
    sy "Hahahahahahahaha! No fucking way!"
    scene sm1cs-mh008-223-c2-sy-talk-mc with dissolve
    play voice4 stacy_angry noloop
    sy "That's the most ridiculous thing I've ever heard, [mcname]!"
    scene sm1cs-mh008-224-mc-talk with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "And what, you two are totally fearless?!"
    scene sm1cs-mh008-225-c2-sy-talk-mc with dissolve
    play voice4 stacy_no_simple1 noloop
    sy "No, I already told you I'm scared of heights. But that one makes sense."
    sy "Because if you fall from super high up, that's it for you."
    sy "My fear makes sense. Yours is just insane!"
    scene sm1cs-mh008-226-c2-mc-talk-sy with dissolve
    play voice2 mc_no_uhuhno noloop
    mc "Is not!"
    scene sm1cs-mh008-227-c2-sy-talk with dissolve
    play voice4 stacy_yes_fine4 noloop
    sy "Suuuuuuuuuure."
    scene sm1cs-mh008-228-mh-talk-mc with dissolve
    play voice3 lissa_lno noloop
    mh "And no, I wouldn't say that I'm not scared of anything. I used to get really bad vertigo, but I think I've finally gotten over that."
    scene sm1cs-mh008-229-c2-sy-talk with dissolve
    play voice4 stacy_hey_happy2 noloop
    sy "And that one totally makes sense! Heights are spooky!"
    scene sm1cs-mh008-230-c2-mh-talk-sy with dissolve
    play voice3 dahlia_yes_simple noloop
    mh "Yes, heights are definitely spooky."
    mh "And I wouldn't say I'm scared of clowns, I just have an... aversion to them."
    scene sm1cs-mh008-232-c2-sy-talk-mh with dissolve
    play voice4 stacy_suckmoan1 noloop
    sy "Mmmm.{w} You know, I think clowns are actually kind of sexy."
    scene sm1cs-mh008-233-c2-mh-talk-sy with dissolve
    play voice3 dahlia_arrogant_ha noloop
    mh "Really?"
    scene sm1cs-mh008-234-c2-sy-talk with dissolve
    play voice4 stacy_thinking_well1 noloop
    sy "Well... the right kind of clown."
    scene sm1cs-mh008-235-c2-mc-talk with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "We know someone who's made a clown porn video or two."
    mc "I think it secretly unlocked a weird kink in Stacy's brain."
    scene sm1cs-mh008-236-c2-sy-talk-mc with dissolve
    play voice4 stacy_hey_angry1 noloop
    sy "Hey!"
    scene sm1cs-mh008-237-c2-mc-talk-sy with dissolve
    play voice2 mc_surprised_uh1 noloop
    mc "Am I wrong?"
    scene sm1cs-mh008-238-c2-sy-talk-mc with dissolve
    play voice4 ["<silence 0.4>", stacy_no_simple2] noloop
    sy "...{w} No."
    scene sm1cs-mh008-239-c2-mh-talk-sy with dissolve
    play voice3 lissa_hey noloop
    mh "Hey, maybe I just haven't met the right clowns."
    scene sm1cs-mh008-240-c2-sy-talk-mh with dissolve
    play voice4 stacy_thinking_oh2 noloop
    sy "Oh, I can totally introduce you! Taisia is a little freak, and-"
    scene sm1cs-mh008-241-c2-mc-talk-sy with dissolve
    play voice2 mc_disappointed_ehh1 noloop
    mc "Stacy, let's maybe not talk about clown porn right now."
    scene sm1cs-mh008-242-c2-sy-talk-mc with dissolve
    play voice4 stacy_angry_breath1 noloop
    sy "Uggghhhhh, fiiiiiiiiiiiine."
    scene sm1cs-mh008-243-c2-sy-talk-mh with dissolve
    play voice4 stacy_arrogant_hmm3 noloop
    sy "But I will totally send you a link later."
    scene sm1cs-mh008-244-c2-mh-talk-sy with dissolve
    play voice3 lissa_laugh noloop
    mh "Hehehehe."
    scene sm1cs-mh008-245-mc-talk-mh with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "But there's only one clown to be afraid of."
    scene sm1cs-mh008-246-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_oh noloop
    mh "Oh yeah? And which one is that?"
    scene sm1cs-mh008-247-mc-talk-mh with dissolve
    play voice2 mc_arrogant_hm2 noloop
    mc "Donald. MacDonald."
    scene sm1cs-mh008-248-mh-talk-mc with dissolve
    play voice3 dahlia_surprised_ah2 noloop
    mh "Like... the mascot for the fast food place?"
    scene sm1cs-mh008-249-c2-sy-talk-mc with dissolve
    play voice4 stacy_arrogant_huh4 noloop
    sy "Didn't Taisia scare the shit out of you when she was in her clown makeup?"
    scene sm1cs-mh008-250-c2-mc-talk-sy with dissolve
    play voice2 mc_no_nah1 noloop
    mc "That was a jump scare, I wasn't scared because she was a clown."
    mc "The only clown to fear, is Donald MacDonald."
    scene sm1cs-mh008-251-mc-talk-mh with dissolve
    play voice2 mc_yes_yes4 noloop
    mc "Yes. He's the most lethal clown in history."
    mc "He's killed more people than Gacy."
    scene sm1cs-mh008-252-mh-talk-mc with dissolve
    play voice3 dahlia_thinking_hmm1 noloop
    mh "You know... you've got a good point there."
    scene sm1cs-mh008-253-c2-sy-talk-mc with dissolve
    play voice4 stacy_thinking_hmm2 noloop
    sy "I've never really thought about it like that..."
    scene sm1cs-mh008-254-mc-talk with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "And he just looks creepy as hell."
    scene sm1cs-mh008-255-mh-talk-mc with dissolve
    play voice3 lissa_haha2 noloop
    mh "Hehehe - yeah, you're not wrong there either."
    scene sm1cs-mh008-256-mh-talk with dissolve
    play voice3 dahlia_surprised_wow noloop
    mh "Wow... sometimes I forget how beautiful Crowning is..."
    scene sm1cs-mh008-257-c2-sy-talk with dissolve
    play voice4 stacy_happy_relief1 noloop
    sy "Right? You can just... forget that we're actually pretty lucky."
    scene sm1cs-mh008-258-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah, the sights are really something..."
    scene sm1cs-mh008-259-c2-mc-talk-sy with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mc "Yeah.{w} They really are..."
    scene sm1cs-mh008-260-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "You're not even looking out at the city, [mcname]."
    scene sm1cs-mh008-261-mc-talk-mh with dissolve
    play voice2 mc_surprised_why1 noloop
    mc "Why would I do that?"
    scene sm1cs-mh008-262-mc-talk-mh with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "Because, as far as I'm concerned, the most beautiful thing I could be looking at, is you, Lyssa."
    scene sm1cs-mh008-263-mh-talk-mc with dissolve
    play voice3 lissa_shyoh noloop
    mh "Oh, you..."
    play sound2 sfx_cloth_rustling4 volume 1.5 noloop
    scene sm1cs-mh008-264-mc-mh-kiss with dissolve
    play voice2 d1s5_orgasm noloop
    play voice3 lissa_mmm2 noloop
    play sound mc_kiss2
    pause
    scene sm1cs-mh008-265-c2-mc-talk-sy with dissolve
    play voice2 mc_happy_a1 noloop
    mc "And I'm the luckiest man in the world, to be sitting here with you, too, Stacy."
    scene sm1cs-mh008-266-c2-sy-talk-mc with dissolve
    play voice4 stacy_disappointed_oh5 noloop
    sy "Oh, all romantic now, are we?"
    scene sm1cs-mh008-267-c2-mc-talk-sy with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "Stacy?"
    scene sm1cs-mh008-268-c2-sy-talk-mc with dissolve
    play voice4 stacy_yes_yeah1 noloop
    sy "Yeah?"
    play sound sfx_cloth_rustling3
    scene sm1cs-mh008-269-c2-mc-talk-sy with dissolve
    play voice2 mc_disappointed_ehh2 noloop
    mc "Shut up, before you ruin the moment."
    scene sm1cs-mh008-270-c2-sy-talk-mc with dissolve
    play voice4 stacy_thinking_emm2 noloop
    sy "Wait-"
    play sound2 sfx_cloth_rustling4 noloop volume 1.7
    scene sm1cs-mh008-271-c2-mc-sy-kiss with dissolve
    play voice2 d1s5_orgasm2 noloop
    play voice3 stacy_suckmoan3 noloop
    play sound dahlia_kiss_french1
    sy "Mmmmm."
    scene sm1cs-mh008-272-c2-mc-talk-sy with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "That trick always works."
    scene sm1cs-mh008-273-c2-sy-talk-mc with dissolve
    play voice4 stacy_laugh4 noloop
    sy "It's a good trick."
    play sound sfx_cloth_rustling5
    scene sm1cs-mh008-275-c2-mc-mh-sy with dissolve
    pause
    scene sm1cs-mh008-277-c2-mc-talk with dissolve
    play voice2 d2s12_emmm noloop
    mc "I-"
    scene sm1cs-mh008-279-c2-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "[mcname]?"
    scene sm1cs-mh008-281-c2-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    scene sm1cs-mh008-283-c2-mh-talk-mc with dissolve
    play voice3 lissa_moan1 noloop
    mh "Let's just enjoy this moment."
    scene sm1cs-mh008-285-c2-mc-talk-mh with dissolve
    play voice2 d9s2_ugu noloop
    mct "When she's right. She's right."
    jump sm1cs_mh008_throuple_carousel_end
label sm1cs_mh008_throuple_carousel_end:
    play sound5 sfx_amusement_park_ambience fadein 2.0 volume 0.4
    stop sound3 fadeout 2.0
    play sound4 sfx_parknight_crickets fadein 2.0 volume 0.5
    play sound sfx_heels_steps1 loop
    play sound2 sfx_heels_steps2
    scene sm1cs-mh008-287-c2-mc-mh-sy with Fade(0.5, 0.5, 0.5)
    pause
    stop sound2 fadeout 1.0
    stop sound fadeout 1.0
    scene sm1cs-mh008-288-mh-talk-mc with dissolve
    play voice3 dahlia_happy_phew noloop
    mh "That was... truly wonderful, [mcname]."
    mh "Another wonderful carnival memory to add to the others."
    scene sm1cs-mh008-289-c2-sy-talk with dissolve
    play voice4 stacy_yes_yeah2 noloop
    sy "Yeah, that was incredible."
    scene sm1cs-mh008-290-mc-talk with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I couldn't think of anyone I'd rather be up there with than you two."
    scene sm1cs-mh008-291-mh-talk with dissolve
    play voice3 dahlia_disappointed_ehh2 noloop
    mh "I hate to cut this short, but I do have a meeting in the morning that I have to make."
    scene sm1cs-mh008-292-c2-sy-talk-mh with dissolve
    play voice3 stacy_disgust_oh1 noloop
    sy "Boooo!"
    scene sm1cs-mh008-293-mc-talk-mh with dissolve
    if gt.next_day in [SATURDAY, SUNDAY]:
        play voice2 mc_thinking_wait1 noloop
        mc "Wait, isn't it the weekend?"
        scene sm1cs-mh008-294-mh-talk-mc with dissolve
        play voice3 lissa_ugu2 noloop
        mh "When you work as a solo practitioner, you're never guaranteed weekends off."
    else:
        play voice2 mc_happy_oof3 noloop
        mc "Oh shit, it's a work night, isn't it?"
        scene sm1cs-mh008-294-mh-talk-mc with dissolve
        play voice3 lissa_ugu2 noloop
        mh "That it is."
    scene sm1cs-mh008-296-mc-talk-mh with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "In that case, I'm glad you had a great night, Lyssa."
    scene sm1cs-mh008-297-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm2 noloop
    mh "There is... one more thing you could do to make tonight phenomenal."
    scene sm1cs-mh008-298-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Oh yeah? And what's that?"
    scene sm1cs-mh008-299-mh-talk-mc with dissolve
    play voice3 dahlia_disappointed_hmm1 noloop
    mh "Kiss me."
    scene sm1cs-mh008-300-mc-talk-mh with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Don't mind if I do."
    play sound2 sfx_throw_something1 noloop volume 1.5
    scene sm1cs-mh008-301-mc-mh-kiss with dissolve
    play voice2 mc_angry_errr8 noloop
    play voice3 lissa_mmm2 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-mh008-302-mh-talk-mc with dissolve
    play voice3 dahlia_happy_hmm1 noloop
    mh "Mmmmm... perfect, [mcname]."
    mh "That was... a hell of a kiss."
    scene sm1cs-mh008-304-mc-talk-mh with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, when you say \"phenomenal\" and \"kiss\", I have to give you the maximum effort kiss, right?"
    scene sm1cs-mh008-305-mh-talk-mc with dissolve
    play voice3 lissa_yes noloop
    mh "Yes, you do."
    mh "And I'm going to be holding you to that, [mcname]."
    scene sm1cs-mh008-306-mc-talk-mh with dissolve
    play voice2 mc_yes_ugu1 noloop
    mc "Good."
    scene sm1cs-mh008-307-c2-sy-talk with dissolve
    play voice4 stacy_disappointed_oh2 noloop
    sy "Well, I want one too!"
    scene sm1cs-mh008-308-c2-mc-talk-sy with dissolve
    play voice2 mc_yes_okay3 noloop
    if persistent.is_special:
        mc "Anything for you, dear sister."
    else:
        mc "Anything for my best friend."
    play sound2 sfx_cloth_rustling4 noloop
    scene sm1cs-mh008-309-c2-mc-sy-kiss with dissolve
    play voice2 mc_angry_errr7 noloop
    play voice4 stacy_suckmoan3 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-mh008-310-c2-sy-talk-mc with dissolve
    play voice4 stacy_hey_attention1 noloop
    sy "Wait... I wanted, like, a whole production with my kiss."
    scene sm1cs-mh008-311-c2-mh-talk-mc with dissolve
    play voice3 dahlia_yes_yeah3 noloop
    mh "Yeah, something like this, [mcname]"
    play sound sfx_throw_something1
    play sound2 sfx_sand_jump1 noloop
    play sound3 sfx_skirt_off2 noloop
    scene sm1cs-mh008-312-c2-sy-talk-mh with dissolve
    play voice4 stacy_scared_ah4 noloop
    sy "Woah - Lyssa!"
    scene sm1cs-mh008-313-c2-mh-talk-sy with dissolve
    play voice3 dahlia_yes_ugu noloop
    mh "Just go with it, Stacy."
    scene sm1cs-mh008-314-c2-mh-sy-kiss with dissolve
    play voice3 lissa_mmm2 noloop
    play voice4 stacy_suckmoan1 noloop
    play sound dahlia_kiss_french1
    pause
    scene sm1cs-mh008-315-c2-mc-inner-talk with dissolve
    play voice2 mc_angry_errr5 noloop
    mct "Holy shit... that's hot."
    play sound sfx_sand_down1
    scene sm1cs-mh008-316-c2-sy-talk-mh with dissolve
    play voice4 stacy_surprised_ohmy1 noloop
    sy "Wow..."
    scene sm1cs-mh008-317-mh-talk-mc with dissolve
    play voice3 lissa_moan3 noloop
    mh "All right, I do need to go though. I hope I see you soon, [mcname]."
    scene sm1cs-mh008-318-mc-talk-mh with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "You will! I have to show you the new studio now that it's done!"
    scene sm1cs-mh008-319-mh-talk-mc with dissolve
    play voice3 lissa_ugu noloop
    mh "Sounds like a date to me."
    scene sm1cs-mh008-320-c2-sy-talk-mc with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "[mcname]?"
    play voice2 mc_arrogant_heh2 noloop
    mc "Yeah?"
    scene sm1cs-mh008-322-c2-sy-talk-mc with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "I need you to help me home. My legs are jelly and I'm scared I'm going to collapse any second now."
    scene sm1cs-mh008-323-c2-mc-talk-sy with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "All right, come on. Let's get you home."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mh008-324-c2-sy-talk-mc with dissolve
    play voice4 stacy_happy_hmm1 noloop
    sy "Thank yoooooouuuuu..."
    scene sm1cs-mh008-325-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop
    mct "I honestly couldn't have planned a better date than this."
    stop sound fadeout 1.0
    jump sm1cs_mh008_end_scene
label sm1cs_mh008_end_scene:
    stop music fadeout 3.0
    stop sound2 fadeout 2.0
    stop sound3 fadeout 2.0
    stop sound4 fadeout 2.0
    stop sound5 fadeout 2.0
    stop music2 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "music2" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(MH_STORY, 4, 0, 6)
    return