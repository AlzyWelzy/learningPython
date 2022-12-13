n = int(input("Enter a positve integer: "))

for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print()
