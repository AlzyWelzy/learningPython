import random
randomInt = random.randint(1, 100)
guesses = 0
userInt = None


def game():
    global userInt, guesses
    while (randomInt != userInt):
        userInt = int(input("Enter a random integer between 1 to 100: "))
        if (randomInt == userInt):
            print(
                f"CORRECT! The Random Number was {randomInt} and you guessed it in {guesses}.")
        else:
            if (userInt < randomInt):
                guesses += 1
                print("Too Low!")
            else:
                guesses += 1
                print("Too High!")


game()


with open("Project 2/hiscore.txt", "r") as f:
    hiScore = int(f.read())
    print(f"Your current high score is {hiScore}.")

if (guesses > hiScore):
    print(
        f"You broke your high score that was {hiScore}. Your new high score is {guesses}.")
    with open("Project 2/hiscore.txt", "w") as f:
        f.write(str(guesses))
