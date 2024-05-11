from game_structure.Blackjack import BlackJack
# from agents.UserAgent import UserAgent
from agents.MonteCarlo import MonteCarloControl
from agents.AgentABC import WIN, DRAW

def monte_carlo_round(agent, game, rewards):
    reward = game.play_round(agent)
    episode = agent.get_episode()
    agent.update_q_values(episode, reward)

    if reward == WIN:
        rewards[0] += 1
    elif reward == DRAW:
        rewards[1] += 1
    else:
        rewards[2] += 1

if __name__ == "__main__":
    # user_agent = UserAgent()

    blackjack = BlackJack()

    # Monte Carlo Methods
    MCES = MonteCarloControl(0, True)
    MC0 = MonteCarloControl(0)
    MC1 = MonteCarloControl(1)
    MC2 = MonteCarloControl(2)

    score = {
        "MCES": [0, 0, 0],
        "MC0": [0, 0, 0],
        "MC1": [0, 0, 0],
        "MC2": [0, 0, 0],
    }

    for _ in range(100000):
        monte_carlo_round(MCES, blackjack, score['MCES'])
        monte_carlo_round(MC0, blackjack, score['MC0'])
        monte_carlo_round(MC1, blackjack, score['MC1'])
        monte_carlo_round(MC2, blackjack, score['MC2'])

    print(f"MCES: Wins: {score['MCES'][0]}, Draws: {score['MCES'][1]}, Losses: {score["MCES"][2]}")
    print(f"MC0: Wins: {score['MC0'][0]}, Draws: {score['MC0'][1]}, Losses: {score["MC0"][2]}")
    print(f"MC1: Wins: {score['MC1'][0]}, Draws: {score['MC1'][1]}, Losses: {score["MC1"][2]}")
    print(f"MC2: Wins: {score['MC2'][0]}, Draws: {score['MC2'][1]}, Losses: {score["MC2"][2]}")
