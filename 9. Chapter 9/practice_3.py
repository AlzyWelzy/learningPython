# num = int(input("Enter a positive integer: "))

# with open('9. Chapter 9/table.txt', "a") as f:
#     for i in range(1, 11):
#         f.write(str(f"{num} * {i} = {num*i}\n"))


for num in range(1, 1001):
    with open(f'9. Chapter 9/TablesOfNums/table-{num}.txt', "w") as f:
        for i in range(1, 1001):
            f.write(str(f"{num} * {i} = {num*i}\n"))
