import random

class CustomPlayer():

    def __init__(self):
        self.hand = []
        self.name = 'input'
        self.player_number = None
        self.game = None
    
    def turn(self):
        if len(self.hand) == 0:
            self.game.winner = 3 - self.player_number
            return

        max_card = ''
        max_value = 0

        for card in self.hand:
            if card in ["King", "Queen", "Jack", "10"] and self.game.total + 10 <= 99:
                max_card = card
                max_value = 10

            if card in "23456789" and int(card) > max_value and self.game.total + int(card) <= 99:
                max_card = card
                max_value = int(card)

        print(f"\nOpponent hand: {self.hand}\nYour opponent has played a {max_card}.")

        if max_card == '':
            hand = self.hand

            for card in hand:
                if card in ["King", "Queen", "Jack"]:
                    card = "10"

            return int(random.choice(hand))

        self.hand.remove(max_card)

        return int(max_value)