import math
import random

from .entity import Entity
from ..projectiles import Projectile
from utils import clamp, approach, cycle

class Enemy(Entity):
    def __init__(self, color, shoot_delay):
        super().__init__(125, -170, color, 256.5, 234, 279)
    
        self.angle_offset = 0
        self.min_shoot_delay = shoot_delay[0]
        self.max_shoot_delay = shoot_delay[1]
        self.shoot_delay = random.randint(self.min_shoot_delay, self.max_shoot_delay)

    def pre_update(self, events):
        pass
    
    def update(self, delta_time, scene):
        super().update(delta_time)

        # Find the nearest ball
        nearest_ball = None
        for ball in scene.balls:
            if nearest_ball is None:
                nearest_ball = ball
            elif ball.y < nearest_ball.y:
                nearest_ball = ball

        # Check if a ball was found
        if nearest_ball is not None:
            # Calculate distance to the ball
            distance_x = nearest_ball.x - self.x
            distance_y = nearest_ball.y - self.y
            angle = -math.degrees(math.atan2(distance_y, distance_x)) + self.angle_offset - 13.5

            # Calculate target angle
            speed = 0.025 * delta_time
            diff = cycle(angle - self.arc_angle, -180, 180)
            target_angle = diff if abs(diff) < speed else diff / abs(diff) * speed

            # Move the shooter
            self.arc_angle = clamp(self.arc_angle + target_angle, self.min_angle, self.max_angle)

            # Move the gear
            if self.min_angle < self.arc_angle < self.max_angle:
                self.polygon_smooth += target_angle * 0.1 * delta_time

        # Reduce shoot delay
        self.shoot_delay = approach(self.shoot_delay, 0, 0.06 * delta_time)

        # Shoot
        if self.shoot_delay == 0 and not scene.score and self.cooldown == 0:            
            # Reset cooldown
            self.cooldown = self.max_cooldown

            # Calculate new shoot delay
            self.shoot_delay = random.randint(self.min_shoot_delay, self.max_shoot_delay)

            # Calculate new angle offset
            self.angle_offset = random.randint(-5, 5)

            # Instantiate the projectile
            scene.projectiles.add(Projectile(self.x, self.y, self.color, -(self.arc_angle + 13.5), 20))
                
            # Play a shooting sound
            random.choice(self.snd_shoot).play()