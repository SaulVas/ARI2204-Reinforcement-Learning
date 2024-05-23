from game_structure.Blackjack import BlackJack
# from agents.UserAgent import UserAgent
from agents.MonteCarlo import MonteCarloControl
from agents.Sarsa import SarsaControl
from agents.QLearning import QlearningControl
from evaluation import run_evaluation

if __name__ == "__main__":
    # user_agent = UserAgent()

    blackjack = BlackJack()

    # Monte Carlo Methods
    agents = [
        MonteCarloControl(0, True),
        MonteCarloControl(0),
        MonteCarloControl(1),
        MonteCarloControl(2),

        SarsaControl(0),
        SarsaControl(1),
        SarsaControl(2),
        SarsaControl(3),

        QlearningControl(0),
        QlearningControl(1),
        QlearningControl(2),
        QlearningControl(3),
    ]

    results = {}

    for agent in agents:
        print(f"Running evaluation for {agent}")
        scores, agent_values = run_evaluation(agent, blackjack)
        results[repr(agent)] = {
            'scores': scores,
            'agent_values': agent_values
        }

    for agent, values in results.items():
        print(agent)
        print(len(values['scores']))
        print(len(values['agent_values']))
        print("\n")
