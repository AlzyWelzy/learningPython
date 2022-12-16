import math


class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return round(math.pow(self.num, 2), 2)

    def cube(self):
        return round(math.pow(self.num, 3), 2)

    def sqrt(self):
        return round(math.sqrt(self.num), 2)


numFor = int(input("Enter a positive integer: "))

calc = Calculator(numFor)

print(calc.square())
print(calc.cube())
print(calc.sqrt())
