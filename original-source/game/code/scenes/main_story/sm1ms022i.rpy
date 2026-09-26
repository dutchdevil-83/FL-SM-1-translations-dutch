label sm1ms022i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "excited01") as sy_excited01
    play voice3 stacy_surprised_huh4 noloop
    sy "Are you ready to film!?"
    play voice2 mc_yes_yeah2 noloop
    mc "Yep!"
    sy "Do you have the money for Kanya?"
    menu:
        "Give Stacy the $200" if player.money>=200 and player.enough_energy(5):
            $ player.spend_money(200, _("Kanya's compensation"), _("You gave $200 to Stacy"))
            $ player.consume_energy(5)
            hide sy_excited01
            show expression cc.get_expression_image("sy", "smile01") as sy_smile01
            play voice3 stacy_yes_okay1 noloop
            sy "Okay. Now help me move this stuff and get the set ready!"
            play voice2 mc_yes_okay1 noloop
            mc "Okay."
            $ StoryController.end_scene(MS)
        "I don't have the money" if player.enough_energy(5):
            hide sy_excited01
            show expression cc.get_expression_image("sy", "angry01") as sy_angry01
            play voice3 stacy_angry_aah1 noloop
            sy "Then come back when you have it!"
            hide sy_angry01
            sy "{size=20}Goddamn [mcname], getting me excited for nothing.{/size}"
            $ player.progress_storyline(MS, -1)
        "I'm too tired..." if not player.enough_energy(5):
            hide sy_excited01
            show expression cc.get_expression_image("sy", "sad01") as sy_sad01
            play voice3 stacy_disappointed_oh1 noloop
            sy "Then we will do it tomorrow..."
            $ player.progress_storyline(MS, -1)
    return