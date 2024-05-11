from game_structure.Blackjack import BlackJack
# from agents.UserAgent import UserAgent
from agents.MonteCarlo import MonteCarloControl
from agents.Sarsa import SarsaControl
from agents.QLearning import QlearningControl
from agents.AgentABC import WIN, DRAW

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

if __name__ == "__main__":
    # user_agent = UserAgent()

    blackjack = BlackJack()

    # Monte Carlo Methods
    MCES = MonteCarloControl(0, True)
    MC0 = MonteCarloControl(0)
    MC1 = MonteCarloControl(1)
    MC2 = MonteCarloControl(2)

    SARSA0 = SarsaControl(0)
    SARSA1 = SarsaControl(1)
    SARSA2 = SarsaControl(2)
    SARSA3 = SarsaControl(3)

    Q0 = QlearningControl(0)
    Q1 = QlearningControl(1)
    Q2 = QlearningControl(2)
    Q3 = QlearningControl(3)


    score = {
        "MCES": [0, 0, 0],
        "MC0": [0, 0, 0],
        "MC1": [0, 0, 0],
        "MC2": [0, 0, 0],
        "SARSA0": [0, 0, 0],
        "SARSA1": [0, 0, 0],
        "SARSA2": [0, 0, 0],
        "SARSA3": [0, 0, 0],
        "QLearning0": [0, 0, 0],
        "QLearning1": [0, 0, 0],
        "QLearning2": [0, 0, 0],
        "QLearning3": [0, 0, 0],
    }

    for _ in range(100000):
        monte_carlo_round(MCES, blackjack, score['MCES'])
        monte_carlo_round(MC0, blackjack, score['MC0'])
        monte_carlo_round(MC1, blackjack, score['MC1'])
        monte_carlo_round(MC2, blackjack, score['MC2'])
        sarsa_q_round(SARSA0, blackjack, score['SARSA0'])
        sarsa_q_round(SARSA1, blackjack, score['SARSA1'])
        sarsa_q_round(SARSA2, blackjack, score['SARSA2'])
        sarsa_q_round(SARSA3, blackjack, score['SARSA3'])
        sarsa_q_round(Q0, blackjack, score['QLearning0'])
        sarsa_q_round(Q1, blackjack, score['QLearning1'])
        sarsa_q_round(Q3, blackjack, score['QLearning2'])
        sarsa_q_round(Q3, blackjack, score['QLearning3'])


    print(f"MCES: Wins: {score['MCES'][0]}, Draws: {score['MCES'][1]}, Losses: {score["MCES"][2]}")
    print(f"MC0: Wins: {score['MC0'][0]}, Draws: {score['MC0'][1]}, Losses: {score["MC0"][2]}")
    print(f"MC1: Wins: {score['MC1'][0]}, Draws: {score['MC1'][1]}, Losses: {score["MC1"][2]}")
    print(f"MC2: Wins: {score['MC2'][0]}, Draws: {score['MC2'][1]}, Losses: {score["MC2"][2]}")

    print(f"SARSA0: Wins: {score['SARSA0'][0]}, Draws: {score['SARSA0'][1]}, Losses: {score["SARSA0"][2]}")
    print(f"SARSA1: Wins: {score['SARSA1'][0]}, Draws: {score['SARSA1'][1]}, Losses: {score["SARSA1"][2]}")
    print(f"SARSA2: Wins: {score['SARSA2'][0]}, Draws: {score['SARSA2'][1]}, Losses: {score["SARSA2"][2]}")
    print(f"SARSA3: Wins: {score['SARSA3'][0]}, Draws: {score['SARSA3'][1]}, Losses: {score["SARSA3"][2]}")
    
    print(f"QLearning0: Wins: {score['QLearning0'][0]}, Draws: {score['QLearning0'][1]}, Losses: {score["QLearning0"][2]}")
    print(f"QLearning1: Wins: {score['QLearning1'][0]}, Draws: {score['QLearning1'][1]}, Losses: {score["QLearning1"][2]}")
    print(f"QLearning2: Wins: {score['QLearning2'][0]}, Draws: {score['QLearning2'][1]}, Losses: {score["QLearning2"][2]}")
    print(f"QLearning3: Wins: {score['QLearning3'][0]}, Draws: {score['QLearning3'][1]}, Losses: {score["QLearning3"][2]}")
