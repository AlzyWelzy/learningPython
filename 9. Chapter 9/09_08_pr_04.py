with open("9. Chapter 9/sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("9. Chapter 9/sample.txt", "w") as f:
    f.write(content)
