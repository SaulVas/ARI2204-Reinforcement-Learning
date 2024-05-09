from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self):
        self.state = ()
        self.choices = ["hit", "stand"]

    def set_state(self, state):
        self.state = state

    def get_action(self):
        """
        Returns the action (hit or stand) based on the current state.
        
        Returns:
        str: The action to be taken, either 'hit' or 'stand'.
        """
        if self.state[0] < 12:
            return "hit"
        elif self.state[0] == 21:
            return "stand"
        else:
            return self._get_action()

    @abstractmethod
    def _get_action(self):
        """
        Returns the action (hit or stand) based on the current state when the hand value is between 11 and 21.
        
        Returns:
        str: The action to be taken, either 'hit' or 'stand'.
        """
