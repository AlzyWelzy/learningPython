file = open("9. Chapter 9/example.txt", "r")
# text=file.read()

# text=file.readline()
text = file.readlines()

print(text)

file.close()

file = open("9. Chapter 9/example.txt", "a")

file.write("I am writing stuff")

text = file.readlines()

print(text)

file.close()
