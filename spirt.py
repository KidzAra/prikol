c = int(input("Введите количество углерода: "))
h = int(input("Введите количество водорода: ")) 
o = int(input("Введите количество кислорода: ")) 

result = 0

while c >=2 and h >= 6 and o >= 1:
    result = result + 1
    c = c - 2
    h = h - 6
    o = o - 1

print(result)