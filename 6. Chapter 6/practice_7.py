userString = input(
    "Enter a string to find out if you are talking about Alzy: ")

if (bool(userString.find("Alzy"))):
    print("You are talking about Alzy")
else:
    print("No you aren't talking about Alzy")
