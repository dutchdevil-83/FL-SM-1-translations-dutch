label sm1fs_t006:
    $ renpy.music.set_volume(0.7, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_urban_funk1
    play sound sfx_door_openclosed1
    play sound4 sfx_wurst_del_inside_amb_day1 fadein 1.0
    play sound2 sfx_heels_steps1
    scene sm1fs_t006_1-01-wurst-delivery with dissolve
    pause
    scene sm1fs_t006_1-02-nr-talk-mc with dissolve
    play voice4 boy7_hey_simple noloop
    nr "Hey, [mcname]. Looking to make some deliveries?"
    stop sound2 fadeout 1.0
    scene sm1fs_t006_1-03-mc-talk-nr with dissolve
    play voice2 mc_no_nah2 noloop
    mc "Maybe later, Nelson."
    mc "I actually had a proposition for you."
    play sound sfx_keyboard_typing1 volume 2.0
    scene sm1fs_t006_1-04-nr-talk-mc with dissolve
    play voice4 boy7_disappointed_aah noloop
    nr "I hope it involves bratwurst or sausages. That's really all my mind can handle today."
    scene sm1fs_t006_1-05-mc-talk-nr with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Well I guess it kind of connects with brats."
    mc "Do you know the theater on Beeks Street?"
    scene sm1fs_t006_1-06-nr-talk-mc with dissolve
    play voice4 boy7_yes_yeah noloop
    nr "Yeah. I saw {i}Hairspray{/i} and {i}Four Seasons{/i} a couple of years ago."
    nr "Always have a good time checking out what the local thespians are up to."
    scene sm1fs_t006_1-07-mc-talk-nr with dissolve
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "That's great. I actually work for the theater troupe who runs the theater."
    mc "The Director is getting ready to announce a new play."
    scene sm1fs_t006_1-08-mas-talk-mc with dissolve
    play voice3 girl28_arrogant_hah3 noloop
    ms "Plays are just fuel for the fire to distract us from the elites having their hands in our wallets."
    play sound sfx_cloth_rustling2 volume 1.6
    scene sm1fs_t006_1-09-mc-talk-mas with dissolve
    play voice2 d1s2_hmm noloop volume 1.8
    mc "What about musicals?"
    scene sm1fs_t006_1-10-mas-talk-mc with dissolve
    play voice3 girl28_disgust_oeagh1 noloop
    ms "They're so much worse. Their song and dance numbers are all about rocking the boat, but where is the musical telling us to burn the whole rotten system down?"
    play voice3 girl28_surprised_huh noloop
    scene sm1fs_t006_1-10-mas-talk-mc with hpunch
    ms "Where is it, [mcname]?!"
    scene sm1fs_t006_1-11-mc-talk-mas with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "Uh... not sure."
    scene sm1fs_t006_1-12-mas-talk-mc with dissolve
    play voice3 girl28_arrogant_pff1 noloop
    ms "*scoffs* They're not going to get my money."
    ms "No freaking way."
    scene sm1fs_t006_1-13-mc-talk-nr with dissolve
    play voice2 d2s12_emmm noloop
    mc "Anyhow..."
    mc "The new show is being sponsored by Pizza World."
    scene sm1fs_t006_1-14-nr-talk-mc with dissolve
    play voice4 boy7_happy_mmm noloop
    nr "Ah Alfredo's place. Good for him."
    nr "He makes a mean pie."
    scene sm1fs_t006_1-15-mc-talk-nr with dissolve
    play voice2 mc_yes_yes7 noloop
    mc "I'll have to check it out one day. But like I was saying, Pizza World is sponsoring the new show."
    mc "We're doing a riff on Romeo and Juliet."
    mc "Instead of two rival families, we figured we could do a story about two rival restaurants."
    scene sm1fs_t006_1-16-nr-talk-mc with dissolve
    play voice4 boy7_arrogant_ha1 noloop
    nr "Hey. That's pretty clever."
    scene sm1fs_t006_1-17-mc-talk-nr with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Thanks. So since we already have one food place, I wanted to see if you'd like to sponsor the show."
    scene sm1fs_t006_1-18-nr-talk-mc with dissolve
    play voice4 boy7_thinking_oh noloop
    nr "Ah I see."
    nr "You want money, that's it."
    scene sm1fs_t006_1-19-mas-talk-nr with dissolve
    play voice3 girl28_arrogant_hah1 noloop
    ms "You just now figured that out?"
    scene sm1fs_t006_1-20-nr-talk-mas with dissolve
    play voice4 boy7_disappointed_mff noloop
    nr "Hush you."
    nr "Just keep swiping on Ember or playing your 'Majik: the Collecting' game."
    scene sm1fs_t006_1-21-mas-talk with dissolve
    play voice3 girl28_arrogant_hmm1 noloop
    ms "Told you. Hands in wallets."
    scene sm1fs_t006_1-22-nr-talk-mc with dissolve
    play voice4 boy7_disappointed_hmm noloop
    nr "So let me get this straight. You want to make a story of two star-crossed lovers, that ends in tragedy."
    nr "One character is from Pizza World, and the other would be from Wurst Delivery."
    scene sm1fs_t006_1-23-mc-talk-nr with dissolve
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah, that was the idea, Nelson. I figured that it would be a great way to drum up more business."
    scene sm1fs_t006_1-24-nr-talk-mc with dissolve
    play voice4 boy7_surprised_huh1 noloop
    nr "Drum up business? We're doing just fine."
    play sound sfx_weather_arctic_wind
    scene sm1fs_t006_1-25-tumble-weed with dissolve
    "*wind wistling*"
    stop sound fadeout 2.0
    scene sm1fs_t006_1-26-nr-talk-mas with dissolve
    play voice4 boy7_disappointed_eh noloop
    nr "Maya I asked you to clean that thing up."
    scene sm1fs_t006_1-27-mas-talk-nr with dissolve
    play voice3 girl28_yes_yeah2 noloop
    ms "It's too fast for me."
    scene sm1fs_t006_1-28-nr-talk-mc with dissolve
    play voice4 boy7_arrogant_hmm1 noloop
    nr "Alright, [mcname]. Maybe you're onto something."
    nr "Maybe it's time for a little virus marketing."
    scene sm1fs_t006_1-29-mc-talk-nr with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "I think you mean viral marketing. But I'm very happy you might be open to discussing things."
    scene sm1fs_t006_1-30-nr-talk-mc with dissolve
    play voice4 boy7_yes_aga1 noloop
    nr "Well, you hit the nail on the head. I definitely would need to discuss things with this Director of yours."
    nr "It sounds like you guys are tweaking the script a bit, but I want to make sure that no one is dying in the play because they work or eat at Wurst Delivery."
    scene sm1fs_t006_1-31-mc-talk-nr with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Of course. I don't think that was going to be an issue anyhow."
    mc "I'll go see Denise, the Director, and let her know you'll be reaching out."
    play sound sfx_cloth_rustling1
    play sound2 sfx_keyboard_typing1
    scene sm1fs_t006_1-32-mc-talk-nr with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Here is her number."
    play sound2 sfx_keyboard_enter1 noloop
    scene sm1fs_t006_1-33-nr-talk-mc with dissolve
    play voice4 boy7_yes_yep noloop
    nr "Nice nice."
    scene sm1fs_t006_1-34-mas-talk-mc with dissolve
    play voice3 girl28_arrogant_hmm3 noloop
    ms "Wurst Delivery is also going to need an entire row of tickets for each show. For free."
    scene sm1fs_t006_1-35-mc-talk-mas with dissolve
    play voice2 mc_surprised_what2 noloop
    mc "When did you?"
    scene sm1fs_t006_1-36-mas-talk-mc with dissolve
    play voice3 girl28_yes_confident noloop
    ms "If Nelson is going to be putting his money into this show of yours, he should get something more than just the hope that more people come to the store."
    scene sm1fs_t006_1-37-mc-talk-mas with dissolve
    play voice2 mc_surprised_ohmy noloop
    mc "Check out the big business brain on Maya."
    scene sm1fs_t006_1-38-nr-talk-mas with dissolve
    play voice4 boy7_angry_hmm noloop
    nr "Wait. This whole time you've said that you hate the theater."
    scene sm1fs_t006_1-39-mas-talk-nr with dissolve
    play voice3 girl28_yes_yap3 noloop
    ms "It's important not to let personal issues get in the way of good business. I learned that from all the assholes flying around on private jets."
    ms "We get those seats, and we can raffle them to customers who buy an order of twenty dollars or more."
    ms "It will be win-win, Nelson."
    scene sm1fs_t006_1-40-nr-talk-mas with dissolve
    play voice4 boy7_thinking_hmm2 noloop
    nr "I guess. I don't want to push this Miss Denise, too much."
    scene sm1fs_t006_1-41-mc-talk-nr with dissolve
    play voice2 mc_no_nono1 noloop
    mc "I'm sure Denise could lose one section of seats and not lose the farm."
    scene sm1fs_t006_1-42-mas-talk-mc with dissolve
    play voice3 girl28_yes_yeah4 noloop
    ms "Yeah she will, if she wants Wurst Delivery to sponsor the show."
    play sound sfx_hair_scratch1
    scene sm1fs_t006_1-43-mc-talk with dissolve
    menu:
        "We should talk business again sometime":
            $ player.set_choice("sm1fs_t006_talk_business")
            play voice2 mc_thinking_mmm7 noloop
            mc "We may have to put our heads together and brainstorm other business ideas, Maya."
            mc "You seem pretty good at this."
            scene sm1fs_t006_1-44-mas-talk-mc with dissolve
            play voice3 girl28_arrogant_hah4 noloop
            ms "Benefits of all those different classes I took that got me into such shitty student debt."
            ms "I know a little about just about everything."
            ms "And yeah, maybe we can get our heads together one day."
            ms "But right now, you should stay focused on landing this sponsorship deal."
            scene sm1fs_t006_1-45-mc-talk-mas with dissolve
            play voice2 mc_yes_yes1 noloop
            mc "Right."
        "Strange how involved you got":
            play voice2 mc_thinking_mmm7 noloop
            mc "Strange just how involved you got when you smelled money, Maya."
            scene sm1fs_t006_1-44-mas-talk-mc with dissolve
            play voice3 girl28_arrogant_hah4 noloop
            ms "Hah. I'm not involved, I'm just helping out Nelson."
            ms "And if he gives me ten percent of proceeds from the combo deals, well then everyone is happy."
            scene sm1fs_t006_1-45-mc-talk-mas with dissolve
            play voice2 mc_thinking_hmm8 noloop
            mc "So I shouldn'd expect to see you at the play when it's ready?"
            play voice3 girl28_disappointed_mmm2 noloop
            ms "No one knows the future, [mcname]."
            mc "Haha."
    play sound sfx_hair_scratch1
    scene sm1fs_t006_1-46-mc-talk-nr with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Alright, I'll get going and report back to Denise."
    mc "Thanks for hearing me out, Nelson. I think this sponsorship will go great."
    scene sm1fs_t006_1-47-mas-talk-mc with dissolve
    play voice3 girl28_surprised_oh noloop
    ms "Where are my 'thanks'?"
    play sound sfx_heels_steps1 loop
    scene sm1fs_t006_1-48-mc-talk-mas with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Come on, Maya. You're too cool to go sniffing around for gratitude."
    stop sound fadeout 1.0
    stop music fadeout 3.0
    stop sound4 fadeout 2.0
    $ renpy.music.set_volume(1.0, 0.5, "music" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    $ StoryController.end_scene(THEATER_STORY_LINE, 2, 0, 1)
    return