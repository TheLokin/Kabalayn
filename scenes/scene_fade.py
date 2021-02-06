from .scene import Scene
from objects import Group, Fade

class SceneFade(Scene):
    is_fading = False
    function = None
    arguments = None
    executed = False
    counter = 0
    fades = Group()

    def fade(self, function, *args):
        SceneFade.is_fading = True
        SceneFade.function = function
        SceneFade.arguments = args
        SceneFade.executed = False
        Fade.reverse = False

    def pre_update(self, events):
        pass
    
    def update(self, delta_time):
        # Check is the scene is fading
        if SceneFade.is_fading:
            # Add fade animation
            if SceneFade.counter < 16:
                SceneFade.fades.add(Fade(SceneFade.counter))
                SceneFade.counter += 1
            
            # Check if the fade is over
            elif len(SceneFade.fades) == 0:
                SceneFade.is_fading = False
                SceneFade.counter = 0

        # Execute the function asociated
        if not SceneFade.executed and Fade.reverse:
            SceneFade.executed = True
            SceneFade.function(*SceneFade.arguments)

        # Update the fade
        SceneFade.fades.update(delta_time)

    def draw(self, screen):
        # Draw the fade
        SceneFade.fades.draw(screen)