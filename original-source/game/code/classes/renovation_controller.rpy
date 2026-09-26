init python:
    class RenovationController:
        def __init__(self):
            self.progress_var = "renovation_progress_percent"
            self.daily_limit = None
            self.renovation_scenes_progress = 10
            self.work_upgrade_price_steps = {
                    "mc": [50, 100, 200, 300],
                    "sy": [100, 150],
                }
        
            self.work_power_steps = {
                    "mc": [0.1, 0.25, 0.5, 1.0, 1.5],
                    "sy": [1.0, 2.0, 3.0]
                }
            self.work_power_step_vars = {
                    "mc": "renovation_mc_work_power_step",
                    "sy": "renovation_sy_work_power_step"
                }
        
            self.left_chars = [{NAME: "ns", SCENE: "sm1cs_ns_renovation"}, {NAME: "tl", SCENE: "sm1cs_tl_renovation"}, {NAME: "kv", SCENE: "sm1cs_kv_renovation"}]
            self.right_chars = [{NAME: "am", SCENE: "sm1cs_am_renovation"}, {NAME: "vs", SCENE: "sm1cs_vs_renovation"}, {NAME: "dc", SCENE: "sm1cs_dc_renovation"}]
        
            self.set_vars()
    
        def set_vars(self):
            if not hasattr(renpy.store, self.progress_var):
                setattr(renpy.store, self.progress_var, 0)
            for character in self.work_power_step_vars:
                if not hasattr(renpy.store, self.work_power_step_vars[character]):
                    setattr(renpy.store, self.work_power_step_vars[character], 0)
    
        def get_progress(self):
            return getattr(renpy.store, self.progress_var)
    
        def set_progress(self, add_progress):
            total_progress = self.get_progress() + add_progress
            setattr(renpy.store, self.progress_var, total_progress)
            player.set_choice("sm1ms_renovation_progress", total_progress)
            if self.get_progress() >= 100:
                if not vn_mode:
                    renpy.notify(_("You have completed renovating the studio"))
                player.set_choice("sm1ms_renovation_completed")
            else:
                if not vn_mode:
                    notify_progress = f"{add_progress:.1f}"
                    renpy.notify(_("Renovation progress increased by {progress}%").format(progress=notify_progress))
            EventController.action(RENOVATION_PROGRESSED, total_progress)
    
        def renovation_work(self):
            used_energy = player.energy
            progress_work = self.get_work_power()
            if self.get_progress() + progress_work > 100:
                used_energy = round((100 - self.get_progress()) / self.get_work_power("mc"))
            if not player.has_played_scene("sm1ms016") and self.get_progress() + progress_work >= 50:
                progress_work = 50 - self.get_progress()
                used_energy = round(progress_work / self.get_work_power("mc"))
            if self.get_progress() < 50:
                renpy.call_in_new_context("studio_renovation_work_stage_1")
            else:
                renpy.call_in_new_context("studio_renovation_work_stage_2")
            self.set_progress(progress_work)
            self.set_daily_limit()
            player.consume_energy(used_energy)
            gt.add(2, 0, 0)
    
        def sy_renovation_work(self):
            if int(self.get_progress()) >= 50 and not player.has_played_scene("sm1ms016"):
                return
            if player.get_choice("sm1ms_renovation_started") and not player.get_choice("sm1ms_renovation_completed"):
                self.set_progress(self.get_work_power("sy"))
    
        def is_renovation_work_restricted(self):
            if self.get_renovation_daily_limit():
                return True
            if gt.curr_timeslot not in INTERACTIONS_CHARACTER_CATALOGUE["io-RENO"][TIMESLOTS]:
                return True
            if player.energy <= 0:
                return True
            if curr_location != STUDIO:
                return True
            if self.get_progress() >= 100:
                return True
            if int(self.get_progress()) >= 50 and not player.has_played_scene("sm1ms016"):
                return True
            return False
    
        def renovation_button_tooltip(self):
            if self.get_progress() >= 100:
                return _("Renovation complete")
            if not player.has_played_scene("sm1ms015") and not player.has_played_scene("sm1ms018") and int(self.get_progress()) >= 50:
                return _("Visit one of your job location with Stacy and Melony first")
            if not player.has_played_scene("sm1ms016") and int(self.get_progress()) >= 50:
                return _("Talk with Stacy to install the stairs")
            if self.get_renovation_daily_limit():
                return _("Done today")
            if player.energy <= 0:
                return _("No energy")
            if gt.curr_timeslot not in INTERACTIONS_CHARACTER_CATALOGUE["io-RENO"][TIMESLOTS]:
                wrong_time_msg = gt.get_wrong_time_msg(INTERACTIONS_CHARACTER_CATALOGUE["io-RENO"][TIMESLOTS])
                return f"{wrong_time_msg}"
            if curr_location != STUDIO:
                return _("You need to be at the Studio to work on renovation")
            return _("Work on renovation")
    
        def get_renovation_daily_limit(self):
            if self.daily_limit != gt.get_day_number():
                return False
            return True
    
        def set_daily_limit(self):
            self.daily_limit = gt.get_day_number()
    
        def get_work_power_step(self, character):
            return getattr(renpy.store, self.work_power_step_vars[character])
    
        def get_work_power(self, character=None):
            if character:
                return self.work_power_steps[character][self.get_work_power_step(character)]
            return (self.get_work_power("mc") * player.energy)
    
        def work_upgradeable(self, character):
            if self.get_progress() >= 100:
                return False
            if self.get_work_power_step(character) < len(self.work_power_steps[character]) - 1 and player.money >= self.get_upgrade_price(character):
                return True
            return False
    
        def upgrade_work(self, character):
            if self.work_upgradeable(character):
                player.spend_money(self.get_upgrade_price(character), _("Renovation upgrade"))
                setattr(renpy.store, self.work_power_step_vars[character], self.get_work_power_step(character) + 1)
    
        def get_upgrade_price(self, character):
            return self.work_upgrade_price_steps[character][self.get_work_power_step(character)]
    
        def upgrade_button_name(self, character):
            if self.get_work_power_step(character) == len(self.work_power_steps[character]) - 1:
                return "    " + _("Max")
            return f"Upgrade\n${self.get_upgrade_price(character)}"
    
        def upgrade_button_tooltip(self, character):
            if self.get_progress() >= 100:
                return _("Renovation complete")
            if self.get_work_power_step(character) == len(self.work_power_steps[character]) - 1 or self.work_upgradeable(character):
                return None
            if player.money < self.get_upgrade_price(character):
                return _("Insufficient money")
    
        @staticmethod
        def get_ms_scenes_and_pos():
            if player.get_choice("io_MS018_first"):
                return [("sm1ms014", 47), ("sm1ms018", 483), ("sm1ms016", 910), ("sm1ms015", 1348), ("sm1ms019", 1774)]
            return [("sm1ms014", 47), ("sm1ms015", 483), ("sm1ms016", 910), ("sm1ms018", 1348), ("sm1ms019", 1774)]
    
        @staticmethod
        def get_ms_scene_image(scene_name):
            if not player.has_played_scene("sm1ms015") and not player.has_played_scene("sm1ms018") and scene_name in ["sm1ms015", "sm1ms018"]:
                return f"images/ui/renovation/scenes/no_scene.webp"
            if player.has_played_scene(scene_name):
                return f"images/ui/renovation/scenes/{scene_name}.webp"
            return f"images/ui/renovation/scenes/{scene_name}_bw.webp"
    
        @staticmethod
        def get_char_scene_image(char):
            if player.has_played_scene(char[SCENE]):
                return f"images/ui/renovation/scenes/renovation_char_scene_{char[NAME]}.webp"
            return f"images/ui/renovation/scenes/renovation_char_scene_{char[NAME]}_bw.webp"
    
        def get_char_tooltip(self, char, side):
            if self.get_progress() >= 100:
                return _("Renovation complete")
            if player.has_played_scene(char[SCENE]):
                return _("Already done.")
            before_after = "before 50%" if side == "left" else "after 50%"
            character_name = CharacterController.get_character(char[NAME]).name
            if side == "left" and self.get_progress() >= 50:
                return _(f"Renovation progress is over 50%.\nYou can no longer receive help from {character_name}.")
            if self.get_progress() < 100:
                return _(f"{character_name} can assist with the renovation {before_after} completion.\nTalk to {character_name} to proceed.")
    
        def get_renovation_scenes_progress(self):
            return self.renovation_scenes_progress
