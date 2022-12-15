with open("9. Chapter 9/poems.txt") as f:
    a = f.read()


print(a)
print(type(a))

print(a.find("twinkle"))

# if (a.find("twinkle")+1):
#     print("It does")
# else:
#     print("it doesn't")

if "twinkle" in a:
    print("It does")
else:
    print("It doesn't")