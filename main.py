from game_structure.Blackjack import BlackJack
# from agents.UserAgent import UserAgent
from agents.MonteCarlo import MonteCarloControl
from agents.Sarsa import SarsaControl
from agents.QLearning import QlearningControl
from evaluation import run_evaluation
from plots import plot_wins_losses_draws, plot_state_action_counts, plot_unique_state_action_pairs, calculate_dealer_advantage, generate_and_save_strategy_tables

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

    plot_wins_losses_draws(results)
    plot_state_action_counts(results)
    plot_unique_state_action_pairs(results)
    calculate_dealer_advantage(results)
    generate_and_save_strategy_tables(results)
