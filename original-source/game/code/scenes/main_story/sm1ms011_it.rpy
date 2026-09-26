label sm1ms011_it:
    play sound sfx_cloth_rustling1
    scene sm1ms011-07 mc-sy-hand_c2 with dissolve
    play voice3 stacy_thinking_oh2 noloop
    sy "Oh! Before I forget, I wanted to say I'm so proud of you for getting the IT job. You're really growing up, finally."
    scene sm1ms011-07 mc-sy-hand_c1 with dissolve
    play voice2 mc_arrogant_huh2 noloop
    mc "You're proud of me? I'm older, I'm supposed to be proud of you for things."
    scene sm1ms011-08 mc-sy-hand2_c2 with dissolve
    play voice3 stacy_angry noloop
    sy "Don't mess up the moment, Buster."
    scene sm1ms011-08 mc-sy-hand2_c1 with dissolve
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "Carry on."
    sy "Thank you."
    scene sm1ms011-10 mc-sy-walk1_c2 with dissolve
    play voice3 stacy_thinking_hmm4 noloop
    sy "Now, you probably already love being an office drone in a room full of computers, but don't forget that you don't have to stop at one."
    sy "Crowning has a lot to offer us, [mcname]."
    scene sm1ms011-10 mc-sy-walk1_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "I just landed the job. I'm not sure I'm ready to think about another job."
    scene sm1ms011-11 mc-sy-walk2_c2 with dissolve
    play voice3 stacy_yes_okay1 noloop
    sy "Okay, fair enough. Speaking of the company, Orbix right? You haven't told me much about the people there."
    scene sm1ms011-11 mc-sy-walk2_c1 with dissolve
    play voice2 d9s2_yeah noloop volume 2.2
    mc "They're fine. It's a little intimidating."
    play sound sfx_cloth_rustling2
    scene sm1ms011-12 mc-sy-sit_c2 with dissolve
    play voice3 stacy_arrogant_huh1 noloop
    sy "What do you mean?"
    scene sm1ms011-12 mc-sy-sit_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "I get the vibe that everyone there knows more than I do. Like they obviously prepared to work in code."
    mc "Meanwhile, I'm just picking things up as I go."
    scene sm1ms011-13 mc-sy-sit2_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "If I didn't have you for advice and tips, I doubt I would have made it into the door."
    scene sm1ms011-13 mc-sy-sit2_c2 with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "[mcname] Young. I don't want to hear any more of that doubt. You're sharp as a tack and you never back down from a challenge."
    sy "You deserve to be there. Got it?"
    menu:
        "If you say so"(hint="sm1ms011_it_m01_h01"):
            play sound sfx_cloth_rustling3
            scene sm1ms011-14 mc-sy-sit3_c1 with dissolve
            play voice2 mc_disappointed_ehh1 noloop
            mc "If you say so."
            scene sm1ms011-14 mc-sy-sit3_c2 with dissolve
            play voice3 stacy_yes_simple1 noloop
            sy "I do."
        "Got it"(hint="sm1ms011_it_m01_h02"):
            call sm1ms011_m01_c02 from _call_sm1ms011_m01_c02
            play sound sfx_cloth_rustling3
            scene sm1ms011-14 mc-sy-sit3_c1 with dissolve
            play voice2 mc_yes_aga1 noloop
            mc "Got it."
            scene sm1ms011-14 mc-sy-sit3_c2 with dissolve
            play voice3 stacy_yes_ugu1 noloop
            sy "Good!"
    play sound sfx_cloth_rustling4
    scene sm1ms011-15 mc-sy-lap_c2 with dissolve
    play voice3 stacy_thinking_hmm2 noloop
    sy "So... tell me about the girls there."
    scene sm1ms011-15 mc-sy-lap_c1 with dissolve
    play voice2 mc_surprised_what1 noloop
    mc "What about them?"
    scene sm1ms011-16 mc-sy-lap2_c2 with dissolve
    play voice3 stacy_disappointed_mmm2 noloop
    sy "Come on. We know that some people there used Fetish Locator, so some of them have gotta be hiding some kinky skeletons under their desks."
    sy "And if they do, they could end up being some of the best porn starlets ever. After me of course."
    scene sm1ms011-16 mc-sy-lap2_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Oh, right. I almost forgot. Hmmm. Well, I'm just starting to know them."
    play sound sfx_cloth_rustling5
    scene sm1ms011-17 mc-sy-lap3_c2 with dissolve
    play voice3 stacy_thinking_hm1 noloop
    sy "Sure, but I'd bet my last pair of panties that someone stood out."
    jump sm1fs_i011_it_menu
