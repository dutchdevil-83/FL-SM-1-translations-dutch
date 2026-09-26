screen flashback_screen(dream=False, fadeout=False):
    if dream is False:
        if fade is False:
            add "memory-overlay"
        else:
            add "memory-overlay" at memory_cloud_fade
    else:
        if fade is False:
            add "dream-overlay"
        else:
            add "dream-overlay" at memory_cloud_fade
transform memory_cloud_fade:
    alpha 1.0
    linear 60.0 alpha 0.2