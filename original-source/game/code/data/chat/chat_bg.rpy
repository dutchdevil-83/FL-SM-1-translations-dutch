init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-bg004"] = [
            {
                TYPE: MESSAGE,
                SENDER: "bg",
                ACTION: PROGRESS_STORY,
                TARGET: BG_STORY,
                CONTENT: _("hey! The pics from the last photo shoot are ready!"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Sweet!"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "bg",
                CONTENT: _("u should come by the studio and check them out"),
            },
        ]
