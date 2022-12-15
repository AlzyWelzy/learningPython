# f1 = open("9. Chapter 9/donkey.txt", "r")
# f2 = open("9. Chapter 9/donkey.txt", "w")

# for word in f1:
#     f2.write(word.replace("DONKEY", "######"))

# f1.close()
# f2.close()

with open("9. Chapter 9/donkey.txt") as r:
    text = r.read().replace("DONKEY", "######")
with open("9. Chapter 9/donkey.txt", "w") as w:
    w.write(text)
