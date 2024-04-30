from game_structure.Blackjack import BlackJack
from agents.UserAgent import UserAgent

user_agent = UserAgent()
game = BlackJack(user_agent)
ret = game.play_round()

if ret == "win":
    print("you won")
elif ret == "loss":
    print("you lost")
else:
    print("tie")
