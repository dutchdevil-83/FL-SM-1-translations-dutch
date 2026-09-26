label sm1cs_ag001:
    $ renpy.music.set_volume(0.5, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound2" )
    $ renpy.music.set_volume(1.0, 0.0, "sound3" )
    play sound2 sfx_office_ambience1 fadein 2.0
    scene sm1cs-ag001-01-mc-walks with dissolve
    pause
    play music "<silence 1.0>"
    scene sm1cs-ag001-02-ag-talk-mc with dissolve
    queue music music_sunny_future
    play voice3 girl27_hey_interested noloop
    ag "Hello, [mcname]."
    scene sm1cs-ag001-03-mc-talk-ag with dissolve
    play voice2 d2s9_mchey noloop
    mc "Hey Anna. I just did the third planned ticket for the week."
    scene sm1cs-ag001-04-ag-talk-mc with dissolve
    play voice3 girl27_happy_great2 noloop
    ag "That's great. So you're enjoying your assignments?"
    scene sm1cs-ag001-05-mc-talk-ag with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "Not too bad. I've gotten pretty good at coding APIs."
    scene sm1cs-ag001-07-c1-ag-talk-mc with dissolve
    play voice3 girl27_happy_nice2 noloop
    ag "That's great. As we expand and take on new clients, we're going to need those modules like the protoss need pylons."
    scene sm1cs-ag001-06-c1-mc-talk-ag with dissolve
    menu:
        "Huh?"(hint="sm1cs_ag001_m01_h01"):
            play voice2 mc_surprised_what1 noloop
            mc "What?"
            play sound sfx_chair_slide1
            scene sm1cs-ag001-09-ag-talk-mc with dissolve
            play voice3 girl27_angry_cough2 noloop
            ag "Ahem. I just mean we'll be able to keep our platform nice and stable as we grow."
        "Totally"(hint="sm1cs_ag001_m01_h02"):
            call sm1cs_ag001_m01_c02 from _call_sm1cs_ag001_m01_c02
            play voice2 mc_happy_hah1 noloop
            mc "Haha. We just have to keep a couple of zealots ready in case the code tries to zerg rush us."
            mc "But today we're in good shape."
            play sound sfx_chair_slide1
            scene sm1cs-ag001-09-ag-talk-mc with dissolve
    play voice3 girl27_hey_greeting noloop
    ag "You know if this stuff is too easy for you, we can kick it up a notch."
    scene sm1cs-ag001-10-mc-talk-ag with dissolve
    play voice2 d1s2_hmm noloop volume 1.6
    mc "What do you mean?"
    scene sm1cs-ag001-11-ag-talk-mc with dissolve
    play voice3 girl27_thinking_hmm3 noloop
    ag "If you think you're up to it, we can send you more difficult databases to apply analytics to."
    ag "It should make your core assignments more difficult, but it will also mean better pay if you get them done right."
    scene sm1cs-ag001-12-c1-mc-talk-ag with dissolve
    play voice2 mc_yes_okay2 noloop
    mc "Cool. How would that work?"
    scene sm1cs-ag001-13-c1-ag-talk-mc with dissolve
    play voice3 girl27_disappointed_ah1 noloop
    ag "You just have to come to me and let me know."
    ag "I can even do it now if you want."
    scene sm1cs-ag001-14-c2-mc-talk-ag with dissolve
    menu:
        "Increase Job Difficulty"(hint="sm1cs_ag001_m02_h01"):
            call sm1cs_ag001_m02_c01 from _call_sm1cs_ag001_m02_c01
            play voice2 mc_yes_sure1 noloop
            mc "Sure, I can take on more work."
            scene sm1cs-ag001-15-c2-ag-talk-mc with dissolve
            play voice3 girl27_happy_great1 noloop
            ag "Great."
        "Do not increase Difficulty"(hint="sm1cs_ag001_m02_h02"):
            play voice2 mc_no_nah2 noloop
            mc "I think I'll pass for now."
            scene sm1cs-ag001-15-c2-ag-talk-mc with dissolve
            play voice3 girl27_yes_aga noloop
            ag "Okay. If you change your mind, let me know."
    scene sm1cs-ag001-16-ag-talk-mc with dissolve
    play voice3 girl27_happy_relief2 noloop
    ag "So, since I have you here, it's probably the perfect time for a little one-on-one chat."
    play sound sfx_heels_steps1
    scene sm1cs-ag001-17-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "Doesn't sound too bad to me."
    scene sm1cs-ag001-18-ag-talk-mc with dissolve
    play voice3 girl27_thinking_hmm5 noloop
    ag "You've been here a little bit, so as your team lead, I have a few questions and make sure you're settling in nicely."
    stop sound fadeout 1.0
    scene sm1cs-ag001-19-mj-talk-ag with dissolve
    play voice4 girl26_hey_sad noloop
    mj "Hey, Anna."
    scene sm1cs-ag001-20-ag-talk-mc with dissolve
    play voice3 girl27_disappointed_oh2 noloop
    ag "Megan. [mcname], have you met Megan?"
    scene sm1cs-ag001-21-mc-talk-ag with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "Not yet."
    play voice3 girl27_thinking_hmm2 noloop
    ag "She's great. She's actually in charge of our Quality Assurance team. Megan makes sure nothing bad remains when we're ready for distribution."
    mc "Cool."
    scene sm1cs-ag001-22-mj-talk-ag with dissolve
    play voice4 girl26_yes_aga noloop
    mj "Thanks. But we actually have a small problem, Anna."
    mj "My team managed to nail down that analytics error that was a real thorn in our butts.. Now I've got Jayden saying the stress test alerts are going off when we're at fifteen percent capacity."
    scene sm1cs-ag001-23-ag-talk-mj with dissolve
    play voice3 girl27_yes_yeah4 noloop
    ag "I'll come to check it out in a bit, Megan. I'm kind of busy right now."
    scene sm1cs-ag001-24-mj-talk-ag with dissolve
    play voice4 girl26_thinking_ehh2 noloop
    mj "Right. That's what I told Jayden. He thinks we should just double up the cluster and-"
    scene sm1cs-ag001-25-ag-talk-mj with dissolve
    play voice3 girl27_surprised_what noloop
    ag "What?"
    scene sm1cs-ag001-26-ag-talk-mj with dissolve
    play voice3 girl27_angry_argh1 noloop
    ag "Full stop. Jayden thinks that's a good idea?"
    ag "*sighs* Oh my god."
    scene sm1cs-ag001-27-ag-talk-mc with dissolve
    play voice3 girl27_thinking_emm4 noloop
    ag "[mcname], sorry, I need to stop a madman before he burns down the whole stack. Megan, with me."
    play sound sfx_heels_steps2 loop
    play sound3 sfx_heels_steps1
    scene sm1cs-ag001-28-mj-talk-ag with dissolve
    play voice4 girl26_yes_simple noloop
    mj "Yes."
    scene sm1cs-ag001-29-mc-talk with Dissolve(0.15)
    play voice2 mc_yes_aga1 noloop
    mc "I guess I'll wait here."
    stop sound fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-ag001-30-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mct "This is just part of the gig. Hurry up and wait."
    $ renpy.music.set_volume(1.0, 1.5, "music" )
    $ renpy.music.set_volume(0.2, 5.5, "sound2" )
    scene sm1cs-ag001-31-mc-waits with fade
    pause
    scene sm1cs-ag001-32-mc-inner-talk with fade
    play voice2 mc_thinking_mmm4 noloop
    mct "Where is she?"
    scene sm1cs-ag001-33-mc-waits with fade
    pause
    $ renpy.music.set_volume(0.6, 1.5, "music" )
    scene sm1cs-ag001-34-mc-talk with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Hmmm."
    scene sm1cs-ag001-35-mc-notice-magazine with dissolve
    pause
    play sound sfx_paper_rustl1
    scene sm1cs-ag001-36-magazine with dissolve
    pause
    play sound sfx_paper_slide1
    scene sm1cs-ag001-37-mc-open-magazine with dissolve
    pause
    scene sm1cs-ag001-38-mc-inner-talk with dissolve
    call sm1cs_ag001_add_gaming_topic from _call_sm1cs_ag001_add_gaming_topic
    play voice2 d1s5_mcthinks noloop volume 1.7
    if player.get_choice("sm1cs_ag001_confused") is True:
        mct "I didn't think Modern Gaming still made paper copies. I haven't read one of these since middle school."
        scene sm1cs-ag001-39-mc-inner-talk with dissolve
        mct "Oh cool. Call to Duty: Sud's Revenge is coming out."
        scene sm1cs-ag001-40-mc-inner-talk with dissolve
        play voice2 d3s11b_mcheh noloop
        mct "I like the originals best, but this new run has some baller multiplayer."
    else:
        mct "Looks like some sort of gamer magazine."
        scene sm1cs-ag001-39-mc-inner-talk with dissolve
        mct "The main article is on some game called Call to Duty: Sud's Revenge."
        scene sm1cs-ag001-40-mc-inner-talk with dissolve
        play voice2 d3s11b_mcheh noloop
        mct "I guess Anna is into gaming. Specifically FPSs."
    scene sm1cs-ag001-41-mc-purse with dissolve
    pause
    scene sm1cs-ag001-42-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm1 noloop
    mct "Now what do we have here?"
    scene sm1cs-ag001-43-mc-notice-purse with dissolve
    pause
    play sound sfx_paper_slide1
    scene sm1cs-ag001-44-mc-looks-around with dissolve
    pause
    scene sm1cs-ag001-45-mc-looks-around with dissolve
    pause
    play sound sfx_paper_rustl3
    scene sm1cs-ag001-46-mc-pulls-book with dissolve
    play voice2 mc_thinking_mmm1 noloop
    mct "Deep. Wet. Undercover."
    scene sm1cs-ag001-47-mc-inner-talk with Dissolve(0.15)
    mct "Mmmm. Just what are you reading, Anna?"
    play sound sfx_chair_slide1
    scene sm1cs-ag001-48-mc-inner-talk with dissolve
    pause
    scene sm1cs-ag001-49-am-talk-mc with dissolve
    play voice4 girl22_surprised_huh1 noloop
    am "What are you doing lurking by Anna's desk, perv?"
    scene sm1cs-ag001-50-mc-talk-am with dissolve
    play voice2 mc_angry_hm1 noloop
    mc "Nothing. Anna told me to wait here. Some kind of meeting."
    scene sm1cs-ag001-51-am-talk-mc with dissolve
    play voice4 girl22_yes_aga1 noloop
    am "Stop being a loser and get back to work."
    am "Standing around with your dick in your hands near Anna's desk is not going to make you a better coder."
    scene sm1cs-ag001-52-mc-talk-am with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Whatever."
    play sound sfx_cloth_rustling1
    scene sm1cs-ag001-53-mc-sighs with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.5
    mc "*sighs*"
    scene sm1cs-ag001-54-mc-inner-talk with dissolve
    mct "What is her deal?"
    $ renpy.music.set_volume(0.5, 6.5, "sound2" )
    scene sm1cs-ag001-55-mc-inner-talk with dissolve
    play sound sfx_mouse_clicks1 loop
    play voice2 mc_angry_hm2 noloop
    mct "I guess I {i}was{/i} snooping around Anna's desk."
    mct "Hmmm. I wonder how dirty that book Anna has is."
    play sound sfx_cloth_rustling1
    scene sm1cs-ag001-56-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "I shouldn't look it up."
    scene sm1cs-ag001-57-mc-inner-talk with dissolve
    mct "I really should just respect her privacy."
    scene sm1cs-ag001-58-mc-inner-talk with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mct "Buuuut... one little look won't hurt anyone."
    play sound sfx_keyboard_typing2 volume 1.5
    scene sm1cs-ag001-59-mc-inner-talk with dissolve
    play voice2 d9s2_ugu noloop volume 1.6
    mct "Deep. Wet. Undercover."
    scene sm1cs-ag001-60-mc-inner-talk with dissolve
    mct "The story of Eva Kingsley as she goes undercover in the salacious Marquis Club"
    mct "Will our hero be able to keep her resolve as she descends into a world of humiliation and debauchery?"
    scene sm1cs-ag001-61-mc-inner-talk with dissolve
    play voice2 mc_thinking_mmm2 noloop
    mct "This certainly deserves an Adults Only rating"
    scene sm1cs-ag001-62-mc-inner-talk with dissolve
    mct "Based on this, I think Anna might have been interested in Fetish Locator if it wasn't shut down"
    scene sm1cs-ag001-63-mc-inner-talk with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mct "I still shouldn't have looked. Now I know she's kinky, but it's not like I can walk up to her and say \"hey, I heard you're into humiliation porn\""
    scene sm1cs-ag001-65-mc-clicks-another-tab with dissolve
    play voice2 mc_scared_oh4 noloop
    mc "Oh cool, they're making a movie based on the book"
    scene sm1cs-ag001-64-ag-talk-mc with dissolve
    play voice3 girl27_hey_serious noloop
    ag "Hey [mcname]."
    play sound sfx_mouse_clicks1 volume 2.0
    scene sm1cs-ag001-66-ag-talk-mc with dissolve
    stop sound fadeout 2.0
    play voice3 girl27_surprised_huh3 noloop
    ag "Watcha looking at? Lingerie for a sweetheart?"
    scene sm1cs-ag001-67-mc-talk-ag with dissolve
    play voice2 mc_arrogant_huh1 noloop
    mc "Huh? Oh nothing. Just uh. Spam. Yeah, spam email."
    scene sm1cs-ag001-68-ag-leans with dissolve
    pause
    scene sm1cs-ag001-69-ag-talk-mc with dissolve
    play voice3 girl27_hey_sexy noloop
    ag "You know we all waste a little time websurfing now and then. Well, except maybe April."
    ag "You don't have to be so worried."
    scene sm1cs-ag001-71-mc-talk-ag with dissolve
    play voice2 d9s3_no noloop volume 2.2
    mc "Me? Worry. Nah. Cool as... cool can be."
    scene sm1cs-ag001-72-ag-giggles with dissolve
    play voice3 girl27_happy_laugh4 noloop
    ag "Hahaha."
    scene sm1cs-ag001-73-ag-talk-mc with dissolve
    play voice3 girl27_happy_yeah5 noloop
    ag "Alright, well, my schedule is officially clear. Let's have that meeting now before anyone else corners me."
    scene sm1cs-ag001-74-mc-talk-ag with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    $ renpy.music.set_volume(0.2, 1.5, "sound2" )
    play sound sfx_door_closed2
    scene sm1cs-ag001-75-mc-inner-talk with fade
    play voice2 mc_thinking_hmm5 noloop
    mct "I really hope she didn't see exactly what I was looking up."
    play sound sfx_cloth_rustling4
    scene sm1cs-ag001-76-ag-talk-mc with dissolve
    play voice3 girl27_thinking_emm5 noloop
    ag "Everything alright, [mcname]?"
    scene sm1cs-ag001-77-mc-talk-ag with dissolve
    play voice2 mc_no_no1 noloop
    mc "No. I mean, yeah. All good, Anna. So what's up with this meeting?"
    scene sm1cs-ag001-78-ag-talk-mc with dissolve
    play voice3 girl27_arrogant_ha noloop
    ag "Just a little informal check-in and review."
    scene sm1cs-ag001-79-ag-talk-mc with dissolve
    play sound sfx_phone_tapping1 volume 2.5
    play voice3 girl27_thinking_mmm noloop volume 1.4
    ag "I just wanted to check in and see how things have been going. Got a couple of questions for you. Let's see."
    ag "How are you liking working for Orbix?"
    stop sound fadeout 1.0
    scene sm1cs-ag001-80-mc-talk-ag with dissolve
    play voice2 mc_happy_a1 noloop
    mc "I like it. Work is pretty demanding, but every day I feel like I'm learning something new."
    scene sm1cs-ag001-81-ag-talk-mc with dissolve
    play voice3 girl27_yes_yap2 noloop
    ag "That's good. A tickled mind is an active mind."
    ag "Let's talk more about the workload. Do you feel like it is too challenging for you?"
    menu:
        "It can be difficult"(hint="sm1cs_ag001_m03_h01"):
            scene sm1cs-ag001-82-c1-mc-talk-ag with dissolve
            play voice2 mc_disappointed_off1 noloop
            mc "I'll admit figuring out all the different frameworks and how to make them sync up can be a little difficult."
            mc "But I'm doing my best."
            play sound sfx_phone_tapping1 volume 2.5
            scene sm1cs-ag001-83-c1-ag-talk-mc with dissolve
            play voice3 girl27_yes_ugu2 noloop
            ag "Well, just remember that when things get hard, you can always come to me to fix it."
            stop sound fadeout 1.0
            scene sm1cs-ag001-84-c1-ag-talk-mc with dissolve
            play voice3 girl27_happy_hmm3 noloop
            ag "These hands are natural born killers when it comes to cloud computing."
            scene sm1cs-ag001-85-c1-mc-talk-ag with dissolve
            play voice2 mc_surprised_huh6 noloop
            mc "Huh?"
            scene sm1cs-ag001-86-c1-ag-talk-mc with dissolve
            play voice3 girl27_arrogant_hah noloop
            ag "I said if you have an issue, come talk to me and we can work out the kinks together."
            scene sm1cs-ag001-87-c1-mc-talk-ag with dissolve
            play voice2 mc_disappointed_ah1 noloop
            mc "Ah. Got it."
            jump sm1cs_ag001_continue
        "Not for me"(hint="sm1cs_ag001_m03_h02"):
            call sm1cs_ag001_m03_c02 from _call_sm1cs_ag001_m03_c02
            scene sm1cs-ag001-88-c2-mc-talk-ag with dissolve
            play voice2 mc_no_nah1 noloop
            mc "Not for me. I'm always ready for new challenges."
            scene sm1cs-ag001-89-c2-ag-talk-mc with dissolve
            play voice3 girl27_happy_great2 noloop
            ag "Great! That's just the kind of attitude we need for the C.U.M. Division."
            ag "I'm glad to hear you like being on top of things, [mcname]."
            jump sm1cs_ag001_next_choice
label sm1cs_ag001_next_choice:
    menu:
        "Flirt"(hint="sm1cs_ag001_m04_h01"):
            call sm1cs_ag001_m04_c01 from _call_sm1cs_ag001_m04_c01
            scene sm1cs-ag001-90-c2-c1-mc-talk-ag with dissolve
            play voice2 mc_hey_hey3 noloop
            mc "On top, on bottom, from the side, I'm always ready to go."
            scene sm1cs-ag001-91-c2-c1-ag-talk-mc with dissolve
            play voice3 girl27_happy_hmm2 noloop volume 1.6
            ag "Hmmm?"
            play sound sfx_cloth_rustling1
            scene sm1cs-ag001-92-c2-c1-mc-awkward with dissolve
            play voice2 mc_pain_mff1 noloop
            pause
            scene sm1cs-ag001-93-c2-c1-ag-talk-mc with dissolve
            play voice3 girl27_happy_hmm1 noloop
            ag "Next question."
        "Professional"(hint="sm1cs_ag001_m04_h02"):
            scene sm1cs-ag001-90-c2-c1-mc-talk-ag with dissolve
            play voice2 mc_hey_hey3 noloop
            mc "Everyone needs to pull their weight when you're on a team."
            scene sm1cs-ag001-93-c2-c1-ag-talk-mc with dissolve
            play voice3 girl27_arrogant_right2 noloop
            ag "Next question."
    jump sm1cs_ag001_continue
label sm1cs_ag001_continue:
    scene sm1cs-ag001-96-ag-talk-mc with dissolve
    play voice3 girl27_surprised_huh2 noloop
    ag "Are you getting along well with your coworkers?"
    menu:
        "It's been smooth"(hint="sm1cs_ag001_m05_h01"):
            scene sm1cs-ag001-94-c2-c2-mc-talk-ag with dissolve
            play voice2 mc_yes_yeah4 noloop
            mc "Oh yeah. It's been smooth sailing since I started."
            mc "Everyone here has been super supportive."
            scene sm1cs-ag001-95-c2-c2-ag-talk-mc with dissolve
            play voice3 girl27_happy_nice4 noloop
            ag "That's wonderful to hear."
        "April is intense"(hint="sm1cs_ag001_m05_h02"):
            call sm1cs_ag001_m05_c02 from _call_sm1cs_ag001_m05_c02
            scene sm1cs-ag001-94-c2-c2-mc-talk-ag with dissolve
            play voice2 mc_thinking_emm1 noloop
            mc "It's been good but working with April has definitely been a little intense."
            scene sm1cs-ag001-95-c2-c2-ag-talk-mc with dissolve
            play voice3 girl27_disappointed_oh1 noloop
            ag "Oh yeah. Intense, pesky, argumentative. She can be a royal pain in the ass when she wants to be."
            ag "I'd like to say she grows on you, but we've worked together a while and I think that would be a lie, hahah."
            play sound sfx_phone_tapping1 volume 2.5
            scene sm1cs-ag001-98-c1-ag-talk-mc with dissolve
            play voice3 girl27_disappointed_mmh noloop
            ag "But she's probably the best damn coder in Crowning, and it's a privilege to have her on the team. Worts and all."
            scene sm1cs-ag001-97-c1-mc-talk-ag with dissolve
            play voice2 mc_yes_yeah5 noloop
            mc "Yeah. Why does she call you Aubergine Anna?"
            scene sm1cs-ag001-100-c2-ag-talk-mc with dissolve
            play voice3 girl27_disappointed_oh3 noloop
            ag "Oh it's just... a little inside joke between us."
            ag "Maybe she'll give you one down the line. Heh."
    scene sm1cs-ag001-101-c2-ag-talk-mc with dissolve
    play voice3 girl27_yes_ugu1 noloop
    ag "Alright, and the last thing."
    ag "It's not really a question. We have a new client coming in and the C.U.M. Division will be taking point and working hand in hand with her."
    scene sm1cs-ag001-103-c2-ag-talk-mc with dissolve
    play voice3 girl27_thinking_emm2 noloop
    ag "I know you just joined up but I should warn you that I might have to ride you extra hard over the next couple of months."
    scene sm1cs-ag001-102-c2-mc-talk-ag with dissolve
    menu:
        "Flirt"(hint="sm1cs_ag001_m06_h01"):
            call sm1cs_ag001_m06_c01 from _call_sm1cs_ag001_m06_c01
            play voice2 mc_thinking_mmm1 noloop
            mct "Oh I don't think either of us would mind that, Anna"
            play voice2 mc_yes_yeah1 noloop
            mc "You can go as hard as you want, Anna."
        "Reassure"(hint="sm1cs_ag001_m06_h02"):
            play voice2 mc_yes_yeah1 noloop
            mc "I won't let you down, Anna."
    scene sm1cs-ag001-111-ag-talk-mc with dissolve
    play voice3 girl27_happy_yes noloop
    ag "Excellent. Well, I think that we're all done here."
    scene sm1cs-ag001-110-mc-talk-ag with dissolve
    play voice2 d2s9_confused noloop volume 1.7
    mc "So I'm good?"
    scene sm1cs-ag001-112-ag-talk-mc with dissolve
    play voice3 girl27_yes_confident noloop
    ag "Oh yes. I'll pass on my thoughts to Claire, let her know you're doing a bang-up job so far, [mcname]."
    ag "Keep up the good work."
    scene sm1cs-ag001-113-mc-talk-ag with dissolve
    play voice2 mc_happy_yay1 noloop
    mc "Thanks Anna. See you around."
    $ renpy.music.set_volume(1.0, 1.5, "sound2" )
    play sound sfx_door_open5
    if CharacterController.get_character("ag").points >= 2:
        scene sm1cs-ag001-115-c2-mc-leave with dissolve
        play voice3 girl27_scared_huh2 noloop
        pause
        pass
    else:
        scene sm1cs-ag001-114-c1-mc-leave with dissolve
        pause
    stop music fadeout 3.0
    stop sound2 fadeout 2.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    $ StoryController.end_scene(AG_STORY, 0, 30, 1)
    return
label sm1cs_ag001_m01_c02:
    $ player.set_choice("sm1cs_ag001_agree_with_ag")
    $ CharacterController.get_character("ag").add_point()
    return
label sm1cs_ag001_m02_c01:
    $ player.set_choice("sm1cs_ag001_increase_difficulity")
    $ player.set_choice("it_job_difficulity", 5)
    return
label sm1cs_ag001_m03_c02:
    $ player.set_choice("sm1cs_ag001_confident")
    return
label sm1cs_ag001_m04_c01:
    $ player.set_choice("sm1cs_ag001_flirt")
    $ CharacterController.get_character("ag").add_point()
    return
label sm1cs_ag001_m05_c02:
    $ player.set_choice("sm1cs_ag001_am_intense")
    return
label sm1cs_ag001_m06_c01:
    $ player.set_choice("sm1cs_ag001_flirt_again")
    $ CharacterController.get_character("ag").add_point()
    return
label sm1cs_ag001_add_gaming_topic:
    $ player.add_topic(TOPIC_GAMING)
    return
label sm1cs_ag001_unlocks:
    call sm1cs_ag001_m01_c02 from _call_sm1cs_ag001_m01_c02_1
    call sm1cs_ag001_m03_c02 from _call_sm1cs_ag001_m03_c02_1
    call sm1cs_ag001_m04_c01 from _call_sm1cs_ag001_m04_c01_1
    call sm1cs_ag001_m05_c02 from _call_sm1cs_ag001_m05_c02_1
    call sm1cs_ag001_m06_c01 from _call_sm1cs_ag001_m06_c01_1
    call sm1cs_ag001_add_gaming_topic from _call_sm1cs_ag001_add_gaming_topic_1
    if config_storyline_mode is True:
        $ execute_storyline_config(AG_STORY)
    return