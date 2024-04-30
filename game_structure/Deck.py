import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def get_value(self):
        return self.value

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
