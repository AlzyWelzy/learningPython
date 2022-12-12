a = {1, 2, 3, 4, 1, 3, 4, 5, 232, 2, 2, 2, 2}  # Set ignores repetitive words
print(type(a))
print(a)

# Important: This syntax will create an empty dictionary instead of an Empty Set
b = {}
print(type(b))

# An empty set can be created using below syntax:
b = set()
print(type(b))

# adding stuff to the set through methods
b.add(4)
b.add(4)
b.add(4)
b.add(4)
b.add(4)
b.add(4)
b.add(4)
b.add(4)
b.add(5)
# b.add([4,5,6]) # will return error
b.add((4, 5, 6))  # will work

# b.add({"Alzy": "Welzy"})  # will throw an error

print(b)

print(len(b))

b.remove(4)

print(len(b))

print(b)


b.pop()

b.clear()
print(b.add(4))
print(b.add(5))
print(b.add(6))
print(b.union({8, 11, 123, 1235, 435, 1, 12}))
print(b)

print(b.intersection({5, 999999999999}))
