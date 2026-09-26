label jump_to_release_1_end:
    $ config_storyline_mode = False
    $ _preferences.show_empty_window = False
    call screen difficulty_choice("r1_enter_name") with fade
    jump r1_enter_name
label r1_enter_name:
    python:
        mcname = renpy.input(_("Please enter your name. (Default - Mike)"), default = __("")).strip().title()
        if not mcname:
            mcname = __("Mike")

    jump r1_ms_unlocks
label r1_ms_unlocks:
    $ player.create_storyline(MS)
    $ player.progress_storyline(MS, 17)
    call sm1ms001_unlocks from _call_sm1ms001_unlocks
    call sm1ms002_unlocks from _call_sm1ms002_unlocks
    $ event_q_ms002_3_unlocks()
    call sm1ms003_unlocks from _call_sm1ms003_unlocks
    $ event_ms003_0_unlocks()
    $ event_q_ms002_4_unlocks()
    jump r1_it_unlocks
label r1_it_unlocks:
    $ player.create_storyline(IT_STORY_LINE)
    $ player.progress_storyline(IT_STORY_LINE, 8)
    call sm1fs_i001_unlocks from _call_sm1fs_i001_unlocks
    call sm1fs_i002_unlocks from _call_sm1fs_i002_unlocks
    call sm1fs_i003_unlocks from _call_sm1fs_i003_unlocks
    jump call_scene_sm1ms011
label call_scene_sm1ms011:
    call sm1ms011 from _call_sm1ms011
    jump lst_1_overview