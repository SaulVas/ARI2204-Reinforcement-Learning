from deck import Deck
from general_functions import caluclate_hand_value
# from dealer import Dealer

class BlackJack():
    def __init__(self, agent):
        self.deck = Deck()
        self.agent = agent
        # self.dealer = Dealer()
        self.agent_hand = []
        self.dealer_hand = []
        self.state = {}

    def play_round(self):
        self.deck.reset()

        # deal cards
        for _ in range(2):
            self._deal_card(self.agent_hand)
            self._deal_card(self.dealer_hand)
    
        # agent actions
        while True:
            self._update_state(self.agent_hand, self.dealer_hand)
            self.agent.update_state(self.state)
            if self.agent.get_action() == "stand":
                break

            self._deal_card(self.agent_hand)
            if self._is_bust(self.agent_hand):
                return "loss"
        
        # dealer actions
        while True:
            self.dealer.set_hand(self.dealer_hand)
            if self.dealer.get_action() == "stand":
                break

            self._deal_card(self.dealer_hand)
            if self._is_bust(self.dealer_hand):
                return "win"

        # calculate the winner
        agent_value = self._calculate_hand_value(self.agent_hand)
        dealer_value = self._calculate_hand_value(self.dealer_hand)

        if agent_value > dealer_value:
            return "win"
        elif agent_value < dealer_value:
            return "loss"
        else:
            return "tie"

    def _deal_card(self, hand):
        hand.append(self.self.deck.draw_card())

    def _update_state(self, agent_hand, dealer_hand):
        self.state = {
            "agent": agent_hand,
            "dealer": dealer_hand[0]
        }

    def _calculate_hand_value(self, hand):
        return caluclate_hand_value(hand)

    def _is_bust(self, hand):
        value = self._calculate_hand_value(hand)
        if value > 21:
            return True
        
        return False