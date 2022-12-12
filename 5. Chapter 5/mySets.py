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
