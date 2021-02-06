from ..object import GameObject
from ..particles import Explosion
from scripts import SpriteManager
from utils import Colors, approach, ease_out_elastic, ease_out_cubic, swap_color

class Instructions(GameObject):
    def __init__(self):
        super().__init__()

        self.spr_instructions = swap_color(SpriteManager.load_sprite('spr_instructions.png'), Colors.WHITE, Colors.LIGHT_WHITE)
        self.x = 250 - self.spr_instructions.get_width() / 2
        self.y = 350 - self.spr_instructions.get_height() - 10

        self.frame = 0
        self.max_frames = (20, 50, 120)
        self.animation = 0

    def pre_update(self, events):
        pass

    def update(self, delta_time, scene):
        # Change animation
        if self.frame == self.max_frames[self.animation]:
            self.frame = 0

            # From animation go up to animation go down
            if self.animation == 1:
                self.animation = 2
            
                # Explosion particles
                for ball in scene.balls:
                    scene.top_particles.add(Explosion(ball.x, ball.y, Colors.LIGHT_WHITE, ball.radius, 75))

            # From animation go down to animation go up
            elif self.animation == 2:
                self.animation = 1

                # Explosion particles
                for ball in scene.balls:
                    scene.top_particles.add(Explosion(ball.x, ball.y, Colors.LIGHT_WHITE, ball.radius, 75))
            
            # From animation static to animation go up
            else:
                self.animation = 1

                # Explosion particles
                for ball in scene.balls:
                    scene.top_particles.add(Explosion(ball.x, ball.y, Colors.LIGHT_WHITE, ball.radius, 75))
        else:
            # Calculate the next frame
            self.frame = approach(self.frame, self.max_frames[self.animation], 0.06 * delta_time)

    def draw(self, surface):
        # Animation go up
        if self.animation == 1:
            distance = ease_out_cubic(self.frame, 0, 20, self.max_frames[self.animation])
            surface.blit(self.spr_instructions, (self.x, self.y - distance))
        
        # Animation go down
        elif self.animation == 2:
            distance = 20 - ease_out_elastic(self.frame, 0, 20, self.max_frames[self.animation])
            surface.blit(self.spr_instructions, (self.x, self.y - distance))

        # Animation static
        else:
            surface.blit(self.spr_instructions, (self.x, self.y))