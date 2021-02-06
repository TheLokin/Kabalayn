import pygame
import scenes

from utils import Colors
from ..scene_fade import SceneFade
from pygame.locals import BLEND_MULT
from .screen_pause import ScreenPause
from .screen_options import ScreenOptions
from scripts import Keyboard, SoundManager

class Pause(SceneFade):
    def __init__(self, undo=False):
        super().__init__()

        self.undo = undo

        # Background
        self.background = pygame.display.get_surface().copy()

        # Screens
        self.screen_pause = ScreenPause(self)
        self.screen_options = ScreenOptions(self)

        # Set the current screen
        self.current_screen = self.screen_pause

        # Click sound
        self.snd_click = SoundManager.load_sound('snd_click.wav')
    
    def exec_continue(self):
        self.director.pop_scene()

    def exec_options(self):
        self.current_screen = self.screen_options

    def exec_quit(self):
        self.director.change_scene(scenes.Menu())
        if self.undo:
            scenes.Cutscene.current_cutscene -= 1
            scenes.ScreenDialog.current_dialog -= 1
    
    def exec_cancel(self):
        self.current_screen = self.screen_pause

    def exec_confirm(self):
        self.current_screen = self.screen_pause

    def pre_update(self, events):
        super().pre_update(events)
        
        # Closes the pause menu
        if Keyboard.check_pressed('pause', events):
            self.snd_click.play()
            self.director.pop_scene()
        else:
            # Pre update the current screen
            self.current_screen.pre_update(events, self)

    def update(self, delta_time):
        super().update(delta_time)

        # Update the current screen
        self.current_screen.update(delta_time)
        
    def draw(self, screen):
        # Draw background
        screen.blit(self.background, (0, 0))

        # Draw shadow over background
        shadow = screen.copy()
        shadow.fill(Colors.LIGHT_GREY)
        shadow.blit(screen, (0, 0), special_flags=BLEND_MULT)
        screen.blit(shadow, (0, 0))

        # Draw the current screen
        self.current_screen.draw(screen)

        super().draw(screen)