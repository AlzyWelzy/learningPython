class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an Employee")


class Programmer(Employee):
    language = "Python"

    def getLanguage(self):
        print(f"The Language this programmer uses is {self.language}.")

    def showDetails(self):
        # return super().showDetails()
        print("This is a programmer.")


e = Employee()
e.showDetails()

p = Programmer()
p.showDetails()
print(p.company)
