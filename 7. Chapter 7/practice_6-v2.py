num = int(input("Enter a positive integer: "))
factorial = 1
if num < 0:
    print("Sorry, factorial doesn't exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print(f"The factorial of {num} is {factorial}")
