from utils import Colors, halign_center
from scripts import FontManager, LanguageManager
from objects import Group, ButtonLanguage, ButtonMasterVolume, ButtonSoundVolume, ButtonMusicVolume, ButtonCancel, ButtonConfirm

class ScreenOptions(object):
    def __init__(self, scene):
        # Title
        self.text_y = 101
        self.text = LanguageManager.load_text("uiOptions")
        self.font = FontManager.load_font('blade.ttf', 72)

        # Buttons
        self.buttons = Group((
            ButtonLanguage(scene),
            ButtonMasterVolume(scene),
            ButtonSoundVolume(scene),
            ButtonMusicVolume(scene),
            ButtonCancel(scene),
            ButtonConfirm(scene)
        ))

    def pre_update(self, events, scene):
        # Pre update the buttons
        self.buttons.pre_update(events, scene)
    
    def update(self, delta_time):
        # Update the buttons
        self.buttons.update(delta_time)

        # Update text
        self.text = LanguageManager.load_text("uiOptions")

    def draw(self, screen):
        # Draw text shadow
        text_surface = self.font.render(self.text, False, Colors.DARK_GREY)
        screen.blit(text_surface, (halign_center(text_surface, screen) + 5, self.text_y + 5))

        # Draw text
        text_surface = self.font.render(self.text, False, Colors.LIGHT_WHITE)
        screen.blit(text_surface, (halign_center(text_surface, screen), self.text_y))

        # Draw the buttons
        self.buttons.draw(screen)