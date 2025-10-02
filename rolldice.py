import random

player1 = int(0)
player2 = int(0)

def diceRoll():
    return random.randint(1, 6)

while player1 < 100 and player2 < 100:
    player1 += diceRoll()
    player2 += diceRoll()

    print(f"{player1} {player2}")