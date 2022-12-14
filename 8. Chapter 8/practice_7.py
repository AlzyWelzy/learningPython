# def removal(val):
#     friends.remove(val)


# friends = ["Sanskriti", "Samisti"]

# userChoice = input("Enter a name you want to remove: ")

# removal(userChoice)

# print(userChoice)
# print(friends)

def remove_and_split(str, word):
    newStr = str.replace(word, "")
    print(newStr)
    return newStr.strip()


userChoice = input("Enter a name you want to remove: ")

n = remove_and_split(userChoice, "ehe te nandayo")

print(n)
