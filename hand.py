from general_functions import caluclate_hand_value 
from deck import Deck

class Hand:
    def __init__(self):
        self.hand = []

    def set_hand(self, hand):
        self.hand = hand

    def add_card(self, card):
        self.hand.append(card)
    
    def __repr__(self):
        text = ""
        for card in self.hand:
            text += str(card) + ", "
        text = text[:-2]  # Remove the trailing comma
        text += f"\nHand Value: {caluclate_hand_value(self.hand)}"
        return text
 
    
deck = Deck()
hand = Hand()
hand.add_card(deck.draw_card())
hand.add_card(deck.draw_card())
hand.add_card(deck.draw_card())

print(hand)