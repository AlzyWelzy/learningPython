class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = set(range(1, seats+1))
        self.seat = False
        self.tatkal = set()

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
            answer = input("Enter if you want to y/n: ")
            if (answer == "y"):
                self.tatkal.add(1)

            else:
                print("Sorry for not being useful")

    def cancelTicket(self):
        if (self.seat):
            self.seats.add(self.seat)
            print("Ticket successfully cancelled")

        else:
            print("you haven't even booked a ticket yet.")

    def isAvailabe(self, seatNum):
        if seatNum in self.seats:
            print(f"Seat Number {seatNum} is available to book.")
        else:
            print(f"Seat Number {seatNum} is not available.")

    def allSeats(self):
        print("The number of available are : ", end="")
        for x in range(len(self.seats)):
            print(f"{x+1}", end="")


intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
intercity.isAvailabe(100)
intercity.allSeats()
