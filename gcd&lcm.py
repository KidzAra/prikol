number1 = a = int(input("Первое число? "))
number2 =b = int(input("Второе число? "))

while b != 0:
        a, b = b, a % b  

print("НОД:", a)
print("НОК:", int(number1 * number2 / a))