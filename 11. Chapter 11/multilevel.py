class Employee:
    company = "Visa"


class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level+1
        return self.level


class Programmer(Employee, Freelancer):
    name = "Rohit"


p = Programmer()

print(p.company)

print(p.upgradeLevel())
