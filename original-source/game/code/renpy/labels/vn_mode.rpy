label vn_mode_start:
    $ vn_mode = True
    $ only_story_mode = True
    call create_first_storyline from _call_create_first_storyline_1
    jump vn_mode_menu
label switch_to_vn_mode:
    scene black
    show screen info_text(_("You will switch to VN Mode now\nYour progress will be carried over\n\nThis is not recomended and doing this can introduce bugs and glitches"))
    with Fade(0.5, 0.5, 0.5)
    pause
    hide screen info_text
    show screen info_text(_("Once you switch, you cannot roll back\n\nYou can still load your old save to continue playing normally"))
    with Fade(0.2, 0.2, 0.2)
    pause
    hide screen info_text
    show screen info_text(_("It's recomended to start a new game in VN Mode\n\nPlease procced at your own risk"))
    with Fade(0.2, 0.2, 0.2)
    pause
    hide screen info_text
    $ vn_mode = True
    $ only_story_mode = True
    $ renpy.block_rollback()
    jump vn_mode_menu
label vn_mode_menu:
    scene black
    $ phone_button = True
    if StoryController.is_all_storylines_finished():
        show screen info_text(_("You have finished all the content avialable in this release"))
        with Fade(0.5, 0.5, 0.5)
        pause
        hide screen info_text
        show screen info_text(_("Please save your game so you can resume playing from here in the next release"))
        with Fade(0.2, 0.2, 0.2)
        pause
        hide screen info_text
    $ renpy.force_autosave(True, True)
    $ VNModeController.auto_progress_all_quests()
    call screen vn_mode_map()
    return
label vn_mode_control(storyline_name, scene_without_storyline=False):
    $ phone_button = False
    $ scene_transition_text = VNModeController.get_scene_transition_text(storyline_name, scene_without_storyline)
    if scene_transition_text:
        scene black
        show screen scene_transistion(scene_transition_text)
        with Fade(0.5, 0.5, 0.5)
        pause
        hide screen scene_transistion
    if scene_without_storyline:
        jump vn_scene_without_storyline
    $ next_scene = VNModeController.get_next_scene(storyline_name)
    if next_scene.startswith("Q"):
        jump vn_mode_chat
    $ progress = player.get_storylines_progress()[storyline_name]
    $ quest = sm_quest_lines_list[storyline_name][QUEST_LINE][progress]
    $ VNModeController.resolve_quest_for_scene(storyline_name, quest)
    $ VNModeController.auto_resolve_quests(storyline_name)
    $ renpy.pop_call()
    jump vn_mode_menu
label vn_mode_offramp_scene(quest_name):
    $ phone_button = False
    $ VNModeController.set_location_data(quest_name)
    $ scene_transition_text = VNModeController.get_scene_transition_text(quest_name, False, True)
    if scene_transition_text:
        scene black
        show screen scene_transistion(scene_transition_text)
        with Fade(0.5, 0.5, 0.5)
        pause
        hide screen scene_transistion
    $ offramp_label = VNModeController.get_offramp_label(quest_name)
    call expression offramp_label from _call_expression_2
    $ renpy.pop_call()
    $ phone_button = True
    jump vn_mode_menu
label vn_scene_without_storyline:
    call expression storyline_name[NAME] from _call_expression_1
    $ renpy.pop_call()
    jump vn_mode_menu
label vn_mode_chat:
    $ next_chat = VNModeController.get_next_chat_data(next_scene)
    $ VNModeController.set_location_data(next_scene)
    $ LocationController.draw_current_location()
    $ renpy.pop_call()
    call screen phone_chat(next(iter(next_chat))) with dissolve
    jump vn_mode_menu