label sm1fs_i011_it_menu_jump:
    if sm1ms011_talk_ns is False or sm1ms011_talk_am is False or sm1ms011_talk_ag is False:
        jump sm1fs_i011_it_menu
    else:
        jump sm1ms011_it_continue
label sm1fs_i011_it_menu:
    menu:
        "Talk about Nari"(hint="sm1ms011_it_m02_h01") if sm1ms011_talk_ns is False:
            $ sm1ms011_talk_ns = True
            jump sm1fs_i011_it_talk_ns
        "Talk about Anna"(hint="sm1ms011_it_m02_h02") if sm1ms011_talk_ag is False:
            $ sm1ms011_talk_ag = True
            jump sm1fs_i011_it_talk_ag
        "Talk about April"(hint="sm1ms011_it_m02_h03") if sm1ms011_talk_am is False:
            $ sm1ms011_talk_am = True
            jump sm1fs_i011_it_talk_am
label sm1fs_i011_it_talk_ns:
    if player.get_choice("sm1ms011_fav_it_girl") is False:
        call sm1ms011_choice_fav_it_girl_ns from _call_sm1ms011_choice_fav_it_girl_ns
    scene sm1ms011-17 mc-sy-lap3_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "This girl Nari Song is pretty cute"
    scene sm1ms011-18 mc-sy-lap4_c2 with dissolve
    play voice3 stacy_happy_laugh2 noloop
    sy "Haha. Someone has a crush. What's she like?"
    scene sm1ms011-18 mc-sy-lap4_c1 with dissolve
    play voice2 mc_arrogant_nah1 noloop
    mc "Eager. Not in that way."
    mc "Like she's this really smart girl from South Korea. She left her family to come out here."
    play sound sfx_cloth_rustling2
    scene sm1ms011-19 mc-sy-lap5_c2 with dissolve
    play voice3 stacy_surprised_wow1 noloop
    sy "Left her home country? That's badass. I like her already!"
    scene sm1ms011-19 mc-sy-lap5_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.7
    mc "Haha. I'm sure she'd be tickled to hear you say that."
    mc "She is a little strange, though. Like when I said eager, I mean super eager."
    mc "And kind of a stickler for rules. She already knows every little detail from the employee handbook."
    scene sm1ms011-19-2 mc-sy-lap6_c1 with dissolve
    play voice3 stacy_disappointed_oh7 noloop
    sy "Okay, I'm a big nerd too, but no one is that big of a nerd."
    scene sm1ms011-19-2 mc-sy-lap6_c2 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "She is."
    play sound sfx_hair_scratch1
    scene sm1ms011-20 mc-sy-ask1_c2 with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "Hmm. Well, maybe you can get her to loosen up a bit."
    sy "You managed to corrupt me over one summer."
    menu:
        "It wasn't all me"(hint="sm1ms011_it_m03_h01"):
            call sm1ms011_m03_c01 from _call_sm1ms011_m03_c01
            scene sm1ms011-20 mc-sy-ask1_c1 with dissolve
            play voice2 mc_no_nah2 noloop
            mc "I think that door was already open a little."
            play sound sfx_cloth_rustling1
            scene sm1ms011-21 mc-sy-ask2_c2 with dissolve
            play voice3 stacy_arrogant_laugh1 noloop
            sy "Haha. Not on your life. I was as innocent as an angel."
            scene sm1ms011-21 mc-sy-ask2_c1 with dissolve
            play voice2 mc_happy_hah2 noloop
            mc "Maybe one of those horny angels."
            play voice3 stacy_happy_laugh1 noloop
            sy "Hehehe."
        "No one made you look at all my porn"(hint="sm1ms011_it_m03_h02"):
            scene sm1ms011-20 mc-sy-ask1_c1 with dissolve
            play voice2 mc_hey_hey3 noloop
            mc "Hey. No one made you look at all my porn."
            play sound sfx_cloth_rustling1
            scene sm1ms011-21 mc-sy-ask2_c2 with dissolve
            play voice3 stacy_arrogant_huh2 noloop
            sy "You know how curious I can be."
            queue voice3 stacy_happy_laugh1 noloop
            sy "*giggles* It was all just a big box of horny catnip."
    jump sm1fs_i011_it_menu_jump
