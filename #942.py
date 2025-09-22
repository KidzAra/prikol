minutes = [40, 30, 60]
sum = int(0)
resultMin = int(0)
summ2 = int(0)
resultMin2 = int(0)
summ3 = int(0)
resultMin3 = int(0)

for task in minutes:
    sum += task
    resultMin += sum
    print(resultMin)

for task in minutes[::-1]:
    summ2 += task
    resultMin2 += summ2
    print(resultMin2)

for task in sorted(minutes):
    summ3 += task
    resultMin3 += summ3
    print(resultMin3)


#TODO