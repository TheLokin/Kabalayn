import scenes

from objects import Player, Enemy
from utils import Colors, approach
from ..scene_fade import SceneFade
from pygame.locals import BLEND_MULT
from ..stage import ScreenBackground
from .screen_dialog import ScreenDialog
from .screen_narrator import ScreenNarrator
from scripts import SoundManager, Configuration as Config

class Cutscene(SceneFade):
    current_cutscene = 1
    
    def __init__(self, update=True):
        super().__init__()

        # Repeat cutscene
        if not update:
            Cutscene.current_cutscene -= 1
            ScreenDialog.current_dialog -= 1
            SoundManager.load_music('bgm_dialog.ogg')

        # Change level
        if Cutscene.current_cutscene in (4, 6, 8, 11, 14, 17):
            Config.level += 1
        
        # Background
        state = Config.state()
        self.background = ScreenBackground((Player(Colors.VIR), Enemy(state['color'], state['shoot_delay'])))

        # Transition
        self.transition = False
        self.transition_delay = 50
        self.snd_transition = SoundManager.load_sound('snd_transition1.wav')

        # Set the current screen
        if Cutscene.current_cutscene in (1, 4, 8, 11, 14, 17):
            self.current_screen = ScreenNarrator()
        elif Cutscene.current_cutscene in (3, 6, 7, 10, 13, 16, 19):
            self.current_screen = ScreenDialog()
            SoundManager.load_music('bgm_dialog.ogg')
        else:
            self.current_screen = ScreenDialog()
    
    def stop(self):
        self.transition = True
        self.snd_transition.play()

    def pre_update(self, events):
        super().pre_update(events)

        # Pre update the current screen
        self.current_screen.pre_update(events)
        
    def update(self, delta_time):
        super().update(delta_time)

        # Update the transition screen shake
        if self.transition:
            self.transition_delay = approach(self.transition_delay, 0, 0.06 * delta_time)
            
            # Check if the next scene should be loaded
            if self.transition_delay == 0:
                self.transition_delay = 50
                self.transition = False

                # Checks if it is the last scene
                if Cutscene.current_cutscene == 19:
                    self.director.change_scene(scenes.Menu(True))
                    Config.level = 1
                    Cutscene.current_cutscene = 1
                    ScreenNarrator.current_narrator = 0
                    ScreenDialog.current_dialog = 0
                
                # Checks wheter next scene is a combat or another cutscene
                elif Cutscene.current_cutscene in (2, 5, 6, 9, 12, 15, 18):
                    Cutscene.current_cutscene += 1
                    self.director.change_scene(scenes.Stage())
                else:
                    Cutscene.current_cutscene += 1
                    self.director.change_scene(scenes.Cutscene())
        else:
            # Update the current screen
            self.current_screen.update(delta_time, self)
    
    def draw(self, screen):
        # Draw background
        self.background.draw(screen)
        
        # Draw shadow over background
        shadow = screen.copy()
        shadow.fill(Colors.LIGHT_GREY)
        shadow.blit(screen, (0, 0), special_flags=BLEND_MULT)
        screen.blit(shadow, (0, 0))

        # Draw the current screen
        self.current_screen.draw(screen)

        # Make the transition screen shake
        if self.transition:
            self.background.screen_distorsion(screen)
        
        super().draw(screen)