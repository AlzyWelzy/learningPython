hindiToEnglish = {
    "naam": "name", "tum": "you", "mein": "I", "kaun": "who", "kya": "what"
}

print(f"Options are {hindiToEnglish.keys()}")

userInput = input("Enter the word you want to lookup in the dictionary: ")

print(
    f"The translation for the English Word {userInput} is {hindiToEnglish.get(userInput)} in Hindi.")
