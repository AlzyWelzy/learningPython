names = ["AlzyWelzy", "Tarun", "Farhan", "Vishal", "Arfad"]

userInput = input("Enter a name: ")

# if (bool(names.index(userInput)+1)):
#     print("Yes it's there")
# else:
#     print("No it's not there")

if (userInput in names):
    print("Yes it's there")
else:
    print("No it's not there")
