# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


userInt = int(input("Enter a Positive Integer: "))

# mulInt = []

# print([item for index, item in enumerate(list1) if index+1 ==
#       3 or index+1 == 5 or index+1 == 7])


# for index, item in enumerate(list1):
#     mulInt.append(f"{userInt} X {item} = {userInt*item}")


# mulInt.append(f"")


# print(mulInt)


table = [f"{userInt} X {i} = {userInt*i}" for i in range(1, 11)]


print(table)
