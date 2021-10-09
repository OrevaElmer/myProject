#This program generate list of password:

import random

userInput = int(input("Enter the lenght of the password: "))

passWord = "abcdefghijklmnopqrstuv"

selectedText = random.sample(passWord, userInput)
passwordText = "".join(selectedText)

'''
#Here is another method:
passwordText =""
for i in range(userInput):
    passwordText += random.choice(passWord) 
'''

print(f"Your password is {passwordText}")
