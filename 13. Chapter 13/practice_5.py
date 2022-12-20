import functools

list1 = [3*i for i in range(1, 10000001)]

sumofList1 = functools.reduce(lambda a, b: a+b, list1)

print(sumofList1)
