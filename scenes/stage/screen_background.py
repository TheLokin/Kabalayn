import random
import pygame

from objects import Group, Ball
from scripts import SpriteManager
from pygame.locals import BLEND_MULT
from utils import Colors, swap_color, clip

class ScreenBackground(object):
    def __init__(self, entities, balls=[]):
        # Calculate sprite corners
        spr_corner = SpriteManager.load_sprite('spr_corner.png')

        width = spr_corner.get_width()
        height = spr_corner.get_height()
        
        spr_corner_top_left = swap_color(spr_corner, Colors.WHITE, Colors.GREY)
        spr_corner_top_right = pygame.transform.flip(spr_corner_top_left, True, False)
        spr_corner_bottom_left = pygame.transform.flip(spr_corner_top_left, False, True)
        spr_corner_bottom_right = pygame.transform.flip(spr_corner_top_right, False, True)
        
        # Generate sprite panel
        self.spr_panel = pygame.Surface((width * 2, height * 2))
        self.spr_panel.fill(Colors.BLACK)
        self.spr_panel.blit(spr_corner_top_left, (0, 0))
        self.spr_panel.blit(spr_corner_top_right, (width, 0))
        self.spr_panel.blit(spr_corner_bottom_left, (0, height))
        self.spr_panel.blit(spr_corner_bottom_right, (width, height))
        self.spr_panel.set_colorkey(Colors.BLACK)

        # Surface for objects that are going to have a shadow
        self.display = pygame.Surface((250, 350))

        # Entities group
        self.entities = Group(entities)

        # Projectiles group
        self.projectiles = Group()

        # Balls group
        self.balls = Group()
        for x, y, radius in balls:
            self.balls.add(Ball(x, y, radius))

        # Particles groups
        self.top_particles = Group()
        self.bottom_particles = Group()
    
    def screen_shake(self, screen):
        # Screen shake
        shake = random.randint(-6, 6)
        width = 500 + shake
        height = 700 + shake
        screen.blit(pygame.transform.scale(screen, (width, height)), (-shake, -shake))

        # Screen distortion
        for _ in range(random.randint(5, 25)):
            x = random.randint(0, 500)
            y = random.randint(0, 700)
            width = random.randint(20, 200)
            height = random.randint(5, 25)
            surface = clip(screen, x, y, width, height)
            screen.blit(surface, (x + random.randint(-20, 20), y + random.randint(-20, 20)))

    def screen_distorsion(self, screen):
        # Screen shake
        shake = random.randint(-6, 6)
        width = 500 + shake
        height = 700 + shake
        screen.blit(pygame.transform.scale(screen, (width, height)), (-shake, -shake))

        # Screen distortion
        for _ in range(random.randint(5, 25)):
            x = random.randint(0, 500)
            y = random.randint(0, 700)
            width = random.randint(20, 200)
            height = random.randint(5, 25)
            surface = clip(screen, x - width, y - height, width, height)
            screen.blit(surface, (x + random.randint(-20, 20), y + random.randint(-20, 20)))

    def draw(self, screen):
        # Screen background color
        screen.fill(Colors.BLACK)
         
        # Display background color
        self.display.fill(Colors.BLACK)

        # Draw the entities
        entities_display = self.display.copy()
        self.entities.draw(entities_display)

        # Draw the bottom particles
        bottom_particles_display = self.display.copy()
        self.bottom_particles.draw(bottom_particles_display)

        # Draw the projectiles
        projectiles_display = self.display.copy()
        self.projectiles.draw(projectiles_display)

        # Draw the balls
        balls_display = self.display.copy()
        self.balls.draw(balls_display)

        # Draw the top particles
        top_particles_display = self.display.copy()
        self.top_particles.draw(top_particles_display)

        # Draw the shadow
        display = self.display.copy()
        display.fill(Colors.DARK_GREY)
        display.blits((
            (entities_display, (0, 0)),
            (top_particles_display, (0, 0)),
            (balls_display, (0, 0)),
            (projectiles_display, (0, 0)),
            (bottom_particles_display, (0, 0))
        ))
        
        shadow = self.display.copy()
        shadow.fill(Colors.LIGHT_GREY)
        shadow.blit(display, (0, 0), special_flags=BLEND_MULT)
        screen.blit(pygame.transform.scale(shadow, (450, 650)), (24, 24))

        # Draw the panel
        screen.blit(self.spr_panel, (0, 0))
        
        # Draw the display
        self.display.blits((
            (bottom_particles_display, (0, 0)),
            (projectiles_display, (0, 0)),
            (balls_display, (0, 0)),
            (top_particles_display, (0, 0)),
            (entities_display, (0, 0))
        ))
        self.display.set_colorkey(Colors.BLACK)
        
        screen.blit(pygame.transform.scale(self.display, (500, 700)), (0, 0))