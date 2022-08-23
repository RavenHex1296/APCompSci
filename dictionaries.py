points = {"Andrew": 0, "Xida": 0, "Justin": 0, "Angel": 0}


def addPoints(player, number):
    points[player] += number


def howPoints(player):
    return points[player]


def cheater(player):
    points[players] = 0


def endGame():
    for key in points:
        print(key + " has " + str(points[key]) + " points.")


endGame()