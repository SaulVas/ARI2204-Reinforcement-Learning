from game_structure.Blackjack import BlackJack
from agents.UserAgent import UserAgent

user_agent = UserAgent()
game = BlackJack(user_agent)
RET = game.play_round()

if RET == "win":
    print("you won")
elif RET == "loss":
    print("you lost")
else:
    print("tie")
