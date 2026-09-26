init -1 python:
    class SCController:
    
        @staticmethod
        def read_magazine():
            topic = TOPIC_TECHNOLOGY
            EventController.action(USE_ITEM, SC_TECH_MAG)
        
            if player.get_topic(topic) < 10:
                player.add_topic(topic, 1)
                player.log_action(f"Read 'SC Magazine' and got 1 point for '{topic}'")
            else:
                renpy.notify(_("You already learned everything from this magazine"))
                player.log_action("Maxed learning from 'SC Magazine'")
        
            renpy.play(audio.sfx_menu_notification1, channel="sound9")
            renpy.jump("location_reenter")
