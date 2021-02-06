from scripts import FontManager
from utils import Colors, halign_center
from objects import Group, ButtonPlay, ButtonMultiplayer, ButtonOptions, ButtonExit

class ScreenMenu(object):
    def __init__(self, scene):
        # Title
        self.text_y = 101
        self.text = "KAbaLYN"
        self.font = FontManager.load_font('blade.ttf', 72)
        
        # Buttons
        self.buttons = Group((
            ButtonPlay(scene),
            ButtonMultiplayer(scene),
            ButtonOptions(scene),
            ButtonExit(scene)
        ))

    def pre_update(self, events, scene):
        # Pre update the buttons
        self.buttons.pre_update(events, scene)

    def update(self, delta_time):
        # Update the buttons
        self.buttons.update(delta_time)

    def draw(self, screen):
        # Draw text shadow
        text_surface = self.font.render(self.text, False, Colors.DARK_GREY)
        screen.blit(text_surface, (halign_center(text_surface, screen) + 5, self.text_y))
        
        # Draw text
        text_surface = self.font.render(self.text, False, Colors.LIGHT_WHITE)
        screen.blit(text_surface, (halign_center(text_surface, screen), self.text_y))

        # Draw the buttons
        self.buttons.draw(screen)