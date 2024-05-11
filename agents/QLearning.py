from random import randint, choices
import numpy as np
from agents.AgentABC import Agent, HIT, STAND, RANDOM, BEST

class QlearningControl(Agent):
    def __repr__(self):
        return f"SARSA_{self.epsilon_method}"

    def update_q_values(self, q, q_1, reward, is_final_state):
        # count update
        self.state_action_values[q][1] += 1
        count = self.state_action_values[q][1]

        # q value update
        alpha = np.divide(1, (count + 1))
        q_value = self.state_action_values[q][0]
        if is_final_state:
            self.state_action_values[q][0] = q_value + (alpha * (reward - q_value))
        else:
            next_state = q_1[0]
            next_q_value = max(self.state_action_values[(next_state, HIT)][0],
                               self.state_action_values[(next_state, STAND)][0])
            self.state_action_values[q][0] = q_value + (alpha * (reward + next_q_value - q_value))

    def _get_action(self):
        if self.epsilon_method == 0:
            epsilon = np.divide(1, self.episodes)
        elif self.epsilon_method == 1:
            power = np.divide(self.episodes, 1000)
            epsilon = np.exp(-power)
        elif self.epsilon_method == 2:
            power = np.divide(self.episodes, 10000)
            epsilon = np.exp(-power)
        else:
            epsilon = 0.1

        policy = choices([RANDOM, BEST], weights=(epsilon, 1 - epsilon), k=1)
        if policy == RANDOM:
            action = randint(STAND, HIT)
        else:
            action = self._best_action()

        self.current_episode.append((self.state, action))
        return action
