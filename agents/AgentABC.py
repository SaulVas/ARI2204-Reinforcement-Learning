from collections import defaultdict
from abc import ABC, abstractmethod

STAND = 0
HIT = 1

LOSS = -1
WIN = 1
DRAW = 0

RANDOM = 0
BEST = 1

def default_q_values():
    return [0, 0]

class Agent(ABC):
    """
    epsilon_method: refers to the method of computing epsilon:
    0 - 1/k
    1 - e^-k/1000
    2 - e^-k/10000
    3 - 0.1
    """
    def __init__(self, epsilon_method=0,):
        self.state = ()
        self.epsilon_method = epsilon_method
        self.episodes = 0
        self.current_episode = []
        self.state_action_values = defaultdict(default_q_values)

    def set_state(self, state):
        self.state = state

    def new_episode(self):
        self.episodes += 1
        self.current_episode = []

    def get_episode(self):
        return self.current_episode

    def get_state_action_value(self, index):
        return self.current_episode[index]

    def remove_state_action_value(self, index):
        self.current_episode.pop(index)

    def get_action(self):
        """
        Returns the action (hit or stand) based on the current state.
        
        Returns:
        str: The action to be taken, either 'hit' or 'stand'.
        """
        if self.state[0] < 12:
            self.current_episode.append((self.state, HIT))
            return HIT
        elif self.state[0] == 21:
            self.current_episode.append((self.state, STAND))
            return STAND
        else:
            return self._get_action()

    @abstractmethod
    def _get_action(self):
        """
        Returns the action (hit or stand) based on the current state when the hand value is between 11 and 21.
        
        Returns:
        str: The action to be taken, either 'hit' or 'stand'.
        """
