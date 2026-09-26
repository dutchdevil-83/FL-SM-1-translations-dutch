label sm1ms011_01i:
    $ player.set_choice("sm1msi001_immediate_start", False)
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice3 stacy_hey noloop
    sy "Hey there."
    if player.get_choice("TH_JOB_UNLOCKED") is False:
        sy "So I've been reading some stuff about a community theater group in town."
        hide lst_sy_naughty1
        show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
        play voice3 stacy_thinking_hm1 noloop
        sy "I'd bet my right boob you could do some acting there for some easy cash. Plus if you're lucky, someone in there might be interested in working on a more adult stage."
        sy "Hehehe."
        play voice2 mc_happy_hah1 noloop
        mc "Haha. Well, I'm sure we can check it out."
    if player.get_choice("IT_JOB_UNLOCKED") is False:
        sy "We're in luck."
        play voice2 mc_yes_yeah8 noloop
        mc "Oh yeah?"
        hide lst_sy_naughty1
        show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
        play voice3 stacy_yes_yeah1 noloop
        sy "There is a IT company in Crowning that is looking for new coders."
        play voice2 d2s9_confused noloop
        mc "Uh, I'm not much of a coder."
        sy "Yeah but you can learn. You're a fast learner and you have a sexy tech-pro by your side."
        mc "Hmm. Alright, if you think I'm up to it, that's something I can look into."
    menu:
        "The IT Job"(hint="sm1ms011_01i_m01_h01") if player.get_choice("IT_JOB_UNLOCKED") is False:
            call sm1ms011_01i_unlock_it_quest from _call_sm1ms011_01i_unlock_it_quest
            play voice2 mc_yes_okay2 noloop
            mc "Talk to me about that IT job."
            hide lst_sy_smile1
            show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
            play voice3 stacy_thinking_well1 noloop
            sy "There is a IT Company called Orbix in Crowning. They're looking for a new software engineer."
            jump sm1ms011_01i_it_job
        "The Theater"(hint="sm1ms011_01i_m01_h02") if player.get_choice("TH_JOB_UNLOCKED") is False:
            call sm1ms011_01i_unlock_theather_quest from _call_sm1ms011_01i_unlock_theather_quest
            mc "Tell me more about the theater."
            hide lst_sy_smile1
            show expression cc.get_expression_image("sy", "ask1") as lst_sy_ask1
            play voice3 stacy_thinking_well1 noloop
            sy "There is a small community theater troupe in Crowning."
            sy "I looked on their website and couldn't find out if they were hiring."
            jump sm1ms011_01i_th_job
label sm1ms011_01i_it_job:
    mc "Uh. I don't know much about coding and stuff. I use computers for porn and... well that's about it."
    sy "It's fine, [mcname] I can show you the ropes. That is if you're interested in the job."
    menu:
        "Tell me more"(hint="sm1ms011_01i_m02_h01"):
            if gt.curr_timeslot in [TIMESLOT_1, TIMESLOT_2, TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6]:
                play voice2 mc_yes_yeah2 noloop
                mc "Yeah, tell me what you learned."
                hide lst_sy_ask1
                show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
                play voice3 stacy_yes_fine2 noloop
                sy "Great. I'll get set up in a bit. Just come talk to me in the evening when I'm on my laptop."
                mc "Got it."
            if gt.curr_timeslot == TIMESLOT_7:
                hide lst_sy_ask1
                show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
                play voice3 stacy_yes_fine2 noloop
                sy "Let me get my laptop."
                $ player.set_choice("sm1msi001_immediate_start", True)
                $ player.progress_storyline(MS, 1)
            if gt.curr_timeslot == TIMESLOT_8:
                play voice2 d1s5_mchappy noloop
                mc "I guess it couldn't hurt to learn more."
                hide lst_sy_ask1
                show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
                play voice3 stacy_yes_ugu1 noloop
                sy "Of course. It's late now, so just find me tomorrow evening when I'm on my laptop."
                sy "I'll walk you through what I found."
                mc "Perfect."
        "I'll think about it"(hint="sm1ms011_01i_m02_h02"):
            play voice2 d1s5_mchappy noloop
            mc "Let me give it a think."
            play voice3 stacy_yes_fine4 noloop
            sy "Your call."
    jump sm1ms011_01i_end
label sm1ms011_01i_th_job:
    sy "But I think I found someone who works in the group who could help us."
    menu:
        "Tell me more"(hint="sm1ms011_01i_m03_h01"):
            if gt.curr_timeslot in [TIMESLOT_1, TIMESLOT_2, TIMESLOT_3, TIMESLOT_4, TIMESLOT_5, TIMESLOT_6]:
                play voice2 mc_yes_yeah2 noloop
                mc "If you found someone who can help us, that would be great."
                hide lst_sy_ask1
                show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
                play voice3 stacy_yes_ugu1 noloop
                sy "Mmhmm. I'll fill you in a little later. Come talk to me in the evening when I'm on my laptop."
                mc "Got it."
            if gt.curr_timeslot == TIMESLOT_7:
                hide lst_sy_ask1
                show expression cc.get_expression_image("sy", "excited1") as lst_sy_excited1
                play voice3 stacy_yes_fine2 noloop
                sy "Let me get my laptop."
                $ player.set_choice("sm1msi001_immediate_start", True)
                $ player.progress_storyline(MS, 1)
            if gt.curr_timeslot == TIMESLOT_8:
                play voice2 d1s5_mchappy noloop
                mc "We should keep our options. Who is this person?"
                hide lst_sy_ask1
                show expression cc.get_expression_image("sy", "yawn1") as lst_sy_yawn1
                play voice3 stacy_disappointed_moan1 noloop
                sy "*yawns* It's a little late now. Come talk to me tomorrow evening when I'm on my laptop."
                sy "I can show you what I got."
                mc "Sounds good to me."
        "I'll think about it"(hint="sm1ms011_01i_m03_h02"):
            play voice2 d1s5_mchappy noloop
            mc "Let me give it a think."
            play voice3 stacy_yes_fine4 noloop
            sy "Your call."
    jump sm1ms011_01i_end
label sm1ms011_01i_end:
    $ StoryController.end_scene(MORE_FACTIONS, 0, 30, 0)
    $ StoryController.activate_story_line(MS, True)
    return
label sm1ms011_01i_unlock_it_quest:
    $ player.set_choice("Current_job_to_unlock", IT_STORY_LINE)
    return
label sm1ms011_01i_unlock_theather_quest:
    $ player.set_choice("Current_job_to_unlock", THEATER_STORY_LINE)
    return