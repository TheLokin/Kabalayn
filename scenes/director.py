import pygame

from utils import Singleton
from scripts import Keyboard
from pygame.locals import QUIT

class Director(object, metaclass=Singleton):
    def __init__(self):
        # Setup pygame
        self.screen = pygame.display.set_mode((500, 700), 0, 32)
        pygame.display.set_caption('Kabalayn')

        # Scene stack
        self.stack = []

        # Flag that says when to leave the scene
        self.quit_scene = False

        # Frame rate
        self.clock = pygame.time.Clock()
    
    def push_scene(self, scene):
        '''
            The scene passing as a parameter is placed at the top of the stack,
            above the current one.

            scene: The scene to put on top of the stack.
        '''

        self.quit_scene = True
        self.stack.append(scene)

    def pop_scene(self):
        '''
            Remove the current scene from the stack, if any.
        '''

        self.quit_scene = True

        if len(self.stack) > 0:
            self.stack.pop()

    def change_scene(self, scene):
        '''
            End the game loop, remove the current scene from the stack and add
            the new scene at the top of the stack to be executed.

            scene: The scene to put on top of the stack.
        '''
        
        self.pop_scene()
        self.stack.append(scene)

    def run(self):
        '''
            Run the game loop for the scene at the top of the stack.
        '''
        
        while len(self.stack) > 0:
            scene = self.stack[len(self.stack) - 1]
            
            self.loop(scene)

    def loop(self, scene):
        '''
            Execute the game loop for the given scene, performing all the actions of it.

            scene: The scene to execute.
        '''

        self.quit_scene = False

        # All events produced before entering the game loop are deleted
        pygame.event.clear()

        # The game loop, the actions performed will be done in each scene
        while not self.quit_scene:
            # Synchronize the game
            delta_time = self.clock.tick(60)

            # Get the list of events
            events = pygame.event.get()

            # Pre update the scene
            scene.pre_update(events)

            # Update the scene
            scene.update(delta_time)
            
            # The scene is drawn on the screen
            scene.draw(self.screen)
            pygame.display.update()

            # Closes the game
            for event in events:
                if event.type == QUIT:
                    self.game_end()
    
    def game_end(self):
        '''
            Empty the list of pending scenes to exit from the game loop.
        '''

        self.stack.clear()
        self.quit_scene = True