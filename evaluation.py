from agents.AgentABC import WIN, DRAW
from agents.MonteCarlo import MonteCarloControl

def monte_carlo_round(agent, game, tally):
    reward = game.play_round_MC(agent)
    update_reward_tally(reward, tally)

def sarsa_q_round(agent, game, tally):
    reward = game.play_round_SARSA_Q(agent)
    update_reward_tally(reward, tally)

def update_reward_tally(reward, tally):
    if reward == WIN:
        tally[0] += 1
    elif reward == DRAW:
        tally[1] += 1
    else:
        tally[2] += 1

def run_evaluation(agent, game, num_episodes=100000, log_interval=1000):
    scores = []
    tally = [0, 0, 0]  # [wins, draws, losses]

    for episode in range(num_episodes):
        if isinstance(agent, MonteCarloControl):
            monte_carlo_round(agent, game, tally)
        else:
            sarsa_q_round(agent, game, tally)

        if (episode + 1) % log_interval == 0:
            scores.append(tally.copy())
            tally = [0, 0, 0]

    agent_values = agent.get_state_action_values()

    return scores, agent_values
