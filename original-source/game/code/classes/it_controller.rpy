init -1 python:
    class ITController:
    
        @staticmethod
        def read_magazine():
            topic = TOPIC_ANIMALS
            EventController.action(USE_ITEM, IT_ANIMAL_MAG)
            if player.get_topic(topic) < 10:
                player.add_topic(topic, 1)
                player.log_action(f"Read 'IT Magazine' and got 1 point for '{topic}'")
            else:
                renpy.notify(_("You already learned everything from this magazine"))
                player.log_action("Maxed learning from 'IT Magazine'")
            renpy.play(audio.sfx_menu_notification1, channel="sound9")
            renpy.jump("location_reenter")
    
        @staticmethod
        def work_it_job():
            renpy.jump("it_job_setup_nonogram")
    
        @staticmethod
        def after_it_job():
            player.consume_energy(4)
            gt.add(8, 0, 0)
            total_days_worked = player.increment_data(DATA_IT_TOTAL_JOB_WORKED_DAYS)
            player.increment_data(DATA_IT_JOB_WORKED_DAYS)
            if player.get_data(DATA_IT_JOB_WORKED_DAYS) == 5:
                player.set_data("Worked_5_days_in_a_week", True)
            EventController.action(IT_JOB_FINISHED, False, False, total_days_worked)
    
        @staticmethod
        def it_job_daily_reward():
            player.increment_data(DATA_IT_JOB_WORKED_SUCCESSFUL_DAYS)
            player.increment_data(DATA_IT_TOTAL_JOB_FINISHED_TIMES)
    
        @staticmethod
        def it_job_weekly_reward(days_worked):
            if days_worked < 1:
                return
            pay_per_day = ITController.get_current_pay_per_day()
            total_earned = pay_per_day * days_worked
            player.add_money(total_earned, _("Orbix Salary ({} days)").format(days_worked))
            player.log_action(f"Earned IT weekly pay of '${total_earned}'")
            player.set_data(DATA_IT_JOB_WORKED_DAYS, 0)
            player.set_data(DATA_IT_JOB_WORKED_SUCCESSFUL_DAYS, 0)
            EventController.action(IT_WEEKLY_MONEY_RECEIVED, total_earned, False, days_worked)
    
        @staticmethod
        def get_current_pay_per_day():
            days_worked = player.get_data(DATA_IT_JOB_WORKED_DAYS)
            it_job_difficulity = player.get_choice("it_job_difficulity")
            max_per_day = it_max_payment_dict.get(it_job_difficulity)
            pay_per_day = max_per_day
            max_days = 5
            if (days_worked < 5):
                pay_per_day = pay_per_day - ((max_days - days_worked) * 10)
            return pay_per_day
    
        @staticmethod
        def take_ns_panty():
            ObjectController.get_object("ns_panty").lock()
            player.log_action("Took 'NS Panty' from 'IT Bathroom'")
            player.set_choice("NS002-took-panty")
            renpy.jump("location_reenter")
