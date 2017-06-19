import random
import sys 
guessestaken = 0
guess = 0
print('What up!')

my_number = random.randint(1, 101)
print('I am thinking of a number between 1 and 100.')
my_input = input("A)Guess a number\nB)Quit\n")
if my_input.lower()== "a":
    while guessestaken < 50:
        print('Take a guess.') 
        guess = input()
        guess = int(guess)

        guessestaken = guessestaken + 1

        if guess < my_number:
            print('Your guess is too low.') 

        if guess > my_number:
            print('Your guess is too high.')

        if guess == my_number:
            break
else: 
    my_input.lower()== "b"    
    sys.exit 
if guess == my_number:
    guessestaken = str(guessestaken)
    print('You guessed my number in ' + guessestaken + ' guesses!')

if guess != my_number and guess != 0:
    my_number = str(my_number)
    print('Nope. The number I was thinking of was ' + my_number)