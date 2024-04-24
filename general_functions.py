def calculate_hand_value(hand):
    card_values = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
        }
    
    value = 0
    num_aces = 0
    for card in hand:
        value += card_values[card.get_value()]
        if card.get_value() == 'A':
            num_aces += 1
    while value <= 11 and num_aces > 0:
        value += 10
    return value