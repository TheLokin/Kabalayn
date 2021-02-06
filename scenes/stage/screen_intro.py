from objects import Instructions
from utils import Colors, approach
from scripts import Keyboard, SoundManager
from .screen_background import ScreenBackground

class ScreenIntro(ScreenBackground):
    def __init__(self, entities, balls):
        super().__init__(entities, balls)

        # Screen shake
        self.shake = False

        # Instructions
        self.instructions = Instructions()

        # Transition
        self.transition = False
        self.transition_delay = 50
        self.snd_transition = SoundManager.load_sound('snd_transition2.wav')
    
    def pre_update(self, events):
        # Check if any key has been pressed
        if not self.transition and Keyboard.check_pressed('any', events):
            # Starts the transition
            self.transition = True
            
            # Make the screen shake
            self.shake = True

            # Play the transition sound
            self.snd_transition.play()
    
    def update(self, delta_time, scene):
        # Update the transition
        if self.transition:
            if self.transition_delay == 0:
                scene.start()
            else:
                self.transition_delay = approach(self.transition_delay, 0, 0.06 * delta_time)

        # Update the instructions
        self.instructions.update(delta_time, self)

        # Update the top particles
        self.top_particles.update(delta_time)

    def draw(self, screen):
        super().draw(screen)

        # Draw the instructions
        self.instructions.draw(screen)

        # Make the screen shake
        if self.shake:
            self.screen_distorsion(screen)