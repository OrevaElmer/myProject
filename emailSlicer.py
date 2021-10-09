#This program return seperated username from domain name:

userInput = input("Enter the email address: \n")

userName = userInput[:userInput.index('@')]
domainName = userInput[userInput.index('@')+1:]

print(f"Your username is '{userName}' and \
your domain name is '{domainName}'")