label sm1fs_i011_it_talk_ag:
    if player.get_choice("sm1ms011_fav_it_girl") is False:
        call sm1ms011_choice_fav_it_girl_ag from _call_sm1ms011_choice_fav_it_girl_ag
    scene sm1ms011-22 mc-sy-think_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Anna, is a real looker and seems pretty cool. She's got very good energy, and I'm excited to learn more about her."
    scene sm1ms011-22 mc-sy-think_c2 with dissolve
    play voice3 stacy_huh2 noloop
    sy "What about anything deeper? Something under the covers?"
    scene sm1ms011-22-2 mc-sy-think2_c1 with dissolve
    play voice2 mc_no_no2 noloop
    mc "If she has any kinks, they haven't come up quite yet. Time will tell."
    scene sm1ms011-33 mc-sy-say1_c2 with dissolve
    play voice3 stacy_thinking_emm2 noloop
    sy "Sure, but if there is nothing there, don't forget there are other fish in the sea."
    sy "And we need those that will make great actresses."
    scene sm1ms011-34 mc-sy-say2_c2 with dissolve
    play voice2 mc_yes_sure1 noloop
    mc "Sure."
    jump sm1fs_i011_it_menu_jump
label sm1fs_i011_it_talk_am:
    if player.get_choice("sm1ms011_fav_it_girl") is False:
        call sm1ms011_choice_fav_it_girl_am from _call_sm1ms011_choice_fav_it_girl_am
    scene sm1ms011-29-2 mc-sy-talk8_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "I feel like, April might be a lot to handle."
    scene sm1ms011-29-2 mc-sy-talk8_c2 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "How so?"
    scene sm1ms011-29-4 mc-sy-talk10_c1 with dissolve
    play voice2 mc_disappointed_off1 noloop
    mc "I guess just her energy. She definitely wanted Nari and I to know how little she felt about us."
    play sound sfx_cloth_rustling2
    scene sm1ms011-29-4 mc-sy-talk10_c2 with dissolve
    play voice3 stacy_arrogant_ha2 noloop
    sy "What a bitch!"
    scene sm1ms011-29-3 mc-sy-talk9_c1 with dissolve
    play voice2 mc_arrogant_heh1 noloop
    mc "Maybe. If she's been pared with other people before that didn't work out, maybe she's tired to dealing with noobs."
    scene sm1ms011-29-3 mc-sy-talk9_c2 with dissolve
    play voice3 stacy_arrogant_hmm1 noloop
    sy "Hmmmph. That's no need to be rude to your or the new girl."
    scene sm1ms011-33 mc-sy-say1_c1 with dissolve
    play voice2 mc_happy_oof3 noloop
    mc "If anything, figuring out what her deal is will be an extra challenge for me."
    scene sm1ms011-33 mc-sy-say1_c2 with dissolve
    play voice3 stacy_no_nah2 noloop
    sy "At least you got the right attitude for it. In a little bit, she'll be glad to have you as a friend."
    sy "Or more."
    jump sm1fs_i011_it_menu_jump
