from agents.AgentABC import Agent

class UserAgent(Agent):
    def _get_action(self):
        print("Your hand:")
        print(self.state["agent"])

        print("\nDealer's hand:")
        print(self.state["dealer"])

        choice = input("\nWould you like to 'hit' or 'stand'?\n").lower()

        while choice not in self.choices:
            choice = input("Invalid choice, try again")

        return choice
