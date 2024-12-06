# Составить функцию, которая напечатает сорок любых символов.
import random

def generate_random_characters(length=40):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Вызов функции и вывод результата
print(generate_random_characters())
