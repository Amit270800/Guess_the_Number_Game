# Guess the number

import random

n = random.randrange(100)
count = 9
while(1):
    m = int(input("Guess the number from 1 - 100\n"))
    count -= 1
    if n > m:
        print("Increase the number")
    elif m > n:
        print("Reduce the number")
    else:
        print("You guessed the number right")
        print('You took', 9-count, 'guesses to guess the number')
        print('Game over')
        break
    print('You are left with', count, 'guesses')
    print()
