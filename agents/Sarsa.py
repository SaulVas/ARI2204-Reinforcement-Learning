from random import randint, choices
from collections import defaultdict
import numpy as np
from agents.AgentABC import Agent, HIT, STAND

RANDOM = 0
BEST = 1

def default_q_values():
    return [0, 0, 0]  # [q_value, count, alpha]

class SarsaControl(Agent):
    """
    epsilon_method: refers to the method of computing epsilon:
    0 - 0.1
    1 - 1/k
    2 - e^-k/1000
    3 - e^-k/10000
    """
    def __init__(self, epsilon_method=0):
        super().__init__()
        self.epsilon_method = epsilon_method
        self.episodes = 0
        self.current_episode = []
        self.state_action_values = defaultdict(default_q_values)
        self.gamma = 0.9  # discount factor

    def __repr__(self):
        return f"SARSA_{self.epsilon_method}"

    def update_q_values(self, state, action, reward, next_state, next_action):
        q_value, count, _ = self.state_action_values[(state, action)]
        next_q_value, _, _ = self.state_action_values[(next_state, next_action)]
        td_target = reward + self.gamma * next_q_value
        alpha = 1 / (count + 1)
        self.state_action_values[(state, action)] = [q_value + alpha * (td_target - q_value), count + 1, alpha]

    def _get_action(self, state):
        if self.epsilon_method == 0:
            epsilon = 0.1
        elif self.epsilon_method == 1:
            epsilon = np.divide(1, self.episodes)
        elif self.epsilon_method == 2:
            power = np.divide(self.episodes, 1000)
            epsilon = np.exp(-power)
        else:
            power = np.divide(self.episodes, 10000)
            epsilon = np.exp(-power)

        policy = choices([RANDOM, BEST], weights=(epsilon, 1 - epsilon), k=1)
        if policy == RANDOM:
            action = randint(STAND, HIT)
        else:
            action = self._best_action(state)

        self.current_episode.append((state, action))
        return action

    def _best_action(self, state):
        if (self.state_action_values[(state, HIT)][0] >=
            self.state_action_values[(state,STAND)][0]):
            return HIT

        return STAND

    def new_episode(self):
        self.episodes += 1
        self.current_episode = []

    def get_episode(self):
        return self.current_episode