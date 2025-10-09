import random

balance = int(1000)
acc = int(0)
oldCost = float(100)
actualCost = float(100)
list = ["+", "-"]

percent = float(oldCost / 100)




def buy():
    global balance
    global acc
    global actualCost
    global oldCost
    if oldCost > actualCost and oldCost - actualCost >= (percent*3):
        if balance >= actualCost:
            acc += 1
            balance -= actualCost
            print("Bought 1 stock at", actualCost)
            print("Balance is now", balance)



def sell():
    global balance
    global acc
    global oldCost
    global actualCost


    pass



while True:
    ch = random.choice(list)
    print(ch)
    randomPercent = float(random.uniform(0.03, 0.05))
    if ch == "+":
        actualCost = actualCost + (actualCost * randomPercent)
    elif ch == "-":
        actualCost = actualCost - (actualCost * randomPercent)

    buy()
    sell()


