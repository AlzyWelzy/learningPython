with open("9. Chapter 9/essay.txt") as f:
    fr = f.read()
if "ython" in fr.lower():
    print("It does")
else:
    print("it doesn't")
