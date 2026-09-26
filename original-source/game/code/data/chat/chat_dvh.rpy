init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-t005"] = [
            {
                TYPE: MESSAGE,
                SENDER: "dvh",
                CONTENT: _("Come to the theater at Noon."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "dvh",
                CONTENT: _("It's important."),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: THEATER_STORY_LINE,
                CONTENT: _("Ok, I'll be there! 🫡"),
            },
        ]
