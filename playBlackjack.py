from game_structure.Blackjack import BlackJack
from agents.UserAgent import UserAgent
from agents.AgentABC import WIN, DRAW
from game_structure.ASCII_skull import SKULL

if __name__ == "__main__":
    user_agent = UserAgent()

    blackjack = BlackJack()

    while True:
        reward, your_hand, dealer_hand = blackjack.play_round(user_agent)

        print(f"Your hand: {your_hand}")
        print(f"Dealers hand: {dealer_hand}")
        if reward == WIN:
            print("You Won")
        elif reward == DRAW:
            print("Draw")
        else:
            print(SKULL)

        print("\n")
