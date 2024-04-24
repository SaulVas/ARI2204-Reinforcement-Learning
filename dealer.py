from deck import Deck
from general_functions import calculate_hand_value

class Dealer:
    def __init__(self):
        self.hand = []
        
    def set_hand(self, hand):
        self.hand = hand

    def _calculate_hand_value(self):
        return calculate_hand_value(self.hand)

    def get_action(self):
        hand_value = self._calculate_hand_value()
        
        if hand_value < 17:
            return "hit"
        else:
            return "stand"
    