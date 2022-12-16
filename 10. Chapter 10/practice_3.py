class supClass:
    arr = "alzy"

    def __init__(self, name):
        self.name = name


alzy = supClass("welzy")

print(supClass.arr)
print(alzy.arr)

alzy.arr = "supAlzy"

print(supClass.arr)
print(alzy.arr)
