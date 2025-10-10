import random

def generate_password():
    characters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0"
    password_length = int(5)
    password = ''.join(random.choice(characters) for i in range(password_length))
    return password

password = generate_password()
print(password)

def passwordCrack(password):
    global guess
    i = int(0)
    guess = ""
    while password != guess:
        guess = generate_password()
        print(guess)
        i += 1
        print(i)
    return(guess)

print(passwordCrack(password))