def totalNum(num):
    if (num < 0):
        return None
    elif (num == 0 or num == 1):
        return 1
    return num+totalNum(num-1)


num = int(input("Enter the number you want to get the sum of natural numbers: "))

print(totalNum(num))
