from agents.AgentABC import Agent, HIT, STAND

class UserAgent(Agent):
    def _get_action(self):
        print("Your hand:")
        print(self.state[0])

        print("\nDealer's hand:")
        print(self.state[1])

        choice = input("\nWould you like to 'hit' or 'stand'?\n").lower()

        while True:
            if choice == "hit":
                return HIT
            if choice == "stand":
                return STAND

            print("Invalid input, try again:")
            choice = input("\nWould you like to 'hit' or 'stand'?\n").lower()
