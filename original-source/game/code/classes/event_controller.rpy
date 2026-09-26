init -1 python:
    class EventController:
    
        @staticmethod
        def action(type, target=False, value=False, total=False):
            action_data = {"type": type}
            if target:
                action_data[TARGET] = target
            if value:
                action_data[VALUE] = value
            if total:
                action_data[TOTAL] = total
        
            if type == ENTER_LOCATION:
                action_data[LOCATION] = curr_location
                action_data[SUBLOCATION] = curr_sublocation
                action_data[POSITION] = curr_position
            if type in [MONEY_SPENT, MONEY_RECEIVED]:
                action_data[VALUE] = target
        
            quest_pool = QuestController.get_quest_pool()
        
            for quest_name in quest_pool:
                event_function_name = sm_quest_list[quest_name].get(EVENT)
                if event_function_name and QuestController.get_offramp(quest_name) == False:
                    event_function = globals().get(event_function_name)
                    if event_function and event_function(action_data):
                        EventController.resolve_event(quest_name)
                        return True
            return False
    
        @staticmethod
        def resolve_event(quest_name):
            player.log_action(f"Resolved event '{quest_name}'")
            QuestController.resolve_quest(quest_name)
