init 1 python:
    STORE_ITEMS_CATALOGUE ={
            PHOTOGRAPHY_101: {
                NAME: _("Photography-101"),
                INCREMENT: 1,
                LIMIT: 10,
                COST: 60,
                TOPIC: TOPIC_PHOTOGRAPHY,
                INTERACION_OPTION: "io-read_photography_book",
                TYPE: BOOK,
            },

            AN_ACTOR_PREPARES: {
                NAME: _("An Actor Prepares"),
                INCREMENT: 1,
                LIMIT: 10,
                COST: 60,
                TOPIC: TOPIC_LITERATURE,
                INTERACION_OPTION: "io-read_an_actor_prepares_book",
                TYPE: BOOK,
            },

            STARS_WEEKLY: {
                NAME: _("Stars Weekly"),
                INCREMENT: 1,
                LIMIT: 5,
                COST: 30,
                TOPIC: TOPIC_FILM_AND_TV,
                INTERACION_OPTION: "io-read_stars_weekly_magazine",
                TYPE: MAGAZINE,
            },

            ENERGY_DRINK:{
                NAME: _("D-Energy"),
                COST: 25,
                TYPE: ENERGY_DRINK,
            },
        }
