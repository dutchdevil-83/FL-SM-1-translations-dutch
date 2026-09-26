label sm1ms007_01i:
    $ LocationController.draw_current_location("sy")
    show expression cc.get_expression_image("sy", "smile1") as lst_sy_smile1
    play voice2 d2s9_mchey noloop
    mc "Hey Stacy I think I have enough money for a wig."
    play voice3 stacy_yay noloop
    sy "Awesome work, [mcname]."
    $ player.spend_money(50, _("Wig for Stacy"), _("You gave $50 to Stacy for buying a wig"))
    sy "I'll order it online, it should be here tomorrow."
    play voice2 mc_yes_aga2 noloop
    mc "Thanks, love you."
    hide lst_sy_smile1
    show expression cc.get_expression_image("sy", "naughty1") as lst_sy_naughty1
    play voice3 stacy_thinking_hm1 noloop
    sy "Right back at you."
    $ StoryController.end_scene(MS)
    return