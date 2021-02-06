from .button import Button
from scripts import SpriteManager
from utils import Colors, draw_box, blit_alpha, halign_center

class ButtonAction(Button):
    def __init__(self, x, y, tile_width, tile_height, text_code):
        super().__init__(text_code)

        self.x = x
        self.y = y
        self.spr_box = draw_box(SpriteManager.load_sprite('spr_box.png'), tile_width, tile_height)

    def draw(self, surface):
        if self.is_selected:
            # Draw the box
            surface.blit(self.spr_box, (self.x, self.y))

            # Draw text shadow
            text_surface = self.font.render(self.text, False, Colors.BROWN)
            surface.blit(text_surface, (self.x + halign_center(text_surface, self.spr_box) + 3, self.y + 13))

            # Draw text
            text_surface = self.font.render(self.text, False, Colors.LIGHT_WHITE)
            surface.blit(text_surface, (self.x + halign_center(text_surface, self.spr_box), self.y + 10))
        else:
            # Draw the box
            blit_alpha(surface, self.spr_box, self.x, self.y, self.opacity)

            # Draw text shadow
            text_surface = self.font.render(self.text, False, Colors.BROWN)
            blit_alpha(surface, text_surface, self.x + halign_center(text_surface, self.spr_box) + 3, self.y + 13, self.opacity)

            # Draw text
            text_surface = self.font.render(self.text, False, Colors.LIGHT_WHITE)
            blit_alpha(surface, text_surface, self.x + halign_center(text_surface, self.spr_box), self.y + 10, self.opacity)