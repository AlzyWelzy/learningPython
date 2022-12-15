with open("9. Chapter 9/donkey.txt", "r") as f:
    a = f.read()
    print([i for i in range(len(a)) if a.find("DONKEY")])
