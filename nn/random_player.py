import random

class RandomPlayer():
    
    def __init__(self):
        self.hand = []
        self.name = 'random'
        self.player_number = None
        self.game = None

    def turn(self):
        
        if len(self.hand) == 0:
            self.game.winner = 3 - self.player_number
            return

        card = random.choice(self.hand)
        print(f"\nOpponent hand: {self.hand}\nYour opponent has played a {card}.")
        self.hand.remove(card)

        if card == 'Ace': return 1
        if card in ['Jack', 'Queen', 'King']: return 10
        return int(card)