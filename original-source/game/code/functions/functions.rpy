init python:
    import random
    import uuid



    def get_sy_surname():
        if persistent.is_special is True:
            return _("Young")
        return _("Brown")

    def get_my_surname():
        if persistent.is_special is True:
            return _("Young")
        return _("Chase")



    def spawn_text(text, x, y, text_size=30, t=1.0):
        tag = "spawn_{}".format(random.randint(0, 10000))
        Show("spawn_text_screen", spawned_text=text, x=x, y=y, text_size=text_size, time=t, tag=tag, _tag=tag)()



    def current_label_callback(name, call_or_jump):
        if name.startswith("_") or not call_or_jump:
            return
        if any(name.startswith(prefix) for prefix in ["sm1", "q_inter"]):
            setattr(renpy.store, "in_a_scene", True)
        else:
            setattr(renpy.store, "in_a_scene", False)
        setattr(renpy.store, "current_label", name)



    def sanitize_variable_name(name):
        sanitized_name = re.sub(r"\W|^(?=\d)", "_", name)
        return sanitized_name



    def save_namer(value):
        setattr(renpy.store, "save_name", value)



    def show_hover_notify(what):
        setattr(renpy.store, "notify_timeout", False)
        renpy.notify(what)

    def hide_hover_notify():
        setattr(renpy.store, "notify_timeout", True)
        renpy.hide_screen("notify")



    def get_uuid():
        return str(uuid.uuid4())



    def set_menu_hints(status=True):
        persistent.menu_hints = status

    set_menu_hints(False)



    def print_verbose(data):
        if is_dev_environment:
            print(data)



    def get_char_btn_pos(button_count):
        positions = []
        x_offset = 100
        y_offset = 250 - 64
        for i in range(button_count):
            line = i // 4
            pos_in_line = i % 4
            x_pos = (line * 210) + (x_offset if pos_in_line in [1, 3] else 0)
            y_pos = (pos_in_line * y_offset) if pos_in_line < 4 else 0
            positions.append((x_pos, y_pos))
        return positions



    def get_location_music():
        if not main_menu:
            for data in location_music_list:
                if curr_location in data[LOCATIONS] and (data[POSITIONS] == ALL_POSITIONS or curr_position in data[POSITIONS]) and (data[SUBLOCATIONS] == ALL_SUBLOCATIONS or curr_sublocation in data[SUBLOCATIONS]) and gt.curr_timeslot in data[TIMESLOTS] and gt.curr_day in data[DAYS]:
                    return data[NAME], data[VOLUME]
        return audio.freeroam_silence, 0.0

    def get_location_ambience():
        if not main_menu:
            for data in location_ambience_list:
                if curr_location in data[LOCATIONS] and (data[POSITIONS] == ALL_POSITIONS or curr_position in data[POSITIONS]) and (data[SUBLOCATIONS] == ALL_SUBLOCATIONS or curr_sublocation in data[SUBLOCATIONS]) and gt.curr_timeslot in data[TIMESLOTS] and gt.curr_day in data[DAYS]:
                    return data[NAME], data[VOLUME]
        return audio.freeroam_silence, 0.0

    def get_location_subambience():
        if not main_menu:
            for data in location_subambience_list:
                if curr_location in data[LOCATIONS] and (data[POSITIONS] == ALL_POSITIONS or curr_position in data[POSITIONS]) and (data[SUBLOCATIONS] == ALL_SUBLOCATIONS or curr_sublocation in data[SUBLOCATIONS]) and gt.curr_timeslot in data[TIMESLOTS] and gt.curr_day in data[DAYS]:
                    return data[NAME], data[VOLUME]
        return audio.freeroam_silence, 0.0

    def stop_all_sound():
        renpy.music.stop("music" , fadeout = 1.0)
        renpy.music.stop("music2", fadeout = 1.0)
        renpy.music.stop("music3", fadeout = 1.0)
        renpy.music.stop("music4", fadeout = 1.0)
        renpy.music.stop("sound" , fadeout = 1.0)
        renpy.music.stop("sound2", fadeout = 1.0)
        renpy.music.stop("sound3", fadeout = 1.0)
        renpy.music.stop("sound4", fadeout = 1.0)
        renpy.music.stop("sound5", fadeout = 1.0)
        renpy.music.stop("sound9", fadeout = 1.0)
        renpy.music.stop("voice" , fadeout = 1.0)
        renpy.music.stop("voice2", fadeout = 1.0)
        renpy.music.stop("voice3", fadeout = 1.0)
        renpy.music.stop("voice4", fadeout = 1.0)
        renpy.music.stop("voice5", fadeout = 1.0)
        renpy.music.stop("voice6", fadeout = 1.0)
        renpy.music.stop("voice7", fadeout = 1.0)
        renpy.music.stop("voice8", fadeout = 1.0)
        renpy.music.stop("voisex2", fadeout = 1.0)
        renpy.music.stop("voisex3", fadeout = 1.0)
        renpy.music.stop("voisex4", fadeout = 1.0)
        renpy.music.stop("voisex5", fadeout = 1.0)
        renpy.music.stop("voisex6", fadeout = 1.0)
        renpy.music.stop("voisex7", fadeout = 1.0)
        renpy.music.stop("voisex8", fadeout = 1.0)
        renpy.music.stop("freeroam_sound1", fadeout = 1.0)
        renpy.music.stop("freeroam_sound2", fadeout = 1.0)
        renpy.music.stop("freeroam_music1", fadeout = 1.0)

    def pause_all_sound():
        renpy.music.set_pause(True, channel = "music" )
        renpy.music.set_pause(True, channel = "music2")
        renpy.music.set_pause(True, channel = "music3")
        renpy.music.set_pause(True, channel = "music4")
        renpy.music.set_pause(True, channel = "sound" )
        renpy.music.set_pause(True, channel = "sound2")
        renpy.music.set_pause(True, channel = "sound3")
        renpy.music.set_pause(True, channel = "sound4")
        renpy.music.set_pause(True, channel = "sound5")
        renpy.music.set_pause(True, channel = "sound9")
        renpy.music.set_pause(True, channel = "voice" )
        renpy.music.set_pause(True, channel = "voice2")
        renpy.music.set_pause(True, channel = "voice3")
        renpy.music.set_pause(True, channel = "voice4")
        renpy.music.set_pause(True, channel = "voice5")
        renpy.music.set_pause(True, channel = "voice6")
        renpy.music.set_pause(True, channel = "voice7")
        renpy.music.set_pause(True, channel = "voice8")
        renpy.music.set_pause(True, channel = "voisex2")
        renpy.music.set_pause(True, channel = "voisex3")
        renpy.music.set_pause(True, channel = "voisex4")
        renpy.music.set_pause(True, channel = "voisex5")
        renpy.music.set_pause(True, channel = "voisex6")
        renpy.music.set_pause(True, channel = "voisex7")
        renpy.music.set_pause(True, channel = "voisex8")
        renpy.music.set_pause(True, channel = "freeroam_sound1")
        renpy.music.set_pause(True, channel = "freeroam_sound2")
        renpy.music.set_pause(True, channel = "freeroam_music1")

    def stop_sound_with_delay():
        renpy.music.stop("music" , fadeout = 0.0)
        renpy.music.stop("music2", fadeout = 0.0)
