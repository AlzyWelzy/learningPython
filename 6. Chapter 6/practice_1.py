a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# if (a > b):
#     if (a > c):
#         if (a > d):
#             print(f"The Value of a is the greatest {a}")
#         else:
#             print(f"The Value of d is the greatest {d}")
#     elif (c > d):
#         print(f"The Value of c is the greatest {c}")
#     else:
#         print(f"The Value of d is the greatest {d}")
# elif (b > c):
#     if (b > d):
#         print(f"The Value of b is the greatest {b}")
#     else:
#         print(f"The Value of d is the greatest {d}")
# elif (c > d):
#     print(f"The Value of c is the greatest {c}")
# else:
#     print(f"The Value of d is the greatest {d}")

# l = [24, 234, 314, 12513, 2]

# print(452 in l)

# non = None
# print(non is None)

f1, f2 = None, None

if (a > d):
    f1 = a
else:
    f1 = b

if (b > c):
    f2 = b
else:
    f2 = b

if (f1 > f2):
    print(f"{f1} is the greatest")
else:
    print(f"{f2} is the greatest")
