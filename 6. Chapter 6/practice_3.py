spam = ["make a lot of money", "buy now", "subscribe this", "click this"]

userInput = input("Enter a string to find it's a spam or not: ")

result = None

# if (userInput.find(spam[0]) or userInput.find(spam[1]) or userInput.find(spam[2])):
#     print("SPAM")
# else:
#     print("not a spam")

if (spam[0] in userInput):
    result = True
elif (spam[1] in userInput):
    result = True
elif (spam[2] in userInput):
    result = True
elif (spam[3] in userInput):
    result = True
else:
    result = False

if (result):
    print("The text you entered is filled with spam")
else:
    print("The text is clean of spam")
