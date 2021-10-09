#This program return the acronym of words:

userInput = input("Enter the word: \n")
words = userInput.split(" ")
acronym = ""
for word in words:
    acronym += str(word[0]).upper()
print(acronym)


