class Employee:
    company = "Google"

    def __init__(self, name, salary, increment):
        self.name = name
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfter(self):
        return self.salary*self.increment

    @salaryAfter.setter
    def salaryAfter(self, val):
        self.increment = val/self.salary


e = Employee("Alzy Welzy", 1000, 1.5)
print(e.salaryAfter)

print(e.increment)
e.salaryAfter = 2000
print(e.increment)
