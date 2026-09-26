init -1 python:
    class PlayerController:
        @staticmethod
        def read_book(itemname, inc=1):
            EventController.action(USE_ITEM, itemname)
            item = STORE_ITEMS_CATALOGUE[itemname]
            inc = item[INCREMENT]
            current = player.get_topic(item[TOPIC])
            limit = item[LIMIT]
            if current < limit:
                if current + inc > limit:
                    inc = limit - current
                player.add_topic(item[TOPIC], inc)
                player.log_action(f"Read '{item[NAME]}' and got {inc} point(s) for '{item[TOPIC]}'")
            else:
                renpy.notify(_("You already learned everything from this book"))
                player.log_action(f"Maxed learning from '{item[NAME]}'")
            renpy.play(audio.sfx_menu_notification1, channel="sound9")
            renpy.jump("lst_read_book_on_couch")
    
        @staticmethod
        def buy_item(itemname):
            item = STORE_ITEMS_CATALOGUE[itemname]
            if player.has_enough_money(item[COST]):
                player.spend_money(item[COST], item[TYPE], _("You bought {} for ${}").format(item[NAME], item[COST]))
                EventController.action(ITEM_PURCHASED, itemname)
                if item[TYPE] == ENERGY_DRINK:
                    PlayerController.energy_drink_consume()
                    player.log_action("Bought 'Energy Drink'")
                    renpy.jump("location_reenter")
                elif item[TYPE] in [BOOK, MAGAZINE]:
                    couch = ObjectController.get_object(COUCH)
                    couch.add_override_interaction_option(item[INTERACION_OPTION])
                    CharacterController.update_interaction_options(interaction_character)
                    player.log_action(f"Bought '{item[NAME]}'")
                    renpy.jump("purchase_item")
            else:
                renpy.notify(_("You don't have enough money."))
    
        @staticmethod
        def energy_drink_consume():
            player.add_energy(3)
            player.log_action("Consumed 'Energy Drink'")
