def sum(x):
    if x == 1:
        return 1
    else:
        return (x+sum(x-1))


num = int(input("Enter a positive integer: "))

result = sum(num)
print(f"The sum of {num} is {result}")
