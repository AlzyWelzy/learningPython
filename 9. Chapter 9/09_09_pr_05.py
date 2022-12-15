words = ["donkey", "kaddu", "mote"]

with open("9. Chapter 9/sample.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("9. Chapter 9/sample.txt", "w") as f:
        f.write(content)
