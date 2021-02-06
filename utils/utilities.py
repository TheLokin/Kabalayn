import math
import pygame
from pygame.locals import SRCALPHA

def approach(start, end, amt):
    '''
        Moves from begin to end by amount and returns the result.

        start: The initial position.

        end: The final position.

        amt: The incremental value.
    '''

    if start < end:
        return min(start + amt, end)
    else:
        return max(start - amt, end)

def clamp(val, min_val, max_val):
    '''
        With this function you can maintain an input value between a specified range.

        val: The value to clamp.
        
        min_val: The minimum value to clamp between.
        
        max_val: The maximum value to clamp between.
    '''

    if val > max_val:
        return max_val
    elif val < min_val:
        return min_val
    else:
        return val

def cycle(val, min_val, max_val):
    '''
        https://yal.cc/angular-rotations-explained/

        The value is limited between the negative range and the positive range by adding the
        value of the range if it's negative, so that it would stay in range.

        val: The angle to cycling.

        min_val: The minimun angle to cycling between.

        max_val: The maximun angle to cycling between.
    '''

    delta = max_val - min_val
    result = (val - min_val) % delta

    if result < 0:
        result += delta
    
    return min_val + result

def angle_rotate(angle, target, speed):
    '''
        https://yal.cc/angular-rotations-explained/

        Calculate the closest rotation to produce a gradual angular rotation.

        angle: The current angle.
        
        target: The target angle.
        
        speed: The speed rotation.
    '''

    diff = cycle(target - angle, -180, 180)

    if diff < -speed:
        return angle - speed
    elif diff > speed:
        return angle + speed
    else:
        return target

def polygon_coordinate(x, y, angle, radius):
    '''
        https://www.mathopenref.com/coordparamcircle.html

        Calculate the points to draw a polygon.

        x: The x coordinate.

        y: The y coordinate.

        angle: The current angle.

        radius: The circle's radius (length from its center to its edge).
    '''

    return x + radius * math.cos(math.radians(angle)), y + radius * math.sin(math.radians(angle))

def swap_color(sprite, old_color, new_color):
    '''
        Swap a color in the sprite for another given.

        sprite: The sprite on which to do the swap.

        old_color: The color to swap.

        new_color: The color for which it's swap.
    '''

    new_r, new_g, new_b = new_color
    width, height = sprite.get_size()

    for x in range(width):
        for y in range(height):
            r, g, b, a = sprite.get_at((x, y))

            if (r, g, b) == old_color:
                sprite.set_at((x, y), pygame.Color(new_r, new_g, new_b, a))

    return sprite

def clip(surface, x, y, width, height):
    '''
        Returns a clipping area of the surface.

        surface: The surface to clip.

        x: The x coordinate from which to clip.

        y: The y coordinate from which to clip.

        width: The width to clip.

        height: The height to clip.
    '''

    surface = surface.copy()

    rectangle = pygame.Rect(x, y, width, height)
    surface.set_clip(rectangle)

    return surface.subsurface(surface.get_clip())

def slice_sprite(sprite, width, height):
    '''
        Slice a sprite in a list of sprites.

        sprite: The sprite to slice.

        width: The width of the slices.

        height: The height of the slices.
    '''

    sprite_sheet = []
    for y in range(sprite.get_height() // height):
        for x in range(sprite.get_width() // width):
            rectangle = pygame.Rect((x * width, y * height, width, height))
            sprite_sheet.append(sprite.subsurface(rectangle))
    
    return sprite_sheet

def draw_box(sprite, tile_width, tile_height):
    '''
        Draw a box from a sprite which is divided in 9 frames containing all slices in
        the following order: top left, top center, top right, middle left, middle center,
        middle left, bottom right, bottom center and bottom left.

        sprite: The sprite with the box.

        tile_width: How many times is it repeated on the horizontal axis.

        tile_height: How many times is it repeated on the vertical axis.
    '''

    # Slices the sprite
    sprite_width = sprite.get_width() // 3
    sprite_height = sprite.get_height() // 3
    sprite_sheet = slice_sprite(sprite, sprite_width, sprite_height)    

    width = sprite_width * 2 + tile_width * sprite_width
    height = sprite_height * 2 + tile_height * sprite_height

    # The surface for the box
    surface = pygame.Surface((width, height), SRCALPHA, 32)
    surface.convert_alpha()

    # Top left
    surface.blit(sprite_sheet[0], (0, 0))

    # Top right
    surface.blit(sprite_sheet[2], (width - sprite_width, 0))

    # Bottom left
    surface.blit(sprite_sheet[6], (0, height - sprite_height))

    # Bottom right
    surface.blit(sprite_sheet[8], (width - sprite_width, height - sprite_height))

    # Sides and center
    width += width % sprite_width
    height += height % sprite_height

    tile_width = int((width - sprite_width * 2) / sprite_width)
    tile_height = int((height - sprite_height * 2) / sprite_height)

    for x in range(tile_width):
        # Top center
        surface.blit(sprite_sheet[1], (sprite_width + x * sprite_width, 0))

        # Middle center
        for y in range(tile_height):
            surface.blit(sprite_sheet[4], (sprite_width + x * sprite_width, sprite_height + y * sprite_height))
        
        # Bottom center
        surface.blit(sprite_sheet[7], (sprite_width + x * sprite_width, height - sprite_height))

    for y in range(tile_height):
        # Middle left
        surface.blit(sprite_sheet[3], (0, sprite_height + y * sprite_height))
        
        # Middle right
        surface.blit(sprite_sheet[5], (width - sprite_width, sprite_height + y * sprite_height))

    return surface

def blit_alpha(surface, sprite, x, y, opacity):
    '''
        Draws a sprite onto the surface with some opacity.
         
        surface: The surface to draw on.
        
        sprite: The sprite to draw.
        
        x: The x coordinate.
        
        y: The y coordinate.

        opacity: The opacity with which the sprite is draw.
    '''

    temp = pygame.Surface((sprite.get_width(), sprite.get_height()))
    temp.blit(surface, (-x, -y))
    temp.blit(sprite, (0, 0))
    temp.set_alpha(opacity)
    surface.blit(temp, (x, y))

def halign_left(text, sprite):
    '''
        Returns the horizontally left aligned position of the text surface with
        respect to the sprite.

        text: The text surface.

        sprite: The sprite surface.
    '''

    return 0

def halign_center(text, sprite):
    '''
        Returns the horizontally center aligned position of the text surface with
        respect to the sprite.

        text: The text surface.

        sprite: The sprite surface.
    '''

    return sprite.get_width() / 2 - text.get_width() / 2

def halign_right(text, sprite):
    '''
        Returns the horizontally right aligned position of the text surface with
        respect to the sprite.

        text: The text surface.

        sprite: The sprite surface.
    '''

    return sprite.get_width() - text.get_width()

def valign_top(text, sprite):
    '''
        Returns the vertically top aligned position of the text surface with
        respect to the sprite.

        text: The text surface.

        sprite: The sprite surface.
    '''

    return 0

def valign_middle(text, sprite):
    '''
        Returns the vertically middle aligned position of the text surface with
        respect to the sprite.

        text: The text surface.

        sprite: The sprite surface.
    '''

    return sprite.get_height() / 2 - text.get_height() / 2

def valign_bottom(text, sprite):
    '''
        Returns the vertically bottom aligned position of the text surface with
        respect to the sprite.

        text: The text surface.

        sprite: The sprite surface.
    '''

    return sprite.get_height() - text.get_height()