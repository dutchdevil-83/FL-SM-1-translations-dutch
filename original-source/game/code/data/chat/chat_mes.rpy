init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-mes003"] = [
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Hey Min. What's happening?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("Classes, studying, sleep 😓"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("Starting to wish I never came back here 😕"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("It's going to get better. I just know it."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("How can I help you, [mcname!i]?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("I want to invite you to check out the studio 😊"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("I would, but I should focus."),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Come on. You're working yourself too hard."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("Ok."),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: MES_STORY,
                CONTENT: _("There you go. Trust me. You're going to love the place."),
            },
        ]

    CHARACTER_CHAT_CATALOGUE["sms-mes004"] = [
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                ACTION: PROGRESS_STORY,
                TARGET: MES_STORY,
                TIMESLOTS: [TIMESLOT_7],
                CONTENT: _("Hey. Want to go for a drink?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("It will be on me."),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Sure. What's the occasion?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("Nothing special. Call it a mind-break date 😇"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Oh. I like the sound of that 😀"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("Don't be strange. I didn't mean a \"date\" date."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("Well."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "mes",
                CONTENT: _("Nevermind. Are you down or not?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: MES_STORY,
                TIMESLOTS: [TIMESLOT_7],
                CONTENT: _("Yes, Min. Send me the details."),
            }
        ]
