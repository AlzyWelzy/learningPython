n = int(input("Enter a positive integer: "))

for i in range(n):
    for i in range(i+1):
        print(" ", end="")
    for j in range(i, n):
        print("*", end="")
    print()
