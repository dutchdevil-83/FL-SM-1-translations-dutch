label sm1ms002_t:
    play sound sfx_glass_bottle_bonk volume 0.4
    scene sm1ms002-09 sy-looking-away-disapointed_c1 with dissolve
    play voice3 stacy_thinking_hmm1 noloop
    sy "Okay so it took some digging but I think I found someone who can you a job at the theater."
    mc "Great. Do you think she might also be interested in making videos with us?"
    scene sm1ms002-13 sy-confident-wants-start-over_c1 with dissolve
    play voice3 stacy_arrogant_huh4 noloop
    sy "Totally. Check out this video she made..."
    scene sm1ms002-14 sy-explains-like-teacher_c1 with dissolve
    play voice3 stacy_happy_hmm1 noloop
    sy "As I was about to tell you, the actress in question has several distinctive features."
    sy "First of all, she's in the hottest ATM video I have ever seen - using a massive dildo."
    sy "Second, she's wearing full body make-up that is damn well unique."
    play sound sfx_gadgets_laptop_opened
    scene sm1ms002-15 sy-opens-computer-shows-him-screen-begin-tutorial_c1 with dissolve
    play voice3 stacy_thinking_hmm3 noloop
    sy "Isn't it stimulating? There is just something about it that really gets my engine going."
    sy "I mean, how does she take THAT and put it THERE? It's massive! Then in her mouth..."
    scene sm1ms002-16-01 laptop-close-up_c1
    show sm1ms002-16-01_tl-deepthroat-cam_c1
    with dissolve
    play voice3 stacy_disappointed_mmm1 noloop
    sy "Then she shoves it down her throat without a second's hesitation."
    sy "I mean, even if you've practiced deepthroating THAT and you had an enema there should be some hesitation."
    mct "Wait a second..."
    sy "She's a dirty, dirty girl."
    scene sm1ms002-16 sy-ask-how-does-that-sound_c1 with dissolve
    play voice3 stacy_moan6 noloop
    sy "That is so fucking hot."
    play voice2 mc_arrogant_heh1 noloop
    mc "I know her."
    sy "Every time I see this video it just makes me so wet-"
    scene sm1ms002-17 mc-choice-menu_c1 with dissolve
    play voice3 stacy_surprised_huh2 noloop
    sy "What?!"
    sy "What do you mean that you know her?!"
    sy "How could you possibly!!!"
    scene sm1ms002-18 mc-simple-enough_c1 with dissolve
    play voice2 d1s2_mchey noloop volume 1.6
    mc "I mean, you know I get around. But I don't \"know her\" know her."
    mc "But I have seen her before in that clown make-up."
    scene sm1ms002-19 mc-still-confused-mc-doesnt-get-it-sy-ask-which-part_c1 with dissolve
    play voice3 stacy_surprised_how2 noloop
    sy "Who is she?!"
    play voice2 mc_arrogant_huh1 noloop
    mc "I don't know her name, but she works at the Haunted House over at the Amusement Park."
    mc "I mean, I didn't think she was real. She doesn't move or do anything."
    scene sm1ms002-20 mc-didnt-get-whole-thing-sy-lets-try-again_c1 with dissolve
    play voice3 stacy_surprised_huh1 noloop
    sy "You're bullshitting me."
    play voice2 mc_no_no1 noloop
    mc "Honest. There's a woman - or maybe a mannequin based on her - with that exact make-up and everything."
    scene sm1ms002-21 sy-happy-mc-got-it-put-it-in-phone_c1 with dissolve
    play voice3 stacy_arrogant_hmm2 noloop
    sy "You had better not be lying to me. This could be just the breakthrough we need!"
    sy "I was just going to visit the theater associated with the IP Address, but now I want to see her in action!"
    scene sm1ms002-22 sy-ask-anything-else-mc-gets-it-has-question_c1 with dissolve
    play voice2 mc_thinking_emm1 noloop
    mc "Question? If we find her, do I get to fuck her?"
    play voice3 stacy_yes_yap1 noloop
    sy "That's the plan."
    scene sm1ms002-23 mc-ask-question_c1 with dissolve
    play voice2 mc_yes_okay3 noloop
    mc "Okay, so can we go over to the Haunted House and see if we can get her to talk."
    mc "Or, you know, whatever."
    scene sm1ms002-27 sy-leans-back-chair-mc-should-look-be-promoted_c1 with dissolve
    play voice3 stacy_angryhuh noloop
    sy "But this better not be some kind of prank."
    play voice2 d1s5_mchappy noloop volume 1.7
    mc "She'll be there. But if I also get to prank you that will be even better."
    sy "You wouldn't dare."
    scene sm1ms002-28 sy-tells-interviews-every-week-no-conflict_c1 with dissolve
    play voice3 stacy_thinking_hmm2 noloop
    sy "Okay, so here's the plan. We'll go over some evening."
    sy "Check out your \"dummy\" and see if we can get her to talk - or at least find out who made her."
    sy "Sounds right?"
    scene sm1ms002-29 mc-stands-up-jokes-captain-obvs_c1 with dissolve
    play voice2 mc_yes_aga2 noloop
    mc "I like most of your plan, but it's already too late tonight."
    if player.get_energy_percent >= 20:
        mc "I'm too fucking tired."
    else:
        mc "I might have other plans."
    scene sm1ms002-31 mc-walks-towards-bed_c1 with dissolve
    play voice2 mc_thinking_mmm4 noloop
    mc "I'll let you know when we can go."
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 3.0, "freeroam_music1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound1" )
    $ renpy.music.set_volume(1.0, 1.0, "freeroam_sound2" )
    return