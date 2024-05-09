from game_structure.Deck import Deck
from agents.Dealer import Dealer
from game_structure.Hand import Hand

class BlackJack:
    def __init__(self, agent):
        self.deck = Deck()
        self.agent = agent
        self.dealer = Dealer()
        self.agent_hand = Hand()
        self.dealer_hand = Hand()
        self.state = ()

    def play_round(self):
        self.deck.reset()
        self.deck.shuffle()

        # deal cards
        for _ in range(2):
            self.agent_hand.add_card(self.deck.draw_card())
            self.dealer_hand.add_card(self.deck.draw_card())

        # agent actions
        while True:
            self._set_state(self.agent_hand, self.dealer_hand)
            self.agent.set_state(self.state)
            if self.agent.get_action() == "stand":
                break

            self.agent_hand.add_card(self.deck.draw_card())
            if self._is_bust(self.agent_hand):
                print("Your hand:") #del
                print(self.agent_hand) #del
                print("bussssss") #del
                return -1

        # dealer actions
        while True:
            self.dealer.set_hand(self.dealer_hand)
            if self.dealer.get_action() == "stand":
                break

            self.dealer_hand.add_card(self.deck.draw_card())
            if self._is_bust(self.dealer_hand):
                print("Your hand:") #del
                print(self.agent_hand) #del

                print("\nDealer's hand:") #del
                print(self.dealer_hand) #del
                return 1

        # calculate the winner
        agent_value = self.agent_hand.calculate_hand_value()
        dealer_value = self.dealer_hand.calculate_hand_value()

        print("Your hand:") #del
        print(self.state[0]) #del

        print("\nDealer's hand:") #del
        print(self.dealer_hand) #del
        if agent_value > dealer_value:
            return 1

        if agent_value < dealer_value:
            return -1

        return 0

    def _set_state(self, agent_hand, dealer_hand):
        agent_sum, usable_ace = agent_hand.calculate_hand_value_with_flag()
        self.state = (agent_sum, dealer_hand.get_card(0), usable_ace,)

    def _is_bust(self, hand):
        value = hand.calculate_hand_value()
        if value > 21:
            return True

        return False
