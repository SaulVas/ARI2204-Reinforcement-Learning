from agents.AgentABC import WIN, LOSS, DRAW, STAND
from game_structure.Deck import Deck
from agents.Dealer import Dealer
from game_structure.Hand import Hand

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.agent = None
        self.dealer = Dealer()
        self.agent_hand = Hand()
        self.dealer_hand = Hand()
        self.state = ()

    def _set_state(self, agent_hand, dealer_hand):
        agent_sum, usable_ace = agent_hand.calculate_hand_value_with_flag()

        self.state = (agent_sum, dealer_hand.get_card_value(0), usable_ace,)

    def _is_bust(self, hand):
        value = hand.calculate_hand_value()
        if value > 21:
            return True

        return False

    def _set_agent(self, agent):
        self.agent = agent

    def initialise_round(self, agent):
        self.deck.reset()
        self.deck.shuffle()
        self._set_agent(agent)
        self.agent.new_episode()
        self.agent_hand.reset_hand()
        self.dealer_hand.reset_hand()

    def play_round_MC(self, agent):
        self.initialise_round(agent)

        # deal cards
        for _ in range(2):
            self.agent_hand.add_card(self.deck.draw_card())
            self.dealer_hand.add_card(self.deck.draw_card())

        # agent actions
        while True:
            self._set_state(self.agent_hand, self.dealer_hand)
            self.agent.set_state(self.state)
            if self.agent.get_action() == STAND:
                break

            self.agent_hand.add_card(self.deck.draw_card())
            if self._is_bust(self.agent_hand):
                break

        # dealer actions
        while not self._is_bust(self.agent_hand):
            self.dealer.set_hand(self.dealer_hand)
            if self.dealer.get_action() == STAND:
                break

            self.dealer_hand.add_card(self.deck.draw_card())
            if self._is_bust(self.dealer_hand):
                break

        # calculate the winner
        agent_value = self.agent_hand.calculate_hand_value()
        dealer_value = self.dealer_hand.calculate_hand_value()

        if agent_value > 21:
            reward = LOSS
        elif dealer_value > 21:
            reward = WIN
        elif agent_value > dealer_value:
            reward = WIN
        elif agent_value < dealer_value:
            reward = LOSS
        else:
            reward = DRAW

        self.agent.update_q_values(agent.get_episode(), reward)
        return reward

    def play_round_SARSA_Q(self, agent):
        self.initialise_round(agent)

        # deal cards
        for _ in range(2):
            self.agent_hand.add_card(self.deck.draw_card())
            self.dealer_hand.add_card(self.deck.draw_card())

        # agent actions
        while True:
            self._set_state(self.agent_hand, self.dealer_hand)
            self.agent.set_state(self.state)
            if self.agent.get_action() == STAND:
                break

            self.agent_hand.add_card(self.deck.draw_card())
            if self._is_bust(self.agent_hand):
                agent.update_q_values(agent.get_state_action_value(-1), None, LOSS, True)
                return LOSS
            if len(agent.get_episode()) == 2:
                agent.update_q_values(agent.get_state_action_value(-2),
                                      agent.get_state_action_value(-1), 0, False)
                agent.remove_state_action_value(0)

        # dealer actions
        while True:
            self.dealer.set_hand(self.dealer_hand)
            if self.dealer.get_action() == STAND:
                break

            self.dealer_hand.add_card(self.deck.draw_card())
            if self._is_bust(self.dealer_hand):
                return WIN

        # calculate the winner
        agent_value = self.agent_hand.calculate_hand_value()
        dealer_value = self.dealer_hand.calculate_hand_value()

        if agent_value > dealer_value:
            # Player gets blackjack
            if len(agent.get_episode()) == 1:
                agent.update_q_values(agent.get_state_action_value(-1), None, WIN, True)
            return WIN

        if agent_value < dealer_value:
            return LOSS

        return DRAW
