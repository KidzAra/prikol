import random

a = int(2)

def diceRollA():
    global sideA
    sideA = random.randint(1, 6)
    return sideA

def diceRollB():
    sideB = 7 - sideA
    return sideB

player1 = int(0)
player2 = int(0)


for i in range(a):
    player1 +=diceRollA()
    player2 +=diceRollB()

print(player1)
print(player2)

#* делалось не по услловиям задачи