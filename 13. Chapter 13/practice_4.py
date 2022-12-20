a = [3*i for i in range(1, 1001)]


b = [i for i in a if i % 5 == 0]


c = filter(lambda a: a % 5 == 0, a)

print(a)
print(b)
print(c)
