from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("YOU ARE BEING CREATED!")

    def getDetails(self):
        print(f"{self.name} works at {self.subunit} and it's salary is {self.salary}")

    def getSalary(self):
        print(
            f"Salary for this employee working in {self.company} is {self.salary}.")

    @staticmethod
    def greet():
        print("GOOD MORNING DARLING!")

    @staticmethod
    def time():
        print("Current Time =", current_time)


# alzy = Employee()

# alzy.salary = 100000000000
# alzy.getSalary()
# alzy.greet()
# alzy.time()
# Employee.getSalary(alzy)


# print(alzy.company)
# print(alzy.getSalary)
# print(alzy.getSalary()) # doesn't need because alzy.getSalary() already has a print() in it

welzy = Employee("Welzy", 1000000000000, "Brain")

# print(welzy.company)
# print(welzy.name)
# print(welzy.salary)
# print(welzy.subunit)

print(welzy.getDetails())
