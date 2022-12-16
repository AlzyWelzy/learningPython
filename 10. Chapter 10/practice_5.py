class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}.")
        print(f"The number of seats available is {self.seats}.")

    def fareInfo(self):
        print(f"The price of {self.name} train is {self.fare}.")

    def bookTicket(self):
        if (self.seats > 0):
            print(
                f"Your Train Ticket {self.name} is booked and your Ticker Number is {self.seats}.")
            self.seats = self.seats-1
        else:
            print(
                f"Sorry, Your Train {self.name} is full. Kindly try in tatkal.")

    def cancelTicket(self):
        if (self.seats < 90):
            print("Ok, your ticket is cancel and you will get 90% of your money back.")
        else:
            print("You haven't booked a ticket yet.")


intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
