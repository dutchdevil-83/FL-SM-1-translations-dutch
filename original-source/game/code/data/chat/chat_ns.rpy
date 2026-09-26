init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-ns010"] = [
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                TIMESLOTS: [TIMESLOT_7],
                CONTENT: _("Hey! I have an idea. Can we meet in cafe?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "ns",
                CONTENT: "😁😜😊...🍆💦? 😇",
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("No-no, I want you to meet someone! Can you come?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "ns",
                CONTENT: "🏃",
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: NS_STORY,
                CONTENT: _("See you there!"),
            },
        ]
