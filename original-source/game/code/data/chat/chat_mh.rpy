init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-mh007"] = [
            {
                TYPE: MESSAGE,
                SENDER: "mh",
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
                TIMESLOTS: [TIMESLOT_4],
                CONTENT: _("Hey! What's up?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Not much, thinking about you 😎"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mh",
                CONTENT: _("Same here. I'm at home, you want to come over?"),
            },
            {
                TYPE: PHOTO,
                SENDER: "mh",
                CONTENT: "d19s08-23 mh-turns-sideways-hand-between-thighs_c1",
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                CONTENT: _("ON MY WAY!"),
            },
        ]

    CHARACTER_CHAT_CATALOGUE["sms-mh009"] = [
            {
                TYPE: MESSAGE,
                SENDER: "mh",
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
                CONTENT: _("Hey, [mcname!i]. I have the next few mornings off. I was wondering if I could stop by and see the new renovations?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Yeah! I'm totally free this morning, stop on by!"),
                TIMESLOTS: [TIMESLOT_3, TIMESLOT_4],
            },
            {
                TYPE: MESSAGE,
                SENDER: "mh",
                CONTENT: _("I'll be over in a jif"),
                ACTION: PROGRESS_STORY,
                TARGET: MH_STORY,
            },
        ]
