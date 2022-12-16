class IndianRailways:
    def __init__(self, name):
        self.name = name
        # self.ticket = ticket
        # self.source = source
        # self.destination = destination

    def bookTicket(self):
        self.source = input("Enter your source: ")
        self.destination = input("Enter the destination you want to go: ")
        self.ticket = input("Enter the train you want to go: ")
        print(
            f"Your Train {self.ticket} ticket is book for {self.source} to {self.destination}.")

    def getFares(self):
        print(f"Your {self.ticket} is on it's way.")


passengerName = input("Enter your name: ")

passenger = IndianRailways(passengerName)

print(passenger.name)

passenger.bookTicket()

passenger.getFares()
