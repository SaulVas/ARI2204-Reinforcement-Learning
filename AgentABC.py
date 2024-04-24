from abc import ABC, abstractmethod
from general_functions import calculate_hand_value

class Agent(ABC):
    def __init__(self):
        self.state = {}
        self.choices = ["hit", "stand"]

    def set_state(self, state):
        self.state = state
    
    @abstractmethod
    def get_action(self):
        """
        Returns the action (hit or stand) based on the current state.
        
        Returns:
        str: The action to be taken, either 'hit' or 'stand'.
        """
