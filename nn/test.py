from game import *
from input_player import *
from random_player import *
from custom_player import *

players = [InputPlayer(), CustomPlayer()]
game = ninetyNine(players)
game.set_player_numbers()
game.set_players()
game.deal(10)
game.run()
