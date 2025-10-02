import random

def encrypt(text: str, key: int) -> str:
    return ''.join(chr((ord(ch) + key) % 0x110000) for ch in text)

def decrypt(text: str, key: int) -> str:
    return ''.join(chr((ord(ch) - key) % 0x110000) for ch in text)

# пример
msg = str("Hello, World!")
key = int(32)
enc = encrypt(msg, key)
dec = decrypt(enc, key)

print("Зашифрованное: \n", enc)
print("Расшифрованное:\n", dec)
print("Ключ:\n ", key)