class Hand:
    def __init__(self, hand = None):
        if hand is None:
            hand = []
        self.hand = hand

    def __repr__(self):
        text = ""
        for card in self.hand:
            text += str(card) + ", "
        text = text[:-2]  # Remove the trailing comma
        text += f"\nHand Value: {self.calculate_hand_value()}"
        return text

    def add_card(self, card):
        self.hand.append(card)

    def get_card(self, index):
        return self.hand[index]

    def calculate_hand_value(self):
        card_values = {
            'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
        }

        value = 0
        num_aces = 0

        # Calculate initial value of the hand and count aces
        for card in self.hand:
            card_value = card.get_value()
            value += card_values[card_value]
            if card_value == 'A':
                num_aces += 1

        # Adjust the value of aces if possible
        while value <= 11 and num_aces > 0:
            value += 10  # Upgrade an ace from 1 to 11
            num_aces -= 1

        return value

    def calculate_hand_value_with_flag(self):
        card_values = {
            'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
            }

        value = 0
        num_aces = 0
        has_usable_ace = False

        for card in self.hand:
            value += card_values[card.get_value()]
            if card.get_value() == 'A':
                num_aces += 1

        while value <= 11 and num_aces > 0:
            value += 10
            has_usable_ace = True

        return value, has_usable_ace
    
    def reset_hand(self):
        self.hand = []
