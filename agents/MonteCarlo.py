from random import randint, choices
import numpy as np
from agents.AgentABC import Agent, HIT, STAND, RANDOM, BEST

class MonteCarloControl(Agent):
    def __init__(self, epsilon_method, exploring_starts=False):
        if epsilon_method < 0 or epsilon_method > 2:
            raise ValueError("Incorrect Epsilon Method")
        super().__init__(epsilon_method)
        self.exploring_starts = exploring_starts

    def __repr__(self):
        ret = f"MC_{self.epsilon_method}"
        if self.exploring_starts:
            ret = ret + "_ES"
        return ret

    def update_q_values(self, new_values, reward):
        for state in new_values:
            # update count for states visited
            self.state_action_values[state][1] += 1
            count = self.state_action_values[state][1]

            # update state-action values for states visited
            q_value = self.state_action_values[state][0]
            self.state_action_values[state][0] = q_value + np.divide(1, count) * (reward - q_value)

    def _get_action(self):
        if self.exploring_starts and len(self.current_episode) == 0:
            action = randint(STAND, HIT)
        else:
            if self.epsilon_method == 0:
                epsilon = np.divide(1, self.episodes)
            elif self.epsilon_method == 1:
                power = np.divide(self.episodes, 1000)
                epsilon = np.exp(-power)
            else:
                power = np.divide(self.episodes, 10000)
                epsilon = np.exp(-power)

            policy = choices([RANDOM, BEST], weights=(epsilon, 1 - epsilon), k=1)
            if policy == RANDOM:
                action = randint(STAND, HIT)
            else:
                action = self._best_action()

        self.current_episode.append((self.state, action))
        return action

    def _best_action(self):
        if (self.state_action_values[(self.state, HIT)][0] >=
            self.state_action_values[(self.state,STAND)][0]):
            return HIT

        return STAND
