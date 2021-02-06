import pygame

from objects import Portrait
from pygame.locals import BLEND_MULT
from utils import Colors, approach, slice_sprite, draw_box
from scripts import Keyboard, SpriteManager, SoundManager, FontManager, LanguageManager, Configuration as Config

class ScreenDialog(object):
    current_dialog = 0
    
    def __init__(self):
        # Load text
        self.sprite_list = []
        self.line_list = []
        ScreenDialog.current_dialog += 1
        for phrase in LanguageManager.load_text('cutscene' + str(ScreenDialog.current_dialog)):
            self.sprite_list.append(phrase['sprite'])
            self.line_list.append(phrase['dialog'])
        
        # Generate portraits
        self.speaker = 0
        self.portrait = {}
        self.portrait_left = Portrait(0, 186)
        self.portrait_right = Portrait(244, 186)
        self.portrait_right.pause()
        for sprite in list(set(self.sprite_list)):
            portrait = {}
            portrait['original'] = SpriteManager.load_sprite(sprite)
            portrait['original_flip'] = pygame.transform.flip(portrait['original'], True, False)
            portrait['shade'] = SpriteManager.load_sprite(sprite)
            portrait['shade'].fill(Colors.ALPHA_LIGHT_GREY, special_flags=BLEND_MULT)
            portrait['shade_flip'] = pygame.transform.flip(portrait['shade'], True, False)
            self.portrait[sprite] = portrait
        
        # Assign sprites
        sprite_left = self.sprite_list[0]
        sprite_right = self.sprite_list[1]
        pos = 1
        while sprite_left == sprite_right:
            pos += 1
            sprite_right = self.sprite_list[pos]
        self.sprite_left = self.portrait[sprite_left]['original_flip']
        self.sprite_right = self.portrait[sprite_right]['shade']

        # Generate box
        self.spr_box = draw_box(SpriteManager.load_sprite('spr_box.png'), 29, 6)
        self.box_x = 2
        self.box_y = 442
        self.spr_box_pause = slice_sprite(SpriteManager.load_sprite('spr_box_pause.png'), 16, 16)
        self.box_pause_x = self.box_x + 480
        self.box_pause_y = self.box_y + 112
        self.box_pause_index = 0

        # Text info
        self.current_index = 0
        self.current_string = ''
        self.current_line = ''
        self.input_string = self.line_list[0]

        # Text location
        self.text_x = self.box_x + 20
        self.text_y = self.box_y + 20
        self.line_length = 500 - self.text_x * 2
        self.font = FontManager.load_font('neogen.ttf', 24)

        # Interaction sounds
        self.snd_blit = SoundManager.load_sound('snd_blip.wav')
        self.snd_blit.fadeout(0)

        # Interaction delay
        self.interval = 2   
        self.ticks = 0     
        self.sleep_ticks = 0

        # Interaction
        self.key_interact = False

    def process_line(self):
        new_char = self.input_string[0]

        # Inspect character
        if new_char == ' ':
            # Check if there's room for the next word
            next_space_pos = self.input_string[1:].find(' ')

            # Plan B if there is no spaces left
            if next_space_pos == -1:
                next_space_pos = len(self.input_string)
            else:
                next_space_pos += 1
            
            # Calculate measurments
            current_width = self.font.size(self.current_line)[0]
            preview_width = self.font.size(self.input_string[:next_space_pos])[0]
            if current_width + preview_width > self.line_length:
                self.current_line = ''
                new_char = '\n'
        
        # Add new character
        self.current_string += new_char
        self.current_line += new_char
        self.input_string = self.input_string[1:]

    def pre_update(self, events):
        self.key_interact = Keyboard.check_pressed('interact', events)
    
    def update(self, delta_time, scene):
        # Check for sleep
        if self.sleep_ticks > 0:
            self.sleep_ticks = approach(self.sleep_ticks, 0, 0.06 * delta_time)
        else:
            # Calculate the current sub-image
            if self.input_string == '':
                self.box_pause_index = approach(self.box_pause_index, len(self.spr_box_pause), 0.005 * delta_time)
                if self.box_pause_index == len(self.spr_box_pause):
                    self.box_pause_index = 0
            
            # Check if a character should be added
            elif self.ticks == self.interval:
                self.ticks = 0
                
                new_char = self.input_string[0]

                # Sleep on space or punctuation mark
                if new_char == ' ':
                    self.sleep_ticks = round(self.interval / 3)
                elif new_char in [',', '.', ':', '?', '!']:
                    self.sleep_ticks = self.interval * 8
                
                # Add new character
                self.process_line()
                self.snd_blit.play()
            
            self.ticks = approach(self.ticks, self.interval, 0.06 * delta_time)

        # Finish text scroll or proceed to next line
        if self.key_interact:
            self.box_pause_index = 0
            
            if self.input_string != '':
                while self.input_string != '':
                    self.process_line()
                
                self.ticks = 0
                self.sleep_ticks = 0
            
            # Load next line
            elif self.current_index + 1 < len(self.line_list):
                # Reset line
                self.current_index += 1
                self.current_string = ''
                self.current_line = ''
                self.input_string = self.line_list[self.current_index]

                # Check if the portrait should be changed
                last_sprite = self.sprite_list[self.current_index - 1]
                new_sprite = self.sprite_list[self.current_index]
                if last_sprite != new_sprite:
                    self.portrait_left.pause()
                    self.portrait_right.pause()
                    if self.speaker == 0:
                        self.speaker = 1
                        self.sprite_left = self.portrait[last_sprite]['shade_flip']
                        self.sprite_right = self.portrait[new_sprite]['original']
                    elif self.speaker == 1:
                        self.speaker = 0
                        self.sprite_left = self.portrait[new_sprite]['original_flip']
                        self.sprite_right = self.portrait[last_sprite]['shade']
            
            # Stop the dialog
            else:
                scene.stop()
        
        # Update the portraits
        self.portrait_left.update(delta_time)
        self.portrait_right.update(delta_time)

    def draw(self, surface):
        # Draw the portraits
        self.portrait_left.draw(surface, self.sprite_left)
        self.portrait_right.draw(surface, self.sprite_right)
        
        # Draw the box
        surface.blit(self.spr_box, (self.box_x, self.box_y))
        if self.input_string == '':
            surface.blit(self.spr_box_pause[int(self.box_pause_index)], (self.box_pause_x, self.box_pause_y))
        
        # Draw the text
        y = self.text_y
        for line in self.current_string.splitlines():
            # Draw text shadow
            line_surface = self.font.render(line, False, Colors.BROWN)
            surface.blit(line_surface, (self.text_x + 3, y + 3))
            
            # Draw text
            line_surface = self.font.render(line, False, Colors.LIGHT_WHITE)
            surface.blit(line_surface, (self.text_x, y))
            
            # Draw the text on the next line
            y += line_surface.get_height()