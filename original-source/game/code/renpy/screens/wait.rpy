screen wait_screen(what):
    if what == WURST_WORK:
        $ wait_text = _("Delivering Wurst...")
    elif what == IT_WORK:
        $ wait_text = _("Coding Solutions...")
    elif what == READ_BOOK:
        $ wait_text = _("Reading Book...")
    elif what == THEATER_JOB:
        $ wait_text = _("Working in the Theater...")
    add "sand_clock_anim" xalign 0.5 yalign 0.5
    text wait_text color "#FFF" size 80 xalign 0.5 yalign 0.2 outlines [(3, "#000000", 0, 0)]