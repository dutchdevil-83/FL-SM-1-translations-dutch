init 2 python:
    CHARACTER_CHAT_CATALOGUE["sms-ms021"] = [
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                NEED_MONEY: 200,
                CONTENT: _("Hey Kanya."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "kv",
                CONDITIONS: [{TYPE: PLAYED_SCENE, VARIABLE: KV_STORY, VALUE: "sm1cs_kv003"}],
                CONTENT: _("Hey stud."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "kv",
                CONDITIONS: [{TYPE: NOT_PLAYED_SCENE, VARIABLE: KV_STORY, VALUE: "sm1cs_kv003"}],
                CONTENT: _("Hiya [mcname!i]."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "kv",
                CONTENT: _("What's cooking?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Stacy and I are planning to cook up a new film 🎬🎬🎬"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "kv",
                CONTENT: _("Asking me to be the 🎥 girl again?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("You know me too well."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "kv",
                CONTENT: _("😝"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "kv",
                CONTENT: _("What's this one going be about?"),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("We haven't figured out the details."),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("But the client wants to focus on anal 🍑"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "kv",
                CONTENT: _("🔥🔥🔥"),
            },
            {
                TYPE: MESSAGE,
                SENDER: "kv",
                CONTENT: _("Stacy might be in trouble, lol."),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("She'll be fine."),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                CONTENT: _("Not our first trip into the mud."),
            },
            {
                TYPE: MESSAGE,
                SENDER: "kv",
                CONTENT: _("Eww. So gross. Haha. Text me when you need me."),
            },
            {
                TYPE: MESSAGE,
                SENDER: YOU,
                ACTION: PROGRESS_STORY,
                TARGET: MS,
                NEED_MONEY: 200,
                CONTENT: _("Sure!"),
            },
        ]
