import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

save_dir= 'documentation/plots'

def filter_state_action_values(values):
    return {k: v for k, v in values.items() if v[1] != 0}

def plot_wins_losses_draws(results):
    for agent, values in results.items():
        scores = values['scores']
        wins = [score[0] for score in scores]
        draws = [score[1] for score in scores]
        losses = [score[2] for score in scores]
        episodes = range(1, len(wins) + 1)

        plt.figure(figsize=(14, 8))
        plt.plot(episodes, wins, label='Wins')
        plt.plot(episodes, draws, label='Draws')
        plt.plot(episodes, losses, label='Losses')
        plt.xlabel('Episodes (x1000)')
        plt.ylabel('Counts')
        plt.title(f'Results for {agent}')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(save_dir, f'results/{agent}_results.png'))
        plt.close()

def plot_state_action_counts(results):
    os.makedirs(save_dir, exist_ok=True)
    for agent, values in results.items():
        filtered_values = filter_state_action_values(values['agent_values'])
        state_action_counts = {str(k): v[1] for k, v in filtered_values.items()}
        sorted_counts = sorted(state_action_counts.items(), key=lambda item: item[1], reverse=True)
        states, counts = zip(*sorted_counts)

        plt.figure(figsize=(14, 8))
        plt.bar(states, counts)
        plt.xlabel('State-Action Pairs')
        plt.ylabel('Count')
        plt.title(f'State-Action Pair Counts for {agent}')
        plt.xticks([])
        plt.tight_layout()
        plt.savefig(os.path.join(save_dir, f'counts/state_action_counts_{agent}.png'))
        plt.close()

def plot_unique_state_action_pairs(results):
    save_dir_unique = os.path.join(save_dir, 'unique_counts')

    mc_counts = {agent: len(filter_state_action_values(values['agent_values'])) for agent, values in results.items() if 'MC' in agent}
    sarsa_counts = {agent: len(filter_state_action_values(values['agent_values'])) for agent, values in results.items() if 'SARSA' in agent}
    q_learning_counts = {agent: len(filter_state_action_values(values['agent_values'])) for agent, values in results.items() if 'QLearning' in agent}

    def plot_counts(counts, title, filename):
        agents = list(counts.keys())
        counts = list(counts.values())

        plt.figure(figsize=(14, 8))
        bars = plt.bar(agents, counts)
        plt.xlabel('Agents')
        plt.ylabel('Number of Unique State-Action Pairs')
        plt.title(title)
        plt.xticks(rotation=90)
        plt.tight_layout()

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

        plt.savefig(os.path.join(save_dir_unique, filename))
        plt.close()

    plot_counts(mc_counts,
                'Unique State-Action Pairs for Monte Carlo',
                'unique_state_action_pairs_mc.png')
    plot_counts(sarsa_counts,
                'Unique State-Action Pairs for SARSA',
                'unique_state_action_pairs_sarsa.png')
    plot_counts(q_learning_counts,
                'Unique State-Action Pairs for Q-Learning',
                'unique_state_action_pairs_q_learning.png')

def calculate_dealer_advantage(results):
    os.makedirs(save_dir, exist_ok=True)
    advantages = {}
    for agent, values in results.items():
        scores = np.array(values['scores'])
        last_10k_scores = scores[-10:]
        mean_losses = np.mean(last_10k_scores[:, 2])
        mean_wins = np.mean(last_10k_scores[:, 0])
        advantage = (mean_losses - mean_wins) / (mean_losses + mean_wins)
        advantages[agent] = advantage

    agents = list(advantages.keys())
    advantages_values = list(advantages.values())

    plt.figure(figsize=(14, 8))
    plt.bar(agents, advantages_values)
    plt.xlabel('Agents')
    plt.ylabel('Dealer Advantage')
    plt.title('Dealer Advantage Across Algorithm Configurations')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, 'dealer_advantage.png'))
    plt.close()

def create_strategy_table(q_values, ace=True):
    strategy_table = pd.DataFrame(index=range(20, 11, -1), columns=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
    dealer_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for player_sum in range(20, 11, -1):
        for dealer_card in dealer_cards:
            if dealer_card == 11:
                dealer_card = 'A'
            state_hit = ((player_sum, dealer_card, ace), 1)
            state_stand = ((player_sum, dealer_card, ace), 0)
            if state_hit in q_values and state_stand in q_values:
                action = 'H' if q_values[state_hit][0] >= q_values[state_stand][0] else 'S'
                strategy_table.loc[player_sum, dealer_card] = action
            elif state_hit in q_values:
                strategy_table.loc[player_sum, dealer_card] = 'H'
            elif state_stand in q_values:
                strategy_table.loc[player_sum, dealer_card] = 'S'
            else:
                strategy_table.loc[player_sum, dealer_card] = 'N/A'
            
    return strategy_table

def save_strategy_table_plot(strategy_table_with_ace, strategy_table_without_ace, config_name):
    fig, axs = plt.subplots(1, 2, figsize=(20, 10))

    axs[0].set_title(f'Strategy Table for {config_name} (with Ace)')
    axs[0].table(cellText=strategy_table_with_ace.values, colLabels=strategy_table_with_ace.columns, rowLabels=strategy_table_with_ace.index, loc='center')
    axs[0].axis('off')

    axs[1].set_title(f'Strategy Table for {config_name} (without Ace)')
    axs[1].table(cellText=strategy_table_without_ace.values, colLabels=strategy_table_without_ace.columns, rowLabels=strategy_table_without_ace.index, loc='center')
    axs[1].axis('off')

    plt.savefig(os.path.join(save_dir, f'strategies/{config_name}_strategy_table_combined.png'))
    plt.close()

def generate_and_save_strategy_tables(results):
    for agent, values in results.items():
        q_values = filter_state_action_values(values['agent_values'])
        strategy_table_with_ace = create_strategy_table(q_values, ace=True)
        strategy_table_without_ace = create_strategy_table(q_values, ace=False)
        save_strategy_table_plot(strategy_table_with_ace, strategy_table_without_ace, agent)