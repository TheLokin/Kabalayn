import os
import random
import pygame

from scenes import Director, Menu

if __name__ == '__main__':
    try:
        # Generate a seed
        random.seed()
        
        # Center window
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        
        # Init pygame
        pygame.mixer.pre_init(44100, -16, 2, 4096)
        pygame.mixer.init()
        pygame.init()
        
        # The scene director is created
        director = Director()
        
        # The scene with the initial screen is created and stacked
        director.push_scene(Menu())
        
        # Start the game loop
        director.run()
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()