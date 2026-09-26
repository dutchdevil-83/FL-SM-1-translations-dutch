image sm1cs-ag003-glambot-1 = Movie(play = "images/FS_IT/AG/s003/anim/sm1cs-ag003-a72-2x-50fps.webm", start_image = "sm1cs-ag003-a72 ag-walk-glambot-00_i", image = "sm1cs-ag003-a72 ag-walk-glambot-80_i", loop = False)
label sm1cs_ag003:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music [music_starducks2_reverbed, music_starducks2_reverbed, music_starducks1_radio, music_starducks1_radio]
    scene sm1cs-ag003-01-coffee-shop with dissolve
    play sound sfx_keyboard_typing2 volume 1.6
    pause
    play sound2 sfx_heels_steps2
    scene sm1cs-ag003-02-mc-talk-ag with dissolve
    play voice2 d1s2_mchey noloop volume 1.5
    mc "Anna!"
    play sound sfx_cloth_planket2
    scene sm1cs-ag003-03-ag-talk-mc with dissolve
    play voice3 girl27_surprised_huh noloop
    ag "[mcname]!? What are you doing here?"
    stop sound2 fadeout 1.0
    scene sm1cs-ag003-04-mc-talk-ag with dissolve
    play voice2 d1s5_mchappy noloop volume 1.6
    if player.has_played_scene("sm1cs_ag003i"):
        mc "I asked Claire where you were."
    else:
        mc "I was just grabbing a cup of coffee and saw you."
    scene sm1cs-ag003-05-ag-talk-mc with dissolve
    play voice3 girl27_thinking_oh2 noloop
    ag "Oh..."
    scene sm1cs-ag003-06-mc-talk-ag with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "What are you doing here?"
    scene sm1cs-ag003-07-ag-talk-mc with dissolve
    play voice3 girl27_thinking_emm noloop
    ag "Erm, I just wanted to, you know, mix up where I was working. Get out of the office."
    scene sm1cs-ag003-08-mc-talk-ag with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh...{w} Is something going on in the office? Is April making fun of you again?"
    play sound sfx_cloth_rustling1
    scene sm1cs-ag003-09-ag-talk-mc with dissolve
    play voice3 girl27_no_nonono3 noloop
    ag "No, no. At least not more than usual. Erm... I just can feel, erm, cramped when I'm in the office."
    scene sm1cs-ag003-10-mc-inner-talk with dissolve
    play voice2 d1s1_mmm noloop volume 1.7
    mct "Man, she is acting super strange... Something has to be up, right?"
    scene sm1cs-ag003-11-mc-talk-ag with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "So, uh, what are you working on? Bug checking, or-"
    play sound sfx_skirt_off1
    scene sm1cs-ag003-12-ag-talk-mc with dissolve
    play voice3 girl27_yes_ya noloop
    ag "Yep! That's what it is! Bugs! All bugs!"
    scene sm1cs-ag003-13-mc-talk-ag with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Is it April's code that's buggy? God, I want her code to be bad."
    play sound sfx_gadgets_laptop_closed
    scene sm1cs-ag003-14-ag-talk-mc with dissolve
    play voice3 girl27_no_nope1 noloop
    ag "Nope!"
    scene sm1cs-ag003-15-ag-talk-mc with dissolve
    play voice3 girl27_disappointed_ehh2 noloop
    ag "It's uhm... my code. Yeah, my code is the problem."
    scene sm1cs-ag003-16-mc-talk-ag with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Okaaaayy..."
    scene sm1cs-ag003-17-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Man... she is being really, really weird. Something is {b}definitely{/b} up."
    scene sm1cs-ag003-18-ag-talk-mc with dissolve
    play voice3 girl27_disappointed_emm noloop
    ag "Sorry, I just, uhm, don't want anyone to see it before it's done."
    ag "My code."
    scene sm1cs-ag003-19-mc-talk-ag with dissolve
    play voice2 mc_yes_aga1 noloop
    mc "Uh huh..."
    play sound sfx_heels_steps1
    scene sm1cs-ag003-20-cs-talk-mc with dissolve
    stop sound fadeout 1.0
    play voice4 girl37_hey_simple noloop
    cs "Welcome to Starducks. Can I take your order?"
    scene sm1cs-ag003-21-mc-talk-cs with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mc "Uhm, sure-"
    scene sm1cs-ag003-22-cs-talk-mc with dissolve
    play voice4 girl37_yes_yeah noloop
    cs "Black coffee, right?"
    scene sm1cs-ag003-23-mc-talk-cs with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Yeah, that sounds great."
    scene sm1cs-ag003-24-mc-inner-talk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "How does she remember my order?"
    play sound sfx_heels_steps1
    scene sm1cs-ag003-25-cs-talk-mc with dissolve
    play voice4 girl37_yes_yep noloop
    cs "That'll be right up!"
    stop sound fadeout 2.0
    scene sm1cs-ag003-25-mc-talk-cs with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Sooo... while I wait for my coffee, can I sit with you?"
    scene sm1cs-ag003-26-cs-talk-mc with dissolve
    play voice3 girl27_disappointed_eh1 noloop
    ag "Erm..."
    ag "Yeah, that's fine. Totally fine."
    play sound sfx_cloth_rustling3
    scene sm1cs-ag003-27-mc-inner-talk with dissolve
    play voice2 mc_surprised_uh1 noloop
    mct "What has gotten into Anna? Is this because of the hug after drinks the other day?"
    scene sm1cs-ag003-28-ag-talk-mc with dissolve
    play voice3 girl27_hey_serious noloop
    ag "[mcname]?"
    scene sm1cs-ag003-29-mc-talk-ag with dissolve
    play voice2 mc_yes_yeah8 noloop
    mc "Yeah?"
    scene sm1cs-ag003-30-ag-talk-mc with dissolve
    play voice3 girl27_happy_relief3 noloop
    ag "Can you... not mention seeing me here to anyone?"
    scene sm1cs-ag003-31-mc-talk-ag with dissolve
    play voice2 mc_yes_okay1 noloop
    mc "Uhm... okay?"
    scene sm1cs-ag003-32-ag-talk-mc with dissolve
    play voice3 girl27_disappointed_ah1 noloop
    ag "It's just... this is where I come when I want to be alone, you know? I don't want Nari or April to come here and start asking me questions."
    scene sm1cs-ag003-33-mc-talk-ag with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, I can understand that."
    mc "Don't worry, your secret is safe with me."
    scene sm1cs-ag003-34-ag-talk-mc with dissolve
    play voice3 girl27_happy_yeah4 noloop
    ag "Thanks, [mcname]. I appreciate it."
    scene sm1cs-ag003-35-mc-talk-ag with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "Of course."
    mc "Do you really get work done here?"
    scene sm1cs-ag003-36-ag-talk-mc with dissolve
    play voice3 girl27_arrogant_huh1 noloop
    ag "What do you mean?"
    scene sm1cs-ag003-37-mc-talk-ag with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "It just feels like the coffee shop could be filled with a lot of distractions."
    scene sm1cs-ag003-38-ag-talk-mc with dissolve
    play voice3 girl27_surprised_oh2 noloop
    ag "Oh, I don't mind that."
    scene sm1cs-ag003-39-mc-talk-ag with dissolve
    play voice2 mc_angry_really noloop
    mc "Really?"
    scene sm1cs-ag003-40-ag-talk-mc with dissolve
    play voice3 girl27_happy_yeah5 noloop
    ag "Yeah, it's kind of like gaming. There's always background noise and you need to block it out in order to keep moving forward."
    ag "The distractions actually kind of help me out."
    scene sm1cs-ag003-41-mc-talk-ag with dissolve
    play voice2 mc_arrogant_huh3 noloop
    mc "Huh, I guess I never thought about it that way."
    scene sm1cs-ag003-42-ag-talk-mc with dissolve
    play voice3 girl27_yes_ugu1 noloop
    ag "Yeah, I'm a little bit weird like that..."
    scene sm1cs-ag003-43-mc-talk-ag with dissolve
    play voice2 mc_no_no2 noloop
    mc "No, it's not weird at all! Just... different."
    scene sm1cs-ag003-44-ag-talk-mc with dissolve
    play voice3 girl27_thinking_hmm noloop
    ag "You know what a synonym for weird is, right?"
    scene sm1cs-ag003-45-mc-talk-ag with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, that's not what I meant."
    play sound sfx_cloth_rustling2
    scene sm1cs-ag003-46-ag-talk-mc with dissolve
    play voice3 girl27_happy_laugh6 noloop
    ag "I know, I'm just teasing you a bit."
    scene sm1cs-ag003-47-mc-talk-ag with dissolve
    play voice2 mc_arrogant_heh3 noloop
    mc "Ha ha, Anna."
    scene sm1cs-ag003-48-ag-talk-mc with dissolve
    play voice3 girl27_thinking_hmm5 noloop
    ag "But seriously, the distractions help, and the coffee is better here."
    scene sm1cs-ag003-49-mc-talk-ag with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Yeah, but that's a pretty low bar. I think if I scooped up some dirt on my way to work, it would be a better cup of coffee."
    scene sm1cs-ag003-50-ag-talk-mc with dissolve
    play voice3 girl27_happy_laugh1 noloop
    ag "Hahahaha! You might be right!"
    scene sm1cs-ag003-51-mc-talk-ah with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "God, who even makes the coffee at the office?"
    scene sm1cs-ag003-52-ag-talk-mc with dissolve
    play voice3 girl27_arrogant_ha noloop
    ag "Take a guess."
    scene sm1cs-ag003-53-mc-talk-ag with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Don't tell me..."
    scene sm1cs-ag003-54-ag-talk-mc with dissolve
    play voice3 girl27_yes_ugu2 noloop
    ag "Mmmhmmmm."
    scene sm1cs-ag003-55-mc-talk-ag with dissolve
    play voice2 mc_angry_off noloop
    mc "Is it Eugene?"
    scene sm1cs-ag003-56-ag-talk-mc with dissolve
    play voice3 girl27_yes_yap3 noloop
    ag "Yep!"
    scene sm1cs-ag003-57-mc-talk-ag with dissolve
    play voice2 mc_happy_yay2 noloop
    mc "That explains so much."
    play sound sfx_cloth_rustling5
    scene sm1cs-ag003-58-ag-talk-mc with dissolve
    play voice3 girl27_happy_laugh2 noloop
    ag "Hahahahaha! I knew you'd guess him!"
    scene sm1cs-ag003-60-mc-talk-ag with dissolve
    play voice2 mc_happy_hah1 noloop
    mc "Who else could take the worst coffee you could buy, and somehow make it even worse?"
    scene sm1cs-ag003-59-ag-talk-mc with dissolve
    play voice3 girl27_happy_laugh3 noloop
    ag "Hahahahahahaha!"
    scene sm1cs-ag003-61-ag-talk-mc with dissolve
    play voice3 girl27_hey_active noloop
    ag "You know, you're pretty funny, [mcname]."
    scene sm1cs-ag003-62-mc-talk-ag with dissolve
    play voice2 mc_surprised_uh3 noloop
    mc "Is this the part where you tell me I'm \"funny looking\" and turn me down for prom?"
    play sound sfx_cloth_rustling3
    scene sm1cs-ag003-63-ag-talk-mc with dissolve
    play voice3 girl27_surprised_what noloop
    ag "What. No! I would never!"
    ag "Is that how you got rejected for your prom?"
    scene sm1cs-ag003-64-mc-talk-ag with dissolve
    play voice2 mc_no_no6 noloop
    mc "No, I'm just teasing you Anna."
    ag "..."
    mc "What! You teased me for the weird thing, I had to get you back somehow."
    scene sm1cs-ag003-65-ag-talk-mc with dissolve
    play voice3 girl27_happy_nice4 noloop
    ag "Okay, fine. Truce?"
    scene sm1cs-ag003-66-mc-talk-ag with dissolve
    play voice2 mc_yes_yes3 noloop
    mc "Truce.{w}.{w}.{w} for now."
    scene sm1cs-ag003-67-ag-talk-mc with dissolve
    play voice3 girl27_disgust_ergh1 noloop
    ag "Be careful of what you wish for, [mcname]!"
    ag "Actually, [mcname], while we wait can you do me a huge favor?"
    scene sm1cs-ag003-68-mc-talk-ag with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Sure. What's up?"
    scene sm1cs-ag003-69-ag-talk-mc with dissolve
    play voice3 girl27_thinking_hmm3 noloop
    ag "Can you watch my stuff while I go to the bathroom?"
    scene sm1cs-ag003-70-mc-talk-ag with dissolve
    play voice2 mc_yes_yeah7 noloop
    mc "Yeah, that's not a problem."
    play sound sfx_cloth_planket2
    scene sm1cs-ag003-71-ag-talk-mc with dissolve
    play voice3 girl27_happy_relief1 noloop
    ag "Thanks! I've been... needing to use the ladies room for awhile, but I hate leaving my stuff unattended. I'll be right back!"
    play sound2 sfx_heels_steps1
    scene sm1cs-ag003-a72 ag-walk-glambot-00_i with dissolve
    pause
    play sound sfx_camera_fly1 volume 2.0
    stop sound2 fadeout 3.0
    scene sm1cs-ag003-glambot-1
    pause
    stop sound fadeout 3.0
    scene sm1cs-ag003-73-mc-look-around with dissolve
    pause
    scene sm1cs-ag003-74-ag-stuff with dissolve
    pause
    scene sm1cs-ag003-75-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "Hmmmm... all of Anna's stuff..."
    play sound sfx_cloth_rustling2
    scene sm1cs-ag003-76-mc-inner-talk with dissolve
    play voice2 mc_angry_errr7 noloop
    mct "Nope. I'm not going to snoop. I'm not going to snoop!"
    mct "That would be wrong!"
    scene sm1cs-ag003-77-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "But... maybe there's a clue as to why she's acting so weird..."
    mct "Maybe she's got hate mail... or a letter of review from Claire..."
    mct "And if I knew what was bothering her, I'd be able to help her with it..."
    play sound sfx_paper_slide1
    scene sm1cs-ag003-78-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm7 noloop
    mct "So, in a way... snooping is kind of the right thing to do. Right?"
    mct "Yeah... yeah, it totally is..."
    scene sm1cs-ag003-79-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm6 noloop
    mct "There's probably something on her laptop-"
    mct "Wait, Anna works in IT. There's no way her laptop doesn't have a password on it."
    mct "Shit, there goes that idea..."
    scene sm1cs-ag003-80-mc-notice-backpack with dissolve
    play voice2 mc_thinking_hm noloop
    mc "Wait a sec... what's this?"
    scene sm1cs-ag003-81-mc-talk with dissolve
    play voice2 mc_thinking_mmm6 noloop
    mc "Maybe there's something in here?"
    play sound sfx_cloth_shuffle1
    scene sm1cs-ag003-82-mc-talk with dissolve
    stop sound fadeout 2.0
    play voice2 mc_thinking_hmm9 noloop
    mct "Oh, this is more of Anna's book porn... I didn't realize she would have more than one."
    mct "I wonder what the appeal is to reading porn."
    mct "Maybe I should give it a shot sometime."
    play sound sfx_skirt_off2
    scene sm1cs-ag003-83-mc-inner-talk with dissolve
    mct "And even more book porn... does she just, carry this with her wherever she goes?"
    play sound sfx_book_pushin1
    scene sm1cs-ag003-84-mc-inner-talk with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mct "I mean... anyone can find this. It's hard to delete the browsing history of a book..."
    play sound sfx_skirt_off2
    scene sm1cs-ag003-85-mc-inner-talk with dissolve
    mct "If it's just the smut... this might be a dead-"
    play sound sfx_paper_rustl1 volume 1.6
    scene sm1cs-ag003-86-mc-inner-talk with dissolve
    play voice2 mc_happy_yes1 noloop
    mct "Jackpot!"
    play sound sfx_book_closed1
    scene sm1cs-ag003-87-mc-inner-talk with dissolve
    stop sound fadeout 0.5
    play voice2 mc_thinking_hmm4 noloop
    mct "Okay, let's see... who the hell is \"Magnolia Fox\"?"
    mct "What else have we got here..."
    play sound sfx_paper_rustl2
    scene sm1cs-ag003-88-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mct "A few dates... is this a diary? Why does Anna have someone else's diary?"
    mct "This is a... travel journal for Magnolia..."
    mct "She's in... Transylvania?"
    scene sm1cs-ag003-89-mc-inner-talk with dissolve
    play voice2 mc_surprised_uh2 noloop
    mct "What the hell did I just find?"
    play sound sfx_paper_rustl3
    scene sm1cs-ag003-90-mc-inner-talk with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mct "Let's skip ahead a bit..."
    mct "Magnolia is in a castle... owned by some... \"hot recluse\"..."
    mct "Skipping ahead, skipping ahead..."
    mct "Okay, it's the middle of the night, and..."
    scene sm1cs-ag003-91-mc-inner-talk with dissolve
    play voice2 mc_happy_wow1 noloop
    mct "Woah. That's... that's a pretty detailed description of Magnolia's pussy..."
    mct "She's... horny, and masturbating, and..."
    scene sm1cs-ag003-92-ag-talk with dissolve
    play voice2 mc_angry_hm1 noloop
    mct "Wait, the recluse... he's watching her. He's watching her lust, and-"
    play sound sfx_leg_kick7
    play voice3 girl27_surprised_ah2 noloop
    scene sm1cs-ag003-93-ag-talk-cs with hpunch
    ag "{size=*0.6}Oh, I am so sorry!{/size}"
    ag "I didn't mean to bump into you, my apologies!"
    scene sm1cs-ag003-94-cs-talk-ag with dissolve
    play voice4 girl37_no_nah noloop
    cs "It's all good, don't worry about it!"
    play sound sfx_book_closed1
    scene sm1cs-ag003-95-mc-inner-talk with dissolve
    play voice2 mc_pain_mff2 noloop
    mct "Oh shit! Anna's coming back! Shit, I need to-"
    play sound sfx_heels_steps1 loop
    scene sm1cs-ag003-96-ag-talk-mc with dissolve
    play voice3 girl27_hey_expressive noloop
    ag "[mcname]!"
    stop sound fadeout 1.0
    scene sm1cs-ag003-97-ag-talk-mc with dissolve
    play voice3 girl27_happy_relief2 noloop volume 0.85
    ag "Thank you for watching my things."
    scene sm1cs-ag003-98-mc-talk-ag with dissolve
    play voice2 d1s5b_emmm noloop volume 1.5
    mc "Erm, yeah! Not, uh, not a problem, Anna!"
    play sound sfx_cloth_rustling4
    scene sm1cs-ag003-99-ag-talk-mc with dissolve
    play voice3 girl27_arrogant_huh4 noloop
    ag "Everything okay? Did something happen while I was in the bathroom?"
    scene sm1cs-ag003-100-mc-talk-ag with dissolve
    play voice2 mc_no_nope2 noloop
    mc "Nope! Everything is fine!"
    play sound sfx_heels_steps2
    scene sm1cs-ag003-101-cs-talk-mc with dissolve
    stop sound fadeout 2.0
    play voice4 girl37_hey_happy3 noloop
    cs "And here you are! One black coffee."
    play sound sfx_skirt_off2
    scene sm1cs-ag003-102-mc-talk-cs with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Thank you!"
    scene sm1cs-ag003-103-cs-talk-mc with dissolve
    play voice4 girl37_yes_happy noloop
    cs "Not a problem."
    scene sm1cs-ag003-104-mc-talk-ag with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I just, uhm, got a call from Claire is all. She wants me back at the office."
    scene sm1cs-ag003-105-ag-talk-mc with dissolve
    play voice3 girl27_thinking_oh3 noloop
    ag "Well, you shouldn't keep her waiting. Claire can be... well, intense about work stuff."
    scene sm1cs-ag003-106-mc-talk-ag with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "Yep! That's why I'm so nervous all of a sudden."
    play sound sfx_gadgets_laptop_opened
    scene sm1cs-ag003-107-ag-talk-mc with dissolve
    play voice3 girl27_yes_aga noloop
    ag "Uh huuuuuuuh..."
    scene sm1cs-ag003-108-mc-talk-ag with dissolve
    play voice2 mc_hey_bye1 noloop
    mc "Anyways, I should get going! I'll see you later, Anna!"
    play sound sfx_heels_steps2 loop
    scene sm1cs-ag003-109-mc-inner-talk with dissolve
    play voice2 mc_angry_errr4 noloop
    mct "Shit. Shit, shit, shit. I just stole Anna's notebook... which I think she stole from someone."
    mct "I need to figure out a way to sneak it back into her bag..."
    mct "But I just came up with the worst excuse ever."
    scene sm1cs-ag003-110-mc-inner-talk with dissolve
    play voice2 d14s16_smell noloop
    mct "I guess... I'll figure something out."
    mct "In the meantime... I wonder what the hot recluse is going to do now that he's seen Magnolia fingering herself..."
    pause
    stop sound fadeout 1.0
    stop music fadeout 3.0
    stop sound2 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    jump sm1cs_ag003_exit_to_map
label sm1cs_ag003_exit_to_map:
    $ StoryController.end_scene(AG_STORY, 1, 0, 1)
    return