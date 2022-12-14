def mySum(arr=0):
    print(sum(arr))
    return 0


num = input("Enter a number: ").split()

mySum(list(map(float, num)))
