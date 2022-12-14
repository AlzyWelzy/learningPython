

def tempConvCF(temp):
    return round((temp * 9/5)+32, 2)


def tempConvFC(temp):
    return round((temp-32)*5/9, 2)


userChoice = int(input(
    "Enter your choice: \n 1 Celsius to Fahrenheit \n 2 Fahrenheit to Celsius \n"))

temp = float(
    input("Enter the temperature you want to convert of your choice: "))

if (userChoice == 1):
    print(
        f"The Temperature you entered {temp} is {tempConvCF(temp)} in Fahrenheit.")
elif (userChoice == 2):
    print(
        f"The Temperature you entered {temp} is {tempConvFC(temp)} in Fahrenheit.")
