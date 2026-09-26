init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-tl005"] = [
            {
                TYPE: MESSAGE,
                SENDER: "tl",
                ACTION: PROGRESS_STORY,
                TARGET: TL_STORY,
                TIMESLOTS: [TIMESLOT_7],
                CONTENT: _("hey, could you swing by the haunted house"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Everything okay?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "tl",
                CONTENT: _("ya just need ur help with something"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: TL_STORY,
                TIMESLOTS: [TIMESLOT_7],
                CONTENT: _("Sure, I'll head over there"),
            },
        ]
    CHARACTER_CHAT_CATALOGUE["sms-tl006"] = [
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                TIMESLOTS: [TIMESLOT_6],
                CONTENT: _("Hey Taisia 👋"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "tl",
                CONTENT: _("yo"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("I was thinking about you"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "tl",
                CONTENT: _("ngl playing pool with you was fun the other night"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "tl",
                CONDITIONS: [{TYPE: PLAYER_CHOICE, VARIABLE: "sm1cs_tl_pool_kiss", VALUE: True}],
                CONTENT: _("even if you cheated"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONDITIONS: [{TYPE: PLAYER_CHOICE, VARIABLE: "sm1cs_tl_pool_kiss", VALUE: True}],
                CONTENT: _("Hey! I won that kiss fair and square! And I'll play you again to prove it!"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "tl",
                CONDITIONS: [{TYPE: PLAYER_CHOICE, VARIABLE: "sm1cs_tl_pool_kiss", VALUE: False}],
                CONTENT: _("even tho i kicked your ass"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONDITIONS: [{TYPE: PLAYER_CHOICE, VARIABLE: "sm1cs_tl_pool_kiss", VALUE: False}],
                CONTENT: _("don't worry, we're going to have a rematch one of these days"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "tl",
                CONTENT: _("how bout tonight?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("funny enough, Stacy and I were just talking about how we all needed to hang out"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "tl",
                CONTENT: _("well youre both welcome to come by the bar, im there most nights"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: TL_STORY,
                TIMESLOTS: [TIMESLOT_6, TIMESLOT_7],
                CONTENT: _("we'll be there!"),
            },
        ]
