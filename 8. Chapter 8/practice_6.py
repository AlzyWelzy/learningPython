def inchesToCM(num):
    return round(num*2.54, 2)


def cmToInches(num):
    return round(num/2.54, 2)


userChoice = int(input(
    "Enter your choice: \n 1 Inches to Centimeters \n 2 Centimeters to Inches \n"))

num = float(
    input("Enter the Value you want to convert of your choice: "))

if (userChoice == 1):
    print(
        f"The Value you entered {num} is {inchesToCM(num)} in Centimeters.")
elif (userChoice == 2):
    print(
        f"The Value you entered {num} is {cmToInches(num)} in Inches.")
