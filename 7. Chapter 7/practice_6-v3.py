def factorial(x):
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))


num = int(input("Enter a positive integer: "))

if num < 0:
    print("Sorry, factorial doesn't exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
