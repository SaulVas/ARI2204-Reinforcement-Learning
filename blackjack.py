from Deck import Deck
from general_functions import calculate_hand_value
from Dealer import Dealer
from Hand import Hand

class BlackJack:
    def __init__(self, agent):
        self.deck = Deck()
        self.agent = agent
        self.dealer = Dealer()
        self.agent_hand = Hand()
        self.dealer_hand = Hand()
        self.state = {}

    def play_round(self):
        self.deck.reset()
        self.deck.shuffle()

        # deal cards
        for _ in range(2):
            self._deal_card(self.agent_hand)
            self._deal_card(self.dealer_hand)
    
        # agent actions
        while True:
            self._set_state(self.agent_hand, self.dealer_hand)
            self.agent.set_state(self.state)
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
        agent_value = self.agent_hand.get_hand_value()
        dealer_value = self.dealer_hand.get_hand_value()

        if agent_value > dealer_value:
            return "win"
        elif agent_value < dealer_value:
            return "loss"
        else:
            return "tie"

    def _deal_card(self, hand):
        hand.add_card(self.deck.draw_card())

    def _set_state(self, agent_hand, dealer_hand):
        self.state = {
            "agent": agent_hand,
            "dealer": dealer_hand.get_card(0)
        }

    def _is_bust(self, hand):
        value = hand.get_hand_value()
        if value > 21:
            return True
        
        return False