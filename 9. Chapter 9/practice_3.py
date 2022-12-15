num = int(input("Enter a positive integer: "))

with open('9. Chapter 9/table.txt', "a") as f:
    for i in range(1, 11):
        f.write(str(f"{num} * {i} = {num*i}\n"))
