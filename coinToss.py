#Coin toss script

import random

toss = random.randint(0, 1) # 0 is tails, 1 is heads
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

print('You guessed ' + guess)

if 'heads' in guess:
    guess = 1
else:
    guess = 0

if toss == guess:
    print('You got it!')

else:
    print('Nope! Guess again!')
    guesss = input()

    if 'heads' in guess:
        guess = 1
    else:
        guess = 0

    if toss == guess:
       print('You got it!')

    else:
        print('Nope. You are really bad at this game.')
