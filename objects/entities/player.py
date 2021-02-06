import random

from utils import clamp
from .entity import Entity
from scripts import Keyboard
from ..projectiles import Projectile

class Player(Entity):
    def __init__(self, color):
        super().__init__(125, 520, color, 76.5, 54, 99)

        self.key_left = False
        self.key_right = False
        self.key_shoot = False

    def pre_update(self, events):
        key_left = Keyboard.check('key_left', events)
        key_right = Keyboard.check('key_right', events)
        
        self.key_left = key_left and not key_right
        self.key_right = key_right and not key_left
        self.key_shoot = Keyboard.check_pressed('key_shoot', events)

    def update(self, delta_time, scene):
        super().update(delta_time)

        # Move to the left
        if self.key_left:
            # Move the shooter
            self.arc_angle = clamp(self.arc_angle + 0.09 * delta_time, self.min_angle, self.max_angle)

            # Move the gear
            if self.arc_angle < self.max_angle:
                self.polygon_smooth += 0.25 * delta_time
        
        # Move to the right
        elif self.key_right:
            # Move the shooter
            self.arc_angle = clamp(self.arc_angle - 0.09 * delta_time, self.min_angle, self.max_angle)

            # Move the gear
            if self.arc_angle > self.min_angle:
                self.polygon_smooth -= 0.25 * delta_time
        
        # Shoot
        if self.key_shoot and not scene.score and self.cooldown == 0:
            # Reset cooldown
            self.cooldown = self.max_cooldown

            # Instantiate the projectile
            scene.projectiles.add(Projectile(self.x, self.y, self.color, -(self.arc_angle + 13.5), 20))
                
            # Play a shooting sound
            random.choice(self.snd_shoot).play()

class Player1(Entity):
    def __init__(self, color):
        super().__init__(125, 520, color, 76.5, 54, 99)

        self.key_left = False
        self.key_right = False
        self.key_shoot = False
    
    def pre_update(self, events):
        key_left = Keyboard.check('key1_left', events)
        key_right = Keyboard.check('key1_right', events)
        
        self.key_left = key_left and not key_right
        self.key_right = key_right and not key_left
        self.key_shoot = Keyboard.check_pressed('key1_shoot', events)

    def update(self, delta_time, scene):
        super().update(delta_time)

        # Move to the left
        if self.key_left:
            # Move the shooter
            self.arc_angle = clamp(self.arc_angle + 0.09 * delta_time, self.min_angle, self.max_angle)

            # Move the gear
            if self.arc_angle < self.max_angle:
                self.polygon_smooth += 0.25 * delta_time
        
        # Move to the right
        elif self.key_right:
            # Move the shooter
            self.arc_angle = clamp(self.arc_angle - 0.09 * delta_time, self.min_angle, self.max_angle)

            # Move the gear
            if self.arc_angle > self.min_angle:
                self.polygon_smooth -= 0.25 * delta_time
        
        # Shoot
        if self.key_shoot and not scene.score and self.cooldown == 0:
            # Reset cooldown
            self.cooldown = self.max_cooldown

            # Instantiate the projectile
            scene.projectiles.add(Projectile(self.x, self.y, self.color, -(self.arc_angle + 13.5), 20))
                
            # Play a shooting sound
            random.choice(self.snd_shoot).play()

class Player2(Entity):
    def __init__(self, color):
        super().__init__(125, -170, color, 256.5, 234, 279)

        self.key_left = False
        self.key_right = False
        self.key_shoot = False
    
    def pre_update(self, events):
        key_left = Keyboard.check('key2_left', events)
        key_right = Keyboard.check('key2_right', events)
        
        self.key_left = key_left and not key_right
        self.key_right = key_right and not key_left
        self.key_shoot = Keyboard.check_pressed('key2_shoot', events)
    
    def update(self, delta_time, scene):
        super().update(delta_time)

        # Move to the left
        if self.key_left:
            # Move the shooter
            self.arc_angle = clamp(self.arc_angle + 0.09 * delta_time, self.min_angle, self.max_angle)

            # Move the gear
            if self.arc_angle < self.max_angle:
                self.polygon_smooth += 0.25 * delta_time
        
        # Move to the right
        elif self.key_right:
            # Move the shooter
            self.arc_angle = clamp(self.arc_angle - 0.09 * delta_time, self.min_angle, self.max_angle)

            # Move the gear
            if self.arc_angle > self.min_angle:
                self.polygon_smooth -= 0.25 * delta_time
        
        # Shoot
        if self.key_shoot and not scene.score and self.cooldown == 0:
            # Reset cooldown
            self.cooldown = self.max_cooldown

            # Instantiate the projectile
            scene.projectiles.add(Projectile(self.x, self.y, self.color, -(self.arc_angle + 13.5), 20))
                
            # Play a shooting sound
            random.choice(self.snd_shoot).play()