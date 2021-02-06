class Controller(object):
    def add(self, name, *bindings):
        '''
            Adds an action to be checked.

            name: The name for the action.

            bindings: The binging or sequence of bindings that trigger this action.
        '''

        raise NotImplementedError('call to abstract method ' + repr(self.add))

    def check(self, name, events):
        '''
            Returns if any of the action keys are held down. With this function you can check
            to see if a key is held down or not. Unlike the 'check_pressed' or 'check_released'
            methods which are only triggered once when a key is pressed or released, this
            function is triggered every step that the key is held down for.

            name: The name for the action.

            events: The list of events.
        '''

        raise NotImplementedError('call to abstract method ' + repr(self.check))
    
    def check_pressed(self, name, events):
        '''
            Returns if any of the action keys has just been pressed. With this function you can
            check to see if a key has been pressed or not. Unlike the 'check' method, this
            function will only run once for every time the key is pressed down, so for it to
            trigger again, the key must be first released and then pressed again.

            name: The name for the action.

            events: The list of events.
        '''

        raise NotImplementedError('call to abstract method ' + repr(self.check_pressed))

    def check_released(self, name, events):
        '''
            Returns if any of the action keys has just been released. With this function you can
            check to see if a key has been released or not. Unlike the 'check' function, this
            function will only run once for every time the key is lifted, so for it to trigger
            again, the key must be first pressed and then released again.

            name: The name for the action.

            events: The list of events.
        '''

        raise NotImplementedError('call to abstract method ' + repr(self.check_released))