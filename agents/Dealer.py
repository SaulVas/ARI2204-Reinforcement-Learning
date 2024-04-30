from game_structure.Hand import Hand

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def set_hand(self, hand):
        self.hand = hand

    def get_action(self):
        hand_value = self.hand.calculate_hand_value()

        if hand_value < 17:
            return "hit"
        else:
            return "stand"
