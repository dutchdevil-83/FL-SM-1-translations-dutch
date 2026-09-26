init 1 python:
    if not "is_special" in persistent.__dict__:
        persistent.__setattr__("is_special", is_steam_edition)



    renpy.music.register_channel("music2", "music")
    renpy.music.register_channel("music3", "music")
    renpy.music.register_channel("music4", "music")
    renpy.music.register_channel("sound2", "sfx")
    renpy.music.register_channel("sound3", "sfx")
    renpy.music.register_channel("sound4", "sfx")
    renpy.music.register_channel("sound5", "sfx")
    renpy.music.register_channel("sound9", "sfx")
    renpy.music.register_channel("sound10", "sfx")
    renpy.music.register_channel("voice2", "voice")
    renpy.music.register_channel("voice3", "voice")
    renpy.music.register_channel("voice4", "voice")
    renpy.music.register_channel("voice5", "voice")
    renpy.music.register_channel("voice6", "voice")
    renpy.music.register_channel("voice7", "voice")
    renpy.music.register_channel("voice8", "voice")
    renpy.music.register_channel("voisex", "voisex", False)
    renpy.music.register_channel("voisex2", "voisex")
    renpy.music.register_channel("voisex3", "voisex")
    renpy.music.register_channel("voisex4", "voisex")
    renpy.music.register_channel("voisex5", "voisex")
    renpy.music.register_channel("voisex6", "voisex")
    renpy.music.register_channel("voisex7", "voisex")
    renpy.music.register_channel("voisex8", "voisex")

    renpy.music.register_channel("freeroam_sound1", "sfx")
    renpy.music.register_channel("freeroam_sound2", "sfx")
    renpy.music.register_channel("freeroam_music1", "music")



    config.label_callbacks.append(current_label_callback)



    mcname = _("Mike")

    def is_dev_env():
        if renpy.loadable("code/debug/dev_screens.rpy"):
            return True
        return False

    is_dev_environment = is_dev_env()

    if is_dev_environment is True:
        config.keymap["fast_skip"].append("noshift_K_q")
