#This is a quiz with three questions:

import time

def checkGuess(guess, answer):
    global score
    stillGuessing = True
    attempt = 0
    while stillGuessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer!')
            score +=1
            stillGuessing = False
        else:
            if attempt<2:
                guess = input('Wrong answer! Please try again\n')
                attempt +=1
            if attempt ==2:
                print(f"The correct answer is {answer}")
                stillGuessing = False

score = 0
print('Starting game...')
time.sleep(1)
guess1 = input('What is the fastest land animal?\n')
checkGuess(guess1, 'cheetah')
guess2 = input('What animal is the king of birds? \n')
checkGuess(guess2,'eagle')
guess3 = input('What is the fastest sea animal?\n')
checkGuess(guess3, 'dolphins')

time.sleep(1)
print('Your final score: ')
time.sleep(1)
print(score)