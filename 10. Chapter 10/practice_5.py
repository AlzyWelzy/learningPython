class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = set(range(1, seats+1))
        self.seat = False

    def getStatus(self):
        if (self.seat):
            print(f"The name of the train is {self.name}.")
            print(f"The number of seats available is {len(self.seats)}.")
        else:
            print("You haven't booked a train yet.")

    def fareInfo(self):
        print(f"The price of {self.name} train is {self.fare}.")

    def bookTicket(self):
        if (len(self.seats) > 0):
            self.seat = self.seats.pop()
            print(
                f"Your Train Ticket {self.name} is booked and your Ticker Number is {self.seat}.")

        else:
            print(
                f"Sorry, Your Train {self.name} is full. Kindly try in tatkal.")

    def cancelTicket(self):
        if (self.seat):
            self.seats.add(self.seat)
            print("Ticket successfully cancelled")

        else:
            print("you haven't even booked a ticket yet.")

    def getTrainInfo(self):
        print(len(self.seats))


intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
