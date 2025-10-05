inputString = str("CBABCACCC")

n1 = bool(True)
n2 = bool(False)
n3 = bool(False)

def swapA():
    global n1 
    global n2
    n1 , n2 = n2 , n1

def swapB():
    global n2 
    global n3
    n2 , n3 = n3 , n2

def swapC():
    global n1
    global n3
    n1 , n3 = n3 , n1

for char in inputString:
    if char == "A":
        swapA()
    elif char == "B":
        swapB()
    elif char == "C":
        swapC()

if n1:
    print("1")
elif n2:
    print("2")
elif n3:
    print("3")
