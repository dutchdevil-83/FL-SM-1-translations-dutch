init python:
    import random

    class SimonSays(object):
        def __init__(self, number):
            self.number = number
    
        def get_button_image(self):
            button_image = "images/minigames/simon_says/buttons/" + ss_buttons_set + "/ss_button_" + str(self.number) + "_%s.webp"
            return button_image
    
        def get_button_audio(self):
            audio = "audio/ui/simonsays/sfx_simonsays_" + ss_buttons_set + "_" + str(self.number) + ".ogg"
            return audio
    
        def button_action(self):
            global ss_input_hint
            if len(ss_input_list) < ss_pattern_length:
                if ss_rehearsal_mode is False:
                    ss_input_list.append(self)
                    renpy.play(self.get_button_audio(), "sound3")
                elif self == ss_pattern_list[len(ss_input_list)]:
                    ss_input_list.append(self)
                    renpy.play(self.get_button_audio(), "sound3")
                else:
                    renpy.play(audio.sfx_simonsays_error, "sound3")
                    ss_input_hint = True
    
        def get_idle_image(self):
            button_image = "images/minigames/simon_says/buttons/" + ss_buttons_set + "/ss_button_" + str(self.number) + "_idle.webp"
            return button_image
    
        def get_insensitive_image(self):
            button_image = "images/minigames/simon_says/buttons/" + ss_buttons_set + "/ss_button_" + str(self.number) + "_insensitive.webp"
            return button_image
    
        def get_adaptive_image(self, idx):
            if idx in [2, 5, 8]:
                image_type = "idle"
            elif idx in [0, 1] and not player.get_data(DATA_FINISHED_TH_REHEARSAL_1):
                image_type = "idle"
            elif idx in [3, 4] and not player.get_data(DATA_FINISHED_TH_REHEARSAL_2):
                image_type = "idle"
            elif idx in [6, 7] and not player.get_data(DATA_FINISHED_TH_REHEARSAL_3):
                image_type = "idle"
            else:
                image_type = "insensitive"
            button_image = "images/minigames/simon_says/buttons/" + ss_buttons_set + "/ss_button_" + str(self.number) + "_" + image_type + ".webp"
            return button_image
    
        @staticmethod
        def get_nxt_btn_img():
            next_button = ss_pattern_list[len(ss_input_list)]
            button_image = "images/minigames/simon_says/buttons/" + ss_buttons_set + "/ss_button_" + str(next_button.number) + "_%s.webp"
            return button_image
    
        @staticmethod
        def nxt_btn_action():
            global ss_input_hint
            next_button = ss_pattern_list[len(ss_input_list)]
            ss_input_list.append(next_button)
            renpy.play(next_button.get_button_audio(), "sound3")
            ss_input_hint = False
    
        @staticmethod
        def get_next_button_action():
            next_button = ss_pattern_list[len(ss_input_list)]
            button_image = "images/minigames/simon_says/buttons/" + ss_buttons_set + "/ss_button_" + str(next_button.number) + "_%s.webp"
            return button_image
    
        @staticmethod
        def generate_buttons():
            buttons_list = []
            number = 0
            for i in range(ss_buttons_count):
                number += 1
                buttons_list.append(SimonSays(number))
            return buttons_list
    
        @staticmethod
        def generate_pattern():
            global ss_pattern_list
            global ss_pattern_list_for_hint
            global ss_pattern_list_for_anim
            random.seed(gt.get_weekly_random_seed)
            ss_pattern_list = random.choices(ss_buttons_list, k = ss_pattern_length)
            ss_pattern_list_for_anim = ss_pattern_list.copy()
            if ss_rehearsal_mode is True:
                ss_pattern_list_for_hint = []
                for i in range(ss_pattern_length):
                    ss_pattern_list_for_hint.append(SimonSays(0))
            else:
                ss_pattern_list_for_hint = ss_pattern_list.copy()
                ss_pattern_list_for_hint[2] = SimonSays(0)
                ss_pattern_list_for_hint[5] = SimonSays(0)
                ss_pattern_list_for_hint[8] = SimonSays(0)
                if not player.get_data(DATA_FINISHED_TH_REHEARSAL_1):
                    ss_pattern_list_for_hint[0] = SimonSays(0)
                    ss_pattern_list_for_hint[1] = SimonSays(0)
                if not player.get_data(DATA_FINISHED_TH_REHEARSAL_2):
                    ss_pattern_list_for_hint[3] = SimonSays(0)
                    ss_pattern_list_for_hint[4] = SimonSays(0)
                if not player.get_data(DATA_FINISHED_TH_REHEARSAL_3):
                    ss_pattern_list_for_hint[6] = SimonSays(0)
                    ss_pattern_list_for_hint[7] = SimonSays(0)
    
        @staticmethod
        def animate_ss_icon():
            global ss_anim_end
            if len(ss_pattern_list_for_anim) > 0:
                ss_pattern_list_for_anim.pop(0)
                if len(ss_pattern_list_for_anim) == 0:
                    ss_anim_end = True
    
        @staticmethod
        def reset_input():
            ss_input_list.clear()
    
        @staticmethod
        def check_input():
            wrong_clicks = 0
            if len(ss_pattern_list) == len(ss_input_list):
                wrong_clicks = sum(1 for pattern, input in zip(ss_pattern_list, ss_input_list) if input.number != pattern.number)
            return wrong_clicks
    
        @staticmethod
        def get_hint_btn_pos():
            button_width = 166
            button_height = 166
            grid_spacing = 0
            columns = 4
        
            index_of_next_button = ss_buttons_list.index(ss_pattern_list[len(ss_input_list)])
            row_index = index_of_next_button // columns
            col_index = index_of_next_button % columns
        
            x_position = col_index * (button_width + grid_spacing) + button_width / 2
            y_position = row_index * (button_height + grid_spacing) + button_height / 2
        
            return x_position, y_position
    
        @staticmethod
        def shuffle_with_seed(lst):
            seed = random.Random(gt.get_weekly_random_seed)
            shuffled_list = lst[:]
            seed.shuffle(shuffled_list)
            return shuffled_list
