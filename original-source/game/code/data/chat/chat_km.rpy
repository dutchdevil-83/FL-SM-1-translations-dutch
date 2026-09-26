init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-km005"] = [
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                CONTENT: _("Hey Kellie. Are you busy?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "km",
                CONTENT: _("Kind of. Why?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("I need to talk to you about something."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "km",
                CONTENT: _("Can it wait?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Not really?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "km",
                CONTENT: _("Fine. Meet me in Denise's office."),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Great."),
                ACTION: PROGRESS_STORY,
                TARGET: KM_STORY,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
            },
        ]
