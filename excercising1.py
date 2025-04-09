# Getting a random number between 1 to 9, the user must guess that number.

import random
intentos = 1
key = random.randint(1, 9)
print(key)
while True:
    number = input('Adivine el número ')
    if number.lower() != 'exit':
        if int(number) != key:
            intentos += 1
            if abs(int(number) - key) > 4:
                print('Intenta de nuevo, estas muy alto')
            elif abs(int(number) - key) >= 1 < 4:
                print('Intenta de nuevo, estas muy cerca')
        else:
            print('Adivinaste en', intentos,'Intentos')
            key = random.randint(1, 9)
            print(key)
    else:
        break

