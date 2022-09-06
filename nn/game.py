import random

class ninetyNine():

    def __init__(self, players):
        self.deck = 4 * ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.total = 0
        self.players = players
        self.winner = None

    def set_players(self):
        for player in self.players:
            player.game = self

    def set_player_numbers(self):
        for n in range(0, len(self.players)):
            self.players[n].player_number = n + 1

    def deal(self, n):
        for player in self.players:
            for _ in range(n):
                card = random.choice(self.deck)
                self.deck.remove(card)
                player.hand.append(card)

    def run(self):

        while self.winner == None:
            for player in self.players:
                
                turn = ''

                while type(turn) != int and self.winner == None:
                    turn = player.turn()

                if self.winner != None: break
                self.total += turn
                print(f"New total: {self.total}")

                if self.total > 99:
                    self.winner = 3 - player.player_number
                    break

            if self.total <= 99 and len(self.players[0].hand) == 0 and len(self.players[1].hand) == 0:
                self.winner = "Tie"

        if self.winner != "Tie":
            print(f"Player {self.winner} won")

        else:
            print("Tied game")
