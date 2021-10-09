#This program roll a dice:

import random
import time

minVal = 1
maxVal = 6
rollAgain = 'y'

while rollAgain == 'y':
    print('Rolling the Dice...')
    time.sleep(1)
    print('The values are:')
    print(random.randint(minVal,maxVal))
    print(random.randint(minVal,maxVal))
    rollAgain = input("Roll the dice again?: \n")
    if rollAgain == 'n':
        break