from Blackjack import BlackJack
from UserAgent import UserAgent

user_agent = UserAgent()
game = BlackJack(user_agent)

game.play_round()