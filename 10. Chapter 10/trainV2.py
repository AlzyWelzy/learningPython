class Train:
    def __init__(self, name, fare, seats):
        self.__name = name
        self.__fare = fare
        self.__seats = set(range(1, seats+1))
        self.__seat = False
        self.__tatkal = set()

    def get_status(self):
        if (self.__seat):
            print(f"The name of the train is {self.__name}.")
            print(f"The number of seats available is {len(self.__seats)}.")
        else:
            print("You haven't booked a train yet.")

    def fare_info(self):
        print(f"The price of {self.__name} train is {self.__fare}.")

    def book_ticket(self):
        if (len(self.__seats) > 0):
            self.__seat = self.__seats.pop()
            print(
                f"Your Train Ticket {self.__name} is booked and your Ticker Number is {self.__seat}.")
        else:
            answer = input(
                "Sorry, Your Train is full. Kindly try in tatkal. Enter y/n: ")
            if (answer == "y"):
                if len(self.__tatkal) > 0:
                    self.__seat = self.__tatkal.pop()
                    print(
                        f"Your Tatkal Ticket {self.__name} is booked and your Ticker Number is {self.__seat}.")
                else:
                    print("Sorry, all tatkal tickets are booked.")
            else:
                print("Sorry for not being useful")

    def cancel_ticket(self):
        if (self.__seat):
            if self.__seat in self.__tatkal:
                self.__tatkal.remove(self.__seat)
            else:
                self.__seats.add(self.__seat)
            self.__seat = False
            print("Ticket successfully cancelled")
        else:
            print("you haven't even booked a ticket yet.")

    def is_available(self, seat_num):
        if seat_num in self.__seats:
            print(f"Seat Number {seat_num} is available to book.")
        else:
            print(f"Seat Number {seat_num} is not available.")

    def all_seats(self):
        print(f"The number of available seats are: {len(self.__seats)}")
