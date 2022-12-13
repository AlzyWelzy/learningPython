n = int(input("Enter a positve integer: "))

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
