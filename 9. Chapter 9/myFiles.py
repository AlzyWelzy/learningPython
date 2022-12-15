file = open("9. Chapter 9/example.txt", "r")
# text=file.read()

# text=file.readline()
text = file.readlines()

print(text)

file.close()

file = open("9. Chapter 9/example.txt", "a")

file.write("I am appending stuff")

# text = file.readlines() # wont work

print(text)

file.close()

file = open("9. Chapter 9/example.txt", "w")  # file will empty


print(file.write("I am writing stuff"))
file.close()

file = open("9. Chapter 9/example.txt", "r")
# text=file.read()

# text=file.readline()
text = file.readlines()

print(text)

file.close()


# with open("9. Chapter 9/example.txt", "r") as f:
with open("9. Chapter 9/example.txt", "w") as f:
    # a = f.read()
    a = f.write('me')

print(a)
