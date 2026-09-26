init python:
    import math
    import random

    class WurstDelivery(object):
        def __init__(self, num, posx, posy, end_location):
            self.num = num
            self.posx = posx
            self.posy = posy
            self.end_location = end_location
        
            self.done = False
            self.distance = 0
            self.travel_time = 0
            self.speed_multiplier = 400
    
        def click_button(self):
            global delivery_time
            global delivery_bar_range
        
            self.distance = WurstDelivery.calculate_distance(self.posx, self.posy, delivery_current_x, delivery_current_y)
            self.travel_time = self.distance / self.speed_multiplier
            setattr(renpy.store, "delivery_time",      self.travel_time)
            setattr(renpy.store, "delivery_bar_range", self.travel_time)
    
        def delivery_done(self):
            global delivery_current_x
            global delivery_current_y
        
            self.done = True
            setattr(renpy.store, "delivery_current_x", self.posx)
            setattr(renpy.store, "delivery_current_y", self.posy - 35)
    
        @staticmethod
        def calculate_distance(x1, y1, x2, y2):
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            distance = math.sqrt(dx**2 + dy**2)
            return distance
    
        @staticmethod
        def is_close_to_points(x, y, points, min_distance=100):
            for p in points:
                distance = WurstDelivery.calculate_distance(x, y, p.posx, p.posy)
                if distance < min_distance:
                    return True
            return False
    
        @staticmethod
        def generate_random_points(start_x, start_y, num_points):
            points = []
            number = 0
            random.seed()
            for _ in range(num_points):
                while True:
                    number += 1
                    x = random.randint(50, 1340)
                    y = random.randint(350, 1020)
                    if WurstDelivery.calculate_distance(start_x, start_y, x, y) > 200:
                        if not WurstDelivery.is_close_to_points(x, y, points):
                            points.append(WurstDelivery(number, x, y, False))
                            break
            points.append(WurstDelivery(number + 1, delivery_start_x, delivery_start_y, True))
            return points
    
        @staticmethod
        def check_delivery_done():
            global delivery_points
            global delivery_clicked_button
        
            for p in delivery_points:
                if p.num == delivery_clicked_button:
                    p.delivery_done()
                    break
            for p in delivery_points:
                if p.end_location is False:
                    if p.done is False:
                        return
            setattr(renpy.store, "delivery_finished", True)
    
        @staticmethod
        def retrurned_to_wd():
            global delivery_points
            global delivery_clicked_button
        
            for p in delivery_points:
                if p.num == delivery_clicked_button:
                    p.delivery_done()
                    break
        
            setattr(renpy.store, "retrurned_to_wd", True)
    
        @staticmethod
        def end_game(mt):
            reward = wurst_delivery_base_reward
            delta = wurst_delivery_average_time - mt.minigame_length
            delta = max(min(delta, wurst_delivery_tip_time_range), - wurst_delivery_tip_time_range)
            reward += round(delta / wurst_delivery_tip_time_range * wurst_delivery_tip)
            player.add_money(reward, _("Wurst Delivery"), _("You earned ${} for working at Wurst Delivery").format(reward))
            StoryController.consume_time_energy(4, 0, WURST_DELIVERY_ENERGY_COST)
            player.log_action("Completed 'Wurst Delivery' and Earned '$" + str(reward) + "'")
            renpy.jump("wurst_delivery_done")
