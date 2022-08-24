points = {"Andrew": 0, "Xida": 0, "Justin": 0, "Angel": 0}


def addPoints(player, number):
    points[player] += number


def howPoints(player):
    return points[player]


def cheater(player):
    points[player] = 0


def endGame():
    max_point_player = list(points.keys())[0]

    for key in points:
        print(key + " has " + str(points[key]) + " points.")

        if points[key] > points[max_point_player]:
            max_point_player = key

    print(max_point_player + " has won!!!")


addPoints("Justin", 727)
addPoints("Xida", 20)
addPoints("Andrew", 45)
addPoints("Angel", 42)
cheater("Justin")
endGame()