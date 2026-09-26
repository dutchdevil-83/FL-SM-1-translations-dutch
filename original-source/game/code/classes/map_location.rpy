init -1 python:
    class MapLocation:
        def __init__(self, name, codename, first_sublocation, first_position, posx, posy):
            self.name = name
            self.codename = codename
            self.first_sublocation = first_sublocation
            self.first_position = first_position
            self.posx = posx
            self.posy = posy
    
        def get_location_button_image(self):
            return f"images/ui/map/{self.codename}_map_button_%s.webp"
    
        def get_location(self):
            return LocationController.get_location(self.codename, self.first_sublocation, self.first_position)
    
        def get_lock_status(self):
            return self.get_location().get_lock_status()
    
        def unlock(self):
            player.log_action(f"Unlocked map location '{self.codename}'")
            return self.get_location().unlock()
    
        def lock(self, value=True):
            player.log_action(f"Locked map location '{self.codename}'")
            return self.get_location().lock(value)
    
        def click(self, d, t):
            location = self.get_location()
            EventController.action(MAP_LOCATION_CLICK, location.get_codename())
            ChatController.get_waiting_chats()
            reason_data = location.get_open_status()
            if reason_data[REASON] is False:
                self.handle_location_open(location)
            elif reason_data[REASON] == LOC_CLOSED_REASON_LOCKED_WITH_REDIRECT:
                self.handle_redirect(reason_data)
            else:
                renpy.notify(self.get_notify(d, t, reason_data))
    
        def handle_location_open(self, location):
            if curr_location != self.codename:
                player.travel(location.get_codename())
            player.log_action(f"Entered '{location.get_codename()}' from the 'Map'")
            renpy.jump(location.get_codename())
    
        def handle_redirect(self, reason_data):
            redirect_location = LocationController.get_location_with_codename(f"{self.codename}_{reason_data[TARGET]}")
            redirect_location_schedule = redirect_location.get_schedule(gt.curr_timeslot, gt.curr_day)
            if redirect_location_schedule and redirect_location_schedule[OPEN]:
                player.log_action(f"Redirected from '{self.first_position}' to '{reason_data[TARGET]}' from the 'Map'")
                if curr_location != self.codename:
                    player.travel(self.codename)
                renpy.jump(f"{self.codename}_{reason_data[TARGET]}")
            renpy.notify(_(f"{self.name} is unavailable"))
    
        def get_tooltip(self, d, t, is_character_list_needed=False, reason_data=False):
            character_list = CharacterController.get_characters_for_map(self.codename) if is_character_list_needed else False
            location = self.get_location()
            reason_data = reason_data or location.get_open_status()
            if reason_data[REASON] is False:
                return (reason_data[HINT] or _(f"Go to {self.name}")), character_list
            return self.get_reason_message(reason_data)
    
        def get_notify(self, d, t, reason_data=False):
            reason_data = reason_data or self.get_location().get_open_status()
            return self.get_reason_message(reason_data)
    
        def get_reason_message(self, reason_data):
            reason_messages = {
                    LOC_CLOSED_REASON_NOT_UNLOCKED: _(f"{self.name} is unavailable"),
                    LOC_CLOSED_REASON_LOCKED_WITH_REDIRECT: _(f"{self.name} is unavailable"),
                    LOC_CLOSED_REASON_SCHEDULE_OPENS_LATER: _(f"{self.name} is not open yet"),
                    LOC_CLOSED_REASON_SCHEDULE_ALREADY_CLOSED: _(f"{self.name} is already closed for the day"),
                    LOC_CLOSED_REASON_SCHEDULE_DAY: _(f"{self.name} is closed today")
                }
            return reason_data[HINT] if reason_data[HINT] else reason_messages.get(reason_data[REASON], "")
