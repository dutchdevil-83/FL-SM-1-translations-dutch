image sm1cs_mes001-glambot-1 = Movie(play = "images/Character-Scenes/MES/s001/anim/sm1cs-mes001-a02-3x-60fps.webm", start_image = "sm1cs-mes001-a02 mes-notices-mc-surprised-glambot-", image = "sm1cs-mes001-a02 mes-notices-mc-surprised-glambot-239", loop = False)
label sm1cs_mes001:
    $ renpy.music.set_volume(0.85, 0.5, "music" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_music1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(0.0, 1.0, "freeroam_sound2" )
    play music music_5_mark_radio
    play sound4 sfx_crowd_fightclub_ambient2 fadein 3.0 volume 0.8
    scene sm1cs-mes001-01 mc-notices-mes_c1 with Fade(0.15, 0.2, 0.15)
    pause
    scene sm1cs-mes001-a02 mes-notices-mc-surprised-glambot- with dissolve
    pause
    play sound [sfx_camera_fly1, "<silence 2.0>", sfx_camera_fly1] volume 2.0
    play sound2 ["<silence 2.5>", sfx_camera_fly1] volume 2.0 noloop
    play sound3 ["<silence 5.0>", sfx_camera_fly1] volume 2.0 noloop
    scene sm1cs_mes001-glambot-1
    pause
    play voice3 min_old_mhuh noloop
    pause
    play sound sfx_heels_steps2
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    scene sm1cs-mes001-03 mc-approach-hey-mes_c1 with dissolve
    play voice2 mc_surprised_huh7 noloop
    mc "Min...?"
    scene sm1cs-mes001-04 mes-surprised-oh-hi-mc_c1 with dissolve
    play voice3 min_surprised_ehh1 noloop
    mes "*slightly startled* Oh... [mcname], hi."
    mct "Her voice sounds hesitant, almost as though she'd rather not admit she's here."
    scene sm1cs-mes001-05 mc-cant-believe-it-you-mes-not-too-long-ago_c1 with dissolve
    play voice2 d2s12_emmm noloop volume 1.6
    mc "I... I can't believe it's you. I kind of figured that you would still be in Korea. When did you get back?"
    play voice3 min_yes_ugu noloop
    mes "Not too long ago. I guess I wanted to slip back quietly. Didn't expect to run into anyone so soon."
    scene sm1cs-mes001-06 mct-barely-recognize-mes-attitude_c1 with dissolve
    play voice2 mc_angry_huh2 noloop
    mct "I barely recognize her from how she last looked. Usually, she has such a determined expression."
    scene sm1cs-mes001-07 mc-may-sit-mes-ofc-bit-embarrassed_c1 with dissolve
    play voice2 mc_hey_hey7 noloop
    mc "Mind if I sit?"
    play voice3 min_yes_yeah2 noloop
    mes "Sure. Although... I'm a bit embarrassed to be caught off guard like this. I should have called when I came back."
    $ renpy.music.set_volume(0.35, 15.5, "sound4" )
    scene sm1cs-mes001-08 mc-it-fine-no-need-feel-embarrassed-mes-sigh-yes_c1 with dissolve
    play voice2 mc_no_uhuh1 noloop
    mc "It's fine. And you don't have to feel embarrassed about anything, Min. We're friends, remember? It's been months, but that doesn't change what we are."
    play voice3 min_yes_simple noloop
    mes "*soft sigh* Yes. Things got a little complicated after the last time we saw each other."
    play sound sfx_cloth_rustling2
    scene sm1cs-mes001-09 mc-slides-next-mes-mc-complicated-mc-bet-trip-was-nice_c1 with dissolve
    play voice2 mc_yes_yeah5 noloop
    mc "\"Complicated\" that's one way to describe everything that's happened."
    mc "But I bet the trip was nice."
    scene sm1cs-mes001-10 mes-was-fine-got-see-parents_c1 with dissolve
    play voice3 min_thinking_emm noloop
    mes "It was... fine, I guess. I got to see my parents. Well, \"see\" them might be an overstatement."
    scene sm1cs-mes001-11 messaw-them-droned-hours-her-future_c1 with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "I {i}saw{/i} them, as they droned on for hours about my future. *chuckles*"
    scene sm1cs-mes001-12 mct-trying-joke-there-hurt-mes-they-have-strong-opinions_c1 with dissolve
    play voice2 mc_thinking_mmm3 noloop
    mct "She's trying to play things off as a joke, but there's hurt in her eyes."
    play voice3 min_arrogant_pff noloop
    mes "They have strong opinions on what path I should take, and it doesn't exactly match with what I have in mind."
    scene sm1cs-mes001-13 mc-sorry-hear-that-know-it-life-mes-keep-telling-that_c1 with dissolve
    play voice2 mc_disappointed_ah1 noloop
    mc "I'm sorry to hear that. Parents can be tough when they disapprove. But, you know, it's your life."
    play voice3 min_yes_yeah1 noloop
    mes "I keep telling myself that."
    scene sm1cs-mes001-14 mes-holding-trembling-glass-mct-mes-nervous-about-something_c1 with dissolve
    play voice2 d1s5_mcthinks noloop volume 1.6
    mct "Hmm. Is Min nervous about something?"
    scene sm1cs-mes001-15 mc-dont-look-thrilled-all-okay-mes-honestly-not-sure_c1 with dissolve
    play voice2 mc_hey_hey2 noloop
    mc "You don't look too thrilled about being back. Is everything okay?"
    play voice3 min_disappointed_ehh3 noloop
    mes "Honestly? I'm not sure. I was so torn about whether to return, and now I'm here, and I'm facing everything I left behind."
    scene sm1cs-mes001-16 mct-cant-say-blame-her-after-everything-happened-fl_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mct "Can't say I blame her for trying to leave behind everything that happened with Lydia and Fetish Locator."
    scene sm1cs-mes001-17 mc-waves-bartender-comes-front-of-him_c1 with dissolve
    play voice2 d2s9_mchey noloop
    mc "Can I have one of those?"
    play sound sfx_cloth_rustling3
    scene sm1cs-mes001-18 mc-orders-one-those_c1 with dissolve
    pause
    play sound sfx_bottle_pouring1
    scene sm1cs-mes001-19 barmaid-gives-mc-order_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "Thanks."
    play sound sfx_drink_slurp2
    scene sm1cs-mes001-20 mc-takes-sip-whiskey-standing_c1 with dissolve
    pause
    scene sm1cs-mes001-21 mc-whinces-mct-that-hot_c1 with dissolve
    play voice2 mc_angry_errr8 noloop
    mct "Fuck, that's hot."
    scene sm1cs-mes001-22 mc-start-about-fl-lydia-mes-chuckles_c1 with dissolve
    play voice2 mc_disappointed_ah2 noloop
    mc "Min... about Lydia and Fetish Locator—"
    play voice3 min_old_laugh noloop
    mes "*chuckles wrly* The elephant in the room."
    scene sm1cs-mes001-23 mes-still-trying-wrap-head-around-how-missed-it_c1 with dissolve
    play voice3 min_angry_breath noloop
    mes "I'm still trying to wrap my head around how I missed it. I can't believe Lydia was behind Fetish Locator the entire time..."
    scene sm1cs-mes001-24 mes-straightens-feel-such-fool-trusting-her-pushed-her-become-who-is-or-was_c1 with dissolve
    play voice3 min_angry_argh2 noloop
    mes "I feel like such a fool for trusting her. We were best friends, you know? She was my confidante, the one who helped push me to become the achiever I am."
    scene sm1cs-mes001-25 mes-sighs-or-was_c1 with dissolve
    play voice3 min_arrogant_hm noloop
    mes "Or was."
    mes "*sighs* We told each other our deepest secrets. At least I thought so..."
    scene sm1cs-mes001-26 mc-still-remember-feeling-shock-mes-frustrated-felt-used_c1 with dissolve
    play voice2 mc_yes_yeah3 noloop
    mc "I can still remember that feeling of shock when I found out. I couldn't believe someone so close to us could do something that manipulative."
    play voice3 min_disgust_off noloop
    mes "I felt so used. And then it dawned on me. I {i}helped{/i} her... I'm just as guilty."
    scene sm1cs-mes001-27 mes-helped-promote-stupid-app-mes-in-my-house_c1 with dissolve
    play voice3 min_angry_argh1 noloop
    mes "I helped her by promoting that stupid app at parties."
    mes "In my fucking house!"
    scene sm1cs-mes001-28 mc-reassures-her-had-no-idea-mct-her-knuckles-white-around-glass_c1 with dissolve
    play voice2 mc_no_no5 noloop
    mc "You had no idea. None of us did. You can't blame yourself."
    mct "Her knuckles are white around that glass. I remember how passionately Min used to talk about Fetish Locator."
    play sound sfx_drink_loop1 volume 2.0 loop
    scene sm1cs-mes001-29 mc-takes-sip-thinks-min-loves-she-could-do-when-unravelled-must-felt-part-die_c1 with dissolve
    play voice2 mc_thinking_hm noloop
    mct "She loved what it could do, how it could bring kink-friendly people together."
    mct "When Fetish Locator unraveled, Min must have felt like part of her life did the same."
    scene sm1cs-mes001-30 mes-takes-sip-whisky_c1 with dissolve
    pause
    play sound sfx_cup_place1 volume 3.0
    scene sm1cs-mes001-31 mes-puts-glass-down-mes-talks-dont-know-about-that_c1 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "I don't know about that.{w} Since that point, I kind of feel trapped. Like my brain is second-guessing everything because of Lydia."
    mes "It felt like the ground was pulled out from under me when I found out."
    scene sm1cs-mes001-32 mes-bitterly-con-by-best-friend_c1 with dissolve
    play voice3 min_disappointed_mph noloop
    mes "One day, I'm hosting Fetish Locator parties, the next, I realize the entire app was basically a scheme."
    mes "*bitterly* A con made up by my best friend for years."
    scene sm1cs-mes001-33 mes-takes-another-sip_c1 with dissolve
    play sound sfx_drink_gulp
    pause
    scene sm1cs-mes001-34 mes-plays-finger-mes-had-get-away-mes-couldnt-be-around-friends_c1 with dissolve
    play voice3 min_disappointed_off noloop
    mes "I had to get away. It's part of why I went to Korea over the summer."
    mes "I couldn't be around my friends. And the other people I knew from school were constantly whispering about it."
    scene sm1cs-mes001-35 mes-bad-joke-all-distance-couldnt-forget_c1 with dissolve
    play voice3 min_disgust_nah noloop
    mes "But, like a bad joke, all the distance in the world couldn't help me forget everything that happened..."
    mes "And the things I left..."
    scene sm1cs-mes001-36 mes-and-things-left-mc-did-at-least-help-family_c1 with dissolve
    play voice2 mc_arrogant_hm3 noloop
    mc "Did it at least help to be with your family for a while, to get a fresh perspective?"
    scene sm1cs-mes001-37 mes-yes-and-no-they-wanted-stay-korea_c1 with dissolve
    play voice3 min_old_argh noloop
    mes "Yes and no. I love my parents, obviously, but they're stuck in this traditional mindset."
    mes "They wanted me to stay in Korea, finish my studies there, and settle down into some stable job."
    scene sm1cs-mes001-38 mes-exact-oposite-of-what-she-doing-oh-trusting-wrong-people_c1 with dissolve
    play voice3 min_thinking_hmm1 noloop
    mes "The exact opposite of what I've been doing here — going to parties, being the best student, dropping in and out of relationships..."
    mes "Oh, and trusting the wrong people.{w} Can't forget about that."
    mct "She looks so weighed down by it all. This is a side of Min I rarely saw — vulnerable and uncertain."
    play sound sfx_wineglass_ding1
    scene sm1cs-mes001-39 mct-she-looks-weighted-down-mc-pushing-bad-stuff-glad-see-you-agian_c1 with dissolve
    play voice2 mc_thinking_hmm5 noloop
    mc "Min, for what it's worth, I'm glad to see you again. I'm sorry if that means you have to be reminded of all the bad stuff, but I'm still happy you're here."
    scene sm1cs-mes001-40 mes-mood-improves-soft-laugh_c1 with dissolve
    play voice3 min_arrogant_heh1 noloop
    mes "*soft laugh* I appreciate that. Really, I do.{w} I- I don't mind that you found me, [mcname]."
    scene sm1cs-mes001-41 mes-sours-same-time-brace-myself-fresh-disappointment_c1 with dissolve
    play voice3 min_pain_ah noloop
    mes "At the same time, my brain is telling me to brace myself for fresh disappointment before long."
    play sound sfx_cloth_rustling5
    scene sm1cs-mes001-42 mes-puts-empty-glass-mc-come-on-one-day-laugh-mes-doubtful_c1 with dissolve
    play voice2 mc_happy_a1 noloop
    mc "Come on. One day, we'll laugh about all that Fetish Locator business."
    play voice3 min_no_nah noloop
    mes "Doubtful."
    scene sm1cs-mes001-43 mc-looks-glass-another-one-mes-prolly-good-for-now-_c1 with dissolve
    play voice2 mc_thinking_hmm4 noloop
    mc "One more?"
    play voice3 min_no_uhuh noloop
    mes "I'm probably good. I'm trying not to drown my sorrows in whiskey tonight. I just... wanted something to calm my nerves. I ended up here thinking I'd be alone."
    play sound sfx_heels_steps2 loop
    play sound2 sfx_heels_steps1
    scene sm1cs-mes001-44 mc-know-feeling-mes-right_c1 with dissolve
    play voice2 mc_arrogant_hm1 noloop
    mc "I know the feeling. Guess it's just dumb luck we both picked this spot."
    play voice3 min_thinking_hmm3 noloop
    mes "Right? It's definitely not my usual hangout — feels a bit random."
    play sound sfx_bed_slide2
    stop sound2 fadeout 1.0
    scene sm1cs-mes001-45 mc-maybe-universe-telling-miss-each-other-decided-could-use-company_c1 with dissolve
    play voice2 mc_thinking_hmm2 noloop
    mc "Maybe the universe knew we'd been missing each other..."
    mc "...Decided we could use some company."
    scene sm1cs-mes001-46 mes-laughs-haha-yes-grand-plan-doesnt-work-like-that_c1 with dissolve
    play voice3 min_arrogant_huh2 noloop
    mes "Hah, yeah some grand plan to put us back together."
    mes "It doesn't work like that, [mcname]. Still, it's nice to see a friendly face."
    play sound sfx_cloth_rustling4
    scene sm1cs-mes001-47 mes-thinking-back-silly-avoid-ppl-been-months_c1 with dissolve
    play voice3 min_happy_relief noloop
    mes "Now, thinking back, it feels a bit silly that I've been avoiding people since I got back."
    mes "It's been months, after all."
    scene sm1cs-mes001-48 mc-grins-min-feeling-silly-mes-ha-enjoy-while-lasts_c1 with dissolve
    play voice2 mc_arrogant_heh2 noloop
    mc "Min feeling silly? I didn't think that was possible."
    play voice3 min_happy_yeah noloop
    mes "Hah, enjoy it while it lasts. I'm sure I'll kick these blues one day or another. Then you'll never see Silly Min again."
    scene sm1cs-mes001-49 mes-curious-rumor-has-dropped-out_c1 with dissolve
    play voice3 min_surprised_huh2 noloop
    mes "So... rumor has it you dropped out, right?"
    scene sm1cs-mes001-50 mc-explaining-guilty-charged-mc-now-focus-porn-studio_c1 with dissolve
    play voice2 mc_yes_yes2 noloop
    mc "*sheepishily* Guilty as charged. The old business management program just wasn't cutting it for me."
    mc "Now my focus is on making my own porn studio."
    scene sm1cs-mes001-51 mes-hear-something-with-sy-mc-yeah-found-studio_c1 with dissolve
    play voice3 min_surprised_oh noloop
    mes "A porn studio? With Stacy, right? I heard bits and pieces."
    play voice2 mc_yes_yeah4 noloop
    mc "Yeah. We found a studio for sort of a home slash office deal."
    mes "I didn't know you two were living together and making a go of it."
    mc "Yeah, it's real, all right — stressful, chaotic, but real."
    if player.get_choice("sm1ms_renovation_completed"):
        mc "We actually just finished renovating our studio."
    elif player.get_choice("sm1ms_renovation_started"):
        mc "We're actually doing some renovations to turn it into a proper studio."
    else:
        mc "We've started laying the groundwork for a real, proper studio."
    scene sm1cs-mes001-52 mc-weary-sometimes-feels-impossible-but-stacy-huge-help_c1 with dissolve
    play voice2 mc_disappointed_ehh5 noloop
    mc "Sometimes it feels impossible. I'll be the first to admit it's pretty ambitious."
    mc "But Stacy is a huge help. She's unstoppable when she sets her mind on something."
    scene sm1cs-mes001-53 mes-sounds-like-girl-determination-mc-she-reason-gotten-so-far_c1 with dissolve
    play voice3 min_thinking_oh noloop
    mes "I didn't get to know her that well, but she sounds like a girl of great determination."
    play voice2 mc_yes_yes1 noloop
    mc "She's the reason we've gotten this far. I'm the eye candy and jokester mostly."
    scene sm1cs-mes001-54 mes-why-does-exactly-need-jokester-mc-helps-when-lot-of-work_c1 with dissolve
    play voice3 min_surprised_ehh2 noloop
    mes "And why exactly does a team of professionals need a jokester?"
    play voice2 mc_disappointed_off1 noloop
    mc "When you're painting and drywalling walls for the third day straight, it helps to have someone cracking jokes at two in the morning."
    scene sm1cs-mes001-55 mes-smiles-believe-it-when-see-it-still-surprised-left-college-for-this_c1 with dissolve
    play voice3 min_arrogant_heh2 noloop
    mes "*light laugh* I'll believe it when I see it."
    mes "But I'm still surprised you gave up college for this."
    scene sm1cs-mes001-56 mc-for-now-yes-might-go-back-when-business-running_c1 with dissolve
    play voice2 mc_yes_yeah2 noloop
    mc "For now, yeah. I might go back once the business is up and running, but I realized I was more passionate about creating something tangible than sitting in a classroom."
    scene sm1cs-mes001-57 mes-passion-good-classes-not-feel-same-after-everything_c1 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "Passion is good. Honestly, I've wrestled with the idea of quitting too, so many times."
    mes "Classes just don't feel the same after everything that happened."
    scene sm1cs-mes001-58 mes-thought-went-korea-things-change-maybe-time-set-things-aside_c1 with dissolve
    play voice3 min_old_shy noloop volume 1.7
    mes "I thought when I went to Korea, things would change. Learning would have that luster it used to have, but it didn't help."
    mes "Maybe it's time to set my classes aside."
    play sound sfx_leg_kick8
    scene sm1cs-mes001-59 mct-her-eyes-flicker-mc-didnt-mean-sound-good-not-everyone_c1 with dissolve
    play voice2 mc_hey_hey9 noloop
    mc "Min, I didn't mean to make it sound like dropping out is the greatest idea in the world. It's not for everyone."
    mc "Stacy and I have definitely had our share of second thoughts. But it's what felt right for me."
    play sound sfx_cloth_rustling1
    scene sm1cs-mes001-60 mc-stacy-i-deff-had-second-thoughts-mes-get-it-dont-worry_c1 with dissolve
    play voice3 min_no_nonono noloop
    mes "I get it. Don't worry, [mcname]. It's not like I'm going to drop out tomorrow or anything."
    scene sm1cs-mes001-61 mes-based-taboo-so-what-like-living-sy_c1 with dissolve
    play voice3 min_surprised_huh1 noloop
    if persistent.is_special:
        mes "So... what's it like living with Stacy as not just your sister, but now your partner in crime and bed, so to speak?"
    else:
        mes "So... what's it like living with your childhood friend, but now your partner in crime and bed, so to speak?"
    scene sm1cs-mes001-62 mc-grins-never-dull-basically-couple-she-doesnt-mind-other-girls_c1 with dissolve
    play voice2 d3s11b_mcheh noloop volume 1.5
    mc "*grin* It's never dull, I'll say that. We were close before, but now that we're building something together, there's this new energy."
    mc "We're basically a couple — but she doesn't mind me being with other girls."
    scene sm1cs-mes001-63 mc-surprised-she-okay-mc-oh-yeah-sometimes-even-pushes_c1 with dissolve
    play voice3 min_surprised_what noloop
    mes "Wait, so she's okay with you dating around?"
    play voice2 mc_yes_yeah1 noloop
    mc "Oh yeah. Sometimes, she even pushes me to do it. She jokes about it constantly. It was a little strange at first, but it works for us."
    scene sm1cs-mes001-64 mes-she-very-unique-mc-can-say-that-again_c1 with dissolve
    play voice3 min_thinking_mhh noloop
    mes "She's very unique."
    play voice2 mc_yes_yes7 noloop
    mc "You can say that again."
    scene sm1cs-mes001-65 mc-thinks-sy-biggest-kink-mc-hey-love-her-she-loves-me_c1 with dissolve
    play voice2 mc_happy_laugh2 noloop
    mc "I think her biggest kink is seeing me squirm in embarrassing situations that she puts me in."
    mc "But hey, I love her for it, and she loves me."
    scene sm1cs-mes001-66 mes-that-good-hear-mes-cant-help-wonder_c1 with dissolve
    play voice3 min_old_aww noloop
    mes "That's good to hear. I'm glad you're doing something that makes you happy."
    mes "But I can't help but wonder if-"
    scene sm1cs-mes001-67 mes-forget-it-mc-come-on-got-something-chest_c1 with dissolve
    play voice3 min_old_mff noloop volume 1.7
    mes "Forget it."
    play voice2 mc_arrogant_huh1 noloop
    mc "Come on, I know you got something on your chest, Min."
    scene sm1cs-mes001-68 mes-silent-mc-cant-believe-this-old-min-never-shy_c1 with dissolve
    mes "..."
    play voice2 d4s4_mclaugh noloop volume 1.5
    mc "I can't believe this. *chuckles*{w} The old Min was never shy."
    scene sm1cs-mes001-69 mes-nothing-just-wonder-mc-you-had-reasons_c1 with dissolve
    play voice3 min_no_simple noloop
    mes "It's nothing. I just... I wonder if I messed up by not staying in touch."
    play voice2 d1s5b_ehhh noloop volume 1.7
    mc "Min, you had your reasons. We all had complicated stuff going on. Lydia, FL, Anthony... there was so much drama swirling around."
    scene sm1cs-mes001-70 mes-yeah-anthony-whole-other-can-worms_c1 with dissolve
    play voice3 min_yes_yeah2 noloop
    mes "Yeah, Anthony... That was a whole other can of worms. He was controlling in his own way, and I guess it didn't help that I was already half in love with you at the time."
    scene sm1cs-mes001-71 mct-min-love-me-mes-obviously-messing-around_c1 with dissolve
    play voice2 d1s1_mmm noloop volume 1.7
    mct "Woah. Min was in love with me?"
    play voice3 min_thinking_emm noloop
    mes "I mean, obviously we were just messing around, not taking it seriously. That's how I saw it."
    scene sm1cs-mes001-72 mc-earnest-really-cared-for-min_c1 with dissolve
    play voice2 mc_no_no8 noloop
    mc "Min, for me, it wasn't just messing around. You know I cared about you. I still do. I'm sorry if I gave you the impression that it was just a fling."
    scene sm1cs-mes001-73 mes-both-had-lot-going-on-mes-then-lydia-betrayal-out_c1 with dissolve
    play voice3 min_disappointed_ehh3 noloop
    mes "*quietly* We both had a lot going on back then..."
    mes "Then Lydia's betrayal came out, I panicked. I pulled away and went off to Korea, trying to 'find myself' or something cheesy like that."
    scene sm1cs-mes001-74 mc-ask-regret-leaving-mes-hesitates-_c1 with dissolve
    play voice2 mc_thinking_mmm5 noloop
    mc "Do you regret leaving?"
    scene sm1cs-mes001-75 mes-regret-running-away-mes-at-least-while_c1 with dissolve
    play voice3 min_disappointed_off noloop
    mes "I regret running away from my problems but not seeing my parents. They needed me, and maybe I needed them more than I realized."
    mes "At least for a while."
    play sound sfx_cloth_rustling3
    scene sm1cs-mes001-76 mc-ask-what-happened-mes-responds-family-tried-setting-up-respectful-suitor_c1 with dissolve
    play voice2 mc_surprised_uh2 noloop
    mc "What happened?"
    play voice3 min_thinking_hmm1 noloop
    mes "My {i}loving{/i} family tried setting me up with a 'nice, respectable' suitor — who does that these days?"
    scene sm1cs-mes001-77 mc-tries-hides-grin-telling-almost-got-married-korea-mes-light-laugh-exactly_c1 with dissolve
    play voice2 mc_thinking_oh1 noloop
    mc "Are you telling me you almost got an set up for an arranged marriage type date in Korea?"
    scene sm1cs-mes001-78 mes-laughs-know-they-meant-well-mes-they-saw-floundering_c1 with dissolve
    play voice3 min_old_laugh noloop
    mes "*light laugh* Exactly. I said 'hard pass,' obviously. But it was still awkward as hell."
    mes "*sighs* I know they meant well."
    mes "They saw me floundering, they knew I was upset about life, and they thought, 'Oh, a stable relationship will fix everything'."
    scene sm1cs-mes001-79 mc-too-bad-not-consider-happiness-mes-exactly_c1 with dissolve
    play voice2 mc_disappointed_ehh4 noloop
    mc "Too bad they didn't consider that stable also means \"happy\" something a forced setup wouldn't necessarily guarantee."
    scene sm1cs-mes001-80 mes-so-about-studio-job-actual-hobby_c1 with dissolve
    play voice3 min_yes_happy noloop
    mes "Exactly."
    mes "So, about the studio... Is it actually a job or more of a hobby?"
    play sound sfx_hair_scratch1
    scene sm1cs-mes001-81 mc-fulltime-job-only-client-readhead_c1 with dissolve
    play voice2 mc_surprised_oh3 noloop
    mc "Oh it's a full-time job."
    mc "I mean, we only have one real client so far — a guy who specifically wanted a redhead in his short film."
    mc "But it's a start."
    scene sm1cs-mes001-82 mc-but-start-mes-impressive-assumed-just-messing-around_c1 with dissolve
    play voice3 min_hey_simple noloop
    mes "Impressive. I just assumed you two were just messing around with a camera in a warehouse."
    scene sm1cs-mes001-83 mc-hey-do-that-too-can-be-serious-mes-find-that-hard-believe_c1 with dissolve
    play voice2 mc_hey_hey3 noloop
    mc "Hey, we do that to, but we can be serious when we need to be."
    play voice3 min_no_nope noloop
    mes "I find that hard to believe."
    scene sm1cs-mes001-84 mes-maybe-bit-jelous-mc-hah-hard-believe_c1 with dissolve
    play voice3 min_arrogant_heh1 noloop
    mes "Or maybe I'm just the teensy bit jealous."
    play voice2 mc_arrogant_heh3 noloop
    mc "Hah, hard to believe that."
    scene sm1cs-mes001-85 mes-getting-mad-being-serious-took-a-risk_c1 with dissolve
    play voice3 min_hey_angry1 noloop
    mes "I'm being serious. You took a risk, and it's paying off. Meanwhile, I'm just drifting."
    scene sm1cs-mes001-86 mc-should-come-by-mes-sure-stacy-fine-with-it_c1 with dissolve
    play voice2 mc_thinking_hmm8 noloop
    mc "You should come check it out sometime. When you're not busy."
    play voice3 min_surprised_ehh1 noloop
    mes "Stacy wouldn't mind me poking around your big project, given our history?"
    scene sm1cs-mes001-87 mc-wont-be-problem-both-can-be-super-driven_c1 with dissolve
    play voice2 mc_no_nah2 noloop
    mc "It won't be a problem. I'm sure, given the chance, you two would connect."
    mc "You both can be super driven."
    play sound sfx_cloth_rustling2
    scene sm1cs-mes001-88 mes-small-chuckle-hm-was-once-right-mc-not-gone-min_c1 with dissolve
    play voice3 min_thinking_hmm3 noloop
    mes "Hmmm. I was once, wasn't I?"
    play voice2 mc_happy_yay2 noloop
    mc "It's not gone, Min. That would be impossible."
    mc "Maybe your spark is just a little sleepy, but I {i}know{/i} it's there, Min."
    scene sm1cs-mes001-89 mc-maybe-spark-just-sleepy-mes-always-knew-how-say-right-things_c1 with dissolve
    play voice3 min_disappointed_ehh2 noloop
    mes "You always did know how to say the right thing to make me feel better."
    scene sm1cs-mes001-90 mc-being-honest-winging-it-mes-laughs-good-know-things-never-change_c1 with dissolve
    play voice2 d2s9_confused noloop volume 1.4
    mc "If I'm being honest, half of the time, I'm winging it, hoping for the best."
    play voice3 min_arrogant_huh2 noloop
    mes "*laughs lightly* Good to know some things never change."
    scene sm1cs-mes001-91 mct-laughter-most-genuine-thing-tonight_c1 with dissolve
    play voice2 mc_thinking_hmm3 noloop
    mct "This laughter is the most genuine thing I've seen from her tonight. It's like a weight has lifted, at least momentarily."
    scene sm1cs-mes001-92 mes-upbeat-well-missed-mc-his-goofy-jokes-used-drive-crazy-now-realize-comfort_c1 with dissolve
    play voice3 min_disappointed_ehh1 noloop
    mes "Well, [mcname], I've got to say, I missed you. You and your silly jokes, the way you always found something goofy in every serious situation."
    mes "It used to drive me crazy, but now I realize how comforting it was."
    scene sm1cs-mes001-93 mc-hey-that-my-specialty_c1 with dissolve
    play voice2 mc_hey_hey8 noloop
    mc "Hey, that's my specialty, acting like a doofus when tension gets too high."
    play sound sfx_cloth_rustling1
    scene sm1cs-mes001-94 mes-stands-up-might-have-another-drink-mc-can-celebrate-with-without-alcohol_c1 with dissolve
    play voice3 min_happy_phew noloop
    mes "You know what, maybe I will have another drink. Or maybe not. I'm not trying to get hammered tonight."
    mes "But I feel like celebrating just a tiny bit — celebrating the fact that I'm not alone here after all."
    play voice2 mc_yes_sure1 noloop
    mc "We can celebrate with or without alcohol, your call. I'm good either way."
    play sound sfx_heels_steps1 loop
    scene sm1cs-mes001-95 mes-lets-go-light-mc-right-continuing-buisness-program_c1 with dissolve
    play voice3 min_yes_aga noloop
    mes "Let's go light on it. The last thing I need is a killer hangover with classes starting up again soon."
    play voice2 mc_yes_yeah8 noloop
    mc "Right, you're continuing your business management program, yeah?"
    play sound2 sfx_heels_steps2
    scene sm1cs-mes001-96 mes-explain-skip-few-electives-mc-makes-sense_c1 with dissolve
    play voice3 min_yes_yeah1 noloop
    mes "Yeah. I might skip a few electives this semester to focus on the core classes, though. My head's been a mess, so I need to pace myself."
    play voice2 mc_thinking_hmm6 noloop
    mc "Makes sense. Honestly, if you ever need help studying, you know where to find me."
    scene sm1cs-mes001-97 mes-something-tells-her-bigger-distraction-mc-hey-know-temper-sex-appeal_c1 with dissolve
    play voice3 min_angry_cough noloop
    mes "Something tells me you'd be a bigger distraction than a help."
    play voice2 mc_hey_hey6 noloop
    mc "*mock offense* Hey, I know how to tamper down my sex appeal. I'm not some out-of-control sex addict."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene sm1cs-mes001-98 mes-orders-drink-ofc-not-mes-probably-show-with-camera-crew-for-movie_c1 with dissolve
    play voice3 min_no_happy noloop
    mes "No, of course not. That's a totally normal response."
    mes "*teasing* Sure, sure. You'd probably show up with a camera crew and say it's for your next short film."
    play sound sfx_bottle_pouring1
    scene sm1cs-mes001-99 mc-now-that-idea-mes-id-watch-that_c1 with dissolve
    play voice2 mc_surprised_ohmy noloop
    mc "Now that's an idea. \"Documenting the daily struggles of a college student dealing with a watersports addiction\". You'd star as yourself, of course, and I'd direct."
    play voice3 min_yes_active noloop
    mes "I'd watch that."
    play sound sfx_wineglass_ding1
    $ renpy.music.set_volume(1.0, 2.2, "music" )
    scene sm1cs-mes001-100 mc-mes-clink-glasses_c1 with dissolve
    pause
    scene sm1cs-mes001-101 drinking-montage-one_c1 with fade
    pause
    scene sm1cs-mes001-102 drinking-montage-three_c1 with fade
    pause
    scene sm1cs-mes001-102 drinking-montage-two_c1 with fade
    pause
    $ renpy.music.set_volume(0.4, 2.2, "music" )
    scene sm1cs-mes001-103 mes-checks-phone_c1 with fade
    pause
    scene sm1cs-mes001-104 mes-getting-late-should-go-mc-really-glad-had-chance-talk_c1 with dissolve
    play voice3 min_arrogant_huh1 noloop
    mes "It's getting late. I should get going."
    play voice2 mc_scared_oh1 noloop
    mc "Min... I'm really glad we got a chance to talk. I know you've been through hell. If there's anything I can do — anything at all — just say the word."
    scene sm1cs-mes001-105 mes-done-that-already-mes-keep-in-mind_c1 with dissolve
    play voice3 min_hey_greeting noloop
    mes "You've already done plenty, [mcname]."
    mes "But I'll keep that in mind."
    scene sm1cs-mes001-106 mes-if-nothing-else-enjoy-drinks-down-line-if-up-for-it_c1 with dissolve
    play voice3 min_yes_ugu noloop
    mes "If nothing else, I'm sure I'd enjoy drinks again. Down the line."
    mes "If you're up to it."
    scene sm1cs-mes001-107 mc-cool-deal-then_c1 with dissolve
    play voice2 mc_yes_yeah1 noloop
    mc "Cool, it's a deal then."
    scene sm1cs-mes001-108 mes-enjoy-moment-end-scene_c1 with dissolve
    pause
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 5.5, "sound4" )
    $ renpy.music.set_volume(1.0, 3.0, "music" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_sound2" )
    stop sound4 fadeout 2.5
    jump sm1cs_mes001_end
label sm1cs_mes001_end:
    $ StoryController.end_scene(MES_STORY, 2, 0, 2)
    return