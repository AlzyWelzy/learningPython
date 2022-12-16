class RailwayForm:
    formtype = "RailwayForm"

    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


AlzysApplication = RailwayForm()

AlzysApplication.name = "AlzyWelzy"
AlzysApplication.train = "Rajdhani Express"
AlzysApplication.printData()
print(AlzysApplication)
