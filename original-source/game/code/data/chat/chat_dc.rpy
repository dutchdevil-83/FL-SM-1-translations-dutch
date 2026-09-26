init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-dc007"] = [
            {
                TYPE: MESSAGE,
                SENDER: "dc",
                ACTION: PROGRESS_STORY,
                TARGET: DC_STORY,
                TIMESLOTS: [TIMESLOT_7],
                CONTENT: _("Hey, [mcname!i]! I just wanted to say that I'm really happy I finally told you everything, and I am really excited for that future date! 😜"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Hey Debbie! Im glad we talked too. Im also pretty pumped for this date"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("In fact, what are you doing tonight?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "dc",
                CONTENT: _("I'm actually stuck working the next few night shifts 😞"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Booo! Well, maybe I'll run into you in the park"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "dc",
                ACTION: PROGRESS_STORY,
                TARGET: DC_STORY,
                CONTENT: _("I would love that 😊"),
            },
        ]

    CHARACTER_CHAT_CATALOGUE["sms-dc008"] = [
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                TIMESLOTS: [TIMESLOT_7],
                CONTENT: _("Hey Debbie! 👋"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "dc",
                CONTENT: _("Hey, [mcname!i]! What can I do for you?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Well I promised you a date and I was wondering if you'd want to go on a date soon? 😊"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "dc",
                CONTENT: _("That sounds delightful!"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("There's this nice restaurant... wanna go there?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "dc",
                CONTENT: _("It sounds like a date, [mcname!i] 😉"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: DC_STORY,
                TIMESLOTS: [TIMESLOT_7],
                CONTENT: _("I'll send  you the address! See you in a bit 😏"),
            },
        ]
