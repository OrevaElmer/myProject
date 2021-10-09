#This program return the body max index:

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

height = height / 100
bmi = weight/(height * height)

print(f"You body mass index is : {bmi}")
if bmi > 0:
    if bmi < 16:
        print("You are severely underweight")
    elif bmi < 18.5:
        print("You are underweight")
    elif bmi <=25:
        print("You are healthy")
    elif bmi <= 30:
        print("You are overweight")
    else:
        print("You are overweight")
else:
    print("Enter a valid number")
