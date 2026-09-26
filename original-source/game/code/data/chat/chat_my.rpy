init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-my001"] = [
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                CONTENT: _("Hey, Mom. I just wanted to say thank you for all your help working on the studio"),
                CONDITIONS: [{TYPE: PERSISTENT, VARIABLE: "is_special", VALUE: True}],
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                CONTENT: _("Hey, Melony. I just wanted to say thank you for all your help working on the studio"),
                CONDITIONS: [{TYPE: PERSISTENT, VARIABLE: "is_special", VALUE: False}],
            },
            {
                TYPE: MESSAGE,
                SENDER: "my",
                CONTENT: _("Of course, sweetie! Happy to help"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("I was wondering if I could maybe treat you to dinner? As a way to show my gratitude?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "my",
                CONTENT: _("I would love that!"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Awesome! I'll send you the address of the restaurant. Is 7 ok?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "my",
                CONTENT: _("Sounds great to me!"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: MY_STORY,
                TIMESLOTS: [TIMESLOT_5, TIMESLOT_6],
                CONTENT: _("See you soon!"),
            },
        ]