label sm1ms011_it_continue:
    scene sm1ms011-34 mc-sy-say2_c1 with dissolve
    play voice3 stacy_thinking_oh1 noloop
    sy "And what about your boss' boss. Claire?"
    scene sm1ms011-35 mc-sy-say3_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "What about her?"
    scene sm1ms011-35 mc-sy-say3_c2 with dissolve
    play voice3 stacy_hey_angry1 noloop
    sy "Please tell me you're not going to leave her out of the party?"
    scene sm1ms011-36 mc-sy-say4_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "Given she's my boss' boss, I figured it would be smart to stay clear of her."
    scene sm1ms011-36 mc-sy-say4_c2 with dissolve
    play voice3 stacy_no_uhuh3 noloop
    sy "No way. Big mistake, pal. Think about it. She could be the biggest close pervert of the mall."
    sy "I just don't think you should leave her out of the conversation, is all."
    menu:
        "She is super hot"(hint="sm1ms011_it_m04_h01"):
            call sm1ms011_m04_c01 from _call_sm1ms011_m04_c01
            scene sm1ms011-37 mc-sy-say5_c1 with dissolve
            play voice2 mc_yes_yeah1 noloop
            mc "She is super hot."
            scene sm1ms011-37 mc-sy-say5_c2 with dissolve
            play voice3 stacy_laugh4 noloop
            sy "See. You totally want to bang your boss. I mean that makes sense. Who wouldn't?"
            scene sm1ms011-38 mc-sy-say6_c1 with dissolve
            play voice2 d2s12_emmm noloop
            mc "Feelings aside, it might make things super complicated."
            scene sm1ms011-38 mc-sy-say6_c2 with dissolve
            play voice3 stacy_yes_yap1 noloop
            sy "Super complicated is just our style."
            play sound sfx_cloth_rustling4 volume 0.7
            scene sm1ms011-39 mc-sy-say7_c1 with dissolve
            play voice2 mc_disappointed_off2 noloop
            mc "I think our style is more like a cat wearing rollerblades flying down a hillside."
            scene sm1ms011-39 mc-sy-say7_c2 with dissolve
            play voice3 stacy_yes_ugu1 noloop
            sy "We can have multiple styles. All I'm saying is that you shouldn't count her out."
            scene sm1ms011-40 mc-sy-say8_c1 with dissolve
            play voice2 mc_yes_yeah2 noloop
            mc "Yeah."
        "I'll see what I can do"(hint="sm1ms011_it_m04_h02"):
            play sound sfx_cloth_rustling4 volume 0.7
            scene sm1ms011-39 mc-sy-say7_c1 with dissolve
            play voice2 mc_disappointed_ehh3 noloop
            mc "I'll see what I can do."
            scene sm1ms011-39 mc-sy-say7_c2 with dissolve
            play voice3 stacy_yay noloop
            sy "Great. I know you, [mcname]. Whatever you put your mind to, I'm sure you can knock it ouf the park."
            scene sm1ms011-40 mc-sy-say8_c1 with dissolve
            play voice2 mc_yes_aga2 noloop
            mc "Maybe. I'll keep my ears open."
    scene sm1ms011-40 mc-sy-say8_c2 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Well it sounds like the place is going to offer you a lot of opportunity."
    scene sm1ms011-41 mc-sy-say9_c2 with dissolve
    play voice3 stacy_yes_fine2 noloop
    sy "Just try not to get lost in the code and ones and zeroes too much."
    sy "We've got to keep our eyes on the prize."
    scene sm1ms011-41 mc-sy-say9_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    if persistent.is_special is True:
        mc "No worries there, Sis."
    else:
        mc "No worries there, Stacy."
    return
label sm1ms011_m01_c02:
    $ player.set_choice("sm1ms011_got_it")
    return
label sm1ms011_choice_fav_it_girl_ns:
    $ player.set_choice("sm1ms011_fav_it_girl", ns)
    return
label sm1ms011_choice_fav_it_girl_ag:
    $ player.set_choice("sm1ms011_fav_it_girl", ag)
    return
label sm1ms011_choice_fav_it_girl_am:
    $ player.set_choice("sm1ms011_fav_it_girl", am)
    return
label sm1ms011_m03_c01:
    $ player.set_choice("sm1ms011_door_was_open")
    return
label sm1ms011_m04_c01:
    $ player.set_choice("sm1ms011_boss_hot")
    return
label sm1ms011_it_unlocks:
    call sm1ms011_m01_c02 from _call_sm1ms011_m01_c02_1
    call sm1ms011_choice_fav_it_girl_ns from _call_sm1ms011_choice_fav_it_girl_ns_1
    call sm1ms011_m03_c01 from _call_sm1ms011_m03_c01_1
    call sm1ms011_m04_c01 from _call_sm1ms011_m04_c01_1
    return