def factorial(num):
    if (num < 0):
        return None
    elif (num == 0 or num == 1):
        return 1
    return num*factorial(num-1)


num = int(input("Enter a positive integer: "))

print(factorial(num))
