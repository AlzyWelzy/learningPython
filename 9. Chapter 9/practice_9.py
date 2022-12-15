with open("9. Chapter 9/essay1.txt") as f:
    ess1 = f.read()

with open("9. Chapter 9/essay2.txt") as f:
    ess2 = f.read()


if ess1 == ess2:
    print("Yes content is same")
else:
    print("No the content is same")
