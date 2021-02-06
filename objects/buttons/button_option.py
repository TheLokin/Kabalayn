from .arrow import ArrowLeft, ArrowRight
from .button import Button
from scripts import SpriteManager
from utils import Colors, draw_box, blit_alpha, halign_left, halign_right

class ButtonOption(Button):
    def __init__(self, x, y, tile_width, tile_height, option, options, is_circular, text_code):
        super().__init__(text_code)

        self.option = int(option)
        self.options = options
        self.is_circular = is_circular

        self.x = x
        self.y = y
        self.text_secondary = ''
        self.spr_box = draw_box(SpriteManager.load_sprite('spr_box.png'), tile_width, tile_height)
        
        self.arrow_left = ArrowLeft(self, x, y + self.spr_box.get_height() / 2)
        self.arrow_right = ArrowRight(self, x + self.spr_box.get_width(), y + self.spr_box.get_height() / 2)

    @classmethod
    def cancel(cls, scene):
        '''
            Method called to cancel the change on the option.
        '''

        raise NotImplementedError('call to abstract method ' + repr(cls.cancel))

    @classmethod
    def confirm(cls, scene):
        '''
            Method called to confirm the change on the option.
        '''

        raise NotImplementedError('call to abstract method ' + repr(cls.confirm))

    def key_left(self, scene):
        self.snd_choice.play()
        if self.option > 0:
            self.option -= 1
        elif self.is_circular:
            self.option = len(self.options) - 1

        self.execute(scene)

    def key_right(self, scene):
        self.snd_choice.play()
        if self.option < len(self.options) - 1:
            self.option += 1
        elif self.is_circular:
            self.option = 0
        
        self.execute(scene)

    def draw(self, surface):
        # Draw the arrows
        self.arrow_left.draw(surface)
        self.arrow_right.draw(surface)

        if self.is_selected:
            # Draw the box
            surface.blit(self.spr_box, (self.x, self.y))

            # Draw text shadow
            text_surface = self.font.render(self.text, False, Colors.BROWN)
            surface.blit(text_surface, (self.x + halign_left(text_surface, self.spr_box) + 23, self.y + 13))

            # Draw text
            text_surface = self.font.render(self.text, False, Colors.LIGHT_WHITE)
            surface.blit(text_surface, (self.x + halign_left(text_surface, self.spr_box) + 20, self.y + 10))

            # Draw secondary text shadow
            text_surface = self.font.render(self.text_secondary, False, Colors.BROWN)
            surface.blit(text_surface, (self.x + halign_right(text_surface, self.spr_box) - 17, self.y + 13))

            # Draw secondary text
            text_surface = self.font.render(self.text_secondary, False, Colors.LIGHT_WHITE)
            surface.blit(text_surface, (self.x + halign_right(text_surface, self.spr_box) - 20, self.y + 10))
        else:
            # Draw the box
            blit_alpha(surface, self.spr_box, self.x, self.y, self.opacity)

            # Draw text shadow
            text_surface = self.font.render(self.text, False, Colors.BROWN)
            blit_alpha(surface, text_surface, self.x + halign_left(text_surface, self.spr_box) + 23, self.y + 13, self.opacity)

            # Draw text
            text_surface = self.font.render(self.text, False, Colors.LIGHT_WHITE)
            blit_alpha(surface, text_surface, self.x + halign_left(text_surface, self.spr_box) + 20, self.y + 10, self.opacity)

            # Draw secondary text shadow
            text_surface = self.font.render(self.text_secondary, False, Colors.BROWN)
            blit_alpha(surface, text_surface, self.x + halign_right(text_surface, self.spr_box) - 17, self.y + 13, self.opacity)

            # Draw secondary text
            text_surface = self.font.render(self.text_secondary, False, Colors.LIGHT_WHITE)
            blit_alpha(surface, text_surface, self.x + halign_right(text_surface, self.spr_box) - 20, self.y + 10, self.opacity)