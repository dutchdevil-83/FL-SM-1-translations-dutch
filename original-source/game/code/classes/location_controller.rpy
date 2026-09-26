init -1 python:
    class LocationController:
    
        @staticmethod
        def enter():
            global curr_location, curr_sublocation, curr_position
            location_schedule = LocationController.get_location_schedule(curr_location, curr_sublocation, curr_position)
            if location_schedule and location_schedule[OPEN]:
                EventController.action(ENTER_LOCATION)
                ChatController.get_waiting_chats()
                return
            renpy.jump("city_map")
    
        @staticmethod
        def get_location(location, sublocation, position):
            key = f"{location}_{sublocation}_{position}"
            if key in indexed_locations_list:
                return indexed_locations_list[key]
            print_verbose(f"Error: location not found \"{location}_{sublocation}_{position}\"")
            return False
    
        @staticmethod
        def get_location_with_codename(location):
            if location in indexed_locations_list:
                return indexed_locations_list[location]
            print_verbose(f"Error: location not found - \"{location}\"")
            return False
    
        @staticmethod
        def get_map_location(location):
            if location in indexed_map_locations_list:
                return indexed_map_locations_list[location]
            print_verbose(f"Error: location not found - \"{location}\"")
            return False
    
        @staticmethod
        def get_characters_and_objects_for_sandbox():
            results = CharacterController.get_characters_for_sandbox() + ObjectController.get_objects_for_sandbox()
            return sorted(results, key=lambda x: int(x.get_pose_depth(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)), reverse=True)
    
        @staticmethod
        def draw_current_location(skip_character=False, skip_object=False, bg_blur=True):
            if vn_mode:
                VNModeController.set_location_data(current_label)
                renpy.music.play(get_location_music()[0],    channel = "freeroam_music1", loop = True, fadeout = 0.5, fadein = 1.0 , if_changed = True, relative_volume = get_location_music()[1])
                renpy.music.play(get_location_ambience()[0], channel = "freeroam_sound1", loop = True, fadeout = 0.15, fadein = 0.12 , if_changed = True, relative_volume = get_location_ambience()[1])
                renpy.music.play(get_location_subambience()[0], channel = "freeroam_sound2", loop = True, fadeout = 0.15, fadein = 0.12 , if_changed = True, relative_volume = get_location_subambience()[1])
        
        
            location_obj = LocationController.get_location(curr_location, curr_sublocation, curr_position)
            scene_bg = location_obj.get_location_image(curr_vn_time if vn_mode else None)
            renpy.scene()
            renpy.show(scene_bg, at_list=[interaction_bg_blur] if bg_blur else [])
        
            LocationController.show_objects(skip_object, bg_blur)
            LocationController.show_characters(skip_character, bg_blur)
    
        @staticmethod
        def show_objects(skip_object, bg_blur):
            for obj in sm_objects_list:
                if obj.get_lock_status() and obj.get_schedule_in_location(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                    if not skip_object or obj.codename != skip_object or not obj.is_in_base_image:
                        obj_image = obj.get_object_image(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
                        renpy.show(obj_image, at_list=[interaction_bg_blur] if bg_blur else [])
    
        @staticmethod
        def show_characters(skip_character, bg_blur):
            for char in sm_characters_list:
                if char.has_schedule() and char.get_schedule_in_location(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                    if not skip_character or char.codename != skip_character:
                        char_image = char.get_character_image(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
                        renpy.show(char_image, at_list=[interaction_bg_blur] if bg_blur else [])
    
        @staticmethod
        def get_visible_locations():
            results = []
            for location in sm_locations_list:
                if location.get_discovered_status():
                    results.append(location)
            return results
    
        @staticmethod
        def get_current_location_data():
            return LocationController.get_location(curr_location, curr_sublocation, curr_position)
    
        @staticmethod
        def get_location_schedule(location, sublocation, position):
            return LocationController.get_location(location, sublocation, position).get_schedule(gt.curr_timeslot, gt.curr_day)
    
        @staticmethod
        def enter_location(location, sublocation, position, skip_interaction=False):
            if position == MAP:
                player.log_action("Jumped to 'the Map' because 'position == MAP'")
                renpy.jump("city_map")
            l = LocationController.get_location(location, sublocation, position)
            if not location:
                return
            if not skip_interaction:
                LocationController.handle_interaction(l)
            if l.get_lock_status() is True:
                LocationController.notify_location_unavailable()
                return
            elif l.get_lock_status() is not False:
                player.log_action(f"Redirected from '{sublocation}' to '{l.get_lock_status()}'")
                LocationController.notify_location_unavailable()
                renpy.jump(f"{location}_{l.get_lock_status()}")
                return
            location_schedule = LocationController.get_location_schedule(location, sublocation, position)
            if not location_schedule:
                return
            if location_schedule[OPEN]:
                player.log_action(f"Entered location '{l.get_codename()}'")
                renpy.jump(f"{location}_{sublocation}_{position}")
            else:
                LocationController.handle_closed_location(l)
    
        @staticmethod
        def handle_interaction(location):
            global interaction_options
            interaction_options = location.get_interaction_options(gt.curr_timeslot, gt.curr_day)
            interaction_options = InteractionLocationOption.get_visible_interaction_options(interaction_options)
            if interaction_options:
                player.log_action(f"Entered interaction menu for location '{location.get_codename()}'")
                renpy.call("interaction_menu_location", location.location, location.sublocation, location.position)
    
        @staticmethod
        def notify_location_unavailable():
            renpy.notify(_("This location is not accessible right now"))
            renpy.play(audio.sfx_nonogram_error1, channel="sound9")
    
        @staticmethod
        def handle_closed_location(location):
            closed_data = location.get_open_status()
            reasons = {
                    LOC_CLOSED_REASON_SCHEDULE_DAY: _("This location is closed today"),
                    LOC_CLOSED_REASON_SCHEDULE_OPENS_LATER: _("This location is not open yet"),
                    LOC_CLOSED_REASON_SCHEDULE_ALREADY_CLOSED: _("This location is already closed for the day"),
                    LOC_CLOSED_REASON_NOT_UNLOCKED: _("This location is unavailable"),
                    LOC_CLOSED_REASON_LOCKED_WITH_REDIRECT: _("This location is unavailable")
                }
            renpy.notify(reasons.get(closed_data[REASON], _("This location is unavailable")))
            renpy.play(audio.sfx_nonogram_error1, channel="sound9")
    
        @staticmethod
        def check_location_open(location, sublocation, position):
            location_schedule = LocationController.get_location_schedule(location, sublocation, position)
            return location_schedule and location_schedule[OPEN] and SMLocation.check_location_discovered(location, sublocation, position) and LocationController.get_location(location, sublocation, position).get_lock_status() is False
    
        @staticmethod
        def unlock_position(location, sublocation, position):
            LocationController.get_location(location, sublocation, position).unlock()
    
        @staticmethod
        def unlock_all_sublocation(location):
            for l in sm_locations_list:
                if l.location == location:
                    l.unlock()
                    l.discover()
