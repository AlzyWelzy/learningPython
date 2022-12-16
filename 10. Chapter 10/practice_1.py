class Information:
    company = "Microsoft"

    def __init__(self, name, salary, jobTitle):
        self.name = name
        self.salary = salary
        self.jobTitle = jobTitle

    def getDetails(self):
        print(f"{self.name} works at {self.company} as a {self.jobTitle} and his in-hand salary is {self.salary}.")


alzywelzy = Information(
    "Alzy Welzy", 1000000000000000000000000000000000000000000000000000000000, "Applied Data Scientist")

alzywelzy.getDetails()
