class InputPlayer():

    def __init__(self):
        self.hand = []
        self.name = 'input'
        self.player_number = None
        self.game = None
    
    def turn(self):
        
        if len(self.hand) == 0:
            self.game.winner = 3 - self.player_number
            return

        card = input(f"\nYour hand: {self.hand} \nWhat card do you want to play? ").title()
        
        if card not in self.hand:
            print("\nThat is an invalid move. Please try again.")
            return

        self.hand.remove(card)

        if card == 'Ace': return int(input("Do you want your Ace to count as 1 or 11? "))
        if card in ['Jack', 'Queen', 'King']: return 10
        return int(card)