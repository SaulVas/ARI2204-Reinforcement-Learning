from general_functions import calculate_hand_value 

class Hand:
    def __init__(self, hand = []):
        self.hand = hand

    def __repr__(self):
        text = ""
        for card in self.hand:
            text += str(card) + ", "
        text = text[:-2]  # Remove the trailing comma
        text += f"\nHand Value: {calculate_hand_value(self.hand)}"
        return text

    def add_card(self, card):
        self.hand.append(card)
    
    def get_card(self, index):
        return self.hand[index]

    def get_hand_value(self):
        return calculate_hand_value(self.hand)
 