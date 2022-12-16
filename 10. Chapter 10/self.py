class Employee:
    company = "Google"

    def getSalary(self):
        print(
            f"Salary for this employee working in {self.company} is {self.salary}.")


alzy = Employee()

alzy.salary = 100000000000
alzy.getSalary()
# Employee.getSalary(alzy)


print(alzy.company)
# print(alzy.getSalary)
# print(alzy.getSalary()) # doesn't need because alzy.getSalary() already has a print() in it
