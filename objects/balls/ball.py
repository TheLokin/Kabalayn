import math
import random
import pygame

from ..object import GameObject
from scripts import SoundManager
from ..particles import Dust, Slash, Explosion
from utils import Colors, approach, clamp, polygon_coordinate

class Ball(GameObject):
    def __init__(self, x, y, radius):
        super().__init__()

        self.x = x
        self.y = y
        
        self.hspeed = 0
        self.vspeed = 0
        
        self.radius = radius
        self.min_x = radius
        self.max_x = 250 - radius
        self.min_y = -radius
        self.max_y = 350 + radius

        self.snd_collide = [SoundManager.load_sound('snd_collide' + str(i) + '.wav') for i in range(3, 5)]
        self.snd_score = [SoundManager.load_sound('snd_score' + str(i) + '.wav') for i in range(1, 4)]
        self.snd_explosion = SoundManager.load_sound('snd_explosion.wav')
    
    def pre_update(self, events):
        pass

    def update(self, delta_time, scene):
        # Check if the ball has to be destroyed
        if scene.score:
            # Dust particles
            radius = round(self.radius)
            for _ in range(20):
                x = self.x + random.randint(-radius, radius)
                y = self.y + random.randint(-radius, radius)
                hspeed = random.randint(-3, 3)
                vspeed = random.randint(-3, 3)
                image_speed = random.uniform(0.005, 0.01)
                scene.top_particles.add(Dust(x, y, Colors.LIGHT_WHITE, hspeed, vspeed, image_speed))
            
            # Explosion particles
            scene.top_particles.add(Explosion(self.x, self.y, Colors.LIGHT_WHITE, self.radius, 100))
            
            # Destroy the ball
            self.destroy()
            return
        
        # Reverse ball direction when the projectile collides with the sides
        if self.x == self.min_x or self.x == self.max_x:
            self.hspeed = -self.hspeed
        
        # Reduce speed
        self.hspeed = approach(self.hspeed, 0, 0.00001 * delta_time)
        self.vspeed = approach(self.vspeed, 0, 0.00001 * delta_time)

        # Calculate the new position
        self.x = clamp(self.x + self.hspeed * 0.06 * delta_time, self.min_x, self.max_x)
        self.y = clamp(self.y + self.vspeed * 0.06 * delta_time, self.min_y, self.max_y)

        # Check if the ball is inside the enemy goal
        if self.y == self.min_y:
            # Make the sceen shake
            scene.shake = True
            
            # Update the scene
            scene.score = True

            # Add the score to the player
            scene.player_score += 1

            # Explosion particles
            scene.top_particles.add(Explosion(self.x, self.min_y, Colors.LIGHT_WHITE, self.radius, 225))
            
            # Play the score sound
            random.choice(self.snd_score).play()

            # Play the explosion sound
            self.snd_explosion.play()

            # Destroy ball
            self.destroy()
            return
        
        # Check if the ball is inside the player goal
        elif self.y == self.max_y:
            # Make the sceen shake
            scene.shake = True
            
            # Update the scene
            scene.score = True

            # Add the score to the enemy
            scene.enemy_score += 1

            # Explosion particles
            scene.top_particles.add(Explosion(self.x, self.max_y, Colors.LIGHT_WHITE, self.radius, 225))
            
            # Play the score sound
            random.choice(self.snd_score).play()

            # Play the explosion sound
            self.snd_explosion.play()

            # Destroy ball
            self.destroy()
            return
        
        # Detect collisions between balls
        speed = 0.7 * math.hypot(self.hspeed, self.vspeed)
        for ball in scene.balls:
            # If is the same ball continue
            if ball == self:
                continue
            
            # Calculate distance to the ball
            distance_x = ball.x - self.x
            distance_y = ball.y - self.y
            distance = math.hypot(distance_x, distance_y)

            # Detect if the ball is close enough to another ball
            if distance <= ball.radius + self.radius:
                # Make the sceen shake
                scene.shake = True
                
                # Calculate the direction after collide
                collision_angle = math.atan2(distance_y, distance_x)
                hspeed = -speed * math.cos(collision_angle)
                vspeed = -speed * math.sin(collision_angle)
                
                if hspeed != 0 or vspeed != 0:
                    self.hspeed = hspeed
                    self.vspeed = vspeed
                    ball.hspeed = -hspeed
                    ball.vspeed = -vspeed
                
                # Plan B if the ball is inside another
                else:
                    self.hspeed = 0.5 * (1 + random.random())
                    self.vspeed = 0.5 * (1 + random.random())
                    ball.hspeed = -(0.5 * (1 + random.random()))
                    ball.vspeed = -(0.5 * (1 + random.random()))
                
                # Slash particles
                x, y = polygon_coordinate(self.x, self.y, math.degrees(collision_angle), self.radius)
                for _ in range(random.randint(1, 2)):
                    angle = math.degrees(collision_angle+90) + random.randint(-60, 60)
                    duration = speed * random.randint(30, 60)

                    scene.top_particles.add(Slash(x, y, Colors.LIGHT_WHITE, angle, duration))
                
                for _ in range(random.randint(1, 2)):
                    angle = math.degrees(collision_angle-90) + random.randint(-60, 60)
                    duration = speed * random.randint(30, 60)

                    scene.top_particles.add(Slash(x, y, Colors.LIGHT_WHITE, angle, duration))

                # Play the collision sound
                random.choice(self.snd_collide).play()

    def draw(self, surface):
        # Draw the ball
        pygame.draw.circle(surface, Colors.LIGHT_WHITE, (round(self.x), round(self.y)), round(self.radius))