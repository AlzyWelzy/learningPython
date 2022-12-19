userInt = int(input("Enter a Positive Integer: "))

table = [userInt*i for i in range(1, 11)]

print(table)

with open("12. Chapter 12/tables.txt", "a") as f:
    f.write(str(table))
    f.write("\n")
