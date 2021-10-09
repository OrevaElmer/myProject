
import random

def renderGame():
    global compChoice 
    global playerInput
    
    choices = ['rock', 'paper','scissors']
    compChoice = random.choice(choices)
    
    playerInput = input("Enter 'rock, paper or scissors.\n You can also enter end to end the game: \n")
    playerInput = playerInput.lower()
    
    return compChoice, playerInput


player = False
compScore = 0
playerScore = 0

while True:
    renderGame()
    if playerInput == compChoice:
        print(f"A tie. {compChoice} equals {playerInput}")
    elif playerInput == 'rock':
        if compChoice == 'paper':
            print(f"You loss {compChoice} cover {playerInput}\n")
            compScore +=1
        else:
            print(f"You won. {playerInput} smashes {compChoice}\n")
            playerScore +=1
    elif playerInput == 'paper':
        if compChoice == 'scissors':
            print(f"You loss {compChoice} cut {playerInput}\n")
            compScore +=1
        else:
            print(f"You won. {playerInput} covers {compChoice}\n")
            playerScore +=1
    elif playerInput == 'scissors':
        if  compScore == 'rock':
            print(f"You lose. {compChoice} smashes {playerInput}\n")
            compScore +=1
        else:
            print(f"You won. {playerInput} cut {compChoice}\n")
            playerScore +=1
    elif playerInput == 'end':
        print('Final Scores:')
        print(f"Computer Score: {compScore}")
        print(f"player Score: {playerScore}")
        break
