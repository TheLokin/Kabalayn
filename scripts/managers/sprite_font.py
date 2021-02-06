import pygame

from utils import slice_sprite
from .sprite import SpriteManager
from pygame.locals import SRCALPHA

class SpriteFontManager(object):
    resources = {}
 
    @classmethod
    def load_font(cls, name, string_map):
        '''
            Creates a new font resource based on a sprite with the sub-images
            ordered by a string.

            name: The sprite to add a font based on.

            string_map:	String from which sprite sub-image order is taken.
        '''

        code = hash(name)
        
        if code in cls.resources:
            raise Exception('Cannot load sprite font: ' + name)
        else:
            sprite = SpriteManager.load_sprite(name)
            sprite_width = sprite.get_width() // len(string_map)
            sprite_height = sprite.get_height()
            sprite_sheet = slice_sprite(sprite, sprite_width, sprite_height)
            
            i = 0
            font_map = {'width': sprite_width, 'height': sprite_height}
            for char in string_map:
                font_map[char] = sprite_sheet[i]
                i += 1
                
            cls.resources[code] = font_map
    
    @classmethod
    def render_text(cls, name, text):
        '''
            Return a surface with the text rendered with the chosen font.

            name: The name of the font.

            text: The string to render.
        '''
        
        code = hash(name)
        
        if code not in cls.resources:
            raise Exception('Cannot load sprite font: ' + name)
        else:
            font_map = cls.resources[code]
            sprite_width = font_map['width']
            sprite_height = font_map['height']
            surface = pygame.Surface((sprite_width * len(text), sprite_height), SRCALPHA, 32)
            surface.convert_alpha()
            
            i = 0
            for char in text:
                surface.blit(font_map[char], (i * sprite_width, 0))
                i += 1
                        
            return surface