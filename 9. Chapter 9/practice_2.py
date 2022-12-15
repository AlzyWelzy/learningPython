def game():
    return 324132


score = game()

with open("9. Chapter 9/hiscore.txt") as f:
    highscorestr = f.read()

if highscorestr == "":
    with open('9. Chapter 9/hiscore.txt', "w") as f:
        f.write(str(score))
elif int(highscorestr) < score:
    with open('9. Chapter 9/hiscore.txt', "w") as f:
        f.write(str(score))
