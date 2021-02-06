from utils import Colors, approach
from scripts import Keyboard, SoundManager, FontManager, LanguageManager, Configuration as Config

class ScreenNarrator(object):
    current_narrator = 0
    
    def __init__(self):
        # Load text
        self.line_list = []
        ScreenNarrator.current_narrator += 1
        for phrase in LanguageManager.load_text('narrator' + str(ScreenNarrator.current_narrator)):
            self.line_list.append(phrase)

        # Text info
        self.current_index = 0
        self.current_string = ''
        self.current_line = ''
        self.input_string = self.line_list[0]

        # Text location
        self.text_x = 44
        self.text_y = 258
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

    def pre_update(self, events):
        self.key_interact = Keyboard.check_pressed('interact', events)

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

    def update(self, delta_time, scene):
        # Check for sleep
        if self.sleep_ticks > 0:
            self.sleep_ticks = approach(self.sleep_ticks, 0, 0.06 * delta_time)
        else:            
            # Check if a character should be added
            if self.ticks == self.interval and self.input_string != '':
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
            if self.input_string != '':
                while self.input_string != '':
                    self.process_line()
                
                self.ticks = 0
                self.sleep_ticks = 0
            elif self.current_index + 1 < len(self.line_list):
                # Reset line
                self.current_index += 1
                self.current_string = ''
                self.current_line = ''
                self.input_string = self.line_list[self.current_index]
                
            # Stop the dialog
            else:
                scene.stop()

    def draw(self, screen):
        # Draw the text
        y = self.text_y
        for line in self.current_string.splitlines():
            # Draw text shadow
            line_surface = self.font.render(line, False, Colors.BROWN)
            screen.blit(line_surface, (self.text_x + 3, y + 3))
            
            # Draw text
            line_surface = self.font.render(line, False, Colors.LIGHT_WHITE)
            screen.blit(line_surface, (self.text_x, y))
            
            # Draw the text on the next line
            y += line_surface.get_height()