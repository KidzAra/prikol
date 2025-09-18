A1, A2, A3 = 10, 20, 30   
B1, B2, B3 = 5, 3, 7      

if A1 < A2:
    A1, A2 = A2, A1
if A1 < A3:
    A1, A3 = A3, A1
if A2 < A3:
    A2, A3 = A3, A2

if B1 < B2:
    B1, B2 = B2, B1
if B1 < B3:
    B1, B3 = B3, B1
if B2 < B3:
    B2, B3 = B3, B2

profit = A1 * B1 + A2 * B2 + A3 * B3

print(profit)
