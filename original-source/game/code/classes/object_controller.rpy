init -1 python:
    class ObjectController:
    
        @staticmethod
        def click(object):
            player.log_action(f"Clicked on object '{object.codename}'")
            if EventController.action(OBJECT_CLICK, object.codename):
                return
        
            global interaction_options
            interaction_options = object.get_interaction_options(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position)
            if not interaction_options:
                return
        
            if EventController.action(OBJECT_INTERACTION, object.codename):
                return
        
            global interaction_object
            interaction_object = object
            interaction_options = QuestController.add_object_interactions_override(char, interaction_options)
            player.log_action(f"Entered interaction menu for object '{interaction_object.codename}'")
            renpy.jump("interaction_menu_object")
    
        @staticmethod
        def get_object(codename):
            return indexed_sm_objects_list[codename] if codename in indexed_sm_objects_list else False
    
        @staticmethod
        def get_objects_for_sandbox():
            result = []
            for obj in sm_objects_list:
                if obj.get_lock_status() and obj.has_schedule() and obj.get_schedule_in_location(gt.curr_timeslot, gt.curr_day, curr_location, curr_sublocation, curr_position):
                    result.append(obj)
            return result
