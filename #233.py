bridgeCount = int(3)
bridges = [763, 245,113]
busHeight = int(437)
crashIndex = int(0)


for i in range(bridgeCount):
    if bridges[i] < busHeight+1:
        
        crashIndex = int(i + 1)
        break

if crashIndex != 0:
    print("Crash " + str(i+1))
else:
    print("No Crash")