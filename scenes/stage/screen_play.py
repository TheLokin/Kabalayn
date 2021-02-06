import random

from objects import Ball
from .screen_background import ScreenBackground
from scripts import SoundManager, SpriteFontManager
from utils import approach, halign_left, halign_right, valign_top, valign_bottom

def collide(objects):
    for obj in objects:
        if 105 <= obj.x <= 145 and 155 <= obj.y <= 195:
            return True
    
    return False

class ScreenPlay(ScreenBackground):
    def __init__(self, entities, balls, max_balls):
        super().__init__(entities, balls)

        # Screen shake
        self.shake = False
        self.shake_duration = 6
        self.shake_time = self.shake_duration

        # Score
        self.score = False
        self.player_score = 0
        self.enemy_score = 0

        # Balls
        self.stage_balls = balls
        self.ball_delay = 300
        self.ball_time = self.ball_delay
        self.max_balls = max_balls
        self.snd_ball = [SoundManager.load_sound('snd_ball' + str(i) + '.wav') for i in range(1, 4)]
    
    def pre_update(self, events):
        # Pre uptade the entities
        self.entities.pre_update(events)
    
    def check_score(self):
        raise NotImplementedError('call to abstract method ' + repr(self.check_score))

    def update(self, delta_time, scene):
        # Update the entities
        self.entities.update(delta_time, self)

        # Update the projectiles
        self.projectiles.update(delta_time, self)

        # Update the balls
        self.balls.update(delta_time, self)

        # Update the top particles
        self.top_particles.update(delta_time)

        # Update the bottom particles
        self.bottom_particles.update(delta_time)

        # Check if an entity has score
        if self.score:
            # Wait until all the balls have been removed to reset the scene
            if len(self.top_particles) == 0 and len(self.balls) == 0:
                # Check if the stage has ended
                self.check_score(scene)

                # Reset score
                self.score = False

                # Reset the time for the next ball
                self.ball_time = self.ball_delay

                # Add the balls with which the stage began
                for x, y, radius in self.stage_balls:
                    self.balls.add(Ball(x, y, radius))
        
        else:
            # Check if the screen have to shake
            if self.shake:
                # Stop screen shake
                if self.shake_time == 0:
                    self.shake = False
                    self.shake_time = self.shake_duration
                
                # Reduce time left
                else:
                    self.shake_time = approach(self.shake_time, 0, 0.06 * delta_time)

            # Check if a new ball should appear
            if len(self.balls) < self.max_balls and self.ball_time == 0:
                # Check if the new ball would collide
                if collide(self.balls):
                    # If the new ball collides, its appearance is delayed
                    self.ball_time = 60
                
                # Spawn a new ball
                else:
                    # Reset the time for the next ball
                    self.ball_time = self.ball_delay * len(self.balls)

                    # Add a new ball to the stage
                    self.balls.add(Ball(125, 175, 10))

                    # Play a sound when a new ball appears
                    random.choice(self.snd_ball).play()
            
            # Reduce time left
            else:
                self.ball_time = approach(self.ball_time, 0, 0.06 * delta_time)

    def draw(self, screen):
        super().draw(screen)
        
        # Enemy score
        text_surface = SpriteFontManager.render_text('spr_font.png', str(self.enemy_score))
        screen.blit(text_surface, (halign_left(text_surface, screen), valign_top(text_surface, screen)))
        
        # Player score
        text_surface = SpriteFontManager.render_text('spr_font.png', str(self.player_score))
        screen.blit(text_surface, (halign_right(text_surface, screen), valign_bottom(text_surface, screen)))

        # Make the screen shake
        if self.shake:
            self.screen_distorsion(screen) if self.score else self.screen_shake(screen)