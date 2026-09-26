init -1 python:
    class THController:
    
        rehearsal_day_1 = TUESDAY
        rehearsal_day_2 = WEDNESDAY
        rehearsal_day_3 = FRIDAY
        final_show_day = SATURDAY
    
        @staticmethod
        def read_magazine():
            topic = TOPIC_FASHION
            EventController.action(USE_ITEM, TH_FASHION_MAG)
            if player.get_topic(topic) < 10:
                player.add_topic(topic, 1)
                player.log_action(f"Read 'TH Magazine' and got 1 point for '{topic}'")
            else:
                renpy.notify(_("You already learned everything from this magazine"))
                player.log_action("Maxed learning from 'TH Magazine'")
            renpy.play(audio.sfx_menu_notification1, channel="sound9")
            renpy.jump("location_reenter")
    
        @staticmethod
        def work_th_job():
            renpy.jump("final_theater_job_setup" if gt.curr_day == THController.final_show_day else "rehearsal_theater_job_setup")
    
        @staticmethod
        def after_th_job():
            player.consume_energy(3)
        
            if gt.curr_day == THController.final_show_day:
                if simon_says_win:
                    player.increment_data(DATA_TH_SHOWS_SUCCESS)
                    player.set_data(DATA_FINISHED_TH_FINAL_SHOW, True)
                    THController.th_after_show_pay()
                else:
                    player.increment_data(DATA_TH_SHOWS_FAILED)
            elif gt.curr_day == THController.rehearsal_day_1:
                player.increment_data(DATA_TH_REHEARSALS_DONE)
                player.set_data(DATA_FINISHED_TH_REHEARSAL_1, True)
            elif gt.curr_day == THController.rehearsal_day_2:
                player.increment_data(DATA_TH_REHEARSALS_DONE)
                player.set_data(DATA_FINISHED_TH_REHEARSAL_2, True)
            elif gt.curr_day == THController.rehearsal_day_3:
                player.increment_data(DATA_TH_REHEARSALS_DONE)
                player.set_data(DATA_FINISHED_TH_REHEARSAL_3, True)
            gt.add(3, 0, 0)
            THController.update_event_controller()
    
        @staticmethod
        def update_event_controller():
            total_rehearsal_done = player.get_data(DATA_TH_REHEARSALS_DONE)
            total_shows_success = player.get_data(DATA_TH_SHOWS_SUCCESS)
            total_shows_failed = player.get_data(DATA_TH_SHOWS_FAILED)
            EventController.action(TH_REHEARSALS_DONE, False, False, total_rehearsal_done)
            EventController.action(TH_SHOWS_SUCCESS, False, False, total_shows_success)
            EventController.action(TH_SHOWS_FAILED, False, False, total_shows_failed)
    
        @staticmethod
        def get_current_pay():
            pay = sum([
                    200 if player.get_data(DATA_FINISHED_TH_FINAL_SHOW) else 0,
                    33 if player.get_data(DATA_FINISHED_TH_REHEARSAL_1) else 0,
                    33 if player.get_data(DATA_FINISHED_TH_REHEARSAL_2) else 0,
                    34 if player.get_data(DATA_FINISHED_TH_REHEARSAL_3) else 0
                    ])
            if THController.get_final_show_missed():
                pay = 0
            return pay
    
        @staticmethod
        def th_after_show_pay():
            th_after_show_pay = THController.get_current_pay()
            player.add_money(th_after_show_pay, _("Theater salary"), _("You earned ${} for working at the Theater").format(th_after_show_pay))
            player.log_action("Earned '$" + str(th_after_show_pay) + "' from TH Job")
            EventController.action(TH_WEEKLY_MONEY_RECIEVED, th_after_show_pay, False, False)
    
        @staticmethod
        def th_reset_progress():
            player.set_data(DATA_FINISHED_TH_FINAL_SHOW, False)
            player.set_data(DATA_FINISHED_TH_REHEARSAL_1, False)
            player.set_data(DATA_FINISHED_TH_REHEARSAL_2, False)
            player.set_data(DATA_FINISHED_TH_REHEARSAL_3, False)
    
        @staticmethod
        def get_rehearsal_1_icon():
            if player.get_data(DATA_FINISHED_TH_REHEARSAL_1):
                return "images/ui/factions/th_faction_check_mark.webp"
            elif gt.curr_timeslot == TIMESLOT_8 and gt.curr_day == THController.rehearsal_day_1 and not player.get_data(DATA_FINISHED_TH_REHEARSAL_1):
                return "images/ui/factions/th_faction_cross_mark.webp"
            elif gt.get_week_day_number(gt.curr_day) > gt.get_week_day_number(THController.rehearsal_day_1) and not player.get_data(DATA_FINISHED_TH_REHEARSAL_1):
                return "images/ui/factions/th_faction_cross_mark.webp"
            else:
                return "images/ui/factions/th_faction_rehearsal.webp"
    
        @staticmethod
        def get_rehearsal_2_icon():
            if player.get_data(DATA_FINISHED_TH_REHEARSAL_2):
                return "images/ui/factions/th_faction_check_mark.webp"
            elif gt.curr_timeslot == TIMESLOT_8 and gt.curr_day == THController.rehearsal_day_2 and not player.get_data(DATA_FINISHED_TH_REHEARSAL_2):
                return "images/ui/factions/th_faction_cross_mark.webp"
            elif gt.get_week_day_number(gt.curr_day) > gt.get_week_day_number(THController.rehearsal_day_2) and not player.get_data(DATA_FINISHED_TH_REHEARSAL_2):
                return "images/ui/factions/th_faction_cross_mark.webp"
            else:
                return "images/ui/factions/th_faction_rehearsal.webp"
    
        @staticmethod
        def get_rehearsal_3_icon():
            if player.get_data(DATA_FINISHED_TH_REHEARSAL_3):
                return "images/ui/factions/th_faction_check_mark.webp"
            elif gt.curr_timeslot == TIMESLOT_8 and gt.curr_day == THController.rehearsal_day_3 and not player.get_data(DATA_FINISHED_TH_REHEARSAL_3):
                return "images/ui/factions/th_faction_cross_mark.webp"
            elif gt.get_week_day_number(gt.curr_day) > gt.get_week_day_number(THController.rehearsal_day_3) and not player.get_data(DATA_FINISHED_TH_REHEARSAL_3):
                return "images/ui/factions/th_faction_cross_mark.webp"
            else:
                return "images/ui/factions/th_faction_rehearsal.webp"
    
        @staticmethod
        def get_final_show_icon():
            if player.get_data(DATA_FINISHED_TH_FINAL_SHOW):
                return "images/ui/factions/th_faction_check_mark.webp"
            elif gt.curr_timeslot == TIMESLOT_8 and gt.curr_day == THController.final_show_day and not player.get_data(DATA_FINISHED_TH_FINAL_SHOW):
                return "images/ui/factions/th_faction_cross_mark.webp"
            elif gt.get_week_day_number(gt.curr_day) > gt.get_week_day_number(THController.final_show_day) and not player.get_data(DATA_FINISHED_TH_FINAL_SHOW):
                return "images/ui/factions/th_faction_cross_mark.webp"
            else:
                return "images/ui/factions/th_faction_final_show.webp"
    
        @staticmethod
        def get_final_show_missed():
            if player.get_data(DATA_FINISHED_TH_REHEARSAL_3):
                return False
            if gt.curr_timeslot == TIMESLOT_8 and gt.curr_day == THController.rehearsal_day_3 and not player.get_data(DATA_FINISHED_TH_REHEARSAL_3):
                return True
            elif gt.get_week_day_number(gt.curr_day) > gt.get_week_day_number(THController.final_show_day) and not player.get_data(DATA_FINISHED_TH_FINAL_SHOW):
                return True
            return False
