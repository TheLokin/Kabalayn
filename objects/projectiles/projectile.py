import math
import random
import pygame

from ..object import GameObject
from scripts import SoundManager
from ..particles import Dust, Slash
from utils import Colors, cycle, approach, clamp, polygon_coordinate

class Projectile(GameObject):
    def __init__(self, x, y, color, angle, radius):
        super().__init__()
        
        speed = 200 - radius
        self.x = clamp(x + speed * math.cos(math.radians(angle)), radius, 250 - radius)
        self.y = clamp(y + speed * math.sin(math.radians(angle)), 0, 350)
        self.color = color
        self.angle = angle
        self.radius = radius
        self.max_radius = radius

        self.collide = False
        self.snd_collide = [SoundManager.load_sound('snd_collide' + str(i) + '.wav') for i in range(1, 3)]

    def pre_update(self, events):
        pass

    def update(self, delta_time, scene):
        # Destroy projectile by radius
        if self.radius == 0:
            self.destroy()
            return

        # Calculate the new position
        percentage = self.radius / self.max_radius
        speed = 0.47 * percentage * delta_time
        self.x = clamp(self.x + speed * math.cos(math.radians(self.angle)), self.radius, 250 - self.radius)
        self.y = clamp(self.y + speed * math.sin(math.radians(self.angle)), 0, 350)

        # Reverse projectile direction when the projectile collides with the sides
        if self.x == self.radius or self.x == 250 - self.radius:
            self.angle = cycle(180 - self.angle, -180, 180)

        # Create the trail particles
        x = self.x + random.randint(0, round(self.radius)) - self.radius / 2
        y = self.y + random.randint(0, round(self.radius)) - self.radius / 27
        image_speed = random.uniform(0.005, 0.01)
        
        scene.bottom_particles.add(Dust(x, y, Colors.LIGHT_GREY, 0, 0, image_speed))

        # Detect collisions between projectiles
        for projectile in scene.projectiles:
            # If is a projectile of the same entity continue
            if self.color == projectile.color:
                continue

            # Calculate distance to the projectile
            distance_x = projectile.x - self.x
            distance_y = projectile.y - self.y
            distance = math.hypot(distance_x, distance_y)

            # Detect if the projectile is close enough to another projectile
            if distance <= projectile.radius + self.radius:
                # The projectile with smaller radius is destroyed
                if self.radius < projectile.radius:
                    self.collide = True
                elif projectile.radius < self.radius:
                    projectile.collide = True
                else:
                    self.collide = True
                    projectile.collide = True
                
        # Detect collisions with balls
        for ball in scene.balls:
            # Calculate distance to the ball
            distance_x = ball.x - self.x
            distance_y = ball.y - self.y
            distance = math.hypot(distance_x, distance_y)

            # Detect if the projectile is close enough to a ball
            if distance <= ball.radius + self.radius:
                # How the projectile collided has to be destroyed
                self.collide = True

                # Calculate the direction after collide
                collision_angle = math.atan2(distance_y, distance_x)
                ball.hspeed = (ball.hspeed / 3) + 1.5 * percentage * math.cos(collision_angle)
                ball.vspeed = (ball.vspeed / 3) + 1.5 * percentage * math.sin(collision_angle)

                # Slash particles up
                x, y = polygon_coordinate(self.x, self.y, math.degrees(collision_angle), self.radius)
                for _ in range(random.randint(2, 4)):
                    angle = math.degrees(collision_angle) + random.randint(-60, 60)
                    duration = percentage * random.randint(50, 100)

                    scene.top_particles.add(Slash(x, y, Colors.LIGHT_WHITE, angle, duration))

                # Slash particles down
                for _ in range(random.randint(1, 2)):
                    angle = math.degrees(-collision_angle) + random.randint(-60, 60)
                    duration = percentage * random.randint(30, 60)

                    scene.top_particles.add(Slash(x, y, Colors.LIGHT_WHITE, angle, duration))

                # Play the collision sound
                random.choice(self.snd_collide).play()

        # Check if the projectile has collided
        if self.collide:
            # Make the sceen shake
            scene.shake = True

            # Dush particles
            radius = round(self.radius / 2)
            for _ in range(radius):
                x = self.x + random.randint(-radius, radius)
                y = self.y + random.randint(-radius, radius)
                hspeed = 1.5 * math.cos(math.radians(self.angle)) + random.randint(-2, 2)
                vspeed = 1.5 * math.sin(math.radians(self.angle)) + random.randint(-2, 2)
                image_speed = random.uniform(0.005, 0.01)

                scene.top_particles.add(Dust(x, y, self.color, hspeed, vspeed, image_speed))

            # Destroy projectile by collision
            self.destroy()
            return
        
        # Reduce projectile radius
        self.radius = approach(self.radius, 0, 0.015 * delta_time)

    def draw(self, surface):
        # Draw the projectile
        pygame.draw.circle(surface, self.color, (round(self.x), round(self.y)), round(self.radius + 1))