init python:
    class PirateMovieController:
        def __init__(self):
            self.total_costume_budget = 200
            self.total_actress_budget = 300
            self.total_props_budget = 250
            self.total_props_energy = 20
            self.total_travel_budget = 200
            self.total_editing_energy = 20
        
            self.add_money_value = 50
            self.add_energy_value = 2
            self.add_energy_limit = 8
        
            self.budget_energy_list = ["costume_budget", "actress_budget", "props_budget", "props_energy", "travel_budget", "editing_energy"]
        
            self.daily_limit = None
        
            self.main_scenes_list = ["sm1mv01s05", "sm1mv01s06", "sm1mv01s08", "sm1mv01s09"]
            self.extra_scenes_list = ["sm1mv01s02", "sm1mv01s03_2", "sm1mv01s04"]
        
            self.sm1mv01s06_animation_done = False
        
            self.set_vars()
    
        def set_vars(self):
            for budget_energy in self.budget_energy_list:
                var_name = f"pirates_movie_curr_{budget_energy}"
                if not hasattr(renpy.store, var_name):
                    setattr(renpy.store, var_name, 0)
    
        def get_curr_budget_energy(self, budget_energy):
            var_name = f"pirates_movie_curr_{budget_energy}"
            return getattr(renpy.store, var_name)
    
        def is_budget_energy_filled(self, budget_energy):
            var_name = f"pirates_movie_curr_{budget_energy}"
            return getattr(renpy.store, var_name) >= getattr(self, f"total_{budget_energy}")
    
        def is_add_button_available(self, budget_energy):
            var_name = f"pirates_movie_curr_{budget_energy}"
            return getattr(renpy.store, var_name) < getattr(self, f"total_{budget_energy}")
    
        def add_budget_energy(self, budget_energy, amount=50):
            var_name = f"pirates_movie_curr_{budget_energy}"
            current_unit = getattr(renpy.store, var_name)
            add_unit = min(amount, getattr(self, f"total_{budget_energy}") - current_unit)
            new_unit = min(current_unit + amount, getattr(self, f"total_{budget_energy}"))
            setattr(renpy.store, var_name, new_unit)
            if budget_energy.endswith("_energy"):
                player.consume_energy(add_unit)
                self.set_daily_limit(amount)
                if budget_energy == "props_energy":
                    renpy.call_in_new_context("pirate_movie_build_props")
                else:
                    renpy.call_in_new_context("pirate_movie_editing_work")
            else:
                player.spend_money(add_unit, _("Pirate Movie"))
            EventController.action(FILL_BUDGET_ENERGY)
    
        def is_add_money_available(self, budget_name):
            if player.money < self.add_money_value:
                return False
            return getattr(renpy.store, f"pirates_movie_curr_{budget_name}") < getattr(self, f"total_{budget_name}")
    
        def get_add_money_tooltip(self, budget_name):
            if getattr(renpy.store, f"pirates_movie_curr_{budget_name}") >= getattr(self, f"total_{budget_name}"):
                return _("You have filled the budget already")
            if player.money < self.add_money_value:
                return _("You don't have enough money")
            else:
                return _("Add ${amount} to {budget_name}").format(amount=self.add_money_value, budget_name=budget_name.replace("_", " ").title())
    
        def is_add_energy_available(self, energy_name):
            if curr_location != STUDIO:
                return False
            if self.is_daily_limit_reached():
                return False
            if player.energy < self.add_energy_value:
                return False
            return getattr(renpy.store, f"pirates_movie_curr_{energy_name}") < getattr(self, f"total_{energy_name}")
    
        def get_add_energy_tooltip(self, energy_name):
            if getattr(renpy.store, f"pirates_movie_curr_{energy_name}") >= getattr(self, f"total_{energy_name}"):
                return _("You have filled the energy bar already")
            if self.is_daily_limit_reached():
                return _("You have reached the daily limit")
            if player.energy < self.add_energy_value:
                return _("You don't have enough energy")
            if curr_location != STUDIO:
                return _("You can only work from the Studio")
            else:
                return _("Add {amount} to {energy_name}").format(amount=self.add_energy_value, energy_name=energy_name.replace("_", " ").title())
    
        def set_daily_limit(self, amount):
            daily_limit = self.daily_limit
            if daily_limit is None:
                daily_limit = [gt.get_day_number(), amount]
            elif daily_limit[0] == gt.get_day_number():
                daily_limit[1] += amount
            else:
                daily_limit = [gt.get_day_number(), amount]
            self.daily_limit = daily_limit
    
        def is_daily_limit_reached(self):
            daily_limit = self.daily_limit
            if daily_limit is None:
                return False
            if daily_limit[0] == gt.get_day_number() and daily_limit[1] >= self.add_energy_limit:
                return True
            return False
    
        def fix_daily_limit(self):
            self.daily_limit = None
    
        def set_sm1mv01s06_animation_done(self, value=True):
            self.sm1mv01s06_animation_done = value
