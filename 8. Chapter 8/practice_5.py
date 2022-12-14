def star(num):
    for i in range(num):
        for j in range(i, num):
            print("*", end=" ")
        print()


num = int(input("Enter a positve integer: "))

star(num)
